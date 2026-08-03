import fs from 'fs';
import path from 'path';
import { describe, expect, it } from 'vitest';

const routesPath = path.resolve(import.meta.dirname, 'cmsRoutes.ts');
const adminAppPath = path.resolve(import.meta.dirname, '..', 'client', 'src', 'admin', 'AdminApp.tsx');
const routesSource = fs.readFileSync(routesPath, 'utf8');
const adminAppSource = fs.readFileSync(adminAppPath, 'utf8');

describe('cms content workflow source coverage', () => {
  it('registers update and delete CMS content routes', () => {
    expect(routesSource).toContain("app.put('/api/cms/content/:id'");
    expect(routesSource).toContain("app.delete('/api/cms/content/:id'");
    expect(routesSource).toContain('updateCmsContentItem(');
    expect(routesSource).toContain('deleteCmsContentItem(itemId)');
  });

  it('supports content editing in the admin interface', () => {
    expect(adminAppSource).toContain('const [editingId, setEditingId] = useState<number | null>(null);');
    expect(adminAppSource).toContain("editingId ? `/api/cms/content/${editingId}` : '/api/cms/content'");
    expect(adminAppSource).toContain("{busy ? 'Saving…' : editingId ? 'Update content item' : 'Create content item'}");
    expect(adminAppSource).toContain('onClick={() => populateForm(item)}');
  });

  it('supports content deletion in the admin interface', () => {
    expect(adminAppSource).toContain('async function removeItem(itemId: number)');
    expect(adminAppSource).toContain("method: 'DELETE'");
    expect(adminAppSource).toContain("{deleteBusyId === item.id ? 'Deleting…' : 'Delete'}");
  });
});
