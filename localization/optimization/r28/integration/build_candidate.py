"""Build an isolated r28 candidate incrementally from frozen r27.

No install, launcher, game entry, save/Steam access, network, or Git operations.
Outputs must be NEW directories. Component sources/resources are identity-snapshotted.
A build manifest says candidate/partial; it never implies real GPU/CRT/input acceptance.
"""
from pathlib import Path
from io import BytesIO
import argparse, hashlib, importlib, json, os, re, subprocess, sys, zipfile
from PIL import Image
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent; OPT=HERE.parent
TOOLS=ROOT/'localization/tools';sys.path.insert(0,str(TOOLS))
from codec import decrypt_file,encrypt_file
from projectlib import parse_atlas
import optimized_fonts
BASE=ROOT/'localization/builds/r27-story12-shaderfix-test5'
BASE_PINS={'cosmobreeder-multi.jar':'dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be','patch.pak':'d2e21deeb85d74e981770b247625ee7ceb7ed39ae566305c1833c2c3d97b54d5'}
JDK=ROOT/'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
JRE=ROOT/'research/testgame_cjk_verified/jre/bin/java.exe'
EXPORTS=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','--add-exports','java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']
COMPONENTS=['core','pattern','compact','scenes','sfw','vsn','images','radio','editorial','names','r4pending','r5creative','r6consistency','r8puzzle','r9polish']
LICENSE8=['boutique-bitmap-7x7/OFL.txt','galmuri/LICENSE.txt','misaki/misaki.txt','miseki-bitmap/LICENSE.txt']
sha=lambda b:hashlib.sha256(b).hexdigest()
file_sha=lambda p:sha(p.read_bytes())

def checked_source(name):
    p=(ROOT/name).resolve()
    if not p.is_relative_to(ROOT) or not p.is_file():raise ValueError('Missing/outside source: '+name)
    return p

def seal(data):
    value=encrypt_file(data,os.urandom(32),os.urandom(8))
    if decrypt_file(value)!=data:raise ValueError('Resource encryption roundtrip')
    return value

def rewrite(source,target,replacements):
    with zipfile.ZipFile(source) as before,zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as after:
        names=set(before.namelist())
        for info in before.infolist():after.writestr(info,replacements.get(info.filename,before.read(info.filename)))
        for name,data in sorted(replacements.items()):
            if name not in names:after.writestr(name,data)
    with zipfile.ZipFile(source) as before,zipfile.ZipFile(target) as after:
        if after.testzip() is not None:raise ValueError('Archive CRC')
        for name in set(before.namelist())-set(replacements):
            if before.read(name)!=after.read(name):raise AssertionError('Unrelated archive entry changed: '+name)

def gather_text(value):
    if isinstance(value,str):return [value]
    if isinstance(value,dict):return [s for v in value.values() for s in gather_text(v)]
    if isinstance(value,list):return [s for v in value for s in gather_text(v)]
    return []

