import re, requests, math
from io import BytesIO
from PIL import Image, ImageOps, ImageDraw
BASE='https://3000-iicqewgfjmadk0d0cw2e4-5e046170.us2.manus.computer'
text=open('generate_service_pages.py').read()
entries=[]
current_slug=None
current_title=None
for line in text.splitlines():
    m=re.search(r"'slug': '([^']+)'", line)
    if m: current_slug=m.group(1)
    m=re.search(r"'title': '([^']+)'", line)
    if m and current_slug: current_title=m.group(1)
    m=re.search(r"'([A-Za-z]+)': \{'note': .*'image': '([^']+)'\},?$", line)
    if m and current_slug and current_title and ' | E4 Power' not in current_title:
        entries.append((current_title, m.group(1), m.group(2)))
# focus on non-user-uploaded remaining stock-like services only
focus={'Readiness Assessments','Intellectual Property','IT Solutions','Grant Management','Project Management','Financial Management','Institutional Discovery','Advisory Alignment'}
entries=[e for e in entries if e[0] in focus]
thumbs=[]
for title,pillar,img_path in entries:
    data=requests.get(BASE+img_path, timeout=30).content
    img=Image.open(BytesIO(data)).convert('RGB').resize((220,120))
    canvas=Image.new('RGB',(220,160),'white')
    canvas.paste(img,(0,0))
    d=ImageDraw.Draw(canvas)
    d.text((6,126), f'{title[:18]}', fill='black')
    d.text((6,142), pillar, fill='black')
    thumbs.append(canvas)
cols=4
rows=math.ceil(len(thumbs)/cols)
out=Image.new('RGB',(cols*230+10,(rows*170)+10),(245,245,245))
for i,img in enumerate(thumbs):
    x=10+(i%cols)*230
    y=10+(i//cols)*170
    out.paste(img,(x,y))
out.save('.manus-notes/quality-audit/service-stock-contact-sheet.jpg', quality=90)
print('saved', len(thumbs))
