"""Studio notes: five listing-page variations, built from the design system (assets/tokens.css + assets/chrome.css).
Kept apart from the main site: they are published as their own preview and nothing on the main site links to them.
usage: python3 -I build_var.py <scratchpad> <out dir>"""
import sys, os, html

S, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

home = open(S + '/h/home.html').read().split('\n')
RAIL = '\n'.join(home[524:534]).replace('<span class="vt">', '<span class="vt" aria-hidden="true">')
NAV = [('courses.html', 'Courses'), ('about.html', 'About'), ('notes.html', 'Studio notes'), ('home.html#faq', 'Questions'), ('contact.html', 'Contact')]

# ------------------------------------------------------------------ content
# (title, iso, shown, tags, image, w, h, alt, excerpt)
NOTES = [
    ('Choosing cartridge paper you won’t be afraid of', '2026-10-22', '22 Oct 2026', ['Materials', 'Paper'], 'meadow.jpg', 800, 419, 'Meadow, watercolour', 'A good sheet forgives the first wrong line. Here is how I test three papers in ten minutes, and the one I keep reaching for.'),
    ('When to stop a wash: watercolour’s last ten seconds', '2026-10-18', '18 Oct 2026', ['Technique', 'Watercolour'], 'course-3.jpg', 600, 960, 'Watercolour garden study', 'There is a moment when the paper still shines and the wash is almost right. Stop there, put the brush down, and count to ten.'),
    ('Three values, not seven: the squint test', '2026-10-12', '12 Oct 2026', ['Technique', 'Pencil'], 'ink-portrait.jpg', 1000, 1289, 'Portrait study in ink', 'Seven values sounds like craft; three is a habit. Squint, name them, and draw only what you named.'),
    ('Thirty seconds a drawing at the Ribeira market', '2026-10-09', '9 Oct 2026', ['Sketchbook', 'Ink'], 'old-street.jpg', 800, 565, 'Old Street, watercolour', 'Half a minute per drawing, forty drawings, one market morning. What a timer does to a nervous hand.'),
    ('Why every drawing starts with one plumb line', '2026-10-03', '3 Oct 2026', ['Technique', 'Pencil'], 'course-1.jpg', 600, 600, 'Pencil study', 'Before the first mark, hang a thread from a pin and let gravity do the first honest measurement.'),
    ('Ink teaches you to commit to the line', '2026-09-28', '28 Sep 2026', ['Sketchbook', 'Ink'], 'gesture.jpg', 500, 372, 'Gesture study in ink', 'A pencil lets you take it back. Ink won’t, and that is the whole lesson.'),
    ('Blue hour in Graça, painted from the studio window', '2026-09-21', '21 Sep 2026', ['Studio', 'Acrylic'], 'blue-hour.jpg', 700, 933, 'Blue Hour, acrylic', 'The window faces east, but the best colour arrives after the sun goes. Notes from a week of twilight panels.'),
    ('The bridge I drew forty times, and what changed', '2026-09-14', '14 Sep 2026', ['Sketchbook', 'Watercolour'], 'bridge.jpg', 600, 479, 'Bridge, watercolour', 'I drew the same bridge forty times last year. The forty-first looked nothing like the first, and that was the point.'),
    ('Mixing the in-between greys you can’t name', '2026-09-07', '7 Sep 2026', ['Materials', 'Acrylic'], 'course-6.jpg', 600, 379, 'Abstract colour study', 'The greys without a name are the ones that make a painting feel true. A mixing recipe, with failures.'),
    ('Ink, line and silence: notes from the new course', '2026-08-31', '31 Aug 2026', ['Course notes', 'Ink'], 'course-4.jpg', 600, 782, 'Ink study', 'Fourteen lessons, one brush pen and a lot of white paper: what we cut, what we kept, and why the course is quiet.'),
    ('Leave the lost edges lost', '2026-08-24', '24 Aug 2026', ['Technique', 'Acrylic'], 'fragments.jpg', 1000, 656, 'Fragments, acrylic', 'Not every edge deserves a line. A short argument for leaving the lost edges lost.'),
    ('Twenty Januaries at the same table', '2026-08-17', '17 Aug 2026', ['Letters', 'Studio'], 'studio.jpg', 1400, 2100, 'Elena at her studio table', 'Twenty Januaries at the same table: what changed, what stayed, and the chair that did not.'),
]
TOPICS = ['Technique', 'Materials', 'Sketchbook', 'Studio', 'Ink', 'Watercolour']
e = html.escape
slug = lambda t: t.lower().replace(' ', '-')
count = lambda t: sum(1 for n in NOTES if t in n[3])
tags_attr = lambda n: '|'.join(slug(t) for t in n[3])
pills = lambda n, cls='body-s': '<ul class="pills">' + ''.join(f'<li class="{cls}">{e(t)}</li>' for t in n[3]) + '</ul>'
img = lambda n, lazy=True, extra='': f'<img src="assets/img/{n[4]}" alt="{e(n[7])}" width="{n[5]}" height="{n[6]}"{" loading=\"lazy\"" if lazy else ""}{extra}>'

