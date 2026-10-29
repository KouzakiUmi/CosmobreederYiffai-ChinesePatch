import json, hashlib
from pathlib import Path
base=Path('localization/editorial/r1')
p=base/'corpus/snapshot-01/packets/packet-07.json'
scenes=json.loads(p.read_text(encoding='utf-8'))
out=base/'audit/packet-07'
findings=[]
def add(scene, lines, zh, reason, severity='B', category='idiom', refs=None, status='proposal'):
 s=next(s for s in scenes if s['scene_id']==scene)
 rows=[r for r in s['rows'] if (r.get('line') in lines if isinstance(lines,list) else r['review_row_id']==lines)]
 assert rows,(scene,lines)
 findings.append(dict(finding_id=f'P07-{len(findings)+1:03}',scene_id=scene,row_ids=[r['review_row_id'] for r in rows],severity=severity,category=category,source_quote='\n'.join(r['source'] for r in rows),current_quote='\n'.join(r.get('current_line') or '' for r in rows),proposed_zh=zh,reason=reason,evidence_refs=[s['logical_path']+' / '+s['root']]+[r['unit_id']+' / '+r.get('location','') for r in rows],reference_keys=refs or [],status=status,apply_scope='scene_draft_only',branch={'mode':s['mode'],'path':s['logical_path'],'controls':s['controls']}))
