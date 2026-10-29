"""机械装配人工通读后的提案/收据；不是语义扫描器，不改输入。"""
import json, hashlib
from pathlib import Path
from collections import Counter
BASE=Path('localization/editorial/r1')
INPUT=BASE/'corpus/snapshot-01/packets/packet-05.json'
READER=INPUT.with_name('packet-05.reader.md')
OUT=BASE/'audit/packet-05'
scenes=json.loads(INPUT.read_text(encoding='utf-8'))
byid={s['scene_id']:s for s in scenes}
findings=[]
def add(scene, lines, severity, category, proposed, reason, refs=(), status='proposal'):
    s=byid[scene]
    if lines is None: rows=s['rows']
    elif isinstance(lines[0],int): rows=[r for r in s['rows'] if r.get('line') in lines]
    else: rows=[r for r in s['rows'] if r['review_row_id'] in lines]
    assert rows,(scene,lines)
    findings.append(dict(finding_id=f'P05-{len(findings)+1:03}',scene_id=scene,row_ids=[r['review_row_id'] for r in rows],severity=severity,category=category,source_quote='\n'.join(r['source'] for r in rows),current_quote='\n'.join(r.get('current_line') or '' for r in rows),proposed_zh=proposed,reason=reason,evidence_refs=[f"{s['logical_path']}::{s['root']}" ]+[r.get('location') or r.get('unit_id') or r['review_row_id'] for r in rows]+[r.get('unit_id') or r['review_row_id'] for r in rows],reference_keys=list(refs),status=status,apply_scope='scene_draft_only',branch_context={'mode':s['mode'],'root':s['root'],'controls':s.get('controls',[])}))
