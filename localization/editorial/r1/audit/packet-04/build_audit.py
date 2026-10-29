import json, hashlib, re
from pathlib import Path
BASE=Path('localization/editorial/r1')
PACK=BASE/'corpus/snapshot-01/packets/packet-04.json'
READER=PACK.with_name('packet-04.reader.md')
OUT=BASE/'audit/packet-04'
scenes=json.loads(PACK.read_text(encoding='utf-8'))
byid={s['scene_id']:s for s in scenes}
findings=[]

def add(sid, lo, hi, severity, category, proposed, reason, refs=None):
    s=byid[sid]
    rows=[r for r in s['rows'] if (lo is None or (isinstance(r.get('line'),int) and lo<=r['line']<=hi))]
    assert rows,(sid,lo,hi)
    ids=[r['review_row_id'] for r in rows]
    # Alias rows remain attached by source line, without merging different scene entities.
    alias=[]
    for a in s.get('aliases',[]):
        rr=[r['review_row_id'] for r in a.get('rows',[]) if lo is None or (isinstance(r.get('line'),int) and lo<=r['line']<=hi)]
        alias.append({'scene_id':a['scene_id'],'mode':a.get('mode'),'row_ids':rr})
    findings.append(dict(finding_id=f'P04-{len(findings)+1:03}',scene_id=sid,row_ids=ids,severity=severity,category=category,
      source_quote='\n'.join(r['source'] for r in rows), current_quote='\n'.join(r.get('current_line') or '' for r in rows),
      proposed_zh=proposed,reason=reason,evidence_refs=[s['logical_path']+' :: '+s['root']]+[r.get('location','') for r in rows]+[r.get('unit_id','') for r in rows]+[r.get('occurrence_id','') for r in rows],
      reference_keys=refs or [],status='needs_evidence' if severity=='Q' else 'proposal',apply_scope='scene_draft_only',
      branch={'mode':s['mode'],'root':s['root'],'controls':s.get('controls',[])},aliases=alias))

