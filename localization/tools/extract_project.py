"""Create the immutable, provenance-complete effective resource/text/image catalog."""
from pathlib import Path
import os
import collections
import csv
import html
import io
import json
import re
import shutil
import sys
import zipfile

from projectlib import *
from codec import decrypt_file
from classfile import load,disasm
from PIL import Image

WORK=PROJECT.parent
GAME=Path(os.environ.get('COSMOBREEDER_GAME_DIR', WORK/'.local/game'))
ARCHIVES=[('jar',GAME/'cosmobreeder-multi.jar'),('patch',GAME/'patch.pak')]
FONT_NAMES={'bbc2','classic','dingbats','st','st2x','nes','japanese'}
FIXED_WORDS=re.compile(r'title|logo|text|tutorial|hint|button|menu|control|credit|help|hud|label|sign',re.I)
DS_ENTRY=re.compile(r'^\s*<([^>]+)>')
DS_SKIP=re.compile(r'^\s*(?:include\b|if\b|else\b|\}|do\b|#)')
DS_TEXT=re.compile(r'^(\s*\*\s?|\s*[^<>{}#*\s][^:]{0,40}:\s?)(.*)$')
VSN_TEXT=re.compile(r'^(\s*(?:text|lang\([^)]*\)|auto\([^)]*\))\s*:\s?)(.*)$')


def put_blob(data,extension):
    sha=digest(data);p=PROJECT/'sources/blobs'/(sha+extension.lower())
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():assert digest(p.read_bytes())==sha
    else:p.write_bytes(data)
    return sha,p.relative_to(PROJECT).as_posix()


def collect_resources():
    versions=collections.defaultdict(list);missing=[];archives=[]
    for tag,path in ARCHIVES:
        archives.append({'tag':tag,'path':str(path),'sha256':digest(path.read_bytes()),'bytes':path.stat().st_size})
        with zipfile.ZipFile(path) as z:
            names=set(z.namelist())
            for index_name in sorted(n for n in names if n.endswith('/0') and n.count('/')==1):
                group=index_name[:-2];idx=json.loads(decrypt_file(z.read(index_name)))
                for rel,slot in sorted(idx.items()):
                    key=group+'/'+rel.lstrip('/');entry=group+'/'+str(slot)
                    if entry not in names:
                        missing.append({'archive':tag,'logical_path':key,'entry':entry});continue
                    ext=Path(rel).suffix.lower();stored=ext!='.bank'
                    data=decrypt_file(z.read(entry)) if stored else None
                    sha,blob=put_blob(data,ext) if stored else ('','')
                    versions[key].append({'archive':tag,'archive_entry':entry,'group':group,'index_path':index_name,
                                          'index_key':rel,'slot':slot,'sha256':sha,'blob_path':blob,'materialized':stored,
                                          'plaintext_bytes':len(data) if stored else None})
            for name in sorted(n for n in names if '/' not in n and Path(n).suffix.lower() in {'.png','.fnt','.json','.txt'}):
                data=z.read(name);sha,blob=put_blob(data,Path(name).suffix)
                versions['plain/'+name].append({'archive':tag,'archive_entry':name,'group':'plain','index_key':name,
                                                'slot':None,'sha256':sha,'blob_path':blob,'materialized':True,'plaintext_bytes':len(data)})
    rows=[]
    for key,ver in sorted(versions.items()):
        rows.append({'resource_id':stable_id('R',key),'logical_path':key,**ver[-1],
                     'versions':ver,'overrides_jar':len(ver)>1,'version_payload_changed':len({v['sha256'] for v in ver})>1})
    write_json(PROJECT/'sources/archives.json',archives)
    write_jsonl(PROJECT/'catalog/resources.jsonl',rows)
    write_csv(PROJECT/'catalog/resource_versions.csv',
              [{'logical_path':r['logical_path'],'effective':v is r['versions'][-1],**v} for r in rows for v in r['versions']],
              ['logical_path','effective','archive','archive_entry','group','index_key','slot','sha256','blob_path','plaintext_bytes'])
    write_json(PROJECT/'reports/missing_index_entries.json',missing)
    return rows


