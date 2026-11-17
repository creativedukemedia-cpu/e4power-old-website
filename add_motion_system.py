from pathlib import Path
from bs4 import BeautifulSoup

BASE = Path('/home/ubuntu/e4powerinc-clone/client')
HTML_FILES = sorted(BASE.glob('**/index.html'))

HEAD_FLAG = 'motion-system-head'
SCRIPT_FLAG = 'motion-system-script'

HEAD_BLOCK = '''
<script id="motion-system-boot">document.documentElement.classList.add('js-motion');</script>
<style id="motion-system-head">
html.js-motion [data-reveal]{opacity:0;transform:translate3d(0,42px,0);transition-property:opacity,transform;transition-duration:900ms;transition-timing-function:cubic-bezier(.2,.8,.2,1);will-change:opacity,transform;}
html.js-motion [data-reveal="soft"]{transform:translate3d(0,24px,0);transition-duration:820ms;}
html.js-motion [data-reveal="line"]{transform:scaleX(.86);transform-origin:left center;transition-duration:980ms;}
html.js-motion [data-reveal="zoom"]{transform:scale(1.04);transition-duration:1100ms;}
html.js-motion [data-reveal].is-visible{opacity:1;transform:none;}
html.js-motion [data-reveal].is-visible[data-reveal="line"]{transform:scaleX(1);}
html.js-motion [data-reveal-stagger="1"]{transition-delay:90ms;}
html.js-motion [data-reveal-stagger="2"]{transition-delay:180ms;}
html.js-motion [data-reveal-stagger="3"]{transition-delay:270ms;}
html.js-motion [data-reveal-stagger="4"]{transition-delay:360ms;}
html.js-motion [data-reveal-stagger="5"]{transition-delay:450ms;}
html.js-motion .service-preview-shell,
html.js-motion .metric-panel,
html.js-motion .service-card,
html.js-motion .relation-card,
html.js-motion .case-card,
html.js-motion .cta-panel{backface-visibility:hidden;}
@media (prefers-reduced-motion: reduce){
  html.js-motion [data-reveal]{opacity:1 !important;transform:none !important;transition:none !important;}
}
</style>
'''

SCRIPT_BLOCK = '''
<script id="motion-system-script">
(function(){
  const nodes = Array.from(document.querySelectorAll('[data-reveal]'));
  if(!nodes.length){return;}
  const show = (el) => el.classList.add('is-visible');
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    nodes.forEach(show);
    return;
  }
  const io = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if(entry.isIntersecting){
        show(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  nodes.forEach((node) => io.observe(node));
  requestAnimationFrame(() => {
    nodes.forEach((node) => {
      const rect = node.getBoundingClientRect();
      if(rect.top < window.innerHeight * 0.9){
        show(node);
        io.unobserve(node);
      }
    });
  });
})();
</script>
'''


def tag_reveal(el, kind='soft', stagger=None):
    if el is None:
        return
    el['data-reveal'] = kind
    if stagger is not None:
        el['data-reveal-stagger'] = str(stagger)


for path in HTML_FILES:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')

    head = soup.head
    if head and not head.find(id=HEAD_FLAG):
        head.append(BeautifulSoup(HEAD_BLOCK, 'html.parser'))

    body = soup.body
    if body and not body.find(id=SCRIPT_FLAG):
        body.append(BeautifulSoup(SCRIPT_BLOCK, 'html.parser'))

    if path == BASE / 'index.html':
        hero_blocks = soup.select('.hero-block')
        for i, block in enumerate(hero_blocks, start=1):
            tag_reveal(block, 'soft', i)
        for shell in soup.select('.service-preview-shell'):
            tag_reveal(shell, 'soft')
            tag_reveal(shell.select_one('.service-preview-top'), 'soft')
            cards = shell.select('.service-preview-card')
            for i, card in enumerate(cards, start=1):
                tag_reveal(card, 'soft', i)
    else:
        tag_reveal(soup.select_one('.page-hero-media'), 'zoom')
        tag_reveal(soup.select_one('.page-eyebrow'), 'soft')
        tag_reveal(soup.select_one('.page-display'), 'soft', 1)
        tag_reveal(soup.select_one('.page-intro'), 'soft', 2)
        tag_reveal(soup.select_one('.metric-panel'), 'soft', 3)
        for section in soup.select('.content-section'):
            tag_reveal(section.select_one('.section-label'), 'soft')
            tag_reveal(section.select_one('.section-title'), 'soft', 1)
            tag_reveal(section.select_one('.section-copy'), 'soft', 2)
            for i, card in enumerate(section.select('.service-card'), start=1):
                tag_reveal(card, 'soft', i)
            for i, card in enumerate(section.select('.relation-card'), start=1):
                tag_reveal(card, 'soft', i)
            for i, card in enumerate(section.select('.case-card'), start=1):
                tag_reveal(card, 'soft', i)
        tag_reveal(soup.select_one('.cta-panel'), 'soft')

    path.write_text(str(soup), encoding='utf-8')
    print(f'Updated {path}')
