(function () {
  document.documentElement.classList.add('js-anim');

  // Mobile navigation
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', open);
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });

  // Duplicate the logo row so the marquee loops seamlessly
  var row = document.querySelector('.logos__row');
  if (row) {
    Array.prototype.slice.call(row.children).forEach(function (tile) {
      var clone = tile.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      row.appendChild(clone);
    });
  }

  // Hero geometry: turn one tile at a time, gently
  var tiles = document.querySelectorAll('.geo__tile');
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (tiles.length && !calm) {
    var last = -1;
    setInterval(function () {
      var i;
      do { i = Math.floor(Math.random() * tiles.length); } while (i === last && tiles.length > 1);
      last = i;
      tiles[i].classList.toggle('is-turning');
    }, 2600);
  }

  // Course filter tabs
  var tabs = document.querySelectorAll('.tab');
  var courses = document.querySelectorAll('.course');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (t) {
        t.classList.toggle('is-active', t === tab);
        t.setAttribute('aria-selected', t === tab);
      });
      var filter = tab.dataset.filter;
      courses.forEach(function (c) {
        c.classList.toggle('is-hidden', filter !== 'all' && c.dataset.cat !== filter);
      });
    });
  });

  // Pricing billing toggle
  var toggles = document.querySelectorAll('.toggle__btn');
  toggles.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var period = btn.dataset.billing;
      toggles.forEach(function (b) { b.classList.toggle('is-active', b === btn); });
      document.querySelectorAll('[data-monthly]').forEach(function (el) {
        el.textContent = el.dataset[period];
      });
    });
  });

  // Active nav link on scroll + reveal animations
  var links = document.querySelectorAll('.nav > a');
  if ('IntersectionObserver' in window) {
    var revealer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          revealer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { revealer.observe(el); });

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    links.forEach(function (a) {
      var section = document.querySelector(a.getAttribute('href'));
      if (section) spy.observe(section);
    });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }
})();
