  // Contents list: mark the section being read. The frame scrolls on desktop, the page on phones.
  const links = [...document.querySelectorAll('.lg-toc a[href^="#"]')], secs = links.map(a => document.querySelector(a.getAttribute('href')));
  const root = matchMedia('(max-width: 980px)').matches ? null : document.querySelector('.frame');
  const spy = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) links.forEach(a => a.getAttribute('href') === '#' + e.target.id ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current')); }), { root, rootMargin: '-20% 0px -70% 0px' });
  secs.forEach(s => s && spy.observe(s));
