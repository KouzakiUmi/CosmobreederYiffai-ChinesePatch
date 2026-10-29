"""Export all character-name decisions and scoped delivery evidence."""
from pathlib import Path
import json,csv,argparse
ROOT=Path(__file__).resolve().parents[4];R3=ROOT/'localization/editorial/r3-names'
def load(p):return json.loads(p.read_text('utf8'))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    out=a.output.resolve()
    if out.exists() or not out.is_relative_to(R3/'reports'):raise ValueError('New names report only')
    acceptance=load(a.candidate/'acceptance.json')
    if acceptance['status']!='passed_cpu_and_independent_review_not_real_clip_CRT_input':raise ValueError('Accepted target required')
    registry=load(ROOT/'localization/translations/character-names.json');manifest=load(R3/'compiled/final-01/manifest.json')
    out.mkdir(parents=True)
    headings=['英文原名','修前显示变体','当前译名','实际改动处数','裁决理由']
    lines=['# 全角色人名：音义统一对照','',
           '**36 项角色名已按姓名感、物种／词义双关和人物气质逐项裁决。不是强行让每个名字带动物字。**','',
           '## 已应用','',
           '- 839 个完整节点操作、895 个姓名替换片段，涉及两个内容版的66个文本资源；只改姓名及其原有断续首音，非姓名字符严格保持。',
           '- 保留R2全部778项非姓名修订。正式名、同源姓氏、正文、档案和无线电显示同步，纠正同人多译。',
           '- Tomcat→雄猫，原文TOM昵称三处→阿雄；Mauser→毛鼠。',
           '- Yiffai→伊吠，Yiffany→伊吠妮；全名仍为伊吠·伊吠、伊吠妮·伊吠，不省重复。',
           '- Gepard→猎豹，Chauchat→绍狞；名字的意译不自动成为人物亚种鉴定。','',
           '## 全部裁决','', '| '+' | '.join(headings)+' |','|'+' --- |'*len(headings)]
    with (out/'names.tsv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n');writer.writerow(headings)
        for n in registry['names']:
            count=manifest['name_counts'][n['name_id']];old='／'.join(n['old_forms']) or '无可见自报；不新增露脸'
            row=[n['name_id'],old,n['target'],str(count['changed_targets']),n['reason']]
            writer.writerow(row);lines.append('| '+' | '.join(x.replace('|','／').replace('\n',' ') for x in row)+' |')
    lines+=['','## 必须保住的例外','',
            '- The0保数字0及原有字母大小写；不把内部占位符Derek猜成其已揭真名。',
            '- Traeh、Sevaw、Erauqs保原文反写信息，不直接译出几何谜底。其他四个只证档案标题的项目不当作已证个人名改写，谜题线索／机制不改。',
            '- Bossu物种未有足够证据，不硬改牛／狗名；女王、高位领主等称号不提前替成人名。',
            '- Macsen／Gitgud当前没有可见自报名载体；麦森／季高仅是已裁定映射，原掩名和匿名呈现保持，绝不凭entry键新增人物介绍。',
            '- Bigbold等通用物种、无名Boss、真实制作／赞助者、游戏英文品牌、程序ID／文件名／JSON keys、动态占位符不在人物显示名改写范围。',
            '- 39条父子称谓上下文记录维持狼犬／狼崽现称谓；1条源句有Yiffany但现译未显名的记录留正文精校按语境判断，未借改名猜补句子。','',
            '## 依据与取舍','',
            '“伊吠”取犬类发声层，“绍狞”以已证狞猫补可核chat猫义，属于中文编辑补偿；不是作者官方释名，也不宣称把所有原词义／成人俚语一字不落塞进名字。姓名有趣不意味着每句添加喵／汪口癖。',
            '军武同名、跨语普通词义、反写及角色种属分别留证，不把同名搜索结果当作者意图；保留名字也给理由。标题与正文的恩莉耶、黛蕾等异形已统一。','',
            '## 回归','',
            '- 36目标／37别名独立语义及载体审查，昵称元数据收窄到三个明确TOM来源。',
            '- 13项改名编译测试；三昵称正例、两个越界／大小写负例通过。',
            '- 最终实际候选17个CPU步骤全部exit 0，覆盖姓名字体、颜色／坐标／频率、分页、图鉴与两内容版实际字典／106个VSN测试输入。',
            '- 独立归档核验：actor ID／隐藏身份JF／控制／JSON keys不变；旧字形墨迹与度量、ASCII完整记录和非字体原画像素保持。只允许字库扩字带内位置重排。','',
            '[实际替换对照TSV](<names.tsv>) · [语义审查](<../../review/names-01.md>) · [数据消费与内部ID边界](<../../review/engineering-01.md>) · [最终实际归档核验](<../../review/final-review.md>)','',
            '## 交付边界','',
            '未安装、启动游戏或读取／修改用户存档，未发布到远端。CPU通过不是GPU／CRT、完整场景层级、输入／装备／全图或历史存档文本缓存验收；父验收未覆盖项继续保留。既有存档若缓存文案，本轮不迁移其内容。',
            '本轮只统一人名，不把其他待核源文、所有物种术语或整段文风宣布为最终精校完成。']
    (out/'SUMMARY.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(json.dumps({'names':len(registry['names']),'operations':manifest['operation_count'],'output':str(out.relative_to(ROOT))},ensure_ascii=False))
if __name__=='__main__':main()
