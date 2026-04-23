from pathlib import Path
from bs4 import BeautifulSoup

BASE = Path('/home/ubuntu/e4powerinc-clone/client')

NAV_HTML = '''<ul class="nav-menu-two w-list-unstyled" role="list"><li><a class="nav-link" href="/services/">SERVICES</a></li><li><a class="nav-link" href="/educate/">EDUCATE</a></li><li><a class="nav-link" href="/empower/">EMPOWER</a></li><li><a class="nav-link" href="/elevate/">ELEVATE</a></li><li><a class="nav-link" href="/engage/">ENGAGE</a></li></ul>'''

PREVIEW_CSS = '''
<style id="service-preview-styles">
.service-preview-shell{margin-top:5rem;border:1px solid rgba(226,178,76,.22);background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.015));padding:2.7rem 2.3rem;}
.service-preview-top{display:flex;justify-content:space-between;align-items:end;gap:2rem;flex-wrap:wrap;}
.service-preview-kicker{color:#e2b24c;text-transform:uppercase;letter-spacing:.18em;font-size:.82rem;}
.service-preview-title{color:#f7f1e8;margin:.85rem 0 0;text-transform:uppercase;font-size:2.2rem;line-height:1.05;max-width:12ch;}
.service-preview-copy{color:#d4c8b8;font-size:1.08rem;line-height:1.9;max-width:40rem;margin-top:1rem;}
.service-preview-cta{display:inline-flex;align-items:center;gap:.65rem;color:#0f0b07;background:#e2b24c;border:1px solid #e2b24c;padding:.95rem 1.2rem;text-decoration:none;text-transform:uppercase;letter-spacing:.12em;font-size:.8rem;white-space:nowrap;}
.service-preview-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin-top:2rem;}
.service-preview-card{border:1px solid rgba(255,255,255,.08);background:rgba(0,0,0,.18);padding:1.25rem;min-height:11.5rem;}
.service-preview-card h4{color:#f0bf5d;margin:0 0 .75rem;text-transform:uppercase;font-size:1rem;line-height:1.3;}
.service-preview-card p{color:#e6dccf;font-size:1.03rem;line-height:1.82;margin:0;}
@media screen and (max-width: 991px){.service-preview-grid{grid-template-columns:1fr;}.service-preview-shell{padding:1.8rem;}.service-preview-title{font-size:1.8rem;max-width:none;}}
</style>
'''

PREVIEWS = {
    'educate': {
        'kicker': 'Broader Services in Educate',
        'title': 'Learning Services that Build Internal Capacity',
        'copy': 'Educate can now signal that this pillar includes more than workshop topics. It can lead visitors into speaking engagements, training programs, and technology-literacy offerings that improve institutional readiness.',
        'cards': [
            ('Speaking Engagements', 'Keynotes, strategic sessions, and leadership talks for institutional audiences.'),
            ('Workshops & Training', 'Structured learning programs for grant strategy, proposal review, partnerships, and compliance.'),
            ('AI & Technology Literacy', 'Practical education that helps teams understand modern tools without losing mission focus.'),
        ],
        'href': '/educate/',
        'label': 'Explore Educate',
    },
    'empower': {
        'kicker': 'Broader Services in Empower',
        'title': 'Strategic Services that Increase Competitiveness',
        'copy': 'Empower can become the clearest bridge between ambition and action by highlighting readiness assessments, intellectual property, proposal strategy, innovation-minded advisory services, and the new IT and Application Development tier.',
        'cards': [
            ('Grant Writing', 'Pre-award strategy and proposal-development support from opportunity discovery to submission.'),
            ('Readiness Assessments', 'Institutional reviews that reveal gaps, strengths, and fundable next moves.'),
            ('IT & App Development', 'Custom portals, web apps, websites, and IT support that expand client delivery capacity.'),
        ],
        'href': '/empower/',
        'label': 'Explore Empower',
    },
    'elevate': {
        'kicker': 'Broader Services in Elevate',
        'title': 'Execution Services that Protect Awarded Work',
        'copy': 'Elevate can now show that E4 Power supports what happens after the award through project management, financial stewardship, grant-management systems, and continuity-minded operational support.',
        'cards': [
            ('Grant Management', 'Post-award reporting, compliance, and closeout support.'),
            ('Project Management', 'Structured delivery systems for complex research and workforce initiatives.'),
            ('Financial Management', 'Budget oversight and fiscal controls aligned with federal expectations.'),
        ],
        'href': '/elevate/',
        'label': 'Explore Elevate',
    },
    'engage': {
        'kicker': 'Broader Services in Engage',
        'title': 'Advisory Entry Points that Begin the Partnership',
        'copy': 'Engage can evolve from a team introduction into the relational front door for E4 Power, connecting institutional discovery, readiness-led onboarding, and specialist-led advisory alignment.',
        'cards': [
            ('Institutional Discovery', 'Early conversations that clarify goals, constraints, and the highest-value starting point.'),
            ('Readiness-Led Onboarding', 'Practical entry work that sets a baseline for future strategy and delivery.'),
            ('Team-Led Partnership Model', 'Introductions to the specialists most relevant to a client’s mission and growth stage.'),
        ],
        'href': '/engage/',
        'label': 'Explore Engage',
    },
}


