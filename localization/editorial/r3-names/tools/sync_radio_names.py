"""Sync radio-only static data from the reviewed registry; never decides names.
Run from any cwd; --check detects stale outputs. No runtime JSON IO is added.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LEDGER = ROOT / 'localization/translations/character-names.json'
HELPER = ROOT / 'localization/layout/src/PRG/RadioLabels.java'
COMPONENT = ROOT / 'localization/optimization/r28/radio/component.json'
TSV = ROOT / 'localization/editorial/r3-names/generated/radio-names.tsv'


def outputs():
    raw = LEDGER.read_bytes()
    ledger = json.loads(raw)
    names = ledger['names']
    assert len(names) == 36
    rows, seen, targets = [], {}, []
    for item in names:
        target = item['target']
        assert 0 < len(target) <= 6, item['name_id']
        targets.append(target)
        for alias in dict.fromkeys(item['source_forms'] + item['radio_aliases']):
            key = alias.lower()
            value = (target, item['preserve_ascii_case'])
            assert key not in seen or seen[key] == value, alias
            if key in seen:
                continue
            seen[key] = value
            rows.append((item['name_id'], alias, target, str(value[1]).lower()))
    assert seen['yifany'] == seen['yiffany']
    source = HELPER.read_text(encoding='utf-8')
    marker = '    // Generated from '
    start = source.index(marker) if marker in source else source.index('    private static boolean localized(')
    localized = list(dict.fromkeys(t for t in targets if any(ord(c) > 127 for c in t)))
    code = '    // Generated from translations/character-names.json; independently reviewed localization names.\n'
    code += '    private static boolean localized(String text) {\n        return text != null && ('
    code += '\n            || '.join('text.contains("%s")' % t for t in localized)
    code += ');\n    }\n\n    /** Exact names only: never infer hidden actors or rewrite script keys. */\n'
    code += '    public static String display(String name) {\n'
    for _, alias, target, preserve in rows:
        code += '        if ("%s".equalsIgnoreCase(name)) return %s;\n' % (alias, 'name' if preserve == 'true' else '"%s"' % target)
    code += '        return name;\n    }\n}\n'
    component = json.loads(COMPONENT.read_text(encoding='utf-8'))
    component['required_chars'] = [' '.join(dict.fromkeys(targets))]
    tsv = '# ledger_sha256=' + hashlib.sha256(raw).hexdigest() + '\n'
    tsv += '# reviewed localization registry; not an author-official etymology claim\nname_id\tsource\ttarget\tpreserve_ascii_case\n'
    tsv += ''.join('\t'.join(row) + '\n' for row in rows)
    return {HELPER: source[:start] + code, COMPONENT: json.dumps(component, ensure_ascii=False, indent=2) + '\n', TSV: tsv}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for path, content in outputs().items():
        if args.check:
            assert path.read_text(encoding='utf-8') == content, 'stale: ' + str(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    print('RADIO_NAMES_SYNC_OK names=36 aliases=37 registry_status=reviewed_for_application')


if __name__ == '__main__':
    main()
