from bs4 import BeautifulSoup
from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.body
sections = body.find_all('section', recursive=False)
if len(sections) < 3:
    raise SystemExit('Unexpected homepage structure')

hero = sections[0]
metrics = sections[1]
elevate = body.find('section', id='elevate', recursive=False)
if elevate is None:
    raise SystemExit('Could not find elevate section')

marquee = elevate.find('div', attrs={'wb-data': 'marquee'})
if marquee is None:
    raise SystemExit('Could not find marquee banner')

heading_block = None
for candidate in elevate.find_all('div', class_='main-content-block'):
    classes = candidate.get('class', [])
    if 'transparent' in classes and candidate.find('h3', string=lambda s: s and 'Partners(curent/previous)' in s):
        heading_block = candidate
        break
if heading_block is None:
    raise SystemExit('Could not find partners heading block')

# If already moved, exit cleanly.
next_sections = hero.find_next_siblings('section', recursive=False)
if next_sections:
    first_after_hero = next_sections[0]
    if first_after_hero.find('div', attrs={'wb-data': 'marquee'}) is not None:
        print('Partner marquee already sits under hero')
        raise SystemExit(0)

heading_block.extract()
marquee.extract()

new_section = soup.new_tag('section', attrs={'class': 'section dark-gray partner-marquee-section'})
container = soup.new_tag('div', attrs={'class': 'container'})
container.append(heading_block)
container.append(marquee)
new_section.append(container)

metrics.insert_before(new_section)

path.write_text(str(soup), encoding='utf-8')
print('Moved partners heading and rotating marquee directly under hero')
