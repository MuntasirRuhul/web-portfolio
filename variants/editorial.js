// Editorial: statement lines drift with scroll, a card follows the cursor
// over the services index, and vertical scroll drives the process track.
(() => {
    const lines = [...document.querySelectorAll('.v3-line')];
    const statement = document.querySelector('.v3-statement');
    const proc = document.querySelector('.v3-process');
    const track = document.querySelector('.v3-track');

    const onScroll = () => {
        if (reduceMotion) return;
        const s = statement.getBoundingClientRect();
        const p = (innerHeight - s.top) / (innerHeight + s.height);
        lines.forEach((el) => {
            el.style.transform = `translateX(${(p - 0.5) * Number(el.dataset.shift) * 100}%)`;
        });

        const r = proc.getBoundingClientRect();
        const t = Math.min(Math.max(-r.top / (r.height - innerHeight), 0), 1);
        const max = track.scrollWidth - track.parentElement.clientWidth + 160;
        track.style.transform = `translateX(${-t * Math.max(max, 0)}px)`;
    };
    addEventListener('scroll', onScroll, { passive: true });
    addEventListener('resize', onScroll);
    onScroll();

    // fall back to a swipeable row when motion is reduced
    if (reduceMotion) {
        proc.style.height = 'auto';
        track.parentElement.style.position = 'static';
        track.parentElement.style.height = 'auto';
        track.parentElement.style.padding = '120px var(--gutter)';
        track.parentElement.style.overflowX = 'auto';
    }

    const follow = document.querySelector('.v3-follow');
    const text = follow.querySelector('.v3-follow-text');
    document.querySelectorAll('.v3-index-row').forEach((row) => {
        row.addEventListener('pointerenter', () => {
            text.textContent = row.dataset.line;
            follow.style.background = getComputedStyle(row).getPropertyValue('--bg');
            follow.style.color = getComputedStyle(row).getPropertyValue('--fg');
            follow.classList.add('is-on');
        });
        row.addEventListener('pointerleave', () => follow.classList.remove('is-on'));
        row.addEventListener('pointermove', (e) => {
            follow.style.left = (e.clientX + 24) + 'px';
            follow.style.top = (e.clientY - 100) + 'px';
        });
    });
})();
