from pathlib import Path
import re

BASE = Path('/home/ubuntu/e4powerinc-clone/client')
source = (BASE / 'index.html').read_text(encoding='utf-8')

head_match = re.search(r'<!DOCTYPE html>.*?</head>', source, re.S)
footer_match = re.search(r'<footer class="section footer">.*?</body></html>', source, re.S)
if not head_match or not footer_match:
    raise SystemExit('Could not extract head/footer from homepage')

base_head = head_match.group(0)
base_footer = footer_match.group(0)

nav_html = '''<nav class="navbar-logo-left"><div class="navbar-logo-left-container shadow-three w-nav" data-animation="over-right" data-collapse="all" data-duration="400" data-easing="ease" data-easing2="ease" role="banner"><div class="navbar-container"><div class="navbar-wrapper"><a class="navbar-brand w-nav-brand" href="/"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg"/></a><div class="navbar-right-div"><div class="socials-div"><a class="social-link-block w-inline-block" href="https://www.instagram.com/e4power_?igsh=bXR4bThxMHh2dHNy&amp;utm_source=qr" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c4ee8e329fe01d525b_instagram.svg"/></a><a class="social-link-block w-inline-block" href="https://www.linkedin.com/company/e4-power-consulting/" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c46c9537fa67bb89bd_linkedin.svg"/></a><a class="social-link-block w-inline-block" href="https://www.tiktok.com/@e4powerconsulting?_t=ZT-90YVLBMkwaT&amp;_r=1" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68f66f4d7a2ffc0d86a72550_tiktok.svg"/></a><a class="social-link-block w-inline-block" href="https://www.facebook.com/profile.php?id=61573544665670&amp;mibextid=wwXIfr&amp;rdid=yOcyRogs7shBnrLD&amp;share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1775G2zRAh%2F%3Fmibextid%3DwwXIfr#" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c48dbb4dd69e849624_facebook.svg"/></a></div><a class="text-link" href="/contact-us">Contact Us</a><div class="menu-button w-nav-button"><div class="hamburger-icon w-icon-nav-menu"></div></div></div><nav class="nav-menu-wrapper w-nav-menu" role="navigation"><ul class="nav-menu-two w-list-unstyled" role="list"><li><a class="nav-link" href="/services">Services</a></li><li><a class="nav-link" href="/educate">Educate</a></li><li><a class="nav-link" href="/empower">Empower</a></li><li><a class="nav-link" href="/elevate">Elevate</a></li><li><a class="nav-link" href="/engage">Engage</a></li></ul></nav></div></div></div></nav>'''

footer_replacements = {
    'href="#educate"': 'href="/educate"',
    'href="#empower"': 'href="/empower"',
    'href="#elevate"': 'href="/elevate"',
    'href="#engage"': 'href="/engage"',
}
shared_footer = base_footer
for old, new in footer_replacements.items():
    shared_footer = shared_footer.replace(old, new)
shared_footer = shared_footer.replace('</div><div class="socials-div footer">', '<a class="testimonial-text footer-link" href="/services">Services</a><div class="testimonial-text footer-link">|</div></div><div class="socials-div footer">')