def chips(cls=''):
    out = f'<div class="chips {cls}" role="group" aria-label="Filter by topic"><button class="chip button" type="button" data-topic="all" aria-pressed="true">All<small class="caption">{len(NOTES)}</small></button>'
    for t in TOPICS:
        out += f'<button class="chip button" type="button" data-topic="{slug(t)}" aria-pressed="false">{e(t)}<small class="caption">{count(t)}</small></button>'
    return out + '</div>'

FILTER_JS = '''  // Topic filter: chips hide the notes that don't carry the topic.
  const chips = [...document.querySelectorAll('.chip')], items = [...document.querySelectorAll('.note[data-tags]')], cnt = document.getElementById('count');
  function apply(topic) {
    items.forEach(i => { i.hidden = topic !== 'all' && !i.dataset.tags.split('|').includes(topic); });
    chips.forEach(c => c.setAttribute('aria-pressed', c.dataset.topic === topic));
    if (cnt) { const n = items.filter(i => !i.hidden).length; cnt.textContent = n + (n === 1 ? ' note' : ' notes') + ' shown'; }
  }
  chips.forEach(c => c.addEventListener('click', () => apply(c.dataset.topic)));
'''

# ------------------------------------------------------------------ shared css
COMMON = '''
.vn{max-width:1336px;margin:0 auto;padding:var(--space-9) var(--space-7) var(--space-10)}
.var-bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--space-3);padding:var(--space-3) var(--space-7);background:var(--night);color:var(--dim)}
.var-bar b{color:var(--paper);font-weight:var(--t-button-weight)}
.var-bar nav{display:flex;gap:var(--space-4)}
.var-bar a{color:var(--paper);text-underline-offset:3px}
.var-bar a:hover{color:var(--accent-lt)}
.pills{display:flex;flex-wrap:wrap;gap:var(--space-1);list-style:none}
.pills li{padding:var(--space-1) var(--space-3);background:var(--pill);color:var(--terra-text)}
.chips{display:flex;flex-wrap:wrap;gap:var(--space-2)}
.chip{display:inline-flex;align-items:center;gap:var(--space-2);height:40px;padding:0 var(--space-4);border:1px solid var(--rule);border-radius:var(--radius-pill);background:transparent;color:var(--ink-2);cursor:pointer;transition:background .2s,color .2s,border-color .2s}
.chip small{color:var(--muted)}
.chip:hover{border-color:var(--ink)}
.chip[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.chip[aria-pressed="true"] small{color:var(--dim)}
.chip:focus-visible{outline:2px solid var(--terra);outline-offset:3px}
.note a{color:inherit;text-decoration:none}
.note a:focus-visible{outline:2px solid var(--terra);outline-offset:6px}
@media (max-width:980px){.vn{padding:var(--space-8) var(--gutter-phone) var(--space-9)}.var-bar{padding:var(--space-3) var(--gutter-phone)}}
'''

