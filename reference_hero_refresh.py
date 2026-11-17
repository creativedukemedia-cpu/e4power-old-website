from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
text = path.read_text()

old_comment = '<!-- Design philosophy: Forensic Webflow mirror. Preserve source structure, typography, media layering, and native interaction timing with minimal reinterpretation. -->'
new_comment = '<!-- Design philosophy: Reference-faithful hero reconstruction. Follow the user-provided homepage reference as closely as possible in the top navigation, bridge-led hero composition, centered emblem, and message hierarchy while preserving the live video background and visible services. -->'
text = text.replace(old_comment, new_comment, 1)

style_block = """
<style id=\"reference-hero-refresh\">
body.home-service-menu .reference-topbar{position:absolute;top:0;left:0;right:0;z-index:55;padding:0;}
body.home-service-menu .reference-topbar-inner{display:grid;grid-template-columns:minmax(20rem,26.5rem) 1fr;min-height:5.7rem;background:#1d1a17;border-bottom:1px solid rgba(255,255,255,.08);}
body.home-service-menu .reference-topbar-brand{display:flex;align-items:center;gap:1.8rem;padding:0 2.35rem;background:linear-gradient(90deg,#d7aa4d 0%,#e4bd65 100%);}
body.home-service-menu .reference-topbar-brand .brand-logo{display:flex;align-items:center;flex:0 0 auto;}
body.home-service-menu .reference-topbar-brand .brand-logo img{width:3.15rem;filter:brightness(0) saturate(100%) invert(10%) sepia(9%) saturate(858%) hue-rotate(357deg) brightness(94%) contrast(93%);}
body.home-service-menu .reference-socials{display:flex;align-items:center;gap:.95rem;}
body.home-service-menu .reference-socials a{width:2.55rem;height:2.55rem;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;border:1px solid rgba(26,22,17,.18);background:rgba(18,14,10,.16);}
body.home-service-menu .reference-socials img{width:1.22rem;height:1.22rem;object-fit:contain;filter:brightness(0) saturate(100%) invert(10%) sepia(9%) saturate(858%) hue-rotate(357deg) brightness(94%) contrast(93%);}
body.home-service-menu .reference-topbar-nav{display:flex;align-items:center;justify-content:center;gap:3.1rem;padding:0 2rem;}
body.home-service-menu .reference-topbar-nav a{color:#f6efe5;text-decoration:none;font-size:1rem;letter-spacing:.05em;text-transform:uppercase;font-weight:700;white-space:nowrap;}
body.home-service-menu .reference-topbar-nav a:hover,body.home-service-menu .reference-topbar-nav a:focus-visible{color:#e7be67;}
body.home-service-menu .hero-container.reference-hero{min-height:100svh;padding:7.6rem 0 7rem;position:relative;overflow:hidden;background:#090806;}
body.home-service-menu .hero-container.reference-hero::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,8,6,.26) 0%,rgba(9,8,6,.56) 64%,rgba(9,8,6,.76) 100%);z-index:1;}
body.home-service-menu .hero-container.reference-hero::after{content:'';position:absolute;left:0;right:0;bottom:7.25rem;height:4.5rem;background:linear-gradient(90deg,rgba(182,124,28,.34) 0%,rgba(182,124,28,.18) 48%,rgba(182,124,28,0) 100%);z-index:2;pointer-events:none;}
body.home-service-menu .reference-hero-bridge{position:absolute;left:50%;top:53%;transform:translate(-50%,-50%);width:min(93vw,112rem);opacity:.43;z-index:2;pointer-events:none;mix-blend-mode:screen;}
body.home-service-menu .reference-hero-copy{position:absolute;left:50%;top:53%;transform:translate(-50%,-50%);width:min(90vw,62rem);z-index:18;text-align:center;}
body.home-service-menu .reference-hero-title{margin:0;font-size:clamp(3rem,6.5vw,6rem);line-height:.92;letter-spacing:.015em;color:#fff7ec;text-transform:uppercase;font-weight:800;}
body.home-service-menu .reference-hero-title .accent{color:#d7aa4d;}
body.home-service-menu .reference-hero-support{max-width:58rem;margin:1.35rem auto 0;font-size:1.34rem;line-height:1.38;color:#f2ede4;}
body.home-service-menu .reference-emblem-wrap{position:absolute;left:50%;top:30.5%;transform:translate(-50%,-50%) scale(.98);z-index:19;}
body.home-service-menu .reference-emblem-wrap .emblem-image{filter:drop-shadow(0 12px 28px rgba(0,0,0,.35));}
body.home-service-menu .hero-services-panel{left:4.75rem;right:auto;bottom:4.2rem;max-width:48rem;z-index:18;padding:1.2rem 1.5rem 1.2rem;background:rgba(14,12,10,.58);border:1px solid rgba(255,255,255,.1);backdrop-filter:blur(6px);}
body.home-service-menu .hero-services-label{font-size:1.05rem;letter-spacing:.16em;color:#d7aa4d;}
body.home-service-menu .hero-services-list{font-size:1rem;line-height:1.8;color:#f5ede3;letter-spacing:.035em;}
body.home-service-menu .hero-service-hover-shell{z-index:28;bottom:2rem;}
@media screen and (max-width: 991px){
  body.home-service-menu .reference-topbar-inner{grid-template-columns:1fr;min-height:auto;}
  body.home-service-menu .reference-topbar-brand{justify-content:space-between;padding:1rem 1.2rem;gap:1rem;}
  body.home-service-menu .reference-topbar-nav{justify-content:flex-start;flex-wrap:wrap;gap:.85rem 1.35rem;padding:.95rem 1.2rem 1.1rem;background:#1d1a17;border-top:1px solid rgba(255,255,255,.06);}
  body.home-service-menu .reference-topbar-nav a{font-size:.86rem;}
  body.home-service-menu .hero-container.reference-hero{min-height:auto;padding:10.4rem 0 11rem;}
  body.home-service-menu .reference-emblem-wrap{top:28%;transform:translate(-50%,-50%) scale(.72);}
  body.home-service-menu .reference-hero-copy{top:53.5%;width:min(92vw,43rem);}
  body.home-service-menu .reference-hero-title{font-size:clamp(2.45rem,8vw,4.4rem);}
  body.home-service-menu .reference-hero-support{font-size:1.08rem;line-height:1.46;}
  body.home-service-menu .hero-services-panel{left:1rem;right:1rem;bottom:1.25rem;max-width:none;padding:1rem 1rem 1rem;}
  body.home-service-menu .reference-hero-bridge{width:115vw;top:58%;opacity:.35;}
}
@media screen and (max-width: 767px){
  body.home-service-menu .reference-topbar-brand{padding:.95rem 1rem;}
  body.home-service-menu .reference-socials{gap:.55rem;}
  body.home-service-menu .reference-socials a{width:2.2rem;height:2.2rem;}
  body.home-service-menu .reference-topbar-nav{gap:.7rem 1rem;padding:.85rem 1rem 1rem;}
  body.home-service-menu .hero-container.reference-hero{padding:10rem 0 11.5rem;}
  body.home-service-menu .reference-emblem-wrap{top:27%;transform:translate(-50%,-50%) scale(.58);}
  body.home-service-menu .reference-hero-copy{top:54%;}
  body.home-service-menu .reference-hero-support{font-size:.98rem;line-height:1.54;max-width:22rem;}
  body.home-service-menu .hero-services-list{font-size:.82rem;line-height:1.7;}
}
</style>
"""
text = text.replace('</style>\n</head><body class="body home-service-menu">', '</style>\n' + style_block + '\n</head><body class="body home-service-menu">', 1)

