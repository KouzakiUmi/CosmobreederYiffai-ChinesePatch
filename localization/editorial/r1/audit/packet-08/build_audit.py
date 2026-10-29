"""仅生成本目录粗校文档；语义判断来自已完成的逐段reader阅读。"""
import json, hashlib
from pathlib import Path
BASE=Path('localization/editorial/r1')
INPUT=BASE/'corpus/snapshot-01/packets/packet-08.reader.md'
PACKET=BASE/'corpus/snapshot-01/packets/packet-08.json'
OUT=BASE/'audit/packet-08'
scenes=json.loads(PACKET.read_text(encoding='utf-8'))
byid={s['scene_id']:s for s in scenes}
findings=[]
def add(sid,ids,sev,cat,proposal,reason,refs=None,status='proposal'):
    s=byid[sid]; rows=[r for r in s['rows'] if r['review_row_id'] in ids]
    assert len(rows)==len(ids),(sid,ids)
    findings.append(dict(finding_id=f'P08-{len(findings)+1:03}',scene_id=sid,row_ids=ids,severity=sev,category=cat,source_quote='\n'.join(r['source'] for r in rows),current_quote='\n'.join(r['current_line'] or '' for r in rows),proposed_zh=proposal,reason=reason,evidence_level='直接文本与连续场景控制证据' if status=='proposal' else '文本疑点；用途或指代尚待外证',evidence_refs=[f"{s['logical_path']} / {s['root']}"]+[r['review_row_id'] for r in rows],reference_keys=refs or [],conditions_branch={'mode':s['mode'],'controls':s.get('controls',[])},status=status,apply_scope='scene_draft_only'))
