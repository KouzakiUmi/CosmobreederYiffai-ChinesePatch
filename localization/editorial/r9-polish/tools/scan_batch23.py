"""batch-23: move the break so a Chinese word is not split across rows.

The engine wraps greedily by pixel width and knows nothing about word
boundaries, so a word can end up with its first character on one row and the
rest on the next (`矮` / `人`). `PixelLayout` treats U+2028 as a hard break, so
the fix is to place one where the break lands on a word boundary.

Three conditions gate every row, and all three are checked here and again by
the repair engine:

* the drawn row count must not change (pagination and animation timing);
* removing the inserted U+2028 must give back the original row verbatim;
* the repair must strictly reduce the number of split pairs — never trade one
  split for another.

Row counts are measured on the **display body**. The speaker prefix (`  * `,
`  Tomcat: `) is not laid out, so measuring the raw physical line overstates
the width and hides rows that would actually grow a line.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
LOC = ROOT / 'localization'
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

OUT = R9 / 'batch-23/orders'
BASE = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate51'
CAND = ROOT / 'localization/builds' / BASE
BUDGET = 240
BREAK = '\u2028'
MIN_PAIR = 8
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^(\\s*\\*\\s?|\\s*[^<>{}#*\\s][^:]{0,40}:\\s?)(.*)$')
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
TEXT_ENTRIES = ('datadf/1', 'datadm/1')

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def body_of(line):
    match = ACTOR.match(line)
    return match.group(2) if match else line


def player(body):
    stripped = body.strip()
    if not stripped or stripped[0] in '{}#<':
        return False
    if stripped.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def wrap(body):
    rows = []
    for segment in body.split(BREAK):
        cur, used = '', 0
        for ch in segment:
            advance = GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
            if used + advance > BUDGET and cur:
                rows.append(cur)
                cur, used = '', 0
            cur += ch
            used += advance
        if cur:
            rows.append(cur)
    return rows


def breaks_of(rows):
    return [(i, rows[i][-1] + rows[i + 1][0]) for i in range(len(rows) - 1) if rows[i] and rows[i + 1]]


def repair(body, rows, splits, bigrams):
    """Pick the break move that removes the most splits and adds the fewest.

    The first candidate that merely lowers the count is not good enough: it can
    land inside a different word (`足` / `够`). So every candidate is scored,
    preferring more splits removed and then fewer *new* split pairs introduced.
    """
    flat = body.replace(BREAK, '')
    original_breaks = body.count(BREAK)
    original_pairs = {pair for _, pair in splits}
    best = None
    for idx, _pair in splits:
        head = ''.join(rows[:idx + 1])
        tail = ''.join(rows[idx + 1:])
        for back in range(1, min(len(head), 14) + 1):
            moved = head[-back:]
            candidate = BREAK.join(row for row in list(rows[:idx]) + [head[:-back], moved + tail] if row)
            if candidate.replace(BREAK, '') != flat:
                continue
            if candidate.count(BREAK) < original_breaks:
                continue
            drawn = wrap(candidate)
            if len(drawn) != len(rows):
                continue
            after = [p for _, p in breaks_of(drawn) if bigrams.get(p, 0) >= MIN_PAIR]
            introduced = [p for p in after if p not in original_pairs]
            removed = len(splits) - len(after)
            if removed <= 0:
                continue
            score = (removed, -len(introduced))
            if best is None or score > best[0]:
                best = (score, candidate, removed, introduced)
    if best is None:
        return None
    return best[1], best[2]


def main():
    bigrams = Counter()
    for archive, _mode in ARCHIVES:
        for entry in TEXT_ENTRIES:
            for line in t.resource_state(CAND, archive, entry, 'line')[0]['lines']:
                body = body_of(line)
                if not HAN.search(body):
                    continue
                han = [c for c in body if '\u4e00' <= c <= '\u9fff']
                for a, b in zip(han, han[1:]):
                    bigrams[a + b] += 1

    scenes = []
    total = 0
    deferred = 0
    fixed_pairs = Counter()
    for archive, mode in ARCHIVES:
        for entry in TEXT_ENTRIES:
            rows = []
            for number, line in enumerate(t.resource_state(CAND, archive, entry, 'line')[0]['lines'], 1):
                body = body_of(line)
                if not player(body):
                    continue
                drawn = wrap(body)
                splits = [(i, p) for i, p in breaks_of(drawn) if bigrams.get(p, 0) >= MIN_PAIR]
                if not splits:
                    continue
                result = repair(body, drawn, splits, bigrams)
                if result is None:
                    deferred += 1
                    continue
                new_body, fixed = result
                for _, pair in splits:
                    fixed_pairs[pair] += 1
                prefix = line[:len(line) - len(body)]
                rows.append({'row_id': 'P23:%s:%s:%d' % (archive, entry, number), 'line': number,
                             'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                             'archive_entry': entry, 'source': '', 'current': line,
                             'target': prefix + new_body, '_fixed': fixed})
            if rows:
                scenes.append({'root': entry.split('/')[0], 'logical_path': entry.replace('/1', '/all.ds'),
                               'mode': mode, 'entry': entry, 'rows': rows})
                total += len(rows)

    out = {
        'schema': 'r9-batch-order/v1',
        'batch': 'batch-23',
        'batch_group': 'batch-23',
        'part': 1,
        'parts': 1,
        'title': '排版：折行不切词（插入 U+2028 把断点移到词边界，显示行数与文本均不变）',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': BASE,
        'corpus_manifest_sha256': '',
        'corpus_status': BASE,
        'current_zh_baseline': BASE,
        'scenes': [{
            'scene_id': 'SC23-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_fixed'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-23.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-23.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_fixed'], r['current'], r['target'])
                                                   for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'base': BASE, 'scenes': len(scenes), 'rows': total, 'deferred': deferred,
                      'top_pairs': fixed_pairs.most_common(5)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
