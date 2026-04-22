from pathlib import Path
from bs4 import BeautifulSoup

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
html = path.read_text(encoding='utf-8')
comment = ''
if html.startswith('<!--'):
    end = html.find('-->')
    if end != -1:
        comment = html[:end + 3] + '\n'
        html = html[end + 3:]

soup = BeautifulSoup(html, 'html.parser')
body = soup.body
if body is None:
    raise SystemExit('No body found in homepage HTML')

order = ['educate', 'empower', 'elevate', 'engage']
section_map = {}
for section_id in order:
    node = body.find('section', id=section_id)
    if node is None:
        raise SystemExit(f'Missing section: {section_id}')
    section_map[section_id] = node.extract()

footer = body.find('footer')
if footer is None:
    raise SystemExit('No footer found')

for section_id in order:
    footer.insert_before(section_map[section_id])

path.write_text(comment + str(soup), encoding='utf-8')
print('Reordered sections:', ', '.join(order))
