"""Build source-context packets; decisions/merged strings are explicitly authored below."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'localization/tools'))
import sfw_localization as sfw


def main():
    review = json.loads((HERE / 'vsn-join-source-review.json').read_text(encoding='utf-8'))
    manifest, payloads = sfw.inventory_archive(ROOT / 'backup/cosmobreeder-multi.jar')
    rows = []
    for operation in review['operations']:
        if operation['status'] != 'unique_whole_source_match_review_only': continue
        lines = payloads[operation['logical_path']].decode('utf-8').splitlines(keepends=True)
        first = operation['inputs'][0]['source_line_evidence']
        last = operation['inputs'][-1]['source_line_evidence']
        rows.append({**operation, 'context_before': lines[max(0, first-6):first-1],
                     'context_after': lines[last:last+5]})
    (HERE / 'vsn-join-contexts.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print('context packets:', len(rows))

if __name__ == '__main__': main()
