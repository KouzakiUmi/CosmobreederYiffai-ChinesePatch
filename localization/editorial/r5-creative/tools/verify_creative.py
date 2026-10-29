"""R5 独立核验：重新解析定位器，确认台账每条旧行与整资源 SHA 实测存在。

不复用 build_creative.py 的解析路径。
"""
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R5 = LOC / 'editorial' / 'r5-creative'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r4-pending-candidate9'
LEDGER = LOC / 'translations' / 'editorial-r5-creative-repairs.jsonl'
DECISIONS = R5 / 'reports' / 'creative-01' / 'decisions.tsv'


def main():
    records = [json.loads(s) for s in LEDGER.read_text('utf-8').splitlines() if s.strip()]
    seen = set()
    for op in records:
        if op['op_id'] in seen:
            raise SystemExit(f"duplicate op_id {op['op_id']}")
        seen.add(op['op_id'])
        for field in ('archive', 'archive_entry', 'kind', 'before_resource_sha256',
                      'old', 'new', 'finding_ids', 'source_refs', 'line'):
            if field not in op:
                raise SystemExit(f"{op['op_id']}: missing {field}")
        if op['kind'] != 'line':
            raise SystemExit(f"{op['op_id']}: only line ops expected")
        if not isinstance(op['line'], int):
            raise SystemExit(f"{op['op_id']}: bad line index")
        if op['old'] == op['new']:
            raise SystemExit(f"{op['op_id']}: no-op")
        if not op['source_refs']:
            raise SystemExit(f"{op['op_id']}: empty source_refs")

    cache = {}
    for op in records:
        key = (op['archive'], op['archive_entry'])
        if key not in cache:
            with zipfile.ZipFile(CAND / key[0]) as z:
                cache[key] = decrypt_file(z.read(key[1]))
        if sha256(cache[key]).hexdigest() != op['before_resource_sha256']:
            raise SystemExit(f"{op['op_id']}: resource SHA mismatch")
        lines = cache[key].decode('utf-8').splitlines()
        if not 1 <= op['line'] <= len(lines):
            raise SystemExit(f"{op['op_id']}: line out of range")
        if lines[op['line'] - 1] != op['old']:
            raise SystemExit(f"{op['op_id']}: old line mismatch")

    rows = [l.split('\t') for l in DECISIONS.read_text('utf-8').splitlines() if l.strip()][1:]
    disposition = {r[0]: r[1] for r in rows}
    findings = sorted({op['finding_ids'][0] for op in records})
    if findings != sorted(disposition):
        raise SystemExit(f'decision/ledger finding mismatch: {findings}')
    for r in rows:
        if r[1] != 'apply':
            raise SystemExit(f'{r[0]}: expected apply, got {r[1]}')
        ops = sum(1 for op in records if op['finding_ids'][0] == r[0])
        if int(r[3]) != ops:
            raise SystemExit(f'{r[0]}: ops column {r[3]} != {ops}')
    print(f'verified ops: {len(records)}')
    print('findings:', findings)


if __name__ == '__main__':
    main()
