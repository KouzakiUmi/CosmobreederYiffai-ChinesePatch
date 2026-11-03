"""Where does `Fenfen` actually sit in player-visible text?

The earlier note claimed 39 occurrences fall in the speaker slot. This checks
that claim directly: a speaker-slot hit is a row shaped `Name: [...]` whose
`Name` contains `Fenfen`. Everything else is prose.
"""
import re
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(R9 / 'tools'))
import r9_targets as t

CAND = ROOT / 'localization/builds/r9-polish-candidate47'
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^\\s*([A-Za-z_][A-Za-z0-9_ ]*)\\s*:\\s*\\[')


def player(x):
    body = x.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


actor = []
prose = Counter()
for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
    for entry in ('datadf/1', 'datadm/1'):
        state, _ = t.resource_state(CAND, archive, entry, 'line')
        for n, line in enumerate(state['lines'], 1):
            if not player(line) or 'Fenfen' not in line:
                continue
            m = ACTOR.match(line)
            if m and 'Fenfen' in m.group(1):
                actor.append((archive[:3], entry, n, line.strip()[:64]))
            else:
                prose[entry] += line.count('Fenfen')
    state, _ = t.resource_state(CAND, archive, 'datav/1', 'json')
    for key, value in state['document'].items():
        if isinstance(value, str) and 'Fenfen' in value:
            prose['datav'] += value.count('Fenfen')

print('speaker-slot hits:', len(actor))
for row in actor[:5]:
    print('  ', row)
print('prose occurrences:', sum(prose.values()), '|', dict(prose))
