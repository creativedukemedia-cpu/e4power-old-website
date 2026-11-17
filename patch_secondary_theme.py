from pathlib import Path
import re

ROOT = Path('/home/ubuntu/e4powerinc-clone/client')
TARGETS = [
    ROOT / 'contact-us' / 'index.html',
    ROOT / 'educate' / 'index.html',
    ROOT / 'elevate' / 'index.html',
    ROOT / 'empower' / 'index.html',
    ROOT / 'engage' / 'index.html',
    ROOT / 'services' / 'index.html',
    ROOT / 'services' / 'advisory-alignment' / 'index.html',
    ROOT / 'services' / 'financial-management' / 'index.html',
    ROOT / 'services' / 'grant-management' / 'index.html',
    ROOT / 'services' / 'grant-writing' / 'index.html',
    ROOT / 'services' / 'institutional-discovery' / 'index.html',
    ROOT / 'services' / 'it-app-development' / 'index.html',
    ROOT / 'services' / 'project-management' / 'index.html',
    ROOT / 'services' / 'readiness-assessments' / 'index.html',
    ROOT / 'services' / 'speaking-engagements' / 'index.html',
    ROOT / 'services' / 'technology-ai-literacy' / 'index.html',
    ROOT / 'services' / 'workshops-training' / 'index.html',
    ROOT / 'team' / 'index.html',
    ROOT / 'team-members' / 'garry-brown' / 'index.html',
    ROOT / 'team-members' / 'kandy-rose' / 'index.html',
    ROOT / 'team-members' / 'larico-j-treadwell' / 'index.html',
]

