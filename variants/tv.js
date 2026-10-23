// TV network: the chapter in view tunes the pinned TV to its channel.
(() => {
    const chapters = [...document.querySelectorAll('.v1-chapter')];
    const screens = [...document.querySelectorAll('.v1-screen')];
    const osd = document.querySelector('.v1-osd-ch');
    const staticEl = document.querySelector('.v1-static');
    const knob = document.querySelector('.v1-knob');
    const groupBtns = [...document.querySelectorAll('.v1-remote-btn')];
    const starts = groupBtns.map((b) => Number(b.dataset.go));
    let current = -1;

    const tune = (i) => {
        if (i === current) return;
        current = i;
        chapters.forEach((el, n) => el.classList.toggle('is-active', n === i));
        screens.forEach((el, n) => el.classList.toggle('is-active', n === i));
        osd.textContent = 'CH ' + String(i + 1).padStart(2, '0');
        knob.style.transform = 'rotate(' + i * 32 + 'deg)';
        let group = 0;
        starts.forEach((s, g) => { if (i >= s) group = g; });
        groupBtns.forEach((b, g) => b.classList.toggle('is-active', g === group));
        if (!reduceMotion) {
            staticEl.classList.add('is-on');
            setTimeout(() => staticEl.classList.remove('is-on'), 220);
        }
    };

    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) tune(Number(entry.target.dataset.ch));
        });
    }, { rootMargin: '-45% 0px -45% 0px' });
    chapters.forEach((el) => io.observe(el));
    tune(0);

    const go = (i) => {
        const el = chapters[Math.max(0, Math.min(chapters.length - 1, i))];
        const y = el.getBoundingClientRect().top + scrollY - innerHeight / 2 + el.offsetHeight / 2;
        scrollTo({ top: y, behavior: reduceMotion ? 'auto' : 'smooth' });
    };
    groupBtns.forEach((b) => b.addEventListener('click', () => go(Number(b.dataset.go))));
    document.querySelectorAll('.v1-remote-step').forEach((b) =>
        b.addEventListener('click', () => go(current + Number(b.dataset.step))));
})();
