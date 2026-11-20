"""Writes pages/home.main.html: the Figma "Desktop / Home" design as markup that uses only style-guide classes.
usage: python3 -I home_src.py <pages dir>"""
import sys, html
P = sys.argv[1]
e = html.escape

COURSES = [
    ('1', 'Foundations\nof drawing', 'course-1.jpg', 600, 600, 'Hands sketching in a spiral notebook', 'Beginner', '24', '6h 10m', '$79', 'Bestseller'),
    ('2', 'The portrait\nin pencil', 'course-2.jpg', 600, 490, 'Pencil portrait of a young woman', 'Intermediate', '18', '5h 40m', '$99', None),
    ('3', 'Watercolour\ngardens', 'course-3.jpg', 600, 960, 'Watercolour study of tulips', 'Beginner', '20', '4h 55m', '$89', None),
    ('4', 'Ink, line\n& silence', 'course-4.jpg', 600, 782, 'Brush-ink line drawing', 'Beginner', '14', '3h 20m', '$69', 'New'),
    ('5', 'Plein air\nin oil', 'course-5.jpg', 600, 900, 'Oil painting of a terrace in warm light', 'Advanced', '26', '8h 05m', '$129', 'New'),
    ('6', 'Abstract\ncolour', 'course-6.jpg', 600, 379, 'Abstract acrylic in green and yellow', 'Intermediate', '16', '4h 30m', '$89', 'New'),
]
courses = ''
for n, t, img, w, h, alt, lvl, les, run, price, badge in COURSES:
    b = f'<span class="badge caption">{badge}</span>' if badge else ''
    courses += (f'<li class="course" style="--c:var(--course-{n})"><a href="course.html">'
                f'<h3 class="heading-4">{e(t)}</h3>'
                f'<span class="poster">{b}<img src="assets/img/{img}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy"></span>'
                f'<dl class="meta"><div><dt class="caption">Level</dt><dd class="body-l">{lvl}</dd></div><div><dt class="caption">Lessons</dt><dd class="body-l">{les}</dd></div>'
                f'<div><dt class="caption">Running</dt><dd class="body-l">{run}</dd></div><div><dt class="caption">Admission</dt><dd class="body-l">{price}</dd></div></dl></a></li>')

WORKS = [
    [('ink-portrait.jpg', 1000, 1289, 'Portrait study, ink on paper', 'Ink on paper · 2025 · 42 × 30 cm', True, 31), ('meadow.jpg', 800, 419, 'Meadow, watercolour', 'Watercolour · 2024 · 30 × 40 cm', False, 25),
     ('gesture.jpg', 500, 372, 'Gesture study in ink', 'Ink · 2025', True, 13), ('blue-hour.jpg', 700, 933, 'Blue Hour, acrylic', 'Acrylic · 2023 · 60 × 80 cm', False, 19)],
    [('old-street.jpg', 800, 565, 'Old Street, watercolour', 'Watercolour · 2024 · 28 × 38 cm', False, 24), ('bridge.jpg', 600, 479, 'Bridge, watercolour', 'Watercolour · 2023', True, 17),
     ('fragments.jpg', 1000, 656, 'Fragments, acrylic', 'Acrylic · 2022 · 50 × 70 cm', False, 36)],
]
works = ''
for row in WORKS:
    works += '<div class="works-row">' + ''.join(
        f'<figure class="work{" dark" if dark else ""}" style="width:{pct}%"><span class="mat"><img src="assets/img/{f}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy"></span><figcaption class="body-s">{e(cap)}</figcaption></figure>'
        for f, w, h, alt, cap, dark, pct in row) + '</div>'

LETTERS = [('rose', 'I finally stopped erasing. Ink taught me to commit to the line.', 'Ana R.', 'Course 04 · Ink, Line & Silence'),
           ('terra', 'My washes used to turn to mud. Now I know exactly when to stop.', 'Tom H.', 'Course 03 · Watercolour Gardens'),
           ('ochre', 'The three-values lesson changed everything. My drawings finally look solid.', 'Priya S.', 'Course 01 · Foundations of Drawing')]
