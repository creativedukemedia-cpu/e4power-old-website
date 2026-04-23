from pathlib import Path
import re

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

custom_css = '''
<style>
.page-shell {
  --accent: #e2b24c;
  --accent-rgb: 226,178,76;
  --accent-strong: #f0bf5d;
  --accent-soft: rgba(226,178,76,0.14);
  --hero-sheen: rgba(226,178,76,0.16);
  --page-ink: #f7f1e8;
  --page-copy: #d6cab9;
  background: linear-gradient(180deg, #17110a 0%, #040404 34%, #0d0d0d 100%);
}
.page-shell.theme-services {
  --accent: #e2b24c;
  --accent-rgb: 226,178,76;
  --accent-strong: #f0bf5d;
  --accent-soft: rgba(226,178,76,0.16);
  --hero-sheen: rgba(226,178,76,0.18);
}
.page-shell.theme-educate {
  --accent: #fdfd02;
  --accent-rgb: 253,253,2;
  --accent-strong: #fff867;
  --accent-soft: rgba(253,253,2,0.14);
  --hero-sheen: rgba(253,253,2,0.15);
}
.page-shell.theme-empower {
  --accent: #02bce9;
  --accent-rgb: 2,188,233;
  --accent-strong: #6fdfff;
  --accent-soft: rgba(2,188,233,0.16);
  --hero-sheen: rgba(2,188,233,0.14);
}
.page-shell.theme-elevate {
  --accent: #ed028e;
  --accent-rgb: 237,2,142;
  --accent-strong: #ff5db6;
  --accent-soft: rgba(237,2,142,0.15);
  --hero-sheen: rgba(237,2,142,0.14);
}
.page-shell.theme-engage {
  --accent: #d4a86a;
  --accent-rgb: 212,168,106;
  --accent-strong: #efca97;
  --accent-soft: rgba(212,168,106,0.17);
  --hero-sheen: rgba(212,168,106,0.15);
}
.page-hero { position: relative; min-height: 80vh; display: flex; align-items: end; overflow: hidden; }
.page-hero::after { content: ''; position: absolute; inset: auto -10% -18% auto; width: 38rem; height: 38rem; border-radius: 999px; background: radial-gradient(circle, var(--hero-sheen) 0%, rgba(0,0,0,0) 68%); z-index: 1; }
.page-hero-media { position: absolute; inset: 0; background-size: cover; background-position: center; filter: grayscale(1); transform: scale(1.03); }
.page-hero-overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0.72) 68%, #050505 100%); }
.page-hero-inner { position: relative; z-index: 2; width: 100%; padding-top: 7rem; padding-bottom: 4rem; }
.page-grid { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(20rem, .8fr); gap: 4rem; align-items: end; }
.page-eyebrow { color: var(--accent); text-transform: uppercase; letter-spacing: .24em; font-size: .95rem; margin-bottom: 1.1rem; }
.page-display { color: var(--page-ink); text-transform: uppercase; line-height: .95; max-width: 12ch; margin: 0; }
.page-intro { color: #ddd0be; max-width: 44rem; font-size: 1.2rem; line-height: 1.8; margin-top: 1.5rem; }
.signature-chip-row { display: flex; flex-wrap: wrap; gap: .8rem; margin-top: 2rem; }
.signature-chip { display: inline-flex; align-items: center; gap: .5rem; padding: .72rem 1rem; border: 1px solid rgba(var(--accent-rgb),0.32); background: rgba(0,0,0,0.24); color: #f4ede2; text-transform: uppercase; letter-spacing: .1em; font-size: .78rem; }
.signature-chip::before { content: ''; width: .5rem; height: .5rem; border-radius: 999px; background: var(--accent); box-shadow: 0 0 18px rgba(var(--accent-rgb),0.45); }
.metric-panel { background: rgba(12, 12, 12, 0.76); border: 1px solid rgba(var(--accent-rgb),0.28); backdrop-filter: blur(12px); padding: 2.4rem; box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
.metric-kicker { color: var(--accent); text-transform: uppercase; letter-spacing: .16em; font-size: .82rem; margin-bottom: .9rem; }
.metric-value { color: var(--accent-strong); font-size: 3.25rem; line-height: 1; margin-bottom: .65rem; }
.metric-copy { color: #efe5d5; font-size: 1.08rem; line-height: 1.9; }
.content-section { position: relative; padding: 8.5rem 0; }
.content-section.dark { background: #050505; }
.content-section.charcoal { background: #130f0a; }
.content-section.band { background: linear-gradient(180deg, rgba(var(--accent-rgb),0.08) 0%, rgba(8,8,8,0.96) 60%); }
.content-section .section-label { color: var(--accent); text-transform: uppercase; letter-spacing: .18em; margin-bottom: 1rem; }
.content-section .section-title { color: var(--page-ink); margin: 0; text-transform: uppercase; }
.content-section .section-copy { color: var(--page-copy); font-size: 1.12rem; line-height: 1.95; max-width: 54rem; margin-top: 1.5rem; }
.section-split { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(18rem, .8fr); gap: 2rem; align-items: start; }
.section-panel { border: 1px solid rgba(var(--accent-rgb),0.24); background: rgba(255,255,255,0.03); padding: 1.4rem; color: #ece0cf; }
.section-panel-title { color: var(--accent); text-transform: uppercase; letter-spacing: .14em; font-size: .8rem; margin-bottom: .7rem; }
.section-panel p { margin: 0; font-size: 1rem; line-height: 1.8; }
.service-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem; margin-top: 3rem; }
.service-card { background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02)); border: 1px solid rgba(var(--accent-rgb),0.24); padding: 2rem 1.75rem; min-height: 18rem; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; }
.service-card::before { content: ''; position: absolute; inset: 0 0 auto 0; height: 3px; background: linear-gradient(90deg, var(--accent) 0%, rgba(255,255,255,0) 85%); }
.service-tag { color: var(--accent); text-transform: uppercase; letter-spacing: .18em; font-size: .8rem; }
.service-card h3 { color: #f7f0e3; margin: .9rem 0 0; text-transform: uppercase; font-size: 1.45rem; line-height: 1.2; }
.service-card p { color: #d1c4b3; font-size: 1.08rem; line-height: 1.88; margin-top: 1rem; }
.service-points { margin-top: 1.5rem; padding-left: 1.2rem; color: #efe5d5; }
.service-points li { font-size: 1.03rem; line-height: 1.78; margin-bottom: .7rem; }
.relation-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; margin-top: 2.4rem; }
.relation-card { border: 1px solid rgba(var(--accent-rgb),0.18); background: rgba(255,255,255,0.03); padding: 1.4rem; }
.relation-card h4 { color: var(--accent-strong); margin: 0 0 .7rem; text-transform: uppercase; }
.relation-card p { color: #d7ccbc; font-size: 1.04rem; line-height: 1.82; margin: 0; }
.case-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin-top: 2.5rem; }
.case-card { background: #090909; border-left: 2px solid var(--accent); padding: 1.8rem; }
.case-card .case-kicker { color: var(--accent); letter-spacing: .18em; text-transform: uppercase; font-size: .8rem; }
.case-card h4 { color: #f7f1e7; margin: .75rem 0; text-transform: uppercase; }
.case-card p { color: #cfc2b1; font-size: 1.05rem; line-height: 1.85; margin: 0; }
.cta-band { padding: 6rem 0 7rem; background: linear-gradient(180deg, rgba(var(--accent-rgb),0.08) 0%, #050505 100%); }
.cta-panel { border: 1px solid rgba(var(--accent-rgb),0.3); background: rgba(255,255,255,0.03); padding: 2.6rem; display: grid; grid-template-columns: 1.2fr auto; gap: 2rem; align-items: center; }
.cta-panel h3 { color: #f7f1e8; margin: 0; text-transform: uppercase; }
.cta-panel p { color: #d5c9b7; font-size: 1.08rem; margin: .8rem 0 0; line-height: 1.85; max-width: 48rem; }
.cta-links { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: end; }
.cta-link { border: 1px solid rgba(var(--accent-rgb),0.45); color: #f2ede5; padding: .9rem 1.15rem; text-transform: uppercase; text-decoration: none; letter-spacing: .1em; }
.cta-link.primary { background: var(--accent); color: #120d08; }
@media screen and (max-width: 991px) {
  .page-grid, .cta-panel, .service-grid, .relation-grid, .case-grid, .section-split { grid-template-columns: 1fr; }
  .page-display { max-width: none; }
  .cta-links { justify-content: start; }
  .page-hero-inner { padding-top: 5.5rem; padding-bottom: 3.5rem; }
  .content-section { padding: 6rem 0; }
}
</style>
'''

