"""Inner-page hero system: an overview plus About and Contact heroes that share the homepage hero's parts.
Kept apart from the main site; published as its own preview.
usage: python3 -I build_hero.py <scratchpad> <out dir> [--thumbs]"""
import sys, os, re, html

S, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
home = open(S + '/h/home.html').read().split('\n')
RAIL = '\n'.join(home[524:534]).replace('<span class="vt">', '<span class="vt" aria-hidden="true">')
NAV = ['Courses', 'About', 'Studio notes', 'Questions', 'Contact']
THUMBS = os.path.exists(OUT + '/thumbs/about-night.jpg')

SHELL = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<meta name="description" content="%%DESC%%">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Caveat:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/chrome.css">
<link rel="stylesheet" href="assets/hero.css">
<style>
%%CSS%%
</style>
</head>
<body>
<div class="cols" aria-hidden="true"><i></i><i></i><i></i></div>
%%RAIL%%
<div class="frame">
<header class="phone-bar"><a class="brand heading-5" href="#"><span class="strokes" aria-hidden="true"><i></i><i></i><i></i></span>Elena Varga <span>Atelier</span></a><button class="menu-btn button" type="button" aria-controls="siteDrawer" aria-expanded="false">Menu</button></header>
%%BAR%%
%%MAIN%%

<footer class="site-foot body-m">
  <div class="c"><h3 class="label">Learn</h3><a href="#">All courses</a><a href="#">Free lessons</a><a href="#">Gift a course</a><a href="#">FAQ</a></div>
  <div class="c"><h3 class="label">Studio</h3><a href="#">About Elena</a><a href="#">Gallery</a><a href="#">Studio notes</a><a href="#">Contact</a></div>
  <div class="c"><h3 class="label">Information</h3><a href="#">Commissions</a><a href="#">Components</a><a href="#">Site map</a><a href="#">Privacy</a><a href="#">Terms</a></div>
  <div class="base body-s"><span>© 2026 Elena Varga Atelier</span><span>Instagram · Pinterest · YouTube</span><span>Style · Components · Made by hand in Lisbon</span></div>
</footer>
</div>

<div class="menu-scrim"></div>
<div class="menu-drawer" id="siteDrawer" role="dialog" aria-modal="true" aria-label="Menu">
  <p class="menu-label label"><b>00</b>Menu</p>
  <nav aria-label="Menu">%%NAV%%</nav>
  <div class="menu-foot"><a class="btn btn-paper" href="#">Watch lesson 1 free <span class="ar" aria-hidden="true">→</span></a><address class="body-s">Rua da Graça 4, 3º · 1170-165 Lisboa<br>Letters read on Tuesday and Friday mornings</address></div>
</div>

<script>
  // Menu: the rail button (desktop) and the phone bar button open the same drawer; the scrim or Escape closes it.
  const drawer = document.getElementById('siteDrawer'), scrim = document.querySelector('.menu-scrim');
  const openers = [...document.querySelectorAll('.burger, .menu-btn')];
  let opener = null;
  const setDrawer = (open, from) => {
    document.body.classList.toggle('menu-open', open);
    openers.forEach(b => b.setAttribute('aria-expanded', open));
    if (open) { opener = from; drawer.querySelector('nav a').focus(); } else if (opener) opener.focus();
  };
  openers.forEach(b => b.addEventListener('click', () => setDrawer(!document.body.classList.contains('menu-open'), b)));
  scrim.addEventListener('click', () => setDrawer(false));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && document.body.classList.contains('menu-open')) setDrawer(false); });
