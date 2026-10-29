import json, hashlib
from pathlib import Path
BASE=Path('localization/editorial/r1')
P=BASE/'corpus/snapshot-01/packets/packet-10.json'
R=P.with_name('packet-10.reader.md')
OUT=BASE/'audit/packet-10'
scenes=json.loads(P.read_text(encoding='utf-8'))
by={s['scene_id']:s for s in scenes}
findings=[]
def add(sid, start, end, zh, reason, cat='continuity', severity='B', status='proposal', refs=None):
 s=by[sid]; rows=[r for r in s['rows'] if start <= (r.get('line') or 0) <= end] if start is not None else s['rows']
 assert rows, (sid,start,end)
 f={'finding_id':f'P10-{len(findings)+1:03}', 'scene_id':sid,'row_ids':[r['review_row_id'] for r in rows], 'severity':severity,'category':cat,'source_quote':'\n'.join(r['source'] for r in rows),'current_quote':'\n'.join(r.get('current_line') or '' for r in rows),'proposed_zh':zh,'reason':reason,'evidence_level':'direct_scene_text' if status=='proposal' else 'text_observed_runtime_or_source_unresolved','evidence_refs':[s['logical_path']+':'+s['root']]+[r.get('location') or r['review_row_id'] for r in rows], 'reference_keys':refs or [],'status':status,'apply_scope':'scene_draft_only','branch':{'mode':s['mode'],'logical_path':s['logical_path'],'root':s['root']}}
 findings.append(f)
