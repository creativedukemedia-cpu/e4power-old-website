import bcrypt from 'bcryptjs';
import { parse as parseCookieHeader } from 'cookie';
import type { Express, Request, Response } from 'express';
import { createCmsContentItem, createCmsUser, countCmsUsers, getCmsUserByEmail, getCmsUserById, listCmsContentItems, touchCmsUserSignIn } from './db';
import { getSessionCookieOptions } from './_core/cookies';
import { CMS_SESSION_COOKIE, getCmsSessionMaxAge, issueCmsSession, verifyCmsSession } from './cmsAuth';

async function getCmsUserFromRequest(req: Request) {
  const cookies = parseCookieHeader(req.headers.cookie || '');
  const token = cookies[CMS_SESSION_COOKIE];
  if (!token) return null;
  try {
    const payload = await verifyCmsSession(token);
    const userId = Number(payload.sub);
    if (!Number.isFinite(userId)) return null;
    const user = await getCmsUserById(userId);
    if (!user || !user.isActive) return null;
    return user;
  } catch {
    return null;
  }
}

function sanitizeUser(user: NonNullable<Awaited<ReturnType<typeof getCmsUserFromRequest>>> | Awaited<ReturnType<typeof getCmsUserByEmail>>) {
  if (!user) return null;
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    role: user.role,
    lastSignedIn: user.lastSignedIn,
  };
}

export function registerCmsRoutes(app: Express) {
  app.get('/api/cms/bootstrap-status', async (_req: Request, res: Response) => {
    const count = await countCmsUsers();
    res.json({ requiresBootstrap: count === 0 });
  });

  app.post('/api/cms/bootstrap', async (req: Request, res: Response) => {
    const count = await countCmsUsers();
    if (count > 0) {
      res.status(409).json({ error: 'CMS admin account already exists' });
      return;
    }

    const { email, password, name } = req.body ?? {};
    if (!email || !password || !name) {
      res.status(400).json({ error: 'name, email, and password are required' });
      return;
    }
    if (String(password).length < 10) {
      res.status(400).json({ error: 'Password must be at least 10 characters long' });
      return;
    }

    const passwordHash = await bcrypt.hash(String(password), 12);
    const user = await createCmsUser({
      email: String(email).trim().toLowerCase(),
      name: String(name).trim(),
      passwordHash,
      role: 'admin',
      isActive: 1,
    });

    if (!user) {
      res.status(500).json({ error: 'Failed to create CMS admin user' });
      return;
    }

    const token = await issueCmsSession({
      sub: String(user.id),
      email: user.email,
      role: user.role,
      name: user.name,
    });
    const cookieOptions = getSessionCookieOptions(req);
    res.cookie(CMS_SESSION_COOKIE, token, { ...cookieOptions, maxAge: getCmsSessionMaxAge() });
    res.json({ user: sanitizeUser(user) });
  });

  app.post('/api/cms/login', async (req: Request, res: Response) => {
    const { email, password } = req.body ?? {};
    if (!email || !password) {
      res.status(400).json({ error: 'email and password are required' });
      return;
    }

    const user = await getCmsUserByEmail(String(email).trim().toLowerCase());
    if (!user || !user.isActive) {
      res.status(401).json({ error: 'Invalid credentials' });
      return;
    }

    const valid = await bcrypt.compare(String(password), user.passwordHash);
    if (!valid) {
      res.status(401).json({ error: 'Invalid credentials' });
      return;
    }

    await touchCmsUserSignIn(user.id);
    const token = await issueCmsSession({
      sub: String(user.id),
      email: user.email,
      role: user.role,
      name: user.name,
    });
    const cookieOptions = getSessionCookieOptions(req);
    res.cookie(CMS_SESSION_COOKIE, token, { ...cookieOptions, maxAge: getCmsSessionMaxAge() });
    res.json({ user: sanitizeUser(user) });
  });

  app.post('/api/cms/logout', async (req: Request, res: Response) => {
    const cookieOptions = getSessionCookieOptions(req);
    res.clearCookie(CMS_SESSION_COOKIE, { ...cookieOptions, maxAge: -1 });
    res.json({ success: true });
  });

  app.get('/api/cms/me', async (req: Request, res: Response) => {
    const user = await getCmsUserFromRequest(req);
    if (!user) {
      res.status(401).json({ error: 'Not authenticated' });
      return;
    }
    res.json({ user: sanitizeUser(user) });
  });

  app.get('/api/cms/content', async (req: Request, res: Response) => {
    const user = await getCmsUserFromRequest(req);
    if (!user) {
      res.status(401).json({ error: 'Not authenticated' });
      return;
    }
    const items = await listCmsContentItems();
    res.json({ items });
  });

  app.post('/api/cms/content', async (req: Request, res: Response) => {
    const user = await getCmsUserFromRequest(req);
    if (!user) {
      res.status(401).json({ error: 'Not authenticated' });
      return;
    }

    const { title, slug, contentType, excerpt, body, status } = req.body ?? {};
    if (!title || !slug || !contentType) {
      res.status(400).json({ error: 'title, slug, and contentType are required' });
      return;
    }

    const item = await createCmsContentItem({
      title: String(title).trim(),
      slug: String(slug).trim().toLowerCase(),
      contentType,
      excerpt: excerpt ? String(excerpt) : null,
      body: body ? String(body) : null,
      status: status === 'published' ? 'published' : 'draft',
      createdByUserId: user.id,
      updatedByUserId: user.id,
      publishedAt: status === 'published' ? new Date() : null,
    });

    res.json({ item });
  });
}
