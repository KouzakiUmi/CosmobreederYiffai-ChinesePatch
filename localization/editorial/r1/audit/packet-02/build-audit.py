from pathlib import Path
import json,hashlib,re,collections
BASE=Path('localization/editorial/r1')
OUT=BASE/'audit/packet-02'
P=BASE/'corpus/snapshot-01/packets/packet-02.json'
R=P.with_suffix('.reader.md')
scenes=json.loads(P.read_text(encoding='utf-8'))
findings=[]
def add(sid, lo, hi, severity, category, proposed, reason, refs=None, status='proposal'):
 s=next(s for s in scenes if s['scene_id']==sid)
 rows=[r for r in s['rows'] if lo is None or lo<=r.get('line',-1)<=hi]
 assert rows,(sid,lo,hi)
 ids=[r['review_row_id'] for r in rows]
 aliases=[]
 for a in s.get('aliases',[]):
  ar=[r for r in a.get('rows',[]) if r.get('unit_id') in {x['unit_id'] for x in rows} or r['review_row_id'] in ids]
  aliases.append({'scene_id':a['scene_id'],'mode':a.get('mode'),'rows':ar})
 f={'finding_id':f'P02-{len(findings)+1:03d}','scene_id':sid,'row_ids':ids,'severity':severity,'category':category,'source_quote':'\n'.join((r.get('speaker')+': ' if r.get('speaker') else '')+r['source'] for r in rows),'current_quote':'\n'.join(r.get('current_line') or '' for r in rows),'proposed_zh':proposed,'reason':reason,'evidence_level':'E1：包内完整场景原文、当前归档与控制上下文直接对照；非实机验证','evidence_refs':[f"{s['logical_path']}/{s['root']}#L{r.get('line')} | {r['unit_id']} | {r.get('occurrence_id')}" for r in rows],'reference_keys':refs or [],'status':status,'apply_scope':'scene_draft_only','branch_context':{'mode':s['mode'],'root':s['root'],'controls':s.get('controls',[])},'stable_ids':[{'review_row_id':r['review_row_id'],'unit_id':r['unit_id'],'occurrence_id':r.get('occurrence_id'),'location':r.get('location')} for r in rows],'aliases':aliases}
 findings.append(f)
