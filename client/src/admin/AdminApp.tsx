import { FormEvent, useEffect, useMemo, useState } from 'react';

type CmsUser = {
  id: number;
  email: string;
  name: string;
  role: 'admin' | 'editor';
  lastSignedIn?: string | null;
};

type CmsItem = {
  id: number;
  title: string;
  slug: string;
  contentType: string;
  status: 'draft' | 'published';
  excerpt?: string | null;
  body?: string | null;
  updatedAt?: string;
  publishedAt?: string | null;
};

type CmsFormState = {
  title: string;
  slug: string;
  contentType: string;
  excerpt: string;
  body: string;
  status: 'draft' | 'published';
};

const cardClass = 'rounded-3xl border border-white/10 bg-black/30 p-6 shadow-2xl backdrop-blur';
const emptyForm: CmsFormState = {
  title: '',
  slug: '',
  contentType: 'white-paper',
  excerpt: '',
  body: '',
  status: 'draft',
};

function formatContentType(value: string) {
  return value
    .split('-')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

export default function AdminApp() {
  const [requiresBootstrap, setRequiresBootstrap] = useState<boolean | null>(null);
  const [user, setUser] = useState<CmsUser | null>(null);
  const [items, setItems] = useState<CmsItem[]>([]);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);
  const [deleteBusyId, setDeleteBusyId] = useState<number | null>(null);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [formState, setFormState] = useState<CmsFormState>(emptyForm);

  const contentTypes = useMemo(
    () => [
      { value: 'white-paper', label: 'White Paper' },
      { value: 'newsletter', label: 'Newsletter' },
      { value: 'funding-opportunity', label: 'Funding Opportunity' },
      { value: 'thought-leadership', label: 'Thought Leadership' },
    ],
    []
  );

  async function loadStatus() {
    const [statusRes, meRes] = await Promise.all([
      fetch('/api/cms/bootstrap-status', { credentials: 'include' }),
      fetch('/api/cms/me', { credentials: 'include' }),
    ]);
    const statusJson = await statusRes.json();
    setRequiresBootstrap(Boolean(statusJson.requiresBootstrap));
    if (meRes.ok) {
      const meJson = await meRes.json();
      setUser(meJson.user);
    } else {
      setUser(null);
    }
  }

  async function loadItems() {
    const res = await fetch('/api/cms/content', { credentials: 'include' });
    if (!res.ok) return;
    const data = await res.json();
    setItems(data.items || []);
  }

  useEffect(() => {
    loadStatus().catch((err) => setError(err instanceof Error ? err.message : 'Failed to load CMS status'));
  }, []);

  useEffect(() => {
    if (user) {
      loadItems().catch(() => undefined);
    }
  }, [user]);

  function resetForm() {
    setEditingId(null);
    setFormState(emptyForm);
  }

  function populateForm(item: CmsItem) {
    setEditingId(item.id);
    setFormState({
      title: item.title,
      slug: item.slug,
      contentType: item.contentType,
      excerpt: item.excerpt || '',
      body: item.body || '',
      status: item.status,
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function submitBootstrap(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError('');
    const form = new FormData(event.currentTarget);
    const payload = {
      name: String(form.get('name') || ''),
      email: String(form.get('email') || ''),
      password: String(form.get('password') || ''),
    };
    const res = await fetch('/api/cms/bootstrap', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setBusy(false);
    if (!res.ok) {
      setError(data.error || 'Bootstrap failed');
      return;
    }
    setUser(data.user);
    setRequiresBootstrap(false);
  }

  async function submitLogin(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError('');
    const form = new FormData(event.currentTarget);
    const payload = {
      email: String(form.get('email') || ''),
      password: String(form.get('password') || ''),
    };
    const res = await fetch('/api/cms/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setBusy(false);
    if (!res.ok) {
      setError(data.error || 'Login failed');
      return;
    }
    setUser(data.user);
  }

  async function submitContent(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError('');
    const payload = {
      title: formState.title.trim(),
      slug: formState.slug.trim().toLowerCase(),
      contentType: formState.contentType,
      excerpt: formState.excerpt.trim(),
      body: formState.body.trim(),
      status: formState.status,
    };
    const res = await fetch(editingId ? `/api/cms/content/${editingId}` : '/api/cms/content', {
      method: editingId ? 'PUT' : 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setBusy(false);
    if (!res.ok) {
      setError(data.error || 'Content save failed');
      return;
    }
    if (data.item) {
      setItems((prev) => {
        const remaining = prev.filter((item) => item.id !== data.item.id);
        return [data.item, ...remaining];
      });
    }
    resetForm();
  }

  async function removeItem(itemId: number) {
    const confirmed = window.confirm('Delete this content item? This cannot be undone.');
    if (!confirmed) return;
    setDeleteBusyId(itemId);
    setError('');
    const res = await fetch(`/api/cms/content/${itemId}`, {
      method: 'DELETE',
      credentials: 'include',
    });
    const data = await res.json();
    setDeleteBusyId(null);
    if (!res.ok) {
      setError(data.error || 'Delete failed');
      return;
    }
    setItems((prev) => prev.filter((item) => item.id !== itemId));
    if (editingId === itemId) resetForm();
  }

  async function logout() {
    await fetch('/api/cms/logout', { method: 'POST', credentials: 'include' });
    setUser(null);
    setItems([]);
    resetForm();
  }

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(231,190,103,0.18),_transparent_30%),_#090806] px-4 py-10 text-stone-100">
      <div className="mx-auto max-w-6xl">
        <div className="mb-8 flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-amber-300/80">E4 Power CMS</p>
            <h1 className="mt-3 text-4xl font-black uppercase tracking-tight text-stone-50">Content publishing workspace</h1>
            <p className="mt-3 max-w-3xl text-sm leading-7 text-stone-300">This first CMS foundation supports staff username and password access, a protected admin area, and structured content types for white papers, newsletters, funding opportunities, and thought leadership.</p>
          </div>
          {user ? (
            <button onClick={logout} className="inline-flex h-11 items-center justify-center rounded-full border border-white/15 px-5 text-sm font-semibold text-stone-100 transition hover:border-amber-300 hover:text-amber-300">Log out</button>
          ) : null}
        </div>

        {error ? <div className="mb-6 rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</div> : null}

        {requiresBootstrap === null ? (
          <div className={cardClass}>Loading CMS setup…</div>
        ) : user ? (
          <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
            <section className={cardClass}>
              <div className="mb-6 flex items-start justify-between gap-4">
                <div>
                  <p className="text-xs uppercase tracking-[0.35em] text-amber-300/80">Signed in</p>
                  <h2 className="mt-2 text-2xl font-bold text-stone-50">Welcome, {user.name}</h2>
                  <p className="mt-2 text-sm text-stone-300">Role: {user.role} · Email: {user.email}</p>
                </div>
                {editingId ? (
                  <button
                    onClick={resetForm}
                    type="button"
                    className="inline-flex h-11 items-center justify-center rounded-full border border-white/10 px-4 text-sm font-semibold text-stone-200 transition hover:border-amber-300 hover:text-amber-300"
                  >
                    Cancel edit
                  </button>
                ) : null}
              </div>

              <form className="grid gap-4" onSubmit={submitContent}>
                <div className="grid gap-4 md:grid-cols-2">
                  <label className="grid gap-2 text-sm">
                    <span>Title</span>
                    <input
                      className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none"
                      name="title"
                      value={formState.title}
                      onChange={(event) => setFormState((prev) => ({ ...prev, title: event.target.value }))}
                      required
                    />
                  </label>
                  <label className="grid gap-2 text-sm">
                    <span>Slug</span>
                    <input
                      className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none"
                      name="slug"
                      value={formState.slug}
                      onChange={(event) => setFormState((prev) => ({ ...prev, slug: event.target.value }))}
                      required
                    />
                  </label>
                </div>
                <div className="grid gap-4 md:grid-cols-2">
                  <label className="grid gap-2 text-sm">
                    <span>Content type</span>
                    <select
                      className="h-11 rounded-xl border border-white/10 bg-[#15120f] px-3 text-stone-100 outline-none"
                      name="contentType"
                      value={formState.contentType}
                      onChange={(event) => setFormState((prev) => ({ ...prev, contentType: event.target.value }))}
                    >
                      {contentTypes.map((type) => (
                        <option key={type.value} value={type.value}>{type.label}</option>
                      ))}
                    </select>
                  </label>
                  <label className="grid gap-2 text-sm">
                    <span>Status</span>
                    <select
                      className="h-11 rounded-xl border border-white/10 bg-[#15120f] px-3 text-stone-100 outline-none"
                      name="status"
                      value={formState.status}
                      onChange={(event) => setFormState((prev) => ({ ...prev, status: event.target.value as 'draft' | 'published' }))}
                    >
                      <option value="draft">Draft</option>
                      <option value="published">Published</option>
                    </select>
                  </label>
                </div>
                <label className="grid gap-2 text-sm">
                  <span>Excerpt</span>
                  <textarea
                    className="min-h-24 rounded-2xl border border-white/10 bg-white/5 px-3 py-3 text-stone-100 outline-none"
                    name="excerpt"
                    value={formState.excerpt}
                    onChange={(event) => setFormState((prev) => ({ ...prev, excerpt: event.target.value }))}
                  />
                </label>
                <label className="grid gap-2 text-sm">
                  <span>Body</span>
                  <textarea
                    className="min-h-48 rounded-2xl border border-white/10 bg-white/5 px-3 py-3 text-stone-100 outline-none"
                    name="body"
                    value={formState.body}
                    onChange={(event) => setFormState((prev) => ({ ...prev, body: event.target.value }))}
                  />
                </label>
                <button disabled={busy} className="inline-flex h-12 items-center justify-center rounded-full bg-amber-400 px-6 text-sm font-bold uppercase tracking-[0.2em] text-stone-950 transition hover:bg-amber-300 disabled:opacity-60">
                  {busy ? 'Saving…' : editingId ? 'Update content item' : 'Create content item'}
                </button>
              </form>
            </section>

            <aside className={cardClass}>
              <div className="flex items-center justify-between gap-3">
                <p className="text-xs uppercase tracking-[0.35em] text-amber-300/80">Current items</p>
                <span className="rounded-full border border-white/10 px-3 py-1 text-[11px] uppercase tracking-[0.18em] text-stone-300">{items.length} total</span>
              </div>
              <div className="mt-5 grid gap-3">
                {items.length ? items.map((item) => (
                  <article key={item.id} className="rounded-2xl border border-white/10 bg-white/5 p-4">
                    <div className="flex items-start justify-between gap-3">
                      <div>
                        <h3 className="font-semibold text-stone-50">{item.title}</h3>
                        <p className="mt-2 text-xs uppercase tracking-[0.18em] text-amber-200/80">{formatContentType(item.contentType)}</p>
                        <p className="mt-2 text-sm text-stone-400">/{item.slug}</p>
                      </div>
                      <span className="rounded-full border border-white/10 px-2.5 py-1 text-[11px] uppercase tracking-[0.18em] text-stone-300">{item.status}</span>
                    </div>
                    {item.excerpt ? <p className="mt-3 text-sm leading-6 text-stone-300">{item.excerpt}</p> : null}
                    <div className="mt-4 flex flex-wrap gap-2">
                      <button
                        type="button"
                        onClick={() => populateForm(item)}
                        className="inline-flex h-10 items-center justify-center rounded-full border border-white/10 px-4 text-xs font-semibold uppercase tracking-[0.16em] text-stone-200 transition hover:border-amber-300 hover:text-amber-300"
                      >
                        Edit
                      </button>
                      <button
                        type="button"
                        onClick={() => removeItem(item.id)}
                        disabled={deleteBusyId === item.id}
                        className="inline-flex h-10 items-center justify-center rounded-full border border-red-400/20 px-4 text-xs font-semibold uppercase tracking-[0.16em] text-red-100 transition hover:border-red-300 hover:text-red-200 disabled:opacity-60"
                      >
                        {deleteBusyId === item.id ? 'Deleting…' : 'Delete'}
                      </button>
                    </div>
                  </article>
                )) : <div className="rounded-2xl border border-dashed border-white/10 bg-white/5 p-5 text-sm text-stone-400">No content items yet. Create the first one from the form.</div>}
              </div>
            </aside>
          </div>
        ) : requiresBootstrap ? (
          <form className={cardClass + ' mx-auto max-w-2xl grid gap-4'} onSubmit={submitBootstrap}>
            <div>
              <p className="text-xs uppercase tracking-[0.35em] text-amber-300/80">Initial setup</p>
              <h2 className="mt-2 text-2xl font-bold text-stone-50">Create the first CMS admin account</h2>
              <p className="mt-2 text-sm leading-7 text-stone-300">This bootstrap step is available only while no CMS users exist. After the first account is created, staff will sign in with email and password.</p>
            </div>
            <div className="grid gap-4 md:grid-cols-2">
              <label className="grid gap-2 text-sm"><span>Name</span><input className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none" name="name" required /></label>
              <label className="grid gap-2 text-sm"><span>Email</span><input className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none" name="email" type="email" required /></label>
            </div>
            <label className="grid gap-2 text-sm"><span>Password</span><input className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none" name="password" type="password" minLength={10} required /></label>
            <button disabled={busy} className="inline-flex h-12 items-center justify-center rounded-full bg-amber-400 px-6 text-sm font-bold uppercase tracking-[0.2em] text-stone-950 transition hover:bg-amber-300 disabled:opacity-60">{busy ? 'Creating…' : 'Create admin account'}</button>
          </form>
        ) : (
          <form className={cardClass + ' mx-auto max-w-xl grid gap-4'} onSubmit={submitLogin}>
            <div>
              <p className="text-xs uppercase tracking-[0.35em] text-amber-300/80">Staff login</p>
              <h2 className="mt-2 text-2xl font-bold text-stone-50">Sign in to the CMS</h2>
              <p className="mt-2 text-sm leading-7 text-stone-300">Use your staff email address and password to manage white papers, newsletters, funding opportunities, and thought leadership content.</p>
            </div>
            <label className="grid gap-2 text-sm"><span>Email</span><input className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none" name="email" type="email" required /></label>
            <label className="grid gap-2 text-sm"><span>Password</span><input className="h-11 rounded-xl border border-white/10 bg-white/5 px-3 text-stone-100 outline-none" name="password" type="password" required /></label>
            <button disabled={busy} className="inline-flex h-12 items-center justify-center rounded-full bg-amber-400 px-6 text-sm font-bold uppercase tracking-[0.2em] text-stone-950 transition hover:bg-amber-300 disabled:opacity-60">{busy ? 'Signing in…' : 'Sign in'}</button>
          </form>
        )}
      </div>
    </div>
  );
}
