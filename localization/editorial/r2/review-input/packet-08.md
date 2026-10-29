# packet-08 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SCec4640a9f4d3aa25 | nsfw | datadf/all.ds | AreaA_Macsen2.Goodbye
CONTROL L467 <AreaA_Macsen2.Goodbye>
ROW CAT:O024daa3301d44fa213d0 | L468 | EDIT E08-001
EN: Good luck with the heat out there!
BEFORE:   * 外面的酷热，祝你好运！
AFTER:   * 外头热得很，祝你一路顺利！
### P08-001 | action=apply
原问题：送客时祝对方应付酷热顺利，现译“外面的酷热，祝你好运”话题悬空，不像商人自然道别。
本轮理由：送客祝福应保留好运之意和室外酷热对象，不把祝愿改成单纯警告。
EDIT_IDS ["E08-001"]

## SCd01d5a6a1d077677 | sfw | datadf/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1710 <AreaH_MacsenBreeding.SpecialFap>
ROW SFW7d0e0bd69cec7fca2500391b | L1711 | EDIT E08-002
EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
BEFORE:   * 既然你已经和那些生物中的一个变得非常亲近了，把这个拿去！
AFTER:   * 既然你已经跟其中一只生物很亲近了，这个给你！
ROW SFWbb67b2b36731c41900aa856f | L1712 | EDIT E08-003
EN: GIVE THEM SOME ATTENTION AND PETS ONE MORE TIME WHILE HOLDING THIS CRYSTAL
BEFORE:   * 拿着这块水晶，再关心它们一次、摸摸它们。
AFTER:   * 拿着这块水晶，再去陪陪它、摸摸它，
ROW SFWd4238c82798f14676f9097e0 | L1713 | EDIT E08-004
EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
BEFORE:   * 并且你也许会感到某种力量流经你……
AFTER:   * 说不定就能感到一股力量流遍全身……
### P08-002 | action=apply
原问题：完整玩法说明应持续指向前句已亲近的那一只；现译“那些生物中的一个变得非常亲近”“并且”有逐字拼接感。保留might，不保证获得力量。
本轮理由：one of和后续them指已亲近的同一只生物；三现有槽分别承载赠礼、持晶抚摸、可能感受力量，保留might。
EDIT_IDS ["E08-002", "E08-003", "E08-004"]

