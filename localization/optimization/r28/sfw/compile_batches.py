"""Compile explicitly authored TSV candidates with frozen English source, never MT."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main():
    sources = {}
    for kind in ('ds', 'vsn', 'ui'):
        for line in (HERE / ('ledger-' + kind + '.jsonl')).read_text(encoding='utf-8').splitlines():
            r = json.loads(line)
            key = r['review_key']
            source = r['raw_source'].strip()
            if key in sources and sources[key] != source: raise ValueError('source key collision')
            sources[key] = source
    for path in sorted((HERE / 'translations').glob('*.tsv')):
        data = {}
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line or line.startswith('#'): continue
            parts = line.split('\t')
            if len(parts) < 2: raise ValueError(f'{path.name}:{number}: missing tab')
            key, target = parts[:2]
            if key in data: raise ValueError('duplicate batch key: ' + key)
            # JSON-style escapes enable authored paragraph/blank-slot preservation.
            target = target.replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
            status = parts[2] if len(parts) > 2 and parts[2] else 'candidate'
            data[key] = {'source': sources[key], 'translation': target, 'status': status,
                         'notes': [parts[3]] if len(parts) > 3 else []}
        out = path.with_suffix('.json')
        assert out.resolve().is_relative_to(HERE)
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(path.name, len(data))

if __name__ == '__main__': main()
