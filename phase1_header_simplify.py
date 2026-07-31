from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
text = path.read_text()

old_css = '''body.home-service-menu .phase-one-nav{position:absolute;top:0;left:0;right:0;z-index:48;height:5.5rem;overflow:hidden;}
body.home-service-menu .phase-one-nav .navbar-logo-left-container{height:5.5rem;background:rgba(24,22,18,.94);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.08);box-shadow:none;}
body.home-service-menu .phase-one-nav .navbar-container{max-width:none;padding:0;}
body.home-service-menu .phase-one-nav .navbar-wrapper{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:stretch;gap:0;min-height:5.5rem;}
body.home-service-menu .phase-one-nav-brand-block{display:flex;align-items:center;align-self:stretch;min-height:5.5rem;gap:1.15rem;background:linear-gradient(90deg,#d7aa4d 0%,#e2ba67 100%);padding:0 1.4rem;}
body.home-service-menu .phase-one-nav .navbar-brand{margin:0;padding:0;display:flex;align-items:center;}
body.home-service-menu .phase-one-nav .navbar-brand img{width:3.25rem;filter:brightness(0) saturate(100%) invert(9%) sepia(10%) saturate(687%) hue-rotate(357deg) brightness(92%) contrast(93%);}
body.home-service-menu .phase-one-nav .socials-div{display:flex;align-items:center;gap:.8rem;}
body.home-service-menu .phase-one-nav .social-link-block{width:2.55rem;height:2.55rem;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:rgba(23,19,14,.16);border:1px solid rgba(23,19,14,.18);}
body.home-service-menu .phase-one-nav .social-link-block img{width:1.25rem;height:1.25rem;object-fit:contain;filter:brightness(0) saturate(100%) invert(10%) sepia(8%) saturate(1029%) hue-rotate(357deg) brightness(95%) contrast(94%);}
body.home-service-menu .phase-one-nav .nav-menu-wrapper{display:flex;align-items:center;justify-content:center;}
@media screen and (min-width: 992px){
  body.home-service-menu .phase-one-nav .nav-menu-wrapper{position:static !important;display:flex !important;flex:1 1 auto !important;align-items:center !important;justify-content:center !important;height:5.5rem !important;min-width:0 !important;padding:0 !important;background:transparent !important;}
  body.home-service-menu .phase-one-nav .w-nav-menu{display:flex !important;position:static !important;inset:auto !important;height:auto !important;width:auto !important;max-width:none !important;background:transparent !important;float:none !important;}
  body.home-service-menu .phase-one-nav .menu-button{display:none !important;}
}
body.home-service-menu .phase-one-nav .nav-menu-two{display:flex;align-items:center;justify-content:center;gap:2.35rem;margin:0;padding:0 2rem;}
body.home-service-menu .phase-one-nav .nav-link{font-size:.98rem;letter-spacing:.11em;text-transform:uppercase;color:#f6efe5;padding:0;text-decoration:none;}
body.home-service-menu .phase-one-nav .nav-link:hover,body.home-service-menu .phase-one-nav .nav-link:focus-visible{color:#f0c66c;}
body.home-service-menu .phase-one-nav .navbar-right-div{display:flex;align-items:center;gap:1.25rem;padding:0 1.5rem 0 1rem;}
body.home-service-menu .phase-one-nav .phase-one-contact{display:inline-flex;align-items:center;justify-content:center;min-height:2.9rem;padding:0 1.2rem;border:1px solid rgba(240,198,108,.4);background:rgba(255,255,255,.03);color:#fff7ea;text-decoration:none;text-transform:none;}
body.home-service-menu .phase-one-nav .menu-button{margin:0;border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.03);}'''