# ------------------------------------------------------------------ variations
def va():
    rows = ''.join(
        f'<li class="note" data-tags="{tags_attr(n)}" data-img="assets/img/{n[4]}"><a href="#"><time class="caption" datetime="{n[1]}">{n[2]}</time><span class="va-t heading-4">{e(n[0])}</span>{pills(n)}<span class="va-ar heading-5" aria-hidden="true">→</span></a></li>'
        for n in NOTES)
    css = '''
.va-head{display:flex;flex-direction:column;gap:var(--space-4);padding-bottom:var(--space-8)}
.va-eye{color:var(--terra-text)}
.va-title{color:var(--ink)}
.va-intro{max-width:560px;color:var(--ink-2)}
.va-bar{display:flex;justify-content:space-between;align-items:center;gap:var(--space-4);flex-wrap:wrap;padding-bottom:var(--space-6)}
.va-count{color:var(--muted)}
.va-list{list-style:none;border-bottom:1px solid var(--rule)}
.va-list li{border-top:1px solid var(--rule)}
.va-list a{display:grid;grid-template-columns:140px minmax(0,1fr) auto 32px;align-items:center;gap:var(--space-5);padding:var(--space-5) 0;transition:padding .35s cubic-bezier(.2,.7,.2,1)}
.va-list time{color:var(--muted)}
.va-t{color:var(--ink);transition:color .25s;text-wrap:balance}
.va-ar{color:var(--terra);transition:transform .3s}
.va-list a:hover,.va-list a:focus-visible{padding-left:var(--space-3)}
.va-list a:hover .va-t,.va-list a:focus-visible .va-t{color:var(--terra)}
.va-list a:hover .va-ar{transform:translateX(4px)}
.va-peek{position:fixed;left:0;top:0;width:240px;height:300px;margin:0;padding:var(--space-2);background:var(--card);box-shadow:var(--shadow-pinned);pointer-events:none;opacity:0;transform:translate(-9999px,0);transition:opacity .2s;z-index:30}
.va-peek.on{opacity:1}
.va-peek img{width:100%;height:100%;object-fit:cover}
@media (max-width:980px){.va-list a{grid-template-columns:1fr;gap:var(--space-2)}.va-ar,.va-peek{display:none}}
'''
    main = f'''<main class="vn">
  <header class="va-head">
    <p class="va-eye label">Journal · 48 notes</p>
    <h1 class="va-title display-m">Studio notes</h1>
    <p class="va-intro body-l">Short pieces from the studio in Graça on drawing, painting, materials and teaching.</p>
  </header>
  <div class="va-bar">{chips()}<p class="va-count caption" id="count" aria-live="polite">{len(NOTES)} notes shown</p></div>
  <ol class="va-list">{rows}</ol>
  <figure class="va-peek" aria-hidden="true"><img alt=""></figure>
</main>'''
    js = FILTER_JS + '''  // Hover a row to see its picture beside the cursor (mouse only).
  const peek = document.querySelector('.va-peek'), pimg = peek.querySelector('img');
  if (matchMedia('(hover: hover) and (min-width: 981px)').matches) items.forEach(i => {
    i.addEventListener('mouseenter', () => { pimg.src = i.dataset.img; peek.classList.add('on'); });
    i.addEventListener('mousemove', e => { peek.style.transform = 'translate(' + (e.clientX + 28) + 'px,' + (e.clientY - 150) + 'px)'; });
    i.addEventListener('mouseleave', () => peek.classList.remove('on'));
  });
'''
    return css, main, js


