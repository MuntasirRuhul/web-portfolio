import re,sys
S=sys.argv[1]
src=open(S+"/valden/Valden/project/Main.dc.html").read()
css=re.search(r"<helmet>.*?<style>(.*?)</style>",src,re.S).group(1)
markup=re.search(r"</helmet>\s*(<div style=\"width: 100%.*)</x-dc>",src,re.S).group(1).rstrip()
script=re.search(r"data-dc-script[^>]*>(.*?)</script>",src,re.S).group(1)

R=[
('<header style="position: fixed; top: 18px;','<header class="v-header" style="position: fixed; top: 18px;'),
('<section aria-labelledby="interlude-title" style=','<section class="v-sec" aria-labelledby="interlude-title" style='),
('<div style="max-width: 1312px; margin: 0 auto; display: grid;','<div class="v-g1" style="max-width: 1312px; margin: 0 auto; display: grid;'),
('<section id="shop" aria-labelledby="shop-title" style=','<section class="v-sec" id="shop" aria-labelledby="shop-title" style='),
('<div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 40px; margin-bottom: 44px">','<div class="v-wrap" style="display: flex; justify-content: space-between; align-items: flex-end; gap: 40px; margin-bottom: 44px">'),
('<div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 30px">','<div class="v-wrap" style="display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 30px">'),
('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 22px">','<div class="v-g4" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 22px">'),
('<p style="margin: 34px 0 0; padding-top: 18px;','<p class="v-wrap" style="margin: 34px 0 0; padding-top: 18px;'),
('<section id="brew" aria-labelledby="brew-title" style=','<section class="v-sec" id="brew" aria-labelledby="brew-title" style='),
('<div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 40px">','<div class="v-wrap" style="display: flex; justify-content: space-between; align-items: flex-end; gap: 40px">'),
('<div style="margin-top: 60px; display: grid; grid-template-columns: 300px','<div class="v-g1" style="margin-top: 60px; display: grid; grid-template-columns: 300px'),
('<section aria-labelledby="close-title" style=','<section class="v-sec" aria-labelledby="close-title" style='),
('<footer style=','<footer class="v-sec" style='),
('<div style="display: flex; align-items: center; gap: 34px; padding-bottom: 40px">','<div class="v-wrap" style="display: flex; align-items: center; gap: 34px; padding-bottom: 40px">'),
('<div style="display: flex; justify-content: space-between; gap: 20px; padding-top: 20px;','<div class="v-wrap" style="display: flex; justify-content: space-between; gap: 20px; padding-top: 20px;'),
('<div style="position: absolute; left: 64px; bottom: 64px; max-width: 300px; z-index: 5">','<div class="v-hc" style="position: absolute; left: 64px; bottom: 64px; max-width: 300px; z-index: 5">'),
('<div id="vS3" style="','<div id="vS3" class="v-s3" style="'),
('<div style="position: absolute; left: 64px; bottom: 72px; z-index: 4; max-width: 340px">','<div class="v-sL" style="position: absolute; left: 64px; bottom: 72px; z-index: 4; max-width: 340px">'),
('<div style="position: absolute; right: 64px; bottom: 72px; z-index: 4;','<div class="v-sR" style="position: absolute; right: 64px; bottom: 72px; z-index: 4;'),
('<div style="position: relative; width: min(1040px, calc(100% - 128px)); height: 520px; margin: 0 auto">','<div class="v-cw" style="position: relative; width: min(1040px, calc(100% - 128px)); height: 520px; margin: 0 auto">'),
('<article style="{{c.style}}"','<article class="v-card2" style="{{c.style}}"'),
('<span style="{{c.avatarStyle}}">','<span class="v-av" style="{{c.avatarStyle}}">'),
('<h3 style="{{c.nameStyle}}">','<h3 class="v-cn" style="{{c.nameStyle}}">'),
('<p style="{{c.textStyle}}">','<p class="v-ct" style="{{c.textStyle}}">'),
]
for a,b in R:
    assert markup.count(a)>=1,a
    markup=markup.replace(a,b)

mobile="""
@media (max-width: 900px){
.v-header{left:8px!important;right:8px!important;top:10px!important;padding:0 8px 0 16px!important}
.v-header nav{display:none!important}
.v-header>a>svg,.v-header>a>span:nth-of-type(2){display:none!important}
section.v-sec{padding-top:88px!important}
.v-sec{padding-left:20px!important;padding-right:20px!important}
.v-g1{grid-template-columns:minmax(0,1fr)!important;gap:32px!important}
.v-g4{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:12px!important}
.v-wrap{flex-wrap:wrap!important;gap:16px!important}
.v-hc{left:20px!important;bottom:40px!important;width:230px!important}
.v-s3{padding:0 20px!important}
#vBadge{top:46%!important;right:4%!important;transform:scale(.7);transform-origin:top right}
.v-sL{left:20px!important;right:20px!important;bottom:170px!important;max-width:none!important}
.v-sL h2{font-size:44px!important}
.v-sR{right:20px!important;bottom:20px!important}
#vShowTins img{width:56vw!important}
#vShowNum{left:20px!important}
.v-cw{width:calc(100% - 40px)!important;height:620px!important}
.v-card2{padding:28px!important}
.v-av{width:72px!important;height:72px!important;margin-top:56px!important;font-size:22px!important}
.v-cn{margin:56px 0 6px!important;font-size:28px!important}
.v-ct{font-size:24px!important;margin-top:24px!important}
[style*="font-size: 84px"]{font-size:52px!important}
}
"""


# ---------- review card restyle (Figma 15:1404) ----------
m=re.search(r'<article class="v-card2".*?</article>',markup,re.S)
new_article = """<article class="v-card2" style="{{c.style}}" aria-hidden="{{c.hidden}}">
          <div style="display: flex; align-items: flex-start; justify-content: space-between; height: 64px; flex: none">
            <svg aria-hidden="true" width="64" height="64" viewBox="0 0 64 64" fill="none" style="display: block; flex: none"><path d="M54.6954 9.84615C58.1087 9.84615 60.2847 14.0275 61.2234 22.3902C61.9914 28.7902 62.3754 36.9822 62.3754 46.9662C62.3754 51.4888 55.4634 53.7502 41.6394 53.7502C39.25 53.7502 37.7567 52.2142 37.1594 49.1422C36.562 46.0702 36.2634 40.7368 36.2634 33.1422C36.2634 17.6115 42.4074 9.84615 54.6954 9.84615ZM19.4166 9.84615C21.8913 9.84615 23.6833 11.8515 24.7926 15.8622C25.9019 20.1288 26.5419 24.3955 26.7126 28.6622C26.9686 34.9768 27.0966 41.0782 27.0966 46.9662C27.0966 51.4888 20.1846 53.7502 6.36062 53.7502C3.97128 53.7502 2.47795 52.2142 1.88062 49.1422C1.28328 46.0702 0.984615 40.7368 0.984615 33.1422C0.984615 17.6115 7.12862 9.84615 19.4166 9.84615Z" fill="{{c.quote}}"></path></svg>
            <span class="v-stamp" style="{{c.stampStyle}}"><span style="font-size: 26px; line-height: 1">{{c.star}}</span><span style="font-size: 26px; line-height: 1">{{c.stampLabel}}</span></span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 32px; padding-left: 20px; flex: 1 1 auto; min-height: 0">
            <div style="display: flex; align-items: center; gap: 12px">
              <span class="v-av" style="{{c.avatarStyle}}"><sc-if value="{{c.photo}}"><img alt="" src="./img/review-avatar.webp" style="width: 100%; height: 100%; object-fit: cover"></sc-if><sc-if value="{{c.noPhoto}}">{{c.mono}}</sc-if></span>
              <div style="display: flex; flex-direction: column; gap: 2px; align-items: flex-start">
                <h3 class="v-cn" style="{{c.nameStyle}}">{{c.name}}</h3>
                <span style="{{c.tagStyle}}">{{c.tag}}</span>
              </div>
            </div>
            <div class="v-bub" style="{{c.bubbleStyle}}">
              <svg aria-hidden="true" width="34.37" height="21.91" viewBox="0 0 34.3719 21.9071" fill="none" style="position: absolute; top: -21px; left: 81px; transform: rotate(180deg)"><path d="M32.368 0H2.00381C0.310871 0 -0.616353 1.97216 0.463635 3.27588L15.2977 21.183C16.0858 22.1343 17.5394 22.1508 18.3489 21.2175L33.879 3.31037C35.0021 2.01537 34.0822 0 32.368 0Z" fill="#F5EEE8"></path></svg>
              <p class="v-ct" style="{{c.textStyle}}">{{c.text}}</p>
            </div>
          </div>
        </article>"""
