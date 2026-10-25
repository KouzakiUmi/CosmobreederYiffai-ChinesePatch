"""Prepare immutable 40-row input parts; never produces translations."""
import argparse
import sys
from projectlib import *


FIELDS=['id','category','source','source_sha256','variant','speaker','context_examples','protected_tokens','markers','width_hint_px','review_flags']


def make_part(batch,start,units):
    if start<0 or start%40 or start>=batch['count']:raise ValueError('Part offset must be a valid multiple of 40')
    source=read_jsonl(PROJECT/batch['path'])[start:start+40];rows=[]
    for r in source:
        u=units[r['id']]
        if r['source_sha256']!=u['source_sha256'] or r['source']!=u['source']:raise ValueError('Original assigned source changed')
        rows.append({k:u[k] for k in FIELDS})
    path=PROJECT/'batches/parts'/(batch['batch_id']+f'_{start:03d}.jsonl')
    if path.exists():
        existing=read_jsonl(path)
        if [(r['id'],r['source_sha256'],r['source']) for r in existing]!=[(r['id'],r['source_sha256'],r['source']) for r in rows]:raise ValueError('Part source identity changed')
    else:write_jsonl(path,rows)
    return path,len(rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('batch_id',nargs='?');ap.add_argument('--start',type=int,default=0);ap.add_argument('--all',action='store_true');a=ap.parse_args()
    units={u['id']:u for u in load_units()};manifest=read_json(PROJECT/'batches/manifest.json')
    targets=manifest['batches'] if a.all else [next(b for b in manifest['batches'] if b['batch_id']==a.batch_id)]
    count=0
    for b in targets:
        if a.all and (PROJECT/b['draft_path']).exists():continue
        starts=range(0,b['count'],40) if a.all else [a.start]
        for start in starts:make_part(b,start,units);count+=1
    print('Prepared immutable small inputs:',count,'parts; <=40 units each')


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
