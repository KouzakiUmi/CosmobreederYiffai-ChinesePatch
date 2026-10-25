"""Export a public translation snapshot without private provenance or source prose.

The export is authoring/reference data, NOT a replacement for the full local
source-identity ledger used by the historical game build.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def read_jsonl(path: Path):
    return [json.loads(row) for row in path.read_text(encoding='utf-8').splitlines() if row.strip()]


def export(input_dir: Path, output_dir: Path):
    source=read_jsonl(input_dir/'zh-CN.jsonl')
    joins=read_jsonl(input_dir/'dialogue-joins.jsonl')
    translations=[{key:record[key] for key in ('id','draft','translation','status','usage_approved','source_sha256') if key in record} for record in source]
    merged=[{key:record[key] for key in ('join_id','logical_path','root','actor','prefix','merged_translation','merged_translation_sha256','status') if key in record} for record in joins]
    short=[{key:record[key] for key in ('key','replacement','status','unit_id') if key in record} for record in read_jsonl(input_dir/'layout-short-overrides.jsonl')]
    data={name:''.join(json.dumps(record,ensure_ascii=False,separators=(',',':'))+'\n' for record in records).encode('utf-8') for name,records in [('zh-CN.jsonl',translations),('dialogue-joins.jsonl',merged),('layout-short-overrides.jsonl',short)]}
    manifest={'schema':1,'version':'alpha0.1','kind':'public-authoring-snapshot-not-build-ledger','source_baseline':'r27-story12-shaderfix-test5','counts':{'units':len(source),'nonempty_drafts':sum(bool(record.get('draft')) for record in source),'untranslated':sum(record.get('status')=='untranslated' for record in source),'merged_groups':len(joins)},'removed_fields':['private provenance paths','review/model handoff notes','nested original-source/context inputs','original expected text'],'files':{name:hashlib.sha256(raw).hexdigest() for name,raw in data.items()}}
    data['snapshot.json']=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    output_dir.mkdir(parents=True,exist_ok=True)
    for name,raw in data.items():
        target=output_dir/name
        if target.exists() and target.read_bytes()!=raw:raise ValueError('Refuse replacing different snapshot: '+name)
        target.write_bytes(raw)
    return manifest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir',type=Path,default=Path('localization/translations'))
    parser.add_argument('--output-dir',type=Path,default=Path('data/translations'))
    args=parser.parse_args();print(json.dumps(export(args.input_dir,args.output_dir),ensure_ascii=False,indent=2))


if __name__=='__main__':main()
