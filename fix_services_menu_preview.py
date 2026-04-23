from pathlib import Path

ROOT = Path('/home/ubuntu/e4powerinc-clone/client')
TARGETS = [
    ROOT / 'index.html',
    ROOT / 'contact-us' / 'index.html',
    ROOT / 'services' / 'index.html',
    ROOT / 'educate' / 'index.html',
    ROOT / 'empower' / 'index.html',
    ROOT / 'elevate' / 'index.html',
    ROOT / 'engage' / 'index.html',
    ROOT / 'team' / 'index.html',
]
TARGETS.extend((ROOT / 'team-members').glob('*/index.html'))

SCRIPT = '''<script id="services-nav-hardening">
(function(){
  const targetHref = '/services/';
  const bind = () => {
    document.querySelectorAll('a.nav-link').forEach((link) => {
      const label = (link.textContent || '').trim().toUpperCase();
      if(label !== 'SERVICES') return;
      link.setAttribute('href', targetHref);
      link.addEventListener('click', function(event){
        event.preventDefault();
        event.stopPropagation();
        window.location.assign(targetHref);
      }, { capture: true });
      const li = link.closest('li');
      if(li){
        li.addEventListener('click', function(event){
          const hit = event.target.closest('a.nav-link');
          if(hit === link) return;
          event.preventDefault();
          event.stopPropagation();
          window.location.assign(targetHref);
        }, { capture: true });
      }
    });
  };
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', bind, { once: true });
  } else {
    bind();
  }
})();
</script>'''

for path in TARGETS:
    text = path.read_text()
    start = '<script id="services-nav-hardening">'
    if start in text:
      before = text.split(start)[0]
      after = text.split('</script>', 1)[1] if '</script>' in text.split(start,1)[1] else ''
      # safer full replacement
      pre, rest = text.split(start, 1)
      _, post = rest.split('</script>', 1)
      text = pre + SCRIPT + post
    else:
      text = text.replace('</body>', SCRIPT + '\n</body>')
    path.write_text(text)

print(f'Patched {len(TARGETS)} files')
