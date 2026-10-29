# packet-02 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SCc3ad59fdff3438ca | nsfw | datadf/all.ds | AreaB_Macsen2.Talk.macsenmoneycode1
CONTROL L805 <AreaB_Macsen2.Talk.macsenmoneycode1>
ROW CAT:Ob00a5efa7d522fa17976 | L806 | no manual edit
EN: What, is taking all my money not good enough?
BEFORE:   * 怎么，把我钱全拿走还不够？
AFTER:   * 怎么，把我钱全拿走还不够？
ROW CAT:O46817f73fbd10e683e84 | L807 | EDIT E02-001
EN: Why don't you take off next, huh punk?
BEFORE:   * 接下来你怎么不走人呢，啊，小混混？
AFTER:   * 钱都拿了，还不快滚，小混混？
### P02-001 | action=apply
原问题：take off 是赶客，不是中性提议；当前“接下来你怎么不走人呢”照搬反问结构，怒气与上一句讨钱语境衔接生硬。
本轮理由：take off紧接抱怨钱被拿光，是赶人；只修第二槽的反问，第一槽现译已完整，不把两节点合句。
EDIT_IDS ["E02-001"]

## SC3380c585541b394c | nsfw | datadf/all.ds | AreaC_Slaver1.Talk.psy
CONTROL L1458 <AreaC_Slaver1.Talk.psy>
CONTROL L1459   if { koboCostume() && hasItem(SpecialPsycards) } {
ROW CAT:O7d30fc1345309b3d1bcf | L1460 | no manual edit
EN: I'll be honest: all this PSY stuff gives me the creeps.
BEFORE:     * 老实说：这些精神力的东西让我发毛。
AFTER:     * 老实说：这些精神力的东西让我发毛。
ROW CAT:O3b4757e27a43f4e0fe4d | L1461 | no manual edit
EN: Jus' don't blow me up and we'll be golden, okay?
BEFORE:     * 就别把我炸了，咱们就妥了，好吗？
AFTER:     * 就别把我炸了，咱们就妥了，好吗？
CONTROL L1462   } else {
ROW CAT:O5d01f6f586123147433c | L1463 | EDIT E02-002
EN: Most kobolds don't really do all these mind games. I get it if y'ain't interested.
BEFORE:     * 大多数科博德并不真搞这些心理把戏。你要是没兴趣，我理解。
AFTER:     * 大多数科博德都不怎么搞这些精神把戏。你要是没兴趣，我理解。
ROW CAT:O0e7f67f7227459bfd079 | L1464 | EDIT E02-003
EN: Any ole club and a length of rope'll do me just fine... All direct-like, ya-know?
BEFORE:     * 随便一根旧棍子加一段绳子就够我用了……全都直接来的，懂吧？
AFTER:     * 随便一根棍子、一截绳子就够我用了……直接动手，懂吧？
CONTROL L1465   }
CONTROL L1467 ### dog handling
### P02-002 | action=apply
原问题：该else分支以棍绳的直接手段反衬PSY；“全都直接来的”不成自然中文。保留mind games双关，不把奴隶商人误写为心理咨询。
本轮理由：else分支把PSY精神把戏与棍绳直接手段对举；不新增省事的评价，也不改科博德现用名。
EDIT_IDS ["E02-002", "E02-003"]

