"""Read-only candidate/API tests, with reports written only to image staging.
No archive/package modification, install, game launch or save access.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import base64
import gzip
import json
import struct
import sys
import zipfile
from PIL import Image, ImageChops

ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
BASE=ROOT/'docs/font-layout-audit-20261025/image-workorders'
sys.path.insert(0,str(ROOT/'localization/tools'))
from optimized_images import apply_overrides, load_overrides, raw_rgba_hash, verify_replacement
from projectlib import parse_atlas
from codec import decrypt_file
from build_images import NativeFont, FONT8, FONT12


def check(condition,message):
    if not condition:raise AssertionError(message)


def rejected(call,reason):
    try:call()
    except ValueError:return reason
    raise AssertionError('negative case accepted: '+reason)


def changed_mask(before,after):
    channels=ImageChops.difference(before,after).split();union=channels[0]
    for channel in channels[1:]:union=ImageChops.lighter(union,channel)
    return union.point(lambda p:255 if p else 0)


def main():
    manifest=json.loads((OUT/'manifest.json').read_text(encoding='utf8'))
    orders=json.loads((BASE/'workorders.json').read_text(encoding='utf8'))
    locked=json.loads((OUT/'candidates.json').read_text(encoding='utf8'))['exact_text']
    all_rows=manifest['replacements']+manifest['retained']
    check(len(all_rows)==243,'exact 243 target rows')
    identities={(r['variant'],r['logical_name'],r['index'],r['ordinal']) for r in all_rows}
    check(len(identities)==243,'unique target identities')
    expected={(v['variant'],a['name'],v['region']['index'],v['region']['ordinal']) for j in orders['workorders'] for a in j['assets'] for v in a['variants'] if v['variant'] in ('jar','patch')}
    check(identities==expected,'exact workorder target coverage')
    check(sha256((BASE/'workorders.json').read_bytes()).hexdigest()==manifest['source_workorders_sha256'],'immutable workorders pin')
    check(sha256((OUT/'candidates.json').read_bytes()).hexdigest()==manifest['candidate_text_sha256'],'locked candidate pin')
    required={ord(c) for text in locked.values() for c in text if c!='\n'}
    with zipfile.ZipFile(FONT12) as z:data12=z.read('fusion-pixel-12px-monospaced-zh_hans.bdf')
    fonts={8:NativeFont(FONT8.read_bytes(),8,required),12:NativeFont(data12,12,required)}
    ops=0
    for variant in ('jar','patch'):
        for row in load_overrides(variant):
            before=Image.open(BASE/row['source_preview']).convert('RGBA');after=row['image']
            check(raw_rgba_hash(before)==row['expected_rawRGBA_sha256'],'exact source crop pin')
            proof=verify_replacement(before,after,row['mask'])
            check(proof['changed_pixels']==row['changed_pixels'],'changed-pixel count')
            for op in row['operations']:
                check(op['exact_locked_text'],'unlocked operation')
                if 'tile_id' in op:
                    check(op['zh'] in '商店','unknown sign character')
                    check(after.crop((0,8,after.width,after.height)).tobytes()==before.crop((0,8,before.width,before.height)).tobytes(),'tile art/rim')
                    continue
                check(op['zh'] in locked[op['english']].split('\n'),'exact codepoints/punctuation/linebreaks')
                raster=fonts[op['font_px']].raster(op['zh'])
                check(sha256(raster.tobytes()).hexdigest()==op['raster_mask_sha256'],'exact native glyph raster pin')
                x,y=op['origin'];x0,y0,x1,y1=op['slot']
                expected=Image.new('RGBA',(x1-x0,y1-y0),tuple(op['background']))
                expected.paste(tuple(op['foreground']),(x-x0,y-y0,x-x0+raster.width,y-y0+raster.height),raster)
                check(after.crop(op['slot']).tobytes()==expected.tobytes(),'exact rendered text/no English residual: '+str((row['logical_name'],op['zh'])))
                ops+=1
            if row['logical_name']=='CosmoCasino2':
                for box in [(30,104,112,168),(0,121,112,168),(0,0,112,96)]:
                    check(after.crop(box).tobytes()==before.crop(box).tobytes(),'casino character/arrow/wheel pixels preserved')
            if row['logical_name']=='CosmoItemMenuBG':
                for box in [(127,15,129,191),(129,161,251,163),(5,15,127,189),(129,15,251,161),(129,163,251,189)]:
                    check(after.crop(box).tobytes()==before.crop(box).tobytes(),'item 128px division/dynamic slot preserved')
            if row['logical_name'] in ('CosmoSaveMenuBG','CosmoNameEntryMenuBG'):
                for box in [(0,42,256,43),(99,23,101,120),(211,23,214,120),(6,43,250,119),(6,33,99,42)]:
                    check(after.crop(box).tobytes()==before.crop(box).tobytes(),'save separators/data/F.DATA preserved')
    negative=[]
    tiny=Image.new('RGBA',(1,1),(1,2,3,0));other=tiny.copy();other.putpixel((0,0),(4,2,3,0))
    negative.append(rejected(lambda:verify_replacement(tiny,other,Image.new('L',(1,1))), 'RGB-under-alpha-outside-mask'))
    other.putpixel((0,0),(1,2,3,255))
    negative.append(rejected(lambda:verify_replacement(tiny,other,Image.new('L',(1,1),255)), 'alpha-change-even-inside-mask'))
    negative.append(rejected(lambda:load_overrides('source-patch'),'unsupported-variant'))
    negative.append(rejected(lambda:apply_overrides(Image.new('RGB',(1,1)),[],'jar'),'non-RGBA-page'))
    negative.append(rejected(lambda:apply_overrides(Image.new('RGBA',(1,1)),[],'jar'),'missing-ordinal-identity'))
    # Independent sign-use evidence: game's compact layers are BIG endian uint32.
    tilepath=ROOT/'localization/sources/blobs/c51673200dc3d4c794b8cbb6e7496837cce357ab8d1431cc6f03bacd6a044d1c.json'
    sign_evidence=[];animated_tilesets=set()
    target_tilesets={f'ClassicTileset0{suffix}.tsx' for suffix in ('','A','B','C','F')}
    for name,m in json.loads(tilepath.read_text(encoding='utf8')):
        t=m['tmx'];refs=[r for r in t['tilesetRefs'] if r['filename'] in target_tilesets]
        if not refs:continue
        f=refs[0]['firstGID']
        ts=next(ts for ref,ts in m['tilesets'] if ref['filename']==refs[0]['filename'])
        animated=next((tile for tile in ts['tiles'] if tile['id']==1),None)
        if animated is not None:
            check(animated['animation']==[[1,0.1],[2,0.1]],'sign OP alternate frame identities')
            animated_tilesets.add(refs[0]['filename'])
        for layer,l in t['layers'].items():
            raw=gzip.decompress(base64.b64decode(l['data']));vals=struct.unpack('>'+'I'*(len(raw)//4),raw);width=l['width']
            for i,v in enumerate(vals):
                if v==f:
                    sign_evidence.append({'map':name,'layer':layer,'xy':[i%width,i//width],
                        'tileset':refs[0]['filename'],'right_tile_local':vals[i+1]-f if i%width<width-1 else None})
    check(sum(r['right_tile_local']==1 for r in sign_evidence)>=8,'sign adjacency evidence incomplete')
    check(animated_tilesets=={'ClassicTileset0.tsx','ClassicTileset0A.tsx','ClassicTileset0C.tsx'},'exact directly referenced sign animation declarations')
    # 0F definitions are embedded as alternates but absent from direct tilesetRefs;
    # 0B has no tile1 animation declaration. Neither fact changes tile geometry.
    atlas_reports=[]
    for variant,e in zip(('jar','patch'),manifest['source_archives']['archives']):
        archive=ROOT/e['archive']
        check(sha256(archive.read_bytes()).hexdigest()==e['archive_sha256'],'r27 archive SHA pin')
        with zipfile.ZipFile(archive) as z:
            atlas=decrypt_file(z.read(e['entries']['sprites.atlas']))
            page_png=decrypt_file(z.read(e['entries']['sprites.png']))
        check(sha256(atlas).hexdigest()==e['atlas_sha256'],'decrypted atlas pin')
        check(sha256(page_png).hexdigest()==e['page_sha256'],'decrypted page pin')
        _,regions=parse_atlas(atlas.decode('utf8'))
        page=Image.open(BytesIO(page_png)).convert('RGBA');input_hash=raw_rgba_hash(page)
        output,report=apply_overrides(page,regions,variant)
        check(input_hash==raw_rgba_hash(page),'pure API mutated caller input')
        allowed=Image.new('L',page.size)
        for row in load_overrides(variant):
            x,y=row['source_xy'];old=allowed.crop((x,y,x+row['size'][0],y+row['size'][1]))
            allowed.paste(ImageChops.lighter(old,row['mask']),(x,y))
            check(raw_rgba_hash(output.crop((x,y,x+row['size'][0],y+row['size'][1])))==row['new_rawRGBA_sha256'],'atlas overlay output crop pin')
        diff=changed_mask(page,output)
        check(ImageChops.subtract(diff,allowed).getbbox() is None,'atlas-level outside-approved-mask')
        check(page.getchannel('A').tobytes()==output.getchannel('A').tobytes(),'atlas-level alpha preservation')
        for row in manifest['retained']:
            if row['variant']!=variant:continue
            x,y=row['source_xy'];w,h=row['size']
            check(raw_rgba_hash(output.crop((x,y,x+w,y+h)))==row['expected_rawRGBA_sha256'],'retained frame changed through alias overlap')
        sample=load_overrides(variant)[0];altered=page.copy();x,y=sample['source_xy'];altered.putpixel((x,y),(11,22,33,44))
        negative.append(rejected(lambda:apply_overrides(altered,regions,variant),'stale-source-hash-'+variant))
        badregions=[dict(r) for r in regions]
        for r in badregions:
            if (r['name'],r['index'],r['ordinal'])==(sample['logical_name'],sample['index'],sample['ordinal']):r['ordinal']=-999
        negative.append(rejected(lambda:apply_overrides(page,badregions,variant),'wrong-ordinal-'+variant))
        report.update({'archive_sha256':e['archive_sha256'],'atlas_changed_pixels':diff.histogram()[255],
                       'changed_pixels_outside_approved_mask':0,'alpha_changed_pixels':0,
                       'retained_rows_exact':sum(r['variant']==variant for r in manifest['retained']),
                       'input_not_mutated':True})
        atlas_reports.append(report)
        print(variant,'decoded atlas overlay passed',report['replacement_count'],flush=True)
    report={'passed':True,'target_rows':243,'redrawn_rows':len(manifest['replacements']),
            'retained_rows':len(manifest['retained']),'exact_text_blocks_checked':ops,
            'negative_cases_rejected':negative,'source_tilemap_sha256':sha256(tilepath.read_bytes()).hexdigest(),
            'sign_tilemap_evidence':sign_evidence,'atlas_reports':atlas_reports,
            'scope':'read-only original archives + in-memory overlay; only this JSON report written to image staging'}
    (OUT/'test-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('PASS',json.dumps({k:v for k,v in report.items() if k not in ('atlas_reports','sign_tilemap_evidence')},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
