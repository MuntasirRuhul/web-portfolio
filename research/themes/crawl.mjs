// Crawl Tutor LMS theme demos and list their pages (run by .github/workflows/capture-themes.yml).
// For each theme: read its tutorlms.com page, find the live demo, then crawl the demo (same host)
// and record each page's URL, title and headings, with one screenshot per page template.
import { chromium } from 'playwright';
import { mkdirSync, writeFileSync } from 'node:fs';

const THEMES = [
  { id: 'pathwise', info: ['https://tutorlms.com/themes/pathwise/'], demos: ['https://pathwise.tutorlms.io/'] },
  { id: 'workademy', info: ['https://tutorlms.com/themes/workademy/'], demos: ['https://workademy.tutorlms.io/'] },
  { id: 'wellthrive', info: ['https://tutorlms.com/blog/wellthrive-tutor-lms-theme', 'https://tutorlms.com/themes/wellthrive/'], demos: ['https://wellthrive.tutorlms.io/'] },
];
const MAX_PAGES = 90, OUT = 'research/themes';
const SKIP = /\.(jpe?g|png|gif|webp|svg|pdf|zip|mp4|css|js|xml)(\?|$)|\/(wp-admin|wp-json|feed|cart\/\?|add-to-cart)|[?&](add-to-cart|replytocom|share|orderby)=|#/i;

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36' });
const summary = [];

async function visit(url) {
  const p = await ctx.newPage();
  try {
    const res = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await p.waitForTimeout(2500);
    const data = await p.evaluate(() => ({
      url: location.href, title: document.title,
      h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim()).filter(Boolean).slice(0, 3),
      h2: [...document.querySelectorAll('h2')].map(h => h.innerText.trim().replace(/\s+/g, ' ')).filter(Boolean).slice(0, 14),
      nav: [...document.querySelectorAll('header a, nav a')].map(a => (a.innerText.trim() || a.getAttribute('aria-label') || '') + ' → ' + a.href).filter(s => !s.startsWith(' →')).slice(0, 60),
      footer: [...document.querySelectorAll('footer a')].map(a => a.innerText.trim() + ' → ' + a.href).filter(s => !s.startsWith(' →')).slice(0, 60),
      links: [...document.querySelectorAll('a[href]')].map(a => a.href),
      bodyClass: document.body.className.slice(0, 300),
      height: document.documentElement.scrollHeight,
    }));
    data.status = res ? res.status() : null;
    return { p, data };
  } catch (e) { await p.close(); return { p: null, data: { url, error: String(e).slice(0, 200) } }; }
}

for (const t of THEMES) {
  const dir = `${OUT}/${t.id}`; mkdirSync(`${dir}/shots`, { recursive: true });
  const info = [];
  const demos = new Set(t.demos);
  for (const u of t.info) {
    const { p, data } = await visit(u);
    if (p) {
      const text = await p.evaluate(() => document.body.innerText.replace(/\n{3,}/g, '\n\n').slice(0, 20000));
      writeFileSync(`${dir}/info-${info.length}.txt`, data.url + '\n\n' + text);
      await p.screenshot({ path: `${dir}/shots/info-${info.length}.jpg`, type: 'jpeg', quality: 45, fullPage: true, clip: { x: 0, y: 0, width: 1440, height: Math.min(data.height, 9000) } }).catch(() => {});
      for (const l of data.links) { try { const h = new URL(l); if (/demo|preview|tutorlms\.io|droip/i.test(l) && !/tutorlms\.com$/.test(h.hostname)) demos.add(h.origin + '/'); } catch {} }
      await p.close();
    }
    info.push({ url: u, title: data.title, error: data.error });
  }

  const pages = [], seen = new Set(), templates = new Map();
  const queue = [...demos];
  const hosts = new Set([...demos].map(d => new URL(d).hostname));
  while (queue.length && pages.length < MAX_PAGES) {
    const url = queue.shift().replace(/\/$/, '') + '/';
    const norm = url.replace(/^https?:\/\/(www\.)?/, '');
    if (seen.has(norm)) continue; seen.add(norm);
    const { p, data } = await visit(url);
    if (!p) { pages.push(data); continue; }
    hosts.add(new URL(data.url).hostname);
    // template key: first path segment + depth (e.g. "courses/2"), so one screenshot per kind of page
    const segs = new URL(data.url).pathname.split('/').filter(Boolean);
    const key = (segs[0] || 'home') + '/' + segs.length;
    data.template = key;
    if (!templates.has(key)) {
      const file = `shots/${String(templates.size + 1).padStart(2, '0')}-${key.replace(/[^a-z0-9]+/gi, '-')}.jpg`;
      templates.set(key, file); data.shot = file;
      await p.screenshot({ path: `${dir}/${file}`, type: 'jpeg', quality: 45, fullPage: true, clip: { x: 0, y: 0, width: 1440, height: Math.min(data.height, 9000) } }).catch(() => {});
    }
    for (const l of data.links) { try { const h = new URL(l); if (hosts.has(h.hostname) && !SKIP.test(l)) queue.push(h.origin + h.pathname); } catch {} }
    delete data.links;
    pages.push(data);
    await p.close();
  }
  writeFileSync(`${dir}/pages.json`, JSON.stringify({ theme: t.id, info, demos: [...demos], pages }, null, 2));
  summary.push(`## ${t.id}\n\nDemos: ${[...demos].join(', ')}\nPages crawled: ${pages.length} · templates: ${templates.size}\n\n` +
    pages.map(pg => `- ${pg.error ? '✗' : '·'} ${pg.url}${pg.title ? ' — ' + pg.title : ''}${pg.template ? ' [' + pg.template + ']' : ''}${pg.error ? ' (' + pg.error + ')' : ''}`).join('\n'));
}
writeFileSync(`${OUT}/SUMMARY.md`, '# Tutor LMS theme demos\n\n' + summary.join('\n\n') + '\n');
await browser.close();
