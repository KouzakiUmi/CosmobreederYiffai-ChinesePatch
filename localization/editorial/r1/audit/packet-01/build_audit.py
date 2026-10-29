import json, hashlib, re
from pathlib import Path
base=Path('localization/editorial/r1'); inp=base/'corpus/snapshot-01/packets/packet-01.json'; reader=inp.with_name('packet-01.reader.md'); out=base/'audit/packet-01'
scenes=json.loads(inp.read_text(encoding='utf-8')); lines=reader.read_text(encoding='utf-8').splitlines(); rows={r['review_row_id']:r for s in scenes for r in s['rows']}; smap={r['review_row_id']:s for s in scenes for r in s['rows']}
findings=[]
def add(a,b,sev,cat,proposal,reason,refs=[] ,status='proposal'):
 if sev=='Q':
  sev='A' if a in (668,900) else 'B'
  reason='Q待核；severity仅标潜在风险，并非确认错译。'+reason
 ids=[re.match(r'ROW (\S+) ',l).group(1) for l in lines[a-1:b] if l.startswith('ROW ')]; rs=[rows[i] for i in ids]; s=smap[ids[0]]
 f=dict(finding_id=f'P01-{len(findings)+1:03}',scene_id=s['scene_id'],row_ids=ids,severity=sev,category=cat,source_quote='\n'.join(r['source'] for r in rs),current_quote='\n'.join(r.get('current_line') or '' for r in rs),proposed_zh=proposal,reason=reason,evidence_refs=[s['logical_path']+' / '+s['root']]+[str(r.get('location'))+' / '+r['review_row_id']+' / '+(r.get('unit_id') or '') for r in rs],reference_keys=refs,status=status,apply_scope='scene_draft_only',branch_scope={'mode':s['mode'],'logical_path':s['logical_path'],'root':s['root']})
 findings.append(f)