custom_css = '''
<style>
.page-shell { background: linear-gradient(180deg, #17110a 0%, #040404 34%, #0d0d0d 100%); }
.page-hero { position: relative; min-height: 76vh; display: flex; align-items: end; overflow: hidden; }
.page-hero-media { position: absolute; inset: 0; background-size: cover; background-position: center; filter: grayscale(1); transform: scale(1.03); }
.page-hero-overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0.72) 68%, #050505 100%); }
.page-hero-inner { position: relative; z-index: 2; width: 100%; }
.page-eyebrow { color: #e2b24c; text-transform: uppercase; letter-spacing: .24em; font-size: .95rem; margin-bottom: 1.1rem; }
.page-display { color: #f6f1e8; text-transform: uppercase; line-height: .95; max-width: 12ch; margin: 0; }
.page-intro { color: #ddd0be; max-width: 44rem; font-size: 1.2rem; line-height: 1.8; margin-top: 1.5rem; }
.page-grid { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(20rem, .8fr); gap: 4rem; align-items: end; }
.metric-panel { background: rgba(24, 24, 24, 0.75); border: 1px solid rgba(226,178,76,0.28); backdrop-filter: blur(12px); padding: 2.2rem; }
.metric-value { color: #f0bf5d; font-size: 3.25rem; line-height: 1; margin-bottom: .65rem; }
.metric-copy { color: #efe5d5; font-size: .98rem; line-height: 1.8; }
.content-section { position: relative; padding: 7rem 0; }
.content-section.dark { background: #050505; }
.content-section.charcoal { background: #130f0a; }
.content-section .section-label { color: #e2b24c; text-transform: uppercase; letter-spacing: .18em; margin-bottom: 1rem; }
.content-section .section-title { color: #f7f1e8; margin: 0; text-transform: uppercase; }
.content-section .section-copy { color: #d6cab9; font-size: 1.02rem; line-height: 1.9; max-width: 52rem; margin-top: 1.5rem; }
.service-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem; margin-top: 3rem; }
.service-card { background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02)); border: 1px solid rgba(226,178,76,0.26); padding: 2rem 1.75rem; min-height: 18rem; display: flex; flex-direction: column; justify-content: space-between; }
.service-tag { color: #e2b24c; text-transform: uppercase; letter-spacing: .18em; font-size: .8rem; }
.service-card h3 { color: #f7f0e3; margin: .9rem 0 0; text-transform: uppercase; font-size: 1.45rem; line-height: 1.2; }
.service-card p { color: #d1c4b3; line-height: 1.8; margin-top: 1rem; }
.service-points { margin-top: 1.5rem; padding-left: 1.2rem; color: #efe5d5; }
.service-points li { margin-bottom: .65rem; }
.relation-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; margin-top: 2.4rem; }
.relation-card { border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.03); padding: 1.4rem; }
.relation-card h4 { color: #f4bd52; margin: 0 0 .7rem; text-transform: uppercase; }
.relation-card p { color: #d7ccbc; line-height: 1.75; margin: 0; }
.case-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin-top: 2.5rem; }
.case-card { background: #090909; border-left: 2px solid #e2b24c; padding: 1.8rem; }
.case-card .case-kicker { color: #e2b24c; letter-spacing: .18em; text-transform: uppercase; font-size: .8rem; }
.case-card h4 { color: #f7f1e7; margin: .75rem 0; text-transform: uppercase; }
.case-card p { color: #cfc2b1; line-height: 1.8; margin: 0; }
.cta-band { padding: 5rem 0 6rem; background: linear-gradient(180deg, #120f0a 0%, #050505 100%); }
.cta-panel { border: 1px solid rgba(226,178,76,0.3); background: rgba(255,255,255,0.03); padding: 2.4rem; display: grid; grid-template-columns: 1.2fr auto; gap: 2rem; align-items: center; }
.cta-panel h3 { color: #f7f1e8; margin: 0; text-transform: uppercase; }
.cta-panel p { color: #d5c9b7; margin: .8rem 0 0; line-height: 1.8; max-width: 46rem; }
.cta-links { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: end; }
.cta-link { border: 1px solid rgba(226,178,76,0.4); color: #f2ede5; padding: .9rem 1.15rem; text-transform: uppercase; text-decoration: none; letter-spacing: .1em; }
.cta-link.primary { background: #e2b24c; color: #120d08; }
@media screen and (max-width: 991px) {
  .page-grid, .cta-panel, .service-grid, .relation-grid, .case-grid { grid-template-columns: 1fr; }
  .page-display { max-width: none; }
  .cta-links { justify-content: start; }
}
</style>
'''