assert m
markup=markup.replace(m.group(0),new_article)
markup=markup.replace('height: 520px; margin: 0 auto">','height: 640px; margin: 0 auto">',1) if 'v-cw' in markup else markup
markup=markup.replace('min(1040px, calc(100% - 128px)); height: 520px','min(1080px, calc(100% - 128px)); height: 620px')

cards_js = r"""var CARDS = [
  { mono: 'N°1', name: 'NUIT', tag: 'DARK ROAST', star: '★5/5', stamp: 'INTENSITY', bg: '#6E231D', nameC: '#F5EEE8', ring: '#EEC453', tapeBg: '#EEC453', tapeC: '#6E231D', quote: '#DE5F2E', stampC: '#F5EEE8', stampB: '#F5EEE8', stampBg: 'rgba(245,238,232,0.12)', bubC: '#6E231D', avBg: '#F5EEE8', avC: '#6E231D',
    text: 'Cocoa nib up front, molasses in the middle and a long cedar finish. We roast it low and slow so the darkness stays sweet, never bitter.' },
  { mono: 'N°2', name: 'VELOURS', tag: 'MEDIUM-DARK', star: '★4/5', stamp: 'INTENSITY', bg: '#B03A2B', nameC: '#F5EEE8', ring: '#F5EEE8', tapeBg: '#F5EEE8', tapeC: '#B03A2B', quote: '#EEC453', stampC: '#F5EEE8', stampB: '#F5EEE8', stampBg: 'rgba(245,238,232,0.12)', bubC: '#6E231D', avBg: '#EEC453', avC: '#6E231D',
    text: 'Hazelnut and dark cherry, with a syrupy body that holds its own under milk. Our everyday espresso, dressed for the occasion.' },
  { mono: 'N°3', name: 'AURORE', tag: 'LIGHT ROAST', star: '★2/5', stamp: 'INTENSITY', bg: '#EEC453', nameC: '#6E231D', ring: '#6E231D', tapeBg: '#6E231D', tapeC: '#EEC453', quote: '#B03A2B', stampC: '#6E231D', stampB: '#000000', stampBg: 'rgba(245,238,232,0.28)', bubC: '#6E231D', avBg: '#B03A2B', avC: '#F5EEE8',
    text: 'Jasmine on the nose, bergamot and apricot in the cup. Brew it slowly by hand and let it cool a little: that is when it opens up.' },
  { mono: 'BOX', name: 'LE COFFRET', tag: 'ALL THREE', star: '3 TINS', stamp: 'GIFT BOX', bg: '#DE5F2E', nameC: '#3A1410', ring: '#3A1410', tapeBg: '#3A1410', tapeC: '#F5EEE8', quote: '#F5EEE8', stampC: '#3A1410', stampB: '#3A1410', stampBg: 'rgba(245,238,232,0.28)', bubC: '#3A1410', avBg: '#F5EEE8', avC: '#DE5F2E',
    text: 'One of each, in a gift box tied by hand. A month of mornings for someone you like very much, or for yourself. We won’t tell.' }
];"""
script=re.sub(r"var CARDS = \[.*?\n\];",lambda _:cards_js,script,count=1,flags=re.S)

cards_map = r"""cards: CARDS.map(function (c, i) {
        var depth = (i - st.card + nC) % nC, D = DEPTH[depth];
        return {
          mono: c.mono, photo: true, noPhoto: false, name: c.name, tag: c.tag, text: c.text, star: c.star, stampLabel: c.stamp, hidden: depth === 0 ? 'false' : 'true',
          style: 'position: absolute; inset: 0; display: flex; flex-direction: column; border-radius: 34px; padding: 60px; overflow: hidden; background: ' + c.bg + '; z-index: ' + D[3] + '; transform: translate(' + D[0] + 'px, ' + D[1] + 'px) rotate(' + D[2] + 'deg); transition: transform .7s cubic-bezier(.2,.8,.2,1); box-shadow: 0 30px 60px rgba(110,35,29,' + (depth === 0 ? 0.25 : 0.1) + ');',
          quoteStyle: 'display: block; width: 64px; height: 64px; font-family: \'Titan One\', sans-serif; font-size: 130px; line-height: 0.9; color: ' + c.quote + ';',
          stampStyle: 'display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; padding: 20px 16px; margin: 6px 14px 0 0; border: 2px dashed ' + c.stampB + '; border-radius: 12px; background: ' + c.stampBg + '; color: ' + c.stampC + '; font-family: \'Mouse Memoirs\', sans-serif; transform: rotate(8deg); white-space: nowrap;',
          avatarStyle: 'flex: 0 0 auto; width: 160px; height: 160px; border: 5px solid ' + c.ring + '; border-radius: 50%; display: grid; place-items: center; overflow: hidden; background: ' + c.avBg + '; color: ' + c.avC + '; font-family: \'Titan One\', sans-serif; font-size: 44px;',
          nameStyle: 'margin: 0; font-family: \'Titan One\', sans-serif; font-weight: 400; font-size: 52px; line-height: 1; color: ' + c.nameC + '; white-space: nowrap;',
          tagStyle: 'display: inline-block; padding: 10px 20px 6px; background: ' + c.tapeBg + '; color: ' + c.tapeC + '; font-family: \'Mouse Memoirs\', sans-serif; font-size: 30px; line-height: 1; white-space: nowrap;',
          bubbleStyle: 'position: relative; flex: 1 1 auto; min-height: 0; background: #F5EEE8; border-radius: 24px; padding: 48px 48px 80px;',
          tailStyle: 'position: absolute; top: -22px; left: 79px; width: 0; height: 0; border-left: 19.5px solid transparent; border-right: 19.5px solid transparent; border-bottom: 23px solid #F5EEE8;',
          textStyle: 'margin: 0; font-family: \'Mouse Memoirs\', sans-serif; font-size: 34px; line-height: 1.12; letter-spacing: 0.34px; text-transform: uppercase; color: ' + c.bubC + ';'
        };
      }),
      cardNext:"""
script=re.sub(r"cards: CARDS\.map\(function \(c, i\) \{.*?\n      cardNext:",lambda _:cards_map,script,count=1,flags=re.S)
mobile=mobile.replace(".v-cw{width:calc(100% - 40px)!important;height:620px!important}",".v-cw{width:calc(100% - 40px)!important;height:720px!important}")
mobile=re.sub(r"\.v-card2\{.*?\n\.v-ct\{[^\n]*\n","""\\.v-card2{padding:24px!important}
.v-av{width:88px!important;height:88px!important;font-size:24px!important}
.v-cn{font-size:30px!important}
.v-stamp{transform:rotate(8deg) scale(.6)!important;transform-origin:top right!important;margin:0!important}
.v-cn{font-size:26px!important}
.v-bub{padding:28px 22px 40px!important}
.v-ct{font-size:22px!important}
""".replace("\\\\.","."),mobile,flags=re.S)


# ---------- hero update (Figma 8:1329) ----------
def rep(a,b,cnt=1):
    global markup
    assert markup.count(a)>=1,a[:80]
    markup=markup.replace(a,b,cnt)
rep('aria-label="Open slowly. Valden grand cru coffee."','aria-label="Helios slowly. Valden grand cru coffee."')
rep('letter-spacing: 0.005em">OPEN</span>','letter-spacing: 0.0165em">HELIOS</span>')
rep('style="--tw: min(23vw, 37vh, 360px); position: sticky;','style="--tw: min(23vw, 37vh, 360px); --jw: min(max(25.8vw, 220px), 45.8vh); position: sticky;')
mm=re.search(r'<div id="vCup".*?id="vLid"[^>]*>\s*</div>',markup,re.S); assert mm
markup=markup.replace(mm.group(0),"""<div id="vCup" role="img" aria-label="A Helios First Light instant coffee jar with a gold lid" style="position: absolute; left: 50%; top: 30.4%; width: var(--jw); aspect-ratio: 1024 / 1536; z-index: 3; transform: translate(-50%, 0); will-change: transform, left, top">
        <sc-for list="{{burst}}" as="b" hint-placeholder-count="0">
          <img aria-hidden="true" alt="" id="{{b.id}}" src="./img/bean.webp" style="{{b.style}}">
        </sc-for>
        <img aria-hidden="true" alt="" src="./img/hero-jar.webp" style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 2; filter: drop-shadow(0 40px 40px rgba(58,20,16,.25))">
      </div>""")
