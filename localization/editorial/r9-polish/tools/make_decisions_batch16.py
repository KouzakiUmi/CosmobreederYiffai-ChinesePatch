"""Write the r9 batch-16 decision table: FENFEN is 芬芬.

Small batch, but it closes the last naming item that had a corpus answer:

* `FENFEN` already reads 芬芬 in three places (dictionary `ClassicFenfen`, and the
  Starkill／Dragon card text 「芬芬长老」). The one dialogue line still spelled it
  in Latin.
* The item `SpecialNecklace` is `FENFEN T`, and it was translated 「翻译项链」 —
  FENFEN was read as "translation". It becomes 「芬芬 T」, keeping the `T` because
  the English keeps it and we have no evidence what it stands for.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

VARIANTS = {
    '翻译项链': ('芬芬 T', '物品 `SpecialNecklace` 的英文是 `FENFEN T`；「翻译项链」把 FENFEN 读成了 translation。'),
    'FENFEN': ('芬芬', 'FENFEN 在库内已作「芬芬」3 处（词典 `ClassicFenfen`、Starkill 与 Dragon 卡面的「芬芬长老」）。'),
}

hits = json.loads(Path('batch-16/orders/batch-16.hits.json').read_text('utf8'))
by_row = {row_id: words for scene_rows in hits.values() for row_id, words in scene_rows}

b = Batch('batch-16')
applied = 0
for row_id, (scene_id, row) in sorted(b.rows.items()):
    words = by_row.get(row_id)
    if not words:
        continue
    current = row.get('current') or ''
    final = current
    reasons = []
    for word in words:
        good, why = VARIANTS[word]
        final = final.replace(word, good)
        reasons.append('%s→%s：%s' % (word, good, why))
    if final == current:
        raise SystemExit('%s: no change' % row_id)
    b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final,
           '；'.join(reasons) + '同一句／同一个值在 jar 与 patch.pak 各有一份，两份都改。')
    applied += 1

b.emit_trailing_space(reason='中文行尾多出半角空格，英文原文行尾没有；只删空格。')
print(b.close())
print('rows applied:', applied)
