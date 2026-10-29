"""Append missing r28 glyphs without moving existing glyphs or changing game art.

Pure producer: frozen r27 JAR + display strings -> FNT/atlas-region buffers and manifest.
Does not write files, install, download, mutate the original runtime, or start the game.
Native12 and native8 sources are local, SHA-pinned Fusion Pixel OFL derivatives.
New default10 glyphs are explicitly nearest-sampled from native12 (not claimed native10).
"""
from __future__ import annotations
from io import BytesIO
from pathlib import Path
import hashlib
import json
import re
import unicodedata
import zipfile
from PIL import Image
from codec import decrypt_file
from projectlib import parse_atlas
from layout_fonts import parse_fnt, GLYPH_FIELDS
from build_story_font12 import native_bdf, SOURCE_ZIP_SHA256, SOURCE_ENTRY, SOURCE_BDF_SHA256
from build_item_font8 import parse_bdf, SOURCE_BDF_SHA256 as BDF8_SHA

ROOT = Path(__file__).resolve().parents[2]
BASE_JAR_SHA = 'dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be'
ROLES = {'default': ('bbc2.fnt', 'bbc2', 10, 1024),
         'classic': ('classic.fnt', 'classic', 8, 1024),
         'story12': ('story12.fnt', 'bbc2', 12, 1280)}
sha = lambda data: hashlib.sha256(data).hexdigest()


def required_ids(texts):
    ids = set()
    for text in texts:
        if not isinstance(text, str):
            raise TypeError('Font coverage inputs must be strings')
        for char in text + text.upper():
            cp = ord(char)
            if char in '\r\n\t\u2028\u2029':
                continue
            if unicodedata.category(char) in ('Cc','Cf'):
                raise ValueError('Unsupported display control U+%04X' % cp)
            if cp > 65535 or 0xD800 <= cp <= 0xDFFF:
                raise ValueError('Original backend is BMP-only: U+%X' % cp)
            ids.add(cp)
    return ids


def append_fnt(raw, records):
    if not records:
        return raw
    font = parse_fnt(raw.decode('utf8'))
    if set(records) & set(font.glyphs):
        raise ValueError('Refuse replacing an existing glyph')
    lines = raw.decode('utf8').splitlines()
    count_at = next(i for i, line in enumerate(lines) if line.startswith('chars '))
    lines[count_at] = 'chars count=%d' % (len(font.glyphs) + len(records))
    at = next((i for i, line in enumerate(lines) if line.startswith('kernings ')), len(lines))
    added = ['char ' + ' '.join('%s=%d' % (key, record[key]) for key in GLYPH_FIELDS)
             for _, record in sorted(records.items())]
    out = ('\n'.join(lines[:at] + added + lines[at:]) + '\n').encode('utf8')
    final = parse_fnt(out.decode('utf8'))
    if any(final.glyphs[cp] != g for cp, g in font.glyphs.items()):
        raise AssertionError('Existing metrics changed')
    return out


def black_transparent(image):
    """Canonical binary RGBA required by both red-channel terminal shaders."""
    result = Image.new('RGBA', image.size, (0, 0, 0, 0))
    result.putdata([(255,255,255,255) if a else (0,0,0,0) for *_, a in image.getdata()])
    return result


