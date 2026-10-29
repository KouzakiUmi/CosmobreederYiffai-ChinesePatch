import json, hashlib, pathlib, re, collections
BASE=pathlib.Path('localization/editorial/r1')
P=BASE/'corpus/snapshot-01/packets/packet-03.json'
R=P.with_suffix('.reader.md')
OUT=BASE/'audit/packet-03'
scenes=json.loads(P.read_text(encoding='utf-8'))
lines=R.read_text(encoding='utf-8').splitlines()
line_rows={i:re.match(r'ROW (\S+) ',s).group(1) for i,s in enumerate(lines,1) if s.startswith('ROW ')}
rowmap={r['review_row_id']:(s,r) for s in scenes for r in s['rows']}
# 以下范围和意见均来自逐段read后人工判断；程序只提取精确引文、ID并校验覆盖。
specs=[
(147,148,'B','voice','一件我现在不怎么穿的衣服。你穿上肯定正——合适！','juuuuust是拉长强调，不是“刚——刚好”的口吃；保留商人含笑推销。'),
(193,193,'A','meaning','你到底是来帮我爽一把，还是就站在那儿看？','NSFW的get off在索求性满足，不是帮忙离开牢房；本包同角色GoodbyeNotRescued提到给矿工解乏，不能套SFW救援语义。'),
(284,285,'B','voice','听说三角能力能提高防御，不过攻击会稍微下降；十字能力则正好相反——挨打更疼，打人也更疼！','合句无漏译，但“挨伤更多、伤人更多”不自然；完整保留攻防反向和伤害增减。'),
(291,293,'B','voice','既然你已经跟其中一只生物亲热过了，这个拿去！拿着它再跟它们亲热一回，说不定就会感到一股力量流遍全身……','原文借亲近委婉表达互动与道具条件；“变得非常亲近”生硬，“他们”对象漂移。建议仍不补具体互动动作。'),
(317,320,'B','relationship','探员，小心。你快到你弟弟被黑暗能量控制的那间密室了。要继续前进，就得做好最坏的打算。','女线已确认kid brother；“你的手足”是明显翻译腔。overtaken不是肢体被吞食；保留危险预警。'),
(325,325,'B','voice','伊法妮，干得好！你已经抓到一些当地生物了！','local fauna指本地生物的集合，不是把“动物群”当捕捉对象；表扬应先落在行动上。'),
(329,330,'B','continuity','是啊，你跟这些当地生物越亲近，它们就会越有自信！','原句跨两框为一个比较结构；“本地动物群越处越熟”不合口语搭配。'),
(341,344,'A','meaning','斯凯菲亚的精灵虽然全是雌性，却并非个个都能长生不老。数百年来，她们身上凡人的特征越来越多。','may...but在此为让步：承认全雌性再否定全不朽，不是推测雌性；后两框倒置碎裂，“有朽特征”生硬。'),
(345,348,'B','voice','伊法妮：等等，那就是说，她们之中真有长生不老的？\nBossu：没错，至少目前掌握的情况是这样。在外活动、参与战斗的精灵，无疑都还年轻，最多也就一百岁。','保留主角惊讶—总部有限度确认—百岁仍年轻的笑点。“就我们所能看出的而言”不是自然通讯表达。'),
(350,352,'B','idiom','Bossu：先别顾着惊叹。保持警惕，才能应付那些年轻精灵的攻击。\n伊法妮：对，得集中精神。','give in to awe指别惊叹得分神，不是“向敬畏屈服”；on your toes保持警觉。'),
(399,402,'B','relationship','Mauser：加油！你能行的！\nTomcat：起来！让你弟弟见识见识你的身手！\nBossu：探员，深呼吸。集中精神，交手时别慌。','已确认女线对弟弟；战斗鼓励不宜使用“你的手足”和“看看怎么战斗”的翻译腔。不得把三人合成一人。'),
(468,468,'B','continuity','我、我、我不是说你不该穿！你穿裙子一定很——','look good on...被截断，现译无依据添出“绝——”，导致突然出现不明半词。保留尚未说完的夸奖。'),
(613,613,'A','meaning','哦，嘿！准备好亲热一番了？就跟本地那群操——','当前只保留了宾语骂词残片，漏去get frisky的挑逗意图；这里只截断FUC-，不能把整句的亲热含义一起丢失。具体断句仍需后续节点回填时核演出。'),
(704,704,'A','meaning','唉，那玩意儿一次都没管用过。白花了那么多LECT……','never worked是试过却从未奏效，不是从未使用。后续承认仅用来吹牛的笑点依赖假证办不成事。'),
(715,717,'A','gameplay','用门卡很简单：拿着卡，直接走进能量门就行。门的等级不超过门卡上标的等级，就能打开！','them回指门卡；现译“等级不超过门上所标数字的门”把门卡权限上限误写成门自己的等级，提示失效。'),
(727,732,'B','voice','老兄。章鱼。我最爱章鱼了。老兄，兄弟，给我吧。还能补脑，我正需要。老——兄……','原文刻意短促重复索食，应保留节拍；末句D U D E残留英文使重复升级的笑点断开。仅段落提案，正式回填不得抹去节点节拍。'),
(852,852,'B','voice','谢、谢了，伙计。真不知道你们不当攻的都是怎么熬过来的……！','non-tops是性角色而非职级；“非上位的是怎么做到的”既缺所指又像阶层分类。保留受救者嘴硬感，不扩为已确认永久偏好。'),
(949,949,'C','idiom','天知道我在这儿关了多久。能帮我一把吗？','stars knows为世界内感叹习语。当前“只有星星才知道”可作为科幻化感叹保留；此处仅给更短促口语的可选方向，不判天文事实错译，不新增神祇设定。'),
(957,957,'A','idiom','等我活动开筋骨，准让那些精灵吃不了兜着走！','won’t know what hit them强调突然而压倒性的反击，不是打完不知道行凶者；现译无端添加隐蔽身份。'),
(995,995,'B','idiom','哟，自己人来了。欢迎光临黑市！','friendly face在koboCostume分支是认作同伙而欢迎，不是评价面孔友善；只说明当下外观误认，不认证主角海盗身份。'),
(1026,1028,'B','voice','嘿，伊法伊！欢迎来我的全新太空实验室！嘿嘿……不过，这原来好像是你姐姐的飞船，对吧？海盗把大部分东西都抢走了，好在我找到了一套还能用的装备维修设施！','先欢迎再心虚揭示实验室来历，当前“在这上面见到你，就在……”挂接生硬；保留sister与角色猜测，不补设施真实规格。'),
(1112,1118,'B','voice','伊法伊：Bossu，请立刻确认我的身体状态——确认我没变成水生生物！\nBossu：放心，伊法伊，你还是百分之百的狗。图托恩的异变导致有人目击到没有实体的水母，可能正是它们让你怀疑起自己来了。\n伊法伊：我可觉得它们实在得很，哎哟……','原段是一本正经请求确认—总部解释—挨打吐槽；“更新当前情况”“相当实体”生硬，使身体接触反驳失去落点。'),
(1123,1124,'B','voice','嗯，你是说灵能啊……看来还得我自己想办法。','“嗯，精神，你是说”保留英语后置倒装，无法承接前文灵能幻象线索；不擅自补具体解法。'),
(1128,1129,'B','term','Bossu！我遇到了一批人形绿蜥蜴兵，看着可一点都不友好！','anthro修饰具人形蜥蜴，当前“兽人绿色蜥蜴兵”容易误认另一兽人种族，且中文定语堆叠。保留主人公此时还不认识科博德。'),
(1238,1242,'B','continuity','Mauser：嗯？伊法伊……？\n伊法伊：对，是我。我只是扮成科博德了。\nMauser：……你拿着PPP无线电到处晃，还不停给人打电话，这伪装怕是没什么用。\n伊法伊：哦……说、说得也是。伊法伊通话完毕。','最后的“是的，我想是这样”对吐槽反应生硬；整段保留认出—解释—戳穿—急挂断，不把角色自称伪装升级成潜伏事实。'),
(1277,1279,'B','source_uncertainty',None,'原文为受干扰的残片GEAR TO... / NOT GIVE...，尚不能确定省略结构；“别给”擅定give为完整祈使。须核对原音/演出或作者意图后再提完整译段，不能凭后文猜补。'),
(1388,1398,'B','voice','Tomcat：天哪，那是什么？\n伊法伊：什么什么？不就是我买的牛奶吗。\nMauser：我以前在奶牛场干过，那绝——对不是牛奶。\n伊法伊：它还会颤呢。牛奶一般也这样吗？\nTomcat：呃……\nMauser：嗯……\nTomcat：不管怎么说，看着倒不像什么毒物，说不定真对你有好处！\n伊法伊：吃鱼对身体好吧？这东西闻着就像鱼！\nMauser：行，我先撤了。\nTomcat：我也是。你自求多福吧。','整场为怀疑伪奶—小心绕开真相—借口挂断；当前NOOOT/UHHHH机械写“啊啊啊”变成惨叫，“祝你好运应付那个”英语腔。“颤”体现凝胶般抖动，不补物质身份。'),
(1533,1534,'B','voice','酥麻\n涌上一种|难以言说的感觉','“生出感觉|如此复杂”是拼接英语语序；此SFW独立变体保留含混感，不挪入NSFW内容。'),
(1669,1669,'C','continuity','他舔着嘴，|急切地等你理他。','现译语义成立，可保留。此建议仅让UI更紧凑口语，不属必改；与同组吃饱/饥饿及愿否抚摸状态分开，不合并为新状态。'),
(1685,1685,'B','voice','精灵冷冷地看着你，|满眼轻蔑。在她这样的|高贵存在面前，你算什么？','“用冷淡的轻蔑看着你”不合中文搭配；保留傲慢的反问，不加封建称号。'),
(1690,1691,'A','meaning','你一来，吱吱怪|便来了精神。现在他|跟你在一起自在多了。\n吱吱怪缩在笼子深处，|紧张地|打量着你。','perks up是精神一振，不是竖起身子；后一条把from the back of his cage拆成“从后面……他的笼子”句法崩裂。两条是不同亲密状态，严禁拼成连续发生。'),
(1696,1696,'B','idiom','你一走近，挥爪便|客气地打起呼噜，|收起那双凶爪。','murder mittens是猫爪戏称；爪可收、肉垫不能像刀剑一样入鞘，“凶器肉垫”逐词且形象失真。'),
(1712,1713,'B','voice','精灵女王恩莉耶，|魔法造诣无人能及。|图托恩近来的变故|并未吓倒她，|她仍让年轻精灵|在林中练习战斗。\n即使长生不老，|恩莉耶也难免有|凡俗的肉体欲望。|与大多数精灵一样，|一场交手之后，|只要认可对手，|她便乐于再交欢一场。','High Lady在同包明示ELF QUEEN，译“高阶女士”失去身份；“无法免疫欲望”“若觉得对手配得上”拗口。两页建议分别回填，竖线仅示意需排版复核，不承诺字宽通过。'),
(1789,1789,'B','idiom','一场汪风大胜，|换来更凶猛的惨败！','WAN/ruffer借狗叫代one/rougher；当前两次“汪”却漏掉rougher的程度对比。建议仅保留一次犬类双关，使先胜后惨败可懂。'),
(1889,1891,'B','meaning','黑暗势力袭向我们所有Fenfen，不分老幼。那时，仿佛真的再没有任何希望。我们族中的超能力者虽然强大，却从未经历过暴力。','powerful though...may have been同属让步，不是怀疑其强大；“暴力对我们全然陌生”可更自然为没有经历。保留Fox族内讲述而非全知旁白。'),
(1903,1906,'B','voice','超能力者将种种本领化作了战争武器。爆裂的灵能弹把敌人轰退，强劲的念动力波阻住了大军前进。有些人甚至改变自己的身体，把它化作战斗的工具。','“能力武库被征用”主被动抽象堆叠，“走得更远”机械比喻；按战力升级重建叙述，不补谁强征谁。'),
(1910,1910,'B','term','其中一些，比如高贵的精灵，拿起古老的武器，援助我们Fenfen……','同包精灵已有中文，Elves残留破坏连读；Fenfen族名尚待术语裁决，暂保留不私拟。'),
(1962,1963,'B','voice','跟以前训练时不一样，真碰上这些家伙，可没人等你先调整到舒服。不过，我学得快，马上就跟着那猛男的节奏摆动起身子。','“家里的训练”把back home误缩为私人家庭，“先适应舒服”不合中文；保留训练与实地之别，不自动定学校/家庭地点。'),
(2263,2266,'B','voice','对，没错，肯定是这样。那无赖突然耍起花招，逼得我只好一遍遍“还手”！没记错的话，我防卫得实在出色，连那位大人都夸我是乖孩子。真是光荣啊！','sudd-enly只是排版断词，不该添加结巴。beat him off是自卫/手淫双关，当前只打退削弱嘴硬性回忆，建议引号留歧义而不补画面动作。'),
(2280,2283,'A','meaning','要是你在矿井里找到地图数据盘，就不用谢我了。对我这个……乖……孩子……来说，都只是分内的工作……？','If you find条件被“要在……找到”写成目的/指令；后接日常工作应承接“那些盘是我的成果”的自夸，不改成叫玩家特意去找。末尾good boy仍保留不安停顿。'),
(2384,2386,'B','voice','特蕾年纪轻轻就天赋过人，总能想到别人想不到的办法，怎么看都是议会的一位得力新成员。因此，她顺利获准接触我们Fenfen储存的力量。','“天赋远超其年纪”“力量贮藏”生硬；原文readily是顺利/毫不犹疑，不宜强化“不费力夺得”。因果只体现叙事承接。'),
(2428,2429,'B','voice','议员们无法克服这股灵能扰动，给她最后一击，只好改将特蕾封在水晶牢笼里。','英文状语前置导致现译无主短段“无法……给出”；完整保留无法击杀而改封禁的行动逻辑，不补具体扰动来源。'),
(2432,2439,'B','voice','失去凶悍首领的指挥，那群投机者便四散溃逃，躲避Fenfen议会的力量。但这并不意味着Fenfen迎来了胜利……双方都付出了惨重代价。你降落的这颗星球，再也不是Fenfen宁静的家园，只剩下往日家园支离混乱的影子。','当前“仓皇逃离……的力量”“往日模样的一个混沌残影”英语抽象搭配明显；按溃败—不算凯旋—残破故土的落点重写，控制边仍分别输出。'),
(2508,2511,'B','term','是我的宇宙头盔！不知怎么跑到这儿来了！以后万一要上太空，可就用得上了。接下来只要再找到宇宙服的衣身部分，就能凑齐一套真正密不透风的装备了！好耶！','Cosmohelm/Cosmosuit未译，装备找回的叙述断裂；现译“密封好装备”搭配不通。词项暂用本包现有宇宙服，最终需统一头盔/星装术语，不全局替换。'),
]
findings=[]
for a,b,sev,cat,zh,reason in specs:
    ids=[line_rows[i] for i in range(a,b+1) if i in line_rows]
    groups=collections.defaultdict(list)
    for rid in ids:
        s,r=rowmap[rid]; groups[s['scene_id']].append(r)
    assert len(groups)==1,(a,b)
    sid,rows=next(iter(groups.items())); s=rowmap[ids[0]][0]
    f={'finding_id':f'P03-{len(findings)+1:03}','scene_id':sid,'row_ids':ids,'severity':sev,'category':cat,'source_quote':'\n'.join(r['source'] for r in rows),'current_quote':'\n'.join(r.get('current_line') or '' for r in rows),'proposed_zh':zh,'reason':reason,'evidence_refs':[f"{s['logical_path']} / {s['root']} / reader:L{a}-L{b}"]+[r['review_row_id'] for r in rows]+[r['unit_id'] for r in rows],'reference_keys':['LOCALIZATION_BRIEF:2-4','characters-primary:事实等级与分支红线','characters-support:使用边界与证据层级'],'status':'needs_evidence' if zh is None else 'proposal','apply_scope':'scene_draft_only','branch':{'mode':s['mode'],'root':s['root'],'controls':s.get('controls',[])}}
    findings.append(f)