pages = {
    'services': {
        'title': 'Services | E4 Power',
        'eyebrow': 'Capabilities Overview',
        'heading': 'Full-Lifecycle Services for Institutional Growth',
        'intro': 'E4 Power supports institutions from early opportunity discovery through funded-program execution. The expanded services architecture brings grant strategy, readiness, intellectual property, financial stewardship, project delivery, and training into one connected partnership model.',
        'metric_value': '07+',
        'metric_copy': 'Core service lines now organized into pillar-led pathways so visitors can understand both the breadth of E4 Power and how each capability supports measurable institutional outcomes.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d8811dee8e329fe0f879dc_elevate%20picture.webp',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Service Architecture',
                'title': 'A Services Hub that Mirrors the BRIDGE Mindset',
                'copy': 'The Services page functions as the capability index for decision-makers. It explains what E4 Power does beyond proposal writing, while also clarifying how those capabilities align with Educate, Empower, Elevate, and Engage.',
                'cards': [
                    ('Pre-Award Strategy', 'Empower', 'Grant writing, readiness planning, opportunity identification, and proposal-development support for HBCUs, ERIs, MSIs, and nonprofits.', ['Opportunity identification', 'Proposal development', 'Competitive positioning']),
                    ('Post-Award Stewardship', 'Elevate', 'Grant management, compliance support, and closeout discipline that protect agency relationships after an award is secured.', ['Award setup and reporting', 'Compliance coordination', 'Closeout readiness']),
                    ('Project & Program Management', 'Elevate', 'Structured execution support for research, workforce, and multi-institution initiatives requiring dependable delivery systems.', ['Risk-aware execution', 'Cross-team coordination', 'Milestone accountability']),
                    ('Readiness Assessments', 'Engage', 'Institutional discovery work that clarifies infrastructure, staffing, and systems gaps before a funding pursuit begins.', ['SWOT review', 'Infrastructure mapping', 'Growth prioritization']),
                    ('Intellectual Property Services', 'Empower', 'Innovation-protection and commercialization support led by IP specialists to help institutions move ideas from lab to market.', ['Patent strategy', 'IP education', 'Commercialization support']),
                    ('Financial Management', 'Elevate', 'Budget development, fiscal oversight, and audit-conscious financial management aligned with federal requirements.', ['Allowable cost tracking', 'Budget oversight', 'Fiscal compliance']),
                ],
                'relations': [
                    ('Educate', 'Translates expertise into workshops, speaking, and skill-building for faculty, researchers, and leaders.'),
                    ('Empower', 'Advances competitiveness through strategic planning, proposals, IP, and innovation-enabled growth.'),
                    ('Elevate', 'Supports funded work through stewardship, execution systems, and outcome visibility.'),
                    ('Engage', 'Creates the institutional partnership doorway through discovery, readiness, and advisory collaboration.'),
                ],
            },
            {
                'tone': 'dark',
                'label': 'Additional Capabilities',
                'title': 'Broader Services Beyond Grant Writing',
                'copy': 'The capabilities deck also highlights speaking engagements, workshops, and IT solution support including large language model and AI integration. Those services broaden the public story from grant consultant to institutional growth partner.',
                'cards': [
                    ('Speaking Engagements', 'Educate', 'Speaker-led engagements that translate technical and strategic experience into motivating, practical sessions for institutional audiences.', ['Leadership talks', 'Research strategy sessions', 'Conference appearances']),
                    ('Workshops & Training', 'Educate', 'Hands-on learning programs that equip teams with grant strategy, proposal review, partnerships, compliance, and readiness knowledge.', ['Faculty training', 'Workshop curriculum', 'Capacity building']),
                    ('IT Solutions & AI Integration', 'Empower', 'Technology-forward advisory support that helps institutions explore automation, large language models, and workflow efficiency in a mission-aligned way.', ['Workflow modernization', 'AI integration concepts', 'Strategic technology advisory']),
                ],
                'relations': [],
            },
        ],
        'cases': [
            ('Full Lifecycle', 'E4 Power is positioned as a single partner from idea to impact, combining readiness, strategy, execution, and financial oversight rather than treating each service in isolation.'),
            ('Institutional Fit', 'The service structure is especially relevant for HBCUs, ERIs, MSIs, nonprofits, and research-led organizations that need both strategic guidance and operational delivery support.'),
        ],
        'cta': 'Use this page as the top-level entry point in the navigation, then route visitors into the pillar pages for a more focused understanding of how services show up within each part of the E4 Power model.'
    },
    'educate': {
        'title': 'Educate | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Educate: Training, Speaking, and Capacity Building',
        'intro': 'Educate should show how E4 Power turns experience into practical knowledge. This page expands the homepage pillar into a deeper training-focused offer for institutions that need stronger internal capability, not just outsourced support.',
        'metric_value': '30+',
        'metric_copy': 'Workshops and speaking-led engagements reinforce the pillar by helping faculty, researchers, and administrators build competitive habits before and during funding pursuits.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d899f54126036ff52c6474_washington%20dc.webp',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Educate Services',
                'title': 'Learning Experiences that Increase Institutional Readiness',
                'copy': 'The deck positions speaking engagements and workshops as a formal service line. On the site, Educate should present those offerings as strategic learning systems that sharpen teams for grant competition, partnership-building, leadership development, and innovation readiness.',
                'cards': [
                    ('Speaking Engagements', 'Education & Training', 'High-value talks for conferences, faculty gatherings, and institutional leadership sessions that translate complex funding and innovation themes into accessible direction.', ['Keynotes and plenaries', 'Leadership motivation', 'Strategic briefings']),
                    ('Workshops', 'Education & Training', 'Structured workshops that teach practical grant, partnership, proposal review, compliance, and career-development skills.', ['Grant writing', 'Proposal review', 'Research strategy']),
                    ('Technology & AI Literacy', 'Emerging Capability', 'An education-oriented framing for IT solutions and AI integration, helping teams understand modern workflows without disrupting mission priorities.', ['AI readiness conversations', 'Workflow education', 'Innovation translation']),
                ],
                'relations': [
                    ('Educate', 'Primary home for speaking, workshops, and capability-building services.'),
                    ('Empower', 'Training improves competitiveness and supports stronger pre-award strategy.'),
                    ('Elevate', 'Learning programs can also strengthen project delivery habits after awards are secured.'),
                    ('Engage', 'Educational programming often becomes the first trusted entry point into a longer partnership.'),
                ],
            }
        ],
        'cases': [
            ('Workshop Leadership', 'Dr. Treadwell’s background includes leading dozens of workshops on skills, leadership, and motivation, which gives Educate a credible human face.'),
            ('Training Themes', 'The current homepage already references grant writing, partnerships, research strategy, proposal review, budget development, and compliance, making this breakout page a natural expansion rather than a new direction.'),
        ],
        'cta': 'Use Educate as the destination for visitors who want practical training, keynote sessions, or institutional workshops before they are ready to engage deeper consulting support.'
    },
    'empower': {
        'title': 'Empower | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Empower: Strategy, Opportunity Creation, and Innovation Support',
        'intro': 'Empower should become the strategy-heavy pillar page. It is where E4 Power explains how it helps institutions move from ambition to competitive action through proposal development, readiness planning, IP support, and innovation-minded advisory services.',
        'metric_value': '78%',
        'metric_copy': 'Proposal-development success and growth-oriented consulting make this pillar the clearest place to show how E4 Power helps clients become more competitive before funding is awarded.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d86ed2cf005d4f005b60bd_1.webp',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Empower Services',
                'title': 'Services that Strengthen Competitive Positioning',
                'copy': 'Empower should hold the services that improve institutional confidence and competitiveness before or alongside major opportunities. That includes pre-award support, readiness reviews, intellectual property strategy, and carefully framed technology and AI integration support.',
                'cards': [
                    ('Grant Writing', 'Pre-Award', 'End-to-end proposal support from opportunity identification through narrative assembly, approvals, and submission discipline.', ['Opportunity scans', 'Proposal writing', 'Submission support']),
                    ('Readiness Assessments', 'Capacity Services', 'Institutional reviews that identify infrastructure gaps, growth priorities, and realistic pathways for future funding.', ['SWOT analysis', 'Infrastructure review', 'Strategic implementation baseline']),
                    ('Intellectual Property', 'Innovation Support', 'Protection and commercialization services that help researchers identify, secure, and position innovation assets.', ['Patent guidance', 'Researcher education', 'Commercialization positioning']),
                    ('IT Solutions & AI Integration', 'Modernization', 'Advisory support for institutions exploring automation, AI, and technology-enabled efficiency as part of long-term research and operational growth.', ['Automation ideas', 'LLM integration framing', 'Process modernization']),
                ],
                'relations': [
                    ('Educate', 'Training improves readiness for the strategic work introduced here.'),
                    ('Empower', 'Primary home for opportunity creation, proposal strategy, and innovation support.'),
                    ('Elevate', 'Strong pre-award strategy needs equally strong execution after an award is won.'),
                    ('Engage', 'Discovery conversations and readiness reviews often begin the work shown on this page.'),
                ],
            }
        ],
        'cases': [
            ('NSF HBCU-UP', 'The capabilities deck highlights a funded NSF HBCU-UP implementation proposal developed after more than two decades without an NSF award, reinforcing the strategic impact of this pillar.'),
            ('EPA Proposal Development', 'The deck also references leadership on a multi-million-dollar EPA proposal for biogenic building materials, showing that the pillar can support highly technical work as well as institutional strategy.'),
        ],
        'cta': 'Use Empower as the destination for prospects who want to know how E4 Power improves their competitiveness before the award, especially where funding, innovation, and strategic capacity intersect.'
    },
    'elevate': {
        'title': 'Elevate | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Elevate: Execution, Stewardship, and Measurable Delivery',
        'intro': 'Elevate should move the narrative from winning support to executing it well. This page clarifies that E4 Power does not stop at proposal submission; it also helps institutions manage awards, run projects, and maintain financial and compliance integrity.',
        'metric_value': '>$100M',
        'metric_copy': 'The capabilities deck positions E4 Power as a post-award and execution partner, not only a proposal partner. Elevate is where that fuller story becomes visible on the site.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d86ed2b8c8966dea03dc39_3.webp',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Elevate Services',
                'title': 'Services that Protect and Scale Awarded Work',
                'copy': 'Elevate should concentrate the post-award service lines that keep institutions compliant, organized, and outcomes-focused once funding is in motion. This makes the site’s promise more credible because it connects strategic wins with responsible delivery.',
                'cards': [
                    ('Grant Management', 'Post-Award', 'Support from award acceptance through reporting and project closeout to protect institutional standing with funding agencies.', ['Reporting coordination', 'Compliance oversight', 'Award closeout']),
                    ('Project Management', 'Program Delivery', 'Structured delivery systems for complex research, workforce, and multi-institution initiatives.', ['Timeline management', 'Cross-team execution', 'Risk-aware coordination']),
                    ('Financial Management', 'Fiscal Oversight', 'Budget and spending oversight aligned with federal expectations so institutions can manage funds with confidence.', ['Drawdown support', 'Cost tracking', 'Audit-conscious stewardship']),
                ],
                'relations': [
                    ('Educate', 'Training can prepare teams for the stewardship responsibilities shown here.'),
                    ('Empower', 'The strongest strategy still depends on disciplined execution after award.'),
                    ('Elevate', 'Primary home for award stewardship, project management, and fiscal oversight.'),
                    ('Engage', 'Ongoing partnerships deepen when E4 Power remains involved after funding is secured.'),
                ],
            }
        ],
        'cases': [
            ('UJIMA Collective', 'The deck references post-award management and reporting for a multi-partner NSF collaborative initiative, demonstrating how Elevate supports complex institutional coordination.'),
            ('Federal Oversight', 'Financial oversight examples and project-delivery case studies show how this pillar can speak to both compliance-sensitive administrators and program leaders.'),
        ],
        'cta': 'Use Elevate as the destination for visitors who need confidence that E4 Power can help protect awarded funding, keep teams aligned, and deliver outcomes responsibly.'
    },
    'engage': {
        'title': 'Engage | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Engage: Partnership Entry, Advisory Trust, and Institutional Alignment',
        'intro': 'Engage should become more than a team page. It should explain how institutions begin working with E4 Power through relationship-building, discovery, readiness discussions, and a collaborative understanding of what growth will require.',
        'metric_value': '10+',
        'metric_copy': 'The firm’s leadership bench, readiness methodology, and partnership orientation make Engage the right place to show how E4 Power enters organizations thoughtfully rather than transactionally.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5%2F68d857925f5c5c405f4b28a4_e4%20Power%20Background%20Vid-poster-00001.jpg',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Engage Services',
                'title': 'The Human and Strategic Entry Point into the Partnership',
                'copy': 'Engage should connect team credibility with the earliest stages of institutional work. It is the best home for readiness-led discovery, advisory alignment, and the relational side of the BRIDGE model that makes later strategy and delivery possible.',
                'cards': [
                    ('Institutional Discovery', 'Advisory Entry', 'Early conversations and strategic review sessions that identify goals, constraints, and where E4 Power can create the most value first.', ['Discovery meetings', 'Needs clarification', 'Initial roadmapping']),
                    ('Readiness-Led Onboarding', 'Capacity Services', 'A practical entry service that helps partners understand current systems, staffing, and funding readiness before moving into larger workstreams.', ['Baseline review', 'Gap identification', 'Priority sequencing']),
                    ('Team-Led Partnership Model', 'People & Expertise', 'A relationship-centered consulting model that introduces prospects to the specialists most relevant to their goals across strategy, finance, IP, project delivery, and training.', ['Executive introductions', 'Specialist alignment', 'Collaborative planning']),
                ],
                'relations': [
                    ('Educate', 'Workshops and speaking engagements can begin the relationship with trust and value.'),
                    ('Empower', 'Strategic service lines often grow from the discovery and readiness work started here.'),
                    ('Elevate', 'Longer partnerships frequently continue into execution and post-award stewardship.'),
                    ('Engage', 'Primary home for discovery, readiness-led entry, and partnership orientation.'),
                ],
            }
        ],
        'cases': [
            ('Executive Bench', 'The team-led model is supported by leadership across grant strategy, intellectual property, finance, project management, and speaking engagements, which makes Engage a meaningful entry page rather than a simple biography section.'),
            ('Bridge Onboarding', 'The readiness assessment examples in the deck make a strong case for presenting Engage as the place where institutional alignment begins before deeper service execution.'),
        ],
        'cta': 'Use Engage as the destination for prospects who want to understand the people, the advisory model, and the first step in becoming an E4 Power partner.'
    },
}