add('SC81615de25860505a',3038,3039,'A','meaning','Bossu：[那座旧太空站里的许多机械装置，都配有纳米机械回收系统。]','后文解释它们能无限自修，built with表示配有系统，不是材料由该系统制造。须连同后面的自修与无法拆解读。',['characters-support:Bossu'])
add('SC1ed8b1131ee2b80b',3194,3205,'B','continuity','Bossu：[斯凯菲亚的精灵虽说全是雌性，却并非个个都能长生不死。她们能与任何物种的雄性交配繁殖，因此也逐渐带上了越来越多凡俗生物的特征。]\nYiffany：[等等，也就是说，还真有精灵能长生不死？]\nBossu：[根据目前掌握的情况，是的。那些在外头露面、参与战斗的，无疑都还年轻，最多也就一百岁。]\nYiffany：[这……哇……]\nBossu：[别光顾着吃惊。想挡住这些年轻精灵的攻击，你得时刻留神。]\nYiffany：[对，得集中精神。]','让步may all不是无证推测“也许全是”；“有朽特征”“就我们所能看出的而言”“别向敬畏屈服”阻碍问答。整段保留Bossu的情报限定与百岁反差，不把youngster写成人类未成年。',['characters-support:Bossu'])
add('SC2df2a934a81fcf00',3135,3136,'B','continuity','Yiffany：[唔，原来跟灵能有关啊……看来还得我自己想办法。]','“灵能，你这么说”机械保留you say语序，接不上自行推理的回应。保持不擅补具体解法。',['characters-primary:Yiffany'])
add('SCc71d1f77950ab7b0',3300,3302,'B','gameplay','Gitgud：[攻击时虽然不能走动，但挥击后的收招阶段仍然可以跳跃，借此恢复一点机动性！]','“挥击恢复期间”易与恢复体力混淆；这里是挥击后收招，可跳而不能走动的操作差别须清楚。',['characters-support:Gitgud'])
add('SC5152e102c93a447b',3321,3323,'B','voice','Gitgud：[外面不少食物都能帮你恢复一点生命，有些还能提升属性！碰上难对付的野兽，就多备些食物。]','“治疗你一点”是生硬施受；末句补出原段指代食物，让实用教程顺着恢复—增益—备粮讲完。',['characters-support:Gitgud'])
add('SCbbaaeb5b391ca914',2335,2337,'Q','source_uncertainty',None,'同一Yiffany连续两句中出现MAUSER ORDERS IN... WHAT?，原文角色/错位或刻意迷糊尚不明。现译把它平整成第二遍呼叫，不能据此断言准确；需核原控制与演出，不擅改说话者。',['characters-primary:Yiffany'])
add('SCedea7267588eb179',3630,3632,'Q','source_uncertainty',None,'女线源文也直呼YIFFAI；应列原文称名疑点，不能把当前忠实沿用的伊法伊直接报成译文弄错性别或亲属。需核触发、原作者意图。',['characters-primary:事实等级与分支红线'])
add('SCdf8c740516154c40',2655,2655,'B','continuity','Bossu：[明白，汤姆猫。伊法妮探员，我们会尽一切——]','寻求任何是英语残句直译，不像紧急支援说到一半被切断。“尽一切——”仍保留未完成，不擅补已经找到营救方案。',['characters-support:紧急救援'])
add('SCd2210497c5398b29',3983,3988,'B','continuity','Tomcat：[哇，你倒真不害臊啊，姑娘。换了我可不会——]\nYiffany：[你敢说你现在就不偶尔吃点软食？]\nTomcat：[喂，听、听我说，那是……那完全是……我还有报、报告要写，再、再见！！]\nYiffany：[嘻！]','当前“现在还是不偶尔吃”否定层叠，读成预设他不吃，削弱她抓住怀旧反将一军的效果；HEE是得逞笑声，不是招呼“嘿”。',['characters-primary:Yiffany','characters-support:Tomcat'])
add('SC70cabd30400d26f1',1974,1977,'B','continuity','Tomcat：[没——错！我们的卫星一直把你的近场数据传回总部。它传输延迟低，数据量虽小，也刚——好够咱们保持联系。]','当前“源源不断地传来/你的近场数据回总部”连续两框合读仍语序破碎，且low latency small data stream应自然交代通信能力限制。',['characters-support:Tomcat'])
add('SC098d910f490ceae6',4208,4214,'B','continuity','Yiffany：[我说，不知道有没有人——]\nTomcat：[行了行了，我以前穿过兽装。怎么了？！]\nYiffany：[你那个性爱俱乐部里，有人戴过这么锋利的爪子吗？]\nTomcat：[都说多少遍了，那不是性爱俱乐部！……而且没有。那些确实是服装配件，不过磨得特别锋利，必要时完全能当武器。]','AND NO是在回答有没有人戴过，不是“不对”推翻自己或对方。保留否认俱乐部说法、再回答爪子问题两层回应及后续实用说明。',['characters-support:Tomcat','characters-primary:Yiffany'])
add('SCd73988c79d0f4049',3953,3956,'B','idiom','Tomcat：[你拿的这颗辣椒可够辣的。只要吃得了辣，应该能帮你恢复不少！……光冲着这个，跟那些蛮横家伙打一架好像也值了！]','almost makes it worth不是“差点就值得……一战”的尚未发生事件；是掂量战利品后半调侃地觉得值得。real good不保证完全恢复，不能强化为恢复个彻底。',['characters-support:Tomcat'])
add('SC3bf1546196e1da59',634,634,'B','idiom','下次我一定不再乱管闲事、乱闯不该去的地方了！','poking my nose习语的重点是越界打探；直译鼻子伸进去会把自省误读成具体动作，保持不再乱探的完整意思。')
add('SCef111241d8b20356',3257,3261,'B','continuity','Yiffai：[波苏，是这些炮变厉害了，还是我变弱了？]\nBossu：[这些炮似乎已经有一阵子没受损、不用自我修复了，因此现在能以更高功率开火。]\nYiffai：[真——棒，这麻烦来得可真是时候……]','源are there疑似these笔误由后句these cannons支持，当前“是有更强的”把眼前比较改成存在性提问；反讽just what I needed不能直译成真需要应付。未添加机制数值。',['characters-primary:Yiffai'])
add('SC6c6396e08a205b23',2814,2818,'B','voice','Bossu：[啊，干得好！看来它们——]\nYiffai：[它根本不是我的对手！我先“嗨呀”，再“啊哒”，然后——]\nBossu：[冷静点，伊法伊。]\nYiffai：[啊、啊，抱歉，我不闹了……]\nBossu：[咳，我刚才说到……]','现译“我会乖乖的”给认真收敛的年轻探员加了幼儿撒娇腔；保留兴奋被打断、道歉回到听讲，不否认其实力。',['characters-primary:Yiffai'])
add('SCc8706a14172fbaba',3770,3775,'A','term','Tomcat：[喂？哦！你不是伊法伊探员！那小狗崽真让几只科博打败了，又把无线电弄丢了……又来一次……]\nYiffai：[……？！]\nTomcat：[但愿那个小混蛋醒过来后能找回来！]\nYiffai：[……]','当前把双方通话装备radio译成只能接收的收音机，且KOBO同一套装在本包叫科博/科博德又漂成狗头人。此处是见外观误认，不是证实主角被抢。科博为本包既有暂名，非全局终裁。',['characters-support:Tomcat'])
add('SCc4c2b7eda0f9ae23',4134,4138,'A','gameplay','Tomcat：[你这条小裙子可真可爱。]\nYiffai：[这……这是任务需要，好吗！！]\nTomcat：[嗯哼。穿上它，站在会坍塌的地面上多久都行，还能顺便扮可爱！]\nYiffai：[看着……什、什么？！算了，伊法伊通话完毕！]','当前把as long as you want的时长误成“想怎么做就怎么做”，关键地形玩法丢失。S-S...不能像当前译文直接补成“性感”；后半仅示不补词的犹豫方向，最终断音须按另一条Q补证后裁定。',['characters-primary:Yiffai'])
add('SCc4c2b7eda0f9ae23',4138,4138,'Q','source_uncertainty',None,'SFW上句明确cute，下句却保留LOOK S-S...，可能是清洁版替换遗留。不能证明他原本想说sexy，建议回填前核SFW原作/演出；上一条只给忠实保留截断的草案，不把性感当事实。')
add('SC7724d8e8640a8af2',4108,4111,'B','meaning','Tomcat：[哎哟，你刚捡到的是牵引绳？没想到你还需要这个呢！]\nYiffai：[喂、喂！！我真的、真的不需要！！只是……有它比较安心，仅此而已！]','comfort thing承接被调侃仍需要牵绳，是情感安慰/安全感；当前无据缩成“穿着舒服”。不新增特殊癖好或童年事实。',['characters-primary:Yiffai'])
add('SC05a8518f0254a8b3',None,None,'A','continuity','吱吱怪缩在笼子深处，紧张地望着你。\n你照料吱吱怪时，他会高兴地吱吱叫。真是只好宠物！\n你一来，吱吱怪就精神起来。现在跟你相处，他似乎放松多了。\n吱吱怪拼凑出了一个逃脱装置，却一直没用……','四段是不同亲密度状态，非同次连续经历。首段from the back of his cage被拆成不成立的“从后面/他的笼子”，perks up也不是竖起身子；完整重写各状态、不调整状态映射，分行符需后续排版确定。')
add('SC1327cc8a29dac457',None,None,'B','idiom','红牛虽说懂得遮羞，却认为大大方方展示自己那根硕大的家伙，是对旁人的尊重——闯入者也不例外。可别因此分了神！\n红牛是如今被称作艾斯卡姆尔的矿井里的古老居民。他会赶走所有闯进“自己”地盘的人，也一直盼着独角兽归来……','modesty是性器裸露语境的遮羞，不是谦逊；full endowment译“完整的禀赋”无法落地笑点。两卡面叙述独立，保留其观念为角色特点，不改成普遍礼仪。此为段落提案，非固定14行回填。')
add('SC04183b08a8d59070',None,None,'B','continuity','\n挥爪怪体型笨重、行动迟缓——在猫科动物里可不多见。只要不从它们正前方经过，就不会有什么危险；一旦挡在前面，它们可会毫不犹豫地挥爪清路！','“挥爪只有在有人……”丢失生物名称的名词身份，“清开面前的路”欧化。暂用能识别动作的挥爪怪作待核名称，保留只在正面危险，不擅加攻击范围/时机。空白卡面仍保留，译名须另与dictionary核对。')
add('SC687e2ba919db7741',None,None,'B','voice','茶是茶，\n可这到底放了多久……？','HOW OLD IS IT用于变质旧茶是放了多久，不是物体有多老；短名与说明合读才是嫌弃笑点。具体分行等待UI验证。')
add('SC350869d0807dfeb5',None,None,'Q','usage_unverified',None,'TazerTrainer为装备键，TRAINER可能指驯兽用途的工具而非“训练者”这个人。当前武器命名疑点，需补读物品/功能上下文，不能仅凭键名强行定译。')
add('SCad1dcb4061c6601c',2533,2540,'Q','source_uncertainty',None,'碎裂通信中SAVE IT的it对象不明，现译“救它”把救援对象固定成非人；应核信号残词与演出，不擅补救姐姐/救世界。末句似曾相识不等于此时已认出亲人。',['characters-support:Starkill'])
add('SC3556c0b1a26b76d9',36,38,'B','continuity','lang(Fox)：凶悍的首领不在了，那群投机之徒便四分五裂，纷纷逃离Fenfen议会的追击。不过，这可算不上Fenfen的凯旋时刻……','当前“逃离理事会的力量”生硬且与本场反复“议会”漂移。fleeing from powers指对力量的畏避，提案追击是过强动作，需改用“在Fenfen议会的威势下四散逃窜”，不添实际追击事实。',['characters-support:Fox'])
# Ensure proposal does not assert pursuit absent from the source.
findings[-1]['proposed_zh']='lang(Fox)：凶悍的首领不在了，那群投机之徒便四分五裂，在Fenfen议会的威势下四散逃窜。不过，这可算不上Fenfen的凯旋时刻……'
add('SC952e581f7322b50b',211,213,'B','voice','哎呀，瞧瞧。原来你还真不是在装睡啊？没事，大个子，躺好，让我伊法妮来处——','good ol’是亲切又自信的自称，不是老年身份；“这儿的老伊法妮”拗口且易给无据年龄。保留她此前误认昏迷为装睡的迟到发现，不把narrator当全知旁白。',['characters-primary:Yiffany'])
add('SCdf603b6c82695577',101,104,'B','continuity','她可、可喜欢你肉棒上侧那些小凸粒了。光是它们长的位置，就能让她兴奋得不行。可、可我没有！！我只是觉得它们硬中带软，是个值得记下的精妙细节！你每次顶到我的……我才没有爽疯呢……啊！','Something about their location really got her riled up不是“不知是不是因为所在地”对因果的无据怀疑；location是身体位置非地点。“记录细节—嘴硬—动作露馅”须连读，保留他引用姐姐的说辞而非全知事实。',['characters-primary:Yiffai'])
add('SCc9710272ec73d1ea',40,41,'B','voice','干得漂亮，姑娘！你和你那小狗崽弟弟，真把下面的坏蛋收拾干净了！不过就算出了名、得意起来，也别忘了总部的我们啊，好吗？','grrrrl残留英文破坏祝贺口吻；fame goes to your heads是带笑提醒，不必僵成“等名气让你们忘乎所以”。说话归属据同段HQ与grrrrl关联Tomcat但未做视觉验证，不宣称已实显确认。',['characters-support:Tomcat'])
add('SCc9710272ec73d1ea',61,61,'B','format','[PPP以拥有这两位探员为荣。]                      ——署名：波苏','人事报告末尾SIGNED, BOSSU为可读署名，不是控制指令；当前留英文与中文报告不连贯。保留署名独立及格式，不把所有narrator行都说成Bossu当场发言。',['characters-support:Bossu'])

