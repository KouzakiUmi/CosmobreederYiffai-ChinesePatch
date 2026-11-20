import csv
from pathlib import Path
import json
from collections import defaultdict

context_map = defaultdict(list)

for tsv_path in Path('tl_work/chunks').rglob('*.tsv'):
    try:
        with open(tsv_path, 'r', encoding='utf8') as f:
            reader = csv.reader(f, delimiter='\t')
            # 跳过标题行
            header = next(reader, None)
            for row in reader:
                if len(row) < 5: continue
                # 假设 TSV 结构: [seq, archive, entry, scene, line, ...]
                # scene 在索引 3, line 在索引 4
                scene = row[3]
                context_map[scene].append({
                    'row': row,
                    'file': str(tsv_path.relative_to('tl_work/chunks'))
                })
    except Exception as e:
        print(f"Error reading {tsv_path}: {e}")

linked_context = {s: r for s, r in context_map.items() if len(r) > 1}
# 将内容写入
with open('review/context-mapping.json', 'w', encoding='utf8') as f:
    json.dump(linked_context, f, ensure_ascii=False, indent=1)

print(f"Mapped {len(linked_context)} linked scenes.")
