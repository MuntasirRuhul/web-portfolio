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
    const ico = {"Pinterest": "<svg viewBox=\"5 14 34 27\" aria-hidden=\"true\"><path class=\"well\" d=\"M37.9959 28.6302C38.3345 16.2152 17.5616 11.4739 8.22563 21.194C6.4917 22.9992 5.20188 25.7656 6.58056 27.7386C8.63689 30.6812 12.7201 27.2588 13.9053 28.6302C15.1147 30.3144 9.1162 34.3806 13.5909 37.9415C19.3408 42.5172 37.6573 41.0452 37.9959 28.6302Z\" style=\"fill:var(--pot-1)\"/><path class=\"glyph\" d=\"M32 27.385C32 29.023 31.4143 30.5243 30.3503 31.6106C29.352 32.6302 27.9961 33.2153 26.6304 33.2153C25.5389 33.2153 24.7384 32.9252 24.1654 32.5691L23.4991 35.3497C23.4746 35.4571 23.4286 35.5587 23.3638 35.6485C23.299 35.7383 23.2168 35.8147 23.1218 35.8731C23.0268 35.9315 22.9209 35.9708 22.8104 35.9888C22.6998 36.0068 22.5867 36.0031 22.4776 35.9778C22.3685 35.9526 22.2656 35.9064 22.1748 35.8418C22.0841 35.7773 22.0072 35.6957 21.9487 35.6018C21.8902 35.5078 21.8513 35.4035 21.8341 35.2947C21.8169 35.1859 21.8219 35.0748 21.8487 34.9679L24.1096 25.5283C24.1341 25.4208 24.1801 25.3193 24.2449 25.2294C24.3097 25.1396 24.3919 25.0633 24.4869 25.0048C24.5819 24.9464 24.6878 24.9071 24.7983 24.8891C24.9089 24.8711 25.022 24.8749 25.1311 24.9001C25.2402 24.9253 25.3431 24.9716 25.4339 25.0361C25.5246 25.1007 25.6015 25.1823 25.66 25.2762C25.7185 25.3701 25.7574 25.4745 25.7746 25.5833C25.7918 25.6921 25.7868 25.8031 25.76 25.91L24.5978 30.7638C24.8443 31.0539 25.4407 31.5495 26.6304 31.5495C28.4363 31.5495 30.3043 29.9913 30.3043 27.385C30.304 26.6612 30.1342 25.9473 29.8081 25.2983C29.482 24.6493 29.0084 24.0827 28.4238 23.6422C27.8392 23.2018 27.1594 22.8993 26.4368 22.7582C25.7143 22.6171 24.9683 22.6411 24.2567 22.8284C23.5451 23.0156 22.8869 23.3612 22.3329 23.8383C21.779 24.3154 21.3441 24.9113 21.0619 25.5798C20.7798 26.2484 20.658 26.9717 20.7058 27.6939C20.7536 28.4162 20.9699 29.1179 21.3379 29.7449C21.4417 29.9355 21.4661 30.1583 21.4057 30.3663C21.3454 30.5742 21.2051 30.7509 21.0145 30.8591C20.824 30.9673 20.598 30.9984 20.3845 30.9459C20.171 30.8934 19.9867 30.7614 19.8704 30.5778C19.3721 29.7295 19.079 28.78 19.0139 27.8027C18.9488 26.8254 19.1134 25.8464 19.4949 24.9416C19.8765 24.0367 20.4649 23.2303 21.2144 22.5845C21.964 21.9388 22.8547 21.4711 23.8177 21.2176C24.7807 20.9641 25.7902 20.9316 26.768 21.1227C27.7458 21.3137 28.6657 21.7232 29.4567 22.3194C30.2477 22.9156 30.8884 23.6825 31.3294 24.5609C31.7705 25.4393 31.9999 26.4055 32 27.385Z\"/></svg>", "Instagram": "<svg viewBox=\"5 45 34 27\" aria-hidden=\"true\"><path class=\"well\" d=\"M6.00409 59.6302C5.66547 47.2152 26.4384 42.4739 35.7744 52.194C37.5083 53.9992 38.7981 56.7656 37.4194 58.7386C35.3631 61.6812 31.2799 58.2588 30.0947 59.6302C28.8853 61.3144 34.8838 65.3806 30.4091 68.9415C24.6592 73.5172 6.34271 72.0452 6.00409 59.6302Z\" style=\"fill:var(--pot-2)\"/><path class=\"glyph\" d=\"M19.5 56.6111C18.9286 56.6111 18.3701 56.7805 17.895 57.098C17.4199 57.4154 17.0497 57.8666 16.831 58.3945C16.6124 58.9223 16.5552 59.5032 16.6666 60.0636C16.7781 60.624 17.0532 61.1387 17.4572 61.5428C17.8613 61.9468 18.376 62.2219 18.9364 62.3334C19.4968 62.4448 20.0777 62.3876 20.6055 62.169C21.1334 61.9503 21.5846 61.5801 21.902 61.105C22.2195 60.6299 22.3889 60.0714 22.3889 59.5C22.3881 58.7341 22.0835 57.9997 21.5419 57.4581C21.0003 56.9165 20.2659 56.6119 19.5 56.6111ZM19.5 60.9444C19.2143 60.9444 18.935 60.8597 18.6975 60.701C18.46 60.5423 18.2748 60.3167 18.1655 60.0528C18.0562 59.7888 18.0276 59.4984 18.0833 59.2182C18.139 58.938 18.2766 58.6806 18.4786 58.4786C18.6806 58.2766 18.938 58.139 19.2182 58.0833C19.4984 58.0276 19.7888 58.0562 20.0528 58.1655C20.3167 58.2748 20.5423 58.46 20.701 58.6975C20.8597 58.935 20.9444 59.2143 20.9444 59.5C20.9444 59.8831 20.7923 60.2505 20.5214 60.5214C20.2505 60.7923 19.8831 60.9444 19.5 60.9444ZM22.3889 53H16.6111C15.6537 53.0011 14.7359 53.3819 14.0589 54.0589C13.3819 54.7359 13.0011 55.6537 13 56.6111V62.3889C13.0011 63.3463 13.3819 64.2641 14.0589 64.9411C14.7359 65.6181 15.6537 65.9989 16.6111 66H22.3889C23.3463 65.9989 24.2641 65.6181 24.9411 64.9411C25.6181 64.2641 25.9989 63.3463 26 62.3889V56.6111C25.9989 55.6537 25.6181 54.7359 24.9411 54.0589C24.2641 53.3819 23.3463 53.0011 22.3889 53ZM24.5556 62.3889C24.5556 62.9635 24.3273 63.5146 23.921 63.921C23.5146 64.3273 22.9635 64.5556 22.3889 64.5556H16.6111C16.0365 64.5556 15.4854 64.3273 15.079 63.921C14.6727 63.5146 14.4444 62.9635 14.4444 62.3889V56.6111C14.4444 56.0365 14.6727 55.4854 15.079 55.079C15.4854 54.6727 16.0365 54.4444 16.6111 54.4444H22.3889C22.9635 54.4444 23.5146 54.6727 23.921 55.079C24.3273 55.4854 24.5556 56.0365 24.5556 56.6111V62.3889ZM23.5926 56.3704C23.5926 56.5608 23.5361 56.747 23.4303 56.9054C23.3245 57.0637 23.1741 57.1871 22.9981 57.26C22.8222 57.3329 22.6286 57.352 22.4418 57.3148C22.255 57.2777 22.0834 57.186 21.9487 57.0513C21.814 56.9166 21.7223 56.745 21.6852 56.5582C21.648 56.3714 21.6671 56.1778 21.74 56.0019C21.8129 55.8259 21.9363 55.6755 22.0946 55.5697C22.253 55.4639 22.4392 55.4074 22.6296 55.4074C22.885 55.4074 23.13 55.5089 23.3105 55.6895C23.4911 55.87 23.5926 56.115 23.5926 56.3704Z\"/></svg>", "YouTube": "<svg viewBox=\"5 76 34 27\" aria-hidden=\"true\"><path class=\"well\" d=\"M37.9959 90.6302C38.3345 78.2152 17.5616 73.4739 8.22563 83.194C6.4917 84.9992 5.20188 87.7656 6.58056 89.7386C8.63689 92.6812 12.7201 89.2588 13.9053 90.6302C15.1147 92.3144 9.1162 96.3806 13.5909 99.9415C19.3408 104.517 37.6573 103.045 37.9959 90.6302Z\" style=\"fill:var(--pot-3)\"/><path class=\"glyph\" d=\"M26.8809 89.8968L23.743 87.7446C23.6414 87.6749 23.5241 87.6357 23.4035 87.6311C23.2828 87.6265 23.1632 87.6566 23.0572 87.7183C22.9512 87.78 22.8628 87.871 22.8011 87.9818C22.7395 88.0926 22.7069 88.219 22.7069 88.3478V92.6522C22.7069 92.781 22.7395 92.9074 22.8011 93.0182C22.8628 93.129 22.9512 93.22 23.0572 93.2817C23.1632 93.3434 23.2828 93.3735 23.4035 93.3689C23.5241 93.3643 23.6414 93.3251 23.743 93.2554L26.8809 91.1032C26.9755 91.0382 27.0533 90.949 27.1072 90.8436C27.1611 90.7382 27.1893 90.62 27.1893 90.5C27.1893 90.38 27.1611 90.2618 27.1072 90.1564C27.0533 90.051 26.9755 89.9618 26.8809 89.8968ZM24.0517 91.337V89.663L25.2738 90.5L24.0517 91.337ZM30.6756 86.9429C30.6137 86.6857 30.4954 86.4478 30.3305 86.2489C30.1655 86.0499 29.9587 85.8956 29.7269 85.7987C27.7724 84.9946 24.6844 85 24.5 85C24.3156 85 21.2276 84.9946 19.2731 85.7999C19.0413 85.8968 18.8345 86.0511 18.6696 86.2501C18.5046 86.449 18.3863 86.6869 18.3244 86.9441C18.1765 87.5539 18 88.6659 18 90.5C18 92.3341 18.1765 93.4461 18.3244 94.0559C18.3863 94.3131 18.5046 94.551 18.6696 94.7499C18.8345 94.9489 19.0413 95.1032 19.2731 95.2001C21.1497 95.9731 24.0719 96 24.4647 96H24.5353C24.9275 96 27.8503 95.9731 29.7269 95.2001C29.9587 95.1032 30.1655 94.9489 30.3305 94.7499C30.4954 94.551 30.6137 94.3131 30.6756 94.0559C30.8235 93.4461 31 92.3341 31 90.5C31 88.6659 30.8235 87.5539 30.6756 86.9441V86.9429ZM29.375 93.696C29.3669 93.7326 29.3508 93.7668 29.328 93.7955C29.3053 93.8243 29.2764 93.8469 29.2439 93.8616C27.5696 94.5509 24.7393 94.5652 24.5179 94.5652H24.4961C24.4664 94.5652 21.4904 94.5754 19.7578 93.8616C19.725 93.8472 19.6958 93.8246 19.6727 93.7959C19.6496 93.7671 19.6333 93.7328 19.625 93.696C19.5197 93.2632 19.3448 92.272 19.3448 90.5C19.3448 88.728 19.5213 87.7368 19.625 87.304C19.6331 87.2674 19.6492 87.2332 19.672 87.2045C19.6947 87.1757 19.7236 87.1531 19.7561 87.1384C21.4904 86.4246 24.4658 86.4348 24.4955 86.4348H24.5039C24.5342 86.4348 27.5096 86.4246 29.2422 87.1384C29.275 87.1528 29.3042 87.1754 29.3273 87.2041C29.3504 87.2329 29.3667 87.2672 29.375 87.304C29.4803 87.7368 29.6552 88.728 29.6552 90.5C29.6552 92.272 29.4787 93.2632 29.375 93.696Z\"/></svg>"};   // palette-shaped wells (Figma "icon" 72:727)
    const rail = document.createElement('aside');
    rail.className = 'rail';
    rail.innerHTML = '<button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="siteDrawer"><span></span></button>' +
      '<span class="vt" aria-hidden="true">Elena Varga — school of drawing — Lisbon</span>' +
      '<div class="soc">' + Object.entries(ico).map(([n, svg]) => `<a href="#" aria-label="${n}">${svg}</a>`).join('') + '</div>';
    const scrim = document.createElement('div'); scrim.className = 'menu-scrim';
    const drawer = document.createElement('div');
    drawer.className = 'menu-drawer'; drawer.id = 'siteDrawer';
    drawer.setAttribute('role', 'dialog'); drawer.setAttribute('aria-modal', 'true'); drawer.setAttribute('aria-label', 'Menu');
    drawer.innerHTML = '<p class="chapter"><b>00</b>Menu</p><nav aria-label="Menu">' +
      links.map(([h, t], i) => `<a href="${h}"${h.split('#')[0] === here && !h.includes('#') ? ' aria-current="page"' : ''}><small>0${i + 1}</small>${t}</a>`).join('') + '</nav>' +
      '<div class="menu-foot"><a class="btn btn-paper" href="lesson.html">Watch lesson 1 free <span class="ar" aria-hidden="true">→</span></a>' +
      '<address>Rua da Graça 4, 3º · 1170-165 Lisboa<br>Letters read on Tuesday and Friday mornings</address></div>';
    // the page body goes into its own panel, beside the side-nav panel
    const frame = document.createElement('div'); frame.className = 'frame';
    [...document.body.children].filter(n => n.tagName !== 'SCRIPT' && !n.classList.contains('review-bar')).forEach(n => frame.appendChild(n));
    document.body.prepend(frame);
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
