"""How many bad splits could be fixed if pagination were allowed to grow?

The user's rule forbids growing pages, but before treating "grow" as off the
table it is worth knowing the size of what that rule excludes. This is a
measurement only: it does not write any ledger and does not change any candidate.

It reports, for each allowance (+0, +1, +2 drawn rows), how many especially-bad
rows could be repaired, split by whether the row sits at a staging hand-off.
"""
import json
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import audit_bad_splits as A  # noqa: E402
import r9_targets as t  # noqa: E402

data = json.loads((R9 / 'batch-24/orders/bad-splits.json').read_text('utf8'))

bigrams = Counter()
for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
    for entry in ('datadf/1', 'datadm/1'):
        for line in t.resource_state(A.CAND, archive, entry, 'line')[0]['lines']:
            body = A.body_of(line)
            if not A.HAN.search(body):
                continue
            han = [c for c in body if '\u4e00' <= c <= '\u9fff']
            for a, b in zip(han, han[1:]):
                bigrams[a + b] += 1


def splits_of(body):
    drawn = A.wrap(body)
    return [(i, drawn[i][-1] + drawn[i + 1][0]) for i in range(len(drawn) - 1)
            if drawn[i] and drawn[i + 1]
            and bigrams.get(drawn[i][-1] + drawn[i + 1][0], 0) >= A.SOLID_PAIR]


def grow_attempt(body, limit):
    drawn = A.wrap(body)
    splits = splits_of(body)
    if not splits:
        return None
    flat = body.replace(A.BREAK, '')
    for idx, _pair in splits:
        head = ''.join(drawn[:idx + 1])
        tail = ''.join(drawn[idx + 1:])
        for back in range(1, min(len(head), 20) + 1):
            moved = head[-back:]
            pieces = list(drawn[:idx]) + [head[:-back], moved + tail]
            candidate = A.BREAK.join(piece for piece in pieces if piece)
            if candidate.replace(A.BREAK, '') != flat:
                continue
            redrawn = A.wrap(candidate)
            if len(redrawn) > len(drawn) + limit:
                continue
            if splits_of(candidate):
                continue
            return len(redrawn) - len(drawn)
    return None


for limit in (0, 1, 2):
    stats = Counter()
    for row in data['rows']:
        if row['worst_word'] < A.LONG_WORD:
            continue
        grew = grow_attempt(row['text'], limit)
        if grew is None:
            continue
        stats[('hand-off' if row['handoff'] else 'free', grew)] += 1
    total = sum(stats.values())
    free = sum(v for (k, _g), v in stats.items() if k == 'free')
    print('allowance +%d row(s): %4d fixable (%d not at a hand-off)  %s'
          % (limit, total, free, dict(sorted(stats.items()))))
