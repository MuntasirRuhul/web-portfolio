"""tokens.json -> tokens.css with per-style --t-<style>-* vars (what the site pages read)."""
import json, re, sys
S = sys.argv[1]
t = json.load(open(S + '/ds/project/tokens.json'))
def cv(v):
    if isinstance(v, dict): v = v.get('light', next(iter(v.values())))
    v = str(v)
    return re.sub(r'\{([\w-]+)\}', r'var(--\1)', v)
def items(sec):
    x = t.get(sec, [])
    if isinstance(x, dict): x = x.get('tokens', x.get('items', []))
    return x
out = ["/* Elena Varga Atelier — generated from tokens.json */", ':root, [data-theme="light"] {']
out += [f"  --{c['name']}: {cv(c['value'])};" for c in items('color')]
out += [f"  --{c['name']}: {cv(c['value'])};" for c in items('shadow')]
out += ["}", ":root {"]
out += [f"  --{c['name']}: {cv(c['value'])};" for c in items('spacing') + items('radius')]
fam = t['type']['families']
out += [f"  --font-{k}: {v};" for k, v in fam.items()]
cls = []
for g in t['type']['groups']:
    for s in g['styles']:
        n, f = s['name'], s.get('family') or g['family']
        out += [f"  --t-{n}-font: var(--font-{f});", f"  --t-{n}-size: {s['fontSize']};", f"  --t-{n}-lh: {s['lineHeight']};",
                f"  --t-{n}-ls: {s['letterSpacing']};", f"  --t-{n}-weight: {s['fontWeight']};"]
        cls.append(f".{n} {{ font-family: var(--t-{n}-font); font-size: var(--t-{n}-size); line-height: var(--t-{n}-lh); letter-spacing: var(--t-{n}-ls); font-weight: var(--t-{n}-weight);" + (" font-style: italic;" if s.get('fontStyle') == 'italic' else '') + " }")
out += ["}"] + cls
open(S + '/ds/project/tokens.css', 'w').write('\n'.join(out) + '\n')