def render_cards(cards):
    html = ['<div class="service-grid">']
    for title, tag, copy, points in cards:
        items = ''.join(f'<li>{p}</li>' for p in points)
        html.append(f'<article class="service-card"><div><div class="service-tag">{tag}</div><h3>{title}</h3><p>{copy}</p></div><ul class="service-points">{items}</ul></article>')
    html.append('</div>')
    return ''.join(html)


def render_relations(relations):
    if not relations:
        return ''
    cards = ''.join(f'<div class="relation-card"><h4>{title}</h4><p>{copy}</p></div>' for title, copy in relations)
    return f'<div class="relation-grid">{cards}</div>'


def render_sections(sections):
    parts = []
    for section in sections:
        parts.append(f'<section class="content-section {section["tone"]}"><div class="container"><div class="section-label">{section["label"]}</div><h2 class="section-title">{section["title"]}</h2><p class="section-copy">{section["copy"]}</p>{render_cards(section["cards"])}{render_relations(section["relations"])}</div></section>')
    return ''.join(parts)


def render_cases(cases):
    cards = ''.join(f'<article class="case-card"><div class="case-kicker">Context</div><h4>{title}</h4><p>{copy}</p></article>' for title, copy in cases)
    return f'<section class="content-section dark"><div class="container"><div class="section-label">Proof Points</div><h2 class="section-title">Real-World Signals Behind the Pillar</h2><div class="case-grid">{cards}</div></div></section>'