pages = {
    'services': {
        'theme_class': 'theme-services',
        'title': 'Services | E4 Power',
        'eyebrow': 'Services Hub',
        'heading': 'Eight Service Tiers Built for Institutional Growth',
        'intro': 'The Services Hub is the clearest view of everything E4 Power delivers beyond grant writing. It organizes advisory, execution, training, financial, intellectual-property, and digital-delivery capabilities into one navigable system tied directly to Educate, Empower, Elevate, and Engage.',
        'signature_chips': ['Capability Index', 'Eight Service Tiers', 'Pillar-Mapped Delivery'],
        'metric_kicker': 'Capability Overview',
        'metric_value': 'SERVICES',
        'metric_copy': 'Use this page as the primary capability index. Each service tier connects to a pillar pathway so visitors can move from the broad overview into a more focused explanation of how E4 Power supports institutional growth.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d87ffc6c9537fa6761ea75_workshop_picture.webp',
        'proof_label': 'Proof Points',
        'proof_title': 'Real-World Signals Behind the Pillar',
        'sections': [
            {
                'tone': 'charcoal',
                'label': 'Service Architecture',
                'title': 'An Eight-Tier Services Hub that Mirrors the BRIDGE Mindset',
                'copy': 'The Services page functions as the capability index for decision-makers. It explains what E4 Power does beyond proposal writing, while also clarifying how those capabilities align with Educate, Empower, Elevate, and Engage.',
                'panel_title': 'Why this page matters',
                'panel_copy': 'This hub is meant to orient institutional decision-makers before they branch into a more detailed pillar page. It works best as the broadest entry point after the homepage.',
                'cards': [
                    ('Pre-Award Strategy', 'Empower', 'Grant writing, readiness planning, opportunity identification, and proposal-development support for HBCUs, ERIs, MSIs, and nonprofits.', ['Opportunity identification', 'Proposal development', 'Competitive positioning']),
                    ('Post-Award Stewardship', 'Elevate', 'Grant management, compliance support, and closeout discipline that protect agency relationships after an award is secured.', ['Award setup and reporting', 'Compliance coordination', 'Closeout readiness']),
                    ('Project & Program Management', 'Elevate', 'Structured execution support for research, workforce, and multi-institution initiatives requiring dependable delivery systems.', ['Risk-aware execution', 'Cross-team coordination', 'Milestone accountability']),
                    ('Readiness Assessments', 'Engage', 'Institutional discovery work that clarifies infrastructure, staffing, and systems gaps before a funding pursuit begins.', ['SWOT review', 'Infrastructure mapping', 'Growth prioritization']),
                    ('Intellectual Property Services', 'Empower', 'Innovation-protection and commercialization support led by IP specialists to help institutions move ideas from lab to market.', ['Patent strategy', 'IP education', 'Commercialization support']),
                    ('Financial Management', 'Elevate', 'Budget development, fiscal oversight, and audit-conscious financial management aligned with federal requirements.', ['Allowable cost tracking', 'Budget oversight', 'Fiscal compliance']),
                    ('Workshops & Speaking', 'Educate', 'Capacity-building engagements that translate expertise into teachable systems for institutional teams and leadership audiences.', ['Workshop design', 'Speaking engagements', 'Training delivery']),
                    ('IT & Application Development', 'Empower', 'Technology delivery services that help organizations build the digital infrastructure behind growth, service delivery, and operational efficiency.', ['Custom portals', 'Web apps and websites', 'Ongoing IT support']),
                ],
                'relations': [
                    ('Educate', 'Translates expertise into workshops, speaking, and skill-building for faculty, researchers, and leaders.'),
                    ('Empower', 'Advances competitiveness through strategic planning, proposals, IP, innovation, and digital-product development.'),
                    ('Elevate', 'Supports funded work through stewardship, execution systems, financial controls, and outcome visibility.'),
                    ('Engage', 'Creates the institutional partnership doorway through discovery, readiness, and advisory collaboration.'),
                ],
            },
            {
                'tone': 'band',
                'label': 'Digital Delivery',
                'title': 'Technology Services that Extend E4 Power Beyond Advisory Work',
                'copy': 'The new IT and Application Development tier gives E4 Power a clearer operational offering for partners that need more than strategy. It positions the firm to support custom portals, web applications, websites, and day-to-day IT support in a way that complements institutional growth and modernization.',
                'panel_title': 'Digital scope',
                'panel_copy': 'This is the clearest place to show that E4 Power can build infrastructure, not only advise on it. It should feel operational and forward-looking.',
                'cards': [
                    ('Custom Portals', 'Empower', 'Secure portal experiences for students, partners, internal teams, or community-facing programs that require structured access and workflow support.', ['Partner portals', 'Program dashboards', 'Operational access points']),
                    ('Web Applications & Websites', 'Empower', 'Digital experiences designed to support outreach, service delivery, internal operations, or public-facing storytelling.', ['Custom web apps', 'Institutional websites', 'Workflow-driven experiences']),
                    ('IT Support Services', 'Elevate', 'Practical technical support that helps clients maintain systems, resolve issues, and keep new digital infrastructure functioning well after launch.', ['Support and troubleshooting', 'Maintenance guidance', 'Operational continuity']),
                ],
                'relations': [],
            },
        ],
        'cases': [
            ('Full Lifecycle', 'E4 Power is positioned as a single partner from idea to impact, combining readiness, strategy, execution, financial oversight, and digital delivery rather than treating each service in isolation.'),
            ('Institutional Fit', 'The service structure is especially relevant for HBCUs, ERIs, MSIs, nonprofits, and research-led organizations that need both strategic guidance and operational delivery support.'),
        ],
        'cta': 'Use this page as the top-level entry point in the navigation, then route visitors into the pillar pages for a more focused understanding of how services show up within each part of the E4 Power model.'
    },
    'educate': {
        'theme_class': 'theme-educate',
        'title': 'Educate | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Educate: Training, Speaking, and Capacity Building',
        'intro': 'Educate should show how E4 Power turns experience into practical knowledge. This page expands the homepage pillar into a deeper training-focused offer for institutions that need stronger internal capability, not just outsourced support.',
        'signature_chips': ['Training Pathway', 'Workshop-Led Growth', 'Leadership Readiness'],
        'metric_kicker': 'Learning impact',
        'metric_value': '30+',
        'metric_copy': 'Workshops and speaking-led engagements reinforce the pillar by helping faculty, researchers, and administrators build competitive habits before and during funding pursuits.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d899f54126036ff52c6474_washington%20dc.webp',
        'proof_label': 'Learning Signals',
        'proof_title': 'Why Educate Works as a Distinct Entry Point',
        'sections': [
            {
                'tone': 'band',
                'label': 'Educate Services',
                'title': 'Learning Experiences that Increase Institutional Readiness',
                'copy': 'The deck positions speaking engagements and workshops as a formal service line. On the site, Educate should present those offerings as strategic learning systems that sharpen teams for grant competition, partnership-building, leadership development, and innovation readiness.',
                'panel_title': 'Page emphasis',
                'panel_copy': 'Educate should feel like a learning environment: clear, structured, confidence-building, and slightly brighter than the other pillar pages.',
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
        'theme_class': 'theme-empower',
        'title': 'Empower | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Empower: Strategy, Opportunity Creation, Digital Build, and Innovation Support',
        'intro': 'Empower should become the strategy-heavy pillar page. It is where E4 Power explains how it helps institutions move from ambition to competitive action through proposal development, readiness planning, intellectual property support, digital-product creation, and innovation-minded advisory services.',
        'signature_chips': ['Competitive Strategy', 'Digital Build', 'Innovation Support'],
        'metric_kicker': 'Competitive posture',
        'metric_value': '78%',
        'metric_copy': 'Proposal-development success, modernization strategy, and custom digital delivery make this pillar the clearest place to show how E4 Power helps clients become more competitive before funding is awarded and as new capacity is built.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d86ed2cf005d4f005b60bd_1.webp',
        'proof_label': 'Strategic Signals',
        'proof_title': 'Why Empower Should Feel Like the Forward-Motion Pillar',
        'sections': [
            {
                'tone': 'band',
                'label': 'Empower Services',
                'title': 'Services that Strengthen Competitive Positioning and Delivery Capacity',
                'copy': 'Empower should hold the services that improve institutional confidence and competitiveness before or alongside major opportunities. That includes pre-award support, readiness reviews, intellectual property strategy, carefully framed technology and AI integration support, and the new IT and Application Development tier.',
                'panel_title': 'Page emphasis',
                'panel_copy': 'Empower should feel sharper and more directional than the other pages, with a technology-forward edge that supports the new digital service tier.',
                'cards': [
                    ('Grant Writing', 'Pre-Award', 'End-to-end proposal support from opportunity identification through narrative assembly, approvals, and submission discipline.', ['Opportunity scans', 'Proposal writing', 'Submission support']),
                    ('Readiness Assessments', 'Capacity Services', 'Institutional reviews that identify infrastructure gaps, growth priorities, and realistic pathways for future funding.', ['SWOT analysis', 'Infrastructure review', 'Strategic implementation baseline']),
                    ('Intellectual Property', 'Innovation Support', 'Protection and commercialization services that help researchers identify, secure, and position innovation assets.', ['Patent guidance', 'Researcher education', 'Commercialization positioning']),
                    ('IT & Application Development', 'Digital Delivery', 'Custom technology services for organizations that need portals, web applications, websites, or dependable IT support as part of their broader growth strategy.', ['Custom portals', 'Web apps and websites', 'IT support']),
                    ('IT Solutions & AI Integration', 'Modernization', 'Advisory support for institutions exploring automation, AI, and technology-enabled efficiency as part of long-term research and operational growth.', ['Automation ideas', 'LLM integration framing', 'Process modernization']),
                ],
                'relations': [
                    ('Educate', 'Training improves readiness for the strategic work introduced here.'),
                    ('Empower', 'Primary home for opportunity creation, proposal strategy, innovation support, and digital-product development.'),
                    ('Elevate', 'Strong pre-award strategy and digital build work still depend on disciplined execution after launch or award.'),
                    ('Engage', 'Discovery conversations and readiness reviews often begin the work shown on this page.'),
                ],
            }
        ],
        'cases': [
            ('NSF HBCU-UP', 'The capabilities deck highlights a funded NSF HBCU-UP implementation proposal developed after more than two decades without an NSF award, reinforcing the strategic impact of this pillar.'),
            ('EPA Proposal Development', 'The deck also references leadership on a multi-million-dollar EPA proposal for biogenic building materials, showing that the pillar can support highly technical work as well as institutional strategy.'),
        ],
        'cta': 'Use Empower as the destination for prospects who want to know how E4 Power improves their competitiveness before the award, especially where funding, innovation, technology, and strategic capacity intersect.'
    },
    'elevate': {
        'theme_class': 'theme-elevate',
        'title': 'Elevate | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Elevate: Execution, Stewardship, and Measurable Delivery',
        'intro': 'Elevate should move the narrative from winning support to executing it well. This page clarifies that E4 Power does not stop at proposal submission; it also helps institutions manage awards, run projects, and maintain financial and compliance integrity.',
        'signature_chips': ['Execution Systems', 'Stewardship', 'Outcome Visibility'],
        'metric_kicker': 'Delivery confidence',
        'metric_value': '>$100M',
        'metric_copy': 'The capabilities deck positions E4 Power as a post-award and execution partner, not only a proposal partner. Elevate is where that fuller story becomes visible on the site.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d86ed2b8c8966dea03dc39_3.webp',
        'proof_label': 'Execution Signals',
        'proof_title': 'Why Elevate Should Feel More Operational and Outcome-Oriented',
        'sections': [
            {
                'tone': 'band',
                'label': 'Elevate Services',
                'title': 'Services that Protect and Scale Awarded Work',
                'copy': 'Elevate should concentrate the post-award service lines that keep institutions compliant, organized, and outcomes-focused once funding is in motion. This makes the site’s promise more credible because it connects strategic wins with responsible delivery.',
                'panel_title': 'Page emphasis',
                'panel_copy': 'Elevate should feel more structured and procedural than the others, emphasizing accountability, continuity, and disciplined oversight.',
                'cards': [
                    ('Grant Management', 'Post-Award', 'Support from award acceptance through reporting and project closeout to protect institutional standing with funding agencies.', ['Reporting coordination', 'Compliance oversight', 'Award closeout']),
                    ('Project Management', 'Program Delivery', 'Structured delivery systems for complex research, workforce, and multi-institution initiatives.', ['Timeline management', 'Cross-team execution', 'Risk-aware coordination']),
                    ('Financial Management', 'Fiscal Oversight', 'Budget and spending oversight aligned with federal expectations so institutions can manage funds with confidence.', ['Drawdown support', 'Cost tracking', 'Audit-conscious stewardship']),
                    ('IT Support Continuity', 'Operational Support', 'Ongoing support and maintenance that help clients keep newly launched digital systems reliable and useful after delivery.', ['Support workflows', 'Maintenance guidance', 'Operational continuity']),
                ],
                'relations': [
                    ('Educate', 'Training can prepare teams for the stewardship responsibilities shown here.'),
                    ('Empower', 'The strongest strategy and digital build work still depend on disciplined execution after award or launch.'),
                    ('Elevate', 'Primary home for award stewardship, project management, fiscal oversight, and continuity support.'),
                    ('Engage', 'Ongoing partnerships deepen when E4 Power remains involved after funding is secured.'),
                ],
            }
        ],
        'cases': [
            ('UJIMA Collective', 'The deck references post-award management and reporting for a multi-partner NSF collaborative initiative, demonstrating how Elevate supports complex institutional coordination.'),
            ('Federal Oversight', 'Financial oversight examples and project-delivery case studies show how this pillar can speak to both compliance-sensitive administrators and program leaders.'),
        ],
        'cta': 'Use Elevate as the destination for visitors who need confidence that E4 Power can help protect awarded funding, keep teams aligned, support operational continuity, and deliver outcomes responsibly.'
    },
    'engage': {
        'theme_class': 'theme-engage',
        'title': 'Engage | E4 Power',
        'eyebrow': 'Pillar Page',
        'heading': 'Engage: Partnership Entry, Advisory Trust, and Institutional Alignment',
        'intro': 'Engage should become more than a team page. It should explain how institutions begin working with E4 Power through relationship-building, discovery, readiness discussions, and a collaborative understanding of what growth will require.',
        'signature_chips': ['Partnership Entry', 'Readiness Discovery', 'Trusted Advisory'],
        'metric_kicker': 'Relationship model',
        'metric_value': '10+',
        'metric_copy': 'The firm’s leadership bench, readiness methodology, and partnership orientation make Engage the right place to show how E4 Power enters organizations thoughtfully rather than transactionally.',
        'hero_image': 'https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5%2F68d857925f5c5c405f4b28a4_e4%20Power%20Background%20Vid-poster-00001.jpg',
        'proof_label': 'Partnership Signals',
        'proof_title': 'Why Engage Should Feel More Relational Than the Other Pillars',
        'sections': [
            {
                'tone': 'band',
                'label': 'Engage Services',
                'title': 'The Human and Strategic Entry Point into the Partnership',
                'copy': 'Engage should connect team credibility with the earliest stages of institutional work. It is the best home for readiness-led discovery, advisory alignment, and the relational side of the BRIDGE model that makes later strategy and delivery possible.',
                'panel_title': 'Page emphasis',
                'panel_copy': 'Engage should feel the most conversational and partnership-led of the pillar pages, with more emphasis on trust, fit, and how the work begins.',
                'cards': [
                    ('Institutional Discovery', 'Advisory Entry', 'Early conversations and strategic review sessions that identify goals, constraints, and where E4 Power can create the most value first.', ['Discovery meetings', 'Needs clarification', 'Initial roadmapping']),
                    ('Readiness-Led Onboarding', 'Capacity Services', 'A practical entry service that helps partners understand current systems, staffing, and funding readiness before moving into larger workstreams.', ['Baseline review', 'Gap identification', 'Priority sequencing']),
                    ('Team-Led Partnership Model', 'People & Expertise', 'A relationship-centered consulting model that introduces prospects to the specialists most relevant to their goals across strategy, finance, intellectual property, project delivery, training, and digital build services.', ['Executive introductions', 'Specialist alignment', 'Collaborative planning']),
                ],
                'relations': [
                    ('Educate', 'Workshops and speaking engagements can begin the relationship with trust and value.'),
                    ('Empower', 'Strategic, innovation, and application-development service lines often grow from the discovery and readiness work started here.'),
                    ('Elevate', 'Longer partnerships frequently continue into execution and post-award stewardship.'),
                    ('Engage', 'Primary home for discovery, readiness-led entry, and partnership orientation.'),
                ],
            }
        ],
        'cases': [
            ('Executive Bench', 'The team-led model is supported by leadership across grant strategy, intellectual property, finance, project management, speaking engagements, and digital delivery, which makes Engage a meaningful entry page rather than a simple biography section.'),
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
        panel_html = ''
        if section.get('panel_title') and section.get('panel_copy'):
            panel_html = f'<aside class="section-panel"><div class="section-panel-title">{section["panel_title"]}</div><p>{section["panel_copy"]}</p></aside>'
        parts.append(
            f'<section class="content-section {section["tone"]}"><div class="container"><div class="section-split"><div><div class="section-label">{section["label"]}</div><h2 class="section-title">{section["title"]}</h2><p class="section-copy">{section["copy"]}</p></div>{panel_html}</div>{render_cards(section["cards"])}{render_relations(section["relations"])}</div></section>'
        )
    return ''.join(parts)


def render_cases(page):
    cards = ''.join(f'<article class="case-card"><div class="case-kicker">Context</div><h4>{title}</h4><p>{copy}</p></article>' for title, copy in page['cases'])
    return f'<section class="content-section dark"><div class="container"><div class="section-label">{page["proof_label"]}</div><h2 class="section-title">{page["proof_title"]}</h2><div class="case-grid">{cards}</div></div></section>'


for slug, page in pages.items():
    page_head = base_head.replace('<title>E4 Power</title>', f'<title>{page["title"]}</title>')
    page_head = page_head.replace('</head>', custom_css + '\n</head>')
    chips = ''.join(f'<div class="signature-chip">{chip}</div>' for chip in page['signature_chips'])
    body = f'''<!-- Design philosophy: Forensic mirror extension. Preserve the original black-and-gold rhythm while giving each pillar page a distinct identity through accent color, emphasis, and section framing. -->
{page_head}<body class="body page-shell {page['theme_class']}">{nav_html}
<section class="page-hero"><div class="page-hero-media" style="background-image:url('{page['hero_image']}')"></div><div class="page-hero-overlay"></div><div class="container page-hero-inner"><div class="page-grid"><div><div class="page-eyebrow">{page['eyebrow']}</div><h1 class="page-display">{page['heading']}</h1><p class="page-intro">{page['intro']}</p><div class="signature-chip-row">{chips}</div></div><aside class="metric-panel"><div class="metric-kicker">{page['metric_kicker']}</div><div class="metric-value">{page['metric_value']}</div><div class="metric-copy">{page['metric_copy']}</div></aside></div></div></section>
{render_sections(page['sections'])}
{render_cases(page)}
<section class="cta-band"><div class="container"><div class="cta-panel"><div><h3>Build the next conversation around this pillar.</h3><p>{page['cta']}</p></div><div class="cta-links"><a class="cta-link primary" href="/contact-us">Contact Us</a><a class="cta-link" href="/services/">Services Hub</a><a class="cta-link" href="/">Back to Homepage</a></div></div></div></section>
{shared_footer}'''
    out_dir = BASE / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(body, encoding='utf-8')
    print('Wrote', out_dir / 'index.html')