add(136,137,'B','idiom','这石头是上回地震时砸到我头上的，可疼了！便宜点卖给你，要不要？','好价钱让给你不自然；整段是拿砸头的石头做买卖的笑话，宜接成商贩招徕，不增加石头功能。',['characters-support.Macsen'])
add(260,261,'B','idiom','你手里那根是手电筒，还是见到我就兴奋得翘起来了？开玩笑啦！你和那支手电筒可真是救星。','happy to see me是勃起双关，当前仅剩无落点的高兴问句；torch在本段接flashlight，不宜突然变火把。保留调侃后立即感谢。',['characters-support.Macsen'])
add(393,396,'B','continuity','Bossu：小心那些四处巡逻的带刺无人机。它们是真的打不坏！\n伊法妮：真的？你是说……只是夸张一下吧？因为我刚刚才干掉——','当前上句不使用字面/比喻表达，下句却突兀问字面意思；整段应建立真的打不坏—只是夸张吧—我刚打坏的递进。')
add(408,411,'B','continuity','Bossu：小心那些四处巡逻的带刺无人机。它们是真的打不坏！\n伊法妮：真的？你是说……只是夸张一下吧？因为我刚刚才干掉——','Zero为独立entry，同一语用问题单独留ID，不合并经历。')
add(430,433,'B','idiom','Mauser：哎呀，这下挨得可不轻……不如找家店，添点装备或回复道具吧！\nTomcat：碰上硬仗前，还可以多备些补给。','挨了重重一下、你甚至可以为硬仗囤好货机械且节奏不顺；这是败北后的具体补给建议，并非夸赞囤货能力。')
add(494,495,'B','idiom','既然我们给你备的装备不在手边，不如干脆四爪着地，自己挖？哈！','barring在此承接铲子和备用铲子都不在身边，不是设置除非带着装备的假条件；按对话落回犬类挖掘笑话。',['characters-support.Tomcat'])
add(591,591,'B','continuity','滚开，杂种狗！这些奴隶早让别的狗抢先占了！','先得手这些奴隶语法不成立；保留抢先占有含义，不猜具体动作或触发。')
add(610,618,'B','voice','Tomcat：嘿，姑娘，有消息要汇——\n伊法妮：汪？\nTomcat：不是吧——姑娘，你认真的？\n伊法妮：汪汪？\nTomcat：好吧，伊法妮，要是你的宠物替你接无线电时，你还能听见我……该干活了！\n伊法妮：……汪？\nTomcat：行吧，随你。等那丫头胡闹够了，希望她肯接电话……','come on是无奈抗议，不是求你；darn girl译该死的姑娘过重，且最后两行倒挂。保留误认宠物接听，不替其认出变身。',['characters-support.Tomcat'])
add(623,631,'B','voice','Tomcat：嘿，姑娘，有消息要汇——\n伊法妮：咕噜？\nTomcat：不是吧——姑娘，你认真的？\n伊法妮：咕叽？\nTomcat：好吧，伊法妮，要是你的宠物替你接无线电时，你还能听见我……该干活了！\n伊法妮：……咕叽？\nTomcat：行吧，随你。等那丫头胡闹够了，希望她肯接电话……','独立Slime分支；GOOP是该形态发声，不是说出黏糊这一形容词。其余同为无奈抗议和倒挂语序。',['characters-primary.变身边界','characters-support.Tomcat'])
add(660,664,'B','continuity','Tomcat：姑娘，你用的可不是普通无线电！\n伊法妮：怎么，锁定不了信号？\nTomcat：不是，信号没问题。而且它还装了先进传感器，能帮你完成任务！\n伊法妮：是啊。完成任务，应该能派上用场。','最后一句帮上把任务做完语法断裂；整段应接信号正常—传感器用途—主角简短回应。')
add(702,703,'B','meaning','嗯。这把在这个象限的哪个星系都过不了规格检查，不过应急还能用。','system在宇宙象限语境指星系，当前任何系统里过不了规格像软件兼容性；保留不合规格但能应急的对比。')
add(945,948,'B','gameplay','先把一只宠物的亲密度培养到最高，再回来领特别奖励。\n【另一条件分支】有了水晶，喜欢你的生物就能给你特殊加成！亲密度满了以后摸摸它，就能给水晶充能。','MAXXXED到顶和MAX亲密度残留英文且对象不清，玩家指令应直接说明任一宠物满亲密度。两条件分支不可串成一次对话。')
add(1035,1044,'B','idiom','伊法伊：那我就能去找那帮混——\nBossu：先等等，小狗崽。飞船虽然勉强能开，但只能贴地飞行。不能冒险让你再次被击落，甚至更糟。\n伊法伊：不是吧——！真不行？\nMauser：现在能行动的特工只有你，可不能冒这种险！\nTomcat：对啊，小狗崽，拿出点大人的样子，先把裤子穿好，稳着点来。……哦，忘了，你把裤子弄丢了。\n伊法伊：好好好！我会更讲究点战、战策的。\nBossu：这就对了。别忘了，我们都会帮你。','BAST是被截断粗口，不是专名；big boy pants是成熟行事的习语，又被下句丢裤子字面化，当前大号短裤只剩尺寸。保留双层笑点；STRATEGIMICAL为滑稽造词，建议局部磕绊而不设固定口癖。',['characters-primary.Yiffai','characters-support.Tomcat','characters-support.Bossu'])
add(1112,1115,'B','continuity','伊法伊：……说得好像那套装备、那艘补给齐全的飞船都还在我手里似的……\nTomcat：既然我们给你备的装备不在手边，不如干脆四爪着地，自己挖？哈！\n伊法伊：那、那你这么一说……','主角totally have是反话，当前肯定句落点生硬；Tomcat接丢装备现状建议犬形挖掘，不是除非有装备才四肢着地。',['characters-primary.Yiffai'])
add(1124,1128,'A','meaning','Bossu：这片区域里似乎还有一名特工，而且一直在四处活动，没有受到限制。\n伊法伊：还有一名特工……\nMauser：我们还在试着联系对方，可是……嗯……现在看来，对方已经关掉无线电了。','另一名是单人未定性别的they，译成他们连续造成多人判断。保留身份未明和受困/自由活动的对比，不提前确认姐姐。',['characters-support.Starkill','characters-primary.揭示边界'])
add(1222,1225,'B','idiom','你好，伊法伊。你不认识我，不过我偷偷探过你的卫星链路。其实我已经观察你一阵子了，想跟你做笔交易：把你在外面找到的那些好芯片带来，我就替你破解门禁！这不是两全其美嘛！','有点偷看链路、黑开门不自然；重写完整自我介绍和交换条件，但Test条目身份不据共用黑客话术强认The0。',['characters-support.The0.归属限度'])
add(1293,1294,'B','continuity','卫星一直在把你的近场数据传回总部。','两行当前拼成源源不断地传来你的近场数据持续传回总部，谓语重复错接；按连续信息合成完整句。')
add(1304,1308,'B','voice','Tomcat：看这读数，你在那边可兴奋起来了啊。怎么，终于找到驯兽电击枪了？\n伊法伊：你、你怎么知道……\nTomcat：能让你这小狗崽把/这种/体征数据传回指挥中心的，还能有什么？','上面兴奋、像/这样/的指标送到指挥中心逐字且不成句；体征监控是调侃依据，不补具体生理数值。',['characters-support.Tomcat'])
add(1315,1317,'B','voice','Tomcat：先缓一分钟，等你的“兴奋”消下去再走吧，小狗崽。可别吓着当地那些家伙。\n伊法伊：我、不知道你在说什么……','当地的那些悬空，Pup残留破坏熟人逗弄；保留兴奋下去双关和急辩，不另加羞辱。')
add(1322,1333,'A','meaning','伊法伊：我……刚帮一个小家伙逃出牢房，可他一碰我的手，我就……\nTomcat：光碰一下手就让你生命体征飙升？那得是什么极品猛男才——\n伊法伊：不是！根本不是那回事！对方把……不知道怎么就把图像直接传进了我脑子里！就像我亲身经历了对方经历过的一切。\nMauser：是真的，Tomcat。P.A.W.还录下了伊法伊经历的全过程。\nTomcat：哇，真够离奇的……\n伊法伊：我感觉自己只听到了对方故事的一小段。不过，要是再找到别的被囚禁的当地人……','同一被救者先他后他们，误变多人；all they did在记忆情境是所经历而非做过的一切。用对方保持指代不猜物种/身份。',['characters-support.Anon/Fox/Fenfen'])
add(1450,1456,'A','relationship','Tomcat：哦，鱼肉塔可！那些挥爪挺会吃啊！你好久没尝过这种滋味了吧？\n伊法伊：哦，呃……大概吧……？\nTomcat：是不是更盼着再见到你姐姐了？\n伊法伊：我不太懂你在说什……你……等等……\nTomcat：呵，我不会告诉别人你体温升高的！\n伊法伊：谢、谢谢……哼……','sis在男线已确认是姐姐，不是你姐妹；I am not sure I know what为没听懂对方暗示，当前我知道什么把问答拆坏。保留荤话暗示但不替人物认定亲密经历。',['characters-primary.Yiffai.关系边界'])
add(1488,1496,'B','voice','伊法伊：太——棒了！\nTomcat：嚯，好大一块肉！\n伊法伊：好——大——！\nTomcat：能往嘴里塞的大肉块，你还真喜欢啊？\n伊法伊：大得不得了——！\nTomcat：会不会让你想起嘴里的别的东西，比如——\n伊法伊：汁水真——足——！\nTomcat：呃，算了。我还是让你俩单独待一会儿吧……','当前好啊啊大啊啊、巨啊啊和重复汁机械拉长单字，欢呼与食物描述均不成中文，LI-也不应当作未译专名。整段让Tomcat试着开荤玩笑，却被专心吃肉的回应打断。',['characters-primary.Yiffai','characters-support.Tomcat'])
add(1507,1512,'B','gameplay','伊法伊：嘿，那颗球就浮在眼前嘛！这股力量好像……能让我更耐打？不过也有代价：打起敌人来，伤害反而会变小？\nTomcat：老天保佑，这方面看来还是你懂得多。总之，小家伙，千万小心……\n伊法伊：我会尽量小心。伊法伊通话结束。','更硬可能偏成性双关而模糊防御增强；原段解释耐打/输出下降的权衡，无数据确认仍保留主角疑问语气。')
add(1920,1921,'B','continuity','说真的，我好久没跟人上床了，上次还是来这颗星球之前呢。所以，来场小群交，我可求之不得。','甚至在下到这颗星球之前是悬空时间状语；连上上一句有段日子没做爱，才能清楚解释为何愿意留下。')
add(1944,1947,'B','continuity','你猜怎么着！刚走没多久，又碰见当地人了！个子小、耳朵大……我心想，这肯定就是酒保说的那种Fenfen了！他还说有机会就帮帮他们，这不，正好碰上一个！','这肯定就是Fenfen的家伙语法不成立；连续回忆应连起外貌—此前听说—决定帮助，且只保留当时误判，后段机械眼揭示不能提前说破。')
add(1956,1959,'B','continuity','反正，我就这么被困在牢房里，让这群机械色魔没日没夜地操……我以前还真没想过，天天被好鸡巴伺候也会腻。可现在，我是真腻了！','也会腻可偏偏就腻了少断句且转折撞接；连接被困遭遇与过量后厌倦，保留原先喜欢、后来受够的反差。')
add(1998,2000,'B','idiom','凡是没能藏进旧日家园阴影里的Fenfen，都被抓去当了奴隶，任那些新征服者差遣。我们从前那种平静、简朴的生活，就这样一去不返了……','modest life是简朴生活，不是生活谦逊；家本身不是阴影，整句应说家园阴暗处藏身。保留Fox的经历叙述，不升级全知。',['characters-support.Anon/Fox/Fenfen'])
add(2042,2043,'B','voice','不，从那一刻起，那位旅者便听命于一股更黑暗的力量……特蕾让做什么，就只能照做！','其便在中文口头记忆讲述中明显生硬，且隐去人的被支配状态；用旅者承接前段，不猜性别或身份。',['characters-support.Anon/Fox/Fenfen'])
add(2162,2163,'B','voice','真有你的，姑娘！你和你那小狗崽弟弟，把下面的坏蛋收拾得够彻底！不过出了名也别得意得把我们这些总部同事忘了啊？','grrrrl是Tomcat拖音称呼，不是人名；当前英文残留令祝贺对话突然中断。熟人玩笑但不加固定喵口癖。',['characters-support.Tomcat'])
add(2174,2180,'B','continuity','图托恩星球的报告到此结束。这颗历经动荡的星球，曾面临有史以来最严峻的挑战，最终由两位勇敢的宇宙育种者奋力拯救：姐姐伊法妮·伊法伊，经验丰富、战技卓绝；弟弟伊法伊·伊法伊，天赋出众、热情不竭。两人携手，就没有应付不了的任务。PPP以拥有这两位特工为荣。——Bossu署名','当前报告被两位…拯救悬挂被动句，姐姐/老兵/技巧名词堆叠；整段是Bossu署名总结，需按中文报告连贯收束，保留原文夸赞而不拿夸赞证明精确履历。',['characters-primary.关系边界','characters-support.Bossu'])
add(2467,2469,'B','continuity','哎呀，不过你根本听不懂我在说什么，对吧？你这么可爱的小家伙，只想四处跑跑跳跳……就该让你自由自在地玩才对！','当前前句已将just wants改成就该，后句又重复应该；恢复想做—理应获准的递进。独立SFW场景，不从NSFW补年龄或回忆。')
# 待核不据残片猜补完整台词
add(1098,1102,'Q','source_uncertainty','待核：先确定可识别残片与BIG TEN笑点的中文呈现；不补全失真通信。','信号残片多数保留英文，末尾BIG TEN又为角色复述；不能按后续剧情猜成完整信息。需整段失真字幕方案和源文确认。',status='needs_evidence')
add(668,670,'Q','source_uncertainty','待核：确认them指门卡还是能量门及实际等级规则后，再定“可开启不高于门卡所标等级的门”等表述。','up to the level displayed on them指代可疑；当前门上所标数字的门无法明确门卡上限。仅记原文/玩法待核，不擅改规则。',status='needs_evidence')
add(715,720,'Q','source_uncertainty','待核：核实SENSOR DARK的源文原意及物件身份后，再决定球体修饰语；暂不据条目名补写能力。','SENSOR DARK FLOATING ORB语法异常，当前硬解释成传感球可能把残错当科技设定。必须查源文或演出/物件证据，不能仅凭其他球体描述推定。',status='needs_evidence')
add(900,901,'Q','source_uncertainty','待核：确认MAGs在该店出售物/宇航服话题中的指称，核实后再定“弹匣”或其他物品名。','宇航服话题后接备用MAGs，不能仅凭缩写判弹匣。需商店库存或道具定义证据；当前译文可能改变物品类别，暂不自动改。',status='needs_evidence')
add(182,182,'B','term','回见啦，姑娘！小心那些吠犬！','本包ui.breeding.Barker明确为吠犬，复数Barkers在犬形告别中指同类命名；吠叫者令同一名称无对应。仅本语境提案，不作全局词替换。',['packet-01.SCad31e69491c94088.CAT:O2464b1af8ebfc21c4d38'])
for f in findings:
 root=f['branch_scope']['root']
 for key,term in [('world-and-plot.W06','EndingGood'),('world-and-plot.H03','f_AgentFZ2'),('world-and-plot.H06','f_AgentFZ5'),('world-and-plot.I07','ZenerTriangle'),('world-and-plot.I05','MacsenDark.Hello'),('world-and-plot.D07','ClassicSpikeball')]:
  if term in root: f['reference_keys'].append(key)
