"""Turn semantic-QA findings into a revision batch.

  python -B tools/apply-findings.py --batch batch_195 --findings work/qa/findings-a.jsonl work/qa/findings-b.jsonl

Each finding supplies id + suggested translation. Before writing, every suggestion is
re-validated with the same rules packaging uses (glyph coverage, markers, whitespace,
control chars). Suggestions that fail validation are NOT applied; they are listed for
manual handling. Provenance of the original batch is preserved via keep_provenance.
"""
import argparse
import json
import re
import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projectlib import PROJECT, digest, glyph_metrics, load_units, validate_translation  # noqa: E402


INSTRUCTION = re.compile(r'(改为|建议改为|建议：|拟改为|应改为|统一为|或保留|本条改为)')

def sanitize(sug):
    """Reviewers sometimes put instructions instead of a plain translation. Extract the
    quoted translation when possible; otherwise refuse the suggestion."""
    if not INSTRUCTION.search(sug):
        return sug
    for pat in (r'本条改为「(.+)」', r'改为「(.+?)」'):
        m = re.search(pat, sug)
        if m:
            return m.group(1).strip()
    return None

QA = PROJECT / 'work/qa'
WORK = PROJECT / 'work/batches'


def read_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--batch', required=True)
    ap.add_argument('--findings', nargs='+', required=True)
    ap.add_argument('--include-b', action='store_true', help='also apply B (terminology) findings')
    ap.add_argument('--include-c', action='store_true', help='also apply C (style) findings')
    a = ap.parse_args()

    records = {r['id']: r for r in (json.loads(l) for l in
               (PROJECT / 'translations/zh-CN.jsonl').read_text(encoding='utf-8').splitlines() if l.strip())}
    units = {u['id']: u for u in load_units()}
    metrics = glyph_metrics()

    applied, rejected = [], []
    for f in a.findings:
        for fnd in read_jsonl(f):
            sev = fnd.get('severity')
            if sev == 'B' and not a.include_b:
                continue
            if sev == 'C' and not a.include_c:
                continue
            if sev == 'ESCALATE':
                rejected.append({'id': uid, 'why': 'escalated by reviewer'})
                continue
            uid = fnd['id']
            sug = (fnd.get('suggested') or '').strip()
            if uid not in records or uid not in units:
                rejected.append({'id': uid, 'why': 'unknown id'})
                continue
            if not sug:
                rejected.append({'id': uid, 'why': 'no suggestion'})
                continue
            sug2 = sanitize(sug)
            if sug2 is None:
                rejected.append({'id': uid, 'why': 'suggestion is an instruction, not a translation'})
                continue
            sug = sug2
            issues = [i for i in validate_translation(units[uid], sug, metrics) if i[0] == 'error']
            if issues:
                rejected.append({'id': uid, 'why': 'suggestion fails validation', 'issues': issues})
                continue
            if sug == (records[uid].get('draft') or ''):
                continue
            applied.append({'id': uid, 'translation': sug,
                            'notes': 'semantic QA fix: ' + (fnd.get('issue') or '')[:120],
                            'pack': fnd.get('pack'),
                            'keep': {'draft_batch': records[uid].get('draft_batch'),
                                     'draft_source_path': records[uid].get('draft_source_path')}})

    groups = {}
    for row in applied:
        groups.setdefault((row['keep']['draft_batch'], row['keep']['draft_source_path']), []).append(row)

    segments = []
    outdir = QA / 'fix'
    outdir.mkdir(parents=True, exist_ok=True)
    for n, ((db, ds), rows) in enumerate(sorted(groups.items(), key=lambda kv: str(kv[0])), 1):
        tag = 'qa-fix-%02d' % n
        p = outdir / (tag + '.jsonl')
        p.write_text(''.join(json.dumps({'id': r['id'], 'translation': r['translation'], 'notes': r['notes']},
                                        ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
        segments.append({'segment': tag, 'candidate': p.relative_to(PROJECT).as_posix(),
                         'candidate_sha256': digest(p.read_bytes()),
                         'ids': [r['id'] for r in rows],
                         'author_route': records[rows[0]['id']].get('model') or '',
                         'keep_provenance': {'draft_batch': db, 'draft_source_path': ds},
                         'revision_note': 'semantic QA fix from independent Grok review'})

    summary = {'batch': a.batch, 'applied': len(applied), 'rejected': rejected,
               'segments': [(s['segment'], len(s['ids'])) for s in segments]}
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    if not applied:
        print('nothing to apply')
        return 1
    job = {'batch_id': a.batch, 'workflow': 'simplified; semantic-QA revision batch',
           'segments': segments, 'targets': [i for s in segments for i in s['ids']],
           'revision_allowed': True, 'reason': 'independent semantic QA findings',
           'rejected_suggestions': rejected}
    d = WORK / a.batch
    d.mkdir(parents=True, exist_ok=True)
    (d / 'job.json').write_text(json.dumps(job, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('wrote job for %d rows; run snapshot/merge/verify next' % len(job['targets']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
