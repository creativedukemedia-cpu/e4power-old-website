from bs4 import BeautifulSoup
from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.body

marquee_section = body.find('section', class_=lambda c: c and 'partner-marquee-section' in c.split(), recursive=False)
elevate = body.find('section', id='elevate', recursive=False)
if marquee_section is None or elevate is None:
    raise SystemExit('Required sections not found')

# Find heading block currently under hero.
heading_block = None
for block in marquee_section.find_all('div', class_='main-content-block'):
    if block.find('h3', string=lambda s: s and 'Partners(curent/previous)' in s):
        heading_block = block
        break
if heading_block is None:
    print('Partners header already not under hero')
    raise SystemExit(0)

# Find insertion point in Elevate near the testimonials end, before the marquee if present.
existing_marquee_in_elevate = elevate.find('div', attrs={'wb-data': 'marquee'})
if existing_marquee_in_elevate is not None:
    existing_marquee_in_elevate.insert_before(heading_block.extract())
else:
    # fallback append near end of elevate container
    container = elevate.find('div', class_='container') or elevate
    container.append(heading_block.extract())

# If the marquee section container only contains the marquee after removal, keep it as-is.
path.write_text(str(soup), encoding='utf-8')
print('Restored Partners header to Elevate section while keeping marquee under hero')
