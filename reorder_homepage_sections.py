from bs4 import BeautifulSoup
from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.body

sections = body.find_all('section', recursive=False)
if len(sections) < 6:
    raise SystemExit(f'Expected at least 6 top-level sections, found {len(sections)}')

hero = sections[0]
metrics = sections[1]
by_id = {section.get('id'): section for section in sections if section.get('id')}

required_ids = ['educate', 'empower', 'elevate', 'engage']
missing = [sid for sid in required_ids if sid not in by_id]
if missing:
    raise SystemExit(f'Missing expected sections: {missing}')

new_order = [
    hero,
    metrics,
    by_id['elevate'],
    by_id['empower'],
    by_id['educate'],
    by_id['engage'],
]

for section in new_order:
    section.extract()

# Insert the reordered sections before the first footer if present, otherwise append to body.
footer = body.find('footer', recursive=False)
insert_before = footer if footer else None
for section in new_order:
    if insert_before is not None:
        insert_before.insert_before(section)
    else:
        body.append(section)

path.write_text(str(soup), encoding='utf-8')
print('Reordered homepage sections: hero -> metrics -> elevate -> empower -> educate -> engage')