def build_assets(base_jar, texts, *, source12_zip=None, source8_bdf=None):
    raw = Path(base_jar).read_bytes()
    if sha(raw) != BASE_JAR_SHA:
        raise ValueError('Frozen r27 JAR identity mismatch')
    wanted = required_ids(texts)
    with zipfile.ZipFile(BytesIO(raw)) as jar:
        route = json.loads(decrypt_file(jar.read('dataq/0')))
        _, regions = parse_atlas(decrypt_file(jar.read('dataq/' + str(route['/sprites.atlas']))).decode('utf8'))
        page = Image.open(BytesIO(decrypt_file(jar.read('dataq/' + str(route['/sprites.png']))))).convert('RGBA')
        original_fnts = {role: jar.read(spec[0]) for role, spec in ROLES.items()}
    fonts = {role: parse_fnt(raw.decode('utf8')) for role, raw in original_fnts.items()}
    missing = {role: sorted(wanted - set(font.glyphs)) for role, font in fonts.items()}
    native12 = native8 = None
    sources = {}
    if missing['default'] or missing['story12']:
        path = Path(source12_zip or ROOT/'localization/work/story-font12/font12.zip')
        source_zip = path.read_bytes()
        if sha(source_zip) != SOURCE_ZIP_SHA256:
            raise ValueError('Native12 source ZIP identity')
        native12 = native_bdf(zipfile.ZipFile(BytesIO(source_zip)).read(SOURCE_ENTRY))
        sources['native12'] = {'zip_sha256':SOURCE_ZIP_SHA256, 'bdf_sha256':SOURCE_BDF_SHA256,
                               'entry':SOURCE_ENTRY, 'license':'OFL-1.1'}
    if missing['classic']:
        path = Path(source8_bdf or ROOT/'work/item-font8/asset/fusion-pixel-8px-monospaced-zh_hans.bdf')
        source = path.read_bytes()
        if sha(source) != BDF8_SHA:
            raise ValueError('Native8 source BDF identity')
        native8 = parse_bdf(source)
        sources['native8'] = {'bdf_sha256':BDF8_SHA, 'license':'OFL-1.1'}
    pages, region_info = {}, {}
    for name in ['bbc2', 'classic']:
        r = next(r for r in regions if r['name'] == name)
        if r['rotation'] or r['size'] != [2048,2048]:
            raise ValueError('Unexpected font region')
        x,y = r['xy']; pages[name] = page.crop((x,y,x+2048,y+2048))
        region_info[name] = {'xy':[x,y], 'size':r['size'], 'index':r['index'], 'ordinal':r['ordinal']}
    old_pages = {name: image.copy() for name, image in pages.items()}
    masks = {name: Image.new('1', (2048,2048)) for name in pages}
    fnts = {}; added_rectangles = []; role_manifest = {}
    # Existing declared rectangles, not only alpha ink, are protected.
    occupied = {name: [] for name in pages}
    for role, font in fonts.items():
        region = ROLES[role][1]
        occupied[region].extend((g['x'],g['y'],g['x']+g['width'],g['y']+g['height'])
                                for g in font.glyphs.values() if g['width'] and g['height'])
    for role, (filename, region, size, y0) in ROLES.items():
        records = {}; cols = 2048 // (size+1)
        for index, cp in enumerate(missing[role]):
            x = (index % cols)*(size+1); y = y0+(index//cols)*(size+1)
            box = (x,y,x+size,y+size)
            if y+size > 2048 or (role=='default' and y+size > 1280):
                raise ValueError('Supplemental font band capacity')
            if any(x<r[2] and x+size>r[0] and y<r[3] and y+size>r[1] for r in occupied[region]):
                raise ValueError('Supplement overlaps an existing declared rectangle')
            if masks[region].crop(box).getbbox():
                raise AssertionError('Supplemental rectangles intersect')
            if role == 'classic':
                if cp not in native8: raise ValueError('Native8 missing U+%04X' % cp)
                w,h,xo,yo,advance,pixels = native8[cp]
                if not (0<=xo<=size-w and 0<=yo<=size-h):
                    raise ValueError('Native8 glyph exceeds cell U+%04X' % cp)
                cell = Image.new('RGBA',(size,size),(0,0,0,0))
                cell.alpha_composite(pixels,(xo,yo)); cell = black_transparent(cell)
            else:
                if cp not in native12: raise ValueError('Native12 missing U+%04X' % cp)
                cell = native12[cp][0].copy()
                if size != 12: cell = cell.resize((size,size),Image.Resampling.NEAREST)
                cell = black_transparent(cell)
            if not chr(cp).isspace() and cell.getchannel('A').getbbox() is None:
                raise ValueError('Empty supplemental glyph U+%04X' % cp)
            pages[region].paste(cell,(x,y)); masks[region].paste(1,box)
            record = dict(id=cp,x=x,y=y,width=size,height=size,xoffset=0,yoffset=0,
                          xadvance=size,page=0,chnl=0)
            records[cp] = record
            added_rectangles.append({'role':role,'region':region,'codepoint':cp,'box':list(box)})
        fnts[filename] = append_fnt(original_fnts[role],records)
        role_manifest[role] = {'fnt':filename,'original_sha256':sha(original_fnts[role]),
            'sha256':sha(fnts[filename]),'original_count':len(fonts[role].glyphs),
            'new_count':len(fonts[role].glyphs)+len(records),'added_ids':list(records),
            'glyph_size':size,'transform':'native8' if size==8 else 'native12' if size==12 else 'native12-nearest-10-not-native10'}
    for name,image in pages.items():
        expected = old_pages[name].copy()
        for entry in added_rectangles:
            if entry['region']==name:
                box=tuple(entry['box']);expected.paste(image.crop(box),box[:2])
        if expected.tobytes()!=image.tobytes():raise AssertionError('Unapproved font pixels changed')
        for role,font in fonts.items():
            if ROLES[role][1]!=name:continue
            for g in font.glyphs.values():
                box=(g['x'],g['y'],g['x']+g['width'],g['y']+g['height'])
                if old_pages[name].crop(box).tobytes()!=image.crop(box).tobytes():
                    raise AssertionError('Original glyph pixels changed')
    pngs={}
    for name,image in pages.items():
        out=BytesIO();image.save(out,format='PNG');pngs[name]=out.getvalue()
    manifest={'schema':1,'baseline_sha256':BASE_JAR_SHA,'required_codepoints':sorted(wanted),
        'roles':role_manifest,'sources':sources,'region_identity':region_info,
        'added_rectangles':added_rectangles,'original_glyph_metrics_pixels_preserved':True,
        'png_container_hashes':{name:sha(raw) for name,raw in pngs.items()},
        'region_rgba_hashes':{name:sha(image.tobytes()) for name,image in pages.items()}}
    return {'fnts':fnts,'png_regions':pngs,'manifest':manifest}
