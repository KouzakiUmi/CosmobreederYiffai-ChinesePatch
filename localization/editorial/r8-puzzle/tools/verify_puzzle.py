"""R8 独立核验：定位器重解 + 旧值实测。"""
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r6-consistency-candidate11'
LEDGER = LOC / 'translations' / 'editorial-r8-puzzle-repairs.jsonl'


def main():
    ops = [json.loads(s) for s in LEDGER.read_text('utf-8').splitlines() if s.strip()]
    cache = {}
    for op in ops:
        key = (op['archive'], op['archive_entry'])
        if key not in cache:
            with zipfile.ZipFile(CAND / key[0]) as z:
                cache[key] = decrypt_file(z.read(key[1]))
        if sha256(cache[key]).hexdigest() != op['before_resource_sha256']:
            raise SystemExit(f"{op['op_id']}: resource SHA mismatch")
        doc = json.loads(cache[key])
        node = doc
        for token in op['pointer'][1:].split('/'):
            node = node[token]
        if node != op['old']:
            raise SystemExit(f"{op['op_id']}: old mismatch")
        if op['old'] == op['new']:
            raise SystemExit(f"{op['op_id']}: no-op")
    print(f'verified ops: {len(ops)}')


if __name__ == '__main__':
    main()
