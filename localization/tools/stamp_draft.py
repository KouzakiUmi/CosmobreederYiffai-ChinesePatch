"""Seal model-written translations with verified source hashes; never translate text."""
import argparse
import re
import sys
from projectlib import *


def main():
    ap=argparse.ArgumentParser();ap.add_argument('batch_id');ap.add_argument('--part-start',type=int);a=ap.parse_args()
    if not re.fullmatch(r'batch_\d{3}',a.batch_id):raise ValueError('Invalid batch ID')
    manifest=read_json(PROJECT/'batches/manifest.json');batch=next(b for b in manifest['batches'] if b['batch_id']==a.batch_id)
    source=read_jsonl(PROJECT/batch['path'])
    if a.part_start is None:
        expected_rows=source;path=PROJECT/batch['draft_path']
    else:
        start=a.part_start
        if start<0 or start%40 or start>=len(source):raise ValueError('Invalid 40-row part offset')
        expected_rows=source[start:start+40]
        path=PROJECT/'drafts/parts'/(a.batch_id+f'_{start:03d}.jsonl')
    origin_model=draft_model_label(path)
    expected={r['id']:r for r in expected_rows};units={r['id']:r for r in load_units()};rows=read_jsonl(path);seen=set()
    for r in rows:
        uid=r['id']
        if uid not in expected or uid in seen:raise ValueError('Unknown or duplicate draft ID')
        seen.add(uid);sha=units[uid]['source_sha256']
        if expected[uid]['source_sha256']!=sha or source_hash(expected[uid]['source'])!=sha:raise ValueError('Input source changed')
        if r.get('source_sha256') not in (None,'',sha):raise ValueError('Existing draft hash mismatches source')
        if not isinstance(r.get('translation'),str):raise ValueError('Translation must already exist as text')
        r['source_sha256']=sha
    write_jsonl(path,rows)
    complete=[r['id'] for r in rows]==[r['id'] for r in expected_rows]
    if complete:
        write_json(path.with_suffix('.ready.json'),{'batch_id':a.batch_id,'part_start':a.part_start,'count':len(rows),'draft_sha256':digest(path.read_bytes()),'origin_model':origin_model})
    print('Stamped source identities only:',a.batch_id,'part',a.part_start,'rows',len(rows),'expected',len(expected),'complete',complete)


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
