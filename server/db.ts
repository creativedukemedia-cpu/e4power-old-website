import { and, desc, eq } from "drizzle-orm";
import { drizzle } from "drizzle-orm/mysql2";
import { CmsContentItem, CmsUser, InsertCmsContentItem, InsertCmsUser, InsertUser, cmsContentItems, cmsUsers, users } from "../drizzle/schema";
import { ENV } from './_core/env';

let _db: ReturnType<typeof drizzle> | null = null;

export async function getDb() {
  if (!_db && process.env.DATABASE_URL) {
    try {
      _db = drizzle(process.env.DATABASE_URL);
    } catch (error) {
      console.warn("[Database] Failed to connect:", error);
      _db = null;
    }
  }
  return _db;
}

export async function upsertUser(user: InsertUser): Promise<void> {
  if (!user.openId) {
    throw new Error("User openId is required for upsert");
  }

  const db = await getDb();
  if (!db) {
    console.warn("[Database] Cannot upsert user: database not available");
    return;
  }

  const values: InsertUser = { openId: user.openId };
  const updateSet: Record<string, unknown> = {};
  const textFields = ["name", "email", "loginMethod"] as const;

  for (const field of textFields) {
    const value = user[field];
    if (value === undefined) continue;
    const normalized = value ?? null;
    values[field] = normalized;
    updateSet[field] = normalized;
  }

  if (user.lastSignedIn !== undefined) {
    values.lastSignedIn = user.lastSignedIn;
    updateSet.lastSignedIn = user.lastSignedIn;
  }
  if (user.role !== undefined) {
    values.role = user.role;
    updateSet.role = user.role;
  } else if (user.openId === ENV.ownerOpenId) {
    values.role = 'admin';
    updateSet.role = 'admin';
  }

  if (!values.lastSignedIn) values.lastSignedIn = new Date();
  if (Object.keys(updateSet).length === 0) updateSet.lastSignedIn = new Date();

  await db.insert(users).values(values).onDuplicateKeyUpdate({ set: updateSet });
}

export async function getUserByOpenId(openId: string) {
  const db = await getDb();
  if (!db) return undefined;
  const result = await db.select().from(users).where(eq(users.openId, openId)).limit(1);
  return result[0];
}

export async function countCmsUsers() {
  const db = await getDb();
  if (!db) return 0;
  const rows = await db.select({ id: cmsUsers.id }).from(cmsUsers);
  return rows.length;
}

export async function createCmsUser(user: InsertCmsUser) {
  const db = await getDb();
  if (!db) throw new Error('Database unavailable');
  await db.insert(cmsUsers).values(user);
  return getCmsUserByEmail(user.email);
}

export async function getCmsUserByEmail(email: string) {
  const db = await getDb();
  if (!db) return undefined;
  const rows = await db.select().from(cmsUsers).where(eq(cmsUsers.email, email)).limit(1);
  return rows[0] as CmsUser | undefined;
}

export async function getCmsUserById(id: number) {
  const db = await getDb();
  if (!db) return undefined;
  const rows = await db.select().from(cmsUsers).where(eq(cmsUsers.id, id)).limit(1);
  return rows[0] as CmsUser | undefined;
}

export async function listCmsUsers() {
  const db = await getDb();
  if (!db) return [];
  return db.select().from(cmsUsers).orderBy(desc(cmsUsers.updatedAt));
}

export async function updateCmsUser(id: number, user: Partial<InsertCmsUser>) {
  const db = await getDb();
  if (!db) throw new Error('Database unavailable');
  await db.update(cmsUsers).set(user).where(eq(cmsUsers.id, id));
  return getCmsUserById(id);
}

export async function touchCmsUserSignIn(id: number) {
  const db = await getDb();
  if (!db) return;
  await db.update(cmsUsers).set({ lastSignedIn: new Date() }).where(eq(cmsUsers.id, id));
}

export async function listCmsContentItems() {
  const db = await getDb();
  if (!db) return [];
  return db.select().from(cmsContentItems).orderBy(desc(cmsContentItems.updatedAt));
}

export async function listPublishedCmsContentItems(contentType?: CmsContentItem['contentType']) {
  const db = await getDb();
  if (!db) return [];

  const baseQuery = db
    .select()
    .from(cmsContentItems)
    .where(
      contentType
        ? and(eq(cmsContentItems.status, 'published'), eq(cmsContentItems.contentType, contentType))
        : eq(cmsContentItems.status, 'published')
    )
    .orderBy(desc(cmsContentItems.publishedAt), desc(cmsContentItems.updatedAt));

  return baseQuery;
}

export async function getPublishedCmsContentItemBySlug(slug: string) {
  const db = await getDb();
  if (!db) return undefined;
  const rows = await db
    .select()
    .from(cmsContentItems)
    .where(and(eq(cmsContentItems.slug, slug), eq(cmsContentItems.status, 'published')))
    .limit(1);
  return rows[0] as CmsContentItem | undefined;
}

export async function createCmsContentItem(item: InsertCmsContentItem) {
  const db = await getDb();
  if (!db) throw new Error('Database unavailable');
  await db.insert(cmsContentItems).values(item);
  const rows = await db.select().from(cmsContentItems).where(eq(cmsContentItems.slug, item.slug)).limit(1);
  return rows[0] as CmsContentItem | undefined;
}

export async function getCmsContentItemById(id: number) {
  const db = await getDb();
  if (!db) return undefined;
  const rows = await db.select().from(cmsContentItems).where(eq(cmsContentItems.id, id)).limit(1);
  return rows[0] as CmsContentItem | undefined;
}

export async function updateCmsContentItem(id: number, item: Partial<InsertCmsContentItem>) {
  const db = await getDb();
  if (!db) throw new Error('Database unavailable');
  await db.update(cmsContentItems).set(item).where(eq(cmsContentItems.id, id));
  return getCmsContentItemById(id);
}

export async function deleteCmsContentItem(id: number) {
  const db = await getDb();
  if (!db) throw new Error('Database unavailable');
  await db.delete(cmsContentItems).where(eq(cmsContentItems.id, id));
}