class TextCatalog:
    def __init__(self):self.units={};self.occ=[];self.unclassified=[]
    def add(self,category,raw,location,variant='',speaker='',context='',prefix='',extra=None):
        leading,source,trailing=edge_parts(raw)
        if not source:return
        uid=stable_id({'dialogue':'D','vsn':'V','ui':'U','code':'C','image':'I'}[category],category,variant,speaker,source)
        if uid not in self.units:
            self.units[uid]={'id':uid,'category':category,'source':source,'source_sha256':source_hash(source),
                'variant':variant,'speaker':speaker,'legacy_id':('X' if category=='code' else category[0].upper())+__import__('hashlib').sha1(source.encode('utf8')).hexdigest()[:10],
                'protected_tokens':protected(source),'markers':marker_signature(source),'width_hint_px':240,
                'occurrence_count':0,'context_examples':[],'review_flags':['code_usage_unverified'] if category=='code' else []}
        u=self.units[uid];u['occurrence_count']+=1
        if context and context not in u['context_examples'] and len(u['context_examples'])<4:u['context_examples'].append(context)
        if category=='ui':u['width_hint_px']=max(len(x)*8 for x in re.split(r'\||\r?\n',source))
        oid=stable_id('O',category,location,source_hash(raw))
        self.occ.append({'occurrence_id':oid,'unit_id':uid,'category':category,'location':location,'context':context,
                         'variant':variant,'speaker':speaker,'prefix':prefix,'leading_ws':leading,'trailing_ws':trailing,
                         'raw_payload_sha256':source_hash(raw),**(extra or {})})
    def finish(self):
        units=list(self.units.values())
        write_jsonl(PROJECT/'catalog/units.jsonl',units);write_jsonl(PROJECT/'catalog/occurrences.jsonl',self.occ)
        write_csv(PROJECT/'catalog/occurrences.csv',self.occ,
                  ['occurrence_id','unit_id','category','location','archive','archive_entry','logical_path','line','json_key','json_pointer',
                   'entry','variant','speaker','context','prefix','leading_ws','trailing_ws','class_name','cp_index','utf8_index','method_refs',
                   'asset_id','image_path','fragment','transcription_notes','runtime_overlay_resource','runtime_overlay_pointer','runtime_overlay_source_differs'])
        write_json(PROJECT/'reports/unclassified_text_lines.json',self.unclassified)
        return units,self.occ


def nested_ui_records(data):
    for key,value in data.get('patchDictionary',{}).items():
        if isinstance(value,str):
            ptr='/patchDictionary/'+key.replace('~','~0').replace('/','~1')
            yield ptr,value,'',f'patchDictionary | {key}',['runtime_dictionary_overlay']
    for variant,shops in data.get('shops',{}).items():
        for shop,record in shops.items():
            for i,product in enumerate(record.get('products',[])):
                for field in ('displayName','displayOut'):
                    value=product.get(field)
                    if isinstance(value,str):
                        ptr='/shops/'+variant+'/'+shop+'/products/'+str(i)+'/'+field
                        yield ptr,value,variant,f'shop {shop} | {field} | raw branch {variant}',['raw_variant_semantics_unverified']
    for variant,entries in data.get('missionLog',{}).items():
        for i,entry in enumerate(entries):
            for field in ('header','text','subject','locationName'):
                value=entry.get(field)
                if isinstance(value,str):
                    ptr='/missionLog/'+variant+'/'+str(i)+'/'+field
                    flags=['raw_variant_semantics_unverified']
                    if re.search(r'(?i)(test|stub)',entry.get('id','')) or re.match(r'(?:Lorem ipsum|Line 1|Stub|Test )',value):flags.append('development_placeholder_or_test_data')
                    yield ptr,value,variant,f'mission {entry.get("id",i)} | {field} | raw branch {variant}',flags


def add_nested_ui(catalog,resource):
    data=read_json(resource_path(resource));key=resource['logical_path']
    common={'logical_path':key,'resource_id':resource['resource_id'],'archive':resource['archive'],'archive_entry':resource['archive_entry']}
    for pointer,value,variant,context,flags in nested_ui_records(data):
        before=len(catalog.occ)
        catalog.add('ui',value,key+'#'+pointer,variant=variant,context=context,
                    extra={**common,'json_pointer':pointer,'raw_branch':variant,'source_review_flags':flags})
        if len(catalog.occ)>before:
            u=catalog.units[catalog.occ[-1]['unit_id']]
            for flag in flags:
                if flag not in u['review_flags']:u['review_flags'].append(flag)
    patch=data.get('patchDictionary',{})
    for o in catalog.occ:
        if o.get('logical_path')=='datav/dictionary.json' and o.get('json_key') in patch:
            o['runtime_overlay_pointer']='/patchDictionary/'+o['json_key'].replace('~','~0').replace('/','~1')
            o['runtime_overlay_resource']=key
            o['runtime_overlay_source_differs']=catalog.units[o['unit_id']]['source']!=str(patch[o['json_key']]).strip()