STYLE_BLOCK = """
<style id="cross-page-theme-system">
body.theme-dark{background:#050505;color:#f4efe7;}
body.theme-light{background:#f5f0e6;color:#1e1a16;}
body.theme-light,
body.theme-light .body,
body.theme-light.ref-page-shell,
body.theme-light .section,
body.theme-light .section.black,
body.theme-light .section.gray,
body.theme-light .section.dark-gray,
body.theme-light .main-content-block,
body.theme-light .main-content-block.gray,
body.theme-light .smaller-container.gray,
body.theme-light .smaller-container.smaller,
body.theme-light .team-member,
body.theme-light .member-bio,
body.theme-light .member-bio.w-richtext,
body.theme-light .service-card,
body.theme-light .relation-card,
body.theme-light .case-card,
body.theme-light .accordion-item-content,
body.theme-light .footer,
body.theme-light .footer-flex-container,
body.theme-light .collection-item,
body.theme-light .div-block-11,
body.theme-light .rich-text-block,
body.theme-light .rich-text-block-2,
body.theme-light .w-richtext,
body.theme-light .tabs-content,
body.theme-light .tab-pane-tab-1,
body.theme-light .tab-pane-tab-2,
body.theme-light .tab-pane-tab-3,
body.theme-light .tab-pane-tab-4,
body.theme-light .ref-page-hero,
body.theme-light .ref-content-panel,
body.theme-light .ref-grid-card,
body.theme-light .ref-card,
body.theme-light .ref-footer-shell,
body.theme-light .ref-service-card,
body.theme-light .ref-feature-card,
body.theme-light .ref-pillar-card,
body.theme-light .ref-stacked-card,
body.theme-light .ref-surface,
body.theme-light .ref-panel,
body.theme-light .ref-grid,
body.theme-light .ref-body,
body.theme-light .ref-summary,
body.theme-light .ref-copy-block,
body.theme-light .ref-column,
body.theme-light .ref-band,
body.theme-light .ref-gallery-section,
body.theme-light .ref-top-block,
body.theme-light .team-members-div,
body.theme-light .team-members-collection-list,
body.theme-light .team-picture-div,
body.theme-light .w-dyn-item{
  background:#f5f0e6 !important;
  color:#1e1a16 !important;
}
body.theme-light p,
body.theme-light li,
body.theme-light label,
body.theme-light input,
body.theme-light textarea,
body.theme-light select,
body.theme-light .paragraph,
body.theme-light .paragraph-2,
body.theme-light .paragraph-3,
body.theme-light .paragraph-4,
body.theme-light .small-heading,
body.theme-light .heading,
body.theme-light .member-title,
body.theme-light .role-text,
body.theme-light .member-bio p,
body.theme-light .member-bio li,
body.theme-light .w-richtext p,
body.theme-light .w-richtext li,
body.theme-light .w-richtext h1,
body.theme-light .w-richtext h2,
body.theme-light .w-richtext h3,
body.theme-light .w-richtext h4,
body.theme-light .h3,
body.theme-light .h4,
body.theme-light .h5,
body.theme-light .nav-link,
body.theme-light .text-link,
body.theme-light .cta-link,
body.theme-light .link-block,
body.theme-light .footer-link,
body.theme-light .tab-link-tab-1,
body.theme-light .tab-link-tab-2,
body.theme-light .tab-link-tab-3,
body.theme-light .tab-link-tab-4,
body.theme-light .accordion-item-trigger,
body.theme-light .list-item,
body.theme-light .list-item-2,
body.theme-light .list-item-3,
body.theme-light .list-item-4,
body.theme-light .list-item-5,
body.theme-light .list-item-6,
body.theme-light .list-item-7,
body.theme-light .list-item-8,
body.theme-light .white-text,
body.theme-light .subheading,
body.theme-light .subheading-div,
body.theme-light .smaller-container,
body.theme-light .container,
body.theme-light .title,
body.theme-light .ref-kicker,
body.theme-light .ref-copy,
body.theme-light .ref-summary,
body.theme-light .ref-body,
body.theme-light .ref-eyebrow,
body.theme-light .ref-label,
body.theme-light .ref-meta,
body.theme-light .ref-subhead,
body.theme-light .ref-overline,
body.theme-light .ref-caption,
body.theme-light .ref-note,
body.theme-light .ref-heading-main,
body.theme-light .ref-heading-accent,
body.theme-light .ref-subtitle,
body.theme-light .ref-page-summary,
body.theme-light .ref-service-title,
body.theme-light .ref-service-kicker,
body.theme-light .ref-card-titleband,
body.theme-light .ref-card-label,
body.theme-light .ref-card-note,
body.theme-light .ref-point-list span,
body.theme-light .ref-point-list li,
body.theme-light .ref-service-link,
body.theme-light .w-form label,
body.theme-light .w-form input,
body.theme-light .w-form textarea,
body.theme-light.ref-page-shell p,
body.theme-light.ref-page-shell li,
body.theme-light.ref-page-shell span,
body.theme-light.ref-page-shell div,
body.theme-light.ref-page-shell a,
body.theme-light.ref-page-shell h1,
body.theme-light.ref-page-shell h2,
body.theme-light.ref-page-shell h3,
body.theme-light.ref-page-shell h4,
body.theme-light.ref-page-shell h5,
body.theme-light.ref-page-shell h6,
body.theme-light.ref-page-shell .heading,
body.theme-light.ref-page-shell .small-heading,
body.theme-light.ref-page-shell .paragraph,
body.theme-light.ref-page-shell .h3,
body.theme-light.ref-page-shell .h4,
body.theme-light.ref-page-shell .h5{
  color:#1e1a16 !important;
  opacity:1 !important;
}
body.theme-light .heading,
body.theme-light .h3,
body.theme-light .member-title,
body.theme-light .role-text,
body.theme-light .small-heading,
body.theme-light .ref-title,
body.theme-light .ref-heading,
body.theme-light .ref-display,
body.theme-light .ref-heading-main,
body.theme-light .ref-subtitle,
body.theme-light strong{
  text-shadow:none !important;
}
body.theme-light .h3-orange,
body.theme-light .orange-text,
body.theme-light .service-preview-kicker,
body.theme-light .service-preview-card h4,
body.theme-light .role-text,
body.theme-light .small-heading span,
body.theme-light .ref-kicker,
body.theme-light .ref-accent,
body.theme-light .ref-highlight,
body.theme-light .ref-pill,
body.theme-light .ref-service-kicker,
body.theme-light .ref-card-label,
body.theme-light .ref-subtitle span,
body.theme-light.ref-page-shell .gold,
body.theme-light.ref-page-shell .orange,
body.theme-light.ref-page-shell .accent{
  color:#c8942e !important;
}
body.theme-light .navbar-logo-left,
body.theme-light .navbar-logo-left-container,
body.theme-light .navbar-container,
body.theme-light .navbar-wrapper,
body.theme-light .nav-menu-wrapper,
body.theme-light .w-nav-overlay,
body.theme-light .w-nav-menu,
body.theme-light .navbar-right-div{
  background:#f5f0e6 !important;
}
body.theme-light .navbar-logo-left-container,
body.theme-light .navbar-wrapper,
body.theme-light .nav-menu-wrapper,
body.theme-light .main-content-block,
body.theme-light .main-content-block.gray,
body.theme-light .smaller-container.gray,
body.theme-light .smaller-container.smaller,
body.theme-light .team-member,
body.theme-light .service-card,
body.theme-light .relation-card,
body.theme-light .case-card,
body.theme-light .accordion-item-content,
body.theme-light .w-richtext,
body.theme-light .link-block,
body.theme-light .white-line,
body.theme-light .service-preview-shell,
body.theme-light .service-preview-card,
body.theme-light .ref-grid-card,
body.theme-light .ref-card,
body.theme-light .ref-service-card,
body.theme-light .ref-feature-card,
body.theme-light .ref-pillar-card,
body.theme-light .ref-stacked-card,
body.theme-light .ref-panel,
body.theme-light .ref-surface,
body.theme-light .ref-copy-block,
body.theme-light .ref-content-panel,
body.theme-light .ref-gallery-section .container,
body.theme-light .ref-page-shell img + div{
  border-color:rgba(30,26,22,.14) !important;
}
body.theme-light .team-member,
body.theme-light .service-card,
body.theme-light .relation-card,
body.theme-light .case-card,
body.theme-light .accordion-item-content,
body.theme-light .service-preview-card,
body.theme-light .link-block,
body.theme-light .ref-grid-card,
body.theme-light .ref-card,
body.theme-light .ref-service-card,
body.theme-light .ref-feature-card,
body.theme-light .ref-pillar-card,
body.theme-light .ref-stacked-card,
body.theme-light .ref-panel,
body.theme-light .ref-surface,
body.theme-light .ref-copy-block,
body.theme-light .ref-content-panel,
body.theme-light .smaller-container.gray,
body.theme-light .smaller-container.smaller{
  box-shadow:0 14px 30px rgba(56,41,18,.08) !important;
}
body.theme-light .white-line{background:rgba(30,26,22,.18) !important;}
body.theme-light .menu-button,
body.theme-light .w-nav-button,
body.theme-light .hamburger-icon,
body.theme-light .w-icon-nav-menu,
body.theme-light .text-link::after,
body.theme-light .link-block::after,
body.theme-light .cta-link::after{color:#1e1a16 !important;background:currentColor !important;}
body.theme-light .menu-button,
body.theme-light .w-nav-button{
  border:1px solid rgba(30,26,22,.14) !important;
  border-radius:999px !important;
  background:rgba(255,255,255,.82) !important;
}
body.theme-light .navbar-wrapper{
  gap:1rem !important;
}
body.theme-light .navbar-right-div{
  display:flex !important;
  align-items:center !important;
  gap:1rem !important;
}
body.theme-light .nav-menu-two{
  gap:0 !important;
}
body.theme-light .nav-menu-two .nav-link,
body.theme-light .text-link{
  color:#1e1a16 !important;
}
body.theme-light .nav-menu-wrapper{
  box-shadow:0 16px 28px rgba(56,41,18,.08) !important;
}
body.theme-light .navbar-brand img,
body.theme-light .small-logo,
body.theme-light .image-6,
body.theme-light .image-7,
body.theme-light .image-8,
body.theme-light .ref-mark{filter:invert(1) brightness(.15) !important;}
body.theme-light .social-link-block{background:rgba(30,26,22,.06) !important;border-color:rgba(30,26,22,.12) !important;}
body.theme-light .social-link-block img{filter:invert(1) brightness(.12) !important;}
body.theme-light .theme-toggle-button{background:rgba(255,255,255,.88)!important;color:#1d1a17!important;border:1px solid rgba(29,26,23,.12)!important;}
body.theme-light .theme-toggle-track{background:rgba(29,26,23,.08)!important;box-shadow:inset 0 0 0 1px rgba(29,26,23,.08)!important;}
body.theme-light .theme-toggle-thumb{background:#1d1a17!important;transform:translateX(1.2rem)!important;}
body.theme-dark .theme-toggle-thumb{transform:none!important;}
.theme-toggle-button{display:inline-flex;align-items:center;gap:.55rem;padding:.55rem .8rem;border-radius:999px;background:rgba(10,10,10,.72);color:#f4efe7;border:1px solid rgba(255,255,255,.1);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;cursor:pointer;}
.theme-toggle-track{position:relative;display:inline-flex;align-items:center;width:2.45rem;height:1.4rem;border-radius:999px;background:rgba(255,255,255,.16);padding:.15rem;transition:background-color .22s ease;}
.theme-toggle-thumb{display:block;width:1.05rem;height:1.05rem;border-radius:999px;background:#e2b24c;transition:transform .22s ease,background-color .22s ease;}
.theme-toggle-label{line-height:1;}
.mobile-theme-toggle{display:none!important;}
.nav-menu-wrapper .mobile-theme-toggle{margin:0 0 1rem auto;}
@media screen and (max-width: 991px){
  .navbar-right-div>.theme-toggle-button{display:none!important;}
  .nav-menu-wrapper .mobile-theme-toggle{display:inline-flex!important;justify-content:space-between;align-self:stretch;}
  body.theme-light .nav-menu-wrapper,
  body.theme-light .w-nav-overlay,
  body.theme-light .w-nav-menu{
    background:#f5f0e6 !important;
  }
}
</style>
""".strip()