nav_start = '<nav class="navbar-logo-left">'
nav_end = '</nav><div class="w-embed"><style>'
new_nav = '''<nav class="reference-topbar" role="navigation"><div class="reference-topbar-inner"><div class="reference-topbar-brand"><a aria-current="page" class="brand-logo" href="/"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg"/></a><div class="reference-socials"><a href="https://www.instagram.com/e4power_?igsh=bXR4bThxMHh2dHNy&amp;utm_source=qr" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c4ee8e329fe01d525b_instagram.svg"/></a><a href="https://www.linkedin.com/company/e4-power-consulting/" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c46c9537fa67bb89bd_linkedin.svg"/></a><a href="https://www.tiktok.com/@e4powerconsulting?_t=ZT-90YVLBMkwaT&amp;_r=1" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68f66f4d7a2ffc0d86a72550_tiktok.svg"/></a><a href="https://www.facebook.com/profile.php?id=61573544665670&amp;mibextid=wwXIfr&amp;rdid=yOcyRogs7shBnrLD&amp;share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1775G2zRAh%2F%3Fmibextid%3DwwXIfr#" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c48dbb4dd69e849624_facebook.svg"/></a></div></div><div class="reference-topbar-nav"><a href="#about-e4">ABOUT E4</a><a href="/services/">OUR SERVICES</a><a href="#empower">THE BRIDGE MODEL</a><a href="#engage">OUR TEAM</a></div></div></nav>'''
pre, rest = text.split(nav_start, 1)
_, post = rest.split(nav_end, 1)
text = pre + new_nav + '<div class="w-embed"><style>' + post

hero_start = '</style></div><section class="section"><div class="hero-container">'
hero_end = '</div></section><section class="section"><div class="container-hero">'
pre, rest = text.split(hero_start, 1)
hero_content, post = rest.split(hero_end, 1)
video_part, resth = hero_content.split('<div class="emblem_div">', 1)
emblem_inner, services_part = resth.split('</div><div class="hero-services-panel"', 1)
services_part = '<div class="hero-services-panel"' + services_part
new_hero = '''</style></div><section class="section"><div class="hero-container reference-hero">''' + video_part + '''<img alt="" class="reference-hero-bridge" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d8550f1d421250bd0d2438_07041dfd1e6c9bd0873206057844ea8b_bridge.svg"/><div class="emblem_div reference-emblem-wrap">''' + emblem_inner + '''</div><div class="reference-hero-copy"><h1 class="reference-hero-title">WE ARE <span class="accent">E4POWER</span></h1><p class="reference-hero-support">At E4Power, we do not just solve problems, we bridge gaps and create sustainable infrastructure solutions for educational institutions, nonprofits, and for-profit partners.</p></div>''' + services_part + '''</div></section><section class="section"><div class="container-hero">'''
text = pre + new_hero + post

path.write_text(text)
print('Reference-led hero refresh applied.')
