"""Rewrite ASCII quotes that wrap Chinese text into full-width Chinese quotes.

`story12.fnt` keeps the ASCII face at 8px (`"` is 7x5, `'` is 6x5) while the Han
glyphs are 12px. A straight quote dropped inside a Chinese sentence therefore
draws one size smaller and off the baseline — it reads as a misplaced mark.

Quotes wrapping pure Latin are deliberately left alone: there the 8px glyphs are
the right size for the Latin run they enclose.

Same shape as `scan_residual_archive.py`: scan both archives of the base
candidate, turn each rewrite into one order row.
"""
from pathlib import Path
import json
import re
import sys
import zipfile

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
LOC = ROOT / 'localization'
sys.path.insert(0, str(R9 / 'tools'))
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

OUT = R9 / 'batch-21/orders'
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
TEXT_ENTRIES = ('datadf/1', 'datadm/1')
HAN = re.compile('[\u4e00-\u9fff]')
DQ = re.compile('"([^"\n]*)"')
SQ = re.compile("'([^'\n]*)'")


def lines(raw):
    body = raw.decode('utf8')
    out = re.findall('[^\r\n]*(?:\r\n|\r|\n|\Z)', body)
    if out and out[-1] == '':
        out.pop()
    return [l.rstrip('\r\n') for l in out]


def player_visible(text):
    """Script labels, includes and conditions are never drawn."""
    body = text.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def rewrite(text):
    """(new_text, count). Only quote pairs whose payload contains Han are touched."""
    count = [0]

    def double(match):
        if not HAN.search(match.group(1)):
            return match.group(0)
        count[0] += 1
        return '\u201c' + match.group(1) + '\u201d'

    def single(match):
        if not HAN.search(match.group(1)):
            return match.group(0)
        count[0] += 1
        return '\u2018' + match.group(1) + '\u2019'

    out = DQ.sub(double, text)
    out = SQ.sub(single, out)
    return out, count[0]


def scan_text_entry(candidate, archive, mode, entry):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read(entry))
    hits = []
    for number, text in enumerate(lines(raw), 1):
        if not player_visible(text):
            continue
        new_text, count = rewrite(text)
        if count:
            hits.append({'row_id': 'P21:%s:%s:%d' % (archive, entry, number), 'line': number,
                         'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                         'archive_entry': entry, 'source': '', 'current': text,
                         'target': new_text, '_hits': ['quote'] * count})
    return hits


def scan_dictionary(candidate, archive, mode):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read('datav/1'))
    document = json.loads(raw.decode('utf8'))
    hits = []
    for key, value in document.items():
        if not isinstance(value, str) or not player_visible(value):
            continue
        # multi-line values are fine now: the shared text rule expands the `␊`
        # sentinel, so a card value spanning several lines round-trips through TSV
        new_value, count = rewrite(value)
        if count:
            hits.append({'row_id': 'P21:%s:datav/1:%s' % (archive, key), 'line': None,
                         'speaker': '', 'variant': mode, 'current_kind': 'dictionary_value',
                         'archive_entry': 'datav/1', 'source': '', 'current': value,
                         'target': new_value, '_hits': ['quote'] * count})
    return hits


def scan_vsn(candidate, archive, mode):
    with zipfile.ZipFile(candidate / archive) as z:
        entries = sorted(n for n in z.namelist() if n.startswith('vsn/') and n != 'vsn/0')
    hits = []
    for entry in entries:
        try:
            hits.extend(scan_text_entry(candidate, archive, mode, entry))
        except Exception:
            continue
    return hits


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate47'
    candidate = ROOT / 'localization/builds' / base
    scenes = []
    total = 0
    for archive, mode in ARCHIVES:
        for entry in TEXT_ENTRIES:
            hits = scan_text_entry(candidate, archive, mode, entry)
            if hits:
                scenes.append({'root': entry.split('/')[0], 'logical_path': entry.replace('/1', '/all.ds'),
                               'mode': mode, 'entry': entry, 'rows': hits})
                total += len(hits)
        vsn_hits = {}
        for hit in scan_vsn(candidate, archive, mode):
            vsn_hits.setdefault(hit['archive_entry'], []).append(hit)
        for entry, hits in sorted(vsn_hits.items()):
            scenes.append({'root': 'vsn', 'logical_path': 'vsn/%s/script.vsn' % entry, 'mode': mode,
                           'entry': entry, 'rows': hits})
            total += len(hits)
        dict_hits = scan_dictionary(candidate, archive, mode)
        if dict_hits:
            scenes.append({'root': 'datav', 'logical_path': 'datav/dictionary.json', 'mode': mode,
                           'entry': 'datav/1', 'rows': dict_hits})
            total += len(dict_hits)

    out = {
        'schema': 'r9-batch-order/v1',
        'batch': 'batch-21',
        'batch_group': 'batch-21',
        'part': 1,
        'parts': 1,
        'title': '中文引号（续）：多行角色卡值里的直引号（多行值通道已就绪）',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': base,
        'corpus_manifest_sha256': '',
        'corpus_status': base,
        'current_zh_baseline': base,
        'scenes': [{
            'scene_id': 'SC21-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_hits'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-21.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-21.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_hits'], r['current'], r['target'])
                                                   for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print('base', base, '| scenes', len(scenes), '| rows', total)
    for s in scenes:
        print('  %-8s %-10s %-12s rows %d' % (s['mode'], s['root'], s['entry'], len(s['rows'])))


if __name__ == '__main__':
    main()