def vb():
    f = NOTES[0]
    cards = ''.join(
        f'<li class="note vb-card" data-tags="{tags_attr(n)}"><a href="#"><span class="vb-ph">{img(n)}</span><span class="title heading-5">{e(n[0])}</span></a><time class="caption" datetime="{n[1]}">{n[2]}</time>{pills(n)}</li>'
        for n in NOTES[1:])
    css = '''
.vb-head{display:flex;justify-content:space-between;align-items:flex-end;gap:var(--space-6);flex-wrap:wrap}
.vb-head h1{color:var(--ink)}
.vb-head p{max-width:360px;color:var(--ink-2)}
.vb-chips{margin-top:var(--space-7)}
.vb-feature{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:var(--space-7);align-items:center;margin-top:var(--space-6);padding:var(--space-5);background:var(--card);border:1px solid var(--rule)}
.vb-fimg{display:block;aspect-ratio:16/10;overflow:hidden;background:var(--page)}
.vb-fimg img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.vb-feature:hover .vb-fimg img{transform:scale(1.03)}
.vb-ftxt{display:flex;flex-direction:column;align-items:flex-start;gap:var(--space-4);padding-right:var(--space-5)}
.vb-ftxt .label{color:var(--terra-text)}
.vb-ftxt h2 a{color:var(--ink);text-decoration:none;text-wrap:balance}
.vb-ftxt h2 a:hover{color:var(--terra)}
.vb-ftxt p{color:var(--ink-2)}
.vb-meta{display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-3);color:var(--muted)}
.vb-grid{list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-8) var(--space-5);margin-top:var(--space-8);align-items:start}
.vb-card a{display:flex;flex-direction:column;gap:var(--space-4)}
.vb-ph{display:block;aspect-ratio:4/3;overflow:hidden;background:var(--card)}
.vb-ph img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.vb-card a:hover .vb-ph img{transform:scale(1.04)}
.vb-card .title{color:var(--ink);transition:color .25s;text-wrap:pretty}
.vb-card a:hover .title{color:var(--terra)}
.vb-card time{display:block;margin-top:var(--space-2);color:var(--muted)}
.vb-card .pills{margin-top:var(--space-3)}
.vb-more{display:flex;justify-content:center;margin-top:var(--space-10)}
@media (max-width:1180px){.vb-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:980px){.vb-feature{grid-template-columns:1fr;gap:var(--space-5)}.vb-ftxt{padding:0 var(--space-3) var(--space-3)}}
@media (max-width:600px){.vb-grid{grid-template-columns:1fr;gap:var(--space-7)}}
'''
    main = f'''<main class="vn">
  <header class="vb-head"><h1 class="heading-2">Studio notes</h1><p class="body-m">Notes from the studio in Graça, since 2016 · 48 notes</p></header>
  {chips('vb-chips')}
  <article class="vb-feature">
    <a class="vb-fimg" href="#" tabindex="-1" aria-hidden="true">{img(f, False)}</a>
    <div class="vb-ftxt">
      <p class="label">Latest note</p>
      <h2 class="heading-3"><a href="#">{e(f[0])}</a></h2>
      <p class="body-l">{e(f[8])}</p>
      <div class="vb-meta"><time class="caption" datetime="{f[1]}">{f[2]}</time>{pills(f)}</div>
      <a class="btn" href="#">Read the note <span class="ar" aria-hidden="true">→</span></a>
    </div>
  </article>
  <ol class="vb-grid">{cards}</ol>
  <div class="vb-more"><button class="btn" type="button">Load more notes <span class="ar" aria-hidden="true">↓</span></button></div>
</main>'''
    return css, main, FILTER_JS.replace("document.getElementById('count')", "null")


