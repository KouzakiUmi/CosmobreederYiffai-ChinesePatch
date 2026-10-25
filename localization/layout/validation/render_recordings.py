"""Replay recorded SN draw calls; no Python text layout and no game startup.

Diagnostic BEFORE shader/CRT, not a screenshot or an actual parent-clip proof.
Uses only the frozen candidate's atlas and the already-paired default font PNG.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'localization/tools'))
from codec import decrypt_file
from projectlib import parse_atlas


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def integer(value, label):
    if not isinstance(value, (int, float)) or isinstance(value, bool) or int(value) != value:
        raise ValueError(label + ' must be an integral logical pixel')
    return int(value)


def composite_checked(canvas, layer, x, y):
    """Clipping is only for generating a view; return the unhidden clip fact."""
    x, y = integer(x, 'x'), integer(y, 'y')
    right, bottom = x + layer.width, y + layer.height
    clipped = x < 0 or y < 0 or right > canvas.width or bottom > canvas.height
    left, top = max(0, x), max(0, y)
    r, b = min(canvas.width, right), min(canvas.height, bottom)
    if r > left and b > top:
        canvas.alpha_composite(layer.crop((left-x, top-y, r-x, b-y)), (left, top))
    return clipped


def load_assets(candidate):
    manifest_raw = (candidate/'package-manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    for entry in manifest['archives']:
        if digest((candidate/entry['archive']).read_bytes()) != entry['sha256']:
            raise ValueError('Candidate archive identity changed')
    with zipfile.ZipFile(candidate/'patch.pak') as archive:
        index = json.loads(decrypt_file(archive.read('dataq/0')))
        atlas_raw = decrypt_file(archive.read('dataq/'+str(index['/sprites.atlas'])))
        png_raw = decrypt_file(archive.read('dataq/'+str(index['/sprites.png'])))
    pages, regions = parse_atlas(atlas_raw.decode('utf-8'))
    with Image.open(io.BytesIO(png_raw)) as image: sheet = image.convert('RGBA')
    if len(pages) != 1 or pages[0]['name'] != 'sprites.png': raise ValueError('Unsupported atlas pages')
    if pages[0]['properties'].get('size') != ', '.join(map(str, sheet.size)):
        raise ValueError('Atlas page size mismatch')
    by_name = {}
    for region in regions: by_name.setdefault(region['name'], []).append(region)
    font_dir = candidate/'layout-bundle/fonts'
    font_png = (font_dir/'bbc2-cjk-10.png').read_bytes()
    with Image.open(io.BytesIO(font_png)) as image: font_page = image.convert('RGBA')
    return manifest_raw, by_name, sheet, font_page, {
        'fnt_sha256': digest((font_dir/'bbc2.fnt').read_bytes()),
        'png_sha256': digest(font_png), 'atlas_sha256': digest(atlas_raw),
        'atlas_png_sha256': digest(png_raw)}


def sprite(name, by_name, sheet, frame=None):
    matches = by_name.get(name, [])
    if frame is not None: matches = [r for r in matches if r['index'] == frame]
    if len(matches) != 1: raise ValueError('Unbound/ambiguous atlas sprite: '+str(name))
    r = matches[0]
    if r['rotation']: raise ValueError('Rotated sprite needs explicit replay support: '+name)
    x, y = r['xy']; width, height = r['size']
    ow, oh = r['orig']; ox, oy = r['offset']
    if min(x,y,width,height,ow,oh,ox,oy) < 0 or x+width > sheet.width or y+height > sheet.height:
        raise ValueError('Sprite bounds invalid')
    # Reconstruct the original untrimmed region before applying the SN anchor.
    image = Image.new('RGBA', (ow, oh), (0,0,0,0))
    clipped = composite_checked(image, sheet.crop((x,y,x+width,y+height)), ox, oh-oy-height)
    if clipped: raise ValueError('Trimmed sprite does not fit its original rectangle')
    return image


def replay_scenario(scenario, width, height, by_name, sheet, font_page):
    canvas = Image.new('RGBA', (width,height), (0,0,0,255))
    occupied = Image.new('L', (width,height), 0)
    text_overlap = Image.new('L', (width,height), 0)
    clipping, quad_boxes, methods = [], [], Counter()
    glyph_count = 0
    for ordinal, call in enumerate(scenario['calls']):
        kind = call['kind']
        for method in call.get('original_methods', []): methods[str(method)] += 1
        if kind == 'text':
            if call.get('font') != 'default': raise ValueError('Only the bound default font is supported')
            for quad in call['quads']:
                sx, sy = integer(quad['srcX'],'srcX'), integer(quad['srcY'],'srcY')
                w, h = integer(quad['width'],'glyph width'), integer(quad['height'],'glyph height')
                x, y = integer(quad['x'],'quad x'), integer(quad['screenTop'],'quad screenTop')
                if min(sx,sy,w,h) < 0 or sx+w > font_page.width or sy+h > font_page.height:
                    raise ValueError('Glyph source rectangle out of font atlas')
                if w == 0 or h == 0: continue
                glyph_count += 1
                glyph = font_page.crop((sx,sy,sx+w,sy+h))
                alpha = Image.new('L', (width,height), 0)
                alpha_canvas = Image.new('RGBA',(width,height),(0,0,0,0))
                clipped = composite_checked(alpha_canvas,glyph,x,y)
                alpha = alpha_canvas.getchannel('A')
                # Binary alpha occupancy; do not mistake transparent glyph padding
                # for overlap. Count each overlapped pixel once, not per glyph pair.
                binary = alpha.point(lambda value: 255 if value else 0)
                text_overlap = ImageChops.lighter(text_overlap, ImageChops.multiply(occupied,binary))
                occupied = ImageChops.lighter(occupied,binary)
                composite_checked(canvas,glyph,x,y)
                if clipped: clipping.append({'call':ordinal,'codepoint':quad['codepoint'],'bounds':[x,y,w,h]})
                quad_boxes.append({'call':ordinal,'codepoint':quad['codepoint'],'bounds':[x,y,w,h]})
        elif kind in ('image','rect'):
            name = call.get('name')
            if name is None: raise ValueError('A rectangle must identify its original fill sprite')
            image = sprite(name,by_name,sheet,call.get('frame'))
            if 'width' in call and 'height' in call and call['width'] is not None and call['height'] is not None:
                w, h = integer(call['width'],'image width'),integer(call['height'],'image height')
                if w <= 0 or h <= 0: raise ValueError('Nonpositive image extent')
                image = image.resize((w,h),Image.Resampling.NEAREST)
            x = integer(call['x'],'image x'); y = height-integer(call['y'],'image y')-image.height
            if composite_checked(canvas,image,x,y): clipping.append({'call':ordinal,'image':name})
        else:
            raise ValueError('Unsupported SN recording kind: '+str(kind))
    return canvas, {'id':scenario['id'],'prototype':scenario['prototype'],
                    'scenario_status':scenario.get('status','UNKNOWN'),
                    'expected_error':scenario.get('expected_error'),'error':scenario.get('error'),
                    'selected_index':scenario.get('selected_index'),'selected_slot':scenario.get('selected_slot'),
                    'text_glyphs':glyph_count,'text_overlap_pixels':text_overlap.histogram()[255],
                    'canvas_clip_events':clipping,'stack_method_occurrences':dict(methods),
                    'parent_clip_verified':False,'crt_verified':False,'glyph_boxes':quad_boxes}


def run(recording, output, candidate):
    root = (ROOT/'localization/work/layout-drawing-replays').resolve()
    output = output.resolve()
    if output == root or not output.is_relative_to(root) or output.exists():
        raise ValueError('Replay output must be a NEW child of work/layout-drawing-replays')
    raw = recording.read_bytes(); data = json.loads(raw)
    if data.get('schema_version') != 1: raise ValueError('Unsupported recording schema')
    width,height = integer(data['width'],'width'),integer(data['height'],'height')
    if (width,height) != (256,224): raise ValueError('Unverified coordinate plane')
    manifest_raw,by_name,sheet,font_page,identities = load_assets(candidate)
    expected_jar = next(a['sha256'] for a in json.loads(manifest_raw)['archives'] if a['archive']=='cosmobreeder-multi.jar')
    if data.get('candidate_jar_sha256') != expected_jar:
        raise ValueError('Recording/candidate code identity mismatch')
    if data.get('guard_active') is not True or data.get('positive_scenario_denied_operations') != 0 or data.get('forbidden_attempts') != []:
        raise ValueError('Recording producer did not attest a clean guarded run')
    if any(s.get('status') not in ('PASS','EXPECTED_REJECTION') for s in data['scenarios']):
        raise ValueError('Recording contains a failed/unknown scenario')
    for key in ('fnt_sha256','png_sha256'):
        if data['font'].get(key) != identities[key]: raise ValueError('Recording/font identity mismatch')
    ids = [s['id'] for s in data['scenarios']]
    if len(ids) != len(set(ids)) or any(not isinstance(v,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,120}',v) for v in ids):
        raise ValueError('Invalid/duplicate scenario identity')
    # Compute and validate all input before creating a visible result directory.
    rendered = [replay_scenario(s,width,height,by_name,sheet,font_page) for s in data['scenarios']]
    output.mkdir(parents=True)
    results = []
    for canvas,result in rendered:
        path = output/(result['id']+'.png'); canvas.save(path)
        big = output/(result['id']+'-4x.png')
        canvas.resize((width*4,height*4),Image.Resampling.NEAREST).save(big)
        result.update(image=path.name,image_sha256=digest(path.read_bytes()),preview=big.name)
        results.append(result)
    report = {'schema_version':1,'status':'CPU_REPLAY_NOT_G3_ACCEPTANCE',
              'recording_sha256':digest(raw),'candidate_package_manifest_sha256':digest(manifest_raw),
              'renderer_source_sha256':digest(Path(__file__).read_bytes()),
              'guard_producer_metadata':{'active':True,'positive_denials':0,'not_an_os_sandbox':True},
              'scenario_status_counts':dict(Counter(r['scenario_status'] for r in results)),
              'collision_scope':'dynamic text alpha only; excludes image, panel, shader and actual parent-clip collisions',
              'assets':identities,'software_projection':'screenTop supplied by original-font CPU quad recording; y-up image anchors',
              'color':'raw atlas RGBA; no shader, tint, fade, CRT or native rasterizer',
              'game_started':False,'parent_clip_verified':False,'results':results}
    (output/'replay-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(output),'scenarios':len(results),
                      'status':report['status'],'overlap_pixels':{r['id']:r['text_overlap_pixels'] for r in results}},ensure_ascii=False,indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recording',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,default=ROOT/'localization/builds/layout-r22-candidate-v2')
    args=parser.parse_args();run(args.recording,args.output,args.candidate)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');main()