def collect_text(resources):
    catalog=TextCatalog()
    for r in resources:
        key=r['logical_path'];ext=Path(key).suffix
        common={'logical_path':key,'resource_id':r['resource_id'],'archive':r['archive'],'archive_entry':r['archive_entry']}
        if ext in ('.ds','.vsn'):
            text=resource_path(r).read_bytes().decode('utf8');entry='';variant='female' if key.startswith('datadf/') or '/f_' in key else 'male' if key.startswith('datadm/') or '/m_' in key else 'shared'
            lines=text.splitlines(keepends=True)
            for number,line in enumerate(lines,1):
                body=line[:-2] if line.endswith('\r\n') else line[:-1] if line.endswith('\n') else line
                if ext=='.ds':
                    m=DS_ENTRY.match(body)
                    if m:entry=m.group(1);continue
                    if not body.strip() or DS_SKIP.match(body):continue
                    m=DS_TEXT.match(body)
                else:m=VSN_TEXT.match(body)
                if not m:
                    if ext=='.ds':catalog.unclassified.append({'path':key,'line':number,'text':body})
                    continue
                prefix,payload=m.groups();speaker=prefix.strip().rstrip(':').strip() if ext=='.ds' else 'narrator'
                category='dialogue' if ext=='.ds' else 'vsn'
                context=f'{key} | {entry or Path(key).parent.name} | line {number}'
                catalog.add(category,payload,f'{key}#L{number}',variant,speaker,context,prefix,
                            {**common,'line':number,'entry':entry,'previous_line':lines[number-2].strip() if number>1 else '',
                             'next_line':lines[number].strip() if number<len(lines) else ''})
        elif key=='datav/dictionary.json':
            for name,value in sorted(read_json(resource_path(r)).items()):
                if isinstance(value,str):catalog.add('ui',value,key+'#'+name,context=name,extra={**common,'json_key':name})
        elif key=='datay/scripts_pack.json':
            add_nested_ui(catalog,r)
    legacy={row['source'] for row in read_csv(PROJECT/'reference/legacy-code-candidates.csv')}
    code_inventory=[]
    # Do not extract obfuscated class files into a case-insensitive loose directory.
    with zipfile.ZipFile(GAME/'cosmobreeder-multi.jar') as z:
        for name in sorted(n for n in z.namelist() if n.startswith('PRG/') and n.endswith('.class')):
            cf=load(z.read(name));literals={i:cf.cp.utf8(v[1]) for i,v in cf.cp.items.items() if v[0]==8}
            if not literals:continue
            used=collections.defaultdict(list)
            for m in cf.methods:
                code,_=cf.code_of(m)
                if code is None:continue
                for pc,op,arg in disasm(cf,code):
                    if op in ('ldc','ldc_w'):
                        idx=int(arg.split(' ',1)[0][1:])
                        if idx in literals:used[idx].append(f'{m["name"]}{m["desc"]}@{pc}')
            stem=Path(name).stem.split('$')[0]
            game_owned=len(stem)<=2 or bool(re.fullmatch(r'a[a-m][A-Za-z]',stem))
            for i,source in literals.items():
                stripped=source.strip();candidate=stripped in legacy
                if game_owned and 2<=len(stripped)<=180 and stripped.isprintable():
                    candidate|=bool((re.search(r'[A-Za-z]{2,} [A-Za-z]{2,}',stripped) or re.fullmatch(r'[A-Z][A-Z 0-9!?.,:%\x27-]{1,60}',stripped))
                                    and not any(c in stripped for c in '/\\;$<>_{}') and stripped not in {'PRG','MODULE','UTF-8','ASCII','ERROR','WARNING'})
                if not candidate:continue
                utf=cf.cp.items[i][1]
                row={'class_name':name,'cp_index':i,'utf8_index':utf,'source':source,'method_refs':used[i],
                     'usage_review':'unverified','game_owned_heuristic':game_owned}
                code_inventory.append(row)
                catalog.add('code',source,f'{name}#CP{i}',context=name+' | '+', '.join(used[i][:2]),
                            extra={**row,'archive':'jar','archive_entry':name,'logical_path':'class/'+name})
    write_jsonl(PROJECT/'catalog/code_string_locations.jsonl',code_inventory)
    # Potentially player-facing JSON outside dictionary is inventoried, never blindly translated.
    candidates=[]
    def walk(value,pointer=''):
        if isinstance(value,dict):
            for k,v in value.items():yield from walk(v,pointer+'/'+str(k).replace('~','~0').replace('/','~1'))
        elif isinstance(value,list):
            for i,v in enumerate(value):yield from walk(v,pointer+'/'+str(i))
        elif isinstance(value,str) and re.search(r'[A-Za-z]{2,} [A-Za-z]{2,}',value) and len(value)<2000:yield pointer,value
    for r in resources:
        key=r['logical_path']
        if not key.endswith('.json') or key=='datav/dictionary.json' or '/hash.json' in key:continue
        for pointer,value in walk(read_json(resource_path(r))):candidates.append({'logical_path':key,'json_pointer':pointer,'source':value,'status':'needs_triage'})
    write_csv(PROJECT/'catalog/additional_json_candidates.csv',candidates,['logical_path','json_pointer','source','status'])
    return catalog.finish()


