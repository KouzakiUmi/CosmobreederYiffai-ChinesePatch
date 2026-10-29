"""Record final editorial artifacts and unchanged source identities, not approval."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import unquote
import argparse
import json
import re

ROOT=Path(__file__).resolve().parents[4]
R1=ROOT/'localization/editorial/r1'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();out=a.output.resolve()
    if out.exists() or not out.is_relative_to(R1/'reports'):raise ValueError('New editorial record only')
    snapshot=R1/'corpus/snapshot-01'
    source=json.loads((snapshot/'manifest.json').read_text('utf8'))
    validation=json.loads((R1/'reports/rough-validation-02.json').read_text('utf8'))
    summary=json.loads((R1/'reports/rough-review-01/summary.json').read_text('utf8'))
    if validation['status']!='PASS_STRUCTURAL_ONLY' or summary['approved'] or summary['applied']:
        raise ValueError('Only structurally checked, unapplied rough-review output')
    if any(r['read_full_scenes']!=r['expected_scenes'] for r in validation['packets']):
        raise ValueError('Incomplete reading receipts')
    unchanged={}
    for name,pin in source['source_sha256'].items():
        path=(ROOT/name).resolve()
        if not path.is_relative_to(ROOT) or digest(path)!=pin:raise ValueError('Source drift '+name)
        unchanged[name]=pin
    required=['README.md','TRANSLATION_PLAN.md','LOCALIZATION_BRIEF.md','WORK_ORDERS.md',
              'reference/characters-primary.md','reference/characters-support.md','reference/world-and-plot.md',
              'reference/cast-and-creatures.md','reference/cast-and-creatures.json','reference/terms-proposals.tsv',
              'review/spotcheck-01.json','review/spotcheck-01.md','reports/rough-review-01/SUMMARY.md']
    if any(not (R1/name).is_file() for name in required):raise ValueError('Missing editorial deliverable')
    broken=[];checked=0
    for doc in R1.rglob('*.md'):
        for target in re.findall(r'\]\(<([^>]+)>\)',doc.read_text('utf8')):
            if re.match(r'^[a-zA-Z]+://',target):continue
            target=unquote(target.split('#',1)[0])
            if not target:continue
            candidates=[(doc.parent/target).resolve(),(ROOT/target).resolve()]
            if not any(p.exists() for p in candidates):broken.append(doc.relative_to(ROOT).as_posix()+' -> '+target)
            checked+=1
    if broken:raise ValueError('Broken editorial links: '+json.dumps(broken,ensure_ascii=False))
    artifacts={p.relative_to(ROOT).as_posix():digest(p) for p in sorted(R1.rglob('*'))
               if p.is_file() and p.suffix in ('.py','.md','.json','.jsonl','.tsv') and p.resolve()!=out}
    value={'status':'R1_documents_and_rough_review_recorded_not_approved','unchanged_original_inputs':unchanged,
           'artifact_sha256':artifacts,'markdown_link_targets_checked':checked,'broken_links':[],
           'catalog_units':source['catalog_units'],'source_rows':source['all_source_rows'],
           'canonical_rows':source['canonical_rows'],'review_blocks':source['canonical_scenes'],
           'findings':summary['findings'],'status_counts':summary['status_counts'],
           'limited_independent_review':summary['limited_independent_review'],
           'formal_translation_ledger_unchanged':True,'game_archives_unchanged':True,
           'applied':False,'approved':False,'installed':False,'game_started':False,
           'notes':['Input identity and artifact hashes are not semantic approval.',
                    'Links accept document-relative paths and repository-root references used by the workspace viewer.',
                    'Original whole-text corpus remains local editorial material, not public patch payload.']}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:value[k] for k in ('status','markdown_link_targets_checked','findings','status_counts','formal_translation_ledger_unchanged','game_archives_unchanged')},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