add('SCec4640a9f4d3aa25',['CAT:O024daa3301d44fa213d0'],'B','voice','出去可得当心那股热浪！','送客时祝对方应付酷热顺利，现译“外面的酷热，祝你好运”话题悬空，不像商人自然道别。',['characters-support/Macsen'])
add('SCd01d5a6a1d077677',['SFW7d0e0bd69cec7fca2500391b','SFWbb67b2b36731c41900aa856f','SFWd4238c82798f14676f9097e0'],'B','continuity','既然你已经跟其中一只生物混熟了，这个给你！拿着这块水晶，再去陪陪它、摸摸它，说不定就能感到一股力量流遍全身……','完整玩法说明应持续指向前句已亲近的那一只；现译“那些生物中的一个变得非常亲近”“并且”有逐字拼接感。保留might，不保证获得力量。',['world-and-plot/I05'])
add('SCaf4aa1fa18c98fd1',['CAT:O452703500077e40a5c31'],'B','term','“物理”攻击？难道还有别的攻击方式？','Bossu刚讲物理攻击无效，主角是在追问这个术语；现译残留PHYSICAL使问答接点失真，不是专名保留。',['world-and-plot/D06'])
add('SCcb7d60767094d0c1',['CAT:O4afe981d246566c2effd','CAT:O6f14ef39f7b448387e02','CAT:Od206255a0d1795eb6fb3','CAT:Oc57b59cc5ed000d9e19d','CAT:O42b010a5ea248a4dbf37'],'B','idiom','Bossu：没错，探员。钻探者只会在划定的范围内活动。\nYiffany：……学院里那些男的要是也能这么守规矩就好了。\nBossu：嗯？\nYiffany：没什么，Bossu！伊法妮通话完毕。','boundaries由机器活动边界转为人际分寸；“更多家伙当时也那样”没有可辨的中文笑点，且guys性别信息消失。建议让“守规矩”承接边界，未补具体骚扰事件。Driller名称只是本段暂译，需术语统筹。',['characters-primary/Yiffany','characters-support/Bossu'])
add('SC3b0f76128c2a6465',['CAT:O488e7fcf58b490344c0e','CAT:O607a8907e8992d69601b','CAT:O8c92c6a7b0f0e6ca8268','CAT:Ob3d22a06579aa146b640'],'A','meaning','Bossu：记录上说，双足飞龙在高潮时容易分神，所以负责“挑逗”的探员要先绑牢，好让队友——\nYiffany：Bossu，我可是一个人行动，记得吗？','现译完整连读仍为“在高潮的高潮的那一刻，所以”，漏失prone to distraction；their comrades是探员队友，不是飞龙同伴。保留未说完的战术，不补队友具体行为，也不擅改原作“须绑牢”条件。',['characters-support/Bossu','characters-primary/Yiffany'])
add('SC4343a658dcedb661',['CAT:O5ecda2eb9350c47b127d','CAT:O03aa924e392fda642789','CAT:O6bc6c43354db66677484','CAT:O7bf5f36e031532b42e2d'],'A','meaning','Mauser：换作是我，打这种硬仗之前肯定先备足吃的！\nTomcat：那还不是因为你打架的本事不行！','would have在此为旁观者给失败外勤的反事实建议，不是Mauser承认自己忘带补给。现译“我本该”把当前失败责任移到总部人员身上；后句正拿他依赖食物的习惯开涮。',['characters-primary/Mauser'])
add('SC535618a487339cf5',['SFWbe1137413ef9a2dc511fb705','SFW7e539f158545313c23072b81'],'A','continuity','哦？倒是难得有陌生人打来。……我是说，执行任务的时候很少有啦 <3','that is收窄上句范围并带调情：不是不常有人搭话，只是在任务期间少。现译“毕竟”误成因果解释，抹去自我补充的笑点。',['characters-primary/Yiffany'])
add('SC41f714a207c66198',['CAT:O4fac43c5e49aa829b099','CAT:O776fa04ee70e5fc3f617'],'B','idiom','这才是我想听的实用情报嘛！该试试这招俯冲踢了。','more my speed指信息合胃口、是自己关心的方向；“信息才像我的路子”搭配生硬，削弱她从装备迷闲聊转回行动的落点。保留前面按键说明，不并入此提案。',['characters-primary/Yiffany'])
add('SC1667be893970acf7',['CAT:Oc9034154b3e2be274504','CAT:Of0dc4ee52debc9106ff1'],'B','idiom','嘿，偶尔玩玩小狗扮演，有什么不好，对吧？再当一回小狗玩玩嘛。','never hurt anyone在此为轻松辩护习语，不是陈述从未发生伤害；现译“玩一点……从来没伤过谁”明显英语腔。只重写她的辩护，不扩大为关系或年龄设定。',['characters-primary/Yiffany'])
add('SC959cea4cd47a5799',['CAT:Oa0f9368daed0e2f03aee','CAT:O975b195a8c93956ff1c4','CAT:O32c5af6d147404aca73b','CAT:O3f8da024a5a58e708cfa','CAT:O6c46a3463878c0ad785a','CAT:Ob6652c192efab5679ed3'],'B','continuity','Tomcat：你上回嘴里尝到这个，是什么时候？\nYiffany：宇宙学院，大二。19XX年的暑假。\nTomcat：什么？真的？你可从没跟我说过这——\nYiffany：那时候海滩边有辆超棒的塔可餐车。我几乎天天去！\nTomcat：哦，对，当然……听着……真香……！','Tomcat故意以食物说暧昧话，被餐车解释截断。现译“大口”“THA-”让问句和截话都不成立；保留食物表层与误会空间，不强加更露骨解释。',['characters-support/Tomcat','characters-primary/Yiffany'])
add('SCfd3a35d14d8646de',['CAT:O4c25f65c290e84e68628'],'B','voice','你这科博德闻着还挺讨人喜欢，嘿嘿。跟哪伙人坐船来的？','现译“身上这味道对科博德来说真够可爱”“一起飞”生硬；前半是按对方外观搭讪，后半问所属来访船员，不问飞行技能。未指定匿名商人姓名。',['characters-support/称呼矩阵'])
add('SC691b3a18b7909076',['CAT:O21b65772d7daa4dbb724','CAT:Oee5ac96f898f7023edfd','CAT:O9e08866d24a2a16e2274'],'B','continuity','Bossu：请把行动笔记再仔细通读一遍。\nYiffai：还好总有人认真做了功课。多谢，Bossu！','paying attention承接Bossu认真看行动笔记、纠正Mauser资料，不是“认真听着”外勤说话。保留年轻主角略带揶揄的感谢，不写成全员无能。',['characters-primary/Yiffai','characters-support/Bossu'])
add('SCb84957d4bbe46c64',['CAT:O211d32bcfc1ea166f9a9','CAT:O3ff7c6da1113e0f47ee0','CAT:O8ffba486b4343ce835c7','CAT:Oafa2c8f4181a40861975','CAT:O58d4ef1a57096949cd79','CAT:Oa34b63c37bc726ad5efe','CAT:Ob2d039e9b4aa38a03127'],'B','idiom','Bossu：确实。看来图托恩的矿坑，早就有人“埋雷占矿”了。\nYiffai：……？占矿我懂，可怎么还炸上了？\nBossu：我说的雷，就是会爆炸的地雷。\nYiffai：我知道是地雷！可为什么要埋在矿坑里——\nMauser：Bossu是说，以前的矿工在自家矿坑里埋了地雷，摆明了告诉别人：“这矿归我！”\nYiffai：什么……？！我躲开就是了，行吧？！伊、伊法伊通话完毕！','当前首句已经明说“布雷”，主角却继续不懂，Bossu再把mines译回矿区，问答倒转。中文以“埋雷占矿”与“这矿归我”的占有笑点重建解释链，使主角从问爆炸到问为何埋雷；不能照搬英语同形词。此为整段创译方向，仍需二审试读，不能原样自动回填。',['world-and-plot/英式用法、双关与语域'])
add('SCe3bb6029d395b6a3',['CAT:Oc2c225656c44ae19718c','CAT:O035264e976fac2b5f223'],'B','idiom','伊法伊，要想弄清这套衣服是干什么的，你得找个没Tomcat那么色的来问！','purr-verted是针对猫的perverted双关，不独立表示“那么喵”的性格属性。当前并列形容词破坏意思，宜先保住熟人挖苦；中文猫双关若不能自然建立，不强凑。',['characters-support/Tomcat'])
add('SC02a295fdd4ce3288',['CAT:O92f5dbaabaf35d253fc3','CAT:Od2fe21f56accd9875e53','CAT:Oc91c83e4cdc8b678f7ca'],'A','gameplay','使用门卡很简单：身上带着卡，直接走向能量门就行。门卡标的是它能开启的最高门禁等级！','up to level displayed on them指门卡可开到其标示等级的门。当前“等级不高于门上所标数字的门”成了门与自身等级比较，丢掉卡片上限，误导玩法。关联本包Keycard3 UI“至3级”可交叉佐证。',['world-and-plot/I04'])
add('SC9dff794087b1ab97',['CAT:O83e5a0026bd38da12dbf'],'B','term','适用于太空的|宇宙头盔。','“防太空”不是自然的防护属性表达；只说明头盔适合太空环境，不保证单戴即可太空行走。管线分隔保留，排版另验。',['world-and-plot/W20'])
add('SC2a2f11f81441cfdd',['SFW2223339b9c447c9f7766170b'],'B','term','适用于太空的|宇宙头盔。','SFW独立场景同样“防太空”生硬；单独保留ID，不把内容版本合并为同一审读实体。',['world-and-plot/W20'])
add('SC0288b8c93129d093',['CAT:O447468eceee608dd9609','CAT:O6bd12b697c1e93411d03','CAT:Oe16d597fcab7b5b5ff6b'],'A','idiom','哎哟，什么情况？你这大傻瓜想干嘛？还想再让我揍一顿吗？赶紧老实点，不然我……不然我……','kick your tail是揍对方/教训对方，不是“用我一尾巴踹过去”。现译凭空添了动作器官与施力方式。按镜头已切到对方反制后的反问，保留她嘴硬而未说完的威胁。',['characters-primary/Yiffany'])
add('SC0288b8c93129d093',['CAT:O6e0b31dcb3af29ab0668','CAT:O56161aa737ae923c6bfb','CAT:O3a2c55905c5e752ed7da'],'B','voice','[亲爱的“伊法妮”，正因为你没对我儿子下手，我才愿意陪你打闹这一场。来，稍稍见识一下我这样的超能力者有什么本领！]','同一人同一段从自然称呼突然切到“吾/汝”，没有英文对应古语证据；超能力/父亲身份不授权奇幻腔。保留方括号表示的演出层差别，不把narrator元数据当实际发言角色。',['world-and-plot/W16','characters-primary/Yiffany'])
add('SCb067f24e0154e7af',['CAT:Ob8680aeaf813c621bb4e'],'B','idiom','这场小小的交流一结束，他们就知道我这双爪子有多会伺候人了！','in good hands/paws指交给可靠能手，当前“落在了好爪上”只是字面对译，中文不成义。上下文主角自夸服务技巧，与被囚现实构成反讽；不把自夸提升成客观自愿。',['world-and-plot/E05'])
add('SC9a688dbe085a347d',['SFWe4874fffc9805a4f8fd2451a','SFW7a78facc8910b8483220a39f','SFW880bdbb3782319b3b878c8a3'],'B','term','Tomcat：哦，嘿！终于找到一把像样的驯兽电击枪了？\nBossu：要近距离研究当地生物，就得在战斗中用驯兽电击枪击败它们。','同场Trainer Tazer先“训练电击器”后“驯兽电击枪”，容易误认为两件装备；统一本场功能名，保持与Trainee新人武器区分。此提案两人台词中间仍有对话，应用不得跨说话人或控制事件合并。',['world-and-plot/I03'])
add('SC756e1e2f94e81d2c',['CAT:O16ef7c2719ad81fc827e'],'B','gameplay','Fenfen故事第5部分。|$在你脑中回响着：|$[心形与十字不相邻]','排序谜题线索中的touch可能指相邻，也可能有特定图形接触规则；“心不接触十字”不够明确。但未核谜题界面和判定，以上仅潜在玩法风险方向，不确认错译，不立即替换。',['world-and-plot/揭示门槛'],'needs_evidence')
# Coverage records preserve canonical identities and all alias metadata without modifying packet.
coverage=[]
for s in scenes:
    fs=[f['finding_id'] for f in findings if f['scene_id']==s['scene_id']]
    uncertain=any(f['status']=='needs_evidence' for f in findings if f['scene_id']==s['scene_id'])
    kind=s['kind']; rows=s['rows']; root=s['root']
    if kind=='code':
        result='inventory_only'; note='逐条读过代码常量；可能为资源键、着色器/库错误或诊断文本，未证玩家可见调用；不据ZH=null报漏译，不建议强翻。'
    elif kind=='image':
        result='inventory_only'; note='仅读到卡牌查看器及A键翻牌的文字转录；未查看原图、布局或重绘，ZH=null不判漏译。'
    elif any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in rows):
        result='needs_evidence'; note='已读任务日志嵌套文本；当前字段与占位内容按源保留，实际运行时用途/调用仍待核，未冒称实显验证。'
    elif fs:
        result='needs_evidence' if uncertain else 'issues_found'; note='已连读完整英文/条件/演出后对照当前归档整段；问题限关联短段，其余可成立表达保留；空白尾行按合句消费。'
    elif kind=='vsn':
        result='retain'; note='已核本场全部镜头、文本和音效/等待等控制；中文连读保留信息揭示、角色说辞/推测与施受；不据narrator自动定发言人，不改控制或已合句空行。'
    elif kind=='dialogue':
        result='retain'; note='已核本entry完整原文及控制，连读当前中文；问答/动作/否定基本成立，口语合法变体保留。形态称呼与性别、内容版本分轴，不把匿名*固定归人；合句尾行不作漏译。'
    else:
        result='retain'; note='已按字段组连读名称/说明/提示；现译主旨、数字、按键及占位符可成立，保留空白源与合法变体；未做字体、排版或实机验证。'
    coverage.append(dict(scene_id=s['scene_id'],read_status='read_full',row_ids=[r['review_row_id'] for r in rows],aliases=s.get('aliases',[]),context_checked=True,findings=fs,result=result,notes=f'{root}：{note}',scope_anchor=rows[0]['source'] if rows else 'control-only'))
