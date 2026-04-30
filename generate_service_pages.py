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
GOLD = '#e2b24c'

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
  max-width: 34rem;
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
  font-size: clamp(3.8rem, 7vw, 5.8rem);
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
.ref-grid {
  margin-top: 3.25rem;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 2.2rem 1.5rem;
}
.ref-card {
  display: flex;
  flex-direction: column;
}
.ref-card-media {
  aspect-ratio: 3 / 4.35;
  background-size: cover;
  background-position: center;
  border: 1px solid rgba(255,255,255,0.06);
  filter: grayscale(1);
  box-shadow: 0 16px 40px rgba(0,0,0,0.26);
}
.ref-card-titleband {
  background: #fff;
  color: #121212;
  text-transform: uppercase;
  letter-spacing: .22em;
  font-size: 1rem;
  text-align: center;
  padding: 1rem .8rem;
}
.ref-card-note {
  color: #d8cab8;
  font-size: 1rem;
  line-height: 1.75;
  margin: 1rem 0 0;
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

pages = {
    'services': {
        'title': 'Services | E4 Power',
        'accent_word': 'All',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'The Services Hub organizes E4 Power’s broader capability stack into a single visual index so visitors can understand the firm’s advisory, training, post-award, digital, and partnership support at a glance.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {
                'title': 'Pre-Award Strategy',
                'note': 'Opportunity and proposal support before submission.',
                'placeholder': 'Pre-Award',
                'points': ['Opportunity identification', 'Proposal development support', 'Competitive positioning reviews']
            },
            {
                'title': 'Workshops & Speaking',
                'note': 'Training-led learning systems for faculty and teams.',
                'placeholder': 'Workshops',
                'points': ['Leadership talks and keynotes', 'Grant-writing workshops', 'Technology literacy sessions']
            },
            {
                'title': 'Project Management',
                'note': 'Execution structures for funded initiatives.',
                'placeholder': 'Project Mgmt',
                'points': ['Risk-aware delivery planning', 'Cross-team coordination', 'Milestone accountability']
            },
            {
                'title': 'Readiness Assessments',
                'note': 'Discovery work that clarifies where to begin.',
                'placeholder': 'Readiness',
                'points': ['Baseline reviews', 'Infrastructure mapping', 'Growth prioritization']
            },
            {
                'title': 'Intellectual Property',
                'note': 'Innovation protection and commercialization support.',
                'placeholder': 'IP Strategy',
                'points': ['Patent strategy guidance', 'IP education for teams', 'Commercialization positioning']
            },
            {
                'title': 'Financial Management',
                'note': 'Fiscal stewardship aligned with federal expectations.',
                'placeholder': 'Financial',
                'points': ['Budget oversight', 'Allowable cost tracking', 'Audit-conscious controls']
            },
            {
                'title': 'IT & App Development',
                'note': 'Custom digital infrastructure for institutional growth.',
                'placeholder': 'Digital Build',
                'points': ['Custom portals', 'Web apps and websites', 'Ongoing IT support']
            },
            {
                'title': 'Partnership Entry',
                'note': 'Relationship-led onboarding and advisory alignment.',
                'placeholder': 'Partnership',
                'points': ['Discovery meetings', 'Readiness-led onboarding', 'Collaborative planning']
            },
        ],
        'closing_copy': 'Use this page as the broadest capability entry point, then route visitors into Educate, Empower, Elevate, and Engage for a more focused explanation of how each service cluster shows up within the E4 Power model.',
        'secondary_links': [('Educate', '/educate/'), ('Empower', '/empower/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
    },
    'educate': {
        'title': 'Educate | E4 Power',
        'accent_word': 'Educate',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Educate is the training-facing pillar. This page presents the learning, speaking, and capacity-building offers in a tighter visual format that mirrors the provided reference while preserving the E4 Power brand tone.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {
                'title': 'Speaking Engagements',
                'note': 'High-value talks for institutional audiences and leadership teams.',
                'placeholder': 'Speaking',
                'points': ['Keynotes and plenaries', 'Leadership motivation', 'Strategic briefings']
            },
            {
                'title': 'Workshops',
                'note': 'Structured learning programs that build team readiness.',
                'placeholder': 'Workshops',
                'points': ['Grant writing', 'Proposal review', 'Research strategy']
            },
            {
                'title': 'Technology & AI Literacy',
                'note': 'Education-led framing for digital change and AI adoption.',
                'placeholder': 'AI Literacy',
                'points': ['AI readiness conversations', 'Workflow education', 'Innovation translation']
            },
            {
                'title': 'Leadership Development',
                'note': 'Practical capacity-building for internal advancement and confidence.',
                'placeholder': 'Leadership',
                'points': ['Career development support', 'Team capacity building', 'Leadership readiness']
            },
        ],
        'closing_copy': 'Use Educate when the audience needs practical learning before deeper consulting support, especially where grant readiness, workshop delivery, and leadership capacity intersect.',
        'secondary_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
    },
    'empower': {
        'title': 'Empower | E4 Power',
        'accent_word': 'Empower',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Empower is the competitive and technology-forward pillar. The layout here follows the reference composition while highlighting proposal strategy, innovation support, and the newly added IT and application-development service tier.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {
                'title': 'Grant Writing',
                'note': 'Proposal-development support from idea to submission.',
                'placeholder': 'Grant Writing',
                'points': ['Opportunity scans', 'Proposal writing', 'Submission support']
            },
            {
                'title': 'Readiness Assessments',
                'note': 'Institutional reviews that clarify fundable next moves.',
                'placeholder': 'Readiness',
                'points': ['SWOT analysis', 'Infrastructure review', 'Strategic implementation baseline']
            },
            {
                'title': 'Intellectual Property',
                'note': 'Protection and commercialization support for research assets.',
                'placeholder': 'IP Support',
                'points': ['Patent guidance', 'Researcher education', 'Commercialization positioning']
            },
            {
                'title': 'IT & Application Development',
                'note': 'Custom digital delivery that extends strategy into infrastructure.',
                'placeholder': 'App Development',
                'points': ['Custom portals', 'Web apps and websites', 'IT support']
            },
        ],
        'closing_copy': 'Use Empower when prospects want to understand how E4 Power improves competitiveness before award, especially where proposal strategy, innovation support, and digital build intersect.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Elevate', '/elevate/'), ('Engage', '/engage/')],
    },
    'elevate': {
        'title': 'Elevate | E4 Power',
        'accent_word': 'Elevate',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Elevate turns the narrative toward execution, stewardship, and measurable delivery. The breakout page now uses the reference card system to present post-award and operational services in a more editorial format.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {
                'title': 'Grant Management',
                'note': 'Post-award support that protects agency relationships.',
                'placeholder': 'Grant Mgmt',
                'points': ['Reporting coordination', 'Compliance oversight', 'Award closeout']
            },
            {
                'title': 'Project Management',
                'note': 'Structured systems for complex initiative delivery.',
                'placeholder': 'Project Delivery',
                'points': ['Timeline management', 'Cross-team execution', 'Risk-aware coordination']
            },
            {
                'title': 'Financial Management',
                'note': 'Fiscal oversight aligned with federal expectations.',
                'placeholder': 'Financial',
                'points': ['Drawdown support', 'Cost tracking', 'Audit-conscious stewardship']
            },
            {
                'title': 'IT Support Continuity',
                'note': 'Operational continuity for launched digital systems.',
                'placeholder': 'IT Support',
                'points': ['Support workflows', 'Maintenance guidance', 'Operational continuity']
            },
        ],
        'closing_copy': 'Use Elevate when visitors need confidence that E4 Power can protect awarded work, coordinate teams, sustain operations, and deliver outcomes responsibly after funding or launch.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Empower', '/empower/'), ('Engage', '/engage/')],
    },
    'engage': {
        'title': 'Engage | E4 Power',
        'accent_word': 'Engage',
        'main_word': 'Services',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Engage is the partnership-entry pillar. The page now uses the same visual system as the reference to frame readiness, discovery, and relationship-led onboarding in a tighter, more intentional layout.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {
                'title': 'Institutional Discovery',
                'note': 'Early conversations that clarify goals and fit.',
                'placeholder': 'Discovery',
                'points': ['Discovery meetings', 'Needs clarification', 'Initial roadmapping']
            },
            {
                'title': 'Readiness-Led Onboarding',
                'note': 'A practical baseline for future workstreams.',
                'placeholder': 'Onboarding',
                'points': ['Baseline review', 'Gap identification', 'Priority sequencing']
            },
            {
                'title': 'Team-Led Partnership Model',
                'note': 'Specialist alignment built around client goals.',
                'placeholder': 'Partnership',
                'points': ['Executive introductions', 'Specialist alignment', 'Collaborative planning']
            },
            {
                'title': 'Advisory Alignment',
                'note': 'The bridge between trust-building and execution planning.',
                'placeholder': 'Advisory',
                'points': ['Partnership-fit review', 'Decision-maker alignment', 'Next-step planning']
            },
        ],
        'closing_copy': 'Use Engage when prospects want to understand the people, the advisory model, and how a thoughtful partnership with E4 Power begins before deeper execution starts.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Empower', '/empower/'), ('Elevate', '/elevate/')],
    },
}