add('SC89e4866f18a5c656',487,489,'想当太空海盗？先来一把官方海盗光电击器！当然，还得有飞船，再拉上一帮亡命之徒！……买了可别忘了装备上，这东西可不只是拿来摆样子的。','Lighttazer没有光速武器之义；整段保留先卖武器、再补飞船船员的促销玩笑。','term','A',refs=['world-and-plot:I03'])
add('SC33ab255adaf1dfb9',2013,2013,'哈哈，那当然！伊法妮通话结束。','“完毕并结束”照搬over and out，中文电台收尾不自然；保留爽快应答。','idiom',refs=['characters-primary:Yiffany','characters-support:Bossu'])
add('SC108f8f86a462d740',2020,2022,'好样的！这才是我们顶尖探员该有的劲头。看来再大的野兽也难不倒你！','夸奖不是在评价“好女孩”；“对你来说太大”英文句式直接残留，丢失迎战自信与荤梗可兼读的调侃。','voice',refs=['characters-support:Bossu'])
add('SCcf88d45ac7bb50f9',2367,2371,'不批准，探员。贴地飞行的限制仍然有效。不过，你的飞船已经安全驶抵你附近。另外，你已目视确认这座传送门的地面坐标，往后应该就能随时传送回来了。','RE- STRICTIONS是断词，不是长官突然拖音；把限制、飞船抵达与解锁回访连成公事简报，保留should。','voice',refs=['characters-support:Bossu'])
add('SCcf88d45ac7bb50f9',2375,2377,'抱歉，我们不能冒险把你传进实体里。你也看到了，这里的地形一直在变，其他传送门也可能移了位置。','RI- SK不是犹豫或拖音。solid surface指传送进实体的风险，不宜“实心地表”；保留地形变化→坐标不可靠的因果。','meaning','B',refs=['characters-support:Bossu'])
add('SC3a9d5c967ef75eca',2983,2986,'伊法妮：看来有人特别不想让外人在矿井里乱逛。要不，就是有什么特殊癖好。\n波苏：噗……探员伊法妮，现在可没空开玩笑。\n伊法妮：还不是把你逗笑了！伊法妮通话结束。','sniffing around是四处探查，不是技术“嗅探”；sex thing是随口往性癖上拐。SNORT接MADE YA SMIRK应呈现憋笑被抓包，不能先冷哼再“让你撇嘴笑了”。','idiom',refs=['characters-primary:Yiffany','characters-support:Bossu'])
add('SC2ff1b2dcad73472a',2188,2192,None,'失真段残留FU...ING等英文字段，但不能从残片反推完整句或把ASS前残片补成新性行为。需按音频/演出确认可恢复信息后，整段重做“失真→误听→屁股回嘴”的笑点；当前保留源残片，不先给确定译文。','source_uncertainty','B','needs_evidence',refs=['world-and-plot:英式用法、双关与语域'])
add('SCdf8aeea039fa8fb6',2194,2197,None,'男线独立失真通话；残片和结巴反应均需保持，不能套女线屁股回嘴。用途已是对白但残词含义未决，先核失真呈现再重写。','source_uncertainty','B','needs_evidence')
add('SCd99de6733dcdc94b',2270,2274,None,'GEAR TO与NOT GIVE宾语/句法残缺，现译“别给”可能把give up类残片误定为给予；证据不足，不补“不要放弃”等完整指令。复核信号失真表现与上下文，仍保持早期身份未揭。','source_uncertainty','A','needs_evidence',refs=['characters-support:Starkill'])
add('SCbc21ae6879225ba0',5219,5220,'装备用着没劲？性能平平？甚至……离最佳状态差远了？只要把需要的零件备齐，我就能帮你调到位！','sub-optimal是在技术人口吻中递进推销，不是中文“感觉平庸／不够优化”。匿名测试角色不擅认The0。','voice')
add('SC674c1f273752aad2',5341,5341,None,'“Just like he did”接take it有成人双关，现译“就像他那样做的”悬空；缺动作/宾语证据，不确定写出施受或性行为。需核测试条目演出与指代后整句处理。','source_uncertainty','B','needs_evidence')
add('SCd9d60e96fc755eca',3743,3743,'不是吧——姑娘，你来真的？','come on在此是无奈质疑，不是恳求；“求你了”使通讯中误认宠物代接的抱怨变成请求。','idiom',refs=['characters-support:Tomcat'])
add('SCf2152b86b3e6a7e0',3764,3764,'不是吧——姑娘，你来真的？','史莱姆接话分支独立收据；同为无奈质疑，不是恳求。','idiom',refs=['characters-support:Tomcat'])
add('SCf2152b86b3e6a7e0',3768,3768,'……咕叽？','GOOP在史莱姆状态是发声，与前后GLUG/GLOOP同类；“黏糊？”变成角色在说一个形容词。','voice',refs=['characters-primary:事实等级与分支红线'])
add('SC743bc08e3d49936f',2700,2700,'咕叽……？','GOOP是史莱姆拟声而非形容词“黏糊”；不扩大为常态口癖。','voice',refs=['characters-primary:事实等级与分支红线'])
add('SC6ab81ac8db1a367d',4240,4244,'汤姆猫：你这身小裙子还真挺可爱。假设啊，要是任务结束后你还留着它……\n伊法妮：假设啊，我现在就咬你一口，汤姆猫。我会利用这件衣服的轻盈效果通过易塌地段，一切都是为了任务。','“假设情境是我要咬你”像逻辑说明，失去以同词回击后故作一本正经的节奏；weightless不必推导成失重物理机制。','voice',refs=['characters-primary:Yiffany'])
add('SCb28ad558d39b8510',4304,4306,None,'门卡阈值应由持有卡等级决定；them在本段可能指keycards，现译“门上所标数字”让提示自我循环。需核原始字典门卡等级与运行显示后定稿；潜在玩法误导，不直接替脚本改数字。','gameplay','A','needs_evidence',refs=['world-and-plot:I04'])
add('SC7f5787288a86d66c',4323,4325,None,'男线门卡4同类指代问题，独立保留；需核them所指和实际显示。不是用相同句子合并男女分支。','gameplay','A','needs_evidence',refs=['world-and-plot:I04'])
add('SC87a1127b4e5bcb85',4246,4247,'唉，希望没被那个鬼鬼祟祟的科博德坑了……汤姆猫，帮我扫描一下这些卡片？','“不是只骗了我”把just误放到“我”的范围，读成不止骗我一人；此处是刚买完担心被骗。','meaning','A')
add('SC18adb5c64c9f45fd',3964,3965,'伊法妮：……你开玩笑的吧？\n汤姆猫：才——没有。序列号ID-10-T-5U5，就是伊法伊那把。','NOPE回答“你开玩笑吧”即没有开玩笑；“不——对”容易被读成否认上一句枪的归属。保留序列号不作文本润色。','continuity','A',refs=['characters-primary:Yiffany'])
add('SCc71a41293028bc8b',682,683,'你知道吗，自从落地后，我就真、真的越来越喜欢狗狗了。说起来，你不就是狗狗嘛……','r-real应是局部结巴，“真真的兴趣”不是自然中文；第二句是搭讪铺垫，不是冷硬指出物种。','voice')
add('SC3048c12be4e1ae2d',3198,3206,'波苏：几百年过去，她们身上凡俗的特征也越来越多。\n伊法伊：等等，那就是说，有些精灵真的不会死？\n波苏：据我们掌握的情况，确实如此。你在外面遇到、会跟你交战的精灵，应该都是年轻一辈，最多一百岁。\n伊法伊：这……哇……\n波苏：别光顾着惊叹。想挡住那些年轻精灵的攻击，你得时刻保持警觉。','跨行“有朽特征／在数百年的岁月流逝之中”倒挂；“就我们所能看出的而言”“别向敬畏屈服”是硬译。保留总部有界认知，不替其认证所有精灵设定。','continuity',refs=['world-and-plot:D04'])
add('SCf220ad115895cc8e',3076,3083,'伊法伊：哇！总部听见刚才的爆炸了吗？！\n波苏：听见了。看来图托恩这矿，已经让人占着了。\n伊法伊：……？那当然，可这跟爆炸有什么关系？\n波苏：占着矿的那些雷。\n伊法伊：对啊，炸的是矿里，可——\n毛瑟：波苏是说，老矿工在自己的矿里埋了雷，意思就是“这矿归我，谁来谁挨炸！”\n伊法伊：什么……？！总之我躲着它们就是了，行吧？！伊、伊法伊通话结束！','英语mine多义驱动误解；现译先明确布雷，主角再问何关爆炸，长官又退成“矿区传来”令问答失配。提案让“占矿”信息先出、“埋雷”后解释，不强造同音笑话；仍需二审笑点。','idiom',refs=['world-and-plot:英式用法、双关与语域'])
add('SC5f1b4d2abe382e83',2044,2049,'波苏：先等等，小子。飞船虽说还能勉强运转，但只准贴地飞行。我们不能再让你被击落，更不能让你出别的事。\n伊法伊：不是吧——！来真的？\n毛瑟：你现在可是我们唯一还在执行任务的探员，不能这么冒险！\n伊法伊：好好好！我会试着多讲点战、战术的。','“不能冒着……风险”句子未收完；active是当前行动状态不宜扩大成整个组织唯一现役人员；STRATEGIMICAL滑稽造词保留不熟练感，但不新增长期口癖。','continuity',refs=['characters-primary:Yiffai'])
add('SC7da96dd7dd612ff3',4425,4428,'伊法伊：应该会！我上过高级战斗装备课。蹲下就能启动圆盾，对吧？\n汤姆猫：没错！它能弹开小型投射物。不过，要攻击就得先放下盾。','战斗语境projectiles是弹丸等投射物，不是涵盖飞机生物的“飞行物”；保留蹲下启动与攻击先放盾两个条件。','term',refs=['world-and-plot:I04'])
add('SCb6b7bb0de1e47345',None,None,'头巾\n久经考验的|传家头巾','experienced修饰有经历的传承物，现译“有阅历的传承布料”不成自然物品文案；提案保留传承与历练，不新增具体持有人。','idiom')
add('SCc1bb2313b9d1996b',None,None,'头巾\n久经考验的|传家头巾','SFW同样生硬，但独立版本收据；不据同文字把来源身份合并。','idiom')
add('SC90869035da22d7e4',None,None,'矮人不要别的财宝，|有你的陪伴就够了。|真是个好宠物！\n你一走近，矮人便|摇起短尾巴，巴巴地|等你理他。\n矮人嘴上抱怨住处，|却还是朝你|粗犷地笑了笑。\n矮人隔着栏杆怒瞪着你，|像是在叫阵：|有胆就跟他对视。','“粗声的笑”把形容态度误成声音；中文按四个独立亲和状态重写，不串成同一次反应。保留每状态各自触发待实机核排版。','continuity')
add('SC48526d547246a31f',None,None,'初出任务的小高手，|这回碰上麻烦了','hotshot是自负/锋芒毕露的高手，不等于冒失鬼；用小高手维持自信遇挫的反讽。','voice',refs=['characters-primary:Yiffai'])
add('SC04b2b885330c22bc',None,None,None,'TRAEH IS / STILL OUT / THERE为同一展示句，现译“特蕾还／在外面／那里”无法自然连成“特蕾仍逍遥在外”。字典排序并非绘制顺序，需核键、定位与逐屏演出后再提逐节点映射，不把列出顺序当播放顺序。','continuity','A','needs_evidence')
add('SC3384501696d551cc',17,20,'也许是母的，也许不是，谁在乎呢，对吧？我正来劲，那身段又那么漂亮，当然得露一手。砰！！我直接把它从空中打了下来！……“直接”？没准还得说是“弯”着来的？','take it out承接战斗与WHAM，是击落而非接住；straight/gay笑点应建立在击落动作上。双关试稿仍待独立二审，不把不确定性别写成确定雌性。','meaning','A',refs=['world-and-plot:W11'])
add('SCba223e0dcbb46a0c',57,60,None,'原文It’s not as if I’m not without an appetite多重否定本身可疑；现译逐层照搬成不可读句。上下文是自夸雄健与欲望，不能凭此反推作者究竟想说有无胃口。标潜在否定风险A，核源后整段重写，不自动消掉not。','source_uncertainty','A','needs_evidence')
add('SCba223e0dcbb46a0c',78,82,'正想着这些，我才突然发现……精灵们不见了！……可我还被困着！那些狡猾的女人，原来只是假装投降！她们转移营地时，把我留在了这间满是触手的牢房里。好哇，竟敢这样耍我！','vixens在此是对精灵的辱称，不是角色突然认定其为雌狐物种；保留自称胜者终于发现受骗的转折，不圆其谎。','meaning','A',refs=['world-and-plot:报告可靠性'])
add('SCba223e0dcbb46a0c',90,91,'哼，新人，算我今天心情好，就把先去试着拯救这颗星球的机会让给你吧……','原文以最后补上的generous把援救后的嘴硬落地；现译“既然我此刻对你挺大方”像因果说明，整段改成居高临下的让功口吻，不认证其真有能力。','voice')
add('SC69e98820bd888ee0',None,None,None,'当前BUMPER译作弹板，但参考D01所述Bumper为失控巡逻机器人。此处Plus型号是否同一对象尚未核演出，存在机械实体被误当场景机关的风险。需核对应图鉴/实体后定名，不从键名自动推广全局替换。','term','A','needs_evidence',refs=['world-and-plot:D01'])
# 逐场阅读判断；生成只负责机械映射与完整性验证，非替代语义阅读。
notes={
'SC33ab255adaf1dfb9':'SFW女线收拾大块头后通话；装备未齐仍需尽力救助，频率27.850；合句尾行完整，不报漏译。',
'SC108f8f86a462d740':'女线胜后夸奖→新护腕滑行→塌顶逃生；保留DOWN与JUMP、装备条件及主角回应。',
'SCcf88d45ac7bb50f9':'女线请求出击被拒→目视确认传送门可回访→质疑规程→地形移动解释→不情愿挂断。',
'SCa0ee2bc475820f52':'SFW女线矮人图鉴：酒吧赌徒往事与挖深/鼓声引用玩笑，长官沉默；现译意思可连，不把文学梗另造设定。',
'SC3a9d5c967ef75eca':'女线机械改装图鉴，查探矿井→性癖玩笑→长官憋笑；需整段恢复节拍。',
'SC5ddaff51f19c0325':'SFW女线初次恢复联络；pipsqueaks引Mauser自嘲不快，主角否认后问频率；现译小矮个与小可爱有承接，不强添鼠类口癖。',
'SC841b41204fa79f67':'女线抵矿区，资料热情与救人优先冲突→同事装备说笑；保留现代科幻语域，少量书面词尚能理解。',
'SC2c6addff352bfb13':'仅hasItem(ZenerStar)分支；虚构游戏内按键声音的担心，保留SELECT和UP+ATTACK，不当人物真被确诊。',
'SC1f3af40987a668b2':'SFW女线限量鞋发烧友对谈→主角求实用信息→空中DOWN+JUMP且命中可受伤对象才反弹，合句条件齐全；不因“会承受伤害”略硬就重写整个合法段。',
'SC61fecac643ed33f5':'女线信号失真，Tomcat残词未足可恢复；主角明确听不清并延后通话，保留残片不猜补。',
'SCfd3daaa3e0ae8d94':'女线Kobo误认被当地群体蹂躏，主角未能解释；不把Tomcat猜测写成真遭遇。跨框引号略拗口但语义成立。',
'SC88308e58fac219d6':'女线史莱姆咕声被误认恶作剧；笑掉尾巴的习语本作兽人可兼读，不按真实脱尾设定理解。',
'SCa75f9bf643dc1302':'SFW水晶仅功能讲解，无NSFW收尾调情；保留版本差异，喜爱→抚摸充能→效果因生物而异条件齐全。',
'SCeb14ae6ce4edf9e8':'NSFW水晶有额外主动亲近生物的回应，不能套回SFW；Jakov/Obscura暂不无证定专名。',
'SCc628ffe48ea2eae1':'女线鞋说明，前文读过指南→口头讲解→Tomcat兴奋弹跳→主角结巴感谢；原文这里确说hit something，不跨场强补条件。',
'SC5f7af24ab0a7d9e8':'作弊菜单提示保留@EmuButtons占位及换行符；没有把动态按键当固定键名。',
'SCfac2344cdaea3f1b':'男线地雷笑话：两种处理方式→主角无语→踩雷冷笑话→假称断线；“踩到你的雷”是有效本地化，明确保留。',
'SCeb6f35bc1c4dc1e8':'男线蜘蛛机器人：恐惧与技术解释相对；真蜘蛛没有的是向人喷网能力，不将其判为原文生物学事实错误；纳米网维护环境为总部说辞。',
'SCbb716ef92ce27ac9':'男线显示器狗视频分神→被催继续行动→越想变兽态→同事担忧；野狗措辞略硬但与真实跑跳画面可读，不把形态兴趣写成既成变化。',
'SCc356eb22f40b28e8':'男线卫星失联重连→地板随时塌落→主角想跺脚深入；保留冒失的行动主意，不替角色改成谨慎。',
'SC15b497f7a4d5a4a9':'男线Werepup后通话：学院故事替代被截断意图，Mauser想听荤话与门卡用途另层；不补幼崽成人互动，门卡1级及东向救援保留。',
'SC3dbb26968789931b':'SFW男线主角变形后通讯：总部缺数据，怀疑撞头→主角遮掩→往东救援；不将总部怀疑认证成幻觉。',
'SC1fdcff4e3d3e1844':'男线C双首领败后，未集齐05/06/08找三人，齐后提示回Zeronia；两分支均读且不拼成一段事件。',
'SCf62482aec41d7fcc':'男线兽态The0按狗误认，芯片扫描动态占位保持；fetch与挖坑能力相连，不认作常态幼年主角。',
'SC994c9cd9ed1177f9':'男线史莱姆The0：身上粘芯片→狭缝能力→扫描→勿弄黏；现译略重复但自然可懂，占位不改。',
'SCf6a3230e9ad0488c':'男线卡片强能量警告反被听作烟花秀，主角兴奋与Tomcat结巴相对；保留语气及不是女线的怀疑被骗。',
'SCab6c8180ed27265e':'男线食物形似Barker部位→心率温度上升→关监控→急辩，笑点有效；不凭entry追加幸运效果。',
'SC991ea0f9329298c2':'Trainer特定怪物最后一击送机库，保留捕获条件，与Trainee弱化武器不同。',
'SC5ef5b1f865e8f630':'SFW男线方形球通话：精神科待命→他人变兽态报告→主角遮掩→反惦记挖洞；传闻层和当前主角经历不合并。',
'SC021a968dd3397402':'双页卡文：龙传说与Sevaw召幻影分层，分行语序虽依原排版但中文可连读；不把传说野兽当当前真实龙。',
'SC4fca002d8d726f51':'SFW卡背源是空白分隔符，现文保持空白；正面Pigobin帝国背景另行存在，绝不补NSFW卡背。',
'SC409ec23e7cec48f7':'SFW片头：时代→组织英雄宣传→冒险梦想→未知危险反转；自动时长与演出已读，中文可连。',
'SC0bbcef2ad0f68b4d':'NSFW片头独立读完；同宣传结构，不把narrator元数据外推所有VSN发言归属。',
'SC293a09cd1a3e883d':'F08完整：强迫海盗→幻想海盗女王→匿名特工击倒→海盗反客为主→抱怨迟来救援；Vickers女王不是Traeh，不替匿名来者点名。现译主要意图和施受保留；leash的it译抬着它需图像二审，当前不无证判错。',
'SC5aaca5284184e89a':'SFW女FZ2 lang(Fox)讲历史：议会不知武力→生物似响应→征服奴役→希望丧失；seemed/仿佛与说辞层保留。',
'SC7d1895732835e072':'SFW女Enelye战后：主角受够不朽者→称赞奖励→被打断换装→裙子舒服但下次自己穿。她并非男线抗拒裙装；尊称原文有据。',
'SC9ddff3d06e1707d8':'女线Area0失败自述完整：先小个体再猫科群体，主动求欢和照料/等待救援双层保留；不等同成功主线，不凭narrator当全知旁白。',
'SC5ef25d681db55e20':'女线E失败报告：小行星Exile→生还可能低但遗体未寻→黑暗女王宿主与扩张推测；现译未断言死亡/已扩张，保留。',
'SC3384501696d551cc':'男M03完整自夸Top→击落飞龙→被拳击飞→落巢遭强迫→身体反应不改同意→岔开逃跑问题；只有动作误译必修，Top双关后续专案。',
'SCba223e0dcbb46a0c':'男M06完整不可靠胜者报告：自述屈服对方与被绑反差→接待→没法离开→发现假投降→嘴硬让新人先救星球；否定源异常独立Q状态，不替角色圆谎。',
'SC78be6b2b2431f3c9':'SFW男MZ5 Fox讲述：星际来客落岩石卫星→入监牢→好奇/精神力不确定→触晶受控；不加旅人身份，译文其虽稍书面但语义成立。',
'SC234ab616e2065b4f':'SFW男Bigbold：回收佩刃→理想与首次生态任务→询问同僚线索→对方跑掉；保留SFW交涉，不添加NSFW战后采集。',
'SC62d1c4dfee938d0f':'SFW男BigboldV2：嫌弱装备→自打脸停顿→生态理想演讲被逃跑打断→撞门塌顶→护腕掉落解围；先后与道具非赠予完整，lucky break回环有效。'
}
coverage=[]
for s in scenes:
 fs=[f['finding_id'] for f in findings if f['scene_id']==s['scene_id']]
 inventory=s['kind'] in ('code','image') or s['logical_path']=='datay/scripts_pack.json'
 note=notes.get(s['scene_id'])
 if inventory:
  note='已逐行读完文本库存；'+('code常量用途未核，null中文不视为漏译，不强翻API/键/日志。' if s['kind']=='code' else '仅静态嵌套JSON候选，含占位/导航字段；运行时用途未核，不强翻标识或占位、不冒称实显已校。')
 elif not note:
  note=('本场逐段先连读英文及控制，再连读当前归档中文；'+s['root']+'：')+('存在所列段落提案/待核，其余表达与完整意思保留。' if fs else '当前表达可自然理解，呼告、动作对象、否定及条件无明显冲突；不为凑数改合法变体。')
 aliases=s.get('aliases',[])
 coverage.append({'scene_id':s['scene_id'],'read_status':'read_full','row_ids':[r['review_row_id'] for r in s['rows']], 'context_checked':not inventory,'findings':fs,'result':'inventory_only' if inventory else ('needs_evidence' if fs and all(f['status']=='needs_evidence' for f in findings if f['finding_id'] in fs) else 'issues_found' if fs else 'retain'),'notes':note,'mode':s['mode'],'kind':s['kind'],'logical_path':s['logical_path'],'root':s['root'],'aliases':aliases})
