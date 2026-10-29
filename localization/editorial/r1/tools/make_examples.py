"""Expose two supported rough directions and one returned draft; no application."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[4]
R1=ROOT/'localization/editorial/r1'
folder=R1/'reports/rough-review-01';out=folder/'EXAMPLES.md'
if out.exists():raise ValueError('New example view only')
records={r['finding_id']:r for r in (json.loads(s) for s in (folder/'findings.jsonl').read_text('utf8').splitlines())}
chosen=[('P02-008','先弄懂问答，再重写技术解释'),('P02-013','把跨框碎句还原成完整方向提示'),('P01-013','反例：顺口不等于保住笑点与人物')]
text=['# 粗校方法对照','',
      '**以下是粗校提案与抽核意见，不是已批准的游戏台词。第三项明确退修，不应采用原建议。**','']
for fid,title in chosen:
    r=records[fid]
    text+=['## '+fid+' · '+title,'',
           '抽核：`'+r['review_conclusion']+'`；下一步：`'+r['next_action']+'`。','',
           '### 连续原文','', '```text',r['source_quote'],'```','',
           '### 当前补丁中文','', '```text',r['current_quote'],'```','',
           '### 粗校草案（非定稿）','', '```text',r['proposed_zh'] or '尚无建议，需补证','```','',
           '### 独立抽核意见','',r['review_reason'],'',
           '[对应分包摘要](<../../audit/'+r['packet']+'/summary.md>)','']
text+=['## 应用前仍须做什么','',
       '在完整场景中复写并试读，再回头核英文；按实际节点形成映射、保护占位符和控制事件。不能把此处整段直接均分回原文行，也不能因为方向获支持就跳过二审。']
out.write_text('\n'.join(text)+'\n',encoding='utf8')
print(out.relative_to(ROOT).as_posix())