ICON = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0 16 8 8 16 0 8Z"></path></svg>'


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
    <text x="146" y="1090" font-family="Arial, Helvetica, sans-serif" font-size="78" font-weight="700" letter-spacing="8" fill="#1f1f1f">{safe}</text>
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
        media = placeholder_svg(card['placeholder'])
        note = f'<p class="ref-card-note">{html.escape(card["note"])}</p>' if card.get('note') else ''
        items.append(
            f'<article class="ref-card"><div class="ref-card-media" style="background-image:url(\'{media}\')"></div><div class="ref-card-titleband">{html.escape(card["title"])}</div>{note}<ul class="ref-point-list">{render_points(card["points"])}</ul></article>'
        )
    return ''.join(items)


def render_links(links):
    items = []
    for idx, (label, href) in enumerate(links):
        cls = 'ref-secondary-link primary' if idx == 0 else 'ref-secondary-link'
        items.append(f'<a class="{cls}" href="{href}">{html.escape(label)}</a>')
    return ''.join(items)


for slug, page in pages.items():
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{page["title"]}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    body = f'''<!-- Design philosophy: Reference-led service gallery. Mirror the provided sample through an editorial header, dark brown canvas, gold accents, white title bands, and image-led service cards with compact feature lists. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">{html.escape(page['accent_word'])}</div><h1 class="ref-heading-main">{html.escape(page['main_word'])}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">{html.escape(page['overline'])}</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">{page['subtitle']}</h2><p class="ref-page-summary">{html.escape(page['summary'])}</p></div><a class="ref-cta-button" href="{page['button_href']}">{html.escape(page['button_label'])}</a></div></div><div class="ref-grid">{render_cards(page['cards'])}</div><div class="ref-bottom-copy">{html.escape(page['closing_copy'])}</div><div class="ref-bottom-links">{render_links(page['secondary_links'])}</div></div></section>
{shared_footer}'''
    out_dir = BASE / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')
