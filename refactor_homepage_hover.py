from pathlib import Path

path = Path('/home/ubuntu/e4powerinc-clone/client/index.html')
html = path.read_text(encoding='utf-8')

body_old = '<body class="body">'
body_new = '<body class="body home-service-menu">'
if body_old in html:
    html = html.replace(body_old, body_new, 1)

quadrant_replacements = {
    'class="_1-4-grid tl w-inline-block" data-w-id="89cabf7d-9580-64ed-1682-99a79e9545ce" href="#engage"': 'class="_1-4-grid tl w-inline-block" data-w-id="89cabf7d-9580-64ed-1682-99a79e9545ce" data-pillar="engage" data-target-page="/engage/" href="#engage"',
    'class="_1-4-grid tr w-inline-block" data-w-id="7603e6e6-8145-33d6-64bd-53463a7a5425" href="#educate"': 'class="_1-4-grid tr w-inline-block" data-w-id="7603e6e6-8145-33d6-64bd-53463a7a5425" data-pillar="educate" data-target-page="/educate/" href="#educate"',
    'class="_1-4-grid bl w-inline-block" data-w-id="0a2fc853-7d39-1b4b-c098-31b03e5986a0" href="#elevate"': 'class="_1-4-grid bl w-inline-block" data-w-id="0a2fc853-7d39-1b4b-c098-31b03e5986a0" data-pillar="elevate" data-target-page="/elevate/" href="#elevate"',
    'class="_1-4-grid br w-inline-block" data-w-id="49ba5e82-9e65-7799-b3aa-17f25fe2f4ca" href="#empower"': 'class="_1-4-grid br w-inline-block" data-w-id="49ba5e82-9e65-7799-b3aa-17f25fe2f4ca" data-pillar="empower" data-target-page="/empower/" href="#empower"',
}
for old, new in quadrant_replacements.items():
    html = html.replace(old, new)

style_block = '''<style id="hero-service-menu-styles">
body.home-service-menu .service-preview-shell,
body.home-service-menu .service-preview-shell + ._120-spacer {
  display: none !important;
}
body.home-service-menu .hero-container {
  position: relative;
}
body.home-service-menu .hero-service-hover-shell {
  position: absolute;
  left: 50%;
  bottom: 2rem;
  transform: translateX(-50%);
  width: min(92vw, 880px);
  z-index: 20;
  pointer-events: none;
}
body.home-service-menu .hero-service-panel {
  display: none;
  pointer-events: auto;
  background: rgba(8, 8, 8, 0.92);
  border: 1px solid rgba(226,178,76,0.38);
  box-shadow: 0 24px 64px rgba(0,0,0,0.32);
  backdrop-filter: blur(12px);
  padding: 1.35rem 1.45rem 1.4rem;
}
body.home-service-menu .hero-service-panel.is-active {
  display: block;
}
body.home-service-menu .hero-service-top {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 1rem;
  flex-wrap: wrap;
}
body.home-service-menu .hero-service-kicker {
  color: #e2b24c;
  text-transform: uppercase;
  letter-spacing: .18em;
  font-size: .75rem;
}
body.home-service-menu .hero-service-title {
  color: #fff7ea;
  text-transform: uppercase;
  margin: .45rem 0 0;
  font-size: 1.55rem;
  line-height: 1.08;
}
body.home-service-menu .hero-service-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: .8rem 1rem;
  background: #e2b24c;
  color: #140e08;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .12em;
  font-size: .72rem;
  font-weight: 700;
}
body.home-service-menu .hero-service-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: .8rem;
  margin-top: 1rem;
}
body.home-service-menu .hero-service-item {
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.03);
  padding: .9rem 1rem;
}
body.home-service-menu .hero-service-item h4 {
  margin: 0;
  color: #f2bf5d;
  text-transform: uppercase;
  font-size: .92rem;
  line-height: 1.3;
}
body.home-service-menu .hero-service-item p {
  margin: .45rem 0 0;
  color: #e3d6c5;
  font-size: .95rem;
  line-height: 1.65;
}
body.home-service-menu .hero-service-empty {
  color: rgba(255,245,234,0.78);
  text-align: center;
  padding: 1rem 0 .4rem;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: .76rem;
}
@media screen and (max-width: 991px) {
  body.home-service-menu .hero-service-hover-shell {
    position: static;
    transform: none;
    width: auto;
    padding: 1.5rem 1rem 0;
  }
  body.home-service-menu .hero-service-grid {
    grid-template-columns: 1fr;
  }
}
</style>'''

if 'hero-service-menu-styles' not in html:
    html = html.replace('</head>', style_block + '\n</head>', 1)