%%JS%%</script>
</body>
</html>
'''

def shell(title, desc, css, main, js='', bar=''):
    nav = ''.join(f'<a href="#"{" aria-current=\"page\"" if i == 1 else ""}><small>0{i + 1}</small>{t}</a>' for i, t in enumerate(NAV))
    return (SHELL.replace('%%TITLE%%', title).replace('%%DESC%%', desc).replace('%%CSS%%', css).replace('%%RAIL%%', RAIL)
            .replace('%%BAR%%', bar).replace('%%MAIN%%', main).replace('%%NAV%%', nav).replace('%%JS%%', js))

PROTO = '''
.var-bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--space-3);padding:var(--space-3) var(--space-7);background:var(--night);color:var(--dim)}
.var-bar b{color:var(--paper);font-weight:var(--t-button-weight)}
.var-bar nav{display:flex;align-items:center;flex-wrap:wrap;gap:var(--space-4)}
.var-bar a{color:var(--paper);text-underline-offset:3px}
.var-bar a:hover{color:var(--accent-lt)}
.tone{display:inline-flex;gap:var(--space-1);padding:var(--space-1);border:1px solid var(--night-2);border-radius:var(--radius-pill)}
.tone button{height:28px;padding:0 var(--space-3);border:0;border-radius:var(--radius-pill);background:transparent;color:var(--dim);cursor:pointer}
.tone button[aria-pressed="true"]{background:var(--paper);color:var(--ink)}
.tone button:focus-visible{outline:2px solid var(--accent-lt);outline-offset:2px}
@media (max-width:980px){.var-bar{padding:var(--space-3) var(--gutter-phone)}}
'''

def bar(name, other):
    return (f'<!-- prototype bar: remove when the hero is attached to the page -->\n<div class="var-bar caption"><span><b>{name} hero</b> · not linked from the main site</span>'
            f'<nav aria-label="Preview"><span class="tone" role="group" aria-label="Tone"><button class="caption" type="button" data-tone="night" aria-pressed="true">Night</button><button class="caption" type="button" data-tone="paper" aria-pressed="false">Paper</button></span>'
            f'<a href="index.html">All heroes</a><a href="{other[0]}">{other[1]} →</a></nav></div>')

TONE_JS = '''  // Preview only: flip the hero between its night and paper tone.
  const hero = document.querySelector('.ih'), tones = [...document.querySelectorAll('.tone button')];
  tones.forEach(b => b.addEventListener('click', () => { hero.classList.toggle('ih-paper', b.dataset.tone === 'paper'); tones.forEach(x => x.setAttribute('aria-pressed', x === b)); }));
'''
if True:
    pass

NAVROW = '''<nav class="ih-nav" aria-label="Main"><a class="ih-brand heading-5" href="#"><span class="strokes" aria-hidden="true"><i></i><i></i><i></i></span>Elena Varga <span>Atelier</span></a><span class="ih-links body-m"><a href="#">FAQ</a><a href="#">Free lesson</a><a href="#">Log in</a></span></nav>'''
GUIDE = '<div class="ih-guide" aria-hidden="true"><i class="ih-line"></i><i class="ih-ring"></i></div>'

# ------------------------------------------------------------------ About
ABOUT_HERO = f'''<header class="ih ih-about">
  {GUIDE}
  {NAVROW}
  <div class="ih-body">
    <div class="ih-text">
      <p class="ih-label label"><b>02</b>The artist<i></i></p>
      <h1 class="ih-title display-m"><span>Elena</span><span class="soft">Varga.</span></h1>
      <p class="ih-intro body-l">Painter, illustrator and teacher. I film every lesson at my own table in Lisbon, at the speed I really work.</p>
    </div>
    <figure class="ih-pic"><img src="assets/img/portrait.jpg" alt="Elena Varga at her studio table" width="600" height="900"><figcaption class="ih-hand hand-s">at the table, Graça</figcaption></figure>
  </div>
  <div class="ih-foot"><p class="body-l">Since 2006 · Graça, Lisbon</p><a class="ih-cta body-l" href="#story">Read her story ↓</a></div>
</header>'''
ABOUT_NEXT = '''<section class="ab-next" id="story">
  <p class="ab-label label"><b>02</b>The artist<i></i></p>
  <h2 class="heading-3">The Atelier captures how Elena Varga draws, paints and teaches, at her own table and at her own pace, <span>for anyone willing to look closely.</span></h2>
  <div class="ab-cols">
    <p class="body-m">I started filming lessons in my Lisbon studio in 2016 because students kept asking the same question: “How do you actually see that?” Ten years and twelve thousand students later, these courses are my best answer, filmed at the speed I really work.</p>
    <p class="body-m">Painting changes slowly, so the Atelier does too. New courses arrive each season, along with guest sessions from painters and illustrators I admire, from ink to oil.</p>
  </div>