def collect_images(resources):
    lookup={r['logical_path']:r for r in resources};all_regions=[];images=[];animations=[];fixed=[]
    raw_dir=PROJECT/'assets/source';raw_dir.mkdir(parents=True,exist_ok=True)
    fixed_dir=PROJECT/'assets/fixed';fixed_dir.mkdir(parents=True,exist_ok=True)
    preview_dir=PROJECT/'assets/scene_previews';preview_dir.mkdir(parents=True,exist_ok=True)
    for r in resources:
        if r['logical_path'].endswith('.png'):
            p=raw_dir/(r['resource_id']+'.png');shutil.copyfile(resource_path(r),p)
            with Image.open(p) as im:dimensions=list(im.size)
            images.append({'image_id':r['resource_id'],'logical_path':r['logical_path'],'archive':r['archive'],
                           'archive_entry':r['archive_entry'],'sha256':r['sha256'],'dimensions':dimensions,
                           'path':p.relative_to(PROJECT).as_posix()})
    for r in resources:
        key=r['logical_path']
        if not key.endswith('.atlas'):continue
        pages,regions=parse_atlas(resource_path(r).read_text(encoding='utf8'));page_images={}
        parent=key.rsplit('/',1)[0];counts=collections.Counter(x['name'] for x in regions)
        for page in pages:
            page_key=parent+'/'+page['name'];pr=lookup[page_key]
            page_images[page['name']]=Image.open(resource_path(pr)).convert('RGBA')
        main=key=='dataq/sprites.atlas'
        for region in regions:
            image=page_images[region['page']];x,y=region['xy'];w,h=region['size'];rot=region['rotation']
            assert rot in (0,90), (key,region)
            pw,ph=(h,w) if rot else (w,h)
            assert 0<=x<=x+pw<=image.width and 0<=y<=y+ph<=image.height,(key,region)
            aid=stable_id('A',key,region['ordinal'],region['name'],region['index'])
            row={'asset_id':aid,'atlas':key,'atlas_resource_id':r['resource_id'],'archive':r['archive'],'archive_entry':r['archive_entry'],
                 'page_logical_path':parent+'/'+region['page'],'page_resource_id':lookup[parent+'/'+region['page']]['resource_id'],
                 **{k:region[k] for k in ('name','ordinal','index','xy','size','orig','offset','rotation')},'atlas_line':region['line']}
            all_regions.append(row)
            if main and (counts[region['name']]==1 or FIXED_WORDS.search(region['name'])):
                crop=image.crop((x,y,x+pw,y+ph))
                if rot:crop=crop.transpose(Image.Transpose.ROTATE_90)
                assert list(crop.size)==region['size']
                p=fixed_dir/(aid+'.png');crop.save(p)
                role='font_reference' if region['name'] in FONT_NAMES else 'name_matched_text_candidate' if FIXED_WORDS.search(region['name']) else 'static_unreviewed'
                fixed.append({**row,'path':p.relative_to(PROJECT).as_posix(),'role':role,'text_verified':False,
                              'source_transcription':'','translation':'','status':'needs_visual_review','review_notes':''})
        if key.startswith('vsn/'):
            slices_key=parent+'/slices.json';metadata_key=parent+'/metadata.json'
            if slices_key in lookup:
                slices=read_json(resource_path(lookup[slices_key]));metadata=read_json(resource_path(lookup[metadata_key]))
                by_name={rr['name']:rr for rr in regions}
                for name,frames in slices.items():
                    anim_id=stable_id('S',parent,name);meta=metadata.get(name,{})
                    animations.append({'animation_id':anim_id,'scene':parent,'name':name,'frame_count':len(frames),
                                       'slices_resource_id':lookup[slices_key]['resource_id'],'atlas_resource_id':r['resource_id'],
                                       'frames':frames,'metadata':meta})
                    if not frames:continue
                    first=frames[0];canvas=Image.new('RGBA',(256,len(first)*16),(0,0,0,0));complete=True
                    for j,slice_id in enumerate(first):
                        reg=by_name.get(f'i_{slice_id}_slice')
                        if reg is None:complete=False;break
                        sx,sy=reg['xy'];sw,sh=reg['size'];assert reg['rotation']==0
                        part=page_images[reg['page']].crop((sx,sy,sx+sw,sy+sh))
                        if part.size!=(256,16):complete=False;break
                        canvas.paste(part,(0,j*16))
                    if complete:
                        p=preview_dir/(anim_id+'.png');canvas.save(p);animations[-1]['first_frame_preview']=p.relative_to(PROJECT).as_posix()
        for im in page_images.values():im.close()
    write_jsonl(PROJECT/'catalog/atlas_regions.jsonl',all_regions)
    write_jsonl(PROJECT/'catalog/scene_animations.jsonl',animations)
    write_csv(PROJECT/'catalog/images.csv',images,['image_id','logical_path','archive','archive_entry','sha256','dimensions','path'])
    write_jsonl(PROJECT/'catalog/fixed_images.jsonl',fixed)
    write_csv(PROJECT/'review/fixed_images.csv',fixed,['asset_id','name','index','role','path','atlas','page_logical_path','xy','size','orig','offset',
              'source_transcription','translation','status','review_notes'])
    cards=[]
    for r in sorted(fixed,key=lambda x:(x['role']!='name_matched_text_candidate',x['name'],x['index'])):
        cards.append('<article><h3>'+html.escape(r['name'])+' / '+str(r['index'])+'</h3><img loading="lazy" src="../'+html.escape(r['path'])+'"><p>'+html.escape(r['asset_id'])+' · '+r['role']+'</p></article>')
    page='<!doctype html><meta charset="utf-8"><title>固定图像资产核对</title><style>body{background:#222;color:#eee;font:14px sans-serif}main{display:flex;flex-wrap:wrap;gap:12px}article{border:1px solid #777;padding:8px;width:340px}img{image-rendering:pixelated;max-width:320px;max-height:280px;background:#555}h3,p{overflow-wrap:anywhere}</style><h1>固定图像资产核对</h1><p>含原游戏成人素材，仅限本地授权校对。名称匹配只是候选，不是 OCR 结论。图片未翻译；动画切片与完整定位另见 catalog。</p><main>'+''.join(cards)+'</main>'
    (PROJECT/'review/image_browser.html').write_text(page,encoding='utf8')
    return {'raw_images':len(images),'atlas_regions':len(all_regions),'fixed_crops':len(fixed),
            'name_matched_fixed_crops':sum(r['role']=='name_matched_text_candidate' for r in fixed),
            'scene_animations':len(animations),'scene_first_frame_previews':sum('first_frame_preview' in a for a in animations)}


def main():
    if (PROJECT/'catalog/units.jsonl').exists():raise SystemExit('Catalog already exists; refuse to replace source identity or reviewer work.')
    resources=collect_resources();units,occ=collect_text(resources);image_stats=collect_images(resources)
    stats={'resources':len(resources),'resource_versions':sum(len(r['versions']) for r in resources),
           'units':len(units),'unit_categories':dict(collections.Counter(r['category'] for r in units)),
           'occurrences':len(occ),'occurrence_categories':dict(collections.Counter(r['category'] for r in occ)),
           'source_characters':sum(len(u['source']) for u in units),'images':image_stats}
    write_json(PROJECT/'reports/extraction-summary.json',stats);print(json.dumps(stats,ensure_ascii=False,indent=2))


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
