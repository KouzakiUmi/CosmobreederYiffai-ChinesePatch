"""Emit batch-19 decisions: every scanned quote rewrite is a straight apply.

The scan already produced the target text, so there is nothing to adjudicate
per row — the only judgement (full-width quotes around Han, keep ASCII around
Latin) lives in `scan_batch19.rewrite`.
"""
from pathlib import Path
import json

R9 = Path(__file__).resolve().parents[1]
BATCH = R9 / 'batch-19'
SYMBOL_FOR_NEWLINE = '␊'  # the ledger restores these into real line breaks
ORDER = json.loads((BATCH / 'orders/batch-19.json').read_text('utf8'))
HITS = json.loads((BATCH / 'orders/batch-19.hits.json').read_text('utf8'))

REASON = ('中文引号：story12.fnt 的 ASCII 引号是 8px 字形（" 7x5、\' 6x5），'
          '汉字是 12px；直引号夹在汉字里会小一号且偏离基线。'
          '引号内是纯拉丁的保持原样，因为那里 8px 才配得上拉丁字。')

header = ['finding_id', 'route', 'severity', 'category', 'scene_id', 'row_id',
          'decision', 'final_zh', 'reason']
rows = []
for scene_id, entries in HITS.items():
    for row_id, hits, current, target in entries:
        assert current != target, row_id
        # card values keep their own line breaks; only quote marks may change
        assert target.count('\n') == current.count('\n'), row_id
        # card values carry real line breaks; a raw LF would split the TSV row
        rows.append(['R9M-%s' % row_id, 'R9M', 'B', 'punct', scene_id, row_id,
                     'apply', target.replace('\n', SYMBOL_FOR_NEWLINE), REASON])
rows.sort(key=lambda r: (r[4], r[5]))
out = BATCH / 'review'
out.mkdir(parents=True, exist_ok=True)
text = '\t'.join(header) + '\r\n' + ''.join('\t'.join(r) + '\r\n' for r in rows)
(out / 'decisions.tsv').write_text(text, 'utf8', newline='')
print(json.dumps({'decisions': len(rows), 'apply': len(rows)}, ensure_ascii=False))
