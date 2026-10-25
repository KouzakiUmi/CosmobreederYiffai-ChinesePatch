"""Append verified nested UI sources without changing assigned batches or existing IDs."""
import collections
from projectlib import *
from extract_project import TextCatalog,add_nested_ui


def main():
    old_units=load_units();old_occ=load_occurrences();old_occ_count=len(old_occ);old_ids={u['id'] for u in old_units}
    key='datay/scripts_pack.json'
    if any(o.get('logical_path')==key and o.get('json_pointer') for o in old_occ):raise SystemExit('Nested UI already appended')
    catalog=TextCatalog();catalog.units={u['id']:u for u in old_units};catalog.occ=old_occ
    resource=next(r for r in read_jsonl(PROJECT/'catalog/resources.jsonl') if r['logical_path']==key)
    add_nested_ui(catalog,resource)
    for u in catalog.units.values():
        u['protected_tokens']=protected(u['source']);u['markers']=marker_signature(u['source'])
        if u['variant'] in ('male','female') and 'raw_variant_semantics_unverified' not in u['review_flags']:
            u['review_flags'].append('raw_variant_semantics_unverified')
    units,occ=catalog.finish();new=[u for u in units if u['id'] not in old_ids]
    manifest=read_json(PROJECT/'batches/manifest.json');old_batches={b['path']:digest((PROJECT/b['path']).read_bytes()) for b in manifest['batches']}
    for start in range(0,len(new),120):
        rows=new[start:start+120];bid='batch_%03d'%len(manifest['batches'])
        records=[{k:u[k] for k in ['id','category','source','source_sha256','variant','speaker','context_examples','protected_tokens','markers','width_hint_px','review_flags']} for u in rows]
        write_jsonl(PROJECT/'batches'/(bid+'.jsonl'),records)
        manifest['batches'].append({'batch_id':bid,'path':'batches/'+bid+'.jsonl','draft_path':'drafts/'+bid+'.jsonl',
                                    'count':len(rows),'source_characters':sum(len(r['source']) for r in rows),'ids':[r['id'] for r in rows],
                                    'appended_reason':'nested shop, mission log and runtime patchDictionary sources'})
    manifest['preferred_part_units']=40;write_json(PROJECT/'batches/manifest.json',manifest)
    assert all(digest((PROJECT/path).read_bytes())==sha for path,sha in old_batches.items()),'An assigned input batch changed'
    translations=current_translations()
    for u in new:translations[u['id']]={'id':u['id'],'source_sha256':u['source_sha256'],'draft':'','translation':'','status':'untranslated','model':'','notes':'','reviewer':'','usage_approved':False}
    write_jsonl(PROJECT/'translations/zh-CN.jsonl',[translations[u['id']] for u in units])
    old_overrides={r['occurrence_id']:r for r in read_csv(PROJECT/'review/occurrence_overrides.csv')}
    by_id={u['id']:u for u in units};rows=[]
    for o in occ:
        row=old_overrides.get(o['occurrence_id'],{'occurrence_id':o['occurrence_id'],'unit_id':o['unit_id'],'location':o['location'],'translation_override':'','status':'untranslated','notes':''})
        row.update(source=by_id[o['unit_id']]['source'],category=o['category'],variant=o['variant'],speaker=o['speaker']);rows.append(row)
    write_csv(PROJECT/'review/occurrence_overrides.csv',rows,['occurrence_id','unit_id','location','source','category','variant','speaker','translation_override','status','notes'])
    summary=read_json(PROJECT/'reports/extraction-summary.json')
    summary.update(units=len(units),occurrences=len(occ),unit_categories=dict(collections.Counter(u['category'] for u in units)),
                   occurrence_categories=dict(collections.Counter(o['category'] for o in occ)),source_characters=sum(len(u['source']) for u in units))
    write_json(PROJECT/'reports/extraction-summary.json',summary)
    report={'added_units':len(new),'added_occurrences':len(occ)-old_occ_count,'existing_ids_preserved':old_ids<=set(by_id),
            'assigned_input_batches_unchanged':True,'total_units':len(units),'total_batches':len(manifest['batches']),
            'source':'datay/scripts_pack.json','evidence':'PRG/iw.<init> PC 173-195 combines lj.c() with li.o(); lg reads li.i() shops and li.k() mission log.',
            'variant_caution':'male/female are raw resource branches; missionLog/male contains Yiffany while female contains Yiffai. Do not override source names/pronouns.'}
    write_json(PROJECT/'reports/nested-ui-append.json',report);print(__import__('json').dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf8');main()