add('SCc3ad59fdff3438ca',806,807,'B','idiom','怎么，把我的钱拿光还不够？拿完就赶紧滚吧，小混混！','take off 是赶客，不是中性提议；当前“接下来你怎么不走人呢”照搬反问结构，怒气与上一句讨钱语境衔接生硬。')
add('SC3380c585541b394c',1463,1464,'B','idiom','大多数科博德都不爱玩这些精神把戏。你要是没兴趣，我也理解。对我来说，随便一根棍子、一截绳子就够了……直接动手，多省事，你说是吧？','该else分支以棍绳的直接手段反衬PSY；“全都直接来的”不成自然中文。保留mind games双关，不把奴隶商人误写为心理咨询。')
add('SC84f50545ab568f13',2114,2115,'B','idiom','Tomcat：[好啦好啦，你是我们的顶尖特工，可又不是专门追踪气味的猎犬。没找着也不奇怪。]','此处在安慰发现弟弟一直近在咫尺的姐姐；“气味猎犬／这种事总会发生”逐字感重，未把“能力强不等于能嗅踪”的安慰落地。',['characters-primary:Mauser资料兴奋及Yiffany亲属分支'])
add('SC0cf0a0ca5caff10d',2730,2730,'B','meaning','Bossu：[伊法妮，抓到了本地动物，干得好！]','fauna 是动物的集合名词，不是捕获“动物群”这个研究门类；当前宾语显著生硬。')
add('SC0cf0a0ca5caff10d',2734,2738,'B','idiom','Mauser：[是啊，你和本地动物越亲近，我们能收到的数据也就越有用！]\nYiffany：[放心吧，伙计们，这套我熟。我会拿出和动物打交道的本事，好好陪陪它们……它们一定会喜欢的，跟以前出任务时一样！]','work my magic 是发挥拿手本领，不是新增动物魔法设定。后句give them attention 与前句培养亲密度呼应；现译“动物群魔法”破坏专业与调侃的切换。',['characters-primary:Yiffany有经验不等于万能'])
add('SCfa5abde862c1f019',3138,3143,'A','meaning','Bossu：[斯凯菲亚的精灵虽然全是雌性，却并非全都长生不死。她们能与任何物种的雄性繁衍后代，也因此逐渐带上了越来越多凡俗生物的特征。]\nYiffany：[等等，也就是说，有些精灵真的长生不死？]\nBossu：[没错。至少据我们目前掌握的情况是这样。]','may all be...but 在此是让步“虽然”，不是物种性别尚不确定；当前“也许全是”改变判断。mortal characteristics 直译“有朽特征”难懂，连读后自然表达。')
add('SCfa5abde862c1f019',3147,3149,'B','idiom','Bossu：[别光顾着惊叹。要挡住那些年轻精灵的攻击，你得时刻保持警惕。]\nYiffany：[对，得集中精神。]','don’t give in to awe 在惊叹一百岁还年轻的上下文中是收心提醒，“别向敬畏屈服”过度庄严且不像现场简报。')
add('SC203f504ddad4428c',3080,3081,'A','meaning','Bossu：[那座老太空站里的许多机械，都配有纳米机械回收系统。]','built with ... systems 指构造中配备回收系统；当前“都是用…造出来的”错成生产手段，与后文自我修复的说明脱节。')
add('SC203f504ddad4428c',3082,3083,'B','voice','Yiffany：[纳米机……什么肛来着？]\nBossu：[简单说，就是它们能不停地自我修复。]','源文将nanomechanical故意听乱并拐到anal；“纳—诺—迈—什么肛门”只是英语音节转录，中文无法承接前句“纳米机械”。提案保留一次听岔的荤笑，不给角色新增固定口癖。')
add('SC3a3a119fd7820329',3072,3075,'A','meaning','Bossu：[如果这颗星球上还有真正有血有肉、长着皮毛的Fenfen，目前也还没有特工遇见过。我们收到的，只有Fenfen服装散落各处的报告。]\nYiffany：[真神秘！我得多留意才行。]','flesh and fur varieties 在机械复制品对照下指真正的生物个体，不是“血肉与毛皮变种”两个变种或变异设定。原文if与yet 的未知状态保留。')
add('SCec58e954ab659019',3090,3091,'B','continuity','Yiffany：[唔，你说是精神力造成的……看来得我自己想办法了。]','“灵能，你这么说”不成口语回应，角色是在抓住总部的线索思考对策，不是重复汇报。术语精神力为本段与包内PSY的暂定统一方向，仍需术语终裁。')
add('SC0c836076db0ee88f',2055,2057,'B','continuity','Bossu：[等一下，小家伙。你的飞船现在只是勉强能飞，只准贴地飞行。我们不能冒险让你再被击落……甚至出更大的事。]','“恐怕只能勉强运转，不过你只能”转折不成立；两项是飞船状态与飞行限制。该SFW女主分支叫“小子”也造成称呼性别漂移，采用不额外设年龄的“小家伙”。')
add('SC6fdb8418c5faf950',3581,3583,'A','continuity','Mauser：[伊法妮，我探测到那颗卫星东北部深处有很强的能量信号。你该找条路进入那片洞窟。]','当前跨框连读成“位于在那颗卫星”，句子断裂；deep 的深处定位也丢失，影响寻找洞窟的指示。')
add('SC60ed91a511e551d2',4694,4695,'B','idiom','Yiffany：[可不嘛，先把那些要往你身体里硬塞的家伙了解个透！]','“把…东西的好信息都拿到”英语名词链生硬，笑点是把fauna info转成对侵入者的情色了解，非赞美信息“好”。')
add('SC60ed91a511e551d2',4702,4703,'B','voice','Yiffany：[哦对，我习惯一拿到就翻到“好看”的那面了。你懂的！]','/GOOD/是强调并暗指情色那面，“/好的/那一面”既译腔也丢掉对正面敌人属性的取舍笑点；不扩写具体图案。')
add('SC156d54281be3db1d',4366,4368,'B','idiom','Tomcat：[更何况，你当年在学院就没破过我的滞空纪录……]\nYiffany：[哼，那是我根本没认真试过……]','could never beat 是既往纪录挑战，当前“永远破不了”将过去说成未来永久断言；“又不是我很努力试过还是怎样”使嘴硬不自然。保留她本人没认真试的说辞，不借男线回忆裁决真伪。',['characters-primary:Yiffany好胜与脚环纪录分支'])
add('SCd3fafd3fc4ec71b5',4398,4399,'A','meaning','Yiffany：[啧，希望那个猥琐的科博德没把我给骗了……汤姆猫，能帮我扫描一下这些卡吗？]','just scam me 是刚买后担心上当，不是“不是只骗了我”的范围否定；现句易理解成担心受害者不止自己，与要求扫描核货的意图不符。')
add('SCce26cc53dbd39f07',1207,1209,'B','continuity','要我说，这精灵拆信刀可真精巧！轻得跟羽毛似的，就像穿上精灵做的裙子那种轻飘飘的感觉……当然啦，那些裙子我可一点都不了解！','“就像…会让你感觉的那样”英语从句悬空；需让裙子造成轻盈的联想自然接到心虚否认，保留商人玩笑不新增穿着经历。')
add('SCde4ad2fe0ab8d046',2351,2352,'B','voice','Bossu：[不批准，特工。贴地飞行限制仍然有效。不过你的飞船已平安抵达你所在的位置。]','NEGATIVE 回答许可应为不批准；RE- STRICTIONS为排版断词，不是角色口吃或拉长音，当前“限——制”制造不必要演出。',['characters-support:Bossu规程与断词'])
add('SC3011f2ede9bd4f18',2899,2902,'B','continuity','Yiffai：[“物理”攻击？那相对的是什么攻击……？]\nBossu：[之前有特工报告说，Blocker怕的是“精神”攻击。我们当时认为这些报告不可靠，没有采信，不过……]','当前PHYSICAL残留英文，使物理／精神对举失效；不是图鉴名强译工单，Blocker暂保留不擅立新译名。')
add('SC7aaea4356d5dbc8a',1990,1993,'B','idiom','Yiffai：[喂，总部！我沿着下来的路爬不回去了！现在怎么办？]\nMauser：[别忘了训练时学的，特工！试着换个办法，找找还有没有别的路。]','“另找一条路绕开这个局面”保留英语抽象宾语，面对无法原路返回的问句不自然。重写为具体鼓励，不凭空指定地图路径。')
add('SC567b9e156beb4379',3489,3491,'A','relationship','Mauser：[导航图上应该标着你姐姐的位置！去把她揍醒吧！……不过可别下手太重！]','本男主分支them回指单一姐姐，不是复数他们。控制条件为未击败StarkillV3，不混同女线弟弟。',['characters-primary:Yiffai姐姐关系'])
add('SC5d3909936e0c2b12',3993,3994,'B','continuity','Tomcat：[嘿嘿，就喜欢看你脸红。祝你顺利追上那只凶巴巴的老蜥蜴！]','当前连读“祝你顺利追上对付那个…”出现两个互不连接的谓语；不能按单框各自润色。catching up 在本段不额外加“对付”。')
add('SC8a2b8e81ea1e21a5',3982,3984,'B','idiom','Tomcat：[别为这块扭结零食犯愁啦！我也不知道矮人为什么会有这东西……不过说不定，吃了它就是他们那么强壮的秘诀！]','get twisted up in a knot 为犯愁的习语并双关pretzel形状；当前要求别把自己扭成结过度字面。保留零食形状的笑点，不补效果数值。')
add('SC7798569b8a1fbb4a',None,None,'B','continuity','感觉涌上心头|复杂难言\n酥麻','两行物品短述连读“生出感觉如此复杂”不是自然中文；提案仅写复杂感受，不凭LuckyBody关联补发情或玩法效果。保留UI分隔符。')
add('SC205dcd8ee4b31d57',None,None,'B','idiom','汪！才刚大获全胜|转眼就败得更惨！','wan/one与ruffer/rougher为犬类谐音；现译“汪的一场／更汪的惨败”读不懂且丢掉rougher的程度对比。提案保留一次源内犬音，不变成全作口癖。')
add('SCc035945720439679',17,18,'B','term','Fox：这名心智被扭曲的特工，将议会剩下的成员逐一抓走，让囚禁特蕾的力量一天比一天衰弱。','同一段council在17、22、28间译成理事会／议会；twisted agent接前文入侵者受控制，机械译“代理人”容易与全作特工脱节。议会为本场暂定统一方向，须术语复审；不把Fox所述升级全知设定。',['characters-support:Fox记忆叙述归属'])
add('SCc035945720439679',22,24,'B','continuity','Fox：议会的智者们仍决心以精神力囚禁特蕾，可一场又一场残酷实验接踵而来……就连Fenfen中最睿智的人，也无法同时应付这么多重折磨。','当前“即便…在…之后…”悬置主语，黑暗实验“摆布”也不自然；整体恢复成员维持囚禁却被多重折磨拖垮的逻辑。fronts是比喻，不新增实际多线战役。')
add('SC4eeb4a129d950b80',11,13,'B','term','没错，年轻的女士。我是恩莉耶，图托恩精灵的不朽至高女领主。你的战斗技艺值得赞赏；就连我这样的长者，看了也觉得十分精彩。','当前对话“恩内莉”与本包字典ClassicEnelye“恩莉耶”不一致。此处只建议以已有字典名为锚整段自然化，不在本轮批准正式译名。')
add('SC6c92dcf306eb4565',80,80,'B','meaning','啊，醒啦，小懒虫！总算连人也醒过来了，嗯？','前段对方仍昏睡但身体反应活跃；rouse the rest of you 对比身体某部分先兴奋、人现在才醒。当前“彻底清醒”抹平rest of you的局部性笑点。证据为同场50–80及后续回话，不另定旁白说话人。')
add('SC2b98992a00a6ce52',143,144,'B','idiom','不过别担心，也会让你尝尝我屁股的滋味——等我先尝够你的再说！','taste of tail 是性语境屁股／身体的隐语，前文明确提到ass、后文grab hips；当前“尝尝我的尾巴”易理解成啃尾巴，不能承接先口交再换体位的期待。不新增已发生动作。')
add('SC374f6d5688afdd2d',2412,2413,'Q','source_uncertainty',None,'原文MIS...ATE为失真残词，当前补成“失……误……”未有完整词证据；其余原样噪音与中文拟声混用。待核原脚本/音效的可辨词策略，不猜成完整指令。',status='needs_evidence')
add('SC0b2a2d5c9e9c6c62',3343,3347,'Q','source_uncertainty',None,'女主史莱姆分支speaker为Yiffany，而Mauser原文喊YIFFAI；当前忠实跟随源文，不能直接报关系错译或擅改成伊法妮。须源作者/触发核验后裁决。',['characters-primary:Mauser.Slime源异常'],status='needs_evidence')
add('SCeed6c44091fb9d0d',None,None,'A','term','手电筒\n照亮|最黑暗的房间。','torch在本作与flashlight为同一道具的英美称法，不是明火火把；当前字典火把与包内多处手电筒提示冲突，误导物品识别。仅本对象建议统一，不把墙上可打碎火把一并替换。',['world-and-plot:I05','world-and-plot:英式用法'])
for f in findings:
 if f['severity']=='Q': f['severity']='B'; f['uncertainty']='Q：潜在B级风险，未确认译错'; f['evidence_level']='E0：已见完整场景，但残词释义/源身份尚缺证据'
 if f['scene_id']=='SC203f504ddad4428c': f['reference_keys'].append('world-and-plot:D03')
 if f['scene_id']=='SCfa5abde862c1f019': f['reference_keys'].append('world-and-plot:D04')
 if f['scene_id']=='SC3a3a119fd7820329': f['reference_keys'].append('world-and-plot:D02')
 if f['scene_id']=='SCc035945720439679': f['reference_keys'].append('world-and-plot:H07')