SCRIPT_BLOCK = """
<script id="cross-page-theme-script">(function(){var body=document.body;if(!body)return;var desktopButton=document.getElementById('theme-toggle-button');var mobileButton=document.getElementById('mobile-theme-toggle-button');var buttons=[desktopButton,mobileButton].filter(Boolean);if(!buttons.length)return;var key='e4-theme';var darkClass='theme-dark';var lightClass='theme-light';var apply=function(theme){body.classList.remove(darkClass,lightClass);body.classList.add(theme==='light'?lightClass:darkClass);buttons.forEach(function(button){button.setAttribute('aria-pressed',theme==='light'?'true':'false');});};var saved='';try{saved=localStorage.getItem(key)||'';}catch(e){}apply(saved==='light'?'light':'dark');buttons.forEach(function(button){button.addEventListener('click',function(){var next=body.classList.contains(lightClass)?'dark':'light';apply(next);try{localStorage.setItem(key,next);}catch(e){}});});})();</script>
""".strip()

DESKTOP_BUTTON = '<button aria-label="Toggle light and dark mode" class="theme-toggle-button" id="theme-toggle-button" type="button"><span class="theme-toggle-track"><span class="theme-toggle-thumb"></span></span><span class="theme-toggle-label">Theme</span></button>'
MOBILE_BUTTON = '<button aria-label="Toggle light and dark mode" class="theme-toggle-button mobile-theme-toggle" id="mobile-theme-toggle-button" type="button"><span class="theme-toggle-label">Theme</span><span class="theme-toggle-track"><span class="theme-toggle-thumb"></span></span></button>'