by_scene=collections.defaultdict(list)
for f in findings: by_scene[f['scene_id']].append(f['finding_id'])
notes={
'SC55c4a209986bb4f7':'裙子段已完整核对：Mauser紧张→精灵赠礼引起资料兴趣→反重力玩法→Yiffany凑对玩笑；cute couple不是已交往。airy同时含轻盈/透气，现译可成立，不强行改为单义。',
'SC05c3dd2092871dea':'已核紧追女王→涡轮未修→逃脱→不确定安全结局。女线文件中的sister由弟弟发言可成立，不因文件名自动改弟弟；未看图，不终裁每框发言人。solar system是否泛指所在恒星系留设定复核。',
'SC9711bca5985d84ed':'完整读开场：女主接任务救弟→匿名女王干扰击落→设备被偷→重新探索。narrator为统一元数据，实际多角色轮流；不自动归旁白。',
'SCf1e352091c207f10':'完整读自夸矮人遭遇→被搅局→记忆模糊→乖孩子洗脑→鼻头挨击醒来；角色吹嘘不升级为客观战力，beat off保留双关，断词不加口吃。',
'SC3b2e2ad5011ee43d':'完整读制服烧毁→飞龙追击与俯冲踢→矮人性经历→科博德囚禁→向玩家搭讪。不同物种与动作主体已区分；dog/pussy口头双关不据此定年龄。',
'SC8cfb083ebf53f503':'完整读对小狗讲话与成年22岁首次任务回忆穿插；回忆与当前不能合并为同一场交配。统一narrator标签不据此定发言人；既有合句空行不报漏译。',
'SC4ae7f053796af024':'Fox语言前缀与主角text短反应分开；Fenfen历史为Fox讲述。特蕾获力量并腐化、议会自责均保留叙述归属，不变全知设定。',
'SCe240b1877125bd63':'Fox讲战争多年→议会受制→短暂机会→封禁→双方代价；未凭其narrator索引定旁白。不能提前补未来宿主信息。',
'SC975be6136054e5ba':'SFW通讯失真残片按残片理解，不将其还原为完整警告。ZH里wake up片段可辨，但原音未核，不进行猜补性精修。',
'SC96febb905f22a5b8':'纯失真音与不完整TR/CALI/ATE保留为源异常待核线索，不擅自恢复成完整剧情命令。',
'SCcf94f585c1e0205e':'SFW海盗帽童年幻想与任务提醒完整；PUPLOCK为角色临时海盗名，尚无证据定正式译名，暂留。',
'SCda5a8d89a42d6a63':'存档地点为地名缩写码，保留以免破坏辨识；需后续与实显位置/可用宽度一并决定是否中文展开，不把缩写本身判漏译。',
'SC41c028c4ae8b572c':'RAPER与Rapier武器ID可形成原作荤双关；不擅改成RAPIER纠正源文，现译保留字面风险留精校复核。',
'SC68dc400330a64e6b':'卡片说明两框承接完整；EN末行自身缺右方括号，当前保留源结构，不在本轮当中文损坏回写。',
'SC2ea0ca051866975b':'literal/figurative→摧毁不可能无人机→作弊露馅的问答成立，现译保留。',
'SC09b1c6371a1b7cec':'SFW捕获→观测单元→亲近提升自信/回礼→女主知道流程。玩法链与说话人分开；不搬用NSFW育种细节。',
'SCb09c7c6e85e32642':'确认姐姐→无回应→下次不留手→先脱险→钩爪操作；UP+ATTACK与未选择异能的条件完整，亲属及施受无误，保留。',
}
coverage=[]
for s in scenes:
    sid=s['scene_id']; code=s['kind'] in ('code','image'); runtime=any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in s['rows'])
    fids=by_scene[sid]
    if code:
        result='inventory_only'; note='已逐条读本场候选字符串，仅登记用途/转录范围。未核调用点、玩家可见性或图像全幅；不将空ZH判漏译，不提供代码字符串自动翻译。'
    elif runtime:
        result='needs_evidence'; note='已读本场嵌套JSON原文及当前文；任务日志/patchDictionary运行时实用性未核，测试/占位内容不冒称正式实显已校。保留现状等待调用链核验。'
    elif fids:
        result='needs_evidence' if all(f['status']=='needs_evidence' for f in findings if f['scene_id']==sid) else 'issues_found'; note='整场原英与当前归档中文连读完成，问题仅作段落提案；其他语义完整部分保留，合句消费的空行不是漏译。'
    else:
        result='retain'; note=f"已连读本场 {s['root']}。原文与当前中文在本场范围的对象、否定、数量及语气承接成立；保留既有译法，不为凑数换词。"
    note=notes.get(sid,note)
    if fids and sid in notes: note+=' 本场发现见关联提案。'
    alias_ids=[r['review_row_id'] for alias in s.get('aliases',[]) for r in alias.get('rows',[])]
    coverage.append({'scene_id':sid,'read_status':'read_full','row_ids':[r['review_row_id'] for r in s['rows']],'context_checked':True,'findings':fids,'result':result,'notes':note,'mode':s['mode'],'root':s['root'],'aliases':s.get('aliases',[]),'alias_row_ids':alias_ids,'validation_scope':'text_only_not_runtime'})
