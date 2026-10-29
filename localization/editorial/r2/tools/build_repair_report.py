"""Build the scoped repair report from frozen decisions and accepted targets."""
from pathlib import Path
from collections import Counter
import argparse,csv,json
ROOT=Path(__file__).resolve().parents[4];R2=ROOT/'localization/editorial/r2'
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines() if s.strip()]
def safe(v):
    s='' if v is None else str(v)
    return "'"+s if s.lstrip().startswith(('=','+','-','@')) else s

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();out=a.output.resolve()
    if out.exists() or not out.is_relative_to(R2/'reports'):raise ValueError('New r2 report only')
    acceptance=json.loads((a.candidate/'acceptance.json').read_text('utf8'))
    if acceptance['status']!='passed_cpu_and_independent_review_not_real_clip_CRT_input':raise ValueError('Accepted CPU/independent target required')
    compiled=R2/'compiled/pass-02';manifest=json.loads((compiled/'manifest.json').read_text('utf8'))
    decisions=rows(compiled/'decisions.jsonl');edits={e['edit_id']:e for e in rows(compiled/'canonical-edits.jsonl')}
    original={f['finding_id']:f for f in rows(ROOT/'localization/editorial/r1/reports/rough-review-01/findings.jsonl')}
    out.mkdir(parents=True)
    with (out/'decisions.tsv').open('w',encoding='utf-8-sig',newline='') as stream:
        fields=['finding_id','packet','action','resolution','reason','remaining_uncertainty','source_quote','before','after','edit_ids']
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t');writer.writeheader()
        for d in decisions:
            f=original[d['finding_id']];after='\n'.join(edits[e]['new'] for e in d.get('edit_ids',[]))
            value={k:d.get(k,'') for k in fields};value.update(source_quote=f['source_quote'],before=f['current_quote'],after=after,
                 edit_ids=', '.join(d.get('edit_ids',[])))
            writer.writerow({k:safe(v) for k,v in value.items()})
    deferred=[d for d in decisions if d['action']=='defer'];rejected=[d for d in decisions if d['action']=='reject']
    pending=['# 留置项与驳回理由','', '留置不等于现译正确；以下没有冒称已修。部分需原文／用途补证，部分双关已确认有问题但尚无可确认的整组改写。','',
             '| 编号 | 处置 | 理由 |','| --- | --- | --- |']
    for d in deferred+rejected:
        pending.append('| '+d['finding_id']+' | '+d['action']+' | '+d['reason'].replace('|','／').replace('\n',' ')+' |')
    pending+=['','## 保守局部修正','',
              'P04-018 撤销未经证实的“性感”，保留源 S、S 残音；没有猜补完整词，也没有声称还原原作表演。']
    (out/'PENDING.md').write_text('\n'.join(pending)+'\n',encoding='utf8')
    md=['# 先修一波：全部粗校提案处置结果','',
        '**已全面复审 339 条记录并落地可确认修订；这不是后续系统整段精校的完成报告。**','',
        '## 本轮结果','',
        '- **291 条 apply、45 条 defer、3 条 reject**。291 含 1 项明确标注的保守局部修正；留置项不算已修。',
        '- 536 个主审节点，按冻结版本别名展开及明确命名撤回后为 **778 个来源锁定资源操作**；其中涉及 91 个正文／字典 Tomcat 命名位置。两者有交集，不能重复相加。',
        '- 每个操作绑定归档、entry、整资源 SHA、原位置和精确旧值，保留控制、分支、actor ID、既有空白合句槽及非目标字节。',
        '- SFW 与 NSFW、男女主、状态分支分别回填，不用目录名字猜发言人。','',
        '## Tomcat','',
        '已撤回没有官方／作者依据的“汤姆猫”，保留英文 Tomcat；原界面的大写流程可显示 TOMCAT。正文、字典、头像名、对白标签、底部联系人一致处理，不改角色 ID、频率或隐藏身份门控。未另定“公猫／雄猫”为角色正式名字。',
        '术语表已记录本次保留原名决定；修前 R1 与冻结初稿保留作历史，不用回改旧证据伪装原先就正确。','',
        '## 修了哪些问题','',
        '- 完整中文意群的衔接、指代和问答；保留同一合句头中全部句义，不照原英文框逐词替换。',
        '- 主宾、否定／让步、玩法权限、技术说明及信号含义；不把配备系统译成制造方法，不把通讯维持译成身体撑不住。',
        '- 真口吃与排版断词分开、人物专业与闲聊转换、笑点铺垫和回应。未定名字与残句不硬猜。',
        '- SFW 明确污染、无据补词、称呼与物种误指；保留不同内容版真正不同的原因／经历。','',
        '## 独立复核与回归','',
        '- 339 条决策、536 个主审节点均有独立语义复核；333 条直接通过，6 条退修后另做定向复核并全部闭环。',
        '- 修订引擎 13 项单测、28 项独立属性测试，真实资源／别名／非目标字节核验另留工程报告。',
        '- 最终候选实际新 JVM／字体／分页／资料卡／繁育／紧凑字段等 **17 个 CPU 回归步骤全部 exit 0**，两内容版测试输入均绑定最终归档。',
        '- 独立比较实际归档：目标文本精确等于复审台账，非目标明文不漂移；旧字形视觉与度量保留、ASCII 度量不变，字体内部坐标重排不是字形变形。','',
        '## 查阅','',
        '[逐条裁决与实际节点新文（TSV）](<decisions.tsv>) · [45 项留置与3项驳回](<PENDING.md>)',
        '', '[复审闭环](<../../compiled/pass-02/semantic-acceptance.json>) · [实际归档独立核验](<../../engineering/final-review.md>)',
        '', '[修订合同与节点保护](<../../REPAIR_CONTRACT.md>)', '',
        '## 边界与下一阶段','',
        '尚未启动游戏、安装到游戏目录、访问存档或完成真实 GPU／CRT／完整场景层次／输入与装备全路径验收。所有父验收限制继续继承；不以 CPU 或结构通过冒充实机。',
        '下一阶段再按 R1 方案做系统整段精校，优先处理留置的特殊双关／源异常和整段口吻；不能将本轮可用修正版称作全游戏最终定稿。']
    (out/'SUMMARY.md').write_text('\n'.join(md)+'\n',encoding='utf8')
    print(json.dumps({'records':len(decisions),'actions':dict(Counter(d['action'] for d in decisions)),'output':str(out.relative_to(ROOT))},ensure_ascii=False))
if __name__=='__main__':main()
