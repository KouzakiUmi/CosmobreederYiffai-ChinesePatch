"""Export or verify the public scene-audit index without copying source columns."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

from tl_tool import ROOT, _read_tsv


def digest(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def load_rows(directory: Path) -> dict[str, tuple[str, list[str]]]:
    rows = {}
    for kind, columns in (('dialogue', 8), ('ui', 6), ('vsn', 8)):
        for path in sorted((directory / kind).glob('*.tsv')):
            chunk = path.relative_to(directory).as_posix()
            for row in _read_tsv(path, columns):
                seq = row[0]
                if seq in rows:
                    raise ValueError(f'重复的译文 ID：{seq}')
                rows[seq] = (chunk, row)
    if not rows:
        raise ValueError(f'找不到译文分块：{directory}')
    return rows


def public_target(row: list[str]) -> dict[str, str]:
    source, target = row[-2:]
    if target == source or target.startswith('__RAW__:'):
        return {}
    if source.strip() and source in target:
        return {}
    if target and not re.search(r'[\u3400-\u9fff]', target):
        return {}
    return {'target': target}


def identity(chunk: str, row: list[str]) -> dict[str, str]:
    return {
        'seq': row[0], 'chunk': chunk, 'scene_or_key': row[3],
        'anchor_sha256': digest('\t'.join(row[:-1])),
        'target_sha256': digest(row[-1]), **public_target(row),
    }


def export_index(path: Path, rows, baseline) -> int:
    if rows.keys() != baseline.keys():
        raise ValueError('审校前后 ID 集合不一致')
    lines = []
    for seq, (chunk, row) in rows.items():
        prior_chunk, old = baseline[seq]
        if chunk != prior_chunk or row[:-1] != old[:-1]:
            raise ValueError(f'{seq} 的分块或保护列发生变化')
        if row[-1] != old[-1]:
            item = {**identity(chunk, row), 'before_target_sha256': digest(old[-1])}
            lines.append(json.dumps(item, ensure_ascii=False, separators=(',', ':')))
    if not lines:
        raise ValueError('没有译文改动')
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write('\n'.join(lines) + '\n')
    return len(lines)


def verify_index(path: Path, rows, baseline=None) -> int:
    if baseline is not None and rows.keys() != baseline.keys():
        raise ValueError('审校前后 ID 集合不一致')
    seen = set()
    for number, line in enumerate(path.read_text(encoding='utf-8').split('\n'), 1):
        if not line:
            continue
        item = json.loads(line)
        seq = item.get('seq')
        if seq in seen or seq not in rows:
            raise ValueError(f'第 {number} 行：无效或重复 ID {seq}')
        seen.add(seq)
        before = item.pop('before_target_sha256', '')
        chunk, row = rows[seq]
        if (not re.fullmatch(r'[0-9a-f]{64}', before) or before == item.get('target_sha256')
                or item != identity(chunk, row)):
            raise ValueError(f'{seq} 的锚点、译文或变更指纹不一致')
        if baseline is not None:
            prior_chunk, old = baseline[seq]
            if prior_chunk != chunk or old[:-1] != row[:-1]:
                raise ValueError(f'{seq} 的审校前定位信息不一致')
            if digest(old[-1]) != before:
                raise ValueError(f'{seq} 的审校前译文指纹不一致')
    if not seen:
        raise ValueError('校对索引为空')
    if baseline is not None and seen != {seq for seq in rows if rows[seq] != baseline[seq]}:
        raise ValueError('校对索引与完整差异范围不一致')
    return len(seen)


def fingerprint(path: Path, rows, count: int) -> dict:
    content = '\n'.join(chunk + '\t' + '\t'.join(row) for _, (chunk, row) in sorted(rows.items()))
    return {
        'schema': 1, 'changes': count, 'total_rows': len(rows),
        'index_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'all_rows_sha256': digest(content),
    }


def check_fingerprint(path: Path, pins: Path, rows, count: int) -> None:
    if json.loads(pins.read_text(encoding='utf-8')) != fingerprint(path, rows, count):
        raise ValueError('公开索引或完整译文快照与发布指纹不一致')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('export', 'verify'))
    parser.add_argument('--chunks', type=Path, default=ROOT / 'tl_work/chunks')
    parser.add_argument('--baseline', type=Path, help='审校前的本地分块快照')
    parser.add_argument('--index', type=Path, default=ROOT / 'review/scene-context-changes.jsonl')
    parser.add_argument('--fingerprint', type=Path, default=ROOT / 'review/scene-context-index.json')
    args = parser.parse_args()
    if args.action == 'export' and args.baseline is None:
        parser.error('export 需要 --baseline')
    rows = load_rows(args.chunks)
    baseline = load_rows(args.baseline) if args.baseline is not None else None
    if args.action == 'export':
        if args.fingerprint.exists():
            raise FileExistsError(args.fingerprint)
        count = export_index(args.index, rows, baseline)
        with args.fingerprint.open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(fingerprint(args.index, rows, count), stream, indent=2)
            stream.write('\n')
    else:
        count = verify_index(args.index, rows, baseline)
        check_fingerprint(args.index, args.fingerprint, rows, count)
    print(f'{args.action}: {count} changes / {len(rows)} rows')


if __name__ == '__main__':
    main()
