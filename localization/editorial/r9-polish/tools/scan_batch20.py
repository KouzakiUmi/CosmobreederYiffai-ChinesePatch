"""Unify the Fenfen spelling to the glossary term 「芬芬」.

`localization/review/glossary.csv` carries `Fenfen,种族名,芬芬,,proposed`. batch-16
acted on it for three all-caps `FENFEN` hits; the camel-case `Fenfen` that the
player actually sees was never touched.

Two rules:

* `Fenfen` -> `芬芬`.
* A space that directly abuts the token goes with it. Nine occurrences sit in
  `关于 Fenfen 服装` / `一位代表重要力量的 Fenfen 核心成员` style spacing, which is
  the old Chinese-Latin gap; once the token is Chinese the gap is just a stray
  space inside a Chinese sentence.

Script lines are skipped for the same reason as batch-19: `Fenfen` doubles as an
identifier (`include { Fenfen_Shared.Hello }`, `<Area0_Fenfen.Hello>`).
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
import r9_targets as targets  # noqa: E402

OUT = R9 / 'batch-20/orders'
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
TEXT_ENTRIES = ('datadf/1', 'datadm/1')
HAN = re.compile('[\u4e00-\u9fff]')
TOKEN = 'Fenfen'
# token with at most one space on either side, so the space can be dropped with it
WITH_GAP = re.compile(' ?Fenfen ?')


def lines(raw):
    body = raw.decode('utf8')
    out = re.findall('[^\r\n]*(?:\r\n|\r|\n|\Z)', body)
    if out and out[-1] == '':
        out.pop()
    return [l.rstrip('\r\n') for l in out]


def player_visible(text):
    body = text.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def rewrite(text):
    """(new_text, count) — collapse the token and any single space hugging it."""
    count = [0]

    def replace(match):
        count[0] += 1
        return '芬芬'

    out = WITH_GAP.sub(replace, text)
    return out, count[0]


def scan_text_entry(candidate, archive, mode, entry):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read(entry))
    hits = []
    for number, text in enumerate(lines(raw), 1):
        if not player_visible(text) or TOKEN not in text:
            continue
        new_text, count = rewrite(text)
        if count:
            hits.append({'row_id': 'P20:%s:%s:%d' % (archive, entry, number), 'line': number,
                         'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                         'archive_entry': entry, 'source': '', 'current': text,
                         'target': new_text, '_hits': ['Fenfen'] * count})
    return hits


def scan_dictionary(candidate, archive, mode):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read('datav/1'))
    document = json.loads(raw.decode('utf8'))
    hits = []
    for key, value in document.items():
        if not isinstance(value, str) or not player_visible(value) or TOKEN not in value:
            continue
        # multi-line card values are fine now: the shared text rule expands the
        # `␊` sentinel that make_decisions writes, so the gate compares equal
        new_value, count = rewrite(value)
        if count:
            hits.append({'row_id': 'P20:%s:datav/1:%s' % (archive, key), 'line': None,
                         'pointer': targets.pointer_of(key),
                         'speaker': '', 'variant': mode, 'current_kind': 'dictionary_value',
                         'archive_entry': 'datav/1', 'source': '', 'current': value,
                         'target': new_value, '_hits': ['Fenfen'] * count})
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
    base = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate48'
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
        'batch': 'batch-20',
        'batch_group': 'batch-20',
        'part': 1,
        'parts': 1,
        'title': '专名统一：Fenfen → 芬芬（glossary 的提议译法，batch-16 只做了全大写）',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': base,
        'corpus_manifest_sha256': '',
        'corpus_status': base,
        'current_zh_baseline': base,
        'scenes': [{
            'scene_id': 'SC20-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_hits'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-20.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-20.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_hits'], r['current'], r['target'])
                                                   for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    by_mode = {}
    for scene in scenes:
        by_mode[scene['mode']] = by_mode.get(scene['mode'], 0) + len(scene['rows'])
    print(json.dumps({'base': base, 'scenes': len(scenes), 'rows': total, 'by_mode': by_mode},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
