from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
text = path.read_text()

old_comment = '<!-- Design philosophy: Forensic Webflow mirror. Preserve source structure, typography, media layering, and native interaction timing with minimal reinterpretation. -->'
new_comment = '<!-- Design philosophy: Strategic Institutional Beacon. Use a clearer top navigation, a message-led hero, earlier trust signals, and brighter foreground planes while preserving E4\'s dark editorial brand and interactive emblem identity. -->'
text = text.replace(old_comment, new_comment, 1)

style_injection = """
<style id=\"phase-one-home-refresh\">
body.home-service-menu .phase-one-nav .navbar-logo-left-container{background:rgba(24,22,18,.94);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.08);box-shadow:none;}
body.home-service-menu .phase-one-nav .navbar-container{max-width:none;padding:0;}
body.home-service-menu .phase-one-nav .navbar-wrapper{display:grid;grid-template-columns:auto 1fr auto;align-items:stretch;gap:0;min-height:5.5rem;}
body.home-service-menu .phase-one-nav-brand-block{display:flex;align-items:center;gap:1.15rem;background:linear-gradient(90deg,#d7aa4d 0%,#e2ba67 100%);padding:0 1.4rem;}
body.home-service-menu .phase-one-nav .navbar-brand{margin:0;padding:0;display:flex;align-items:center;}
body.home-service-menu .phase-one-nav .navbar-brand img{width:3.25rem;filter:brightness(0) saturate(100%) invert(9%) sepia(10%) saturate(687%) hue-rotate(357deg) brightness(92%) contrast(93%);}
body.home-service-menu .phase-one-nav .socials-div{display:flex;align-items:center;gap:.8rem;}
body.home-service-menu .phase-one-nav .social-link-block{width:2.55rem;height:2.55rem;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:rgba(23,19,14,.16);border:1px solid rgba(23,19,14,.18);}
body.home-service-menu .phase-one-nav .social-link-block img{width:1.25rem;height:1.25rem;object-fit:contain;filter:brightness(0) saturate(100%) invert(10%) sepia(8%) saturate(1029%) hue-rotate(357deg) brightness(95%) contrast(94%);}
body.home-service-menu .phase-one-nav .nav-menu-wrapper{display:flex;align-items:center;justify-content:center;}
body.home-service-menu .phase-one-nav .nav-menu-two{display:flex;align-items:center;justify-content:center;gap:2.35rem;margin:0;padding:0 2rem;}
body.home-service-menu .phase-one-nav .nav-link{font-size:.98rem;letter-spacing:.11em;text-transform:uppercase;color:#f6efe5;padding:0;text-decoration:none;}
body.home-service-menu .phase-one-nav .nav-link:hover,body.home-service-menu .phase-one-nav .nav-link:focus-visible{color:#f0c66c;}
body.home-service-menu .phase-one-nav .navbar-right-div{display:flex;align-items:center;gap:1.25rem;padding:0 1.5rem 0 1rem;}
body.home-service-menu .phase-one-nav .phase-one-contact{display:inline-flex;align-items:center;justify-content:center;min-height:2.9rem;padding:0 1.2rem;border:1px solid rgba(240,198,108,.4);background:rgba(255,255,255,.03);color:#fff7ea;text-decoration:none;text-transform:none;}
body.home-service-menu .phase-one-nav .menu-button{margin:0;border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.03);}
body.home-service-menu .hero-container{position:relative;min-height:100svh;padding:8.4rem 0 8rem;overflow:hidden;background:#0b0907;}
body.home-service-menu .hero-container::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.36) 0%,rgba(8,8,8,.54) 46%,rgba(8,8,8,.72) 100%);z-index:1;pointer-events:none;}
body.home-service-menu .hero-container::after{content:'';position:absolute;inset:auto 0 0 0;height:34%;background:linear-gradient(180deg,rgba(8,8,8,0) 0%,rgba(8,8,8,.84) 100%);z-index:1;pointer-events:none;}
body.home-service-menu .hero-phase-one-bridge{position:absolute;inset:auto -2% 0 auto;width:min(60vw,58rem);opacity:.2;z-index:2;pointer-events:none;mix-blend-mode:screen;}
body.home-service-menu .hero-phase-one-copy{position:absolute;left:50%;top:57%;transform:translate(-50%,-50%);width:min(88vw,64rem);z-index:18;text-align:center;padding:1.8rem 1.8rem 2rem;border:1px solid rgba(255,255,255,.08);background:linear-gradient(180deg,rgba(13,11,9,.62),rgba(13,11,9,.34));backdrop-filter:blur(10px);box-shadow:0 32px 70px rgba(0,0,0,.24);}
body.home-service-menu .hero-phase-one-kicker{margin:0 0 1rem;color:#d7aa4d;font-size:.9rem;letter-spacing:.22em;text-transform:uppercase;}
body.home-service-menu .hero-phase-one-title{margin:0;font-size:clamp(2.7rem,5.7vw,5.3rem);line-height:.95;letter-spacing:.03em;color:#fff8ee;text-transform:uppercase;}
body.home-service-menu .hero-phase-one-title .accent{color:#d7aa4d;}
body.home-service-menu .hero-phase-one-support{max-width:49rem;margin:1.35rem auto 0;font-size:1.28rem;line-height:1.55;color:#f4ebdf;}
body.home-service-menu .hero-phase-one-audience{display:flex;flex-wrap:wrap;justify-content:center;gap:.75rem;margin:1.4rem auto 0;max-width:46rem;}
body.home-service-menu .hero-phase-one-audience span{display:inline-flex;align-items:center;min-height:2.35rem;padding:0 .95rem;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.05);color:#f7f0e6;font-size:.82rem;letter-spacing:.08em;text-transform:uppercase;}
body.home-service-menu .hero-phase-one-actions{display:flex;justify-content:center;flex-wrap:wrap;gap:.9rem;margin-top:1.55rem;}
body.home-service-menu .hero-phase-one-actions .cta-link{display:inline-flex;align-items:center;justify-content:center;min-height:3rem;padding:0 1.3rem;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);color:#fff8ee;text-decoration:none;font-size:.86rem;letter-spacing:.1em;text-transform:uppercase;}
body.home-service-menu .hero-phase-one-actions .cta-link.primary{background:#d7aa4d;border-color:#d7aa4d;color:#17120c;}
body.home-service-menu .emblem_div{z-index:12;}
body.home-service-menu .hero-services-panel{left:5.4vw;right:auto;bottom:2.4rem;z-index:16;max-width:42rem;padding:1.4rem 1.5rem 1.2rem;border:1px solid rgba(236,216,188,.18);background:linear-gradient(180deg,rgba(243,234,220,.12),rgba(243,234,220,.06));backdrop-filter:blur(8px);}
body.home-service-menu .hero-services-label{color:#f0c66c;}
body.home-service-menu .hero-service-hover-shell{left:50%;bottom:1.4rem;width:min(92vw,880px);z-index:20;}
body.home-service-menu .phase-one-proof{position:relative;background:linear-gradient(180deg,#15110d 0%,#0e0c0a 100%);padding:2.8rem 0 2.6rem;}
body.home-service-menu .phase-one-proof::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at top left,rgba(215,170,77,.18),transparent 42%);pointer-events:none;}
body.home-service-menu .phase-one-proof-wrap{position:relative;z-index:1;width:min(92vw,1180px);margin:0 auto;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:1.4rem;align-items:stretch;}
body.home-service-menu .phase-one-proof-main,body.home-service-menu .phase-one-proof-quote{padding:1.75rem 1.6rem;border:1px solid rgba(255,255,255,.1);}
body.home-service-menu .phase-one-proof-main{background:linear-gradient(180deg,rgba(244,236,223,.95),rgba(231,219,200,.9));color:#18120d;}
body.home-service-menu .phase-one-proof-quote{background:linear-gradient(180deg,rgba(31,26,21,.92),rgba(22,19,15,.92));color:#f7f0e4;}
body.home-service-menu .phase-one-proof-kicker{margin:0 0 .85rem;font-size:.86rem;letter-spacing:.2em;text-transform:uppercase;color:#94661d;}
body.home-service-menu .phase-one-proof-main h2,body.home-service-menu .phase-one-proof-quote h3{margin:0;font-size:clamp(1.8rem,3vw,3rem);line-height:1.02;text-transform:uppercase;}
body.home-service-menu .phase-one-proof-main p{margin:1rem 0 0;color:#2a2219;font-size:1rem;line-height:1.7;max-width:42rem;}
body.home-service-menu .phase-one-logo-row{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem;margin-top:1.5rem;align-items:center;}
body.home-service-menu .phase-one-logo-row img{max-width:100%;height:3.9rem;object-fit:contain;filter:brightness(.15) saturate(.7);opacity:.9;}
body.home-service-menu .phase-one-proof-quote p{margin:1rem 0 0;font-size:1rem;line-height:1.8;color:#f0e5d5;}
body.home-service-menu .phase-one-proof-quote cite{display:block;margin-top:1rem;color:#d7aa4d;font-style:normal;font-size:.88rem;letter-spacing:.08em;text-transform:uppercase;}
body.home-service-menu .container-hero{margin-top:0;padding-top:2.1rem;}
@media screen and (max-width: 991px){
  body.home-service-menu .phase-one-nav .navbar-wrapper{grid-template-columns:1fr auto;}
  body.home-service-menu .phase-one-nav-brand-block{padding:0 1rem;min-height:4.8rem;}
  body.home-service-menu .phase-one-nav .nav-menu-wrapper{justify-content:flex-start;background:rgba(18,15,11,.98);padding:1rem 1.25rem 1.5rem;}
  body.home-service-menu .phase-one-nav .nav-menu-two{flex-direction:column;align-items:flex-start;gap:1rem;padding:0;}
  body.home-service-menu .phase-one-nav .navbar-right-div{padding-right:1rem;gap:.8rem;}
  body.home-service-menu .phase-one-nav .phase-one-contact{display:none;}
  body.home-service-menu .hero-container{min-height:auto;padding:7.6rem 0 11rem;}
  body.home-service-menu .hero-phase-one-copy{top:56%;width:min(92vw,44rem);padding:1.45rem 1.15rem 1.55rem;}
  body.home-service-menu .hero-phase-one-title{font-size:clamp(2.2rem,8vw,4rem);}
  body.home-service-menu .hero-phase-one-support{font-size:1.06rem;}
  body.home-service-menu .hero-phase-one-audience{gap:.55rem;}
  body.home-service-menu .hero-phase-one-audience span{font-size:.74rem;min-height:2.1rem;}
  body.home-service-menu .phase-one-proof-wrap{grid-template-columns:1fr;}
  body.home-service-menu .phase-one-logo-row{grid-template-columns:repeat(2,minmax(0,1fr));}
  body.home-service-menu .hero-services-panel{left:1rem;right:1rem;max-width:none;bottom:1.25rem;padding:1rem 1rem .9rem;}
}
@media screen and (max-width: 767px){
  body.home-service-menu .phase-one-nav-brand-block .socials-div{display:none;}
  body.home-service-menu .hero-container{padding:6.9rem 0 10.5rem;}
  body.home-service-menu .hero-phase-one-copy{top:58%;}
  body.home-service-menu .hero-phase-one-support{font-size:1rem;line-height:1.62;}
  body.home-service-menu .hero-phase-one-actions{flex-direction:column;align-items:stretch;}
  body.home-service-menu .hero-phase-one-actions .cta-link{width:100%;}
  body.home-service-menu .hero-phase-one-bridge{width:92vw;opacity:.16;}
}
</style>
"""
text = text.replace('</style>\n</head><body class="body home-service-menu">', '</style>\n' + style_injection + '\n</head><body class="body home-service-menu">', 1)

