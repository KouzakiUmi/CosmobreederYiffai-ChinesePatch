"""Scan the candidate archives themselves for leftover minority spellings.

The snapshot-based selector cannot see everything the cleanup pass needs: one
Chinese sentence can sit in the jar **and** in patch.pak (the pak copy overrides
at runtime), and the snapshot only records one display line per unit. Earlier
batches fixed the jar copies and left the pak twins behind, which is exactly what
LEFTOVERS.md has been tracking.

So this scans the archives: every dialogue/VSN entry and every dictionary value in
both archives of the base candidate, looking for the minority spellings. Each hit
becomes one row in the order, with the archive encoded in `mode` (jar → sfw,
patch.pak → nsfw) so the ledger builder targets the right file.
"""
from pathlib import Path
from hashlib import sha256
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
import r9_targets  # noqa: E402

OUT = R9 / 'batch-17/orders'
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
TEXT_ENTRIES = ('datadf/1', 'datadm/1')

VARIANTS = {
    '干员': ('特工', 'agent 在库内作「特工」548 处、「干员」8 处；batch-15 当时只扫了「探员」，漏了这一个同义写法。'),
    '光电击器': ('光击枪', 'LIGHTTAZER 的统一写法：TAZER 作「电击枪」，LIGHT TAZER 作「光击枪」，不写「光电击枪」。'),
    '光刃电击器': ('光击枪', 'LIGHTTAZER 的统一写法；「光刃电击器」把 light 读成了「光刃」。'),
}


def lines(raw):
    body = raw.decode('utf8')
    out = re.findall(r'[^\r\n]*(?:\r\n|\r|\n|\Z)', body)
    if out and out[-1] == '':
        out.pop()
    return [l.rstrip('\r\n') for l in out]


def scan_text_entry(candidate, archive, mode, entry):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read(entry))
    hits = []
    for number, text in enumerate(lines(raw), 1):
        found = [w for w in VARIANTS if w in text]
        if found:
            hits.append({'row_id': 'P15:%s:%s:%d' % (archive, entry, number), 'line': number,
                         'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                         'archive_entry': entry, 'source': '', 'current': text,
                         '_hits': found})
    return hits


def scan_dictionary(candidate, archive, mode):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read('datav/1'))
    document = json.loads(raw.decode('utf8'))
    hits = []
    for key, value in document.items():
        if not isinstance(value, str):
            continue
        found = [w for w in VARIANTS if w in value]
        if found:
            hits.append({'row_id': 'P15:%s:datav/1:%s' % (archive, key), 'line': None,
                         'speaker': '', 'variant': mode, 'current_kind': 'dictionary_value',
                         'archive_entry': 'datav/1', 'source': '', 'current': value,
                         '_hits': found})
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
    base = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate43'
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
        'batch': 'batch-17',
        'batch_group': 'batch-17',
        'part': 1,
        'parts': 1,
        'title': '术语补漏：干员与 LIGHTTAZER',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': base,
        'corpus_manifest_sha256': '',
        'corpus_status': base,
        'current_zh_baseline': base,
        'scenes': [{
            'scene_id': 'SC15-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_hits'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-17.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-17.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_hits']) for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    from collections import Counter
    words = Counter()
    for s in scenes:
        for row in s['rows']:
            for w in row['_hits']:
                words[w] += 1
    print('base', base, '| scenes', len(scenes), '| hits', total)
    print('by word', dict(words))
    for s in scenes:
        print('  %-8s %-10s %-12s rows %d' % (s['mode'], s['root'], s['entry'], len(s['rows'])))


if __name__ == '__main__':
    main()