</section>'''
ABOUT_CSS = '''
.ab-next{max-width:960px;margin:0 auto;padding:var(--space-10) var(--space-7)}
.ab-label{display:flex;align-items:center;gap:var(--space-3);color:var(--ink-2)}
.ab-label b{font-weight:inherit;color:var(--terra-text)}
.ab-label i{width:34px;height:1px;background:var(--ink-2)}
.ab-next h2{margin-top:var(--space-5);color:var(--ink);text-wrap:balance}
.ab-next h2 span{color:var(--terra)}
.ab-cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-7);margin-top:var(--space-8);color:var(--ink)}
@media (max-width:980px){.ab-next{padding:var(--space-9) var(--gutter-phone)}.ab-cols{grid-template-columns:1fr;gap:var(--space-5)}}
'''

# ------------------------------------------------------------------ Contact
CONTACT_HERO = f'''<header class="ih ih-contact">
  {GUIDE}
  {NAVROW}
  <div class="ih-body">
    <span class="ih-hand hand-s">she answers every one</span>
    <p class="ih-label label"><b>05</b>Contact<i></i></p>
    <h1 class="ih-title display-l"><span>Contact</span> <span class="soft">me.</span></h1>
    <dl class="ih-facts body-l">
      <div><dt class="label">The studio</dt><dd>Rua da Graça 4, 3º<br>1170-165 Lisboa</dd></div>
      <div><dt class="label">Letters read</dt><dd>Tuesday and Friday<br>mornings</dd></div>
      <div><dt class="label">She replies</dt><dd>Within two<br>working days</dd></div>
    </dl>
  </div>
  <div class="ih-foot"><p class="body-l">Since 2010 · Graça, Lisbon</p><a class="ih-cta body-l" href="#write">Write to Elena ↓</a></div>
</header>'''
cm = open(S + '/site/pages/contact.main.html').read()
form = cm[cm.find('<div>\n      <form'):cm.rfind('</div>\n  </div>\n</main>')]
CONTACT_NEXT = f'''<section class="ct ct-after" id="write">
  <div class="ct-grid">
    <div class="ct-intro">
      <h2 class="heading-3">Tell her what you’re drawing.</h2>
      <p class="body-m">If it’s about a drawing, say which course and lesson. If it’s about a commission, say where it would hang.</p>
    </div>
    {form}
  </div>
