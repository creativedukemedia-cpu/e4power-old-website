from pathlib import Path

ROOT = Path('/home/ubuntu/e4powerinc-clone/client')
FILES = [
    ROOT / 'index.html',
    ROOT / 'contact-us' / 'index.html',
    ROOT / 'educate' / 'index.html',
    ROOT / 'elevate' / 'index.html',
    ROOT / 'empower' / 'index.html',
    ROOT / 'engage' / 'index.html',
    ROOT / 'services' / 'index.html',
    ROOT / 'team' / 'index.html',
]

HOMEPAGE_OLD = '<a href="/contact-us" onclick="document.body.classList.remove(\'mobile-nav-open\'); document.querySelector(\'.reference-topbar-toggle\')?.setAttribute(\'aria-expanded\',\'false\');">CONTACT</a>'
HOMEPAGE_NEW = '<a href="/content/index.html" onclick="document.body.classList.remove(\'mobile-nav-open\'); document.querySelector(\'.reference-topbar-toggle\')?.setAttribute(\'aria-expanded\',\'false\');">INSIGHTS</a><a href="/contact-us" onclick="document.body.classList.remove(\'mobile-nav-open\'); document.querySelector(\'.reference-topbar-toggle\')?.setAttribute(\'aria-expanded\',\'false\');">CONTACT</a>'

SECONDARY_OLD = '<li><a class="nav-link" href="/engage/">ENGAGE</a></li></ul>'
SECONDARY_NEW = '<li><a class="nav-link" href="/engage/">ENGAGE</a></li><li><a class="nav-link" href="/content/index.html">INSIGHTS</a></li></ul>'

for path in FILES:
    text = path.read_text()
    original = text
    if path.name == 'index.html' and path.parent == ROOT:
        if '/content/index.html' not in text:
            text = text.replace(HOMEPAGE_OLD, HOMEPAGE_NEW)
    else:
        if '/content/index.html' not in text:
            text = text.replace(SECONDARY_OLD, SECONDARY_NEW)
    if text != original:
        path.write_text(text)
        print(f'updated {path}')
    else:
        print(f'unchanged {path}')
