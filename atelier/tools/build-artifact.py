# Build the linked artifact: home as the main page, every other page as an extra file.
# Run from a scratch folder (it writes ./atelier-v7.html and ./site/*); it reads from atelier/.
#   python3 /home/user/web-portfolio/atelier/tools/build-artifact.py
# Publish: main file ./atelier-v7.html; files = site/<page>.html and site/assets/* at their names.
import re, io, base64, os, shutil
from PIL import Image
root='/home/user/web-portfolio/atelier/'
PAGES=['course.html','lesson.html','style.html']   # extra pages besides home
cache={}
def embed(s):
    def rep(m):
        p=m.group(0)
        if p not in cache:
            im=Image.open(root+p).convert('RGB')
            if im.width>1400: im=im.resize((1400, round(im.height*1400/im.width)))
            b=io.BytesIO(); im.save(b,'JPEG',quality=72,optimize=True,progressive=True)
            cache[p]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
        return cache[p]
    return re.sub(r'img/[0-9a-f-]+-w\d+\.jpg', rep, s)
def strip_doc(s):
    s=re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*','',s,flags=re.I)
    s=s.replace('<meta charset="utf-8">\n','').replace('<meta name="viewport" content="width=device-width, initial-scale=1">\n','')
    return s.replace('</head>\n<body','<body').replace('</body>\n</html>','')
os.makedirs('site/assets',exist_ok=True)
home_e=embed(open(root+'atelier-v7.html').read())
open('site/home.html','w').write(home_e)             # full document, served as its own page
open('atelier-v7.html','w').write(strip_doc(home_e)) # main artifact page
sizes={'main':len(home_e)//1024}
for page in PAGES:
    s=open(root+page).read().replace('atelier-v7.html','home.html')   # pages link back to the home file
    open('site/'+page,'w').write(embed(s)); sizes[page]=os.path.getsize('site/'+page)//1024
for f in os.listdir(root+'assets'):
    shutil.copy(root+'assets/'+f,'site/assets/'+f); sizes['assets/'+f]=os.path.getsize('site/assets/'+f)//1024
print(sizes,'KB')
