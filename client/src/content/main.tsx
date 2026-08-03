import '../index.css';
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { useEffect, useMemo, useState } from 'react';

type CmsItem = {
  id: number;
  title: string;
  slug: string;
  contentType: 'white-paper' | 'newsletter' | 'funding-opportunity' | 'thought-leadership';
  status: 'draft' | 'published';
  excerpt?: string | null;
  body?: string | null;
  coverImageUrl?: string | null;
  publishedAt?: string | null;
};

const typeOptions = [
  { value: 'all', label: 'All published content' },
  { value: 'white-paper', label: 'White papers' },
  { value: 'newsletter', label: 'Newsletters' },
  { value: 'funding-opportunity', label: 'Funding opportunities' },
  { value: 'thought-leadership', label: 'Thought leadership' },
] as const;

function formatContentType(value: CmsItem['contentType']) {
  return value
    .split('-')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

function formatDate(value?: string | null) {
  if (!value) return 'Recently updated';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return 'Recently updated';
  return date.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

function useQueryState() {
  return useMemo(() => new URLSearchParams(window.location.search), [window.location.search]);
}

function ContentHubApp() {
  const [items, setItems] = useState<CmsItem[]>([]);
  const [item, setItem] = useState<CmsItem | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const query = useQueryState();
  const slug = query.get('slug')?.trim() || '';
  const filter = query.get('type')?.trim() || 'all';
  const search = query.get('q')?.trim().toLowerCase() || '';

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError('');

    const url = slug
      ? `/api/cms/public/content/${encodeURIComponent(slug)}`
      : `/api/cms/public/content${filter !== 'all' ? `?contentType=${encodeURIComponent(filter)}` : ''}`;

    fetch(url)
      .then(async (res) => {
        const data = await res.json();
        if (!res.ok) {
          throw new Error(data.error || 'Failed to load published content');
        }
        if (!active) return;
        if (slug) {
          setItem(data.item || null);
          setItems([]);
        } else {
          setItems(data.items || []);
          setItem(null);
        }
      })
      .catch((err) => {
        if (!active) return;
        setError(err instanceof Error ? err.message : 'Failed to load published content');
        setItem(null);
        setItems([]);
      })
      .finally(() => {
        if (active) setLoading(false);
      });

    return () => {
      active = false;
    };
  }, [slug, filter]);

  const filteredItems = useMemo(() => {
    if (!search) return items;
    return items.filter((entry) => entry.title.toLowerCase().includes(search) || entry.slug.toLowerCase().includes(search) || (entry.excerpt || '').toLowerCase().includes(search));
  }, [items, search]);

  const pageTitle = slug && item ? `${item.title} | E4 Power Insights` : 'E4 Power Insights';

  useEffect(() => {
    document.title = pageTitle;
  }, [pageTitle]);

  return (
    <div className="min-h-screen bg-[linear-gradient(180deg,#f6f1e3_0%,#f3ede0_45%,#eee5d4_100%)] text-stone-900">
      <header className="border-b border-black/10 bg-[#11100e] text-white">
        <div className="mx-auto flex max-w-6xl items-center justify-between gap-6 px-4 py-5 md:px-6">
          <div>
            <p className="text-xs uppercase tracking-[0.35em] text-amber-300/80">E4 Power</p>
            <h1 className="mt-2 text-2xl font-black uppercase tracking-tight">Insights</h1>
          </div>
          <nav className="flex items-center gap-4 text-sm font-semibold">
            <a className="text-stone-200 transition hover:text-amber-300" href="/">Back to main site</a>
            {slug ? <a className="text-stone-200 transition hover:text-amber-300" href="/content/index.html">All content</a> : null}
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-4 py-10 md:px-6 md:py-14">
        {slug ? (
          <article className="rounded-[2rem] border border-black/10 bg-white/85 p-6 shadow-[0_30px_60px_rgba(15,10,5,0.12)] backdrop-blur md:p-10">
            {loading ? (
              <p className="text-sm text-stone-500">Loading published content…</p>
            ) : error ? (
              <div className="rounded-2xl border border-red-300 bg-red-50 px-4 py-3 text-sm text-red-700">{error}</div>
            ) : item ? (
              <>
                <p className="text-xs font-semibold uppercase tracking-[0.35em] text-amber-700">{formatContentType(item.contentType)}</p>
                <h2 className="mt-4 text-4xl font-black uppercase tracking-tight text-stone-950">{item.title}</h2>
                <p className="mt-4 text-sm font-medium text-stone-500">Published {formatDate(item.publishedAt)}</p>
                {item.coverImageUrl ? (
                  <img src={item.coverImageUrl} alt={item.title} className="mt-8 h-auto w-full rounded-[1.75rem] border border-black/5 object-cover shadow-xl" />
                ) : null}
                {item.excerpt ? <p className="mt-8 text-lg leading-8 text-stone-700">{item.excerpt}</p> : null}
                {item.body ? (
                  <div className="prose prose-stone mt-8 max-w-none whitespace-pre-wrap text-base leading-8 text-stone-800">{item.body}</div>
                ) : null}
              </>
            ) : (
              <div className="rounded-2xl border border-black/10 bg-stone-50 px-4 py-4 text-sm text-stone-600">This published content item could not be found.</div>
            )}
          </article>
        ) : (
          <section>
            <div className="flex flex-col gap-6 rounded-[2rem] border border-black/10 bg-white/80 p-6 shadow-[0_30px_60px_rgba(15,10,5,0.10)] backdrop-blur md:flex-row md:items-end md:justify-between md:p-8">
              <div className="max-w-3xl">
                <p className="text-xs font-semibold uppercase tracking-[0.35em] text-amber-700">Published content hub</p>
                <h2 className="mt-4 text-4xl font-black uppercase tracking-tight text-stone-950">White papers, newsletters, opportunities, and thought leadership</h2>
                <p className="mt-4 text-base leading-8 text-stone-700">Browse the first public-facing CMS area. This page only surfaces items marked as published in the staff admin workspace.</p>
              </div>
              <div className="grid gap-4 md:min-w-[24rem]">
                <label className="grid gap-2 text-sm font-medium text-stone-700">
                  <span>Search published content</span>
                  <input
                    className="h-11 rounded-full border border-black/10 bg-[#f5efdf] px-4 text-stone-900 outline-none placeholder:text-stone-500"
                    defaultValue={query.get('q') || ''}
                    placeholder="Search by title, slug, or excerpt"
                    onKeyDown={(event) => {
                      if (event.key !== 'Enter') return;
                      const next = (event.currentTarget as HTMLInputElement).value.trim();
                      const params = new URLSearchParams(window.location.search);
                      if (next) params.set('q', next);
                      else params.delete('q');
                      const queryString = params.toString();
                      window.location.href = `/content/index.html${queryString ? `?${queryString}` : ''}`;
                    }}
                  />
                </label>
                <label className="grid gap-2 text-sm font-medium text-stone-700">
                  <span>Filter by content type</span>
                  <select
                    className="h-11 rounded-full border border-black/10 bg-[#f5efdf] px-4 text-stone-900 outline-none"
                    value={filter}
                    onChange={(event) => {
                      const next = event.target.value;
                      const params = new URLSearchParams(window.location.search);
                      if (next === 'all') params.delete('type');
                      else params.set('type', next);
                      const queryString = params.toString();
                      window.location.href = `/content/index.html${queryString ? `?${queryString}` : ''}`;
                    }}
                  >
                    {typeOptions.map((option) => (
                      <option key={option.value} value={option.value}>{option.label}</option>
                    ))}
                  </select>
                </label>
              </div>
            </div>

            <div className="mt-5 flex items-center justify-between gap-4 px-2 text-sm text-stone-600">
              <p>{filteredItems.length} result{filteredItems.length === 1 ? '' : 's'} shown</p>
              {search ? <a className="font-semibold text-amber-700 transition hover:text-amber-800" href={filter === 'all' ? '/content/index.html' : `/content/index.html?type=${encodeURIComponent(filter)}`}>Clear search</a> : null}
            </div>

            <div className="mt-8 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
              {loading ? (
                <div className="rounded-[1.75rem] border border-black/10 bg-white/70 p-6 text-sm text-stone-500">Loading published content…</div>
              ) : error ? (
                <div className="rounded-[1.75rem] border border-red-300 bg-red-50 p-6 text-sm text-red-700">{error}</div>
              ) : filteredItems.length === 0 ? (
                <div className="rounded-[1.75rem] border border-black/10 bg-white/70 p-6 text-sm text-stone-600">No published entries match the current search and filter settings yet.</div>
              ) : (
                filteredItems.map((entry) => (
                  <a
                    key={entry.id}
                    href={`/content/index.html?slug=${encodeURIComponent(entry.slug)}`}
                    className="group overflow-hidden rounded-[1.75rem] border border-black/10 bg-white/85 shadow-[0_22px_45px_rgba(15,10,5,0.10)] transition hover:-translate-y-1 hover:shadow-[0_28px_60px_rgba(15,10,5,0.14)]"
                  >
                    {entry.coverImageUrl ? (
                      <img src={entry.coverImageUrl} alt={entry.title} className="h-52 w-full object-cover transition duration-300 group-hover:scale-[1.02]" />
                    ) : (
                      <div className="flex h-52 items-end bg-[linear-gradient(135deg,rgba(214,170,82,0.25),rgba(17,16,14,0.9))] p-6">
                        <p className="text-xs font-semibold uppercase tracking-[0.35em] text-white/75">E4 Power</p>
                      </div>
                    )}
                    <div className="p-6">
                      <p className="text-xs font-semibold uppercase tracking-[0.35em] text-amber-700">{formatContentType(entry.contentType)}</p>
                      <h3 className="mt-4 text-2xl font-black uppercase tracking-tight text-stone-950">{entry.title}</h3>
                      <p className="mt-3 text-sm font-medium text-stone-500">Published {formatDate(entry.publishedAt)}</p>
                      {entry.excerpt ? <p className="mt-4 text-sm leading-7 text-stone-700">{entry.excerpt}</p> : null}
                    </div>
                  </a>
                ))
              )}
            </div>
          </section>
        )}
      </main>
    </div>
  );
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ContentHubApp />
  </StrictMode>
);
