"""Seal this bounded UI increment only after fresh CPU tests and independent review.

Does not install, launch, or weaken the original full-candidate acceptance.
Unchanged resources/classes inherit evidence only after byte/decrypted-byte comparison.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'localization/tools'))
from codec import decrypt_file


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(value, message):
    if not value:
        raise ValueError(message)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--tests', type=Path, required=True)
    p.add_argument('--review', type=Path, required=True)
    a = p.parse_args()
    candidate, tests, review = (v.resolve() for v in (a.candidate, a.tests, a.review))
    for value in (candidate, tests, review):
        require(value.is_relative_to(ROOT), 'Workspace paths only')
    output = candidate / 'acceptance.json'
    require(not output.exists(), 'New acceptance only')
    base = ROOT / 'localization/builds/r28-full-opt-candidate2'
    base_acceptance = json.loads((base / 'acceptance.json').read_text('utf8'))
    build = json.loads((candidate / 'build-manifest.json').read_text('utf8'))
    result = json.loads((tests / 'results.json').read_text('utf8'))
    independent = json.loads(review.read_text('utf8'))
    names = ('cosmobreeder-multi.jar', 'patch.pak')
    archives = {n: digest(candidate / n) for n in names}
    require(build['full_component_set'] and set(build['selected_components']) ==
            {'core', 'pattern', 'compact', 'scenes', 'sfw', 'vsn', 'images', 'radio'}, 'Full eight-component build')
    require(build['status'] == 'integrated_candidate_not_real_clip_CRT_input_acceptance', 'Candidate status')
    require(all(c['exit_code'] == 0 for c in build['commands']), 'Successful build required')
    require(all(build['archives'][n]['sha256'] == archives[n] for n in names), 'Build archive identity')
    require(result['status'] == 'passed_cpu_only_not_real_clip_CRT_input' and
            result['candidate_sha256'] == archives[names[0]], 'Actual candidate CPU tests')
    expected = {'compile-tests', 'radio-labels', 'core-regression', 'pixel-layout', 'dialogue-grid',
                'dialogue-wrap', 'continue', 'subtitle', 'pattern', 'ending-sfw', 'ending-nsfw',
                'scenes', 'story12-lifecycle', 'compact-inputs', 'compact-compile', 'compact-cpu', 'compact-pixels'}
    require(len(result['steps']) == len(expected) and {s['name'] for s in result['steps']} == expected and
            all(s['exit_code'] == 0 for s in result['steps']), 'All seventeen exact test steps')
    require(result['test_sources_unchanged_after_run'], 'Test source stability')
    for mapping in (build['source_sha256'], result['test_source_sha256'], independent['source_sha256']):
        for name, pin in mapping.items():
            path = (ROOT / name).resolve()
            require(path.is_relative_to(ROOT) and digest(path) == pin, 'Source drift: ' + name)
    require(independent['status'] == 'PASS' and independent['archives'] == archives,
            'Independent final-archive review')
    require(independent['checks'] and all(c['passed'] for c in independent['checks']), 'Independent checks')
    require(base_acceptance['status'] == 'passed_cpu_and_independent_review_not_real_clip_CRT_input',
            'Accepted parent required')
    require(base_acceptance['archives'] == {n: digest(base / n) for n in names}, 'Parent archive identity')
    require(base_acceptance['build_manifest_sha256'] == digest(base / 'build-manifest.json'),
            'Parent build identity')
    for item in base_acceptance['evidence']:
        path = (ROOT / item['path']).resolve()
        require(path.is_relative_to(ROOT) and digest(path) == item['sha256'], 'Parent evidence drift')
    for name, pin in independent['evidence_sha256'].items():
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT) and digest(path) == pin, 'Independent evidence drift')
    allowed = {'PRG/Kc.class', 'PRG/JM.class', 'PRG/JQ.class', 'PRG/SceneText.class', 'PRG/RadioLabels.class'}
    changes = {}; compared = {}
    for archive in names:
        changed = []; decoded = 0
        with zipfile.ZipFile(base / archive) as old, zipfile.ZipFile(candidate / archive) as new:
            before, after = set(old.namelist()), set(new.namelist())
            require(not before - after and after - before <= {'PRG/RadioLabels.class'}, 'Unexpected entry set')
            for name in sorted(after):
                current = new.read(name)
                if name not in before:
                    require(archive == names[0] and name in allowed, 'Unexpected new entry')
                    changed.append(name); continue
                previous = old.read(name)
                if previous == current:
                    continue
                if name.endswith('.class'):
                    require(archive == names[0] and name in allowed, 'Unrelated class changed: ' + name)
                    changed.append(name)
                else:
                    require(decrypt_file(previous) == decrypt_file(current), 'Resource semantic drift: ' + name)
                    decoded += 1
        changes[archive] = changed; compared[archive] = decoded
    require(set(changes[names[0]]) == allowed and not changes[names[1]], 'Exact bounded class delta')
    evidence = [tests / 'results.json', review, base / 'acceptance.json']
    value = {'schema': 1, 'status': 'passed_cpu_and_independent_review_not_real_clip_CRT_input',
             'archives': archives, 'build_manifest_sha256': digest(candidate / 'build-manifest.json'),
             'evidence': [{'path': f.relative_to(ROOT).as_posix(), 'sha256': digest(f)} for f in evidence],
             'actual_candidate_jvm_steps': result['steps'], 'changed_entries': changes,
             'encrypted_entries_rechecked_semantically': compared,
             'parent_evidence_inherited_only_for_identical_content': True,
             'game_started': False, 'installed': False, 'user_save_accessed': False,
             'not_verified': list(dict.fromkeys(base_acceptance['not_verified'] + independent['not_verified'] +
                              ['Real game rendering, CRT/shader, full parent clip and input traversal',
                               'Live game installation and save compatibility']))}
    require(archives == {n: digest(candidate / n) for n in names}, 'Final archive stability')
    output.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'status': value['status'], 'changed_entries': changes}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
