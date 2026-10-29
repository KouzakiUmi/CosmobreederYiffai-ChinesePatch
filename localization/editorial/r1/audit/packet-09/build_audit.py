import json,hashlib,pathlib
base=pathlib.Path('localization/editorial/r1')
p=base/'corpus/snapshot-01/packets/packet-09.json'
reader=p.with_suffix('.reader.md')
scenes=json.loads(p.read_text(encoding='utf-8'))
out=base/'audit/packet-09'
findings=[]
def add(sid, selectors, zh, reason, severity='B',category='continuity',status='proposal',refs=None):
 s=next(x for x in scenes if x['scene_id']==sid)
 rows=[r for r in s['rows'] if not selectors or any((isinstance(k,int) and r.get('line')==k) or (isinstance(k,str) and k in r['source']) for k in selectors)]
 assert rows,(sid,selectors)
 findings.append({'finding_id':f'P09-{len(findings)+1:03d}','scene_id':sid,'row_ids':[r['review_row_id'] for r in rows],'severity':severity,'category':category,'source_quote':'\n'.join(r['source'] for r in rows),'current_quote':'\n'.join(str(r.get('current_line') or '') for r in rows),'proposed_zh':zh,'reason':reason,'evidence_refs':[s['logical_path']+' / '+s['root']]+[r['review_row_id'] for r in rows],'reference_keys':refs or [],'status':status,'apply_scope':'scene_draft_only','branch':{'mode':s['mode'],'root':s['root'],'controls':s.get('controls',[])},'alias_scene_ids':[a['scene_id'] for a in s.get('aliases',[])]})
add('SC42015eed937529ef',[], '一件我已经不怎么穿的衣服。给你穿嘛，肯——定合身！','拉长juuuuust是商贩拖音，不是“刚——刚好”的结巴；保留推销语气和合句空尾。',category='voice')
add('SCcbf017b30c0a13e0',[918],'我马上跟上，嘿嘿！腿有点麻了……','fell asleep是腿麻；“睡麻”不自然且引入睡觉经历。',category='idiom')
for sid in ['SC753054d754f9793e','SCa6c44bc03317898b']:
 add(sid,['gonna need like'],'你得有把钥匙才行，你知道吧……？','like是口语填充，不是“那种”；当前破坏救援提示的表达。',category='voice')
add('SCe121946bba2b1c8e',[],'进来吧，育种同行！','fellow breeder是招呼同行，不是生硬的职位组合。',category='voice')
add('SCb18d51254d264ab3',[2531,2532],'没错。你脚下这块地，是一颗低轨道卫星的一部分。看起来，这里以前是座监狱？','“属于／到了那颗”接不成中文句；须整段重排，保留低轨与监狱推测。','A',refs=['world-and-plot:E07'])
for sid,line in [('SCb18d51254d264ab3',2536),('SCad10f274abd694b4',2568)]:
 add(sid,[line],'所以先确认一下，没人偷偷把它拿走。','snuck away with it是偷拿走装备，不限于穿走；两主角独立提案。',category='meaning')
add('SCb00e0afe598df446',[3095,3096,3098,3102,3103],'随着几百年过去，她们身上逐渐多了凡俗生灵的特征。\n确实，至少据我们目前了解是这样。\n先别顾着惊叹。那些年轻精灵的攻击也不好对付，要时刻留神。','“有朽特征／就我们所能看出的而言／别向敬畏屈服”逐词痕迹重；专业说明和提醒应连贯自然。三个独立发言节点只分别重写，不实际合并跨人台词。',category='voice',refs=['world-and-plot:D04'])
for sid,ls in [('SC46b40e6ec47e8a6d',[3180,3184]),('SCbbbce3c2e89f8789',[3250,3254])]:
 add(sid,ls,'波苏，是这些炮变强了，还是我变弱了？\n太——好了，偏偏又摊上这种麻烦……','原文there疑为these笔误，后文明确谈眼前炮台；“是有更强的”问非所指。末句是反讽，不是正好需要应付。',category='idiom')