add('SCf89ffbe39fe88fa1',3236,3240,'A','term','Yiffai：[又是这些家伙……]\nBossu：[那一区的撞击机器人，装甲似乎比你之前见过的更厚。尽量别让它们撞到，那层额外装甲肯定也让它们撞得更疼。]','世界参照D01已核Bumper为失控巡逻机器人，当前撞击兽误成生物；同一段装甲—撞击伤害因果也应自然连读，不添伤害数值。',['world-and-plot:D01'])
add('SCcc794b01eea2df32',None,None,'A','term','照亮最黑暗的房间。\n手电筒','world I05及英式用法段确认torch/flashlight是同一手电，当前火把改变了装备类型；与本包MacsenDark现译手电筒互证。不作英文torch全局规则。',['world-and-plot:I05','world-and-plot:英式用法'])
# Supplemented completed world reference; bind only relevant scope, not universal truth.
for f in findings:
    if f['scene_id']=='SC81615de25860505a': f['reference_keys'].append('world-and-plot:D03')
    if f['scene_id']=='SC1ed8b1131ee2b80b': f['reference_keys'].append('world-and-plot:D04')
    if f['scene_id']=='SC350869d0807dfeb5':
        f['reference_keys'].append('world-and-plot:I03')
        f['reason']='参照I03补证Trainer是能把特定生物送机库的武器、不同于Trainee新人弱武器。当前TRAINER写训练者可能误作人，待核物品正式命名和完整功能段后拟名；不凭键名全局换词。'
