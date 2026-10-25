"""Freeze an existing, independently identified r21 and original archive pair.
Only writes this task's new baseline.json; never scans or writes the installation.
"""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'localization/layout/baseline.json'
TARGETS = ['Yg', 'jo', 'jl', 'amH', 'amn', 'Mf', 'LX', 'LY', 'Iu', 'Le', 'Lg', 'Lb']


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    if BASE.exists():
        raise ValueError('Baseline already frozen; do not silently refresh it')
    build = ROOT / 'localization/builds/final-8146-r21-images'
    manifest = json.loads((build / 'package-manifest.json').read_text(encoding='utf-8'))
    original = ROOT / 'backup/cosmobreeder-multi.jar'
    expected_original = next(a['sha256'] for a in manifest['originals'] if a['tag'] == 'jar')
    if sha(original.read_bytes()) != expected_original:
        raise ValueError('Original archive does not match recorded r21 original')
    archives = {}
    for entry in manifest['archives']:
        path = build / entry['archive']
        if sha(path.read_bytes()) != entry['sha256']:
            raise ValueError('r21 manifest mismatch: ' + entry['archive'])
        archives[entry['archive']] = entry['sha256']
    pins = {}
    with zipfile.ZipFile(original) as old, zipfile.ZipFile(build / 'cosmobreeder-multi.jar') as current:
        for name in TARGETS:
            entry = 'PRG/' + name + '.class'
            before, after = old.read(entry), current.read(entry)
            if before != after:
                raise ValueError('Target already modified in r21: ' + entry)
            pins[entry[:-6]] = sha(before)
        font_inputs = {name: sha(current.read(name)) for name in ('bbc2.fnt', 'classic.fnt')}
    runtime = ROOT / 'localization/runtime'
    resources = {name: sha((runtime / name).read_bytes()) for name in (
        'bbc2.fnt', 'bbc2-cjk-10.png', 'classic.fnt', 'classic-cjk.png',
        'LICENSE-FusionPixel-OFL.txt', 'NOTICE.txt', 'font-license-metadata.json')}
    if any(resources[name] != font_inputs[name] for name in font_inputs):
        raise ValueError('Runtime FNT does not match r21')
    document = {'schema_version': 1, 'baseline_revision': 2, 'game_version': '1.0.5_full',
                'target_expansion_reason': 'Preserve exact VSN source identity through original amn copies',
                'baseline_build': str(build.relative_to(ROOT)).replace('\\', '/'),
                'baseline_archives': archives,
                'original_jar': str(original.relative_to(ROOT)).replace('\\', '/'),
                'original_jar_sha256': expected_original,
                'target_classes': pins, 'runtime_resources': resources,
                'status': 'frozen_inputs_not_visual_acceptance'}
    BASE.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('FROZEN', len(pins), 'class targets and', len(resources), 'resource identities')


if __name__ == '__main__':
    main()
