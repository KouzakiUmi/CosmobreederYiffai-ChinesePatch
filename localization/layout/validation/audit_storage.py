"""Read-only bytecode preflight; never invokes a JVM or reads a save.
Writes only a new project-local evidence directory. Not a native IO sandbox proof.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'localization/tools'))
import classfile
classfile.OPS[0xb9]=('invokeinterface','cp2pad')


def sha(raw): return hashlib.sha256(raw).hexdigest()


def run(output):
    allowed=(ROOT/'localization/work/layout-storage-audit').resolve()
    output=output.resolve()
    if output==allowed or not output.is_relative_to(allowed) or output.exists():
        raise ValueError('Output must be a new child of layout-storage-audit')
    baseline=json.loads((ROOT/'localization/layout/baseline.json').read_text(encoding='utf-8'))
    original=ROOT/baseline['original_jar']
    if sha(original.read_bytes())!=baseline['original_jar_sha256']: raise ValueError('Original identity changed')
    inventory=ROOT/'docs/full-layout-study-20261023/inventory'
    summary=json.loads((inventory/'summary.json').read_text(encoding='utf-8'))
    if summary['archives']['cosmobreeder-multi.jar']['sha256']!=baseline['original_jar_sha256']:
        raise ValueError('Saved call index belongs to another original')
    candidate=ROOT/'localization/builds/layout-r22-candidate-v2/cosmobreeder-multi.jar'
    chosen={'SO':{'a','b'},'Hi':{'<clinit>','a'},'He':{'<init>','a'},'Tk':{'<init>','a'},
            'Yu':{'<clinit>','a'},'iF':{'b'},'iP':{'a'},'iG':{'uncaughtException'},
            'adh':{'a','b'},'aqn':{'b'},'aqo':{'<clinit>'}}
    classes={}
    with zipfile.ZipFile(original) as before,zipfile.ZipFile(candidate) as after:
        for short,names in chosen.items():
            entry='PRG/'+short+'.class';raw=before.read(entry);cf=classfile.load(raw)
            if cf.this_name+'.class'!=entry: raise ValueError('Internal identity mismatch')
            methods=[]
            for method in cf.methods:
                if method['name'] not in names:continue
                if short=='iF' and method['desc']!='(Ljava/nio/file/Path;)V':continue
                if short=='SO' and method['desc'] not in ('()Ljava/lang/String;','(Ljava/lang/String;)V'):continue
                code=cf.code_of(method)
                if code: methods.append({'name':method['name'],'descriptor':method['desc'],
                    'instructions':[{'pc':pc,'opcode':op,'operand':arg} for pc,op,arg in classfile.disasm(cf,code[0])]})
            classes[entry]={'sha256':sha(raw),'candidate_unchanged':raw==after.read(entry),'selected_methods':methods}
    calls=[]
    with (inventory/'all-invocations.jsonl').open(encoding='utf-8') as source:
        for line in source:
            row=json.loads(line)
            if (row['owner']=='PRG/SO' and row['name'] in ('a','b') and row['desc'] in ('()Ljava/lang/String;','(Ljava/lang/String;)V')) \
                    or (row['owner']=='PRG/Yu' and row['name']=='a'):
                calls.append(row)
    report={'schema_version':1,'status':'STATIC_ONLY_FULL_RUN_ISOLATION_UNPROVEN',
            'original_sha256':baseline['original_jar_sha256'],'candidate_sha256':sha(candidate.read_bytes()),
            'saved_index_sha256':sha((inventory/'all-invocations.jsonl').read_bytes()),
            'classes':classes,'saved_direct_call_index_subset':calls,
            'jvm_started':False,'game_started':False,'save_content_read':False,
            'conclusions':[
                'SO String setters do not rebind already-created Hi/He/Tk file handles.',
                'The old redirect replacement contains both save and options setters; historical failure cause is not proven.',
                'Tk can write both save_backups and loadfail backups; options and error logs have separate paths.',
                'Private SO getters plus whole-method Yu None fallback are a proposed test-only design, not an executed safety proof.',
                'Java tripwire does not constrain native DLL or external Steam client IO; do not launch the old verification copy.'
            ]}
    output.mkdir(parents=True)
    (output/'storage-preflight.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(output),'classes':len(classes),'direct_call_records':len(calls),
                      'all_storage_classes_unchanged':all(c['candidate_unchanged'] for c in classes.values()),
                      'game_started':False,'status':report['status']},ensure_ascii=False,indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    run(parser.parse_args().output)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');main()