notes={
'SC80dbffa3a4b4d5b4':'保留地震强度与货物大半被埋，未把商人自述扩成客观世界全貌。',
'SCab2419f72e0befa7':'hasItem(Key)与else分别是催促开门/告知要钥匙，两个分支中文对应，未合并经历。',
'SC1881e5dc92d1413c':'依击败Starkill和缺少的飞船零件逐层分支；门卡、洞穴照明、灵能可达与震后藏点信息保留；1774/1791/1798空行已被前句合法消费。',
'SC83aac16ba3b49295':'匿名来者自述曾为Queen办事，差一点有力量换身体与赶快出击承接；1855已合句，不报漏译，不据星号定亲属。',
'SC48cc4c9accffe5d3':'男线独立核，Queen换身体将成而未成；1865空行合句，不与女线合并当前经历。',
'SCf8c62480a20fd0e4':'同类玩笑、繁殖季与请晚饭的转折保留；3047为已合句尾行。',
'SCbbb3f9743ac83409':'SFW只保留被咬与相似性互损，没有把NSFW繁殖季与晚饭玩笑移入。',
'SC751bba20914410de':'保留两种爆雷方法的故意无用、踩雷双关、沉默与假借断线退场，冷笑话在中文成立。',
'SC37328493f75dcf8d':'NSFW先给团队诱饵方案，再发现独行、改用躲俯冲；笑点与尴尬停顿保留，不当真实多人任务。',
'SC85c26ce8e54ee7d9':'SFW弱点是自身攻击时分心与俯冲中出手，没有套用NSFW高潮诱饵方案。',
'SC590c465e89cd507f':'触球—无装备—新力量—听见按键声—同事担心脑震荡—愿意倾听；SELECT与UP+ATTACK动态操作组合保留，2310/2311空行被合句。',
'SCe1a779c61c9843af':'违法币引出绝密任务权限、主角幻想滥用、USL技术解释、Mauser索副本失言；整场包袱递进通顺，4594等空行已合句。',
'SC496237bd51383a3b':'女主救回弟弟：唤醒、旧时打闹回忆、女王抽力、传父亲哨子与驾驶救援；长幼与首任务赠哨保留，不补未说出口的决定。',
'SCa41ed1323c6042e4':'男主救回姐姐：三轮击头、姐姐要五秒缓神、旧时反摔、体虚与代驾；与女线语气不同，未互换长幼。',
'SCfc42c34b7707b552':'SFW关怀小狗、放行、承诺听叫救援、挖出1级门卡，连贯自然；不套NSFW性经历。',
'SC5b08efc340c04910':'第一人称被救者讲述吠犬经历与个人态度变化，不视作主角已发生经历或全知旁白；动作、施受、先恐惧后主动的揭示仍保留。',
'SCc7795e6405707551':'新人的兴奋与受制经历、眼镜丢失、再遇捕获与仍期待任务构成反差；当前断续句多数对应原话未完，不新增自愿或反抗事实。',
'SC63db3a0838280464':'变性后Bossu误认姐姐，实际speaker仍Yiffai；保留道歉与急挂，不当身份互换。',
'SC2d33a135540467ba':'变性后Mauser误认姐姐；源out是结束通话而非空间离开，当前先走了可口语作急挂，保留但后续可统一电台结束语。',
'SC0ba29e6323e29812':'误认海盗—担忧探员—认出套装—愿删记录；未把误认变成主角海盗履历。',
'SC3cc336eda1f609a0':'SFW省去Tomcat同款套装与删记录台词，保留独立控制身份，未补NSFW内容。',
'SC12eb80f200f666ee':'橡皮鸭后句已解释听人谈电脑，技术梗可由上下文领会，保留而不增课外解释。',
'SC9e2981a6f46a8db0':'难得来客的招呼自然，未从匿名标签臆定新身份。',
}
for f in findings:
    if f['severity']=='Q':
        f['severity']='B'
        f['review_state']='Q'
        f['severity_basis']='潜在风险供复核排序，不代表已确认错译；仅status=needs_evidence。'
