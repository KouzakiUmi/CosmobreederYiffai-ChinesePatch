"""Batch pipeline: snapshot -> merge -> verify. Single writer, atomic, one record per batch.

Simplified workflow per localization/docs/简化工作流-20261024.md.

  python -B tools/batch.py status
  python -B tools/batch.py snapshot --batch batch_181
  python -B tools/batch.py merge    --batch batch_181
  python -B tools/batch.py verify   --batch batch_181

job.json holds the whole batch contract. A batch may be one candidate file or several
segments (each with its own candidate, QA pin and author route); segments keep their own
provenance so a large batch does not blur who translated what.
"""
import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projectlib import PROJECT, digest, load_units  # noqa: E402

CANON = PROJECT / 'translations/zh-CN.jsonl'
WORK = PROJECT / 'work/batches'
TOTAL = 8973


def obj_hash(record):
    raw = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return digest(raw)


def batch_dir(bid):
    d = WORK / bid
    d.mkdir(parents=True, exist_ok=True)
    return d


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def dump(path, doc):
    tmp = Path(str(path) + '.tmp')
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def rows():
    return [json.loads(l) for l in CANON.read_text(encoding='utf-8').splitlines() if l.strip()]


def state(records, batch_targets=None):
    by_id = {r['id']: obj_hash(r) for r in records}
    drafts = sum(1 for r in records if r.get('draft'))
    doc = {'total': len(records), 'drafts': drafts, 'untranslated': len(records) - drafts,
           'canonical_sha256': digest(CANON.read_bytes()), 'objects': by_id}
    if batch_targets:
        doc['target_state'] = {i: by_id.get(i) for i in batch_targets}
    return doc


def segments(job):
    if job.get('segments'):
        return job['segments']
    return [{'segment': 'main', 'candidate': job['candidate'],
             'candidate_sha256': job.get('candidate_sha256'), 'ids': job['targets'],
             'author_route': job.get('author_route') or ''}]


def load_segments(job):
    """Return [(record, segment)] in batch order, verifying every candidate file."""
    out = []
    for seg in segments(job):
        raw = (PROJECT / seg['candidate']).read_bytes()
        if seg.get('candidate_sha256') and digest(raw) != seg['candidate_sha256']:
            raise SystemExit('candidate drifted for segment %s' % seg['segment'])
        rows_ = [json.loads(l) for l in raw.decode('utf-8').splitlines() if l.strip()]
        if [r['id'] for r in rows_] != seg['ids']:
            raise SystemExit('segment %s ids/order mismatch' % seg['segment'])
        out += [(r, seg) for r in rows_]
    return out


def require_job(bid):
    p = batch_dir(bid) / 'job.json'
    if not p.exists():
        raise SystemExit('missing job manifest: %s' % p)
    job = load(p)
    if job.get('batch_id') != bid:
        raise SystemExit('job.batch_id mismatch')
    ids = job['targets']
    if not ids or len(set(ids)) != len(ids):
        raise SystemExit('job.targets must be a non-empty unique list')
    flat = [r['id'] for r, _ in load_segments(job)]
    if flat != ids:
        raise SystemExit('job.targets must equal the concatenated segment ids')
    return job


def cmd_status(_a):
    recs = rows()
    drafts = sum(1 for r in recs if r.get('draft'))
    st = PROJECT / '.agent-state.json'
    wb = load(st).get('latest_exported_workbook_count') if st.exists() else None
    print(json.dumps({'total': len(recs), 'drafts': drafts, 'untranslated': len(recs) - drafts,
                      'latest_exported_workbook_count': wb,
                      'canonical_sha256': digest(CANON.read_bytes())}, ensure_ascii=False))


