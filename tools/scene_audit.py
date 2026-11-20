"""Read-only bilingual scene view over the translation chunks and frozen scripts."""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import sys

from tl_tool import ARCHIVE_TAG, ROOT, _line_role, _read_tsv, escape_tsv


@dataclass(frozen=True)
class Variant:
    label: str
    # The first element is a script line number (0 for JSON fields).
    lines: tuple[tuple[int, str, str, str, str], ...]

    @property
    def signature(self):
        # Physical lines and row IDs differ between profiles. Keep commands,
        # source, speaker and translation in the equivalence test.
        return tuple(line[2:] for line in self.lines)


def ui_scene(key: str) -> str:
    """Associate fields read in the same record, not dictionary insertion order."""
    if key.startswith('/missionLog/'):
        return key.rsplit('/', 1)[0]
    if key.startswith('/patchDictionary/'):
        return ui_scene(key.removeprefix('/patchDictionary/'))
    if key.startswith('/shops/'):
        return key.rsplit('/', 1)[0]
    if key.startswith('ui.end.'):
        return key.rsplit('.', 1)[0]
    if key.startswith('ui.backers.'):
        return 'ui.backers'
    return re.sub(r'\.(?:name|popup|title|hint|desc(?:\.(?:Front|Back))?)$', '', key)


def inventory(tl_dir: Path) -> dict[tuple[str, str], list[Variant]]:
    groups = defaultdict(list)
    seen = set()
    for kind, cols in (('dialogue', 8), ('vsn', 8), ('ui', 6)):
        for file in sorted((tl_dir / 'chunks' / kind).glob('*.tsv')):
            entries = defaultdict(dict)
            ui = defaultdict(list)
            for row in _read_tsv(file, cols):
                seq, archive, entry, key = row[:4]
                if seq in seen:
                    raise ValueError(f'duplicate seq: {seq}')
                seen.add(seq)
                if kind == 'ui':
                    ui[ui_scene(key)].append((0, seq, key, row[-2], row[-1]))
                else:
                    pos = int(row[4])
                    if pos in entries[archive, entry]:
                        raise ValueError(f'duplicate position: {archive}:{entry}:{pos}')
                    entries[archive, entry][pos] = row
            for name, fields in ui.items():
                groups[kind, name].append(Variant(file.stem, tuple(sorted(fields, key=lambda row: row[2]))))
            for (archive, entry), by_pos in entries.items():
                tag = ARCHIVE_TAG[archive]
                script = (tl_dir / 'template' / tag / entry).read_text(encoding='utf-8').split('\n')
                ranges = []
                if kind == 'dialogue':
                    headers = [(i, line.strip()[1:-1]) for i, line in enumerate(script, 1)
                               if line.strip().startswith('<') and line.strip().endswith('>')
                               and len(line.strip()) > 2]
                    ranges = [(name, i, j) for (i, name), (j, _) in zip(headers, headers[1:] + [(len(script)+1, '')])]
                else:
                    names = {row[3] for row in by_pos.values()}
                    if len(names) != 1:
                        raise ValueError(f'ambiguous script label: {archive}:{entry}: {names}')
                    ranges = [(names.pop(), 1, len(script)+1)]
                occurrences = defaultdict(int)
                for name, start, stop in ranges:
                    occurrences[name] += 1
                    label = f'{file.stem}:{entry}:{start}'
                    if occurrences[name] > 1:
                        label += f' (occurrence {occurrences[name]})'
                    display = []
                    for pos in range(start, stop):
                        text = script[pos-1]
                        row = by_pos.pop(pos, None)
                        role = _line_role(text, 'ds' if kind == 'dialogue' else 'vsn')
                        if row:
                            seq, _, _, row_name, _, prefix, source, target = row
                            if row_name != name or role is None or tuple(map(escape_tsv, role)) != (prefix, source):
                                raise ValueError(f'{seq}: location, speaker or source differs from frozen script')
                            display.append((pos, seq, prefix, source, target))
                        elif text.strip() and (kind == 'vsn' or pos > start):
                            display.append((pos, '', text, '', ''))
                    if any(line[1] for line in display) or any('include {' in line[2] for line in display):
                        groups[kind, name].append(Variant(label, tuple(display)))
                if by_pos:
                    raise ValueError(f'{archive}:{entry}: unmapped rows: {sorted(by_pos)}')
    return groups


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('list', 'show'))
    parser.add_argument('pattern', nargs='?', default='.', help='case-insensitive regex on kind:scene')
    parser.add_argument('--tl-dir', type=Path, default=ROOT / 'tl_work')
    args = parser.parse_args()
    rx = re.compile(args.pattern, re.I)
    rows = groups = 0
    for (kind, name), variants in inventory(args.tl_dir).items():
        if not rx.search(f'{kind}:{name}'):
            continue
        aliases = defaultdict(list)
        for v in variants:
            aliases[v.signature].append(v)
        count = sum(bool(line[1]) for v in variants for line in v.lines)
        rows += count
        groups += 1
        print(f'## {kind}:{name} · {count} rows · {len(variants)} variants / {len(aliases)} distinct')
        if args.mode != 'show':
            continue
        for same in aliases.values():
            print('[' + ' = '.join(v.label for v in same) + ']')
            for lines in zip(*(v.lines for v in same)):
                pos, seq, prefix, source, target = lines[0]
                if seq:
                    ids = '/'.join(line[1] for line in lines)
                    print(f'{pos or "-"} {ids} {prefix} EN: {source}  ⇒  {target or "∅"}')
                else:
                    print(f'{pos} │ {prefix}')
    print(f'-- {groups} groups, {rows} TSV rows --')
    if not groups:
        sys.exit(1)


if __name__ == '__main__':
    main()