body_re = re.compile(r'<body class="([^"]*)">', re.IGNORECASE)

for path in TARGETS:
    text = path.read_text()

    if 'id="cross-page-theme-system"' not in text:
        text = text.replace('</head>', STYLE_BLOCK + '</head>')
    else:
        text = re.sub(r'<style id="cross-page-theme-system">.*?</style>', STYLE_BLOCK, text, flags=re.DOTALL)

    def add_theme_class(match):
        classes = match.group(1).split()
        if 'theme-dark' not in classes and 'theme-light' not in classes:
            classes.append('theme-dark')
        return '<body class="' + ' '.join(classes) + '">' 

    text = body_re.sub(add_theme_class, text, count=1)

    if 'id="theme-toggle-button"' not in text:
        text = text.replace('</div><a class="text-link" href="/contact-us">Contact Us</a><div class="menu-button w-nav-button">', f'</div>{DESKTOP_BUTTON}<a class="text-link" href="/contact-us">Contact Us</a><div class="menu-button w-nav-button">', 1)

    if 'id="mobile-theme-toggle-button"' not in text:
        text = text.replace('<nav class="nav-menu-wrapper w-nav-menu" role="navigation"><ul class="nav-menu-two w-list-unstyled" role="list">', f'<nav class="nav-menu-wrapper w-nav-menu" role="navigation">{MOBILE_BUTTON}<ul class="nav-menu-two w-list-unstyled" role="list">', 1)

    if 'id="cross-page-theme-script"' in text:
        text = re.sub(r'<script id="cross-page-theme-script">.*?</script>', SCRIPT_BLOCK, text, flags=re.DOTALL)
    elif '</body>' in text:
        text = text.replace('</body>', SCRIPT_BLOCK + '</body>')
    elif '</html>' in text:
        text = text.replace('</html>', SCRIPT_BLOCK + '</html>')
    else:
        text = text.rstrip() + '\n' + SCRIPT_BLOCK + '\n'

    path.write_text(text)

print(f'patched {len(TARGETS)} files')