def cmd_snapshot(a):
    job = require_job(a.batch)
    recs = rows()
    if len(recs) != TOTAL:
        raise SystemExit('canonical must hold %d rows, got %d' % (TOTAL, len(recs)))
    have = {r['id']: r for r in recs}
    missing = [i for i in job['targets'] if i not in have]
    if missing:
        raise SystemExit('unknown target ids: %r' % missing[:5])
    already = [i for i in job['targets'] if have[i].get('draft')]
    if already and not job.get('revision_allowed'):
        raise SystemExit('targets already translated: %r' % already[:5])
    doc = state(recs, job['targets'])
    doc['batch_id'] = a.batch
    doc['job'] = {'path': (batch_dir(a.batch) / 'job.json').relative_to(PROJECT).as_posix(),
                  'sha256': digest((batch_dir(a.batch) / 'job.json').read_bytes())}
    p = batch_dir(a.batch) / 'before.json'
    if p.exists():
        raise SystemExit('before.json already exists; refusing to overwrite snapshot')
    dump(p, doc)
    print(json.dumps({'batch': a.batch, 'drafts_before': doc['drafts'], 'targets': len(job['targets']),
                      'segments': len(segments(job)), 'canonical_sha256': doc['canonical_sha256']}, ensure_ascii=False))


def expected_records(before_rows, pairs, units):
    by_id = {r['id']: r for r in before_rows}
    exp = {}
    for c, seg in pairs:
        unit = units[c['id']]
        if c.get('source_sha256') and c['source_sha256'] != unit['source_sha256']:
            raise SystemExit('candidate source hash mismatch for %s' % c['id'])
        new = json.loads(json.dumps(by_id[c['id']]))
        new['source_sha256'] = unit['source_sha256']
        new['draft'] = c['translation']
        new['translation'] = new.get('translation', '')
        new['status'] = 'draft'
        new['model'] = seg.get('author_route') or new.get('model', '')
        new['notes'] = new.get('notes', '')
        new['draft_notes'] = c.get('notes', '')
        new['reviewer'] = new.get('reviewer', '')
        new['usage_approved'] = new.get('usage_approved', False)
        keep = seg.get('keep_provenance') or {}
        new['draft_batch'] = keep.get('draft_batch') or seg.get('batch_tag') or seg['segment']
        new['draft_source_path'] = keep.get('draft_source_path') or seg['candidate']
        exp[c['id']] = new
    return exp


def cmd_merge(a):
    job = require_job(a.batch)
    bpath = batch_dir(a.batch) / 'before.json'
    if not bpath.exists():
        raise SystemExit('run snapshot first')
    before = load(bpath)
    pairs = load_segments(job)
    for c, _seg in pairs:
        if not isinstance(c.get('translation'), str) or not c['translation'].strip():
            raise SystemExit('empty translation for %s' % c['id'])

    backup = batch_dir(a.batch) / 'canonical.before.jsonl'
    if backup.exists():
        raise SystemExit('pre-merge backup already exists; this batch was already merged')
    recs = rows()
    if state(recs)['canonical_sha256'] != before['canonical_sha256']:
        raise SystemExit('canonical changed since snapshot; refusing to merge')
    exp = expected_records(recs, pairs, {u['id']: u for u in load_units()})

    out, seen = [], set()
    for r in recs:
        if r['id'] in exp:
            out.append(exp[r['id']])
            seen.add(r['id'])
        else:
            out.append(r)
    if seen != set(job['targets']):
        raise SystemExit('not all targets replaced')

    body = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in out).encode('utf-8')
    backup.write_bytes(CANON.read_bytes())
    tmp = CANON.with_suffix('.jsonl.tmp')
    tmp.write_bytes(body)
    os.replace(tmp, CANON)
    print(json.dumps({'merged': a.batch, 'rows': len(out), 'targets': len(job['targets']),
                      'canonical_sha256': digest(body)}, ensure_ascii=False))


