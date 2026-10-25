"""Intake translated pack output into a batch contract.

  python -B tools/intake.py --batch batch_185 --packs pk01 pk02 --route "openai-codex/gpt-6.1-sol/high"

Reads each pack's input.jsonl (ids/order/source/protected) and output.jsonl
(id/translation/notes), runs the machine checks below, then writes
work/batches/<bid>/job.json which tools/batch.py can snapshot/merge/verify.

Machine checks (blocking): row count, id order, non-empty translation, protected
tokens preserved, JSONL valid. Report-only: latin residue, width hint, duplicate
source inconsistencies, empty-note coverage.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projectlib import PROJECT, digest  # noqa: E402

TR = PROJECT / 'work/translate'
LATIN = re.compile(r'[A-Za-z]{3,}')


def read_jsonl(path):
    out = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--batch', required=True)
    ap.add_argument('--packs', nargs='+', required=True)
    ap.add_argument('--route', required=True)
    ap.add_argument('--allow-empty', action='store_true',
                    help='accept rows the translator deliberately left empty (recorded, not merged)')
    a = ap.parse_args()

    segments, report, blocking = [], [], []
    for pk in a.packs:
        d = TR / pk
        inp = read_jsonl(d / 'input.jsonl')
        outp = d / 'output.jsonl'
        if not outp.exists():
            blocking.append('%s: output.jsonl missing' % pk)
            continue
        out = read_jsonl(outp)
        if len(out) != len(inp):
            blocking.append('%s: row count %d != input %d' % (pk, len(out), len(inp)))
            continue
        ids_in = [r['id'] for r in inp]
        ids_out = [r['id'] for r in out]
        if ids_in != ids_out:
            blocking.append('%s: id order differs from input' % pk)
            continue
        cand, empty, latin, no_note, dup = [], [], [], [], {}
        for src, tr in zip(inp, out):
            tx = tr.get('translation')
            if not isinstance(tx, str):
                blocking.append('%s: %s translation not a string' % (pk, src['id']))
                continue
            if not tx.strip():
                empty.append(src['id'])
                if not a.allow_empty:
                    blocking.append('%s: %s empty translation' % (pk, src['id']))
                continue
            for tok in (src.get('protected') or []):
                if tx.count(tok) < src['source'].count(tok):
                    blocking.append('%s: %s lost protected token %r' % (pk, src['id'], tok))
            if LATIN.search(tx) and not LATIN.search(src['source']):
                latin.append(src['id'])
            if not (tr.get('notes') or '').strip():
                no_note.append(src['id'])
            key = src['source']
            dup.setdefault(key, set()).add(tx)
            cand.append({'id': src['id'], 'translation': tx, 'notes': tr.get('notes') or '',
                         'source_sha256': src.get('source_sha256')})
        cand_path = d / 'candidate.jsonl'
        cand_path.write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in cand),
                             encoding='utf-8')
        segments.append({'segment': pk, 'batch_tag': a.batch,
                         'candidate': cand_path.relative_to(PROJECT).as_posix(),
                         'candidate_sha256': digest(cand_path.read_bytes()),
                         'ids': [c['id'] for c in cand],
                         'author_route': a.route, 'qa': None,
                         'qa_note': 'machine checks only at intake; semantic spot-check recorded in the batch report'})
        inconsistent = {k: sorted(v) for k, v in dup.items() if len(v) > 1}
        report.append({'pack': pk, 'rows': len(cand), 'empty': len(empty), 'latin_residue': len(latin),
                       'rows_without_notes': len(no_note),
                       'duplicate_source_inconsistent': len(inconsistent),
                       'empty_ids': empty[:5], 'latin_ids': latin[:5]})

    print(json.dumps({'packs': len(segments), 'rows': sum(len(s['ids']) for s in segments),
                      'blocking': blocking[:10], 'blocking_count': len(blocking),
                      'report': report}, ensure_ascii=False, indent=1))
    if blocking:
        print('BLOCKED: fix the packs and rerun; nothing written')
        return 1

    job = {'batch_id': a.batch,
           'workflow': 'simplified 2026-10-24 + new translation intake (machine checks at intake)',
           'segments': segments,
           'targets': [i for s in segments for i in s['ids']],
           'intake_report': report,
           'batch_180_exception_applicable': False}
    d = PROJECT / 'work/batches' / a.batch
    d.mkdir(parents=True, exist_ok=True)
    p = d / 'job.json'
    if p.exists():
        print('job.json already exists; refusing to overwrite')
        return 1
    p.write_text(json.dumps(job, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('wrote %s with %d rows' % (p.relative_to(PROJECT).as_posix(), len(job['targets'])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
