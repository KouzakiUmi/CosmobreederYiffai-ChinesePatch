"""Read immutable workorders; write source-review contact sheets in this staging only."""
from pathlib import Path
import json
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT/'docs/font-layout-audit-20261025/image-workorders'
OUT = Path(__file__).resolve().parent/'review'
OUT.mkdir(exist_ok=True)
w = json.loads((BASE/'workorders.json').read_text(encoding='utf8'))
rows=[]
for j in w['workorders']:
    seen=set()
    for a in j['assets']:
        for v in a['variants']:
            if v['variant'] not in ('jar','patch') or v['rgba_sha256'] in seen: continue
            seen.add(v['rgba_sha256'])
            im=Image.open(BASE/v['preview']).convert('RGBA')
            kind='title' if j['name'].startswith('ClassicTitlescreen') else 'animation' if j['workorder_id'] in ('IMG-020','IMG-021','IMG-022','IMG-026','IMG-027') else 'ui'
            if kind=='title': im=im.crop((0,65,256,224))
            elif j['name'].startswith('ClassicTileset'): im=im.crop((0,0,64,32)).resize((256,128),Image.Resampling.NEAREST)
            elif im.width<=32: im=im.resize((im.width*8,im.height*8),Image.Resampling.NEAREST)
            label=f"{j['workorder_id']} {a['name']} {a['catalog_index']} {v['variant']}"
            rows.append((kind,label,im))
for kind in ('ui','animation','title'):
    group=[r for r in rows if r[0]==kind]
    for start in range(0,len(group),12):
        batch=group[start:start+12]
        sheet=Image.new('RGB',(3*320,4*250),(70,70,70)); d=ImageDraw.Draw(sheet)
        for i,(_,label,im) in enumerate(batch):
            x=(i%3)*320;y=(i//3)*250
            d.text((x+3,y+3),label,fill='white')
            sheet.paste(Image.alpha_composite(Image.new('RGBA',im.size,(0,0,0,255)),im).convert('RGB'),(x,y+20))
        sheet.save(OUT/f'source-{kind}-{start//12+1}.png')
print('Review sheets:',len(list(OUT.glob('source-*.png'))),'unique source images',len(rows))