# 覆盖的程序工作仅做已读场景与稳定ID映射；不代替上游逐100行语义通读。
by_scene=collections.defaultdict(list)
for f in findings: by_scene[f['scene_id']].append(f['finding_id'])
coverage=[]
for s in scenes:
 ids=[r['review_row_id'] for r in s['rows']]
 alias_rows=[r for a in s.get('aliases',[]) for r in a.get('rows',[])]
 allids=list(dict.fromkeys(ids+[r['review_row_id'] for r in alias_rows]))
 fs=by_scene[s['scene_id']]
 if s['kind']=='code': result='inventory_only';notes='已完整读入候选字符串；CP常量用途未证实，未声称玩家可见，未提自动强译。'
 elif s['kind']=='image': result='inventory_only';notes='仅完整读取文字转录；未检查原图、OCR完整性、重绘或实显，不能视为图像已校。'
 elif fs: result='needs_evidence' if all(next(f for f in findings if f['finding_id']==fid)['status']=='needs_evidence' for fid in fs) else 'issues_found';notes='完整场景连读；所列完整短段提案待复审，其余合法通顺变体保留；控制与分支不重组。'
 else: result='retain';notes='完整场景对照原文与当前归档；本轮保留语义成立的变体。合句尾空行未报漏译；无凭据不增角色身份、口癖或剧情。'
 if s['logical_path']=='datay/scripts_pack.json': result='inventory_only' if not fs else result;notes='仅核嵌套JSON文本内容；runtime_usage_check未验证，待实显用途核验，不以stub/测试占位文案报玩家文本漏译。'
 if s['root'].startswith('Static.') and not fs: notes+=' 原文残词/电流音不猜补整词，保留失真信息边界。'
 if s['kind']=='vsn': notes+=' 已按cut/snap/queue边界和对白人称理解；catalog narrator不等于实际全知旁白。'
 coverage.append({'scene_id':s['scene_id'],'read_status':'read_full','row_ids':allids,'canonical_row_ids':ids,'context_checked':True,'findings':fs,'result':result,'notes':notes,'mode':s['mode'],'logical_path':s['logical_path'],'root':s['root'],'stable_ids':[{'review_row_id':r['review_row_id'],'unit_id':r['unit_id'],'occurrence_id':r.get('occurrence_id'),'location':r.get('location'),'line':r.get('line')} for r in s['rows']],'aliases':s.get('aliases',[])})
