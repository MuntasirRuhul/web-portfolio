// Elena Varga Atelier · site.js (shared behaviour; see openspec change atelier-site-pages)
// Pages add in <head>, before any CSS paints:
//   <script>try{var m=new URLSearchParams(location.search).get('mode')||localStorage.getItem('atelier-mode');document.documentElement.dataset.mode=m==='academy'?'academy':'solo'}catch(e){document.documentElement.dataset.mode='solo'}document.documentElement.classList.add('js')</script>
// and at the end of <body>: <script src="assets/site.js"></script>
(function () {
  const html = document.documentElement;
  const store = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
                  set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} } };

  // Phone menu
  const menuBtn = document.querySelector('.menu-btn'), menu = document.getElementById('siteMenu');
  if (menuBtn && menu) {
    const set = open => { menuBtn.setAttribute('aria-expanded', open); menu.hidden = !open; };
    menuBtn.addEventListener('click', () => set(menu.hidden));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { set(false); menuBtn.focus(); } });
  }

  // Review bar: Solo / Academy, plus the page's own states from <body data-states="a,b" data-states-label="View">
  const bar = document.createElement('div');
  bar.className = 'review-bar'; bar.setAttribute('role', 'group'); bar.setAttribute('aria-label', 'Review switches');
  const group = (label, values, current, onPick) => {
    const g = document.createElement('div'); g.className = 'grp';
    g.innerHTML = `<span>${label}</span>` + values.map(v => `<button type="button" data-v="${v}" aria-pressed="${v === current}">${v[0].toUpperCase() + v.slice(1)}</button>`).join('');
    g.querySelectorAll('button').forEach(b => b.addEventListener('click', () => { g.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x === b)); onPick(b.dataset.v); }));
    bar.appendChild(g);
  };
  group('Mode', ['solo', 'academy'], html.dataset.mode || 'solo', v => {
    html.dataset.mode = v; store.set('atelier-mode', v);
    document.dispatchEvent(new CustomEvent('atelier:mode', { detail: v }));
  });
  const states = document.body.dataset.states;
  if (states) {
    const list = states.split(',');
    const cur = document.body.dataset.state || list[0];
    group(document.body.dataset.statesLabel || 'View', list, cur, v => document.dispatchEvent(new CustomEvent('atelier:state', { detail: v })));
  }
  if (!document.body.hasAttribute('data-no-review-bar')) document.body.appendChild(bar);

  // Left rail and menu drawer (every page but Workroom screens, which keep their own header)
  if (document.body.dataset.archetype !== 'workroom' && !document.body.hasAttribute('data-no-rail')) {
    const here = location.pathname.split('/').pop() || 'index.html';
    const links = [['courses.html','Courses'],['about.html','About'],['sitemap.html#notes','Studio notes'],['index.html#faq','Questions'],['contact.html','Contact']];
    const ico = { Instagram:'<rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17" cy="7" r=".6"/>',
      Pinterest:'<circle cx="12" cy="12" r="8.5"/><path d="M11 8.5c3-1 5.2 1 4.2 3.6s-3.6 2.6-4.6 1M11.2 9 9 19.5"/>',
      YouTube:'<rect x="3" y="6" width="18" height="12" rx="3.5"/><path d="M10.5 9.5l4 2.5-4 2.5z"/>' };
    const rail = document.createElement('aside');
    rail.className = 'rail';
    rail.innerHTML = '<button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="siteDrawer"><span></span></button>' +
      '<span class="vt" aria-hidden="true">Elena Varga — school of drawing — Lisbon</span>' +
      '<div class="soc">' + Object.entries(ico).map(([n, d]) => `<a href="#" aria-label="${n}"><svg viewBox="0 0 24 24">${d}</svg></a>`).join('') + '</div>';
    const scrim = document.createElement('div'); scrim.className = 'menu-scrim';
    const drawer = document.createElement('div');
    drawer.className = 'menu-drawer'; drawer.id = 'siteDrawer';
    drawer.setAttribute('role', 'dialog'); drawer.setAttribute('aria-modal', 'true'); drawer.setAttribute('aria-label', 'Menu');
    drawer.innerHTML = '<p class="chapter"><b>00</b>Menu</p><nav aria-label="Menu">' +
      links.map(([h, t], i) => `<a href="${h}"${h.split('#')[0] === here && !h.includes('#') ? ' aria-current="page"' : ''}><small>0${i + 1}</small>${t}</a>`).join('') + '</nav>' +
      '<div class="menu-foot"><a class="btn btn-paper" href="lesson.html">Watch lesson 1 free <span class="ar" aria-hidden="true">→</span></a>' +
      '<address>Rua da Graça 4, 3º · 1170-165 Lisboa<br>Letters read on Tuesday and Friday mornings</address></div>';
    document.body.prepend(rail); document.body.append(scrim, drawer); document.body.classList.add('has-rail');
    const burger = rail.querySelector('.burger');
    const setMenu = open => {
      document.body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open); burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (open) drawer.querySelector('nav a').focus(); else burger.focus();
    };
    burger.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
    scrim.addEventListener('click', () => setMenu(false));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && document.body.classList.contains('menu-open')) setMenu(false); });
  }

  // Reveal on scroll and the footer circle
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12 }) : null;
  document.querySelectorAll('.reveal,.draw').forEach(el => io ? io.observe(el) : el.classList.add('is-in'));
  const foot = document.querySelector('.site-foot');
  if (foot && io) new IntersectionObserver(([e]) => foot.classList.toggle('ring-on', e.isIntersecting), { threshold: .3 }).observe(foot);

  // Small helpers for pages
  window.Atelier = {
    store,
    // Inline field validation: fields are .field elements with an input and a .err message.
    validate(form) {
      let first = null;
      form.querySelectorAll('.field').forEach(f => {
        const input = f.querySelector('input,select,textarea'); if (!input) return;
        const ok = input.checkValidity();
        f.toggleAttribute('data-invalid', !ok); input.setAttribute('aria-invalid', !ok);
        if (!ok && !first) first = input;
      });
      if (first) first.focus();
      return !first;
    }
  };
})();
