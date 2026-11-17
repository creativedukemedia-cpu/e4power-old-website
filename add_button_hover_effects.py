from pathlib import Path

BASE = Path('/home/ubuntu/e4powerinc-clone/client')
HTML_FILES = sorted(BASE.glob('**/index.html'))

HOVER_BLOCK = """
<style id="button-hover-system">
.service-preview-cta,
.cta-link,
.submit-button.w-button,
.link-block,
.text-link {
  transition: transform 260ms cubic-bezier(.2,.8,.2,1),
              box-shadow 260ms cubic-bezier(.2,.8,.2,1),
              background-color 220ms ease,
              color 220ms ease,
              border-color 220ms ease,
              opacity 220ms ease;
}
.service-preview-cta,
.cta-link.primary,
.submit-button.w-button {
  box-shadow: 0 0 0 rgba(226,178,76,0);
}
.service-preview-cta:hover,
.service-preview-cta:focus-visible,
.cta-link.primary:hover,
.cta-link.primary:focus-visible,
.submit-button.w-button:hover,
.submit-button.w-button:focus-visible {
  transform: translate3d(0,-3px,0);
  background: #f0c66c;
  border-color: #f0c66c;
  color: #120d08;
  box-shadow: 0 18px 36px rgba(0,0,0,.28), 0 0 0 1px rgba(240,198,108,.45);
}
.cta-link,
.link-block {
  position: relative;
  overflow: hidden;
}
.cta-link::after,
.link-block::after,
.text-link::after {
  content: '';
  position: absolute;
  left: 1rem;
  right: 1rem;
  bottom: .55rem;
  height: 1px;
  background: currentColor;
  opacity: .42;
  transform: scaleX(.42);
  transform-origin: left center;
  transition: transform 260ms cubic-bezier(.2,.8,.2,1), opacity 220ms ease;
}
.link-block::after {
  left: 1.15rem;
  right: 1.15rem;
  bottom: .8rem;
}
.text-link::after {
  left: 0;
  right: 0;
  bottom: -.18rem;
}
.cta-link:hover,
.cta-link:focus-visible {
  transform: translate3d(0,-3px,0);
  border-color: rgba(240,198,108,.9);
  color: #fff8ee;
  box-shadow: 0 16px 34px rgba(0,0,0,.22);
}
.cta-link:hover::after,
.cta-link:focus-visible::after,
.link-block:hover::after,
.link-block:focus-visible::after,
.text-link:hover::after,
.text-link:focus-visible::after {
  transform: scaleX(1);
  opacity: .95;
}
.link-block:hover,
.link-block:focus-visible {
  transform: translate3d(0,-4px,0);
  box-shadow: 0 14px 28px rgba(0,0,0,.2);
}
.text-link:hover,
.text-link:focus-visible {
  color: #f0c66c;
}
.service-preview-card,
.case-card,
.relation-card,
.service-card {
  transition: transform 280ms cubic-bezier(.2,.8,.2,1), border-color 220ms ease, box-shadow 280ms cubic-bezier(.2,.8,.2,1);
}
.service-preview-card:hover,
.case-card:hover,
.relation-card:hover,
.service-card:hover {
  transform: translate3d(0,-6px,0);
  border-color: rgba(240,198,108,.45);
  box-shadow: 0 18px 34px rgba(0,0,0,.22);
}
@media (prefers-reduced-motion: reduce) {
  .service-preview-cta,
  .cta-link,
  .submit-button.w-button,
  .link-block,
  .text-link,
  .service-preview-card,
  .case-card,
  .relation-card,
  .service-card {
    transition: none !important;
  }
  .cta-link::after,
  .link-block::after,
  .text-link::after {
    transition: none !important;
  }
}
</style>
"""

for path in HTML_FILES:
    text = path.read_text(encoding='utf-8')
    if 'button-hover-system' in text:
        continue
    insert_at = text.find('</head>')
    if insert_at == -1:
        continue
    text = text[:insert_at] + HOVER_BLOCK + text[insert_at:]
    path.write_text(text, encoding='utf-8')
    print(f'Updated {path}')
