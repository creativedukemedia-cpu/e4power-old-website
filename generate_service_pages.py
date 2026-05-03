from pathlib import Path
import html
import re
import urllib.parse

BASE = Path('/home/ubuntu/e4powerinc-clone/client')
source = (BASE / 'index.html').read_text(encoding='utf-8')

head_match = re.search(r'<!DOCTYPE html>.*?</head>', source, re.S)
footer_match = re.search(r'<footer class="section footer">.*', source, re.S)
if not head_match or not footer_match:
    raise SystemExit('Could not extract head/footer from homepage')

base_head = head_match.group(0)
base_footer = footer_match.group(0)

nav_html = '''<nav class="navbar-logo-left"><div class="navbar-logo-left-container shadow-three w-nav" data-animation="over-right" data-collapse="all" data-duration="400" data-easing="ease" data-easing2="ease" role="banner"><div class="navbar-container"><div class="navbar-wrapper"><a class="navbar-brand w-nav-brand" href="/"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg"/></a><div class="navbar-right-div"><div class="socials-div"><a class="social-link-block w-inline-block" href="https://www.instagram.com/e4power_?igsh=bXR4bThxMHh2dHNy&amp;utm_source=qr" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c4ee8e329fe01d525b_instagram.svg"/></a><a class="social-link-block w-inline-block" href="https://www.linkedin.com/company/e4-power-consulting/" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c46c9537fa67bb89bd_linkedin.svg"/></a><a class="social-link-block w-inline-block" href="https://www.tiktok.com/@e4powerconsulting?_t=ZT-90YVLBMkwaT&amp;_r=1" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68f66f4d7a2ffc0d86a72550_tiktok.svg"/></a><a class="social-link-block w-inline-block" href="https://www.facebook.com/profile.php?id=61573544665670&amp;mibextid=wwXIfr&amp;rdid=yOcyRogs7shBnrLD&amp;share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1775G2zRAh%2F%3Fmibextid%3DwwXIfr#" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c48dbb4dd69e849624_facebook.svg"/></a></div><a class="text-link" href="/contact-us">Contact Us</a><div class="menu-button w-nav-button"><div class="hamburger-icon w-icon-nav-menu"></div></div></div><nav class="nav-menu-wrapper w-nav-menu" role="navigation"><ul class="nav-menu-two w-list-unstyled" role="list"><li><a class="nav-link" href="/services/">SERVICES</a></li><li><a class="nav-link" href="/educate/">EDUCATE</a></li><li><a class="nav-link" href="/empower/">EMPOWER</a></li><li><a class="nav-link" href="/elevate/">ELEVATE</a></li><li><a class="nav-link" href="/engage/">ENGAGE</a></li></ul></nav></div></div></div></nav>'''

footer_replacements = {
    'href="#educate"': 'href="/educate/"',
    'href="#empower"': 'href="/empower/"',
    'href="#elevate"': 'href="/elevate/"',
    'href="#engage"': 'href="/engage/"',
}
shared_footer = base_footer
for old, new in footer_replacements.items():
    shared_footer = shared_footer.replace(old, new)
shared_footer = shared_footer.replace('</div><div class="socials-div footer">', '<a class="testimonial-text footer-link" href="/services/">SERVICES</a><div class="testimonial-text footer-link">|</div></div><div class="socials-div footer">')

E4_LOGO = 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg'
ICON = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0 16 8 8 16 0 8Z"></path></svg>'
PILLAR_ORDER = ['Educate', 'Empower', 'Elevate', 'Engage']
PILLAR_SLUGS = {'Educate': 'educate', 'Empower': 'empower', 'Elevate': 'elevate', 'Engage': 'engage'}