for slug, page in pages.items():
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{page["title"]}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    body = f'''<!-- Design philosophy: Forensic mirror extension. Preserve the original black-and-gold rhythm while expanding the information architecture through dedicated Services and pillar pages. -->
{page_head}<body class="body page-shell">{nav_html}
<section class="page-hero"><div class="page-hero-media" style="background-image:url('{page['hero_image']}')"></div><div class="page-hero-overlay"></div><div class="container page-hero-inner"><div class="_120-spacer"></div><div class="page-grid"><div><div class="page-eyebrow">{page['eyebrow']}</div><h1 class="page-display">{page['heading']}</h1><p class="page-intro">{page['intro']}</p></div><aside class="metric-panel"><div class="metric-value">{page['metric_value']}</div><div class="metric-copy">{page['metric_copy']}</div></aside></div><div class="_120-spacer"></div></div></section>
{render_sections(page['sections'])}
{render_cases(page['cases'])}
<section class="cta-band"><div class="container"><div class="cta-panel"><div><h3>Build the next conversation around this pillar.</h3><p>{page['cta']}</p></div><div class="cta-links"><a class="cta-link primary" href="/contact-us">Contact Us</a><a class="cta-link" href="/services">Services Hub</a><a class="cta-link" href="/">Back to Homepage</a></div></div></div></section>
{shared_footer}'''
    out_dir = BASE / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')