def vc():
    items = ''.join(
        f'<li class="note" data-tags="{tags_attr(n)}" data-title="{e(n[0].lower())}"><a href="#">{img(n)}<span class="title body-l">{e(n[0])}</span></a><p class="vc-meta caption">{n[2]} · {" · ".join(e(t) for t in n[3])}</p></li>'
        for n in NOTES)
    topics = f'<li><button class="vc-topic body-m" type="button" data-topic="all" aria-pressed="true">All notes<small class="caption">{len(NOTES)}</small></button></li>' + ''.join(
        f'<li><button class="vc-topic body-m" type="button" data-topic="{slug(t)}" aria-pressed="false">{e(t)}<small class="caption">{count(t)}</small></button></li>' for t in TOPICS)
    css = '''
.vc-wrap{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:var(--space-8);align-items:start}
.vc-side{position:sticky;top:var(--space-7);display:flex;flex-direction:column;gap:var(--space-5)}
.vc-side h1{color:var(--ink)}
.vc-side > p{color:var(--ink-2)}
.vc-search{display:flex;flex-direction:column;gap:var(--space-2)}
.vc-search span{color:var(--muted)}
.vc-in{width:100%;height:48px;padding:0;border:0;border-bottom:1px solid var(--ink);border-radius:0;background:transparent;font-family:var(--t-body-l-font);font-size:var(--t-body-l-size);line-height:var(--t-body-l-lh);letter-spacing:var(--t-body-l-ls);font-weight:var(--t-body-l-weight);color:var(--ink)}
.vc-in::placeholder{color:var(--muted)}
.vc-in:focus{outline:none;border-bottom:2px solid var(--terra)}
.vc-topics{list-style:none;border-top:1px solid var(--rule)}
.vc-topics li{border-bottom:1px solid var(--rule)}
.vc-topic{display:flex;justify-content:space-between;align-items:baseline;width:100%;padding:var(--space-3) 0;border:0;background:transparent;color:var(--ink-2);cursor:pointer;text-align:left;transition:color .2s,padding .3s cubic-bezier(.2,.7,.2,1)}
.vc-topic small{color:var(--muted)}
.vc-topic:hover,.vc-topic[aria-pressed="true"]{color:var(--ink);padding-left:var(--space-2)}
.vc-topic[aria-pressed="true"] small{color:var(--terra-text)}
.vc-topic:focus-visible{outline:2px solid var(--terra);outline-offset:2px}
.vc-label{color:var(--muted)}
.vc-masonry{list-style:none;column-count:2;column-gap:var(--space-5)}
.vc-masonry li{break-inside:avoid;margin-bottom:var(--space-7)}
.vc-masonry img{display:block;width:100%;height:auto;background:var(--card)}
.vc-masonry .title{display:block;margin-top:var(--space-4);color:var(--ink);transition:color .25s;text-wrap:pretty}
.vc-masonry a:hover .title{color:var(--terra)}
.vc-meta{margin-top:var(--space-2);color:var(--muted)}
.vc-empty{padding:var(--space-8) 0;color:var(--ink-2)}
@media (max-width:980px){.vc-wrap{grid-template-columns:1fr;gap:var(--space-7)}.vc-side{position:static}}
@media (max-width:600px){.vc-masonry{column-count:1}}
'''
    main = f'''<main class="vn">
  <div class="vc-wrap">
    <aside class="vc-side">
      <h1 class="heading-3">Studio notes</h1>
      <p class="body-m">Notes from the studio in Graça, since 2016 · 48 notes</p>
      <label class="vc-search"><span class="caption">Search</span><input class="vc-in" id="q" type="search" placeholder="Search the notes" autocomplete="off"></label>
      <nav aria-label="Topics"><p class="vc-label label">Topics</p><ul class="vc-topics">{topics}</ul></nav>
      <a class="btn" href="#">Get the studio notes <span class="ar" aria-hidden="true">→</span></a>
    </aside>
    <div>
      <ol class="vc-masonry">{items}</ol>
      <p class="vc-empty body-l" id="empty" hidden>No notes match that yet. Try another word or topic.</p>
    </div>
  </div>
</main>'''
    js = '''  // Topic list and search work together.
  const topics = [...document.querySelectorAll('.vc-topic')], items = [...document.querySelectorAll('.note[data-tags]')], q = document.getElementById('q'), empty = document.getElementById('empty');
  let topic = 'all';
  function apply() {
    const term = q.value.trim().toLowerCase();
    items.forEach(i => { i.hidden = (topic !== 'all' && !i.dataset.tags.split('|').includes(topic)) || (term && !i.dataset.title.includes(term)); });
    topics.forEach(c => c.setAttribute('aria-pressed', c.dataset.topic === topic));
    empty.hidden = items.some(i => !i.hidden);
  }
  topics.forEach(c => c.addEventListener('click', () => { topic = c.dataset.topic; apply(); }));
  q.addEventListener('input', apply);
'''
    return css, main, js