OUT.mkdir(parents=True,exist_ok=True)
for name,rows in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
 (OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
log={'packet':'packet-02','input_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [P,R]},'read_method':'functions.read；正文100行分段；程序仅作ID/别名映射与统计，不代替语义通读','actual_read_ranges':[[i,min(i+99,2738)] for i in range(1,2739,100)],'requested_limit_max':100,'actual_lines_read':2738,'reader_total_lines':2738,'truncation_occurred':False,'precision_scope':'原英文、当前归档中文、包内全部控制事件；scene内语义通读，问题短段整体重写；未逐一核源blob及运行时触发','references_read':{'LOCALIZATION_BRIEF.md':[[1,65]],'WORK_ORDERS.md':[[1,48]],'characters-primary.md':[[1,150],[151,300],[301,377]],'characters-support.md':[[1,128]],'world-and-plot.md':[[1,100],[101,200],[201,300],[301,400],[401,406]]},'uncovered':['运行时顺序与用途','原图及全图OCR/布局','实机显示与正式应用','术语最终裁决（参考库已补读，不代表终裁）'],'status':'semantic_reader_complete_references_rechecked','scene_count':len(scenes),'canonical_row_count':sum(len(s['rows']) for s in scenes),'finding_count':len(findings)}
log['input_path']=str(R)
log['input_files_sha256']=log['input_sha256']
log['input_sha256']=hashlib.sha256(R.read_bytes()).hexdigest()
log['read_ranges']=log['actual_read_ranges']
log['truncated_ranges']=[]
log['reference_recheck']='world-and-plot全文406行补读；D02/D03/D04/H07/I05与本包复核，新增torch/flashlight对象术语提案；其余分支与叙述归属边界一致。'
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
counts=collections.Counter(f['severity'] for f in findings)
summary=f'''# packet-02 首轮粗校提案\n\n状态：正文语义通读完成，角色与[世界观参照](<../../reference/world-and-plot.md>)均已补读复核；所有提案均未approved，未回写正式译文。\n\n- 精简阅读稿1–2738行，逐100行read，无输出裁剪；{len(scenes)}场景逐场覆盖，{log['canonical_row_count']}个canonical row。别名与全部稳定ID在覆盖收据中保留。\n- 发现{len(findings)}条：{dict(counts)}。其中2条为潜在B级风险、status=needs_evidence（Q），不视为已证实译错。\n- 开头code仅候选字符串inventory；image仅文字转录inventory；嵌套scripts_pack仍待运行用途核验。\n\n## 高风险连续段\n\n1. 女线SFW东北洞窟提示“位于/在”断裂并丢deep；男线SFW光电击器祝语“追上/对付”断裂。\n2. 捕获动物通讯把惯用表达译成动物魔法；纳米系统把“配备”错成生产材料/方法，影响后续自修复解释。\n3. 精灵图鉴may...but让步误作推测；机械Fenfen/真实生物对比误作血肉毛皮变种。\n4. 男线Endgame以复数他们回指姐姐；Enelye场景译名与字典不一致。\n5. 卡牌情色玩笑、脚环嘴硬、商人轻盈裙子否认需要完整短段精修，不逐词替换。\n\n## 新证据及边界\n\n男主Bigbold场景明确自称21岁、首次任务；女主BigboldV2自述22岁荣誉毕业及弟弟打破最年轻记录。均为对应场景本人自述，不能合并男女路线经历，也不借测试证件台词泛化年龄。Fenfen历史段实际prefix为lang(Fox)，不按catalog narrator冒充客观旁白；Traeh与议会历史仍保留叙述归属。女主Slime喊YIFFAI与Static残词保留为源/解码待核。\n\n## 后续工单\n\n优先独立复审A项及跨框断裂，再按场景精修习语和专业/玩笑切换。已补读世界观参照，复核PSY/灵能/精神力、council、Lighttazer及手电筒对象边界。新增SpecialTorch字典“火把”与同一道具flashlight不一致的A项；墙上可打碎火把不在此替换范围。术语仍待终裁，本包不作全局规则。所有段落稿须另做实际节点映射，不能按句数切回脚本。\n\n## 验证范围\n\n执行：人工式完整语义阅读、JSONL结构/场景唯一性/稳定ID映射检查。未执行：正式应用、构建、部署、Git写、图像验证、运行时遍历或实机验证。数据入库与已读不等于发现终审。\n'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
assert len(coverage)==len(scenes)==len({c['scene_id'] for c in coverage})
assert set(c['scene_id'] for c in coverage)==set(s['scene_id'] for s in scenes)
for c,s in zip(coverage,scenes): assert set(r['review_row_id'] for r in s['rows'])<=set(c['row_ids'])
print(json.dumps({'scenes':len(coverage),'canonical_rows':log['canonical_row_count'],'findings':len(findings),'severity':dict(counts),'results':dict(collections.Counter(c['result'] for c in coverage))},ensure_ascii=False))