OUT.mkdir(parents=True,exist_ok=True)
for name,items in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
    (OUT/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items),encoding='utf-8')
log=dict(input_path=INPUT.as_posix(),input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),packet_path=PACKET.as_posix(),packet_sha256=hashlib.sha256(PACKET.read_bytes()).hexdigest(),read_ranges=[[i,min(i+99,2494)] for i in range(1,2495,100)],truncated_ranges=[],references_read=['characters-primary.md','characters-support.md','world-and-plot.md'],references_read_ranges={'characters-primary.md':[[1,277],[278,377]],'characters-support.md':[[1,128]],'world-and-plot.md':[[1,150],[151,300],[301,406]]},reference_truncation_recovered={'characters-primary.md':[278,377]},read_status='read_full',reader_total_lines=2494,semantic_read_method='read工具每次<=100行连续读取，1–2494全部实际可见；程序仅提取ID/别名与输出，不替代语义通读',formal_application=False,runtime_verified=False)
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from collections import Counter
counts=Counter(f['severity'] for f in findings); results=Counter(c['result'] for c in coverage)
summary=f'''# packet-08 首轮粗校提案\n\n仅文档／待复审，不入正式译文或安装包，不是approved。\n\n## 阅读与覆盖\n\n- reader 2494行已以100行小段逐段read全部读完，无reader裁剪；三参考完整读取，primary参考初次输出裁剪已补读。实际SHA及区间见reading-log.json。\n- {len(scenes)}个canonical场景、{sum(len(s['rows']) for s in scenes)}条canonical row；每场收据保留全部row IDs及原packet alias元数据。未修改输入JSON。\n- {len(findings)}条提案／待核：A {counts['A']}、B {counts['B']}、C {counts['C']}；其中needs_evidence {sum(f['status']=='needs_evidence' for f in findings)}。覆盖结果：{dict(results)}。\n- code只作用途待核清单，image仅转录清单，嵌套日志用途继续待核；read_full只证明本reader已读，不代表玩家实显、全图或运行验证。\n\n## 优先精修\n\n1. 女线Wyvern战术：补回容易分神，修探员队友指代；保留被打断及单人行动反驳。\n2. 门卡2：重写等级上限说明；卡片等级不可写成门和自身等级比较。\n3. Werehund：修kick your tail动作误解；移除突兀吾/汝，不删角色反制与变形揭示。\n4. The0初次女线通话：that is是范围修正，不是毕竟的因果；保留调情再转技术的节奏。\n5. 地雷问答：当前首句先说破地雷，后文却装不懂；整段重建双关，P08-013只给方向，须二审试读，不机械逐行回填。\n6. Driller边界笑话、鱼肉塔可截话、in good paws、more my speed及purr-verted都需按中文对话功能重写。\n\n## 保留与新增证据\n\n- 本包女线小狗礼物、男线Starkill相认哨子段，长幼、赠予与飞船接应基本正确，保留；不把不同路线当同一次历险。\n- 假肉/假茶不确定保证、Bigbold装备合句、TazerAttuned修复前后分支、地图及按键提示多数可成立；没有把合句blank报成漏译。\n- Fenfen记忆由lang(Fox)讲述，属于有归属的回忆；不当全知事实。篇内议会/理事会等译名应在后续术语裁决中统筹，本轮不强做全局规则。\n- Werehund父子末段明确父亲相信主角是chosen one，并以“等再大些”结束儿子训练请求；不前灌身份、不追加年龄或关系。\n- 头盔“防太空”改为自然说明不代表单件具备整套气密能力。\n\n## 待核与边界\n\n- 排序线索touch的实际相邻规则尚未核界面／判定，P08-022为B级潜在风险、needs_evidence，不是确认错译。\n- 失真广播保留残片，未据上下文猜补完整命令。测试entry及占位报告不自动当正式剧情。\n- 未执行正式应用、dry-run节点回填、字体排版、图像核验、部署或实机游玩。当前四份记录与同目录生成脚本只供后续复审；不将覆盖收据当正确性的自动证明。\n'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
assert len({c['scene_id'] for c in coverage})==len(scenes)
assert sum(len(c['row_ids']) for c in coverage)==sum(len(s['rows']) for s in scenes)
assert all(set(c['row_ids'])=={r['review_row_id'] for r in byid[c['scene_id']]['rows']} for c in coverage)
print(json.dumps({'scenes':len(scenes),'canonical_rows':sum(len(s['rows']) for s in scenes),'findings':len(findings),'severity':dict(counts),'results':dict(results),'reader_sha256':log['input_sha256']},ensure_ascii=False))