nav_start = '<nav class="navbar-logo-left">'
nav_end = '</nav><div class="w-embed"><style>'
nav_new = '''<nav class="navbar-logo-left phase-one-nav"><div class="navbar-logo-left-container shadow-three w-nav" data-animation="over-right" data-collapse="all" data-duration="400" data-easing="ease" data-easing2="ease" role="banner"><div class="navbar-container"><div class="navbar-wrapper"><div class="phase-one-nav-brand-block"><a aria-current="page" class="navbar-brand w-nav-brand w--current" href="/"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68bcc54da8714105bb252c7f_e4_logo_white.svg"/></a><div class="socials-div"><a class="social-link-block w-inline-block" href="https://www.instagram.com/e4power_?igsh=bXR4bThxMHh2dHNy&amp;utm_source=qr" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c4ee8e329fe01d525b_instagram.svg"/></a><a class="social-link-block w-inline-block" href="https://www.linkedin.com/company/e4-power-consulting/" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c46c9537fa67bb89bd_linkedin.svg"/></a><a class="social-link-block w-inline-block" href="https://www.tiktok.com/@e4powerconsulting?_t=ZT-90YVLBMkwaT&amp;_r=1" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68f66f4d7a2ffc0d86a72550_tiktok.svg"/></a><a class="social-link-block w-inline-block" href="https://www.facebook.com/profile.php?id=61573544665670&amp;mibextid=wwXIfr&amp;rdid=yOcyRogs7shBnrLD&amp;share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1775G2zRAh%2F%3Fmibextid%3DwwXIfr#" target="_blank"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d9d0c48dbb4dd69e849624_facebook.svg"/></a></div></div><nav class="nav-menu-wrapper w-nav-menu" role="navigation"><ul class="nav-menu-two w-list-unstyled" role="list"><li><a class="nav-link" href="#about-e4">ABOUT E4</a></li><li class="menu-services-row"><a class="nav-link menu-services-link" href="/services/" onclick="window.location.href='/services/'; return false;">OUR SERVICES</a></li><li><a class="nav-link" href="#empower">THE BRIDGE MODEL</a></li><li><a class="nav-link" href="#engage">OUR TEAM</a></li></ul></nav><div class="navbar-right-div"><a class="text-link phase-one-contact" href="/contact-us">Contact Us</a><div class="menu-button w-nav-button"><div class="hamburger-icon w-icon-nav-menu"></div></div></div></div></div></div></nav>'''
pre, rest = text.split(nav_start, 1)
_, post = rest.split(nav_end, 1)
text = pre + nav_new + '<div class="w-embed"><style>' + post

