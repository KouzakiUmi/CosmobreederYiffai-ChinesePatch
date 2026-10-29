"""Generate enlarged source/candidate text comparisons, never redraw assets."""
from pathlib import Path
import json
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
BASE=ROOT/'docs/font-layout-audit-20261025/image-workorders'
m=json.loads((OUT/'manifest.json').read_text(encoding='utf8'))
seen=set();items=[]
for row in m['replacements']:
    before=Image.open(BASE/row['source_preview']).convert('RGBA')
    after=Image.open(ROOT/row['newPNG']).convert('RGBA')
    for op in row['operations']:
        key=(op['english'],op['zh'],op['font_px'],tuple(op.get('foreground',[])))
        if key in seen:continue
        seen.add(key)
        box=op['slot']
        items.append((row['workorder_id'],op['english'],op['zh'],op['font_px'],before.crop(box),after.crop(box)))
for start in range(0,len(items),8):
    batch=items[start:start+8]
    sheet=Image.new('RGB',(1500,8*110),(64,64,64));d=ImageDraw.Draw(sheet)
    for i,(wid,english,zh,size,before,after) in enumerate(batch):
        y=i*110
        d.text((5,y+2),f'{wid} {english} / native {size}px',fill='white')
        for x,im in ((0,before),(750,after)):
            im=Image.alpha_composite(Image.new('RGBA',im.size,(0,0,0,255)),im).convert('RGB')
            sheet.paste(im.resize((im.width*3,im.height*3),Image.Resampling.NEAREST),(x,y+22))
    sheet.save(OUT/'review'/f'text-proof-{start//8+1}.png')
print('Exact text proof blocks',len(items),'sheets',(len(items)+7)//8)