custom_css = '''
<style>
.ref-page-shell {
  background: radial-gradient(circle at 82% 14%, rgba(226,178,76,0.12) 0%, rgba(226,178,76,0) 24%), #140904;
  color: #f7f0e6;
}
.ref-gallery-section {
  padding: 10rem 0 6rem;
}
.ref-top-block {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}
.ref-heading-stack {
  max-width: 48rem;
}
.ref-heading-accent {
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .08em;
  font-size: clamp(2.2rem, 4vw, 3.6rem);
  line-height: .92;
  margin: 0;
}
.ref-heading-main {
  color: #fff;
  text-transform: uppercase;
  letter-spacing: .02em;
  font-size: clamp(3.4rem, 6.8vw, 5.8rem);
  line-height: .92;
  margin: .35rem 0 0;
}
.ref-meta-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 1.5rem;
  align-items: center;
}
.ref-divider-wrap {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}
.ref-divider {
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,0.74);
}
.ref-overline {
  color: rgba(255,255,255,0.86);
  text-transform: uppercase;
  letter-spacing: .26em;
  font-size: .86rem;
  white-space: nowrap;
}
.ref-mark {
  width: 52px;
  height: auto;
  opacity: .98;
}
.ref-subhead-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 2rem;
  margin-top: .8rem;
  flex-wrap: wrap;
}
.ref-subtitle {
  color: #fff;
  margin: 0;
  text-transform: uppercase;
  font-size: clamp(2rem, 4vw, 3.3rem);
  line-height: 1.05;
  max-width: 18ch;
}
.ref-subtitle span {
  color: #e2b24c;
}
.ref-page-summary {
  margin: 1.4rem 0 0;
  max-width: 62rem;
  color: #ddcfbf;
  font-size: 1.08rem;
  line-height: 1.9;
}
.ref-cta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1.25rem 2rem;
  background: #e2b24c;
  color: #16110b;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .1em;
  font-size: .96rem;
  font-weight: 700;
  border: 1px solid #e2b24c;
  min-width: 14rem;
}
.ref-service-section {
  margin-top: 4.5rem;
  padding-top: 3rem;
  border-top: 1px solid rgba(255,255,255,0.12);
}
.ref-service-kicker {
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .22em;
  font-size: .75rem;
}
.ref-service-title-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem 2rem;
  margin-top: .6rem;
}
.ref-service-title {
  margin: 0;
  color: #fff;
  text-transform: uppercase;
  font-size: clamp(2rem, 4vw, 3.1rem);
  line-height: 1;
}
.ref-service-link {
  color: #e2b24c;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: .82rem;
}
.ref-service-summary {
  margin: 1rem 0 0;
  max-width: 60rem;
  color: #d8cab8;
  font-size: 1.02rem;
  line-height: 1.8;
}
.ref-grid {
  margin-top: 2rem;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 2.2rem 1.5rem;
}
.ref-card-link {
  display: block;
  height: 100%;
  color: inherit;
  text-decoration: none;
}
.ref-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: transform .22s ease, box-shadow .22s ease;
}
.ref-card-link:hover .ref-card,
.ref-card-link:focus .ref-card,
.ref-card-link:focus-visible .ref-card {
  transform: translateY(-6px);
}
.ref-card-media {
  aspect-ratio: 3 / 4.35;
  background-size: cover;
  background-position: center;
  border: 1px solid rgba(255,255,255,0.06);
  filter: grayscale(1);
  transition: filter .28s ease, transform .28s ease;
  box-shadow: 0 16px 40px rgba(0,0,0,0.26);
}
.ref-card-link:hover .ref-card-media,
.ref-card-link:focus .ref-card-media,
.ref-card-link:focus-visible .ref-card-media,
.ref-card:hover .ref-card-media {
  filter: grayscale(0);
}
.ref-card-titleband {
  background: #fff;
  color: #121212;
  text-transform: uppercase;
  letter-spacing: .18em;
  font-size: .95rem;
  text-align: center;
  padding: 1rem .8rem;
  min-height: 4.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.ref-card-label {
  margin-top: .95rem;
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .18em;
  font-size: .72rem;
}
.ref-card-note {
  color: #d8cab8;
  font-size: 1rem;
  line-height: 1.75;
  margin: .4rem 0 0;
}
.ref-point-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
}
.ref-point-list li {
  display: grid;
  grid-template-columns: 16px minmax(0, 1fr);
  gap: .8rem;
  align-items: start;
  color: #f5eee4;
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: .92rem;
}
.ref-point-list svg {
  width: 12px;
  height: 12px;
  fill: #e2b24c;
  margin-top: .35rem;
}
.ref-bottom-copy {
  margin-top: 3.5rem;
  max-width: 58rem;
  color: #d9ccb9;
  font-size: 1.04rem;
  line-height: 1.9;
}
.ref-bottom-links {
  display: flex;
  flex-wrap: wrap;
  gap: .9rem;
  margin-top: 1.5rem;
}
.ref-secondary-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: .9rem 1.15rem;
  border: 1px solid rgba(226,178,76,0.38);
  color: #f5eee4;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .12em;
  font-size: .78rem;
}
.ref-secondary-link.primary {
  background: rgba(226,178,76,0.12);
}
@media screen and (max-width: 1200px) {
  .ref-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media screen and (max-width: 767px) {
  .ref-gallery-section {
    padding: 8.25rem 0 4.75rem;
  }
  .ref-meta-row {
    grid-template-columns: 1fr;
  }
  .ref-divider-wrap {
    flex-wrap: wrap;
  }
  .ref-overline {
    white-space: normal;
  }
  .ref-subhead-row {
    flex-direction: column;
    align-items: stretch;
  }
  .ref-cta-button {
    width: 100%;
  }
  .ref-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
</style>
'''