assert len(coverage)==len(scenes) and len({c['scene_id'] for c in coverage})==len(scenes)
assert {x for c in coverage for x in c['row_ids']}==set(rowmap)
for filename,data in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
    (OUT/filename).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),encoding='utf-8')
log={'packet':'packet-03','packet_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'reader_sha256':hashlib.sha256(R.read_bytes()).hexdigest(),'reading_method':'read工具连续小段通读；脚本仅用于精确引用/ID/覆盖schema生成与校验，不替代语义阅读','read_ranges':[[1,100]]+[[i,min(i+149,2500)] for i in range(101,2501,150)]+[[2501,2531]],'reader_total_lines':2531,'reader_output_truncated':False,'reader_read_full':True,'reference_reads':{'LOCALIZATION_BRIEF.md':'1-65','WORK_ORDERS.md':'1-48','characters-primary.md':'1-277（原请求发生裁剪，随后补278-377，已全读）','characters-support.md':'1-128','world-and-plot.md':'1-150、151-300、301-406；完稿前全读复核，无裁剪'},'scene_count':len(scenes),'row_count':sum(len(s['rows']) for s in scenes),'unique_row_count':len(rowmap),'alias_count':sum(len(s.get('aliases',[])) for s in scenes),'finding_count':len(findings),'finding_counts':dict(collections.Counter(f['severity'] for f in findings)),'limitations':['所有read_full仅指本包工单文字已完整通读，不等于完整游戏全文/运行验证','code仅inventory；嵌套JSON实显用途待核；未做图片/音频/实机验证','未正式应用、未approved、未改译文或catalog、未部署','世界观参照已补读复核：W17幼崽/成人回忆边界、W19女线弟弟驾驶、W20气密套装、D04精灵让步、H01-H05记忆叙述、R06不可靠自夸均已对照；非终裁'],'validation':{'coverage_scene_ids_exact':True,'coverage_primary_row_ids_exact':True,'aliases_preserved':True,'findings_row_ids_valid':True}}
log.update({'input_path':str(R).replace('\\','/'),'input_sha256':hashlib.sha256(R.read_bytes()).hexdigest(),'packet_input_path':str(P).replace('\\','/'),'truncated_ranges':[],'references_read':[{'path':str(BASE/'reference'/n).replace('\\','/'),'ranges':ranges,'read_full':True} for n,ranges in [('characters-primary.md',[[1,277],[278,377]]),('characters-support.md',[[1,128]]),('world-and-plot.md',[[1,150],[151,300],[301,406]])]],'world_reference_recheck_completed':True})
log['references_read'] += [{'path':str(BASE/n).replace('\\','/'),'ranges':ranges,'read_full':True} for n,ranges in [('LOCALIZATION_BRIEF.md',[[1,65]]),('WORK_ORDERS.md',[[1,48]])]]
for f in findings:
    f['reference_keys'].append('world-and-plot:11-17,390-406')
# 最终世界观复核只更新参照，不改变原packet、别名或分支身份。
(OUT/'findings.jsonl').write_text(''.join(json.dumps(f,ensure_ascii=False)+'\n' for f in findings),encoding='utf-8')
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'scenes':len(scenes),'rows':log['row_count'],'findings':len(findings),'counts':log['finding_counts'],'results':dict(collections.Counter(c['result'] for c in coverage))},ensure_ascii=False))