hero_start = '</style></div><section class="section"><div class="hero-container">'
hero_end = '</div></section><section class="section"><div class="container-hero">'
pre, rest = text.split(hero_start, 1)
hero_content, post = rest.split(hero_end, 1)
video_part, resth = hero_content.split('<div class="emblem_div">', 1)
emblem_inner, services_part = resth.split('</div><div class="hero-services-panel"', 1)
services_part = '<div class="hero-services-panel"' + services_part
new_hero_block = '''</style></div><section class="section"><div class="hero-container">''' + video_part + '''<img alt="" class="hero-phase-one-bridge" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d8550f1d421250bd0d2438_07041dfd1e6c9bd0873206057844ea8b_bridge.svg"/><div class="hero-phase-one-copy"><div class="hero-phase-one-kicker">GRANT STRATEGY | OPERATIONAL SUPPORT | PARTNERSHIP GROWTH</div><h1 class="hero-phase-one-title">WE HELP <span class="accent">INSTITUTIONS</span> BRIDGE OPPORTUNITY INTO EXECUTION</h1><p class="hero-phase-one-support">E4 Power serves educational institutions, nonprofits, and mission-aligned partners with grant writing, post-award management, readiness assessments, financial guidance, speaking engagements, and technology-enabled support that strengthens long-term capacity.</p><div class="hero-phase-one-audience"><span>Educational Institutions</span><span>Nonprofits</span><span>Mission-Aligned Partners</span></div><div class="hero-phase-one-actions"><a class="cta-link primary" href="/services/">Explore Services</a><a class="cta-link" href="#about-e4">Why E4 Power</a><a class="cta-link" href="#empower">See the Bridge Model</a></div></div><div class="emblem_div">''' + emblem_inner + '''</div>''' + services_part + '''</div></section><section class="section phase-one-proof" id="about-e4"><div class="phase-one-proof-wrap"><div class="phase-one-proof-main"><div class="phase-one-proof-kicker">Why organizations choose E4</div><h2>Strategy, stewardship, and execution in one advisory partner</h2><p>E4 Power helps clients move from opportunity identification to awarded work, operational readiness, financial discipline, and sustained implementation. The homepage should show that this is not a single-service firm. It is a bridge across the full capacity-building journey.</p><div class="phase-one-logo-row"><img alt="Alabama A and M University" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d89270105b5ac81fbe7e81_Alabama%201.png"/><img alt="Florida A and M University" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d89270abefb77e81f25cfe_Florida-AM%201.png"/><img alt="Prairie View A and M University" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d8927001555a861b216698_PrairieViewAMUniversity_icon_color%201.png"/><img alt="Johns Hopkins" loading="lazy" src="https://cdn.prod.website-files.com/68ba0532388ab756f96c84d5/68d89270404223839d4ea05d_John%20Hopkins%201.png"/></div></div><div class="phase-one-proof-quote"><div class="phase-one-proof-kicker">Client confidence</div><h3>Trusted guidance that improves competitiveness</h3><p>My experience with E4 Power has been consistently positive. Their consultants bring exceptional professionalism and structure to the proposal development process, providing valuable insight that enhances both efficiency and competitiveness.</p><cite>Clyde Varner | Alabama A&amp;M University</cite></div></div></section><section class="section"><div class="container-hero">'''
text = pre + new_hero_block + post

path.write_text(text)
print('Phase 1 homepage refresh applied.')