letters = ''.join(f'<li><blockquote class="letter lt-{c}"><span class="mark heading-1" aria-hidden="true">“</span><p class="heading-4">{e(q)}</p><footer><span class="button">{e(n)}</span><span class="caption">{e(k)}</span></footer></blockquote></li>' for c, q, n, k in LETTERS)

BOOK_SHUT = '<svg class="shut" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3.5h11.5v15H7.5A1.5 1.5 0 0 0 6 20z"/><path d="M6 20a1.5 1.5 0 0 0 1.5 1H18.5"/><path d="M6 4v16"/><path d="M10 7.5h4.5"/></svg>'
BOOK_OPEN = '<svg class="open" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6.5C9.6 5 6.6 4.7 3 5.3v13c3.6-.6 6.6-.3 9 1.2 2.4-1.5 5.4-1.8 9-1.2v-13c-3.6-.6-6.6-.3-9 1.2z"/><path d="M12 6.5v13"/><path d="M5.5 8.6c1.6-.2 3.1 0 4.4.6M5.5 11.4c1.6-.2 3.1 0 4.4.6M14.1 9.2c1.3-.6 2.8-.8 4.4-.6M14.1 12c1.3-.6 2.8-.8 4.4-.6"/></svg>'
QA = [('I’ve never drawn before. Is this for me?', 'Yes, and especially you. Foundations of Drawing assumes nothing. If you can hold a pencil and write your name, you can learn to draw.'),
      ('What materials do I need?', 'Each course has a downloadable materials list with budget and studio options. Most beginner courses need only a pencil, an eraser and a sketchbook.'),
      ('How long do I have access?', 'Forever. Buy once and watch at your own pace, including all future updates to that course.'),
      ('Can I get feedback on my work?', 'Every course includes one private video critique from me, plus access to our student community for ongoing encouragement.')]
faq = ''.join(f'<details{" open" if i == 0 else ""}><summary class="heading-4">{e(q)}{BOOK_SHUT}{BOOK_OPEN}</summary><p class="body-m">{e(a)}</p></details>' for i, (q, a) in enumerate(QA))

ICONS = {
    'Look': '<path d="M6 42 C 20 20, 64 20, 78 42 C 64 64, 20 64, 6 42 Z"/><path d="M42 30 a12 12 0 1 0 .1 0 Z"/>',
    'Sketch': '<path d="M58 8 L76 26 L30 72 L10 76 L14 56 Z M52 14 L70 32"/><path d="M8 82 C 30 74, 50 84, 80 76"/>',
    'Paint': '<path d="M70 6 L44 44 M38 46 C 28 46, 24 56, 26 62 C 20 70, 12 72, 8 72 C 20 80, 40 76, 46 62 C 50 54, 46 46, 38 46 Z"/><path d="M52 70 a6 6 0 1 0 .1 0 M66 58 a5 5 0 1 0 .1 0"/>',
}
STEPS = [('ochre', '01', 'Look', 'Short exercises that train your eye to see shapes, values and edges before you make a mark.'),
         ('rose', '02', 'Sketch', 'Draw along in real time. Elena works beside you and explains each decision as she makes it.'),
         ('terra', '03', 'Paint', 'Finish a real piece, then get a private video critique from Elena on what to try next.')]
steps = ''.join(f'<li class="hm-step st-{c}"><span class="caption">{n}</span><svg viewBox="0 0 84 84" aria-hidden="true">{ICONS[t]}</svg><h3 class="heading-3">{t}</h3><p class="body-m">{e(b)}</p></li>' for c, n, t, b in STEPS)

