from pathlib import Path

BASE = Path('/home/ubuntu/e4powerinc-clone/client')
TARGETS = {
    'href="/services"': 'href="/services/"',
    'href="/educate"': 'href="/educate/"',
    'href="/empower"': 'href="/empower/"',
    'href="/elevate"': 'href="/elevate/"',
    'href="/engage"': 'href="/engage/"',
}

for html_path in BASE.glob('**/index.html'):
    text = html_path.read_text(encoding='utf-8')
    original = text
    for old, new in TARGETS.items():
        text = text.replace(old, new)
    if text != original:
        html_path.write_text(text, encoding='utf-8')
        print(f'Updated {html_path}')
