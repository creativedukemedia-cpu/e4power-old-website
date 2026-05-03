import re, hashlib, requests, json
from collections import defaultdict
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
        entries.append({'title': current_title, 'pillar': m.group(1), 'image': m.group(2)})

sess=requests.Session()
cache={}
for e in entries:
    path=e['image']
    if path not in cache:
        content=sess.get(BASE+path, timeout=30).content
        cache[path]=hashlib.sha256(content).hexdigest()
    e['sha256']=cache[path]
by_hash=defaultdict(list)
for e in entries:
    by_hash[e['sha256']].append({'label': f"{e['title']} | {e['pillar']}", 'image': e['image']})
res={h:v for h,v in by_hash.items() if len(v)>1}
open('.manus-notes/catalog-audit/exact_duplicates.json','w').write(json.dumps(res, indent=2))
print('duplicate_hash_groups', len(res))
for h, group in res.items():
    print(h)
    for item in group:
        print(' ', item['label'], '|', item['image'])
