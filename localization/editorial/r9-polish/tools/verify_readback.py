"""Check every landed operation against a built candidate's plaintext.

`verify_round` proves a batch applies cleanly on its base. This proves the built
candidate actually carries the text, which catches a batch that silently failed
to merge, a component.json entry in the wrong order, or a later batch overwriting
an earlier one. Read-only.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R9 = LOC / 'editorial/r9-polish'
sys.path.insert(0, str(R9 / 'tools'))
import r9_targets as targets  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('candidate', help='build directory under localization/builds')
    a = ap.parse_args()
    candidate = LOC / 'builds' / a.candidate
    component = json.loads((LOC / 'optimization/r28/r9polish/component.json').read_text('utf8'))
    state = {}
    problems, checked = [], 0
    for batch in component['batches']:
        ledger = Path(batch['ledger'])
        if not ledger.is_absolute():
            ledger = ROOT / ledger
        if not ledger.exists():
            problems.append('missing ledger: ' + str(ledger))
            continue
        for line in ledger.read_text('utf8').splitlines():
            if not line.strip():
                continue
            op = json.loads(line)
            key = (op['archive'], op['archive_entry'])
            if key not in state:
                state[key] = targets.resource_state(candidate, key[0], key[1], op['kind'])
            value = targets.old_text(state[key][0], op['kind'], op.get('pointer') or op.get('line'), None)
            checked += 1
            if value != op['new']:
                problems.append('%s %s %s: candidate has %r, ledger expects %r'
                                % (batch['batch'], op['op_id'], op.get('pointer') or op.get('line'),
                                   value[:40], op['new'][:40]))
    print(json.dumps({'candidate': a.candidate, 'operations_checked': checked,
                      'batches': len(component['batches']), 'problems': problems[:20],
                      'problem_count': len(problems)}, ensure_ascii=False, indent=1))
    raise SystemExit(1 if problems else 0)


if __name__ == '__main__':
    main()
