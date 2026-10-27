"""Assemble site pages from the shared chrome + each page's own main, CSS and JS.
Every page loads assets/tokens.css (the design system) and assets/chrome.css (rail, drawer, footer, buttons)."""
import os, sys, shutil

S, R = sys.argv[1], sys.argv[2]
P = S + '/site/pages'
import json
# The site copy of the design system: tokens.css plus its "below 980px" rule (display steps down two places,
# headings one), generated from tokens.json so every size still comes from the scale.
tok = json.load(open(S + '/ds/project/tokens.json'))
st = {x['name']: x for g in tok['type']['groups'] for x in g['styles']}
STEP = {'display-xl': 'display-m', 'display-l': 'heading-1', 'display-m': 'heading-1', 'heading-1': 'heading-2',
        'heading-2': 'heading-3', 'heading-3': 'heading-4', 'heading-4': 'heading-5', 'title-caps': 'title-caps-s'}
rows = []
for a_, b_ in STEP.items():
    t = st[b_]
    rows += [f"--t-{a_}-size: {t['fontSize']}", f"--t-{a_}-lh: {t['lineHeight']}", f"--t-{a_}-ls: {t['letterSpacing']}", f"--t-{a_}-weight: {t['fontWeight']}"]
css = open(S + '/ds/project/tokens.css').read()
css += '\n/* Below 980px: display styles step down two places, headings one (README, Type) */\n@media (max-width: 980px) {\n  :root {\n    ' + ';\n    '.join(rows) + ';\n  }\n}\n'
open(R + '/assets/tokens.css', 'w').write(css)

home = open(S + '/h/home.html').read().split('\n')
rail = '\n'.join(home[524:534]).replace('<span class="vt">', '<span class="vt" aria-hidden="true">')

PAGES = {  # key: (output file, which nav link is current)
    'components': ('components.html', None),
    'notes': ('notes.html', 'notes.html'),
    'note': ('note.html', 'notes.html'),
    'contact': ('contact.html', 'contact.html'),
    'login': ('login.html', None),
    'register': ('register.html', None),
    'terms': ('terms.html', None),
    'privacy': ('privacy.html', None),
}
SHARED = {'login': 'auth', 'register': 'auth', 'terms': 'legal', 'privacy': 'legal'}  # pages that share one layout's CSS (and JS)
src = lambda key, ext: f'{P}/{key}.{ext}' if os.path.exists(f'{P}/{key}.{ext}') else f'{P}/{SHARED[key]}.{ext}'
NAV = [('courses.html', 'Courses'), ('about.html', 'About'), ('notes.html', 'Studio notes'), ('home.html#faq', 'Questions'), ('contact.html', 'Contact')]

def page(key):
    out, current = PAGES[key]
    title, desc = open(f'{P}/{key}.meta').read().strip().split('\n')
    css, main, js = (open(src(key, x)).read() for x in ('css', 'main.html', 'js'))
    cur = lambda h: ' aria-current="page"' if h == current else ''
    nav = ''.join(f'<a href="{h}"{cur(h)}><small>0{i + 1}</small>{t}</a>' for i, (h, t) in enumerate(NAV))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Caveat:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/chrome.css">
<style>
{css}
</style>
</head>
<body>
<div class="cols" aria-hidden="true"><i></i><i></i><i></i></div>
{rail}
<div class="frame">
<header class="phone-bar"><a class="brand heading-5" href="home.html"><span class="strokes" aria-hidden="true"><i></i><i></i><i></i></span>Elena Varga <span>Atelier</span></a><button class="menu-btn button" type="button" aria-controls="siteDrawer" aria-expanded="false">Menu</button></header>
{main}

<footer class="site-foot body-m">
  <div class="c"><h3 class="label">Learn</h3><a href="courses.html">All courses</a><a href="lesson.html">Free lessons</a><a href="course.html">Gift a course</a><a href="home.html#faq">FAQ</a><a href="login.html">Log in</a></div>
  <div class="c"><h3 class="label">Studio</h3><a href="about.html">About Elena</a><a href="home.html#gallery">Gallery</a><a href="notes.html">Studio notes</a><a href="contact.html">Contact</a></div>
  <div class="c"><h3 class="label">Information</h3><a href="contact.html">Commissions</a><a href="components.html">Components</a><a href="sitemap.html">Site map</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div>
  <div class="base body-s"><span>© 2026 Elena Varga Atelier</span><span>Instagram · Pinterest · YouTube</span><span><a href="style.html">Style</a> · <a href="components.html">Components</a> · Made by hand in Lisbon</span></div>
</footer>
</div>

<div class="menu-scrim"></div>
<div class="menu-drawer" id="siteDrawer" role="dialog" aria-modal="true" aria-label="Menu">
  <p class="menu-label label"><b>00</b>Menu</p>
  <nav aria-label="Menu">{nav}</nav>
  <div class="menu-foot"><a class="btn btn-paper" href="lesson.html">Watch lesson 1 free <span class="ar" aria-hidden="true">→</span></a><p class="menu-acct body-m"><a href="login.html">Log in</a> · <a href="register.html">Create an account</a></p><address class="body-s">Rua da Graça 4, 3º · 1170-165 Lisboa<br>Letters read on Tuesday and Friday mornings</address></div>
</div>

<script>
  // Menu: the rail button (desktop) and the phone bar button open the same drawer; the scrim or Escape closes it.
  const drawer = document.getElementById('siteDrawer'), scrim = document.querySelector('.menu-scrim');
  const openers = [...document.querySelectorAll('.burger, .menu-btn')];
  let opener = null;
  const setDrawer = (open, from) => {{
    document.body.classList.toggle('menu-open', open);
    openers.forEach(b => b.setAttribute('aria-expanded', open));
    if (open) {{ opener = from; drawer.querySelector('nav a').focus(); }} else if (opener) opener.focus();
  }};
  openers.forEach(b => b.addEventListener('click', () => setDrawer(!document.body.classList.contains('menu-open'), b)));
  scrim.addEventListener('click', () => setDrawer(false));
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape' && document.body.classList.contains('menu-open')) setDrawer(false); }});
{js}</script>
</body>
</html>
'''

for k in PAGES:
    open(R + '/' + PAGES[k][0], 'w').write(page(k))
    print('built', PAGES[k][0])