script_block = '''<script id="hero-service-menu-script">
(function(){
  var data = {
    educate: {
      kicker: 'Educate Services',
      title: 'Hover to preview the Educate service group',
      href: '/educate/',
      label: 'Explore Educate',
      items: [
        {title: 'Speaking Engagements', copy: 'Keynotes, strategic sessions, and leadership talks for institutional audiences.'},
        {title: 'Workshops', copy: 'Structured learning programs for grant strategy, proposal review, partnerships, and compliance.'},
        {title: 'Technology & AI Literacy', copy: 'Practical education that helps teams understand modern tools without losing mission focus.'},
        {title: 'Leadership Development', copy: 'Capacity-building support that helps teams grow internal confidence and readiness.'}
      ]
    },
    empower: {
      kicker: 'Empower Services',
      title: 'Hover to preview the Empower service group',
      href: '/empower/',
      label: 'Explore Empower',
      items: [
        {title: 'Grant Writing', copy: 'Pre-award strategy and proposal-development support from opportunity discovery to submission.'},
        {title: 'Readiness Assessments', copy: 'Institutional reviews that reveal gaps, strengths, and fundable next moves.'},
        {title: 'Intellectual Property', copy: 'Protection and commercialization services for research and innovation assets.'},
        {title: 'IT & App Development', copy: 'Custom portals, web apps, websites, and IT support that expand delivery capacity.'}
      ]
    },
    elevate: {
      kicker: 'Elevate Services',
      title: 'Hover to preview the Elevate service group',
      href: '/elevate/',
      label: 'Explore Elevate',
      items: [
        {title: 'Grant Management', copy: 'Post-award reporting, compliance, and closeout support.'},
        {title: 'Project Management', copy: 'Structured delivery systems for complex research and workforce initiatives.'},
        {title: 'Financial Management', copy: 'Budget oversight and fiscal controls aligned with federal expectations.'},
        {title: 'IT Support Continuity', copy: 'Operational continuity support for launched digital systems and tools.'}
      ]
    },
    engage: {
      kicker: 'Engage Services',
      title: 'Hover to preview the Engage service group',
      href: '/engage/',
      label: 'Explore Engage',
      items: [
        {title: 'Institutional Discovery', copy: 'Early conversations that clarify goals, constraints, and the highest-value starting point.'},
        {title: 'Readiness-Led Onboarding', copy: 'Practical entry work that sets a baseline for future strategy and delivery.'},
        {title: 'Team-Led Partnership Model', copy: 'Introductions to the specialists most relevant to a client mission and growth stage.'},
        {title: 'Advisory Alignment', copy: 'Trust-building guidance that helps define the right first move together.'}
      ]
    }
  };

  function ready(fn){
    if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, {once:true});
    else fn();
  }

  ready(function(){
    var hero = document.querySelector('.hero-container');
    var targets = Array.prototype.slice.call(document.querySelectorAll('.emblem-grid [data-pillar]'));
    if(!hero || !targets.length) return;

    var shell = document.createElement('div');
    shell.className = 'hero-service-hover-shell';
    var panel = document.createElement('div');
    panel.className = 'hero-service-panel';
    panel.innerHTML = '<div class="hero-service-empty">Hover over a pillar to preview services</div>';
    shell.appendChild(panel);
    hero.appendChild(shell);

    var hideTimer = null;

    function render(key){
      var entry = data[key];
      if(!entry) return;
      var items = entry.items.map(function(item){
        return '<article class="hero-service-item"><h4>' + item.title + '</h4><p>' + item.copy + '</p></article>';
      }).join('');
      panel.innerHTML = '<div class="hero-service-top"><div><div class="hero-service-kicker">' + entry.kicker + '</div><h3 class="hero-service-title">' + entry.title + '</h3></div><a class="hero-service-link" href="' + entry.href + '">' + entry.label + '</a></div><div class="hero-service-grid">' + items + '</div>';
      panel.classList.add('is-active');
    }

    function scheduleHide(){
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function(){
        panel.classList.remove('is-active');
        panel.innerHTML = '<div class="hero-service-empty">Hover over a pillar to preview services</div>';
      }, 180);
    }

    targets.forEach(function(target){
      target.addEventListener('mouseenter', function(){
        clearTimeout(hideTimer);
        render(target.getAttribute('data-pillar'));
      });
      target.addEventListener('focus', function(){
        clearTimeout(hideTimer);
        render(target.getAttribute('data-pillar'));
      });
      target.addEventListener('mouseleave', scheduleHide);
      target.addEventListener('blur', scheduleHide);
    });

    panel.addEventListener('mouseenter', function(){ clearTimeout(hideTimer); });
    panel.addEventListener('mouseleave', scheduleHide);
  });
})();
</script>'''

if 'hero-service-menu-script' not in html:
    html = html.replace('</body></html>', script_block + '</body></html>', 1)

path.write_text(html, encoding='utf-8')
print('Patched homepage hero service hover menu in', path)