coverage=[]
for s in scenes:
    fs=[f['finding_id'] for f in findings if f['scene_id']==s['scene_id']]
    uncertain=s['kind']=='code' or any(r.get('current_kind') in ['usage_unverified','nested_json_value_runtime_usage_check'] for r in s['rows'])
    aliases=[{'scene_id':a['scene_id'],'mode':a.get('mode'),'row_ids':[r['review_row_id'] for r in a.get('rows',[])]} for a in s.get('aliases',[])]
    note=notes.get(s['scene_id'])
    if not note:
        if uncertain: note='完整读过此条源文与当前转录（若有）；用途/运行时是否可达未证实，只作清单，不把空译、测试占位或代码常量强判漏译。'
        elif fs: note='已整场核英语、candidate4与所载控制；下列提案仅作用本分支，未列部分保留，物理空白按合句总义判断。'
        elif s['kind']=='ui': note='已合读此键下全部名称/说明或状态文本；中文对象、肯否、数量与功能说明成立，保留现译。仅文本核读，未核UI空间或实际调用。'
        elif s['kind']=='vsn': note='已连读全部语言节点与切镜/音效控制；中文回应、动作施受及信息揭示成立，保留。narrator仅索引标签，实际第一人称按场景读，未凭画面ID宣称视觉身份。'
        else: note='已完整读本entry；'+s['root']+' 的招呼/反应/提示在当前语境可自然成立，原文指向、否定和条件未见须改项，保留。匿名星号不凭空定名，变身反应不外推常态。'
    result='inventory_only' if uncertain else ('issues_found' if fs else 'retain')
    if fs and all(f['status']=='needs_evidence' for f in findings if f['scene_id']==s['scene_id']): result='needs_evidence'
    coverage.append(dict(scene_id=s['scene_id'],read_status='read_full',row_ids=[r['review_row_id'] for r in s['rows']],aliases=aliases,context_checked=s['kind'] in ['dialogue','vsn'],findings=fs,result=result,notes=note,mode=s['mode'],logical_path=s['logical_path'],root=s['root']))
