# packet-03 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SCbbb5b122ac5f7040 | sfw | datadf/all.ds | Area0_Macsen2.DoggyHead
CONTROL L125 <Area0_Macsen2.DoggyHead>
ROW SFWa906efaa019799430e462c20 | L126 | EDIT E03-001
EN: A garment that I don't wear much anymore. It'd 
BEFORE:   * 一件我已经不怎么穿的衣服。它大概会刚——刚好合身！ 
AFTER:   * 一件我现在不怎么穿的衣服。你穿上大概正——合适！
ROW SFW00a123b54034a750d1c3d8d5 | L127 | no manual edit
EN: probably fit you juuuuust fine!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P03-001 | action=apply
原问题：juuuuust是拉长强调，不是“刚——刚好”的口吃；保留商人含笑推销。
本轮理由：拉长强调不是口吃；保留probably的不确定，不采草案的肯定。
EDIT_IDS ["E03-001"]

## SCbfac1cd7cb210faa | nsfw | datadf/all.ds | AreaA_Prison2.CancelPurchase
CONTROL L616 <AreaA_Prison2.CancelPurchase>
ROW CAT:Oe85a830cf5ef188113db | L617 | EDIT E03-002
EN: Are you gonna help me get off, or just stand there lookin'?
BEFORE:   * 你是要帮我出来，还是就站在那儿看着？
AFTER:   * 你是来帮我爽一把，还是就站在那儿看着？
### P03-002 | action=apply
原问题：NSFW的get off在索求性满足，不是帮忙离开牢房；本包同角色GoodbyeNotRescued提到给矿工解乏，不能套SFW救援语义。
本轮理由：本NSFW取消交易话语中的get off为性满足，非离开牢房；不移入SFW。
EDIT_IDS ["E03-002"]

## SCde7a7e36a57b61d6 | nsfw | datadf/all.ds | AreaH_MacsenBar.Talk.zener1
CONTROL L1640 <AreaH_MacsenBar.Talk.zener1>
ROW CAT:Oae1f2ace4da36045c5e8 | L1641 | no manual edit
EN: You ever hear about these ol' PSY powers that some folks be gettin' these days?
BEFORE:   * 你听说过近来有些人搞到的那些念力吗？
AFTER:   * 你听说过近来有些人搞到的那些念力吗？
ROW CAT:Obdbe34a033b17139d972 | L1642 | EDIT E03-003
EN: The say Triangle powers will boost your defense while lowering your attack a bit
BEFORE:   * 听说三角能力能增强防御，不过攻击会稍微降低，而十字之力刚好相反！挨伤更多、伤人更多！
AFTER:   * 听说三角能力能增强防御，不过攻击会稍微降低；十字能力则正好相反！挨打更疼，打人也更疼！
ROW CAT:Od20f2307e5aebf3c4cf6 | L1643 | no manual edit
EN: while a Cross power will do the opposite! Take AND deal more damage!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O332ddebd08ff48ae4de8 | L1644 | no manual edit
EN: Not only that, but they say... they say...
BEFORE:   * 不止如此，他们说……他们说……
AFTER:   * 不止如此，他们说……他们说……
ROW CAT:O49c30c6803d66da3a4ac | L1645 | no manual edit
EN: ...nevermind, I forgot what they say about the other powers...
BEFORE:   * ……算了，其他能力的传闻我给忘了……
AFTER:   * ……算了，其他能力的传闻我给忘了……
### P03-003 | action=apply
原问题：合句无漏译，但“挨伤更多、伤人更多”不自然；完整保留攻防反向和伤害增减。
本轮理由：攻防反向成立，改自然伤害表达，保留传闻与稍微。
EDIT_IDS ["E03-003"]

## SCc948bf3eea745d6b | nsfw | datadf/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1708 <AreaH_MacsenBreeding.SpecialFap>
ROW CAT:Ob2e7374a4e7d4ffa2477 | L1709 | EDIT E03-004
EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
BEFORE:   * 既然你已经和那些生物中的一个变得非常亲近了，把这个拿去！
AFTER:   * 既然你已经跟其中一只生物很亲近了，这个拿去！
ROW CAT:O8c8eb7a9f3a40f14e988 | L1710 | EDIT E03-005
EN: GET REAL CLOSE AND AFFECTIONATE TO THEM ONE MORE TIME WHILE HOLDING THIS
BEFORE:   * 拿着这个，再跟他们亲近一回，你也许会感到某种力量流经全身……
AFTER:   * 拿着这个，再跟它们好好亲近一回，说不定就能感到一股力量流遍全身……
ROW CAT:Ocd3254ce5b97ddbc7f05 | L1711 | no manual edit
EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P03-004 | action=apply
原问题：原文借亲近委婉表达互动与道具条件；“变得非常亲近”生硬，“他们”对象漂移。建议仍不补具体互动动作。
本轮理由：不用亲热强定具体行为；保留持有道具、再次亲近及might，不给them增加单体限制。
EDIT_IDS ["E03-004", "E03-005"]

