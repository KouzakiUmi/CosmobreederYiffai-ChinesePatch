"""Self-check of the batch-19 ledger invariants (read-only).

Runs the same three checks an outside reviewer would: every change is a quote
swap, the quote pairs are balanced, and no full-width quote ends up wrapping a
pure-Latin run (the scan is supposed to leave those as ASCII).
"""
from pathlib import Path
import difflib
import json

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
LEDGER = ROOT / 'localization/translations/editorial-r9-batch-19-repairs.jsonl'
OPEN_D, CLOSE_D = '\u201c', '\u201d'
OPEN_S, CLOSE_S = '\u2018', '\u2019'

ops = [json.loads(line) for line in LEDGER.read_text('utf8').splitlines() if line.strip()]

off_quote = []
for op in ops:
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, op['old'], op['new']).get_opcodes():
        if tag == 'equal':
            continue
        a, b = op['old'][i1:i2], op['new'][j1:j2]
        allowed = (a == '"' and b in (OPEN_D, CLOSE_D)) or (a == "'" and b in (OPEN_S, CLOSE_S))
        if not allowed:
            off_quote.append((op['op_id'], repr(a), repr(b)))

unbalanced = [op['op_id'] for op in ops
              if op['new'].count(OPEN_D) != op['new'].count(CLOSE_D)
              or op['new'].count(OPEN_S) != op['new'].count(CLOSE_S)]

latin_inside = []
for op in ops:
    text = op['new']
    for opener, closer in ((OPEN_D, CLOSE_D), (OPEN_S, CLOSE_S)):
        start = text.find(opener)
        while start != -1:
            end = text.find(closer, start + 1)
            if end == -1:
                break
            inner = text[start + 1:end]
            if inner and all(ch.isascii() for ch in inner):
                latin_inside.append((op['op_id'], inner))
            start = text.find(opener, end + 1)

print(json.dumps({
    'operations': len(ops),
    'kinds': sorted({op['kind'] for op in ops}),
    'non_quote_changes': off_quote,
    'unbalanced': unbalanced,
    'latin_inside_full_width': latin_inside,
}, ensure_ascii=False, indent=1))
