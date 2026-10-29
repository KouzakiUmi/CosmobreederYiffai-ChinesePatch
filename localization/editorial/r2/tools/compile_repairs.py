"""Compile reviewed canonical-row edits into edition-specific source-locked ops.

Writes only a NEW r2/compiled child; no game/archive/old-ledger mutation.
"""
from pathlib import Path
from collections import defaultdict,Counter
from hashlib import sha256
import argparse,json,re,sys,zipfile

ROOT=Path(__file__).resolve().parents[4];LOC=ROOT/'localization';R1=LOC/'editorial/r1';R2=LOC/'editorial/r2'
sys.path.insert(0,str(LOC/'tools'))
from codec import decrypt_file
import editorial_repairs as engine


def rows(path):return [json.loads(s) for s in path.read_text('utf8').splitlines() if s.strip()]
def sha(data):return sha256(data).hexdigest()
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def pointer(parts):return '/'+ '/'.join(str(p).replace('~','~0').replace('/','~1') for p in parts)
def strings(value,parts=()):
    if isinstance(value,str):yield pointer(parts),value
    elif isinstance(value,dict):
        for k,v in value.items():yield from strings(v,parts+(k,))
    elif isinstance(value,list):
        for k,v in enumerate(value):yield from strings(v,parts+(str(k),))
