"""Write the r9 batch-15 decision table from the archive scan.

One decision per row, replacing every minority spelling found in that line with
the majority one. The hit list comes from `tools/scan_residual_archive.py`, which
reads the base candidate's own archives — so this also covers the patch.pak twins
that earlier batches left behind.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

VARIANTS = {
    '狗头人': ('科博德', 'kobold 在库内作「科博德」99 处、「狗头人」10 处'),
    '吠叫者': ('吠犬', 'BARKER 在库内作「吠犬」40 处、「吠叫者」1 处'),
    '探员': ('特工', 'agent 在库内作「特工」471 处、「探员」3 处'),
    '宇航服': ('宇宙服', 'COSMOSUIT 在库内作「宇宙服」19 处、「宇航服」9 处'),
    '电击器': ('电击枪', 'TAZER 在库内作「电击枪」92 处、「电击器」10 处，其中一处是早前批次反向改出来的'),
    'UP+攻击': ('UP+ATTACK', '按键名一律保留英文（R9 batch-01 已裁决）'),
    'DOWN+攻击': ('DOWN+ATTACK', '按键名一律保留英文（R9 batch-01 已裁决）'),
    '高级芯片': ('花哨芯片', 'FANCY CHIPS 在库内作「花哨芯片」3 处、「高级芯片」1 处'),
    '卫星通讯': ('卫星链路', 'SATLINK 在库内作「卫星链路」3 处、「卫星通讯」1 处'),
}

# The independent review caught a false positive the mechanical scan cannot see:
# 「电击器」 inside 「光电击器／光刃电击器」 is LIGHTTAZER, not TAZER, and plain
# `space suit` is not COSMOSUIT. Those rows keep their wording until the two
# names are ruled on; the rest of the scan stands.
LIGHTTAZER = {
    'P15:cosmobreeder-multi.jar:datadf/1:487',
    'P15:cosmobreeder-multi.jar:datadm/1:471',
    'P15:patch.pak:datadf/1:487',
    'P15:patch.pak:datadm/1:470',
    'P15:cosmobreeder-multi.jar:vsn/47:17',
}
SPACE_SUIT = {
    'P15:cosmobreeder-multi.jar:datadf/1:1504',
    'P15:cosmobreeder-multi.jar:datadm/1:1502',
    'P15:patch.pak:datadf/1:1502',
    'P15:patch.pak:vsn/59:7',
}

hits = json.loads(Path('batch-15/orders/batch-15.hits.json').read_text('utf8'))
by_row = {row_id: words for scene_rows in hits.values() for row_id, words in scene_rows}

b = Batch('batch-15')
applied = 0
for row_id, (scene_id, row) in sorted(b.rows.items()):
    words = by_row.get(row_id)
    if not words:
        continue
    if row_id in LIGHTTAZER:
        b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'reject', '',
               '英文是 `lighttazer`（官方海盗光…电击器／光刃电击器），「电击器」是 LIGHTTAZER 的译法，'
               '不是 TAZER；LIGHTTAZER 的中文名未终裁，不能按 TAZER 统一。')
        continue
    if row_id in SPACE_SUIT:
        b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'reject', '',
               '英文是 `space suit`／`spacesuit`（普通太空服），不是 COSMOSUIT，也没有 `inCosmoSuit()` 条件；'
               '改成「宇宙服」会把普通太空服说成宇宙服。')
        continue
    current = row.get('current') or ''
    final = current
    reasons = []
    for word in words:
        good, why = VARIANTS[word]
        final = final.replace(word, good)
        reasons.append('%s→%s：%s' % (word, good, why))
    if final == current:
        raise SystemExit('%s: replacement produced no change' % row_id)
    b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final,
           '；'.join(reasons) + '。同一句在 jar 与 patch.pak 各有一份，两份都改。')
    applied += 1

b.emit_trailing_space(reason='中文行尾多出半角空格，英文原文行尾没有；只删空格。')
print(b.close())
print('rows applied:', applied)
