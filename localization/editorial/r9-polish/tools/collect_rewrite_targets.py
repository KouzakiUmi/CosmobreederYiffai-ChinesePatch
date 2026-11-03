"""Enumerate the rows that still cut a real word, with the English original.

User's decision: rewriting the Chinese is allowed (polish is part of translation),
including changing the page count, as long as the meaning survives.

So this collects every row where a firmly established word (a 2-char pair seen
>= 30 times in the corpus) is split across two drawn rows, and pairs it with the
English source line at the same physical index. That is the input for rewriting.

Output is a review file, not a ledger: `batch-25/orders/rewrite-targets.json`.
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
sys.path.insert(0, str(ROOT / 'localization/tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402
from codec import decrypt_file  # noqa: E402

CAND = ROOT / 'localization/builds/r9-polish-candidate52'
SOURCE = ROOT / 'backup'
OUT = R9 / 'batch-25/orders'
BUDGET = 240
BREAK = '\u2028'
SOLID_PAIR = 30
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^(\\s*\\*\\s?|\\s*[^<>{}#*\\s][^:]{0,40}:\\s?)(.*)$')
ARCHIVES = (('cosmobreeder-multi.jar', 'sfw'), ('patch.pak', 'nsfw'))
ENTRIES = ('datadf/1', 'datadm/1')

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


def main():
    # corpus for the solid-pair test
    bigrams = Counter()
    chinese = {}
    for archive, mode in ARCHIVES:
        for entry in ENTRIES:
            chinese[(archive, entry)] = t.resource_state(CAND, archive, entry, 'line')[0]['lines']
            for line in chinese[(archive, entry)]:
                body = body_of(line)
                if not HAN.search(body):
                    continue
                han = [c for c in body if '\u4e00' <= c <= '\u9fff']
                for a, b in zip(han, han[1:]):
                    bigrams[a + b] += 1

    # the English originals, same physical indices
    english = {}
    for archive, _mode in ARCHIVES:
        with zipfile.ZipFile(SOURCE / archive) as z:
            for entry in ENTRIES:
                try:
                    raw = decrypt_file(z.read(entry))
                except Exception:
                    continue
                lines = re.findall(r'[^\r\n]*(?:\r\n|\r|\n|\Z)', raw.decode('utf8'))
                if lines and lines[-1] == '':
                    lines.pop()
                english[(archive, entry)] = [l.rstrip('\r\n') for l in lines]

    rows = []
    for (archive, entry), lines in sorted(chinese.items()):
        mode = 'sfw' if archive == 'cosmobreeder-multi.jar' else 'nsfw'
        for number, line in enumerate(lines, 1):
            body = body_of(line)
            if not HAN.search(body):
                continue
            drawn = wrap(body)
            splits = []
            for i in range(len(drawn) - 1):
                if drawn[i] and drawn[i + 1]:
                    pair = drawn[i][-1] + drawn[i + 1][0]
                    if bigrams.get(pair, 0) >= SOLID_PAIR:
                        splits.append(pair)
            if not splits:
                continue
            en = english.get((archive, entry), [])
            rows.append({
                'archive': archive, 'entry': entry, 'line': number, 'mode': mode,
                'current': line, 'body': body, 'drawn': drawn,
                'widths': [width(r) for r in drawn],
                'split_pairs': splits,
                'english': en[number - 1].strip() if number - 1 < len(en) else '',
            })

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'rewrite-targets.json').write_text(
        json.dumps({'candidate': CAND.name, 'solid_pair': SOLID_PAIR,
                    'budget_px': BUDGET, 'rows': rows},
                   ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'rows': len(rows),
                      'by_container': dict(Counter('%s/%s' % (r['archive'][:3], r['entry'])
                                                   for r in rows)),
                      'with_english': sum(1 for r in rows if r['english'])},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
