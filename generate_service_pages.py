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
  max-width: 40rem;
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
.ref-grid {
  margin-top: 3.25rem;
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
  box-shadow: 0 16px 40px rgba(0,0,0,0.26);
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
    <text x="146" y="1090" font-family="Arial, Helvetica, sans-serif" font-size="68" font-weight="700" letter-spacing="6" fill="#1f1f1f">{safe}</text>
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
        media = placeholder_svg(card.get('placeholder', card['title']))
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


def write_page(relative_dir, title, accent_word, main_word, overline, subtitle, summary, button_label, button_href, cards, closing_copy, secondary_links):
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{html.escape(title)}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    body = f'''<!-- Design philosophy: Reference-led service gallery. Mirror the provided sample through an editorial header, dark brown canvas, gold accents, white title bands, and image-led service cards with compact feature lists. -->
{page_head}<body class="body ref-page-shell">{nav_html}
<section class="ref-gallery-section"><div class="container"><div class="ref-top-block"><div class="ref-heading-stack"><div class="ref-heading-accent">{html.escape(accent_word)}</div><h1 class="ref-heading-main">{html.escape(main_word)}</h1></div><div class="ref-meta-row"><div class="ref-divider-wrap"><div class="ref-divider"></div><div class="ref-overline">{html.escape(overline)}</div></div><img class="ref-mark" alt="E4 Power logo" src="{E4_LOGO}"/></div><div class="ref-subhead-row"><div><h2 class="ref-subtitle">{subtitle}</h2><p class="ref-page-summary">{html.escape(summary)}</p></div><a class="ref-cta-button" href="{button_href}">{html.escape(button_label)}</a></div></div><div class="ref-grid">{render_cards(cards)}</div><div class="ref-bottom-copy">{html.escape(closing_copy)}</div><div class="ref-bottom-links">{render_links(secondary_links)}</div></div></section>
{shared_footer}'''
    out_dir = BASE / relative_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')


service_details = [
    {
        'slug': 'speaking-engagements',
        'title': 'Speaking Engagements',
        'accent_word': 'Educate',
        'main_word': 'Speaking Engagements',
        'pillar': 'Educate',
        'hub_note': 'Executive keynotes and strategic talks for mission-driven institutions.',
        'placeholder': 'Speaking',
        'hub_points': ['Conference keynotes', 'Executive briefings', 'Mission-aligned thought leadership'],
        'summary': 'Speaking Engagements gives leaders a high-trust way to introduce E4 Power’s perspective on strategy, innovation, grants, and institutional growth in rooms where influence matters.',
        'detail_cards': [
            {'title': 'Keynotes', 'label': 'Audience Format', 'note': 'High-energy framing for conferences, summits, and leadership gatherings.', 'placeholder': 'Keynote', 'points': ['Signature conference talks', 'Opening and closing keynotes', 'Sector-informed messaging']},
            {'title': 'Leadership Briefings', 'label': 'Executive Use', 'note': 'Strategic presentations built for presidents, provosts, boards, and executive teams.', 'placeholder': 'Briefing', 'points': ['Board-level conversations', 'Executive planning sessions', 'Challenge framing for decision-makers']},
            {'title': 'Custom Themes', 'label': 'Content Direction', 'note': 'Sessions tuned to grants, innovation, AI readiness, or institutional transformation.', 'placeholder': 'Themes', 'points': ['Grant competitiveness', 'Innovation storytelling', 'Digital-change positioning']},
            {'title': 'Next-Step Conversion', 'label': 'Follow Through', 'note': 'Structured follow-up that turns interest into a deeper advisory conversation.', 'placeholder': 'Follow Up', 'points': ['Q&A facilitation', 'Follow-up consultation', 'Audience-to-engagement pathway']},
        ],
        'closing_copy': 'This service is strongest when E4 Power needs to establish trust, insight, and strategic clarity early in the relationship before training or delivery begins.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Workshops & Training', '/services/workshops-training/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'workshops-training',
        'title': 'Workshops & Training',
        'accent_word': 'Educate',
        'main_word': 'Workshops & Training',
        'pillar': 'Educate',
        'hub_note': 'Structured learning experiences that build grant, technology, and leadership readiness.',
        'placeholder': 'Workshops',
        'hub_points': ['Grant writing labs', 'Team-based learning sessions', 'Internal capacity building'],
        'summary': 'Workshops & Training packages E4 Power’s expertise into practical sessions that help teams develop shared language, repeatable habits, and stronger institutional confidence.',
        'detail_cards': [
            {'title': 'Grant Writing Labs', 'label': 'Training Track', 'note': 'Hands-on sessions that move teams from concept to stronger submissions.', 'placeholder': 'Grant Lab', 'points': ['Proposal development practice', 'Narrative review exercises', 'Budget and compliance awareness']},
            {'title': 'Faculty & Staff Upskilling', 'label': 'Internal Readiness', 'note': 'Programs designed for campus teams, nonprofits, and operational staff.', 'placeholder': 'Upskilling', 'points': ['Cross-functional participation', 'Role-specific guidance', 'Repeatable internal systems']},
            {'title': 'Custom Delivery Formats', 'label': 'Session Design', 'note': 'Training delivered as virtual intensives, on-site workshops, or blended cohorts.', 'placeholder': 'Delivery', 'points': ['Virtual cohorts', 'On-site intensives', 'Leadership retreat formats']},
            {'title': 'Actionable Follow-Up', 'label': 'Implementation', 'note': 'Every workshop points to practical next steps rather than abstract inspiration alone.', 'placeholder': 'Next Steps', 'points': ['Templates and takeaways', 'Priority action lists', 'Pathways into deeper support']},
        ],
        'closing_copy': 'This service works best when the goal is to build shared readiness across a team before moving into more specialized consulting or execution support.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Technology & AI Literacy', '/services/technology-ai-literacy/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'technology-ai-literacy',
        'title': 'Technology & AI Literacy',
        'accent_word': 'Educate',
        'main_word': 'Technology & AI Literacy',
        'pillar': 'Educate',
        'hub_note': 'Practical education that helps teams understand digital tools without losing mission focus.',
        'placeholder': 'AI Literacy',
        'hub_points': ['AI readiness framing', 'Workflow education', 'Responsible adoption conversations'],
        'summary': 'Technology & AI Literacy helps organizations understand how modern tools can support research, operations, and communication in ways that stay aligned with policy, people, and purpose.',
        'detail_cards': [
            {'title': 'Readiness Education', 'label': 'Starting Point', 'note': 'Foundational conversations that remove confusion and build confidence.', 'placeholder': 'Readiness', 'points': ['Plain-language AI framing', 'Misconception removal', 'Decision-maker education']},
            {'title': 'Workflow Translation', 'label': 'Practical Use', 'note': 'Sessions focused on where digital systems can reduce friction inside real operations.', 'placeholder': 'Workflow', 'points': ['Administrative workflows', 'Proposal support workflows', 'Knowledge-management habits']},
            {'title': 'Responsible Adoption', 'label': 'Governance Lens', 'note': 'Guidance that keeps experimentation aligned with institutional standards.', 'placeholder': 'Governance', 'points': ['Risk-aware adoption', 'Human review checkpoints', 'Policy-conscious implementation']},
            {'title': 'Bridge to Build', 'label': 'Next Service', 'note': 'This literacy layer can lead naturally into custom IT and application development work.', 'placeholder': 'Bridge Build', 'points': ['Tool evaluation', 'Process mapping', 'Referral into solution design']},
        ],
        'closing_copy': 'This service gives E4 Power a thoughtful way to introduce technology strategy without overwhelming teams that need clarity before implementation.',
        'related_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('IT & App Development', '/services/it-app-development/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'grant-writing',
        'title': 'Grant Writing',
        'accent_word': 'Empower',
        'main_word': 'Grant Writing',
        'pillar': 'Empower',
        'hub_note': 'Pre-award strategy and proposal-development support from concept to submission.',
        'placeholder': 'Grant Writing',
        'hub_points': ['Opportunity scans', 'Narrative development', 'Submission support'],
        'summary': 'Grant Writing is one of E4 Power’s clearest competitiveness services, helping institutions shape stronger opportunities, tell sharper stories, and submit more strategically.',
        'detail_cards': [
            {'title': 'Opportunity Positioning', 'label': 'Pre-Award Strategy', 'note': 'Match the right opportunities to the right institutional strengths.', 'placeholder': 'Positioning', 'points': ['Opportunity review', 'Fit assessment', 'Competitive framing']},
            {'title': 'Proposal Development', 'label': 'Core Delivery', 'note': 'Move from rough concept to coherent proposal package.', 'placeholder': 'Proposal', 'points': ['Narrative drafting', 'Budget coordination', 'Attachment support']},
            {'title': 'Internal Coordination', 'label': 'Stakeholder Flow', 'note': 'Keep collaborators, reviewers, and leadership aligned through submission.', 'placeholder': 'Coordination', 'points': ['Reviewer management', 'Approval sequencing', 'Timeline discipline']},
            {'title': 'Submission Readiness', 'label': 'Final Stage', 'note': 'Protect quality at the end of the process with clear checks and polish.', 'placeholder': 'Submission', 'points': ['Final review passes', 'Compliance checks', 'Submission support']},
        ],
        'closing_copy': 'This service is often the first visible proof of E4 Power’s strategic value because it ties institutional ambition directly to fundable action.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Readiness Assessments', '/services/readiness-assessments/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'readiness-assessments',
        'title': 'Readiness Assessments',
        'accent_word': 'Empower',
        'main_word': 'Readiness Assessments',
        'pillar': 'Empower',
        'hub_note': 'Baseline reviews that reveal strengths, gaps, and the right first move.',
        'placeholder': 'Readiness',
        'hub_points': ['Gap identification', 'Infrastructure mapping', 'Strategic prioritization'],
        'summary': 'Readiness Assessments helps E4 Power identify what an institution can do now, what needs strengthening, and what path will create the most credible momentum.',
        'detail_cards': [
            {'title': 'Baseline Review', 'label': 'Current State', 'note': 'Understand the real operating condition before recommending action.', 'placeholder': 'Baseline', 'points': ['Current-capacity review', 'Process visibility', 'Strength mapping']},
            {'title': 'Gap Discovery', 'label': 'Risk & Friction', 'note': 'Surface the barriers that could slow growth, funding, or delivery.', 'placeholder': 'Gap Discovery', 'points': ['Capability gaps', 'Role ambiguity', 'Infrastructure bottlenecks']},
            {'title': 'Priority Sequencing', 'label': 'Decision Support', 'note': 'Translate findings into an order of operations leaders can actually act on.', 'placeholder': 'Priority', 'points': ['Phased roadmap', 'Near-term priorities', 'Service-fit recommendations']},
            {'title': 'Bridge into Delivery', 'label': 'Activation', 'note': 'Assessments become a launch point for proposal, partnership, or implementation support.', 'placeholder': 'Activation', 'points': ['Grant-readiness activation', 'Onboarding readiness', 'Execution planning']},
        ],
        'closing_copy': 'This service is especially useful when an organization knows it needs support but wants a disciplined diagnosis before investing in a larger workstream.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Institutional Discovery', '/services/institutional-discovery/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'intellectual-property',
        'title': 'Intellectual Property',
        'accent_word': 'Empower',
        'main_word': 'Intellectual Property',
        'pillar': 'Empower',
        'hub_note': 'Innovation protection and commercialization guidance for research-driven institutions.',
        'placeholder': 'IP Strategy',
        'hub_points': ['Patent guidance', 'Researcher education', 'Commercialization positioning'],
        'summary': 'Intellectual Property support helps institutions protect what they create, make smarter strategic decisions, and align innovation work with long-term value creation.',
        'detail_cards': [
            {'title': 'Protection Strategy', 'label': 'Core Service', 'note': 'Clarify where innovation should be protected and how to think about timing.', 'placeholder': 'Protection', 'points': ['Protection-path education', 'Decision support', 'Value-sensitive guidance']},
            {'title': 'Research Translation', 'label': 'Faculty Support', 'note': 'Help technical teams understand the strategic implications of their discoveries.', 'placeholder': 'Translation', 'points': ['Inventor-facing conversations', 'Commercial framing', 'Documentation readiness']},
            {'title': 'Commercial Positioning', 'label': 'Growth Lens', 'note': 'Support the move from idea to market relevance with thoughtful framing.', 'placeholder': 'Commercial', 'points': ['Opportunity framing', 'Partner positioning', 'Innovation storytelling']},
            {'title': 'Integrated Advisory', 'label': 'Cross-Service Fit', 'note': 'IP strategy can strengthen grants, partnerships, and digital initiatives when aligned early.', 'placeholder': 'Advisory', 'points': ['Grant-aligned IP thinking', 'Partnership context', 'Innovation ecosystem support']},
        ],
        'closing_copy': 'This service helps E4 Power stand out as a partner that understands not only funding, but also the strategic protection and positioning of research-driven value.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Grant Writing', '/services/grant-writing/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'it-app-development',
        'title': 'IT & App Development',
        'accent_word': 'Empower',
        'main_word': 'IT & App Development',
        'pillar': 'Empower',
        'hub_note': 'Custom portals, websites, and internal tools that extend strategy into working infrastructure.',
        'placeholder': 'App Build',
        'hub_points': ['Custom portals', 'Web app delivery', 'Operational tool design'],
        'summary': 'IT & App Development gives E4 Power a tangible implementation layer for organizations that need custom digital systems, better workflows, or more credible operational infrastructure.',
        'detail_cards': [
            {'title': 'Custom Portals', 'label': 'Digital Delivery', 'note': 'Build mission-specific interfaces for internal use, partners, or public audiences.', 'placeholder': 'Portals', 'points': ['Role-based dashboards', 'Stakeholder portals', 'Branded access experiences']},
            {'title': 'Websites & Apps', 'label': 'Public & Internal', 'note': 'Translate institutional goals into practical, high-trust digital experiences.', 'placeholder': 'Web Apps', 'points': ['Marketing websites', 'Process tools', 'Application workflows']},
            {'title': 'Workflow Design', 'label': 'Operational Fit', 'note': 'Anchor technology decisions in real process needs rather than novelty.', 'placeholder': 'Workflow Design', 'points': ['Process mapping', 'Feature prioritization', 'Human-centered use cases']},
            {'title': 'Ongoing Support', 'label': 'Continuity', 'note': 'Keep systems useful after launch through maintenance-minded planning.', 'placeholder': 'Support', 'points': ['Maintenance guidance', 'Iteration planning', 'Continuity support']},
        ],
        'closing_copy': 'This service is a natural extension of Empower because it turns advisory recommendations into visible, usable infrastructure that helps teams operate better.',
        'related_links': [('Services Hub', '/services/'), ('Empower', '/empower/'), ('Technology & AI Literacy', '/services/technology-ai-literacy/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'grant-management',
        'title': 'Grant Management',
        'accent_word': 'Elevate',
        'main_word': 'Grant Management',
        'pillar': 'Elevate',
        'hub_note': 'Post-award coordination that protects compliance, relationships, and momentum.',
        'placeholder': 'Grant Mgmt',
        'hub_points': ['Reporting coordination', 'Compliance oversight', 'Award closeout support'],
        'summary': 'Grant Management helps organizations protect the work they have already won by building steadier reporting, documentation, and stewardship practices after the award.',
        'detail_cards': [
            {'title': 'Post-Award Oversight', 'label': 'Core Scope', 'note': 'Support the systems needed to manage awards responsibly.', 'placeholder': 'Oversight', 'points': ['Award setup support', 'Milestone planning', 'Program stewardship']},
            {'title': 'Reporting Rhythm', 'label': 'Agency Trust', 'note': 'Keep reporting obligations visible, timely, and aligned with expectations.', 'placeholder': 'Reporting', 'points': ['Deadline management', 'Narrative coordination', 'Submission organization']},
            {'title': 'Compliance Support', 'label': 'Risk Control', 'note': 'Reduce preventable issues by making compliance part of the operating rhythm.', 'placeholder': 'Compliance', 'points': ['Documentation discipline', 'Review checkpoints', 'Agency-conscious controls']},
            {'title': 'Closeout Planning', 'label': 'Lifecycle Completion', 'note': 'Prepare the end of the award with the same care as the beginning.', 'placeholder': 'Closeout', 'points': ['Closeout preparation', 'Lessons-learned review', 'Future-opportunity readiness']},
        ],
        'closing_copy': 'This service is essential for clients who need confidence that awarded work will be managed with the discipline and credibility expected by funders.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Project Management', '/services/project-management/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'project-management',
        'title': 'Project Management',
        'accent_word': 'Elevate',
        'main_word': 'Project Management',
        'pillar': 'Elevate',
        'hub_note': 'Execution systems that keep complex initiatives coordinated and accountable.',
        'placeholder': 'Project Delivery',
        'hub_points': ['Timeline management', 'Cross-team execution', 'Risk-aware coordination'],
        'summary': 'Project Management turns ambitious initiatives into a tracked, coordinated, and more predictable operating system so teams can execute without losing alignment.',
        'detail_cards': [
            {'title': 'Execution Frameworks', 'label': 'Delivery Design', 'note': 'Build a visible structure for work, accountability, and pacing.', 'placeholder': 'Framework', 'points': ['Milestone mapping', 'Ownership clarity', 'Decision pathways']},
            {'title': 'Cross-Team Coordination', 'label': 'Operational Alignment', 'note': 'Reduce friction between stakeholders, units, and external partners.', 'placeholder': 'Coordination', 'points': ['Meeting cadence design', 'Responsibility tracking', 'Inter-team communication']},
            {'title': 'Risk Awareness', 'label': 'Control Layer', 'note': 'Keep projects moving by identifying issues before they become delivery failures.', 'placeholder': 'Risk', 'points': ['Issue visibility', 'Escalation logic', 'Contingency planning']},
            {'title': 'Outcome Visibility', 'label': 'Leadership Confidence', 'note': 'Give leaders a clearer picture of progress and next decisions.', 'placeholder': 'Visibility', 'points': ['Status reporting', 'Progress summaries', 'Decision-support checkpoints']},
        ],
        'closing_copy': 'This service is strongest when a client needs help translating strategic intent into managed execution across multiple stakeholders and moving parts.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Financial Management', '/services/financial-management/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'financial-management',
        'title': 'Financial Management',
        'accent_word': 'Elevate',
        'main_word': 'Financial Management',
        'pillar': 'Elevate',
        'hub_note': 'Budget oversight and fiscal stewardship aligned with funder expectations.',
        'placeholder': 'Financial',
        'hub_points': ['Budget tracking', 'Allowable-cost awareness', 'Audit-conscious oversight'],
        'summary': 'Financial Management helps institutions create steadier fiscal controls around funded work so budgets, reporting, and stewardship stay credible under scrutiny.',
        'detail_cards': [
            {'title': 'Budget Stewardship', 'label': 'Core Scope', 'note': 'Keep funds aligned to approved use and operational reality.', 'placeholder': 'Budget', 'points': ['Budget monitoring', 'Expense visibility', 'Use-of-funds alignment']},
            {'title': 'Control Discipline', 'label': 'Operational Guardrails', 'note': 'Create a stronger environment for accountability and review.', 'placeholder': 'Controls', 'points': ['Checkpoints and approvals', 'Documentation habits', 'Exception awareness']},
            {'title': 'Reporting Support', 'label': 'Fiscal Communication', 'note': 'Improve how financial information is assembled and communicated.', 'placeholder': 'Reporting', 'points': ['Financial reporting support', 'Cross-team coordination', 'Decision-ready summaries']},
            {'title': 'Audit Awareness', 'label': 'Confidence Layer', 'note': 'Prepare teams to operate with greater confidence under oversight.', 'placeholder': 'Audit', 'points': ['Audit-conscious habits', 'Record discipline', 'Risk reduction practices']},
        ],
        'closing_copy': 'This service reinforces E4 Power’s role as an execution partner that protects not only delivery, but also the fiscal credibility behind delivery.',
        'related_links': [('Services Hub', '/services/'), ('Elevate', '/elevate/'), ('Grant Management', '/services/grant-management/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'institutional-discovery',
        'title': 'Institutional Discovery',
        'accent_word': 'Engage',
        'main_word': 'Institutional Discovery',
        'pillar': 'Engage',
        'hub_note': 'Early conversations that clarify fit, constraints, and the best starting point.',
        'placeholder': 'Discovery',
        'hub_points': ['Discovery meetings', 'Needs clarification', 'Initial roadmap framing'],
        'summary': 'Institutional Discovery is the relationship-front-door service that helps E4 Power understand the organization, its goals, and the smartest first move before deeper work begins.',
        'detail_cards': [
            {'title': 'Discovery Meetings', 'label': 'Entry Conversation', 'note': 'Create space for honest discussion about context, pressure points, and priorities.', 'placeholder': 'Meetings', 'points': ['Leadership conversations', 'Goal clarification', 'Constraint mapping']},
            {'title': 'Needs Clarification', 'label': 'Problem Framing', 'note': 'Translate broad ambition into a more usable definition of the work ahead.', 'placeholder': 'Clarification', 'points': ['Challenge articulation', 'Service-fit discussion', 'Scope framing']},
            {'title': 'Readiness Signals', 'label': 'Early Insight', 'note': 'Spot what is ready now and what needs strengthening before action.', 'placeholder': 'Signals', 'points': ['Capacity indicators', 'Priority pressure points', 'Immediate opportunities']},
            {'title': 'Next-Step Pathway', 'label': 'Momentum', 'note': 'Turn the first conversation into a structured recommendation for what comes next.', 'placeholder': 'Pathway', 'points': ['Recommended sequencing', 'Suggested service path', 'Follow-up planning']},
        ],
        'closing_copy': 'This service is valuable because it lets E4 Power begin with listening, fit, and clarity rather than forcing organizations into a preselected pathway.',
        'related_links': [('Services Hub', '/services/'), ('Engage', '/engage/'), ('Advisory Alignment', '/services/advisory-alignment/'), ('Contact Us', '/contact-us')],
    },
    {
        'slug': 'advisory-alignment',
        'title': 'Advisory Alignment',
        'accent_word': 'Engage',
        'main_word': 'Advisory Alignment',
        'pillar': 'Engage',
        'hub_note': 'Trust-building guidance that aligns the right experts, priorities, and first actions.',
        'placeholder': 'Advisory',
        'hub_points': ['Decision-maker alignment', 'Specialist matching', 'Structured next steps'],
        'summary': 'Advisory Alignment helps E4 Power connect the right people to the right challenge so the relationship starts with clarity, trust, and a shared definition of progress.',
        'detail_cards': [
            {'title': 'Decision-Maker Alignment', 'label': 'Leadership Fit', 'note': 'Make sure the people shaping the work agree on direction and expectations.', 'placeholder': 'Leadership', 'points': ['Leadership alignment', 'Stakeholder clarity', 'Expectation setting']},
            {'title': 'Specialist Matching', 'label': 'Team Formation', 'note': 'Bring the right E4 expertise into the conversation at the right time.', 'placeholder': 'Specialists', 'points': ['Expert matching', 'Role clarity', 'Cross-functional coordination']},
            {'title': 'Partnership Structure', 'label': 'Working Model', 'note': 'Define how collaboration will function before execution accelerates.', 'placeholder': 'Structure', 'points': ['Communication rhythm', 'Engagement model', 'Decision checkpoints']},
            {'title': 'Action Launch', 'label': 'Momentum', 'note': 'Convert alignment into a practical next-step plan with accountability.', 'placeholder': 'Launch', 'points': ['Immediate actions', 'Ownership mapping', 'Engagement launch plan']},
        ],
        'closing_copy': 'This service is the bridge between discovery and execution because it helps relationships move from possibility into a more committed, coherent working model.',
        'related_links': [('Services Hub', '/services/'), ('Engage', '/engage/'), ('Institutional Discovery', '/services/institutional-discovery/'), ('Contact Us', '/contact-us')],
    },
]

service_cards_for_hub = [
    {
        'title': service['title'],
        'label': service['pillar'],
        'note': service['hub_note'],
        'placeholder': service['placeholder'],
        'points': service['hub_points'],
        'href': f'/services/{service["slug"]}/',
    }
    for service in service_details
]

standard_pages = {
    'services': {
        'title': 'Services | E4 Power',
        'accent_word': 'Service',
        'main_word': 'Catalog',
        'overline': 'Meet the experts behind your success',
        'subtitle': 'Our expertise <span>Your advantage</span>',
        'summary': 'Explore E4 Power by individual service title rather than broad buckets. Each card below works as a direct entry point into a dedicated service breakout page built in the same editorial system as the provided example.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': service_cards_for_hub,
        'closing_copy': 'This page is now the clearest capability index on the site: visitors can scan named services, understand which pillar each one belongs to, and move directly into a focused breakout page for deeper review.',
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
            {'title': 'Speaking Engagements', 'label': 'Educate', 'note': 'High-value talks for institutional audiences and leadership teams.', 'placeholder': 'Speaking', 'points': ['Keynotes and plenaries', 'Leadership motivation', 'Strategic briefings']},
            {'title': 'Workshops', 'label': 'Educate', 'note': 'Structured learning programs that build team readiness.', 'placeholder': 'Workshops', 'points': ['Grant writing', 'Proposal review', 'Research strategy']},
            {'title': 'Technology & AI Literacy', 'label': 'Educate', 'note': 'Education-led framing for digital change and AI adoption.', 'placeholder': 'AI Literacy', 'points': ['AI readiness conversations', 'Workflow education', 'Innovation translation']},
            {'title': 'Leadership Development', 'label': 'Educate', 'note': 'Practical capacity-building for internal advancement and confidence.', 'placeholder': 'Leadership', 'points': ['Career development support', 'Team capacity building', 'Leadership readiness']},
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
            {'title': 'Grant Writing', 'label': 'Empower', 'note': 'Proposal-development support from idea to submission.', 'placeholder': 'Grant Writing', 'points': ['Opportunity scans', 'Proposal writing', 'Submission support']},
            {'title': 'Readiness Assessments', 'label': 'Empower', 'note': 'Institutional reviews that clarify fundable next moves.', 'placeholder': 'Readiness', 'points': ['SWOT analysis', 'Infrastructure review', 'Strategic implementation baseline']},
            {'title': 'Intellectual Property', 'label': 'Empower', 'note': 'Protection and commercialization support for research assets.', 'placeholder': 'IP Support', 'points': ['Patent guidance', 'Researcher education', 'Commercialization positioning']},
            {'title': 'IT & Application Development', 'label': 'Empower', 'note': 'Custom digital delivery that extends strategy into infrastructure.', 'placeholder': 'App Development', 'points': ['Custom portals', 'Web apps and websites', 'IT support']},
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
        'summary': 'Elevate turns the narrative toward execution, stewardship, and measurable delivery. The breakout page uses the reference card system to present post-award and operational services in a more editorial format.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Grant Management', 'label': 'Elevate', 'note': 'Post-award support that protects agency relationships.', 'placeholder': 'Grant Mgmt', 'points': ['Reporting coordination', 'Compliance oversight', 'Award closeout']},
            {'title': 'Project Management', 'label': 'Elevate', 'note': 'Structured systems for complex initiative delivery.', 'placeholder': 'Project Delivery', 'points': ['Timeline management', 'Cross-team execution', 'Risk-aware coordination']},
            {'title': 'Financial Management', 'label': 'Elevate', 'note': 'Fiscal oversight aligned with federal expectations.', 'placeholder': 'Financial', 'points': ['Drawdown support', 'Cost tracking', 'Audit-conscious stewardship']},
            {'title': 'IT Support Continuity', 'label': 'Elevate', 'note': 'Operational continuity for launched digital systems.', 'placeholder': 'IT Support', 'points': ['Support workflows', 'Maintenance guidance', 'Operational continuity']},
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
        'summary': 'Engage is the partnership-entry pillar. The page uses the same visual system as the reference to frame readiness, discovery, and relationship-led onboarding in a tighter, more intentional layout.',
        'button_label': 'Contact Us',
        'button_href': '/contact-us',
        'cards': [
            {'title': 'Institutional Discovery', 'label': 'Engage', 'note': 'Early conversations that clarify goals and fit.', 'placeholder': 'Discovery', 'points': ['Discovery meetings', 'Needs clarification', 'Initial roadmapping']},
            {'title': 'Readiness-Led Onboarding', 'label': 'Engage', 'note': 'A practical baseline for future workstreams.', 'placeholder': 'Onboarding', 'points': ['Baseline review', 'Gap identification', 'Priority sequencing']},
            {'title': 'Team-Led Partnership Model', 'label': 'Engage', 'note': 'Specialist alignment built around client goals.', 'placeholder': 'Partnership', 'points': ['Executive introductions', 'Specialist alignment', 'Collaborative planning']},
            {'title': 'Advisory Alignment', 'label': 'Engage', 'note': 'The bridge between trust-building and execution planning.', 'placeholder': 'Advisory', 'points': ['Partnership-fit review', 'Decision-maker alignment', 'Next-step planning']},
        ],
        'closing_copy': 'Use Engage when prospects want to understand the people, the advisory model, and how a thoughtful partnership with E4 Power begins before deeper execution starts.',
        'secondary_links': [('Services Hub', '/services/'), ('Educate', '/educate/'), ('Empower', '/empower/'), ('Elevate', '/elevate/')],
    },
}

for relative_dir, page in standard_pages.items():
    write_page(
        relative_dir=relative_dir,
        title=page['title'],
        accent_word=page['accent_word'],
        main_word=page['main_word'],
        overline=page['overline'],
        subtitle=page['subtitle'],
        summary=page['summary'],
        button_label=page['button_label'],
        button_href=page['button_href'],
        cards=page['cards'],
        closing_copy=page['closing_copy'],
        secondary_links=page['secondary_links'],
    )

for service in service_details:
    write_page(
        relative_dir=f'services/{service["slug"]}',
        title=f'{service["title"]} | E4 Power',
        accent_word=service['accent_word'],
        main_word=service['main_word'],
        overline='Meet the experts behind your success',
        subtitle='Our expertise <span>Your advantage</span>',
        summary=service['summary'],
        button_label='Contact Us',
        button_href='/contact-us',
        cards=service['detail_cards'],
        closing_copy=service['closing_copy'],
        secondary_links=service['related_links'],
    )