</section>'''
CONTACT_CSS = open(S + '/site/pages/contact.css').read() + '''
.ct-after{padding-top:var(--space-10)}
.ct-after .ct-grid{margin-top:0;grid-template-columns:minmax(0,1fr) minmax(0,640px)}
.ct-intro{display:flex;flex-direction:column;gap:var(--space-4);max-width:360px}
.ct-intro h2{color:var(--ink)}
.ct-intro p{color:var(--ink-2)}
.ih-contact .ih-title span{display:inline}
@media (max-width:980px){.ct-after{padding-top:var(--space-9)}.ct-after .ct-grid{grid-template-columns:1fr}}
'''
CONTACT_JS = open(S + '/site/pages/contact.js').read()

open(OUT + '/about-hero.html', 'w').write(shell('About hero · Elena Varga Atelier', 'The About page hero, built from the homepage hero’s parts.', PROTO + ABOUT_CSS, ABOUT_HERO + ABOUT_NEXT, TONE_JS, bar('About', ('contact-hero.html', 'Contact'))))
open(OUT + '/contact-hero.html', 'w').write(shell('Contact hero · Elena Varga Atelier', 'The Contact page hero, built from the homepage hero’s parts.', PROTO + CONTACT_CSS, CONTACT_HERO + CONTACT_NEXT, TONE_JS + CONTACT_JS, bar('Contact', ('about-hero.html', 'About'))))
print('built about-hero.html, contact-hero.html')

# ------------------------------------------------------------------ overview
def thumb(n, alt):
    return f'<img src="thumbs/{n}.jpg" alt="{alt}" width="1326" height="560" loading="lazy">' if THUMBS else ''

PARTS = [
    ('Nav row', 'The same brand and three links as the homepage hero. Hidden on phones, where the phone bar already carries them.', 'Same on every page'),
    ('Guide line and ring', 'The drawing’s construction lines. The same two shapes on every page, moved and resized: that is what makes it one family without repeating the home composition.', 'Moves per page'),
    ('Numbered label', 'The mono “02 · The artist” eyebrow, as in the section heads on the homepage.', 'Same on every page'),
    ('Title', 'The only large type. Display on story pages (display-m, display-l), heading-1 on utility pages. Two tones: the first word in the main colour, the rest softer.', 'Size per page'),
    ('One picture, or none', 'Only in the homepage frame style: square corners, black and white. At most one, and not the wide photo the homepage uses.', 'Varies per page'),
    ('Foot row', 'A little meta on the left, one link on the right, as in the homepage hero’s bottom row.', 'Content per page'),
]
parts = ''.join(f'<li><span class="pt-n caption">{i + 1}</span><div><h3 class="heading-5">{e}</h3><p class="body-m">{d}</p></div><span class="pt-tag caption">{t}</span></li>' for i, (e, d, t) in enumerate(PARTS))
PAGES = [
    ('About', 'Night', 'display-m, name on two lines', 'One tall portrait', 'Since 2006 · Read her story'),
    ('Contact', 'Night', 'display-l, “Contact me.”', 'None; three facts in the hero', 'Since 2010 · Write to Elena'),
    ('Courses', 'Night', 'display-m, “Six courses.”', 'A strip of the six posters', 'Free lesson link'),
    ('Course page', 'Night', 'heading-1, course title in its colour', 'The course poster', 'Price and Enrol'),
    ('Lesson', 'Night', 'heading-1', 'The video, in the frame style', 'Lesson number · Next'),
    ('Studio notes', 'Paper', 'heading-1, short hero (360px)', 'None', 'Topic filters'),
    ('Login, Create account', 'Paper', 'heading-1', 'None (the form is the page)', 'Link to the other form'),
    ('Terms, Privacy', 'Paper', 'heading-1, short hero (360px)', 'None', 'Last updated'),
]
rows = ''.join(f'<li><span class="heading-5">{a}</span><span class="body-m">{b}</span><span class="body-m">{c}</span><span class="body-m">{d}</span><span class="body-m">{f}</span></li>' for a, b, c, d, f in PAGES)

OV_CSS = PROTO + '''
.vn{max-width:1180px;margin:0 auto;padding:var(--space-9) var(--space-7) var(--space-10)}
.ov-head{display:flex;flex-direction:column;gap:var(--space-4);max-width:760px}
.ov-head .label{color:var(--terra-text)}
.ov-head h1{color:var(--ink)}
.ov-head p{color:var(--ink-2)}
.ov-sec{margin-top:var(--space-10)}
.ov-sec > .label{color:var(--terra-text)}
.ov-sec h2{margin-top:var(--space-3);color:var(--ink);text-wrap:balance}
.ov-sec > p{max-width:640px;margin-top:var(--space-4);color:var(--ink-2)}
.ov-fig{position:relative;margin-top:var(--space-7);border:1px solid var(--rule)}
.ov-fig img{display:block;width:100%;height:auto}
.mk{position:absolute;display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--terra);color:var(--paper);transform:translate(-50%,-50%)}
.pt{list-style:none;margin-top:var(--space-7);border-top:1px solid var(--rule)}
.pt li{display:grid;grid-template-columns:40px minmax(0,1fr) 160px;gap:var(--space-4);align-items:start;padding:var(--space-5) 0;border-bottom:1px solid var(--rule)}
.pt-n{color:var(--terra-text)}
.pt p{margin-top:var(--space-1);color:var(--ink-2);max-width:620px}
.pt-tag{color:var(--muted);text-align:right}
.ex{list-style:none;align-items:start;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-7) var(--space-5);margin-top:var(--space-7)}
.ex a{display:flex;flex-direction:column;gap:var(--space-3);color:inherit;text-decoration:none}
.ex .pair{display:flex;flex-direction:column;gap:var(--space-2)}
.ex .pair img{display:block;width:100%;aspect-ratio:1326/570;object-fit:cover;object-position:top;border:1px solid var(--rule)}
.ex h3{color:var(--ink);transition:color .25s}
.ex a:hover h3{color:var(--terra)}
.ex p{color:var(--ink-2)}
.rc{list-style:none;margin-top:var(--space-7);border-top:1px solid var(--ink)}
.rc li{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.6fr) minmax(0,1.5fr) minmax(0,1.3fr) minmax(0,1.3fr);gap:var(--space-4);align-items:baseline;padding:var(--space-4) 0;border-bottom:1px solid var(--rule)}
.rc .rc-h{color:var(--muted);text-transform:uppercase}
.rc li span:not(.heading-5){color:var(--ink-2)}
.ov-note{margin-top:var(--space-7);padding:var(--space-5);background:var(--card);border:1px solid var(--rule);max-width:640px;color:var(--ink-2)}
@media (max-width:980px){
  .vn{padding:var(--space-8) var(--gutter-phone) var(--space-9)}
  .pt li{grid-template-columns:32px minmax(0,1fr)}.pt-tag{grid-column:2;text-align:left}
  .ex{grid-template-columns:1fr}
  .rc li{grid-template-columns:1fr;gap:var(--space-1)}.rc .rc-h{display:none}
}
'''
ov = f'''<main class="vn">
  <header class="ov-head">
    <p class="label">Inner pages</p>
    <h1 class="heading-1">One hero system, not one hero per page.</h1>
    <p class="body-l">The homepage hero is a composition: a small portrait, a wide photograph, the name. Copy it onto About and the pages look the same; ignore it and they feel like another site. The way out is to keep its <em>parts</em> and change the <em>composition</em> on each page.</p>
  </header>

  <section class="ov-sec">
    <p class="label">Anatomy</p>
    <h2 class="heading-2">Six parts, all taken from the homepage.</h2>
    <p class="body-m">Every inner hero is these six parts. Keep all six and it belongs to the family; change only what the last column says.</p>
    <div class="ov-fig">{thumb('about-night', 'The About hero with its six parts numbered')}
      <span class="mk caption" style="left:21.5%;top:6%">1</span><span class="mk caption" style="left:75%;top:9%">2</span><span class="mk caption" style="left:15%;top:19%">3</span><span class="mk caption" style="left:27%;top:33%">4</span><span class="mk caption" style="left:98%;top:21%">5</span><span class="mk caption" style="left:23.5%;top:87.5%">6</span>
    </div>
    <ol class="pt">{parts}</ol>
  </section>

  <section class="ov-sec">
    <p class="label">Two examples</p>
    <h2 class="heading-2">About and Contact, same parts, different pictures.</h2>
    <p class="body-m">Open either one and use the Night / Paper switch in the dark bar to see the same hero in both tones.</p>
    <ul class="ex">
      <li><a href="about-hero.html"><span class="pair">{thumb('about-night', 'About hero, night')}{thumb('about-paper', 'About hero, paper')}</span><h3 class="heading-4">About</h3><p class="body-m">The name large on the left, one tall portrait on the right with the ring behind it.</p></a></li>
      <li><a href="contact-hero.html"><span class="pair">{thumb('contact-night', 'Contact hero, night')}{thumb('contact-paper', 'Contact hero, paper')}</span><h3 class="heading-4">Contact</h3><p class="body-m">Type only. The facts that sat in a left column move into the hero, so the form starts right below.</p></a></li>
    </ul>
  </section>

  <section class="ov-sec">
    <p class="label">The rule for the other pages</p>
    <h2 class="heading-2">Night to sell and tell, paper to get things done.</h2>
    <p class="body-m">Story and course pages get the night hero (about 560px). Utility pages get the same parts on paper and shorter (about 360px), so a visitor reaches the form or the list fast. The homepage stays the only 864px hero.</p>
    <ol class="rc">
      <li class="rc-h caption"><span>Page</span><span>Tone</span><span>Title</span><span>Picture</span><span>Foot row</span></li>
      {rows}
    </ol>
    <p class="ov-note body-m">Not decided yet: whether Courses and Course pages should be night or paper. Night keeps them closest to the homepage; paper puts the colourful posters on a calmer ground.</p>
  </section>
</main>'''
open(OUT + '/index.html', 'w').write(shell('Inner page heroes', 'How the About, Contact and other inner-page heroes share the homepage hero’s parts.', OV_CSS, ov))
print('built index.html', 'thumbs' if THUMBS else 'no thumbs yet')