def get(value,ptr):
    for p in ptr[1:].split('/'):
        p=p.replace('~1','/').replace('~0','~');value=value[int(p)] if isinstance(value,list) else value[p]
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--packets',nargs='*');p.add_argument('--corrections',type=Path)
    a=p.parse_args();out=a.output.resolve()
    if out.exists() or not out.is_relative_to(R2/'compiled'):raise ValueError('New r2/compiled child only')
    names=a.packets or ['packet-%02d'%n for n in range(1,11)]
    complete=set(names)=={'packet-%02d'%n for n in range(1,11)}
    original=rows(R1/'reports/rough-review-01/findings.jsonl');original_by={f['finding_id']:f for f in original}
    occ={r['occurrence_id']:r for r in rows(LOC/'catalog/occurrences.jsonl')}
    sfw={r['id']:r for k in ('ds','vsn','ui') for r in rows(LOC/('optimization/r28/sfw/ledger-'+k+'.jsonl'))}
    base=LOC/'builds/r28-radio-book-candidate4'
    identity=json.loads((base/'build-manifest.json').read_text('utf8'))
    archives={n:zipfile.ZipFile(base/n) for n in ('cosmobreeder-multi.jar','patch.pak')}
    for n in archives:
        if sha((base/n).read_bytes())!=identity['archives'][n]['sha256']:raise ValueError('Candidate4 archive drift')
    cache={};decoded={};source_pins={};errors=[];decisions=[];canonical=[];targets={}
    corrections={};corrections_used=set()
    if a.corrections:
        correction_path=a.corrections.resolve()
        if not correction_path.is_relative_to(R2/'corrections'):raise ValueError('Correction scope')
        cs=rows(correction_path);corrections={c['edit_id']:c for c in cs}
        if len(corrections)!=len(cs):raise ValueError('Duplicate correction edit')
        for path in [correction_path]+[(ROOT/c['review_ref']).resolve() for c in cs]:
            if not path.is_relative_to(ROOT):raise ValueError('Correction evidence scope')
            source_pins[path.relative_to(ROOT).as_posix()]=sha(path.read_bytes())
    def raw(archive,entry):
        key=(archive,entry)
        if key not in cache:cache[key]=decrypt_file(archives[archive].read(entry))
        return cache[key]
    def json_value(archive,entry,ptr):
        key=(archive,entry)
        if key not in decoded:decoded[key]=json.loads(raw(*key))
        return get(decoded[key],ptr)
    def line_value(archive,entry,n):
        return raw(archive,entry).decode('utf8').splitlines()[n-1]
    def physical(alias_row,scene_kind):
        rid=alias_row['review_row_id']
        if rid.startswith('CAT:'):
            r=occ[rid[4:]];archive='cosmobreeder-multi.jar' if r.get('archive')=='jar' else 'patch.pak'
            entry=r['archive_entry']
            ptr=pointer((r['json_key'],)) if 'json_key' in r else r.get('json_pointer')
        else:
            r=sfw[rid];archive='cosmobreeder-multi.jar';entry=r['archive_entry']
            ptr=pointer((r['root'],)) if scene_kind=='ui' else None
        if scene_kind in ('dialogue','vsn'):return archive,entry,'line',alias_row['line']
        if scene_kind=='ui' and ptr is not None:return archive,entry,'json',ptr
        raise ValueError('Unverified code/image target')
    def add_target(key,old,new,fids,refs,origin):
        archive,entry,kind,locator=key
        if not engine.ENTRY.fullmatch(entry):raise ValueError('Target outside text scope')
        actual=line_value(archive,entry,locator) if kind=='line' else json_value(archive,entry,locator)
        if actual!=old:raise ValueError('Baseline alias old mismatch '+str(key))
        new=new.replace('汤姆猫','Tomcat')
        if old==new:raise ValueError('No-op edit '+str(key))
        if key in targets:
            t=targets[key]
            if t['old']!=old or t['new']!=new:raise ValueError('Conflicting node '+str(key))
            t['finding_ids'].update(fids);t['source_refs'].update(refs);t['origins'].append(origin)
        else:
            targets[key]={'old':old,'new':new,'finding_ids':set(fids),'source_refs':set(refs),'origins':[origin]}
        if '汤姆猫' in old and '汤姆猫' not in new:
            targets[key]['finding_ids'].add('NAME-TOMCAT')
            targets[key]['source_refs'].add('user-confirmed:keep-Tomcat-without-unapproved-Chinese-name')
    for name in names:
        inp=R2/'input'/(name+'.json');folder=R2/'packets'/name
        data=json.loads(inp.read_text('utf8'));scenes={s['scene_id']:s for s in data['scenes']}
        found={f['finding_id']:f for f in data['findings']}
        ds=rows(folder/'decisions.jsonl');es=rows(folder/'edits.jsonl')
        for path in (inp,folder/'decisions.jsonl',folder/'edits.jsonl',folder/'summary.md'):
            source_pins[path.relative_to(ROOT).as_posix()]=sha(path.read_bytes())
        by_dec={d['finding_id']:d for d in ds};by_edit={e['edit_id']:e for e in es}
        if len(by_dec)!=len(ds) or set(by_dec)!=set(found):raise ValueError('Finding decision coverage '+name)
        if len(by_edit)!=len(es):raise ValueError('Duplicate edit ID '+name)
        for d in ds:
            fid=d['finding_id']
            if d['action'] not in ('apply','reject','defer') or not d.get('reason'):raise ValueError('Invalid decision '+fid)
            if d['scene_id']!=found[fid]['scene_id']:raise ValueError('Decision scene drift')
            links=d.get('edit_ids',[])
            if d['action']=='apply' and not links:raise ValueError('Apply without edits '+fid)
            if d['action']!='apply' and links:raise ValueError('Non-apply with edits '+fid)
            for eid in links:
                if eid not in by_edit or fid not in by_edit[eid]['finding_ids']:raise ValueError('Decision/edit backlink '+fid)
            decisions.append({'packet':name,**d})
        seen=set()
        for original_edit in es:
            e=dict(original_edit)
            if e['edit_id'] in corrections:
                c=corrections[e['edit_id']]
                if c['finding_id'] not in e['finding_ids'] or c['old_proposed']!=e['new']:
                    raise ValueError('Correction proposal drift '+e['edit_id'])
                if not isinstance(c['new_proposed'],str) or c['new_proposed']==e['new']:
                    raise ValueError('Invalid/no-op correction')
                e['pre_correction_new']=e['new'];e['new']=c['new_proposed']
                e['correction_reason']=c['reason'];e['correction_review_ref']=c['review_ref']
                e['source_refs']=[*e['source_refs'],'independent-review:'+c['review_ref']+'#'+c['finding_id']]
                corrections_used.add(e['edit_id'])
            sid=e['scene_id'];scene=scenes[sid];rid=e['row_id']
            mapped={r['review_row_id']:(i,r) for i,r in enumerate(scene['rows'])}
            if rid not in mapped:raise ValueError('Edit outside scene '+e['edit_id'])
            i,row=mapped[rid]
            if (sid,rid) in seen:raise ValueError('Duplicate canonical node '+rid)
            seen.add((sid,rid))
            if e['old']!=row['current_line'] or not isinstance(e['new'],str):raise ValueError('Canonical old/new mismatch '+e['edit_id'])
            if not e['finding_ids'] or not e.get('source_refs'):raise ValueError('Missing edit provenance')
            for fid in e['finding_ids']:
                if fid not in by_dec or by_dec[fid]['action']!='apply' or e['edit_id'] not in by_dec[fid]['edit_ids'] or by_dec[fid]['scene_id']!=sid:
                    raise ValueError('Edit/decision backlink '+e['edit_id'])
            canonical.append({'packet':name,**e})
            for alias in scene['aliases']:
                ar=alias['rows'][i];key=physical(ar,scene['kind'])
                add_target(key,e['old'],e['new'],e['finding_ids'],e['source_refs'],
                           {'packet':name,'edit_id':e['edit_id'],'canonical_row_id':rid,'alias_row_id':ar['review_row_id'],'scene_id':sid})
    if corrections_used!=set(corrections):raise ValueError('Unbound independent correction')
    if complete and {d['finding_id'] for d in decisions}!=set(original_by):raise ValueError('Full 339 decision coverage')
    # Explicit user-authorized name restoration on localized text values only.
    name_targets=0
    for archive,z in archives.items():
        for entry in z.namelist():
            if not engine.ENTRY.fullmatch(entry):continue
            data=raw(archive,entry)
            if '汤姆猫'.encode() not in data:continue
            family=entry.split('/')[0]
            if family in ('datav','datay'):
                vals=[('json',ptr,value) for ptr,value in strings(json.loads(data)) if '汤姆猫' in value]
            else:
                vals=[('line',n,value) for n,value in enumerate(data.decode('utf8').splitlines(),1)
                      if '汤姆猫' in value and engine._line_role(value,family) is not None]
            for kind,locator,old in vals:
                key=(archive,entry,kind,locator);previous=targets.get(key)
                value=previous['new'] if previous else old
                new=value.replace('汤姆猫','Tomcat')
                if new==old:continue
                if previous:
                    previous['new']=new;previous['finding_ids'].add('NAME-TOMCAT')
                    previous['source_refs'].add('user-confirmed:keep-Tomcat-without-unapproved-Chinese-name')
                else:
                    add_target(key,old,new,['NAME-TOMCAT'],['candidate4:'+archive+'/'+entry+'#'+str(locator),
                               'user-confirmed:keep-Tomcat-without-unapproved-Chinese-name'],{'type':'explicit_name_restoration'})
                name_targets+=1
    operations=[];bindings=[]
    for n,(key,t) in enumerate(sorted(targets.items(),key=lambda x:str(x[0])),1):
        archive,entry,kind,locator=key;opid='ER2-%04d'%n
        operation={'op_id':opid,'archive':archive,'archive_entry':entry,'kind':kind,
                   'before_resource_sha256':sha(raw(archive,entry)),'old':t['old'],'new':t['new'],
                   'finding_ids':sorted(t['finding_ids']),'source_refs':sorted(t['source_refs']),
                   'line' if kind=='line' else 'pointer':locator}
        operations.append(operation);bindings.append({'op_id':opid,'origins':t['origins']})
    grouped=defaultdict(list)
    for op in operations:grouped[(op['archive'],op['archive_entry'])].append(op)
    output_entries={};reports=[]
    for key,ops in grouped.items():
        try:
            output_entries[key],report=engine.apply_entry(*key,raw(*key),ops);reports.append(report)
        except engine.EditorialRepairError as exc:
            details=[{'op_id':o['op_id'],'finding_ids':o['finding_ids'],
                      'removed_markers':list((engine._markers(o['old'])-engine._markers(o['new'])).elements()),
                      'added_markers':list((engine._markers(o['new'])-engine._markers(o['old'])).elements())} for o in ops
                     if engine._markers(o['old'])!=engine._markers(o['new'])]
            errors.append({'archive':key[0],'entry':key[1],'error':str(exc),'marker_diagnostics':details})
    out.mkdir(parents=True)
    for filename,value in [('decisions.jsonl',decisions),('canonical-edits.jsonl',canonical),('bindings.jsonl',bindings)]:
        (out/filename).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in value),encoding='utf8')
    opname='operations.unvalidated.jsonl' if errors else 'operations.jsonl'
    (out/opname).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in operations),encoding='utf8')
    if not errors:
        for (archive,entry),data in output_entries.items():
            target=out/'entries'/archive/entry;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    status='validation_failed' if errors else 'validated_full_repair_candidate' if complete else 'validated_partial_preview_not_buildable'
    manifest={'status':status,'full_339_coverage':complete,'baseline_archives':{n:identity['archives'][n]['sha256'] for n in archives},
              'source_sha256':source_pins,'decision_count':len(decisions),'decision_actions':dict(Counter(d['action'] for d in decisions)),
              'safe_partial_findings':[d['finding_id'] for d in decisions if d.get('resolution')=='safe_partial'],
              'independent_corrections_applied':sorted(corrections_used),
              'canonical_edits':len(canonical),'expanded_operations':len(operations),'name_restore_targets':name_targets,
              'operations_file':opname,'operations_sha256':sha((out/opname).read_bytes()),'resource_reports':reports,'errors':errors,
              'applied_to_archives':False,'installed':False,'game_started':False}
    dump(out/'manifest.json',manifest)
    for z in archives.values():z.close()
    print(json.dumps({k:manifest[k] for k in ('status','decision_count','decision_actions','canonical_edits','expanded_operations','name_restore_targets','errors')},ensure_ascii=False,indent=2))
    if errors:raise SystemExit(1)


if __name__=='__main__':main()