def cmd_verify(a):
    job = require_job(a.batch)
    before = load(batch_dir(a.batch) / 'before.json')
    segs = segments(job)
    pairs = load_segments(job)
    recs = rows()
    after = state(recs, job['targets'])
    by_id = {r['id']: r for r in recs}
    units = {u['id']: u for u in load_units()}
    checks, problems = [], []

    def add(cid, title, ok, detail=''):
        checks.append({'id': cid, 'title': title, 'result': 'PASS' if ok else 'FAIL', 'detail': detail})
        if not ok:
            problems.append(cid)

    add('C1', 'canonical still holds %d objects' % TOTAL, len(recs) == TOTAL, len(recs))
    changed = [i for i, h in after['objects'].items() if before['objects'].get(i) != h]
    add('C2', 'only this batch targets changed', set(changed) == set(job['targets']),
        'changed=%d expected=%d' % (len(changed), len(job['targets'])))
    add('C3', 'every target is a non-empty draft row', all(by_id[i].get('draft') for i in job['targets']))
    if job.get('revision_allowed'):
        add('C4', 'draft count unchanged by a revision batch', after['drafts'] == before['drafts'],
            'before=%d after=%d' % (before['drafts'], after['drafts']))
    else:
        add('C4', 'draft count grew by exactly the batch size', after['drafts'] == before['drafts'] + len(job['targets']),
            'before=%d after=%d' % (before['drafts'], after['drafts']))
    add('C5', 'segment candidate ids/order equal job targets',
        [r['id'] for r, _ in pairs] == job['targets'])
    add('C6', 'every target keeps its catalog source hash',
        all(by_id[i]['source_sha256'] == units[i]['source_sha256'] for i in job['targets']))
    add('C7', 'every target keeps its segment provenance',
        all(by_id[c['id']].get('draft_batch') == ((seg.get('keep_provenance') or {}).get('draft_batch') or seg.get('batch_tag') or seg['segment']) and
            by_id[c['id']].get('draft_source_path') == ((seg.get('keep_provenance') or {}).get('draft_source_path') or seg['candidate']) for c, seg in pairs))
    add('C8', 'no target left untranslated', all(by_id[i]['status'] == 'draft' for i in job['targets']))
    add('C9', 'every target draft equals its candidate translation byte-for-byte',
        all(by_id[c['id']]['draft'] == c['translation'] for c, _ in pairs))
    add('C10', 'segment author routes were recorded per segment',
        all(by_id[c['id']].get('model') == (seg.get('author_route') or '') for c, seg in pairs))

    doc = {'batch_id': a.batch, 'checks': checks, 'problems': problems,
           'verdict': 'PASS' if not problems else 'FAIL',
           'counts': {'before_drafts': before['drafts'], 'after_drafts': after['drafts'],
                      'targets': len(job['targets']), 'segments': len(segs), 'total': after['total']},
           'canonical_sha256_before': before['canonical_sha256'],
           'canonical_sha256_after': after['canonical_sha256'],
           'job': before.get('job'),
           'segments': [{'segment': s['segment'], 'rows': len(s['ids']), 'candidate': s['candidate'],
                         'qa': s.get('qa'), 'author_route': s.get('author_route')} for s in segs]}
    dump(batch_dir(a.batch) / 'after.json', after)
    dump(batch_dir(a.batch) / 'result.json', doc)
    print(json.dumps({'batch': a.batch, 'verdict': doc['verdict'],
                      'checks': {c['id']: c['result'] for c in checks},
                      'drafts': after['drafts'], 'canonical_sha256': after['canonical_sha256']}, ensure_ascii=False))
    return 0 if not problems else 1


def main(argv):
    assert os.environ.get('PYTHONDONTWRITEBYTECODE') == '1' and os.environ.get('PYTHONIOENCODING') == 'utf-8'
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('status')
    for name in ('snapshot', 'merge', 'verify'):
        p = sub.add_parser(name)
        p.add_argument('--batch', required=True)
    a = ap.parse_args(argv[1:])
    return {'status': cmd_status, 'snapshot': cmd_snapshot, 'merge': cmd_merge, 'verify': cmd_verify}[a.cmd](a) or 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
