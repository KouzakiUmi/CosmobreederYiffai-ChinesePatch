"""Build a pinned native12 story role on the EXISTING default10 texture page.

build_story_font12(official_source_zip, NEW_output_dir); validate_story_font12(dir).
Packaging: copy story12.fnt to JAR/PAK root; replace only the existing bbc2 atlas
region with bbc2-shared-story12.png. Never replace bbc2.fnt/default/classic roles.
The original default10 PNG and every original glyph rectangle remain untouched.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import unicodedata
import zipfile
from PIL import Image
from layout_fonts import parse_fnt

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / 'localization/runtime'
ROLE = 'story12'
SOURCE_URL = 'https://github.com/TakWolf/fusion-pixel-font/releases/download/2026.10.16/fusion-pixel-font-12px-monospaced-bdf-v2026.10.16.zip'
SOURCE_ZIP_SHA256 = '76ed4adde0cc43ae8312041960d586c130c75a9d0f7c1c64a7cace7e4130c358'
SOURCE_ENTRY = 'fusion-pixel-12px-monospaced-zh_hans.bdf'
SOURCE_BDF_SHA256 = 'b1e9a54fdd1c1e86fdc32efa16a04d8bd2897391ddb441238cee66947d6e3388'
DEFAULT_FNT_SHA256 = '000c85594bb86de3402ab9c4dab3b50c0590051dbbe9b96a8d856acb7e983753'
DEFAULT_PNG_SHA256 = '075a2803ee8c5e04ff8d755e76a7d7803fd45080b6a4b031be99bf1a656db306'
FONT_SHA256 = '972d49918484e3e5521a7da58dbe94f6c6c604e4f486844b75f5b3be87fa2546'
PNG_SHA256 = '486935a160007265569428c871ce3f949fd1b3a1d68f3690ea7f6572276540bd'
FNT_NAME = 'story12.fnt'
PNG_NAME = 'bbc2-shared-story12.png'
MANIFEST_NAME = 'story12.manifest.json'
FULL_PUNCTUATION = {0x00b7, 0x2014, 0x2018, 0x2019, 0x201c, 0x201d, 0x2026}


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(value):
    return sha256(value).hexdigest()


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def wide(cp):
    return (cp > 127 and (unicodedata.east_asian_width(chr(cp)) in ('W', 'F')
                         or cp in FULL_PUNCTUATION or 0x2e80 <= cp <= 0x9fff))


def coverage():
    loc = ROOT / 'localization'
    paths = [loc/'catalog/units.jsonl', loc/'translations/zh-CN.jsonl', loc/'translations/dialogue-joins.jsonl']
    units = rows(paths[0]); translated = {r['id']: r for r in rows(paths[1])}; joins = rows(paths[2])
    selected = [r for r in units if r['category'] in ('dialogue', 'vsn')]
    texts = []
    for unit in selected:
        texts.append(unit['source'])
        record = translated.get(unit['id'], {})
        texts.extend(record[k] for k in ('draft', 'translation') if record.get(k))
    texts.extend(r['merged_translation'] for r in joins)
    # Superset covers dynamic reports/variables already present in the default10
    # charset as well; do not let source-only vs draft selection hide characters.
    source_font = parse_fnt((RUNTIME/'bbc2-10px.fnt').read_text(encoding='utf-8'))
    ids = set(source_font.glyphs)
    for text in texts:
        ids.update(ord(c) for c in text + text.upper() if ord(c) >= 32)
    require(all(cp <= 65535 and not 0xd800 <= cp <= 0xdfff for cp in ids), 'legacy font backend requires BMP corpus')
    require(len(joins) == 956 and len(selected) > 6000, 'story coverage input count drift')
    return {'schema': 1, 'unit_categories': ['dialogue', 'vsn'], 'unit_count': len(selected),
            'join_count': len(joins), 'texts_checked': len(texts), 'required_ids': sorted(ids),
            'source_and_current_draft_and_translation_and_uppercase': True,
            'dynamic_default10_charset_included': True,
            'sources': [{'path': p.relative_to(ROOT).as_posix(), 'sha256': digest(p.read_bytes())} for p in paths]}


def source_pair():
    fnt = (RUNTIME/'bbc2-10px.fnt').read_bytes(); png = (RUNTIME/'bbc2-cjk-10.png').read_bytes()
    require(digest(fnt) == DEFAULT_FNT_SHA256 and digest(png) == DEFAULT_PNG_SHA256, 'default10 source identity changed')
    font = parse_fnt(fnt.decode('utf-8')); image = Image.open(BytesIO(png)).convert('RGBA')
    require(image.size == (2048, 2048), 'default10 texture dimensions')
    require(max(g['y'] + g['height'] for g in font.glyphs.values()) < 256, 'default10 glyph overlaps reserved story strip')
    require(image.crop((0,256,2048,2048)).getchannel('A').getbbox() is None, 'reserved story strip contains existing ink')
    return fnt, png, font, image


def native_bdf(source):
    require(digest(source) == SOURCE_BDF_SHA256, 'native12 BDF SHA')
    text = source.decode('utf-8')
    require('\nSIZE 12 75 75\n' in text and '\nPIXEL_SIZE 12\n' in text and
            '\nFONTBOUNDINGBOX 12 12 0 -2\n' in text, 'not official native12 BDF')
    glyphs = {}
    for block in text.split('STARTCHAR ')[1:]:
        lines = block.splitlines()
        cp = int(next(l for l in lines if l.startswith('ENCODING ')).split()[1])
        if not 0 <= cp <= 65535 or 0xd800 <= cp <= 0xdfff:
            continue
        w,h,xo,yo = map(int,next(l for l in lines if l.startswith('BBX ')).split()[1:])
        advance, vertical = map(int,next(l for l in lines if l.startswith('DWIDTH ')).split()[1:])
        # Upstream also contains non-body-box tone marks, double-height kana
        # and private 30px logos. They are NOT claimed as12px; a corpus reference
        # to one fails the explicit required-ID subset gate below.
        if not (0 <= w <= 12 and 0 <= h <= 12 and vertical == 0 and 0 < advance <= 12):
            continue
        bits = lines[lines.index('BITMAP')+1:lines.index('ENDCHAR')]
        require(len(bits) == h and cp not in glyphs, 'BDF count/duplicate')
        # Both shipped terminal shaders test texture.r, NOT texture.a.
        # Transparent white would turn an entire 12x12 glyph into a solid block.
        cell = Image.new('RGBA',(12,12),(0,0,0,0))
        top = 10-yo-h
        require(0 <= xo <= 12-w and 0 <= top <= 12-h, 'BDF glyph outside 12px body box')
        for y, row in enumerate(bits):
            value = int(row,16); count = 4*len(row)
            for x in range(w):
                if value & (1 << (count-1-x)):
                    cell.putpixel((xo+x,top+y),(255,255,255,255))
        glyphs[cp] = (cell, advance)
    require(len(glyphs) > 30000, 'native12 BDF unexpectedly incomplete')
    return glyphs


def compose(source, corpus):
    _,_,old,image = source_pair(); native = native_bdf(source)
    ids = set(corpus['required_ids'])
    copied = sorted(cp for cp in ids if not wide(cp) and cp in old.glyphs)
    added = sorted(ids - set(copied))
    require(set(added) <= native.keys(), 'official12 missing corpus: ' + str(sorted(set(added)-native.keys())))
    # Keep the entire ASCII/common metadata contract, especially baseline8 and
    # padding1. This makes mixed masked ASCII pen/vertical placement IDENTICAL
    # across default10/story12 role changes. The native CJK body is still12x12.
    lines = ['info face="Cosmo Story Native 12 + Original BBC ASCII" size=12 bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=0 aa=1 padding=1,1,1,1 spacing=-2,-2',
             'common lineHeight=16 base=8 scaleW=2048 scaleH=2048 pages=1 packed=0',
             'page id=0 file="bbc2.png"', f'chars count={len(ids)}']
    glyphs = {cp:dict(old.glyphs[cp]) for cp in copied}
    boxes = []
    for index,cp in enumerate(added):
        x,y = (index%157)*13, 256+(index//157)*13
        require(y+12<=2048, 'native12 reserved atlas capacity')
        cell,advance = native[cp]
        image.paste(cell,(x,y))
        glyphs[cp] = dict(id=cp,x=x,y=y,width=12,height=12,xoffset=0,yoffset=0,
                          xadvance=12 if wide(cp) else advance,page=0,chnl=0)
        boxes.append([cp,x,y,12,12])
    fields = ('id','x','y','width','height','xoffset','yoffset','xadvance','page','chnl')
    for cp,g in sorted(glyphs.items()):
        lines.append('char '+' '.join(f'{key}={g[key]}' for key in fields))
    lines.append('kernings count=0')
    fnt=('\n'.join(lines)+'\n').encode('utf-8'); buffer=BytesIO(); image.save(buffer,format='PNG')
    return fnt,buffer.getvalue(),copied,added,boxes


def validate_pair(fnt,png,corpus,source=None):
    require(digest(fnt)==FONT_SHA256 and digest(png)==PNG_SHA256, 'sealed story12 FNT/PNG output identity')
    font=parse_fnt(fnt.decode('utf-8')); image=Image.open(BytesIO(png)).convert('RGBA')
    _,_,old,original=source_pair()
    require(font.info['size']==12 and font.common['lineHeight']==16 and font.common['base']==8, 'story12 metric header')
    require(font.info['padding']=='1,1,1,1' and font.pages=={0:'bbc2.png'} and not font.kernings, 'original shared page/ascii padding contract')
    require(image.size==(2048,2048) and set(font.glyphs)==set(corpus['required_ids']), 'story12 charset/PNG identity')
    for cp,g in old.glyphs.items():
        box=(g['x'],g['y'],g['x']+g['width'],g['y']+g['height'])
        require(image.crop(box).tobytes()==original.crop(box).tobytes(), f'old10 glyph pixels changed U+{cp:04X}')
    require(image.crop((0,0,2048,256)).tobytes()==original.crop((0,0,2048,256)).tobytes(), 'entire protected original strip changed')
    occupied=Image.new('1',(2048,2048),0)
    expected_background=original.copy()
    native=native_bdf(source) if source is not None else None
    for cp,g in font.glyphs.items():
        require(g['xadvance']>=0, 'negative advance')
        if not wide(cp) and cp in old.glyphs:
            require(g==old.glyphs[cp], f'original ASCII/nonwide metrics changed U+{cp:04X}')
            continue
        require(g['width']==g['height']==12 and (not wide(cp) or g['xadvance']==12), f'not real12 glyph U+{cp:04X}')
        require(g['y']>=256 and g['xoffset']==g['yoffset']==0, 'new glyph escaped reserved grid')
        box=(g['x'],g['y'],g['x']+12,g['y']+12)
        require(occupied.crop(box).getbbox() is None, 'new glyph rectangles overlap')
        occupied.paste(1,box)
        expected_background.paste(image.crop(box),box[:2])
        cell=image.crop(box)
        alpha=cell.getchannel('A')
        require(set(alpha.tobytes()) <= {0,255}, 'native bits were smoothed/scaled')
        # Actual cosmo/vsn terminal shaders use base_color.r > 0, ignoring A.
        # Validate that exact channel contract instead of only inspecting alpha.
        require(cell.getchannel('R').tobytes()==alpha.tobytes(), 'shader red mask differs from native alpha mask')
        require(all(pixel in ((0,0,0,0),(255,255,255,255)) for pixel in cell.getdata()), 'native transparent RGB would render as solid blocks')
        if not chr(cp).isspace(): require(alpha.getbbox() is not None, f'empty story glyph U+{cp:04X}')
        if native is not None: require(image.crop(box).tobytes()==native[cp][0].tobytes(), 'native12 pixels changed')
    # Exact RGBA equality for EVERY pixel outside added rectangles, including
    # transparent RGB bytes and partial neighborhoods next to added cells.
    require(expected_background.tobytes()==image.tobytes(), 'unrelated atlas pixels changed')
    return font


def build_story_font12_assets(source_zip):
    """Read-only deterministic asset producer -> (manifest, {name: bytes}).

    Archive builders can consume these validated buffers directly as their
    already-authorized packaging inputs; this API performs NO filesystem write.
    It does not retry or claim to repair any refused output-directory operation.
    """
    raw=Path(source_zip).read_bytes(); require(digest(raw)==SOURCE_ZIP_SHA256, 'official12 ZIP SHA')
    archive=zipfile.ZipFile(BytesIO(raw)); source=archive.read(SOURCE_ENTRY)
    corpus=coverage(); fnt,png,copied,added,boxes=compose(source,corpus)
    validate_pair(fnt,png,corpus,source)
    licenses={n:archive.read(n) for n in archive.namelist() if n=='OFL.txt' or n.startswith('LICENSES/')}
    require(b'SIL OPEN FONT LICENSE Version 1.1' in licenses['OFL.txt'], 'full OFL missing')
    notice=('Cosmo Story Native 12 bitmap derivative of Fusion Pixel 12px Mono zh_Hans 2026.10.16.\n'
            'Copyright (c) 2022, TakWolf (https://takwolf.com). SIL Open Font License1.1.\n'
            'https://github.com/TakWolf/fusion-pixel-font\n'
            'Native BDF bits copied 1:1 into12x12 cells, no scaling. Original game ASCII pixels/metrics remain under original rightsholders terms.\n'
            'OFL covers the new font contribution, NOT a relicensing grant for original game texture/ASCII.\n').encode()
    files={FNT_NAME:fnt,PNG_NAME:png,'story12.coverage.json':(json.dumps(corpus,ensure_ascii=False,indent=2)+'\n').encode(),
           'NOTICE.txt':notice,**licenses}
    manifest={'schema':1,'role':ROLE,'native_size':12,'lineHeight':16,'base':8,
              'source':{'url':SOURCE_URL,'zip_sha256':SOURCE_ZIP_SHA256,'entry':SOURCE_ENTRY,'bdf_sha256':SOURCE_BDF_SHA256,
                        'copyright':'Copyright (c) 2022, TakWolf (https://takwolf.com)','license':'OFL-1.1'},
              'original':{'bbc2-10px.fnt':DEFAULT_FNT_SHA256,'bbc2-cjk-10.png':DEFAULT_PNG_SHA256},
              'glyph_count':len(corpus['required_ids']),'copied_ids':copied,'native12_ids':added,'native_rectangles':boxes,
              'protection':{'all_original_glyph_coordinates_unchanged':True,'all_original_glyph_pixels_unchanged':True,
                            'entire_original_strip':[0,0,2048,256],'new_texture':False,'rescaled':False,
                            'terminal_shader_mask':'red_equals_native_alpha; transparent pixels RGBA(0,0,0,0)',
                            'ascii_baseline_padding_and_records':'unchanged','shared_atlas_role':'bbc2'},
              'packaging':{'fnt_entry':'story12.fnt','hybrid_png':PNG_NAME,'base_r21_region_bbox':[0,4096,2048,6144],
                           'atlas_string_changed':False,'both_archives_required':True},
              'inventory':{n:digest(b) for n,b in sorted(files.items())}}
    files[MANIFEST_NAME]=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    return manifest,files


def build_story_font12(source_zip,output_dir):
    output=Path(output_dir); require(not output.exists(), 'refuse existing story12 output')
    manifest,files=build_story_font12_assets(source_zip)
    output.mkdir(parents=True)
    for name,data in files.items():
        target=output/name; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
    return manifest


def validate_story_font12(output_dir,source_zip=None):
    output=Path(output_dir); manifest=json.loads((output/MANIFEST_NAME).read_text(encoding='utf-8'))
    require(manifest['source']['bdf_sha256']==SOURCE_BDF_SHA256 and manifest['original']=={'bbc2-10px.fnt':DEFAULT_FNT_SHA256,'bbc2-cjk-10.png':DEFAULT_PNG_SHA256},'font provenance pin')
    for name,sha in manifest['inventory'].items(): require(digest((output/name).read_bytes())==sha,'asset/license SHA drift '+name)
    corpus=json.loads((output/'story12.coverage.json').read_text(encoding='utf-8')); require(corpus==coverage(),'current corpus changed')
    source=None
    if source_zip is not None:
        raw=Path(source_zip).read_bytes(); require(digest(raw)==SOURCE_ZIP_SHA256,'source ZIP pin')
        source=zipfile.ZipFile(BytesIO(raw)).read(SOURCE_ENTRY)
    font=validate_pair((output/FNT_NAME).read_bytes(),(output/PNG_NAME).read_bytes(),corpus,source)
    require(len(font.glyphs)==manifest['glyph_count'],'glyph count manifest drift')
    return manifest


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-zip',type=Path); parser.add_argument('--output',type=Path); parser.add_argument('--validate',type=Path)
    args=parser.parse_args()
    if args.validate: result=validate_story_font12(args.validate,args.source_zip)
    else:
        if not args.source_zip or not args.output: parser.error('--source-zip and --output required')
        result=build_story_font12(args.source_zip,args.output)
    print(json.dumps({'role':result['role'],'glyph_count':result['glyph_count'],'assets':result['inventory'],'source':result['source']},ensure_ascii=False,indent=2))
