from pathlib import Path

ROOT = Path('/home/ubuntu/e4powerinc-clone/client')
FILES = [
    ROOT / 'index.html',
    ROOT / 'services' / 'index.html',
    ROOT / 'educate' / 'index.html',
    ROOT / 'empower' / 'index.html',
    ROOT / 'elevate' / 'index.html',
    ROOT / 'engage' / 'index.html',
    ROOT / 'contact-us' / 'index.html',
    ROOT / 'team' / 'index.html',
]
FILES.extend((ROOT / 'team-members').glob('*/index.html'))

STYLE = """<style id=\"services-row-hitbox\">\n.nav-menu-two li{position:relative;}\n.nav-menu-two .nav-link{display:block;width:100%;position:relative;z-index:3;}\n.nav-menu-two .menu-services-link{cursor:pointer;}\n.nav-menu-two .menu-services-row{position:relative;}\n</style>"""

for path in FILES:
    text = path.read_text()
    text = text.replace(
        '<li><a class="nav-link" href="/services/">SERVICES</a></li>',
        '<li class="menu-services-row"><a class="nav-link menu-services-link" href="/services/" onclick="window.location.href=\'/services/\'; return false;">SERVICES</a></li>'
    )
    if 'id="services-row-hitbox"' not in text:
        text = text.replace('</head>', STYLE + '\n</head>')
    path.write_text(text)

print(f'Updated {len(FILES)} files')
