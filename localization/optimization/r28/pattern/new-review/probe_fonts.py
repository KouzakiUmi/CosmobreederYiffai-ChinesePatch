"""Read-only independent r28 supplemental-font review; output only beside script."""
from pathlib import Path
from io import BytesIO
import hashlib, json, re, sys, zipfile
from collections import Counter
from PIL import Image, ImageChops
ROOT=Path(__file__).resolve().parents[5]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'localization/tools'))
import optimized_fonts as f
from codec import decrypt_file
from projectlib import parse_atlas
from layout_fonts import parse_fnt
sha=lambda b:hashlib.sha256(b).hexdigest()


def raw_cell(source,cp,size):
    block=source[cp]
    lines=block.splitlines();w,h,xo,yo=map(int,next(l for l in lines if l.startswith('BBX ')).split()[1:])
    advance=int(next(l for l in lines if l.startswith('DWIDTH ')).split()[1])
    top=(7 if size==8 else 10)-yo-h
    image=Image.new('RGBA',(size,size),(0,0,0,0));ink=0
    assert 0<=xo<=size-w and 0<=top<=size-h
    for y,line in enumerate(lines[lines.index('BITMAP')+1:lines.index('ENDCHAR')]):
        bits=bin(int(line,16))[2:].zfill(4*len(line))
        for x,bit in enumerate(bits[:w]):
            if bit=='1':image.putpixel((xo+x,top+y),(255,255,255,255));ink+=1
    return image,(w,h,xo,top,advance),ink


def main():
    jar=ROOT/'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
    pak=jar.with_name('patch.pak')
    texts=[json.loads((ROOT/'localization/optimization/r28/sfw/required_chars.json').read_text('utf8'))['characters'],
           (ROOT/'localization/optimization/r28/vsn/required_chars.txt').read_text('utf8')]
    old={};source_regions={};nested={}
    for archive in [jar,pak]:
        with zipfile.ZipFile(archive) as z:
            texts.extend(json.loads(decrypt_file(z.read('datav/1'))).values())
            route=json.loads(decrypt_file(z.read('dataq/0')))
            _,regions=parse_atlas(decrypt_file(z.read('dataq/'+str(route['/sprites.atlas']))).decode('utf8'))
            image=Image.open(BytesIO(decrypt_file(z.read('dataq/'+str(route['/sprites.png']))))).convert('RGBA')
            source_regions[archive.name]={}
            for name in ['bbc2','classic']:
                rows=[r for r in regions if r['name']==name]
                assert len(rows)==1
                r=rows[0];x,y=r['xy'];w,h=r['size']
                source_regions[archive.name][name]=image.crop((x,y,x+w,y+h))
            if archive==jar:
                old={n:z.read(n) for n in ['bbc2.fnt','classic.fnt','story12.fnt']}
                nested=json.loads(z.read('story12/story12.manifest.json'))
    assets=f.build_assets(jar,texts)
    source12zip=ROOT/'localization/work/story-font12/font12.zip'
    with zipfile.ZipFile(source12zip) as z:source12=z.read(f.SOURCE_ENTRY)
    source8=(ROOT/'work/item-font8/asset/fusion-pixel-8px-monospaced-zh_hans.bdf').read_bytes()
    source12={int(re.search(r'(?m)^ENCODING (-?\d+)$',b)[1]):b for b in source12.decode('utf8').split('STARTCHAR ')[1:]}
    source8={int(re.search(r'(?m)^ENCODING (-?\d+)$',b)[1]):b for b in source8.decode('utf8').split('STARTCHAR ')[1:]}
    report={'scope':'independent read-only actual ledger/dictionary union, no candidate build/game/GL/installer',
            'input_source_sha256':{str(ROOT/'localization/tools/optimized_fonts.py'):sha((ROOT/'localization/tools/optimized_fonts.py').read_bytes())},
            'wanted_count':len(assets['manifest']['required_codepoints']),
            'roles':{},'baseline_jar_pak_regions_identical':{name:source_regions[jar.name][name].tobytes()==source_regions[pak.name][name].tobytes() for name in ['bbc2','classic']},
            'old_story_manifest_inventory':nested['inventory']}
    new_pages={name:Image.open(BytesIO(raw)).convert('RGBA') for name,raw in assets['png_regions'].items()}
    old_bg=Counter();nonfull8=[]
    for role,spec in f.ROLES.items():
        filename,region,size,_=spec;before=parse_fnt(old[filename].decode('utf8'));after=parse_fnt(assets['fnts'][filename].decode('utf8'))
        assert before.common==after.common and before.info==after.info and before.pages==after.pages and before.kernings==after.kernings
        assert all(after.glyphs[cp]==g for cp,g in before.glyphs.items())
        original=source_regions[jar.name][region];page=new_pages[region]
        for g in before.glyphs.values():
            box=(g['x'],g['y'],g['x']+g['width'],g['y']+g['height'])
            assert original.crop(box).tobytes()==page.crop(box).tobytes()
        for cp in assets['manifest']['roles'][role]['added_ids']:
            g=after.glyphs[cp];box=(g['x'],g['y'],g['x']+size,g['y']+size)
            actual=page.crop(box)
            ref,bbox,ink=raw_cell(source8 if size==8 else source12,cp,8 if size==8 else 12)
            if size==10:ref=ref.resize((10,10),Image.Resampling.NEAREST)
            assert actual.tobytes()==ref.tobytes(),(role,cp,'BDF pixel mismatch')
            assert set(actual.getdata())<={(0,0,0,0),(255,255,255,255)}
            old_bg.update(original.crop(box).getdata())
            if size==8 and bbox!=(8,8,0,0,8):nonfull8.append({'cp':cp,'bbox':bbox})
        report['roles'][role]={'original':len(before.glyphs),'added':len(after.glyphs)-len(before.glyphs),'added_ids':assets['manifest']['roles'][role]['added_ids'],
                               'fnt_sha256':sha(assets['fnts'][filename]),'source_exact_pixels':True,'old_glyph_metrics_pixels_headers_preserved':True}
    for name,page in new_pages.items():
        mask=Image.new('1',page.size,0)
        for entry in assets['manifest']['added_rectangles']:
            if entry['region']==name:mask.paste(1,tuple(entry['box']))
        expected=source_regions[jar.name][name].copy()
        expected.paste(page,mask=mask)
        assert expected.tobytes()==page.tobytes(),'pixels changed outside appended rectangles'
    report['old_append_rect_pixel_colors']={str(k):v for k,v in old_bg.items()}
    report['non_full_cell_native8_added']=nonfull8
    report['all_outside_append_pixels_unchanged']=True
    report['nested_story_manifest_matches_new_png']=nested['inventory']['bbc2-shared-story12.png']==sha(assets['png_regions']['bbc2'])
    report['nested_story_manifest_matches_new_root_fnt']=nested['inventory']['story12.fnt']==sha(assets['fnts']['story12.fnt'])
    report['generated_font_manifest']=assets['manifest']
    (HERE/'font-probe-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['generated_font_manifest','old_story_manifest_inventory']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
