"""Write the r9 batch-05-part01 decision table.

Row ids are read back from the batch order and checked against the current
text, so a stale id fails loudly instead of binding a repair to another line.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-05-part01'
ORDER = json.loads((BASE / 'orders/batch-05-part01.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# —— 术语实测（写入 decisions 的 reason 里，便于复核）——
#   SPIKER→刺虫、DRILLER→钻探者、SQUEAKER→吱吱怪、BUMPER→弹跳机、FLAMER→喷火者
#   取自 datav/dictionary.json 的条目名；『刺甲机／钻掘机／吱吱兽』三说在库里零出现。

APPLY = [
    # —— A：两条实测超限行，压回 3 行 ——
    ('CAT:O422deacf720938629a08', 'ds:P05-118', 'A', 'format',
     '  Bossu: [早先的报告说，不少同僚特工被科博德抓了。能救就救，哪怕得先做点交易保证他们的安全。]',
     '工单四之二点名超限：现译 56 字，224px 数据书折成 4 行，构建抛异常。保留「早先报告／同僚特工／被科博德抓／能救就救／先做交易／保证安全」全部条件，无增删因果。两条路线各自压到 41／44 字，取 DS 版，因其保留「先做」这层不情愿的语气。'),
    ('SFW01c279ac5b41aa55ec6a42b2', 'ds:P05-119', 'A', 'format',
     '  Bossu: [这些小型轮式无人机原本在矿井里运送矿石和工具，如今被改装上粗陋的尖刺，并加上搜寻入侵者的程序。]',
     '工单四之二点名超限：现译 66 字，折成 4 行。保留「原本／如今」时间对比、运送对象、粗陋尖刺、搜寻入侵者四项事实。取 DS 版并保留「无人机」（Gemini 版压成「轮式机」，丢了 drone 这层）。'),

    # —— A：图鉴条目名与外文残留 ——
    ('CAT:Oc8227e39ed2d2509f0dc', 'ds:P05-102', 'A', 'term',
     '  Bossu: [那些银色带刺的机器人，叫做「刺虫」。]',
     '正文把条目名 SPIKERS 原样留作英文、用半角双引号、句末无标点。游戏内 datav 词典条目名实测为「刺虫」（SPIKER→刺虫，全库 1 处无第二说）；「刺甲机」在库里零出现，是参照摘录写错、Gemini 跟着错。'),
    ('CAT:Obe556b284687ca06d598', 'ds:P05-104', 'A', 'term',
     '  Bossu: [作为一种纳米机械机器人，那些钻探者会持续自我修复。它们会不知疲倦地钻掘。]',
     '正文残留未译条目名 DRILLER。词典实测 DRILLER→钻探者；「钻掘机」零出现。BURROW 的动作仍译「钻掘」，与条目名分开。'),
    ('CAT:O501f09c7008d9f4f7633', 'ds:P05-105', 'A', 'term',
     '  Bossu: [那些钻探者只会在划定的区域内活动。]',
     '同场 DRILLER 第二次未译，与上一条同一术语；本行句末还缺句号，单独成行时无标点收尾。'),

    # —— A：无线电呼叫与收线 ——
    ('CAT:Oebaa9ca90d8f126b1f45', 'ds:P05-106', 'A', 'format',
     '  Bossu: [波苏在此，出什么问题了，特工？]',
     '「波苏 在此」中间夹半角空格，是 R1 把 `[BOSSU 在此…]` 换成中文名后留下的排版残留，渲染时名字后多一个空档。只删空格；「在此」对应 BOSSU HERE 的报身份，不改成「收到」（那是 roger，语义不同）。'),
    ('CAT:Ofae81cd00d4f84252689', 'ds:P05-107', 'A', 'term',
     '  Yiffai: [当然，当然！伊吠通话完毕！]',
     '「下线」会被读成退出系统；BossuDex 内收线词实测 通话完毕 11／通话结束 2／完毕 1／撤了 1／下线 1，「下线」是唯一一处。按 root 内主用法归位。'),
    ('CAT:Ofb4c3ae02e7843cc968d', 'ds:P05-128', 'A', 'term',
     '  Yiffany: [唉……谢——谢啦波苏。伊吠妮通话完毕。]',
     '同一 root 收线套语三种写法里「完毕」缺「通话」，与上一条一并按主用法归位。'),
    ('CAT:O93747cb50f2482f26380', 'gemini:P05-111', 'B', 'meaning',
     '  Yiffai: [呼叫波苏，能进来吗？]',
     'COME IN. BOSSU? 是无线电请对方应答，源文带问号，现译「波苏，我进来了。」把呼叫写成已成事实的陈述，且句号抹掉了问句。下行波苏拿 come in 开黄腔接「希望你别进来，孩子。」——中文用「能进来吗」同时保住呼叫与双关，波苏的反问才有着落。'),

    # —— B：超限行以外的排版残留 ——
    ('CAT:O07b2c3b2e1eda4aaec28', 'ds:P05-113', 'B', 'format',
     '  Yiffai: [它根本不是我的对手！我先嗨呀，再啊哒，还——]',
     '原文 AN- 是被打断的词；中文行尾留了半角短横「-」，12px 渲染成一个孤立小横。全批其它被打断处一律用「——」。'),
    ('CAT:Odb4931725a302877f84b', 'ds:P05-116', 'B', 'format',
     '  Yiffany: [我说啊，波苏，我不是人鱼，对吧？]',
     '「我说啊 波苏」中间是半角空格，原文是逗号前的拖长称呼；补逗号并去掉空格。'),
    ('CAT:O4f91ec4e352430882278', 'ds:P05-115', 'C', 'format',
     '  Bossu: [不管怎样，小心点，特工！]',
     '行尾残留两个半角空格，是 R1 合句时留下的排版垃圾，会参与行宽测量。只删空格。'),
    ('SFWe8d99a8751c9ac2f368e4701', 'R9M-503', 'C', 'format',
     '  Bossu: [图托恩上异常的源头，特工。小心！]',
     '与上一条同类：行尾两个半角空格。两条路线都没提，主代理补。'),
    ('CAT:O5f600ae5ab4c4abda1ac', 'ds:P05-108', 'B', 'format',
     '  Bossu: [那些装在天花板上的炮塔全都失控了，大概是电力系统损坏得太厉害的缘故。]',
     '本行是三行英文合并在一个物理行，下一 ROW 为空的合句尾行，句子在此收尾，中文却无句号，与同场其它行不一致。只补句号。'),
    ('SFWb4d62462c32d758271eb1b3c', 'ds:P05-122', 'B', 'format',
     '  Bossu: [这些大块头以强劲的利爪闻名。]',
     '英文句到此结束，下一行是新的祈使句；中文以「闻名」裸收，会把两句读成「以强劲的利爪闻名尽量别从正面攻击它们」。补句号断开。'),
    ('CAT:O74a589a54a137f4033ed', 'ds:P05-123', 'B', 'format',
     '  Bossu: [图托恩上发生的怪事，导致有人目击到非实体的水母。]',
     '本行合并了「…HAVE LEAD TO」「SIGHTINGS OF…」两条英文，后一条 current 为空；句子在此完结而缺句号。'),
    ('CAT:Oe793fb515df5430c4feb', 'ds:P05-124', 'B', 'format',
     '  Bossu: [干掉它，但别被围住，才能活下来。]',
     '本场收尾行缺句号，与同 root 其它场（「一旦过了采矿区，你就安全了。」）收尾不一致。'),
    ('SFWd96bb58052321c0b20d85e5b', 'ds:P05-125', 'B', 'format',
     '  Bossu: [你可以靠近它们，诱使它们自爆，或者打它们，让它们爆炸。你自己选。]',
     '两条英文合并在本行，句末缺句号；同 root 男版对应句已作「你选吧。」，此处补齐即对齐。'),
    ('CAT:Ob0e7622b60ee1b85b055', 'ds:P05-126', 'B', 'format',
     '  Yiffai: [我不记得简报里提到过这个区域。]',
     '本行是一个完整句子，下一行换波苏说话，中文却无句末标点，视觉上像被截断。'),
    ('CAT:Ob727de40e97ec2c611bd', 'ds:P05-127', 'B', 'format',
     '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     '整句到此为止，下一行是「THEY\'RE LITERALLY IMPOSSIBLE TO DESTROY!」，中文两行会粘成一串。'),

    # —— B：语义 ——
    ('CAT:O51bbf635a96c12cb2f4e', 'gemini:P05-107', 'B', 'meaning',
     '  Yiffai: [……？矿井当然开采过了，可这跟爆炸有什么关系？]',
     '原文 WELL SURE 是「那当然」，接的是波苏的 mine（矿井／地雷）双关；现译「挖矿有那么多忌讳？」凭空造出原文没有的「忌讳」，也断了后面毛鼠拆解「在矿井里埋地雷」的接续。中文无法复现双关，取 Gemini 版把误解落在「开采过了」这一层，与下行「我是说，雷区里的雷炸了。」能接上；DS 版「那当然」过短，读者看不出误解的是什么。'),
    ('CAT:O6b9a3bb37d35006c7838', 'ds:P05-109', 'B', 'idiom',
     '  Bossu: [没错，至少据我们目前了解是这样。]',
     '「就我们所能看出的而言」是 as far as we can tell 的逐字直搬，中文不成句。同 root 女版同句已作「没错，至少据我们目前了解是这样。」，此处直接对齐，不确定度不升格为断言。'),
    ('CAT:O585683ee840628bb888b', 'ds:P05-111', 'B', 'continuity',
     '  Bossu: [之前没有矮人出现在这片区域的报告，但他们确实很擅长嗅出稀有矿脉。]',
     '同一段里指矮人一会儿「它们」一会儿「他们」（下一行紧接「他们怎么能又大又高」）。矮人是犬科里的人形矿工，同 root 女版同句用「他们」，全库 DWARF 相关行亦用「他们」。'),
    ('CAT:Ob55c6939b4a70b2747f2', 'R9M-502', 'B', 'continuity',
     '  Bossu: [当心他们的力气。一拳就能把你打得倒栽葱飞出去。]',
     '与上一条同场同因：MIND THEIR STRENGTH 指这些矮人矿工，本行仍用「它们」。同场已统一为「他们」，一并归位。'),
    ('CAT:Oa696b99ee3f92a47dce7', 'R9M-504', 'B', 'continuity',
     '  Bossu: [之前没有矮人出现在这片区域的报告，但他们确实很擅长嗅出稀有矿脉。]',
     'DwarfThrower 与 ClassicDwarf 是同文两场，本行沿用「它们」；与上两条同一处指称问题，一并归位。'),
    ('CAT:O117b0d9e8514ef00020d', 'R9M-505', 'B', 'continuity',
     '  Bossu: [当心他们的力气。一拳就能把你打得倒栽葱飞出去。]',
     'DwarfThrower 男版同句；与上一条同改。'),
    ('SFW2ee9695ece6b2141a65e2555', 'R9M-506', 'B', 'continuity',
     '  Bossu: [之前没有矮人出现在这片区域的报告，但他们确实很擅长嗅出稀有矿脉。]',
     'DwarfThrower 女版（SFW）同句；与上一条同改。'),
    ('SFW7d3d415fcba4c5e91855ce85', 'R9M-507', 'B', 'continuity',
     '  Bossu: [当心他们的力气。一拳就能把你打得倒栽葱飞出去。]',
     'DwarfThrower 女版同句；与上一条同改。'),
    ('CAT:O7955489532c488358c6e', 'ds:P05-112', 'B', 'term',
     '  Bossu: [“喷火兽”属于龙类的一员。]',
     '「龙形科」是自造科名，全库仅此处一处；同 root 女版作「龙兽科」（同样一处自造），而 DRACONID 在正文里的通行说法是「龙类」（MauserHints「巨大的龙类」、Wyvern 场「会飞的龙类生物」）。龙类是物种归类而非分类学「科」，故改「龙类的一员」；条目名「喷火兽」不在本条内改。'),
    ('CAT:Od80b27f552d4d8d94722', 'R9M-508', 'B', 'term',
     '  Yiffany: [波苏，我刚遇到了一只会飞的龙类生物。]',
     '同一句 DRACONID 在本批女版作「龙人」、part03 男版已作「会飞的龙类生物」；「龙人」全库仅此一处。与上一条同一术语口径，一并归位（part03 对应行届时保持）。'),
    ('CAT:O9f5dd3fddc00368e8de8', 'ds:P05-114', 'B', 'idiom',
     '  Bossu: [那些圆滚滚的悬浮无人机，和你在泽罗尼亚周围见过的那种很像。不过这一型号还配备了爆炸载荷。]',
     '「和你见过在泽罗尼亚周围飞的」把定语从句按英文语序塞进「和…很像」之间，中文读不通；改为「你在泽罗尼亚周围见过的那种」，三条英文仍合一行，字数还略降。'),
    ('CAT:Oe05bfaf92f0f6aeeb3bf', 'ds:P05-129', 'C', 'idiom',
     '  Bossu: [信不信由你，那些是最近才造的，出自你们碰上的那些蜥蜴太空海盗之手。]',
     '「你们遇到的那些蜥蜴太空海盗最近造出来的」把「最近造」压在句末，重心落在海盗身上。同场 TWIN 行（本场景下一行）已作「更近期造出来的，出自你们遇到的那些蜥蜴太空海盗之手」，此处对齐句式。'),
    ('CAT:Oe0aa7e76dfc1f8da1973', 'ds:P05-117', 'B', 'term',
     '  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，凡是最后能捞到 Lect 的事，他们都干！]',
     '源文大写 LECT，且工单第 43 行把 `Lect` 列为保护标记；本行写成小写「lect」。全库 20 处作 Lect、8 处作 lect（后者源文也是小写），本行源文大写，改回 Lect。'),
    ('SFW6e7ffa47864e257d741d96fe', 'ds:P05-101', 'B', 'meaning',
     '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并非个个都能长生不老。]',
     '原文 MAY 是总部掌握的推测，现译「虽说全是女性」把推测升成断言；同 root 另两版同句均作「也许…雌性」。保住推断强度与转折结构，「女性」也随之与另两版统一为「雌性」。'),
    ('CAT:Ob01ce1e481fa6d8e9eea', 'ds:P05-103', 'C', 'idiom',
     '  Bossu: [虽说那些家伙看着像在地上爬的虫子，其实是一具精巧的机械仿制品。]',
     '两条英文已合成一行，「虽说」后靠逗号硬接、转折词落在后半，读起来断气；「机械仿体」不是通行说法。补「其实」为主句转折支点，改「机械仿制品」，合行长度略降。'),
    ('SFWab74b9d79595e6b56cf2c6f4', 'ds:P05-131', 'C', 'idiom',
     '  Yiffai: [波苏，请立刻给我个状态更新，确认我没变成水生生物！]',
     '一句里连用两个「确认」，第二个还把 REQUESTING UPDATE（请求更新）压成「确认」；改成「给我个状态更新」既不重复，也保住「要一份状态报告来核实」的语义。'),
    ('CAT:O5efbd3492bc7aae253bf', 'ds:P05-132', 'C', 'term',
     '  Bossu: [它们简直就像灵能扰动化出的实体……]',
     '「被扰乱的灵能」是英文词序直搬；同一现象在 Jellyfish 场作「灵能躁动形成的幻影」，全库 psychic disturbance 通行译「灵能扰动」（12 处）。取「灵能扰动」并理顺语序，「化身」改「实体」以别于下行「幽灵者」这个具体名。'),
    ('CAT:Ob502fba8e84f0f537434', 'ds:P05-133', 'C', 'idiom',
     '  Yiffai: [字面意思？你是说……只是打个比方吧？]',
     'LITERALLY／FIGURATIVELY 的对举是这句的笑点，现译「打比方吧？」读起来像在确认修辞手法；补「只是」把对举点明。女版同位已作「只是夸张一下吧？」，语气同源。'),
    ('CAT:O72c46d5d58897e28ada1', 'ds:P05-130', 'C', 'term',
     '  Bossu: [我们只有那些关于 Fenfen 服装散落各处的报告。]',
     '同一场里物种名先作 Fenfen 后作 FENFEN。全库 124 处作 Fenfen、3 处作 芬芬、3 处作全大写；只统一英文写法，中文条目名待 UI 同源确认后另裁。'),
    ('CAT:O000059a9bccb01172eaa', 'ds:P05-110', 'C', 'voice',
     '  Yiffany: [这、这些一直朝我扑过来的机器虫是怎么搞的？]',
     'KEEP COMING AT ME 是被成群扑来，「冲过来」偏中性；「怎么回事」偏书面，与结巴脱口而出的口气不合。'),
    ('CAT:Odaefef7908bae16febfb', 'gemini:P05-109', 'B', 'idiom',
     '  Bossu: [……当然，除非它们愿意请你吃晚饭。]',
     '原译把句尾状语 of course 硬直译后置成「……当然。」，中文不成句；前置为「当然，除非……」保调侃语气，条件与对象不动。'),
]

# 同一物理行的重复提案：另一路也报了，改动已按上表某个 finding_id 落地。
# 单列出来是为了让逐条审计对得上，不重复写台账。
DUPLICATE = [
    ('gemini:P05-101', 'A', 'format', 'SCcc1017cf7ebd30ac', 'CAT:O422deacf720938629a08',
     '与本表 ds:P05-118 同一行同一处超限压缩；取 DS 版措辞，本条不另立操作。'),
    ('gemini:P05-102', 'A', 'format', 'SCfae065df9d829e6c', 'SFW01c279ac5b41aa55ec6a42b2',
     '与本表 ds:P05-119 同一行同一处超限压缩；取 DS 版并保留「无人机」，本条不另立操作。'),
    ('gemini:P05-108', 'B', 'idiom', 'SC9a50ee5c19b72be6', 'CAT:O6b9a3bb37d35006c7838',
     '与本表 ds:P05-109 同一行同一处直译修正；取与同 root 女版完全一致的措辞，本条不另立操作。'),
    ('gemini:P05-112', 'C', 'format', 'SC6c6396e08a205b23', 'CAT:O07b2c3b2e1eda4aaec28',
     '与本表 ds:P05-113 同一行的半角短横改全角破折号；已按行落地，本条不另立操作。'),
    ('gemini:P05-113', 'C', 'format', 'SC2df2a934a81fcf00', 'CAT:Odb4931725a302877f84b',
     '与本表 ds:P05-116 同一行的半角空格改逗号；已按行落地，本条不另立操作。'),
    ('ds:P05-120', 'B', 'meaning', 'SCb6f36febbdf9e0cd', 'CAT:O51bbf635a96c12cb2f4e',
     '与本表 gemini:P05-107 同一行的 mine 双关；DS 版「那当然」过短、看不出误解落在哪一层，取 Gemini 版，本条的措辞不采用。'),
]

REJECT = [
    ('gemini:P05-106', 'B', 'term', 'SCa226bce097a955f8', 'CAT:O98c14bff4eea72e7f0d2',
     'Gemini 依工单术语表把 Squeaker 改成「吱吱兽」，但游戏内 datav 词典条目名实测是「吱吱怪」（SQUEAKER→吱吱怪，breeding／card／SpecialFap 共 16 处同源），「吱吱兽」全库零出现。工单摘录本身写错，两路都受影响，这里按实测驳回。'),
    ('gemini:P05-103', 'B', 'term', 'SC36a4246a3fd4b93d', 'CAT:Oc8227e39ed2d2509f0dc',
     '同一行 Gemini 给的「刺甲机」与词典条目名「刺虫」不符，已按 DS 版落地；本条只驳回术语写法，行本身已修。'),
    ('gemini:P05-104', 'B', 'term', 'SCf096caa44f045c89', 'CAT:Obe556b284687ca06d598',
     '同上：Gemini 的「钻掘机」与词典条目名「钻探者」不符，已按 DS 版落地。'),
    ('gemini:P05-105', 'B', 'term', 'SCf096caa44f045c89', 'CAT:O501f09c7008d9f4f7633',
     '同上：术语写法驳回，句末补标点部分已落地。'),
    ('gemini:P05-110', 'B', 'voice', 'SCfeff53e003014bf2', 'CAT:Oebaa9ca90d8f126b1f45',
     'Gemini 把 BOSSU HERE 改成「波苏收到」。「收到」对应 roger／copy that，而 HERE 是报明身份（这里是波苏），改后与原意错位；已按 DS 版只删空格。'),
]

HOLD = [
    ('ds:P05-121', 'needs_evidence', 'source_uncertainty', 'SC03c43e680b4ff75e', 'SFW3c0385107b32a2c4d0d39b95',
     '原文 ACTUAL_HINTS 带下划线，不像正常英文，也不在本批保护标记清单内。不确定是源文件占位符残留（应译成「真正有用的提示」）还是游戏会替换的标记（必须原样保留），全 root 共 6 处同文。未提案。'),
    ('ds:P05-130b', 'needs_evidence', 'term', 'SC46fe33beaab2503d', 'CAT:O72c46d5d58897e28ada1',
     'FENFEN 的中文条目名待裁：datav 词典 SFW 版作「芬芬」、NSFW 版作「Fenfen」，正文 124 处作 Fenfen。本条只统一大小写，中文名不新造。'),
    ('R9M-501', 'B', 'term', 'SC176bd1d1147dcec8', 'CAT:O7955489532c488358c6e',
     '条目名 FLAMER 在正文作「喷火兽」（4 处），而 datav 词典实测作「喷火者」。本批只改「龙形科→龙类」这层归类口径，物种名留待跨 part 一次定，避免 part01 改一半、part03 打折。'),
    ('R9M-509', 'C', 'format', 'SC176bd1d1147dcec8', 'CAT:O7955489532c488358c6e',
     '本批「“”」与「「」」两套引号并存（part01 内 6 对 10），属跨 part 格式裁决，不在单批内统一。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()
    for rid, fid, sev, cat, new, reason in APPLY:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        if fid in seen:
            raise SystemExit('duplicate finding ' + fid)
        seen.add(fid)
        scene_id, row = ROWS[rid]
        if not (row['current'] or '').strip():
            raise SystemExit('blank line target ' + rid)
        if row['current'] == new:
            raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'apply', new, reason)))
    for fid, sev, cat, scene_id, rid, reason in REJECT:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'reject', '', reason)))
    for fid, sev, cat, scene_id, rid, reason in DUPLICATE:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        if fid in seen:
            raise SystemExit('duplicate finding ' + fid)
        seen.add(fid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'reject', '', reason)))
    for fid, sev, cat, scene_id, rid, reason in HOLD:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'hold', '', reason)))
    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(APPLY),
                      'reject': len(REJECT) + len(DUPLICATE), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