## SCaf4aa1fa18c98fd1 | nsfw | datadf/all.ds | BossuDex.ClassicBlocker
CONTROL L2852 <BossuDex.ClassicBlocker>
ROW CAT:O0e5a41d2c344740f70d0 | L2853 | no manual edit
EN: [OKAY, THAT THING WAS GROSS. WHAT THE HECK WAS IT?]
BEFORE:   Yiffany: [好吧，那东西真恶心。那到底是什么玩意儿？]
AFTER:   Yiffany: [好吧，那东西真恶心。那到底是什么玩意儿？]
ROW CAT:O0c10e334cb4b99352c88 | L2854 | no manual edit
EN: [THAT APPEARS TO HAVE BEEN A BLOCKER.]
BEFORE:   Bossu: [那看来是一只Blocker。]
AFTER:   Bossu: [那看来是一只Blocker。]
ROW CAT:O97f148a87ec70e4b87e0 | L2855 | no manual edit
EN: [IT'S A STRANGE ANOMALY THAT EMERGES FROM RUINS]
BEFORE:   Bossu: [它是一种会从废墟中现身的奇异异常体，而且看来对大多数物理攻击都免疫。]
AFTER:   Bossu: [它是一种会从废墟中现身的奇异异常体，而且看来对大多数物理攻击都免疫。]
ROW CAT:Oc793f9f472b72c0546c2 | L2856 | no manual edit
EN: [AND SEEMS TO BE IMPERVIOUS TO MOST PHYSICAL ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O452703500077e40a5c31 | L2857 | EDIT E08-005
EN: ["PHYSICAL" ATTACKS? WHAT OTHER KIND OF ATTACKS ARE THERE?]
BEFORE:   Yiffany: ["PHYSICAL"攻击？那还有什么别的种类的攻击？]
AFTER:   Yiffany: [“物理”攻击？还有别的攻击方式吗？]
ROW CAT:O3e46e393283fa9b6a801 | L2858 | no manual edit
EN: [SOME REPORTS FROM PREVIOUS AGENTS MENTIONED THAT]
BEFORE:   Bossu: [之前有些特工的报告提到过，Blocker对“精神”攻击较为脆弱]
AFTER:   Bossu: [之前有些特工的报告提到过，Blocker对“精神”攻击较为脆弱]
ROW CAT:O939504abe908703a845a | L2859 | no manual edit
EN: [BLOCKERS WERE VUL- NERABLE TO "PSYCHICAL" ATTACKS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oeb08b46de7a471930845 | L2860 | no manual edit
EN: [WE DISMISSED THOSE REPORTS AS UNRELIABLE, BUT...]
BEFORE:   Bossu: [我们当时把这些报告当作不可靠的给驳回了，但是……]
AFTER:   Bossu: [我们当时把这些报告当作不可靠的给驳回了，但是……]
ROW CAT:Od92264dfaaed6f0083ba | L2861 | no manual edit
EN: [AFTER SEEING THIS THING IN PERSON]
BEFORE:   Yiffany: [不过，在亲眼见过这东西之后，我已经不确定到底*什么*还算可靠了……]
AFTER:   Yiffany: [不过，在亲眼见过这东西之后，我已经不确定到底*什么*还算可靠了……]
ROW CAT:O1844b18dbde47bb2d0b5 | L2862 | no manual edit
EN: [I'M NOT SURE WHAT EVEN *IS* RELIABLE ANYMORE...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P08-003 | action=apply
原问题：Bossu刚讲物理攻击无效，主角是在追问这个术语；现译残留PHYSICAL使问答接点失真，不是专名保留。
本轮理由：PHYSICAL是紧接上文的普通术语，不是专名；改中文问句，保留对其他攻击种类的追问。
EDIT_IDS ["E08-005"]

## SCcb7d60767094d0c1 | nsfw | datadf/all.ds | BossuDex.ClassicDriller
CONTROL L3006  <BossuDex.ClassicDriller>
ROW CAT:O92e36425c795c5a40b5f | L3007 | no manual edit
EN: [AS A NANOMECHANICAL ROBOT, THE 'DRILLER' UNITS WILL]
BEFORE:   Bossu: [作为一种纳米机械机器人，那些'DRILLER'单元会持续自我修复。它们会不知疲倦地钻掘。]
AFTER:   Bossu: [作为一种纳米机械机器人，那些'DRILLER'单元会持续自我修复。它们会不知疲倦地钻掘。]
ROW CAT:O89878dbc0b0d28e5ab4e | L3008 | no manual edit
EN: [CONTINUOUSLY REPAIR THEMSELVES. THEY'LL BURROW TIRELESSLY.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O10b3176a11ba4251478a | L3009 | no manual edit
EN: [WELL I GUESS THAT MEANS I JUST HAVE TO MAKE AN]
BEFORE:   Yiffany: [那我猜我就只能开一个口子，然后跑掉！]
AFTER:   Yiffany: [那我猜我就只能开一个口子，然后跑掉！]
ROW CAT:O90fb2f8542999a06bdd1 | L3010 | no manual edit
EN: [OPENING AND THEN RUN FOR IT!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4afe981d246566c2effd | L3011 | EDIT E08-006
EN: [INDEED, AGENT. THE DRILLER UNITS WILL ONLY OPERATE WITHIN]
BEFORE:   Bossu: [的确，特工。DRILLER单元只会在它们预定的边界之内运作。]
AFTER:   Bossu: [的确，特工。DRILLER单元只在预定范围内活动，不会越界。]
ROW CAT:O6f14ef39f7b448387e02 | L3012 | no manual edit
EN: [THEIR PREDETERMINED BOUNDARIES.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od206255a0d1795eb6fb3 | L3013 | EDIT E08-007
EN: [...WISH MORE GUYS AT THE ACADEMY HAD BEEN LIKE THAT.]
BEFORE:   Yiffany: [……真希望学院里更多家伙当时也那样。]
AFTER:   Yiffany: [……真希望学院里能多些这么懂得分寸的男生。]
ROW CAT:Oc57b59cc5ed000d9e19d | L3014 | no manual edit
EN: [HMM?]
BEFORE:   Bossu: [嗯？]
AFTER:   Bossu: [嗯？]
ROW CAT:O42b010a5ea248a4dbf37 | L3015 | no manual edit
EN: [NOTHING BOSSU! YIFFANY OUT.]
BEFORE:   Yiffany: [没什么，Bossu！伊法妮通话完毕。]
AFTER:   Yiffany: [没什么，Bossu！伊法妮通话完毕。]
### P08-004 | action=apply
原问题：boundaries由机器活动边界转为人际分寸；“更多家伙当时也那样”没有可辨的中文笑点，且guys性别信息消失。建议让“守规矩”承接边界，未补具体骚扰事件。Driller名称只是本段暂译，需术语统筹。
本轮理由：机器边界和学院男生的分寸构成双关；用“越界”连接两人台词，不给DRILLER另造译名，也不添加具体骚扰经历。
EDIT_IDS ["E08-006", "E08-007"]

## SC3b0f76128c2a6465 | nsfw | datadf/all.ds | BossuDex.ClassicWyvern
CONTROL L2988 <BossuDex.ClassicWyvern>
ROW CAT:Od80b27f552d4d8d94722 | L2989 | no manual edit
EN: [BOSSU, I'VE JUST ENCOUNTERED A FLYING DRACONID.]
BEFORE:   Yiffany: [波苏，我刚遇到了一只飞行的龙人。]
AFTER:   Yiffany: [波苏，我刚遇到了一只飞行的龙人。]
ROW CAT:Ob497c3f126d40ee9da3b | L2990 | no manual edit
EN: [NOT SURPRISING. THE PREVIOUS MISSION REPORTED MULTIPLE]
BEFORE:   Bossu: [并不意外。上次任务报告里有多起双足飞龙目击记录。那些狡猾的家伙肌肉发达，在空中也极其灵活。]
AFTER:   Bossu: [并不意外。上次任务报告里有多起双足飞龙目击记录。那些狡猾的家伙肌肉发达，在空中也极其灵活。]
ROW CAT:Ob380fb6e70b98120e9ba | L2991 | no manual edit
EN: [WYVERN SIGHTINGS. THOSE CRAFTY CREATURES ARE WELL]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obeb22d815d680115eebe | L2992 | no manual edit
EN: [MUSCLED AS WELL AS EXTREMELY AGILE IN THE AIR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O3086af88c3c340d46255 | L2993 | no manual edit
EN: [ANY TACTICS REPORTED BY THE PREVIOUS TEAM?]
BEFORE:   Yiffany: [上一支队伍报告过什么战术吗？]
AFTER:   Yiffany: [上一支队伍报告过什么战术吗？]
ROW CAT:O488e7fcf58b490344c0e | L2994 | EDIT E08-008
EN: [THE NOTES SAY WYVERNS ARE PRONE TO DISTRACTION AT THE]
BEFORE:   Bossu: [记录上说，双足飞龙在高潮的]
AFTER:   Bossu: [记录上说，双足飞龙在高潮时容易分神。]
ROW CAT:O607a8907e8992d69601b | L2995 | EDIT E08-009
EN: [MOMENT OF ORGASM, SO A 'TEASER' AGENT SHOULD]
BEFORE:   Bossu: [高潮的那一刻，所以负责“挑逗”的特工应该]
AFTER:   Bossu: [所以负责“挑逗”的特工必须被牢牢绑住，]
ROW CAT:O8c92c6a7b0f0e6ca8268 | L2996 | EDIT E08-010
EN: [BE BOUND SECURELY WHILE THEIR COMRADES-]
BEFORE:   Bossu: [被牢牢绑住，好让它们的同伴-]
AFTER:   Bossu: [而这名特工的队友则——]
ROW CAT:Ob3d22a06579aa146b640 | L2997 | no manual edit
EN: [BOSSU. I'M SOLO, REMEMBER?]
BEFORE:   Yiffany: [波苏。我是单独行动，记得吗？]
AFTER:   Yiffany: [波苏。我是单独行动，记得吗？]
ROW CAT:Oa45a58ed5b4b94640c54 | L2998 | no manual edit
EN: [AHEM. THEN I SUGGEST YOU EVADE THEIR SWOOPING AND]
BEFORE:   Bossu: [咳。那我建议你避开它们的俯冲，有机会就出手。]
AFTER:   Bossu: [咳。那我建议你避开它们的俯冲，有机会就出手。]
ROW CAT:Oe147c07877e0d58a3331 | L2999 | no manual edit
EN: [STRIKE WHENEVER YOU ARE ABLE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofb4c3ae02e7843cc968d | L3000 | no manual edit
EN: [SIGH... THAAANKS BOSSU. YIFFANY OUT.]
BEFORE:   Yiffany: [唉……谢——谢啦波苏。伊法妮完毕。]
AFTER:   Yiffany: [唉……谢——谢啦波苏。伊法妮完毕。]
### P08-005 | action=apply
原问题：现译完整连读仍为“在高潮的高潮的那一刻，所以”，漏失prone to distraction；their comrades是探员队友，不是飞龙同伴。保留未说完的战术，不补队友具体行为，也不擅改原作“须绑牢”条件。
本轮理由：完整战术为飞龙高潮易分神、挑逗特工须绑牢、其队友行动尚未说完；三槽保留非空，不补中断后的行动，their不指飞龙。
EDIT_IDS ["E08-008", "E08-009", "E08-010"]

## SC4343a658dcedb661 | nsfw | datadf/all.ds | DefeatHints.ClassicWerehund.food
CONTROL L4860 <DefeatHints.ClassicWerehund.food>
ROW CAT:O6e90d7f43092e3157ec0 | L4861 | no manual edit
EN: COME IN, YIFFANY!
BEFORE:   Mauser: 伊法妮，收到请回答！
AFTER:   Mauser: 伊法妮，收到请回答！
ROW CAT:O089f833557621221f163 | L4862 | no manual edit
EN: I THINK SHE'S OUT GOOD...
BEFORE:   Tomcat: 我看她是彻底昏过去了……
AFTER:   Tomcat: 我看她是彻底昏过去了……
ROW CAT:Ob8b87276cc3102293ac7 | L4863 | no manual edit
EN: OH MAN, THIS IS TERRIBLE...
BEFORE:   Mauser: 天啊，这也太惨了……
AFTER:   Mauser: 天啊，这也太惨了……
ROW CAT:O5ecda2eb9350c47b127d | L4864 | EDIT E08-011
EN: I WOULD'VE STOCKED UP ON FOOD
BEFORE:   Mauser: 在这种大仗之前，我本该先囤点食物的！
AFTER:   Mauser: 换作是我，打这种硬仗之前肯定先备足吃的！
ROW CAT:O03aa924e392fda642789 | L4865 | no manual edit
EN: BEFORE A BIG FIGHT LIKE THAT!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6bc6c43354db66677484 | L4866 | EDIT E08-012
EN: THAT'S JUST BECAUSE YOU LACK
BEFORE:   Tomcat: 那只是因为你缺少一身老练的战斗功夫！ 
AFTER:   Tomcat: 那还不是因为你打架的本事不行！
ROW CAT:O7bf5f36e031532b42e2d | L4867 | no manual edit
EN: GOOD OL' FIGHTING SKILLS!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od6da413ab8b0409aaa64 | L4868 | no manual edit
EN: HEY! C-COME ON...!
BEFORE:   Mauser: 喂！别、别这么说……！
AFTER:   Mauser: 喂！别、别这么说……！
CONTROL L4869 # STARKILL 2
### P08-006 | action=apply
原问题：would have在此为旁观者给失败外勤的反事实建议，不是Mauser承认自己忘带补给。现译“我本该”把当前失败责任移到总部人员身上；后句正拿他依赖食物的习惯开涮。
本轮理由：Mauser在总部设想自己会如何备战，不是承认自己害外勤失败；合句头保留大仗前备粮，Tomcat仍讥讽他的战斗本事。
EDIT_IDS ["E08-011", "E08-012"]

## SC535618a487339cf5 | sfw | datadf/all.ds | The0.AreaX_intro noselect noamendfreq
CONTROL L2587 <The0.AreaX_intro noselect noamendfreq>
ROW SFWbe1137413ef9a2dc511fb705 | L2588 | EDIT E08-013
EN: [OH? IT'S NOT OFTEN THAT I GET STRANGERS CALLING ME.]
BEFORE:   Yiffany: [哦？不常有陌生人联系我。]
AFTER:   Yiffany: [哦？倒是难得有陌生人打来。]
ROW SFW7e539f158545313c23072b81 | L2589 | EDIT E08-014
EN: [...WHILE I'M ON MISSION, THAT IS <3]
BEFORE:   Yiffany: [……毕竟我正在执行任务 <3]
AFTER:   Yiffany: [……我是说，在我执行任务的时候 <3]
ROW SFWd139edd0957e13c2bea2d36a | L2590 | no manual edit
EN: [OH H-HEY! I'M NO STRANGER! IT'S JUST YOUR FRIENDLY]
BEFORE:   The0: [哦、嘿！我可不是陌生人！就是你那友好的小小黑客狗。只是想顺便插进你这条小小的一次性密码本加密频道！]
AFTER:   The0: [哦、嘿！我可不是陌生人！就是你那友好的小小黑客狗。只是想顺便插进你这条小小的一次性密码本加密频道！]
ROW SFW6da66a944ed656c9a214c845 | L2591 | no manual edit
EN: [LITTLE HACKER DOG. JUST THOUGHT I'D POP IN ON THIS LITTLE]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW278e87aef46c580d1ce4a6d0 | L2592 | no manual edit
EN: [OTP CIPHER ENCRYPTED CHANNEL OF YOURS!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW2c3e84801d53fcb22d29605c | L2593 | no manual edit
EN: [OH YEAH? HOW'D YOU GET IN HERE LITTLE BUDDY?]
BEFORE:   Yiffany: [哦，是吗？你是怎么进来的，小家伙？]
AFTER:   Yiffany: [哦，是吗？你是怎么进来的，小家伙？]
ROW SFWd2070b7f907227c63ab055cc | L2594 | no manual edit
EN: [WELL, CAN YOU REALLY CALL IT A "ONE TIME PAD"]
BEFORE:   The0: [话说，你们明明在重复使用密码表片段，还真能把它叫成「一次性密码本」吗……]
AFTER:   The0: [话说，你们明明在重复使用密码表片段，还真能把它叫成「一次性密码本」吗……]
ROW SFWe7953e04a7dcc89be63e458d | L2595 | no manual edit
EN: [WHEN YOU GUYS ARE CLEARLY RECYCLING TABLE CHUNKS...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW44198b301ce38fc4ee679131 | L2596 | no manual edit
EN: [...ANYWAYS!]
BEFORE:   The0: [……总之！]
AFTER:   The0: [……总之！]
ROW SFW65d9d936f1cca2237a1c8b0e | L2597 | no manual edit
EN: [YOU CAN CALL ME "THE0"! THOUGHT I'D HELP YOU OUT BY]
BEFORE:   The0: [你就叫我“The0”吧！想着来帮帮你，告诉你一个区域里还剩多少芯片。]
AFTER:   The0: [你就叫我“The0”吧！想着来帮帮你，告诉你一个区域里还剩多少芯片。]
ROW SFWf0978e8aaf9dd0739216e474 | L2598 | no manual edit
EN: [LETTING YOU KNOW HOW MANY CHIPS ARE LEFT IN AN AREA.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW2bf49e332695ba3ac74e619b | L2599 | no manual edit
EN: [JUST GIVE ME A CALL AT 28.250 AND I'LL FILL YOU IN!]
BEFORE:   The0: [打28.250联系我，我就告诉你详情！]
AFTER:   The0: [打28.250联系我，我就告诉你详情！]
ROW SFW6588147e125567c32637552e | L2600 | no manual edit
EN: [AWW, ISN'T THAT SWEET OF YOU. I'LL BE SURE TO RING!]
BEFORE:   Yiffany: [哎呀，你真好。我一定会打的！]
AFTER:   Yiffany: [哎呀，你真好。我一定会打的！]
ROW SFWd37c63f4a8c0dfbbc5cdd98d | L2601 | no manual edit
EN: [...FORWARDING THIS CALL TO TECH...]
BEFORE:   Bossu: [……把这通电话转给技术组……]
AFTER:   Bossu: [……把这通电话转给技术组……]
### P08-007 | action=apply
原问题：that is收窄上句范围并带调情：不是不常有人搭话，只是在任务期间少。现译“毕竟”误成因果解释，抹去自我补充的笑点。
本轮理由：that is把陌生人来电少限于执行任务期间，是事后补充的调情，不是毕竟引出的因果。保留两槽及爱心。
EDIT_IDS ["E08-013", "E08-014"]

## SC41f714a207c66198 | nsfw | datadf/all.ds | Tomcat.AreaA_map42_a noselect
CONTROL L2228 <Tomcat.AreaA_map42_a noselect>
ROW CAT:O198fa5fe515916c884e2 | L2229 | no manual edit
EN: [OOOOH ARE THOSE THE MARK IV MODELS?]
BEFORE:   Tomcat: [哦哦，那是马克 IV 型吗？]
AFTER:   Tomcat: [哦哦，那是马克 IV 型吗？]
ROW CAT:Oc4e610c65db3b5ddc39f | L2230 | no manual edit
EN: [MARK WHAT MODELS?]
BEFORE:   Yiffany: [马克什么型？]
AFTER:   Yiffany: [马克什么型？]
ROW CAT:Od02c77d54b29629a3772 | L2231 | no manual edit
EN: [WOOOAH THEY ARE, COMPLETE WITH TRAJ- ECTORAL BOOSTERS!]
BEFORE:   Mauser: [哇——还真是，还配了轨迹助推器！]
AFTER:   Mauser: [哇——还真是，还配了轨迹助推器！]
ROW CAT:Ob70e5a0343129ffc46d2 | L2232 | no manual edit
EN: [NIIICE, EVERYONE'S GONNA BE 'MIRIN' THOSE, YOU KNOW!]
BEFORE:   Tomcat: [不——错，你知道的，人人都会盯着看的！]
AFTER:   Tomcat: [不——错，你知道的，人人都会盯着看的！]
ROW CAT:O12bcd77b0ecd237a2103 | L2233 | no manual edit
EN: [NOBODY HERE IN HQ CAN AFFORD THE MARK III COSMOBOOTS]
BEFORE:   Mauser: [总部这儿没人买得起马克 III 宇宙靴，更别说那双了！那可是顶配！]
AFTER:   Mauser: [总部这儿没人买得起马克 III 宇宙靴，更别说那双了！那可是顶配！]
ROW CAT:O77a99bd526c794c06126 | L2234 | no manual edit
EN: [NEVERMIND THOSE ONES! THEY'RE TOP OF THE LINE!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O49f6501f67e6eb011602 | L2235 | no manual edit
EN: [ARE YOU TWO HAVING A MOMENT? SHOULD I LEAVE YOU ALONE?]
BEFORE:   Yiffany: [你们俩在培养感情吗？要我避开吗？]
AFTER:   Yiffany: [你们俩在培养感情吗？要我避开吗？]
ROW CAT:Oabc44e0b08fb98fb29e4 | L2236 | no manual edit
EN: [YOU'RE JOKING, RIGHT? WHAT SORT OF AGENT ARE YA?]
BEFORE:   Tomcat: [你在开玩笑吧？你算哪门子特工？]
AFTER:   Tomcat: [你在开玩笑吧？你算哪门子特工？]
ROW CAT:O4d0b85b3042cc4723913 | L2237 | no manual edit
EN: [THE KIND THAT DOESN'T HAVE A SHOE FETISH, I GUESS?]
BEFORE:   Yiffany: [大概是没有鞋子性癖的那种？]
AFTER:   Yiffany: [大概是没有鞋子性癖的那种？]
ROW CAT:O65b33cb8fe08e060e949 | L2238 | no manual edit
EN: [THOSE AREN'T JUST SHOES]
BEFORE:   Mauser: [那不只是鞋子]
AFTER:   Mauser: [那不只是鞋子]
ROW CAT:O181b2d865178ba95a976 | L2239 | no manual edit
EN: [NO?]
BEFORE:   Yiffany: [不是吗？]
AFTER:   Yiffany: [不是吗？]
ROW CAT:O3a775d3332e66cb5e7fc | L2240 | no manual edit
EN: [YEAH, THEY'RE /EXPENSIVE/ SHOES! LIMITED EDITIONS!]
BEFORE:   Tomcat: [对，它们是/昂贵的/鞋！限量版！]
AFTER:   Tomcat: [对，它们是/昂贵的/鞋！限量版！]
ROW CAT:Ofad4c36b42a39b70646e | L2241 | no manual edit
EN: [BUT ON TOP OF THAT THEY'LL LET YOU DO COOL DIVE KICKS!]
BEFORE:   Mauser: [而且它们还能让你使出很酷的俯冲踢！]
AFTER:   Mauser: [而且它们还能让你使出很酷的俯冲踢！]
ROW CAT:O95483222f6562283ff7b | L2242 | no manual edit
EN: [YEAH, GIVE IT A TRY NEXT TIME YOU JUMP AROUND.]
BEFORE:   Tomcat: [对，下次跳起来的时候试试。]
AFTER:   Tomcat: [对，下次跳起来的时候试试。]
ROW CAT:O84f58ac1929bd4e50de4 | L2243 | no manual edit
EN: [PRESS DOWN + JUMP WHILE ALREADY IN THE AIR]
BEFORE:   Tomcat: [在已经腾空时按 DOWN + JUMP，你就会做出一次俯冲踢；如果接触到任何会承受伤害的东西，还会把你向上弹起。]
AFTER:   Tomcat: [在已经腾空时按 DOWN + JUMP，你就会做出一次俯冲踢；如果接触到任何会承受伤害的东西，还会把你向上弹起。]
ROW CAT:O1c1d21885a52d903fa9a | L2244 | no manual edit
EN: [AND YOU'LL DO A DIVEKICK THAT WILL ALSO BOUNCE YOU UP]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oe38139f3141ced808a82 | L2245 | no manual edit
EN: [IF YOU MAKE CONTACT WITH ANYTHING THAT TAKES DAMAGE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4fac43c5e49aa829b099 | L2246 | EDIT E08-015
EN: [ALRIGHT, THAT SORT OF INFO IS MORE MY SPEED!]
BEFORE:   Yiffany: [好，这种信息才像我的路子！]
AFTER:   Yiffany: [好，这种实用情报才对我的胃口！]
ROW CAT:O776fa04ee70e5fc3f617 | L2247 | no manual edit
EN: [TIME TO GIVE THIS DIVEKICKING THING A TEST RUN.]
BEFORE:   Yiffany: [是时候试试这俯冲踢了。]
AFTER:   Yiffany: [是时候试试这俯冲踢了。]
ROW CAT:O9ed522c5a1ac7d9b6e2f | L2248 | no manual edit
EN: [YUP, JUST REMEMBER THAT DOWN + JUMP WILL ONLY DIVEKICK]
BEFORE:   Mauser: [对，记住 DOWN + JUMP 只有在你身处半空时才会使出俯冲踢！]
AFTER:   Mauser: [对，记住 DOWN + JUMP 只有在你身处半空时才会使出俯冲踢！]
ROW CAT:O68953a36028086029e8b | L2249 | no manual edit
EN: [WHILE YOU'RE MID-AIR!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P08-008 | action=apply
原问题：more my speed指信息合胃口、是自己关心的方向；“信息才像我的路子”搭配生硬，削弱她从装备迷闲聊转回行动的落点。保留前面按键说明，不并入此提案。
本轮理由：more my speed是回到她关心的实用内容，不是速度或路子；下一现有节点保留主动试招，未改按键说明。
EDIT_IDS ["E08-015"]

## SC1667be893970acf7 | nsfw | datadf/all.ds | TomcatItems.DoggyBody
CONTROL L4080 <TomcatItems.DoggyBody>
ROW CAT:O38daf7736e66d23fea45 | L4081 | no manual edit
EN: [AWWW, IS THAT A LEASH THAT YOU JUST PICKED UP THERE?]
BEFORE:   Tomcat: [哎呀，你刚捡到的是牵引绳吗？]
AFTER:   Tomcat: [哎呀，你刚捡到的是牵引绳吗？]
ROW CAT:O11ed902353a3a1cb85f6 | L4082 | no manual edit
EN: [I DIDN'T KNOW YOU STILL NEEDED ONE OF THOSE!]
BEFORE:   Tomcat: [我不知道你还需要这个！]
AFTER:   Tomcat: [我不知道你还需要这个！]
ROW CAT:Oc9034154b3e2be274504 | L4083 | EDIT E08-016
EN: [HEY, A LITTLE PUPPY PLAY NEVER HURT ANYONE, RIGHT?]
BEFORE:   Yiffany: [嘿，玩一点小狗扮演从来没伤过谁，对吧？]
AFTER:   Yiffany: [嘿，偶尔玩玩小狗扮演，又没什么坏处，对吧？]
ROW CAT:Of0dc4ee52debc9106ff1 | L4084 | EDIT E08-017
EN: [NOTHING BAD ABOUT PRETENDING TO BE A LIL PUP AGAIN.]
BEFORE:   Yiffany: [再假装一下小幼犬，也没什么不好。]
AFTER:   Yiffany: [再假装一回小狗，也没什么不好嘛。]
ROW CAT:O52efb42ea8c0ed53c593 | L4085 | no manual edit
EN: [WOW, SHAMELESS AREN'TYA GIRL? YOU'D NEVER CATCH ME DO-]
BEFORE:   Tomcat: [哇，不害臊是吧，姑娘？你绝对见不到我去-]
AFTER:   Tomcat: [哇，不害臊是吧，姑娘？你绝对见不到我去-]
ROW CAT:Ob1ff940814bb4a3d032f | L4086 | no manual edit
EN: [YOU'RE GONNA TELL ME YOU STILL DON'T DIP INTO SOFT FOOD]
BEFORE:   Yiffany: [你该不会告诉我，你现在还是不偶尔吃点软食吧？]
AFTER:   Yiffany: [你该不会告诉我，你现在还是不偶尔吃点软食吧？]
ROW CAT:O9bd72fdcd7f75babf7e7 | L4087 | no manual edit
EN: [EVERY NOW AND AGAIN?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O78df07866a7683642e52 | L4088 | no manual edit
EN: [HEY, L-LOOK, THAT'S... THAT'S COMPLETELY...]
BEFORE:   Tomcat: [嘿，听、听着，那是……那完全是……]
AFTER:   Tomcat: [嘿，听、听着，那是……那完全是……]
ROW CAT:O8fc9be8992c1c799bf49 | L4089 | no manual edit
EN: [I'VE GOT R-R-REPORTS TO DO, B-BYE!!]
BEFORE:   Tomcat: [我还有报、报告要做，再、再见！！]
AFTER:   Tomcat: [我还有报、报告要做，再、再见！！]
ROW CAT:O572dd451b408ddcc2bf4 | L4090 | no manual edit
EN: [HEE!]
BEFORE:   Yiffany: [嘿！]
AFTER:   Yiffany: [嘿！]
### P08-009 | action=apply
原问题：never hurt anyone在此为轻松辩护习语，不是陈述从未发生伤害；现译“玩一点……从来没伤过谁”明显英语腔。只重写她的辩护，不扩大为关系或年龄设定。
本轮理由：never hurt anyone是轻松辩护，非伤害史陈述；两槽分别保留小狗扮演与再次假扮的意思，不变年龄或关系。
EDIT_IDS ["E08-016", "E08-017"]

## SC959cea4cd47a5799 | nsfw | datadf/all.ds | TomcatItems.StatFishtaco
CONTROL L3884 <TomcatItems.StatFishtaco>
ROW CAT:O1f855df614098112c5c0 | L3885 | no manual edit
EN: [OH, A FISH TACO! THOSE SWIPERS HAVE GOOD TASTE!]
BEFORE:   Tomcat: [哦，鱼肉塔可！那些挥爪挺有品味！]
AFTER:   Tomcat: [哦，鱼肉塔可！那些挥爪挺有品味！]
ROW CAT:Oa0f9368daed0e2f03aee | L3886 | EDIT E08-018
EN: [WHEN WAS THE LAST TIME YOU HAD ONE OF THOSE IN YOUR MAW?]
BEFORE:   Tomcat: [你上次把那种放进大口是什么时候？]
AFTER:   Tomcat: [你上回嘴里尝到这个，是什么时候？]
ROW CAT:O975b195a8c93956ff1c4 | L3887 | EDIT E08-019
EN: [COSMO COLLEGE. SECOND YEAR. SUMMER VACATION, 19XX.]
BEFORE:   Yiffany: [Cosmo学院。第二年。暑假，19XX。]
AFTER:   Yiffany: [Cosmo学院。大二。19XX年的暑假。]
ROW CAT:O32c5af6d147404aca73b | L3888 | EDIT E08-020
EN: [WHAT? SERIOUS? YOU'VE NEVER TOLD ME ABOUT THA-]
BEFORE:   Tomcat: [什么？当真？你从没跟我说过THA-]
AFTER:   Tomcat: [什么？真的？你从没跟我说过这——]
ROW CAT:O3f8da024a5a58e708cfa | L3889 | no manual edit
EN: [USED TO BE THIS AMAZING TACO TRUCK BY THE BEACH.]
BEFORE:   Yiffany: [以前海滩边有一辆特别棒的塔可餐车。]
AFTER:   Yiffany: [以前海滩边有一辆特别棒的塔可餐车。]
ROW CAT:O6c46a3463878c0ad785a | L3890 | no manual edit
EN: [WENT THERE PRACTICALLY EVERY DAY!]
BEFORE:   Yiffany: [几乎每天都去那儿！]
AFTER:   Yiffany: [几乎每天都去那儿！]
ROW CAT:Ob6652c192efab5679ed3 | L3891 | EDIT E08-021
EN: [OH RIGHT, OF COURSE... SOUNDS... YUM...!]
BEFORE:   Tomcat: [哦对，当然……听起来……好吃……!]
AFTER:   Tomcat: [哦，对，当然……听着……挺好吃的……！]
### P08-010 | action=apply
原问题：Tomcat故意以食物说暧昧话，被餐车解释截断。现译“大口”“THA-”让问句和截话都不成立；保留食物表层与误会空间，不强加更露骨解释。
本轮理由：嘴里尝到保留鱼肉塔可表层与暧昧空间，THA为被打断的that不留英文残片；不补具体成人经历，Cosmo沿当前写法。
EDIT_IDS ["E08-018", "E08-019", "E08-020", "E08-021"]

## SCfd3a35d14d8646de | nsfw | datadm/all.ds | AreaB_Slaver2.Talk.kobo
CONTROL L1065 <AreaB_Slaver2.Talk.kobo>
CONTROL L1066   if { koboCostume() } {
ROW CAT:O4c25f65c290e84e68628 | L1067 | EDIT E08-022
EN: You smell pretty cute for a kobold, heh-heh. What crew you fly in with?
BEFORE:     * 你身上这味道对科博德来说真够可爱的，嘿嘿。你跟哪一伙船员一起飞？
AFTER:     * 作为科博德，你闻着还挺可爱的，嘿嘿。你跟哪伙船员来的？
CONTROL L1068   }
CONTROL L1070 ### dog handling
### P08-011 | action=apply
原问题：现译“身上这味道对科博德来说真够可爱”“一起飞”生硬；前半是按对方外观搭讪，后半问所属来访船员，不问飞行技能。未指定匿名商人姓名。
本轮理由：条件为koboCostume，搭讪基于当前外观；保留对科博德而言的比较、气味与来访船队问题，不给匿名者定姓名。
EDIT_IDS ["E08-022"]

## SCb84957d4bbe46c64 | nsfw | datadm/all.ds | BossuDex.ClassicMineWall
CONTROL L3085 <BossuDex.ClassicMineWall>
ROW CAT:O4a4999543c195b6fd4ac | L3086 | no manual edit
EN: [WOAH! DID YOU PICK UP THAT EXPLOSION AT HQ?!]
BEFORE:   Yiffai: [哇哦！总部那边有接到那声爆炸吗？！]
AFTER:   Yiffai: [哇哦！总部那边有接到那声爆炸吗？！]
ROW CAT:O211d32bcfc1ea166f9a9 | L3087 | no manual edit
EN: [INDEED, IT APPEARS THE MINES OF TUTONE HAVE BEEN MINED.]
BEFORE:   Bossu: [确实，看来图托恩的矿山都已经布上了雷。]
AFTER:   Bossu: [确实，看来图托恩的矿山都已经布上了雷。]
ROW CAT:O3ff7c6da1113e0f47ee0 | L3088 | no manual edit
EN: [...? WELL SURE, BUT WHAT'S THAT GOTTA DO WITH EXPLOSIONS?]
BEFORE:   Yiffai: [……? 好吧，可那跟爆炸有什么关系？]
AFTER:   Yiffai: [……? 好吧，可那跟爆炸有什么关系？]
ROW CAT:O8ffba486b4343ce835c7 | L3089 | no manual edit
EN: [THE EXPLOSIONS FROM THE MINES.]
BEFORE:   Bossu: [是那些矿区传来的爆炸。]
AFTER:   Bossu: [是那些矿区传来的爆炸。]
ROW CAT:Oafa2c8f4181a40861975 | L3090 | no manual edit
EN: [YEAH! IT WAS IN THE MINES, BUT-]
BEFORE:   Yiffai: [对啊！那是在矿坑里，但是-]
AFTER:   Yiffai: [对啊！那是在矿坑里，但是-]
ROW CAT:O58d4ef1a57096949cd79 | L3091 | no manual edit
EN: [WHAT BOSSU MEANS IS THAT THOSE OLD MINERS PLACED]
BEFORE:   Mauser: [Bossu的意思是，那些老矿工当年在他们自己的矿里埋了地雷，好喊一声"这是我的！"]
AFTER:   Mauser: [Bossu的意思是，那些老矿工当年在他们自己的矿里埋了地雷，好喊一声"这是我的！"]
ROW CAT:Oa34b63c37bc726ad5efe | L3092 | no manual edit
EN: [MINES IN THEIR MINES, AS A WAY TO SAY "THAT'S MINE!"]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ob2d039e9b4aa38a03127 | L3093 | no manual edit
EN: [WHAT...?! I'LL JUST AVOID THEM, OKAY?! Y-YIFFAI OUT!]
BEFORE:   Yiffai: [什么……？！那我就躲开它们，行吧？！伊、伊法伊通话完毕！]
AFTER:   Yiffai: [什么……？！那我就躲开它们，行吧？！伊、伊法伊通话完毕！]
### P08-013 | action=defer
原问题：当前首句已经明说“布雷”，主角却继续不懂，Bossu再把mines译回矿区，问答倒转。中文以“埋雷占矿”与“这矿归我”的占有笑点重建解释链，使主角从问爆炸到问为何埋雷；不能照搬英语同形词。此为整段创译方向，仍需二审试读，不能原样自动回填。
本轮理由：确认当前矿区/地雷指代来回倒转，破坏误解链；但R1“明说埋雷后主角仍追问爆炸”的草案同样不成立。英文mine/mined/mines/mine的多义无法靠中文词面堆叠恢复，本次尚未形成既保Bossu冷笑话、Yiffai误听和Mauser占有梗、又不添机制的整组中文终稿，因此留置整组，不以局部修词冒充完成；须后续专项中文创译并整组试读。
EDIT_IDS []

## SC691b3a18b7909076 | nsfw | datadm/all.ds | Mauser.AreaC_map01_a noselect
CONTROL L2396 <Mauser.AreaC_map01_a noselect>
ROW CAT:O4362cbd9a282f9edaa16 | L2397 | no manual edit
EN: [BEHOLD, YIFFAI! YOU ARE IN THE LUSH LAND OF SCEAFYA!]
BEFORE:   Mauser: [看好了，伊法伊！你已身处草木繁茂的斯凯菲亚大地！]
AFTER:   Mauser: [看好了，伊法伊！你已身处草木繁茂的斯凯菲亚大地！]
ROW CAT:Oa9a7209c0eaf049dcb68 | L2398 | no manual edit
EN: [GOBINS AND ELVES OF ALL SORTS LAY IN WAIT]
BEFORE:   Mauser: [各式各样的哥布林与精灵，就在每一丛灌木、每一棵树后面埋伏着等你——]
AFTER:   Mauser: [各式各样的哥布林与精灵，就在每一丛灌木、每一棵树后面埋伏着等你——]
ROW CAT:O30a90846e5982295f056 | L2399 | no manual edit
EN: [BEHIND ANY BUSH OR TREE THAT YOU MA-]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6547f802f69089870576 | L2400 | no manual edit
EN: [WAIT, BUSHES? TREES?]
BEFORE:   Yiffai: [等等，灌木？树木？]
AFTER:   Yiffai: [等等，灌木？树木？]
ROW CAT:O1d238d09885606e2a91e | L2401 | no manual edit
EN: [THERE'S NOTHING RESEMBLING A PLANT NEAR ME.]
BEFORE:   Yiffai: [我附近根本没有任何像植物的东西。]
AFTER:   Yiffai: [我附近根本没有任何像植物的东西。]
ROW CAT:O795058d0773b6522536d | L2402 | no manual edit
EN: [W-WHAT? BUT MY RESEARCH SAYS...]
BEFORE:   Mauser: [什、什么？可我的研究明明说……]
AFTER:   Mauser: [什、什么？可我的研究明明说……]
ROW CAT:O536d10dbd5f025689c7f | L2403 | no manual edit
EN: [ALLOW ME TO INTERJECT, AGENT.]
BEFORE:   Bossu: [请允许我插一句，特工。]
AFTER:   Bossu: [请允许我插一句，特工。]
ROW CAT:O55d14928aa3e032c89d9 | L2404 | no manual edit
EN: [YOU'VE ENTERED SCEAFYA FROM THE SOUTHERN CONNECTION]
BEFORE:   Bossu: [你是从南侧连接段进入斯凯菲亚的，从一处古老、早已停用的港区冒出来。]
AFTER:   Bossu: [你是从南侧连接段进入斯凯菲亚的，从一处古老、早已停用的港区冒出来。]
ROW CAT:Oe443c37b11932e54727f | L2405 | no manual edit
EN: [EMERGING IN AN ANCIENT NON- FUNCTIONAL PORT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O312567efe935a74d3cc2 | L2406 | no manual edit
EN: [OH! OH! THAT MUST MEAN THAT HE'S IN TH-]
BEFORE:   Mauser: [哦！哦！那说明他就在那——]
AFTER:   Mauser: [哦！哦！那说明他就在那——]
ROW CAT:Oa7e28457745b4222d835 | L2407 | no manual edit
EN: [WHAT LOOKS LIKE A GIANT TREE IN SCEAFYA IS ACTUALLY]
BEFORE:   Bossu: [斯凯菲亚里那棵看着像巨树的玩意儿，其实是一座来自很久很久以前的旧星际港。]
AFTER:   Bossu: [斯凯菲亚里那棵看着像巨树的玩意儿，其实是一座来自很久很久以前的旧星际港。]
ROW CAT:Obeae32f3c69caf443ba5 | L2408 | no manual edit
EN: [AN OLD STARPORT FROM A TIME LONG, LONG AGO.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oaff38004fd2098fa4c88 | L2409 | no manual edit
EN: [NOWADAYS THE ELVES ARE MORE LIKELY TO CHASE YOU AWAY]
BEFORE:   Bossu: [如今那些精灵更可能把你赶走，而不是跟你做生意，所以你可得留神。]
AFTER:   Bossu: [如今那些精灵更可能把你赶走，而不是跟你做生意，所以你可得留神。]
ROW CAT:O4ecfc6dc87b2085e585f | L2410 | no manual edit
EN: [RATHER THAN PARTAKE OF TRADE, SO BE ON YOUR GUARD.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ode8b336b93b6fb4096bd | L2411 | no manual edit
EN: [...AND MAUSER?]
BEFORE:   Bossu: [……还有，毛瑟？]
AFTER:   Bossu: [……还有，毛瑟？]
ROW CAT:Oceffdec89b28559243fe | L2412 | no manual edit
EN: [Y-YEAH BOSSU?]
BEFORE:   Mauser: [是、是，BOSSU？]
AFTER:   Mauser: [是、是，BOSSU？]
ROW CAT:O21b65772d7daa4dbb724 | L2413 | no manual edit
EN: [PLEASE REVIEW THE OPERATION NOTES MORE THOROUGHLY.]
BEFORE:   Bossu: [请把行动笔记再仔细通读一遍。]
AFTER:   Bossu: [请把行动笔记再仔细通读一遍。]
ROW CAT:Oee5ac96f898f7023edfd | L2414 | EDIT E08-023
EN: [GOOD TO KNOW SOME FOLKS ARE PAYING ATTENTION.]
BEFORE:   Yiffai: [知道还有人在认真听着，真不错。]
AFTER:   Yiffai: [还好有人认真做了功课。]
ROW CAT:O9e08866d24a2a16e2274 | L2415 | no manual edit
EN: [THANKS A LOT, BOSSU!]
BEFORE:   Yiffai: [太感谢了，BOSSU！]
AFTER:   Yiffai: [太感谢了，BOSSU！]
### P08-012 | action=apply
原问题：paying attention承接Bossu认真看行动笔记、纠正Mauser资料，不是“认真听着”外勤说话。保留年轻主角略带揶揄的感谢，不写成全员无能。
本轮理由：paying attention接Bossu做足任务准备并纠错，而不是正在听通讯；只改主角揶揄节点，其余合适台词保留。
EDIT_IDS ["E08-023"]

## SC9a688dbe085a347d | sfw | datadm/all.ds | Tomcat.AreaH_map02_a noselect
CONTROL L2582 <Tomcat.AreaH_map02_a noselect>
ROW SFWe4874fffc9805a4f8fd2451a | L2583 | EDIT E08-031
EN: [OH HEY! FINALLY FOUND A PROPER TRAINER TAZER, HUH?]
BEFORE:   Tomcat: [哦，嘿！终于找到一把像样的训练电击器了？]
AFTER:   Tomcat: [哦，嘿！终于找到一把像样的驯兽电击枪了？]
ROW SFW3c455fbaf48f200592ba1b29 | L2584 | no manual edit
EN: [YUP, NOW I CAN CAPTURE A FEW OF THE CREATURES DOWN HERE]
BEFORE:   Yiffai: [对，现在能抓几只这里的生物了，]
AFTER:   Yiffai: [对，现在能抓几只这里的生物了，]
ROW SFWa17096296e21870a4c5a3248 | L2585 | no manual edit
EN: [AND WE CAN SORT WHAT'S HAPPENING ON THIS PLANET.]
BEFORE:   Yiffai: [我们也就能弄清这颗星球发生了什么。]
AFTER:   Yiffai: [我们也就能弄清这颗星球发生了什么。]
ROW SFWad567767bbeb5a6cf4b786ff | L2586 | no manual edit
EN: [JUST REMEMBER, AGENT.]
BEFORE:   Bossu: [记住，特工。]
AFTER:   Bossu: [记住，特工。]
ROW SFW7a78facc8910b8483220a39f | L2587 | EDIT E08-032
EN: [IN ORDER TO STUDY LOCAL LIFE CLOSELY, YOU MUST DEFEAT]
BEFORE:   Bossu: [为了就近研究当地生命，你必须在战斗中使用驯兽电击枪击败它们。]
AFTER:   Bossu: [要近距离研究当地生物，你必须在战斗中用驯兽电击枪击败它们。]
ROW SFW880bdbb3782319b3b878c8a3 | L2588 | no manual edit
EN: [THEM IN COMBAT USING THE TRAINER TAZER.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW4fc9344aa4db5b93e1570b30 | L2589 | no manual edit
EN: [DOING SO ALLOWS THE OBSERVATION UNITS TO PICK UP FAUNA]
BEFORE:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
AFTER:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
ROW SFW5cc81a4db8e41f956e1ffa3f | L2590 | no manual edit
EN: [SO THAT YOU MAY OBSERVE THEM CLOSER IN THE HANGAR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW448426cb4c390e5d8c330eb3 | L2591 | no manual edit
EN: [OF COURSE! STANDARD PROTOCOL. I'M ON IT.]
BEFORE:   Yiffai: [当然！标准流程。我这就去办。]
AFTER:   Yiffai: [当然！标准流程。我这就去办。]
### P08-021 | action=apply
原问题：同场Trainer Tazer先“训练电击器”后“驯兽电击枪”，容易误认为两件装备；统一本场功能名，保持与Trainee新人武器区分。此提案两人台词中间仍有对话，应用不得跨说话人或控制事件合并。
本轮理由：同场两处Trainer Tazer应同一功能名；沿已有“驯兽电击枪”而非强推新词，保留与Trainee的区分及不同说话人节点。
EDIT_IDS ["E08-031", "E08-032"]

## SCe3bb6029d395b6a3 | nsfw | datadm/all.ds | TomcatItems.KoboBody
CONTROL L4233 <TomcatItems.KoboBody>
ROW CAT:O5e4ddef25efcd5a48da9 | L4234 | no manual edit
EN: [THAT SEEMS TO BE THE BODY PORTION OF SOME SORT OF...]
BEFORE:   Tomcat: [这好像是某种……服装的衣身部分]
AFTER:   Tomcat: [这好像是某种……服装的衣身部分]
ROW CAT:O63fa9747ea736593fbc6 | L4235 | no manual edit
EN: [...SCALE SUIT?]
BEFORE:   Tomcat: [……鳞皮套装？]
AFTER:   Tomcat: [……鳞皮套装？]
ROW CAT:O2ef1f27be3f89fc1dc13 | L4236 | no manual edit
EN: [SEEMS KINDA WEIRD. CAN YOU FILL ME IN ON IT?]
BEFORE:   Yiffai: [感觉怪怪的。给我讲讲呗？]
AFTER:   Yiffai: [感觉怪怪的。给我讲讲呗？]
ROW CAT:O9b9f60ca039e4299a149 | L4237 | no manual edit
EN: [WELLLL SOME FOLKS I KNEW BACK AT THE ACADEMY WERE REALLY]
BEFORE:   Tomcat: [这个嘛，我在学院认识的一些家伙特别热衷于扮成别的种族……]
AFTER:   Tomcat: [这个嘛，我在学院认识的一些家伙特别热衷于扮成别的种族……]
ROW CAT:O68a6fce8a74ac9664521 | L4238 | no manual edit
EN: [INTO DRESSING UP AS OTHER SPECIES...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oddf9ec4817f064fc2bb1 | L4239 | no manual edit
EN: [WASN'T REALLY MY THING, BUT I USED TO TAKE PART NOW AND]
BEFORE:   Tomcat: [我不算特别喜欢，但以前偶尔也会玩玩，主要是他们还有些很棒的玩具可以配着——]
AFTER:   Tomcat: [我不算特别喜欢，但以前偶尔也会玩玩，主要是他们还有些很棒的玩具可以配着——]
ROW CAT:O98b697140e8ce6e2943a | L4240 | no manual edit
EN: [AGAIN, MOSTLY 'CUS THEY HAD GREAT TOYS TO GO ALONG WI-]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ob4991a60cdb3aa9518d4 | L4241 | no manual edit
EN: [THAT IS  N O T  WHAT THIS OUTFIT IS FOR!!]
BEFORE:   Yiffai: [这套衣服绝、对、不、是干那个用的！！]
AFTER:   Yiffai: [这套衣服绝、对、不、是干那个用的！！]
ROW CAT:O4bdd112bcc35128fb6f5 | L4242 | no manual edit
EN: [...RIGHT?]
BEFORE:   Yiffai: [……对吧？]
AFTER:   Yiffai: [……对吧？]
ROW CAT:Oc2c225656c44ae19718c | L4243 | EDIT E08-024
EN: [YOU'LL HAVE TO FIND SOMEONE LESS PURR- VERTED THAN TOMCAT]
BEFORE:   Mauser: [你得找个没汤姆猫那么色、那么喵的家伙，给你讲讲这套衣服的用途了，伊法伊！]
AFTER:   Mauser: [伊法伊，想弄清这套衣服的用途，你得找个没Tomcat那么色的家伙来问！]
ROW CAT:O035264e976fac2b5f223 | L4244 | no manual edit
EN: [TO TELL YOU WHAT THAT SUIT IS FOR, YIFFAI!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oaa261154aaebe0f71a1c | L4245 | no manual edit
EN: [HMMMPH!]
BEFORE:   Yiffai: [哼嗯！]
AFTER:   Yiffai: [哼嗯！]
CONTROL L4247 ### Elf ###
### P08-014 | action=apply
原问题：purr-verted是针对猫的perverted双关，不独立表示“那么喵”的性格属性。当前并列形容词破坏意思，宜先保住熟人挖苦；中文猫双关若不能自然建立，不强凑。
本轮理由：purr-verted是猫谐音式挖苦，不是色与喵两种并列属性；用自然损友口吻，Tomcat按本轮明确命名保英文。完整合句保留询问衣服用途及伊法伊称呼。
EDIT_IDS ["E08-024"]

## SC02a295fdd4ce3288 | nsfw | datadm/all.ds | TomcatItems.SpecialKeycard2
CONTROL L4312 <TomcatItems.SpecialKeycard2>
ROW CAT:O92f5dbaabaf35d253fc3 | L4313 | no manual edit
EN: [IN ORDER TO USE A KEYCARD, ALL YOU HAVE TO DO IS]
BEFORE:   Tomcat: [要使用门卡，只需要带着卡走向能量门就行。]
AFTER:   Tomcat: [要使用门卡，只需要带着卡走向能量门就行。]
ROW CAT:Od2fe21f56accd9875e53 | L4314 | no manual edit
EN: [WALK INTO AN ENERGY DOOR WHILE HOLDING ONE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc91c83e4cdc8b678f7ca | L4315 | EDIT E08-025
EN: [YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!]
BEFORE:   Tomcat: [可打开等级不高于门上所标数字的门！]
AFTER:   Tomcat: [门卡上标的等级，就是它能开启的最高门禁等级！]
### P08-015 | action=apply
原问题：up to level displayed on them指门卡可开到其标示等级的门。当前“等级不高于门上所标数字的门”成了门与自身等级比较，丢掉卡片上限，误导玩法。关联本包Keycard3 UI“至3级”可交叉佐证。
本轮理由：up to为门卡开启等级上限，不是门与自身数字比较；保留前两行已合句及空尾，只修错指代节点，不增加按键。
EDIT_IDS ["E08-025"]

## SC9dff794087b1ab97 | nsfw | datav/dictionary.json | CosmoHead
ROW CAT:O3928c3df4af4c4bda759 | L- | no manual edit
EN: STARHELM
BEFORE: 星盔
AFTER: 星盔
ROW CAT:O83e5a0026bd38da12dbf | L- | EDIT E08-026
EN: SPACE-PROOF|COSMO HELMET.
BEFORE: 防太空|宇宙头盔。
AFTER: 适用于太空的|宇宙头盔。
### P08-016 | action=apply
原问题：“防太空”不是自然的防护属性表达；只说明头盔适合太空环境，不保证单戴即可太空行走。管线分隔保留，排版另验。
本轮理由：space-proof说明头盔适用环境，不是防止太空，也不等于单件可太空行走；保留管线及宇宙头盔名称。
EDIT_IDS ["E08-026"]

## SC2a2f11f81441cfdd | sfw | datav/dictionary.json | CosmoHead
ROW SFW2223339b9c447c9f7766170b | L- | EDIT E08-027
EN: SPACE-PROOF|COSMO HELMET.
BEFORE: 防太空|宇宙头盔。
AFTER: 适用于太空的|宇宙头盔。
ROW SFWa493a27751aef85806fb2884 | L- | no manual edit
EN: STARHELM
BEFORE: 星盔
AFTER: 星盔
### P08-017 | action=apply
原问题：SFW独立场景同样“防太空”生硬；单独保留ID，不把内容版本合并为同一审读实体。
本轮理由：独立核SFW相同说明，space-proof同样是适用环境；不从NSFW引入额外功能，管线保留。
EDIT_IDS ["E08-027"]

## SC756e1e2f94e81d2c | nsfw | datav/dictionary.json | ui.data.f_AgentFZ5
ROW CAT:O16ef7c2719ad81fc827e | L- | no manual edit
EN: PART 5 OF THE FENFEN STORY.|$IN YOUR MIND, THIS ECHOES:|$[HEART IS NOT TOUCH CROSS]
BEFORE: Fenfen故事第5部分。|$在你脑中回响着：|$[心不接触十字]
AFTER: Fenfen故事第5部分。|$在你脑中回响着：|$[心不接触十字]
### P08-022 | action=defer
原问题：排序谜题线索中的touch可能指相邻，也可能有特定图形接触规则；“心不接触十字”不够明确。但未核谜题界面和判定，以上仅潜在玩法风险方向，不确认错译，不立即替换。
本轮理由：touch在谜题中是否等于相邻、接触或另有图形规则未核界面与判定。现文未确认错误，不能将“不接触”收窄为“不相邻”；待获得规则和界面证据再裁决。
EDIT_IDS []

## SC0288b8c93129d093 | nsfw | vsn/f_ClassicWerehund/script.vsn | vsn/f_ClassicWerehund/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L3 fade(9, 0, 1)
CONTROL L4 fadein(1.0, 4): YiffanyCloseupGrin
CONTROL L5 rewind!
ROW CAT:Oe307a079d8c2d778f585 | L6 | no manual edit
EN: Allllriiiight big boy, had enough yet? You've finally calmed down!
BEFORE: text: 好啦，大个子，闹够没？总算安静了！
AFTER: text: 好啦，大个子，闹够没？总算安静了！
ROW CAT:Oc4e7296cc8b72f16d670 | L7 | no manual edit
EN: Just sit back while I show you what Cosmo- breeding is all about.
BEFORE: text: 乖乖躺好，让你见识什么叫宇宙育种。
AFTER: text: 乖乖躺好，让你见识什么叫宇宙育种。
ROW CAT:O19ed1af19eeaf4da5b0e | L8 | no manual edit
EN: Gotta get my favorite jacket off so it doesn't get dirty and th-
BEFORE: text: 得先脱掉我最爱的夹克，免得弄脏，然后——
AFTER: text: 得先脱掉我最爱的夹克，免得弄脏，然后——
CONTROL L10 fadecut(0.266, 2): ClassicAreaB01N
CONTROL L11 rewind!
ROW CAT:O447468eceee608dd9609 | L12 | no manual edit
EN: Ow what? What are you doing you big goof?
BEFORE: text: 哎哟，什么呀？你这大傻瓜想干嘛？
AFTER: text: 哎哟，什么呀？你这大傻瓜想干嘛？
ROW CAT:O6bd12b697c1e93411d03 | L13 | EDIT E08-028
EN: You don't want me to kick your tail AGAIN, do ya?
BEFORE: text: 你总不想再被我一尾巴踹过去吧？ 
AFTER: text: 你总不想再让我揍一顿吧？
ROW CAT:Oe16d597fcab7b5b5ff6b | L14 | no manual edit
EN: So back down before I... Before I...
BEFORE: text: 所以赶紧退下，不然我……不然我……
AFTER: text: 所以赶紧退下，不然我……不然我……
CONTROL L16 fadecut(0.266, 2): ClassicAreaB01A
CONTROL L17 rewind!
CONTROL L18 sfxcue: ClassicAreaB01A {
CONTROL L19   play [ClassicYiffaiXSlap5] at [2]
CONTROL L20 }
ROW CAT:O6c2d6586b98614930f94 | L21 | no manual edit
EN: ...oooh, you just wanted to get a head start, didn't ya boy?
BEFORE: text: ……哦，你就是想抢先开干，对吧，狗狗？
AFTER: text: ……哦，你就是想抢先开干，对吧，狗狗？
ROW CAT:Of2b18357248c418fb5c0 | L22 | no manual edit
EN: It was beginning to feel like nobody on this planet wanted to rut!
BEFORE: text: 我都快以为这星球上没谁想交配了！
AFTER: text: 我都快以为这星球上没谁想交配了！
ROW CAT:Obd6becd4e08d5b44ba5b | L23 | no manual edit
EN: Thankfully you seemed to have read my mind <3
BEFORE: text: 幸好你好像看透了我的心思 <3
AFTER: text: 幸好你好像看透了我的心思 <3
CONTROL L25 fadecut(0.266, 2): ClassicAreaB01BShort
CONTROL L26 rewind!
CONTROL L27 sfxcue: ClassicAreaB01BShort {
CONTROL L28   play [ClassicYiffaiXSlap8] at [4, 9, 14, 19]
CONTROL L29 }
ROW CAT:O2bbc4ab7104ebb000a4b | L30 | no manual edit
EN: R-real eager, ain't ya? Watch those claws!
BEFORE: text: 还、还真心急啊你？当心爪子！
AFTER: text: 还、还真心急啊你？当心爪子！
ROW CAT:O1d60c369edcb542b080d | L31 | no manual edit
EN: Don't wanna be running around freeing other agents on this planet
BEFORE: text: 我可不想两条腿都被抓得一道道的，还满星球跑着救其他特工。
AFTER: text: 我可不想两条腿都被抓得一道道的，还满星球跑着救其他特工。
ROW CAT:O7dc7d391305c6dca8cd1 | L32 | no manual edit
EN: with my legs all scratched up.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obf684b88fa9eb36521da | L33 | no manual edit
EN: It's practically indecent to show off like that!
BEFORE: text: 这么显摆，简直有伤风化！
AFTER: text: 这么显摆，简直有伤风化！
CONTROL L35 fadecut(0.266, 2): ClassicAreaB01DShort
CONTROL L36 rewind!
CONTROL L37 sfxcue: ClassicAreaB01DShort {
CONTROL L38   play [ClassicYiffaiXSlap5] at [6]
CONTROL L39 }
ROW CAT:O8bfc957b822cdda6a0c1 | L40 | no manual edit
EN: Theeere you go, finally hitting the target <3 <3
BEFORE: text: 对——就是这样，终于射中靶心啦<3 <3 
AFTER: text: 对——就是这样，终于射中靶心啦<3 <3 
ROW CAT:O05c8f168f413e803c55e | L41 | no manual edit
EN: Don't be afraid to fill me up, I always carry some Estrafin on me!
BEFORE: text: 放心把我灌满吧，我随身都带着 Estrafin！ 
AFTER: text: 放心把我灌满吧，我随身都带着 Estrafin！ 
ROW CAT:O0b05cac644cb213c2aa2 | L42 | no manual edit
EN: So even if we're species compatible I won't get knocked up.
BEFORE: text: 所以就算物种相容，我也不会怀孕。
AFTER: text: 所以就算物种相容，我也不会怀孕。
ROW CAT:O2e4dc7afc3bc83b8072c | L43 | no manual edit
EN: ...or, I did, until my gear got stolen.
BEFORE: text: ……至少，装备被偷前是这样。
AFTER: text: ……至少，装备被偷前是这样。
CONTROL L45 fadecut(0.266, 2): ClassicAreaB01EShort
CONTROL L46 rewind!
CONTROL L47 sfxcue: ClassicAreaB01EShort {
CONTROL L48   play [ClassicYiffaiXSlap7] at [1]
CONTROL L49 }
ROW CAT:O8f64582dd619656a4b25 | L50 | no manual edit
EN: B-but I'm sure I could find some again, on the very slim chance
BEFORE: text: 不、不过，万一咱俩恰好完全合得来，能一起生个宝宝，我肯定还能再弄到些！虽然这可能性微乎其微。
AFTER: text: 不、不过，万一咱俩恰好完全合得来，能一起生个宝宝，我肯定还能再弄到些！虽然这可能性微乎其微。
ROW CAT:Ofa60c615bbc14c7e45cb | L51 | no manual edit
EN: that we happen to be perfect to make a baby together!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Odb8980182435e1c29e59 | L52 | no manual edit
EN: Aww, what's wrong, turn you off? At this rate your knot won't tie inside of me...
BEFORE: text: 哎呀，怎么了，扫兴啦？这样你的肉结可锁不住我……
AFTER: text: 哎呀，怎么了，扫兴啦？这样你的肉结可锁不住我……
CONTROL L54 fadecut(0.266, 2): ClassicAreaB01B
CONTROL L55 rewind!
CONTROL L56 sfxcue: ClassicAreaB01B {
CONTROL L57   play [ClassicYiffaiXSlap8] at [2]
CONTROL L58 }
ROW CAT:Ob306df860d633351f922 | L59 | no manual edit
EN: ...hold on there, you're gonna keep on thrusting? What a GOOD boy!
BEFORE: text: ……等等，你还要继续插？真是乖狗狗！
AFTER: text: ……等等，你还要继续插？真是乖狗狗！
ROW CAT:O882c8c68d0b6f7416add | L60 | no manual edit
EN: Nnnf, who taught you how to do this little trick, huh?
BEFORE: text: 嗯呃，谁教会你这小花招的，嗯？
AFTER: text: 嗯呃，谁教会你这小花招的，嗯？
ROW CAT:Od26574a966de491be47b | L61 | no manual edit
EN: I gotta thank them, whoever they are. Most ferals stop once the knot swells up.
BEFORE: text: 不管是谁教的，我都得谢谢。多数野性兽人一涨起肉结就停了。
AFTER: text: 不管是谁教的，我都得谢谢。多数野性兽人一涨起肉结就停了。
CONTROL L63 fadecut(0.266, 2): ClassicAreaB01DDeep
CONTROL L64 rewind!
CONTROL L65 sfxcue: ClassicAreaB01DDeep {
CONTROL L66   play [ClassicYiffaiXSlap1] at [4]
CONTROL L67 }
ROW CAT:Ob23fa44507c0667ae78d | L68 | no manual edit
EN: D-damn... you're r-really stirring me up now...
BEFORE: text: 可、可恶……你真把我搅、搅得欲火焚身了……
AFTER: text: 可、可恶……你真把我搅、搅得欲火焚身了……
ROW CAT:Occ5e84efc3820ba2ac0f | L69 | no manual edit
EN: Gotta admit that I was looking forward to a tie, but with how good you thrust
BEFORE: text: 不得不说，我本来还盼着锁结，可你插得这么爽，这份安慰奖也真是相当不错！
AFTER: text: 不得不说，我本来还盼着锁结，可你插得这么爽，这份安慰奖也真是相当不错！
ROW CAT:O3dfc7a918081a1ed7841 | L70 | no manual edit
EN: this is a preeeetty good consolation prize!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L72 fadecut(0.266, 2): ClassicAreaB01E
CONTROL L73 rewind!
CONTROL L74 sfxcue: ClassicAreaB01E {
CONTROL L75   play [ClassicYiffaiXSlap7] at [1]
CONTROL L76 }
ROW CAT:Ofeff8f51c3d0b105c516 | L77 | no manual edit
EN: Just gotta give you another moment or two, and maybe some of that doggy cream
BEFORE: text: 再给你一小会儿，说不定那些狗狗精液就能蹭进我里面了！
AFTER: text: 再给你一小会儿，说不定那些狗狗精液就能蹭进我里面了！
ROW CAT:O5326c52a3731736105ac | L78 | no manual edit
EN: will rub off in me!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ocdd2dd48340608c20760 | L79 | no manual edit
EN: ...or rub in, off me?
BEFORE: text: ……还是蹭进去、蹭出我身体？
AFTER: text: ……还是蹭进去、蹭出我身体？
ROW CAT:O2e6b6bd07f1e30c29234 | L80 | no manual edit
EN: Whatever! Just k-keep at it, stud!
BEFORE: text: 随便啦！继、继续，猛男！
AFTER: text: 随便啦！继、继续，猛男！
CONTROL L82 fadecut(0.266, 2): ClassicAreaB01O
CONTROL L83 rewind!
CONTROL L84 sfxcue: ClassicAreaB01O {
CONTROL L85   play [ClassicYiffaiXBlink1] at [4]
CONTROL L86 }
ROW CAT:O9bd79ab92b9572781408 | L87 | no manual edit
EN: Uh w-wait... You aren't getting... thicker, are you?
BEFORE: text: 呃，等、等等……你不会……在变粗吧？
AFTER: text: 呃，等、等等……你不会……在变粗吧？
ROW CAT:O9ebc0f713f5e3ddcb712 | L88 | no manual edit
EN: That's actually getting a bit rough now, h-hey!
BEFORE: text: 现在可有点太粗暴了，喂、喂！
AFTER: text: 现在可有点太粗暴了，喂、喂！
ROW CAT:O4c1c4fe2ac0c5c04e880 | L89 | no manual edit
EN: Settle down a bit boy! Gimme a second!
BEFORE: text: 冷静点，小子！让我缓口气！
AFTER: text: 冷静点，小子！让我缓口气！
CONTROL L91 fadecut(0.266, 2): ClassicAreaB01DDeep2
CONTROL L92 rewind!
CONTROL L93 sfxcue: ClassicAreaB01DDeep2 {
CONTROL L94   play [ClassicYiffaiXSlap1] at [3]
CONTROL L95 }
ROW CAT:Ocfcd32e763928f6c1458 | L96 | no manual edit
EN: D-damn it! I thought your knot was out already? If you keep thrusting like that
BEFORE: text: 该、该死！我还以为你的肉结早就胀起来了呢？再这样顶下去，那、那你就可能顶进我的……
AFTER: text: 该、该死！我还以为你的肉结早就胀起来了呢？再这样顶下去，那、那你就可能顶进我的……
ROW CAT:O98aa52a454e49412dac4 | L97 | no manual edit
EN: then y-you might press into my...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O85f7a284f82a70c606d7 | L98 | no manual edit
EN: ...my...!!
BEFORE: text: ……我的……！！
AFTER: text: ……我的……！！
CONTROL L100 sync!
CONTROL L101 queue: ClassicAreaB01D3DeepToCum
CONTROL L102 sfxcue: ClassicAreaB01D3DeepToCum {
CONTROL L103   play [ClassicYiffaiXSlap1] at [3, 11, 15, 19]
CONTROL L104     play [ClassicYiffaiXTwitch2] at [22, 24, 30, 34, 38, 42]
CONTROL L105   play [ClassicYiffaiXShoot1] at [46]
CONTROL L106 }
CONTROL L108 sync!
CONTROL L109 queue: ClassicAreaB01D2Cum
CONTROL L110 rewind!
CONTROL L111 sfxcue: ClassicAreaB01D2Cum {
CONTROL L112   play [ClassicYiffaiXTwitch2] at [6, 24]
CONTROL L113   play [ClassicYiffaiXShoot1] at [17]
CONTROL L114 }
ROW CAT:O6e14e650b2247c2c5edf | L115 | no manual edit
EN: Oh... ohmygosh... y-you really did get thicker...
BEFORE: text: 哦……天哪……你、你还真变粗了……
AFTER: text: 哦……天哪……你、你还真变粗了……
ROW CAT:O0b313379484471972970 | L116 | no manual edit
EN: D-damn, what a breeder...<3 my turn to catch my breath... huff...
BEFORE: text: 该、该死，真是配种猛将……<3 轮到我喘口气了……呼……
AFTER: text: 该、该死，真是配种猛将……<3 轮到我喘口气了……呼……
CONTROL L118 fadecut(0.266, 2): ClassicAreaB01H
CONTROL L119 rewind!
ROW CAT:O8d71843c27637d5b5784 | L120 | no manual edit
EN: Y-yeah that's it, just settle down a bit while I... ahh!
BEFORE: text: 对、对，就是这样，先安分点，让我……啊！
AFTER: text: 对、对，就是这样，先安分点，让我……啊！
ROW CAT:O020f13d4ae19cb7b4ad8 | L121 | no manual edit
EN: Your knot's so good that it makes me glad I didn't waste my time
BEFORE: text: 你这肉结太舒服了，真庆幸之前没把时间浪费在那只蓝毛小不点狗崽身上！
AFTER: text: 你这肉结太舒服了，真庆幸之前没把时间浪费在那只蓝毛小不点狗崽身上！
ROW CAT:Occbfea037cef4d592de6 | L122 | no manual edit
EN: on that other little blue furred pupper pipsqueak earlier!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L124 fadecut(0.266, 2): ClassicAreaB01J
CONTROL L125 rewind!
ROW CAT:O6e0b31dcb3af29ab0668 | L126 | no manual edit
EN: [My dear "Yiffany", it's only thanks to the fact that you left my son alone]
BEFORE: text: [亲爱的“伊法妮”，只因你没对我儿子下手，]
AFTER: text: [亲爱的“伊法妮”，只因你没对我儿子下手，]
ROW CAT:O56161aa737ae923c6bfb | L127 | EDIT E08-029
EN: [that I decided to play along with your little round of roughhousing.]
BEFORE: text: [吾才决定陪汝玩一场小小的打闹。]
AFTER: text: [我才决定陪你玩这一场小小的打闹。]
ROW CAT:O3a2c55905c5e752ed7da | L128 | no manual edit
EN: [Please, have a mere taste of what an Esper like me is capable of!]
BEFORE: text: [来，稍稍领教一下我这样的超能力者有何本领！]
AFTER: text: [来，稍稍领教一下我这样的超能力者有何本领！]
CONTROL L130 sync!
CONTROL L131 queue: ClassicAreaB01J2
CONTROL L132 sfxcue: ClassicAreaB01J2 {
CONTROL L133   play [YiffaiPsyAbility] at [4]
CONTROL L134 }
CONTROL L136 sync!
CONTROL L137 fadecut(0.266, 2): ClassicAreaB01H2
CONTROL L138 rewind!
ROW CAT:Oddbbb75251c8041be1a2 | L139 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O884e9cb3fa9505011f40 | L140 | no manual edit
EN: ...bark!?!?
BEFORE: text: ……汪！？！？
AFTER: text: ……汪！？！？
CONTROL L142 fadecut(0.266, 2): ClassicAreaB01F
CONTROL L143 rewind!
ROW CAT:O40954a0487bef535787e | L144 | no manual edit
EN: [That's right my dear, you are indeed now a feral yourself.]
BEFORE: text: [没错，亲爱的，你现在确实也成了兽形。]
AFTER: text: [没错，亲爱的，你现在确实也成了兽形。]
ROW CAT:O4450d7ba9700cd6a3202 | L145 | no manual edit
EN: [Now please forgive me for "wasting your time"...]
BEFORE: text: [那么，请原谅我要“浪费你的时间”了……]
AFTER: text: [那么，请原谅我要“浪费你的时间”了……]
ROW CAT:Obb10b476fa1d0425d5a2 | L146 | no manual edit
EN: [...as I put your body to the test so that you may grow accustomed to it...]
BEFORE: text: [……我要考验一下你的身体，好让你习惯这副模样……]
AFTER: text: [……我要考验一下你的身体，好让你习惯这副模样……]
CONTROL L148 fadecut(0.266, 2): ClassicAreaBlackAnimation
CONTROL L149 rewind!
CONTROL L150 sfxcue: ClassicAreaBlackAnimation {
CONTROL L151   play [ClassicYiffaiXSlap3] at [6]
CONTROL L152 }
ROW CAT:Oeeb4076c029b448b4628 | L153 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:Of496276846549936248c | L154 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O1ddc351276f55fb2d84b | L155 | no manual edit
EN: ...*whine*...
BEFORE: text: ……*呜咽*……
AFTER: text: ……*呜咽*……
CONTROL L157 fadecut(0.266, 2): ClassicAreaB01Q
CONTROL L158 rewind!
ROW CAT:O9ee4331f18a5f7c879e6 | L159 | no manual edit
EN: Th-there... I'm finally back on two legs again...
BEFORE: text: 好、好了……总算又能两条腿站着了……
AFTER: text: 好、好了……总算又能两条腿站着了……
ROW CAT:O2292c260fee213f9e3bb | L160 | no manual edit
EN: A-and that big fellar ran off somewhere, s-so now I can...
BEFORE: text: 而、而且那大家伙也跑没影了，这、这样我就能……
AFTER: text: 而、而且那大家伙也跑没影了，这、这样我就能……
ROW CAT:O9694d87545bba15984ed | L161 | no manual edit
EN: ...I can make a break for it... ow...
BEFORE: text: ……我能趁机跑了……哎哟……
AFTER: text: ……我能趁机跑了……哎哟……
CONTROL L163 sync!
CONTROL L164 queue: ClassicAreaB01QToQ2
CONTROL L166 sync!
CONTROL L167 queue: ClassicAreaB01Q2
CONTROL L168 rewind!
ROW CAT:O5860daec9bb7192b3044 | L169 | no manual edit
EN: Gee papa, are you sure that yellow dog lady is really the chosen one?
BEFORE: text: 爸爸，你确定那位黄毛狗女士真是天选之人吗？
AFTER: text: 爸爸，你确定那位黄毛狗女士真是天选之人吗？
CONTROL L171 fadecut(0.266, 2): ClassicAreaB01R
CONTROL L172 rewind!
ROW CAT:O85906cc0c624726b9b43 | L173 | no manual edit
EN: That lady, Yiffany, mastered one of the Zener powers in record time
BEFORE: text: 那位伊法妮女士，以破纪录的速度掌握了一种泽纳之力，所以我深信，她就是解放这颗星球的人。
AFTER: text: 那位伊法妮女士，以破纪录的速度掌握了一种泽纳之力，所以我深信，她就是解放这颗星球的人。
ROW CAT:Ocf253289dd1ddd2e648b | L174 | no manual edit
EN: so I have no doubt that she will be the one to set this planet free.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6fe1da1871f1fcaf9448 | L175 | no manual edit
EN: That sounds so cool! She's a real superhero, isn't she dad?
BEFORE: text: 听着好酷！她真是超级英雄，对吧，爸爸？
AFTER: text: 听着好酷！她真是超级英雄，对吧，爸爸？
ROW CAT:Oe4e80dd01f8fa7e811f8 | L176 | no manual edit
EN: I wish I could train with her next time. Can I dad? Can I??
BEFORE: text: 下次真想跟她一起训练。爸爸，可以吗？可以吗？？
AFTER: text: 下次真想跟她一起训练。爸爸，可以吗？可以吗？？
CONTROL L178 fadecut(0.266, 2): Black
CONTROL L179 rewind!
ROW CAT:Oa00348e244efafe1d34a | L180 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:Oe0b91b9b9d5bc189ccb9 | L181 | no manual edit
EN: ...maybe when you're older, son.
BEFORE: text: ……等你再大些吧，儿子。
AFTER: text: ……等你再大些吧，儿子。
CONTROL L183 fadeout(1.0, 1.0, 4)
### P08-018 | action=apply
原问题：kick your tail是揍对方/教训对方，不是“用我一尾巴踹过去”。现译凭空添了动作器官与施力方式。按镜头已切到对方反制后的反问，保留她嘴硬而未说完的威胁。
本轮理由：kick your tail是再次揍对方，不是用尾巴施力；只修该完整物理行，前后嘴硬威胁和中断节点原样不动。
EDIT_IDS ["E08-028"]
### P08-019 | action=apply
原问题：同一人同一段从自然称呼突然切到“吾/汝”，没有英文对应古语证据；超能力/父亲身份不授权奇幻腔。保留方括号表示的演出层差别，不把narrator元数据当实际发言角色。
本轮理由：父亲同段仅该槽突然吾汝，无英文古语依据；改现代庄重口吻，保留前槽“只因”限定和后槽Esper能力邀请，方括号原样。
EDIT_IDS ["E08-029"]

## SCb067f24e0154e7af | nsfw | vsn/m_GameOverAreaB/script.vsn | vsn/m_GameOverAreaB/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 snap: ClassicGameOverAreaBA
CONTROL L3 waitForCue!
CONTROL L4 rewind!
ROW CAT:Od73defbb0ea500ceb1c9 | L5 | no manual edit
EN: Owie owie ow...
BEFORE: text: 疼疼疼……
AFTER: text: 疼疼疼……
ROW CAT:Offba67b1d9d2b3cfe4b8 | L6 | no manual edit
EN: That was a much harder bump than I was expecting...
BEFORE: text: 这下撞得可比我想的狠多了……
AFTER: text: 这下撞得可比我想的狠多了……
ROW CAT:O82d0605520dc0fe51eb8 | L7 | no manual edit
EN: Time to put that cosmo training to use and collect any data I can...
BEFORE: text: 该用上宇宙训练，尽量收集数据了……
AFTER: text: 该用上宇宙训练，尽量收集数据了……
CONTROL L9 fadeout(1.0, 1.0, 4)
CONTROL L10 cut(0.06): Black
ROW CAT:O9456de189083896c1fd3 | L11 | no manual edit
EN: ...in case anything happens...
BEFORE: text: ……以防万一出了什么事……
AFTER: text: ……以防万一出了什么事……
ROW CAT:Ocbd38724ba8b6452b81a | L12 | no manual edit
EN: ...while I...zzz....
BEFORE: text: ……在我……呼噜……
AFTER: text: ……在我……呼噜……
ROW CAT:O9871413114da8fc2aac4 | L13 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:Oa27c42ca97ee5c25a513 | L14 | no manual edit
EN: ...nnngh...?
BEFORE: text: ……嗯呃……？
AFTER: text: ……嗯呃……？
CONTROL L16 fade(9, 0, 1)
CONTROL L17 fadein(1.0, 4): ClassicGameOverAreaBB
CONTROL L18 rewind!
ROW CAT:Oc570ca9cfd9b3473f474 | L19 | no manual edit
EN: O-okay, I think I'm awake now. Sensitive Hyper Aware Recording: Enabled!
BEFORE: text: 好、好了，我应该醒了。超敏锐感知记录：启用！
AFTER: text: 好、好了，我应该醒了。超敏锐感知记录：启用！
ROW CAT:O7ba68ae49a1a6774b6d6 | L20 | no manual edit
EN: I'm not really a heavy sleeper, really! I just wasn't expecting to be
BEFORE: text: 我睡得真没那么死，真的！只是没想到会被科博德太空海盗这么热情地弄醒！
AFTER: text: 我睡得真没那么死，真的！只是没想到会被科博德太空海盗这么热情地弄醒！
ROW CAT:O8355aa0ed92c4b19c827 | L21 | no manual edit
EN: woken up by a space pirate kobold so eagerly!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O5dc9df634e079a066331 | L22 | no manual edit
EN: If I was able to wake up faste- I mean, if I had more energy, I would have ran
BEFORE: text: 要是能快点醒—我是说，再有力气些，我早就跑了，不过都是这科博德在出力，其实也没那么糟嘛！
AFTER: text: 要是能快点醒—我是说，再有力气些，我早就跑了，不过都是这科博德在出力，其实也没那么糟嘛！
ROW CAT:O37909c81de72ef197b9e | L23 | no manual edit
EN: but you know, this kobold is doing all the work so it's not that bad, really!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L25 cut(0.06): ClassicGameOverAreaBC
CONTROL L26 rewind!
ROW CAT:Oaa9a9e0a036e0e5d58b0 | L27 | no manual edit
EN: Or at least, that's what I thought at first. But then more and more kobolds came
BEFORE: text: 至少起初我是这么想的，可科博德越聚越多，好像都收到了我被逮住的消息。
AFTER: text: 至少起初我是这么想的，可科博德越聚越多，好像都收到了我被逮住的消息。
ROW CAT:O8371be2d32de6a98252b | L28 | no manual edit
EN: almost like they were getting alerted to the fact that I was caught.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oedf9301aa02c941ab93e | L29 | no manual edit
EN: Not that I was really caught, that is. I was letting them double team me
BEFORE: text: 当然，不是真被抓了。我是主动让他们双人夹攻我，还让他们把我往同伴的鸡巴上按。这可是宝贵数据！
AFTER: text: 当然，不是真被抓了。我是主动让他们双人夹攻我，还让他们把我往同伴的鸡巴上按。这可是宝贵数据！
ROW CAT:O7aa32f44729edfd7bac5 | L30 | no manual edit
EN: and I was letting them shove me down on their friend's dicks. That's valuable data!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L32 cut(0.06): ClassicGameOverAreaBD
CONTROL L33 rewind!
ROW CAT:Oa9caa87f987c217b9cdb | L34 | no manual edit
EN: Learning the "tells" that the group of kobolds had was a good test of skill too.
BEFORE: text: 学着看懂那群科博德的“信号”，也挺考验本事。
AFTER: text: 学着看懂那群科博德的“信号”，也挺考验本事。
ROW CAT:O881403a958622127b091 | L35 | no manual edit
EN: Tracking the twitching of each dick I was holding while also riding on one
BEFORE: text: 一边骑着一根，一边留意手里每根鸡巴的抽动，真让我学会了怎么把他们全伺候舒服。
AFTER: text: 一边骑着一根，一边留意手里每根鸡巴的抽动，真让我学会了怎么把他们全伺候舒服。
ROW CAT:Oec42feacc1a2712c9af4 | L36 | no manual edit
EN: really taught me how to please them all.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ob8680aeaf813c621bb4e | L37 | EDIT E08-030
EN: They knew they were in good paws at the end of our little session!
BEFORE: text: 小小交流一结束，他们就知道自己落在了好爪上！
AFTER: text: 这场小小的交流一结束，他们就知道交给我这双爪子，准能伺候得舒舒服服！
CONTROL L39 cut(0.06): ClassicGameOverAreaBE
CONTROL L40 rewind!
ROW CAT:O68a5c8403527b8fdd13b | L41 | no manual edit
EN: In hindsight, maybe I made it feel too good for the space pirates...
BEFORE: text: 现在想想，也许我把那些太空海盗伺候得太舒服了……
AFTER: text: 现在想想，也许我把那些太空海盗伺候得太舒服了……
ROW CAT:O4464d4f4856f8982f0fe | L42 | no manual edit
EN: They ended up keeping me in one of their cells, using me at any hour of the day.
BEFORE: text: 最后他们把我关进牢房，日夜随时拿我泄欲。
AFTER: text: 最后他们把我关进牢房，日夜随时拿我泄欲。
ROW CAT:O5dc22ffdf876f9da852e | L43 | no manual edit
EN: Like I was some sort of pup toy of theirs!
BEFORE: text: 搞得我像是他们的宠物狗玩具似的！
AFTER: text: 搞得我像是他们的宠物狗玩具似的！
ROW CAT:O9cf475ee50697529d010 | L44 | no manual edit
EN: I lost track of both time and my mission as I settled into my new role...
BEFORE: text: 我渐渐适应了新身份，把时间和任务都忘得一干二净……
AFTER: text: 我渐渐适应了新身份，把时间和任务都忘得一干二净……
CONTROL L46 cut(0.06): ClassicGameOverAreaBF
CONTROL L47 rewind!
ROW CAT:O1dce080cf987d34353cb | L48 | no manual edit
EN: At some point while I was chained up and waiting for my next round of fuckies
BEFORE: text: 我记得，被锁着等下一轮挨操时，有个大耳朵的家伙来过，不是海盗！
AFTER: text: 我记得，被锁着等下一轮挨操时，有个大耳朵的家伙来过，不是海盗！
ROW CAT:O3b5d86d7519611d98497 | L49 | no manual edit
EN: I recall there being some big-eared non-pirate stopping by!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O775b4c7997a76783a838 | L50 | no manual edit
EN: They didn't look like they wanted to fuck, so I wasn't really too interested...
BEFORE: text: 对方看着不像想操我，所以我没多大兴趣……
AFTER: text: 对方看着不像想操我，所以我没多大兴趣……
ROW CAT:O654a9546d3075fe1ed06 | L51 | no manual edit
EN: ...in fact, they seemed like they wanted to help me or something?
BEFORE: text: ……倒像是想帮我，还是怎么的？
AFTER: text: ……倒像是想帮我，还是怎么的？
CONTROL L53 cut(0.06): ClassicGameOverAreaBG
CONTROL L54 rewind!
ROW CAT:O0a32694f4ee0a32863a3 | L55 | no manual edit
EN: Another, bigger one came along and seemed to tell the smaller to leave me alone
BEFORE: text: 又来了个更大的，好像叫那个小的别再烦我，像是早就见识过业务能力超强的特工似的！
AFTER: text: 又来了个更大的，好像叫那个小的别再烦我，像是早就见识过业务能力超强的特工似的！
ROW CAT:O410ac8328eb466678a42 | L56 | no manual edit
EN: like they were familiar with agents that were super awesome at their jobs!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O1c87f56be14a51c8c773 | L57 | no manual edit
EN: Yeah, that must be it. They didn't want to get in the way of my skills!
BEFORE: text: 对，肯定是这样。他们不想妨碍我大展身手！ 
AFTER: text: 对，肯定是这样。他们不想妨碍我大展身手！ 
CONTROL L59 cut(0.06): Black
ROW CAT:O4d986d721e2459c648f8 | L60 | no manual edit
EN: But nevermind them. Let's get back to the fun stuff!
BEFORE: text: 不过别管他们了！接着说好玩的吧！
AFTER: text: 不过别管他们了！接着说好玩的吧！
CONTROL L62 cut(0.06): ClassicGameOverAreaBH
CONTROL L63 rewind!
ROW CAT:Oabc068b35e5d8ae84fb2 | L64 | no manual edit
EN: Like when I got upgraded from an iron shackle to a shiny new collar!
BEFORE: text: 比如我的铁脚镣升级成了闪亮的新项圈！
AFTER: text: 比如我的铁脚镣升级成了闪亮的新项圈！
ROW CAT:Oe58be9244449f6ac492d | L65 | no manual edit
EN: That was a definite sign that those kobolds knew that I had real skills.
BEFORE: text: 这就证明，那些科博德知道我有真本事。
AFTER: text: 这就证明，那些科博德知道我有真本事。
ROW CAT:Oe4e2546be316c1fb2a9e | L66 | no manual edit
EN: Those years at the academy really paid off, and I took the loads to prove it!
BEFORE: text: 学院那几年真没白练，我接下的精液就是证明！
AFTER: text: 学院那几年真没白练，我接下的精液就是证明！
CONTROL L68 cut(0.06): ClassicGameOverAreaBI
CONTROL L69 rewind!
ROW CAT:O1849e384ca8124d698c2 | L70 | no manual edit
EN: After collaring me up all nice and spiffy, I was led out to some sort of stage
BEFORE: text: 给我戴上那漂亮又神气的项圈后，他们把我带上了一个台子，台下围着一大群海盗和各色外星人！
AFTER: text: 给我戴上那漂亮又神气的项圈后，他们把我带上了一个台子，台下围着一大群海盗和各色外星人！
ROW CAT:Odd3a6ef886e0ca023688 | L71 | no manual edit
EN: with plenty of pirates and aliens of all sort watching!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O674d7a2414d127ef5c79 | L72 | no manual edit
EN: They seemed to be waiting for some kind of show to start...
BEFORE: text: 他们好像在等某场表演开场……
AFTER: text: 他们好像在等某场表演开场……
ROW CAT:O72417861043e18750974 | L73 | no manual edit
EN: ...but what was the show? This could be some important data to collect!
BEFORE: text: ……可是什么表演呢？这说不定是值得收集的重要数据！
AFTER: text: ……可是什么表演呢？这说不定是值得收集的重要数据！
CONTROL L75 cut(0.06): ClassicGameOverAreaBJ
CONTROL L76 rewind!
ROW CAT:Oe3be8de3ee76625d2ad3 | L77 | no manual edit
EN: Well, a cold nose under my tail helped clue me in to what the show was gonna be.
BEFORE: text: 尾巴下面一碰到冰鼻头，我就猜到要演什么了。
AFTER: text: 尾巴下面一碰到冰鼻头，我就猜到要演什么了。
ROW CAT:Oc6fbe0ea978c3ea783dd | L78 | no manual edit
EN: An orange furred Barker had been let loose on me before I was even able to stand
BEFORE: text: 我还没来得及站起来，一只橙毛吠犬就被放过来扑向我，  
AFTER: text: 我还没来得及站起来，一只橙毛吠犬就被放过来扑向我，  
ROW CAT:Od251414e19cf8a75c37c | L79 | no manual edit
EN: It was so long since I was together with anything that wasn't a Kobold that I...
BEFORE: text: 我太久没跟科博德以外的家伙做过了，以至于……
AFTER: text: 我太久没跟科博德以外的家伙做过了，以至于……
ROW CAT:O13e39ec1db2f15308a03 | L80 | no manual edit
EN: ...I just sort of froze while the Barker moved to mount me!
BEFORE: text: ……那只吠犬爬上来要骑我时，我就这么僵住了！
AFTER: text: ……那只吠犬爬上来要骑我时，我就这么僵住了！
CONTROL L82 cut(0.06): ClassicGameOverAreaBK
CONTROL L83 rewind!
ROW CAT:O9ef6fd1d15a04d1b8d92 | L84 | no manual edit
EN: The shock of all this hap- pening while I was under a blindingly bright spotlight
BEFORE: text: 这一切竟发生在刺眼的聚光灯下，惊得我一下就从科博德的快感迷恋里清醒了！！
AFTER: text: 这一切竟发生在刺眼的聚光灯下，惊得我一下就从科博德的快感迷恋里清醒了！！
ROW CAT:O96023262139074ec9816 | L85 | no manual edit
EN: snapped me out of my Kobold pleasure fascination real quick!!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obcdf85bebe908e4189bf | L86 | no manual edit
EN: After taking note of the Barker's giant canid phallus and the copius ejaculations
BEFORE: text: 记录完吠犬的巨大犬型鸡巴和惊人射精量后，我环顾四周，想看看自己/究竟/在参与什么。
AFTER: text: 记录完吠犬的巨大犬型鸡巴和惊人射精量后，我环顾四周，想看看自己/究竟/在参与什么。
ROW CAT:Oced02a1fb297d044adbf | L87 | no manual edit
EN: I looked around to see what I was /really/ taking part of.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O075c27a074b7299e9aee | L88 | no manual edit
EN: ...and it was an auction! They were auctioning off... me?!?
BEFORE: text: ……居然是拍卖会！他们在拍卖……我？！？
AFTER: text: ……居然是拍卖会！他们在拍卖……我？！？
CONTROL L90 cut(0.06): ClassicGameOverAreaBL
CONTROL L91 rewind!
ROW CAT:O138a1976323df826a569 | L92 | no manual edit
EN: That was all I had time to process before the Barker shoved that huge knot inside
BEFORE: text: 我才刚反应过来，吠犬就把那巨大的结塞了进来，我又僵住了，努力理解它到底……有！多！大！
AFTER: text: 我才刚反应过来，吠犬就把那巨大的结塞了进来，我又僵住了，努力理解它到底……有！多！大！
ROW CAT:O69dcbca7f2803bca0373 | L93 | no manual edit
EN: causing me to freeze up ag- ain while I tried to process just how... huge! It! Was!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6b49d4834a13c89092a4 | L94 | no manual edit
EN: Oh my gosh!!
BEFORE: text: 我的天啊！！
AFTER: text: 我的天啊！！
ROW CAT:Od6dd3f30f23977bd9da2 | L95 | no manual edit
EN: I could barely keep my mind straight as the Barker dragged me along the stage
BEFORE: text: 吠犬拖着我在台上走，向所有外星竞拍客展示我翘起的尾巴时，我脑子都快转不动了。
AFTER: text: 吠犬拖着我在台上走，向所有外星竞拍客展示我翘起的尾巴时，我脑子都快转不动了。
ROW CAT:O4ab5e59eae971ae338f6 | L96 | no manual edit
EN: showing off my raised tail to all the alien auction goers.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od7ed49e6b50d21537b66 | L97 | no manual edit
EN: Pretty sure I heard the sounds of bidding before I blacked out once more...
BEFORE: text: 再次昏过去前，我分明听见了竞价声……
AFTER: text: 再次昏过去前，我分明听见了竞价声……
CONTROL L99 cut(0.06): Black
CONTROL L100 rewind!
ROW CAT:Oa307950de5f57ff96f25 | L101 | no manual edit
EN: So, yeah. Kobolds love me! Or at least, they /loved/ me.
BEFORE: text: 所以嘛，科博德都爱我！至少，他们/爱过/我。
AFTER: text: 所以嘛，科博德都爱我！至少，他们/爱过/我。
ROW CAT:Occ5d261f129e94bbab5c | L102 | no manual edit
EN: I can tell you all sorts of sexy tidbits about them, just try me!
BEFORE: text: 他们那些色色的小知识，我知道一大堆，尽管问！
AFTER: text: 他们那些色色的小知识，我知道一大堆，尽管问！
ROW CAT:O1c135ab02914eddd143f | L103 | no manual edit
EN: But, uhh...
BEFORE: text: 不过，呃……
AFTER: text: 不过，呃……
ROW CAT:O1db74beb8d12fe7d8cea | L104 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O789d6e8453122adc2b2b | L105 | no manual edit
EN: ...what planet are we on, anyways?
BEFORE: text: ……话说，我们这是在哪颗星球？
AFTER: text: ……话说，我们这是在哪颗星球？
CONTROL L107 wait: 0.2
CONTROL L108 fadeout(1.0, 1.0, 4)
### P08-020 | action=apply
原问题：in good hands/paws指交给可靠能手，当前“落在了好爪上”只是字面对译，中文不成义。上下文主角自夸服务技巧，与被囚现实构成反讽；不把自夸提升成客观自愿。
本轮理由：in good paws是能手可靠地接手，结合上句主角自夸服务技巧写成其夸口，不把报告自述变成客观同意或自由。
EDIT_IDS ["E08-030"]