## SC70bc836984031e04 | nsfw | datadf/all.ds | Bossu.AreaE_map26 noselect
CONTROL L2569 <Bossu.AreaE_map26 noselect>
ROW CAT:Ocf51a77d625e3b00b68b | L2570 | no manual edit
EN: [BE CAREFUL, AGENT.]
BEFORE:   Bossu: [小心，特工。]
AFTER:   Bossu: [小心，特工。]
ROW CAT:O8ed5328423c2d0e56b38 | L2571 | EDIT E03-006
EN: [YOU'RE NEARING THE CHAMBER WHERE YOUR SIBLING]
BEFORE:   Bossu: [你快要接近你的手足被黑暗能量吞噬的那间房间了。]
AFTER:   Bossu: [你快到你弟弟被黑暗能量控制的那间房间了。]
ROW CAT:O685f0af1fde7953d8270 | L2572 | no manual edit
EN: [WAS OVERTAKEN BY DARK ENERGY.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O40daf99e52e675738220 | L2573 | no manual edit
EN: [YOU'D BE BEST BE PREPARED FOR THE WORST IF YOU GO ON.]
BEFORE:   Bossu: [如果你继续前进，最好做好最坏的打算。]
AFTER:   Bossu: [如果你继续前进，最好做好最坏的打算。]
ROW CAT:Oe3ac51c65da84394fb44 | L2574 | no manual edit
EN: [UNDERSTOOD.]
BEFORE:   Yiffany: [明白。]
AFTER:   Yiffany: [明白。]
### P03-005 | action=apply
原问题：女线已确认kid brother；“你的手足”是明显翻译腔。overtaken不是肢体被吞食；保留危险预警。
本轮理由：女线已确认弟弟；overtaken为受控制，非肉体吞食。其余警告与特工称呼原样保留。
EDIT_IDS ["E03-006"]

## SC09b1c6371a1b7cec | sfw | datadf/all.ds | Bossu.CapturedPet
CONTROL L2707 <Bossu.CapturedPet>
ROW SFWbb3ee866274b489095adf0aa | L2708 | EDIT E03-007
EN: [GOOD JOB CAPTURING SOME OF THE LOCAL FAUNA, YIFFANY!]
BEFORE:   Bossu: [本地动物群抓得不错，伊法妮！]
AFTER:   Bossu: [抓到一些当地生物了，干得好，伊法妮！]
ROW SFWebc2b231bee88d21a5d0c117 | L2709 | no manual edit
EN: [PREVIOUS AGENTS REPORTED SETTING UP OBSERVATION UNITS]
BEFORE:   Bossu: [之前的特工报告说，就在为你保养飞船的机库区域架设了观测单元。]
AFTER:   Bossu: [之前的特工报告说，就在为你保养飞船的机库区域架设了观测单元。]
ROW SFWd8b2bd2542dfd0f1eb58d08c | L2710 | no manual edit
EN: [IN THE HANGAR AREA WHERE YOUR SHIP IS SERVICED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWfff1adf8ededc71c05cb60d3 | L2711 | no manual edit
EN: [NOW THAT YOU MADE A FRIEND, YOU SHOULD STOP BY THERE!]
BEFORE:   Tomcat: [既然你交上了朋友，就该去那边转转！]
AFTER:   Tomcat: [既然你交上了朋友，就该去那边转转！]
ROW SFW1203289ce50d3a3699df530d | L2712 | EDIT E03-008
EN: [YEAH, THE FRIEND- LIER YOU GET WITH THE LOCAL FAUNA]
BEFORE:   Mauser: [是啊，你跟本地动物群越处越熟]
AFTER:   Mauser: [是啊，你跟这些当地生物越亲近，]
ROW SFW5e6917eb4d4ddaeeef10e3c5 | L2713 | EDIT E03-009
EN: [THE MORE THEIR CONFIDENCE WILL BE BOOSTED!]
BEFORE:   Mauser: [它们的自信就会提升得越多！]
AFTER:   Mauser: [它们就会越有自信！]
ROW SFW4ceaf870903393ed36ca840e | L2714 | no manual edit
EN: [MAYBE YOU'LL EVEN GET A REWARD AS THANKS...]
BEFORE:   Mauser: [说不定还会送你礼物表示感谢……]
AFTER:   Mauser: [说不定还会送你礼物表示感谢……]
ROW SFWbb9666ea8888eac578c9a11b | L2715 | no manual edit
EN: [DON'T WORRY GUYS, I KNOW HOW THIS WORKS.]
BEFORE:   Yiffany: [别担心，伙计们，这套我熟。]
AFTER:   Yiffany: [别担心，伙计们，这套我熟。]
### P03-006 | action=apply
原问题：local fauna指本地生物的集合，不是把“动物群”当捕捉对象；表扬应先落在行动上。
本轮理由：fauna为集合名，不是整群捕捉；保留表扬。
EDIT_IDS ["E03-007"]
### P03-007 | action=apply
原问题：原句跨两框为一个比较结构；“本地动物群越处越熟”不合口语搭配。
本轮理由：两个原有非空槽分别放比较前后项，不新增合句。
EDIT_IDS ["E03-008", "E03-009"]

## SC1a561dc84c24895f | sfw | datadf/all.ds | BossuDex.ClassicElf
CONTROL L3148 <BossuDex.ClassicElf>
ROW SFW3c55b548e14bb21d02c561d4 | L3149 | EDIT E03-010
EN: [THE ELVES OF SCEAFYA MAY ALL BE FEMALE]
BEFORE:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
AFTER:   Bossu: [斯凯菲亚的精灵虽然全是雌性，却并非个个都能长生不老。]
ROW SFW69ef86cce571a86bfd0959b0 | L3150 | no manual edit
EN: [BUT THEY AREN'T ALL IMMORTAL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWb8771a345322ed5bc49b341a | L3151 | EDIT E03-011
EN: [THEY'VE TAKEN ON MORE AND MORE MORTAL CHARACTERISTICS]
BEFORE:   Bossu: [她们便带上了越来越多的有朽特征]
AFTER:   Bossu: [数百年的岁月过去，]
ROW SFWca14c62fec3031a7c70c3e74 | L3152 | EDIT E03-012
EN: [AS THE CENTURIES HAVE GONE BY.]
BEFORE:   Bossu: [在数百年的岁月流逝之中。]
AFTER:   Bossu: [她们身上凡人的特征也越来越多了。]
ROW SFW0408ee9a2cc8f20a1d08b40a | L3153 | EDIT E03-013
EN: [WAIT, SO THAT MEANS SOME OF THEM *ARE* IMMORTAL?]
BEFORE:   Yiffany: [等等，所以这意味着她们中有些*是*不朽的？]
AFTER:   Yiffany: [等等，那就是说，她们之中有些*真能*长生不老？]
ROW SFWf5b8edbac076f8fa7bbf8a2d | L3154 | EDIT E03-014
EN: [INDEED, AS FAR AS WE CAN TELL.]
BEFORE:   Bossu: [的确，就我们所能看出的而言。]
AFTER:   Bossu: [没错，至少目前掌握的情况是这样。]
ROW SFW6728b569e0f4958a7c606016 | L3155 | EDIT E03-015
EN: [ANY ELF THAT IS OUT IN THE OPEN AND ENGAGING IN COMBAT]
BEFORE:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
AFTER:   Bossu: [在外活动、参与战斗的精灵，无疑都还年轻。最多也就一百岁。]
ROW SFW4fef1339a0c59b056786cf36 | L3156 | no manual edit
EN: [WILL NO DOUBT BE A YOUNGSTER. A HUNDRED YEARS OLD AT MOST.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW69c1a94b77da3b7687d873c0 | L3157 | no manual edit
EN: [THAT'S... WOW...]
BEFORE:   Yiffany: [这……哇……]
AFTER:   Yiffany: [这……哇……]
ROW SFW09e63c38e1bfd45e1df7ffca | L3158 | EDIT E03-016
EN: [DON'T GIVE IN TO AWE. YOU'LL NEED TO BE ON YOUR TOES]
BEFORE:   Bossu: [别向敬畏屈服。你得保持警觉，以便击退那些年幼精灵的攻击。]
AFTER:   Bossu: [先别顾着惊叹。你得保持警惕，才能击退那些年轻精灵的攻击。]
ROW SFWa6bef8f2989c3eb95191f76e | L3159 | no manual edit
EN: [IN ORDER TO REPEL THE YOUNG ELVES' ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWe696a3c61749275e7014e96e | L3160 | EDIT E03-017
EN: [RIGHT, GOTTA FOCUS.]
BEFORE:   Yiffany: [对，得专注。]
AFTER:   Yiffany: [对，得集中精神。]
### P03-008 | action=apply
原问题：may...but在此为让步：承认全雌性再否定全不朽，不是推测雌性；后两框倒置碎裂，“有朽特征”生硬。
本轮理由：may为让步非推测；时间与变化意群分配既有两槽，无条件边界跨移。
EDIT_IDS ["E03-010", "E03-011", "E03-012"]
### P03-009 | action=apply
原问题：保留主角惊讶—总部有限度确认—百岁仍年轻的笑点。“就我们所能看出的而言”不是自然通讯表达。
本轮理由：保留惊讶强调、知识限定和百岁仍年轻；不添年龄事实。
EDIT_IDS ["E03-013", "E03-014", "E03-015"]
### P03-010 | action=apply
原问题：give in to awe指别惊叹得分神，不是“向敬畏屈服”；on your toes保持警觉。
本轮理由：恢复awe分神及on your toes警惕的功能。
EDIT_IDS ["E03-016", "E03-017"]

## SCf83fdc75783e5548 | nsfw | datadf/all.ds | DefeatHints.ClassicStarkillV3.stub
CONTROL L4783 <DefeatHints.ClassicStarkillV3.stub>
ROW CAT:Odec046d2ef67b410906a | L4784 | no manual edit
EN: COME ON! YOU CAN DO IT!
BEFORE:   Mauser: 上啊！你能做到的！
AFTER:   Mauser: 上啊！你能做到的！
ROW CAT:Oec9d0049694928119170 | L4785 | EDIT E03-018
EN: GET UP! SHOW YOUR SIBLING HOW TO FIGHT
BEFORE:   Tomcat: 起来！让你的手足看看怎么战斗
AFTER:   Tomcat: 起来！让你弟弟见识见识你的身手！
ROW CAT:O55e32328578aba61d308 | L4786 | EDIT E03-019
EN: AGENT, TAKE A DEEP BREATH
BEFORE:   Bossu: 特工，深呼吸
AFTER:   Bossu: 特工，深呼吸。
ROW CAT:O87f6f7c2778c2a3a1390 | L4787 | EDIT E03-020
EN: FOCUS AND DON'T PANIC IN COMBAT.
BEFORE:   Bossu: 集中注意，战斗中别慌张。
AFTER:   Bossu: 集中精神，交手时别慌。
CONTROL L4788 # DRAGON
### P03-011 | action=apply
原问题：已确认女线对弟弟；战斗鼓励不宜使用“你的手足”和“看看怎么战斗”的翻译腔。不得把三人合成一人。
本轮理由：仅调整各自声部；女线弟弟明确，Agent保留特工，不合并三位发话人。
EDIT_IDS ["E03-018", "E03-019", "E03-020"]

## SC55c4a209986bb4f7 | nsfw | datadf/all.ds | Mauser.AreaC_map65_a noselect
CONTROL L2475 <Mauser.AreaC_map65_a noselect>
ROW CAT:O2d95dcaddea35bc1869a | L2476 | no manual edit
EN: [Y-YIFFANY!]
BEFORE:   Mauser: [伊、伊法妮！]
AFTER:   Mauser: [伊、伊法妮！]
ROW CAT:O4f73fb9a54a0fb063fdc | L2477 | no manual edit
EN: [OH HEY MAUSER, WHAT'S UP?]
BEFORE:   Yiffany: [哦，嘿毛瑟，怎么了？]
AFTER:   Yiffany: [哦，嘿毛瑟，怎么了？]
ROW CAT:O65bd6ed637352f08cae8 | L2478 | no manual edit
EN: [I-I HEARD YOU... THAT IS, YOU FOUND... I MEAN...]
BEFORE:   Mauser: [我、我听说你……就是说，你找到了……我是说……]
AFTER:   Mauser: [我、我听说你……就是说，你找到了……我是说……]
ROW CAT:O7147d13b15e078f959b0 | L2479 | no manual edit
EN: [YOU OKAY THERE, BUDDY?]
BEFORE:   Yiffany: [你没事吧，老兄？]
AFTER:   Yiffany: [你没事吧，老兄？]
ROW CAT:O019057427e0ff6c7d7b4 | L2480 | no manual edit
EN: [FORGIVE HIM GRRRL, I JUST HAPPENED TO TELL HIM]
BEFORE:   Tomcat: [原谅他吧丫头，我也就顺口跟他提了句，说你最近弄到了一条裙子。]
AFTER:   Tomcat: [原谅他吧丫头，我也就顺口跟他提了句，说你最近弄到了一条裙子。]
ROW CAT:O5f5688fb2731b495813d | L2481 | no manual edit
EN: [THAT YOU RECENTLY ACQUIRED A DRESS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O58c73e489c74416a144d | L2482 | no manual edit
EN: [IS IT TRUE?!? YOU NEVER WEAR DRESSES!]
BEFORE:   Mauser: [真的吗？！？你从来不穿裙子的！]
AFTER:   Mauser: [真的吗？！？你从来不穿裙子的！]
ROW CAT:O4b20c65773d6989892bc | L2483 | EDIT E03-021
EN: [N-N-NOT THAT YOU SHOULDN'T! THEY'D LOOK GOOD O-]
BEFORE:   Mauser: [我、我、我不是说你不该穿！穿起来会很好看的，绝——]
AFTER:   Mauser: [我、我、我不是说你不该穿！裙子穿在你身上会很——]
ROW CAT:O278d86fd96b3289468ad | L2484 | no manual edit
EN: [WELL, IT'S TRUE. A GIFT! FROM ELF QUEEN ENELYE.]
BEFORE:   Yiffany: [嗯，是真的。是礼物！精灵女王恩内莉送的。]
AFTER:   Yiffany: [嗯，是真的。是礼物！精灵女王恩内莉送的。]
ROW CAT:O0ff9f42511382466c6b3 | L2485 | no manual edit
EN: [!!!]
BEFORE:   Mauser: [！！！]
AFTER:   Mauser: [！！！]
ROW CAT:O2c7062e3dd39a403386a | L2486 | no manual edit
EN: [YEAH CHEESEBALL OVER HERE LOOKS LIKE HE'S ABOUT TO FAINT]
BEFORE:   Tomcat: [是啊，这边这位芝士球看着快晕过去了，也许我也该开始监测一下/他/的生命体征了……]
AFTER:   Tomcat: [是啊，这边这位芝士球看着快晕过去了，也许我也该开始监测一下/他/的生命体征了……]
ROW CAT:O102bef63f627ec0a464b | L2487 | no manual edit
EN: [MAYBE I SHOULD START MONITORING /HIS/ VITALS TOO...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O15853070c9bae3dcd17b | L2488 | no manual edit
EN: [NO!! THAT'S NOT IT! SHE SAID IT WAS AN ELVEN GIFT!]
BEFORE:   Mauser: [不！！不是那样的！她说那是精灵的赠礼！]
AFTER:   Mauser: [不！！不是那样的！她说那是精灵的赠礼！]
ROW CAT:O858e168f6fe1a5e067e2 | L2489 | no manual edit
EN: [YEAH, AND...?]
BEFORE:   Yiffany: [嗯，然后呢……？]
AFTER:   Yiffany: [嗯，然后呢……？]
ROW CAT:O1320955f247bc497178a | L2490 | no manual edit
EN: [THE TUTONE ELVES ARE SAID TO HAVE WOVEN SPECIAL CLOTH]
BEFORE:   Mauser: [据说图托恩的精灵会织出特别的布料，穿在身上真的会让人感觉更轻盈！]
AFTER:   Mauser: [据说图托恩的精灵会织出特别的布料，穿在身上真的会让人感觉更轻盈！]
ROW CAT:O52ed73bef590f579c54c | L2491 | no manual edit
EN: [THAT WOULD ACTUALLY MAKE A PERSON FEEL LIGHTER WHEN WORN!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obba757f71ab5a8baef0e | L2492 | no manual edit
EN: [HUH, NOW THAT YA MENTION IT, THIS IT DOES FEEL AIRY.]
BEFORE:   Yiffany: [唔，你这么一说，这裙子确实挺透气的。]
AFTER:   Yiffany: [唔，你这么一说，这裙子确实挺透气的。]
ROW CAT:O6a4ee3edb80c32231bc0 | L2493 | no manual edit
EN: [MAYBE I'LL PUT IT ON AND TEST IT ON SOME CRUMBLY BLOCKS]
BEFORE:   Yiffany: [也许我该穿上它，找几块易碎的砖块试一试]
AFTER:   Yiffany: [也许我该穿上它，找几块易碎的砖块试一试]
ROW CAT:Odf8eaee8f25e3ff7e70d | L2494 | no manual edit
EN: [A-A-A-A-A-AIRY!!?]
BEFORE:   Mauser: [透、透、透、透、透、透气！！？]
AFTER:   Mauser: [透、透、透、透、透、透气！！？]
ROW CAT:Occ36c36d2b0aa020f33a | L2495 | no manual edit
EN: [OKAY GIRL YOU GO FIND SOME OLD CRUMBLING BLOCKS]
BEFORE:   Tomcat: [行吧姑娘，你去找几块老旧易碎的砖块，试试那条反重力裙子，这边这只快晕过去的鼠鼠就交给我吧。]
AFTER:   Tomcat: [行吧姑娘，你去找几块老旧易碎的砖块，试试那条反重力裙子，这边这只快晕过去的鼠鼠就交给我吧。]
ROW CAT:O6a082ca3ee2074e4adcd | L2496 | no manual edit
EN: [TO TEST THAT ANTI-GRAV DRESS ON]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O837254dff2b71d006e8c | L2497 | no manual edit
EN: [WHILE I DEAL WITH THIS FAINTING MOUSE OVER HERE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4b68c81f222b720baba3 | L2498 | no manual edit
EN: [AWWW, WHAT A CUTE COUPLE. HAVE FUN!]
BEFORE:   Yiffany: [哎呀，多可爱的一对。玩得开心！]
AFTER:   Yiffany: [哎呀，多可爱的一对。玩得开心！]
### P03-012 | action=apply
原问题：look good on...被截断，现译无依据添出“绝——”，导致突然出现不明半词。保留尚未说完的夸奖。
本轮理由：保留局部结巴及被截断的夸奖，不凭空添绝字残片。
EDIT_IDS ["E03-021"]

## SCf532915a63773f91 | nsfw | datadf/all.ds | Tomcat.AreaH_map02_a noselect
CONTROL L2590 <Tomcat.AreaH_map02_a noselect>
ROW CAT:O16593fd46e1a28313c75 | L2591 | EDIT E03-022
EN: [OH HEY! READY TO GET FRISKY WITH THE LOCAL FUC-]
BEFORE:   Tomcat: [哦嘿！准备跟本地的那些操-]
AFTER:   Tomcat: [哦，嘿！准备好亲热一番了？就跟本地那些操——]
ROW CAT:O819647f6652669d93d6f | L2592 | no manual edit
EN: [THE LOCAL FAUNA WILL PROVIDE US WITH IMPORTANT DATA]
BEFORE:   Yiffany: [我会用双方同意的接触和自愿给予的实物，与本地生物建立联结，之后它们就会给我们提供重要数据，这才配得上一位宇宙大使。]
AFTER:   Yiffany: [我会用双方同意的接触和自愿给予的实物，与本地生物建立联结，之后它们就会给我们提供重要数据，这才配得上一位宇宙大使。]
ROW CAT:O41c5c57fde9156338c9a | L2593 | no manual edit
EN: [AFTER I'VE BONDED WITH THEM USING A COMBINATION OF]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oef1436e0305dabf72bb7 | L2594 | no manual edit
EN: [CONSENSUAL CONTACT AND FREELY GIVEN MATERIAL GOODS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oce074f825fc014f7d2fc | L2595 | no manual edit
EN: [AS BEFITS A COSMO AMBASSADOR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O033816f68b73722f386c | L2596 | no manual edit
EN: [...]
BEFORE:   Tomcat: [……]
AFTER:   Tomcat: [……]
ROW CAT:O948e459ae0d32dcfad7d | L2597 | no manual edit
EN: [GIRL, YOU KNOW I CAN SEE YOUR HEART RATE RISING]
BEFORE:   Tomcat: [姑娘，你知道吧，你念手册上那套废话的时候，我看得到你心率在往上飙，对吧？]
AFTER:   Tomcat: [姑娘，你知道吧，你念手册上那套废话的时候，我看得到你心率在往上飙，对吧？]
ROW CAT:O3b1b574f02364924e636 | L2598 | no manual edit
EN: [WHILE YOU SPEWED THAT NONSENSE FROM THE MANUAL, RIGHT?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O44abc9ae439d2607ec8c | L2599 | no manual edit
EN: [COME ON, I DIDN'T GRADUATE TOP OF MY CLASS FOR NOTHING!]
BEFORE:   Yiffany: [拜托，我可不是白当年级第一毕业的！]
AFTER:   Yiffany: [拜托，我可不是白当年级第一毕业的！]
ROW CAT:O4dfa926bcd7db9480abe | L2600 | no manual edit
EN: [YEAH, SURE. JUST REMEMBER THAT THERE ARE OTHER MISSIONS]
BEFORE:   Tomcat: [是是是。记住，除了「和本地生物建立联结」，还有别的任务，好吗？]
AFTER:   Tomcat: [是是是。记住，除了「和本地生物建立联结」，还有别的任务，好吗？]
ROW CAT:Oa3925c37af59273e8a01 | L2601 | no manual edit
EN: [BEYOND "BONDING WITH THE LOCALS", ALRIGHT?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obf1ae30118ffe3d4566e | L2602 | no manual edit
EN: [YOU ARE SOOOOOO JEALOUS, HEHE...]
BEFORE:   Yiffany: [你超————嫉妒了吧，嘿嘿……]
AFTER:   Yiffany: [你超————嫉妒了吧，嘿嘿……]
ROW CAT:Ofbc6eb29909d31de873f | L2603 | no manual edit
EN: [JUST REMEMBER, AGENT.]
BEFORE:   Bossu: [记住，特工。]
AFTER:   Bossu: [记住，特工。]
ROW CAT:O99755dc740e44b72ed68 | L2604 | no manual edit
EN: [IN ORDER TO STUDY LOCAL LIFE CLOSELY, YOU MUST DEFEAT]
BEFORE:   Bossu: [要近距离研究本地生命，你必须在战斗中使用驯兽电击枪击败它们。]
AFTER:   Bossu: [要近距离研究本地生命，你必须在战斗中使用驯兽电击枪击败它们。]
ROW CAT:O4f8f7552ab42c3a6e4bb | L2605 | no manual edit
EN: [THEM IN COMBAT USING THE TRAINER TAZER.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O1c6c293a0eb2ce81ff06 | L2606 | no manual edit
EN: [DOING SO ALLOWS THE OBSERVATION UNITS TO PICK UP FAUNA]
BEFORE:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
AFTER:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
ROW CAT:O35d35780256bbe6d3462 | L2607 | no manual edit
EN: [SO THAT YOU MAY OBSERVE THEM CLOSER IN THE HANGAR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6adb3bbeac6ba0316849 | L2608 | no manual edit
EN: [OF COURSE! STANDARD PROTOCOL. I'M ON IT.]
BEFORE:   Yiffany: [当然！标准流程。我这就去办。]
AFTER:   Yiffany: [当然！标准流程。我这就去办。]
### P03-013 | action=apply
原问题：当前只保留了宾语骂词残片，漏去get frisky的挑逗意图；这里只截断FUC-，不能把整句的亲热含义一起丢失。具体断句仍需后续节点回填时核演出。
本轮理由：先恢复get frisky，再落在FUC残词的中断；不补残词完整宾语。
EDIT_IDS ["E03-022"]

## SCe177d9059160b711 | nsfw | datadf/all.ds | TomcatItems.SpecialCosmoID
CONTROL L4373 <TomcatItems.SpecialCosmoID>
ROW CAT:Of7b4aee023da16f4c3ba | L4374 | no manual edit
EN: [GOT YOUR ID! FINALLY, YOU'RE A BIG GIRL AGAIN!]
BEFORE:   Tomcat: [拿到你的证件了！你终于又是大姑娘了！]
AFTER:   Tomcat: [拿到你的证件了！你终于又是大姑娘了！]
ROW CAT:O1772a86177ede9f09849 | L4375 | no manual edit
EN: [CAN'T REALLY HAVE A NIGHT ON THE TOWN AROUND HERE, BUT AT]
BEFORE:   Yiffany: [这附近没法好好进城玩一夜，不过至少我能用这些点对点传送台了。]
AFTER:   Yiffany: [这附近没法好好进城玩一夜，不过至少我能用这些点对点传送台了。]
ROW CAT:Oc55802bbd227f66b6b46 | L4376 | no manual edit
EN: [LEAST I CAN ACCESS THESE SITE-TO-SITE TELEPADS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O55a87e76455b7b089c78 | L4377 | no manual edit
EN: [HEH, I REMEMBER THAT FAKE ID YOU GOT BACK IN SCHOOL.]
BEFORE:   Tomcat: [呵，我还记得你上学时弄的那张假证。]
AFTER:   Tomcat: [呵，我还记得你上学时弄的那张假证。]
ROW CAT:O8cf3b3edc2135e613e04 | L4378 | EDIT E03-023
EN: [UGH, THAT THING *NEVER* WORKED. SUCH A WASTE OF LECT...]
BEFORE:   Yiffany: [呃，那东西*从来*没用过。纯属浪费 LECT……]
AFTER:   Yiffany: [呃，那东西*从来*就没管用过。纯属浪费 LECT……]
ROW CAT:Odc623c1b8ddaab72be50 | L4379 | no manual edit
EN: [REALLY?! I REMEMBER YOU BRAGGING ABOUT ALL THE THINGS]
BEFORE:   Tomcat: [真的？！我记得你吹过，用它能买到多少东西！]
AFTER:   Tomcat: [真的？！我记得你吹过，用它能买到多少东西！]
ROW CAT:Oa1fb7434119a411cfada | L4380 | no manual edit
EN: [YOU COULD BUY WITH IT!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od17e01d90b4af52d92c9 | L4381 | no manual edit
EN: [HEY, I HAD TO GET *SOME* USE OUT OF IT, EVEN IF IT]
BEFORE:   Yiffany: [嘿，我也得让它*有点*用处，哪怕只是拿来让你们佩服……]
AFTER:   Yiffany: [嘿，我也得让它*有点*用处，哪怕只是拿来让你们佩服……]
ROW CAT:O3af7278976aa706b959e | L4382 | no manual edit
EN: [WAS JUST IMPRESSING YOU GUYS...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa2fdfbcbdfde84e705ed | L4383 | no manual edit
EN: [PFT, YOU ALWAYS DID TRY AND ACT COOL.]
BEFORE:   Tomcat: [噗，你一直都想装酷。]
AFTER:   Tomcat: [噗，你一直都想装酷。]
ROW CAT:O530d744fbc41a9eb9a6a | L4384 | no manual edit
EN: [YEAH YEAH. WE CAN HAVE SOME DRINKS FOR REAL WHEN]
BEFORE:   Yiffany: [是是。等我回去，我们可以真的喝一杯。伊法妮完毕。]
AFTER:   Yiffany: [是是。等我回去，我们可以真的喝一杯。伊法妮完毕。]
ROW CAT:O778c7c582a1314858d08 | L4385 | no manual edit
EN: [I GET BACK. YIFFANY OUT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P03-014 | action=apply
原问题：never worked是试过却从未奏效，不是从未使用。后续承认仅用来吹牛的笑点依赖假证办不成事。
本轮理由：never worked为从未奏效而非从未用；保留强调标记、货币及否定。
EDIT_IDS ["E03-023"]

## SC37d79a5ff9bf0f1b | nsfw | datadf/all.ds | TomcatItems.SpecialKeycard0
CONTROL L4293 <TomcatItems.SpecialKeycard0>
ROW CAT:Oebe45a2327d803479266 | L4294 | no manual edit
EN: [IN ORDER TO USE A KEYCARD, ALL YOU HAVE TO DO IS]
BEFORE:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
AFTER:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
ROW CAT:O9dd6948923178eafbdff | L4295 | no manual edit
EN: [WALK INTO AN ENERGY DOOR WHILE HOLDING ONE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of6fefcbd1cb655d79172 | L4296 | no manual edit
EN: [YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!]
BEFORE:   Tomcat: [你能打开等级不超过门上所标数字的门！]
AFTER:   Tomcat: [你能打开等级不超过门上所标数字的门！]
### P03-015 | action=defer
原问题：them回指门卡；现译“等级不超过门上所标数字的门”把门卡权限上限误写成门自己的等级，提示失效。
本轮理由：them回指门卡或门本身有源歧义；没有机制证据，不凭草案发明门卡等级规则。保留待补证。
EDIT_IDS []

## SCc45766061e40d9cd | nsfw | datadf/all.ds | TomcatItems.StatOctopus
CONTROL L3933 <TomcatItems.StatOctopus>
ROW CAT:Ofd55b37f453cce17d335 | L3934 | no manual edit
EN: [DUDE.]
BEFORE:   Tomcat: [老兄。]
AFTER:   Tomcat: [老兄。]
ROW CAT:O139a69e86e1235595827 | L3935 | no manual edit
EN: [OCTOPUS.]
BEFORE:   Tomcat: [章鱼。]
AFTER:   Tomcat: [章鱼。]
ROW CAT:O6f6af8172e3ca9da333f | L3936 | no manual edit
EN: [I LOVE OCTOPUS.]
BEFORE:   Tomcat: [我爱章鱼。]
AFTER:   Tomcat: [我爱章鱼。]
ROW CAT:Ob1a1ae3ce44bb5f5c94d | L3937 | no manual edit
EN: [DUDE. BRO. GIMME.]
BEFORE:   Tomcat: [老兄。兄弟。给我。]
AFTER:   Tomcat: [老兄。兄弟。给我。]
ROW CAT:O92fb630da87f74497dd2 | L3938 | no manual edit
EN: [IT MAKES YOU SMARTER TOO, I NEED IT.]
BEFORE:   Tomcat: [它也能让你更聪明，我需要它。]
AFTER:   Tomcat: [它也能让你更聪明，我需要它。]
ROW CAT:Ocf29b73ac06f6610bf26 | L3939 | EDIT E03-024
EN: [D U D E . . .]
BEFORE:   Tomcat: [D U D E . . .]
AFTER:   Tomcat: [老——兄……]
### P03-016 | action=apply
原问题：原文刻意短促重复索食，应保留节拍；末句D U D E残留英文使重复升级的笑点断开。仅段落提案，正式回填不得抹去节点节拍。
本轮理由：只修末尾英文呼唤；前五槽短促索食语义与节拍成立，不机械全段换词。
EDIT_IDS ["E03-024"]

## SC282b145b3fce5463 | nsfw | datadm/all.ds | AreaA_Prison1.Goodbye
CONTROL L549 <AreaA_Prison1.Goodbye>
ROW CAT:Oab76df87a78ccef91359 | L550 | EDIT E03-025
EN: Th-thanks pal, I don't know how you non-tops do it...!
BEFORE:   * 谢、谢谢你，伙计，我真不知道你们非上位的是怎么做到的……！
AFTER:   * 谢、谢谢你，伙计。真不知道你们不当攻的都是怎么熬过来的……！
### P03-017 | action=apply
原问题：non-tops是性角色而非职级；“非上位的是怎么做到的”既缺所指又像阶层分类。保留受救者嘴硬感，不扩为已确认永久偏好。
本轮理由：non-tops在本成人语境是性角色，不是职级；保留当事人嘴硬。
EDIT_IDS ["E03-025"]

## SCa3b719e08b22fe40 | nsfw | datadm/all.ds | AreaC_Prison1.Rescue
CONTROL L1296 <AreaC_Prison1.Rescue>
ROW CAT:Of535660610aae08766ef | L1297 | no manual edit
EN: I've been cooped up here for stars knows how long. Can ya gimme me a hand?
BEFORE:   * 只有星星才知道我被关在这儿多久了。能帮我一把吗？
AFTER:   * 只有星星才知道我被关在这儿多久了。能帮我一把吗？
### P03-018 | action=reject
原问题：stars knows为世界内感叹习语。当前“只有星星才知道”可作为科幻化感叹保留；此处仅给更短促口语的可选方向，不判天文事实错译，不新增神祇设定。
本轮理由：当前星星才知道可作世界内感叹；原发现也承认可保留，天知道仅偏好替换，不足判错。
EDIT_IDS []

## SC41c8c647818eb3b1 | nsfw | datadm/all.ds | AreaC_Prison2.Goodbye
CONTROL L1314 <AreaC_Prison2.Goodbye>
ROW CAT:Oedc404756cca377cd829 | L1315 | EDIT E03-026
EN: Just wait 'til I limber up, those elves won't know what hit 'em!
BEFORE:   * 等我活动开筋骨，那些精灵挨了打都不知道是谁干的！
AFTER:   * 等我活动开筋骨，准让那些精灵吃不了兜着走！
### P03-019 | action=apply
原问题：won’t know what hit them强调突然而压倒性的反击，不是打完不知道行凶者；现译无端添加隐蔽身份。
本轮理由：习语强调凌厉反击，不发明隐瞒身份。
EDIT_IDS ["E03-026"]

## SC4fbf9bea793d927e | sfw | datadm/all.ds | AreaC_Slaver1.Hello
CONTROL L1394 <AreaC_Slaver1.Hello>
CONTROL L1395   if { !koboCostume() } {
ROW SFW15558a0003a544fca98b5ad2 | L1396 | no manual edit
EN: Nice night in the forest huh? 
BEFORE:     * 森林里今晚夜色不错，是吧？ 
AFTER:     * 森林里今晚夜色不错，是吧？ 
ROW SFWaf96c05d90ce42366e265acc | L1397 | no manual edit
EN: A fine night to enjoy some fine dining, wouldn't you say?
BEFORE:     * 这样的夜晚正适合享用一顿美餐，你说是不是？
AFTER:     * 这样的夜晚正适合享用一顿美餐，你说是不是？
CONTROL L1398   } else {
ROW SFWf35e96a4a0adfc726f3a91c9 | L1399 | EDIT E03-027
EN: Well lookee here, a friendly face. Welcome to the black market!
BEFORE:     * 哟，瞧瞧这儿，一张友善的面孔。欢迎来到黑市！
AFTER:     * 哟，自己人来了。欢迎光临黑市！
CONTROL L1400   }
### P03-020 | action=apply
原问题：friendly face在koboCostume分支是认作同伙而欢迎，不是评价面孔友善；只说明当下外观误认，不认证主角海盗身份。
本轮理由：仅koboCostume分支的当下误认，不把主角认证为奴贩。
EDIT_IDS ["E03-027"]

## SC1688edd7961e362d | nsfw | datadm/all.ds | AreaX_Upgrade.Meeting
CONTROL L1878 <AreaX_Upgrade.Meeting>
ROW CAT:O21bd5c0d2d2a2ca67053 | L1879 | EDIT E03-028
EN: Heya Yiffai! Nice to see you up here in my brand new spacelab!
BEFORE:   * 嘿，伊法伊！很高兴在这上面见到你，就在我全新的太空实验室里！
AFTER:   * 嘿，伊法伊！很高兴你能上来，看看我全新的太空实验室！
ROW CAT:Ofcc19fdc75fbc098c9f5 | L1880 | no manual edit
EN: Heheh... I guess this used to be your sister's ship though, huh?
BEFORE:   * 嘿嘿……不过我想，这以前是你姐姐的飞船吧？
AFTER:   * 嘿嘿……不过我想，这以前是你姐姐的飞船吧？
ROW CAT:Oc0058d264996e559a686 | L1881 | no manual edit
EN: Pirates already looted most of it, but I found a working equipment repair bay!
BEFORE:   * 海盗已经把大部分东西都抢走了，但我找到了一台还能用的装备修理舱！
AFTER:   * 海盗已经把大部分东西都抢走了，但我找到了一台还能用的装备修理舱！
### P03-021 | action=apply
原问题：先欢迎再心虚揭示实验室来历，当前“在这上面见到你，就在……”挂接生硬；保留sister与角色猜测，不补设施真实规格。
本轮理由：保留up here与欢迎；姐姐飞船猜测及修理舱后两槽已成立，不照草案强改规格。
EDIT_IDS ["E03-028"]

## SC2fc4d040f52d9594 | sfw | datadm/all.ds | BossuDex.ClassicJellyfish
CONTROL L3125 <BossuDex.ClassicJellyfish>
ROW SFWab74b9d79595e6b56cf2c6f4 | L3126 | EDIT E03-029
EN: [BOSSU, REQUESTING IMMEDIATE UPDATE ON CONDITIONS]
BEFORE:   Yiffai: [波苏，请求立即更新当前情况，以确认我并非水生生物。]
AFTER:   Yiffai: [波苏，请立刻确认我的身体状态，确认我没变成水生生物！]
ROW SFWcb5d996c9687d6bf5b360c0c | L3127 | no manual edit
EN: [TO VERIFY THAT I AM NOT AN AQUATIC BEING.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWba623e6105806e3ce3b40293 | L3128 | no manual edit
EN: [DON'T WORRY YIFFAI, YOU ARE STILL 100% DOG.]
BEFORE:   Bossu: [放心，伊法伊，你还是100%的狗。]
AFTER:   Bossu: [放心，伊法伊，你还是100%的狗。]
ROW SFW6a1756d9f6939e5750ad2633 | L3129 | EDIT E03-030
EN: [THE STRANGE HAPPE- NINGS ON TUTONE HAVE LEAD TO]
BEFORE:   Bossu: [图托恩上发生的怪事，导致有人目击到非实体的水母，这也许会让你产生别的想法。]
AFTER:   Bossu: [图托恩的异变导致有人目击到没有实体的水母，可能正是它们让你怀疑起自己来了。]
ROW SFWd3873285709b8f2bb9e6c863 | L3130 | no manual edit
EN: [SIGHTINGS OF NON- PHYSICAL JELLY FISH] 
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWf6556f2e2d7703a9429b7728 | L3131 | no manual edit
EN: [WHICH MIGHT BE CAUSING YOU TO THINK OTHERWISE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW9dd081848f9516546525af9f | L3132 | EDIT E03-031
EN: [THEY SEEM PLENTY PHYSICAL TO ME, OW...]
BEFORE:   Yiffai: [在我看来它们相当实体，哎哟……]
AFTER:   Yiffai: [我可觉得它们实在得很，哎哟……]
ROW SFW6055ad0fc865c3cc213ecea5 | L3133 | no manual edit
EN: [ON THE CONTRARY, IF YOU'RE TO BELIEVE THE REPORTS...]
BEFORE:   Bossu: [恰恰相反，如果那些报告可信的话……]
AFTER:   Bossu: [恰恰相反，如果那些报告可信的话……]
ROW SFWd62b66008dbc8c0a05abe2d9 | L3134 | no manual edit
EN: [ANY CREATURE FLASHING OMINOUSLY PURPLE ON TUTONE]
BEFORE:   Bossu: [图托恩上任何闪着不祥紫光的生物，其实都是灵能动荡产生的幻象。]
AFTER:   Bossu: [图托恩上任何闪着不祥紫光的生物，其实都是灵能动荡产生的幻象。]
ROW SFW96217f3adb4f9e4dc136b308 | L3135 | no manual edit
EN: [IS ACTUALLY AN APPARITION OF PSYCHIC TURMOIL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW7beae928290b54c438a1e3e3 | L3136 | no manual edit
EN: [HOW YOU DEAL WITH THEM, WE CANNOT SAY FROM HERE.]
BEFORE:   Bossu: [至于你该怎么应付它们，我们从这边说不准。]
AFTER:   Bossu: [至于你该怎么应付它们，我们从这边说不准。]
ROW SFWd8b5ab372387af0a73b0e6b2 | L3137 | EDIT E03-032
EN: [HMM, PSYCHIC, YOU SAY.]
BEFORE:   Yiffai: [嗯，精神，你是说。]
AFTER:   Yiffai: [嗯，你是说灵能啊。]
ROW SFW569d446d59b9462d5008947b | L3138 | no manual edit
EN: [GUESS I'LL HAVE TO FIGURE IT OUT MYSELF...]
BEFORE:   Yiffai: [看来只能我自己想办法搞清楚了……]
AFTER:   Yiffai: [看来只能我自己想办法搞清楚了……]
### P03-022 | action=apply
原问题：原段是一本正经请求确认—总部解释—挨打吐槽；“更新当前情况”“相当实体”生硬，使身体接触反驳失去落点。
本轮理由：重建郑重请求、总部推测和挨打反驳，不动100%数值节点。
EDIT_IDS ["E03-029", "E03-030", "E03-031"]
### P03-023 | action=apply
原问题：“嗯，精神，你是说”保留英语后置倒装，无法承接前文灵能幻象线索；不擅自补具体解法。
本轮理由：恢复中文承接语序；不补能力解法，后槽现译保留。
EDIT_IDS ["E03-032"]

## SCdd1003a024a00fd3 | sfw | datadm/all.ds | BossuDex.ClassicKobold
CONTROL L3049 <BossuDex.ClassicKobold>
ROW SFW2394b80f83eb536c44a88428 | L3050 | EDIT E03-033
EN: [BOSSU! I'VE RUN INTO SOME ANTHRO GREEN LIZARD UNITS]
BEFORE:   Yiffai: [波苏！我撞上了一些兽人绿色蜥蜴兵，但它们看着相当不友好！]
AFTER:   Yiffai: [波苏！我遇到了一批人形绿蜥蜴兵，看着可一点都不友好！]
ROW SFW09875f32c4278b4d86aeb378 | L3051 | no manual edit
EN: [BUT THEY SEEM DECIDEDLY UNFRIENDLY!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW4e609f69b3598e127a985dad | L3052 | no manual edit
EN: [AHH YOU'VE RUN INTO SOME KOBOLDS DOWN THERE, HAVE YOU?]
BEFORE:   Bossu: [啊，你在下面撞上科博德了，是吧？]
AFTER:   Bossu: [啊，你在下面撞上科博德了，是吧？]
ROW SFWaf83e99ee3bad2569ac39250 | L3053 | no manual edit
EN: [IS THAT WHAT THESE BIG LIZARD FOLKS ARE?]
BEFORE:   Yiffai: [这些大蜥蜴家伙就是科博德？]
AFTER:   Yiffai: [这些大蜥蜴家伙就是科博德？]
ROW SFWf77c88552453f91dc858a799 | L3054 | no manual edit
EN: [CORRECT. YOU BETTER GET USED TO TANGLING WITH THEM.]
BEFORE:   Bossu: [没错。你最好习惯跟他们缠斗。]
AFTER:   Bossu: [没错。你最好习惯跟他们缠斗。]
ROW SFWf5e2d63876c039cc8f63fe79 | L3055 | no manual edit
EN: [THOSE LIZARDS ARE A SLY BUNCH, KNOWN FOR PIRACY AND SLAVING]  
BEFORE:   Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到最后能赚到LECT的营生！]  
AFTER:   Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到最后能赚到LECT的营生！]  
ROW SFW30082df353dcdbd47eea893b | L3056 | no manual edit
EN: [AND ANYTHING ELSE THAT HAS A LECT PAYOFF AT THE END!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW9dcd4998baf7934e5dc81ff3 | L3057 | no manual edit
EN: [YOU'RE LIABLE TO RUN INTO THEM ON MOST ANY SORTIE.]
BEFORE:   Bossu: [你随便出趟任务都可能撞上他们。]
AFTER:   Bossu: [你随便出趟任务都可能撞上他们。]
ROW SFW2e7c4bbdb359f32a6cdf8d25 | L3058 | no manual edit
EN: [I CAN HANDLE THEM! I'VE ALREADY TAKEN OUT, LIKE...]
BEFORE:   Yiffai: [我应付得了他们！我已经干掉了，大概……]
AFTER:   Yiffai: [我应付得了他们！我已经干掉了，大概……]
ROW SFW3fc5a57eb16e0c02910657d6 | L3059 | no manual edit
EN: [...A BUNCH!]
BEFORE:   Yiffai: [……一大把！]
AFTER:   Yiffai: [……一大把！]
### P03-024 | action=apply
原问题：anthro修饰具人形蜥蜴，当前“兽人绿色蜥蜴兵”容易误认另一兽人种族，且中文定语堆叠。保留主人公此时还不认识科博德。
本轮理由：anthro指人形，不额外立兽人种族，也不提前揭科博德。
EDIT_IDS ["E03-033"]

## SC6681188910c28840 | nsfw | datadm/all.ds | Mauser.Kobo noselect noamendfreq
CONTROL L3422 <Mauser.Kobo noselect noamendfreq>
ROW CAT:O2e4746b55c7e9ff8e37b | L3423 | no manual edit
EN: [HUH? YIFFAI...?]
BEFORE:   Mauser: [嗯？伊法伊……？]
AFTER:   Mauser: [嗯？伊法伊……？]
ROW CAT:O3812029a336d4ea60d00 | L3424 | no manual edit
EN: [YEAH IT'S ME. I'M JUST IN DISGUISE AS A KOBOLD.]
BEFORE:   Yiffai: [对，是我。我只是伪装成了一只科博德。]
AFTER:   Yiffai: [对，是我。我只是伪装成了一只科博德。]
ROW CAT:O3e5e25ee5a75819994b1 | L3425 | no manual edit
EN: [... I DON'T THINK THE DISGUISE WILL WORK WELL IF YOU'RE]
BEFORE:   Mauser: [……如果你还挥着台PPP电台到处叫人，我不觉得这套伪装会有多好用。]
AFTER:   Mauser: [……如果你还挥着台PPP电台到处叫人，我不觉得这套伪装会有多好用。]
ROW CAT:O264f938f48b111a8d81b | L3426 | no manual edit
EN: [WAVING A PPP RADIO AROUND AND CALLING PEOPLE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oee4718c741515082806b | L3427 | EDIT E03-034
EN: [OH... R-RIGHT I GUESS SO. YIFFAI OUT.]
BEFORE:   Yiffai: [哦……是、是的，我想是这样。伊法伊通话完毕。]
AFTER:   Yiffai: [哦……说、说得也是。伊法伊通话完毕。]
### P03-025 | action=apply
原问题：最后的“是的，我想是这样”对吐槽反应生硬；整段保留认出—解释—戳穿—急挂断，不把角色自称伪装升级成潜伏事实。
本轮理由：只修急挂断反应，保留原局部结巴；其余认出和无线电吐槽成立。
EDIT_IDS ["E03-034"]

## SC6aad09e2fe9e972d | nsfw | datadm/all.ds | Starkill.AreaA_map33_a noselect noamendfreq
CONTROL L2280 <Starkill.AreaA_map33_a noselect noamendfreq>
ROW CAT:O5a19743a35953088a62d | L2281 | no manual edit
EN: [SRRRRKT... GEAR TO... KKZZZ... ADVANCE!]
BEFORE:   Starkill: [SRRRRKT... GEAR TO... KKZZZ... 前进！]
AFTER:   Starkill: [SRRRRKT... GEAR TO... KKZZZ... 前进！]
ROW CAT:O81f52049e705dfcdb1b6 | L2282 | no manual edit
EN: [...NOT GIVE... SHHSHSHKK...TOO... ....ZZKT..LATE!...]
BEFORE:   Starkill: [...别给... SHHSHSHKK...太... ....ZZKT..晚了！...]
AFTER:   Starkill: [...别给... SHHSHSHKK...太... ....ZZKT..晚了！...]
ROW CAT:Oc3375c095596038a08d2 | L2283 | no manual edit
EN: [...EKSKHSKKS....]
BEFORE:   Starkill: [...EKSKHSKKS....]
AFTER:   Starkill: [...EKSKHSKKS....]
ROW CAT:Of0e3701437037f9cee5b | L2284 | no manual edit
EN: [...KKKKZBE... PREPARED... ...AGENT...ZZZRK...]
BEFORE:   Starkill: [……咔咔滋……做好准备……特工……滋咔……]
AFTER:   Starkill: [……咔咔滋……做好准备……特工……滋咔……]
ROW CAT:O0d56bb947c54f8b5bb99 | L2285 | no manual edit
EN: [...]
BEFORE:   Starkill: [……]
AFTER:   Starkill: [……]
### P03-026 | action=defer
原问题：原文为受干扰的残片GEAR TO... / NOT GIVE...，尚不能确定省略结构；“别给”擅定give为完整祈使。须核对原音/演出或作者意图后再提完整译段，不能凭后文猜补。
本轮理由：受干扰GEAR TO及NOT GIVE残片不能确定省略句法；无原音或作者补证，不猜补完整命令。
EDIT_IDS []

## SC53d8c681becfa52c | nsfw | datadm/all.ds | TomcatItems.FakeMilk
CONTROL L4024 <TomcatItems.FakeMilk>
ROW CAT:O28161799936a71beeff2 | L4025 | no manual edit
EN: [OH MAN WHAT IS THAT?]
BEFORE:   Tomcat: [天哪，那是什么？]
AFTER:   Tomcat: [天哪，那是什么？]
ROW CAT:O61267c0f69f680d8b549 | L4026 | no manual edit
EN: [WHAT DO YOU MEAN? IT'S JUST SOME MILK THAT I BOUGHT.]
BEFORE:   Yiffai: [你什么意思？就是我买的一些牛奶。]
AFTER:   Yiffai: [你什么意思？就是我买的一些牛奶。]
ROW CAT:Of79481260db1acaacbc6 | L4027 | EDIT E03-035
EN: [I USED TO WORK AT A DAIRY FARM, AND THAT IS NOOOT MILK.]
BEFORE:   Mauser: [我以前在奶牛场干活，而那才不是啊啊啊牛奶。]
AFTER:   Mauser: [我以前在奶牛场干过，那可绝——对不是牛奶。]
ROW CAT:Ofc3c1699918ebdb466c4 | L4028 | EDIT E03-036
EN: [IT IS KINDA JIGGLY. IS MILK USUALLY JIGGLY?]
BEFORE:   Yiffai: [它有点晃。牛奶通常会晃吗？]
AFTER:   Yiffai: [它还有点颤。牛奶一般也这样吗？]
ROW CAT:O0ecebf6276ab2a76ccf2 | L4029 | EDIT E03-037
EN: [UHHHHHH]
BEFORE:   Tomcat: [呃啊啊啊啊啊啊]
AFTER:   Tomcat: [呃……]
ROW CAT:O31de2499cb14bd65b67d | L4030 | EDIT E03-038
EN: [UMMMMMM]
BEFORE:   Mauser: [嗯啊啊啊啊啊啊]
AFTER:   Mauser: [嗯……]
ROW CAT:Od44a03e6962901e10a79 | L4031 | EDIT E03-039
EN: [IT DOESN'T SEEM TO BE OUTRIGHT POISON, IN ANY CASE]
BEFORE:   Tomcat: [不管怎样，它看起来不是明摆着的毒药，所以也许它对你真有好处！]
AFTER:   Tomcat: [不管怎样，看着倒不像什么毒物，说不定还真对你有好处！]
ROW CAT:Od7c13083cc0ed5530f5d | L4032 | no manual edit
EN: [SO MAYBE IT'LL ACTUALLY BE GOOD FOR YOU!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of724e913618e4a23a97b | L4033 | no manual edit
EN: [FISH IS GOOD FOR YOU RIGHT? AND THIS SMELLS LIKE FISH!]
BEFORE:   Yiffai: [鱼对人有好处吧？而这东西闻着像鱼！]
AFTER:   Yiffai: [鱼对人有好处吧？而这东西闻着像鱼！]
ROW CAT:O9eb0bdc02a7ccefb178e | L4034 | no manual edit
EN: [OKAY I'M OUT.]
BEFORE:   Mauser: [好，我撤了。]
AFTER:   Mauser: [好，我撤了。]
ROW CAT:Odd6bdbf49fdc48356f3d | L4035 | EDIT E03-040
EN: [ME TOO. GOOD LUCK WITH THAT.]
BEFORE:   Tomcat: [我也是。祝你好运应付那个。]
AFTER:   Tomcat: [我也是。你自求多福吧。]
### P03-027 | action=apply
原问题：整场为怀疑伪奶—小心绕开真相—借口挂断；当前NOOOT/UHHHH机械写“啊啊啊”变成惨叫，“祝你好运应付那个”英语腔。“颤”体现凝胶般抖动，不补物质身份。
本轮理由：拉长音改迟疑而非惨叫，凝胶感不定物质身份；保留毒性及益处的不确定和各人槽位。
EDIT_IDS ["E03-035", "E03-036", "E03-037", "E03-038", "E03-039", "E03-040"]

## SC6953d2082e5c2552 | sfw | datav/dictionary.json | LuckyBodyNotUpgraded
ROW SFW06d50563ea2f7b10aee429aa | L- | no manual edit
EN: TINGLE
BEFORE: 酥麻
AFTER: 酥麻
ROW SFW9bbcf9584dc4b13b18e840f1 | L- | EDIT E03-041
EN: GET A FEELING|SO COMPLICATED
BEFORE: 生出感觉|如此复杂
AFTER: 涌上一种|复杂的感觉
### P03-028 | action=apply
原问题：“生出感觉|如此复杂”是拼接英语语序；此SFW独立变体保留含混感，不挪入NSFW内容。
本轮理由：保留complicated的复杂含义，不以难以言说替换；保留竖线结构。
EDIT_IDS ["E03-041"]

## SC1bef76d7b7f0bddd | nsfw | datav/dictionary.json | ui.breeding.Bigbold.needs
ROW CAT:O0718f958638cd7693e8e | L- | no manual edit
EN: HE'S LICKING HIS CHOPS, AND|IS EAGER FOR YOUR ATTENTION.
BEFORE: 他舔着嘴，而且|急切想要你的关注。
AFTER: 他舔着嘴，而且|急切想要你的关注。
ROW CAT:O57a1cbb252bee3e96c63 | L- | no manual edit
EN: HE'S WELL FED FOR NOW, AND|WOULD RATHER BE LEFT ALONE.
BEFORE: 他这会儿吃饱了，|宁可别人别来烦他。
AFTER: 他这会儿吃饱了，|宁可别人别来烦他。
ROW CAT:O6aaec0c528799572e7ee | L- | no manual edit
EN: HE'S WELL FED FOR NOW, BUT|STILL WANTS YOUR ATTENTION.
BEFORE: 他这会儿吃饱了，但|还是想要你的关注。
AFTER: 他这会儿吃饱了，但|还是想要你的关注。
ROW CAT:Oaf7fbce9b03dcffb4ba9 | L- | no manual edit
EN: HE'S LICKING HIS CHOPS, BUT|DOESN'T WANT TO BE PET.
BEFORE: 他舔着嘴，但|不想被抚摸。
AFTER: 他舔着嘴，但|不想被抚摸。
### P03-029 | action=reject
原问题：现译语义成立，可保留。此建议仅让UI更紧凑口语，不属必改；与同组吃饱/饥饿及愿否抚摸状态分开，不合并为新状态。
本轮理由：原译舔嘴和急切关注语义已成立，且原发现明确是可选紧凑化；不作无必要修改。
EDIT_IDS []

## SC1678a02582b6b47e | nsfw | datav/dictionary.json | ui.breeding.Elf.affinity
ROW CAT:O0333653e3caab4b9a180 | L- | no manual edit
EN: THE ELF PRACTICES FENCING,|INVITING YOU TO JOIN. SHE'LL|BEST YOU IN MERE SECONDS.
BEFORE: 精灵在练剑，|邀请你加入。她|几秒就能胜过你。
AFTER: 精灵在练剑，|邀请你加入。她|几秒就能胜过你。
ROW CAT:O1818bba2828106c39166 | L- | EDIT E03-042
EN: THE ELF GAZES UPON YOU WITH|COOL DISDAIN. WHAT ARE YOU|TO A REGAL BEING LIKE HER?
BEFORE: 精灵用冷淡的轻蔑|看着你。对她这样的|高贵存在，你算什么？
AFTER: 精灵冷冷地看着你，|满眼轻蔑。对她这样的|高贵存在，你算什么？
ROW CAT:O8301ced04cbfa4b0ecf3 | L- | no manual edit
EN: THE ELF SINGS A FRIENDSHIP|SONG IN STRANGE SWEET WORDS.|WHAT A WONDERFUL PET!
BEFORE: 精灵用奇怪而甜美的|词唱起友谊之歌。|真是棒极了的宠物！
AFTER: 精灵用奇怪而甜美的|词唱起友谊之歌。|真是棒极了的宠物！
ROW CAT:Of877d5e8cec3116ce70e | L- | no manual edit
EN: THE ELF'S TAIL TWITCHES. SHE|HAS AN ELFISH NAME FOR YOU.|YOU CAN'T PRONOUNCE IT.
BEFORE: 精灵的尾巴抽动。她|给你起了个精灵名字。|你念不出来。
AFTER: 精灵的尾巴抽动。她|给你起了个精灵名字。|你念不出来。
### P03-030 | action=apply
原问题：“用冷淡的轻蔑看着你”不合中文搭配；保留傲慢的反问，不加封建称号。
本轮理由：自然轻蔑搭配；维持三行亲和说明，无新增称号。
EDIT_IDS ["E03-042"]

## SCd19d3654dc2bc722 | nsfw | datav/dictionary.json | ui.breeding.Squeaker.affinity
ROW CAT:O34c1afa2d1033b450203 | L- | EDIT E03-043
EN: THE SQUEAKER PERKS UP AS|YOU ARRIVE. HE SEEMS MORE|RELAXED WITH YOU NOW.
BEFORE: 你一到，吱吱怪|就竖起身子。他现在|跟你在一起更放松了。
AFTER: 你一到，吱吱怪|便来了精神。他现在|似乎跟你更自在了。
ROW CAT:O8698586a853dbc4d581c | L- | EDIT E03-044
EN: THE SQUEAKER EYES YOU|NERVOUSLY FROM THE BACK OF|HIS CAGE.
BEFORE: 吱吱怪紧张地|从后面盯着你。|他的笼子。
AFTER: 吱吱怪在笼子深处，|紧张地|打量着你。
ROW CAT:Od4283c3ccd4870977249 | L- | no manual edit
EN: THE SQUEAKER HAS COBBLED|TOGETHER AN ESCAPE DEVICE|BUT HE HASN'T USED IT...
BEFORE: 吱吱怪拼出了一个|逃脱装置，|但他还没用……
AFTER: 吱吱怪拼出了一个|逃脱装置，|但他还没用……
ROW CAT:Of457667d4b325537b993 | L- | no manual edit
EN: THE SQUEAKER CHITTERS|HAPPILY AS YOU TEND TO HIM.|WHAT A WONDERFUL PET!
BEFORE: 吱吱怪在你照料他时|高兴地吱吱叫。|真是棒极了的宠物！
AFTER: 吱吱怪在你照料他时|高兴地吱吱叫。|真是棒极了的宠物！
### P03-031 | action=apply
原问题：perks up是精神一振，不是竖起身子；后一条把from the back of his cage拆成“从后面……他的笼子”句法崩裂。两条是不同亲密状态，严禁拼成连续发生。
本轮理由：perks up非竖身；seems仍留似乎；后一状态不添缩身动作。
EDIT_IDS ["E03-043", "E03-044"]

## SCdca9ae7e45afa7b9 | sfw | datav/dictionary.json | ui.breeding.Swiper.affinity
ROW SFW55c663bd17549c6c9b846041 | L- | EDIT E03-045
EN: THE SWIPER PURRS POLITELY,|SHEATHING HIS MURDER MITTENS|AT YOUR APPROACH.
BEFORE: 挥爪礼貌地呼噜，|在你走近时收起|他的凶器肉垫。
AFTER: 你一走近，挥爪便|客气地打起呼噜，|收起那双凶爪。
ROW SFW8bb176e14d5c10704039997a | L- | no manual edit
EN: THE SWIPER CURLS HIS TAIL|INTO A QUESTION MARK, AS IF|ASKING YOU 'WHAT NOW?'
BEFORE: 挥爪把尾巴卷成|问号，仿佛在问你|'现在怎样？'
AFTER: 挥爪把尾巴卷成|问号，仿佛在问你|'现在怎样？'
ROW SFWaaedd2aa397476243ee7f3ab | L- | no manual edit
EN: THE SWIPER STUDIOUSLY AVOIDS|YOUR GAZE. YOU MIGHT AS WELL|NOT EXIST AT ALL...
BEFORE: 挥爪刻意避开|你的目光。你简直|像根本不存在……
AFTER: 挥爪刻意避开|你的目光。你简直|像根本不存在……
ROW SFWad204455895f5b10dc757f9e | L- | no manual edit
EN: THE SWIPER GREETS YOU WITH|A LOW, ADORABLE MEOW.|WHAT A WONDERFUL PET!
BEFORE: 挥爪用一声低低的、|可爱的喵迎接你。|真是棒极了的宠物！
AFTER: 挥爪用一声低低的、|可爱的喵迎接你。|真是棒极了的宠物！
### P03-032 | action=apply
原问题：murder mittens是猫爪戏称；爪可收、肉垫不能像刀剑一样入鞘，“凶器肉垫”逐词且形象失真。
本轮理由：murder mittens为凶爪戏称，非肉垫入鞘；沿用当前暂名。
EDIT_IDS ["E03-045"]

## SC82495adafc04ff45 | nsfw | datav/dictionary.json | ui.card.CosmoCardEnelye.desc
ROW CAT:O33d205e8c3d2c6695fbb | L- | no manual edit
EN: High Lady of the| Elves, Enelye is| unmatched in her| magical prowess.| Undaunted by the| 
EN+ recent events on| Tutone, she has | allowed the more| youthful Elves  | to practice com-| 
EN+ bat in the woods
BEFORE: 精灵的|高阶女士|恩莉耶，|魔法造诣|无人能及。|图托恩|近来的变故|没有吓倒她。|她让更年轻的|精灵在林中|练习战斗。

AFTER: 精灵的|高阶女士|恩莉耶，|魔法造诣|无人能及。|图托恩|近来的变故|没有吓倒她。|她让更年轻的|精灵在林中|练习战斗。

ROW CAT:O465fc7ed2d94b0d91e1a | L- | no manual edit
EN: Despite being an| ageless entity, | Enelye is not   | immune to mund- | ane physical    | 
EN+ desires. After a| round of combat | she (like most  | elves) enjoys a | round of mating | 
EN+ if she's found  | her opponent to | be worthy.      |
                |
BEFORE: 尽管是|不老的存在，|恩莉耶|也无法免疫|凡俗的|肉体欲望。|一轮战斗后，|她（和大多数|精灵一样）|若觉得对手|配得上，|就享受一轮|交配。      |
BEFORE+ 
                |

AFTER: 尽管是|不老的存在，|恩莉耶|也无法免疫|凡俗的|肉体欲望。|一轮战斗后，|她（和大多数|精灵一样）|若觉得对手|配得上，|就享受一轮|交配。      |
AFTER+ 
                |

### P03-033 | action=defer
原问题：High Lady在同包明示ELF QUEEN，译“高阶女士”失去身份；“无法免疫欲望”“若觉得对手配得上”拗口。两页建议分别回填，竖线仅示意需排版复核，不承诺字宽通过。
本轮理由：可确认高阶女士及免疫欲望生硬，但卡片完整值含真实换行及留白；未经当前16格字体容器核验不采缩成六行草案，也不擅定High Lady等同正式女王头衔。
EDIT_IDS []

## SC6bee720011b54d59 | nsfw | datav/dictionary.json | ui.data.m_ClassicWerehund
ROW CAT:O7e2208e284fff845e691 | L- | EDIT E03-046
EN: WAN GREAT VICTORY|LEADS TO A RUFFER DEFEAT!
BEFORE: 汪的一场大胜|引向更汪的惨败！
AFTER: 一场汪汪大胜，|竟换来更惨的失败！
### P03-034 | action=apply
原问题：WAN/ruffer借狗叫代one/rougher；当前两次“汪”却漏掉rougher的程度对比。建议仅保留一次犬类双关，使先胜后惨败可懂。
本轮理由：保留犬声趣味与rougher更惨的对比，拒绝无据汪风新词。
EDIT_IDS ["E03-046"]

## SC652fb83a82ba3090 | sfw | vsn/f_AgentFZ3/script.vsn | vsn/f_AgentFZ3/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Female
CONTROL L4 rewind!
ROW SFWebac2ce1577e8920f91a74c9 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
AFTER: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFW4884bd3acd76c6d685febbf5 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放到我的手上。
AFTER: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFWc7b051a15e7cf8ffd7fb68f4 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
AFTER: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L9 cut(0.06): FenfenC01
CONTROL L10 rewind!
ROW SFWfa8bf8e695bc49cdaf9f6edd | L11 | no manual edit
EN: As dark forces descended on all Fenfen, young and old alike,
BEFORE: lang(Fox): 当黑暗势力降临到全体Fenfen——无论老幼——头上时，
AFTER: lang(Fox): 当黑暗势力降临到全体Fenfen——无论老幼——头上时，
ROW SFWdce0ad110584ec03265dce41 | L12 | no manual edit
EN: it truly did seem like all hope was lost.
BEFORE: lang(Fox): 一切希望看起来当真都已破灭。
AFTER: lang(Fox): 一切希望看起来当真都已破灭。
ROW SFW6eac03aba6556c9f77fed55f | L13 | EDIT E03-047
EN: Powerful though the ESPers of our people may have been, violence was unknown to us.
BEFORE: lang(Fox): 我们族中的超能力者纵然或许强大，暴力对我们却全然陌生。
AFTER: lang(Fox): 我们族中的超能力者虽然强大，却从未接触过暴力。
CONTROL L15 cut(0.06): FenfenC02
CONTROL L16 rewind!
ROW SFW7101f4a3e4de1873250ee5df | L17 | no manual edit
EN: Only when pushed to the end of options, when even surrender seemed impossible
BEFORE: lang(Fox): 只有当被逼至绝路，连投降似乎都变得不可能时，
AFTER: lang(Fox): 只有当被逼至绝路，连投降似乎都变得不可能时，
ROW SFWc2b5f43ae93ecb3133222b5d | L18 | no manual edit
EN: did the first of us strike out...
BEFORE: lang(Fox): 我们中才有人第一个出手反抗……
AFTER: lang(Fox): 我们中才有人第一个出手反抗……
CONTROL L20 cut(0.06): FenfenC03
CONTROL L21 rewind!
ROW SFW945b08ede4c4f2cb3d59aa13 | L22 | no manual edit
EN: ...and retaliate!
BEFORE: lang(Fox): ……并予以还击！
AFTER: lang(Fox): ……并予以还击！
ROW SFWce76a404aa5652bf758efd22 | L23 | no manual edit
EN: Psychic abilities once turned only towards a common good
BEFORE: lang(Fox): 曾经只用于共同福祉的心灵能力，
AFTER: lang(Fox): 曾经只用于共同福祉的心灵能力，
ROW SFW75bdb6fc8c3401200beae20c | L24 | no manual edit
EN: would now be turned against those who would try to subjugate us Fenfen!
BEFORE: lang(Fox): 如今要对准那些企图征服我们Fenfen的人！
AFTER: lang(Fox): 如今要对准那些企图征服我们Fenfen的人！
CONTROL L26 cut(0.06): FenfenC04
CONTROL L27 rewind!
ROW SFWed477f818c706c042838e017 | L28 | EDIT E03-048
EN: An arsenal of ESPer abilities became harnessed as weapons of war.
BEFORE: lang(Fox): 超能力者的能力武库被征用为战争的武器。
AFTER: lang(Fox): 超能力者的种种本领，都化作了战争武器。
ROW SFW05f245da42409c522a518cb9 | L29 | no manual edit
EN: Explosive psychic projectiles blasted away foes. 
BEFORE: lang(Fox): 爆裂的灵能弹将敌人轰退。 
AFTER: lang(Fox): 爆裂的灵能弹将敌人轰退。 
ROW SFWc4da9a2dfe23ce50b98a607b | L30 | EDIT E03-049
EN: Punishing waves of telekinetic force prevented advancement of armies.
BEFORE: lang(Fox): 一波波慑人的念动力浪潮，挡住了大军的推进。
AFTER: lang(Fox): 强劲的念动力波阻住了大军前进。
ROW SFW9f0c0a33676025c2a5ae634f | L31 | EDIT E03-050
EN: Some even went so far as to transform their very bodies into tools for combat.
BEFORE: lang(Fox): 有些人甚至走得更远，将自己的身体化作战斗的工具。
AFTER: lang(Fox): 有些人甚至改变自己的身体，把它化作战斗的工具。
CONTROL L34 cut(0.06): FenfenC05
CONTROL L35 rewind!
ROW SFW436f8fdeb7c341a5165b963d | L36 | no manual edit
EN: Ancient beings heard the cries of mental anguish that rang throughout the planet
BEFORE: lang(Fox): 古老的存在们听见了回荡于整颗星球的精神痛呼，
AFTER: lang(Fox): 古老的存在们听见了回荡于整颗星球的精神痛呼，
ROW SFW19fa87c272d83d19be05b8b5 | L37 | EDIT E03-051
EN: Some, like the noble Elves, took up ancient weapons in order to aid us Fenfen...
BEFORE: lang(Fox): 其中一些，比如高贵的Elves，拿起了古老的武器来援助我们Fenfen……
AFTER: lang(Fox): 其中一些，比如高贵的精灵，拿起了古老的武器来援助我们Fenfen……
CONTROL L40 cut(0.06): FenfenC06
CONTROL L41 rewind!
ROW SFW8f7c74bb117521e1df7bc53a | L42 | no manual edit
EN: ...while other ancient beings, from deep within the bowels of the planet
BEFORE: lang(Fox): ……而其他古老的存在，则从这颗星球最深的地底，
AFTER: lang(Fox): ……而其他古老的存在，则从这颗星球最深的地底，
ROW SFW78b848d09d03f4c5a04abd78 | L43 | no manual edit
EN: awoke with a desire for vengeance and domination of their own...
BEFORE: lang(Fox): 带着属于它们自己的复仇与征服欲望苏醒了……
AFTER: lang(Fox): 带着属于它们自己的复仇与征服欲望苏醒了……
CONTROL L46 wait: 0.2
CONTROL L47 fadeout(1.0, 1.0, 4)
### P03-035 | action=apply
原问题：powerful though...may have been同属让步，不是怀疑其强大；“暴力对我们全然陌生”可更自然为没有经历。保留Fox族内讲述而非全知旁白。
本轮理由：though may为让步；不怀疑其强大，不将unknown限定成曾被施暴。前两槽现译成立。
EDIT_IDS ["E03-047"]
### P03-036 | action=apply
原问题：“能力武库被征用”主被动抽象堆叠，“走得更远”机械比喻；按战力升级重建叙述，不补谁强征谁。
本轮理由：去抽象武库被征用，不补强征施事，保留战力升级；灵能弹现译不必改。
EDIT_IDS ["E03-048", "E03-049", "E03-050"]
### P03-037 | action=apply
原问题：同包精灵已有中文，Elves残留破坏连读；Fenfen族名尚待术语裁决，暂保留不私拟。
本轮理由：Elves是已明义精灵，Fenfen未终裁仍留英文。
EDIT_IDS ["E03-051"]

## SC8cfb083ebf53f503 | nsfw | vsn/f_ClassicWerepup/script.vsn | vsn/f_ClassicWerepup/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): ClassicAreaB01A
CONTROL L4 rewind!
ROW CAT:O18e9e3d86666fc41db20 | L5 | no manual edit
EN: Well! You're a feisty little fella, aren't ya? You almost did some damage there
BEFORE: text: 嚯！小家伙还挺有劲啊？刚才那阵又跑又跳，差点就伤到我了！
AFTER: text: 嚯！小家伙还挺有劲啊？刚才那阵又跑又跳，差点就伤到我了！
ROW CAT:O15d4663c749d8662af6f | L6 | no manual edit
EN: with all that running and jumping you were doing!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc12d4ceabc900d526391 | L7 | no manual edit
EN: But who could be angry after seeing your cute lil face, awwwww!
BEFORE: text: 不过看你这可爱的小脸，谁还气得起来啊，哎哟！
AFTER: text: 不过看你这可爱的小脸，谁还气得起来啊，哎哟！
CONTROL L9 fadecut(0.266, 2): ClassicAreaB01B
CONTROL L10 rewind!
ROW CAT:Obf6006c9ce3b7c01168d | L11 | no manual edit
EN: Little pups like you are so perky and energetic! I bet you're almost ready for
BEFORE: text: 你这样的小狗崽真是活泼有劲！我猜你已经快准备好再打一场了，是不是？
AFTER: text: 你这样的小狗崽真是活泼有劲！我猜你已经快准备好再打一场了，是不是？
ROW CAT:O90dd4fe140e1dd95fb60 | L12 | no manual edit
EN: another round of tussling already, aren't you?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O1d2ee2eb9e57b2cceb16 | L13 | no manual edit
EN: That's how I was too, when I graduated from the Cosmobreeder program
BEFORE: text: 我当年从宇宙育种者培训班毕业、年仅22岁就踏上头一次任务时，也是这样……
AFTER: text: 我当年从宇宙育种者培训班毕业、年仅22岁就踏上头一次任务时，也是这样……
ROW CAT:Oebf655298a17570b6028 | L14 | no manual edit
EN: and went on my very first mission at the young age of only 22...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L16 fadecut(0.266, 2): ClassicAreaB01C
CONTROL L17 rewind!
ROW CAT:O663227fa1582e0bc175d | L18 | no manual edit
EN: Back then, I was a clumsy lil bitch, I tell ya. Managed to lose all my gear
BEFORE: text: 告诉你，那时我就是个笨手笨脚的小母狗，还没机会收集数据，装备就弄丢得只剩电击枪了！
AFTER: text: 告诉你，那时我就是个笨手笨脚的小母狗，还没机会收集数据，装备就弄丢得只剩电击枪了！
ROW CAT:Of74f2ece306c4e238a8f | L19 | no manual edit
EN: except for my tazer, before I even had a chance to gather some data!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obdde138a199c3c89e538 | L20 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O7f5ecd01a1b4ad036c3a | L21 | no manual edit
EN: ...completely different from now, when I always manage to keep my jacket on.
BEFORE: text: ……跟现在完全不同，我现在总能保住外套不脱。
AFTER: text: ……跟现在完全不同，我现在总能保住外套不脱。
CONTROL L23 fadecut(0.266, 2): ClassicAreaB01D
CONTROL L24 rewind!
CONTROL L25 sfxcue: ClassicAreaB01D {
CONTROL L26   play [ClassicRockSpawn] at [3, 11]
CONTROL L27 }
ROW CAT:Od68ba2d99a1766deb1ef | L28 | no manual edit
EN: It was a bit of a shock seeing my first space pirate Kobold in person.
BEFORE: text: 头一次亲眼见到科博德太空海盗，真有点吃惊。
AFTER: text: 头一次亲眼见到科博德太空海盗，真有点吃惊。
ROW CAT:O95e2d1d3b3d091126a5a | L29 | no manual edit
EN: They're way more aggressive and nimble in person than the simulations showed
BEFORE: text: 真家伙比模拟里的凶猛、灵活多了，也可能只是肾上腺素飙升，让我有这错觉。
AFTER: text: 真家伙比模拟里的凶猛、灵活多了，也可能只是肾上腺素飙升，让我有这错觉。
ROW CAT:Oa2670e3929a7ebd5634b | L30 | no manual edit
EN: or maybe it was the adren- aline pumping through me that made it seem that way.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2c3d286f2d26a5ff51f7 | L31 | no manual edit
EN: Either way, it didn't take long...
BEFORE: text: 不管怎样，没过多久……
AFTER: text: 不管怎样，没过多久……
CONTROL L33 fadecut(0.266, 2): ClassicAreaB01E
CONTROL L34 rewind!
CONTROL L35 sfxcue: ClassicAreaB01E {
CONTROL L36   play [ClassicYiffaiXSlap1] at [5]
CONTROL L37 }
ROW CAT:Od88f45e5d9dcf189d3b5 | L38 | no manual edit
EN: ...for the Kobold to be pumping through me too!
BEFORE: text: ……科博德也要在我体内猛冲了！
AFTER: text: ……科博德也要在我体内猛冲了！
ROW CAT:O0ac8cbfd43431d1cac57 | L39 | no manual edit
EN: I can't even recall getting disarmed and being pushed up against a wall.
BEFORE: text: 我都不记得自己怎么被缴械、推到墙上的。
AFTER: text: 我都不记得自己怎么被缴械、推到墙上的。
ROW CAT:O13870a899b5f59e3d9b5 | L40 | no manual edit
EN: The details of my very first live data collection are crystal clear though.
BEFORE: text: 但头次实地采集数据的细节，我记得一清二楚。
AFTER: text: 但头次实地采集数据的细节，我记得一清二楚。
ROW CAT:Oa1892581d836433ed548 | L41 | no manual edit
EN: That Kobold's thick tail slapping at the ground every time he thrust in...
BEFORE: text: 那科博德每次插入，粗尾巴都会拍打地面……
AFTER: text: 那科博德每次插入，粗尾巴都会拍打地面……
CONTROL L43 fadecut(0.266, 2): ClassicAreaB01F
CONTROL L44 rewind!
CONTROL L45 sfxcue: ClassicAreaB01F {
CONTROL L46   play [ClassicStalactiteLand] at [6]
CONTROL L47 }
ROW CAT:O8f3437abd6f7010bd925 | L48 | no manual edit
EN: ...while my poor cheek fur got all tussled up from being pushed into the wall!
BEFORE: text: ……我可怜的脸颊毛被顶在墙上，蹭得乱七八糟！
AFTER: text: ……我可怜的脸颊毛被顶在墙上，蹭得乱七八糟！
ROW CAT:Oc4ff17f95adf1e66b9f2 | L49 | EDIT E03-052
EN: Unlike the training back home, the real fellas don't wait for you to get comfy.
BEFORE: text: 跟家里的训练不同，真家伙可不等你先适应舒服。
AFTER: text: 跟故乡的训练不同，真碰上这些家伙，可没人等你先调整到舒服。
ROW CAT:O6693674df6c88ac16428 | L50 | EDIT E03-053
EN: But! I'm a quick learner and began rocking my body along with the stud.
BEFORE: text: 不过！我学得可快了，立刻就跟着那猛男晃动身子。 
AFTER: text: 不过！我学得快，很快就跟着那猛男的节奏摆动起身子。
CONTROL L52 fadecut(0.266, 2): ClassicAreaB01G
CONTROL L53 rewind!
CONTROL L54 sfxcue: ClassicAreaB01G {
CONTROL L55   play [ClassicYiffaiXSlap2] at [5,12,19,26]
CONTROL L56 }
ROW CAT:Od8b915328c6e81fbfd9d | L57 | no manual edit
EN: The trick is to not resist them when they pull your hips back, you know.
BEFORE: text: 诀窍就是，他们拽你屁股往后时，别反抗，懂吧。
AFTER: text: 诀窍就是，他们拽你屁股往后时，别反抗，懂吧。
ROW CAT:O4eee43c5c8a791ffade4 | L58 | no manual edit
EN: When you give in and start pushing your tail back on each thrust
BEFORE: text: 等你放开自己，每次插入都把屁股往后迎，我发誓他们会自己调角度，让那些凸粒恰好顶中你。
AFTER: text: 等你放开自己，每次插入都把屁股往后迎，我发誓他们会自己调角度，让那些凸粒恰好顶中你。
ROW CAT:O7ff18303365beacbaea1 | L59 | no manual edit
EN: I swear they start to angle themselves so that their nubs meet you juuuust right.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L61 fadecut(0.266, 2): ClassicAreaB01H
CONTROL L62 rewind!
CONTROL L63 sfxcue: ClassicAreaB01H {
CONTROL L64   play [ClassicYiffaiXSlap9] at [1]
CONTROL L65 }
ROW CAT:O5aa3b925e8852716a427 | L66 | no manual edit
EN: Of course, my training kicked in instantly once the data collection began.
BEFORE: text: 当然，一开始采集数据，我受过的训练立刻就派上用场了。
AFTER: text: 当然，一开始采集数据，我受过的训练立刻就派上用场了。
ROW CAT:O7e9c952e4cc25d90bf94 | L67 | no manual edit
EN: Allll the details of the Kobold breeding habits etched themselves in my mind
BEFORE: text: 科博德交配习性的每个细节，都刻进了我脑子：从那根意外尖细的肉棒光滑的下侧，到他们抽插时把我拽过去，爪子挠过的触感……
AFTER: text: 科博德交配习性的每个细节，都刻进了我脑子：从那根意外尖细的肉棒光滑的下侧，到他们抽插时把我拽过去，爪子挠过的触感……
ROW CAT:Oc7424df37734c3d82ee4 | L68 | no manual edit
EN: Everything from the smooth underside of their surprisingly tapered shaft,
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obee9fe147186870b2f15 | L69 | no manual edit
EN: to the way their claws scratched when they pulled me in with their thrusts...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L71 fadecut(0.266, 2): ClassicAreaB01E2
CONTROL L72 rewind!
CONTROL L73 sfxcue: ClassicAreaB01E2 {
CONTROL L74   play [ClassicYiffaiXSlap1] at [5,11]
CONTROL L75 }
ROW CAT:O853dc94cda1d6d23b2c8 | L76 | no manual edit
EN: Not to mention how hot they got me once they started to speed up!
BEFORE: text: 更别提他们一加速，我就欲火焚身了！
AFTER: text: 更别提他们一加速，我就欲火焚身了！
ROW CAT:Of0d0f34aeea30e02f029 | L77 | no manual edit
EN: I didn't even care about my hips getting scratched up while they bred me.
BEFORE: text: 被他们干的时候，我连胯上被抓破都不在乎了。
AFTER: text: 被他们干的时候，我连胯上被抓破都不在乎了。
ROW CAT:O69baa83e48daf378756f | L78 | no manual edit
EN: ...well, alright, that's not true...
BEFORE: text: ……好吧，其实不是那么回事……
AFTER: text: ……好吧，其实不是那么回事……
ROW CAT:Odc776c4e536fd5a5b93e | L79 | no manual edit
EN: ...I actually kinda liked it, heh...
BEFORE: text: ……其实我还挺喜欢的，嘿……
AFTER: text: ……其实我还挺喜欢的，嘿……
CONTROL L81 fadecut(0.266, 2): ClassicAreaB01X1
CONTROL L82 rewind!
CONTROL L83 sfxcue: ClassicAreaB01X1 {
CONTROL L84   play [ClassicYiffaiXSlap7] at [2]
CONTROL L85 }
ROW CAT:Oc8c1ecea6821ce60c0b6 | L86 | no manual edit
EN: After a certain point I didn't even have to do any work, the boy kept getting
BEFORE: text: 后来我根本不用费力，那小子越来越凶，到最后干脆随心所欲地摆布我！
AFTER: text: 后来我根本不用费力，那小子越来越凶，到最后干脆随心所欲地摆布我！
ROW CAT:Ocb2eb6f8c4cd07aa03a6 | L87 | no manual edit
EN: more and more aggressive until he was just boyhandling me as he wanted!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6c0314e0c477858f8c51 | L88 | no manual edit
EN: With this kind of data to focus on though, I had nooooo problems with that.
BEFORE: text: 不过，有这种数据可专心研究，我完全没意见。
AFTER: text: 不过，有这种数据可专心研究，我完全没意见。
CONTROL L90 fadecut(0.266, 2): ClassicAreaB01G2
CONTROL L91 rewind!
CONTROL L92 sfxcue: ClassicAreaB01G2 {
CONTROL L93   play [ClassicYiffaiXSlap2] at [5,12]
CONTROL L94 }
ROW CAT:O0d6a53cb05c0a0fe9a35 | L95 | no manual edit
EN: Bracing myself against the wall was the best I could do while he rutted me
BEFORE: text: 他狠狠干我时，我能做的就只有撑住墙壁，免得被四处淌落的体液滑倒。
AFTER: text: 他狠狠干我时，我能做的就只有撑住墙壁，免得被四处淌落的体液滑倒。
ROW CAT:O6301de0602c5bc1b3870 | L96 | no manual edit
EN: making sure I didn't slip from all the juices that were spilling about.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O05347bdb7d500c761a9e | L97 | no manual edit
EN: One detail that the training material at the academy never fully replicated
BEFORE: text: 学院的训练器材，有个细节一直没能完全模拟出来，就是这些家伙快射时，鸡巴能变得多滑！
AFTER: text: 学院的训练器材，有个细节一直没能完全模拟出来，就是这些家伙快射时，鸡巴能变得多滑！
ROW CAT:O750aa4d441ea14aa2740 | L98 | no manual edit
EN: was just how slick the boys got when they were getting close!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L100 fadecut(0.266, 2): ClassicAreaB01X2
CONTROL L101 rewind!
CONTROL L102 sfxcue: ClassicAreaB01X2 {
CONTROL L103   play [ClassicYiffaiXSlap7] at [1]
CONTROL L104 }
ROW CAT:O94e76523300f202abc64 | L105 | no manual edit
EN: And I knew he was close since his thrusts were not only faster, but shallower
BEFORE: text: 我知道他快了，因为他不光插得更快，也插得更浅，总不让那些凸粒全滑出来，一个劲地挑逗我里面，但我知道，他马上就要……
AFTER: text: 我知道他快了，因为他不光插得更快，也插得更浅，总不让那些凸粒全滑出来，一个劲地挑逗我里面，但我知道，他马上就要……
ROW CAT:Of109f85d970a9c234f75 | L106 | no manual edit
EN: he just kept teasing my insides by never letting all his nubs slip out
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O8b6e542aca06d7a36c10 | L107 | no manual edit
EN: but I knew he was just about to...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oce4c92243cbcd875ace2 | L108 | no manual edit
EN: ...!
BEFORE: text: ……！
AFTER: text: ……！
CONTROL L110 sync!
CONTROL L111 queue: ClassicAreaB01X3
CONTROL L112 sfxcue: ClassicAreaB01X3 {
CONTROL L113   play [ClassicYiffaiXSlap7] at [1,8]
CONTROL L114   play [ClassicYiffaiXShoot1] at [4,12,16,20]
CONTROL L115   play [ClassicYiffaiXShoot2] at [26]
CONTROL L116 }
CONTROL L118 sync!
CONTROL L119 queue: ClassicAreaB01X4
CONTROL L120 sfxcue: ClassicAreaB01X4 {
CONTROL L121   play [ClassicYiffaiXShoot2] at [4]
CONTROL L122 }
ROW CAT:Of21bf870386872add51c | L123 | no manual edit
EN: Mmmh, cum inside of me <3
BEFORE: text: 嗯唔，射进我里面 <3
AFTER: text: 嗯唔，射进我里面 <3
ROW CAT:O1fce3feb9f6383628fbc | L124 | no manual edit
EN: It felt like he kept on squirting forever as he held my hips still
BEFORE: text: 他按住我的胯，仿佛永远也射不完，把他的一部分留在我体内，精液满得都溢出来了。
AFTER: text: 他按住我的胯，仿佛永远也射不完，把他的一部分留在我体内，精液满得都溢出来了。
ROW CAT:Obb9c5e4406f7c1140a8f | L125 | no manual edit
EN: just leaving part of himself in me while his semen overflowed my insides.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L127 fadecut(0.266, 2): ClassicAreaB01K
CONTROL L128 rewind!
CONTROL L129 sfxcue: ClassicAreaB01K {
CONTROL L130   play [ClassicYiffaiXTwitch2] at [5,15]
CONTROL L131 }
ROW CAT:Oc84cda126153449523dc | L132 | no manual edit
EN: After some time he finally let go and went off on his merry lizard way
BEFORE: text: 过了一阵，那蜥蜴总算松开我，心满意足地走了，这时我才双腿一软，只好先歇一会儿。
AFTER: text: 过了一阵，那蜥蜴总算松开我，心满意足地走了，这时我才双腿一软，只好先歇一会儿。
ROW CAT:Od82eedfd2a424dec3176 | L133 | no manual edit
EN: and that's when my legs gave out and I had to rest a moment.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L135 fadecut(0.266, 2): ClassicAreaB01J
CONTROL L136 rewind!
CONTROL L137 sfxcue: ClassicAreaB01J {
CONTROL L138   play [ClassicYiffaiXTwitch1] at [7]
CONTROL L139 }
ROW CAT:O32691dd2b0473bf9e6e0 | L140 | no manual edit
EN: Just like you, lil pupper, I was ready and rearin' to go after only a minute.
BEFORE: text: 跟你一样，小狗狗，我只歇了一分钟，就又活蹦乱跳了。
AFTER: text: 跟你一样，小狗狗，我只歇了一分钟，就又活蹦乱跳了。
ROW CAT:O369b1232b257fd39c121 | L141 | no manual edit
EN: With a new healthy glow on my cheeks, I toweled off and enjoyed a nice drink
BEFORE: text: 脸颊又泛起健康红晕，我擦干身子，美美喝了一杯，地板还没干，就出发去找下一个研究对象了！
AFTER: text: 脸颊又泛起健康红晕，我擦干身子，美美喝了一杯，地板还没干，就出发去找下一个研究对象了！
ROW CAT:O82cf460331481f1a0e9a | L142 | no manual edit
EN: and was off to find my next subject before the floor had even dried!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L144 fadecut(0.266, 2): ClassicAreaB01A
CONTROL L145 rewind!
ROW CAT:O454bde00c075bb3f21cf | L146 | no manual edit
EN: ...you don't understand much of all this adult nonsense, do ya?
BEFORE: text: ……这些大人的乱七八糟，你还不太懂吧？
AFTER: text: ……这些大人的乱七八糟，你还不太懂吧？
ROW CAT:O2a1ce8dd77078b6f7dea | L147 | no manual edit
EN: All you really want to do is run around and play, I bet.
BEFORE: text: 我猜你其实只想四处跑着玩。  
AFTER: text: 我猜你其实只想四处跑着玩。  
ROW CAT:Obb1b89adec7c2df10a66 | L148 | no manual edit
EN: Just not the icky kind of playing us Cosmobreeders do.
BEFORE: text: 只是不是我们宇宙育种者那种恶心的玩法。
AFTER: text: 只是不是我们宇宙育种者那种恶心的玩法。
CONTROL L150 fadecut(0.266, 2): ClassicAreaB01L
CONTROL L151 rewind!
ROW CAT:O8895e8cbb1babe889e2f | L152 | no manual edit
EN: You've been a good pup and listened to all my rambling, so how about this:
BEFORE: text: 乖狗狗，听我唠叨了这么久，不如这样吧：
AFTER: text: 乖狗狗，听我唠叨了这么久，不如这样吧：
ROW CAT:O3c7e2ed98a17bbfd5b20 | L153 | no manual edit
EN: I'll let you go off on your way, and if you remember me when you get older
BEFORE: text: 我放你走，等你长大些，要是还记得我，就打给PPP，说找伊法妮，好吗？
AFTER: text: 我放你走，等你长大些，要是还记得我，就打给PPP，说找伊法妮，好吗？
ROW CAT:O73e306970e1e5283b9fa | L154 | no manual edit
EN: just call up the PPP and ask for Yiffany, alright?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa32ee6a7c36bfc8dec63 | L155 | no manual edit
EN: I'm sure you'll grow up to be one real handsome fella <3
BEFORE: text: 我敢说，你长大后一定是个大帅哥<3
AFTER: text: 我敢说，你长大后一定是个大帅哥<3
CONTROL L157 fadecut(0.266, 2): ClassicAreaB01M
CONTROL L158 rewind!
CONTROL L159 sfxcue: ClassicAreaB01M {
CONTROL L160   play [BlockBreak] at [4,10]
CONTROL L161 }
ROW CAT:O7e84e8128b4c69365cfa | L162 | no manual edit
EN: Woah, hey now! Why'd you run over there and start digging away?
BEFORE: text: 哎，等等！你怎么跑到那边刨起土来了？
AFTER: text: 哎，等等！你怎么跑到那边刨起土来了？
ROW CAT:O4c10ca3d13458eec520c | L163 | no manual edit
EN: I'm not out to steal any of your buried bones, I swear!
BEFORE: text: 我保证，不会偷你埋的骨头！
AFTER: text: 我保证，不会偷你埋的骨头！
ROW CAT:Od0d46f9c729a962ddb78 | L164 | no manual edit
EN: If you're not careful, you might uncover some dangerous wires or weapons or...
BEFORE: text: 不小心的话，可能挖到危险的电线、武器，或是……
AFTER: text: 不小心的话，可能挖到危险的电线、武器，或是……
CONTROL L166 fadecut(0.266, 2): ClassicAreaB01N
CONTROL L167 rewind!
ROW CAT:O73f937415b645a0484e6 | L168 | no manual edit
EN: ...or a keycard for this area! Wow! Area you really giving this to me?!?
BEFORE: text: ……或者这片区域的门卡！哇！真要送给我？！？
AFTER: text: ……或者这片区域的门卡！哇！真要送给我？！？
ROW CAT:O2076a1491514a1f86278 | L169 | no manual edit
EN: I was just wondering where I was gonna find one of these for this place!
BEFORE: text: 我刚还在想，上哪找张这地方的门卡呢！
AFTER: text: 我刚还在想，上哪找张这地方的门卡呢！
CONTROL L171 fadecut(0.266, 2): Black
CONTROL L172 rewind!
ROW CAT:O1d9c146b5aadbfb7475c | L173 | no manual edit
EN: With this new keycard, I should be able to make my way deeper into the area
BEFORE: text: 有这张新门卡，我就能深入这片区域了，所以再次谢啦，小狗狗！欠你个人情！
AFTER: text: 有这张新门卡，我就能深入这片区域了，所以再次谢啦，小狗狗！欠你个人情！
ROW CAT:O5065508b1dbaa12295cd | L174 | no manual edit
EN: so thanks again pupper! I owe you one!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L176 fadeout(1.0, 1.0, 4)
### P03-038 | action=apply
原问题：“家里的训练”把back home误缩为私人家庭，“先适应舒服”不合中文；保留训练与实地之别，不自动定学校/家庭地点。
本轮理由：back home不锁定私人家庭，保留训练地点相对故乡；两槽不合并。
EDIT_IDS ["E03-052", "E03-053"]

## SCf1e352091c207f10 | nsfw | vsn/m_AgentM04/script.vsn | vsn/m_AgentM04/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L3 snap: AreaAMale02A
CONTROL L4 rewind!
ROW CAT:O8c9180a5c85ca65f5d39 | L5 | no manual edit
EN: Ahh! Sorry lad! I don't know what came over me there!
BEFORE: text: 啊！抱歉，小伙子！我也不知道刚才怎么鬼迷心窍了！ 
AFTER: text: 啊！抱歉，小伙子！我也不知道刚才怎么鬼迷心窍了！ 
ROW CAT:Of59c439236ca6381cf94 | L6 | no manual edit
EN: ...Or what came over my tazer, for that matter...
BEFORE: text: ……或者该问，我的电击枪又是怎么了……
AFTER: text: ……或者该问，我的电击枪又是怎么了……
ROW CAT:O34595bdb5a13b322828b | L7 | no manual edit
EN: ...wait no that was me...
BEFORE: text: ……等等，不对，那是我……
AFTER: text: ……等等，不对，那是我……
ROW CAT:O155cc4ba4f0eb0ede061 | L8 | no manual edit
EN: Let's start at the beginning, shall we?
BEFORE: text: 咱们从头说起，好吗？
AFTER: text: 咱们从头说起，好吗？
CONTROL L10 cut(0.06): AreaAMale02B
CONTROL L11 rewind!
ROW CAT:O48edb39c13f2ea6f5ffa | L12 | no manual edit
EN: A shame you had to see me like that, but it's not really my fault.
BEFORE: text: 可惜让你看见我那副样子，可这真不是我的错。
AFTER: text: 可惜让你看见我那副样子，可这真不是我的错。
ROW CAT:Oa2cd57135fc44f946e46 | L13 | no manual edit
EN: It all began when I stumbled upon a group of Dwarves in the midst of scouting.
BEFORE: text: 一切都始于侦察时，我偶遇了一群矮人。
AFTER: text: 一切都始于侦察时，我偶遇了一群矮人。
ROW CAT:O55a7b36ff988ca787714 | L14 | no manual edit
EN: I was too engrossed in mapping out this large mine area that they call Ayskammr
BEFORE: text: 我太专心绘制那片叫艾斯卡姆的大矿区地图了，所以壮汉们突然撕扯我的制服，让我措手不及！
AFTER: text: 我太专心绘制那片叫艾斯卡姆的大矿区地图了，所以壮汉们突然撕扯我的制服，让我措手不及！
ROW CAT:O156b7a635b65486d3b53 | L15 | no manual edit
EN: so I was caught off guard as the burly boys started to tear at my uniform!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L17 cut(0.06): AreaAMale02C
CONTROL L18 rewind!
ROW CAT:O63afc322520f4e19b369 | L19 | no manual edit
EN: I probably don't have to explain it, but I of course held back while fighting
BEFORE: text: 这大概不用解释，打斗时我当然手下留情了。我壮得如此惊人，当然担心伤着那些可怜的矮人。他们显然对练肌肉也只是稍有兴趣，但可惜，他们跟我根本没法比。
AFTER: text: 这大概不用解释，打斗时我当然手下留情了。我壮得如此惊人，当然担心伤着那些可怜的矮人。他们显然对练肌肉也只是稍有兴趣，但可惜，他们跟我根本没法比。
ROW CAT:Oc7956838c9af742dcfb2 | L20 | no manual edit
EN: being as prodigiously buff as I am, I worried about hurting the poor Dwarves
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7e58216feb0ebfff64c6 | L21 | no manual edit
EN: they clearly had taken a passing interest in muscular development, but alas
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obed49bf6e0e80f6e46d0 | L22 | no manual edit
EN: there was just no comparison between us.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O07d7803f6c239ad1b344 | L23 | no manual edit
EN: While holding back, one of the boys quite rudely grabbed my tail. Scandalous!
BEFORE: text: 我正手下留情，一个家伙却无礼地抓住我的尾巴。太不像话！
AFTER: text: 我正手下留情，一个家伙却无礼地抓住我的尾巴。太不像话！
CONTROL L25 cut(0.06): AreaAMale02D
CONTROL L26 rewind!
ROW CAT:O9d0760fc16df25928b41 | L27 | no manual edit
EN: Such rudeness was no way to repay the kindness that I showed them. Nosirree.
BEFORE: text: 我好心待他们，他们却这么无礼，哪有这种道理！
AFTER: text: 我好心待他们，他们却这么无礼，哪有这种道理！
ROW CAT:Oa1f2426f4091adb0d5b9 | L28 | no manual edit
EN: It was enough to make a man consider teaching the brash lad a /proper/ lesson.
BEFORE: text: 真让人想给那冒失小子一个/像样/的教训。
AFTER: text: 真让人想给那冒失小子一个/像样/的教训。
ROW CAT:O2d3ed9707eea95dfa8ba | L29 | no manual edit
EN: As I considered a fitting punishment, the Dwarf seemed inclined to escalate things
BEFORE: text: 我正琢磨该怎么惩罚，那矮人似乎还想得寸进尺，也就是那时，我决定认真起来。
AFTER: text: 我正琢磨该怎么惩罚，那矮人似乎还想得寸进尺，也就是那时，我决定认真起来。
ROW CAT:O41a384ff32b5fccb84c7 | L30 | no manual edit
EN: and it was at that point that I decided to take things seriously.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L32 cut(0.06): AreaAMale02E
CONTROL L33 rewind!
ROW CAT:O67dfb289ebb02fc4375a | L34 | no manual edit
EN: Treating me like I was a common boylass for them to enjoy, such nerve.
BEFORE: text: 竟把我当成随便给他们玩弄的男婊子，真是放肆。
AFTER: text: 竟把我当成随便给他们玩弄的男婊子，真是放肆。
ROW CAT:Oe947d2a31817e4963a47 | L35 | no manual edit
EN: In a burst of fairness I tried to warn the crudes that they were about to be
BEFORE: text: 出于公平，我还好心警告那群粗人，接下来他们就要承受我使出全力的一击。
AFTER: text: 出于公平，我还好心警告那群粗人，接下来他们就要承受我使出全力的一击。
ROW CAT:O3d8950ccd17a268d1a4d | L36 | no manual edit
EN: on the receiving end of my full power.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ocd5ab7b73d16f7ae590d | L37 | no manual edit
EN: The poor kids didn't know what they were bringing on themselves...
BEFORE: text: 那帮可怜的小子，根本不知自己惹上了什么……
AFTER: text: 那帮可怜的小子，根本不知自己惹上了什么……
CONTROL L39 cut(0.06): AreaAMale02F
CONTROL L40 rewind!
ROW CAT:O826e37513f2e5c6d6c38 | L41 | no manual edit
EN: Luckily for the brats, an interloper came along before I showed them whatfor!
BEFORE: text: 算那帮崽子走运，我正要教训他们，就来了个搅局的！
AFTER: text: 算那帮崽子走运，我正要教训他们，就来了个搅局的！
ROW CAT:O009519e2ee18d74caaca | L42 | no manual edit
EN: I unclenched my... fist... and breathed a sigh of relief.
BEFORE: text: 我松开紧握的……拳头……长舒了一口气。
AFTER: text: 我松开紧握的……拳头……长舒了一口气。
ROW CAT:Od44b8626c0255fb88c3d | L43 | no manual edit
EN: A gentleman such as I hates to resort to violence, as should be apparent.
BEFORE: text: 像我这样的绅士，显然最不愿诉诸暴力。
AFTER: text: 像我这样的绅士，显然最不愿诉诸暴力。
CONTROL L45 cut(0.06): AreaAMale02G
CONTROL L46 rewind!
ROW CAT:Obaa241aa92e487c94c4f | L47 | no manual edit
EN: It was then that the youngsters decided to hightail out of the vicinity
BEFORE: text: 看清自己面对的是什么后，那帮小子都吓破了胆，决定夹着尾巴逃离此地。
AFTER: text: 看清自己面对的是什么后，那帮小子都吓破了胆，决定夹着尾巴逃离此地。
ROW CAT:O3c7438246d3fda547760 | L48 | no manual edit
EN: being overcome with coward- ice once they realized what they were up against.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O67ac61baef2969b46a52 | L49 | no manual edit
EN: I gave them a word or two of advice while they retreated, for good measure.
BEFORE: text: 他们撤退时，我还好心补了几句忠告。
AFTER: text: 他们撤退时，我还好心补了几句忠告。
CONTROL L51 cut(0.06): Black
CONTROL L52 rewind! 
ROW CAT:O1caf7afab764edd5020a | L53 | no manual edit
EN: Now this is where things start to get a bit hazy. Uncharacteristically so...
BEFORE: text: 从这儿起，记忆就有点模糊了。这可不像我平时的记性……
AFTER: text: 从这儿起，记忆就有点模糊了。这可不像我平时的记性……
ROW CAT:Od3f23f6b049f0ab02d7b | L54 | no manual edit
EN: I turned to introduce myself to the fella that had chanced upon the scene
BEFORE: text: 我转身向那个碰巧路过的家伙自我介绍，然后……我就记不太清了……
AFTER: text: 我转身向那个碰巧路过的家伙自我介绍，然后……我就记不太清了……
ROW CAT:O407e697bbd8dba3d4feb | L55 | no manual edit
EN: and then... I can't recall much...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc827b8fa53847e6d87e9 | L56 | no manual edit
EN: ...some mesmerizing light... ...warm and... grabby...?
BEFORE: text: ……某种迷人的光……暖暖的……还会乱摸……？
AFTER: text: ……某种迷人的光……暖暖的……还会乱摸……？
CONTROL L58 cut(0.06): AreaAMale02H
CONTROL L59 rewind!
ROW CAT:O0d3c2740c0cfcfbf0c0d | L60 | no manual edit
EN: Yes that's right, I was just about to warn the fella to leave the fighting to me
BEFORE: text: 对，没错，我正要叫那家伙把战斗交给我，可我记得自己好像被……几只幽灵手抓住了？
AFTER: text: 对，没错，我正要叫那家伙把战斗交给我，可我记得自己好像被……几只幽灵手抓住了？
ROW CAT:O38b18924a65cb2573784 | L61 | no manual edit
EN: but I think I was in the clutches of... some ghostly hands?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O944b89c8813c207c0817 | L62 | no manual edit
EN: No, that can't be right. I think there was some weapon that he may have aimed at me
BEFORE: text: 不，不可能。我想他或许拿某种武器对准了我，当然，也不是说有什么武器是我应付不了的。
AFTER: text: 不，不可能。我想他或许拿某种武器对准了我，当然，也不是说有什么武器是我应付不了的。
ROW CAT:Oa66cda4c4c90a6ed9e3b | L63 | no manual edit
EN: not that there's no weapon I can't handle, of course.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L65 cut(0.06): AreaAMale02I
CONTROL L66 rewind!
ROW CAT:Oad80f00d07b618f57ae5 | L67 | EDIT E03-054
EN: Right, of course, that must have been it. The cad sudd- enly engaged in shenanigans
BEFORE: text: 对，没错，肯定是这样。那无赖突、突然耍起了花招，逼得我一遍遍把他打退！
AFTER: text: 对，没错，肯定是这样。那无赖突然耍起花招，逼得我只好一遍遍“还手”！
ROW CAT:Od327401b9acce5d13ba7 | L68 | no manual edit
EN: and I was forced to beat him off repeatedly!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4d08b7392d3679af8557 | L69 | no manual edit
EN: If memory serves me correct, I was doing such a good job at defending myself
BEFORE: text: 没记错的话，我的自卫实在太出色，连那位大人都夸我是个乖孩子。真是光荣时刻！
AFTER: text: 没记错的话，我的自卫实在太出色，连那位大人都夸我是个乖孩子。真是光荣时刻！
ROW CAT:O310441d8d2f27937beae | L70 | no manual edit
EN: that his lordship considered me to be a very good boy. A proud hour!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L72 cut(0.06): AreaAMale02J
CONTROL L73 rewind!
ROW CAT:O4175b26ebed929519053 | L74 | no manual edit
EN: Hold on, no... what? Why would I be a good boy...
BEFORE: text: 等等，不……什么？我怎么会是乖孩子……
AFTER: text: 等等，不……什么？我怎么会是乖孩子……
ROW CAT:O126165e01946807d86b0 | L75 | no manual edit
EN: why would those words fill me with glee, even now...
BEFORE: text: 为什么就算现在，听到这话还是会满心欢喜……
AFTER: text: 为什么就算现在，听到这话还是会满心欢喜……
ROW CAT:O2c4af6c2e52ea85a263e | L76 | no manual edit
EN: Disregard whatever nonsense was recorded then, clearly it's unreliable.
BEFORE: text: 那时候录下的胡话别当真，显然不可靠。
AFTER: text: 那时候录下的胡话别当真，显然不可靠。
CONTROL L78 cut(0.06): AreaAMale02K
CONTROL L79 rewind!
ROW CAT:O7a54eedc2c9335c6e0d2 | L80 | no manual edit
EN: The important thing is that when you found me, I had been left alone in this cell
BEFORE: text: 重点是，你找到我时，我已被独自丢在这间牢房里，除了那把没电的电击枪，什么消遣也没有，只有那挥不去的渴望，想再被夸一句乖孩子。
AFTER: text: 重点是，你找到我时，我已被独自丢在这间牢房里，除了那把没电的电击枪，什么消遣也没有，只有那挥不去的渴望，想再被夸一句乖孩子。
ROW CAT:O3928e293e543ee2d3e9e | L81 | no manual edit
EN: with naught to entertain myself with but my de-energized tazer
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O73e2514db670464f2d07 | L82 | no manual edit
EN: and a lingering desire to be called a good boy once more.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L84 cut(0.06): Black
CONTROL L85 rewind!
ROW CAT:Oa06b818257839a1d0fb4 | L86 | no manual edit
EN: Thankfully, a good bop on the snout returned me to my rightful state of mind!
BEFORE: text: 幸好鼻头挨了一记，我就彻底清醒了！
AFTER: text: 幸好鼻头挨了一记，我就彻底清醒了！
ROW CAT:Oc057c47b03ed955b0c4a | L87 | EDIT E03-055
EN: If you find any map data disks out in these mines, there's no need to thank me.
BEFORE: text: 要在矿井里找到地图数据盘，不用谢我。
AFTER: text: 要是你在矿井里找到地图数据盘，不用谢我。
ROW CAT:Ocdbec35343720fc11098 | L88 | EDIT E03-056
EN: It's all in a day's work for this...
BEFORE: text: 对我这个……来说，都只是日常工作…… 
AFTER: text: 对我这个……来说，都只是分内的工作……
ROW CAT:O7f9ae1cc96f8492f1c10 | L89 | no manual edit
EN: good...
BEFORE: text: 乖…… 
AFTER: text: 乖…… 
ROW CAT:Oa27ea73cca8fc7422640 | L90 | no manual edit
EN: boy...?
BEFORE: text: 孩子……？
AFTER: text: 孩子……？
CONTROL L92 fadeout(1.0, 1.0, 4)
### P03-039 | action=apply
原问题：sudd-enly只是排版断词，不该添加结巴。beat him off是自卫/手淫双关，当前只打退削弱嘴硬性回忆，建议引号留歧义而不补画面动作。
本轮理由：删除排版断词造成的虚构结巴；还手引号提示beat off的双关，不补画面动作；后段自夸原样。
EDIT_IDS ["E03-054"]
### P03-040 | action=apply
原问题：If you find条件被“要在……找到”写成目的/指令；后接日常工作应承接“那些盘是我的成果”的自夸，不改成叫玩家特意去找。末尾good boy仍保留不安停顿。
本轮理由：if恢复条件，不把后续乖孩子提前搬入本槽；末两槽停顿及问号原样。
EDIT_IDS ["E03-055", "E03-056"]

## SC4ae7f053796af024 | nsfw | vsn/m_AgentMZ1/script.vsn | vsn/m_AgentMZ1/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntroMale
CONTROL L4 rewind!
ROW CAT:Ob3561ecd5daca9db50ca | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
AFTER: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
ROW CAT:O0472e1e7889a2e6fead6 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放在我的手上。
AFTER: lang(Fox): 现在，把你的双手放在我的手上。
ROW CAT:Odf81a6c9c82a44fc665a | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
AFTER: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
CONTROL L10 cut(0.06): Black
CONTROL L11 rewind!
ROW CAT:Od11adb079d5b47a966b1 | L12 | no manual edit
EN: ...I can see...!
BEFORE: text: ……我能看见了……！
AFTER: text: ……我能看见了……！
CONTROL L14 cut(0.06): FenfenA01
CONTROL L15 rewind!
ROW CAT:O5e717ded0cdff7d519a6 | L16 | no manual edit
EN: We, the Fenfen, have lived for eons on this planet that you know as "Tutone".
BEFORE: lang(Fox): 我们Fenfen，在你们称作“图托恩”的星球上已生活了无数岁月。
AFTER: lang(Fox): 我们Fenfen，在你们称作“图托恩”的星球上已生活了无数岁月。
ROW CAT:O3f7c00f2c42b39b682a6 | L17 | no manual edit
EN: Having eschewed the sort of technological advances that your culture thrives on
BEFORE: lang(Fox): 摒弃了你们的文化赖以繁荣的那类技术进步之后，
AFTER: lang(Fox): 摒弃了你们的文化赖以繁荣的那类技术进步之后，
ROW CAT:O144d0ffd207d3f3be671 | L18 | no manual edit
EN: we have lived simple, satisfying lives in harmony with the planet itself.
BEFORE: lang(Fox): 我们与星球本身和谐共处，过着简单而满足的生活。
AFTER: lang(Fox): 我们与星球本身和谐共处，过着简单而满足的生活。
CONTROL L20 cut(0.06): FenfenA02
CONTROL L21 rewind!
ROW CAT:Oe4d2ffd0bb60a3773ea7 | L22 | no manual edit
EN: Quiet and modest are the best ways to describe us Fenfen.
BEFORE: lang(Fox): 安静谦逊，最适合形容我们Fenfen。
AFTER: lang(Fox): 安静谦逊，最适合形容我们Fenfen。
ROW CAT:Of6a21486357ccd694334 | L23 | no manual edit
EN: All major quarrels were sorted out by a council of the wisest ESPers we had.
BEFORE: lang(Fox): 所有重大争端，都由我们最睿智的超能力者组成的议会裁决。
AFTER: lang(Fox): 所有重大争端，都由我们最睿智的超能力者组成的议会裁决。
ROW CAT:Oadd5dcb043a4d98e0531 | L24 | no manual edit
EN: With our highly attuned senses and powers, we were able to find solutions that
BEFORE: lang(Fox): 凭借敏锐的感官与力量，我们总能找到办法， 
AFTER: lang(Fox): 凭借敏锐的感官与力量，我们总能找到办法， 
ROW CAT:O965e5b14da113211f062 | L25 | no manual edit
EN: benefitted all of society at once.
BEFORE: lang(Fox): 能让整个社会一同受益。
AFTER: lang(Fox): 能让整个社会一同受益。
CONTROL L27 cut(0.06): FenfenA03
CONTROL L28 rewind!
ROW CAT:O8e876cf0c5aa4582cd63 | L29 | no manual edit
EN: However, even with our attunement...
BEFORE: lang(Fox): 然而，即便有着这份感应力……
AFTER: lang(Fox): 然而，即便有着这份感应力……
ROW CAT:Oef6ff3f9d0294dd3cb2c | L30 | no manual edit
EN: ...we were not able to sense that amongst us ESPers lay one whose ambitions
BEFORE: lang(Fox): ……我们竟未察觉，超能力者之中藏着一人，其野心
AFTER: lang(Fox): ……我们竟未察觉，超能力者之中藏着一人，其野心
ROW CAT:O28324fa92c85e73b4945 | L31 | no manual edit
EN: would throw the very planet itself into chaos...
BEFORE: lang(Fox): 会令整颗星球陷入混乱……
AFTER: lang(Fox): 会令整颗星球陷入混乱……
ROW CAT:O89ced14a26277c8a1ef6 | L32 | no manual edit
EN: ...
BEFORE: lang(Fox): ……
AFTER: lang(Fox): ……
ROW CAT:O360664088cc170c15424 | L33 | no manual edit
EN: ...her name was Traeh.
BEFORE: lang(Fox): ……她的名字是特蕾。
AFTER: lang(Fox): ……她的名字是特蕾。
CONTROL L35 cut(0.06): FenfenA04
CONTROL L36 rewind!
ROW CAT:O5ff33ddf10d3a4b75acf | L37 | EDIT E03-057
EN: Gifted beyond her years, with an uncanny ability to find solutions others missed
BEFORE: lang(Fox): 天赋远超其年纪，又有着总能找到他人所遗漏之解法的非凡本事，
AFTER: lang(Fox): 她年纪轻轻就天赋过人，总能想到别人想不到的办法，
ROW CAT:O5947c3c9753a4c2024d5 | L38 | EDIT E03-058
EN: the ESPer Traeh seemed like a fine addition to the council.
BEFORE: lang(Fox): 超能力者特蕾，看上去是议会的一位出色新成员。
AFTER: lang(Fox): 超能力者特蕾看上去会是议会的一位得力新成员。
ROW CAT:Occ321125b20fca89feae | L39 | EDIT E03-059
EN: She was readily granted access to the stores of power that we Fenfen kept.
BEFORE: lang(Fox): 她很轻易便获准接触我们Fenfen所封存的力量贮藏。
AFTER: lang(Fox): 她顺利获准接触我们Fenfen储存的力量。
CONTROL L41 snap: FenfenA05
ROW CAT:Of878375ed8d262b42a88 | L42 | no manual edit
EN: Power... that she then proceeded to corrupt.
BEFORE: lang(Fox): 力量……而她随即着手将其腐化。
AFTER: lang(Fox): 力量……而她随即着手将其腐化。
ROW CAT:Oa539c68f9bb4711ab6bf | L43 | no manual edit
EN: Absorbing ancient caches of ESPer power that were left by previous generations
BEFORE: lang(Fox): 吸收了前代遗留下来的古老超能力者力量贮藏之后，
AFTER: lang(Fox): 吸收了前代遗留下来的古老超能力者力量贮藏之后，
ROW CAT:O37d5fc90219f2b1cbf78 | L44 | no manual edit
EN: Traeh was left deeply disfigured, down to her very core.
BEFORE: lang(Fox): 特蕾从外貌到内心，都已扭曲得面目全非。
AFTER: lang(Fox): 特蕾从外貌到内心，都已扭曲得面目全非。
CONTROL L46 cut(0.06): FenfenA06
CONTROL L47 rewind!
ROW CAT:O8519953fa494e8dd2f24 | L48 | no manual edit
EN: Maybe if we, the remaining elder ESPers of the council, reacted faster
BEFORE: lang(Fox): 也许我们议会中剩下的超能力者长老若能更快应对
AFTER: lang(Fox): 也许我们议会中剩下的超能力者长老若能更快应对
ROW CAT:O711a358948f67dfe7f69 | L49 | no manual edit
EN: then we could've prevented the calamity that was about to befall our people.
BEFORE: lang(Fox): 或许就能阻止那场即将降临族人的浩劫。
AFTER: lang(Fox): 或许就能阻止那场即将降临族人的浩劫。
ROW CAT:O60820730ed685809a691 | L50 | no manual edit
EN: Alas, we did not, and that will forever be our greatest failing...
BEFORE: lang(Fox): 可惜我们没有，这永远是我们最大的过失……
AFTER: lang(Fox): 可惜我们没有，这永远是我们最大的过失……
CONTROL L52 cut(0.06): Black
CONTROL L53 rewind!
ROW CAT:Oa0d712ce9f0125fed208 | L54 | no manual edit
EN: Now go, destined hero.
BEFORE: lang(Fox): 去吧，命定的英雄。
AFTER: lang(Fox): 去吧，命定的英雄。
ROW CAT:O828282e786e0f24a123a | L55 | no manual edit
EN: Free my brothers and sisters and restore peace to the land!
BEFORE: lang(Fox): 解救我的兄弟姐妹，让这片土地重归安宁！
AFTER: lang(Fox): 解救我的兄弟姐妹，让这片土地重归安宁！
CONTROL L57 wait: 0.2
CONTROL L58 fadeout(1.0, 1.0, 4)
### P03-041 | action=apply
原问题：“天赋远超其年纪”“力量贮藏”生硬；原文readily是顺利/毫不犹疑，不宜强化“不费力夺得”。因果只体现叙事承接。
本轮理由：保留seemed而非草案怎么看都是；readily不增设夺取，不加明示因此。
EDIT_IDS ["E03-057", "E03-058", "E03-059"]

## SCe240b1877125bd63 | sfw | vsn/m_AgentMZ4/script.vsn | vsn/m_AgentMZ4/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Male
CONTROL L4 rewind!
ROW SFWc6cbb0ea773c2fb4bacad389 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
AFTER: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
ROW SFWa429aaa9ed2884fe23d62160 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放在我的手上。
AFTER: lang(Fox): 现在，把你的双手放在我的手上。
ROW SFW7f21b66c1b380776a669929d | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
AFTER: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
CONTROL L10 cut(0.06): FenfenD01
CONTROL L11 rewind!
ROW SFW74cae508eb4effc519ae6fca | L12 | no manual edit
EN: The great war waged for years between the evil forces of Traeh
BEFORE: lang(Fox): 这场大战持续多年，交战双方是特蕾的邪恶势力
AFTER: lang(Fox): 这场大战持续多年，交战双方是特蕾的邪恶势力
ROW SFW65aa28ef538c847d31da1b55 | L13 | no manual edit
EN: and the formerly peaceful Fenfen that inhabited this land.
BEFORE: lang(Fox): 和这片土地上原本爱好和平的Fenfen。
AFTER: lang(Fox): 和这片土地上原本爱好和平的Fenfen。
ROW SFW5a77bbfeb53138e053807c56 | L14 | no manual edit
EN: It seemed to all that this war might go on forever, with no decisive victories.
BEFORE: lang(Fox): 所有人都觉得，这场战争也许永无休止，谁也无法彻底取胜。
AFTER: lang(Fox): 所有人都觉得，这场战争也许永无休止，谁也无法彻底取胜。
CONTROL L16 cut(0.06): FenfenD02
CONTROL L17 rewind!
ROW SFWda2dd5b02bcb6b0b6dd1f095 | L18 | no manual edit
EN: Without a vital member of the Fenfen council representing a vital force
BEFORE: lang(Fox): 议会失去了一位代表重要力量的 Fenfen 核心成员，
AFTER: lang(Fox): 议会失去了一位代表重要力量的 Fenfen 核心成员，
ROW SFW85bdfbc50638df33c8d53432 | L19 | no manual edit
EN: the remaining councilors were hamstrung.
BEFORE: lang(Fox): 余下的议员便处处受制。
AFTER: lang(Fox): 余下的议员便处处受制。
ROW SFW94eb9f77b59b379685104327 | L20 | no manual edit
EN: The psychic bonds between the members still held, requiring constant vigilance
BEFORE: lang(Fox): 成员之间的灵能联结依然维系着，只是需要时刻保持警觉，
AFTER: lang(Fox): 成员之间的灵能联结依然维系着，只是需要时刻保持警觉，
ROW SFWdd2b5e1b0e070c5ecba1d74f | L21 | no manual edit
EN: to keep dark forces from consuming more ESPers.  
BEFORE: lang(Fox): 以免黑暗力量吞噬更多超能力者。  
AFTER: lang(Fox): 以免黑暗力量吞噬更多超能力者。  
CONTROL L23 cut(0.06): Black
CONTROL L24 rewind!
ROW SFWc37ae1ad48aab6d288cef274 | L25 | no manual edit
EN: ...but then, one day, an opportunity arose...
BEFORE: lang(Fox): ……但有一天，机会终于来了……
AFTER: lang(Fox): ……但有一天，机会终于来了……
CONTROL L27 cut(0.06): FenfenD03
CONTROL L28 rewind!
ROW SFW0c142b5a497db773331a0e1e | L29 | no manual edit
EN: A moment of psychic weakness left Traeh disarmed and distracted for but a moment
BEFORE: lang(Fox): 心灵上的一时虚弱，让特蕾卸下防备、分了神，哪怕只有一瞬，
AFTER: lang(Fox): 心灵上的一时虚弱，让特蕾卸下防备、分了神，哪怕只有一瞬，
ROW SFW3f0dc6d0f59c0b87ec0f3b4f | L30 | no manual edit
EN: and in that moment the remaining members of the council struck!
BEFORE: lang(Fox): 就在那一刻，其余议员出手了！
AFTER: lang(Fox): 就在那一刻，其余议员出手了！
ROW SFW26e60b551278d5aaa880ada8 | L31 | EDIT E03-060
EN: Unable to overcome the psychic disturbance and deal a final blow, 
BEFORE: lang(Fox): 无法克服这股灵能扰动、给出致命一击， 
AFTER: lang(Fox): 议员们无法克服这股灵能扰动，给她致命一击，
ROW SFW57fafbcc5ded09fad32122d8 | L32 | EDIT E03-061
EN: the councilors instead froze Traeh in a crystal prison.
BEFORE: lang(Fox): 议员们转而将特蕾封冻在一座水晶囚牢之中。
AFTER: lang(Fox): 只好改将特蕾封冻在水晶牢笼里。
CONTROL L34 cut(0.06): FenfenD04
CONTROL L35 rewind!
ROW SFW817abda736bb4166386a9297 | L36 | EDIT E03-062
EN: With no fierce leader to guide them, the oppor- tunistic hordes broke apart
BEFORE: lang(Fox): 没有了凶悍首领的指引，那群见风转舵的乌合之众土崩瓦解，
AFTER: lang(Fox): 失去凶悍首领的指挥，那群投机者便四散溃逃，
ROW SFWc1f748d306c7e4c7886b19b9 | L37 | EDIT E03-063
EN: fleeing from the powers of the Fenfen council.
BEFORE: lang(Fox): 仓皇逃离Fenfen议会的力量。
AFTER: lang(Fox): 躲避Fenfen议会的力量。
ROW SFW2500bbe9f5885a583a6ddfcb | L38 | EDIT E03-064
EN: This is not to say that it was a triumphant moment for the Fenfen...
BEFORE: lang(Fox): 这并不是说，对Fenfen而言这是一个凯旋的时刻……
AFTER: lang(Fox): 但这并不意味着Fenfen迎来了凯旋时刻……
CONTROL L40 cut(0.06): FenfenD05
CONTROL L41 rewind!
ROW SFWdd9433262f31100fc341b0bf | L42 | no manual edit
EN: Indeed, heavy prices were paid on both sides of the conflict.
BEFORE: lang(Fox): 确实，冲突双方都付出了惨重代价。
AFTER: lang(Fox): 确实，冲突双方都付出了惨重代价。
ROW SFW4a77f56ab3ae58134483963f | L43 | EDIT E03-065
EN: The planet you landed on is no longer the peaceful home of the Fenfen
BEFORE: lang(Fox): 你降落的星球，已不再是Fenfen的和平家园，
AFTER: lang(Fox): 你降落的这颗星球，已不再是Fenfen宁静的家园，
ROW SFW824ad0523e5ddb5767b698c8 | L44 | EDIT E03-066
EN: but merely a chaotic shadow of its former self.
BEFORE: lang(Fox): 而只是往日模样的一个混沌残影。
AFTER: lang(Fox): 只剩下往日家园支离混乱的影子。
ROW SFW1202507c265fc2a9505ffa9a | L45 | no manual edit
EN: Many Fenfen as of yet are held captive by remnants of the would-be conquerors
BEFORE: lang(Fox): 至今，仍有许多Fenfen被那些妄图征服我们的残党囚禁
AFTER: lang(Fox): 至今，仍有许多Fenfen被那些妄图征服我们的残党囚禁
ROW SFWb720eb72d238ff3f446a08ca | L46 | no manual edit
EN: awaiting the day that a hero will free them...
BEFORE: lang(Fox): 等待着英雄前来解救的那一天……
AFTER: lang(Fox): 等待着英雄前来解救的那一天……
CONTROL L48 wait: 0.2
CONTROL L49 fadeout(1.0, 1.0, 4)
### P03-042 | action=apply
原问题：英文状语前置导致现译无主短段“无法……给出”；完整保留无法击杀而改封禁的行动逻辑，不补具体扰动来源。
本轮理由：明确主语和无法击杀转封禁，freeze意义保留；两个非空事件槽各承意群。
EDIT_IDS ["E03-060", "E03-061"]
### P03-043 | action=apply
原问题：当前“仓皇逃离……的力量”“往日模样的一个混沌残影”英语抽象搭配明显；按溃败—不算凯旋—残破故土的落点重写，控制边仍分别输出。
本轮理由：保留失去领导的溃败、不算凯旋及故土残破；惨重代价原槽成立不动，不跨cut移动。
EDIT_IDS ["E03-062", "E03-063", "E03-064", "E03-065", "E03-066"]

## SCe68f2e03acd6f17b | nsfw | vsn/m_ClassicSqueakerBoss/script.vsn | vsn/m_ClassicSqueakerBoss/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): Asset22A
CONTROL L4 rewind!
ROW CAT:O0b15430051d27c9823e6 | L5 | no manual edit
EN: Now WHY did you have to go and do that, huh?
BEFORE: text: 现在，你干嘛非得去干那种事，嗯？
AFTER: text: 现在，你干嘛非得去干那种事，嗯？
ROW CAT:Oc09b61265d10a8dc61ae | L6 | no manual edit
EN: One of you sorts went and ransacked all my belongings right after I landed
BEFORE: text: 你们这种家伙前脚在我刚落地时把我的所有家当翻了个精光，如今你又想在一对一单挑里把我打倒？
AFTER: text: 你们这种家伙前脚在我刚落地时把我的所有家当翻了个精光，如今你又想在一对一单挑里把我打倒？
ROW CAT:Ob86bf9c51ac943c3ead7 | L7 | no manual edit
EN: and now you're trying to take me down in one-on-one combat?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O671c452929f5604d0458 | L8 | no manual edit
EN: No chance! I've just about had enough of you little bra-
BEFORE: text: 没门！我真是受够了你们这些小混-
AFTER: text: 没门！我真是受够了你们这些小混-
CONTROL L10 snap: Asset22B
CONTROL L11 rewind!
ROW CAT:O7188e11ab7cd06c3e395 | L12 | no manual edit
EN: -hey...
BEFORE: text: -嘿……
AFTER: text: -嘿……
ROW CAT:O1364d8857165c433f58e | L13 | no manual edit
EN: Is that... No way...
BEFORE: text: 那是……不可能吧……
AFTER: text: 那是……不可能吧……
ROW CAT:Obfc9f8da375d35c46fa9 | L14 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O377a9af5891337c01e23 | L15 | no manual edit
EN: ...but YES way!
BEFORE: text: ……可偏偏就是！
AFTER: text: ……可偏偏就是！
CONTROL L17 fadecut(0.266, 2): Asset23
CONTROL L18 rewind!
ROW CAT:O670c59a52e7d88ed0538 | L19 | no manual edit
EN: It's my Cosmohelm! It got all the way over here somehow!
BEFORE: text: 是我的Cosmohelm！它不知怎么一路跑到这边来了！
AFTER: text: 是我的Cosmohelm！它不知怎么一路跑到这边来了！
ROW CAT:O89c349c8e6123e4f43f7 | L20 | no manual edit
EN: This'll be real good to have in case I ever have to go into space or something!
BEFORE: text: 万一哪天我得上太空什么的，这玩意儿可就派上大用场了！
AFTER: text: 万一哪天我得上太空什么的，这玩意儿可就派上大用场了！
ROW CAT:Oaea9196d5c151cdad1dd | L21 | no manual edit
EN: Just need to keep an eye out for the Cosmosuit portion...
BEFORE: text: 只要再留心Cosmosuit那一部分就好...
AFTER: text: 只要再留心Cosmosuit那一部分就好...
ROW CAT:Oe5f0ee057ad8e11e594a | L22 | EDIT E03-067
EN: ...and I'll be able to have a nice proper airtight outfit! Hoorah!
BEFORE: text: ……我就能有一套像样的密封好装备啦！好耶！
AFTER: text: ……我就能凑齐一套像样的气密装备啦！好耶！
CONTROL L24 fadeout(1.0, 1.0, 4)
### P03-044 | action=apply
原问题：Cosmohelm/Cosmosuit未译，装备找回的叙述断裂；现译“密封好装备”搭配不通。词项暂用本包现有宇宙服，最终需统一头盔/星装术语，不全局替换。
本轮理由：仅修密封好装备的搭配；Cosmohelm/Cosmosuit未终裁不强命名，保留尚须另一部分的条件。
EDIT_IDS ["E03-067"]