add('SCfae065df9d829e6c',[2956,2957,2958,2959,2960],'波苏：这些小型轮式无人机原本负责在矿井里运送矿石和工具。后来有人给它们装上了粗陋的尖刺，还改写程序，让它们追击入侵者。\n伊法妮：看来，有人是真不想让外人来这里的矿井探个究竟。','整段把改装堆叠语和“嗅探／这里的矿井”断裂改成正常技术说明→人物判断；不把入侵者逻辑误成生物本能。',refs=['world-and-plot:D01'])
add('SC3d40dc4f2e053d40',[2564,2565],'对，奶酪口气那家伙说得没错。当地Fenfen说过的话，值得再仔细琢磨琢磨。','CHEESE BREATH是Tomcat损Mauser的外号，不是需要英文保留的新人物；保留插科打诨后回到解谜提示。',category='voice',refs=['characters-support:Tomcat'])
add('SC24fd938ea56dbe72',[3462,3463,3464,3465],'地底太深，扫描信号很难看清。不过我在矿井更深处探测到了几道安全门的信号，你的新门卡应该能打开它们。','clean scans不是“干净的扫描”；整段明确探测限制→发现门→门卡用途。',category='term')
add('SC2d557c5f86ef9923',[],'那附近有不少高等级门，肯定也藏着一张高等级门卡！最好先找到它，看看能打开哪些地方。','“高级门／带你去哪”生硬且等级信息不直观；保留must和best bet的提示语气。',category='gameplay')
add('SC692b79fe52f83d3f',[3731,3733,3734,3736,3737],'怎么回事？这是在开玩笑吗？\n行了行了，真好笑。我知道你在旁边，正为这通恶作剧电话笑得尾巴乱颤呢。\n我这儿还得工作呢！喂，小狗，告诉你主人，她这笑话可一点都不好笑！','“哦什么／是啊哈哈／换点幽默感”不自然；Tomcat误认狗与主人分离须保留，不把主角真的拆成两人。',category='voice',refs=['characters-primary:状态轴','characters-support:Tomcat'])
add('SC6b2494bddfad8bc0',[4016,4017],'以前我就爱穿着自己那套柔道服，在学院里随便逛逛。每次穿上，都觉得自己像个格斗家。','JUST CASUALLY AROUND THE ACADEMY丢失，当前第二行重复“猛”；恢复日常穿柔道服的自信笑点。','A','meaning',refs=['characters-primary:Yiffany'])
add('SCfb0717823b73e65d',[3849,3850,3851],'记得吧，你以前总拿果汁去换肉。后来长大了，又发现还有更省事的换——\n——拿钱去店里换更多肉，没错！','原文没有“跟我”这个交易对象；保留Tomcat未说完、姐姐抢话掩饰的接梗结构，不擅补被截断的真正内容。','A','meaning')
add('SC48a4bc82fca232b0',[4294,4295],'这把手电筒——波苏用的是英式叫法——会自动照亮昏暗的地方。','torch与flashlight是同一物；译为火把制造错误道具差异。中文按笑话功能重写，正式落地需再按显示节点分配。','A','term',refs=['world-and-plot:I05','world-and-plot:英式用法'])
add('SC8b9b4e57a1559d32',[470,471,472],'想当太空海盗？先来把这款“官方海盗光电击器”！当然，还得配艘飞船，再找一帮亡命徒当船员！\n……买了别忘装备上，可不是让你拿来摆着看的。','lighttazer不表示光速枪；保留“官方海盗”商贩推销反差，与装备分析对照。','A','term',refs=['world-and-plot:I03'])
add('SC0961d1327c965343',[],'你手里那是手电筒，还是见了我太兴奋了？\n逗你的，逗你的！你和这把手电筒可真是救星。','同一段flashlight/torch不可译成两个物品；首句保留俏皮双关，不为直白另加身体器官。','A','term',refs=['world-and-plot:英式用法'])
add('SCb4b182f56b8fa17b',[],'你、你好啊，朋友！我倒想好好招呼你，可我被困在这儿，实在施展不开！','cooped up是被关/困着，不是单纯空间太挤。',category='meaning')
add('SCb593a77c58d4a298',[],'真的……我可淡定着呢，救我不用急。我可是这次派来的一线精英，资历也老。把我弄出去，我教你几招，哈哈！','SFW上下文是自夸资历能力，“资深上位特工”平白造职位/性角色；不把NSFW或Top自称全局套入。',category='voice',refs=['world-and-plot:Top/bottom'])
add('SCd557a750eabd9d1c',[2002,2005,2006],'干得好，等着看你的数据。\n哦，还有，记得把新装备装上。完毕！\n知道啦，我又不是小狗崽……','Good boy和pup形成被当幼犬→嘴硬的笑点；“好男孩／Pup”残留使口语和回嘴落点失效。',category='voice',refs=['characters-primary:Yiffai'])
add('SCb19035363d3c7b1f',[2377,2378],'不批准，探员。贴地飞行限制仍然有效，不过你的飞船已经顺利抵达你的位置，没受袭扰。','RE- STRICTIONS为排版断词，不是限——制的表演拖音；NEGATIVE在此是拒绝行动申请。',category='voice',refs=['characters-support:Bossu'])
add('SCb6f36febbdf9e0cd',[3067,3068,3069,3070,3071,3072],'波苏：没错，图托恩矿区的“雷区”可不少。\n伊法伊：……雷区？挖矿不就得到处爆破吗？\n波苏：我是说地雷爆炸。\n伊法伊：对啊，矿里炸东西嘛，可是——\n毛瑟：波苏是说，老矿工在自家矿里埋了地雷，谁敢抢矿，就让谁踩雷！','现译先明确布雷，主角却问爆炸关系；后句又把地雷译回矿区，问答逻辑崩。建议以“爆破/地雷”中文误解重建双关节奏，不逐词硬凑mine/mine/mine；属改编提案须独立复审。',category='idiom',refs=['world-and-plot:mine/miner/mine'])
add('SC9bb714108286af8a',[],'使用门卡很简单：带着它，直接走向能量门就行。门上标着所需等级，你的门卡等级够高就能开门。','“可打开等级不高于门上所标数字的门”把门和卡的比较对象写乱，近乎同义反复；结合本包Keycard1的最低等级说明校正提示，不编新机制。','A','gameplay',refs=['world-and-plot:I04'])
add('SC0010041113ecb2fa',[4330],'我碰到一个发光的球体，它在我身上留了个印记。','glowing漏义；这是球体视觉特征，不应因后文探测不到就删掉。','A','meaning')
add('SC6e4d979cdf3f0678',[4070,4071],'哈，这件衣服既能好好保护我，穿着还显得酷！太棒了！','“又能让大家／会觉得”串联成病句，整句恢复显摆与实用并存。',category='continuity')
add('SC6b99892905a98a17',['SMELLS LIKE'],'透着一股|格斗干劲','气味/战斗劲头的诙谐比喻可保留，但“闻起来像好斗的劲头”搭配不成中文。保留两行控制分隔。',category='idiom')
add('SC86e3980ef25f719b',[],'精灵加成：|闲置时回复精神力','原UI把ELF写成主语，容易理解为精灵自己回复；这是SpecialFap.ElfBuff效果名，但idle具体判定未核，暂不写“静止/未输入几秒”。','B','gameplay','needs_evidence',refs=['world-and-plot:I05'])
add('SCd1604a5e213330b8',['Covered with'],'挥爪的阴茎|长满朝前的|肉刺，|很受一些|特工欢迎。|这些肉刺|柔软有弹性，|能带来|特别的刺激；|它粗壮的双腿|则让每次|猛烈抽插|都格外带劲。','“以兴奋的方式／抽插成为可能”逐词腔拖长科普段；重写因果和主宾，保留柔软与朝向，不把barbs一律写反向倒刺。',category='continuity')
add('SCff66aeccebc5f999',[],'再老练的母狗|也经不起一再撩拨……','can only take so much是忍耐有极限；“只能受这么多，然后”未给数量又悬断，预告语应保留后果省略。',category='idiom')
add('SC21fefe59ec8bd90b',[],'沦为奴隶的狐族特工|自以为能算计所有人，|直到一位陌生人现身……','“由特工变成奴隶的狐／显出他能智胜”生硬；outfox双关依靠狐族身份即可承接。自以为是预告的反转语气提案，不当客观能力认证。',category='voice')
add('SC6649f2ce601a031d',[],None,'路径为female，但英文连续写his/Yiffai；中文忠于当前源文，不能直接报女主误译。须查该nested_json的实际调用与female/male选择，风险为主角/版本串线。','A','source_uncertainty','needs_evidence',refs=['world-and-plot:W04','world-and-plot:W05'])
add('SCa4f1ced2b88fd910',[100,101,102,103],'此后，这名特工似乎先被抽干了心智，再被交给图托恩的另一种本土生物。\n两者似乎有着某种共生关系：剥心魔先抽干受害者的心智，再交由另一种生物圈养，充作能量来源。','“先被／被”重复；原文another local fauna泛指另一种本土生物，不必限定一只；共生为seem阶段判断，不改成因果“以此形成”。各原发言节点分别回填，不跨cut合句。',category='continuity',refs=['world-and-plot:E04'])
add('SCc2e08d1dfc6c98fd',[13,28],'我们族中的超能力者虽有强大的力量，却从未接触过暴力。\n各种超能力，就这样被用作战争的武器。','may have been在让步句不必生硬“纵然或许”；“能力武库被征用为武器”名词堆砌。两个独立节点分别润写。',category='voice',refs=['world-and-plot:H04','characters-support:Fox'])
add('SCb9a3af2c476d7f1b',[30,31],'是黑暗灵能在作祟，还是单纯出于好奇，谁也无法确定。只知道，这位旅人触碰了囚禁特蕾的水晶监牢……','“黑暗的超能力者力量”不自然；保留动机不明，不以访客接触水晶推断故意受控。',category='term',refs=['world-and-plot:H06'])
add('SC8a7eb1951fe9843f',[146,147,148],'来试试你这副新身体的能耐，如何？\n我记得，你是想再比一场吧？不过恐怕你不会喜欢。\n……你的屁股倒可能喜欢另一种“再战”……','同一父亲连续发言突然“吾汝”与前后现代语域脱节；此处不是Pigobin古语分支，不搬其文风。',category='voice',refs=['world-and-plot:W16','characters-support:语域边界'])
# 将已逐场读过的语义判断落为覆盖收据；结构提取只负责ID，不代替通读。
coverage=[]
for s in scenes:
 fs=[f for f in findings if f['scene_id']==s['scene_id']]
 inv=s['kind'] in ('code','image')
 usage=any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in s['rows'])
 if inv: result='inventory_only'; note='已读全部列出字符串；用途未验证，不按未翻译报错，不把常量/错误诊断/内部键强行汉化。'
 elif usage and not fs: result='needs_evidence'; note='已读本条嵌套JSON英文与当前中文；含占位/测试文本的运行时用途未验证，暂保留，不冒称玩家实际显示已验证。'
 elif fs: result='needs_evidence' if all(f['status']=='needs_evidence' for f in fs) else 'issues_found'; note='已连读本场英文、控制与当前中文；问题见段落提案。其余内容保留，不按合句空尾报漏译。'
 elif s['kind']=='vsn': result='retain'; note='已通读整份VSN含演出节点；当前语义与动作/问答基本连贯，保留分支角色与揭示顺序；narrator元数据不作为说话人裁决。'
 elif s['kind']=='dialogue': result='retain'; note='已通读完整entry和所列条件；原意、称呼与回答衔接成立，保留现译；星号不据此认定身份，合句空尾非漏译。'
 else: result='retain'; note='已读全部名称/描述/同组UI；数量、占位和分隔符保留，当前语义成立；未作版面或运行时实测。'
 coverage.append({'scene_id':s['scene_id'],'read_status':'read_full','row_ids':[r['review_row_id'] for r in s['rows']],'context_checked':True,'findings':[f['finding_id'] for f in fs],'result':result,'notes':note,'mode':s['mode'],'root':s['root'],'alias_scene_ids':[a['scene_id'] for a in s.get('aliases',[])],'alias_row_ids':[r['review_row_id'] for a in s.get('aliases',[]) for r in a.get('rows',[])]})