assert len({c['scene_id'] for c in coverage})==len(scenes)
assert sum(len(c['row_ids']) for c in coverage)==sum(len(s['rows']) for s in scenes)
OUT.mkdir(parents=True,exist_ok=True)
for name, data in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
 (OUT/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),encoding='utf-8')
log={'input_path':str(R).replace('\\','/'),'input_sha256':hashlib.sha256(R.read_bytes()).hexdigest(),'packet_path':str(P).replace('\\','/'),'packet_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'read_status':'read_full','read_ranges':[[i,min(i+99,2386)] for i in range(1,2387,100)],'truncated_ranges':[],'references_read':['LOCALIZATION_BRIEF.md:1-65','WORK_ORDERS.md:1-48','characters-primary.md:1-377','characters-support.md:1-128','world-and-plot.md:1-406'],'reference_read_ranges':{'characters-primary.md':[[1,100],[101,200],[201,300],[301,377]],'characters-support.md':[[1,100],[101,128]],'world-and-plot.md':[[1,100],[101,200],[201,300],[301,400],[401,406]]},'method':'实际read每次100行，1–2386全部返回，无工具裁剪；每场先连读英语/控制，再连读candidate4当前段。JSON仅作canonical行ID、别名、原稿溯源的机械映射，不作脚本扫读冒充语义通读。','limits':['静态粗校提案，不是approved或正式应用','code用途、嵌套JSON实显与排版/运行未核','别名沿输入保留，未另行把不同版本/性别/形态合并','旧ledger未作为当前问题依据，合句空行不报漏译']}
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from collections import Counter
counts=Counter(c['result'] for c in coverage)
summary=f'''# packet-10 连续语境粗校提案

## 完成范围
- 实际逐100行 read 阅读稿 1–2386，共2386行，无裁剪；三个角色/世界参照及brief、工单协议全文已读。详见 [reading-log.json](<reading-log.json>)。
- {len(scenes)}个canonical场景、{sum(len(s['rows']) for s in scenes)}个canonical rowid逐场收据，无重无漏；别名原样附在 [coverage.jsonl](<coverage.jsonl>)，不改输入JSON及旧稿。
- 共{len(findings)}条发现，其中{sum(f['status']=='proposal' for f in findings)}条段落提案、{sum(f['status']=='needs_evidence' for f in findings)}条待核；分级{dict(Counter(f['severity'] for f in findings))}。Q仅状态，待核仍标潜在A/B风险。
- 场景结果：{dict(counts)}。库存读完不等于玩家可见文本已校。

## 优先二审
1. 女线传送规程：去除RE-STRICTIONS/RI-SK误读的拖音，恢复职业化限制解释。
2. 男女门卡等级指代：需结合卡等级与显示确认them，不直接按门自身数字回填。
3. 男线矿井mine笑话：现译先讲布雷再问爆炸，问答失配；中文功能重写须独立检验，不追求逐词同音。
4. 男M03 take out击落误译成接住；保留Top嘴硬、被强迫与身体反应分层。
5. 男M06多重否定属于源异常待核；vixens不可误成精灵物种变雌狐。自称胜者不能变全知事实。
6. 失真通讯残片与坏结局逐屏拼句先补演出证据，不强补完整英语或猜播放顺序。

## 明确保留
- 地雷“踩到你的雷”冷笑话、男女/SFW各自主线反应、原文SFW空白卡背、合句后的空行均不按漏译处理。
- 片头宣传语保留来源口吻，Fox的lang讲述不因narrator索引变成全知旁白。F08海盗女王幻想不与Traeh混同。
- 男Werepup后只谈故事与门卡，不补被截断成人意图；M03身体反应不反证同意。
- Zener能力按键、@DerekChipReport、序列号、规程编号及版本条件保持；科技语不套奇幻文风。

## 新增有界证据
- 女线Bossu确会以再大野兽也难不倒她调侃式夸奖；不外推全篇轻浮。
- 男M03与M06都是当事人自我辩解，不把败北归咎或胜者自夸当客观设定。
- female SpecialFap的NSFW有额外亲近生物回应，SFW没有；不能由文本大部分相同就拼接。

## 边界
仅写本目录四份审计文件及构造脚本。未改正式译文、catalog、归档、游戏或他人文件；未安装、Git写、委派或标approved。没有运行游戏、核图像、测字体排版或正式回填。构造脚本仅保全映射与校验收据，不代替上述实际小段阅读。
'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
print(json.dumps({'scenes':len(scenes),'canonical_rows':sum(len(s['rows']) for s in scenes),'findings':len(findings),'results':dict(counts),'sha256':log['input_sha256']},ensure_ascii=False))