rep('<div class="v-hc" style="position: absolute; left: 64px; bottom: 64px; max-width: 300px; z-index: 5">','<div class="v-hc" style="position: absolute; left: 66px; bottom: 66px; width: 279px; z-index: 5">')
rep('<p style="margin: 0 0 22px; font-size: 15px; line-height: 1.6">Grand cru','<p style="margin: 0 0 20px; font-size: 15px; line-height: 1.6">Grand cru')
rep('display: inline-flex; align-items: center; gap: 30px; min-height: 56px; padding: 0 26px; border-radius: 999px; background: #F5EEE8; color: #6E231D; font-family: \'Titan One\', sans-serif; font-size: 17px; text-decoration: none">FIND YOUR TIN <span aria-hidden="true">→</span></a>',
    'display: inline-flex; align-items: center; gap: 10px; height: 56px; padding: 0 26px; border-radius: 28px; background: #F5EEE8; color: #6E231D; font-family: \'Titan One\', sans-serif; font-size: 17px; line-height: 1.55; text-decoration: none; white-space: nowrap">FIND YOUR TIN <img class="v-arr" alt="" aria-hidden="true" src="./img/doodle-arrow-sharp.svg" width="44" height="26" style="display: block; flex: none; width: 44px; height: 26px"></a>')
rep('<div aria-hidden="true" style="position: absolute; left: 64px; bottom: 28px; z-index: 6; display: flex; align-items: center; gap: 8px">','<div aria-hidden="true" style="position: absolute; left: 66px; bottom: 28px; z-index: 6; display: flex; align-items: center; gap: 4px">')
rep('style="position: absolute; right: 8%; top: 52%; z-index: 6; width: 150px; height: 150px; text-decoration: none"','style="position: absolute; right: 9.5%; top: 64.8%; z-index: 6; width: 149px; height: 151px; text-decoration: none"')
css += "\n.v-arr{transition:transform .2s}.v-btn:hover .v-arr{transform:translateX(4px)}\n"

# paint(): jar instead of tin + lid
def srep(a,b):
    global script
    assert script.count(a)==1,a[:70]
    script=script.replace(a,b)
srep("cup = $('vCup'), lid = $('vLid');","cup = $('vCup');")
srep("s1 && s2 && s3 && cup && lid) {","s1 && s2 && s3 && cup) {")
old=re.search(r"      cup\.style\.left = mix\(50, 71, u\).*?lid\.style\.transform = [^\n]*\n",script,re.S); assert old
script=script.replace(old.group(0),"""      var iw = window.innerWidth, ih = window.innerHeight, SH = Math.max(ih, 720);
      var jw = Math.min(Math.max(0.258 * iw, 220), 0.458 * ih), tw = Math.min(0.23 * iw, 0.37 * ih, 360);
      var landS = Math.min(1, tw * 1.058 / jw), hj = jw * 1.5, tinB = 0.12 * SH + tw * 1.467 * 1.04;
      var landTop = (tinB - hj * (1 + landS) / 2) / SH * 100;   // jar base sits where the tin base sat
      cup.style.left = mix(50, 71, u) + '%';
      cup.style.top = (p < 0.55 ? mix(mix(30.4, 24, o), -80, u) : mix(-80, landTop, dn)) + '%';
      var rot = p < 0.55 ? mix(mix(-8, -11, o), 2, u) : mix(2, 0, dn);   // upright jar: starts with a slight tilt like the design, lands straight
      cup.style.transform = 'translate(-50%, 0) rotate(' + rot + 'deg) scale(' + (p < 0.55 ? mix(1, 1.04, o) : mix(1.04, landS, dn)) + ')';
""")
srep("el.style.top = mix(23, b[1], o) + '%';","el.style.top = mix(8, b[1], o) + '%';")
srep("left: 50%; top: 23%; width: ' + b[2]","left: 50%; top: 8%; width: ' + b[2]")


# ---------- blend showcase order: Velours -> Aurore -> Nuit ----------
m=re.search(r"var SCENES = \[\n(.*?)\n\];",script,re.S); assert m
parts=re.split(r"\n(?=  \{ id: )","\n"+m.group(1)); parts=[x.strip("\n") for x in parts if x.strip()]
byid={re.search(r"id: '(\w+)'",x).group(1):x.rstrip().rstrip(",") for x in parts}
order=["velours","aurore","nuit"]
script=script.replace(m.group(0),"var SCENES = [\n"+",\n".join(byid[k] for k in order)+"\n];")
for a,b in [('id="vT0" alt="" src="./img/tin-nuit.webp"','id="vT0" alt="" src="./img/tin-velours.webp"'),
            ('id="vT1" alt="" src="./img/tin-velours.webp"','id="vT1" alt="" src="./img/tin-aurore.webp"'),
            ('id="vT2" alt="" src="./img/tin-aurore.webp"','id="vT2" alt="" src="./img/tin-nuit.webp"'),
            ('<div id="vShow" style="position: sticky; top: 0; height: 100vh; min-height: 720px; overflow: hidden; background: #6E231D">','<div id="vShow" style="position: sticky; top: 0; height: 100vh; min-height: 720px; overflow: hidden; background: #DE5F2E">')]:
    assert markup.count(a)==1,a
    markup=markup.replace(a,b)


# ---------- ribbons section: B + C combined (headline + tilted tape of scrolling stamps) ----------
mm=re.search(r'<div id="vRib".*?</svg>\s*</div>',markup,re.S); assert mm
def stamp(a,b,bg,rot): return f'<span class="v-st" style="background:{bg};transform:rotate({rot}deg)">{a}<br>{b}</span>'
one=("".join([stamp("SMALL","LOTS","rgba(245,238,232,.7)",-6),'<i>✦</i>',stamp("HAND-","SEALED","#B03A2B",4).replace('class="v-st"','class="v-st v-st-r"'),'<i>✦</i>',stamp("ROASTED","TO ORDER","rgba(245,238,232,.7)",-3),'<i>✦</i>']))
half=one*4
markup=markup.replace(mm.group(0),f"""<div id="vRib" class="v-bc">
      <p class="v-sr">Dangerously smooth. Small lots. Hand-sealed. Roasted to order.</p>
      <div class="v-bc-band" aria-hidden="true"><div class="v-bc-in"><div>{half}</div><div>{half}</div></div></div>
    </div>""")
css+="""
.v-bc{position:relative;padding:72px 0 0;text-align:center;margin-bottom:150px}
.v-bc-h{margin:0;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(52px,9vw,128px);line-height:.9;color:#6E231D}
.v-bc-h em{font-style:normal;color:#B03A2B}
.v-bc-band{width:120%;margin:0 0 0 -10%;transform:rotate(-2deg);background:#EEC453;padding:26px 0;overflow:hidden;white-space:nowrap}
.v-bc-in{display:inline-flex;animation:vBc 60s linear infinite}
.v-bc-in>div{display:inline-flex;align-items:center;gap:36px;padding-right:36px}
.v-bc-in i{font-style:normal;font-size:30px;color:#6E231D}
.v-st{flex:none;width:116px;height:116px;border-radius:50%;border:2px dashed #6E231D;display:grid;place-items:center;text-align:center;font-family:'Mouse Memoirs',sans-serif;font-size:25px;line-height:1;color:#6E231D}
.v-st-r{color:#F5EEE8}
.v-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes vBc{to{transform:translateX(-50%)}}
@media (max-width:900px){.v-bc{padding-top:48px;margin-bottom:100px}.v-st{width:96px;height:96px;font-size:21px}}
@media (prefers-reduced-motion:reduce){.v-bc-in{animation:none}}
"""


