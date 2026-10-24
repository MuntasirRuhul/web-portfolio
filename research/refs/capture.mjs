// Captures reference sites for colour and type: full-page screenshots plus the
// computed colours and fonts actually used. Output: research/refs/<host>/.
import { chromium } from 'playwright';
import fs from 'node:fs';
const URLS = fs.readFileSync('research/refs/urls.txt', 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
const browser = await chromium.launch();
for (const url of URLS) {
  const host = new URL(url).host.replace(/^www\./, ''), dir = `research/refs/${host}`;
  fs.mkdirSync(dir, { recursive: true });
  for (const [w, name] of [[1440, 'desktop'], [390, 'phone']]) {
    const page = await browser.newPage({ viewport: { width: w, height: 900 }, userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); } scrollTo(0, 0); });
      await page.waitForTimeout(1200);
      await page.screenshot({ path: `${dir}/${name}.jpg`, fullPage: true, type: 'jpeg', quality: 60 });
      if (name === 'desktop') {
        const data = await page.evaluate(() => {
          const count = (m, k, area) => { m[k] = (m[k] || 0) + area; };
          const bg = {}, fg = {}, border = {}, fonts = {};
          for (const el of document.querySelectorAll('body *')) {
            const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
            const cs = getComputedStyle(el), area = r.width * r.height;
            if (cs.backgroundColor && !cs.backgroundColor.endsWith(', 0)') && cs.backgroundColor !== 'transparent') count(bg, cs.backgroundColor, area);
            if (el.childNodes.length && [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) { count(fg, cs.color, r.width); count(fonts, cs.fontFamily.split(',')[0] + ' ' + cs.fontWeight, r.width); }
            if (cs.borderTopWidth !== '0px' && cs.borderTopStyle !== 'none') count(border, cs.borderTopColor, r.width);
          }
          const top = (m, n) => Object.entries(m).sort((a, b) => b[1] - a[1]).slice(0, n).map(([k, v]) => `${k}  (${Math.round(v)})`);
          const vars = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch { return []; } })
            .filter(r => r.selectorText === ':root' || r.selectorText === 'html' || r.selectorText === 'body').map(r => r.cssText).join('\n').slice(0, 6000);
          const sections = [...document.querySelectorAll('section, header, footer, main > div')].slice(0, 30).map(s => {
            const cs = getComputedStyle(s); return `${s.tagName.toLowerCase()}.${(s.className || '').toString().slice(0, 40)} bg=${cs.backgroundColor} color=${cs.color} h=${Math.round(s.getBoundingClientRect().height)}`;
          });
          return { title: document.title, body: getComputedStyle(document.body).backgroundColor, bg: top(bg, 15), fg: top(fg, 12), border: top(border, 8), fonts: top(fonts, 10), vars, sections };
        });
        fs.writeFileSync(`${dir}/colours.md`, `# ${data.title}\n\nURL: ${url}\nBody background: ${data.body}\n\n## Backgrounds by area\n${data.bg.join('\n')}\n\n## Text colours\n${data.fg.join('\n')}\n\n## Borders\n${data.border.join('\n')}\n\n## Fonts\n${data.fonts.join('\n')}\n\n## Sections\n${data.sections.join('\n')}\n\n## Root CSS\n${data.vars}\n`);
      }
    } catch (e) { fs.writeFileSync(`${dir}/error-${name}.txt`, String(e)); }
    await page.close();
  }
}
await browser.close();