for name,data in [('findings.jsonl',findings),('coverage.jsonl',coverage)]:
    (OUT/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),encoding='utf-8')
log=dict(packet='packet-04',input_sha256=hashlib.sha256(PACK.read_bytes()).hexdigest(),reader_sha256=hashlib.sha256(READER.read_bytes()).hexdigest(),reader_total_lines=2591,actual_read_ranges=[[i,min(i+99,2591)] for i in range(1,2592,100)],reader_output_capped=False,semantic_read_complete=True,reading_method='read工具每次100行，1–2591实际完整返回；程序仅提取已读证据及校验覆盖，不计为阅读。',reference_reads={'LOCALIZATION_BRIEF.md':'1–65','WORK_ORDERS.md':'1–48','characters-primary.md':'1–277首次被截，278–377补读完成','characters-support.md':'1–128','world-and-plot.md':'两次read不存在，最终需补读/明确欠项'},scene_count=len(scenes),primary_row_count=sum(len(s['rows']) for s in scenes),finding_count=len(findings),stage='first_pass_proposals_not_approved',not_performed=['正式应用','逐输出节点映射','实机验证','图像验证','code用途验证','独立二审'])
log['packet_json_sha256']=log['input_sha256']
log['input_path']=str(READER).replace('\\\\','/')
log['input_sha256']=log['reader_sha256']
log['read_ranges']=log['actual_read_ranges']
log['truncated_ranges']=[]
log['references_read']=[{'path':str(BASE/'LOCALIZATION_BRIEF.md'),'ranges':[[1,65]]},{'path':str(BASE/'WORK_ORDERS.md'),'ranges':[[1,48]]},{'path':str(BASE/'reference/characters-primary.md'),'ranges':[[1,277],[278,377]],'initial_output_capped':True},{'path':str(BASE/'reference/characters-support.md'),'ranges':[[1,128]]},{'path':str(BASE/'reference/world-and-plot.md'),'ranges':[[1,150],[151,250],[251,350],[351,406]],'supplemented_before_completion':True}]
log['reference_reads']['world-and-plot.md']='初两次不存在；完稿前已补读1–150、151–250、251–350、351–406，实际全文返回无裁剪；按D01/D03/D04/I03/I05复核。'
log['world_reference_sha256']=hashlib.sha256((BASE/'reference/world-and-plot.md').read_bytes()).hexdigest()
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from collections import Counter
counts=Counter(f['severity'] for f in findings)
summary=f'''# packet-04 首轮连续语境粗校\n\n状态：文档与提案，未 approved，未正式入库。\n\n## 实际范围\n- 精简阅读稿2591行，已用26次read（每段100行，末段91行）完整看到；无裁剪。不是搜索或程序遍历代读。\n- {len(scenes)}个场景、{log['primary_row_count']}个主行逐场景留覆盖，aliases单独保留全部rowid；SFW/NSFW、男女线、形态不跨实体合并。\n- {len(findings)}条发现，分级：{dict(counts)}；其中27条待复审改写提案、5条needs_evidence（Q状态，B仅潜在风险排序，不表示已确认错译）。code与待核运行用途另有inventory覆盖，不因没有中文强翻。\n- 角色主参照首次长输出发生裁剪，已从278补读到377；配角参照全读。world-and-plot初两次不存在，完稿前已补读全部406行，复核后新增Bumper机械身份、torch手电类型，并以I03补充Trainer待核依据。所有参照仍为草案，非设定终裁。\n\n## 高风险与后续工单\n1. SFW男线ElfBody：地形站立时长误译，另有cute/S-S源替换残留；先核SFW意图再精修，勿自动补性感。\n2. SFW吱吱怪亲密状态：笼子后部指向破句，精神振奋误成竖起身子；各状态分开回填。\n3. SFW女线机器飞虫：配备自修系统误为由系统制造。\n4. 爪子问答：AND NO必须答有没有人戴过，不是“不对”。\n5. 女线坠轨支援、SFW初次装备通信与牵绳反将一军，须按短段顺清句法，不能只换词。\n6. 整段精修优先：精灵寿命简报、红牛卡牌、Fenfen战争叙述、男线大壮兽嘴硬段、结局祝贺与署名；保留演出切镜与说话人边界。\n\n## 保留与证据边界\n- 两线SFW救回亲人的回忆/哨子、NSFW男线违禁币技术解释与索副本包袱、踩雷冷笑话均保留，理由见逐场收据；不为凑数给通顺句换写。\n- 女线YIFFAI称名和MAUSER ORDERS、Starkill SAVE IT、SFW S-S截断是Q，不直接归译者错；不得强补对象或身份。\n- VSN被救者讲述与Fox的lang(Fox)区别于索引narrator；结局多角色也不是同一旁白。匿名*仅沿entry语境读，未声称画面已确认。\n- Macsen多店自述不证实分身；Queen换体将成未成与被控者说辞保留，不并入早期已知信息。\n- 当前归档空行按同场总义核，未用ledger修前稿报当前问题。\n- UI段落重写是语义稿，分行符、固定宽度与每个输出节点另做映射和dry-run；这轮不做实际回填。\n\n## 验证与未执行\n已对JSONL解析、scene唯一/全集、rowid与alias全集、发现引用、输入SHA及范围做静态校验。无正式译文、catalog、构建、游戏或他人文件修改；无安装、Git写、委派、应用、实机或二审。\n'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
assert len(coverage)==len(scenes)==len({c['scene_id'] for c in coverage})
assert {c['scene_id'] for c in coverage}==set(byid)
for c in coverage:
    s=byid[c['scene_id']]
    assert c['row_ids']==[r['review_row_id'] for r in s['rows']]
    assert c['aliases']==[{'scene_id':a['scene_id'],'mode':a.get('mode'),'row_ids':[r['review_row_id'] for r in a.get('rows',[])]} for a in s.get('aliases',[])]
for f in findings:
    assert set(f['row_ids'])<={r['review_row_id'] for r in byid[f['scene_id']]['rows']}
print(json.dumps({'scenes':len(scenes),'rows':log['primary_row_count'],'findings':len(findings),'severities':dict(counts),'packet_sha256':log['input_sha256'],'validation':'passed'},ensure_ascii=False))