# 以下判断均来自 reader 逐段实际通读；行号为原资源行，不是输出映射。
add('SC60b2521ed8918dd3',[1062],'B','idiom','你这科博德闻起来还挺讨喜，嘿嘿。你是跟哪路人马来的？','船员在问所属船队/团伙，不是询问与哪些船员共同飞行；前半句也不宜写成“味道对科博德来说可爱”的判断句。',['LOCALIZATION_BRIEF:条件与形态边界'])
add('SC51b737558bc257e4',[1439,1440],'B','idiom','哦？想尝尝我这儿的特制肉？胆子不小嘛，嘿嘿……','商品推销带阴森调侃，当前“我的特别的肉／不能说你没胆子”逐字且绕口；不推定肉的实际成分。')
add('SCfb40649184a4a38a',[1449,1450],'B','idiom','哦？想尝尝我这儿的特制肉？胆子不小嘛，嘿嘿……','男线为独立场景收据；同样的推销反话不必保留英语双重否定句法。')
add('SC1a5d579ca870656a',[2048,2049,2050],'B','continuity','救出特工后，你可以在 P.A.W. 里查看采集到的数据。我们这里也会留一份，你以后随时都能调出来看！','前一框句号截断条件，下一框以“在救下一名特工之后。”孤立开头；应把时间条件前置，数据留存与回看连起来。',['characters-primary:Mauser/自然中文整段重写原则'])
add('SCa7d50e8f2d64a2e7',[3167,3168],'B','term','那一区的弹跳机器人，装甲似乎比你之前见过的都厚。','前文 ClassicBumper/Plus 明说机器/巡逻机器人；这里改称“撞击兽”把同类对象写成兽类，且重复赘重。此处描述性称呼不是全局专名裁决。')
add('SCe810fe1962b453b0',[2963],'A','meaning','波苏，我刚遇到了一只会飞的龙类生物。','draconid 在本包喷火兽条目中属于龙类生物的上位分类，不等于人形龙人；下一句识别为双足飞龙。')
add('SCe810fe1962b453b0',[2968,2969,2970],'A','gameplay','记录上说，双足飞龙在发动攻击的那一刻容易分神。尽量抓住它俯冲的空当出手。','SFW源文仅写发动自身攻击的一刻，当前残留“在高潮的”既无源义又把战斗提示接成病句；不是合句空行漏译。')
add('SC77ea58a1063412b5',[2059,2060,2061],'A','voice','先等等，小家伙。你的飞船虽然还能勉强飞，但只能贴地飞行。我们不能再让你冒被击落、甚至更糟的风险。','女线当前把PUP叫“小子”，与该场Yiffany及后面的GOOD GIRL不符；同时“恐怕…不过…不过你只能”的说明重排为让步—限制—理由，不新增军衔。',['characters-primary:Yiffany/身份','characters-support:Bossu/语域'])
add('SC426f7f71c0aa693b',[1996,1997],'A','gameplay','是先把我的数据存好，万一出事也不怕丢，对吧？','in case 是预防性保存；当前“会在出事时保存”可能使玩家误认为出事自动存档，且后文明确要求站平台手动启动。')
add('SC713dd4f4639c27ba',[4228,4229],'B','continuity','看！是那种鳞片套装的衣身！还记得学院那会儿，你参加的那个性社团吗？','“套装的身体”误作肉体，后半句“就像我们在学院那会儿，你参加的那个性社团”比较对象悬空；用回忆问句衔接随后的Tomcat辩解。',['characters-primary:Yiffany/关系边界'])
add('SC713dd4f4639c27ba',[4233,4234,4235],'B','idiom','Tomcat：那就是闹着玩，主要图个开心、放松一下而已。真的。\nYiffany：可不是，松得很。我还记得你们有些玩具大得吓人。','原文let loose/loose 是“放松／松”的反将一军；当前“放开是放开了”接不到玩具尺寸笑点。保留双方说辞，不把社团性质定为客观事实。',['characters-support:Tomcat/多面性'])
add('SCae76be512589a7df',[4069],'B','voice','姑娘，我可不敢打包票，不过能帮的我一定帮。','当前“不敢喵喵保证”既不成自然搭配，也把原文猫语双关机械展开成叠字叫声。这里只保留熟人帮忙但不承诺的意图，不新增固定喵口癖。',['characters-support:Tomcat/语域'])
add('SCb6f24971b727c80c',[3825,3826,3827,3828,3829,3830,3831,3832,3833],'B','continuity','Yiffany：太——好了！\nTomcat：哇，好大一块肉！\nYiffany：好——大——\nTomcat：你就喜欢能往嘴里塞的大肉，是吧？\nYiffany：还——热——乎——着——\nTomcat：这么大，会不会让你想起那回任务，我——\nYiffany：快——进——我——嘴——里——！\nTomcat：呃，算了。我先不打扰你俩了……','场景是主角盯着肉拖长音、Tomcat越说越被无视；当前“是啊啊／进啊啊 到啊啊 我啊啊”无法成句，且WH-残留英语断词。建议保留夸张节奏和食物双关，不补具体任务内容。',['characters-primary:Yiffany/专业语与玩笑转换'])
add('SC1c0e8e24cfeaa003',[4353,4354,4355,4356,4357],'B','continuity','当初有特工报告自己获得了所谓的“超能力”，我们还把精神科医生请来了！他们说的事也太离谱了：发射星星、打出能量弹……有个犬族的家伙甚至咬定自己能变成野兽！','当前第一句缺“报告”，后面“特工们说的那些怪事…告诉我们的怪事”重复拼接；整段是总部不信怪力的回忆，接主角心虚，不应逐行保留残句。星星/能量弹按能力描述，不把shooting stars误设为天文观测。')
add('SC188abbfbd53fac7b',[4532],'A','meaning','让我猜猜：又碰了一颗传感器完全探测不到的悬浮球体？','sensor dark修饰对传感器不可见；当前“暗色传感球”反而将其说成有传感功能的暗色球，与同包ZenerSquare近场数据完全不可见、后文无数据呼应冲突。')
add('SC188abbfbd53fac7b',[4533,4534],'B','gameplay','是啊。我感觉这股力量能让我更耐打，不过战斗力会下降。','tougher在能力利弊说明里指更能承受伤害，“变得更硬”容易误成硬度或色情双关；该段没有主角开荤笑的信号。')
add('SCbb24ffbfac0746d8',[3140,3141,3142,3143],'B','continuity','斯凯菲亚的精灵虽说全是女性，却不全都能长生不老。几百年来，她们身上凡人的特征越来越多。','may… but…为让步，当前“也许全是”弱化已在讲述的前提；“有朽特征／在数百年的岁月流逝之中”倒装生硬。此为Bossu报告说辞，不外推绝对设定。')
add('SCbb24ffbfac0746d8',[3145,3146,3147],'B','voice','据我们掌握的情况，确实如此。那些公开现身、参加战斗的精灵，肯定都还年轻——最多也就一百岁。','当前“就我们所能看出的而言”明显翻译腔；“年幼者”不如“还年轻”能自然接“一百岁”的寿命落差，不把youngster转为现实未成年判定。')
add('SCbb24ffbfac0746d8',[3149,3150],'B','idiom','别光顾着惊叹。打起精神，才能挡住那些年轻精灵的攻击。','“别向敬畏屈服”把让人回神的提醒译成抽象服从关系；问答正在讲寿命惊讶与战斗专注。')
add('SC46fe33beaab2503d',[3124],'A','meaning','呼叫波苏，收到请回答？','无线电come in不是实体进入。当前“我这就进来”错置动作和意图；本NSFW分支紧跟I HOPE NOT为情色双关，后续整段精修需连同这句回话重建中文笑点，不能因此保留主句错译。',['characters-support:Bossu/语域'])
add('SC54121e70d4d54642',[3063],'A','meaning','呼叫波苏，收到请回答？','SFW平行分支已删双关回复，此处纯粹呼叫；“我这就进来”不是无线电用语。单独记录，不与NSFW当作同场经历。')
add('SC553c64bb4bea4bc3',[3108,3109],'B','continuity','波苏！我遇到一群人形的绿皮蜥蜴兵，看起来很不友好！','“兽人绿色蜥蜴兵”分类叠放不自然，anthro在这里描述人形，并非另加一个兽人种族；接下句由Bossu识别为kobolds，保留先见外观后揭名。')
add('SCe0520bfb2096fa57',[2577],'B','voice','能——再说具体点吗，小狗崽？','PUPPEROO是Tomcat对男主的逗弄称呼，当前原样遗留使中文中断，不应当新专名；拖音只在原有处保留。',['characters-support:称呼矩阵'])
add('SC87c3d069f4408f43',[2664,2665],'B','continuity','已经在查。星际服的降落伞用不了……这个高度，动能制动器也不够用。','紧急技术评估应说明设备制动能力不足，“此高度的动能制动器不足”像设备数量不足，定语关系生硬，降低救援判断清晰度。',['characters-support:Tomcat/紧急救援'])
add('SC87c3d069f4408f43',[2670],'A','meaning','你的信号断断续续的……我没法维持……！','Mauser在总部接线，前半已明说信号衰减；“我撑不住”容易变成本人遭遇物理险境。原文省略keep宾语，建议仍保留未说完的省略，不擅补完整救援动作。',['characters-primary:Mauser/身份'])
add('SC70adcf011b42bbeb',[2239,2240,2241,2242],'B','continuity','Tomcat：心率没升高……\nYiffai：啊？什么？你打给我干什——\nTomcat：血压正常，眼球也没动……可你不对劲啊，小狗崽。','call me up在这里是打电话，当前“你为什么叫我U-”把短语尾词当台词字母；连同前后体征检查重建铺垫，Pup也不应残留为专名。')
add('SC70adcf011b42bbeb',[2244,2245,2246,2247,2248,2249,2250],'B','voice','Tomcat：换成别的外勤，突然弄到一双 Mark IV Cosmoboots，早就乐疯了！\nYiffai：……你是说刚才被扔到我这儿的这双鞋？\nMauser：那可不是普通鞋。\nYiffai：不是？\nTomcat：对，那是/贵得要命/的鞋！限量版！','当前“成为…主人／彻底歇斯底里／昂贵的鞋”像履历与病症描述；这是装备迷见主角无反应后的夸张控诉，重写为自然兴奋并保留贵—限量的落点。品牌型号不擅改。',['characters-support:Tomcat/装备讲解'])
add('SC70adcf011b42bbeb',[2254,2255,2256],'B','gameplay','人在空中时按 DOWN + JUMP，就能使出俯冲踢。踢中能受伤的目标，还能借力向上弹起！','当前整句按英语关系从句层层叠加，“接触到任何会承受伤害的东西”不易一听读懂；把输入、动作、反弹条件顺序讲清，不改按键和命中条件。')
add('SCcfed64c6d940ad62',[3974,3975,3976,3977,3978,3979],'B','voice','老兄。\n章鱼。\n我最爱章鱼了。\n兄弟，给我来点。\n还能变聪明，我正需要呢。\n老——兄……','末句D U D E为同一称呼拉长，不是专名；整段刻意短促地馋食讨要，最后原样英文打断重复催讨的笑点。不新增猫叫。')
add('SC58ccd1b993ca1ca5',['SFWb62610a60cd111d1800a1671'],'B','idiom','科博德蜷起身子，|惬意地依偎在你身边。|真是棒极了的宠物！','bask in your presence是享受陪伴，当前“沐浴在你的存在里”抽象直译，破坏亲密度最高档的自然叙述。保留三段管线仅作段落提案，实际排版另验。')
add('SCe2b05d5a4cb5a705',['CAT:O731e71de3518446fbac9'],'B','idiom','矮人嘟囔着抱怨住处，|却还是冲你|粗犷地笑了笑。','gruff smile不是有粗声音的笑；抱怨与笑之间的转折应自然落地，不新增亲密关系。')
add('SC87699368a000005b',None,'B','idiom','害羞的侦察兵|体会到采集数据的乐趣。','learn the joys是体验其中乐趣，不是“学会乐趣”；完整回忆菜单简介需成自然短段。')
add('SCdb93fddeabca5d30',None,'B','continuity','打败小狼崽后，|往事涌上心头，犹豫不决！','当前把时间条件后置成“回味着，又犹豫着在打败…之后”，中文无法连读。只表达追忆与犹豫，不擅补回忆对象。')
add('SC96a89c88351f6c03',None,'B','term','获得泽纳波','wave在超能力/泽纳取得提示里为“波”，不是水的“波浪”。该nested值运行用途未验证；这是有条件文本提案，不宣称游戏中显示。')
add('SCd8d9edde0d88a8f5',None,'A','meaning','旧杂物','路径是商品displayName，OLD JUNK指旧杂物/旧货，不是店铺。用途仍需运行验证，不能据资源位置声称已经可见。')
add('SC830eb1f5ee0725d9',None,'A','source_uncertainty',None,'路径标male/13而源段写Yiffany/her；当前译文忠实女主身份。须核实际触发、测试数据与路径映射，不能以男线路径直接报中文错人。源中ger亦有拼写异常。',status='needs_evidence')
add('SCa1e42fd2a89cb4a7',[3636,3637],'B','term','你在 Exile 东北部发现的那座宝库，看来很重要。','Exile是绕Tutone的小行星名称；当前“在流放东北”把地名当普通动作名词，地点关系不清。此处暂保留英文专名，译名待统一裁决。',['world-and-plot:E07','world-and-plot:C06'])
add('SC29248fbcf75fe78f',[25,26,27],'B','voice','汪！汪！万岁！\n汪！汪！万岁！\n赞颂宇宙育种者！他们是我们星球的救星！','YIP/YIP/HOORAY把犬类叫声嵌进欢呼，当前原样YIP与“愿…受颂”均妨碍群众欢庆的中文节奏；不是证明所有说话者物种的证据。')
add('SC29248fbcf75fe78f',[40,41],'B','voice','真有你的，姑娘！你跟你家小狗崽弟弟把下面收拾得够干净的！等成了大明星，可别飘得把我们总部的人都忘了啊。','grrrrl是Tomcat拖长的girl称呼，不是人名；当前原样残留。合并角色同一发言短段，保持熟人调侃与弟弟犬类称呼，不提前否定成名仅是玩笑。',['characters-support:Tomcat/语域'])
add('SC29248fbcf75fe78f',[55,56,57,58,59,60,61],'B','continuity','图托恩星球的报告到此结束。\n这颗历经动荡、面临空前危机的星球，因两位勇敢的宇宙育种者奋战而获救：\n姐姐伊法妮·伊法伊，经验丰富，战斗技巧无可匹敌；弟弟伊法伊·伊法伊，天赋出众，始终热情满怀。\n两人携手，就没有应付不了的任务。PPP以拥有这样的特工为荣。\n——波苏','结尾是Bossu署名报告，不是无归属的全知性格定论；当前“直面着…被…奋勇拯救”跨框连读僵硬。重建报告句法，保留原署名、姓名长幼与赞扬归属；实际控制标签和输出节点不得据此直接合并。',['characters-support:Bossu/语域','characters-primary:事实等级与分支红线'])
add('SC394405c5c61c5988',[6,7,8],'B','continuity','正好趁机练习写被俘经历报告！\n我看看……从现在开始留心，把这段短短的……结束前发生的事都记下来……','“被俘结束报告”是机械名词串；接下来short/little/nap分次被昏睡打断，是故作专业后睡着的笑点，建议保持未完句，不跨Black控制把“打盹”提前补齐。')
# 每个场景的实际语义判断。短菜单/交易合法变体不为了凑数改写。
notes={
'SCc5a39b46e31a19e3':'zener条件尾句与anyways转回话题可保留；本输入只给独立entry，未臆造前段。',
'SC3bd61b10e81bc264':'催促与打铁式节奏成立，MAN对象保留；咕噜噜虽可润色，不升必改。',
'SC261c757407969621':'夸狗外观后给野兽刨土操作，DOWN+攻击与形态条件保留。',
'SC048046829ebef139':'koboCostume条件两种招呼分开，顶级好菜/杂货铺推销差别保留。',
'SCe07f941205affd55':'Macsen自称非海盗及伪装/地图售卖连贯；不把伪装说辞提升为主角真海盗。',
'SC534b27bb191911f5':'无手电与已有手电两分支均读；失窃/停电抱怨、地震与不祥预感保留不强改。',
'SCa77905dd8a62d2c1':'反向推销探险装置、异常探测和地图查漏功能连贯，1493空行为已有合句。',
'SCf860af81d8f34a5a':'修船求零件问机修工，跨两原行已正确合句，非漏译。',
'SC2a9e7e815d78c579':'sis口语称姐在本entry可保留，不仅凭匿名星号认定实际说话者身份。',
'SC3d34d0fbc8f5e312':'野兽形态只会汪，Bossu错认电台被偷并损弟弟；专业姐姐对照成立。',
'SCb3ab0694fcd68270':'装束/胡闹后再接听，保留喜剧停顿；不据复数“你们”新增实际在场者。',
'SCad5fbd3752d9240e':'制式炮塔使用多年、耐用但挨揍可停，问答与尾梗成立。',
'SC126cbdcbb22257b0':'Bossu试图拉回公事，Yiffany继续讲矮人床事，最后结巴回应；节奏与粗俗度保留。',
'SC86ba5caa7762044d':'临时命名反讽、青蛙受能量影响仍有seems推测，不硬改合法说明。',
'SCd989e3ef96634b81':'先卖关子“两种办法”再全是引爆的冷幽默，ACTUAL_HINTS下划线来源已有，不误判脚本损坏。',
'SC3a28513b100a3730':'蜘蛛/机器人纠正与纳米网支撑环境的说明连贯；不把Bossu关于真蜘蛛的说辞作现实百科纠错。',
'SC3b2099d5bd0f2c4e':'挨幼犬揍—补给嘴硬—黑市食物便宜但中毒笑点完整，非持续无能/吝啬性格定论。',
'SC545db67f494b57d8':'ducky与重构组合是橡皮鸭调试语境的叫法，可保留；不误作真实鸭变身。',
'SC3c1ce79c8d1fad83':'窥探卫星链路—观察—芯片换开门交易完整；稍显书面仍可成立，不凑润色。',
'SCd7e3aa69e31742f0':'再讨骨头会赔光家底，骨头/破产习语转成中文已成立。',
'SC581aac8836b915da':'首次与复听的条件分开；失联后怀疑学院技法、总部否认与转脚环教学保留揭示顺序。',
'SCc84763bc1dd8de7b':'碰球—新力量—脑内指令—同事担心脑震荡，问答和按键全，保留。',
'SC81629a933df116e2':'正下方求救、漆黑难行、谨慎前进；未把should安全预期夸成保证。',
'SC450f7f96b03561f6':'undercover为主角说辞及Mauser接话，虽译“任务”略显具体，不据此建立真实任务设定。',
'SCa1e42fd2a89cb4a7':'需先见锁条件保留，Fenfen技术与听其话语的谜题方向成立；Exile名暂不强定。',
'SCc811ebb442c0d188':'电流杂音/FE/FEN残片与姓氏反应单独理解；不补全Fenfen、不提前揭弟弟。杂音拟声保留可合法，未作漏译。',
'SCd1574a99193e960c':'变性误认“你是我”与普通Kobo“你是”不合并，不推身份互换。',
'SCde06b7c24bea01f3':'纯噪声及词残片无足够可恢复语义，保留失真，不猜补校准等完整命令。',
'SCad3ea7970d37573b':'姐姐刚确认弟弟—总部要求勿留手—先脱险—钩索无能力选中条件，连续意图成立。钩锁/钩索另待全局术语裁决，不凑条。',
'SC1c722fa26d1718c5':'接触传图由本人报告、PAW录下支持；they可为单数/族群，当前轻微代词摇摆不够证据定错人数。',
'SCa9fe935a4367db72':'无蛋白/汽油味反转完整，拖长谢谢反话可成立，不强换拟声。',
'SCeb8000b49b6c43e2':'夹克旧主人气味、主角辩称了解装备、同事揭穿，对话意图完整。',
'SCb0333c2793da348c':'武器手感swift/surgical/true译为快准到位，合法不额外色情化。',
'SC303f83b6cec490b0':'作弊码SXUXYGAX原样，崩溃责任元游戏笑话正确，不把世界崩掉当剧情事实。',
'SC5f439cfa5fd5569e':'反复索财后恼火吐作弊码，码GEKKYZAA保留，商人口气可成立。',
'SCc27e8f58c8e9a99d':'Bossu错认电台被夺，护短威胁又损男主娇小，沉默落点完整。',
'SC7738d5683df9b077':'男主无制服只怕毛烧的嘴硬笑话保留，不移用女线反应。',
'SC242d9e3c6d253668':'literally/figuratively、超能力/作弊猜测、心虚挂线的问答链成立。',
'SC5639e750c29c987c':'Tomcat she/her由源文支持，不以名字或猫默认男性。',
'SCbef498a71645cdb4':'torch误称被下一问点出，是原作词汇笑点不能擅统一成手电消梗。',
'SCb9a1ad247f8eee59':'flashlight/torch显式回扣Bossu词汇区别，自动照明与无需特别操作清楚。',
'SCae345fce997f566f':'变性时Tomcat误认姐姐、当前男主急忙道歉结束，路线身份分开。',
'SCb3df0be96568258e':'史莱姆音节与总部误判被史莱姆俘获的语气可保留，非旁白认定。',
'SC7f00fdd5a5b7a70e':'女线SFW整VSN读完：精英自夸/22岁荣誉毕业/弟弟破年龄纪录均为本人说辞，承重门框坍塌及护腕落下转好运保留；控制事件间不合句。',
'SC61f9a16922cf2556':'女线SFW整VSN读完：主角自夸被父亲角色挫败，四足训练借口、父子谈可能救世英雄；不把VSN narrator统一当实际说话者，不从pup认定年龄。',
'SCc81867d38ef92db1':'女线NSFW全结局已读：最初嫌科博德温柔、自愿求粗暴，与后续受吠犬影响/被俘/拒救分时理解；本人报告不是客观正常人格模板。大部分中文已合段可保留，未冒称看到对应画面。',
'SCad124eb3e41e68a7':'男线Fenfen第四记忆全读：lang(Fox)讲述战争、缺失议员导致受制、联结仍维持、趁虚封水晶；是角色传来的历史，不是统一narrator全知结论。',
'SC394405c5c61c5988':'男线NSFW全VSN已读：故作专业、被俘嘴硬与结尾“你信吧”同一表演弧；没有把其“我随时能逃”当客观保证。开头报告段列B，其余可保留。',
'SC42b1851d50303cc3':'男线NSFW全VSN已读：先被Gobins耗尽力气、偶然逃脱、被精灵哄诱后认知转向，水/精神力仍是本人疑问；结尾服从不是前段主动同意。粗暴施受与否定都保留。',
'SC0a4e99945784e808':'片段按key排序非演出顺序，需按布局拼YOU ARE A TRUE COSMO-BREEDER；未擅改控制星号/空白。实显排版未验证。',
'SC3da55b03891395ae':'条目按键名顺序而非显示顺序，按完整警告理解为修改作弊设置会重置且丢失未保存进度；中文意思仍完整，不以顺序误报错乱。'
}
for f in findings:
    notes.setdefault(f['scene_id'],'整场英语意图、当前中文与控制分支已连读；见所列具体完整短段提案，其余合法变体保留。')