assert len({c['scene_id'] for c in coverage})==len(scenes)
assert sum(len(c['row_ids']) for c in coverage)==sum(len(s['rows']) for s in scenes)
for name,items in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
 (out/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items),encoding='utf-8')
ranges=[[1,100]]+[[n,min(n+149,2448)] for n in range(101,2351,150)]+[[2351,2448]]
log={'packet':'packet-09','input_path':reader.as_posix(),'input_sha256':hashlib.sha256(reader.read_bytes()).hexdigest(),'read_status':'read_full','read_ranges':ranges,'truncated_ranges':[],'references_read':[{'name':'LOCALIZATION_BRIEF.md','read_ranges':[[1,65]]},{'name':'WORK_ORDERS.md','read_ranges':[[1,48]]},{'name':'characters-primary.md','read_ranges':[[1,150],[151,250],[251,377]]},{'name':'characters-support.md','read_ranges':[[1,128]]},{'name':'world-and-plot.md','read_ranges':[[1,150],[151,300],[301,406]]}],'packet_json_path':p.as_posix(),'packet_json_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'method':'read工具分段实际阅读reader全部2448行；程序仅提取已读场景canonical/alias ID和序列化收据，非程序语义扫描。旧ledger不作为当前中文。','limitations':['未运行游戏，未验证嵌套JSON运行用途、动态UI拼接或排版','未approved，未应用正式译文','各建议为scene_draft_only，不能均分回填节点']}
(out/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from collections import Counter
stats=Counter(f['severity'] for f in findings); results=Counter(c['result'] for c in coverage)
(out/'summary.md').write_text('# packet-09 首轮全文粗校\n\n状态：全文已读，提案待复审；非 approved，未回写正式译文。\n\n## 范围\n\n实际以 read 小段连续读完 reader 1–2448，无裁剪；三个角色/世界参考及两份口径全文已读。逐场覆盖 '+str(len(scenes))+' 场、'+str(sum(len(s['rows']) for s in scenes))+' 个 canonical rowid；alias ID另随收据保留。\n\n发现 '+str(len(findings))+' 条：'+str(dict(stats))+'；收据结果 '+str(dict(results))+'。待核状态不是严重度Q，以A/B/C标风险。\n\n## 高风险与后续精修\n\n- SFW女线气闸低轨卫星说明断句失效；柔道服遗漏学院日常穿着；同物torch/flashlight误成火把。\n- 男线传送限制把排版断词当拖音；mine双关须整段重建问答，不逐词硬凑；门卡提示需明确卡等级与门要求的比较对象。\n- Tomcat损友外号英文残留、狗态误认电话逐词腔；专业说明与插话必须分别回填原节点。\n- Werehund父亲连续段突然吾汝；父亲的预言只作本人判断，儿子后置问答与成人主角前段保持区分。\n- female missionLog原文自身为男性Yiffai，风险A、needs_evidence；不擅自改女主。SpecialFap.ElfBuff的idle判定待运行证据。\n\n## 明确保留\n\nF04/F07主要叙事通顺，保留施受与自述层；F07 lighttazer是比喻，不变实际攻击。SFW卡背留白保留。维生素段先假求援后玩笑揭示成立，不以开头认定真实中毒。占位角色/Test文本不补正史。Starkill/Static残片保留失真，不猜补完整指令。Fenfen回忆保留传述与推测，不归全知narrator。\n\n## 边界\n\ncode只列inventory_only，未证用途不强译；nested JSON逐条读过但用途待核。当前中文来自reader的candidate4/current_line，旧ledger仅溯源；合句空尾不报漏译。无构建、游戏、部署、Git写入、正式应用、独立二审或实机排版验证。本目录构造脚本只序列化人工式阅读判断。\n',encoding='utf-8')
print(json.dumps({'scenes':len(scenes),'rows':sum(len(s['rows']) for s in scenes),'findings':len(findings),'severity':dict(stats),'results':dict(results),'reader_sha256':log['input_sha256']},ensure_ascii=False))