def vd():
    rows = ''.join(
        f'<li class="note"><a class="vd-img" href="#" tabindex="-1" aria-hidden="true">{img(n)}</a><div class="vd-body"><div class="vd-meta"><time class="caption" datetime="{n[1]}">{n[2]}</time>{pills(n)}</div><h2 class="heading-3"><a href="#">{e(n[0])}</a></h2><p class="body-m">{e(n[8])}</p><a class="vd-more body-m" href="#">Read the note →</a></div></li>'
        for n in NOTES)
    css = '''
.vd-head{max-width:760px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:var(--space-4);text-align:center}
.vd-hand{color:var(--ink-2)}
.vd-head h1{color:var(--ink)}
.vd-head p{color:var(--ink-2);text-wrap:balance}
.vd-list{list-style:none;max-width:1080px;margin:var(--space-9) auto 0;border-bottom:1px solid var(--rule)}
.vd-list > li{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);gap:var(--space-7);align-items:center;padding:var(--space-8) 0;border-top:1px solid var(--rule)}
.vd-list > li:nth-child(even) .vd-img{order:2}
.vd-img{display:block;aspect-ratio:4/3;overflow:hidden;background:var(--card)}
.vd-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.vd-list > li:hover .vd-img img{transform:scale(1.03)}
.vd-body{display:flex;flex-direction:column;align-items:flex-start;gap:var(--space-4)}
.vd-meta{display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-3);color:var(--muted)}
.vd-body h2 a{color:var(--ink);transition:color .25s;text-wrap:balance}
.vd-body h2 a:hover{color:var(--terra)}
.vd-body p{max-width:440px;color:var(--ink-2)}
.vd-more{color:var(--ink);text-underline-offset:3px}
.vd-more:hover{color:var(--terra)}
.vd-end{display:flex;justify-content:center;margin-top:var(--space-9)}
@media (max-width:980px){.vd-list > li{grid-template-columns:1fr;gap:var(--space-5);padding:var(--space-7) 0}.vd-list > li:nth-child(even) .vd-img{order:0}}
'''
    main = f'''<main class="vn">
  <header class="vd-head">
    <span class="vd-hand hand-s">from the studio table</span>
    <h1 class="heading-1">Studio notes</h1>
    <p class="body-l">Short pieces on drawing, painting, materials and teaching, written in Graça since 2016. Forty-eight so far.</p>
  </header>
  <ol class="vd-list">{rows}</ol>
  <div class="vd-end"><button class="btn" type="button">Load more notes <span class="ar" aria-hidden="true">↓</span></button></div>
</main>'''
    return css, main, ''


