"""独立核验 R4 台账：每个 op 的定位与旧值必须真实存在于 candidate8 归档。

不复用 build_decisions.py 的解析路径（重新实现 locator 解析），只读归档。
"""
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r28-character-names-candidate8'
LEDGER = LOC / 'translations' / 'editorial-r4-pending-repairs.jsonl'
DECISIONS = LOC / 'editorial' / 'r4-pending' / 'reports' / 'pending-01' / 'decisions.tsv'


def get_pointer(doc, ptr):
    node = doc
    for token in ptr[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        node = node[int(token)] if isinstance(node, list) else node[token]
    return node


def main():
    acc = json.loads((CAND / 'acceptance.json').read_text('utf-8'))
    archives = {}
    for name in ('cosmobreeder-multi.jar', 'patch.pak'):
        data = (CAND / name).read_bytes()
        if sha256(data).hexdigest() != acc['archives'][name]:
            raise SystemExit(f'archive drift: {name}')
        archives[name] = zipfile.ZipFile(CAND / name)

    ops = [json.loads(s) for s in LEDGER.read_text('utf-8').splitlines() if s.strip()]
    required = {'op_id', 'archive', 'archive_entry', 'kind', 'before_resource_sha256',
                'old', 'new', 'finding_ids', 'source_refs'}
    for op in ops:
        if not required <= set(op):
            raise SystemExit(f"{op.get('op_id')}: missing engine fields")
        if op['kind'] == 'json' and 'pointer' not in op:
            raise SystemExit(f"{op['op_id']}: json op needs pointer")
        if op['kind'] == 'line' and not isinstance(op.get('line'), int):
            raise SystemExit(f"{op['op_id']}: line op needs line index")
        if not op['source_refs'] or any(not isinstance(x, str) or not x for x in op['source_refs']):
            raise SystemExit(f"{op['op_id']}: bad source_refs")
    if len(ops) != len({o['op_id'] for o in ops}):
        raise SystemExit('duplicate op_id')

    cache = {}

    def raw(archive, entry):
        key = (archive, entry)
        if key not in cache:
            cache[key] = decrypt_file(archives[archive].read(key[1]))
        return cache[key]

    ok = 0
    for op in ops:
        res_sha = sha256(raw(op['archive'], op['archive_entry'])).hexdigest()
        if res_sha != op['before_resource_sha256']:
            raise SystemExit(f"{op['op_id']}: resource SHA mismatch")
        if op['kind'] == 'json':
            doc = json.loads(raw(op['archive'], op['archive_entry']))
            actual = get_pointer(doc, op['pointer'])
            if actual != op['old']:
                raise SystemExit(f"{op['op_id']}: old mismatch {actual!r} != {op['old']!r}")
        elif op['kind'] == 'line':
            lines = raw(op['archive'], op['archive_entry']).decode('utf-8').splitlines()
            if lines[op['line'] - 1] != op['old']:
                raise SystemExit(f"{op['op_id']}: line {op['line']} mismatch")
        else:
            raise SystemExit(f"{op['op_id']}: unknown kind {op['kind']}")
        if op['old'] == op['new']:
            raise SystemExit(f"{op['op_id']}: no-op")
        ok += 1

    # 决策表覆盖 45 条 defer
    rows = [l.split('\t') for l in DECISIONS.read_text('utf-8').splitlines() if l.strip()]
    header, body = rows[0], rows[1:]
    if len(body) != 45:
        raise SystemExit(f'decisions rows {len(body)} != 45')
    if len({r[0] for r in body}) != 45:
        raise SystemExit('duplicate finding ids in decisions')
    apply_ids = {o['finding_ids'][0] for o in ops}
    table_apply = {r[0] for r in body if r[1] == 'apply'}
    if apply_ids != table_apply:
        raise SystemExit(f'apply/ledger mismatch: {sorted(apply_ids ^ table_apply)}')
    for r in body:
        if r[1] == 'apply' and int(r[3]) != sum(1 for o in ops if o['finding_ids'][0] == r[0]):
            raise SystemExit(f'{r[0]}: apply_ops column mismatch')

    print(f'verified ops: {ok}')
    print(f'decisions: {len(body)} rows, dispositions consistent')
    print('apply findings:', sorted(apply_ids))


if __name__ == '__main__':
    main()