coverage=[]
for s in scenes:
    sid=s['scene_id']; fs=[f['finding_id'] for f in findings if f['scene_id']==sid]
    ids=list(dict.fromkeys([r['review_row_id'] for r in s['rows']]+[r['review_row_id'] for a in s.get('aliases',[]) for r in a['rows']]))
    if s['kind']=='code':
        result='inventory_only'; note='已逐条实际阅读本资源常量文本；用途未证，不把null中文报漏译、不翻程序键/路径/错误文本、不声称玩家可见。'
    elif any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in s['rows']):
        result='needs_evidence' if fs else 'inventory_only'; note=notes.get(sid,'已读嵌套资源值与当前中文；运行时用途未证，占位/地点/标题按文本保留，不冒称实显已校。')
    else:
        result='issues_found' if fs else 'retain'; note=notes.get(sid, f"已读{s['root']}完整输入段；当前中文与英语的对象、否定、条件及语气相容，菜单/招呼/交易或短反应保留现有合法表达，不为逐行一对一而改译。")
    coverage.append(dict(scene_id=sid,read_status='read_full',row_ids=ids,context_checked=True,findings=fs,result=result,notes=note,scope='packet_input_only; no runtime or visual verification',mode=s['mode'],kind=s['kind'],root=s['root'],aliases=s.get('aliases',[])))
