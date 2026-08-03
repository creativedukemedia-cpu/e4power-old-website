from bs4 import BeautifulSoup
from pathlib import Path

html = Path('/home/ubuntu/e4powerinc-clone/client/index.html').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

for i, section in enumerate(soup.find_all('section', recursive=True), start=1):
    sec_id = section.get('id', '')
    heading = ''
    for tag in ['h1', 'h2', 'h3', 'h4']:
        node = section.find(tag)
        if node and node.get_text(' ', strip=True):
            heading = node.get_text(' ', strip=True)
            break
    summary = ''
    summary_node = section.find('summary')
    if summary_node and summary_node.get_text(' ', strip=True):
        summary = summary_node.get_text(' ', strip=True)
    print(f'{i:02d} | id={sec_id or "(none)"} | heading={heading or "(none)"} | summary={summary or "(none)"}')
