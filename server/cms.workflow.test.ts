import fs from 'fs';
import path from 'path';
import { describe, expect, it } from 'vitest';

const routesPath = path.resolve(import.meta.dirname, 'cmsRoutes.ts');
const adminAppPath = path.resolve(import.meta.dirname, '..', 'client', 'src', 'admin', 'AdminApp.tsx');
const publicContentEntryPath = path.resolve(import.meta.dirname, '..', 'client', 'src', 'content', 'main.tsx');
const publicContentHtmlPath = path.resolve(import.meta.dirname, '..', 'client', 'content', 'index.html');
const vitePath = path.resolve(import.meta.dirname, '_core', 'vite.ts');

const routesSource = fs.readFileSync(routesPath, 'utf8');
const adminAppSource = fs.readFileSync(adminAppPath, 'utf8');
const publicContentEntrySource = fs.readFileSync(publicContentEntryPath, 'utf8');
const publicContentHtmlSource = fs.readFileSync(publicContentHtmlPath, 'utf8');
const viteSource = fs.readFileSync(vitePath, 'utf8');

describe('cms content workflow source coverage', () => {
  it('registers update and delete CMS content routes', () => {
    expect(routesSource).toContain("app.put('/api/cms/content/:id'");
    expect(routesSource).toContain("app.delete('/api/cms/content/:id'");
    expect(routesSource).toContain('updateCmsContentItem(');
    expect(routesSource).toContain('deleteCmsContentItem(itemId)');
  });

  it('registers cover-image upload and removal routes', () => {
    expect(routesSource).toContain("app.post('/api/cms/content/:id/cover-image'");
    expect(routesSource).toContain("app.delete('/api/cms/content/:id/cover-image'");
    expect(routesSource).toContain("upload.single('coverImage')");
    expect(routesSource).toContain('storagePut(`cms/content-${itemId}/');
    expect(routesSource).toContain('coverImageUrl: stored.url');
  });

  it('registers public published-content read routes', () => {
    expect(routesSource).toContain("app.get('/api/cms/public/content'");
    expect(routesSource).toContain("app.get('/api/cms/public/content/:slug'");
    expect(routesSource).toContain('listPublishedCmsContentItems(');
    expect(routesSource).toContain('getPublishedCmsContentItemBySlug(');
    expect(routesSource).toContain("Published content item not found");
  });

  it('supports content editing in the admin interface', () => {
    expect(adminAppSource).toContain('const [editingId, setEditingId] = useState<number | null>(null);');
    expect(adminAppSource).toContain("editingId ? `/api/cms/content/${editingId}` : '/api/cms/content'");
    expect(adminAppSource).toContain("{busy ? 'Saving…' : editingId ? 'Update content item' : 'Create content item'}");
    expect(adminAppSource).toContain('onClick={() => populateForm(item)}');
  });

  it('shows a public-view shortcut only for published items in the admin interface', () => {
    expect(adminAppSource).toContain("item.status === 'published'");
    expect(adminAppSource).toContain('href={`/content/index.html?slug=${encodeURIComponent(item.slug)}`}');
    expect(adminAppSource).toContain('View live');
  });

  it('supports admin-side content search and filters', () => {
    expect(adminAppSource).toContain("const [searchQuery, setSearchQuery] = useState('')");
    expect(adminAppSource).toContain("const [statusFilter, setStatusFilter] = useState<'all' | 'draft' | 'published'>('all')");
    expect(adminAppSource).toContain("const [typeFilter, setTypeFilter] = useState<'all' | string>('all')");
    expect(adminAppSource).toContain('const filteredItems = useMemo(() => {');
    expect(adminAppSource).toContain('Find by title or slug');
    expect(adminAppSource).toContain('All statuses');
    expect(adminAppSource).toContain('All types');
    expect(adminAppSource).toContain('No items match the current filters.');
  });

  it('supports content deletion in the admin interface', () => {
    expect(adminAppSource).toContain('async function removeItem(itemId: number)');
    expect(adminAppSource).toContain("method: 'DELETE'");
    expect(adminAppSource).toContain("{deleteBusyId === item.id ? 'Deleting…' : 'Delete'}");
  });

  it('supports cover-image upload and removal in the admin interface', () => {
    expect(adminAppSource).toContain('const [coverImageFile, setCoverImageFile] = useState<File | null>(null);');
    expect(adminAppSource).toContain('async function syncCoverImage(itemId: number)');
    expect(adminAppSource).toContain('/api/cms/content/${itemId}/cover-image');
    expect(adminAppSource).toContain('Upload a replacement image so staff can manage visuals without touching code.');
    expect(adminAppSource).toContain('Remove image');
  });

  it('creates a dedicated public content entry point', () => {
    expect(publicContentHtmlSource).toContain('<div id="root"></div>');
    expect(publicContentHtmlSource).toContain('/src/content/main.tsx');
    expect(viteSource).toContain('/src/content/main.tsx');
  });

  it('renders published content cards and detail views in the public content app', () => {
    expect(publicContentEntrySource).toContain('/api/cms/public/content');
    expect(publicContentEntrySource).toContain('/content/index.html?slug=');
    expect(publicContentEntrySource).toContain('This page only surfaces items marked as published in the staff admin workspace.');
    expect(publicContentEntrySource).toContain('This published content item could not be found.');
  });

  it('supports public Insights search and clearer listing feedback', () => {
    expect(publicContentEntrySource).toContain("const search = query.get('q')?.trim().toLowerCase() || '';");
    expect(publicContentEntrySource).toContain('Search by title, slug, or excerpt');
    expect(publicContentEntrySource).toContain("filteredItems.length === 1 ? '' : 's'");
    expect(publicContentEntrySource).toContain('Clear search');
    expect(publicContentEntrySource).toContain('No published entries match the current search and filter settings yet.');
  });

  it('registers admin-only CMS staff user management routes', () => {
    expect(routesSource).toContain("app.get('/api/cms/users'");
    expect(routesSource).toContain("app.post('/api/cms/users'");
    expect(routesSource).toContain("app.put('/api/cms/users/:id'");
    expect(routesSource).toContain('Admin access required');
    expect(routesSource).toContain('A CMS staff user with that email already exists');
  });

  it('supports admin-side staff account management in the CMS interface', () => {
    expect(adminAppSource).toContain('const [staffUsers, setStaffUsers] = useState<CmsUser[]>([]);');
    expect(adminAppSource).toContain('const [staffForm, setStaffForm] = useState<StaffFormState>(emptyStaffForm);');
    expect(adminAppSource).toContain('async function submitStaffUser(event: FormEvent<HTMLFormElement>)');
    expect(adminAppSource).toContain('async function updateStaffUserRole(userId: number, role: \'admin\' | \'editor\')');
    expect(adminAppSource).toContain('async function toggleStaffActive(userId: number, isActive: boolean, role: \'admin\' | \'editor\')');
    expect(adminAppSource).toContain('Manage CMS users');
    expect(adminAppSource).toContain('Create staff user');
    expect(adminAppSource).toContain('Reactivate access');
  });
});