for name,data in [('findings.jsonl',findings)]:
 (out/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),encoding='utf-8')
cov=[]
for s in scenes:
 fs=[f['finding_id'] for f in findings if f['scene_id']==s['scene_id']]; kind=s['kind']; result='issues_found' if fs else 'retain'; note='已连读原文、当前归档与本entry控制；保留原有语义和分支，不对通顺句作同义润色。'
 if kind=='code': result='inventory_only'; note='已读全部字符串；用途未证实，仅inventory，不以空current判漏译。'
 elif kind=='image': result='inventory_only'; note='仅文字转录范围，未核图像实显。'
 elif any(f['status']=='needs_evidence' for f in findings if f['scene_id']==s['scene_id']): result='needs_evidence'; note='失真源文或玩法指代待核，未补剧情与触发。'
 elif 'scripts_pack' in s['logical_path']: note='已读本嵌套字段；文字暂保留，运行时用途未核，未冒称玩家实显已验证。'
 elif kind=='ui': note='已连读本键全部值；保留数值、占位、换行和专名边界；未做界面/排版验证。'
 elif kind=='vsn': note='已读完整演出及换镜/语言控制；narrator仅索引，按text/lang和场景说话动作理解；无跨镜合句应用。'
 if not fs:
  retain_notes={'TomcatItems.SpecialWhistle':'父亲旧哨子—姐姐归还—首次任务承诺—呼叫接应的先后与亲情落点成立，保留；不猜运行时吹哨范围。','Mauser.Area0_map03_b noselect':'地震后问安—报告塌方—提醒传送出口—决定上地表，问答与行动承接成立；合句尾行非漏译。','BossuDex.ClassicMineWall':'诡雷与矿脉推测—远离或远程引爆—确认收到，风险建议明确，保留perhaps而不认证设雷者。','TomcatItems.StatFortune':'饼干/奶油蛋糕口感误判转舔咬调情，双方接话成立；不凭键名补幸运数值。','TomcatItems.ElfHead':'防御性能嘴硬—超级可爱反击—哼声，人物节奏成立，不强改。','TomcatItems.StatCream':'奶油美味—非乳来源—蜥蜴产奶被截话—安排课程，保留误解与遮掩，不提前补说明。','vsn/m_ClassicEnelye/script.vsn':'赞赏战斗—许诺奖励—男主抗议裙装，保留SFW本身换镜与抗议，不移入成人版动作。','vsn/m_AgentM02/script.vsn':'Top自夸、失手后圆场、别人高潮自己例外及末尾再遇的嘴硬反差保留；不当军衔或客观胜利。','vsn/m_ClassicWerepup/script.vsn':'成人主角训练回忆与当下对小狗说话分开；挖卡由小狗赠主角，未倒置施受。','vsn/m_EndingBad/script.vsn':'追击失败来自船未修齐，结尾只是希望银河安全，不改成保证；不与Good顺接。'}
  if s['root'] in retain_notes: note+=' '+retain_notes[s['root']]
 note+=' 独立审读实体：'+s['mode']+' / '+s['root']+'。'
 cov.append(dict(scene_id=s['scene_id'],read_status='read_full',row_ids=[r['review_row_id'] for r in s['rows']],context_checked=kind!='code',findings=fs,result=result,notes=note,mode=s['mode'],logical_path=s['logical_path'],root=s['root']))