def dump_jsonl(name,rows):
    (OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
dump_jsonl('findings.jsonl',findings)
dump_jsonl('coverage.jsonl',coverage)
reads=[[1,100],[101,250]]+[[i,min(i+99,2475)] for i in range(251,2476,100)]
log=dict(packet='packet-05',input_path=str(READER).replace('\\\\','/'),input_sha256=hashlib.sha256(READER.read_bytes()).hexdigest(),packet_json_path=str(INPUT).replace('\\\\','/'),packet_json_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),read_ranges=reads,truncated_ranges=[],references_read=[{'path':str(BASE/'LOCALIZATION_BRIEF.md'),'ranges':[[1,65]]},{'path':str(BASE/'WORK_ORDERS.md'),'ranges':[[1,48]]},{'path':str(BASE/'reference/characters-primary.md'),'ranges':[[1,277],[278,377]],'initial_cap_recovered':True},{'path':str(BASE/'reference/characters-support.md'),'ranges':[[1,128]]},{'path':str(BASE/'reference/world-and-plot.md'),'ranges':[[1,150],[151,250],[251,350],[351,406]],'sha256':hashlib.sha256((BASE/'reference/world-and-plot.md').read_bytes()).hexdigest()}],reader_sha256=hashlib.sha256(READER.read_bytes()).hexdigest(),reader_total_lines=2475,actual_read_ranges=reads,reader_cropped=False,method='工具read逐段实际语义通读；每整entry/VSN先连读EN意图，再连读candidate4当前ZH；机械脚本仅提取已读证据和完整rowid制作收据，不替代阅读。',reference_reads={'LOCALIZATION_BRIEF.md':'1–65','WORK_ORDERS.md':'1–48','characters-primary.md':'1–277 capped then 278–377 completed','characters-support.md':'1–128','world-and-plot.md':'起初两次not found；汇合后1–150、151–250、251–350、351–406完整补读，复核D01/D02/D04/I06/I07/E05/E06/E07/W06/W08/H05'},semantic_scope={'scenes':len(scenes),'kinds':dict(Counter(s['kind'] for s in scenes)),'all_input_scenes_read':True,'code_usage_unverified':True,'runtime_verified':False,'images_visually_verified':False,'translation_applied':False,'approved':False},uncovered=['外部include的未入本包正文不等于已读','运行时触发/商店或missionLog使用状态未验证','视觉画面及实际排版未验'],finding_counts=dict(Counter(f['severity'] for f in findings)))
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary=f'''# packet-05 首轮粗校提案

## 结果
- 已实际read全稿2475行，区间见reading-log；无reader裁剪。{len(scenes)}个输入场景各一覆盖收据，含本场主rowid及全部alias rowid。
- {len(findings)}条发现：{dict(Counter(f['severity'] for f in findings))}。仅待复审场景提案；未回写译文/catalog/资源/游戏，未部署、Git写或approved。
- code仅inventory；nested JSON运行用途未证，即使提文本建议也不冒称实显。无图像验证。空行按整段已消费处理，未报合句尾行为漏译。

## 高风险与续办
1. 女线SFW双足飞龙战斗提示残留“在高潮的”，并把draconid写成龙人。
2. 女线存档解释把“以防出事”写成“在出事时保存”；女线首次飞船通讯把PUP叫“小子”。
3. 男线与SFW平行Fenfen呼叫COME IN误作“我这就进来”；NSFW邻句情色双关须整段再设计，不能靠保留主句错译过关。
4. 男线坠落段Mauser说信号断续，“我撑不住”错误牵引为总部人物遇险；建议仍保留源省略。
5. 女线肉块拖音、SFW泽纳方形解释拼接、鳞装回忆与loose笑点、男线昂贵靴教学、结局Bossu报告等为整段精修重点。
6. male missionLog/13源段写Yiffany/her，为源/用途待核（潜在A风险，status=needs_evidence），不直接改男主。sensor dark已对照世界观I06近场不可见复核；不擅补颜色或成因。Exile已据E07记为专名语境，不翻成普通“流放”。

## 新增角色/设定证据（不作事实升级）
- 女线SFW BigboldV2：Yiffany自述22岁荣誉毕业、曾是最年轻实战特工，弟弟后来夺纪录；只记录自述，不外推弟弟确切年龄。
- 女线SFW Werehund：父亲角色称其一场战斗学会力量、可能救世；父子互称来自原台词，不以narrator字段判人。
- 男线Fox记忆：议会成员缺席使其受制，精神联结仍在；最终封Traeh而未杀死。lang(Fox)讲述有归属，不当全知旁白。
- 男线AreaC败北的末尾服从是整场认知转变，不倒推早先自愿；女线AreaB的主动粗暴兴趣亦不得移作弟弟常态。

## 明确保留
- 黑市食物价廉/中毒互损、Bossu两种拆雷全是引爆的冷幽默、torch/flashlight误称回扣、Rapier专业手感、型态误认、作弊码与@DerekChipReport均保留。
- 词残片FE/FEN与电流声不擅补全；匿名*、narrator不直接作角色证明；SFW/NSFW与男女路线不并经历。
- 当前大部分VSN已整段合句，尾空行不报漏译。GameOver两条男线和女线AreaB全场读完，不冒称已见演出图片。

## 验证范围
构造脚本只装配手工判断，检查JSONL可解析、场景一对一、全部rowid、发现链接及哈希。未做正式应用、输出节点映射、字体排版或实机验证。

## 参考汇合复核
世界观参照现已完整补读406行。D01支持Bumper机械分类；D02支持无线电COME IN主功能；D04支持精灵寿命的总部认知边界；I06/I07支持泽纳传感不可见与三角取舍；E05/E06支持男女失败分支不混写及认知转变；E07支持Exile专名；W06/W08/H05支持报告署名、履历说辞及封印史分层。已据此复核并加入Exile问题；未把参照升级为运行时验证。
'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
assert len({c['scene_id'] for c in coverage})==len(scenes)
for s,c in zip(scenes,coverage):
    expected={r['review_row_id'] for r in s['rows']}|{r['review_row_id'] for a in s.get('aliases',[]) for r in a['rows']}
    assert set(c['row_ids'])==expected
for f in findings:
    assert set(f['row_ids'])<=set(next(c['row_ids'] for c in coverage if c['scene_id']==f['scene_id']))
print(json.dumps({'scenes':len(scenes),'findings':len(findings),'severity':dict(Counter(f['severity'] for f in findings)),'unique_receipt_rowids':len(set(r for c in coverage for r in c['row_ids'])),'kinds':log['semantic_scope']['kinds'],'input_sha256':log['input_sha256']},ensure_ascii=False))