def resources(selected,components,work):
    replacements={name:{} for name in BASE_PINS};reports={};texts=[]
    for name in selected:
        chars=components[name].get('required_chars',[])
        if isinstance(chars,str):
            p=ROOT/chars;texts.append(p.read_text('utf8') if p.is_file() else chars)
        elif isinstance(chars,list):texts.extend(chars)
    if 'vsn' in selected:
        import vsn_joins
        count=0;rv=[]
        with zipfile.ZipFile(BASE/'patch.pak') as z:
            for logical,record in components['vsn']['resources'].items():
                entry=record['archive_entry'];raw=decrypt_file(z.read(entry))
                new,report=vsn_joins.rewrite_vsn(logical,raw,archive='patch.pak')
                if new!=raw:replacements['patch.pak'][entry]=seal(new);count+=1
                texts.append(new.decode('utf8'))
                rv.append(report)
        reports['vsn']={'resources_changed':count,'resources':rv}
        ds_dir=OPT/'vsn/ds-polish';sys.path.insert(0,str(ds_dir))
        from ds_polish import rewrite_ds_polish
        ds_manifest=json.loads((ds_dir/'component_ds.json').read_text('utf8'));ds_reports=[]
        texts.append((ds_dir/'required_chars.txt').read_text('utf8'))
        with zipfile.ZipFile(BASE/'patch.pak') as z:
            for logical,record in ds_manifest['resources'].items():
                entry=record['archive_entry'];raw=decrypt_file(z.read(entry))
                new,report=rewrite_ds_polish(logical,raw,archive='patch.pak')
                replacements['patch.pak'][entry]=seal(new);texts.append(new.decode('utf8'));ds_reports.append(report)
        reports['ds_polish']=ds_reports
    if 'sfw' in selected:
        # This adapter is deliberately explicit; no arbitrary function in metadata executes.
        import sfw_localization
        import dialogue_joins
        value=sfw_localization.rebuild_candidate_entries(ROOT/'backup/cosmobreeder-multi.jar',
            data_dir=OPT/'sfw',canonical_join_records=dialogue_joins.load_records(),
            allow_pattern_candidates=True)
        if not isinstance(value,tuple) or len(value)!=2:raise ValueError('SFW API must return (plaintext entry dict, report)')
        plain,report=value
        for entry,data in plain.items():
            if not isinstance(data,bytes):raise TypeError('SFW plaintext bytes required')
            replacements['cosmobreeder-multi.jar'][entry]=seal(data)
            if entry.startswith('datav/'):
                texts.extend(gather_text(json.loads(data)))
            elif entry.startswith(('vsn/','datadf/','datadm/')):
                texts.append(data.decode('utf8'))
        reports['sfw']=report
    if 'editorial' in selected:
        import editorial_repairs
        component=components['editorial']
        ledger_path=checked_source(component['ledger'])
        editorial_manifest=json.loads(checked_source(component['review_manifest']).read_text('utf8'))
        if editorial_manifest['status']!='validated_full_repair_candidate' or not editorial_manifest['full_339_coverage']:
            raise ValueError('Editorial component requires full source-validated 339-decision ledger')
        if file_sha(ledger_path)!=editorial_manifest['operations_sha256']:
            raise ValueError('Editorial operation ledger drift')
        for filename,pin in editorial_manifest['source_sha256'].items():
            if file_sha(checked_source(filename))!=pin:raise ValueError('Editorial author source drift: '+filename)
        semantic=json.loads(checked_source(component['semantic_manifest']).read_text('utf8'))
        if (semantic['status']!='passed_scoped_repair_semantic_review_not_global_proofread'
                or semantic['findings_checked']!=339 or semantic['operations_sha256']!=file_sha(ledger_path)):
            raise ValueError('Editorial semantic closure does not match this exact operation ledger')
        for filename,pin in semantic['evidence_sha256'].items():
            if file_sha(checked_source(filename))!=pin:raise ValueError('Editorial semantic evidence drift: '+filename)
        operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations})
        original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:
                        original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        repaired,editorial_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in repaired.items():
            replacements[archive][entry]=seal(data)
            texts.append(data.decode('utf8'))
        reports['editorial']={'ledger_sha256':file_sha(ledger_path),'decision_count':editorial_manifest['decision_count'],
            'decision_actions':editorial_manifest['decision_actions'],'resource_reports':editorial_reports,
            'installed':False,'semantic_review_is_separate':True}
    if 'names' in selected:
        import editorial_repairs
        component=components['names']
        registry_path=checked_source(component['registry']);ledger=checked_source(component['ledger'])
        registry=json.loads(registry_path.read_text('utf8'))
        name_manifest=json.loads(checked_source(component['manifest']).read_text('utf8'))
        review_path=checked_source(registry['semantic_review']['path'])
        review=json.loads(review_path.read_text('utf8'))
        carrier_review=json.loads(checked_source(component['carrier_review']).read_text('utf8'))
        if (registry['status']!='reviewed_for_application' or len(registry['names'])!=36
                or file_sha(review_path)!=registry['semantic_review']['sha256']
                or any(n['blocking_issues'] for n in review['names'])
                or {n['name_id']:n['target'] for n in registry['names']}!={n['name_id']:n['target'] for n in review['names']}
                or carrier_review['status']!='PASS'):
            raise ValueError('Names require exact independently reviewed registry and carrier boundaries')
        if (name_manifest['all_entry_preflight']!='passed'
                or file_sha(registry_path)!=name_manifest['registrySHA']
                or file_sha(ledger)!=name_manifest['operationsSHA']
                or file_sha(checked_source(component['inventory']))!=name_manifest['inventorySHA']
                or file_sha(checked_source(component['compiler']))!=name_manifest['compilerSHA']):
            raise ValueError('Names source compilation drift')
        for filename,pin in carrier_review['evidence_sha256'].items():
            if file_sha(checked_source(filename))!=pin:raise ValueError('Names carrier evidence drift: '+filename)
        for archive,pin in name_manifest['baseline_archiveSHA'].items():
            if file_sha(checked_source(name_manifest['baseline']+'/'+archive))!=pin:raise ValueError('Names baseline drift')
        subprocess.run([sys.executable,'-B',str(checked_source(component['sync_tool'])),'--check'],cwd=ROOT,check=True)
        operations=[json.loads(line) for line in ledger.read_text('utf8').splitlines() if line.strip()]
        if len(operations)!=name_manifest['operation_count']:raise ValueError('Names operation count')
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        renamed,name_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in renamed.items():
            replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
        reports['names']={'registry_sha256':file_sha(registry_path),'operations_sha256':file_sha(ledger),
            'names_reviewed':36,'operation_count':len(operations),'resource_reports':name_reports,
            'r2_preservation':name_manifest['r2_preservation']['non_name_preserved'],'installed':False}
    if 'r4pending' in selected:
        import editorial_repairs
        component=components['r4pending']
        ledger_path=checked_source(component['ledger'])
        gate=json.loads(checked_source(component['gate']).read_text('utf8'))
        if gate['status']!='verified_for_application':
            raise ValueError('R4 gate is not verified')
        if file_sha(ledger_path)!=gate['ledger_sha256']:raise ValueError('R4 operation ledger drift')
        if file_sha(checked_source(component['decisions']))!=gate['decisions_sha256']:raise ValueError('R4 decisions drift')
        if file_sha(checked_source(component['evidence']))!=gate['evidence_sha256']:raise ValueError('R4 evidence drift')
        if file_sha(checked_source(gate['verifier']['path']))!=gate['verifier']['sha256']:raise ValueError('R4 verifier drift')
        operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
        if len(operations)!=gate['operations']:raise ValueError('R4 operation count')
        if sorted({op['finding_ids'][0] for op in operations})!=gate['apply_findings']:raise ValueError('R4 apply findings drift')
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        repaired,r4_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in repaired.items():
            replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
        reports['r4pending']={'ledger_sha256':file_sha(ledger_path),'operation_count':len(operations),
            'decisions_total':gate['decisions_total'],'apply_findings':gate['apply_findings'],
            'resource_reports':r4_reports,'gate':'verified_for_application','installed':False}
    if 'r5creative' in selected:
        import editorial_repairs
        component=components['r5creative']
        ledger_path=checked_source(component['ledger'])
        gate=json.loads(checked_source(component['gate']).read_text('utf8'))
        if gate['status']!='verified_for_application':
            raise ValueError('R5 gate is not verified')
        if file_sha(ledger_path)!=gate['ledger_sha256']:raise ValueError('R5 operation ledger drift')
        if file_sha(checked_source(component['decisions']))!=gate['decisions_sha256']:raise ValueError('R5 decisions drift')
        if file_sha(checked_source(gate['verifier']['path']))!=gate['verifier']['sha256']:raise ValueError('R5 verifier drift')
        operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
        if len(operations)!=gate['operations']:raise ValueError('R5 operation count')
        if sorted({op['finding_ids'][0] for op in operations})!=gate['apply_findings']:raise ValueError('R5 apply findings drift')
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        rewritten,r5_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in rewritten.items():
            replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
        reports['r5creative']={'ledger_sha256':file_sha(ledger_path),'operation_count':len(operations),
            'decisions_total':gate['decisions_total'],'apply_findings':gate['apply_findings'],
            'resource_reports':r5_reports,'gate':'verified_for_application','installed':False}
    if 'r6consistency' in selected:
        import editorial_repairs
        component=components['r6consistency']
        ledger_path=checked_source(component['ledger'])
        gate=json.loads(checked_source(component['gate']).read_text('utf8'))
        if gate['status']!='verified_for_application':
            raise ValueError('R6 gate is not verified')
        if file_sha(ledger_path)!=gate['ledger_sha256']:raise ValueError('R6 operation ledger drift')
        if file_sha(checked_source(component['decisions']))!=gate['decisions_sha256']:raise ValueError('R6 decisions drift')
        if file_sha(checked_source(gate['verifier']['path']))!=gate['verifier']['sha256']:raise ValueError('R6 verifier drift')
        operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
        if len(operations)!=gate['operations']:raise ValueError('R6 operation count')
        if sorted({op['finding_ids'][0] for op in operations})!=gate['apply_findings']:raise ValueError('R6 apply findings drift')
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        fixed,r6_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in fixed.items():
            replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
        reports['r6consistency']={'ledger_sha256':file_sha(ledger_path),'operation_count':len(operations),
            'decisions_total':gate['decisions_total'],'apply_findings':gate['apply_findings'],
            'resource_reports':r6_reports,'gate':'verified_for_application','installed':False}
    if 'r8puzzle' in selected:
        import editorial_repairs
        component=components['r8puzzle']
        ledger_path=checked_source(component['ledger'])
        gate=json.loads(checked_source(component['gate']).read_text('utf8'))
        if gate['status']!='verified_for_application':
            raise ValueError('R8 gate is not verified')
        if file_sha(ledger_path)!=gate['ledger_sha256']:raise ValueError('R8 operation ledger drift')
        if file_sha(checked_source(component['decisions']))!=gate['decisions_sha256']:raise ValueError('R8 decisions drift')
        if file_sha(checked_source(gate['verifier']['path']))!=gate['verifier']['sha256']:raise ValueError('R8 verifier drift')
        operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
        if len(operations)!=gate['operations']:raise ValueError('R8 operation count')
        if sorted({op['finding_ids'][0] for op in operations})!=gate['apply_findings']:raise ValueError('R8 apply findings drift')
        entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
        for archive in BASE_PINS:
            with zipfile.ZipFile(BASE/archive) as z:
                for name,entry in entry_keys:
                    if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
        fixed,r8_reports=editorial_repairs.apply_entries(original_entries,operations)
        for (archive,entry),data in fixed.items():
            replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
        reports['r8puzzle']={'ledger_sha256':file_sha(ledger_path),'operation_count':len(operations),
            'decisions_total':gate['decisions_total'],'apply_findings':gate['apply_findings'],
            'resource_reports':r8_reports,'gate':'verified_for_application','installed':False}
    if 'r9polish' in selected:
        import editorial_repairs
        component=components['r9polish']
        batches=component.get('batches') or [component]
        for index,batch in enumerate(batches,1):
            label='r9polish' if len(batches)==1 else 'r9polish-%02d' % index
            ledger_path=checked_source(batch['ledger'])
            gate=json.loads(checked_source(batch['gate']).read_text('utf8'))
            if gate['status']!='verified_for_application':
                raise ValueError('%s gate is not verified' % label)
            if file_sha(ledger_path)!=gate['ledger_sha256']:raise ValueError('%s operation ledger drift' % label)
            if file_sha(checked_source(batch['decisions']))!=gate['decisions_sha256']:raise ValueError('%s decisions drift' % label)
            if file_sha(checked_source(gate['verifier']['path']))!=gate['verifier']['sha256']:raise ValueError('%s verifier drift' % label)
            operations=[json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
            if len(operations)!=gate['operations']:raise ValueError('%s operation count' % label)
            if sorted({op['finding_ids'][0] for op in operations})!=gate['apply_findings']:raise ValueError('%s apply findings drift' % label)
            entry_keys=sorted({(op['archive'],op['archive_entry']) for op in operations});original_entries={}
            for archive in BASE_PINS:
                with zipfile.ZipFile(BASE/archive) as z:
                    for name,entry in entry_keys:
                        if name==archive:original_entries[(archive,entry)]=decrypt_file(replacements[archive].get(entry,z.read(entry)))
            polished,batch_reports=editorial_repairs.apply_entries(original_entries,operations)
            for (archive,entry),data in polished.items():
                replacements[archive][entry]=seal(data);texts.append(data.decode('utf8'))
            reports[label]={'ledger_sha256':file_sha(ledger_path),'operation_count':len(operations),
                'decisions_total':gate['decisions_total'],'apply_findings':gate['apply_findings'],
                'resource_reports':batch_reports,'gate':'verified_for_application','installed':False}
    # Include final display resources/derived char ledgers rather than only original catalog.
    for archive in BASE_PINS:
        with zipfile.ZipFile(BASE/archive) as z:
            for key in ['datav/1']:
                plain=decrypt_file(replacements[archive].get(key,z.read(key)))
                texts.extend(gather_text(json.loads(plain)))
    font_assets=optimized_fonts.build_assets(BASE/'cosmobreeder-multi.jar',texts)
    (work/'font-manifest.json').write_text(json.dumps(font_assets['manifest'],ensure_ascii=False,indent=2),encoding='utf8')
    (work/'fonts').mkdir()
    for filename,data in font_assets['fnts'].items():(work/'fonts'/filename).write_bytes(data)
    (work/'fonts/bbc2-10px.fnt').write_bytes(font_assets['fnts']['bbc2.fnt'])
    with zipfile.ZipFile(BASE/'cosmobreeder-multi.jar') as z:(work/'fonts/dingbats.fnt').write_bytes(z.read('dingbats.fnt'))
    for archive in BASE_PINS:
        with zipfile.ZipFile(BASE/archive) as z:
            route=json.loads(decrypt_file(z.read('dataq/0')))
            _,regions=parse_atlas(decrypt_file(z.read('dataq/'+str(route['/sprites.atlas']))).decode('utf8'))
            page_entry='dataq/'+str(route['/sprites.png'])
            page=Image.open(BytesIO(decrypt_file(z.read(page_entry)))).convert('RGBA')
            original=page.copy()
            if 'images' in selected:
                import optimized_images
                page,image_report=optimized_images.apply_overrides(page,regions,'jar' if archive.endswith('.jar') else 'patch')
                reports['images_'+archive]=image_report
            # Font region overlay follows artwork checks, in disjoint atlas rectangles.
            for name,png in font_assets['png_regions'].items():
                role=next(r for r in regions if r['name']==name)
                new=Image.open(BytesIO(png)).convert('RGBA');x,y=role['xy']
                if list(new.size)!=role['size'] or role['rotation']:raise ValueError('Font overlay geometry')
                page.paste(new,(x,y))
            if page.tobytes()!=original.tobytes():
                b=BytesIO();page.save(b,format='PNG');replacements[archive][page_entry]=seal(b.getvalue())
            for filename,data in font_assets['fnts'].items():
                if filename in z.namelist() and z.read(filename)==data:continue
                replacements[archive][filename]=data
            # The frozen story12/ diagnostic bundle remains internally paired.
            # Expanded live fonts get a complete separate r28 diagnostic bundle.
            if font_assets['manifest']['added_rectangles']:
                for filename,data in font_assets['fnts'].items():
                    replacements[archive]['r28-font/'+filename]=data
                for name,png in font_assets['png_regions'].items():
                    replacements[archive]['r28-font/'+name+'.png']=png
                replacements[archive]['r28-font/manifest.json']=json.dumps(font_assets['manifest'],ensure_ascii=False,indent=2).encode('utf8')
                replacements[archive]['r28-font/OFL8.txt']=(ROOT/'work/item-font8/asset/OFL.txt').read_bytes()
                for license_name in LICENSE8:
                    replacements[archive]['r28-font/LICENSES8/'+license_name]=(ROOT/'work/item-font8/asset/LICENSES'/license_name).read_bytes()
                replacements[archive]['r28-font/NOTICE.txt']=('Additional glyph contribution: Fusion Pixel Font 2026.10.16, Copyright (c) 2022 TakWolf, SIL OFL 1.1. Native12 and native8 source SHA are recorded in manifest.json. New default10 cells are nearest-sampled derivatives of native12, not native10. Existing game ASCII/font pixels remain under the original rightsholders terms; OFL does not relicense game artwork. Full original font component notices remain in the frozen story12/ bundle.\n').encode('utf8')
    return replacements,reports,font_assets['manifest']

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--components',default=','.join(COMPONENTS))
    args=p.parse_args();selected=args.components.split(',')
    if len(set(selected))!=len(selected) or any(s not in COMPONENTS for s in selected):raise ValueError('Unknown/duplicate component')
    if 'names' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('Names require the full source-locked predecessor pipeline')
    if 'r4pending' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('R4 pending repairs require the full predecessor pipeline')
    if 'r5creative' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('R5 creative rewrites require the full predecessor pipeline')
    if 'r6consistency' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('R6 consistency repairs require the full predecessor pipeline')
    if 'r8puzzle' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('R8 puzzle hint rewrite requires the full predecessor pipeline')
    if 'r9polish' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('R9 prose polish requires the full predecessor pipeline')
    if 'editorial' in selected and set(selected)!=set(COMPONENTS):
        raise ValueError('Editorial repairs require all predecessor components for exact source-locked resources')
    if 'sfw' in selected and not {'core','pattern','scenes'}<=set(selected):
        raise ValueError('SFW candidate requires core, pattern and scenes: text layout, unreadable-language compatibility and all font pin owners')
    out=args.output.resolve()
    allowed=[(ROOT/'localization/builds').resolve(),(HERE/'builds').resolve()]
    if out.exists() or not any(out!=root and out.is_relative_to(root) for root in allowed):raise ValueError('New isolated output directory only')
    for filename,pin in BASE_PINS.items():
        if file_sha(BASE/filename)!=pin:raise ValueError('Frozen r27 archive drift')
    component_paths={name:checked_source('localization/optimization/r28/'+name+'/component.json') for name in selected}
    components={name:json.loads(path.read_text('utf8')) for name,path in component_paths.items()}
    out.mkdir(parents=True);(out/'logs').mkdir();(out/'classes').mkdir();(out/'tools').mkdir();(out/'staging-src').mkdir()
    manifest={'version':'r28-full-opt-candidate','status':'building','selected_components':selected,'full_component_set':set(selected)==set(COMPONENTS),'base_archives':BASE_PINS,'commands':[],'game_started':False,'user_save_accessed':False,'installed':False,'real_clip_CRT_input_verified':False}
    save=lambda:(out/'build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
    save()
    def run(label,argv):
        r=subprocess.run([str(a) for a in argv],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (out/'logs'/(label+'.log')).write_bytes(r.stdout)
        manifest['commands'].append({'name':label,'exit_code':r.returncode});save();print(label,'exit',r.returncode,flush=True)
        if r.returncode:raise RuntimeError('Inspect '+str(out/'logs'/(label+'.log')))
    runtime=sorted({f for c in components.values() for f in c.get('runtime_sources',c.get('runtime',[]))})
    tools=sorted({f for c in components.values() for f in c.get('tool_sources',c.get('tools',[]))+c.get('tool_dependencies',[])})
    # No runtime source is compiled until every selected source exists and is snapshotted.
    sources=[checked_source(n) for n in runtime+tools]+list(component_paths.values())+[Path(__file__),HERE/'IncrementalPatchDriver.java',TOOLS/'optimized_fonts.py',TOOLS/'layout_fonts.py',TOOLS/'build_story_font12.py',TOOLS/'build_item_font8.py',TOOLS/'codec.py',TOOLS/'projectlib.py',ROOT/'work/item-font8/asset/OFL.txt']
    sources.extend(ROOT/'work/item-font8/asset/LICENSES'/name for name in LICENSE8)
    for name,c in components.items():
        api=c.get('api'); module=api.get('module') if isinstance(api,dict) else api
        if isinstance(module,str) and module.endswith('.py'):sources.append(checked_source(module))
        for filename in c.get('required_data',[]):sources.append(checked_source('localization/optimization/r28/'+name+'/'+filename))
        for batch in c.get('batches') or []:
            for filename in batch.get('required_data',[]):
                sources.append(checked_source('localization/optimization/r28/'+name+'/'+filename))
        chars=c.get('required_chars')
        charfile=chars.get('file') if isinstance(chars,dict) else chars
        if isinstance(charfile,str) and charfile.startswith('localization/') and charfile.endswith(('.txt','.json')):sources.append(checked_source(charfile))
        if name=='vsn':
            sources.append(OPT/'vsn/operations.jsonl')
            sources.extend(OPT/'vsn/ds-polish'/filename for filename in ['component_ds.json','ds_polish.py','operations.jsonl','review-ledger.jsonl','derived-skips.json','required_chars.txt'])
        if name=='names':
            carrier_review=json.loads(checked_source(c['carrier_review']).read_text('utf8'))
            sources.extend(checked_source(filename) for filename in carrier_review['evidence_sha256'])
        if name=='sfw':sources.extend([TOOLS/'dialogue_joins.py',TOOLS/'dialogue_sfw.py'])
        if name=='editorial':
            repair_manifest=json.loads(checked_source(c['review_manifest']).read_text('utf8'))
            sources.extend(checked_source(filename) for filename in repair_manifest['source_sha256'])
            semantic=json.loads(checked_source(c['semantic_manifest']).read_text('utf8'))
            sources.extend(checked_source(filename) for filename in semantic['evidence_sha256'])
        if name=='images':
            image_manifest=checked_source(c['manifest']);sources.append(image_manifest)
            for row in json.loads(image_manifest.read_text('utf8'))['replacements']:
                sources.extend([checked_source(row['newPNG']),checked_source(row['approved_mask'])])
    sources=sorted(set(sources))
    source_pins={str(path.relative_to(ROOT)).replace('\\','/'):file_sha(path) for path in sources}
    manifest['source_sha256']=source_pins;save()
    replacements,reports,font_manifest=resources(selected,components,out)
    font_owners={'default':'localization/layout/src/PRG/DialogueWrap.java',
                 'classic':'localization/layout/src/PRG/EndingReportLayout.java',
                 'story12':'localization/layout/src/PRG/StoryFont12.java'}
    for role,record in font_manifest['roles'].items():
        if record['original_sha256']!=record['sha256'] and font_owners[role] not in runtime:
            raise ValueError('Expanded '+role+' font requires recompiling its pin owner: '+font_owners[role])
    manifest['resource_reports']=reports;manifest['font_manifest']=font_manifest;save()
    font_pins={record['original_sha256']:record['sha256'] for record in font_manifest['roles'].values() if record['original_sha256']!=record['sha256']}
    compiled=[];pin_rewrites=[]
    pinned_sources={'localization/layout/src/PRG/DialogueWrap.java','localization/layout/src/PRG/StoryFont12.java','localization/layout/src/PRG/EndingReportLayout.java'}
    for source_name in runtime:
        source=checked_source(source_name);text=source.read_text('utf8');generated=text
        if source_name in pinned_sources:
            for old,new in font_pins.items():
                if old in generated:generated=generated.replace(old,new);pin_rewrites.append({'source':source_name,'old':old,'new':new})
        target=out/'staging-src'/source_name;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(generated,encoding='utf8');compiled.append(target)
    manifest['staged_font_pin_rewrites']=pin_rewrites;save()
    run('compile-runtime',[JDK/'javac.exe','--release','8','-encoding','UTF-8','-cp',BASE/'cosmobreeder-multi.jar','-d',out/'classes',*compiled])
    cp=os.pathsep.join(map(str,[out/'classes',BASE/'cosmobreeder-multi.jar']))
    run('compile-tools',[JDK/'javac.exe',*EXPORTS,'-encoding','UTF-8','-cp',cp,'-d',out/'tools',*[checked_source(f) for f in tools],HERE/'IncrementalPatchDriver.java',ROOT/'localization/layout/tools/java/VerifyLayout.java'])
    pins={};passes=[]
    for name,c in components.items():
        for cls,pin in c.get('target_pins',{}).items():
            cls=cls.removesuffix('.class')
            if cls in pins and pins[cls]!=pin:raise ValueError('Conflicting component pin '+cls)
            pins[cls]=pin
        if c.get('patcher_class'):
            method=c.get('patcher_method','apply');passes.append((c['patcher_class'],method))
        for item in c.get('patchers',[]):passes.append((item['class'],item.get('method','apply')))
    (out/'target-pins.tsv').write_text(''.join(n+'\t'+v+'\n' for n,v in sorted(pins.items())),encoding='utf8')
    (out/'patch-passes.tsv').write_text(''.join(n+'\t'+m+'\n' for n,m in passes),encoding='utf8')
    toolcp=os.pathsep.join(map(str,[out/'tools',out/'classes',BASE/'cosmobreeder-multi.jar']))
    run('patch-targets',[JDK/'java.exe',*EXPORTS,'-cp',toolcp,'IncrementalPatchDriver',BASE/'cosmobreeder-multi.jar',out/'classes',out/'target-pins.tsv',out/'patch-passes.tsv',out/'targets.jar'])
    with zipfile.ZipFile(out/'targets.jar') as z:code={n:z.read(n) for n in z.namelist()}
    for path in (out/'classes').rglob('*.class'):
        name=path.relative_to(out/'classes').as_posix();data=path.read_bytes()
        if not name.startswith(('PRG/','cosmoloc/layout/')) or int.from_bytes(data[6:8],'big')!=52:raise ValueError('Runtime class scope/version '+name)
        if name in code:raise ValueError('Helper/target ownership collision '+name)
        code[name]=data
    replacements['cosmobreeder-multi.jar'].update(code)
    for archive in BASE_PINS:rewrite(BASE/archive,out/archive,replacements[archive])
    (out/'classes.txt').write_text('\n'.join(n[:-6].replace('/','.') for n in code)+'\n',encoding='utf8')
    verifycp=os.pathsep.join(map(str,[out/'cosmobreeder-multi.jar',out/'tools']))
    run('verify-final-classes',[JRE,'-Dfile.encoding=UTF-8','-Xverify:all','-cp',verifycp,'VerifyLayout',out/'classes.txt'])
    for name,expected in source_pins.items():
        if file_sha(ROOT/name)!=expected:raise ValueError('Concurrent component source change: '+name)
    for filename,pin in BASE_PINS.items():
        if file_sha(BASE/filename)!=pin:raise ValueError('Frozen archive changed during build')
    manifest['archives']={name:{'sha256':file_sha(out/name),'bytes':(out/name).stat().st_size,'changed_entries':sorted(replacements[name])} for name in BASE_PINS}
    manifest['status']='integrated_candidate_not_real_clip_CRT_input_acceptance' if manifest['full_component_set'] else 'partial_integration_not_release'
    manifest['class_inventory']=sorted(code);save()
    print(json.dumps({'output':str(out.relative_to(ROOT)),'status':manifest['status'],'classes':len(code)},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
