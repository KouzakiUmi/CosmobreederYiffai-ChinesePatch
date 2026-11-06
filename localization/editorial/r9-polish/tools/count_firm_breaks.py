"""Count firm (>=30) bigram breaks in a SceneRender corpus output.

The metric is the one scene-render-review.md reproduced against the recorded
batch-25 numbers: a break counts when the two characters either side of an
engine row boundary form a pair that occurs >=30 times in the corpus display
bodies (frequency proxy, not segmentation). Frequency table is built from the
`A` rows of render-corpus.tsv (the candidate54 wording corpus).

Usage: count_firm_breaks.py <corpus.tsv (5-col, has A rows)> <render-out.json>
"""
import collections
import json
import re
import sys

HAN = re.compile('[\u4e00-\u9fff]')


def firm_table(corpus_tsv):
    bodies = []
    for ln in open(corpus_tsv, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln:
            continue
        p = ln.split('\t')
        if p[0] == 'A':
            bodies.append(p[4])
    freq = collections.Counter()
    for b in bodies:
        s = ''.join(ch for ch in b.replace('\u2028', '') if HAN.match(ch))
        for i in range(len(s) - 1):
            freq[s[i:i + 2]] += 1
    return {bg for bg, c in freq.items() if c >= 30}


def main():
    firm = firm_table(sys.argv[1])
    out = json.load(open(sys.argv[2], encoding='utf-8'))
    errors = 0
    bad = 0
    cases = 0
    for k, v in out.items():
        if not v.get('ok'):
            errors += 1
            continue
        cases += 1
        lines = [l.strip() for l in v['pages'][0]['lines'] if l.strip()]
        for i in range(len(lines) - 1):
            if lines[i][-1] + lines[i + 1][0] in firm:
                bad += 1
    print(json.dumps({'cases': cases, 'engine_errors': errors,
                      'firm_bigrams': bad}, ensure_ascii=False))


if __name__ == '__main__':
    main()
