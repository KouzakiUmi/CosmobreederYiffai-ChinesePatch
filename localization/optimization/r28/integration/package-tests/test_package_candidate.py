"""Synthetic delta + staged verifier + read-only schema tests; NOT full packaging.
Writes only a fresh child of this package-tests directory. Never invokes install,
uninstall, game entry points, a real candidate build or any EXE builder.
"""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import sys
import uuid
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
SCRIPT=HERE.parent/'package_candidate.py'
spec=importlib.util.spec_from_file_location('r28_package_candidate',SCRIPT)
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def check(value,message):
    if not value:raise AssertionError(message)


def reject(call,label,expected_message=None):
    try:call()
    except ValueError as error:
        check(expected_message is None or expected_message in str(error),'wrong rejection gate: '+str(error))
        return label
    raise AssertionError('gate accepted: '+label)


def main():
    run=HERE/('run-'+uuid.uuid4().hex[:12]);run.mkdir()
    report={'status':'running_synthetic_only','production_package_created':False,
            'install_invoked':False,'uninstall_invoked':False,'game_started':False,'exe_built':False,'checks':[]}
    def save():p.dump(run/'test-results.json',report)
    save()
    source=run/'synthetic-source.bin'
    source.write_bytes(bytes((i*37+i//257)%256 for i in range(p.BLOCK*2+15)))
    block=p.BLOCK;raw=source.read_bytes()
    changed=bytearray(raw[:block]);changed[11]^=17;changed[-7]^=99
    target=run/'synthetic-target.bin';target.write_bytes(raw[block:2*block]+changed+b'new-tail-not-game'*19)
    staged=run/'staged';package=staged/'cosmobreeder_patch';payload=package/'payload';payload.mkdir(parents=True)
    entries={}
    for index,name in enumerate(p.NAMES):
        cbd=payload/(name+'.cbd');e=p.build(source,target,cbd);e['delta']=name+'.cbd';entries[name]=e
        rebuilt=run/f'synthetic-reconstruction-{index}.bin';p.apply(source,cbd,rebuilt,e)
        check(p.byte_equal(rebuilt,target),'synthetic byte-for-byte reconstruction')
        check(e['copy_bytes']>=block,'synthetic must exercise COPY and XOR, not only XOR')
        check(cbd.read_bytes().startswith(p.MAGIC),'unchanged CBDELTA1 protocol')
    fixture_manifest={'version':'alpha0.1','prerelease':True,'baseline':'synthetic-test-only',
                      'fixture_only':True,'files':entries}
    p.dump(payload/'manifest.json',fixture_manifest)
    for name in p.MODULES:(package/name).write_bytes((ROOT/'src/cosmobreeder_patch'/name).read_bytes())
    logs=run/'checks';logs.mkdir()
    report['staged_verify_payload']=p.verify_staged(staged,payload,logs)
    report['checks'].append('synthetic-COPY-XOR-source-dependent-bytewise-reconstruction')
    bad=run/'wrong-source.bin';bad.write_bytes(bytes([raw[0]^1])+raw[1:])
    report['checks'].append(reject(lambda:p.apply(bad,payload/entries[p.NAMES[0]]['delta'],run/'must-not-apply.bin',entries[p.NAMES[0]]),'wrong-source-SHA-rejected'))
    # A small schema fixture is NOT a built candidate and is never packaged.
    candidate=run/'synthetic-schema';candidate.mkdir()
    for name in p.NAMES:
        with zipfile.ZipFile(candidate/name,'x') as z:z.writestr('synthetic-only.txt','not a game; schema probe')
    cm={'version':p.BUILD_VERSION,'status':p.BUILD_STATUS,'selected_components':sorted(p.COMPONENTS),
        'full_component_set':True,'base_archives':dict(p.BASE_PINS),'game_started':False,
        'user_save_accessed':False,'installed':False,'real_clip_CRT_input_verified':False,
        'commands':[{'name':n,'exit_code':0} for n in ('compile-runtime','compile-tools','patch-targets','verify-final-classes')],
        'archives':{n:{'sha256':p.sha(candidate/n),'bytes':(candidate/n).stat().st_size} for n in p.NAMES}}
    mp=candidate/'build-manifest.json';p.dump(mp,cm)
    ap=candidate/'acceptance.json';acceptance_output=run/'acceptance-must-not-create-output'
    report['checks'].append(reject(lambda:p.package_candidate(candidate,acceptance_output),'missing-acceptance-before-output','acceptance'))
    acceptance={'status':'passed_cpu_and_independent_review_not_real_clip_CRT_input',
                'archives':{n:cm['archives'][n]['sha256'] for n in p.NAMES}}
    bad_acceptance=copy.deepcopy(acceptance);bad_acceptance['status']='failed_cpu'
    p.dump(ap,bad_acceptance)
    report['checks'].append(reject(lambda:p.package_candidate(candidate,acceptance_output),'failed-acceptance-before-output','acceptance'))
    bad_acceptance=copy.deepcopy(acceptance);bad_acceptance['archives'][p.NAMES[0]]='0'*64
    p.dump(ap,bad_acceptance)
    report['checks'].append(reject(lambda:p.package_candidate(candidate,acceptance_output),'wrong-acceptance-SHA-before-output','acceptance'))
    check(not acceptance_output.exists(),'acceptance gates created output')
    p.dump(ap,acceptance)
    check(p.validate_candidate(candidate)[2]=='synthetic-schema','complete-schema plus passed acceptance')
    report['checks'].append('synthetic-complete-schema-accepted-only-as-read-only-probe')
    bad_cases=[]
    value=copy.deepcopy(cm);value['status']='partial_integration_not_release';bad_cases.append(('partial',value))
    value=copy.deepcopy(cm);value['full_component_set']=False;bad_cases.append(('not-full',value))
    value=copy.deepcopy(cm);value['selected_components'].pop();bad_cases.append(('missing-component',value))
    value=copy.deepcopy(cm);value['selected_components'][-1]=value['selected_components'][0];bad_cases.append(('duplicate-component',value))
    value=copy.deepcopy(cm);value['base_archives'][p.NAMES[0]]='0'*64;bad_cases.append(('wrong-r27-base-pin',value))
    value=copy.deepcopy(cm);value['installed']=True;bad_cases.append(('installed-boundary-claim',value))
    value=copy.deepcopy(cm);value['archives'][p.NAMES[0]]['sha256']='0'*64;bad_cases.append(('stale-target-SHA',value))
    value=copy.deepcopy(cm);value['commands'][0]['exit_code']=1;bad_cases.append(('failed-build-command',value))
    value=copy.deepcopy(cm);value['build_id']='../unsafe';bad_cases.append(('unsafe-build-id',value))
    for label,value in bad_cases:
        p.dump(mp,value);report['checks'].append(reject(lambda:p.validate_candidate(candidate),label))
    p.dump(mp,cm)
    report['checks'].append(reject(lambda:p.package_candidate(candidate,ROOT/'dist/alpha0.1'),'old-alpha-output-rejected-before-write'))
    forbidden_output=run/'must-not-create-output'
    report['checks'].append(reject(lambda:p.package_candidate(candidate,forbidden_output),'non-dist-r28-output-rejected-before-write'))
    check(not forbidden_output.exists(),'invalid output gate created files')
    pilot=HERE.parent/'builds/pilot-01'
    if pilot.exists():report['checks'].append(reject(lambda:p.validate_candidate(pilot),'actual-partial-pilot-rejected-without-packaging'))
    good={'cosmobreeder_patch/payload/manifest.json','cosmobreeder_patch/payload/patch.pak.cbd','cosmobreeder_patch/delta.py'}
    p.validate_zip_members(sorted(good),good)
    for name in ('cosmobreeder_patch/patch.pak','cosmobreeder_patch/x.png','cosmobreeder_patch/font.bdf',
                 'cosmobreeder_patch/../oops.txt','cosmobreeder_patch/x.exe'):
        report['checks'].append(reject(lambda n=name:p.validate_zip_members([n],{n}),'zip-blocks-'+name))
    report['checks'].append(reject(lambda:p.validate_zip_members(sorted(good)+['extra.txt'],good),'ZIP-exact-allowlist'))
    legal,pins=p.collect_text_inputs()
    check(all(('licenses/'+name) in legal for name in p.REQUIRED_LICENSES),'old legal tree complete')
    check(all(('licenses/fonts/native8/LICENSES/'+name) in legal for name in p.NATIVE8_COMPONENTS),'native8 legal tree complete')
    check(all(legal[n]==(ROOT/'src/cosmobreeder_patch'/n).read_bytes() for n in p.MODULES),'installer source unchanged')
    report['checks'].append('complete-original-and-native8-legal-text-inventory-with-unmodified-installer')
    report['original_backups_read_only_pins']={}
    for name in p.NAMES:
        path=ROOT/'backup'/name
        check(path.stat().st_size==p.SOURCE_SIZES[name] and p.sha(path)==p.SOURCE_PINS[name],'real backup source SHA')
        report['original_backups_read_only_pins'][name]=p.SOURCE_PINS[name]
    check(not list(package.rglob('*.pyc')),'staged verifier must not create pycache')
    report.update({'status':'passed_synthetic_delta_and_static_gates_only','check_count':len(report['checks']),
                   'installer_and_legal_input_count':len(pins),'script_sha256':p.sha(SCRIPT),
                   'full_production_candidate_package_validation':'not_run; parent executes only after final seven-component candidate exists'})
    save();print(json.dumps({'status':report['status'],'checks':len(report['checks']),'output':run.relative_to(ROOT).as_posix()},ensure_ascii=False))


if __name__=='__main__':main()