add('SC23766530c1074c47',[1648,1649,1650],'外面等着救的特工可真不少啊？等你多救几个回来，我就给你点好东西……嘿嘿嘿！','somethin somethin是故作神秘的好处，不是“那个那个”；“一大批他们”使招徕整段失去自然口气。')
add('SC5737f92fda658079',[2005,2006],'谢谢！不过还得追上他，采点生物数据。他可比我想的有劲儿多了。','SPUNK残留使后句接不上；此处战后先说对手活力，Bossu再接正式采集时但愿如此的双关，不宜提前单义化成精液。',category='continuity',refs=['W11'])
add('SC5737f92fda658079',[2014],'哈哈，那当然！通话结束。','over and out不能逐词作“完毕并结束”，应保留无线电收线功能。',category='voice')
add('SC78ced646a25915e8',[3173,3174,3175,3176,3177],'波苏，是这些炮变强了，还是我变弱了？\n这些炮似乎有阵子没受损到需要自我修复了，所以能以更高功率开火。\n真——好，又多一桩麻烦……','开头问的是眼前这些炮，译成“是有更强的加农炮”改变比较对象；尾句反讽不可僵硬作“正好是我需要应付的”。',category='continuity')
add('SC8bbefad7d6e7d322',[2253,2254,2255,2256],'我……我应该还好。刚才的情况，你们听见了吗？\n听见什么？你生命体征都乱了，无线电又怎么也呼不通，可把我吓得够呛！','catch与catch a case of the willies构成接词；“接收到一阵发毛”不是中文感受表达。按关切与前问重写，不改生命体征异常事实。',category='continuity')
add('SCba33d0aea1ed874d',[2610,2611],'哦？难得有陌生人打给我呢。\n……我是说，执行任务的时候。<3','that is是收窄前句范围的俏皮补充，不是“毕竟”因果；当前稿删掉了任务外陌生来电的调情暗示。',severity='A',category='meaning')
add('SC71bccdad94bc42b7',[2465,2466],'你那支手电筒挺不错啊？\n要是波苏，就该叫它“照明电筒”了。','torch是英式手电用法，不是火把；提案用同物异称承接吐槽，不改设备种类。精校还可试更贴合称呼的中文变体。',severity='A',category='term',refs=['I05'])
add('SCf8e6890f7b25c51e',[4037,4038,4039,4040],'汤姆猫，收到请回答。\n他们说我无论如何都不能丢钥匙，该不会是认——\n——认真的。没错，任何情况下都不能丢。报告你看过，原因你也知道！','当前“告诉我他们不是认真的，当他们说我-”倒挂英文语序，接话也悬空。需按中文重做截话落点；两位发话者不能合并。',category='continuity')
add('SC31281e1f7d7bb273',[4181],'这顶帽子一戴，气势就出来了，是不是？','make a statement指造型鲜明有气势，不是“说明问题”；后续海盗角色扮演从造型引发。')
add('SCc208e23b19701617',[4067],'这顶帽子一戴，气势就出来了，是不是？','SFW独立场景同样是造型气势，保留之后索财而非成人幻想的不同走向。')
add('SC546e06cb0db8f471',[3942,3943,3944],'可别为这点零食纠结得像它一样打了结！\n矮人为什么会有这东西，我也不清楚……不过说不定，他们就是靠它才那么壮！','twisted up in a knot既是焦躁习语又照应椒盐卷外形，当前只说身体扭结；整段改成口语冷笑话与不确定效果说明。')
add('SCd26ac691afa4c235',[676],'我……我想接下来自己就能应付了。要是换成*你*来，我、我也吃得消！<3','take it from you在成人语境接性承受暗示，不能“从你那儿接手”。不擅定具体姿势或器官。',category='meaning')
add('SC9a50ee5c19b72be6',[3216,3217,3218,3219],'这……哇……\n先别光顾着惊叹。保持警惕，才能挡住那些年轻精灵的攻击。\n对，得集中精神。','“别向敬畏屈服”僵硬误置语用，指挥端是在叫他别被设定惊住而分心，并非与敬畏战斗。',category='voice',refs=['D04'])
add('SC5c5f5477be1d2b03',[3205,3206],'嗯，你说是灵能造成的？\n看来只能自己想办法了……','“嗯，精神，你是说”英语倒装残留，且无法接上刚讲的灵能幻象。',category='continuity',refs=['D06'])
add('SC82f75109d82edca1',[3597,3598,3599,3600,3601],'伊法伊，你真没事吧？\n你说听见有声音叫你“按 SELECT 循环切换超能力，再按 UP+ATTACK 发动”，我还以为你没法继续执行任务了！','out for the mission在关切精神异常语境指无法继续任务，当前“以为你出任务去了”与开头担心相反；保留按键教学。',severity='A',category='meaning',refs=['I06'])
add('SC290cf7270ee68e5f',[4302,4303,4304],'使用门卡很简单：带着它走向能量门就行。门卡上标着等级，等级不超过它的门都能打开！','当前译成“等级不高于门上所标数字的门”比较对象循环，丢失卡等级控制可开门范围；同包门卡2说明佐证。',severity='A',category='gameplay')
add('SC635c7bb3776a92f5','CAT:Ob43a7364be8223b23d1c','硬脆打结的|面包','PRETZEL与HARD KNOTTED表明BRED极可能为BREAD拼误，不是繁殖动词。建议供复核，须先确认源拼误口径；不能按“培育而成”交付。',severity='A',category='source_uncertainty',status='needs_evidence')
add('SCec282ed3f0097e07','CAT:O863e8be60e21ccc27300','科博德蜷在你身边，|惬意地享受你的陪伴。|真是个好宠物！','basking in your presence指享受陪伴，“沐浴在你的存在里”是直译腔；保留亲和等级状态，不添加永久关系。')
add('SC1c6bb8c065b63e86','CAT:O200bab53d25e977893d4','打败小狼崽之后，|回忆涌上心头，又迟疑起来。','当前状语倒挂成“回味着，又犹豫着在……之后”，读不成完整中文。保留追忆与迟疑，不从别包补具体成人行动。',category='continuity')
add('SC27cc2aa84f61748c','CAT:Off797ac2172f2048be26','强势的上位猫特工，|迎战来犯之敌！','当前“一只凶的上位猫去”结构生硬；保留top角色自夸及aggressors来犯，不升级军衔。',category='voice',refs=['R05'])
add('SCf1c781ff2a344ed4','CAT:Oedce2833d606527862d5','穿久了更合身，|还能接着穿','broken in指穿软穿顺，不是“穿开”；并非破损不能穿。')
add('SC23fcdb3817e041e0',[37,38,39],'她年纪虽轻，却天赋出众，总能找到别人想不到的办法。大家都觉得，超能力者特蕾加入议会再合适不过，因此很快就准许她接触我们Fenfen储存的力量。','“天赋远超其年纪”“所遗漏之解法”“力量贮藏”连续名词化不自然；保留曾被信任的过去视角，不提前将其写成阴谋已被察觉。',category='continuity',refs=['H02'])
add('SC9e9ceda84c287300',[28,29,30,31],'各式各样的超能力，都成了战争武器：爆裂的灵能弹轰退敌人，猛烈的念动力一波波挡住大军。有些人甚至改变自己的身体，直接投入战斗。','“能力武库被征用为战争的武器”重复抽象名词、施事模糊。整段保持技术描述与不同能力清单，不转成奇幻咒术。',category='continuity',refs=['H04'])
add('SCa2fb98b0f0ceefb5',[17,18],'这名受控的特工将议会剩下的成员逐个抓走，囚禁特蕾的力量也因此一天天减弱。','agent在本场延续前章闯入者及后续Starkill受控脉络；“被扭曲的代理人”在中文成抽象委托人，削弱身份与因果。保留Fox有界叙述。',category='term',refs=['H07'])
add('SC960d377d64349226',[53],'——总之！他到处乱抓，我只好使尽浑身解数，想把他打退——呃，撸退！','beat him off兼击退/手淫，现稿“撸退”无中文落点；用自我纠正兼顾其辩解和露馅，不把同伴最初挣扎变自愿。',category='idiom',refs=['R02'])
add('SC3c96e35204cd3dcc',[64,65],'真该让你看看他那时的眼神！俺双腿往他身上一缠，就把他夹在俺尾巴和牢房栏杆之间。哈！','现稿“看看……眼神，把他夹在……”主语衔接错位；按先邀听者想象、再叙自己动作重写。',category='continuity',refs=['R07'])
add('SC230a3742479654b5',[3243,3244,3245,3246,3247],'波苏，是这些炮变强了，还是我变弱了？\n这些炮似乎有阵子没受损到需要自我修复了，所以能以更高功率开火。\n真——好，又多一桩麻烦……','男线独立记录：问眼前这些炮的强弱，而非是否存在更强的炮；尾句为反讽。与女线相同字面不合并人物经历。',category='continuity')
# Q不猜补失真广播或含混宾语。
add('SC30945afec706cce8',[2513,2514,2515,2516],None,'SAVE IT宾语与失真残片不足以判明；当前“救它”暂不凭后文替换成救人/救星球。请核音画与触发后再定整段，保留主角被打断和对方求援。',category='source_uncertainty',status='needs_evidence')
notes={
'SC8559b2a4c2d88fb3':'已对读Erma与Daleir两份报告：前者相信搭档指导、反抗后才后知后觉；后者的诱导嫌疑属口误与自述，不替她洗成客观双方自愿。现稿主体叙述与揭示顺序成立，单复数they随语境不机械报错。',
'SC960d377d64349226':'与F05对读；自我辩解、get off改口、tricking露馅以及怀孕暗示保留，不能把narrator元数据等同全知叙述。局部双关另提案。',
'SC14401ed419ed1e23':'SFW独立完整演出：主角自夸→父亲变形反制→主角负伤离开→父子评英雄。保留无成人段版本，不补NSFW内容；说话人根据来回与Dad/my son判断，不机械narrator。',
'SC0f1be81dd740b331':'男线开场已知失踪姐姐；首次飞行不等于没训练。攻击、迫降、船损、换潜行服、盗装备与追踪顺序均保留。后轨道推进器语义技术用途仍待专项核定，不无证改型号。',
'SC7979a606b9be0aad':'女线弟弟定位已揭示阶段；Mauser炫计算被催才报地点、Tomcat调侃、Bossu转回行动的节拍保留。空行系合句消费，不报漏译。',
'SC862403c68f1d4607':'两种拆雷都让其爆炸的冷笑话与踩雷双关、冷场挂断成立；ACTUAL_HINTS下划线源已有，不擅认脚本损坏。',
'SC2314258606729cd4':'SFW女线另一地雷entry保留自身收尾，不与墙雷或男线合并；实际提示与玩笑都通顺。',
'SC1bfee9d188c714cf':'男线拆雷冷笑话→假装信号差退场，与女线不同，当前语义口吻成立。',
'SC7eb3c574023e5012':'脚环操作完整，姐姐两周练习为弟弟回忆；与姐姐没认真练的说辞形成嘴硬反差，不改成客观设定矛盾。',
'SCbaa7f66957029a4f':'男线误吃维生素、Top双关、主动期待尺寸变大、被告知蛋白补充剂，笑点及成人人物边界保留，不以pup推未成年。',
'SC88df48b156a94b0d':'USL技术全称、设备可运行、生物影响违法与绝密任务自决保留；pa(w)wing中文转爪子活合法，不凑双关问题。',
'SC86a162ee3099dd1b':'逐缺件else-if核南部炮/深洞护盾/精灵雷达/地震露出涡轮，及齐件安装与未胜时付费口径；未当成全图可达攻略。',
}
for f in findings:
 notes.setdefault(f['scene_id'],'已按本场原文、控制及当前中文连读；发现列有完整相关短段提案，其余语义成立的表达保留，不因合句空行报漏译。')
