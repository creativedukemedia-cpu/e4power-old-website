import re, json, requests
from io import BytesIO
from PIL import Image
BASE='https://3000-iicqewgfjmadk0d0cw2e4-5e046170.us2.manus.computer'
text=open('generate_service_pages.py').read()
entries=[]
current_slug=None
current_title=None
for line in text.splitlines():
    m=re.search(r"'slug': '([^']+)'", line)
    if m:
        current_slug=m.group(1)
    m=re.search(r"'title': '([^']+)'", line)
    if m and current_slug:
        current_title=m.group(1)
    m=re.search(r"'([A-Za-z]+)': \{'note': .*'image': '([^']+)'\},?$", line)
    if m and current_slug and current_title and ' | E4 Power' not in current_title:
        pillar,image=m.group(1),m.group(2)
        content=requests.get(BASE+image, timeout=30).content
        img=Image.open(BytesIO(content))
        entries.append({'title':current_title,'pillar':pillar,'image':image,'width':img.width,'height':img.height,'bytes':len(content)})
open('.manus-notes/quality-audit/image_dimensions.json','w').write(json.dumps(entries, indent=2))
for e in sorted(entries, key=lambda x:(x['width']*x['height'], x['bytes']))[:20]:
    print(f"{e['width']}x{e['height']}\t{e['bytes']}\t{e['title']} | {e['pillar']}\t{e['image']}")