## SC84f50545ab568f13 | sfw | datadf/all.ds | Bossu.Area0_StarkillHint noselect
CONTROL L2100 <Bossu.Area0_StarkillHint noselect>
ROW SFW7bf5ef88f361a975c41249da | L2101 | no manual edit
EN: [AGENT, IMPORTANT NEWS INCOMING.]
BEFORE:   Bossu: [特工，重要消息传来。]
AFTER:   Bossu: [特工，重要消息传来。]
ROW SFW3e7b0fbc27fabf1d96ff6e8b | L2102 | no manual edit
EN: [BIG BRAIN SQUEAKS OVER HERE HAS SOMETHING TO SHARE!]
BEFORE:   Tomcat: [这边这位大脑袋小吱吱有事要分享！]
AFTER:   Tomcat: [这边这位大脑袋小吱吱有事要分享！]
ROW SFW35b2b5a255363618f2c26e2b | L2103 | no manual edit
EN: [I DID IT! I GOT A BREAKTHROUGH!]
BEFORE:   Mauser: [我做到了！我取得了突破！]
AFTER:   Mauser: [我做到了！我取得了突破！]
ROW SFWa405d652ddd0dc2065fab59d | L2104 | no manual edit
EN: [SLOW DOWN, SLOW DOWN. WHAT'S GOING ON?]
BEFORE:   Yiffany: [慢点，慢点。怎么回事？]
AFTER:   Yiffany: [慢点，慢点。怎么回事？]
ROW SFW75321189b4363bcfd3fff84a | L2105 | no manual edit
EN: [I MANAGED TO CAL- CULATE WHERE THAT ROGUE AGENT]
BEFORE:   Mauser: [我成功计算出那个脱控特工——我是说，你的弟弟——所在的位置了！]
AFTER:   Mauser: [我成功计算出那个脱控特工——我是说，你的弟弟——所在的位置了！]
ROW SFW42655082c46e0848f08ca3a1 | L2106 | no manual edit
EN: [-I MEAN, YOUR BROTHER, IS LOCATED!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW35a8324377aa9faf97f04be2 | L2107 | no manual edit
EN: [WHAT!? REALLY? WHERE IS HE?]
BEFORE:   Yiffany: [什么！？ 真的？ 他在哪？]
AFTER:   Yiffany: [什么！？ 真的？ 他在哪？]
ROW SFW7093294d9a24e819a40d4a99 | L2108 | no manual edit
EN: [YOU SEE, FIRST I NOTED THE AREAS WITHOUT RECEPTION]
BEFORE:   Mauser: [你看，我先记下了那些没有接收信号的区域，并把它们和各竞技场做了三角定位，在你-]
AFTER:   Mauser: [你看，我先记下了那些没有接收信号的区域，并把它们和各竞技场做了三角定位，在你-]
ROW SFW5dc2f4fae4c4da40f371fa12 | L2109 | no manual edit
EN: [AND TRIANGULATED THOSE WITH THE ARENAS WHERE YO-]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW627470b6c3caadc872c1d666 | L2110 | no manual edit
EN: [COME OOOOON SQUEAKS, OUT WITH IT!]
BEFORE:   Yiffany: [快点啊啊啊啊啊，小吱吱，有话快说！]
AFTER:   Yiffany: [快点啊啊啊啊啊，小吱吱，有话快说！]
ROW SFWed9b361549c61f086c1352a3 | L2111 | no manual edit
EN: [R-RIGHT! YOUR BROTHER IS LOCATED IN ZERONIA]
BEFORE:   Mauser: [对、对！你的弟弟位于泽罗尼亚]
AFTER:   Mauser: [对、对！你的弟弟位于泽罗尼亚]
ROW SFW430f6e27b5412d3222f25b18 | L2112 | no manual edit
EN: [WHY, JUST TO THE WEST OF WHERE YOU CRASH LANDED!]
BEFORE:   Mauser: [哎，就在你坠机着陆处的西边！]
AFTER:   Mauser: [哎，就在你坠机着陆处的西边！]
ROW SFW9d95d939ba850233fcf8cb13 | L2113 | no manual edit
EN: [I'VE WAS THAT CLOSE ALL THIS TIME... DAMN!]
BEFORE:   Yiffany: [我一直就离得那么近…… 该死！]
AFTER:   Yiffany: [我一直就离得那么近…… 该死！]
ROW SFW2d946416b3fd361e8e9dda82 | L2114 | EDIT E02-004
EN: [NOW NOW, YOU MAY BE ONE OF OUR TOP AGENTS]
BEFORE:   Tomcat: [好啦好啦，你或许是我们的顶尖特工之一，]
AFTER:   Tomcat: [好啦好啦，你虽说是我们的顶尖特工之一，]
ROW SFW6c31580a04f0f2b00e5c9a7a | L2115 | EDIT E02-005
EN: [BUT YOU'RE NO SCENT HOUND. THESE THINGS HAPPEN.]
BEFORE:   Tomcat: [但你可不是气味猎犬。这种事总会发生。]
AFTER:   Tomcat: [可又不是靠鼻子追踪的猎犬。没找着也不奇怪。]
ROW SFWf486b49bf4f4938e43209c17 | L2116 | no manual edit
EN: [TOMCAT'S RIGHT, YIFFANY. BUT NOW THAT YOU KNOW WHERE]
BEFORE:   Bossu: [汤姆猫说得对，伊法妮。但既然你现在知道你弟弟在哪，我想你知道该怎么做。]
AFTER:   Bossu: [Tomcat说得对，伊法妮。但既然你现在知道你弟弟在哪，我想你知道该怎么做。]
ROW SFWc12c255294382eab172e8c06 | L2117 | no manual edit
EN: [YOUR BROTHER IS, I THINK YOU KNOW WHAT TO DO.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW57a67a747fd9f7d3700c7243 | L2118 | no manual edit
EN: [TIME FOR A LITTLE FAMILY REUNION...]
BEFORE:   Yiffany: [是时候来一场小小的家人重聚了……]
AFTER:   Yiffany: [是时候来一场小小的家人重聚了……]
ROW SFW102fb53bde4a18eb47162fcf | L2119 | no manual edit
EN: [OH! AND THE NAVMAP COORDINATES HAVE BEEN SENT]
BEFORE:   Mauser: [哦！而且导航地图坐标已经发出，所以你应该能轻松到达那里。祝你好运！]
AFTER:   Mauser: [哦！而且导航地图坐标已经发出，所以你应该能轻松到达那里。祝你好运！]
ROW SFWe004ccb36f336427fef8e921 | L2120 | no manual edit
EN: [SO YOU SHOULD BE ABLE TO GET THERE EASILY. GOOD LUCK!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L2121   do { give(MapDataStarkillHint, 1) }
### P02-003 | action=apply
原问题：此处在安慰发现弟弟一直近在咫尺的姐姐；“气味猎犬／这种事总会发生”逐字感重，未把“能力强不等于能嗅踪”的安慰落地。
本轮理由：may...but是认可本领后的让步安慰，保留顶尖特工之一；第二个有效槽仍独立显示嗅踪局限与安慰。
EDIT_IDS ["E02-004", "E02-005"]

## SC0cf0a0ca5caff10d | nsfw | datadf/all.ds | Bossu.CapturedPet
CONTROL L2729 <Bossu.CapturedPet>
ROW CAT:O96a7314bc333c954f54c | L2730 | EDIT E02-006
EN: [GOOD JOB CAPTURING SOME OF THE LOCAL FAUNA, YIFFANY!]
BEFORE:   Bossu: [本地动物群抓得不错，伊法妮！]
AFTER:   Bossu: [伊法妮，抓到了本地动物，干得好！]
ROW CAT:Oda2c444361d4ffdf92f8 | L2731 | no manual edit
EN: [PREVIOUS AGENTS REPORTED SETTING UP OBSERVATION UNITS]
BEFORE:   Bossu: [之前的特工报告说，就在为你保养飞船的机库区域架设了观测单元。]
AFTER:   Bossu: [之前的特工报告说，就在为你保养飞船的机库区域架设了观测单元。]
ROW CAT:O1485d5c94a5f0ff3810c | L2732 | no manual edit
EN: [IN THE HANGAR AREA WHERE YOUR SHIP IS SERVICED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od8e4e0feb5658689e137 | L2733 | no manual edit
EN: [NOW THAT YOU MADE A FRIEND, YOU SHOULD STOP BY THERE!]
BEFORE:   Tomcat: [既然你交上了朋友，就该去那边转转！]
AFTER:   Tomcat: [既然你交上了朋友，就该去那边转转！]
ROW CAT:O1b920f9d68a963eec973 | L2734 | EDIT E02-007
EN: [YEAH, THE FRIEND- LIER YOU GET WITH THE LOCAL FAUNA]
BEFORE:   Mauser: [是啊，你跟本地动物群越处越熟，我们收到的数据也就越有用！]
AFTER:   Mauser: [是啊，你和本地动物越亲近，我们收到的数据就越有用！]
ROW CAT:O1d939e3083a7692b250a | L2735 | no manual edit
EN: [THE MORE USEFUL DATA WE CAN RECEIVE, TOO!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O261efa16fa81056af87d | L2736 | no manual edit
EN: [DON'T WORRY GUYS, I KNOW HOW THIS WORKS.]
BEFORE:   Yiffany: [别担心，伙计们，这套我熟。]
AFTER:   Yiffany: [别担心，伙计们，这套我熟。]
ROW CAT:O98a4f6cbcabfcff2e823 | L2737 | EDIT E02-008
EN: [I'LL WORK MY FAUNA MAGIC, GIVE THEM SOME ATTENTION...]
BEFORE:   Yiffany: [我施展动物群魔法，给它们点关注……]
AFTER:   Yiffany: [我会使出和动物打交道的拿手本事，好好陪陪它们……]
ROW CAT:Oe89cde8d1cbb65ca3350 | L2738 | EDIT E02-009
EN: [AND THEY'LL LOVE IT JUST LIKE EVERY OTHER MISSION!]
BEFORE:   Yiffany: [它们会爱上这个，跟每次任务一样！]
AFTER:   Yiffany: [它们一定会喜欢的，跟以往每次出任务时一样！]
### P02-004 | action=apply
原问题：fauna 是动物的集合名词，不是捕获“动物群”这个研究门类；当前宾语显著生硬。
本轮理由：some of the local fauna是捕获本地动物，不是捕获动物群这个分类；保留表扬与姓名。
EDIT_IDS ["E02-006"]
### P02-005 | action=apply
原问题：work my magic 是发挥拿手本领，不是新增动物魔法设定。后句give them attention 与前句培养亲密度呼应；现译“动物群魔法”破坏专业与调侃的切换。
本轮理由：friendlier是亲近程度，work my magic是拿手本领；三个Yiffany非空节点分别保留放心、照顾动物、既往任务经验，不合并。
EDIT_IDS ["E02-007", "E02-008", "E02-009"]

## SCfa5abde862c1f019 | nsfw | datadf/all.ds | BossuDex.ClassicArcher
CONTROL L3137 <BossuDex.ClassicArcher>
ROW CAT:O25871effa77ad5bdc2c5 | L3138 | EDIT E02-010
EN: [THE ELVES OF SCEAFYA MAY ALL BE FEMALE]
BEFORE:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
AFTER:   Bossu: [斯凯菲亚的精灵虽说全是雌性，却并非全都长生不死。]
ROW CAT:Oa6d3456892c3db2ba721 | L3139 | no manual edit
EN: [BUT THEY AREN'T ALL IMMORTAL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7fae111e665ce1629a13 | L3140 | EDIT E02-011
EN: [AS THEY CAN BREED WITH ANY MALE OF ANY SPECIES]
BEFORE:   Bossu: [由于她们能与任何物种的任何雄性繁殖，她们便带上了越来越多的有朽特征。]
AFTER:   Bossu: [她们能与任何物种的雄性繁衍后代，因此逐渐具有了越来越多会衰老死亡的生物特征。]
ROW CAT:O790dd8e1da208cd632f2 | L3141 | no manual edit
EN: [THEY'VE TAKEN ON MORE AND MORE MORTAL CHARACTERISTICS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4ae23ce7af2794c799f6 | L3142 | EDIT E02-012
EN: [WAIT, SO THAT MEANS SOME OF THEM *ARE* IMMORTAL?]
BEFORE:   Yiffany: [等等，所以这意味着她们中有些*是*不朽的？]
AFTER:   Yiffany: [等等，也就是说，她们当中有些*是*长生不死的？]
ROW CAT:Ob1d0df02de13defb3902 | L3143 | EDIT E02-013
EN: [INDEED, AS FAR AS WE CAN TELL.]
BEFORE:   Bossu: [的确，就我们所能看出的而言。]
AFTER:   Bossu: [没错，至少据我们目前所知是这样。]
ROW CAT:Oceaf87d76d4903e16846 | L3144 | no manual edit
EN: [ANY ELF THAT IS OUT IN THE OPEN AND ENGAGING IN COMBAT]
BEFORE:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
AFTER:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
ROW CAT:Ocdc5828c5aad0c882e38 | L3145 | no manual edit
EN: [WILL NO DOUBT BE A YOUNGSTER. A HUNDRED YEARS OLD AT MOST.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2fed7bf11426cea63b18 | L3146 | no manual edit
EN: [THAT'S... WOW...]
BEFORE:   Yiffany: [这……哇……]
AFTER:   Yiffany: [这……哇……]
ROW CAT:O69cbc6cd1ebefbade52c | L3147 | EDIT E02-014
EN: [DON'T GIVE IN TO AWE. YOU'LL NEED TO BE ON YOUR TOES]
BEFORE:   Bossu: [别向敬畏屈服。你得保持警觉，以便击退那些年幼精灵的攻击。]
AFTER:   Bossu: [别光顾着惊叹。要挡住那些年轻精灵的攻击，你得时刻保持警惕。]
ROW CAT:Ob1a94c803176e0827671 | L3148 | no manual edit
EN: [IN ORDER TO REPEL THE YOUNG ELVES' ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of01cc9cc00d689b5074b | L3149 | no manual edit
EN: [RIGHT, GOTTA FOCUS.]
BEFORE:   Yiffany: [对，得专注。]
AFTER:   Yiffany: [对，得专注。]
### P02-006 | action=apply
原问题：may all be...but 在此是让步“虽然”，不是物种性别尚不确定；当前“也许全是”改变判断。mortal characteristics 直译“有朽特征”难懂，连读后自然表达。
本轮理由：may all be...but让步成立；繁殖解释仅此NSFW源，不扩SFW。保留any species/any male及Bossu的as far as有限认知，星球/精灵名称沿当前。
EDIT_IDS ["E02-010", "E02-011", "E02-012", "E02-013"]
### P02-007 | action=apply
原问题：don’t give in to awe 在惊叹一百岁还年轻的上下文中是收心提醒，“别向敬畏屈服”过度庄严且不像现场简报。
本轮理由：awe接百岁仍年轻的惊叹，是指挥提醒收心；不把精灵young等同人类未成年，不改下一槽已经自然的集中精神回应。
EDIT_IDS ["E02-014"]

## SC203f504ddad4428c | nsfw | datadf/all.ds | BossuDex.ClassicBugFlier
CONTROL L3077 <BossuDex.ClassicBugFlier>
ROW CAT:O000059a9bccb01172eaa | L3078 | no manual edit
EN: [W-WHAT'S UP WITH THESE ROBO BUGS THAT KEEP COMING AT ME?]
BEFORE:   Yiffany: [这、这些一直朝我冲过来的机器虫是怎么回事？]
AFTER:   Yiffany: [这、这些一直朝我冲过来的机器虫是怎么回事？]
ROW CAT:Oda9ef6373a46d45c5e34 | L3079 | no manual edit
EN: [YOU'D THINK THEY'D RUN OUT MATERIALS BY NOW!]
BEFORE:   Yiffany: [按理说它们的材料早该用光了吧！]
AFTER:   Yiffany: [按理说它们的材料早该用光了吧！]
ROW CAT:O5b0a6357201513684e9a | L3080 | EDIT E02-015
EN: [MUCH OF THE ROBOTIC MATERIAL IN THAT OLD SPACE STATION]
BEFORE:   Bossu: [那座废弃太空站里的很多机器人材料，都是用纳米机械回收系统造出来的。]
AFTER:   Bossu: [那座老太空站里的许多机械，都配有纳米机械回收系统。]
ROW CAT:Of451268f917c1335a33b | L3081 | no manual edit
EN: [ARE BUILT WITH NANOMECHANICAL RECYCLING SYSTEMS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obfa0b0ba2acf2312e6a9 | L3082 | no manual edit
EN: [NA-NO-MY-WHAT ANAL?]
BEFORE:   Yiffany: [纳—诺—迈—什么肛门？]
AFTER:   Yiffany: [纳—诺—迈—什么肛门？]
ROW CAT:O83fd9a0441b46dc75151 | L3083 | no manual edit
EN: [BASICALLY THEY'RE DESIGNED TO SELF REPAIR ENDLESSLY.]
BEFORE:   Bossu: [简单说，它们被设计成能无限自我修复。]
AFTER:   Bossu: [简单说，它们被设计成能无限自我修复。]
ROW CAT:O26a3f0cec5b86b5e904b | L3084 | no manual edit
EN: [IT USED TO BE A POPULAR LOW- MAINTENANCE DESIGN]
BEFORE:   Bossu: [这种低维护设计以前很受欢迎，直到后来人们发现，等它们过时以后，也没办法把它们拆开。]
AFTER:   Bossu: [这种低维护设计以前很受欢迎，直到后来人们发现，等它们过时以后，也没办法把它们拆开。]
ROW CAT:Ocf01f56c24cf5f771def | L3085 | no manual edit
EN: [UNTIL IT WAS REALIZED THAT THEY COULDN'T BE TAKEN]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O0d8bf9979aaea2bf9468 | L3086 | no manual edit
EN: [APART WHEN THEY BECAME OBSOLETE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9404ef39ae67fd3db122 | L3087 | no manual edit
EN: [THEY REPAIR THEM- SELVES FASTER THAN WE CAN BREAK EM!]
BEFORE:   Bossu: [它们自我修复的速度比我们破坏的还快！]
AFTER:   Bossu: [它们自我修复的速度比我们破坏的还快！]
ROW CAT:O49332bbe010db8b1b1d7 | L3088 | no manual edit
EN: [AHH, SO THAT'S WHY I'VE NEVER SEEN THESE KIND OF]
BEFORE:   Yiffany: [啊，难怪我从小到大都没见过这种机器人……]
AFTER:   Yiffany: [啊，难怪我从小到大都没见过这种机器人……]
ROW CAT:Oe31aff21e4cfdaed306f | L3089 | no manual edit
EN: [ROBOTS WHILE GROWING UP...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of7c7443674eea58a5741 | L3090 | no manual edit
EN: [...NEATO!]
BEFORE:   Yiffany: [……真酷！]
AFTER:   Yiffany: [……真酷！]
### P02-008 | action=apply
原问题：built with ... systems 指构造中配备回收系统；当前“都是用…造出来的”错成生产手段，与后文自我修复的说明脱节。
本轮理由：built with是机械构造配有系统；前问耗材、后答自修支持此读法，不能说系统生产机器人材料。
EDIT_IDS ["E02-015"]
### P02-009 | action=defer
原问题：源文将nanomechanical故意听乱并拐到anal；“纳—诺—迈—什么肛门”只是英语音节转录，中文无法承接前句“纳米机械”。提案保留一次听岔的荤笑，不给角色新增固定口癖。
本轮理由：defer：独立抽核needs_revision成立，问题确认但原提案纳米机/什么肛没有真正中文音桥。重新尝试机械的近音转折后仍需生造不通用的性词，不能将这种文字拼接冒充自然听错双关。本轮尚无可确认的中文节点稿，保留原快照待专项重写；不删anal荤笑、不加新动作、不照抄退修稿。Bossu下一槽自修解释准确，不另改。
EDIT_IDS []

## SC3a3a119fd7820329 | nsfw | datadf/all.ds | BossuDex.ClassicFenfen
CONTROL L3064 <BossuDex.ClassicFenfen>
ROW CAT:Oa6d18b09a8386995abec | L3065 | no manual edit
EN: [HEY BOSSU, I'VE FOUND SOME LITTLE ANTHROID DOG FELLAS]
BEFORE:   Yiffany: [嘿 BOSSU，我发现了几只小小的拟人犬家伙，但它们身上有点非常古怪的地方……]
AFTER:   Yiffany: [嘿 BOSSU，我发现了几只小小的拟人犬家伙，但它们身上有点非常古怪的地方……]
ROW CAT:O10c30c6c4fbaee77d171 | L3066 | no manual edit
EN: [BUT THERE'S SOMETHING REAL ODD ABOUT THEM...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa82bb5297602e9c2a1e1 | L3067 | no manual edit
EN: [THEY DON'T SEEM TO RESPOND TO ANYTHING I SAY.]
BEFORE:   Yiffany: [它们好像对我说的任何话都没反应。]
AFTER:   Yiffany: [它们好像对我说的任何话都没反应。]
ROW CAT:Odc69224b4b20ba216f7a | L3068 | no manual edit
EN: [AND ARE EVEN THROWING ROCKS AT ME!]
BEFORE:   Yiffany: [甚至还朝我扔石头！]
AFTER:   Yiffany: [甚至还朝我扔石头！]
ROW CAT:Oc20d580ebf9fe1f0c4ef | L3069 | no manual edit
EN: [THEY MAY LOOK ORGANIC, BUT BELIEVE IT OR NOT THOSE ARE]
BEFORE:   Bossu: [它们看着也许像有机生物，但信不信由你，那些其实是图托恩物种Fenfen的机械复制品。]
AFTER:   Bossu: [它们看着也许像有机生物，但信不信由你，那些其实是图托恩物种Fenfen的机械复制品。]
ROW CAT:Oabf4e035c119513c9d9c | L3070 | no manual edit
EN: [MECHANICAL COPIES OF A TUTONE SPECIES, THE FENFEN.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O687dfbe15106f4ba8330 | L3071 | no manual edit
EN: [WOAH, REALLY?]
BEFORE:   Yiffany: [哇哦，真的吗？]
AFTER:   Yiffany: [哇哦，真的吗？]
ROW CAT:O06df7215b3a78f02c7d1 | L3072 | EDIT E02-016
EN: [IF THERE ARE FLESH AND FUR VARIETIES OF THAT SPECIES STILL]
BEFORE:   Bossu: [如果这颗星球上还存在那个物种的血肉与毛皮变种，也还没有任何特工撞见过它们。]
AFTER:   Bossu: [如果这颗星球上还有有血有肉、长着皮毛的Fenfen，目前也还没有特工遇到过。]
ROW CAT:Ob652aabd0f59c9df7e01 | L3073 | no manual edit
EN: [ON THE PLANET, NO AGENTS HAVE RUN INTO THEM YET.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofb481ed7de5a55002a18 | L3074 | no manual edit
EN: [REPORTS OF FENFEN OUTFITS STREWN ABOUT ARE ALL WE HAVE.]
BEFORE:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
AFTER:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
ROW CAT:O4a779f0d302a2fb467bb | L3075 | no manual edit
EN: [HOW MYSTERIOUS! I'LL HAVE TO KEEP AN EYE OUT FOR THEM.]
BEFORE:   Yiffany: [真是神秘！我得多留意它们才行。]
AFTER:   Yiffany: [真是神秘！我得多留意它们才行。]
### P02-010 | action=apply
原问题：flesh and fur varieties 在机械复制品对照下指真正的生物个体，不是“血肉与毛皮变种”两个变种或变异设定。原文if与yet 的未知状态保留。
本轮理由：机械复制体与flesh and fur对举，指有血肉皮毛的活体而非两个变种；只改完整头节点，if/yet/no agents保留，后两条现译不必改。
EDIT_IDS ["E02-016"]

## SCec58e954ab659019 | sfw | datadf/all.ds | BossuDex.ClassicJellyfish
CONTROL L3080 <BossuDex.ClassicJellyfish>
ROW SFWfd2c4208f624717be854fef7 | L3081 | no manual edit
EN: [SAAAY BOSSU, I'M NOT A MERMAID, AM I?]
BEFORE:   Yiffany: [我说啊 Bossu，我不是人鱼，对吧？]
AFTER:   Yiffany: [我说啊 Bossu，我不是人鱼，对吧？]
ROW SFW397245f79210d8325661f969 | L3082 | no manual edit
EN: [BECAUSE I'M DEFIN- ITELY SEEING JELLY FISH AROUND HERE.]
BEFORE:   Yiffany: [因为我在这附近确实看到水母了。]
AFTER:   Yiffany: [因为我在这附近确实看到水母了。]
ROW SFW21077e81213c5d4b82446ec3 | L3083 | no manual edit
EN: [THE STRANGE HAPPE- NINGS ON TUTONE HAVE LEAD TO]
BEFORE:   Bossu: [图托恩上发生的怪事，导致有人目击到非实体的水母]
AFTER:   Bossu: [图托恩上发生的怪事，导致有人目击到非实体的水母]
ROW SFW00e9c441a1b8ca0d9a1d9ef4 | L3084 | no manual edit
EN: [SIGHTINGS OF NON- PHYSICAL JELLY FISH] 
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWfa93d99394124712bb56f157 | L3085 | no manual edit
EN: [THEY SEEM PLENTY PHYSICAL TO ME, OW...]
BEFORE:   Yiffany: [对我来说它们可实体得很，哎哟……]
AFTER:   Yiffany: [对我来说它们可实体得很，哎哟……]
ROW SFW340c890d2c0cc98f059d57ef | L3086 | no manual edit
EN: [ON THE CONTRARY, IF YOU'RE TO BELIEVE THE REPORTS...]
BEFORE:   Bossu: [恰恰相反，如果你相信那些报告的话……]
AFTER:   Bossu: [恰恰相反，如果你相信那些报告的话……]
ROW SFW4c3a2bbc20d8bbccb50a353e | L3087 | no manual edit
EN: [ANY CREATURE FLASHING OMINOUSLY PURPLE ON TUTONE]
BEFORE:   Bossu: [在图托恩上闪着不祥紫光的任何生物，其实都是灵能躁动形成的幻影。]
AFTER:   Bossu: [在图托恩上闪着不祥紫光的任何生物，其实都是灵能躁动形成的幻影。]
ROW SFWeb76b3980bcbf4a9af931ba0 | L3088 | no manual edit
EN: [IS ACTUALLY AN APPARITION OF PSYCHIC TURMOIL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW241b37f02d21f547e53bebf9 | L3089 | no manual edit
EN: [HOW YOU DEAL WITH THEM, WE CANNOT SAY FROM HERE.]
BEFORE:   Bossu: [至于该怎么应付它们，我们在这边可说不准。]
AFTER:   Bossu: [至于该怎么应付它们，我们在这边可说不准。]
ROW SFWd9ca903b6e9892ef8c15b46b | L3090 | EDIT E02-017
EN: [HMM, PSYCHIC, YOU SAY.]
BEFORE:   Yiffany: [唔，灵能，你这么说。]
AFTER:   Yiffany: [唔，你说是灵能啊。]
ROW SFWdbbc094b6a523e01fe87bf5c | L3091 | no manual edit
EN: [GUESS I'LL HAVE TO FIGURE IT OUT MYSELF...]
BEFORE:   Yiffany: [看来只能我自己想办法搞清楚了……]
AFTER:   Yiffany: [看来只能我自己想办法搞清楚了……]
### P02-011 | action=apply
原问题：“灵能，你这么说”不成口语回应，角色是在抓住总部的线索思考对策，不是重复汇报。术语精神力为本段与包内PSY的暂定统一方向，仍需术语终裁。
本轮理由：只修you say的口语回应，不以本提案终裁PSY术语；沿同场现用灵能，后一个非空槽继续保留自行研究的意思。
EDIT_IDS ["E02-017"]

## SC0c836076db0ee88f | sfw | datadf/all.ds | Mauser.Area0Transportal1 noselect
CONTROL L2048 <Mauser.Area0Transportal1 noselect>
ROW SFW1791ae9545e4667ee6694b02 | L2049 | no manual edit
EN: [YIFFANY, HAVE YOU COME ACROSS ANY TELEPORTALS YET?]
BEFORE:   Mauser: [伊法妮，你遇到传送门了吗？]
AFTER:   Mauser: [伊法妮，你遇到传送门了吗？]
ROW SFW4ff5bb7003b26eaf52f33924 | L2050 | no manual edit
EN: [YEAH, I'VE JUST ENCOUNTERED ONE.]
BEFORE:   Yiffany: [嗯，我刚遇到过一个。]
AFTER:   Yiffany: [嗯，我刚遇到过一个。]
ROW SFW20a19114dfb51c24ade7f5d0 | L2051 | no manual edit
EN: [HOW'S MY SHIP BEEN SINCE I LEFT IT?]
BEFORE:   Yiffany: [我走之后我的飞船怎么样了？]
AFTER:   Yiffany: [我走之后我的飞船怎么样了？]
ROW SFW10fb49e444bfc811f6d26cba | L2052 | no manual edit
EN: [WE MANAGED TO SET IT ON FOLLOW MODE]
BEFORE:   Tomcat: [我们设法把它设成了跟随模式。]
AFTER:   Tomcat: [我们设法把它设成了跟随模式。]
ROW SFW6a971f7c5766b9b4d3fda5e2 | L2053 | no manual edit
EN: [SO YOU SHOULD BE ABLE TO TELEPORT INTO IT, DEAR.]
BEFORE:   Tomcat: [所以你应该能传送进你的飞船了，亲爱的。]
AFTER:   Tomcat: [所以你应该能传送进你的飞船了，亲爱的。]
ROW SFWa0135058a5e523d6b74a0c8d | L2054 | no manual edit
EN: [GREAT, THEN I CAN GO AND BLAST THOSE DARN SHIPS THA-]
BEFORE:   Yiffany: [太好了，那我就能去轰掉那些该死的飞船——]
AFTER:   Yiffany: [太好了，那我就能去轰掉那些该死的飞船——]
ROW SFW62d191fa2ec474938e341901 | L2055 | EDIT E02-018
EN: [HOLD ON THERE PUP. YOUR SHIP MAY BE BARELY WORKING]
BEFORE:   Bossu: [等一下，小子。你的飞船恐怕只能勉强运转，不过你只能贴地飞行。]
AFTER:   Bossu: [等一下，小家伙。你的飞船虽说勉强能飞，但只准贴地飞行。]
ROW SFW400dfb9a4583f6b90eae566f | L2056 | no manual edit
EN: [BUT YOU MAY ONLY FLY NAP-OF-THE- EARTH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWc96667c21486114525893bfe | L2057 | EDIT E02-019
EN: [WE CAN'T RISK YOU GETTING REDOWNED... OR WORSE.]
BEFORE:   Bossu: [我们不能冒着让你被击落……甚至更糟的风险。]
AFTER:   Bossu: [我们不能冒险让你再被击落……甚至遭遇更糟的事。]
ROW SFW198a467e49ce96e09cf0baff | L2058 | no manual edit
EN: [AWWW MAAAAAN!]
BEFORE:   Yiffany: [啊啊——！]
AFTER:   Yiffany: [啊啊——！]
ROW SFW9d6a1ad65837185432d11279 | L2059 | no manual edit
EN: [NO GOING AFTER THOSE SCUM WITH GUNS BLAZING, GRRRL.] 
BEFORE:   Tomcat: [不准开着枪冲去找那帮混蛋，丫头。] 
AFTER:   Tomcat: [不准开着枪冲去找那帮混蛋，丫头。] 
ROW SFW4cd825f9c0023abd07cf53ee | L2060 | no manual edit
EN: [THAT'S RIGHT! WE'RE RELYING SOLELY ON YOU NOW!]
BEFORE:   Mauser: [没错！现在我们只能指望你了！]
AFTER:   Mauser: [没错！现在我们只能指望你了！]
ROW SFW9838bb7d1d145d5986884a4c | L2061 | no manual edit
EN: [ALRIGHT ALRIGHT, I'LL TAKE THINGS SLOWLY...]
BEFORE:   Yiffany: [好吧好吧，我会慢慢来的……]
AFTER:   Yiffany: [好吧好吧，我会慢慢来的……]
ROW SFWff9bf288a91b5251c86f3bbe | L2062 | no manual edit
EN: [GOOD GIRL. DON'T FORGET, WE'RE ALL HERE TO HELP YOU.]
BEFORE:   Bossu: [好姑娘。别忘了，我们都在这儿帮你。]
AFTER:   Bossu: [好姑娘。别忘了，我们都在这儿帮你。]
ROW SFWaccdcb7f7a35affe44724e4c | L2063 | no manual edit
EN: [AND ON TOP OF THAT, THE HANGAR THAT THE OTHER AGENTS]
BEFORE:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
AFTER:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
ROW SFWc36448961c77db37ad18a029 | L2064 | no manual edit
EN: [WERE USING AS AN AUTOPILOT SERVICE STATION]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW9f2ef0b2a12217e377df3aaf | L2065 | no manual edit
EN: [SEEMS TO STILL BE RUNNING.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWa6629a61ae85fa82836a6ad5 | L2066 | no manual edit
EN: [YOU SHOULD STOP BY THERE AND SEE IF ANYONE'S AROUND!]
BEFORE:   Mauser: [你该去那边看看有没有人在！]
AFTER:   Mauser: [你该去那边看看有没有人在！]
ROW SFW3a66000f1982eb6b47f7ce81 | L2067 | no manual edit
EN: [SOUNDS LIKE A GOOD IDEA. ROGER THAT!]
BEFORE:   Yiffany: [听起来不错。收到！]
AFTER:   Yiffany: [听起来不错。收到！]
### P02-012 | action=apply
原问题：“恐怕只能勉强运转，不过你只能”转折不成立；两项是飞船状态与飞行限制。该SFW女主分支叫“小子”也造成称呼性别漂移，采用不额外设年龄的“小家伙”。
本轮理由：前一may是承认飞船勉强能飞的让步，后一may only是许可限制；女线pup不应落为小子。两个非空槽保留状态/限制与风险两层。
EDIT_IDS ["E02-018", "E02-019"]

## SC0b2a2d5c9e9c6c62 | nsfw | datadf/all.ds | Mauser.Slime noselect noamendfreq
CONTROL L3342 <Mauser.Slime noselect noamendfreq>
ROW CAT:O820d3707b65dfc5b4551 | L3343 | no manual edit
EN: [GLOOP...]
BEFORE:   Yiffany: [咕叽……]
AFTER:   Yiffany: [咕叽……]
ROW CAT:O139baccbe4571e62632d | L3344 | no manual edit
EN: [H-HUH? WHO'S THIS? YIFFAI?!]
BEFORE:   Mauser: [啊、啊？谁在说话？伊法伊？！]
AFTER:   Mauser: [啊、啊？谁在说话？伊法伊？！]
ROW CAT:O9bbf3a7be671102d8a38 | L3345 | no manual edit
EN: [GLUGH]
BEFORE:   Yiffany: [咕噜]
AFTER:   Yiffany: [咕噜]
ROW CAT:Ode619721e1496d1af8af | L3346 | no manual edit
EN: [UM... THIS CHANNEL IS FOR AUTHORIZED COSMOBREEDERS ONLY.]
BEFORE:   Mauser: [呃……这个频道仅供授权的宇宙育种者使用。]
AFTER:   Mauser: [呃……这个频道仅供授权的宇宙育种者使用。]
ROW CAT:O7ed3d1b243d0ec83fdf1 | L3347 | no manual edit
EN: [I'LL HAVE TO DISCONNECT, 'MAM'. OVER.]
BEFORE:   Mauser: [只好挂断了，“女士”。完毕。]
AFTER:   Mauser: [只好挂断了，“女士”。完毕。]
### P02-033 | action=defer
原问题：女主史莱姆分支speaker为Yiffany，而Mauser原文喊YIFFAI；当前忠实跟随源文，不能直接报关系错译或擅改成伊法妮。须源作者/触发核验后裁决。
本轮理由：defer：该节点源确为YIFFAI、发话对象speaker为Yiffany且有MAM，属于源/触发疑点；当前跟源不能直接认定翻译关系错，不改名或亲属关系。
EDIT_IDS []

## SC6fdb8418c5faf950 | sfw | datadf/all.ds | MauserHints_AreaE.AfterFirstEnteredAreaE
CONTROL L3580 <MauserHints_AreaE.AfterFirstEnteredAreaE>
ROW SFW5fcadca254065f81d358d161 | L3581 | EDIT E02-020
EN: [I'M DETECTING STRONG ENERGY SIGNATURES DEEP IN]
BEFORE:   Mauser: [我探测到强烈能量特征，位于]
AFTER:   Mauser: [伊法妮，我探测到了很强的能量信号。]
ROW SFWd40939bcf1fb5974ce06ba38 | L3582 | EDIT E02-021
EN: [THE NORTHEAST OF THAT MOON, YIFFANY.]
BEFORE:   Mauser: [在那颗卫星的东北部，伊法妮。]
AFTER:   Mauser: [就在那颗卫星的东北部深处。]
ROW SFW744c27461afee6102905e239 | L3583 | no manual edit
EN: [YOU SHOULD TRY TO FIND A WAY INTO THOSE CAVERNS.]
BEFORE:   Mauser: [你该试着找条路进那些洞窟。]
AFTER:   Mauser: [你该试着找条路进那些洞窟。]
### P02-013 | action=apply
原问题：当前跨框连读成“位于在那颗卫星”，句子断裂；deep 的深处定位也丢失，影响寻找洞窟的指示。
本轮理由：两个非空定位槽不能合并；按中文意群把能量检测与东北部深处定位分别放置，第三槽建议现译已完整。
EDIT_IDS ["E02-020", "E02-021"]

## SC60ed91a511e551d2 | nsfw | datadf/all.ds | TomcatItems.CosmoCard
CONTROL L4691 <TomcatItems.CosmoCard>
ROW CAT:Oe42913059da382b2e142 | L4692 | no manual edit
EN: [HEEEEY WE'VE GOT COSMOCARDS ON THIS PLANET!]
BEFORE:   Yiffany: [嘿————这颗星球上有宇宙卡！]
AFTER:   Yiffany: [嘿————这颗星球上有宇宙卡！]
ROW CAT:O941d1568f55e5cc2d492 | L4693 | no manual edit
EN: [OH NEAT! THOSE ARE GREAT FOR SOME FAUNA INFO]
BEFORE:   Tomcat: [哦，不错！那些对了解生物很有用]
AFTER:   Tomcat: [哦，不错！那些对了解生物很有用]
ROW CAT:Oad234307117b0fcbc530 | L4694 | EDIT E02-022
EN: [YUP, GET ALL THAT GREAT INFO ON WHAT'S GONNA]
BEFORE:   Yiffany: [对，把那些会直直塞进你里面的东西的好信息都拿到！]
AFTER:   Yiffany: [可不嘛，那些要被硬塞进你身体里的东西，都能了解个透！]
ROW CAT:O7b51efe0da728afd52d6 | L4695 | no manual edit
EN: [BE JAMMED RIGHT UP INSIDE OF YA!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O23ea5c8ed4918d1e538d | L4696 | no manual edit
EN: [...]
BEFORE:   Tomcat: [……]
AFTER:   Tomcat: [……]
ROW CAT:O969105df60b44f1811b2 | L4697 | no manual edit
EN: [...AND OF ENEMY STATS AND ITEM DROPS, YOU KNOW.]
BEFORE:   Tomcat: [……还有敌人属性和掉落物，你知道的。]
AFTER:   Tomcat: [……还有敌人属性和掉落物，你知道的。]
ROW CAT:O889386a659b0a2ebef46 | L4698 | no manual edit
EN: [REALLY? IS THAT STUFF ON THE FRONT OF THE CARDS]
BEFORE:   Yiffany: [真的？那些东西是在卡片正面还是哪儿？我从来不去看那一面……]
AFTER:   Yiffany: [真的？那些东西是在卡片正面还是哪儿？我从来不去看那一面……]
ROW CAT:O0f1c998ff1376d74eda2 | L4699 | no manual edit
EN: [OR SOMETHING? I NEVER LOOK AT THAT SIDE...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od81753aa11063247cc2d | L4700 | no manual edit
EN: [EVEN THOUGH YOU HAVE TO SEE THE FRONTSIDE FIRST]
BEFORE:   Tomcat: [就算你进 P.A.W 子菜单看卡片数据时，也得先看到正面……]
AFTER:   Tomcat: [就算你进 P.A.W 子菜单看卡片数据时，也得先看到正面……]
ROW CAT:O5b4960792f7eb254d64e | L4701 | no manual edit
EN: [WHILE ACCESSING THE CARD DATA IN YOUR P.A.W SUBMENU...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofbb1adfd4a9613dfb175 | L4702 | EDIT E02-023
EN: [OH YEAH I JUST HABITUALLY FLIP TO THE /GOOD/ SIDE]
BEFORE:   Yiffany: [哦对，我就是习惯性翻到/好的/那一面]
AFTER:   Yiffany: [哦对，我就是习惯翻到/好看/的那一面。]
ROW CAT:Odccaa53d6a43504e404a | L4703 | no manual edit
EN: [IF YOU KNOW WHAT I MEAN!]
BEFORE:   Yiffany: [你懂我意思吧！]
AFTER:   Yiffany: [你懂我意思吧！]
ROW CAT:Oc806f262e9defda611b0 | L4704 | no manual edit
EN: [RIIIIIIIIGHT...]
BEFORE:   Tomcat: [是————啊……]
AFTER:   Tomcat: [是————啊……]
CONTROL L4706 ### Ship Parts
### P02-014 | action=apply
原问题：“把…东西的好信息都拿到”英语名词链生硬，笑点是把fauna info转成对侵入者的情色了解，非赞美信息“好”。
本轮理由：fauna info被Yiffany歪为了解将塞进身体的东西；修名词链，保留被塞入的施受关系，不改成家伙主动塞别人。
EDIT_IDS ["E02-022"]
### P02-015 | action=apply
原问题：/GOOD/是强调并暗指情色那面，“/好的/那一面”既译腔也丢掉对正面敌人属性的取舍笑点；不扩写具体图案。
本轮理由：GOOD强调偏爱的那面，按情色背面笑话自然写好看，但保留/ /样式；不采原建议新增一拿到的时间条件，第二槽现译完整。
EDIT_IDS ["E02-023"]

## SC156d54281be3db1d | nsfw | datadf/all.ds | TomcatItems.SpecialAnklet
CONTROL L4361 <TomcatItems.SpecialAnklet>
ROW CAT:Ofab4b72b42de039d89eb | L4362 | no manual edit
EN: [WELL WELL, LOOKS LIKE YOU GOT YOURSELF AN]
BEFORE:   Tomcat: [哟哟，看来你搞到了一只反重力踝环！]
AFTER:   Tomcat: [哟哟，看来你搞到了一只反重力踝环！]
ROW CAT:Oe62a4aa1059a364a5bc8 | L4363 | no manual edit
EN: [ANTI-GRAV ANKLET!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2c8f92e31c46b0e8dcdd | L4364 | no manual edit
EN: [YEAH, NEVER DID LIKE THESE THINGS. PREFER MY TAZER]
BEFORE:   Yiffany: [是啊，我一直不喜欢这东西。我更喜欢双脚着地，用电击枪进行对决。]
AFTER:   Yiffany: [是啊，我一直不喜欢这东西。我更喜欢双脚着地，用电击枪进行对决。]
ROW CAT:O6839692a40e387eeb69b | L4365 | no manual edit
EN: [DUELS WITH BOTH FEET ON THE GROUND.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O79cbf1cb2271c265a62a | L4366 | EDIT E02-024
EN: [NOT TO MENTION, YOU COULD NEVER BEAT MY AIRTIME RECORD]
BEFORE:   Tomcat: [更别说，你永远破不了我在学院那会儿的滞空纪录……]
AFTER:   Tomcat: [更何况，你当年在学院可从没破过我的滞空纪录……]
ROW CAT:Of0cf4feed28708a53023 | L4367 | no manual edit
EN: [BACK AT THE ACADEMY...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O06f887a2d5c397ad1f70 | L4368 | EDIT E02-025
EN: [GRR. NOT LIKE I TRIED VERY HARD OR ANYTHING...]
BEFORE:   Yiffany: [哼。又不是我很努力试过还是怎样……]
AFTER:   Yiffany: [哼，又不是我认真试过了……]
ROW CAT:O74f519d224040430d054 | L4369 | no manual edit
EN: [RIIIGHT. WELL YOU PROBABLY DON'T NEED TO HEAR IT, BUT]
BEFORE:   Tomcat: [是——啊。好吧，你大概不用听，不过半空中贴墙再跳，就能触发！]
AFTER:   Tomcat: [是——啊。好吧，你大概不用听，不过半空中贴墙再跳，就能触发！]
ROW CAT:Od740658be81e944c6cdc | L4370 | no manual edit
EN: [HUG A WALL MID-AIR AND JUMP AGAIN TO TRIGGER IT!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O86cbc877ab5a35f985ee | L4371 | no manual edit
EN: [I REMEMBER HOW TO USE IT!!! YIFFANY OUT!]
BEFORE:   Yiffany: [我记得怎么用！！！伊法妮完毕！]
AFTER:   Yiffany: [我记得怎么用！！！伊法妮完毕！]
### P02-016 | action=apply
原问题：could never beat 是既往纪录挑战，当前“永远破不了”将过去说成未来永久断言；“又不是我很努力试过还是怎样”使嘴硬不自然。保留她本人没认真试的说辞，不借男线回忆裁决真伪。
本轮理由：back at academy限定既往纪录；没认真试是Yiffany嘴硬的本人说辞，不用男线回忆裁真伪，不增强为根本从未努力。
EDIT_IDS ["E02-024", "E02-025"]

## SCd3fafd3fc4ec71b5 | nsfw | datadf/all.ds | TomcatItems.SpecialPsycards
CONTROL L4397 <TomcatItems.SpecialPsycards>
ROW CAT:O7c9f522b8050258a86a8 | L4398 | EDIT E02-026
EN: [UGH, I HOPE THAT SKEEVY KOBOLD DIDN'T JUST SCAM ME...]
BEFORE:   Yiffany: [呃，希望那个恶心的科博德不是只骗了我……]
AFTER:   Yiffany: [啧，希望那个猥琐的科博德没把我给骗了……]
ROW CAT:Oc01dd149b7329f57dd2a | L4399 | EDIT E02-027
EN: [TOMCAT, CAN I GET A SCAN ON THESE CARDS?]
BEFORE:   Yiffany: [汤姆猫，能扫描一下这些卡吗？]
AFTER:   Yiffany: [Tomcat，能帮我扫描一下这些卡吗？]
ROW CAT:O6df8c578323637af4488 | L4400 | no manual edit
EN: [GIRL, WHATEVER YOU JUST BOUGHT... ]
BEFORE:   Tomcat: [姑娘，你刚买的那东西……]
AFTER:   Tomcat: [姑娘，你刚买的那东西……]
ROW CAT:Oc0a74050e0e36799c111 | L4401 | no manual edit
EN: [IS JUST A WHITE HOT POINT OF LIGHT ON MY SCANNER.]
BEFORE:   Tomcat: [在我的扫描仪上只是一个白热的光点。]
AFTER:   Tomcat: [在我的扫描仪上只是一个白热的光点。]
ROW CAT:Obbd4d9653b1dbb50a7bf | L4402 | no manual edit
EN: [WITH THAT MUCH ENERGY... YOU SHOULD BE BURSTING INTO]
BEFORE:   Tomcat: [能量这么高……光是拿着它，你就应该会浑身冒火。]
AFTER:   Tomcat: [能量这么高……光是拿着它，你就应该会浑身冒火。]
ROW CAT:O973f95626824074a2198 | L4403 | no manual edit
EN: [FLAMES JUST HOLDING IT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4870d76097f0ff06c40b | L4404 | no manual edit
EN: [HOW... CONFIDENCE INSPIRING. WELL, I BOUGHT EM]
BEFORE:   Yiffany: [还真是……让人信心十足啊。好吧，反正都买了，那我就用精神力来试试它们吧。] 
AFTER:   Yiffany: [还真是……让人信心十足啊。好吧，反正都买了，那我就用精神力来试试它们吧。] 
ROW CAT:Oc1173adbd3e709e9a26d | L4405 | no manual edit
EN: [SO I GUESS I'LL JUST TRY THEM OUT WITH MY PSY POWERS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P02-017 | action=apply
原问题：just scam me 是刚买后担心上当，不是“不是只骗了我”的范围否定；现句易理解成担心受害者不止自己，与要求扫描核货的意图不符。
本轮理由：just scam me是担心刚上当，不是只有自己被骗；两个现有非空节点分别放抱怨和请求扫描。同步在被改请求中执行明确Tomcat命名。
EDIT_IDS ["E02-026", "E02-027"]

## SCce26cc53dbd39f07 | nsfw | datadm/all.ds | AreaC_MacsenDark.TazerRapier
CONTROL L1206 <AreaC_MacsenDark.TazerRapier>
ROW CAT:O06ed0e4e63f85b7cc02a | L1207 | no manual edit
EN: This is a pretty little elven letter opener, if I do say so myself!
BEFORE:   * 要我自己说，这可是一把精巧的精灵拆信刀！
AFTER:   * 要我自己说，这可是一把精巧的精灵拆信刀！
ROW CAT:O25aa1989ac563f073a4f | L1208 | EDIT E02-028
EN: Feather light, just like how those dresses the elves craft will make you feel.
BEFORE:   * 轻得像羽毛，就像精灵们缝的那些裙子会让你感觉的那样。
AFTER:   * 轻得像羽毛，就跟穿上精灵做的裙子时那种轻盈的感觉一样。
ROW CAT:O3cdd39af6e8eee373ebb | L1209 | no manual edit
EN: ...not that I would know anything about those!
BEFORE:   * ……当然，那些裙子我一点都不了解！
AFTER:   * ……当然，那些裙子我一点都不了解！
### P02-018 | action=apply
原问题：“就像…会让你感觉的那样”英语从句悬空；需让裙子造成轻盈的联想自然接到心虚否认，保留商人玩笑不新增穿着经历。
本轮理由：只修轻盈裙子联想的悬空句法，前夸刀/后心虚否认已完整；不把玩笑认定为商人真实穿裙履历。
EDIT_IDS ["E02-028"]

## SCde4ad2fe0ab8d046 | sfw | datadm/all.ds | Bossu.AreaBTransportal2_a noselect
CONTROL L2348 <Bossu.AreaBTransportal2_a noselect>
ROW SFWb352cadede0f223905acce8e | L2349 | no manual edit
EN: [COMMAND, THIS IS AGENT YIFFAI. I'VE ENCOUNTERED ANOTHER]
BEFORE:   Yiffai: [指挥部，这里是特工伊法伊。我又遇到了另一座传送门。我获准出击了吗？]
AFTER:   Yiffai: [指挥部，这里是特工伊法伊。我又遇到了另一座传送门。我获准出击了吗？]
ROW SFWa3bfee353eee073e6a59690f | L2350 | no manual edit
EN: [TELEPORTAL. DO I HAVE PERMISSION TO SORTIE?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWfe4dcf171c9ea84761787dbe | L2351 | EDIT E02-029
EN: [NEGATIVE, AGENT. NAP-OF-THE-EARTH RE- STRICTIONS PERSIST]
BEFORE:   Bossu: [否定，特工。贴地飞行的限——制仍在持续，不过，你的飞船已安然无恙地驶到你身边。]
AFTER:   Bossu: [不批准，特工。贴地飞行限制仍然有效，不过你的飞船已平安抵达你所在的位置。]
ROW SFWff74e9cc52f5c4c313a275a8 | L2352 | no manual edit
EN: [HOWEVER, YOUR SHIP HAS NAVIGATED TO YOU UNMOLESTED]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW83700f79f110d57656ab98de | L2353 | no manual edit
EN: [NOT ONLY THAT, BUT NOW THAT YOU'VE VISUALLY CONFIRMED]
BEFORE:   Bossu: [不止如此，既然你已经亲眼确认了这座传送门的地面坐标，应该就能随心所欲地回到那里了。]
AFTER:   Bossu: [不止如此，既然你已经亲眼确认了这座传送门的地面坐标，应该就能随心所欲地回到那里了。]
ROW SFWacfc83cbda53cbb28e3ffda7 | L2354 | no manual edit
EN: [THIS TELEPORTAL'S GROUND COORDINATES YOU SHOULD BE]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW443edb7c1ff15472cafb6067 | L2355 | no manual edit
EN: [ABLE TO RETURN TO IT AS YOU DESIRE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWa6760e9ceea06e598b8407d4 | L2356 | no manual edit
EN: [IS VISUAL CONFIRMATION REALLY NECESSARY, SIR?]
BEFORE:   Yiffai: [真的有必要亲眼确认吗，长官？]
AFTER:   Yiffai: [真的有必要亲眼确认吗，长官？]
ROW SFWa836e1ebeace429cd23ea322 | L2357 | no manual edit
EN: [CAN'T I JUST USE THE TELEPORTAL COORDINATES FROM]
BEFORE:   Yiffai: [我就不能直接沿用之前那些特工的传送门坐标吗？]
AFTER:   Yiffai: [我就不能直接沿用之前那些特工的传送门坐标吗？]
ROW SFW1081caf63fffbac179b49a61 | L2358 | no manual edit
EN: [THE PREVIOUS AGENTS?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWfc559e66b4dabf26ba221dd8 | L2359 | no manual edit
EN: [SORRY, WE CAN'T RI- SK YOU PORTING INTO A SOLID SURFACE]
BEFORE:   Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的唯一希望。]
AFTER:   Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的唯一希望。]
ROW SFW09f544c8e3bd8d2614c1845b | L2360 | no manual edit
EN: [ESPECIALLY AS YOU ARE OUR ONLY HOPE LEFT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW10d37e708bc1861e9cb97381 | L2361 | no manual edit
EN: [ALRIGHT, UNDERSTOOD. YIFFAI OUT!] 
BEFORE:   Yiffai: [明白了。伊法伊结束通话！] 
AFTER:   Yiffai: [明白了。伊法伊结束通话！] 
### P02-019 | action=apply
原问题：NEGATIVE 回答许可应为不批准；RE- STRICTIONS为排版断词，不是角色口吃或拉长音，当前“限——制”制造不必要演出。
本轮理由：NEGATIVE是不批准许可；RE- STRICTIONS排版断词不是口吃，完整头槽还含飞船平安抵达信息，不能删。
EDIT_IDS ["E02-029"]

## SC3011f2ede9bd4f18 | nsfw | datadm/all.ds | BossuDex.ClassicBlocker
CONTROL L2894 <BossuDex.ClassicBlocker>
ROW CAT:Od42effc413ac521cd509 | L2895 | no manual edit
EN: [EEYUCK, WASN'T EXPECTING SOMETHING LIKE THAT HERE...]
BEFORE:   Yiffai: [呕，没料到这儿会有那种东西……]
AFTER:   Yiffai: [呕，没料到这儿会有那种东西……]
ROW CAT:O9fe6271f3979738aa046 | L2896 | no manual edit
EN: [THAT APPEARS TO HAVE BEEN A BLOCKER.]
BEFORE:   Bossu: [那看来是一只Blocker。]
AFTER:   Bossu: [那看来是一只Blocker。]
ROW CAT:O4508271d5397776d9370 | L2897 | no manual edit
EN: [IT'S A STRANGE ANOMALY THAT EMERGES FROM RUINS]
BEFORE:   Bossu: [它是一种会从废墟中现身的奇异异常体，而且看来对大多数物理攻击都免疫。]
AFTER:   Bossu: [它是一种会从废墟中现身的奇异异常体，而且看来对大多数物理攻击都免疫。]
ROW CAT:Oae82d96fb96d9692ad99 | L2898 | no manual edit
EN: [AND SEEMS TO BE IMPERVIOUS TO MOST PHYSICAL ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4c947b6413dbe4e7dd16 | L2899 | EDIT E02-030
EN: ["PHYSICAL" ATTACKS? AS OPPOSED TO...?]
BEFORE:   Yiffai: ["PHYSICAL"攻击？相对于...？]
AFTER:   Yiffai: [“物理”攻击？那相对的是什么攻击……？]
ROW CAT:O082400a1a8bda600d198 | L2900 | no manual edit
EN: [SOME REPORTS FROM PREVIOUS AGENTS MENTIONED THAT]
BEFORE:   Bossu: [之前有些特工的报告提到过，Blocker对“精神”攻击较为脆弱。]
AFTER:   Bossu: [之前有些特工的报告提到过，Blocker对“精神”攻击较为脆弱。]
ROW CAT:O694a0d80ee1352d6e95d | L2901 | no manual edit
EN: [BLOCKERS WERE VUL- NERABLE TO "PSYCHICAL" ATTACKS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9cdef9aa9fb57bc9465f | L2902 | EDIT E02-031
EN: [WE DISMISSED THOSE REPORTS AS UNRELIABLE, BUT...]
BEFORE:   Bossu: [我们当时把这些报告当作不可靠的给驳回了，但是……]
AFTER:   Bossu: [我们当时觉得这些报告不可靠，没有采信，不过……]
ROW CAT:O62d364ed82c4d6573b47 | L2903 | no manual edit
EN: [I'VE NEVER SEEN GLOWING TENTACLES SPROUTING BEFORE]
BEFORE:   Yiffai: [我从没见过会发光的触须冒出来，所以我差不多什么都能信了……]
AFTER:   Yiffai: [我从没见过会发光的触须冒出来，所以我差不多什么都能信了……]
ROW CAT:O75306fec07212a69e000 | L2904 | no manual edit
EN: [SO I'M ALMOST READY TO BELIEVE ANYTHING...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P02-020 | action=apply
原问题：当前PHYSICAL残留英文，使物理／精神对举失效；不是图鉴名强译工单，Blocker暂保留不擅立新译名。
本轮理由：物理/精神对举需可读；报告归属、不可靠的先前判断均保留。只修英文残留问句和生硬驳回，不强改Blocker暂名。
EDIT_IDS ["E02-030", "E02-031"]

## SC7aaea4356d5dbc8a | nsfw | datadm/all.ds | Mauser.Area0_map12_a noselect
CONTROL L1989 <Mauser.Area0_map12_a noselect>
ROW CAT:O0e77964a22124a31503b | L1990 | no manual edit
EN: [HEY HQ! I CAN'T GET UP THE WAY THAT I CAME DOWN!]
BEFORE:   Yiffai: [喂，总部！我顺原路爬不回去了！]
AFTER:   Yiffai: [喂，总部！我顺原路爬不回去了！]
ROW CAT:Oaef836dac703601d3969 | L1991 | no manual edit
EN: [WHAT AM I SUPPOSED TO DO NOW?]
BEFORE:   Yiffai: [我现在该怎么办？]
AFTER:   Yiffai: [我现在该怎么办？]
ROW CAT:O02e4d8ebfbcde4a8661f | L1992 | no manual edit
EN: [DON'T FORGET YOUR TRAINING, AGENT!]
BEFORE:   Mauser: [别忘了你的训练，特工！]
AFTER:   Mauser: [别忘了你的训练，特工！]
ROW CAT:O039bb17bace9399d6dee | L1993 | EDIT E02-032
EN: [TRY TO FIND AN ALTERNATE WAY AROUND THE SITUATION.]
BEFORE:   Mauser: [试着另找一条路绕开这个局面。]
AFTER:   Mauser: [试着另找一条路，绕过去。]
### P02-021 | action=apply
原问题：“另找一条路绕开这个局面”保留英语抽象宾语，面对无法原路返回的问句不自然。重写为具体鼓励，不凭空指定地图路径。
本轮理由：玩家不能原路爬回与总部鼓励已足，只改绕开局面的抽象宾语，不增加具体地图路线。
EDIT_IDS ["E02-032"]

## SC567b9e156beb4379 | nsfw | datadm/all.ds | MauserHints_Area0.Endgame
CONTROL L3486 <MauserHints_Area0.Endgame>
CONTROL L3487   if { f(ClassicPigobinV3_defeated) && f(ClassicEnelye_defeated) } {
CONTROL L3488     if { !f(ClassicStarkillV3_defeated) } {
ROW CAT:O4bb1917176b03c96c3f0 | L3489 | no manual edit
EN: [YOUR NAVMAP SHOULD SHOW WHERE YOUR SISTER IS!]
BEFORE:       Mauser: [你的导航图应该标着你姐姐的位置！]
AFTER:       Mauser: [你的导航图应该标着你姐姐的位置！]
ROW CAT:O201825a8a0a17f3f659f | L3490 | EDIT E02-033
EN: [GO AND SLAP SOME SENSE INTO THEM!]
BEFORE:       Mauser: [去把他们揍醒吧！]
AFTER:       Mauser: [去把她揍醒吧！]
ROW CAT:Ocf0ed5914e20a248647a | L3491 | no manual edit
EN: [...BUT NOT TOO HARD!]
BEFORE:       Mauser: [……不过可别下手太重！]
AFTER:       Mauser: [……不过可别下手太重！]
CONTROL L3492     } else if { !hasItem(CosmoBody) || !hasItem(CosmoHead) } {
ROW CAT:O493c14fdafa36c200802 | L3493 | no manual edit
EN: [ARE YOU REALLY GOING UP TO THE PRISON MOON?]
BEFORE:       Mauser: [你真的要去那座监狱月球吗？]
AFTER:       Mauser: [你真的要去那座监狱月球吗？]
ROW CAT:O8af677897cd0d331b6e2 | L3494 | no manual edit
EN: [YOU'LL WANT TO GET YOUR COSMOSUIT BACK FIRST]
BEFORE:       Mauser: [你最好先把自己的宇宙服找回来]
AFTER:       Mauser: [你最好先把自己的宇宙服找回来]
ROW CAT:O9948c8af8d258c2d5b50 | L3495 | no manual edit
EN: [THOSE DWEEBY SQUEAKERS COULDN'T HAVE TAKEN IT FAR!]
BEFORE:       Mauser: [那些窝囊的吱吱怪不可能把它带远！]
AFTER:       Mauser: [那些窝囊的吱吱怪不可能把它带远！]
CONTROL L3496     } else {
ROW CAT:O1e76c90271a952dcb597 | L3497 | no manual edit
EN: [YOU'VE GOT YOUR COSMOSUIT BACK TOGETHER AGAIN!]
BEFORE:       Mauser: [你的宇宙服又凑齐了！]
AFTER:       Mauser: [你的宇宙服又凑齐了！]
ROW CAT:O8acb8d21dd835b5c8209 | L3498 | no manual edit
EN: [NOTHING'S STOPPING YOU FROM HEADING UP]
BEFORE:       Mauser: [没有什么能拦着你前往那颗名叫“流放地”的监狱卫星！]
AFTER:       Mauser: [没有什么能拦着你前往那颗名叫“流放地”的监狱卫星！]
ROW CAT:Oe2a4f8c91004efcb1f06 | L3499 | no manual edit
EN: [TO THE PRISON MOON NAMED "EXILE"!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L3500     }
CONTROL L3501   }
### P02-022 | action=apply
原问题：本男主分支them回指单一姐姐，不是复数他们。控制条件为未击败StarkillV3，不混同女线弟弟。
本轮理由：该条件块sister为单一姐姐；them单数回指，不能译复数他们。只改代词，前后非空节点保持。
EDIT_IDS ["E02-033"]

## SC374f6d5688afdd2d | sfw | datadm/all.ds | Static.AreaC_map56_override noselect noamendfreq
CONTROL L2411 <Static.AreaC_map56_override noselect noamendfreq>
ROW SFWf9f87bbf8e77ed0f1b466dee | L2412 | no manual edit
EN: [KKZZT! TR... SSSH MIS...ATE...]
BEFORE:   Static: [咔滋滋！特……嘶嘶……失……误……]
AFTER:   Static: [咔滋滋！特……嘶嘶……失……误……]
ROW SFW4cd45f92825f11284d257993 | L2413 | no manual edit
EN: [...KKKKK- ZZT!]
BEFORE:   Static: [...KKKKK- ZZT!]
AFTER:   Static: [...KKKKK- ZZT!]
### P02-032 | action=defer
原问题：原文MIS...ATE为失真残词，当前补成“失……误……”未有完整词证据；其余原样噪音与中文拟声混用。待核原脚本/音效的可辨词策略，不猜成完整指令。
本轮理由：defer：原文TR...MIS...ATE为未知失真残片；文本证明不足以扩成失误或某条完整指令，音效/残词字幕策略未核。本轮不猜补也不擅将现字幕换成另一猜词。
EDIT_IDS []

## SC8a2b8e81ea1e21a5 | nsfw | datadm/all.ds | TomcatItems.StatPretzel
CONTROL L3981 <TomcatItems.StatPretzel>
ROW CAT:O1f5ef1c43f7617f6f4b8 | L3982 | EDIT E02-036
EN: [DON'T GET TWISTED UP IN A KNOT OVER THAT SNACK!]
BEFORE:   Tomcat: [别为那零食把自己扭成一个结！]
AFTER:   Tomcat: [别为这块扭结零食犯愁，把自己也绕进结里啦！]
ROW CAT:O3bbbe08fbce2450dfb33 | L3983 | no manual edit
EN: [WHY THE DWARVES HAVE THEM I DON'T REALLY KNOW...]
BEFORE:   Tomcat: [至于矮人为什么会有这东西，我也不太清楚……]
AFTER:   Tomcat: [至于矮人为什么会有这东西，我也不太清楚……]
ROW CAT:Oa61413c487836575ea55 | L3984 | no manual edit
EN: [BUT MAYBE IT'S THE KEY TO BEING STRONG LIKE THEM!]
BEFORE:   Tomcat: [但也许这就是像他们一样强壮的关键！]
AFTER:   Tomcat: [但也许这就是像他们一样强壮的关键！]
### P02-024 | action=apply
原问题：get twisted up in a knot 为犯愁的习语并双关pretzel形状；当前要求别把自己扭成结过度字面。保留零食形状的笑点，不补效果数值。
本轮理由：knot习语与pretzel形状双关成立，只在第一槽做犯愁/扭结呼应；不知道与maybe已在后续原节点，保持原样不夸效果。
EDIT_IDS ["E02-036"]

## SC5d3909936e0c2b12 | sfw | datadm/all.ds | TomcatItems.TazerTrainee
CONTROL L3990 <TomcatItems.TazerTrainee>
ROW SFW0a9197197558d94e611f8af8 | L3991 | no manual edit
EN: [GOOD JOB GETTING YOUR LIGHTTAZER BACK, KIDDO!]
BEFORE:   Tomcat: [找回光电击枪了，干得好，小家伙！]
AFTER:   Tomcat: [找回光电击枪了，干得好，小家伙！]
ROW SFWb7b656d47148bd74e728d6e9 | L3992 | no manual edit
EN: [HEY COME ON! IT'S BAD ENOUGH WHEN MY SISTER SAYS THAT.]
BEFORE:   Yiffai: [喂，别这样！我姐这么叫就够受的了。]
AFTER:   Yiffai: [喂，别这样！我姐这么叫就够受的了。]
ROW SFWaad32990d09035f0d7a9ccea | L3993 | EDIT E02-034
EN: [HEHE! IT'S JUST FUN TO SEE YOU BLUSH. GOOD LUCK CATCHING]
BEFORE:   Tomcat: [嘿嘿！看你脸红就是好玩。祝你顺利追上]
AFTER:   Tomcat: [嘿嘿！看你脸红就是好玩。]
ROW SFWb684cb41a24a59e1460cade8 | L3994 | EDIT E02-035
EN: [UP WITH THAT MEAN OL' LIZARD!]
BEFORE:   Tomcat: [对付那个凶巴巴的老蜥蜴！]
AFTER:   Tomcat: [祝你顺利追上那只凶巴巴的老蜥蜴！]
### P02-023 | action=apply
原问题：当前连读“祝你顺利追上对付那个…”出现两个互不连接的谓语；不能按单框各自润色。catching up 在本段不额外加“对付”。
本轮理由：两个非空节点分别保留脸红调侃和祝追上蜥蜴；不把catching up增译为对付，不合句消费任何节点。
EDIT_IDS ["E02-034", "E02-035"]

## SC7798569b8a1fbb4a | nsfw | datav/dictionary.json | LuckyBodyNotUpgraded
ROW CAT:O247377a0cecab145b15c | L- | EDIT E02-037
EN: GET A FEELING|SO COMPLICATED
BEFORE: 生出感觉|如此复杂
AFTER: 涌起的感觉|复杂难言
ROW CAT:Oc134cca929a3e327f41d | L- | no manual edit
EN: TINGLE
BEFORE: 酥麻
AFTER: 酥麻
### P02-025 | action=apply
原问题：两行物品短述连读“生出感觉如此复杂”不是自然中文；提案仅写复杂感受，不凭LuckyBody关联补发情或玩法效果。保留UI分隔符。
本轮理由：当前两段短述语序不通；可确认只修复杂感觉的表达，不凭键名补发情或功能。保留竖线及另一个酥麻值，短于草案以适配容器。
EDIT_IDS ["E02-037"]

## SCeed6c44091fb9d0d | sfw | datav/dictionary.json | SpecialTorch
ROW SFW86fe1744044d513f4246dc88 | L- | EDIT E02-045
EN: TORCH
BEFORE: 火把
AFTER: 手电筒
ROW SFWd54f9209d9d986da1818daa2 | L- | no manual edit
EN: LIGHTS UP THE|DARKEST ROOMS.
BEFORE: 照亮|最黑暗的房间。
AFTER: 照亮|最黑暗的房间。
### P02-034 | action=apply
原问题：torch在本作与flashlight为同一道具的英美称法，不是明火火把；当前字典火把与包内多处手电筒提示冲突，误导物品识别。仅本对象建议统一，不把墙上可打碎火把一并替换。
本轮理由：SpecialTorch对应DS明说FLASHLIGHT且3P-X69自动照暗，足以确认此对象不是明火；仅改该UI名，照亮短述保持，不波及墙上火把。
EDIT_IDS ["E02-045"]

## SC205dcd8ee4b31d57 | nsfw | datav/dictionary.json | ui.data.f_ClassicWerehund
ROW CAT:O6b4934990569ea09a790 | L- | EDIT E02-038
EN: WAN GREAT VICTORY|LEADS TO A RUFFER DEFEAT!
BEFORE: 汪的一场大胜|引向更汪的惨败！
AFTER: 汪！一场大胜|换来更惨的败仗！
### P02-026 | action=apply
原问题：wan/one与ruffer/rougher为犬类谐音；现译“汪的一场／更汪的惨败”读不懂且丢掉rougher的程度对比。提案保留一次源内犬音，不变成全作口癖。
本轮理由：WAN/one与RUFFER/rougher为犬音梗，当前汪的一场不成句；保留一次犬音及更惨的比较。保持UI两段，未扩新功能或事件。
EDIT_IDS ["E02-038"]

## SCc035945720439679 | sfw | vsn/f_AgentFZ6/script.vsn | vsn/f_AgentFZ6/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Female
CONTROL L4 rewind!
ROW SFW4621b8f6759b7aa983bea550 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
AFTER: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFWd5fa628625cbee26b45fb10d | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放到我的手上。
AFTER: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFW6800bff60c98235c6699d306 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
AFTER: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L9 cut(0.06): FenfenF01
CONTROL L10 rewind!
ROW SFWde402c03cecbce7a52167a5a | L11 | no manual edit
EN: Having touched the prison of Traeh, the interloper was no longer themself.
BEFORE: lang(Fox): 触碰到特蕾的囚牢之后，那名闯入者便不再是从前的自己。
AFTER: lang(Fox): 触碰到特蕾的囚牢之后，那名闯入者便不再是从前的自己。
ROW SFWa7d298c0e66d3a8290e98c46 | L12 | no manual edit
EN: Enough dark psychic power had passed in that one moment of contact
BEFORE: lang(Fox): 就在接触的那一刻，已有足够多的黑暗灵能传递了过去，
AFTER: lang(Fox): 就在接触的那一刻，已有足够多的黑暗灵能传递了过去，
ROW SFWc5bd3cfbb0ee61843ec4cc4b | L13 | no manual edit
EN: that Traeh had a willing minion to send out into the wild.
BEFORE: lang(Fox): 特蕾也就有了一个甘愿效命的爪牙，可被差往荒野。
AFTER: lang(Fox): 特蕾也就有了一个甘愿效命的爪牙，可被差往荒野。
CONTROL L15 cut(0.06): FenfenF02
CONTROL L16 rewind!
ROW SFW39d5eb9162169d4e317d1d1d | L17 | EDIT E02-039
EN: One by one, this twisted agent rounded up the remaining council members
BEFORE: lang(Fox): 这名被扭曲的代理人，把理事会余下的成员一个一个捉走，
AFTER: lang(Fox): 这名心智被扭曲的特工，将理事会余下的成员逐一抓走，
ROW SFW450211e40433bf2e1895d29f | L18 | no manual edit
EN: ensuring that the powers that kept Traeh imprisoned weakened more each day.
BEFORE: lang(Fox): 以此确保囚禁特蕾的力量一天天地衰弱下去。
AFTER: lang(Fox): 以此确保囚禁特蕾的力量一天天地衰弱下去。
CONTROL L20 cut(0.06): FenfenF03S
CONTROL L21 rewind!
ROW SFW4ff4f709195c19ceb8b344aa | L22 | EDIT E02-040
EN: Even if the wise council members were intent on psychically detaining Traeh
BEFORE: lang(Fox): 即便睿智的议会成员决意以心灵之力拘禁特蕾，
AFTER: lang(Fox): 即便理事会的智者们仍决心以心灵之力囚禁特蕾，
ROW SFWab3d8f0f421b2d4ba9206035 | L23 | EDIT E02-041
EN: after being subjugated to experiment after dark experiment...
BEFORE: lang(Fox): 在接连遭受一场又一场黑暗实验的摆布之后……
AFTER: lang(Fox): 可在被迫接连遭受一场又一场黑暗实验之后……
ROW SFW3dea1217bfd7e870899f242d | L24 | EDIT E02-042
EN: ...not even the wisest of Fenfen minds could wage battles on that many fronts.
BEFORE: lang(Fox): ……即便是Fenfen中最智慧的头脑，也无法在如此众多的战线上同时作战。
AFTER: lang(Fox): ……就连Fenfen中最睿智的人，也无法同时应付这么多方面的压力。
CONTROL L26 cut(0.06): FenfenF04
CONTROL L27 rewind!
ROW SFW112e61664bc516ada92ee1c6 | L28 | no manual edit
EN: Without the powers of the Fenfen council to hold Traeh prisoner
BEFORE: lang(Fox): 一旦没有了Fenfen理事会的力量来囚禁特蕾，
AFTER: lang(Fox): 一旦没有了Fenfen理事会的力量来囚禁特蕾，
ROW SFW8bee223b190af5b928171600 | L29 | no manual edit
EN: it's only a matter of time before she's able to break free and wage war once more.
BEFORE: lang(Fox): 她破囚而出、再度开战，便只是时间问题。
AFTER: lang(Fox): 她破囚而出、再度开战，便只是时间问题。
ROW SFWf8bcea27a992084af2841574 | L30 | no manual edit
EN: And this time, there will be no resistance against her evil power.
BEFORE: lang(Fox): 而到了那时，将再没有任何力量能够抵挡她的邪恶之力。
AFTER: lang(Fox): 而到了那时，将再没有任何力量能够抵挡她的邪恶之力。
CONTROL L32 cut(0.06): FenfenF05
CONTROL L33 rewind!
ROW SFW80474f5a9f1ba049177d2eab | L34 | no manual edit
EN: The only thing that keeps this evil Queen from conquering all of Tutone 
BEFORE: lang(Fox): 唯一让这邪恶女王尚未征服整个图托恩的， 
AFTER: lang(Fox): 唯一让这邪恶女王尚未征服整个图托恩的， 
ROW SFW5c24ea3a393727bf552638e0 | L35 | no manual edit
EN: is her desire to gain enough strength to transfer into a new host body.
BEFORE: lang(Fox): 是她想要积蓄足够的力量，转移到一个新的宿主躯体之中。
AFTER: lang(Fox): 是她想要积蓄足够的力量，转移到一个新的宿主躯体之中。
CONTROL L37 cut(0.06): FenfenF06
CONTROL L38 rewind!
ROW SFWdef347de64c5d5dec7d6446e | L39 | no manual edit
EN: Perhaps, then, it is another twist of Fate that sent you to this planet
BEFORE: lang(Fox): 那么，也许又是命运的一次转折，把你送到了这颗星球，
AFTER: lang(Fox): 那么，也许又是命运的一次转折，把你送到了这颗星球，
ROW SFWce9ed901f92f9afdac5a7c3b | L40 | no manual edit
EN: and had you arrive so near to where all this calamitous action took place.
BEFORE: lang(Fox): 并且让你来到距离这场灾难发生之地如此之近的地方。
AFTER: lang(Fox): 并且让你来到距离这场灾难发生之地如此之近的地方。
CONTROL L42 cut(0.06): Black
CONTROL L43 rewind!
ROW SFW8dda6052e71b1320259671e3 | L44 | no manual edit
EN: Will you be an even more powerful host for Traeh, Queen of Darkness?
BEFORE: lang(Fox): 你会成为黑暗女王特蕾更加强大的宿主吗？
AFTER: lang(Fox): 你会成为黑暗女王特蕾更加强大的宿主吗？
ROW SFW601bbca52a637c4b83462245 | L45 | no manual edit
EN: Or will you be the saviour of the Fenfen, a beacon of courage and hope...?
BEFORE: lang(Fox): 还是说，你会成为Fenfen的救主，一座勇气与希望的灯塔……？
AFTER: lang(Fox): 还是说，你会成为Fenfen的救主，一座勇气与希望的灯塔……？
ROW SFW647b823224b3721bb5b8185f | L46 | no manual edit
EN: ...
BEFORE: lang(Fox): ……
AFTER: lang(Fox): ……
ROW SFW02d197c1d509bb2fe76bd924 | L47 | no manual edit
EN: ...Only you can decide, hero.
BEFORE: lang(Fox): ……只有你能决定，英雄。
AFTER: lang(Fox): ……只有你能决定，英雄。
CONTROL L50 wait: 0.2
CONTROL L51 fadeout(1.0, 1.0, 4)
### P02-027 | action=apply
原问题：同一段council在17、22、28间译成理事会／议会；twisted agent接前文入侵者受控制，机械译“代理人”容易与全作特工脱节。议会为本场暂定统一方向，须术语复审；不把Fox所述升级全知设定。
本轮理由：twisted agent回接被控制的闯入者，按本作现用特工修复代理人；council不终裁议会新名，保留本场多数理事会，P028对应节点局部一致。Fox原前缀保留其讲述归属。
EDIT_IDS ["E02-039", "E02-040"]
### P02-028 | action=apply
原问题：当前“即便…在…之后…”悬置主语，黑暗实验“摆布”也不自然；整体恢复成员维持囚禁却被多重折磨拖垮的逻辑。fronts是比喻，不新增实际多线战役。
本轮理由：按三个有效节点依次承载维持囚禁的意愿、受迫遭受实验、难以多面应付；fronts仍作比喻，不新增战役。council局部沿理事会而不终裁全作术语。
EDIT_IDS ["E02-040", "E02-041", "E02-042"]

## SC6c92dcf306eb4565 | nsfw | vsn/f_ClassicBigboldV2/script.vsn | vsn/f_ClassicBigboldV2/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): ClassicArea01AA
CONTROL L4 rewind!
ROW CAT:O278065456943fef91d30 | L5 | no manual edit
EN: Well now, see what happens when you run away?
BEFORE: text: 瞧吧，现在知道逃跑的下场了？
AFTER: text: 瞧吧，现在知道逃跑的下场了？
ROW CAT:O66dbecd15f5c7e29ece2 | L6 | no manual edit
EN: Didn't mean to bonk you so hard, but were you trying to ruin my reputation
BEFORE: text: 不是故意敲那么重，可我还没好好采集你的数据，你就想跑，是想砸我的招牌吗？
AFTER: text: 不是故意敲那么重，可我还没好好采集你的数据，你就想跑，是想砸我的招牌吗？
ROW CAT:O63863649488c5a53ac7c | L7 | no manual edit
EN: by running away before I could get some proper data on ya?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L9 wait: 0.2
CONTROL L10 fadecut(0.266, 2): ClassicArea001PlusA
CONTROL L11 sfxcue: ClassicArea001PlusA {
CONTROL L12   play [ClassicVisualSlapA] at [14, 69]
CONTROL L13 }
CONTROL L14 rewind!
ROW CAT:Oaceef4097553b99b104b | L15 | no manual edit
EN: I tell ya, I used to spend soooo many hours practicing after class.
BEFORE: text: 跟你说，我以前课后练习一练就是好——几个钟头。
AFTER: text: 跟你说，我以前课后练习一练就是好——几个钟头。
ROW CAT:O2366cfebee7fa8352f1f | L16 | no manual edit
EN: Signing out larger and larger training tools from the academy
BEFORE: text: 从学院领用的训练道具也越来越大，大到连几位教授都怀疑，我是不是练得太急了！
AFTER: text: 从学院领用的训练道具也越来越大，大到连几位教授都怀疑，我是不是练得太急了！
ROW CAT:O8874cf656f739cdad878 | L17 | no manual edit
EN: to the point where even some of my professors wondered if I was rushing too much!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O59ccf375dd0c8b688503 | L18 | no manual edit
EN: In the end, it was all worth it though.
BEFORE: text: 不过到头来，一切都值了。
AFTER: text: 不过到头来，一切都值了。
CONTROL L20 wait: 0.2
CONTROL L21 fadecut(0.266, 2): ClassicArea001PlusF
CONTROL L22 rewind!
ROW CAT:Ob902a1b0b8c5857d72ca | L23 | no manual edit
EN: When I graduated at only 22 years old, with honors, it was big news!
BEFORE: text: 才22岁就以优异成绩毕业，我当时可上了大新闻！
AFTER: text: 才22岁就以优异成绩毕业，我当时可上了大新闻！
ROW CAT:O2fad3f13d7c36ff782aa | L24 | no manual edit
EN: I was the face of the PPPC's recruitment campaign and everything.
BEFORE: text: 我还当过PPPC招募宣传的代言人呢。
AFTER: text: 我还当过PPPC招募宣传的代言人呢。
ROW CAT:Of36ebca2e9a880fcabfb | L25 | no manual edit
EN: Being the youngest agent to ever see active duty was craaaaazy intense.
BEFORE: text: 作为史上最年轻的实战特工，压力简直大到爆。
AFTER: text: 作为史上最年轻的实战特工，压力简直大到爆。
ROW CAT:O356b4b4a9e1d0b9d5fb0 | L26 | no manual edit
EN: ...even if my little brother managed to take that record from me...
BEFORE: text: ……虽然最年轻的纪录后来被我弟弟抢走了……
AFTER: text: ……虽然最年轻的纪录后来被我弟弟抢走了……
CONTROL L28 wait: 0.2
CONTROL L29 fadecut(0.266, 2): ClassicArea02
CONTROL L30 rewind!
ROW CAT:O4967051d5394fd804726 | L31 | no manual edit
EN: But no matter! That doesn't diminish my accomplishments one bit.
BEFORE: text: 不过无所谓！这丝毫不损我的功绩。
AFTER: text: 不过无所谓！这丝毫不损我的功绩。
ROW CAT:Oe979906e5e64a03f3b2f | L32 | no manual edit
EN: And no feisty lizard is gonna diminish my reputation one bit, either!
BEFORE: text: 再凶的蜥蜴，也别想让我的名声受半点损伤！
AFTER: text: 再凶的蜥蜴，也别想让我的名声受半点损伤！
CONTROL L34 wait: 0.2
CONTROL L35 fadecut(0.266, 2): ClassicArea0Jacket
CONTROL L36 sfxcue: ClassicArea0Jacket {
CONTROL L37   play [EnterTransitionRoom] at [2]
CONTROL L38 }
CONTROL L39 rewind!
ROW CAT:O1c45b0a02921ee0f6ffa | L40 | no manual edit
EN: ...Come here boy!
BEFORE: text: ……过来吧，小子！
AFTER: text: ……过来吧，小子！
CONTROL L41 sync!
ROW CAT:Of99170dcaedf3126849f | L42 | no manual edit
EN: Let's get this show on the road!
BEFORE: text: 好戏开场啦！
AFTER: text: 好戏开场啦！
CONTROL L44 wait: 0.2
CONTROL L45 fadecut(0.266, 2): ClassicArea002P
CONTROL L46 sfxcue: ClassicArea002P {
CONTROL L47   play [ClassicYiffaiXTwitch2] at [5]
CONTROL L48 }
CONTROL L49 rewind!
ROW CAT:O3a0e0f4f540a3c87fb48 | L50 | no manual edit
EN: Not sure what it is about you big ol' overgrown lizards
BEFORE: text: 真不懂你们这些长得过头的大蜥蜴是什么体质，可不管打得多凶，你们都不会软，对吧？
AFTER: text: 真不懂你们这些长得过头的大蜥蜴是什么体质，可不管打得多凶，你们都不会软，对吧？
ROW CAT:O7714d249b0990b239ecf | L51 | no manual edit
EN: but no amount of fighting ever makes you get soft, does it?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od2f538a1528a7bca9909 | L52 | no manual edit
EN: I swear! Sometimes it just seems to be like foreplay to you space pirate types!
BEFORE: text: 真受不了！对你们太空海盗来说，打架就像前戏！
AFTER: text: 真受不了！对你们太空海盗来说，打架就像前戏！
CONTROL L54 wait: 0.2
CONTROL L55 fadecut(0.266, 2): ClassicArea10A
CONTROL L56 rewind!
CONTROL L57 sfxcue: ClassicArea10A {
CONTROL L58   play [ClassicYiffaiXSlap5] at [6]
CONTROL L59 }
ROW CAT:Ob6fbbbdfab69209c043b | L60 | no manual edit
EN: Mmmmmf!
BEFORE: text: 嗯——唔！
AFTER: text: 嗯——唔！
ROW CAT:Oc4f9e42ac5d2de1742fc | L61 | no manual edit
EN: At least while you're dazed I can warm myself how I like to...
BEFORE: text: 至少趁你还晕乎乎的，我能按自己喜欢的方式暖和暖和……
AFTER: text: 至少趁你还晕乎乎的，我能按自己喜欢的方式暖和暖和……
ROW CAT:O13eac633da650462e777 | L62 | no manual edit
EN: Just gotta enjoy your tapered little tip for a bit before the REAL show starts.
BEFORE: text: 正式开场前，先享受一下你尖尖的小龟头。
AFTER: text: 正式开场前，先享受一下你尖尖的小龟头。
CONTROL L64 wait: 0.2
CONTROL L65 fadecut(0.266, 2): ClassicArea013A
CONTROL L66 rewind!
CONTROL L67 sfxcue: ClassicArea013A {
CONTROL L68   play [ClassicYiffaiXSlap6] at [5, 13]
CONTROL L69 }
ROW CAT:O8a1be63d4b97444594fb | L70 | no manual edit
EN: Don't get me wrong, I could handle any of you wannabe badboys with noooo problem.
BEFORE: text: 别误会，你们这些装坏小子的家伙，我收拾谁都轻——松。
AFTER: text: 别误会，你们这些装坏小子的家伙，我收拾谁都轻——松。
ROW CAT:O02c71e903853644321eb | L71 | no manual edit
EN: But a girl's gotta have some nice and easy days too, you know?
BEFORE: text: 可姑娘也得过几天轻松日子，你懂吧？
AFTER: text: 可姑娘也得过几天轻松日子，你懂吧？
ROW CAT:O3d31b930d7654c6ad15e | L72 | no manual edit
EN: We can't be all romp and pomp ALL the time!
BEFORE: text: 总不能一天到晚都闹腾着大干一场嘛！
AFTER: text: 总不能一天到晚都闹腾着大干一场嘛！
CONTROL L74 wait: 0.2
CONTROL L75 fadecut(0.266, 2): ClassicArea03A
CONTROL L76 rewind!
CONTROL L77 sfxcue: ClassicArea03A {
CONTROL L78   play [ClassicYiffaiXBlink1] at [0, 5]
CONTROL L79 }
ROW CAT:O2338e96358b569c6c946 | L80 | EDIT E02-043
EN: Ahh there ya are, sleepy head! Finally managed to rouse the rest of you, huh?
BEFORE: text: 啊，醒啦，小懒虫！你总算彻底清醒了？
AFTER: text: 啊，醒啦，小懒虫！这下连你整个人也总算醒过来了，是吧？
ROW CAT:O472effdb44387dbb2253 | L81 | no manual edit
EN: Don't you worry, I'll keep this lighttazer nice and saaafely turned off
BEFORE: text: 别担心，只要你别跑，我会让这把光电击枪安安——全全地关着。说定了？
AFTER: text: 别担心，只要你别跑，我会让这把光电击枪安安——全全地关着。说定了？
ROW CAT:Oebc4da7e91dc56db62be | L82 | no manual edit
EN: so long as you don't run. Deal?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L84 wait: 0.2
CONTROL L85 fadecut(0.266, 2): ClassicArea11A
CONTROL L86 rewind!
CONTROL L87 sfxcue: ClassicArea11A {
CONTROL L88   play [ClassicYiffaiXSlap8] at [3, 10]
CONTROL L89 }
ROW CAT:O9e544041d176db06e40b | L90 | no manual edit
EN: That's what I thought, mmmh hmm!
BEFORE: text: 我就知道，嗯哼！
AFTER: text: 我就知道，嗯哼！
ROW CAT:Oc8bf4e1a965f3b85c737 | L91 | no manual edit
EN: You just... sit back and... mmmh... relax...
BEFORE: text: 你只要……靠着……嗯……放松……
AFTER: text: 你只要……靠着……嗯……放松……
ROW CAT:Oed48afc2883931857258 | L92 | no manual edit
EN: While I show you what a... ahh! Cosmobreeder is all about!
BEFORE: text: 让我来教你……啊！宇宙育种者是干什么的！
AFTER: text: 让我来教你……啊！宇宙育种者是干什么的！
CONTROL L94 wait: 0.2
CONTROL L95 fadecut(0.266, 2): ClassicArea012A
CONTROL L96 rewind!
CONTROL L97 sfxcue: ClassicArea012A {
CONTROL L98   play [ClassicYiffaiXSlap1] at [3]
CONTROL L99 }
ROW CAT:O00132e07d2a0e3077acc | L100 | no manual edit
EN: Don't think I'll ever tire of the.... nnngh... nubs you have...
BEFORE: text: 你那些……嗯啊……小肉突，我怕是永远也玩不腻……
AFTER: text: 你那些……嗯啊……小肉突，我怕是永远也玩不腻……
ROW CAT:O63fdda2c70f08ff2cdf0 | L101 | no manual edit
EN: You darn space pirate lizards get all over the galaxy, but at the same time
BEFORE: text: 你们这些该死的蜥蜴太空海盗，整个银河都钻得遍，你们那该死的鸡巴，也特别会往我里面钻……！
AFTER: text: 你们这些该死的蜥蜴太空海盗，整个银河都钻得遍，你们那该死的鸡巴，也特别会往我里面钻……！
ROW CAT:Oac901b0c505eb941c8b9 | L102 | no manual edit
EN: your gosh darn dicks are so good at getting all inside me, too...!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L104 wait: 0.2
CONTROL L105 fadecut(0.266, 2): ClassicArea016A
CONTROL L106 rewind!
CONTROL L107 sfxcue: ClassicArea016A {
CONTROL L108   play [ClassicYiffaiXSlap7] at [3]
CONTROL L109 }
ROW CAT:Oa45572a7f8d99eb674d2 | L110 | no manual edit
EN: I have half a mind to complain about having to study you guys over and over
BEFORE: text: 老得反复研究你们，我都想抱怨了，不过看在你们鸡巴上那些爽人凸粒的份上，就算啦，嘿嘿……
AFTER: text: 老得反复研究你们，我都想抱怨了，不过看在你们鸡巴上那些爽人凸粒的份上，就算啦，嘿嘿……
ROW CAT:O1cda5d052aa7a0d71d4d | L111 | no manual edit
EN: but with those pleasurenubs built onto your dicks, I'll let it slide, hehe...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O56f4a1c91f633e20f37c | L112 | no manual edit
EN: S...slide... just like that...
BEFORE: text: 滑……滑进去……就这样……
AFTER: text: 滑……滑进去……就这样……
ROW CAT:O2713edbd6a6d00359d1a | L113 | no manual edit
EN: ...ah!
BEFORE: text: ……啊！
AFTER: text: ……啊！
CONTROL L115 wait: 0.2
CONTROL L116 fadecut(0.266, 2): ClassicArea013A
CONTROL L117 rewind!
CONTROL L118 sfxcue: ClassicArea013A {
CONTROL L119   play [ClassicYiffaiXSlap6] at [5, 13]
CONTROL L120 }
ROW CAT:O4a69bee6c48017b8f70a | L121 | no manual edit
EN: It's been a while since I've had one of you kobofolks grabbing onto my hips
BEFORE: text: 我有阵子没被你们科博德搂住胯了，但既然你坚持让我这次掌握主动……
AFTER: text: 我有阵子没被你们科博德搂住胯了，但既然你坚持让我这次掌握主动……
ROW CAT:O76539d4551d3261a5a63 | L122 | no manual edit
EN: but if you insist on letting me take control this time...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L124 sync!
CONTROL L125 queue: ClassicArea013B
CONTROL L126 sfxcue: ClassicArea013B {
CONTROL L127   play [ClassicYiffaiXSlap6] at [5, 13]
CONTROL L128 }
ROW CAT:O7b36b17a1d86b2c31488 | L129 | no manual edit
EN: ...then we're gonna have to ramp things up!
BEFORE: text: ……那咱们可得加把劲了！
AFTER: text: ……那咱们可得加把劲了！
ROW CAT:O93c2b5f3b0bbaf261c4f | L130 | no manual edit
EN: Warm up time is over, ya know!
BEFORE: text: 热身时间结束啦！
AFTER: text: 热身时间结束啦！
CONTROL L132 wait: 0.2
CONTROL L133 fadecut(0.266, 2): ClassicArea03B
CONTROL L134 rewind!
CONTROL L135 sfxcue: ClassicArea03B {
CONTROL L136   play [ClassicYiffaiXSlap6] at [1, 7]
CONTROL L137 }
ROW CAT:Oc2590dda5177ffb4631b | L138 | no manual edit
EN: Hey! Did you even hear me?
BEFORE: text: 喂！你到底听见没有？
AFTER: text: 喂！你到底听见没有？
ROW CAT:O829f97d7ebd10b03076a | L139 | no manual edit
EN: Heh, guess this cosmotalent I have has left you just completely speechless.
BEFORE: text: 嘿，看来我这宇宙级的本事，真让你一句话都说不出了。
AFTER: text: 嘿，看来我这宇宙级的本事，真让你一句话都说不出了。
CONTROL L141 wait: 0.2
CONTROL L142 fadecut(0.266, 2): ClassicArea11B
CONTROL L143 rewind!
CONTROL L144 sfxcue: ClassicArea11B {
CONTROL L145   play [ClassicYiffaiXSlap8] at [3, 10]
CONTROL L146 }
ROW CAT:O0dc5289d6431d48d8e7f | L147 | no manual edit
EN: Dooooon't you worry though, I know exactly what I'm doing here.
BEFORE: text: 别——担心，我很清楚自己在做什么。
AFTER: text: 别——担心，我很清楚自己在做什么。
ROW CAT:Oe0a4cce1aa61f397e351 | L148 | no manual edit
EN: You're in good hands!
BEFORE: text: 交给我这双巧手就放心吧！
AFTER: text: 交给我这双巧手就放心吧！
ROW CAT:O6fec86312c6dbdf7c86d | L149 | no manual edit
EN: ...and mouth!
BEFORE: text: ……还有我的嘴！
AFTER: text: ……还有我的嘴！
ROW CAT:Ofc2c4f5e2aa6645e3203 | L150 | no manual edit
EN: ...and... you get the idea!
BEFORE: text: ……还有……你明白的！
AFTER: text: ……还有……你明白的！
CONTROL L152 wait: 0.2
CONTROL L153 fadecut(0.266, 2): ClassicArea012B
CONTROL L154 rewind!
CONTROL L155 sfxcue: ClassicArea012B {
CONTROL L156   play [ClassicYiffaiXSlap1] at [3]
CONTROL L157 }
ROW CAT:Od812791c64306cd564c7 | L158 | no manual edit
EN: Huff... pant...
BEFORE: text: 呼……哈……
AFTER: text: 呼……哈……
ROW CAT:O6733ba4d4486dca88711 | L159 | no manual edit
EN: Usually I like it when a man grabs me by the hips and helps out
BEFORE: text: 平时我挺喜欢男人抓着我的胯，帮我一把，不过我……呼……要让你见识特工独自上阵的本事。
AFTER: text: 平时我挺喜欢男人抓着我的胯，帮我一把，不过我……呼……要让你见识特工独自上阵的本事。
ROW CAT:O55770235ebfff753908b | L160 | no manual edit
EN: but I'll... hff... let you see what an agent can do on their own.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O12c0156aa0812521b656 | L161 | no manual edit
EN: Just this once, mind you!
BEFORE: text: 记住，就这一次！
AFTER: text: 记住，就这一次！
CONTROL L163 wait: 0.2
CONTROL L164 fadecut(0.266, 2): ClassicArea016B
CONTROL L165 rewind!
CONTROL L166 sfxcue: ClassicArea016B {
CONTROL L167   play [ClassicYiffaiXSlap7] at [3]
CONTROL L168 }
ROW CAT:O411564645c172dbf9850 | L169 | no manual edit
EN: Back in my academy days, I'd be riding up and down on training material
BEFORE: text: 当年在学院，我可是天天骑着比你粗一倍的训练器材上下起伏！
AFTER: text: 当年在学院，我可是天天骑着比你粗一倍的训练器材上下起伏！
ROW CAT:O29a44d9a97b7a525a6e2 | L170 | no manual edit
EN: that was twice as thick as you. Day after day!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9da79abbeed72846791c | L171 | no manual edit
EN: Boys do feel better... nmmm... after a bit of a break, though...
BEFORE: text: 不过，歇一阵再跟男人做……嗯……确实更舒服……
AFTER: text: 不过，歇一阵再跟男人做……嗯……确实更舒服……
CONTROL L173 sync!
CONTROL L174 queue: ClassicArea016C
CONTROL L175 sfxcue: ClassicArea016C {
CONTROL L176   play [ClassicYiffaiXSlap7] at [4]
CONTROL L177 }
ROW CAT:O5d024e7b20ad46a57b77 | L178 | no manual edit
EN: Oh, yeah, there we go...
BEFORE: text: 哦，对，就是这样……
AFTER: text: 哦，对，就是这样……
ROW CAT:Od35d1ca755c8b98fc67c | L179 | no manual edit
EN: I just gotta keep... ahh! Bumping that s-spot until...
BEFORE: text: 我只要继续……啊！顶着那、那里，直到……
AFTER: text: 我只要继续……啊！顶着那、那里，直到……
ROW CAT:Ocdf4c3b5b1bedf45879a | L180 | no manual edit
EN: U-until...
BEFORE: text: 直、直到……
AFTER: text: 直、直到……
CONTROL L182 sync!
CONTROL L183 queue: ClassicArea016CumA
CONTROL L184 sfxcue: ClassicArea016CumA {
CONTROL L185   play [ClassicYiffaiXSlap7] at [3, 8, 13]
CONTROL L186   play [ClassicYiffaiXShoot1] at [18, 26, 36, 42, 48, 54, 60]
CONTROL L187 }
ROW CAT:Oc4b55386955bd5c4faec | L188 | no manual edit
EN: ...!!!
BEFORE: text: ……！！！
AFTER: text: ……！！！
CONTROL L190 sync!
CONTROL L191 queue: ClassicArea016CumB
CONTROL L192 sfxcue: ClassicArea016CumB {
CONTROL L193   play [ClassicYiffaiXShoot1] at [4]
CONTROL L194 }
ROW CAT:Oa92feaf550ac456f083b | L195 | no manual edit
EN: A h h h h...!
BEFORE: text:  啊 啊 啊 啊……！
AFTER: text:  啊 啊 啊 啊……！
ROW CAT:O79a29e4d1c28e31748f1 | L196 | no manual edit
EN: Now thaaaaat's what I like to f-feeeeel...!
BEFORE: text: 这才是我喜、喜欢的感觉……！
AFTER: text: 这才是我喜、喜欢的感觉……！
CONTROL L198 wait: 0.2
CONTROL L199 fadecut(0.266, 2): Black
CONTROL L200 rewind!
ROW CAT:O570a456ee9c58ae339f3 | L201 | no manual edit
EN: ...phew!
BEFORE: text: ……呼！
AFTER: text: ……呼！
CONTROL L203 wait: 0.2
CONTROL L204 fadecut(0.266, 2): ClassicArea17A
CONTROL L205 rewind!
ROW CAT:O09f3e379eaa63c683a8c | L206 | no manual edit
EN: I told ya! There's no running away from me, hehehe!
BEFORE: text: 早说了！你逃不出我的手掌心，嘿嘿嘿！
AFTER: text: 早说了！你逃不出我的手掌心，嘿嘿嘿！
ROW CAT:O7404d7bb3be3adb3633d | L207 | no manual edit
EN: A girl's got a reputation to keep, and not even a nice handsome man like yourself
BEFORE: text: 姑娘我还得维护名声，就算你又帅又讨喜，想搞破坏，也别想全身而退！
AFTER: text: 姑娘我还得维护名声，就算你又帅又讨喜，想搞破坏，也别想全身而退！
ROW CAT:O6f2e1057caec45829882 | L208 | no manual edit
EN: is gonna get away with trying to ruin it!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L210 sync!
CONTROL L211 queue: ClassicArea17B
CONTROL L213 queue: ClassicArea17C
ROW CAT:O2301852f464b3314ffbd | L214 | no manual edit
EN: In fact, maybe I should teach you a lesson...
BEFORE: text: 其实，我也许该给你个教训……
AFTER: text: 其实，我也许该给你个教训……
ROW CAT:Oc7b1463a408aea90af22 | L215 | no manual edit
EN: Show you how much endurance a pro like me...
BEFORE: text: 让你看看，我这样的专业人士，耐力究竟……
AFTER: text: 让你看看，我这样的专业人士，耐力究竟……
ROW CAT:Odcb84291d8e2b5f8039e | L216 | no manual edit
EN: ...really has...
BEFORE: text: ……到底有多少……
AFTER: text: ……到底有多少……
CONTROL L218 sync!
CONTROL L219 queue: ClassicArea001F1
CONTROL L220 rewind!
CONTROL L221 sfxcue: ClassicArea001F1 {
CONTROL L222   play [LeverActivate] at [1]
CONTROL L223 }
CONTROL L224 sync!
CONTROL L225 queue: ClassicArea001F2
ROW CAT:Offf6dc4caec13bca4423 | L226 | no manual edit
EN: W-woah big boy!
BEFORE: text: 哇、哇，大块头！
AFTER: text: 哇、哇，大块头！
ROW CAT:O447e05f5c676773a34ad | L227 | no manual edit
EN: I was just kidding, you don't have to scramble off!
BEFORE: text: 我开玩笑的，你不用慌忙逃走！
AFTER: text: 我开玩笑的，你不用慌忙逃走！
CONTROL L229 wait: 0.2
CONTROL L230 fadecut(0.266, 2): ClassicArea18A
CONTROL L231 rewind!
ROW CAT:Ob5c8d7da3490095699c7 | L232 | no manual edit
EN: Aaaand you definitely didn't have to take the door out on your way, ow!
BEFORE: text: 还有，你走的时候真没必要连门都拆了，哎哟！
AFTER: text: 还有，你走的时候真没必要连门都拆了，哎哟！
ROW CAT:Oddbb94c6cc67d26a86df | L233 | no manual edit
EN: You gotta be careful with those, you know. They're often load bearing!
BEFORE: text: 那些可得当心点，知道吗？经常都是承重的！
AFTER: text: 那些可得当心点，知道吗？经常都是承重的！
ROW CAT:Oa676d833eb0371433eed | L234 | no manual edit
EN: Not even us agents will take out a door frame, because you run the risk of-
BEFORE: text: 连我们特工都不拆门框，因为一不小心就——
AFTER: text: 连我们特工都不拆门框，因为一不小心就——
CONTROL L236 wait: 0.2
CONTROL L237 fadecut(0.266, 2): ClassicArea019A
CONTROL L238 rewind!
CONTROL L239 sfxcue: ClassicArea019A {
CONTROL L240   play [ClassicRockSpawn] at [2, 6]
CONTROL L241 }
ROW CAT:Od94ea7c9b4e5d81e356b | L242 | no manual edit
EN: -having the ceiling collapse on ya! Darn it!
BEFORE: text: ——被塌下来的天花板砸！可恶！
AFTER: text: ——被塌下来的天花板砸！可恶！
ROW CAT:Oca7be4b9f2fc0c599c32 | L243 | no manual edit
EN: Not even gonna let me enjoy my afterglow before I have to rush around, huh?
BEFORE: text: 连事后余韵都不让我享受，就得四处奔忙，是吧？ 
AFTER: text: 连事后余韵都不让我享受，就得四处奔忙，是吧？ 
ROW CAT:O9d7f8f924e140f4961b5 | L244 | no manual edit
EN: Well I was hoping to dig around for more of my gear, but I guess I'll...
BEFORE: text: 本想再翻翻，找些自己的装备，可看来我得……
AFTER: text: 本想再翻翻，找些自己的装备，可看来我得……
CONTROL L246 queue: ClassicArea019B
CONTROL L247 rewind!
CONTROL L248 sfxcue: ClassicArea019B {
CONTROL L249   play [ClassicRockSpawn] at [2, 6]
CONTROL L250 }
ROW CAT:O811683ccd337ea5e1e99 | L251 | no manual edit
EN: ...wait a sec, what's that falling from up there...?
BEFORE: text: ……等下，上头掉下来的是什么……？
AFTER: text: ……等下，上头掉下来的是什么……？
ROW CAT:Oa1e589cffe9a0a4f7a9e | L252 | no manual edit
EN: No way... I can't believe my luck!
BEFORE: text: 不会吧……我的运气也太好了！
AFTER: text: 不会吧……我的运气也太好了！
CONTROL L254 wait: 0.2
CONTROL L255 fadecut(0.266, 2): ClassicArea20A
CONTROL L256 rewind!
ROW CAT:O135bcf4a1161a2fe5c2c | L257 | no manual edit
EN: I was just thinking about how useful a hyper bracer would be right about now!
BEFORE: text: 我刚还在想，这会儿要是有个超能护腕可就太有用了！
AFTER: text: 我刚还在想，这会儿要是有个超能护腕可就太有用了！
ROW CAT:O05783ad14b8cb5858ea8 | L258 | no manual edit
EN: I'll be able to slide my way out of here in no time, heh!
BEFORE: text: 我马上就能一路滑出这地方啦，嘿！
AFTER: text: 我马上就能一路滑出这地方啦，嘿！
CONTROL L260 wait: 0.2
CONTROL L261 fadecut(0.266, 2): Black
ROW CAT:Oe5815496e4fcf32a1070 | L262 | no manual edit
EN: ...just let me grab my jacket again...
BEFORE: text: ……让我先把外套拿回来……
AFTER: text: ……让我先把外套拿回来……
ROW CAT:O439c556c73594ce4cd4f | L263 | no manual edit
EN: ...and away we go!
BEFORE: text: ……出发喽！
AFTER: text: ……出发喽！
CONTROL L265 fadeout(1.0, 1.0, 4)
### P02-030 | action=apply
原问题：前段对方仍昏睡但身体反应活跃；rouse the rest of you 对比身体某部分先兴奋、人现在才醒。当前“彻底清醒”抹平rest of you的局部性笑点。证据为同场50–80及后续回话，不另定旁白说话人。
本轮理由：前段dazed/身体仍活跃，rouse the rest of you是人终于跟着身体一起醒的玩笑；不新增具体动作或将兴奋判断当旁白事实。
EDIT_IDS ["E02-043"]

## SC4eeb4a129d950b80 | nsfw | vsn/f_ClassicEnelye/script.vsn | vsn/f_ClassicEnelye/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): ClassicArea02
CONTROL L4 rewind!
ROW CAT:O27ef07c95061c3fc73b7 | L5 | no manual edit
EN: Hmf, getting a bit tired of this planet, and all you immortal beings on it...
BEFORE: text: 哼，有点受够这颗星球，还有你们这些住在上面的不朽生灵了……
AFTER: text: 哼，有点受够这颗星球，还有你们这些住在上面的不朽生灵了……
ROW CAT:Oc61be941ec8590e278cf | L6 | no manual edit
EN: No matter how many hits you take, you're still fresh as when I walked in here!
BEFORE: text: 不管挨了多少下，你还是跟我刚进来时一样精神！
AFTER: text: 不管挨了多少下，你还是跟我刚进来时一样精神！
ROW CAT:O1307d62adc71a28e315e | L7 | no manual edit
EN: Lemme guess, you're one of those immortal elves?
BEFORE: text: 让我猜猜，你也是那些不朽精灵中的一员？
AFTER: text: 让我猜猜，你也是那些不朽精灵中的一员？
CONTROL L9 fadecut(0.266, 2): Asset09
CONTROL L10 rewind!
ROW CAT:Od2c1712d4532bba3a3e9 | L11 | no manual edit
EN: Correct, young lady. I am Enelye, the Immortal High Lady of the Tutone Elves.
BEFORE: text: 没错，年轻的女士。我是恩内莉，图托恩精灵的不朽至高女领主。
AFTER: text: 没错，年轻的女士。我是恩内莉，图托恩精灵的不朽至高女领主。
ROW CAT:Ob391b6891fa84c69f9a3 | L12 | no manual edit
EN: I must commend your most respectable performance in the art of combat
BEFORE: text: 你在战斗技艺上的表现令人肃然起敬，我必须予以赞扬。即便对我这样年长的人而言，观赏这场表演也十分愉快。
AFTER: text: 你在战斗技艺上的表现令人肃然起敬，我必须予以赞扬。即便对我这样年长的人而言，观赏这场表演也十分愉快。
ROW CAT:O400ed7e966ec9e5f5f27 | L13 | no manual edit
EN: it was a highly enjoyable act to watch, even for one as old as I.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L15 fadecut(0.266, 2): Asset10
CONTROL L16 rewind!
ROW CAT:Od7145b4ad2f5e7b27c59 | L17 | no manual edit
EN: It was so enjoyable, that I believe you are due for a reward.
BEFORE: text: 实在是太令人愉快了，我想你理应得到一份奖励。
AFTER: text: 实在是太令人愉快了，我想你理应得到一份奖励。
ROW CAT:O7da9768d79daf9c2072c | L18 | no manual edit
EN: So please, sit back and relax while I...
BEFORE: text: 所以，请坐好，放松下来，让我……
AFTER: text: 所以，请坐好，放松下来，让我……
ROW CAT:O2b3434a18603f8c0021b | L19 | no manual edit
EN: ...reward... you suitably...
BEFORE: text: ……好好地……奖励你……
AFTER: text: ……好好地……奖励你……
ROW CAT:O2f769fe691064620ef24 | L20 | no manual edit
EN: Woah! W-wait a minute, L-lady Enelye...! I'm here to *save* your-
BEFORE: text: 哇！等、等一下，女、女领主恩内莉……！我是来*拯救*你的——
AFTER: text: 哇！等、等一下，女、女领主恩内莉……！我是来*拯救*你的——
CONTROL L22 cut(0.06): Fwoosh2
CONTROL L23 rewind!
ROW CAT:Od68c3726c31fe5e5fc20 | L24 | no manual edit
EN: Eeeek!
BEFORE: text: 呀啊！
AFTER: text: 呀啊！
ROW CAT:O52d2f84fae38b49dd10c | L25 | no manual edit
EN: ...really!? I can do this myself!
BEFORE: text: ……不是吧！？我自己能来！
AFTER: text: ……不是吧！？我自己能来！
CONTROL L27 fadecut(0.266, 2): Asset11A
ROW CAT:O9b1b758ddebcf41e0c68 | L28 | no manual edit
EN: Wa-hey! Actually, I'm usually not a dress-girl... but this feels really nice!
BEFORE: text: 哇哦！其实我平时不怎么穿裙子……不过这感觉真不错！
AFTER: text: 哇哦！其实我平时不怎么穿裙子……不过这感觉真不错！
ROW CAT:O1034dec3adb82375dc02 | L29 | no manual edit
EN: ...but next time, your highness?
BEFORE: text: ……不过下次，殿下？ 
AFTER: text: ……不过下次，殿下？ 
ROW CAT:O29333bb5bb0e75b0c36f | L30 | no manual edit
EN: I'll dress myself!
BEFORE: text: 我自己穿衣服！
AFTER: text: 我自己穿衣服！
CONTROL L32 fadeout(1.0, 1.0, 4)
### P02-029 | action=defer
原问题：当前对话“恩内莉”与本包字典ClassicEnelye“恩莉耶”不一致。此处只建议以已有字典名为锚整段自然化，不在本轮批准正式译名。
本轮理由：defer：只凭字典恩莉耶与对白恩内莉不一致不足终裁正式译名；用户明确除Tomcat外未终裁名不强定。现译身份和赞赏的核心意思成立，不借整段自然化偷批新名。
EDIT_IDS []

## SC2b98992a00a6ce52 | nsfw | vsn/m_ClassicBigbold/script.vsn | vsn/m_ClassicBigbold/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): ClassicArea001A
CONTROL L4 rewind!
ROW CAT:O1aa238e07f000c950fb4 | L5 | no manual edit
EN: Wow, I wasn't expecting a rowdy fella like you around here!
BEFORE: text: 哇，没想到这里有你这么闹腾的家伙！
AFTER: text: 哇，没想到这里有你这么闹腾的家伙！
ROW CAT:Ob4c716fe96f3360a225d | L6 | no manual edit
EN: Didn't mean to be so rough with you, but you know how it is!
BEFORE: text: 不是故意下手这么重的，可你也懂嘛！
AFTER: text: 不是故意下手这么重的，可你也懂嘛！
CONTROL L8 wait: 0.2
CONTROL L9 cut(0.06): ClassicArea001B
CONTROL L10 rewind!
ROW CAT:O3f6a881cbca7a0dbb1a9 | L11 | no manual edit
EN: Gotta get physical one way or another to calm down a big beast like yourself!
BEFORE: text: 要让你这头大野兽冷静，总得有点肢体接触！
AFTER: text: 要让你这头大野兽冷静，总得有点肢体接触！
ROW CAT:Od02689fbe46f16eb07ba | L12 | no manual edit
EN: On the bright side, looks like some of my gear ended up in here too.
BEFORE: text: 往好处想，我的一些装备好像也落在这儿了。
AFTER: text: 往好处想，我的一些装备好像也落在这儿了。
CONTROL L14 wait: 0.2
CONTROL L15 fadecut(0.266, 2): ClassicArea001C
CONTROL L16 rewind!
ROW CAT:O3507bc012cce3bdf16bb | L17 | no manual edit
EN: And here it is, my trusty sideblade.
BEFORE: text: 找到了，我那可靠的佩刃。 
AFTER: text: 找到了，我那可靠的佩刃。 
ROW CAT:Od90970b90960915a86e0 | L18 | no manual edit
EN: Not a particularly strong Lighttazer, but...
BEFORE: text: 这把光电击枪威力不算大，不过……
AFTER: text: 这把光电击枪威力不算大，不过……
CONTROL L20 sync!
CONTROL L21 wait: 0.2
CONTROL L22 snap: ClassicArea001CToD
CONTROL L23 sfxcue: ClassicArea001CToD {
CONTROL L24   play [ClassicCutsceneTazer] at [11]
CONTROL L25 }
CONTROL L27 queue: ClassicArea001D
ROW CAT:O6867426f1306d8f6be18 | L28 | no manual edit
EN: ...it's definitely a privilege to carry such an elegant weapon as this.
BEFORE: text: ……能带着这么精致的武器，真是荣幸。
AFTER: text: ……能带着这么精致的武器，真是荣幸。
ROW CAT:Ocbe82e039e25ba1ec022 | L29 | no manual edit
EN: It's my duty as a Cosmobreeder to take care of it!
BEFORE: text: 身为宇宙育种者，保养它是我的职责！
AFTER: text: 身为宇宙育种者，保养它是我的职责！
CONTROL L31 wait: 0.2
CONTROL L32 fadecut(0.266, 2): ClassicArea001PlusA
CONTROL L33 rewind!
ROW CAT:O8711c26c30b47d3461b5 | L34 | no manual edit
EN: Ever since I was a pup, I had always wanted to be a Cosmobreeder.
BEFORE: text: 从小狗崽时起，我就一直想当宇宙育种者。
AFTER: text: 从小狗崽时起，我就一直想当宇宙育种者。
ROW CAT:Oe44748857b07d9bcf49b | L35 | no manual edit
EN: ...even if I didn't really know what the "breeding" part meant at the time!
BEFORE: text: ……虽然那时，我还不懂“育种”是什么意思！
AFTER: text: ……虽然那时，我还不懂“育种”是什么意思！
ROW CAT:O278b93e832b369463afa | L36 | no manual edit
EN: All I knew was that a life filled with excitement and adventure
BEFORE: text: 我只知道，充满刺激与冒险的生活就是我生来该过的日子！
AFTER: text: 我只知道，充满刺激与冒险的生活就是我生来该过的日子！
ROW CAT:O19fd0f181d43c952a001 | L37 | no manual edit
EN: is what I was born to do!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L40 wait: 0.2
CONTROL L41 fadecut(0.266, 2): Black
ROW CAT:Oaa587262e6765c1a13c0 | L42 | no manual edit
EN: After working my tail off for all those years, here I am now.
BEFORE: text: 拼死拼活努力了那么多年，如今我总算站到了这里。
AFTER: text: 拼死拼活努力了那么多年，如今我总算站到了这里。
ROW CAT:O944727aa4c6611e47011 | L43 | no manual edit
EN: The 3P's 21 year old prodigy, on my very first mission!
BEFORE: text: 3P 组织二十一岁的天才，第一次出任务！
AFTER: text: 3P 组织二十一岁的天才，第一次出任务！
CONTROL L45 wait: 0.2
CONTROL L46 fadecut(0.266, 2): ClassicArea02
CONTROL L47 rewind!
ROW CAT:Oc5e5dbba55316ceb1142 | L48 | no manual edit
EN: Now it's time to put that training to use!
BEFORE: text: 该让训练成果派上用场了！
AFTER: text: 该让训练成果派上用场了！
ROW CAT:Ob72d4fa9493ea44820aa | L49 | no manual edit
EN: I hope you're as excited as I am, big guy!
BEFORE: text: 大块头，希望你也跟我一样兴奋！
AFTER: text: 大块头，希望你也跟我一样兴奋！
CONTROL L51 wait: 0.2
CONTROL L52 fadecut(0.266, 2): ClassicArea06B
CONTROL L53 sfxcue: ClassicArea06B {
CONTROL L54   play [ClassicYiffaiXTwitch1] at [1, 3, 9, 11]
CONTROL L55 }
CONTROL L56 rewind!
ROW CAT:Odeb79a1c05ee33374a5f | L57 | no manual edit
EN: At least PART of you seems excited, hehe...
BEFORE: text: 至少你身上某个部位挺兴奋嘛，嘿嘿……
AFTER: text: 至少你身上某个部位挺兴奋嘛，嘿嘿……
ROW CAT:O04b5ddf7a95d342237c2 | L58 | no manual edit
EN: Kinda nubbly, but you've got a nice taper too.
BEFORE: text: 有些小凸粒，前端收得也很漂亮。
AFTER: text: 有些小凸粒，前端收得也很漂亮。
ROW CAT:O37ad7302b6da4a25d624 | L59 | no manual edit
EN: Almost like you were designed to be a rookie buster!
BEFORE: text: 简直像专为给菜鸟开苞而生的！
AFTER: text: 简直像专为给菜鸟开苞而生的！
CONTROL L61 wait: 0.2
CONTROL L62 fadecut(0.266, 2): ClassicArea04A
CONTROL L63 sfxcue: ClassicArea04A {
CONTROL L64   play [ClassicYiffaiXSlap1] at [3]
CONTROL L65 }
CONTROL L66 rewind!
ROW CAT:O8ed50808426e40cdd8a4 | L67 | no manual edit
EN: Mmmh, lesh shee...
BEFORE: text: 唔，让偶看看……
AFTER: text: 唔，让偶看看……
ROW CAT:O328df6e811b469a2bdea | L68 | no manual edit
EN: You're kinda thick, but alsho kinda pliable too.
BEFORE: text: 你还挺粗，不过也挺软韧的。
AFTER: text: 你还挺粗，不过也挺软韧的。
ROW CAT:O170ba53233f055ca4b0d | L69 | no manual edit
EN: Remindsh me of the beginner toysh I ushed to ushe...
BEFORE: text: 唔，让我想起以前用的入门玩具了…… 
AFTER: text: 唔，让我想起以前用的入门玩具了…… 
CONTROL L71 wait: 0.2
CONTROL L72 fadecut(0.266, 2): ClassicArea05A
CONTROL L73 sfxcue: ClassicArea05A {
CONTROL L74   play [ClassicYiffaiXSlap2] at [4]
CONTROL L75 }
CONTROL L76 rewind!
ROW CAT:O1d56f8a19a00fd323cd5 | L77 | no manual edit
EN: A little shalty, but not unpleashent at all.
BEFORE: text: 有点咸咸的，不过一点也不难吃。
AFTER: text: 有点咸咸的，不过一点也不难吃。
ROW CAT:Od7182589f4aac90873a4 | L78 | no manual edit
EN: Wash wondering if you were gonna be fishy, but nope!
BEFORE: text: 还以为会有腥味，唔，结果没有嘛！
AFTER: text: 还以为会有腥味，唔，结果没有嘛！
ROW CAT:Ob3675a9e1bdcc60b5b4a | L79 | no manual edit
EN: Got theshe fun little nubsh along the one shide of ya, too.
BEFORE: text: 你这侧还长着一排好、好玩的小凸粒呢。
AFTER: text: 你这侧还长着一排好、好玩的小凸粒呢。
CONTROL L81 wait: 0.2
CONTROL L82 fadecut(0.266, 2): ClassicArea03B
CONTROL L83 sfxcue: ClassicArea03B {
CONTROL L84   play [ClassicYiffaiXSlap6] at [1, 7]
CONTROL L85 }
CONTROL L86 rewind!
ROW CAT:O4c85f3bd8977eca2df2c | L87 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O5a45ebfe17e71be169e6 | L88 | no manual edit
EN: ...I didn't bonk you that hard, did I?
BEFORE: text: ……我没把你打得那么狠吧？
AFTER: text: ……我没把你打得那么狠吧？
ROW CAT:Oebd27e9320d34d05c75a | L89 | no manual edit
EN: How are you shtill ashleep while I do thish???
BEFORE: text: 我都介样弄你了，你肿么还睡得着啊？？？
AFTER: text: 我都介样弄你了，你肿么还睡得着啊？？？
CONTROL L91 wait: 0.2
CONTROL L92 fadecut(0.266, 2): ClassicArea08A
CONTROL L93 sfxcue: ClassicArea08A {
CONTROL L94   play [ClassicYiffaiXSlap4] at [3]
CONTROL L95 }
CONTROL L96 rewind!
ROW CAT:O1c357de59862c5d5af6a | L97 | no manual edit
EN: Oh well, at leasht I get to get familiar with your bitsh while you shnooze
BEFORE: text: 算啦，趁你打盹，至少我能熟悉熟悉你的宝贝，反正你那些要紧的部位，还活蹦乱跳着呢！
AFTER: text: 算啦，趁你打盹，至少我能熟悉熟悉你的宝贝，反正你那些要紧的部位，还活蹦乱跳着呢！
ROW CAT:Ob8426b5a4c228109caf4 | L98 | no manual edit
EN: shince all your important partsh are nice and active still!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L100 wait: 0.2
CONTROL L101 fadecut(0.266, 2): ClassicArea04A2
CONTROL L102 sfxcue: ClassicArea04A2 {
CONTROL L103   play [ClassicYiffaiXSlap1] at [3]
CONTROL L104 }
CONTROL L105 rewind!
ROW CAT:O32bbdc94c3437d58bdfd | L106 | no manual edit
EN: If I didn't know better, I'd shay they were even enjoying thish all...
BEFORE: text: 要不是知道内情，我都要说它们挺享受了……
AFTER: text: 要不是知道内情，我都要说它们挺享受了……
ROW CAT:O931f104c43401d9e4588 | L107 | no manual edit
EN: ...your nubsh are getting shlightly harder, even if your shaft ishn't...
BEFORE: text: ……唔，肉棒没变硬，你的凸粒倒是硬了点……
AFTER: text: ……唔，肉棒没变硬，你的凸粒倒是硬了点……
CONTROL L108 sync!
CONTROL L109 queue: ClassicArea04B
CONTROL L110 sfxcue: ClassicArea04B {
CONTROL L111   play [ClassicYiffaiXSlap8] at [4]
CONTROL L112 }
ROW CAT:Oe874abf726b381206f39 | L113 | no manual edit
EN: ...it makesh me want to shuck on it more!
BEFORE: text: ……害得我更想继续吸吮它！
AFTER: text: ……害得我更想继续吸吮它！
ROW CAT:O3833091807537ad11fcf | L114 | no manual edit
EN: Mmmh, WAY better than jusht ushing a toy.
BEFORE: text: 嗯唔，比只用玩具舒服多啦。
AFTER: text: 嗯唔，比只用玩具舒服多啦。
CONTROL L116 wait: 0.2
CONTROL L117 fadecut(0.266, 2): ClassicArea05B
CONTROL L118 sfxcue: ClassicArea05B {
CONTROL L119   play [ClassicYiffaiXSlap2] at [3]
CONTROL L120 }
CONTROL L121 rewind!
ROW CAT:O6b0c03ff2b3aafe54151 | L122 | no manual edit
EN: I hope all you fellash on thish planet are thish good to play with.
BEFORE: text: 但愿你们这星球上的伙计，都这么好玩。
AFTER: text: 但愿你们这星球上的伙计，都这么好玩。
ROW CAT:O796e7031b77ebfd43322 | L123 | no manual edit
EN: I would've been fighting to get shent on a misshion shooner if I only knew
BEFORE: text: 要是早知道真家伙居然能舒服成这样，我早就争着早点出任、任务了！
AFTER: text: 要是早知道真家伙居然能舒服成这样，我早就争着早点出任、任务了！
ROW CAT:O6e050629825e06f513c4 | L124 | no manual edit
EN: that the real thingsh were thish much fun!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L126 wait: 0.2
CONTROL L127 fadecut(0.266, 2): ClassicArea03C
CONTROL L128 sfxcue: ClassicArea03C {
CONTROL L129   play [ClassicYiffaiXSlap6] at [1, 3]
CONTROL L130 }
CONTROL L131 rewind!
ROW CAT:Ode732c0cfabc69737c54 | L132 | no manual edit
EN: Heh, sheems like you're having fun too.
BEFORE: text: 嘿，看样子你也挺享受嘛。
AFTER: text: 嘿，看样子你也挺享受嘛。
ROW CAT:O762877530b8f040a06da | L133 | no manual edit
EN: Dreaming of shome of the other agentsh that came down here before me, maybe?
BEFORE: text: 你该不会梦到比我先来的其他特工了吧？
AFTER: text: 你该不会梦到比我先来的其他特工了吧？
ROW CAT:O7b7b722981893bf095a9 | L134 | no manual edit
EN: Or maybe I'm alsho doing thingsh to you in your dreamsh!
BEFORE: text: 说不定你梦里也是我在玩弄你呢！ 
AFTER: text: 说不定你梦里也是我在玩弄你呢！ 
ROW CAT:O94bba31b08cb62ce0e17 | L135 | no manual edit
EN: Wouldn't shurprishe me, you sheemed dishtracted by my assh in the fight.
BEFORE: text: 也不奇怪啦，打架时你好像就光顾着看我屁、屁股了。
AFTER: text: 也不奇怪啦，打架时你好像就光顾着看我屁、屁股了。
CONTROL L137 wait: 0.2
CONTROL L138 fadecut(0.266, 2): ClassicArea08B
CONTROL L139 sfxcue: ClassicArea08B {
CONTROL L140   play [ClassicYiffaiXSlap4] at [2]
CONTROL L141 }
CONTROL L142 rewind!
ROW CAT:Oc1af2a2dd536862d7e94 | L143 | EDIT E02-044
EN: Don't shyou worry though, I'll be shure to give you a tashte of tail too.
BEFORE: text: 不过别担心，我肯定也会让你尝尝我的尾巴。
AFTER: text: 不过别担心，我也一定会让你尝尝我屁股的滋味。
ROW CAT:O97dba56f23f6ad9de004 | L144 | no manual edit
EN: Just ash shoon ash I'm done tashting YOU!
BEFORE: text: 等我尝够了你的滋味就来！
AFTER: text: 等我尝够了你的滋味就来！
CONTROL L146 rewind!
CONTROL L147 sync!
CONTROL L148 queue: ClassicArea08B2
CONTROL L149 sfxcue: ClassicArea08B2 {
CONTROL L150   play [ClassicYiffaiXSlap5] at [1]
CONTROL L151 }
ROW CAT:O7d94068e2d7e74da19da | L152 | no manual edit
EN: Ahh, I can feel you throbbing more. Are you about to...
BEFORE: text: 啊，我感觉你跳得更厉害了。你是不是快要……
AFTER: text: 啊，我感觉你跳得更厉害了。你是不是快要……
ROW CAT:Oe71540d8518e56ffae83 | L153 | no manual edit
EN: ...!
BEFORE: text: ……！
AFTER: text: ……！
CONTROL L155 sync!
CONTROL L156 queue: ClassicArea08B2ToC
CONTROL L157 sfxcue: ClassicArea08B2ToC {
CONTROL L158   play [ClassicYiffaiXShoot2] at [3, 11, 16, 21, 24, 27, 29, 31]
CONTROL L159 }
CONTROL L161 sync!
CONTROL L162 queue: ClassicArea08C
ROW CAT:O5fca6877e2bc90972d42 | L163 | no manual edit
EN: ...mmmmmh <3!
BEFORE: text: ……嗯唔 <3！
AFTER: text: ……嗯唔 <3！
CONTROL L165 wait: 0.2
CONTROL L166 fadecut(0.266, 2): ClassicArea05C
CONTROL L167 sfxcue: ClassicArea05C {
CONTROL L168   play [ClassicYiffaiXShoot1] at [1, 6]
CONTROL L169 }
CONTROL L170 rewind!
ROW CAT:O0366923d8927f8b848d4 | L171 | no manual edit
EN: Holy gosh!
BEFORE: text: 我的天哪！
AFTER: text: 我的天哪！
ROW CAT:O2074d1706d5e4b9b239c | L172 | no manual edit
EN: How can you shquirt sho much?
BEFORE: text: 你怎么能射这么多呀？
AFTER: text: 你怎么能射这么多呀？
ROW CAT:O3dc605b0821d1e5790ae | L173 | no manual edit
EN: Almosht like itsh never ending, wow...!
BEFORE: text: 简直好像射不完一样，哇……！
AFTER: text: 简直好像射不完一样，哇……！
CONTROL L175 sync!
CONTROL L176 queue: ClassicArea05CToD
CONTROL L177 sfxcue: ClassicArea05CToD {
CONTROL L178   play [ClassicYiffaiXShoot1] at [2]
CONTROL L179   play [ClassicYiffaiXShoot2] at [7]
CONTROL L180 }
CONTROL L182 sync!
CONTROL L183 queue: ClassicArea05D
CONTROL L184 rewind!
ROW CAT:O9ba16acdb8eb2dcd0274 | L185 | no manual edit
EN: Hah.... Hah...
BEFORE: text: 哈……哈……
AFTER: text: 哈……哈……
ROW CAT:Oe778cba3d4af7a14ff1d | L186 | no manual edit
EN: That was... a lot!
BEFORE: text: 刚才可真……够多的！
AFTER: text: 刚才可真……够多的！
CONTROL L188 wait: 0.2
CONTROL L189 fadecut(0.266, 2): ClassicArea06A
CONTROL L190 sfxcue: ClassicArea06A {
CONTROL L191   play [ClassicYiffaiXTwitch2] at [1, 3, 9, 11, 16, 18, 23, 25]
CONTROL L192 }
CONTROL L193 rewind!
ROW CAT:O9f717f6e14b1a82c5733 | L194 | no manual edit
EN: Even after all that, you're still rearing to go?
BEFORE: text: 都这样了，你还想再来？
AFTER: text: 都这样了，你还想再来？
ROW CAT:O65753134cf4fa5e62253 | L195 | no manual edit
EN: Must be because of how good I am! I'm not just an ANAL prodigy, you know!
BEFORE: text: 肯定是我技术太好！我可不只是肛交天才！
AFTER: text: 肯定是我技术太好！我可不只是肛交天才！
ROW CAT:O3ceab6f33cf0b6f3af04 | L196 | no manual edit
EN: Just makes you want to keep going forever, amirite?
BEFORE: text: 爽得让你想一直干下去，对吧？
AFTER: text: 爽得让你想一直干下去，对吧？
CONTROL L198 wait: 0.2
CONTROL L199 fadecut(0.266, 2): ClassicArea03A
CONTROL L200 sfxcue: ClassicArea03A {
CONTROL L201   play [ClassicYiffaiXBlink1] at [0, 5]
CONTROL L202 }
CONTROL L203 rewind!
ROW CAT:O3049b54282026314f729 | L204 | no manual edit
EN: Oh look at that!
BEFORE: text: 哟，瞧瞧！
AFTER: text: 哟，瞧瞧！
ROW CAT:O2264c512ab8683da097f | L205 | no manual edit
EN: Sleepy head has finally woken up after some sleepy head!
BEFORE: text: 享受过睡梦中的口交，瞌睡鬼终于醒啦！
AFTER: text: 享受过睡梦中的口交，瞌睡鬼终于醒啦！
ROW CAT:O9c4f2131c6220591a25d | L206 | no manual edit
EN: You ready to grab me by the hips and make me your bi-
BEFORE: text: 准备好抓着我的胯，把我干成你的小母——
AFTER: text: 准备好抓着我的胯，把我干成你的小母——
CONTROL L208 wait: 0.2
CONTROL L209 cut(0.06): ClassicArea001F1
CONTROL L210 rewind!
CONTROL L211 sfxcue: ClassicArea001F1 {
CONTROL L212   play [LeverActivate] at [1]
CONTROL L213 }
CONTROL L214 sync!
CONTROL L215 queue: ClassicArea001F2
ROW CAT:Oaba588760bd819883a48 | L216 | no manual edit
EN: What the heck!!
BEFORE: text: 什么鬼！！
AFTER: text: 什么鬼！！
CONTROL L218 wait: 0.2
CONTROL L219 fadecut(0.266, 2): ClassicArea001G
CONTROL L220 rewind!
ROW CAT:Oe74844ebdf33b8ca4e47 | L221 | no manual edit
EN: Where are you going???
BEFORE: text: 你上哪儿去？？？
AFTER: text: 你上哪儿去？？？
ROW CAT:O39a49e6a2dac3fb4a6ec | L222 | no manual edit
EN: I'm not gonna hurt ya, that was just the warm-up! Come back here!!
BEFORE: text: 又不会弄伤你，那才只是热身！给我回来！！
AFTER: text: 又不会弄伤你，那才只是热身！给我回来！！
ROW CAT:Ob991ada4c7ad025c6910 | L223 | no manual edit
EN: I still need to properly gather data before... oh darn it!
BEFORE: text: 我还得先好好收集数据才……哎，真是的！
AFTER: text: 我还得先好好收集数据才……哎，真是的！
CONTROL L225 fadeout(1.0, 1.0, 4)
### P02-031 | action=apply
原问题：taste of tail 是性语境屁股／身体的隐语，前文明确提到ass、后文grab hips；当前“尝尝我的尾巴”易理解成啃尾巴，不能承接先口交再换体位的期待。不新增已发生动作。
本轮理由：承接前文ass、后文抓胯，tail在此是身体/屁股的性隐语，不是啃尾巴。只改第一槽，第二槽已保留先尝够你的时序；不写换位已发生。
EDIT_IDS ["E02-044"]

