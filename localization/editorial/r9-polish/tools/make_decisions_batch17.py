"""Write the r9 batch-17 decision table: FENFEN is 芬芬.

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
    '干员': ('特工', 'agent 在库内作「特工」548 处、「干员」8 处；batch-15 当时只扫了「探员」，漏了这一个同义写法。'),
    '光电击器': ('光击枪', 'LIGHTTAZER 统一作「光击枪」：TAZER 是「电击枪」，LIGHT TAZER 省掉重复的「电」；「光电击器」读起来像光电-击器。'),
    '光刃电击器': ('光击枪', 'LIGHTTAZER 统一作「光击枪」；「光刃电击器」把 light 读成了「光刃」。'),
}

hits = json.loads(Path('batch-17/orders/batch-17.hits.json').read_text('utf8'))
by_row = {row_id: words for scene_rows in hits.values() for row_id, words in scene_rows}

b = Batch('batch-17')
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
