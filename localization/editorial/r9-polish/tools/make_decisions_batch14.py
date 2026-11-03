"""Write the r9 batch-14 decision table (DS route; Grok route appended later).

This batch is a copy-alignment batch, not a fresh translation pass: the 21 scenes
are the sfw (jar) side, and their sentences also exist on the pak side, where
batch-01 already polished them. The independent evidence for each proposal is that
the proposed line equals the pak-side landed text character for character — I
checked all twenty against `candidate44`'s `patch.pak datadf/1`／`datadm/1`
(longest-match per row); nineteen match exactly.

The one that does not match is P14-0110: the pak side still says 「那片区域那边怎么了」,
and the proposal invents a different wording. Aligning the two copies matters more
than polishing one of them, so it is rejected and noted.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

b = Batch('batch-14')

ALIGN = '本行与 patch.pak 侧同句是同一句话的两份；pak 侧在 batch-01 已精校，sfw 侧是旧副本。改成 pak 落地文本，两份一致。'

# finding -> the rows it covers (some findings cover several identical lines)
TARGETS = {
    'P14-0115': ['SFW7e606362a247bdb62af6867a', 'SFWaf565ae95ed0e28c813cb8fc'],
    'P14-0119': ['SFW5edb695493e80313202c08a1', 'SFW5f20146db1eafff3f27c4e8e'],
}

findings = {}
for line in (Path('batch-14/ds/findings.jsonl')).read_text('utf8').splitlines():
    if line.strip():
        f = json.loads(line)
        findings[f['finding_id']] = f

rejects = {
    'P14-0110': 'pak 侧同句就是当前写法（「那片区域那边怎么了」），本条提的是新措辞；'
                '本批的目标是让两侧一致，不是把一侧润色成第三种说法。记为可选润色，留 LEFTOVERS。',
}

for fid, f in sorted(findings.items()):
    if fid in rejects:
        b.reject('ds:' + fid, rejects[fid])
        continue
    final = f['proposed_zh']
    rows = TARGETS.get(fid, [f['row_ids'][0]])
    for row_id in rows:
        b.emit('R9M-' + fid + '-' + row_id[-6:], 'R9M', f.get('severity', 'B'),
               f.get('category', 'term'), row_id, 'apply', final,
               ALIGN + ' 提案原文：%s' % (f.get('reason') or '').strip()[:160])

# Second route (Grok) proposed 25 changes. Twenty-one of them land on exactly the
# same text as the pak side, i.e. the same fix as the DS route, so they are
# recorded as duplicates. The other four invent a wording the pak side does not
# use; aligning the two copies matters more than polishing one of them.
GROK_SAME = {'P14-X001', 'P14-X002', 'P14-X003', 'P14-X004', 'P14-X006', 'P14-X007', 'P14-X008',
             'P14-X009', 'P14-X010', 'P14-X012', 'P14-X013', 'P14-X014', 'P14-X016', 'P14-X017',
             'P14-X018', 'P14-X019', 'P14-X020', 'P14-X021', 'P14-X022', 'P14-X023', 'P14-X024',
             'P14-X025'}
for route_finding in sorted(GROK_SAME):
    b.reject('grok:' + route_finding, '与 DS 路同一点、同一条 pak 落地文本，取一条落地。')
for route_finding in ('P14-X005', 'P14-X011', 'P14-X015'):
    b.reject('grok:' + route_finding,
             'pak 侧同句就是当前写法，本条提的是新措辞；本批目标是让两侧一致，不把一侧润色成第三种说法。'
             '记入 LEFTOVERS 作为可选润色。')

b.emit_trailing_space(reason='中文行尾多出半角空格，英文原文行尾没有；只删空格。')
print(b.close())