new_css = '''body.home-service-menu .phase-one-nav{position:absolute;top:0;left:0;right:0;z-index:48;padding:0 2.4rem;}
body.home-service-menu .phase-one-topbar-inner{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:1.5rem;min-height:5.5rem;background:rgba(24,22,18,.94);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.08);}
body.home-service-menu .phase-one-nav-brand-block{display:flex;align-items:center;align-self:stretch;min-height:5.5rem;gap:1.15rem;background:linear-gradient(90deg,#d7aa4d 0%,#e2ba67 100%);padding:0 1.4rem;}
body.home-service-menu .phase-one-nav .navbar-brand{margin:0;padding:0;display:flex;align-items:center;}
body.home-service-menu .phase-one-nav .navbar-brand img{width:3.25rem;filter:brightness(0) saturate(100%) invert(9%) sepia(10%) saturate(687%) hue-rotate(357deg) brightness(92%) contrast(93%);}
body.home-service-menu .phase-one-nav .socials-div{display:flex;align-items:center;gap:.8rem;}
body.home-service-menu .phase-one-nav .social-link-block{width:2.55rem;height:2.55rem;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:rgba(23,19,14,.16);border:1px solid rgba(23,19,14,.18);}
body.home-service-menu .phase-one-nav .social-link-block img{width:1.25rem;height:1.25rem;object-fit:contain;filter:brightness(0) saturate(100%) invert(10%) sepia(8%) saturate(1029%) hue-rotate(357deg) brightness(95%) contrast(94%);}
body.home-service-menu .phase-one-nav-links{display:flex;align-items:center;justify-content:center;gap:2.35rem;min-width:0;padding:0 1rem;}
body.home-service-menu .phase-one-nav .nav-link{font-size:.98rem;letter-spacing:.11em;text-transform:uppercase;color:#f6efe5;padding:0;text-decoration:none;white-space:nowrap;}
body.home-service-menu .phase-one-nav .nav-link:hover,body.home-service-menu .phase-one-nav .nav-link:focus-visible{color:#f0c66c;}
body.home-service-menu .phase-one-nav .phase-one-contact{display:inline-flex;align-items:center;justify-content:center;min-height:2.9rem;padding:0 1.2rem;border:1px solid rgba(240,198,108,.4);background:rgba(255,255,255,.03);color:#fff7ea;text-decoration:none;text-transform:none;margin-right:1.3rem;}'''

text = text.replace(old_css, new_css, 1)

text = text.replace('''  body.home-service-menu .phase-one-nav{height:auto;overflow:visible;}
  body.home-service-menu .phase-one-nav .navbar-logo-left-container{height:auto;}
  body.home-service-menu .phase-one-nav .navbar-wrapper{grid-template-columns:1fr auto;}
  body.home-service-menu .phase-one-nav .menu-button{display:flex !important;}
  body.home-service-menu .phase-one-nav-brand-block{padding:0 1rem;min-height:4.8rem;}
  body.home-service-menu .phase-one-nav .nav-menu-wrapper{justify-content:flex-start;background:rgba(18,15,11,.98);padding:1rem 1.25rem 1.5rem;}
  body.home-service-menu .phase-one-nav .nav-menu-two{flex-direction:column;align-items:flex-start;gap:1rem;padding:0;}
  body.home-service-menu .phase-one-nav .navbar-right-div{padding-right:1rem;gap:.8rem;}
  body.home-service-menu .phase-one-nav .phase-one-contact{display:none;}''', '''  body.home-service-menu .phase-one-nav{padding:0 1rem;}
  body.home-service-menu .phase-one-topbar-inner{grid-template-columns:1fr;gap:.7rem;padding:0 0 .95rem;}
  body.home-service-menu .phase-one-nav-brand-block{padding:0 1rem;min-height:4.8rem;justify-content:space-between;}
  body.home-service-menu .phase-one-nav-links{flex-wrap:wrap;justify-content:flex-start;gap:.9rem 1.25rem;padding:0 1rem;}
  body.home-service-menu .phase-one-nav .phase-one-contact{display:inline-flex;margin:0 1rem;}''', 1)

nav_start = '<nav class="navbar-logo-left phase-one-nav">'
nav_end = '</nav><div class="w-embed"><style>'
new_nav = '''<nav class="phase-one-nav" role="navigation"><div class="phase-one-topbar-inner"><div class="phase-one-nav-brand-block"><a aria-current="page" class="navbar-brand w--current" href="/"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg"/></a><div class="socials-div"><a class="social-link-block" href="https://www.instagram.com/e4power_?igsh=bXR4bThxMHh2dHNy&amp;utm_source=qr" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c4ee8e329fe01d525b_instagram.svg"/></a><a class="social-link-block" href="https://www.linkedin.com/company/e4-power-consulting/" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c46c9537fa67bb89bd_linkedin.svg"/></a><a class="social-link-block" href="https://www.tiktok.com/@e4powerconsulting?_t=ZT-90YVLBMkwaT&amp;_r=1" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68f66f4d7a2ffc0d86a72550_tiktok.svg"/></a><a class="social-link-block" href="https://www.facebook.com/profile.php?id=61573544665670&amp;mibextid=wwXIfr&amp;rdid=yOcyRogs7shBnrLD&amp;share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1775G2zRAh%2F%3Fmibextid%3DwwXIfr#" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c48dbb4dd69e849624_facebook.svg"/></a></div></div><div class="phase-one-nav-links"><a class="nav-link" href="#about-e4">ABOUT E4</a><a class="nav-link" href="/services/">OUR SERVICES</a><a class="nav-link" href="#empower">THE BRIDGE MODEL</a><a class="nav-link" href="#engage">OUR TEAM</a></div><a class="text-link phase-one-contact" href="/contact-us">Contact Us</a></div></nav>'''
pre, rest = text.split(nav_start, 1)
_, post = rest.split(nav_end, 1)
text = pre + new_nav + '<div class="w-embed"><style>' + post

path.write_text(text)
print('Phase 1 custom header applied.')
