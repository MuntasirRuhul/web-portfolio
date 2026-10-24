// Art-direction audit (openspec change: atelier-art-direction, spec design-review).
// Opens each page at 1440px and 390px and checks it against the design language.
//
//   node atelier/tools/audit.mjs [page.html ...] [--strict-links] [--json]
//
// With no pages it audits every *.html in atelier/ that declares data-archetype.
// BLOCK items fail the run (exit 1); WARN items are reported only.
// --strict-links makes `href="#"` in primary navigation blocking (used once the
// full page set exists, see atelier-site-pages).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readdirSync, readFileSync } from 'node:fs';
import { resolve, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const strictLinks = args.includes('--strict-links');
const asJson = args.includes('--json');
let pages = args.filter(a => !a.startsWith('--'));
if (!pages.length) pages = readdirSync(ROOT).filter(f => f.endsWith('.html') && /data-archetype=/.test(readFileSync(resolve(ROOT, f), 'utf8')));

// Which archetype each page must declare (spec page-archetypes).
const ARCHETYPE = {
  'atelier-v7.html': 'gallery', 'style.html': 'gallery', 'about.html': 'gallery', 'teachers.html': 'gallery',
  'services.html': 'gallery', 'courses.html': 'gallery', 'notes.html': 'gallery',
  'course.html': 'reading', 'note.html': 'reading',
  'lesson.html': 'workroom', 'quiz.html': 'workroom', 'assignment.html': 'workroom', 'dashboard.html': 'workroom',
  'account.html': 'counter', 'checkout.html': 'counter', 'contact.html': 'counter',
};

// Allow-list: selector -> reason. Matched with element.matches().
const ALLOW_SHADOW = {
  '.soc a': 'paint pots: inset rim is part of the drawn object (design-language: Spacing, radii and rules)',
};
const ALLOW_RADIUS = {
  '.soc a': 'paint-pot blobs are irregular by design',
  '.meter i, .prog i, .prog i::before, .rhythm i, .bars i, .prog-h i, .prog-h s, .cont .pg i, .cont .pg s, .scrub::before, .scrub .fill, .step li, [class*="bar"] i': 'thin progress bars keep 2–3px round ends',
};

// Scale (spec design-language: Typography scale). clamp() steps resolved per viewport.
const clamp = (min, vw, max, w) => Math.min(max, Math.max(min, vw * w / 100));
const scale = w => [clamp(40, 5, 68, w), clamp(30, 3.5, 48, w), clamp(22, 2, 28, w), 18, 16, 14, 10.5];
// Component titles measured on the home page: block title (v7:198) and FAQ question (v7:353).
const componentSteps = w => [clamp(24, 2.2, 30, w), clamp(20, 2, 25, w)];
// Documented component exceptions (reported as WARN if outside both lists).
const EXCEPTIONS = [9, 9.5, 10, 11, 12, 12.5, 13, 13.5, 14.5, 15, 15.5, 17, 20, 36];

const RADII_OK = [0, 12, 16, 22, 28];

function report(rows) { return rows; }

const browser = await chromium.launch();
const out = [];
let blocking = 0;

for (const page of pages) {
  for (const width of [1440, 390]) {
    const p = await browser.newPage({ viewport: { width, height: 900 } });
    const errors = [];
    p.on('pageerror', e => errors.push(e.message));
    const [file, hash] = page.split('#');
    await p.goto('file://' + resolve(ROOT, file) + (hash ? '#' + hash : ''));
    await p.waitForTimeout(400);
    // show every reveal so hidden-until-scrolled content is audited too
    await p.addStyleTag({ content: '*,*::before,*::after{transition:none!important;animation:none!important}' });
    await p.evaluate(() => document.querySelectorAll('.reveal,.draw').forEach(e => e.classList.add('is-in')));
    await p.waitForTimeout(150);

    const r = await p.evaluate(({ ALLOW_SHADOW, ALLOW_RADIUS, scaleSteps, EXCEPTIONS, RADII_OK }) => {
      const res = { archetype: document.body.dataset.archetype || null, sw: document.documentElement.scrollWidth, vw: innerWidth,
        shadows: [], radii: [], quotes: [], italic: [], fonts: {}, contrast: [], alt: [], hashLinks: [] };
      const sel = e => { let s = e.tagName.toLowerCase(); if (e.id) s += '#' + e.id; if (e.classList.length) s += '.' + [...e.classList].slice(0, 3).join('.'); const pa = e.parentElement; return (pa && pa !== document.body ? (pa.classList[0] ? '.' + pa.classList[0] + ' > ' : pa.tagName.toLowerCase() + ' > ') : '') + s; };
      const visible = e => { const r = e.getBoundingClientRect(); if (!r.width || !r.height) return false; const cs = getComputedStyle(e); return cs.visibility !== 'hidden' && cs.display !== 'none'; };
      const allowed = (e, map) => Object.keys(map).some(k => { try { return e.matches(k); } catch { return false; } });
      const near = (v, list, tol = 0.6) => list.some(x => Math.abs(v - x) <= tol);

      // colour helpers
      const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: v[0], g: v[1], b: v[2], a: v[3] ?? 1 }; };
      const lum = ({ r, g, b }) => { const f = x => { x /= 255; return x <= .03928 ? x / 12.92 : ((x + .055) / 1.055) ** 2.4; }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
      const blend = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
      const bgOf = e => { let layers = []; for (let n = e; n; n = n.parentElement) { const cs = getComputedStyle(n); if (cs.backgroundImage !== 'none' && !/gradient/.test(cs.backgroundImage)) return null; const c = parse(cs.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } } let base = { r: 255, g: 255, b: 255, a: 1 }; for (const l of layers.reverse()) base = blend(l, base); return base; };
      const opacityOf = e => { let o = 1; for (let n = e; n; n = n.parentElement) o *= +getComputedStyle(n).opacity; return o; };
      const overImage = e => { for (let n = e.parentElement; n; n = n.parentElement) { if (n.querySelector(':scope > img, :scope > picture, :scope > video')) { const r = n.getBoundingClientRect(), er = e.getBoundingClientRect(); const img = n.querySelector(':scope > img'); if (img) { const ir = img.getBoundingClientRect(); if (er.left < ir.right && er.right > ir.left && er.top < ir.bottom && er.bottom > ir.top) return true; } } } return false; };

      for (const e of document.body.querySelectorAll('*')) {
        if (!visible(e) || e.closest('svg,[aria-hidden="true"],.review-bar,.dont')) continue;
        const cs = getComputedStyle(e);
        if (cs.boxShadow !== 'none' && !allowed(e, ALLOW_SHADOW)) res.shadows.push(sel(e) + ' → ' + cs.boxShadow.slice(0, 60));
        const rad = cs.borderTopLeftRadius;
        if (rad && rad !== '0px') {
          const r = e.getBoundingClientRect(), v = parseFloat(rad);
          const pill = rad.endsWith('%') || v >= Math.min(r.width, r.height) / 2 - 1;
          if (!pill && !near(v, RADII_OK, 0.5) && !allowed(e, ALLOW_RADIUS) && !(v <= 3 && r.height <= 8)) res.radii.push(sel(e) + ' → ' + rad);
        }
        const own = [...e.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent).join(' ').trim();
        if (!own) continue;
        if (e.closest('code,pre,script,style,textarea,input')) continue;
        if (/"/.test(own)) res.quotes.push(sel(e) + ' → ' + own.slice(0, 50));
        if (/[A-Za-z]'[A-Za-z]|'\s|\s'/.test(own)) res.quotes.push(sel(e) + ' → straight apostrophe: ' + own.slice(0, 50));
        if (/\s-\s/.test(own)) res.quotes.push(sel(e) + ' → separator " - ": ' + own.slice(0, 50));
        if (cs.fontStyle === 'italic' && !/Caveat/.test(cs.fontFamily)) res.italic.push(sel(e) + ' → ' + own.slice(0, 40));
        const fs = Math.round(parseFloat(cs.fontSize) * 10) / 10;
        const isMono = /Mono/.test(cs.fontFamily), isHand = /Caveat/.test(cs.fontFamily);
        if (!isHand && !near(fs, scaleSteps, 0.6)) { const k = fs + (near(fs, EXCEPTIONS, 0.3) ? ' (exception)' : ' (OFF-SCALE)'); res.fonts[k] = (res.fonts[k] || 0) + 1; }
        // contrast
        const fg = parse(cs.color); const bg = bgOf(e);
        if (fg && bg && !overImage(e)) {
          const f = blend({ ...fg, a: fg.a * opacityOf(e) }, bg);
          const L1 = lum(f), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
          const large = fs >= 24 || (fs >= 18.66 && +cs.fontWeight >= 700);
          const need = large ? 3 : 4.5;
          if (ratio < need - 0.05) res.contrast.push(`${sel(e)} → ${ratio.toFixed(2)}:1 (needs ${need}) "${own.slice(0, 30)}"`);
        }
      }
      for (const img of document.images) if (!img.hasAttribute('alt')) res.alt.push(img.src.slice(-50));
      // one footer for the whole site: the dark room footer (.site-foot), or the home page's original
      res.footer = [...document.querySelectorAll('footer')].filter(f => !f.classList.contains('site-foot') && !document.querySelector('.hero .hn')).map(f => sel(f) + ' is not the shared .site-foot');
      for (const a of document.querySelectorAll('header a[href="#"], nav a[href="#"], footer a[href="#"], .poster[href="#"], .pcard[href="#"], a.btn[href="#"], a.cta[href="#"]')) if (visible(a)) res.hashLinks.push(sel(a) + ' "' + a.textContent.trim().slice(0, 30) + '"');
      return res;
    }, { ALLOW_SHADOW, ALLOW_RADIUS, scaleSteps: [...scale(width), ...componentSteps(width)], EXCEPTIONS, RADII_OK });

    const expected = ARCHETYPE[basename(page.split('#')[0])];
    const items = [];
    const add = (level, name, list) => { if (list && list.length) items.push({ level, name, list }); };
    if (!r.archetype) add('BLOCK', 'missing data-archetype', ['<body> has no data-archetype']);
    else if (expected && r.archetype !== expected) add('BLOCK', 'wrong archetype', [`declares ${r.archetype}, expected ${expected}`]);
    if (r.sw > r.vw) add('BLOCK', 'horizontal overflow', [`scrollWidth ${r.sw} > ${r.vw}`]);
    add('BLOCK', 'page errors', errors);
    add('BLOCK', 'shadows', r.shadows);
    add('BLOCK', 'off-scale radii', r.radii);
    add('BLOCK', 'straight quotes / " - " separators', r.quotes);
    add('BLOCK', 'italic text', r.italic);
    add('BLOCK', 'contrast', r.contrast);
    add('BLOCK', 'images without alt', r.alt);
    add('BLOCK', 'footer is not the shared one', r.footer);
    add(strictLinks ? 'BLOCK' : 'WARN', 'href="#" in primary links', r.hashLinks);
    const off = Object.entries(r.fonts).filter(([k]) => k.includes('OFF-SCALE')).map(([k, n]) => `${k} ×${n}`);
    add('WARN', 'font sizes off the scale', off);
    const nb = items.filter(i => i.level === 'BLOCK').length;
    blocking += nb;
    out.push({ page, width, archetype: r.archetype, items });
    await p.close();
  }
}
await browser.close();

if (asJson) console.log(JSON.stringify(out, null, 2));
else {
  for (const o of out) {
    const nb = o.items.filter(i => i.level === 'BLOCK').length, nw = o.items.length - nb;
    console.log(`\n${nb ? '✗' : '✓'} ${o.page} @${o.width}  archetype=${o.archetype}  ${nb} blocking, ${nw} warnings`);
    for (const it of o.items) {
      console.log(`  ${it.level} ${it.name} (${it.list.length})`);
      for (const l of it.list.slice(0, 8)) console.log('     · ' + l);
      if (it.list.length > 8) console.log(`     · … ${it.list.length - 8} more`);
    }
  }
  console.log(`\n${blocking ? 'FAIL' : 'PASS'}: ${blocking} blocking item group(s) across ${out.length} page views.`);
}
process.exit(blocking ? 1 : 0);