def ve():
    # (note index, kind, colour or None, size class, title style)
    T = [(0, 'img', None, 'w2 h2', 'heading-4'), (1, 'txt', 'ochre', '', 'heading-5'), (2, 'img', None, 'h2', 'heading-5'), (3, 'txt', 'night', '', 'heading-5'),
         (4, 'img', None, '', 'heading-5'), (5, 'txt', 'rose', '', 'heading-5'), (7, 'img', None, 'w2', 'heading-4'), (6, 'img', None, 'h2', 'heading-5'),
         (9, 'txt', 'page', '', 'heading-5'), (8, 'img', None, 'w2', 'heading-4'), (10, 'img', None, '', 'heading-5'), (11, 'txt', 'ochre', 'w2', 'heading-4')]
    tiles = ''
    for i, kind, colour, size, ts in T:
        n = NOTES[i]
        if kind == 'img':
            tiles += f'<li class="note {size}"><a class="ve-t ve-img" href="#">{img(n)}<span class="ve-cap"><time class="caption" datetime="{n[1]}">{n[2]}</time><span class="{ts}">{e(n[0])}</span></span></a></li>'
        else:
            tiles += f'<li class="note {size}"><a class="ve-t ve-txt ve-{colour}" href="#"><span class="ve-top"><time class="caption" datetime="{n[1]}">{n[2]}</time><span class="caption">{e(n[3][0])}</span></span><span class="{ts}">{e(n[0])}</span></a></li>'
    css = '''
.ve-head{display:flex;justify-content:space-between;align-items:flex-end;gap:var(--space-6);flex-wrap:wrap;padding-bottom:var(--space-7)}
.ve-head h1{color:var(--ink)}
.ve-head p{max-width:360px;color:var(--ink-2)}
.ve-grid{list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:280px;grid-auto-flow:dense;gap:var(--space-5)}
.ve-grid > li{min-width:0}
.ve-grid > li.w2{grid-column:span 2}
.ve-grid > li.h2{grid-row:span 2}
.ve-t{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:var(--space-4);height:100%;padding:var(--space-5);overflow:hidden}
.ve-grid .ve-img{padding:0;justify-content:flex-end;background:var(--night);color:var(--paper)}
.ve-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.ve-img::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,var(--night) 100%);opacity:.92}
.ve-img:hover img{transform:scale(1.05)}
.ve-cap{position:relative;z-index:1;display:flex;flex-direction:column;gap:var(--space-1);padding:var(--space-5)}
.ve-cap time{color:var(--paper)}
.ve-top{display:flex;justify-content:space-between;gap:var(--space-3)}
.ve-top .caption{white-space:nowrap}
.ve-txt{transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.ve-txt:hover{transform:translateY(-4px)}
.ve-grid .ve-ochre{background:var(--ochre);color:var(--ink)}
.ve-grid .ve-rose{background:var(--rose);color:var(--ink)}
.ve-grid .ve-night{background:var(--night);color:var(--paper)}
.ve-night .ve-top{color:var(--dim)}
.ve-grid .ve-page{background:var(--card);color:var(--ink);box-shadow:inset 0 0 0 1px var(--rule)}
.ve-page .ve-top{color:var(--muted)}
.ve-t:focus-visible{outline:2px solid var(--terra);outline-offset:4px}
.ve-more{display:flex;justify-content:center;margin-top:var(--space-9)}
@media (max-width:980px){.ve-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:600px){.ve-grid{grid-template-columns:1fr;grid-auto-rows:auto}.ve-grid > li.w2,.ve-grid > li.h2{grid-column:auto;grid-row:auto}.ve-t{min-height:280px}}
'''
    main = f'''<main class="vn">
  <header class="ve-head"><h1 class="heading-1">Studio notes</h1><p class="body-m">Notes from the studio in Graça, since 2016 · 48 notes</p></header>
  <ol class="ve-grid">{tiles}</ol>
  <div class="ve-more"><button class="btn" type="button">Load more notes <span class="ar" aria-hidden="true">↓</span></button></div>
</main>'''
    return css, main, ''


VARS = [
    ('a', 'A', 'Index', 'A typographic list: date, title and topics on one line. Hover a row to see its picture.', va),
    ('b', 'B', 'Featured and grid', 'The latest note large, then a three-column grid with topic filters.', vb),
    ('c', 'C', 'Sidebar and masonry', 'A sticky sidebar with search and topics beside a two-column masonry of pictures at their own shape.', vc),
    ('d', 'D', 'Journal rows', 'One wide row per note with an excerpt, like a magazine contents page.', vd),
    ('e', 'E', 'Mosaic', 'A dense mosaic of pictures and coloured text tiles, no filters.', ve),
]

