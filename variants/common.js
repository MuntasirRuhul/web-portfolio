// Shared behaviour for the design-direction pages: menu, scroll progress,
// reveal on scroll and count-up numbers.
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

(() => {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.getElementById('site-nav');
    toggle.addEventListener('click', () => {
        const open = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!open));
        toggle.setAttribute('aria-label', open ? 'Open menu' : 'Close menu');
        nav.classList.toggle('is-open', !open);
    });
    nav.addEventListener('click', (e) => {
        if (e.target.tagName === 'A') toggle.click();
    });

    const bar = document.querySelector('.scroll-progress');
    const onScroll = () => {
        const max = document.documentElement.scrollHeight - innerHeight;
        bar.style.transform = 'scaleX(' + Math.min(scrollY / max, 1) + ')';
    };
    addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    const countUp = (el) => {
        const target = Number(el.dataset.count);
        const suffix = el.dataset.suffix || '';
        const start = performance.now();
        const tick = (now) => {
            const t = Math.min((now - start) / 1400, 1);
            el.textContent = Math.round(target * (1 - Math.pow(1 - t, 3))) + suffix;
            if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
    };

    const targets = document.querySelectorAll('[data-reveal]');
    if (reduceMotion || !('IntersectionObserver' in window)) return;
    targets.forEach((el) => el.classList.add('reveal'));
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('is-visible');
            entry.target.querySelectorAll('[data-count]').forEach(countUp);
            io.unobserve(entry.target);
        });
    }, { threshold: 0.15 });
    targets.forEach((el) => io.observe(el));
})();
