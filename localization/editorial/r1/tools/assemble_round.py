"""Assemble read-only rough-review proposals; never apply them to translations."""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import argparse
import csv
import json

ROOT=Path(__file__).resolve().parents[4]
R1=ROOT/'localization/editorial/r1'


def records(path):
    return [json.loads(s) for s in path.read_text('utf8').splitlines() if s.strip()]


def tsv_display(value):
    text=json.dumps(value,ensure_ascii=False) if isinstance(value,(list,dict)) else '' if value is None else str(value)
    # TSV is a viewing copy; exact unmodified values remain in JSONL.
    return "'"+text if text.lstrip().startswith(('=','+','-','@')) else text


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--validation',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();out=a.output.resolve()
    if out.exists() or not out.is_relative_to(R1/'reports'):raise ValueError('New editorial report directory only')
    valid=json.loads(a.validation.read_text('utf8'))
    if valid['status']!='PASS_STRUCTURAL_ONLY' or any(p['read_full_scenes']!=p['expected_scenes'] for p in valid['packets']):
        raise ValueError('All ten packet coverage and structural checks required')
    findings=[];cover=[];packet_summary=[]
    for packet in valid['packets']:
        name=packet['packet'];folder=R1/'audit'/name
        found=records(folder/'findings.jsonl');covered=records(folder/'coverage.jsonl')
        for f in found:findings.append({'packet':name,**f})
        for c in covered:cover.append({'packet':name,**c})
        packet_summary.append({'packet':name,'scenes':len(covered),'rows':packet['read_full_rows'],
                               'findings':len(found),'statuses':dict(Counter(f['status'] for f in found)),
                               'severity':dict(Counter(f['severity'] for f in found))})
    if len({f['finding_id'] for f in findings})!=len(findings):raise ValueError('Duplicate global finding ID')
    review_path=R1/'review/spotcheck-01.json'
    review=json.loads(review_path.read_text('utf8'))
    for name,pin in review['input_sha256'].items():
        if sha256((ROOT/name).read_bytes()).hexdigest()!=pin:raise ValueError('Independent review input drift')
    reviewed={r['finding_id']:r for r in review['findings']}
    if len(reviewed)!=len(review['findings']) or not set(reviewed)<={f['finding_id'] for f in findings}:
        raise ValueError('Independent review finding scope')
    for f in findings:
        r=reviewed.get(f['finding_id'])
        f['review_conclusion']=r['conclusion'] if r else 'not_spotchecked'
        f['review_calibration']=r['calibrated_severity'] if r else ''
        f['review_reason']=r['reason'] if r else ''
        f['next_action']='gather_evidence' if f['status']=='needs_evidence' or (r and r['conclusion']=='needs_evidence') else 'rewrite_proposal' if r and r['conclusion']=='needs_revision' else 'full_second_review_and_node_mapping' if r and r['conclusion']=='support_proposal' else 'independent_review'
        f['usable_as_final_translation']=False
    out.mkdir(parents=True)
    (out/'findings.jsonl').write_text(''.join(json.dumps(f,ensure_ascii=False)+'\n' for f in findings),encoding='utf8')
    columns=['finding_id','packet','scene_id','severity','status','category','source_quote','current_quote','proposed_zh','reason','row_ids','evidence_refs','reference_keys','review_conclusion','review_calibration','review_reason','next_action']
    with (out/'findings.tsv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',extrasaction='ignore');writer.writeheader()
        for f in findings:
            writer.writerow({k:tsv_display(v) for k,v in f.items()})
    statuses=Counter(f['status'] for f in findings);severity=Counter(f['severity'] for f in findings)
    proposed_severity=Counter(f['severity'] for f in findings if f['status']=='proposal')
    pending_severity=Counter(f['severity'] for f in findings if f['status']=='needs_evidence')
    summary={'stage':'R1_rough_proposals_not_approved','catalog_units':valid['catalog_units'],
             'source_rows':valid['source_rows'],'canonical_rows':valid['counts']['canonical_rows'],
             'review_blocks':valid['scenes'],'packets':packet_summary,'findings':len(findings),
             'status_counts':dict(statuses),'risk_severity_all':dict(severity),
             'proposal_severity':dict(proposed_severity),'pending_evidence_risk':dict(pending_severity),
             'category_counts':dict(Counter(f['category'] for f in findings)),
             'block_results':dict(Counter(c['result'] for c in cover)),
             'limited_independent_review':{'scope':review['scope'],'checked':len(reviewed),
                  'conclusions':dict(Counter(r['conclusion'] for r in reviewed.values())),
                  'not_spotchecked':len(findings)-len(reviewed),'approved':False},
             'formal_translations_modified':False,'applied':False,'approved':False,
             'limits':valid['limits']+['Findings can overlap across variants and are not a count of unique defective sentences.',
                                      'Pending-evidence risks are not confirmed translation mistakes.',
                                      'Independent spotchecks cover only their explicitly named findings.']}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    md=['# 首轮全文粗校总览','',
        '**本轮为文档与粗校提案，不是正式定稿、回填或部署。**','',
        '## 覆盖','',
        f"- {valid['catalog_units']:,} catalog 单元、{valid['source_rows']:,} 来源记录已进入工单；全十包已提交整块通读收据。",
        f"- 去重后 {valid['counts']['canonical_rows']:,} 审读行、{valid['scenes']:,} 审读块（包含 UI 组与代码库存，不等于剧情场数）。",
        '- 版本别名仅在源文／现译／控制全部相同时共享阅读；不同主角与分支不强行归一。',
        '- code 与图像仅按用途／转录范围记录，未证实的实际画面不冒称已校。','',
        '## 发现与待核','',f'- 共 {len(findings)} 条记录：'+ '；'.join(f'{k} {v}' for k,v in sorted(statuses.items()))+'。',
        '- 待复审改写提案分级：'+ '；'.join(f'{k} {v}' for k,v in sorted(proposed_severity.items()))+'。',
        '- 待证据项只记录潜在风险，不算已确认错译：'+ '；'.join(f'{k} {v}' for k,v in sorted(pending_severity.items()))+'。',
        '- 发现可能在男女／内容版本中重复，不能直接说有同样数量的独立坏句。',
        '- 以上等级按首轮原记录统计；独立抽核的降级／退修另列，不覆盖作者稿，也不冒充全部发现已复审。','',
        '[完整逐段记录（TSV）](<findings.tsv>) · [机器记录](<findings.jsonl>) · [统计](<summary.json>)','',
        '## 代表性问题与重写方法','',
        '- 技术问答：先理解“配有回收系统”，不能顺着英文把它写成“用回收系统造出来”。',
        '- 连续方向提示：把“位于／在”式跨框破句整合成完整中文，同时保留“东北部深处”等关键信息。',
        '- 成组笑点：大人裤子／丢裤子／装专业造词须连同回应重写；粗校中看似顺口但提前包袱、添加无源口吃的建议已退修。','',
        '[原文—现译—粗校稿—抽核意见对照](<EXAMPLES.md>)。示例不是定稿；退修稿明确不可直接采用。','',
        '## 分包','', '| 包 | 审读块 | 审读行 | 发现 | 摘要 |','| --- | ---: | ---: | ---: | --- |']
    for r in packet_summary:
        name=r['packet'];md.append(f"| {name} | {r['scenes']} | {r['rows']} | {r['findings']} | [摘要](<../../audit/{name}/summary.md>) |")
    md += ['', '## 有限独立抽核', '',
           f"已对01／02／04三包中的 {len(reviewed)} 条高风险／代表提案回到整场原文抽核，结论："+
             '；'.join(f'{k} {v}' for k,v in sorted(Counter(r['conclusion'] for r in reviewed.values()).items()))+'。',
           '支持仅指粗校方向，不是批准；退修项已在完整表加入 review_conclusion／review_reason／next_action，不能把原建议直接当定稿。其余发现尚未独立抽核。',
           '[抽核说明](<../../review/spotcheck-01.md>)',
           '', '## 下一步精修', '',
           '1. 先裁决 A 类施受／否定／玩法／关系问题和涉及源异常的待核项。',
           '2. 按完整场景处理 B 类连续衔接、习语、笑点与口吻，不退回单句同义词替换。',
           '3. 术语先核语境和名称／说明／对话互证；不把未裁决术语做全局替换。',
           '4. 独立复审具体提案，接受／改写／驳回均留记录；本表不自动获得批准。',
           '5. 定稿后另做实际输出节点映射、保护字段检查、字宽／分页与实机，不直接应用段落稿。', '',
           '结构校验只能核身份、字段和覆盖收据，不能代替读懂全文；本轮未更改正式译文、归档、安装器或存档。']
    (out/'SUMMARY.md').write_text('\n'.join(md)+'\n',encoding='utf8')
    print(json.dumps({k:summary[k] for k in ('stage','review_blocks','canonical_rows','findings','status_counts','proposal_severity','pending_evidence_risk')},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
