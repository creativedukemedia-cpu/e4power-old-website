import os, re, math, json
from collections import defaultdict
from io import BytesIO
import requests
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
    if m and current_slug:
        pillar=m.group(1)
        image=m.group(2)
        if current_title and ' | E4 Power' not in current_title:
            entries.append({'slug': current_slug, 'title': current_title, 'pillar': pillar, 'image': image})

sess=requests.Session()

def ahash(img, size=16):
    gray=img.convert('L').resize((size,size))
    px=list(gray.getdata())
    avg=sum(px)/len(px)
    return ''.join('1' if p>avg else '0' for p in px)

def dhash(img, size=16):
    gray=img.convert('L').resize((size+1,size))
    out=[]
    for y in range(size):
        row=[gray.getpixel((x,y)) for x in range(size+1)]
        out.extend('1' if row[x]>row[x+1] else '0' for x in range(size))
    return ''.join(out)

def hist_feat(img, bins=8):
    small=img.convert('RGB').resize((64,64))
    hist=small.histogram()
    # 256 bins each channel -> compress to bins
    comp=[]
    for ch in range(3):
        channel=hist[ch*256:(ch+1)*256]
        step=256//bins
        vals=[sum(channel[i*step:(i+1)*step]) for i in range(bins)]
        s=sum(vals) or 1
        comp.extend(v/s for v in vals)
    return comp

def bitdist(a,b):
    return sum(c1!=c2 for c1,c2 in zip(a,b))

def cosdist(a,b):
    dot=sum(x*y for x,y in zip(a,b))
    na=math.sqrt(sum(x*x for x in a)) or 1
    nb=math.sqrt(sum(y*y for y in b)) or 1
    return 1 - dot/(na*nb)

cache={}
for e in entries:
    img_path=e['image']
    if img_path not in cache:
        r=sess.get(BASE+img_path, timeout=30)
        r.raise_for_status()
        img=Image.open(BytesIO(r.content)).convert('RGB')
        cache[img_path]={
            'ahash': ahash(img),
            'dhash': dhash(img),
            'hist': hist_feat(img),
            'size': img.size,
            'bytes': len(r.content),
        }
    e.update(cache[img_path])

pairs=[]
for i in range(len(entries)):
    for j in range(i+1,len(entries)):
        a,b=entries[i],entries[j]
        ad=bitdist(a['ahash'], b['ahash'])
        dd=bitdist(a['dhash'], b['dhash'])
        hd=cosdist(a['hist'], b['hist'])
        # Lower = more similar. Weighted score.
        score=ad/256*0.35 + dd/256*0.45 + hd*0.20
        pairs.append({
            'score': round(score, 4),
            'ahash_dist': ad,
            'dhash_dist': dd,
            'hist_dist': round(hd,4),
            'a': f"{a['title']} | {a['pillar']}",
            'b': f"{b['title']} | {b['pillar']}",
            'a_image': a['image'],
            'b_image': b['image'],
        })

pairs.sort(key=lambda x: x['score'])
out={'count': len(entries), 'top_pairs': pairs[:40]}
open('.manus-notes/catalog-audit/similar_pairs.json','w').write(json.dumps(out, indent=2))
print('entries', len(entries))
for p in pairs[:20]:
    print(p['score'], '|', p['a'], '<->', p['b'], '|', p['a_image'], '|', p['b_image'])
