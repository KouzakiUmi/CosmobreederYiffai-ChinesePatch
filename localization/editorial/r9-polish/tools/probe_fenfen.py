"""Dump every player-visible `Fenfen` occurrence, with an honest count.

An earlier probe listed 337 "rows" but used only the script-line filter, so it
included rows that contain the token without any Chinese text. This one keeps
the stricter definition: a row counts only if it is player-visible (not a tag,
include or condition) *and* contains Han characters.

It also answers the question the docs got wrong: is any `Fenfen` sitting in the
speaker slot (`Fenfen: [...]`)? Those are engine-side actor lookups and must not
be rewritten.
"""
import json
import re
import sys
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(R9 / 'tools'))
import r9_targets as t

CAND = ROOT / 'localization/builds/r9-polish-candidate47'
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^\\s*([A-Za-z_][A-Za-z0-9_ ]*)\\s*:\\s*\\[')
OUT = R9 / 'out/layout/probe/fenfen-hits.json'


def player(text):
    body = text.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def main():
    records = []
    actor_rows = []
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        side = 'sfw' if archive.endswith('.jar') else 'nsfw'
        for entry in ('datadf/1', 'datadm/1'):
            state, _ = t.resource_state(CAND, archive, entry, 'line')
            for n, line in enumerate(state['lines'], 1):
                if not player(line) or 'Fenfen' not in line:
                    continue
                match = ACTOR.match(line)
                in_actor = bool(match and 'Fenfen' in match.group(1))
                records.append({'side': side, 'archive': archive, 'entry': entry, 'line': n,
                                'kind': 'line', 'count': line.count('Fenfen'),
                                'actor_slot': in_actor, 'text': line})
                if in_actor:
                    actor_rows.append((archive, entry, n))
        state, _ = t.resource_state(CAND, archive, 'datav/1', 'json')
        for key, value in state['document'].items():
            if isinstance(value, str) and player(value) and 'Fenfen' in value:
                records.append({'side': side, 'archive': archive, 'entry': 'datav/1', 'key': key,
                                'kind': 'value', 'count': value.count('Fenfen'),
                                'actor_slot': False, 'text': value})
        import zipfile
        with zipfile.ZipFile(CAND / archive) as z:
            entries = sorted(x for x in z.namelist() if x.startswith('vsn/') and x != 'vsn/0')
        for entry in entries:
            try:
                state, _ = t.resource_state(CAND, archive, entry, 'line')
            except Exception:
                continue
            for n, line in enumerate(state['lines'], 1):
                if not player(line) or 'Fenfen' not in line:
                    continue
                records.append({'side': side, 'archive': archive, 'entry': entry, 'line': n,
                                'kind': 'line', 'count': line.count('Fenfen'),
                                'actor_slot': False, 'text': line})

    by_source = {}
    for record in records:
        key = record['entry'].split('/')[0]
        by_source[key] = by_source.get(key, 0) + record['count']
    summary = {
        'candidate': 'r9-polish-candidate47',
        'definition': 'player-visible rows/values that contain Han characters and the token',
        'occurrences': sum(record['count'] for record in records),
        'locations': len(records),
        'by_source': by_source,
        'actor_slot_locations': len(actor_rows),
        'records': records,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({k: summary[k] for k in
                      ('occurrences', 'locations', 'by_source', 'actor_slot_locations')},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