main = f'''<main class="hm">
  <section class="hm-hero" aria-labelledby="hm-title">
    <i class="hm-guide" aria-hidden="true"></i><i class="hm-ring" aria-hidden="true"></i>
    <nav class="hm-nav" aria-label="Quick links"><a class="hm-brand heading-5" href="home-v2.html"><span class="strokes" aria-hidden="true"><i></i><i></i><i></i></span>Elena Varga <span>Atelier</span></a><span class="hm-links body-m"><a href="#faq">FAQ</a><a href="lesson.html">Free lesson</a><a href="login.html">Log in</a></span></nav>
    <div class="hm-main">
      <div class="hm-intro">
        <img class="small" src="assets/img/portrait.jpg" alt="Elena Varga at her studio table, brush in hand" width="600" height="900">
        <h1 class="heading-3" id="hm-title"><span>Elena Varga.</span><span class="soft">Learn to draw what you see.</span></h1>
        <ul class="hm-roles body-l"><li>(1) Painter</li><li>(2) Illustrator</li><li>(3) Teacher</li></ul>
      </div>
      <div class="hm-show">
        <img class="big" src="assets/img/studio.jpg" alt="Elena among plaster and bronze casts in her Lisbon studio, holding a paintbrush" width="1400" height="2100">
        <div class="hm-bottom body-l"><span>Since 2006</span><a class="hm-cta" href="#courses">Explore the courses →</a></div>
      </div>
    </div>
  </section>

  <section class="hm-about" id="about" aria-labelledby="about-title">
    <div class="hm-statement">
      <p class="sec-label label"><b>02</b>The artist<i></i></p>
      <h2 class="heading-3" id="about-title">The Atelier captures how Elena Varga draws, paints and teaches, at her own table and at her own pace, <em>for anyone willing to look closely.</em></h2>
    </div>
    <div class="hm-story">
      <img src="assets/img/elena-chair.webp" alt="Elena Varga sitting on a wooden studio chair" width="1162" height="1354" loading="lazy">
      <div class="hm-story-text">
        <p class="body-m">I started filming lessons in my Lisbon studio in 2016 because students kept asking the same question: “How do you actually see that?” Ten years and twelve thousand students later, these courses are my best answer, filmed at the speed I really work.</p>
        <p class="body-m">Painting changes slowly, so the Atelier does too. New courses arrive each season, along with guest sessions from painters and illustrators I admire, from ink to oil. <a href="#join">Get the studio notes</a> to hear first.</p>
        <span class="signature" aria-hidden="true">Elena V.</span>
      </div>
    </div>
  </section>

  <section class="hm-method" aria-labelledby="method-title">
    <div class="hm-method-intro">
      <p class="sec-label on-night label"><b>03</b>How you’ll learn<i></i></p>
      <h2 class="heading-3" id="method-title">Look. Sketch. <em>Paint.</em></h2>
      <p class="body-l">Every course follows the same three steps, whether you’re holding a pencil or a brush. You always know what you’re doing and why.</p>
      <a class="caption" href="#courses">See the courses →</a>
    </div>
    <ol class="hm-steps">{steps}</ol>
  </section>

  <section class="hm-courses" id="courses" aria-labelledby="courses-title">
    <div class="hm-head">
      <p class="sec-label label"><b>04</b>The collection<i></i></p>
      <h2 class="heading-2" id="courses-title">Six courses, hung <em>like posters.</em></h2>
      <p class="body-l">Lifetime access, reference sheets and a private critique of your final piece. Three courses are new this autumn.</p>
    </div>
    <ul class="hm-grid">{courses}</ul>
  </section>

  <section class="hm-gallery" id="gallery" aria-labelledby="gallery-title">
    <div class="hm-head">
      <p class="sec-label label"><b>05</b>Selected works<i></i></p>
      <h2 class="heading-2" id="gallery-title">Hung in <em>the studio.</em></h2>
      <p class="note caption">Hung on centre · 145 cm · seven works, 2022–2025</p>
    </div>
    <div class="works">{works}</div>
  </section>

  <!-- Student letters and figures below are the site's sample content: replace with real, approved quotes and numbers before launch. -->
  <section class="hm-students" id="students" aria-labelledby="students-title">
    <div class="hm-students-head">
      <div><p class="sec-label on-night label"><b>06</b>Students<i></i></p><h2 class="heading-2" id="students-title">Letters from <em>the wall.</em></h2></div>
      <p class="body-m">Written by students after their final critique. Every one of them started with a pencil and no experience.</p>
    </div>
    <ul class="letters" aria-label="Student letters">{letters}</ul>
    <dl class="stats">
      <div><dt class="caption">Average rating · 2,870 reviews</dt><dd class="heading-2">4.9</dd></div>
      <div><dt class="caption">Students since 2016</dt><dd class="heading-2">12,400</dd></div>
      <div><dt class="caption">Pieces shared this year</dt><dd class="heading-2">3,100</dd></div>
      <div><dt class="caption">Countries</dt><dd class="heading-2">64</dd></div>
    </dl>
    <a class="body-m" href="#">Read all reviews →</a>
  </section>

  <section class="hm-faq" id="faq" aria-labelledby="faq-title">
    <div class="hm-head"><p class="sec-label label"><b>07</b>Questions<i></i></p><h2 class="heading-2" id="faq-title">Before you <em>begin.</em></h2></div>
    <div class="faq-list">{faq}</div>
  </section>

  <section class="hm-join" id="join" aria-label="Start drawing">
    <div class="hm-cta-band">
      <span class="stripes" aria-hidden="true"><i style="background:var(--ochre)"></i><i style="background:var(--terra)"></i><i style="background:var(--rose)"></i><i style="background:var(--plum)"></i><i style="background:var(--paper)"></i><i style="background:var(--sage)"></i></span>
      <h2 class="heading-1">Start drawing.</h2>
      <p class="body-m">Lesson 1 is free: twelve minutes, one pencil,<br>and whatever chair you’re sitting on.</p>
      <a class="btn btn-paper" href="lesson.html">Watch lesson 1 free <span class="ar" aria-hidden="true">→</span></a>
    </div>
    <div class="hm-news">
      <h2 class="heading-4">Get a <em>free 45-minute lesson</em> and monthly studio notes.</h2>
      <form class="news-form" id="newsForm" novalidate>
        <label class="vh" for="newsEmail">Email address</label>
        <div class="news-field"><input id="newsEmail" type="email" name="email" autocomplete="email" placeholder="Enter your email" required aria-describedby="newsMsg"><button type="submit" aria-label="Send me the free lesson"><span class="heading-5" aria-hidden="true">→</span></button></div>
        <p class="news-msg body-s" id="newsMsg" aria-live="polite"></p>
      </form>
    </div>
  </section>

  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"Elena Varga Atelier","description":"Online drawing and painting courses taught by Elena Varga from her studio in Lisbon.","address":{{"@type":"PostalAddress","streetAddress":"Rua da Graça 4, 3º","postalCode":"1170-165","addressLocality":"Lisboa","addressCountry":"PT"}},"founder":{{"@type":"Person","name":"Elena Varga"}}}}</script>
</main>'''
open(P + '/home.main.html', 'w').write(main)
open(P + '/home.meta', 'w').write('Elena Varga Atelier · Learn to draw what you see\nOnline drawing and painting courses from Elena Varga’s studio in Lisbon. Six courses, a free first lesson and a private critique of your final piece.\n')
open(P + '/home.js', 'w').write('''  // Newsletter: check the address, then thank them in place (the sandboxed preview blocks real form submission, so the button and Enter call it directly).
  const news = document.getElementById('newsForm'), email = document.getElementById('newsEmail'), msg = document.getElementById('newsMsg');
  const join = e => {
    e.preventDefault();
    const ok = email.checkValidity() && email.value.trim() !== '';
    email.setAttribute('aria-invalid', !ok);
    msg.classList.toggle('ok', ok);
    msg.textContent = ok ? 'Thank you. The lesson is on its way to ' + email.value.trim() + '.' : 'Add an email address, like marta@example.com.';
    if (!ok) email.focus();
  };
  news.addEventListener('submit', join);
  news.querySelector('button').addEventListener('click', join);
  email.addEventListener('keydown', e => { if (e.key === 'Enter') join(e); });
''')
print('wrote home.main.html, home.meta, home.js')