def preview_fragment(soup, data):
    wrapper = soup.new_tag('div', attrs={'class': 'service-preview-shell'})
    top = soup.new_tag('div', attrs={'class': 'service-preview-top'})
    left = soup.new_tag('div')
    kicker = soup.new_tag('div', attrs={'class': 'service-preview-kicker'})
    kicker.string = data['kicker']
    title = soup.new_tag('h3', attrs={'class': 'service-preview-title'})
    title.string = data['title']
    copy = soup.new_tag('p', attrs={'class': 'service-preview-copy'})
    copy.string = data['copy']
    left.extend([kicker, title, copy])
    cta = soup.new_tag('a', attrs={'class': 'service-preview-cta', 'href': data['href']})
    cta.string = data['label']
    top.extend([left, cta])
    grid = soup.new_tag('div', attrs={'class': 'service-preview-grid'})
    for heading, paragraph in data['cards']:
        card = soup.new_tag('article', attrs={'class': 'service-preview-card'})
        h4 = soup.new_tag('h4')
        h4.string = heading
        p = soup.new_tag('p')
        p.string = paragraph
        card.extend([h4, p])
        grid.append(card)
    wrapper.extend([top, grid])
    return wrapper


for html_path in sorted(BASE.glob('**/index.html')):
    text = html_path.read_text(encoding='utf-8')
    if 'service-preview-styles' in text:
        start = text.index('<style id="service-preview-styles">')
        end = text.index('</style>', start) + len('</style>')
        text = text[:start] + PREVIEW_CSS.strip() + text[end:]
    else:
        text = text.replace('</head>', PREVIEW_CSS + '\n</head>')
    soup = BeautifulSoup(text, 'html.parser')

    nav_menu = soup.select_one('nav.nav-menu-wrapper ul.nav-menu-two')
    if nav_menu is not None:
        nav_menu.replace_with(BeautifulSoup(NAV_HTML, 'html.parser').ul)

    footer_links = soup.select_one('.footer-links-div')
    if footer_links is not None:
        footer_links.clear()
        footer_markup = '''
        <a class="testimonial-text footer-link" href="/services/">SERVICES</a>
        <div class="testimonial-text footer-link">|</div>
        <a class="testimonial-text footer-link" href="/educate/">EDUCATE</a>
        <div class="testimonial-text footer-link">|</div>
        <a class="testimonial-text footer-link" href="/empower/">EMPOWER</a>
        <div class="testimonial-text footer-link">|</div>
        <a class="testimonial-text footer-link" href="/elevate/">ELEVATE</a>
        <div class="testimonial-text footer-link">|</div>
        <a class="testimonial-text footer-link" href="/engage/">ENGAGE</a>
        '''
        parsed = BeautifulSoup(footer_markup, 'html.parser')
        for child in parsed.contents:
            footer_links.append(child)

    if html_path == BASE / 'index.html':
        for preview in soup.select('.service-preview-shell'):
            preview.decompose()
        for section_id, data in PREVIEWS.items():
            section = soup.find('section', id=section_id)
            if section is None:
                continue
            anchor = section.find(class_='_120-spacer')
            preview = preview_fragment(soup, data)
            if anchor is not None:
                anchor.insert_before(preview)
            else:
                section.append(preview)

    html_path.write_text(str(soup), encoding='utf-8')
    print('Updated', html_path)