# ---------- wave ribbon dividers ----------
def _wave(top_c, band_c, below_c, txt, txt_c, uid, h=120):
    segs=[(0,150),((150,175),(280,190),(450,140)),((640,85),(820,40),(1010,52)),((1190,63),(1330,100),(1440,120))]
    def fwd(dy):
        d=f"M0 {150+dy}"
        for c in segs[1:]:
            d+=" C"+" ".join(f"{x} {y+dy}" for x,y in c)
        return d
    def rev(dy):
        pts=[segs[0]]+[c[2] for c in segs[1:]]
        ctrl=[c for c in segs[1:]]
        d=f"L1440 {120+dy}"
        for i in range(len(ctrl)-1,-1,-1):
            c1,c2,e=ctrl[i]; start=pts[i]
            d+=f" C{c2[0]} {c2[1]+dy} {c1[0]} {c1[1]+dy} {start[0]} {start[1]+dy}"
        return d
    band=fwd(0)+" "+rev(h)+" Z"
    below=f"M0 {150+h}"+"".join(" C"+" ".join(f"{x} {y+h}" for x,y in c) for c in segs[1:])+" L1440 330 L0 330 Z"
    mid=fwd(h//2)
    rep=(txt+" ✦ ")*3
    return f'<div class="v-div" aria-hidden="true" style="background:{top_c}"><svg viewBox="0 0 1440 330"><path d="{below}" fill="{below_c}"/><path d="{band}" fill="{band_c}"/><path id="dvp{uid}" d="{mid}" fill="none"/><text font-family="Titan One, sans-serif" font-size="62" letter-spacing="2" fill="{txt_c}" dominant-baseline="central"><textPath href="#dvp{uid}" startOffset="-100">{rep}</textPath></text></svg></div>'
a='<section id="notes" aria-labelledby="notes-title"'
assert markup.count(a)==1
markup=markup.replace(a,_wave("#6E231D","#B03A2B","#E9BFAE","DANGEROUSLY SMOOTH","#F5EEE8",0)+"\n  "+a)
b='<!-- ================= FOOTER ================= -->'
assert markup.count(b)==1
markup=markup.replace(b,_wave("#B03A2B","#6E231D","#E9BFAE","GRAND CRU COFFEE","#E9BFAE",1)+"\n  "+b)
css+="""
.v-div{line-height:0;overflow:hidden;margin-bottom:-1px}
.v-div svg{display:block;width:100%;height:auto}
"""


srep("    // ---------- ribbons follow the scroll ----------","""    // ---------- wave dividers: text drifts along the ribbon ----------
    if (this.state.cine) {
      var dvs = document.querySelectorAll('.v-div');
      for (var di = 0; di < dvs.length; di++) {
        var dr = dvs[di].getBoundingClientRect(), dq = clamp((window.innerHeight - dr.top) / (window.innerHeight + dr.height));
        var dtp = dvs[di].querySelector('textPath');
        if (dtp) dtp.setAttribute('startOffset', String(-80 - dq * 700));
      }
    }
    // ---------- ribbons follow the scroll ----------""")


# ---------- notebook heading: remove the visible title, keep an accessible name ----------
hm=re.search(r'<h2 id="notes-title".*?</h2>',markup,re.S); assert hm
markup=markup.replace(hm.group(0),'<h2 id="notes-title" class="v-sr">From the roaster’s notebook</h2>')


# ---------- shop: sliding panels (replaces the 4-card grid) ----------
gm=re.search(r'<div class="v-g4".*?</sc-for>\s*</div>',markup,re.S); assert gm
markup=markup.replace(gm.group(0),"""<div class="v-acc">
      <sc-for list="{{visible}}" as="p" hint-placeholder-count="4">
        <div class="v-pn{{p.onCls}}" role="button" tabindex="0" aria-expanded="{{p.on}}" aria-label="{{p.name}}" onClick="{{p.select}}" style="background: {{p.tint}}">
          <span class="v-vn" aria-hidden="true">{{p.nameUp}}</span>
          <sc-if value="{{p.isNuit}}" hint-placeholder-val="{{ false }}"><img class="v-pa v-pj" src="./img/helios-jar.webp" alt="Helios First Light instant coffee jar"></sc-if>
          <sc-if value="{{p.isVel}}" hint-placeholder-val="{{ false }}"><img class="v-pa" src="./img/tin-velours.webp" alt="Oxblood Velours tin with a gold lid"></sc-if>
          <sc-if value="{{p.isAur}}" hint-placeholder-val="{{ false }}"><img class="v-pa" src="./img/tin-aurore.webp" alt="Ivory Aurore tin with a gold lid"></sc-if>
          <sc-if value="{{p.set}}" hint-placeholder-val="{{ false }}"><div class="v-pa v-pset"><img src="./img/tin-aurore.webp" alt=""><img src="./img/tin-velours.webp" alt=""><img src="./img/tin-nuit.webp" alt="Nuit, Velours and Aurore tins together"></div></sc-if>
          <div class="v-det">
            <span class="v-tg">{{p.tag}}</span>
            <h3 class="v-dn"><button type="button" onClick="{{p.open}}">{{p.nameUp}}</button></h3>
            <div class="v-nt"><sc-for list="{{p.noteList}}" as="n" hint-placeholder-count="3"><span>{{n.t}}</span></sc-for></div>
            <div class="v-bt"><span class="v-pr">{{p.priceText}}</span><button class="v-add2" type="button" onClick="{{p.quick}}" aria-label="{{p.quickLabel}}"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></button></div>
          </div>
        </div>
      </sc-for>
    </div>""")
css+="""
.v-acc{display:flex;gap:12px;height:520px}
.v-pn{flex:1;min-width:0;border-radius:26px;position:relative;overflow:hidden;cursor:pointer;transition:flex .6s cubic-bezier(.2,.8,.2,1)}
.v-pn.on{flex:3.6;cursor:default}
.v-vn{position:absolute;left:50%;top:50%;writing-mode:vertical-rl;transform:translate(-50%,-50%) rotate(180deg);font-family:'Titan One',sans-serif;font-size:clamp(34px,3.4vw,50px);line-height:1;color:#6E231D;white-space:nowrap;transition:opacity .25s}
.v-pn.on .v-vn{opacity:0}
.v-pa{position:absolute;right:5%;bottom:26px;width:min(300px,42%);opacity:0;pointer-events:none;transition:opacity .3s;filter:drop-shadow(0 18px 14px rgba(58,20,16,.25))}
.v-pn.on .v-pa{opacity:1;transition-delay:.2s}
.v-pj{width:auto;height:min(450px,86%)}
.v-pset{aspect-ratio:1/1;width:min(340px,46%)}
.v-pset img{position:absolute;width:44%}
.v-pset img:nth-child(1){left:2%;top:24%;transform:rotate(-10deg)}
.v-pset img:nth-child(2){right:2%;top:22%;transform:rotate(9deg)}
.v-pset img:nth-child(3){left:26%;top:32%;width:48%}
.v-det{position:absolute;left:32px;bottom:30px;width:calc(53% - 64px);max-width:330px;opacity:0;transform:translateY(14px);pointer-events:none;visibility:hidden;transition:opacity .35s,transform .35s,visibility 0s .4s}
.v-pn.on .v-det{opacity:1;transform:none;pointer-events:auto;visibility:visible;transition:opacity .35s .2s,transform .35s .2s,visibility 0s}
.v-tg{display:inline-block;padding:7px 12px 3px;background:#EEC453;color:#6E231D;font-family:'Mouse Memoirs',sans-serif;font-size:21px;line-height:1;text-transform:uppercase;transform:rotate(-3deg)}
.v-dn{margin:14px 0;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(30px,3.4vw,50px);line-height:.95;color:#6E231D}
.v-dn button{padding:0;border:0;background:none;font:inherit;color:inherit;text-align:left;text-transform:uppercase}
.v-nt{display:flex;flex-wrap:wrap;gap:6px}
.v-nt span{background:#F5EEE8;color:#6E231D;padding:6px 10px 2px;font-family:'Mouse Memoirs',sans-serif;font-size:20px;line-height:1.1;text-transform:uppercase}
.v-bt{display:flex;align-items:center;gap:14px;margin-top:20px}
.v-pr{font-family:'Titan One',sans-serif;font-size:34px;line-height:1;color:#6E231D}
.v-add2{flex:none;width:46px;height:46px;border-radius:50%;border:0;background:#6E231D;color:#F5EEE8;display:grid;place-items:center;transition:background-color .2s,color .2s,transform .2s}
.v-add2:hover{background:#B03A2B;transform:rotate(90deg)}
@media (max-width:820px){
.v-acc{flex-direction:column;height:auto}
.v-pn{flex:none;height:78px;transition:height .55s cubic-bezier(.2,.8,.2,1)}
.v-pn.on{height:470px;flex:none}
.v-vn{writing-mode:horizontal-tb;transform:translateY(-50%);left:22px;top:39px;font-size:32px}
.v-pa{right:10px;bottom:16px;width:44%}
.v-pj{width:auto;height:300px}
.v-pset{width:46%}
.v-det{left:22px;bottom:24px;width:50%}
.v-dn{font-size:30px}
}
@media (prefers-reduced-motion:reduce){.v-pn,.v-pa,.v-det{transition-duration:.01ms!important}}
"""
# state + data
def sub(a,b):
    global script
    assert script.count(a)==1,a[:70]
    script=script.replace(a,b)
sub("this.state = { cine: true, filter: 'all', sort: 'featured',","this.state = { cine: true, panel: 'nuit', filter: 'all', sort: 'featured',")
sub("    var d = st.detail ? BY[st.detail] : null;","    var act = list.some(function (x) { return x.id === st.panel; }) ? st.panel : (list[0] && list[0].id);\n    var d = st.detail ? BY[st.detail] : null;")
sub("          quickLabel: 'Add ' + p.name + ' to bag',","          quickLabel: 'Add ' + p.name + ' to bag',\n          on: p.id === act, onCls: p.id === act ? ' on' : '', tint: p.tint,\n          noteList: p.notes.split(', ').map(function (t) { return { t: t }; }),\n          select: function () { self.setState({ panel: p.id }); },")


# ---------- remove the stamp tape; keep a small spacer under the wave ----------
vm=re.search(r'<div id="vRib" class="v-bc">.*?</div></div></div>\s*</div>',markup,re.S); assert vm
markup=markup.replace(vm.group(0),'<div id="vRib" class="v-gap" aria-hidden="true"></div>')
css+=".v-gap{height:200px}\n@media (max-width:900px){.v-gap{height:120px}}\n"


# ---------- doodle arrow everywhere ----------
def _da(w,h,extra=""):
    return f'<img class="v-arr" alt="" aria-hidden="true" src="./img/doodle-arrow-sharp.svg" width="{w}" height="{h}" style="display: block; flex: none; width: {w}px; height: {h}px{extra}">'
n1=markup.count('<span aria-hidden="true">→</span>')
markup=markup.replace('<span aria-hidden="true">→</span>',_da(44,26))
n2=markup.count('<span class="v-arrow" aria-hidden="true">→</span>')
markup=markup.replace('<span class="v-arrow" aria-hidden="true">→</span>',_da(36,21))
def _rb(m): return m.group(1)+(_da(40,24,"; transform: scaleX(-1)") if m.group(2)=="←" else _da(40,24))+m.group(3)
markup,n3=re.subn(r'(<span class="v-mag-in"[^>]*>)([←→])(</span>)',_rb,markup)
print("arrows replaced:",n1,n2,n3)
assert n1>=1 and n2==3 and n3==2


# ---------- closing section: boarding pass ----------
cm=re.search(r'<section class="v-sec" aria-labelledby="close-title".*?</section>',markup,re.S); assert cm
markup=markup.replace(cm.group(0),"""<section class="v-sec v-close" aria-labelledby="close-title">
    <div class="v-pass">
      <div class="v-pm">
        <p class="v-pe">Same time tomorrow?</p>
        <h2 id="close-title" class="v-ph">SEE YOU<br>AT SEVEN.</h2>
        <a class="v-btn v-pcta" href="#shop">SHOP THE TINS <img class="v-arr" alt="" aria-hidden="true" src="./img/doodle-arrow-sharp.svg" width="44" height="26"></a>
        <p class="v-pf">Roasted to order. Sealed by hand.</p>
        <img class="v-ptin" src="./img/tin-velours.webp" alt="Velours tin with a gold lid">
      </div>
      <div class="v-pstub" aria-hidden="true"><small>Admit one</small><b>7:00<br>AM</b><span class="v-bar"></span></div>
    </div>
  </section>""")
css+="""
.v-close{background:#B03A2B;padding:160px 56px 140px;overflow:hidden}
.v-pass{position:relative;width:min(1100px,100%);margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) 210px;background:#F5EEE8;border-radius:20px;transform:rotate(-1.5deg);filter:drop-shadow(0 28px 34px rgba(58,20,16,.35))}
.v-pm{position:relative;padding:56px 250px 50px 60px}
.v-pe{margin:0;font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#B03A2B}
.v-ph{margin:16px 0 30px;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(44px,7.4vw,104px);line-height:.88;color:#6E231D;text-transform:uppercase}
.v-pcta{display:inline-flex;align-items:center;gap:10px;height:56px;padding:0 26px;border-radius:28px;background:#6E231D;color:#F5EEE8;font-family:'Titan One',sans-serif;font-size:17px;line-height:1.55;text-decoration:none;white-space:nowrap}
.v-pcta img{display:block;width:44px;height:26px}
.v-pf{margin:18px 0 0;font-size:14px;line-height:1.5;color:#7A5A50}
.v-ptin{position:absolute;right:26px;bottom:-56px;width:min(230px,23%);transform:rotate(7deg);filter:drop-shadow(0 24px 20px rgba(58,20,16,.4))}
.v-pstub{position:relative;border-left:3px dashed rgba(110,35,29,.3);padding:30px 22px;display:grid;align-content:space-between;justify-items:center;gap:16px;text-align:center}
.v-pstub::before,.v-pstub::after{content:"";position:absolute;left:-17px;width:30px;height:30px;border-radius:50%;background:#B03A2B}
.v-pstub::before{top:-15px}.v-pstub::after{bottom:-15px}
.v-pstub small{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#7A5A50}
.v-pstub b{font-family:'Titan One',sans-serif;font-weight:400;font-size:62px;line-height:.9;color:#B03A2B}
.v-bar{display:block;width:100%;height:64px;background:repeating-linear-gradient(90deg,#6E231D 0 3px,transparent 3px 6px,#6E231D 6px 7px,transparent 7px 11px,#6E231D 11px 15px,transparent 15px 18px)}
@media (max-width:820px){.v-close{padding:110px 20px 90px}.v-pass{grid-template-columns:1fr}.v-pm{padding:34px 24px}.v-ph{margin-bottom:22px}.v-ptin{right:16px;top:-56px;bottom:auto;width:96px}.v-pstub{border-left:0;border-top:3px dashed rgba(110,35,29,.3);grid-template-columns:auto 1fr;align-content:center;padding:20px}.v-pstub::before,.v-pstub::after{display:none}.v-pstub b{font-size:44px}}
"""


# ---------- sticker band between the review cards and the shop ----------
_defs="""<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<g id="i-bean"><g transform="rotate(28 60 60)"><ellipse cx="60" cy="60" rx="28" ry="42"/><path d="M60 20C44 44 76 76 60 100" fill="none"/></g></g>
<g id="i-beans"><use href="#i-bean" transform="translate(-14 -16) scale(.62)"/><use href="#i-bean" transform="translate(44 -2) scale(.62)"/><use href="#i-bean" transform="translate(12 46) scale(.62)"/></g>
<g id="i-moka"><path d="M32 104H88L80 70H40Z"/><path d="M40 70L33 34H87L80 70"/><path d="M35 34L60 20L85 34"/><path d="M87 42H102V68H82" fill="none"/><circle cx="60" cy="15" r="5"/><path d="M50 40L52 66M60 40V66M70 40L68 66M46 84L74 84" fill="none"/></g>
<g id="i-cup"><path d="M30 54H84V84A24 24 0 0 1 60 108H54A24 24 0 0 1 30 84Z"/><path d="M84 62H92A11 11 0 0 1 92 84H84" fill="none"/><path d="M46 44C38 36 54 32 46 22M62 44C54 36 70 32 62 22" fill="none"/><path d="M38 66H76" fill="none"/></g>
<g id="i-dripper"><path d="M24 36H96L76 70H44Z"/><path d="M96 42H108V54H92" fill="none"/><path d="M42 78H78V92A14 14 0 0 1 64 106H56A14 14 0 0 1 42 92Z"/><path d="M60 72V76M48 48H72" fill="none"/></g>
<g id="i-tin"><path d="M34 44V92A26 9 0 0 0 86 92V44"/><ellipse cx="60" cy="44" rx="26" ry="9"/><path d="M34 54A26 9 0 0 0 86 54M34 82A26 9 0 0 0 86 82" fill="none"/><circle cx="60" cy="68" r="9"/><path d="M56 64L60 73L64 64" fill="none"/></g>
<g id="i-latte"><circle cx="60" cy="60" r="40"/><circle cx="60" cy="60" r="29" fill="none"/><path d="M60 80C34 62 44 40 60 54C76 40 86 62 60 80Z"/></g>
<g id="i-sun"><circle cx="60" cy="50" r="24"/><path d="M60 10V19M60 81V90M20 50H29M91 50H100M31 21L37 27M89 21L83 27M31 79L37 73M89 79L83 73" fill="none"/><path d="M47 49Q51 54 55 49M65 49Q69 54 73 49M54 60Q60 65 66 60" fill="none"/><path d="M40 86H80V96A12 12 0 0 1 68 108H52A12 12 0 0 1 40 96Z"/></g>
</defs></svg>"""
_badge="""<svg class="v-stk" viewBox="-8 -8 136 136" width="{w}" height="{w}" style="transform:rotate({r}deg);margin-top:{m}px" aria-hidden="true"><defs><path id="bdp" d="M28 66A32 40 0 0 1 92 66"/></defs><ellipse cx="60" cy="60" rx="42" ry="54" fill="#F5EEE8" stroke="#F5EEE8" stroke-width="15"/><ellipse cx="60" cy="60" rx="42" ry="54" fill="#F5EEE8" stroke="#6E231D" stroke-width="2.6"/><ellipse cx="60" cy="60" rx="35" ry="47" fill="none" stroke="#6E231D" stroke-width="1.4"/><text font-family="Mouse Memoirs, sans-serif" font-size="13" letter-spacing="1.5" fill="#6E231D" text-anchor="middle"><textPath href="#bdp" startOffset="50%">GRAND CRU COFFEE</textPath></text><text x="60" y="78" text-anchor="middle" font-family="Titan One, sans-serif" font-size="46" fill="#B03A2B">V</text><text x="60" y="96" text-anchor="middle" font-family="Mouse Memoirs, sans-serif" font-size="12" letter-spacing="1.5" fill="#6E231D">SMALL LOTS</text></svg>"""
def _stk(i,w,r,m):
    return f'<svg class="v-stk" viewBox="-8 -8 136 136" width="{w}" height="{w}" style="transform:rotate({r}deg);margin-top:{m}px" aria-hidden="true"><g fill="#F5EEE8" stroke="#F5EEE8" stroke-width="15" stroke-linejoin="round" stroke-linecap="round"><use href="#i-{i}"/></g><g fill="#F5EEE8" stroke="#6E231D" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"><use href="#i-{i}"/></g></svg>'
_seq=[("cup",120,-8,-10),("badge",116,5,14),("moka",138,-4,-4),("beans",110,10,18),("sun",126,-9,-14),("tin",132,6,6),("bean",96,-14,16),("dripper",130,-5,-8),("latte",112,9,12)]
_seq=[(k,round(w*1.2),r,m) for k,w,r,m in _seq]
_one="".join((_badge.format(w=w,r=r,m=m) if k=="badge" else _stk(k,w,r,m)) for k,w,r,m in _seq)
_band=f'<div class="v-stk-band" aria-hidden="true">{_defs}<div class="v-stk-in"><div>{_one}</div><div>{_one}</div></div></div>'
_sh='<section class="v-sec" id="shop"'
assert markup.count(_sh)==1
pass  # sticker band removed; no shared sticker defs needed
css+="""
.v-stk-band{background:#B03A2B;padding:54px 0;overflow:hidden;white-space:nowrap}
.v-stk-in{display:inline-flex;animation:vStk 120s linear infinite}
.v-stk-in>div{display:inline-flex;align-items:center;gap:30px;padding-right:30px}
.v-stk{display:block;flex:none;filter:drop-shadow(0 5px 0 rgba(58,20,16,.22))}
@keyframes vStk{to{transform:translateX(-50%)}}
@media (max-width:900px){.v-stk-band{padding:34px 0}.v-stk{zoom:.78}}
@media (prefers-reduced-motion:reduce){.v-stk-in{animation:none}}
"""




# ---------- brew bar: profile card with recipe-poster grid ----------
bm=re.search(r'(<section class="v-sec" id="brew"[^>]*>).*?</section>',markup,re.S); assert bm
markup=markup.replace(bm.group(0),bm.group(1)+"""
    <div class="v-br">
      <div class="v-br-l">
        <span style="display: inline-block; padding: 8px 14px 4px; background: #B03A2B; color: #F5EEE8; font-family: 'Mouse Memoirs', sans-serif; font-size: 24px; line-height: 1; transform: rotate(-3deg)">THE BREW BAR</span>
        <h2 id="brew-title" class="v-br-h">HOW MANY CUPS?<br><span>WE’LL DO THE MATHS.</span></h2>
        <p class="v-br-p">Pick a method and a number of cups. The recipe updates as you go.</p>
      </div>
      <div class="v-brc">
        <img class="v-brj" src="./img/helios-jar.webp" alt="" aria-hidden="true">
        <div class="v-brc-top"><b>valden.brewbar</b><span aria-hidden="true">✦</span></div>
        <div class="v-brc-pro">
          <span class="v-brc-av" aria-hidden="true">V</span>
          <div class="v-brc-st"><div><b>4</b><small>methods</small></div><div><b>{{brew.cups}}</b><small>{{brew.unitPlural}}</small></div><div><b>1:{{brew.ratio}}</b><small>ratio</small></div></div>
        </div>
        <p class="v-brc-bio">The best brew, by weight. Pick a method below, set your cups, and we do the maths.<br><span>valden.coffee/brew</span></p>
        <div class="v-brc-step" role="group" aria-label="Number of cups">
          <button type="button" onClick="{{cupsDown}}" aria-label="Fewer">−</button>
          <output aria-live="polite">{{brew.cups}}</output>
          <button type="button" onClick="{{cupsUp}}" aria-label="More">+</button>
          <span>{{brew.unitPlural}}</span>
        </div>
        <div class="v-brc-tabs" role="group" aria-label="Brew method">
          <sc-for list="{{methods}}" as="m" hint-placeholder-count="4"><button type="button" aria-pressed="{{m.pressed}}" onClick="{{m.pick}}">{{m.label}}</button></sc-for>
        </div>
        <div class="v-brc-grid" aria-live="polite">
          <div class="v-pt" style="background:#6E231D;color:#EEC453"><i>Method</i><div class="v-pt-rep"><span>{{brew.method}}</span><span>{{brew.method}}</span><span>{{brew.method}}</span></div></div>
          <div class="v-pt" style="background:#F5EEE8;color:#B03A2B;box-shadow:inset 0 0 0 2px #E9BFAE"><i>Coffee</i><b>{{brew.dose}}<small> g</small></b></div>
          <div class="v-pt" style="background:#E9BFAE;color:#6E231D"><i>{{brew.waterLabel}}</i><b>{{brew.water}}<small> g</small></b></div>
          <div class="v-pt" style="background:#DE5F2E;color:#F5EEE8"><i>Time</i><em>{{brew.time}}</em></div>
          <div class="v-pt" style="background:#F2D58A;color:#6E231D"><i>Grind</i><em>{{brew.grind}}</em></div>
          <div class="v-pt" style="background:#F0B79A;color:#6E231D"><i>Water temp</i><b>{{brew.temp}}</b></div>
          <div class="v-pt" style="background:#D9C7D8;color:#6E231D"><i>{{brew.unitPlural}}</i><b>{{brew.cups}}</b></div>
          <div class="v-pt" style="background:#EEC453;color:#6E231D;box-shadow:inset 0 0 0 2px #6E231D"><i>Ratio</i><b>1:{{brew.ratio}}</b></div>
          <div class="v-pt v-pt-tip" style="background:#B03A2B;color:#F5EEE8"><i>Tip</i><span>✦ {{brew.tip}}</span></div>
        </div>
      </div>
    </div>
  </section>""")
css+="""
.v-br{max-width:1312px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,600px);gap:64px;align-items:start}
.v-br-l{display:grid;gap:26px;justify-items:start;padding-top:24px}
.v-br-h{margin:0;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(48px,6vw,92px);line-height:.92;color:#6E231D}
.v-br-h span{color:#B03A2B}
.v-br-p{margin:0;max-width:340px;font-size:16px;line-height:1.7}
.v-brc{position:relative;background:#F5EEE8;color:#3A1410;border-radius:34px;padding:28px 28px 26px;box-shadow:0 30px 60px rgba(110,35,29,.3);margin-top:150px}
.v-brj{position:absolute;right:-40px;top:-246px;width:196px;height:auto;transform:rotate(9deg);pointer-events:none;filter:drop-shadow(0 26px 22px rgba(58,20,16,.38));z-index:3}
.v-brc-top{display:flex;justify-content:space-between;align-items:center;font-size:20px}
.v-brc-top b{font-weight:700;letter-spacing:.01em}.v-brc-top span{color:#B03A2B;font-size:22px;margin-right:140px}
.v-brc-pro{display:flex;align-items:center;gap:22px;margin-top:20px}
.v-brc-av{flex:none;width:92px;height:92px;border-radius:50%;background:#B03A2B;color:#F5EEE8;display:grid;place-items:center;font-family:'Titan One',sans-serif;font-size:46px;box-shadow:0 0 0 4px #F5EEE8,0 0 0 7px #E9BFAE}
.v-brc-st{display:flex;gap:26px}
.v-brc-st div{display:grid;justify-items:center;line-height:1.1}
.v-brc-st b{font-family:'Titan One',sans-serif;font-weight:400;font-size:28px;color:#6E231D}
.v-brc-st small{font-size:12px;color:#7A5A50;margin-top:3px}
.v-brc-bio{margin:16px 0 0;font-size:14px;line-height:1.55}
.v-brc-bio span{font-weight:700;color:#B03A2B}
.v-brc-step{display:inline-flex;align-items:center;gap:8px;margin-top:14px;padding:5px 16px 5px 5px;border-radius:999px;background:#E9BFAE}
.v-brc-step button{width:40px;height:40px;border-radius:50%;border:0;background:#F5EEE8;color:#6E231D;font:400 22px 'Titan One',sans-serif}
.v-brc-step button:last-of-type{background:#B03A2B;color:#F5EEE8}
.v-brc-step output{min-width:30px;text-align:center;font:400 28px 'Titan One',sans-serif;color:#6E231D}
.v-brc-step span{font-size:13px;font-weight:700;color:#6E231D}
.v-brc-tabs{display:flex;margin-top:18px;border-bottom:1px solid rgba(58,20,16,.18)}
.v-brc-tabs button{flex:1;padding:12px 2px 11px;border:0;border-bottom:3px solid transparent;background:none;color:#7A5A50;font:400 14px 'Titan One',sans-serif;text-transform:uppercase;margin-bottom:-1px;transition:color .2s,border-color .2s}
.v-brc-tabs button[aria-pressed=true]{color:#6E231D;border-bottom-color:#6E231D}
.v-brc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin-top:6px}
.v-pt{position:relative;aspect-ratio:1/1;border-radius:6px;padding:12px;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;min-width:0}
.v-pt i{font-style:normal;font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;opacity:.85}
.v-pt b{font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(34px,4.6vw,56px);line-height:.9}
.v-pt b small{font-size:.4em}
.v-pt em{font-style:normal;font-family:'Mouse Memoirs',sans-serif;text-transform:uppercase;font-size:clamp(24px,3vw,34px);line-height:1}
.v-pt-rep{display:grid;font-family:'Titan One',sans-serif;text-transform:uppercase;font-size:clamp(20px,2.6vw,30px);line-height:.86;overflow:hidden;word-break:break-word}
.v-pt-rep span:nth-child(2){opacity:.65}.v-pt-rep span:nth-child(3){opacity:.3}
.v-pt-tip span{font-size:12px;line-height:1.35;font-weight:700}
@media (max-width:900px){.v-br{grid-template-columns:1fr;gap:28px}.v-br-l{padding-top:0}.v-brc{margin-top:170px;padding:20px 16px 18px}.v-brj{width:140px;right:10px;top:-182px}.v-brc-top span{margin-right:110px}.v-brc-av{width:72px;height:72px;font-size:36px}.v-brc-st{gap:16px}.v-brc-st b{font-size:22px}.v-brc-tabs button{font-size:11px}.v-pt{padding:9px}.v-pt i{font-size:8px;letter-spacing:.12em}.v-pt-tip span{font-size:10px}.v-pt-rep{font-size:18px}}
"""
def sub(a,b):
    global script
    assert script.count(a)==1,a[:70]
    script=script.replace(a,b)
sub("cups: cups, unitPlural: M.units, waterLabel: M.waterLabel,","cups: cups, unitPlural: M.units, waterLabel: M.waterLabel, method: M.label, ratio: String(Math.round(M.water / M.dose * 10) / 10),")


# neutral brew tips (no blend names)
for old,new in [("Velours shines here. Pull it short and taste before adding milk.","Pull it short and taste before adding milk."),
                ("Aurore wants a slow, even pour. Let it bloom for thirty seconds first.","Pour slowly and evenly. Let it bloom for thirty seconds first."),
                ("Nuit turns heavy and chocolatey. Press gently, then pour it all at once.","Press gently, then pour it all at once."),
                ("Velours makes a silky cold brew. Steep it in the fridge overnight.","Steep in the fridge overnight, then dilute to taste.")]:
    assert script.count(old)==1,old
    script=script.replace(old,new)


# ===== v2: Heist-inspired information presentation (facts strip, method comparison, blend guide, FAQ, mono labels) =====
def _before(marker, block):
    global markup
    assert markup.count(marker)==1, marker
    markup=markup.replace(marker, block+marker)
facts = """<section class="v-facts" aria-label="At a glance">
    <div class="v-facts-in">
      <div><b>03</b><span>blends</span></div><div><b>01</b><span>gift box</span></div><div><b>04</b><span>brew methods</span></div><div><b>00</b><span>rush</span></div>
    </div>
    <div class="v-tick" aria-hidden="true"><div class="v-tick-in"><span>SMALL LOTS ✦ ROASTED TO ORDER ✦ HAND-SEALED ✦ WHOLE BEAN ✦ SMALL LOTS ✦ ROASTED TO ORDER ✦ HAND-SEALED ✦ WHOLE BEAN ✦&nbsp;</span><span>SMALL LOTS ✦ ROASTED TO ORDER ✦ HAND-SEALED ✦ WHOLE BEAN ✦ SMALL LOTS ✦ ROASTED TO ORDER ✦ HAND-SEALED ✦ WHOLE BEAN ✦&nbsp;</span></div></div>
  </section>
  """
_before('<section class="v-sec" id="shop"', facts)
cmp_html = """
    <div class="v-cmp" aria-labelledby="cmp-title">
      <h3 id="cmp-title" class="v-cmp-h">Four ways to brew, side by side</h3>
      <div class="v-cmp-g" role="table">
        <div class="v-cmp-r v-cmp-hd" role="row"><span>Method</span><span>Coffee</span><span>Water</span><span>Time</span><span>Grind</span><span>Water temp</span></div>
        <sc-for list="{{compare}}" as="c" hint-placeholder-count="4"><div class="v-cmp-r{{c.on}}" role="row"><b>{{c.label}}</b><span>{{c.dose}} g</span><span>{{c.water}} g</span><span>{{c.time}}</span><span>{{c.grind}}</span><span>{{c.temp}}</span></div></sc-for>
      </div>
      <p class="v-cmp-n">Amounts follow the cup counter above.</p>
    </div>
  """
bi=markup.index('<section class="v-sec" id="brew"'); be=markup.index('</section>',bi)
markup=markup[:be]+cmp_html+markup[be:]
know = """<section class="v-know" aria-labelledby="know-title">
    <div class="v-know-in">
      <span class="v-know-eb">Good to know</span>
      <h2 id="know-title" class="v-know-h">Which tin is yours?</h2>
      <div class="v-blt" role="table" aria-label="Compare the blends">
        <div class="v-blt-r v-blt-hd" role="row"><span>Tin</span><span>Roast</span><span>Tasting notes</span><span>Best for</span><span>Price</span></div>
        <div class="v-blt-r" role="row"><b>Nuit</b><span>Dark</span><span>Cocoa nib, molasses, cedar</span><span>After dinner, slow conversation</span><span>$24</span></div>
        <div class="v-blt-r" role="row"><b>Velours</b><span>Medium-dark</span><span>Hazelnut, dark cherry, brown sugar</span><span>Milk drinks and short espresso</span><span>$24</span></div>
        <div class="v-blt-r" role="row"><b>Aurore</b><span>Light</span><span>Jasmine, bergamot, apricot</span><span>Pour-over in the early light</span><span>$28</span></div>
        <div class="v-blt-r" role="row"><b>Le Coffret</b><span>All three</span><span>One of each blend</span><span>Gifts, and trying everything</span><span>$68</span></div>
      </div>
      <div class="v-faq">
        <details open><summary>Which tin should I start with?</summary><p>Choose Nuit for dark and slow, Velours for milk drinks and espresso, and Aurore for bright pour-overs. Le Coffret has all three.</p></details>
        <details><summary>How do I brew it?</summary><p>Use the Brew Bar above. Pick a method and a number of cups, and it gives you the coffee, water, time, grind and temperature.</p></details>
        <details><summary>What does “roasted to order” mean?</summary><p>Every tin is roasted after you order it, then sealed by hand.</p></details>
        <details><summary>Is Le Coffret a gift?</summary><p>Yes. It holds one of each blend in a gift box, tied by hand.</p></details>
        <details><summary>Are these real prices?</summary><p>No. This is a concept storefront with sample prices, and the checkout is a demo that takes no payment.</p></details>
      </div>
    </div>
  </section>
  """
_before('<section class="v-sec v-close"', know)
css+="""
.v-facts{background:#3A1410;color:#F5EEE8;overflow:hidden}
.v-facts-in{max-width:1312px;margin:0 auto;padding:72px 64px 56px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.v-facts-in div{display:grid;gap:10px;padding:0 24px;border-left:1px solid rgba(245,238,232,.18)}
.v-facts-in div:first-child{border-left:0;padding-left:0}
.v-facts-in b{font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(56px,7vw,104px);line-height:.9;color:#EEC453}
.v-facts-in span{font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:#E9BFAE}
.v-tick{border-top:1px solid rgba(245,238,232,.18);overflow:hidden;white-space:nowrap;padding:16px 0}
.v-tick-in{display:inline-flex;animation:vTk 70s linear infinite}
.v-tick-in span{font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.2em;color:#F5EEE8;opacity:.8;padding-right:0}
@keyframes vTk{to{transform:translateX(-50%)}}
.v-cmp{max-width:1312px;margin:90px auto 0}
.v-cmp-h{margin:0 0 20px;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(30px,3.6vw,48px);line-height:1;color:#6E231D;text-transform:uppercase}
.v-cmp-g{border-radius:22px;overflow:hidden;background:#F5EEE8}
.v-cmp-r{display:grid;grid-template-columns:1.3fr repeat(5,1fr);gap:12px;padding:18px 26px;align-items:center;border-top:1px solid rgba(110,35,29,.14);font-size:15px;color:#3A1410;transition:background-color .25s}
.v-cmp-r b{font-family:'Titan One',sans-serif;font-weight:400;font-size:18px;text-transform:uppercase;color:#6E231D}
.v-cmp-hd{border-top:0;background:#6E231D;color:#EEC453;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding-block:14px}
.v-cmp-r.on{background:#F2D58A}
.v-cmp-n{margin:12px 0 0;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.08em;color:#6E231D}
.v-know{background:#F5EEE8;padding:120px 64px}
.v-know-in{max-width:1312px;margin:0 auto}
.v-know-eb{font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#B03A2B}
.v-know-h{margin:14px 0 36px;font-family:'Titan One',sans-serif;font-weight:400;font-size:clamp(44px,6vw,88px);line-height:.92;color:#3A1410;text-transform:uppercase}
.v-blt{border-top:2px solid #3A1410}
.v-blt-r{display:grid;grid-template-columns:1fr .9fr 1.6fr 1.6fr .6fr;gap:16px;padding:20px 4px;border-bottom:1px solid rgba(58,20,16,.2);align-items:baseline;font-size:15px}
.v-blt-r b{font-family:'Titan One',sans-serif;font-weight:400;font-size:24px;text-transform:uppercase;color:#6E231D}
.v-blt-r span:last-child{font-family:'Titan One',sans-serif;font-size:22px;color:#B03A2B;text-align:right}
.v-blt-hd{padding-block:12px;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#7A5A50}
.v-blt-hd span:last-child{font-family:'DM Mono',monospace;font-size:12px;color:#7A5A50}
.v-faq{margin-top:72px;border-top:2px solid #3A1410}
.v-faq details{border-bottom:1px solid rgba(58,20,16,.2)}
.v-faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:24px 4px;font-family:'Titan One',sans-serif;font-size:clamp(20px,2.2vw,28px);color:#3A1410}
.v-faq summary::-webkit-details-marker{display:none}
.v-faq summary::after{content:"+";flex:none;width:40px;height:40px;border-radius:50%;background:#6E231D;color:#F5EEE8;display:grid;place-items:center;font:400 22px/1 'Titan One',sans-serif;transition:transform .3s}
.v-faq details[open] summary::after{transform:rotate(45deg)}
.v-faq summary:focus-visible{outline:3px solid #2F5FA8;outline-offset:2px}
.v-faq p{margin:0 0 26px;max-width:62ch;font-size:16px;line-height:1.7;color:#3A1410}
.v-pt i,.v-brc-st small,.v-pe,.v-poster small{font-family:'DM Mono',monospace!important}
@media (max-width:900px){.v-facts-in{grid-template-columns:repeat(2,minmax(0,1fr));gap:34px 0;padding:56px 20px 40px}.v-facts-in div:nth-child(3){border-left:0;padding-left:0}.v-cmp{margin-top:56px}.v-cmp-r{grid-template-columns:1fr 1fr;gap:6px 12px;padding:14px 16px}.v-cmp-r b{grid-column:1/-1}.v-cmp-hd{display:none}.v-know{padding:80px 20px}.v-blt-hd{display:none}.v-blt-r{grid-template-columns:1fr 1fr;gap:6px 12px}.v-blt-r b{grid-column:1/-1}.v-blt-r span:last-child{text-align:left}}
@media (prefers-reduced-motion:reduce){.v-tick-in{animation:none}}
"""
b="      bagCount: count,"
assert script.count(b)==1
script=script.replace(b,"      compare: METHODS.map(function (m, i) { var c = Math.min(st.cups, m.max); return { label: m.label, on: i === st.method ? ' on' : '', dose: m.dose * c, water: m.water * c, time: m.time, grind: m.grind, temp: m.temp }; }),\n"+b)

shim=r"""
class DCLogic{constructor(p){this.props=p||{}}setState(s){Object.assign(this.state,s);if(this._r)this._r()}}
(function(){
var H=[];
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function parse(src){
  var re=/<(\/?)sc-(for|if)\b([^>]*)>/g,root={k:[]},stack=[root],last=0,m;
  while((m=re.exec(src))){
    if(m.index>last)stack[stack.length-1].k.push({t:'text',s:src.slice(last,m.index)});
    last=re.lastIndex;
    if(m[1]){stack.pop();continue}
    var a=m[3],n={t:m[2],k:[]};
    var pm=/(?:list|value)="\{\{\s*([^}]+?)\s*\}\}"/.exec(a);n.path=pm?pm[1]:'';
    var am=/\bas="([^"]+)"/.exec(a);n.as=am?am[1]:'item';
    stack[stack.length-1].k.push(n);stack.push(n);
  }
  if(last<src.length)root.k.push({t:'text',s:src.slice(last)});
  return root;
}
function get(path,sc){
  var p=path.split('.'),v;
  for(var i=sc.length-1;i>=0;i--){if(sc[i]&&Object.prototype.hasOwnProperty.call(sc[i],p[0])){v=sc[i][p[0]];break}}
  for(var j=1;j<p.length&&v!=null;j++)v=v[p[j]];
  return v;
}
function out(nodes,sc){
  var h='';
  nodes.forEach(function(n){
    if(n.t==='text'){
      h+=n.s.replace(/\bon(Click|Change)="\{\{\s*([^}]+?)\s*\}\}"/g,function(m,ev,path){
        var f=get(path,sc);if(typeof f!=='function')return '';
        H.push(f);return 'data-on-'+ev.toLowerCase()+'="'+(H.length-1)+'"';
      }).replace(/\{\{\s*([^}]+?)\s*\}\}/g,function(m,path){var v=get(path,sc);return v==null?'':esc(v)});
    }else if(n.t==='if'){
      if(get(n.path,sc))h+=out(n.k,sc);
    }else{
      var list=get(n.path,sc)||[];
      list.forEach(function(it){var o={};o[n.as]=it;h+=out(n.k,sc.concat([o]))});
    }
  });
  return h;
}
function morph(a,b){
  var ca=a.childNodes,cb=b.childNodes,i;
  for(i=0;i<cb.length;i++){
    var x=ca[i],y=cb[i];
    if(!x){a.appendChild(y.cloneNode(true));continue}
    if(x.nodeType!==y.nodeType||x.nodeName!==y.nodeName){a.replaceChild(y.cloneNode(true),x);continue}
    if(x.nodeType!==1){if(x.nodeValue!==y.nodeValue)x.nodeValue=y.nodeValue;continue}
    var at=y.attributes,j;
    for(j=0;j<at.length;j++){if(x.getAttribute(at[j].name)!==at[j].value)x.setAttribute(at[j].name,at[j].value)}
    var xa=Array.prototype.slice.call(x.attributes);
    for(j=0;j<xa.length;j++){if(!y.hasAttribute(xa[j].name))x.removeAttribute(xa[j].name)}
    morph(x,y);
  }
  while(ca.length>cb.length)a.removeChild(a.lastChild);
}
var app=document.getElementById('app'),tree=parse(document.getElementById('dc-tpl').textContent),inst=null,mounted=false;
function render(){
  H=[];
  var html=out(tree.k,[inst.renderVals()]),tmp=document.createElement('div');
  tmp.innerHTML=html;
  if(!mounted){app.innerHTML=html;mounted=true}else morph(app,tmp);
}
function fire(attr,e){
  var el=e.target.closest&&e.target.closest('['+attr+']');
  if(el){var f=H[+el.getAttribute(attr)];if(f)f(e)}
}
document.addEventListener('click',function(e){fire('data-on-click',e)});
document.addEventListener('change',function(e){fire('data-on-change',e)});
document.addEventListener('keydown',function(e){
  if((e.key==='Enter'||e.key===' ')&&e.target.matches&&e.target.matches('[role="button"][data-on-click]')){e.preventDefault();fire('data-on-click',e);return}
  if(e.key==='Escape'&&inst&&(inst.state.detail||inst.state.bagOpen))inst.setState({detail:null,bagOpen:false,ordered:false});
});
window.__bootValden=function(C){
  inst=new C({});
  inst._r=function(){render();if(inst.componentDidUpdate)inst.componentDidUpdate()};
  render();
  if(inst.componentDidMount)inst.componentDidMount();
};
})();
"""
out=f'''<title>Valden Coffee</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titan+One&family=Mouse+Memoirs&family=DM+Sans:opsz,wght@9..40,400..700&family=DM+Mono:wght@400;500&display=swap">
<style>
{css}
{mobile}
</style>
<div id="app"></div>
<script type="text/x-template" id="dc-tpl">
{markup}
</script>
<script>
{shim}
{script}
window.__bootValden(Component);
</script>
'''
open(S+"/experiments/valden-v2/out.html","w").write(out)
print(len(out))
