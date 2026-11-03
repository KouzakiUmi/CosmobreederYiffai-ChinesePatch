"""Emit batch-20 decisions: every scanned Fenfen hit is a straight apply.

The scan already produced the target text; the judgement (glossary term
「芬芬」, and the stray Chinese-Latin space that hugs the token) lives in
`scan_batch20.rewrite`. Multi-line card values are carried through the `␊`
sentinel, which the shared text rule expands on both sides.
"""
from pathlib import Path
import json

R9 = Path(__file__).resolve().parents[1]
BATCH = R9 / 'batch-20'
ORDER = json.loads((BATCH / 'orders/batch-20.json').read_text('utf8'))
HITS = json.loads((BATCH / 'orders/batch-20.hits.json').read_text('utf8'))
SYMBOL_FOR_NEWLINE = '\u240a'

REASON = ('glossary 的条目是「Fenfen／种族名／芬芬」（状态 proposed）；batch-16 只改了'
          '三处全大写 FENFEN，驼峰写法一直没跟上。引号与上下文保持不变，'
          '紧贴 token 的单个空格随 token 一起去掉（那是中英之间的旧间距）。')

header = ['finding_id', 'route', 'severity', 'category', 'scene_id', 'row_id',
          'decision', 'final_zh', 'reason']
rows = []
for scene_id, entries in HITS.items():
    for row_id, hits, current, target in entries:
        assert current != target, row_id
        assert target.count('\n') == current.count('\n'), row_id
        assert 'Fenfen' not in target, row_id
        rows.append(['R9M-%s' % row_id, 'R9M', 'B', 'term', scene_id, row_id,
                     'apply', target.replace('\n', SYMBOL_FOR_NEWLINE), REASON])
rows.sort(key=lambda r: (r[4], r[5]))
out = BATCH / 'review'
out.mkdir(parents=True, exist_ok=True)
text = '\t'.join(header) + '\r\n' + ''.join('\t'.join(r) + '\r\n' for r in rows)
(out / 'decisions.tsv').write_text(text, 'utf8', newline='')
print(json.dumps({'decisions': len(rows), 'apply': len(rows),
                  'multiline': sum(1 for r in rows if SYMBOL_FOR_NEWLINE in r[7])},
                 ensure_ascii=False))
