"""batch-24: repair the worst word splits, pagination untouched.

The user's rule for this batch: **do not move pagination** unless a row is
especially bad, and even then only when the page count does not grow and the
row is not at a staging hand-off (`cut`, `fadecut`, `snap`, `music`, `rewind!`
— where the background or actor changes).

So three conditions, all enforced here:

1. the drawn row count must stay exactly the same;
2. the row must be especially bad — a firmly established word of 3+ characters
   cut in two (the loose two-character test flags too much, because `的`
   combines with everything);
3. the row must not sit immediately before a staging command with no other
   dialogue in between, so nothing that changes on screen shifts its timing.

The text never changes: removing the inserted U+2028 must give back the
original row verbatim.
"""
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

OUT = R9 / 'batch-24/orders'
BASE = sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate52'
CAND = ROOT / 'localization/builds' / BASE
BUDGET = 240
BREAK = '\u2028'
MIN_PAIR = 8
SOLID_PAIR = 30
LONG_WORD = 3
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^(\\s*\\*\\s?|\\s*[^<>{}#*\\s][^:]{0,40}:\\s?)(.*)$')
STAGING = re.compile('^(?:cut|fadecut|snap|music|rewind|wait|queue|fade)\\b', re.I)
TEXT_LINE = re.compile('^\\s*(?:text|lang\\([^)]*\\)|auto\\([^)]*\\))\\s*:\\s?')

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def body_of(line):
    match = ACTOR.match(line)
    return match.group(2) if match else line


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


def splits_of(body, bigrams, floor):
    drawn = wrap(body)
    return [(i, drawn[i][-1] + drawn[i + 1][0]) for i in range(len(drawn) - 1)
            if drawn[i] and drawn[i + 1]
            and bigrams.get(drawn[i][-1] + drawn[i + 1][0], 0) >= floor]


def long_word_at(rows, idx, bigrams):
    left = ''.join(rows[:idx + 1])
    right = ''.join(rows[idx + 1:])
    best = 1
    for take_left in range(1, 4):
        for take_right in range(1, 4):
            if take_left > len(left) or take_right > len(right):
                continue
            candidate = left[-take_left:] + right[:take_right]
            if len(candidate) < 2:
                continue
            if all(bigrams.get(candidate[i:i + 2], 0) >= SOLID_PAIR for i in range(len(candidate) - 1)):
                best = max(best, len(candidate))
    return best

# Characters that do not form a word on their own: breaking before or after
# them reads as a normal line break, not as a cut word. `的` in particular
# combines with almost everything, which is why a frequency floor cannot
# separate a real word from a function-word join.
FUNCTION_CHARS = set('的了着过是在和与就都也还而且但如果因为所以把被给让从对向')
CONTENT_PAIR = 30


def cuts_a_content_word(candidate, drawn):
    """Does the candidate separate two characters that form a real word?

    A break before/after a function character is acceptable. Breaking between
    two content characters is only acceptable when that pair was already split
    in the original layout.
    """
    flat = candidate.replace(BREAK, '')
    redrawn = wrap(candidate)
    for i in range(len(redrawn) - 1):
        left, right = redrawn[i], redrawn[i + 1]
        if not left or not right:
            continue
        pair = left[-1] + right[0]
        if pair[0] in FUNCTION_CHARS or pair[1] in FUNCTION_CHARS:
            continue
        if any(row[-1] + next_row[0] == pair
               for row, next_row in zip(drawn, drawn[1:]) if row and next_row):
            continue
        return True
    return False


def repair(body, bigrams):
    """Insert a break that kills the split without changing the row count."""
    drawn = wrap(body)
    splits = splits_of(body, bigrams, SOLID_PAIR)
    if not splits:
        return None
    flat = body.replace(BREAK, '')
    original_breaks = body.count(BREAK)
    for idx, _pair in splits:
        head = ''.join(drawn[:idx + 1])
        tail = ''.join(drawn[idx + 1:])
        for back in range(1, min(len(head), 20) + 1):
            moved = head[-back:]
            pieces = list(drawn[:idx]) + [head[:-back], moved + tail]
            candidate = BREAK.join(piece for piece in pieces if piece)
            if candidate.replace(BREAK, '') != flat:
                continue
            if candidate.count(BREAK) < original_breaks:
                continue
            redrawn = wrap(candidate)
            if len(redrawn) != len(drawn):
                continue
            if splits_of(candidate, bigrams, SOLID_PAIR):
                continue
            # A frequency floor cannot tell a real word from a function-word
            # join: `印记` may fall below it while `么的` clears it, and then a
            # "repair" cuts a real word to avoid breaking before `的`. So also
            # reject any candidate that newly separates an adjacent character
            # pair, whatever its frequency.
            if cuts_a_content_word(candidate, drawn):
                continue
            return candidate
    return None


def main():
    bigrams = Counter()
    scripts = {}
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            scripts[(archive, entry)] = t.resource_state(CAND, archive, entry, 'line')[0]['lines']
        with zipfile.ZipFile(CAND / archive) as z:
            names = sorted(n for n in z.namelist() if n.startswith('vsn/') and n != 'vsn/0')
        for entry in names:
            try:
                scripts[(archive, entry)] = t.resource_state(CAND, archive, entry, 'line')[0]['lines']
            except Exception:
                continue
    for lines in scripts.values():
        for line in lines:
            body = body_of(line)
            if not HAN.search(body):
                continue
            han = [c for c in body if '\u4e00' <= c <= '\u9fff']
            for a, b in zip(han, han[1:]):
                bigrams[a + b] += 1

    scenes = []
    total = 0
    skipped_handoff = 0
    skipped_mild = 0
    skipped_rows = 0
    for (archive, entry), lines in sorted(scripts.items()):
        # `vsn` rows also feed the subtitle container, whose parser rejects
        # U+2028 outright (`SubtitleLayoutTest` fails with a parse error). Only
        # the dialogue containers take an explicit break.
        if entry.startswith('vsn/'):
            continue
        mode = 'sfw' if archive == 'cosmobreeder-multi.jar' else 'nsfw'
        rows = []
        for number, line in enumerate(lines, 1):
            body = body_of(line)
            if not HAN.search(body):
                continue
            loose = splits_of(body, bigrams, MIN_PAIR)
            if not loose:
                continue
            drawn = wrap(body)
            worst = max(long_word_at(drawn, i, bigrams) for i, _ in loose)
            if worst < LONG_WORD:
                skipped_mild += 1
                continue
            handoff = False
            for nxt in lines[number:]:
                stripped = nxt.strip()
                if not stripped:
                    continue
                if STAGING.match(stripped):
                    handoff = True
                    break
                if TEXT_LINE.match(nxt) or ACTOR.match(nxt):
                    break
            if handoff:
                skipped_handoff += 1
                continue
            new_body = repair(body, bigrams)
            if new_body is None:
                skipped_rows += 1
                continue
            prefix = line[:len(line) - len(body)]
            rows.append({'row_id': 'P24:%s:%s:%d' % (archive, entry, number), 'line': number,
                         'speaker': '', 'variant': mode, 'current_kind': 'physical_line',
                         'archive_entry': entry, 'source': '', 'current': line,
                         'target': prefix + new_body, '_worst': worst})
        if rows:
            scenes.append({'root': entry.split('/')[0], 'logical_path': entry.replace('/1', '/all.ds'),
                           'mode': mode, 'entry': entry, 'rows': rows})
            total += len(rows)

    out = {
        'schema': 'r9-batch-order/v1',
        'batch': 'batch-24',
        'batch_group': 'batch-24',
        'part': 1,
        'parts': 1,
        'title': '排版：修最严重的折行切词（分页不动，跳过演出交接点）',
        'roots': sorted({s['root'] for s in scenes}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': BASE,
        'corpus_manifest_sha256': '',
        'corpus_status': BASE,
        'current_zh_baseline': BASE,
        'scenes': [{
            'scene_id': 'SC24-%s-%s' % (s['mode'], s['entry'].replace('/', '_')),
            'mode': s['mode'],
            'logical_path': s['logical_path'],
            'root': s['root'],
            'header_line': None,
            'controls': [],
            'rows': [{k: v for k, v in row.items() if k != '_worst'} for row in s['rows']],
        } for s in scenes],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-24.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (OUT / 'batch-24.hits.json').write_text(
        json.dumps({out['scenes'][i]['scene_id']: [(r['row_id'], r['_worst'], r['current'], r['target'])
                                                   for r in s['rows']]
                    for i, s in enumerate(scenes)}, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'base': BASE, 'scenes': len(scenes), 'rows': total,
                      'skipped_handoff': skipped_handoff, 'skipped_not_bad_enough': skipped_mild,
                      'skipped_no_clean_move': skipped_rows}, ensure_ascii=False))


if __name__ == '__main__':
    main()
