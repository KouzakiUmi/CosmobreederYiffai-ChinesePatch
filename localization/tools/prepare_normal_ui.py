"""Create nine disjoint, manually screened normal-UI jobs; do not translate."""
from projectlib import *

GROUPS=[
 ('R1','root',['ui.inputConfig.L1','ui.inputConfig.R1','ui.inputConfig.circle','ui.inputConfig.cross','ui.inputConfig.square','ui.inputConfig.unbound']),
 ('R2','root',['ui.inputConfig.gamepadConfig','ui.inputConfig.keyboardConfig','ui.inputConfig.reset','ui.inputConfig.return']),
 ('R3','root',['ui.defeated.debrief','ui.defeated.end','ui.defeated.retry','ui.gameOver.continue','ui.options.exitGame','ui.options.exitGame.confirm']),
 ('R4','root',['ui.item.cardview','ui.item.communicate','ui.item.equipment','ui.item.missionlog','ui.item.navigation']),
 ('S1','sol',['ui.options.cheats','ui.options.confirm','ui.options.confirmCheat.red0','ui.options.confirmCheat.red4','ui.options.confirmCheat.red7','ui.options.confirmCheat.red8']),
 ('S2','sol',['ui.options.confirmCheat.wht2','ui.options.confirmCheat.wht3','ui.options.confirmCheat.wht4','ui.options.confirmCheat.wht5','ui.options.confirmSaveCodes.wht7','ui.options.enterCheatMenu','ui.options.progress1','ui.options.progress2','ui.options.reset','ui.options.reset.confirm']),
 ('S3','sol',['ui.options.fill.aspect','ui.options.fill.integer','ui.options.fill.stretch','ui.options.windowFill','ui.options.windowScale']),
 ('S4','sol',['ui.options.windowFilter','ui.options.windowFilter.crt','ui.options.windowFilter.plain','ui.options.windowFilter.scan','ui.options.windowMode','ui.options.windowMode.full','ui.options.windowMode.window']),
 ('S5','sol',['ui.options.gamepadConfig','ui.options.header','ui.options.keyboardConfig','ui.options.musicVolume','ui.options.off','ui.options.on','ui.options.sfxVolume','ui.save.deletebutton','ui.save.entername','ui.save.fileclear']),
]
FIELDS=['id','category','source','source_sha256','variant','speaker','context_examples','protected_tokens','markers','width_hint_px','review_flags']


def main():
    dest=PROJECT/'batches/normal/manifest.json'
    if dest.exists():raise SystemExit('Normal jobs already exist; do not regenerate.')
    units={u['id']:u for u in load_units()};records=current_translations();by_key={};all_locations={}
    for o in load_occurrences():
        if o['category']=='ui' and o.get('json_key'):
            by_key[o['json_key']]=o['unit_id'];all_locations.setdefault(o['unit_id'],[]).append(o['json_key'])
    rejected={r['source_sha256'] for r in read_jsonl(PROJECT/'batches/parts/batch_044_000.jsonl')}
    manifest=read_json(PROJECT/'batches/manifest.json');registry=read_json(PROJECT/'catalog/draft-provenance.json');seen=set();jobs=[]
    for group,owner,keys in GROUPS:
        rows=[]
        for key in keys:
            uid=by_key[key];u=units[uid]
            assert uid not in seen and not records[uid].get('draft') and not records[uid].get('translation')
            assert u['source_sha256'] not in rejected and u['category']=='ui'
            assert all(k.startswith(('ui.inputConfig.','ui.options.','ui.save.','ui.item.','ui.defeated.','ui.gameOver.')) for k in all_locations[uid])
            assert not any(term in u['source'].upper() for term in ('BREED','BESTIAL','GENITAL','SPERM','PENIS','VAGINA','ORGASM','SEXM'))
            seen.add(uid);rows.append({k:u[k] for k in FIELDS})
        bid=f'batch_{len(manifest["batches"]):03d}';input_path=f'batches/normal/{bid}.jsonl';output=f'drafts/normal/{owner}/{bid}.jsonl'
        write_jsonl(PROJECT/input_path,rows)
        job={'batch_id':bid,'group':group,'owner':owner,'path':input_path,'draft_path':output,'count':len(rows),'ids':[r['id'] for r in rows],
             'source_characters':sum(len(r['source']) for r in rows),'scope':'manually screened normal UI only','require_ready':True}
        manifest['batches'].append(job);jobs.append(job)
        registry['drafts'][output]={'provider':'xiaomi-token-plan-cn','model':'mimo-v2.6-pro','reasoning_effort':'high','source_input':input_path,
                                    'source_input_sha256':digest((PROJECT/input_path).read_bytes()),'group':group,'saved_by':owner+' coordinator; text produced by MiMo'}
        packet={'group':group,'batch_id':bid,'output':output,'rows':[{'id':r['id'],'source':r['source'],'context':'; '.join(all_locations[r['id']])} for r in rows]}
        write_json(PROJECT/'batches/normal/packets'/(group+'.json'),packet)
    assert len(jobs)==9 and len(seen)==59 and all(0<j['count']<=40 for j in jobs)
    write_json(PROJECT/'batches/manifest.json',manifest);write_json(PROJECT/'catalog/draft-provenance.json',registry)
    write_json(dest,{'scope':'normal UI first-translation wave','total_units':59,'jobs':jobs,'semantic_review':'sample only; two precision passes later',
                     'deferred':'Sensitive, previously filtered, ambiguous, story, and other unclassified text are not included; original units unchanged.',
                     'quota_status':'query authentication failed; user confirmed cookie expired and actual route/capacity available',
                     'approvals':['approve_sol_coordinator','approve_mimo_normal_nine']})
    write_json(PROJECT/'reports/normal-ui-selection.json',{'selected_units':59,'selected_ids':sorted(seen),'groups':{j['group']:j['count'] for j in jobs},
               'previously_filtered_source_reused':False,'symbols_and_ambiguous_titles_held':['-----------','BESTIALIARY','POCKET BREED','EXTRA SPRITES'],
               'base_units_and_source_ids_unchanged':True,'completion_accounting':'Unique canonical unit records, not the sum of overlapping historical task inputs.'})
    for j in jobs:print(j['group'],j['batch_id'],j['count'],j['draft_path'])


if __name__=='__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf8');main()
