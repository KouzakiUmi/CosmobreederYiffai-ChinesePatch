"""R8：Fenfen 谜题第 5 条提示按同族排列约束改为“不相邻”。

六条提示中五条描述先后位置（之间/最前/之后/不是最后），第 5 条 TOUCH 指序列或格位上的相邻；
“不接触”既不合族群也会被读成“不能碰”。本次改两版内容、两层归档共 4 处，并补「邻」字形。
锚定 candidate11；只写台账与处置表。
"""
import csv
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R8 = LOC / 'editorial' / 'r8-puzzle'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r6-consistency-candidate11'
OLD = 'Fenfen故事第5部分。|$在你脑中回响着：|$[心不接触十字]'
NEW = 'Fenfen故事第5部分。|$在你脑中回响着：|$[心形与十字不相邻]'
KEYS = ['ui.data.f_AgentFZ5.desc', 'ui.data.m_AgentMZ5.desc']
ARCHIVES = ['cosmobreeder-multi.jar', 'patch.pak']

REASON = ('同族六条提示有五条是先后位置约束（之间/最前/之后/不是最后），第 5 条的 TOUCH 只能理解为'
          '序列或格位上的相邻；“不接触”不合族群且有“不能碰”的误读。改为“心形与十字不相邻”。'
          '数据书容器 224px、最多 3 行，新文仍 1 行 100px，不越界。')


def main():
    archives = {n: zipfile.ZipFile(CAND / n) for n in ARCHIVES}
    ledger = []
    n = 0
    for archive in ARCHIVES:
        data = decrypt_file(archives[archive].read('datav/1'))
        doc = json.loads(data)
        for key in KEYS:
            if doc[key] != OLD:
                raise SystemExit(f'{archive} {key}: unexpected current value {doc[key]!r}')
            n += 1
            ledger.append({
                'op_id': f'R8-{n:04d}',
                'archive': archive,
                'archive_entry': 'datav/1',
                'kind': 'json',
                'before_resource_sha256': sha256(data).hexdigest(),
                'old': OLD,
                'new': NEW,
                'finding_ids': ['P08-022'],
                'source_refs': ['R1:P08-022',
                                'localization/editorial/r7-render/README.md',
                                'localization/editorial/r8-puzzle/reports/puzzle-01/decisions.tsv'],
                'pointer': '/' + key,
            })
    out = R8 / 'reports' / 'puzzle-01'
    out.mkdir(parents=True, exist_ok=True)
    ledger_path = LOC / 'translations' / 'editorial-r8-puzzle-repairs.jsonl'
    ledger_path.write_text('\n'.join(json.dumps(o, ensure_ascii=False) for o in ledger) + '\n',
                           encoding='utf-8')
    with (out / 'decisions.tsv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['finding_id', 'disposition', 'evidence_class', 'ops', 'reason'])
        w.writerow(['P08-022', 'apply', 'sibling_constraint_family', len(ledger), REASON])
    print('ops:', len(ledger))
    for o in ledger:
        print(' ', o['op_id'], o['archive'], o['pointer'])


if __name__ == '__main__':
    main()