coverage=[]
for s in scenes:
 fs=[f['finding_id'] for f in findings if f['scene_id']==s['scene_id']]
 kind=s['kind']
 unverified=any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in s['rows'])
 result='issues_found' if fs else 'retain'
 note=notes.get(s['scene_id'])
 if kind=='code': result='needs_evidence';note='已逐项读源字符串；玩家可见用途未证实，仅登记库存，null不当漏译，不提自动翻译。'
 elif kind=='image': result='inventory_only';note='只读包内五条转录：手柄推荐、L+R、Q+E、配置入口与成人限定；未看图、未OCR、未重绘，不声称图像已校。'
 elif unverified: result='needs_evidence';note='已读nested JSON当前文本及数字/坐标/占位结构，仅静态文本收据；运行时用途与界面实显未核，不冒称已实机校验。'
 elif not note:
  if kind=='ui':note='已连读本键完整源文及当前值；名称/说明或状态分支语义成立，数值、分隔符与合法留白保留。未核屏幕排版。'
  else:note='已读本entry全部英语/控制再连读当前中文；本场问答、动作对象及语气可成立，保留合法译法；匿名发言仅按entry局部理解，不凭星号认角色。'
 coverage.append(dict(scene_id=s['scene_id'],read_status='read_full',row_ids=[r['review_row_id'] for r in s['rows']],context_checked=kind not in ['code','image'],findings=fs,result=result,notes=note,mode=s['mode'],root=s['root'],aliases=s.get('aliases',[])))
