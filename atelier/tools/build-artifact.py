# Build the linked artifact: home as the main page, home.html + course.html + lesson.html as extra pages.
import re, io, base64
from PIL import Image
root='/home/user/web-portfolio/atelier/'
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
    return s.replace('</head>\n<body>','').replace('</body>\n</html>','')
home=open(root+'atelier-v7.html').read()
course=open(root+'course.html').read()
lesson=open(root+'lesson.html').read()
# course page links back to the home page file
course=course.replace('atelier-v7.html','home.html')
home_e=embed(home); course_e=embed(course)
open('site/home.html','w').write(home_e)            # full document, served as its own page
open('site/course.html','w').write(course_e)        # full document
open('site/lesson.html','w').write(embed(lesson))   # full document
open('atelier-v7.html','w').write(strip_doc(home_e)) # main artifact page
print({k:len(open(p).read())//1024 for k,p in [('main','atelier-v7.html'),('home','site/home.html'),('course','site/course.html'),('lesson','site/lesson.html')]}, 'KB')