(out/'coverage.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in cov),encoding='utf-8')
log=dict(packet='packet-01',status='read_full',input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [inp,reader]},actual_read_ranges=[[1,100]]+[[a,min(a+149,2350)] for a in range(101,2351,150)]+[[2351,2450],[2451,2510]],reader_output_capped=False,reference_read={'LOCALIZATION_BRIEF.md':'1-65','WORK_ORDERS.md':'1-48','characters-primary.md':'1-277 (initial output capped); supplemented 278-377','characters-support.md':'1-128','world-and-plot.md':'1-150,151-300,301-406; full, no truncation; final proposals rechecked against W06/W09/W17/H03/H06/E01/E02/R05/I05/I07'},scene_count=len(scenes),row_count=sum(len(s['rows']) for s in scenes),findings_count=len(findings),semantic_method='实际小段read完整reader后，按连续场景和参考复核；程序仅关联稳定ID、原当前引文、收据和哈希。ledger未用作当前问题依据。',unverified=['运行时触发顺序','实机/UI/字体排版','code字符串玩家可见用途','正式应用与独立复审'])
log['input_path']=reader.as_posix()
log['input_hashes']=log['input_sha256']
log['input_sha256']=hashlib.sha256(reader.read_bytes()).hexdigest()
log['read_ranges']=log['actual_read_ranges']
log['truncated_ranges']=[]
log['references_read']=log['reference_read']
log['findings_status_counts']={k:sum(f['status']==k for f in findings) for k in ['proposal','needs_evidence']}
log['world_reference_recheck']='completed; no factual conflict requiring withdrawal; Q remains unresolved by world reference'
(out/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'scenes':len(cov),'rows':log['row_count'],'findings':len(findings),'severity':{k:sum(f['severity']==k for f in findings) for k in ['A','B','C','Q']}},ensure_ascii=False))
assert len({s['scene_id'] for s in cov})==len(scenes)
assert all(f['row_ids'] and all(smap[r]['scene_id']==f['scene_id'] for r in f['row_ids']) for f in findings)