def placeholder_svg(label):
    safe = html.escape(label.upper())
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1200" role="img" aria-label="{safe}">
    <rect width="900" height="1200" fill="#d8d8d8"/>
    <rect width="900" height="1200" fill="url(#g)"/>
    <rect x="78" y="84" width="744" height="344" rx="18" fill="#202020" opacity="0.92"/>
    <rect x="78" y="472" width="744" height="548" rx="18" fill="#f5f5f5" opacity="0.9"/>
    <rect x="128" y="146" width="210" height="210" rx="20" fill="#3b3b3b" opacity="0.72"/>
    <rect x="374" y="146" width="378" height="34" rx="10" fill="#5a5a5a" opacity="0.7"/>
    <rect x="374" y="214" width="294" height="26" rx="10" fill="#707070" opacity="0.58"/>
    <rect x="374" y="268" width="332" height="26" rx="10" fill="#707070" opacity="0.58"/>
    <rect x="374" y="322" width="238" height="26" rx="10" fill="#707070" opacity="0.58"/>
    <rect x="146" y="548" width="608" height="320" rx="18" fill="#b1b1b1" opacity="0.72"/>
    <rect x="146" y="916" width="480" height="32" rx="10" fill="#949494" opacity="0.7"/>
    <text x="146" y="1090" font-family="Arial, Helvetica, sans-serif" font-size="64" font-weight="700" letter-spacing="6" fill="#1f1f1f">{safe}</text>
    <defs>
      <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#ececec"/>
        <stop offset="55%" stop-color="#cfcfcf"/>
        <stop offset="100%" stop-color="#adadad"/>
      </linearGradient>
    </defs>
    </svg>'''
    return 'data:image/svg+xml;charset=UTF-8,' + urllib.parse.quote(svg)


def render_points(points):
    return ''.join(f'<li>{ICON}<span>{html.escape(point)}</span></li>' for point in points)


def render_cards(cards):
    items = []
    for card in cards:
        media = card.get('image') or placeholder_svg(card.get('placeholder', card['title']))
        label = f'<div class="ref-card-label">{html.escape(card["label"])}</div>' if card.get('label') else ''
        note = f'<p class="ref-card-note">{html.escape(card["note"])}</p>' if card.get('note') else ''
        article = (
            f'<article class="ref-card">'
            f'<div class="ref-card-media" style="background-image:url(\'{media}\')"></div>'
            f'<div class="ref-card-titleband">{html.escape(card["title"])}</div>'
            f'{label}{note}<ul class="ref-point-list">{render_points(card["points"])}</ul>'
            f'</article>'
        )
        if card.get('href'):
            article = f'<a class="ref-card-link" href="{card["href"]}">{article}</a>'
        items.append(article)
    return ''.join(items)


def render_links(links):
    items = []
    for idx, (label, href) in enumerate(links):
        cls = 'ref-secondary-link primary' if idx == 0 else 'ref-secondary-link'
        items.append(f'<a class="{cls}" href="{href}">{html.escape(label)}</a>')
    return ''.join(items)


def build_service_section(service, include_links=True):
    cards = []
    for pillar in PILLAR_ORDER:
        detail = service['pillars'][pillar]
        href = f'/services/{service["slug"]}/#{PILLAR_SLUGS[pillar]}' if include_links else None
        cards.append({
            'title': pillar,
            'label': service['title'],
            'note': detail['note'],
            'points': detail['points'],
            'placeholder': f'{service["title"]} {pillar}',
            'image': detail.get('image'),
            'href': href,
        })
    return (
        f'<section class="ref-service-section" id="{service["slug"]}">'
        f'<div class="ref-service-kicker">Service Focus</div>'
        f'<div class="ref-service-title-row"><h3 class="ref-service-title">{html.escape(service["title"])}</h3>'
        f'<a class="ref-service-link" href="/services/{service["slug"]}/">Open service page</a></div>'
        f'<p class="ref-service-summary">{html.escape(service["catalog_summary"])}</p>'
        f'<div class="ref-grid">{render_cards(cards)}</div>'
        f'</section>'
    )


def write_catalog_page(page):
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{html.escape(page["title"])}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    service_sections = ''.join(build_service_section(service) for service in services)
    body = f'''<!-- Design philosophy: Reference-led service gallery. Organize the Services catalog by named service, then show the four pillar lenses together beneath each service heading. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">{html.escape(page['accent_word'])}</div><h1 class="ref-heading-main">{html.escape(page['main_word'])}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">{html.escape(page['overline'])}</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">{page['subtitle']}</h2><p class="ref-page-summary">{html.escape(page['summary'])}</p></div><a class="ref-cta-button" href="{page['button_href']}">{html.escape(page['button_label'])}</a></div></div>{service_sections}<div class="ref-bottom-copy">{html.escape(page['closing_copy'])}</div><div class="ref-bottom-links">{render_links(page['secondary_links'])}</div></div></section>
{shared_footer}'''
    out_dir = BASE / 'services'
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')


def write_detail_page(service):
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{html.escape(service["title"])} | E4 Power</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    detail_cards = []
    for pillar in PILLAR_ORDER:
        detail = service['pillars'][pillar]
        detail_cards.append({
            'title': pillar,
            'label': service['title'],
            'note': detail['note'],
            'points': detail['points'],
            'placeholder': f'{service["title"]} {pillar}',
            'image': detail.get('image'),
        })
    body = f'''<!-- Design philosophy: Reference-led service detail page. Each service page keeps the example’s editorial layout while presenting the four pillars together under one service heading. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">Service</div><h1 class="ref-heading-main">{html.escape(service['title'])}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">Meet the experts behind your success</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">Our expertise <span>Your advantage</span></h2><p class="ref-page-summary">{html.escape(service['detail_summary'])}</p></div><a class="ref-cta-button" href="/contact-us">Contact Us</a></div></div><div class="ref-grid">{render_cards(detail_cards)}</div><div class="ref-bottom-copy">{html.escape(service['closing_copy'])}</div><div class="ref-bottom-links">{render_links(service['related_links'])}</div></div></section>
{shared_footer}'''
    out_dir = BASE / 'services' / service['slug']
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')


def write_pillar_page(page):
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{html.escape(page["title"])}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    body = f'''<!-- Design philosophy: Reference-led pillar page. Keep the dark editorial layout while preserving a pillar-specific summary. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">{html.escape(page['accent_word'])}</div><h1 class="ref-heading-main">{html.escape(page['main_word'])}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">{html.escape(page['overline'])}</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">{page['subtitle']}</h2><p class="ref-page-summary">{html.escape(page['summary'])}</p></div><a class="ref-cta-button" href="{page['button_href']}">{html.escape(page['button_label'])}</a></div></div><div class="ref-grid">{render_cards(page['cards'])}</div><div class="ref-bottom-copy">{html.escape(page['closing_copy'])}</div><div class="ref-bottom-links">{render_links(page['secondary_links'])}</div></div></section>
{shared_footer}'''
    out_dir = BASE / page['slug']
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')


services = [
    {
        'slug': 'speaking-engagements',
        'title': 'Speaking Engagements',
        'catalog_summary': 'Speaking Engagements should show how one service can educate audiences, empower leadership, elevate implementation, and engage new institutional relationships.',
        'detail_summary': 'This service page frames Speaking Engagements through all four pillars so decision-makers can see how one speaking offer creates value across education, strategy, execution, and partnership-building.',
        'closing_copy': 'Speaking Engagements works best when E4 Power needs to create trust quickly, shape the room, and open a broader pathway into training, advisory support, or implementation work.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use talks and keynote sessions to transfer knowledge, train teams, and introduce new language around innovation and grants.', 'points': ['Conference keynotes', 'Learning-centered sessions', 'Team readiness framing'], 'image': '/manus-storage/SpeakingEngagementsEducate_c4effd85.jpg'},
            'Empower': {'note': 'Position speaking as a strategic catalyst that helps leaders see competitive opportunities and organizational next steps.', 'points': ['Executive briefings', 'Opportunity framing', 'Strategic positioning'], 'image': '/manus-storage/SpeakingEngagementsEmpower_3fc5583d.jpg'},
            'Elevate': {'note': 'Translate ideas into action by using speaking engagements to reinforce implementation discipline and institutional accountability.', 'points': ['Execution-minded messaging', 'Operational clarity', 'Action-oriented summaries'], 'image': '/manus-storage/SpeakingEngagementsElevate_18d2199e.jpg'},
            'Engage': {'note': 'Open new relationships through visible thought leadership that builds trust before deeper consulting begins.', 'points': ['Relationship-first introductions', 'Advisory entry point', 'Trust-building presence'], 'image': '/manus-storage/SpeakingEngagementsEngage_85977d11.jpg'},
        },
    },
    {
        'slug': 'workshops-training',
        'title': 'Workshops & Training',
        'catalog_summary': 'Workshops & Training should show how one learning offer can touch the full E4 framework instead of sitting only inside Educate.',
        'detail_summary': 'This service page presents Workshops & Training as a cross-pillar capability, with each card translating the same service into a different institutional outcome.',
        'closing_copy': 'Workshops & Training is most effective when organizations need shared language, stronger internal readiness, and a practical bridge from learning into action.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Build understanding through hands-on learning sessions that increase team knowledge and confidence.', 'points': ['Grant-writing workshops', 'Team learning cohorts', 'Capacity-building sessions'], 'image': '/manus-storage/WorkshopsEducate_b45793c3.jpg'},
            'Empower': {'note': 'Turn training into strategic momentum by focusing workshops on opportunity creation and competitive readiness.', 'points': ['Proposal strategy labs', 'Innovation workshops', 'Readiness acceleration'], 'image': '/manus-storage/WorkshopsEmpower_1c7c419c.jpg'},
            'Elevate': {'note': 'Use training to strengthen execution systems, role clarity, and post-award stewardship habits.', 'points': ['Compliance training', 'Delivery workflows', 'Execution support routines'], 'image': '/manus-storage/WorkshopsElevate_4dfab6d9.jpg'},
            'Engage': {'note': 'Create a collaborative entry point through workshops that align stakeholders before larger engagements begin.', 'points': ['Cross-team sessions', 'Partnership-building facilitation', 'Stakeholder alignment'], 'image': '/manus-storage/WorkshopsEngage_4153d98d.jpg'},
        },
    },
    {
        'slug': 'technology-ai-literacy',
        'title': 'Technology & AI Literacy',
        'catalog_summary': 'Technology & AI Literacy should be shown as one service with four different applications across the E4 pillars.',
        'detail_summary': 'This page shows how Technology & AI Literacy can educate teams, empower leaders, elevate operations, and engage institutions in a responsible adoption conversation.',
        'closing_copy': 'Technology & AI Literacy is the right starting point when organizations need confidence, context, and a human-centered approach before moving into deeper digital implementation.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Teach foundational concepts in plain language so teams understand what AI and digital systems actually mean in practice.', 'points': ['AI readiness education', 'Digital-literacy training', 'Common-language building'], 'image': '/manus-storage/TechnologyEducate_ddab685d.jpg'},
            'Empower': {'note': 'Connect literacy to strategy by helping leaders spot where technology can strengthen competitiveness.', 'points': ['Strategic tool evaluation', 'Innovation positioning', 'Opportunity prioritization'], 'image': '/manus-storage/TechnologyEmpower_b7f31cc8.jpg'},
            'Elevate': {'note': 'Apply literacy to operations by clarifying workflows, governance needs, and practical system use.', 'points': ['Workflow translation', 'Governance-aware adoption', 'Operational clarity'], 'image': '/manus-storage/TechnologyElevate_138a698f.jpg'},
            'Engage': {'note': 'Use technology conversations to open thoughtful, trust-based advisory relationships with cautious or curious organizations.', 'points': ['Discovery-led technology talks', 'Human-centered alignment', 'Low-pressure entry point'], 'image': '/manus-storage/TechnologyEngage_d37c12cc.jpg'},
        },
    },
    {
        'slug': 'grant-writing',
        'title': 'Grant Writing',
        'catalog_summary': 'Grant Writing should appear as a single named service with pillar-specific value cards underneath it, not as one item inside only Empower.',
        'detail_summary': 'This page reframes Grant Writing through all four pillars so visitors can see both the direct proposal function and the broader institutional value around it.',
        'closing_copy': 'Grant Writing remains one of the clearest expressions of E4 Power’s value because it joins strategic opportunity, institutional storytelling, delivery discipline, and trust-building in one service.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use grant-writing support to teach teams the language, structure, and habits behind stronger proposals.', 'points': ['Proposal education', 'Narrative coaching', 'Team writing readiness'], 'image': '/manus-storage/GrantWritingEducate_c171d3af.jpg'},
            'Empower': {'note': 'Drive competitive positioning through pre-award strategy, proposal development, and stronger submissions.', 'points': ['Opportunity scans', 'Narrative development', 'Submission support'], 'image': '/manus-storage/GrantwritingEmpower_25766faf.jpg'},
            'Elevate': {'note': 'Carry proposal work into delivery readiness by clarifying budgets, compliance expectations, and operational follow-through.', 'points': ['Budget discipline', 'Compliance preparation', 'Post-award handoff clarity'], 'image': '/manus-storage/GrantwritingElevate_dbfa3042.jpg'},
            'Engage': {'note': 'Use grant-writing conversations as an advisory front door that reveals fit, priorities, and institutional ambition.', 'points': ['Discovery conversations', 'Relationship-based planning', 'Trust-first scoping'], 'image': '/manus-storage/GrantwritingEngage_25ed8665.jpg'},
        },
    },
    {
        'slug': 'readiness-assessments',
        'title': 'Readiness Assessments',
        'catalog_summary': 'Readiness Assessments should be treated as a service with four pillar lenses, because its value touches training, strategy, execution, and partnership entry.',
        'detail_summary': 'This page shows Readiness Assessments as a diagnostic service that can support learning, strategic planning, operational discipline, and relationship design at the same time.',
        'closing_copy': 'Readiness Assessments work best when an organization needs a disciplined view of what is ready now, what is missing, and what path deserves priority.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use the assessment to teach teams where capacity gaps exist and what internal development should happen next.', 'points': ['Capability awareness', 'Learning priorities', 'Readiness education'], 'image': '/manus-storage/readiness-assessments-educate_8cfcac33.jpg'},
            'Empower': {'note': 'Clarify the strategic path forward by identifying where competitiveness and growth can be strengthened.', 'points': ['Gap identification', 'Infrastructure mapping', 'Priority sequencing'], 'image': '/manus-storage/readiness-assessments-empower_45928b64.jpg'},
            'Elevate': {'note': 'Translate findings into better execution systems, accountability, and operational sequencing.', 'points': ['Execution baseline', 'Workflow visibility', 'Delivery planning'], 'image': '/manus-storage/readiness-assessments-elevate_fdd3c036.jpg'},
            'Engage': {'note': 'Use assessments as an advisory entry service that creates clarity before larger commitments are made.', 'points': ['Discovery-led onboarding', 'Trust-building diagnosis', 'Relationship-fit review'], 'image': '/manus-storage/readiness-assessments-engage_a98215f4.jpg'},
        },
    },
    {
        'slug': 'intellectual-property',
        'title': 'Intellectual Property',
        'catalog_summary': 'Intellectual Property should be grouped as one named service with four pillar interpretations, rather than appearing as only an Empower capability.',
        'detail_summary': 'This page shows Intellectual Property as a strategic service that can educate innovators, empower competitive positioning, elevate commercialization workflows, and engage long-term advisory relationships.',
        'closing_copy': 'Intellectual Property becomes more valuable when it is not isolated as a legal concern, but connected to funding strategy, institutional execution, and innovation partnerships.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Teach researchers and teams how innovation protection works in practical, decision-oriented language.', 'points': ['Inventor education', 'Protection basics', 'Innovation literacy'], 'image': '/manus-storage/intellectual-property-educate_15920b4d.jpg'},
            'Empower': {'note': 'Use IP strategy to improve competitive position, strengthen value creation, and support opportunity development.', 'points': ['Protection strategy', 'Commercial positioning', 'Research-value framing'], 'image': '/manus-storage/intellectual-property-empower-replacement_64bb49e5.jpg'},
            'Elevate': {'note': 'Support the operational side of innovation by aligning process, documentation, and execution pathways.', 'points': ['Documentation readiness', 'Workflow coordination', 'Execution support'], 'image': '/manus-storage/intellectual-property-elevate_1840c229.jpg'},
            'Engage': {'note': 'Open relationship-led conversations around innovation ecosystems, partnerships, and institutional growth.', 'points': ['Innovation advisory entry', 'Partnership conversations', 'Long-term strategic fit'], 'image': '/manus-storage/intellectual-property-engage_f87e60f0.jpg'},
        },
    },
    {
        'slug': 'it-app-development',
        'title': 'IT Solutions',
        'catalog_summary': 'IT Solutions should be presented exactly as a named service block with all four pillar cards beneath it, so visitors can see how one digital service supports the full E4 model.',
        'detail_summary': 'This page frames IT Solutions as a service that teaches teams, strengthens competitiveness, improves execution, and creates stronger partnership pathways through custom digital infrastructure.',
        'closing_copy': 'IT Solutions is strongest when E4 Power needs to turn advisory thinking into practical systems, whether that means education, workflow enablement, or full digital delivery.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use IT Solutions to help teams understand systems, tools, and digital possibilities before full implementation begins.', 'points': ['Technology orientation', 'Tool literacy', 'Digital-confidence building'], 'image': '/manus-storage/it-solutions-educate_6a8e2cf8.jpg'},
            'Empower': {'note': 'Position IT Solutions as a competitive growth service through custom apps, portals, and strategic digital buildouts.', 'points': ['Custom portals', 'Web app delivery', 'Strategic digital infrastructure'], 'image': '/manus-storage/it-solutions-empower_467be857.jpg'},
            'Elevate': {'note': 'Strengthen execution through operational systems that improve workflows, visibility, and continuity after launch.', 'points': ['Workflow automation', 'Operational dashboards', 'Maintenance planning'], 'image': '/manus-storage/it-solutions-elevate_9fe8b38b.jpg'},
            'Engage': {'note': 'Use digital solution conversations to open advisory relationships built around listening, fit, and institutional needs.', 'points': ['Discovery-led scoping', 'Stakeholder alignment', 'Partnership-first planning'], 'image': '/manus-storage/it-solutions-engage_0f24fbf1.jpg'},
        },
    },
    {
        'slug': 'grant-management',
        'title': 'Grant Management',
        'catalog_summary': 'Grant Management should be shown as one service with four related pillar cards so visitors can understand its full institutional role.',
        'detail_summary': 'This page organizes Grant Management through the four pillars, showing how the same service supports learning, strategy, execution discipline, and partnership trust.',
        'closing_copy': 'Grant Management matters because winning funding is only the beginning; this service protects the credibility, reporting rhythm, and stewardship needed to sustain success.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use grant-management support to teach teams the systems and habits required for responsible post-award work.', 'points': ['Post-award education', 'Reporting literacy', 'Compliance awareness'], 'image': '/manus-storage/grant-management-educate_e38adbf6.jpg'},
            'Empower': {'note': 'Strengthen future competitiveness by proving the institution can manage awards with discipline and credibility.', 'points': ['Stewardship positioning', 'Funders-confidence building', 'Future-opportunity readiness'], 'image': '/manus-storage/grant-management-empower_c2434eaf.jpg'},
            'Elevate': {'note': 'Center execution through award oversight, reporting coordination, and compliance-driven workflows.', 'points': ['Reporting coordination', 'Compliance oversight', 'Award closeout support'], 'image': '/manus-storage/grant-management-elevate_6fe29bfa.jpg'},
            'Engage': {'note': 'Build durable client relationships by supporting institutions after the award, not just before it.', 'points': ['Longer-term advisory trust', 'Operational partnership', 'Continuation planning'], 'image': '/manus-storage/grant-management-engage_eb2ba404.jpg'},
        },
    },
    {
        'slug': 'project-management',
        'title': 'Project Management',
        'catalog_summary': 'Project Management should be grouped as its own service and then translated across all four pillars underneath it.',
        'detail_summary': 'This page shows Project Management as more than delivery mechanics: it can educate teams, empower planning, elevate execution, and engage stakeholders in a clearer working model.',
        'closing_copy': 'Project Management is essential when ambitious work needs more than strategy alone and requires disciplined coordination across people, timelines, and decisions.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Teach teams how structured delivery works so responsibilities, milestones, and expectations become clearer.', 'points': ['Delivery education', 'Role clarity', 'Project literacy'], 'image': '/manus-storage/project-management-educate_464d8e84.jpg'},
            'Empower': {'note': 'Use project-management framing to turn strategic ambition into a phased, achievable plan.', 'points': ['Milestone mapping', 'Strategic sequencing', 'Ownership definition'], 'image': '/manus-storage/project-management-empower_c9414cbd.jpg'},
            'Elevate': {'note': 'Support active delivery through coordination systems, issue visibility, and measurable operational progress.', 'points': ['Timeline management', 'Cross-team execution', 'Risk-aware coordination'], 'image': '/manus-storage/project-management-elevate_0a1e56d2.jpg'},
            'Engage': {'note': 'Create a healthier partnership by giving stakeholders a shared way to work, communicate, and make decisions.', 'points': ['Stakeholder coordination', 'Meeting cadence design', 'Collaboration structure'], 'image': '/manus-storage/project-management-engage_01ca1dc3.jpg'},
        },
    },
    {
        'slug': 'financial-management',
        'title': 'Financial Management',
        'catalog_summary': 'Financial Management should sit as one named service with four supporting pillar cards beneath it, rather than as only an Elevate item.',
        'detail_summary': 'This page presents Financial Management as a service that improves institutional understanding, strategic trust, operational control, and relationship confidence all at once.',
        'closing_copy': 'Financial Management reinforces E4 Power’s role as a credible implementation partner by protecting the fiscal integrity behind ambitious work.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Teach teams the budget, stewardship, and accountability basics that support strong funded work.', 'points': ['Budget literacy', 'Stewardship education', 'Control awareness'], 'image': '/manus-storage/financial-management-educate_e4e173a6.jpg'},
            'Empower': {'note': 'Use strong fiscal systems to improve institutional credibility and support future opportunities.', 'points': ['Credibility building', 'Funding confidence', 'Strategic trust'], 'image': '/manus-storage/financial-management-empower_442d9b13.jpg'},
            'Elevate': {'note': 'Anchor operations in disciplined budget tracking, reporting, and audit-aware management.', 'points': ['Budget oversight', 'Allowable-cost awareness', 'Audit-conscious controls'], 'image': '/manus-storage/financial-management-elevate_835b074e.jpg'},
            'Engage': {'note': 'Build client trust by showing that operational relationships will be handled with transparency and financial discipline.', 'points': ['Transparent stewardship', 'Relationship confidence', 'Clear financial communication'], 'image': '/manus-storage/financial-management-engage_df889e8e.jpg'},
        },
    },
    {
        'slug': 'institutional-discovery',
        'title': 'Institutional Discovery',
        'catalog_summary': 'Institutional Discovery should be shown as a named service with four pillar cards so its role as an entry point is visible across the whole E4 model.',
        'detail_summary': 'This page frames Institutional Discovery as the service that listens first, diagnoses context, and then translates insight across education, strategy, execution, and partnership design.',
        'closing_copy': 'Institutional Discovery is valuable because it gives organizations a lower-pressure starting point that still leads to concrete insight and stronger next-step clarity.',
        'related_links': [('Services Hub', '/services/'), ('Engage', '/engage/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use discovery to help teams understand their current condition, internal language, and development needs.', 'points': ['Current-state awareness', 'Team understanding', 'Learning-oriented diagnosis'], 'image': '/manus-storage/institutional-discovery-educate_a031e3d2.jpg'},
            'Empower': {'note': 'Turn early conversations into clearer strategic direction and more deliberate opportunity choices.', 'points': ['Needs clarification', 'Goal framing', 'Roadmap direction'], 'image': '/manus-storage/institutional-discovery-empower_17cf85e3.jpg'},
            'Elevate': {'note': 'Use discovery findings to shape more realistic operational plans and execution sequencing.', 'points': ['Execution baseline', 'Constraint mapping', 'Delivery readiness'], 'image': '/manus-storage/institutional-discovery-elevate_d69b2fc3.jpg'},
            'Engage': {'note': 'Lead with trust, listening, and fit so the relationship begins with clarity rather than assumption.', 'points': ['Discovery meetings', 'Advisory entry point', 'Relationship-fit assessment'], 'image': '/manus-storage/institutional-discovery-engage_10839b6c.jpg'},
        },
    },
    {
        'slug': 'advisory-alignment',
        'title': 'Advisory Alignment',
        'catalog_summary': 'Advisory Alignment should be structured as one service group with Educate, Empower, Elevate, and Engage cards under it.',
        'detail_summary': 'This page shows Advisory Alignment as a service that supports shared understanding, strategic clarity, stronger execution planning, and healthier working relationships.',
        'closing_copy': 'Advisory Alignment helps E4 Power move from possibility into a more coherent working model by matching the right people to the right next steps.',
        'related_links': [('Services Hub', '/services/'), ('Engage', '/engage/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use alignment conversations to teach stakeholders what success requires and how responsibilities should be understood.', 'points': ['Expectation setting', 'Shared language', 'Role understanding'], 'image': '/manus-storage/advisory-alignment-educate_1a41d707.jpg'},
            'Empower': {'note': 'Clarify the strategic path by aligning leaders, specialists, and priorities before work accelerates.', 'points': ['Decision-maker alignment', 'Specialist matching', 'Strategic clarity'], 'image': '/manus-storage/advisory-alignment-empower_88d02727.jpg'},
            'Elevate': {'note': 'Translate alignment into an actionable engagement model with clear responsibilities and momentum.', 'points': ['Action launch planning', 'Working-model definition', 'Operational checkpoints'], 'image': '/manus-storage/advisory-alignment-elevate_d42572ca.jpg'},
            'Engage': {'note': 'Use alignment as the partnership bridge that turns a first conversation into a durable advisory relationship.', 'points': ['Trust-building follow-through', 'Partnership structure', 'Collaborative planning'], 'image': '/manus-storage/advisory-alignment-engage_399926cc.jpg'},
        },
    },
]

pillar_pages = [
    {
        'slug': 'educate',
        'title': 'Educate | E4 Power',
        'accent_word': 'Educate',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Educate remains the knowledge-building pillar, showing how E4 Power turns expertise into training, speaking, literacy, and readiness-building experiences.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Speaking Engagements', 'label': 'Educate', 'note': 'Thought leadership designed to inform, motivate, and guide audiences.', 'points': ['Conference talks', 'Executive briefings', 'Learning-centered sessions'], 'placeholder': 'Speaking'},
            {'title': 'Workshops & Training', 'label': 'Educate', 'note': 'Structured learning experiences that build internal confidence and shared language.', 'points': ['Hands-on training', 'Team cohorts', 'Capacity building'], 'placeholder': 'Training'},
            {'title': 'Technology & AI Literacy', 'label': 'Educate', 'note': 'Practical instruction that makes digital change understandable and useful.', 'points': ['AI literacy', 'Workflow education', 'Responsible adoption'], 'placeholder': 'AI Literacy'},
            {'title': 'Readiness Assessments', 'label': 'Educate', 'note': 'Diagnostic learning that shows teams where to focus development next.', 'points': ['Gap visibility', 'Capacity insight', 'Priority learning'], 'placeholder': 'Assessment'},
        ],
        'closing_copy': 'Use Educate when the immediate need is shared understanding, confidence-building, and practical learning before deeper consulting or execution begins.',
        'secondary_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
    },
    {
        'slug': 'empower',
        'title': 'Empower | E4 Power',
        'accent_word': 'Empower',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Empower remains the strategy and competitiveness pillar, showing how E4 Power strengthens positioning, innovation, and opportunity creation.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Grant Writing', 'label': 'Empower', 'note': 'Proposal strategy and submission support with competitive focus.', 'points': ['Opportunity scans', 'Narrative development', 'Submission support'], 'placeholder': 'Grant Writing'},
            {'title': 'Intellectual Property', 'label': 'Empower', 'note': 'Innovation protection and commercialization-aware guidance.', 'points': ['Protection strategy', 'Commercial framing', 'Research-value alignment'], 'placeholder': 'IP'},
            {'title': 'IT Solutions', 'label': 'Empower', 'note': 'Digital systems that turn strategy into tangible infrastructure.', 'points': ['Custom portals', 'Web app delivery', 'Strategic buildouts'], 'placeholder': 'IT Solutions'},
            {'title': 'Readiness Assessments', 'label': 'Empower', 'note': 'Assessments that clarify what path can create momentum fastest.', 'points': ['Priority sequencing', 'Infrastructure mapping', 'Competitive baseline'], 'placeholder': 'Readiness'},
        ],
        'closing_copy': 'Use Empower when the focus is opportunity creation, strategic positioning, and the systems that help organizations move forward with greater confidence.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
    },
    {
        'slug': 'elevate',
        'title': 'Elevate | E4 Power',
        'accent_word': 'Elevate',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Elevate remains the execution-facing pillar, showing how E4 Power supports operational discipline, stewardship, and measurable delivery after plans are made.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Grant Management', 'label': 'Elevate', 'note': 'Post-award stewardship that protects credibility and momentum.', 'points': ['Reporting coordination', 'Compliance oversight', 'Award closeout support'], 'placeholder': 'Grant Management'},
            {'title': 'Project Management', 'label': 'Elevate', 'note': 'Execution systems that keep complex initiatives coordinated.', 'points': ['Timeline management', 'Cross-team execution', 'Risk-aware coordination'], 'placeholder': 'Project Management'},
            {'title': 'Financial Management', 'label': 'Elevate', 'note': 'Fiscal discipline aligned with funder expectations and operational trust.', 'points': ['Budget oversight', 'Audit-conscious controls', 'Financial communication'], 'placeholder': 'Financial'},
            {'title': 'IT Solutions', 'label': 'Elevate', 'note': 'Operational systems that improve visibility, workflows, and continuity.', 'points': ['Workflow automation', 'Dashboards', 'Maintenance planning'], 'placeholder': 'IT Elevate'},
        ],
        'closing_copy': 'Use Elevate when clients need proof that E4 Power can move from planning into disciplined delivery, stewardship, and operational continuity.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Empower', '/empower/'), ('Engage', '/engage/')],
    },
    {
        'slug': 'engage',
        'title': 'Engage | E4 Power',
        'accent_word': 'Engage',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Engage remains the relationship-building pillar, showing how E4 Power creates trust, fit, and collaborative momentum at the beginning of the client journey.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Institutional Discovery', 'label': 'Engage', 'note': 'Early conversations that clarify fit, priorities, and the best first move.', 'points': ['Discovery meetings', 'Needs clarification', 'Roadmap direction'], 'placeholder': 'Discovery'},
            {'title': 'Advisory Alignment', 'label': 'Engage', 'note': 'Alignment work that connects the right people to the right plan.', 'points': ['Decision-maker alignment', 'Partnership structure', 'Collaborative planning'], 'placeholder': 'Alignment'},
            {'title': 'Speaking Engagements', 'label': 'Engage', 'note': 'Visible thought leadership that opens trust-based relationships.', 'points': ['Thought-leadership entry', 'Trust-building presence', 'Advisory opening'], 'placeholder': 'Speaking Engage'},
            {'title': 'IT Solutions', 'label': 'Engage', 'note': 'Digital discovery conversations shaped around listening and institutional fit.', 'points': ['Discovery-led scoping', 'Stakeholder alignment', 'Partnership-first planning'], 'placeholder': 'IT Engage'},
        ],
        'closing_copy': 'Use Engage when the work should begin with listening, advisory trust, and a deliberate pathway into broader support.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Empower', '/empower/'), ('Elevate', '/elevate/')],
    },
]

catalog_page = {
    'title': 'Services | E4 Power',
    'accent_word': 'Service',
    'main_word': 'Catalog',
    'overline': 'Meet the experts behind your success',
    'subtitle': 'Our expertise <span>Your advantage</span>',
    'summary': 'This catalog is now organized by named service first. Each service block shows how that single offer expresses itself through Educate, Empower, Elevate, and Engage so visitors can compare the full E4 model side by side.',
    'button_label': 'Contact Us',
    'button_href': '/contact-us',
    'closing_copy': 'The Services page now behaves like a decision-maker map: start with the service name, review the four pillar expressions together, and then enter a dedicated service page for deeper context.',
    'secondary_links': [('Educate', '/educate/'), ('Empower', '/empower/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
}

write_catalog_page(catalog_page)
for page in pillar_pages:
    write_pillar_page(page)
for service in services:
    write_detail_page(service)
