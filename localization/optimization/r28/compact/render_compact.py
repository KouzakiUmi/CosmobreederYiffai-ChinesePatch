"""Actual final arq positions + exact archive atlas alpha, no font substitute.
CPU/synthetic/no GPU/CRT. Also proves text excludes conservative FULL16x16 icon
rectangles at all original42 coordinates, stronger than a particular icon mask.
"""
import sys,io,json,hashlib,zipfile,argparse
from pathlib import Path
from PIL import Image,ImageDraw,__version__
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
DEFAULT_OUT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('candidate_jar',type=Path,nargs='?',default=ROOT/'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar')
parser.add_argument('--output-dir',type=Path,default=DEFAULT_OUT)
args=parser.parse_args()
OUT=args.output_dir.resolve(strict=True)
r28=(ROOT/'localization/optimization/r28').resolve(strict=True)
tests=r28/'integration/tests'
relative=OUT.relative_to(tests) if OUT.is_relative_to(tests) else None
if not OUT.is_dir() or not (OUT==r28/'compact' or (relative is not None and len(relative.parts)==2 and relative.name=='compact')):
    parser.error('output must be pre-existing r28/compact or r28/integration/tests/<run>/compact')
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file
from projectlib import parse_atlas
rec=json.loads((OUT/'cpu-recording.json').read_text('utf8'))
jar=args.candidate_jar.resolve(strict=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(jar.read_bytes())==rec['jar_sha256']
assert rec['forbidden_attempts']==[]
with zipfile.ZipFile(jar) as z:
    index=json.loads(decrypt_file(z.read('dataq/0')))
    atlas=decrypt_file(z.read('dataq/'+str(index['/sprites.atlas'])))
    page_bytes=decrypt_file(z.read('dataq/'+str(index['/sprites.png'])))
    _,regions=parse_atlas(atlas.decode('utf8'))
    page=Image.open(io.BytesIO(page_bytes)).convert('RGBA')
    for role,entry in [('default','bbc2.fnt'),('classic','classic.fnt')]:
        assert sha(z.read(entry))==rec['fonts'][role]['sha256']
assets={}
needed={'bbc2','classic'}|{c['name'] for s in rec['scenarios'] for c in s['calls'] if c['kind'] in ('image','rect')}
for name in needed:
    r=next(r for r in regions if r['name']==name)
    assert r['rotation']==0
    x,y=r['xy'];w,h=r['size'];ow,oh=r['orig'];ox,oy=r['offset']
    im=Image.new('RGBA',(ow,oh));im.alpha_composite(page.crop((x,y,x+w,y+h)),(ox,oh-oy-h));assets[name]=im
fontpages={'default':assets['bbc2'],'classic':assets['classic']}
def mask(im,x,y):
    return {(x+u,y+v) for v in range(im.height) for u in range(im.width) if im.getpixel((u,v))[3]}
def bounds(points):
    return [min(x for x,y in points),min(y for x,y in points),max(x for x,y in points)+1,max(y for x,y in points)+1] if points else None
recorded_icons=[c for s in rec['scenarios'] if s['id']=='item-selector-0' for c in s['calls'] if c.get('name')=='IconEmpty']
assert len(recorded_icons)==42
full_icon_bounds={(a,b) for c in recorded_icons for a in range(c['x'],c['x']+16) for b in range(224-c['y']-16,224-c['y'])}
report=[];previews=[]
for scene in rec['scenarios']:
    sid=scene['id'];canvas=Image.new('RGBA',(256,224),(0,0,0,255));ink=set();overlap=set();divider=set();nonpanel=[];later=set();glyphs=[];boxes_out=[];description_escapes=[]
    icon_bounds=set(full_icon_bounds) if sid.startswith('item-name-') else set();fields={};highlight=set()
    for c in scene['calls']:
        if c['kind'] in ('image','rect'):
            im=assets[c['name']]
            if c['kind']=='rect':im=im.resize((c['width'],c['height']),Image.Resampling.NEAREST)
            x=c['x'];y=224-c['y']-im.height;m=mask(im,x,y)
            if c['name'].endswith('BG'):later|=ink&m
            elif c['name']=='WhiteFill':
                # Existing selection paint is intentionally below the letter.
                # A later cursor must exclude name ink. Selected-letter repaint
                # is the sole expected white-background/text intersection.
                if sid!='letter-selected':later|=ink&m
                else:highlight|=m
            else:nonpanel.append((c['name'],m))
            if c['name']=='IconEmpty':icon_bounds|={(a,b) for a in range(x,x+16) for b in range(y,y+16)}
            if c['name']=='CosmoItemMenuBG':
                divider|={(127,v) for v in range(y,y+192)}|{(128,v) for v in range(y,y+192)}|{(u,v) for u in range(128,252) for v in [y+161,y+162]}
            canvas.alpha_composite(im,(x,y));continue
        role=c['font']
        for q in c['quads']:
            x,y,w,h=map(int,[q['x'],q['screenTop'],q['width'],q['height']])
            assert [x+w,y+h]==[q['right'],q['screenBottom']]
            sx,sy=q['srcX'],q['srcY'];g=fontpages[role].crop((sx,sy,sx+w,sy+h))
            if 'color_rgba' in c:
                color=c['color_rgba'];g.putdata([tuple(round(pixel[i]*color[i]) for i in range(4)) for pixel in g.getdata()])
            m=mask(g,x,y)
            overlap|=ink&m;ink|=m
            if x<0 or y<0 or x+w>256 or y+h>224:boxes_out.append([x,y,x+w,y+h])
            # Conservative real description interior; evaluate actual INK, not
            # transparent Latin quad padding against the 122x26 inner rectangle.
            isdesc=sid.startswith('item-') and not sid.startswith(('item-selector-','item-name-'))
            if isdesc:
                outside={(a,b) for a,b in m if not(130<=a<252 and 196<=b<222)}
                if outside:description_escapes.append({'char':chr(q['codepoint']),'bounds':bounds(outside)})
            fields.setdefault(str(c['x'])+','+str(c['y']),set()).update(m)
            glyphs.append({'char':chr(q['codepoint']),'role':role,'box':[x,y,x+w,y+h],'ink_bounds':bounds(m),'actual_advance':q['arr_advance']})
            canvas.alpha_composite(g,(x,y))
    intersections=[{'name':n,'ink_pixels':len(ink&m)} for n,m in nonpanel if n!='IconEmpty']
    r={'id':sid,'glyphs':len(glyphs),'ink_overlap_unique_pixels':len(overlap),'divider_ink_pixels':len(ink&divider),'conservative_full16_icon_overlap_pixels':len(ink&icon_bounds),'later_panel_or_cursor_occlusion_pixels':len(later),'text_vs_actual_nonpanel_images':intersections,'description_ink_escapes':description_escapes,'canvas_quad_clips':boxes_out,'ink_bounds':bounds(ink),'field_bounds':{k:bounds(v) for k,v in fields.items()}}
    report.append(r)
    if sid in {'save-three-slots','name-8-cjk','name-7-cjk','letter-selected','item-selector-0','item-selector-21','item-selector-35','item-corpus-PAK-SpecialGeiger','item-corpus-JAR-SpecialGeiger','item-overheight-page-0'}:
        path=OUT/(sid+'.png');canvas.save(path);large=canvas.resize((1024,896),Image.Resampling.NEAREST);large.save(OUT/(sid+'-4x.png'));previews.append((sid,canvas))
summary={'scenarios':len(report),'vertices':rec['vertices'],'ink_overlap':sum(r['ink_overlap_unique_pixels'] for r in report),'divider_ink':sum(r['divider_ink_pixels'] for r in report),'full16_icon_overlap':sum(r['conservative_full16_icon_overlap_pixels'] for r in report),'later_occlusion':sum(r['later_panel_or_cursor_occlusion_pixels'] for r in report),'actual_nonpanel_ink':sum(i['ink_pixels'] for r in report for i in r['text_vs_actual_nonpanel_images']),'description_escapes':sum(len(r['description_ink_escapes']) for r in report),'canvas_clips':sum(len(r['canvas_quad_clips']) for r in report)}
output={'status':'ACTUAL_FINAL_CLASS_CPU_RAW_ATLAS_NOT_GAME_OR_CRT','pillow':__version__,'recording_sha256':sha((OUT/'cpu-recording.json').read_bytes()),'jar_sha256':rec['jar_sha256'],'overlay_sha256':rec['overlay_sha256'],'atlas_sha256':sha(atlas),'atlas_page_sha256':sha(page_bytes),'summary':summary,'results':report,'limitations':rec['fixture_limits']}
(OUT/'render-report.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
plate=Image.new('RGB',(768,((len(previews)+2)//3)*246),(20,20,20));d=ImageDraw.Draw(plate)
for i,(sid,im) in enumerate(previews):x=(i%3)*256;y=(i//3)*246;d.text((x+3,y+3),'CPU / SYNTHETIC / NO CRT',fill='white');plate.paste(im,(x,y+22))
plate.save(OUT/'compact-contact-sheet.png')
print(json.dumps(summary,indent=2))
assert all(v==0 for k,v in summary.items() if k not in ('scenarios','vertices')), 'actual ink/panel geometry failed; see render-report.json'