# ------------------------------------------------------------------ shell (same chrome as the main site)
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
  <div class="c"><h3 class="label">Studio</h3><a href="#">About Elena</a><a href="#">Gallery</a><a href="#" aria-current="page">Studio notes</a><a href="#">Contact</a></div>
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

def shell(title, desc, css, main, js, bar=''):
    nav = ''.join(f'<a href="#"{" aria-current=\"page\"" if t == "Studio notes" else ""}><small>0{i + 1}</small>{t}</a>' for i, (h, t) in enumerate(NAV))
    return (SHELL.replace('%%TITLE%%', title).replace('%%DESC%%', desc).replace('%%CSS%%', css).replace('%%RAIL%%', RAIL)
            .replace('%%BAR%%', bar).replace('%%MAIN%%', main).replace('%%NAV%%', nav).replace('%%JS%%', js))

def bar(i):
    key, letter, name, _, _ = VARS[i]
    prev, nxt = VARS[(i - 1) % 5], VARS[(i + 1) % 5]
    return (f'<!-- prototype bar: remove when a variation is chosen -->\n<div class="var-bar caption"><span><b>Variation {letter}</b> · {name} · not linked from the main site</span>'
            f'<nav aria-label="Variations"><a href="index.html">All variations</a><a href="notes-{prev[0]}.html">← {prev[1]}</a><a href="notes-{nxt[0]}.html">{nxt[1]} →</a></nav></div>')

for i, (key, letter, name, desc, fn) in enumerate(VARS):
    css, main, js = fn()
    open(f'{OUT}/notes-{key}.html', 'w').write(shell(f'Studio notes {letter} · Elena Varga Atelier', desc, COMMON + css, main, js, bar(i)))
    print('built notes-' + key + '.html')

# ------------------------------------------------------------------ hub
hub_css = COMMON + '''
.hb-head{display:flex;flex-direction:column;gap:var(--space-4);max-width:720px}
.hb-head .label{color:var(--terra-text)}
.hb-head h1{color:var(--ink)}
.hb-head p{color:var(--ink-2)}
.hb-grid{list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-8) var(--space-5);margin-top:var(--space-8)}
.hb-card a{display:flex;flex-direction:column;gap:var(--space-4);color:inherit;text-decoration:none}
.hb-ph{display:block;aspect-ratio:16/10;overflow:hidden;background:var(--card);border:1px solid var(--rule)}
.hb-ph img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.hb-card a:hover .hb-ph img{transform:scale(1.03)}
.hb-top{display:flex;align-items:baseline;gap:var(--space-3)}
.hb-top .caption{color:var(--terra-text)}
.hb-card h2{color:var(--ink);transition:color .25s}
.hb-card a:hover h2{color:var(--terra)}
.hb-card p{max-width:520px;color:var(--ink-2)}
@media (max-width:980px){.hb-grid{grid-template-columns:1fr}}
'''
cards = ''.join(
    f'<li class="hb-card"><a href="notes-{k}.html"><span class="hb-ph"><img src="thumbs/{k}.jpg" alt="Preview of variation {l}" width="1200" height="750"></span><span class="hb-top"><span class="caption">Variation {l}</span></span><h2 class="heading-3">{n}</h2><p class="body-m">{d}</p></a></li>'
    for k, l, n, d, _ in VARS)
hub = f'''<main class="vn">
  <header class="hb-head">
    <p class="label">Studio notes · listing page</p>
    <h1 class="heading-1">Five variations.</h1>
    <p class="body-l">Five ways to lay out the Studio notes page, all built from the style guide. They are kept apart from the main site while we iterate; pick one (or mix) and it gets attached at the end.</p>
  </header>
  <ol class="hb-grid">{cards}</ol>
</main>'''
open(f'{OUT}/index.html', 'w').write(shell('Studio notes variations', 'Five layout variations of the Studio notes listing page, kept apart from the main site.', hub_css, hub, ''))
print('built index.html')
