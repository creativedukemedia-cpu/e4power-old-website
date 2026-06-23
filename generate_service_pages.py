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
.ref-gallery-section > .container {
  width: min(100% - 6rem, 1280px);
  margin: 0 auto;
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
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  gap: .8rem;
  padding: .92rem 1.35rem;
  border: 1px solid rgba(226,178,76,0.5);
  border-radius: 999px;
  background: linear-gradient(135deg, rgba(226,178,76,0.18), rgba(226,178,76,0.05));
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.18);
  color: #f6e7c4;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: .76rem;
  font-weight: 700;
  line-height: 1;
  transition: transform .28s ease, border-color .28s ease, background .28s ease, color .28s ease, box-shadow .28s ease;
}
.ref-service-link::before {
  content: '';
  position: absolute;
  inset: -35%;
  background: linear-gradient(120deg, rgba(255,255,255,0) 34%, rgba(255,244,212,0.02) 42%, rgba(255,244,212,0.38) 50%, rgba(255,244,212,0.02) 58%, rgba(255,255,255,0) 66%);
  transform: translateX(-165%) skewX(-24deg);
  animation: ref-service-link-sweep 3s ease-in-out infinite;
  pointer-events: none;
  z-index: 0;
}
.ref-service-link > * {
  position: relative;
  z-index: 1;
}
.ref-service-link::after {
  content: '→';
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.7rem;
  height: 1.7rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.1);
  color: #e2b24c;
  font-size: .95rem;
  line-height: 1;
  transition: transform .28s ease, background .28s ease, color .28s ease;
}
.ref-service-link:hover,
.ref-service-link:focus-visible {
  transform: translateY(-2px);
  border-color: rgba(226,178,76,0.88);
  background: linear-gradient(135deg, rgba(226,178,76,0.28), rgba(226,178,76,0.09));
  box-shadow: 0 18px 34px rgba(0, 0, 0, 0.24);
  color: #fff5dc;
}
.ref-service-link:hover::before,
.ref-service-link:focus-visible::before {
  animation-duration: 2.2s;
}
.ref-service-link:hover::after,
.ref-service-link:focus-visible::after {
  transform: translateX(3px);
  background: rgba(226,178,76,0.2);
  color: #fff4d4;
}
@keyframes ref-service-link-sweep {
  0%, 70%, 100% {
    transform: translateX(-165%) skewX(-24deg);
    opacity: 0;
  }
  8% {
    opacity: .15;
  }
  24% {
    transform: translateX(165%) skewX(-24deg);
    opacity: .72;
  }
  32% {
    opacity: 0;
  }
}
@media (prefers-reduced-motion: reduce) {
  .ref-service-link::before {
    animation: none;
  }
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
  aspect-ratio: 3 / 2.45;
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
  padding: .82rem .8rem;
  min-height: 4.1rem;
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
  font-size: 1.08rem;
  line-height: 1.56;
  margin-bottom: .86rem;
}
.ref-point-list svg {
  width: 13px;
  height: 13px;
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
.ref-detail-stack {
  margin-top: 3.5rem;
  display: grid;
  gap: 1.6rem;
}
.ref-detail-panel {
  border: 1px solid rgba(226,178,76,0.16);
  background: linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.015));
  padding: 1.65rem 1.55rem;
}
.ref-detail-panel--intro {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) minmax(18rem, .9fr);
  gap: 1.5rem;
  align-items: start;
}
.ref-detail-kicker {
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .18em;
  font-size: .72rem;
}
.ref-detail-heading {
  margin: .65rem 0 0;
  color: #fff;
  text-transform: uppercase;
  font-size: clamp(1.45rem, 2.4vw, 2.1rem);
  line-height: 1.04;
}
.ref-detail-copy {
  color: #dfd0bf;
  font-size: 1.02rem;
  line-height: 1.82;
}
.ref-detail-copy p {
  margin: 0;
}
.ref-detail-copy p + p {
  margin-top: .95rem;
}
.ref-badge-column {
  display: grid;
  gap: .8rem;
}
.ref-badge {
  border: 1px solid rgba(226,178,76,0.24);
  background: rgba(226,178,76,0.08);
  color: #fff4df;
  padding: .95rem 1rem;
  text-transform: uppercase;
  letter-spacing: .1em;
  font-size: .8rem;
  line-height: 1.5;
}
.ref-model-grid,
.ref-tool-grid,
.ref-example-grid {
  display: grid;
  gap: 1rem;
}
.ref-model-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.ref-example-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.ref-model-card,
.ref-example-card {
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(0,0,0,0.18);
  padding: 1.35rem 1.2rem 1.25rem;
}
.ref-model-card h4,
.ref-example-card h4 {
  margin: 0;
  color: #fff3dd;
  text-transform: uppercase;
  letter-spacing: .08em;
  font-size: 1rem;
  line-height: 1.3;
}
.ref-model-card p,
.ref-example-card p {
  margin: .75rem 0 0;
  color: #d8cab8;
  font-size: .98rem;
  line-height: 1.72;
}
.ref-mini-list {
  list-style: none;
  padding: 0;
  margin: .95rem 0 0;
}
.ref-mini-list--wide {
  max-width: 58rem;
}
.ref-mini-list li {
  position: relative;
  padding-left: 1rem;
  color: #f3ebdf;
  font-size: .97rem;
  line-height: 1.62;
}
.ref-mini-list li + li {
  margin-top: .45rem;
}
.ref-mini-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: .65rem;
  width: 6px;
  height: 6px;
  background: #e2b24c;
  transform: rotate(45deg);
}
.ref-tool-grid {
  grid-template-columns: repeat(5, minmax(0, 1fr));
}
.ref-tool-pill {
  border: 1px solid rgba(226,178,76,0.24);
  background: rgba(255,255,255,0.03);
  color: #f7f0e4;
  padding: .9rem .85rem;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: .08em;
  font-size: .8rem;
  line-height: 1.4;
}
.ref-outcome-panel {
  display: grid;
  grid-template-columns: minmax(10rem, .34fr) minmax(0, 1fr);
  gap: 1.4rem;
  align-items: start;
  border: 1px solid rgba(226,178,76,0.2);
  background: linear-gradient(180deg, rgba(8,8,8,0.96), rgba(18,18,18,0.9));
  padding: 1.5rem 1.55rem;
}
.ref-outcome-label {
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .2em;
  font-size: .78rem;
  line-height: 1.45;
}
.ref-outcome-panel p {
  margin: 0;
  color: #f5ede2;
  font-size: 1.06rem;
  line-height: 1.82;
}
@media screen and (max-width: 1200px) {
  .ref-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media screen and (max-width: 767px) {
  .ref-service-link {
    width: 100%;
    justify-content: space-between;
  }
  .ref-gallery-section {
    padding: 8.25rem 0 4.75rem;
  }
  .ref-gallery-section > .container {
    width: min(100% - 2.2rem, 1280px);
  }
  .ref-detail-panel--intro,
  .ref-model-grid,
  .ref-tool-grid,
  .ref-example-grid,
  .ref-outcome-panel {
    grid-template-columns: 1fr;
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


def render_detail_sections(service):
    sections = []
    intro_paragraphs = service.get('detail_paragraphs', [])
    credentials = service.get('credentials', [])
    intro_kicker = service.get('detail_intro_kicker', 'How We Support')
    intro_heading = service.get('detail_intro_heading', 'Flexible, end-to-end project leadership built for mission-driven work')
    credential_kicker = service.get('credentials_kicker', 'Certifications')
    if intro_paragraphs or credentials:
        intro_copy = ''.join(f'<p>{html.escape(paragraph)}</p>' for paragraph in intro_paragraphs)
        credential_html = ''.join(f'<div class="ref-badge">{html.escape(item)}</div>' for item in credentials)
        sections.append(
            '<section class="ref-detail-panel ref-detail-panel--intro">'
            '<div>'
            f'<div class="ref-detail-kicker">{html.escape(intro_kicker)}</div>'
            f'<h3 class="ref-detail-heading">{html.escape(intro_heading)}</h3>'
            f'<div class="ref-detail-copy">{intro_copy}</div>'
            '</div>'
            '<div>'
            f'<div class="ref-detail-kicker">{html.escape(credential_kicker)}</div>'
            f'<div class="ref-badge-column">{credential_html}</div>'
            '</div>'
            '</section>'
        )
    service_steps = service.get('service_steps', [])
    if service_steps:
        steps_html = ''.join(f'<li>{html.escape(step)}</li>' for step in service_steps)
        sections.append(
            '<section class="ref-detail-panel">'
            f'<div class="ref-detail-kicker">{html.escape(service.get("service_steps_kicker", "What We Do"))}</div>'
            f'<h3 class="ref-detail-heading">{html.escape(service.get("service_steps_heading", "Proposal development support that keeps strategy, compliance, and submission on track"))}</h3>'
            f'<ul class="ref-mini-list ref-mini-list--wide">{steps_html}</ul>'
            '</section>'
        )
    case_studies = service.get('case_studies', [])
    if case_studies:
        case_html = ''.join(
            '<article class="ref-example-card">'
            f'<h4>{html.escape(example["title"])}</h4>'
            f'<p>{html.escape(example["summary"])}</p>'
            '</article>'
            for example in case_studies
        )
        sections.append(
            '<section class="ref-detail-panel">'
            f'<div class="ref-detail-kicker">{html.escape(service.get("case_studies_kicker", "Real-World Examples"))}</div>'
            f'<h3 class="ref-detail-heading">{html.escape(service.get("case_studies_heading", "Selected wins that show how E4 translates strategy into funded outcomes"))}</h3>'
            f'<div class="ref-example-grid">{case_html}</div>'
            '</section>'
        )
    models = service.get('engagement_models', [])
    if models:
        model_html = ''.join(
            '<article class="ref-model-card">'
            f'<h4>{html.escape(model["title"])}</h4>'
            f'<p>{html.escape(model["summary"])}</p>'
            f'<ul class="ref-mini-list">{"".join(f"<li>{html.escape(point)}</li>" for point in model["points"])}</ul>'
            '</article>'
            for model in models
        )
        sections.append(
            '<section class="ref-detail-panel">'
            '<div class="ref-detail-kicker">Engagement Models</div>'
            '<h3 class="ref-detail-heading">Support structured around how your organization needs to work</h3>'
            f'<div class="ref-model-grid">{model_html}</div>'
            '</section>'
        )
    tools = service.get('tools_used', [])
    if tools:
        tool_html = ''.join(f'<div class="ref-tool-pill">{html.escape(tool)}</div>' for tool in tools)
        sections.append(
            '<section class="ref-detail-panel">'
            '<div class="ref-detail-kicker">Tools Used</div>'
            '<h3 class="ref-detail-heading">Platforms that support planning, tracking, reporting, and execution visibility</h3>'
            f'<div class="ref-tool-grid">{tool_html}</div>'
            '</section>'
        )
    key_outcome = service.get('key_outcome')
    if key_outcome:
        sections.append(
            '<section class="ref-outcome-panel">'
            '<div class="ref-outcome-label">Key Outcome</div>'
            f'<p>{html.escape(key_outcome)}</p>'
            '</section>'
        )
    if not sections:
        return ''
    return f'<div class="ref-detail-stack">{"".join(sections)}</div>'


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
    service_lookup = {service['slug']: service for service in services}
    featured_service_slugs = [
        'grant-writing',
        'grant-management',
        'project-management',
        'readiness-assessments',
        'financial-management',
        'speaking-engagements',
        'it-app-development',
    ]
    service_sections = ''.join(
        build_service_section(service_lookup[slug])
        for slug in featured_service_slugs
        if slug in service_lookup
    )
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
    detail_extras = render_detail_sections(service)
    body = f'''<!-- Design philosophy: Reference-led service detail page. Each service page keeps the example’s editorial layout while moving directly from the hero into service-specific content. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">Service</div><h1 class="ref-heading-main">{html.escape(service['title'])}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">Meet the experts behind your success</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">Our expertise <span>Your advantage</span></h2><p class="ref-page-summary">{html.escape(service['detail_summary'])}</p></div><a class="ref-cta-button" href="/contact-us">Contact Us</a></div></div>{detail_extras}<div class="ref-bottom-copy">{html.escape(service['closing_copy'])}</div><div class="ref-bottom-links">{render_links(service['related_links'])}</div></div></section>
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
        'catalog_summary': 'E4 Power uses speaking engagements, workshops, and education-focused training to build knowledge, sharpen strategy, reinforce execution, and open trust-based institutional relationships.',
        'detail_summary': 'Led by Dr. Harold Lee III, E4 Power engages individuals and organizations through workshops, keynotes, and strategic training that strengthen leadership, workforce readiness, research development, and professional performance.',
        'detail_intro_kicker': 'Education & Training Services',
        'detail_intro_heading': 'Speaking, keynote, and workshop experiences that transfer knowledge, sharpen strategy, and create actionable momentum',
        'detail_paragraphs': [
            'Led by Dr. Harold Lee, E4 Power engages individuals and organizations through workshops that equip teams with practical skills, decision-making frameworks, and strategies that strengthen leadership, workforce readiness, and performance.',
            'The work educates clients on research and operational strategy development, grant development, and broader professional growth while helping organizations at every level—from administrators and researchers to senior leadership—move with greater clarity and confidence.',
        ],
        'credentials_kicker': 'Speaker Leadership',
        'credentials': ['Led by Harold Lee III, PhD', 'Keynotes, workshops, and panel facilitation', 'Research, grant, and professional development training'],
        'service_steps_kicker': 'What We Do',
        'service_steps_heading': 'Education and training services that help teams learn faster, lead better, and act with greater clarity',
        'service_steps': [
            'Full-cycle grant writing workshops',
            'Research and operational strategy training',
            'Partnership development sessions',
            'Professional development',
            'Keynote speeches & panel appearances',
            'National security updates',
            'Emerging technology updates',
        ],
        'case_studies_kicker': 'Real-World Examples',
        'case_studies_heading': 'Selected speaking and workshop engagements that turned thought leadership into practical institutional value',
        'case_studies': [
            {
                'title': 'UVI School of Business Mini Retreat',
                'summary': 'Delivered retreat-based speaking and workshop content for the University of the Virgin Islands School of Business, connecting practical grant strategy, professional growth, and institutional readiness.',
            },
            {
                'title': 'From Idea to Award Grant Development Workshop',
                'summary': 'Facilitated grant-development sessions and lunch-and-learn programming that helped researchers move from early concepts to stronger, more competitive proposal framing.',
            },
            {
                'title': 'Conference & National Opportunity Briefings',
                'summary': 'Presented thought-leadership sessions on topics including national security, research opportunity positioning, and career pathways across conference and campus audiences.',
            },
        ],
        'engagement_models': [
            {
                'title': 'Educate',
                'summary': 'We offer talks, keynotes, and workshops designed to transfer knowledge, train teams, and introduce new language around innovation and grants through hands-on learning that increases understanding, knowledge, and confidence.',
                'points': ['Conference keynotes', 'Learning-centered sessions', 'Team readiness framing', 'Grant-writing workshops', 'Team learning cohorts', 'Capacity-building sessions'],
            },
            {
                'title': 'Empower',
                'summary': 'We use speaking engagements as a strategic catalyst that helps leaders see competitive opportunities, define organizational next steps, and turn training into momentum through opportunity-centered and readiness-building sessions.',
                'points': ['Executive briefings', 'Opportunity framing', 'Strategic positioning', 'Proposal strategy labs', 'Innovation workshops', 'Readiness acceleration'],
            },
            {
                'title': 'Elevate',
                'summary': 'We translate ideas into action by leveraging speaking engagements to reinforce implementation discipline, institutional accountability, and the execution habits that make strategy operational.',
                'points': ['Execution-minded messaging', 'Operational clarity', 'Action-oriented summaries', 'Compliance training', 'Delivery workflows', 'Execution support routines'],
            },
            {
                'title': 'Engage',
                'summary': 'We use visible thought leadership to open new relationships, establish trust before deeper consulting begins, and create a collaborative entry point through workshops that align stakeholders ahead of larger engagements.',
                'points': ['Relationship-first introductions', 'Advisory entry point', 'Trust-building presence', 'Cross-team sessions', 'Partnership-building facilitation', 'Stakeholder alignment'],
            },
        ],
        'key_outcome': 'Institutions and individual researchers gain practical, actionable skills they can apply immediately—sharpening their competitive edge, improving future proposal readiness, and building more confident teams and leaders.',
        'closing_copy': 'Speaking Engagements is especially effective when E4 Power needs to shape the room early, build trust quickly, and create a pathway into broader workshops, advisory work, grant development, or operational support.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use talks, keynotes, and workshops to transfer knowledge, train teams, and introduce new language around innovation, grants, and professional growth.', 'points': ['Conference keynotes', 'Learning-centered sessions', 'Team readiness framing'], 'image': '/manus-storage/SpeakingEngagementsEducate_c4effd85.jpg'},
            'Empower': {'note': 'Position speaking as a strategic catalyst that helps leaders see opportunities, define next steps, and strengthen competitive readiness.', 'points': ['Executive briefings', 'Opportunity framing', 'Strategic positioning'], 'image': '/manus-storage/SpeakingEngagementsEmpower_3fc5583d.jpg'},
            'Elevate': {'note': 'Translate ideas into action by using speaking engagements to reinforce implementation discipline, operational clarity, and institutional accountability.', 'points': ['Execution-minded messaging', 'Operational clarity', 'Action-oriented summaries'], 'image': '/manus-storage/SpeakingEngagementsElevate_18d2199e.jpg'},
            'Engage': {'note': 'Open new relationships through visible thought leadership that establishes trust before deeper consulting or larger engagements begin.', 'points': ['Relationship-first introductions', 'Advisory entry point', 'Trust-building presence'], 'image': '/manus-storage/SpeakingEngagementsEngage_85977d11.jpg'},
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
        'title': 'Grant Writing (Pre-Award)',
        'catalog_summary': 'Grant Writing should appear as a single named service with pillar-specific value cards underneath it, not as one item inside only Empower.',
        'detail_summary': 'E4 Power’s pre-award team guides institutions through every stage of proposal development—from opportunity identification to on-time submission—while helping clients compete more effectively across federal and foundation funding environments.',
        'detail_intro_kicker': 'Pre-Award Support',
        'detail_intro_heading': 'Proposal development support from opportunity identification to on-time submission',
        'detail_paragraphs': [
            'E4 Power’s pre-award team guides institutions through every stage of proposal development—from opportunity identification to on-time submission, with a 78% success rate across NSF, DoD, DoE, DoEd, and DoL.',
        ],
        'credentials_kicker': 'Performance Snapshot',
        'credentials': ['78% success rate across NSF, DoD, DoE, DoEd, and DoL'],
        'service_steps': [
            'Funding opportunity identification & alignment',
            'Needs assessment & feasibility analysis',
            'Proposal narrative development',
            'Budget creation & justification',
            'Letters of support coordination',
            'Internal review & compliance check',
            'Final submission & follow-up',
        ],
        'case_studies': [
            {
                'title': 'NSF HBCU-UP Implementation',
                'summary': 'Developed a $2M proposal for the UMES STEM program that was funded on first submission after more than 20 years without an NSF award.',
            },
            {
                'title': 'EPA Biogenic Building Materials',
                'summary': 'Led a $6.1M EPA proposal enabling robust EPDs for biogenic building materials with PI Jacob Waddell.',
            },
            {
                'title': 'Costco Foundation',
                'summary': 'Secured $140,000 for Mentor Washington to strengthen statewide mentorship program monitoring and impact tracking.',
            },
        ],
        'key_outcome': 'Clients gain compelling, submission-ready grant proposals backed by subject-matter experts, tailored narratives, and airtight budgets—maximizing award probability from the very first submission.',
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
        'detail_summary': 'E4 Power uses Readiness Assessments to give institutions a clear, evidence-based picture of current strengths, gaps, and next-step opportunities before larger research, grant, or infrastructure investments begin.',
        'detail_intro_kicker': 'Assessment & Strategy Support',
        'detail_intro_heading': 'Institutional readiness diagnostics that turn uncertainty into a prioritized growth roadmap',
        'detail_paragraphs': [
            'Our Readiness Assessments help institutions understand where they are today, what is holding them back, and what must be strengthened to compete more effectively for major opportunities.',
            'The work combines infrastructure review, compliance analysis, capacity benchmarking, and strategic mapping so leaders can move forward with a more honest baseline and a more actionable plan.',
        ],
        'credentials_kicker': 'Assessment Lenses',
        'credentials': ['SWOT analysis', 'P.I.C.K. opportunity mapping', 'Compliance and capacity review'],
        'service_steps_kicker': 'What We Do',
        'service_steps_heading': 'A structured review of institutional strength, research capacity, and funding readiness',
        'service_steps': [
            'Organizational SWOT analysis',
            'Research infrastructure capacity review',
            'Grant readiness & compliance gap analysis',
            'Faculty & staff capacity benchmarking',
            'Strategic opportunity mapping (P.I.C.K.)',
            'Funding eligibility screening',
            'Custom institutional growth roadmap',
            'Short-, mid-, and long-term research strategy development',
            'Research readiness assessments',
        ],
        'case_studies_kicker': 'Real-World Examples',
        'case_studies_heading': 'Representative readiness engagements that clarified gaps, surfaced savings, and created stronger funding pathways',
        'case_studies': [
            {
                'title': 'HBCU Institutional Audit',
                'summary': 'A comprehensive infrastructure and compliance assessment identified more than $120K in administrative savings and surfaced three high-probability funding pathways.',
            },
            {
                'title': 'BRIDGE Program Onboarding Review',
                'summary': 'Delivered a readiness assessment as the first step of the BRIDGE model for new university partners, establishing the baseline for research infrastructure growth.',
            },
        ],
        'key_outcome': 'Institutions gain a clear, honest picture of current strengths and gaps—along with a prioritized, actionable roadmap for building the infrastructure needed to compete for and win major awards.',
        'closing_copy': 'Readiness Assessments are most valuable when an institution needs more than a snapshot; it needs a grounded diagnosis, a practical sequence of next moves, and a roadmap for stronger long-term competitiveness.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Use the assessment to teach teams where capacity gaps exist and what internal development should happen next.', 'points': ['Capability awareness', 'Learning priorities', 'Readiness education'], 'image': '/manus-storage/readiness-assessments-educate_8cfcac33.jpg'},
            'Empower': {'note': 'Clarify the strategic path forward by identifying where competitiveness and growth can be strengthened.', 'points': ['Gap identification', 'Infrastructure mapping', 'Priority sequencing'], 'image': '/manus-storage/readiness-assessments-empower_45928b64.jpg'},
            'Elevate': {'note': 'Translate findings into better execution systems, accountability, and operational sequencing.', 'points': ['Execution baseline', 'Workflow visibility', 'Delivery planning'], 'image': '/manus-storage/readiness-assessments-elevate_fdd3c036.jpg'},
            'Engage': {'note': 'Use assessments as an advisory entry service that creates clarity before larger commitments are made.', 'points': ['Discovery-led onboarding', 'Trust-building diagnosis', 'Relationship-fit review'], 'image': '/manus-storage/readiness-assessments-engage_a98215f4.jpg'},
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
        'title': 'Grant Management (Post-Award)',
        'catalog_summary': 'E4 Power provides post-award grant management that keeps institutions compliant, coordinated, and audit-ready from award acceptance through project closeout.',
        'detail_summary': 'Winning a grant is only the beginning. E4 Power’s post-award team supports the full grant lifecycle—from award acceptance and kickoff through compliance monitoring, reporting, modifications, and closeout.',
        'detail_intro_kicker': 'Post-Award Services',
        'detail_intro_heading': 'Full-lifecycle grant stewardship that protects funding relationships and strengthens institutional credibility',
        'detail_paragraphs': [
            'E4 Power’s post-award support helps institutions manage the operational reality of funded work after the proposal is approved, ensuring that schedules, reports, compliance obligations, and sponsor expectations stay on track.',
            'The focus is not only on keeping awards active, but on building the discipline, visibility, and funder confidence needed to preserve long-term funding relationships and position organizations for future opportunities.',
        ],
        'credentials_kicker': 'Post-Award Leadership',
        'credentials': ['Led by Tamara Henry, PMP', 'Federal post-award compliance oversight', 'Lifecycle coordination from kickoff through closeout'],
        'service_steps_kicker': 'What We Do',
        'service_steps_heading': 'Post-award management support from kickoff to closeout',
        'service_steps': [
            'Award acceptance & kickoff administration',
            'Milestone tracking & schedule management',
            'Federal compliance monitoring (2 CFR 200)',
            'Progress & technical report preparation',
            'No-cost extension & modification requests',
            'Sub-award & subcontract management',
            'Project closeout & lessons learned',
        ],
        'case_studies_kicker': 'Real-World Examples',
        'case_studies_heading': 'Selected examples that show how E4 Power protects award performance after funding is secured',
        'case_studies': [
            {
                'title': 'NSF HBCU UJIMA Collective',
                'summary': 'Managed post-award compliance and reporting for a $3M NSF collaborative research initiative across multiple HBCU partners.',
            },
            {
                'title': 'SBIR STEM-I-Am Material Science',
                'summary': 'Coordinated award management and technical deliverables for a $300K SBIR Phase I award with PI Dr. David.',
            },
        ],
        'key_outcome': 'Institutions remain audit-ready and compliant throughout the award period, protecting sponsor relationships and creating stronger positioning for follow-on awards.',
        'closing_copy': 'Grant Management becomes one of E4 Power’s most valuable post-award services because it protects funded work after the win, reduces administrative strain, and helps clients sustain trust with federal sponsors over time.',
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
        'catalog_summary': 'E4 provides flexible, end-to-end project management support designed to engage stakeholders, educate teams, elevate execution, and empower organizations to sustain impact.',
        'detail_summary': 'E4 provides flexible, end-to-end project management support for nonprofits, universities, and community-based organizations that need structure, alignment, and execution support across complex or mission-driven work.',
        'detail_paragraphs': [
            'We partner with nonprofits, universities, and community-based organizations to plan, manage, and strengthen projects—especially those that are grant-funded, multi-stakeholder, or mission-driven.',
            'Our work often includes strategic assessments such as SWOT analyses and the design of process improvement initiatives so projects are not only delivered, but delivered more effectively over time.',
            'We understand the balance required between compliance, accountability, and real-world impact, and we build systems that actually work in practice, not just on paper.',
            'Our approach goes beyond managing tasks. We create structure, clarity, and alignment while strengthening internal capacity, so organizations are not only successful in the moment, but more confident and equipped for what comes next.',
        ],
        'credentials': ['PMP Certified', 'SAFe Scrum Master Certified', 'Lean & Six Sigma Certified'],
        'engagement_models': [
            {
                'title': 'Short-Term Engagements',
                'summary': 'Targeted support for immediate or high-priority needs.',
                'points': ['Project startup and planning (charter, scope, and work planning)', 'Project recovery or stabilization', 'Support for specific initiatives or grant-funded projects'],
            },
            {
                'title': 'Long-Term Engagements',
                'summary': 'Ongoing partnership to manage and sustain complex work.',
                'points': ['End-to-end project management and oversight', 'Multi-phase or multi-year initiative management', 'Embedded or fractional project management support'],
            },
            {
                'title': 'Capacity-Building Engagements',
                'summary': 'Support that strengthens internal teams and systems over time.',
                'points': ['Project management training and coaching', 'Development of internal tools, templates, and workflows', 'Support to build sustainable project management practices'],
            },
        ],
        'tools_used': ['Smartsheet', 'MS Project', 'Notion', 'Monday', 'Excel', 'AppSheet'],
        'closing_copy': 'Project Management is most valuable when organizations need more than coordination alone and want a partner who can build structure, strengthen execution, and leave behind systems their teams can sustain.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'Build knowledge and strengthen internal capacity. We educate teams so they can confidently manage projects and sustain success beyond our engagement.', 'points': ['Project management training (foundational and advanced)', 'Time management and productivity training', 'Tools and systems training (planning, tracking, and reporting)'], 'image': '/manus-storage/project-management-educate_464d8e84.jpg'},
            'Empower': {'note': 'Enable organizations to lead, adapt, and sustain impact. We empower organizations by equipping teams with the tools, systems, and confidence to independently manage and grow their work.', 'points': ['SWOT analysis to assess organizational and project positioning', 'Process improvement initiatives to enhance efficiency and effectiveness', 'Development of project management frameworks, playbooks, and documentation'], 'image': '/manus-storage/project-management-empower_c9414cbd.jpg'},
            'Elevate': {'note': 'Strengthen execution through structure, tools, and accountability. We elevate project performance by introducing clear processes, proactive planning, and data-driven tracking.', 'points': ['Development of detailed work plans (schedule management and milestone tracking)', 'Risk identification and mitigation planning', 'Performance metrics and KPI reporting'], 'image': '/manus-storage/project-management-elevate_0a1e56d2.jpg'},
            'Engage': {'note': 'Establish clarity, alignment, and shared direction. We engage organizations by building strong project foundations and ensuring stakeholders are aligned from the start.', 'points': ['Project charter and scope definition', 'Stakeholder communication planning', 'Procurement and vendor coordination'], 'image': '/manus-storage/project-management-engage_01ca1dc3.jpg'},
        },
    },
    {
        'slug': 'financial-management',
        'title': 'Financial Management',
        'catalog_summary': 'Financial Management should sit as one named service with four supporting pillar cards beneath it, rather than as only an Elevate item.',
        'detail_summary': 'E4 Power’s Financial Operations and Management Division helps organizations strengthen financial infrastructure, improve operational efficiency, maintain compliance, and support long-term growth through strategic financial support and operational oversight.',
        'detail_intro_kicker': 'Building Financial Infrastructure for Sustainable Growth',
        'detail_intro_heading': 'Structured financial support that helps organizations operate with clarity, accountability, and confidence',
        'detail_paragraphs': [
            'From financial setup and budgeting to compliance management and strategic advisory, E4 Power provides the structure and guidance organizations need to operate with confidence.',
            'The broader division framework is designed as a comprehensive financial operations ecosystem that combines infrastructure development, operational financial management, compliance oversight, revenue support, strategic advisory, and financial education for institutions, nonprofits, businesses, and grant-funded programs.',
        ],
        'credentials_kicker': 'Division Structure',
        'credentials': ['Division 1: Financial Infrastructure and Setup', 'Division 2: Financial Operations and Revenue Management', 'Division 3: Compliance and Grant Financial Oversight', 'Division 4: Financial Strategy and Advisory'],
        'service_steps_kicker': '4 E’s of Financial Management',
        'service_steps_heading': 'Financial Management organized through Educate, Empower, Engage, and Elevate',
        'service_steps': [
            'Educate: Financial workshops, budget development training, grant financial education, financial operations training, and compliance education.',
            'Empower: Financial system setup, accounting infrastructure, revenue cycle support, billing process optimization, and financial workflow development.',
            'Engage: Monthly financial operations, compliance management, grant and budget financial oversight, audit readiness, and financial reporting support.',
            'Elevate: CFO advisory services, budget oversight, cash flow planning, financial forecasting, and strategic financial guidance.',
        ],
        'engagement_models': [
            {
                'title': 'Financial Infrastructure and Setup',
                'summary': 'Foundational support that helps organizations build the right structure before growth accelerates.',
                'points': ['Nonprofit and LLC formation support', 'EIN, SAM.gov, UEI, and business registration assistance', 'Accounting system setup, QuickBooks setup, and chart-of-accounts design'],
            },
            {
                'title': 'Financial Operations and Revenue Management',
                'summary': 'Ongoing operational support that keeps reporting, billing, and revenue processes organized and visible.',
                'points': ['Monthly bookkeeping and reconciliations', 'Accounts payable, accounts receivable, and invoice management', 'Payroll processing, contractor support, and monthly financial reporting'],
            },
            {
                'title': 'Compliance and Grant Financial Oversight',
                'summary': 'Compliance-centered financial management that strengthens accountability and reduces grant-related risk.',
                'points': ['Grant financial tracking and post-award oversight', 'Cost allowability review and audit preparation', 'Sub-recipient monitoring, reporting support, and compliance assessments'],
            },
            {
                'title': 'Financial Strategy and Advisory',
                'summary': 'Strategic guidance that helps organizations improve performance and plan for long-term sustainability.',
                'points': ['Cash flow planning and revenue goal setting', 'Budget development, forecasting, and KPI analysis', 'Pricing guidance, owner compensation strategy, and CFO advisory'],
            },
        ],
        'tools_used': ['QuickBooks', 'Financial Reporting Systems', 'Budget Oversight Workflows', 'Revenue Cycle Processes', 'Compliance Review Frameworks', 'CFO Advisory Reviews'],
        'key_outcome': 'Organizations gain stronger financial infrastructure, clearer reporting, better compliance discipline, and the strategic guidance needed to manage growth with confidence.',
        'closing_copy': 'Financial Management reinforces E4 Power’s role as a long-term operational partner by combining education, infrastructure, compliance support, and strategic advisory into one scalable financial ecosystem.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Contact Us', '/contact-us')],
        'pillars': {
            'Educate': {'note': 'We equip organizations with the financial knowledge, training, and operational education needed to strengthen financial understanding and improve decision-making.', 'points': ['Financial workshops', 'Budget development training', 'Grant financial education'], 'image': '/manus-storage/financial-management-educate-v2_76674b6b.jpg'},
            'Empower': {'note': 'We help organizations build strong financial systems, operational workflows, and scalable financial infrastructure that support accountability and long-term stability.', 'points': ['Financial system setup', 'Accounting infrastructure', 'Revenue cycle support'], 'image': '/manus-storage/financial-management-empower_442d9b13.jpg'},
            'Elevate': {'note': 'We provide strategic financial insight and advisory support that helps organizations strengthen financial performance, improve visibility, and plan for sustainable growth.', 'points': ['CFO advisory services', 'Cash flow planning', 'Financial forecasting'], 'image': '/manus-storage/financial-management-elevate_835b074e.jpg'},
            'Engage': {'note': 'We work alongside organizations through ongoing financial management, compliance oversight, and operational support to maintain accountability and operational consistency.', 'points': ['Monthly financial operations', 'Audit readiness', 'Financial reporting support'], 'image': '/manus-storage/financial-management-engage-v2_2b7701b5.jpg'},
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
            'Empower': {'note': 'Turn early conversations into clearer strategic direction and more deliberate opportunity choices.', 'points': ['Needs clarification', 'Goal framing', 'Roadmap direction'], 'image': '/manus-storage/institutional-discovery-empower-v2_aede0af7.jpeg'},
            'Elevate': {'note': 'Use discovery findings to shape more realistic operational plans and execution sequencing.', 'points': ['Execution baseline', 'Constraint mapping', 'Delivery readiness'], 'image': '/manus-storage/institutional-discovery-elevate-v2_ab07840a.jpg'},
            'Engage': {'note': 'Lead with trust, listening, and fit so the relationship begins with clarity rather than assumption.', 'points': ['Discovery meetings', 'Advisory entry point', 'Relationship-fit assessment'], 'image': '/manus-storage/institutional-discovery-engage-v2_c8bc48de.jpg'},
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
            'Empower': {'note': 'Clarify the strategic path by aligning leaders, specialists, and priorities before work accelerates.', 'points': ['Decision-maker alignment', 'Specialist matching', 'Strategic clarity'], 'image': '/manus-storage/advisory-alignment-empower-v2_987b7c4d.jpg'},
            'Elevate': {'note': 'Translate alignment into an actionable engagement model with clear responsibilities and momentum.', 'points': ['Action launch planning', 'Working-model definition', 'Operational checkpoints'], 'image': '/manus-storage/advisory-alignment-elevate_d42572ca.jpg'},
            'Engage': {'note': 'Use alignment as the partnership bridge that turns a first conversation into a durable advisory relationship.', 'points': ['Trust-building follow-through', 'Partnership structure', 'Collaborative planning'], 'image': '/manus-storage/advisory-alignment-engage-v2_0e9aea2b.jpg'},
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
            {'title': 'Grant Writing (Pre-Award)', 'label': 'Empower', 'note': 'Proposal strategy and submission support with competitive focus.', 'points': ['Opportunity scans', 'Narrative development', 'Submission support'], 'placeholder': 'Grant Writing'},
            {'title': 'Financial Management', 'label': 'Empower', 'note': 'Financial strategy that helps organizations connect opportunity ambition to practical stewardship.', 'points': ['Funding-readiness framing', 'Budget strategy', 'Financial decision support'], 'placeholder': 'Financial Management'},
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
            {'title': 'Grant Management (Post-Award)', 'label': 'Elevate', 'note': 'Post-award stewardship that protects credibility and momentum.', 'points': ['Reporting coordination', 'Compliance oversight', 'Award closeout support'], 'placeholder': 'Grant Management'},
            {'title': 'Project Management', 'label': 'Elevate', 'note': 'Execution systems that keep complex initiatives coordinated while strengthening accountability and internal delivery discipline.', 'points': ['Detailed work plans', 'Risk mitigation planning', 'KPI reporting'], 'placeholder': 'Project Management'},
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
