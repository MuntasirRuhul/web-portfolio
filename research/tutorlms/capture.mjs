// Captures reference Tutor LMS demo sites: screenshots, page text, headings and links.
// Run by .github/workflows/capture-tutorlms.yml; output goes to research/tutorlms/<site>/.
import { chromium } from 'playwright';
import fs from 'node:fs';

const SITES = ['https://workademy.tutorlms.io/', 'https://pathwise.tutorlms.io/', 'https://wellthrive.tutorlms.io/'];
// URL fragments that usually identify the page types we care about, in priority order.
const WANT = ['/courses/', '/course/', '/lesson', '/quiz', '/assignment', '/topic', 'course-category', '/instructor', 'pricing', 'membership',
  '/about', '/contact', '/blog', '/event', 'dashboard', 'login', 'register', 'sign', 'cart', 'checkout', '/faq', '/shop', 'become'];
const MAX_PAGES = 22;

const slug = u => (new URL(u).pathname.replace(/\/+$/, '').replace(/^\//, '').replace(/[^a-z0-9]+/gi, '_') || 'home').slice(0, 80);

const browser = await chromium.launch();
for (const site of SITES) {
  const host = new URL(site).host, dir = `research/tutorlms/${host.split('.')[0]}`;
  fs.mkdirSync(dir, { recursive: true });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
  const page = await ctx.newPage();
  const seen = new Set(), queue = [site], index = [];
  while (queue.length && index.length < MAX_PAGES) {
    const url = queue.shift().split('#')[0];
    if (seen.has(url)) continue; seen.add(url);
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
      await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
      await page.waitForTimeout(800);
      const data = await page.evaluate(() => {
        const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
        const headings = [...document.querySelectorAll('h1,h2,h3,h4')].filter(vis).map(h => `${h.tagName} ${h.innerText.trim().replace(/\s+/g, ' ')}`).filter(t => t.length > 3);
        const links = [...new Set([...document.querySelectorAll('a[href]')].map(a => a.href))];
        const nav = [...document.querySelectorAll('header a, nav a')].map(a => `${a.innerText.trim().replace(/\s+/g, ' ')} -> ${a.href}`).filter(t => !t.startsWith(' ->'));
        const footer = [...document.querySelectorAll('footer a')].map(a => `${a.innerText.trim().replace(/\s+/g, ' ')} -> ${a.href}`);
        const sections = [...document.querySelectorAll('main section, .elementor-section, .wp-block-group, section')].filter(vis).slice(0, 60)
          .map(s => (s.querySelector('h1,h2,h3')?.innerText || s.className || '').toString().trim().replace(/\s+/g, ' ').slice(0, 90));
        const body = document.body.className;
        return { title: document.title, headings, links, nav, footer, sections, bodyClass: body, text: document.body.innerText.slice(0, 40000) };
      });
      const name = slug(url);
      await page.screenshot({ path: `${dir}/${name}.jpg`, fullPage: true, type: 'jpeg', quality: 55 });
      fs.writeFileSync(`${dir}/${name}.md`,
        `# ${data.title}\n\nURL: ${url}\nbody class: ${data.bodyClass}\n\n## Headings\n${data.headings.join('\n')}\n\n## Sections\n${[...new Set(data.sections)].join('\n')}\n\n## Header/nav links\n${[...new Set(data.nav)].join('\n')}\n\n## Footer links\n${[...new Set(data.footer)].join('\n')}\n\n## Page text\n${data.text}\n`);
      index.push(`${name}\t${url}\t${data.title}`);
      const same = data.links.filter(l => { try { return new URL(l).host === host; } catch { return false; } }).map(l => l.split('#')[0]);
      // queue wanted page types first, one or two examples of each
      for (const w of WANT) {
        same.filter(l => l.includes(w) && !seen.has(l) && !queue.includes(l)).slice(0, w === '/course/' || w === '/courses/' || w === '/lesson' ? 3 : 1).forEach(l => queue.push(l));
      }
    } catch (e) { index.push(`ERROR\t${url}\t${e.message.split('\n')[0]}`); }
  }
  fs.writeFileSync(`${dir}/index.tsv`, index.join('\n') + '\n');
  await ctx.close();
}
await browser.close();
