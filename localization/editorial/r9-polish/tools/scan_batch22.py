"""batch-22: keep continuation lines from opening on punctuation.

The engine wraps greedily by pixel width and has no kinsoku rules, so a
continuation line can begin with `，` `。` `！` `？` `…`. `PixelLayout` treats U+2028
as an explicit line break, so inserting one moves the mark onto the previous
line.

U+2028 rather than LF on purpose: this toolchain splits rows on CR/LF only, so
a U+2028 keeps the row count — and therefore every row number in every ledger —
exactly as it was. An LF would renumber the whole entry and invalidate the
existing ledgers, which is what an earlier attempt did.

Only rows fixable **without changing the number of display rows** are included,
so pagination and animation timing stay identical. The text never changes:
removing the inserted U+2028 must give back the original row verbatim, and the
repair engine enforces exactly that for line rows.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
LOC = ROOT / 'localization'
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402
import render  # noqa: E402

OUT = R9 / 'batch-22/orders'
BASE = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate50'
CAND = ROOT / 'localization/builds' / BASE
BUDGET = 240
HAN = re.compile('[\u4e00-\u9fff]')
BAD_HEAD = '，。、；：？！）》」』”’·…—'
BREAK = '\u2028'
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
TEXT_ENTRIES = ('datadf/1', 'datadm/1')

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def player(text):
    body = text.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def wrap(text):
    rows = []
    for segment in text.split(BREAK):
        cur, used = '', 0
        for ch in segment:
            advance = GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
            if used + advance > BUDGET and cur:
                rows.append(cur)
                cur, used = '', 0
            cur += ch
            used += advance
        rows.append(cur)
    return rows


def attempt(text):
    """(new_text, marks_fixed) or None when the row count would change."""
    rows = wrap(text)
    if len(rows) < 2 or not any(row and row[0] in BAD_HEAD for row in rows[1:]):
        return None
    segments = list(rows)
    fixed = 0
    for i in range(1, len(segments)):
        if not segments[i] or segments[i][0] not in BAD_HEAD:
            continue
        mark = segments[i][0]
        if width(segments[i - 1] + mark) <= BUDGET:
            segments[i - 1] += mark
            segments[i] = segments[i][1:]
            fixed += 1
            continue
        if segments[i - 1]:
            moved = segments[i - 1][-1]
            segments[i - 1] = segments[i - 1][:-1]
            segments[i] = moved + segments[i]
            fixed += 1
    if not fixed or any(row and row[0] in BAD_HEAD for row in segments[1:]):
        return None
    new_text = BREAK.join(segments)
    if len(wrap(new_text)) != len(rows):
        return None
    if any(width(row) > BUDGET for row in segments):
        return None
    if new_text.replace(BREAK, '') != text:
        return None
    return new_text, fixed


def lines(raw):
    body = raw.decode('utf8')
    out = re.findall('[^\r\n]*(?:\r\n|\r|\n|\Z)', body)
    if out and out[-1] == '':
        out.pop()
    return [l.rstrip('\r\n') for l in out]


def main():
    scenes = []
    total = 0
    deferred = 0
    for archive, mode in ARCHIVES:
        for entry in TEXT_ENTRIES:
            with zipfile.ZipFile(CAND / archive) as z:
                raw = decrypt_file(z.read(entry))
            rows = []
            for number, text in enumerate(lines(raw), 1):
                if not player(text):
                    continue
                if not any(row and row[0] in BAD_HEAD for row in wrap(text)[1:]):
                    continue
                result = attempt(text)
                if result is None:
                    deferred += 1
                    continue
                new_text, fixed = result
                rows.append({'row_id': 'P22:%s:%s:%d' % (archive, entry, number), 'line': number,
                             'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                             'archive_entry': entry, 'source': '', 'current': text,
                             'target': new_text, '_marks': fixed})
            if rows:
                scenes.append({'root': entry.split('/')[0], 'logical_path': entry.replace('/1', '/all.ds'),
                               'mode': mode, 'entry': entry, 'rows': rows})
                total += len(rows)

    out = {
        'schema': 'r9-batch-order/v1',
        'batch': 'batch-22',
        'batch_group': 'batch-22',
        'part': 1,
        'parts': 1,
        'title': '排版：续行不以标点开头（插入 U+2028 显式断行，行号与文本均不变）',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': BASE,
        'corpus_manifest_sha256': '',
        'corpus_status': BASE,
        'current_zh_baseline': BASE,
        'scenes': [{
            'scene_id': 'SC22-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_marks'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-22.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-22.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_marks'], r['current'], r['target'])
                                                   for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'base': BASE, 'scenes': len(scenes), 'rows': total, 'deferred': deferred},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
