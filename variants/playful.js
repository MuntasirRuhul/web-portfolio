// Playful: draggable stickers, physics pills, tilt cards, card deck,
// chat FAQ, magnetic button with confetti and a custom cursor.
(() => {
    const colors = ['#325baa', '#fff847', '#f947ff', '#46f4fc', '#fa580d'];

    // custom cursor
    if (matchMedia('(hover: hover)').matches) {
        const ring = document.createElement('div');
        const dot = document.createElement('div');
        ring.className = 'v2-cursor';
        dot.className = 'v2-cursor-dot';
        document.body.append(ring, dot);
        let rx = 0, ry = 0, mx = 0, my = 0;
        addEventListener('pointermove', (e) => {
            mx = e.clientX; my = e.clientY;
            ring.classList.add('is-ready'); dot.classList.add('is-ready');
            dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%, -50%)`;
            const hot = e.target.closest('a, button, .v2-sticker, .v2-pill, .v2-deck, .v2-flip');
            ring.classList.toggle('is-hover', !!hot);
            ring.textContent = e.target.closest('.v2-pill, .v2-sticker') ? 'drag' : '';
        });
        const follow = () => {
            rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
            ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%, -50%)`;
            requestAnimationFrame(follow);
        };
        follow();
    }

    // draggable stickers
    document.querySelectorAll('.v2-sticker').forEach((el) => {
        el.addEventListener('pointerdown', (e) => {
            el.setPointerCapture(e.pointerId);
            el.classList.add('is-dragging');
            const box = el.parentElement.getBoundingClientRect();
            const r = el.getBoundingClientRect();
            const ox = e.clientX - r.left, oy = e.clientY - r.top;
            const move = (ev) => {
                el.style.left = ((ev.clientX - box.left - ox) / box.width * 100) + '%';
                el.style.top = ((ev.clientY - box.top - oy) / box.height * 100) + '%';
            };
            const up = () => {
                el.classList.remove('is-dragging');
                el.removeEventListener('pointermove', move);
                el.removeEventListener('pointerup', up);
            };
            el.addEventListener('pointermove', move);
            el.addEventListener('pointerup', up);
        });
    });

    // physics pills: gravity, walls, box collisions, grab and throw
    const field = document.querySelector('.v2-playground');
    const pills = [...field.querySelectorAll('.v2-pill')].map((el) => ({
        el, x: 0, y: 0, vx: 0, vy: 0, w: el.offsetWidth, h: el.offsetHeight, held: false,
    }));
    let W = field.clientWidth, H = field.clientHeight;
    const drop = () => {
        W = field.clientWidth; H = field.clientHeight;
        pills.forEach((p, i) => {
            p.w = p.el.offsetWidth; p.h = p.el.offsetHeight;
            p.x = Math.random() * (W - p.w);
            p.y = -p.h - i * 70;
            p.vx = (Math.random() - 0.5) * 4; p.vy = 0;
        });
    };
    let running = false;
    const step = () => {
        for (const p of pills) {
            if (p.held) continue;
            p.vy += 0.6;
            p.vx *= 0.99; p.vy *= 0.995;
            p.x += p.vx; p.y += p.vy;
            if (p.y + p.h > H) { p.y = H - p.h; p.vy *= -0.35; p.vx *= 0.9; }
            if (p.x < 0) { p.x = 0; p.vx *= -0.6; }
            if (p.x + p.w > W) { p.x = W - p.w; p.vx *= -0.6; }
        }
        for (let k = 0; k < 3; k++) {
            for (let i = 0; i < pills.length; i++) {
                for (let j = i + 1; j < pills.length; j++) {
                    const a = pills[i], b = pills[j];
                    const dx = (a.x + a.w / 2) - (b.x + b.w / 2);
                    const dy = (a.y + a.h / 2) - (b.y + b.h / 2);
                    const ox = (a.w + b.w) / 2 - Math.abs(dx);
                    const oy = (a.h + b.h) / 2 - Math.abs(dy);
                    if (ox <= 0 || oy <= 0) continue;
                    const wa = a.held ? 0 : b.held ? 1 : 0.5, wb = 1 - wa;
                    if (ox < oy) {
                        const s = Math.sign(dx) || 1;
                        a.x += s * ox * wa; b.x -= s * ox * wb;
                        const v = (a.vx + b.vx) / 2; a.vx = b.vx = v;
                    } else {
                        const s = Math.sign(dy) || 1;
                        a.y += s * oy * wa; b.y -= s * oy * wb;
                        if (!a.held) a.vy *= 0.2;
                        if (!b.held) b.vy *= 0.2;
                    }
                }
            }
        }
        for (const p of pills) p.el.style.transform = `translate(${p.x}px, ${p.y}px)`;
        if (running) requestAnimationFrame(step);
    };
    pills.forEach((p) => {
        p.el.addEventListener('pointerdown', (e) => {
            p.el.setPointerCapture(e.pointerId);
            p.held = true; p.el.classList.add('is-dragging');
            const box = field.getBoundingClientRect();
            const ox = e.clientX - box.left - p.x, oy = e.clientY - box.top - p.y;
            let lx = e.clientX, ly = e.clientY;
            const move = (ev) => {
                p.x = Math.max(0, Math.min(W - p.w, ev.clientX - box.left - ox));
                p.y = Math.max(0, Math.min(H - p.h, ev.clientY - box.top - oy));
                p.vx = ev.clientX - lx; p.vy = ev.clientY - ly;
                lx = ev.clientX; ly = ev.clientY;
            };
            const up = () => {
                p.held = false; p.el.classList.remove('is-dragging');
                p.el.removeEventListener('pointermove', move);
                p.el.removeEventListener('pointerup', up);
            };
            p.el.addEventListener('pointermove', move);
            p.el.addEventListener('pointerup', up);
        });
    });
    document.querySelector('.v2-shake').addEventListener('click', () => {
        pills.forEach((p) => { p.vy = -14 - Math.random() * 10; p.vx = (Math.random() - 0.5) * 24; });
    });
    addEventListener('resize', () => { W = field.clientWidth; H = field.clientHeight; });
    const startPhysics = () => {
        if (running) return;
        running = true;
        drop();
        if (reduceMotion) {
            for (let i = 0; i < 400; i++) { running = false; step(); }
            running = false;
            step();
            return;
        }
        step();
    };
    new IntersectionObserver((entries, io) => {
        if (entries[0].isIntersecting) { startPhysics(); io.disconnect(); }
    }, { threshold: 0.3 }).observe(field);

    // tilt cards
    document.querySelectorAll('.v2-card').forEach((card) => {
        card.addEventListener('pointermove', (e) => {
            const r = card.getBoundingClientRect();
            const px = (e.clientX - r.left) / r.width - 0.5;
            const py = (e.clientY - r.top) / r.height - 0.5;
            card.style.transform = `rotateY(${px * 18}deg) rotateX(${-py * 18}deg) translateY(-6px)`;
        });
        card.addEventListener('pointerleave', () => { card.style.transform = ''; });
    });

    // testimonial deck
    const deck = document.querySelector('.v2-deck');
    let order = [...deck.querySelectorAll('.v2-deck-card')];
    const layout = () => order.forEach((c, i) => {
        c.style.zIndex = String(order.length - i);
        c.style.transform = `translate(${i * 14}px, ${i * 14}px) rotate(${i * 2.5}deg)`;
    });
    const next = () => {
        const top = order[0];
        top.classList.add('is-flying');
        setTimeout(() => {
            top.classList.remove('is-flying');
            order = [...order.slice(1), top];
            layout();
        }, 450);
    };
    layout();
    deck.addEventListener('click', next);
    deck.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); next(); } });

    // chat faq
    const log = document.querySelector('.v2-chat-log');
    const msg = (text, who) => {
        const el = document.createElement('div');
        el.className = 'v2-msg v2-msg-' + who;
        el.innerHTML = (who === 'them' ? '<span class="avatar avatar-sm avatar-orange"></span>' : '') + '<p></p>';
        el.querySelector('p').textContent = text;
        log.append(el);
        return el;
    };
    document.querySelectorAll('.v2-reply').forEach((btn) => {
        btn.addEventListener('click', () => {
            btn.disabled = true;
            msg(btn.textContent, 'me');
            const typing = msg('', 'them');
            typing.classList.add('v2-typing');
            typing.querySelector('p').innerHTML = '<i></i><i></i><i></i>';
            setTimeout(() => { typing.remove(); msg(btn.dataset.a, 'them'); }, reduceMotion ? 0 : 900);
        });
    });

    // magnetic button + confetti
    const big = document.querySelector('.v2-big-btn');
    const contact = document.querySelector('.v2-contact');
    contact.addEventListener('pointermove', (e) => {
        if (reduceMotion) return;
        const r = big.getBoundingClientRect();
        const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
        const d = Math.hypot(dx, dy);
        const pull = d < 320 ? (1 - d / 320) * 0.35 : 0;
        big.style.transform = `translate(${dx * pull}px, ${dy * pull}px)`;
    });
    contact.addEventListener('pointerleave', () => { big.style.transform = ''; });
    big.addEventListener('click', (e) => {
        if (reduceMotion) return;
        for (let i = 0; i < 70; i++) {
            const c = document.createElement('i');
            c.className = 'v2-confetti';
            c.style.background = colors[i % colors.length];
            c.style.left = e.clientX + 'px';
            c.style.top = e.clientY + 'px';
            document.body.append(c);
            const a = Math.random() * Math.PI * 2, v = 200 + Math.random() * 400;
            c.animate([
                { transform: 'translate(0,0) rotate(0deg)', opacity: 1 },
                { transform: `translate(${Math.cos(a) * v}px, ${Math.sin(a) * v + 300}px) rotate(${Math.random() * 720}deg)`, opacity: 0 },
            ], { duration: 1200 + Math.random() * 600, easing: 'cubic-bezier(.2,.6,.4,1)' }).onfinish = () => c.remove();
        }
    });
})();