def dump(name,vals):
 (out/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in vals),encoding='utf-8')
dump('findings.jsonl',findings);dump('coverage.jsonl',coverage)
ranges=[[1,100]]+[[a,min(a+149,2409)] for a in range(101,2351,150)]+[[2351,2409]]
log=dict(packet='packet-07',input_path=str(p.parent/'packet-07.reader.md'),input_sha256=hashlib.sha256((p.parent/'packet-07.reader.md').read_bytes()).hexdigest(),packet_json_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),read_ranges=ranges,truncated_ranges=[],references_read=['LOCALIZATION_BRIEF.md','WORK_ORDERS.md','reference/characters-primary.md','reference/characters-support.md','reference/world-and-plot.md'],reader_sha256=hashlib.sha256((p.parent/'packet-07.reader.md').read_bytes()).hexdigest(),read_status='read_full',actual_read_ranges=ranges,reader_lines=2409,reader_clipped=False,reference_reads={'LOCALIZATION_BRIEF.md':[1,65],'WORK_ORDERS.md':[1,48],'characters-primary.md':[[1,277],[278,377]],'characters-support.md':[1,128],'world-and-plot.md':[[1,150],[151,300],[301,406]]},reference_clipping={'characters-primary.md':'初次默认read裁剪于277；已补读278–377','world-and-plot.md':'首次不存在，完成后已补读1–406'},method='全包以read每段不超过150行依序实际通读；脚本仅整理已判断发现、抽取精确引文/ID与覆盖库存，不代替语义阅读。',not_done=['正式译文应用','逐实际节点回填映射','独立二审','code用途运行核验','图像视觉/OCR/重绘','UI排版及实机验证'],counts={'scenes':len(scenes),'rows':sum(len(s['rows']) for s in scenes),'findings':len(findings)})
(out/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
from collections import Counter
counts=Counter(f['severity'] for f in findings); statuses=Counter(c['result'] for c in coverage)
(out/'summary.md').write_text(f'''# packet-07 首轮粗校提案

已以小段 read 完整通读 reader 1–2409，共{len(scenes)}场、{sum(len(s['rows']) for s in scenes)}个主审行；逐场留覆盖收据，未以扫描冒充阅读。JSON别名保存在收据，不把平行分支拼成同次经历。

## 结果

- 发现{len(findings)}项：A {counts['A']}，B {counts['B']}；均为待复审提案/待证据，不是 approved。
- 覆盖结果：{dict(statuses)}。
- 优先必修：The0开场“that is”误作因果、任务资格 out for the mission反译、门卡等级比较对象、torch误成火把。PRETZEL的BRED疑似源拼误单列待判，不直接修源。
- 连续精修优先：钥匙接话、女线采集SPUNK双关、接收到一阵发毛、Fenfen Z1/Z3/Z6叙述、Daleir beat off与男同事夹住海盗动作。
- 合法保留：三组地雷笑话；脚环两周练习与姐姐说辞反差；USL/生物加密货币科幻语；维生素Top玩笑；SFW Werehund父子对话与独立非成人演出。没有把合句消费空行或旧ledger当当前漏译。

## 新增语境证据及边界

Erma F05与Daleir F06完整对读：前者相信指导、后者口误暴露诱导嫌疑；保留角色不可靠叙述，后续快感不追溯改成最初自愿。Fox记忆用lang(Fox)，不因catalog narrator改作全知旁白。男M08的F.A.P.-like jewel不直接认证与宠物水晶同机制。男女、SFW/NSFW与形态条件各自记录。

world-and-plot初次尚未落盘，结束前已补读全部406行并复核相关H/R/I项。角色主参考初次裁剪已补尾段。reader全部小段未裁剪。

## 后续

先复审A与Q，再逐完整场景精修B；提案不得按行数平均切回节点。code只登记用途未证实库存；image只读转录，不冒称图像完成；nested JSON运行用途单独待核。未修改正式译文、catalog、游戏或归档，未部署、未Git写、未再委派。
''',encoding='utf-8')
assert len({c['scene_id'] for c in coverage})==len(scenes)
assert {r for c in coverage for r in c['row_ids']}=={r['review_row_id'] for s in scenes for r in s['rows']}
print(json.dumps({'scenes':len(scenes),'rows':log['counts']['rows'],'findings':len(findings),'severity':dict(counts),'coverage':dict(statuses)},ensure_ascii=False))
