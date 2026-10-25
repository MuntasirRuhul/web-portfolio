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
