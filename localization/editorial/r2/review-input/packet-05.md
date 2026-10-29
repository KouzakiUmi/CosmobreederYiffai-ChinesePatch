# packet-05 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SC60b2521ed8918dd3 | nsfw | datadf/all.ds | AreaB_Slaver2.Talk.kobo
CONTROL L1060 <AreaB_Slaver2.Talk.kobo>
CONTROL L1061   if { koboCostume() } {
ROW CAT:O74e8ea2524757a3baa1b | L1062 | EDIT E05-001
EN: You smell pretty cute for a kobold, heh-heh. What crew you fly in with?
BEFORE:     * 你身上这味道对科博德来说真够可爱的，嘿嘿。你跟哪一伙船员一起飞？
AFTER:     * 你这科博德，闻起来倒挺讨人喜欢，嘿嘿。你跟哪支船队来的？
CONTROL L1063   }
CONTROL L1065 ### dog handling
### P05-001 | action=apply
原问题：船员在问所属船队/团伙，不是询问与哪些船员共同飞行；前半句也不宜写成“味道对科博德来说可爱”的判断句。
本轮理由：条件限kobo外观；crew问同来的船队归属，保留气味调侃而不增真实身份。
EDIT_IDS ["E05-001"]

## SC51b737558bc257e4 | nsfw | datadf/all.ds | AreaC_Slaver1.FakeMeat
CONTROL L1438 <AreaC_Slaver1.FakeMeat>
ROW CAT:Of1a1a7123907891803e4 | L1439 | EDIT E05-002
EN: Oh? You want to try my special meat?
BEFORE:   * 哦？你想试试我的特别的肉？
AFTER:   * 哦？想尝尝我的特制肉？
ROW CAT:O27aecbe4010c8c073ec7 | L1440 | EDIT E05-003
EN: Can't say you don't have guts, heh-heh...
BEFORE:   * 不能说你没胆子，嘿嘿……
AFTER:   * 胆子倒是不小，嘿嘿……
### P05-002 | action=apply
原问题：商品推销带阴森调侃，当前“我的特别的肉／不能说你没胆子”逐字且绕口；不推定肉的实际成分。
本轮理由：保两次发言和阴森反话；不猜肉的成分。
EDIT_IDS ["E05-002", "E05-003"]

## SC1a5d579ca870656a | nsfw | datadf/all.ds | Bossu.Area0_map26_a noselect
CONTROL L2041 <Bossu.Area0_map26_a noselect>
ROW CAT:O66e4355b77d4646c9ea6 | L2042 | no manual edit
EN: [WE JUST RECEIVED WORD FROM AGENT CETARTNI]
BEFORE:   Bossu: [我们刚收到 Cetartni 特工的消息，说你成功救出了对方。]
AFTER:   Bossu: [我们刚收到 Cetartni 特工的消息，说你成功救出了对方。]
ROW CAT:O123ee879f27d5c1764e2 | L2043 | no manual edit
EN: [THAT YOU SUCCESSFULLY RESCUED THEM.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oebc81acbc6616c0c1f95 | L2044 | no manual edit
EN: [THAT'S RIGHT, THEY WERE A LITTLE PAWED UP HERE AND THERE]
BEFORE:   Yiffany: [没错，对方身上到处都有点挠伤，不过看起来还算没什么大碍。]
AFTER:   Yiffany: [没错，对方身上到处都有点挠伤，不过看起来还算没什么大碍。]
ROW CAT:O4700fdc6687e02aa49c5 | L2045 | no manual edit
EN: [BUT SEEMED TO BE WELL ENOUGH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O392c1ffc63b2a29c3936 | L2046 | no manual edit
EN: [ALWAYS GLAD TO SEE AN AGENT SAFE AND SOUND, THAT BODES]
BEFORE:   Bossu: [每次看到特工平安归来，总让人欣慰，这对其他特工来说也是个好兆头。]
AFTER:   Bossu: [每次看到特工平安归来，总让人欣慰，这对其他特工来说也是个好兆头。]
ROW CAT:O72f9319e825d8367c508 | L2047 | no manual edit
EN: [WELL FOR THE OTHER AGENTS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Odfeb7b31b56edde34d91 | L2048 | EDIT E05-006
EN: [REMEMBER THAT YOU CAN VERIFY ANY DATA FROM YOUR P.A.W.]
BEFORE:   Mauser: [记住，你可以在自己的 P.A.W. 里核实任何数据。]
AFTER:   Mauser: [记住，救出特工后，可以在你的 P.A.W. 里核对数据。]
ROW CAT:O2cfc2161b3c6340e2309 | L2049 | EDIT E05-007
EN: [AFTER YOU RESCUED AN AGENT. WE'LL ALSO HAVE A COPY OF THE]
BEFORE:   Mauser: [在救下一名特工之后。我们当然也会保留一份数据副本，你之后随时都能查看！]
AFTER:   Mauser: [我们也会留一份数据副本，方便你以后查看！]
ROW CAT:Oe37f23d81ad5efe999dd | L2050 | no manual edit
EN: [DATA THAT YOU CAN REVIEW AT A LATER TIME TOO OF COURSE!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P05-004 | action=apply
原问题：前一框句号截断条件，下一框以“在救下一名特工之后。”孤立开头；应把时间条件前置，数据留存与回看连起来。
本轮理由：手动回看与总部副本为完整三源行含义；时间条件放入首有效槽，消费尾保持空白。
EDIT_IDS ["E05-006", "E05-007"]

## SCa7d50e8f2d64a2e7 | nsfw | datadf/all.ds | BossuDex.ClassicBumperC
CONTROL L3165 <BossuDex.ClassicBumperC>
ROW CAT:O36f6164c219bb7a1683c | L3166 | no manual edit
EN: [EVEN MORE OF THESE...]
BEFORE:   Yiffany: [这种东西还真多……]
AFTER:   Yiffany: [这种东西还真多……]
ROW CAT:O22d5bea9ba6d2cc3f48f | L3167 | EDIT E05-008
EN: [THE BUMPERS IN THAT SECTION SEEM TO HAVE BETTER ARMOR]
BEFORE:   Bossu: [那一区的撞击兽，装甲似乎比你见过的其他撞击兽都要好。]
AFTER:   Bossu: [那一区的撞击机器人，装甲似乎比你之前见过的同类更好。]
ROW CAT:O1235067bbab026f475dc | L3168 | no manual edit
EN: [THAN THE OTHER BUMPERS YOU'VE SEEN.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O5ec4dae75bb8ec47eac9 | L3169 | no manual edit
EN: [TRY NOT TO LET THEM HIT YOU, SINCE THAT EXTRA PLATING]
BEFORE:   Bossu: [尽量别被撞到，因为那层额外装甲肯定也会造成额外伤害。]
AFTER:   Bossu: [尽量别被撞到，因为那层额外装甲肯定也会造成额外伤害。]
ROW CAT:Oeb6304183553ecb38c42 | L3170 | no manual edit
EN: [IS SURE TO RESULT IN EXTRA DAMAGE, TOO.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P05-005 | action=apply
原问题：前文 ClassicBumper/Plus 明说机器/巡逻机器人；这里改称“撞击兽”把同类对象写成兽类，且重复赘重。此处描述性称呼不是全局专名裁决。
本轮理由：Bumper为机器而非兽；仅用描述性机器人称呼，不另立全局专名。
EDIT_IDS ["E05-008"]

## SCe810fe1962b453b0 | sfw | datadf/all.ds | BossuDex.ClassicWyvern
CONTROL L2962 <BossuDex.ClassicWyvern>
ROW SFW3da493426410d61e56e08e99 | L2963 | EDIT E05-009
EN: [BOSSU, I'VE JUST ENCOUNTERED A FLYING DRACONID.]
BEFORE:   Yiffany: [波苏，我刚遇到了一只飞行的龙人。]
AFTER:   Yiffany: [波苏，我刚遇到了一只会飞的龙类生物。]
ROW SFWe444d65a1d2abb99aa14dbc2 | L2964 | no manual edit
EN: [NOT SURPRISING. THE PREVIOUS MISSION REPORTED MULTIPLE]
BEFORE:   Bossu: [并不意外。上次任务报告里有多起双足飞龙目击记录。那些狡猾的家伙肌肉发达，在空中也极其灵活。]
AFTER:   Bossu: [并不意外。上次任务报告里有多起双足飞龙目击记录。那些狡猾的家伙肌肉发达，在空中也极其灵活。]
ROW SFW9fa8178cd3427e0c9330b4b0 | L2965 | no manual edit
EN: [WYVERN SIGHTINGS. THOSE CRAFTY CREATURES ARE WELL]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW5f9738b2862b67bc83b65ca0 | L2966 | no manual edit
EN: [MUSCLED AS WELL AS EXTREMELY AGILE IN THE AIR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWba948fccb62247c15d1af4a3 | L2967 | no manual edit
EN: [ANY TACTICS REPORTED BY THE PREVIOUS TEAM?]
BEFORE:   Yiffany: [上一支队伍报告过什么战术吗？]
AFTER:   Yiffany: [上一支队伍报告过什么战术吗？]
ROW SFWbebd51e47af1ea7fbaaec9c9 | L2968 | EDIT E05-010
EN: [THE NOTES SAY WYVERNS ARE PRONE TO DISTRACTION AT THE]
BEFORE:   Bossu: [记录上说，双足飞龙在高潮的]
AFTER:   Bossu: [记录上说，双足飞龙自己发动攻击时，]
ROW SFW656d1194409abaf471e2c8a9 | L2969 | EDIT E05-011
EN: [MOMENT OF THEIR OWN ATTACK.]
BEFORE:   Bossu: [它们自己发动攻击的那一刻。]
AFTER:   Bossu: [注意力容易分散。]
ROW SFW19be9cdb9218ba3a9b02543d | L2970 | EDIT E05-012
EN: [SO TRY TO CATCH THEM IN THE MIDDLE OF A DIVE.]
BEFORE:   Bossu: [所以尽量趁它们俯冲时出手。]
AFTER:   Bossu: [所以尽量趁它们俯冲到一半时出手。]
### P05-006 | action=apply
原问题：draconid 在本包喷火兽条目中属于龙类生物的上位分类，不等于人形龙人；下一句识别为双足飞龙。
本轮理由：draconid是龙类分类，未说明人形；保现用波苏。
EDIT_IDS ["E05-009"]
### P05-007 | action=apply
原问题：SFW源文仅写发动自身攻击的一刻，当前残留“在高潮的”既无源义又把战斗提示接成病句；不是合句空行漏译。
本轮理由：仅据JAR SFW攻击时分神及俯冲提示；移除PAK高潮污染，三个现有有效槽自然分配，不将分神说成高潮。
EDIT_IDS ["E05-010", "E05-011", "E05-012"]

## SC77ea58a1063412b5 | nsfw | datadf/all.ds | Mauser.Area0Transportal1 noselect
CONTROL L2052 <Mauser.Area0Transportal1 noselect>
ROW CAT:O0918eb0af4d8b0de1b92 | L2053 | no manual edit
EN: [YIFFANY, HAVE YOU COME ACROSS ANY TELEPORTALS YET?]
BEFORE:   Mauser: [伊法妮，你遇到传送门了吗？]
AFTER:   Mauser: [伊法妮，你遇到传送门了吗？]
ROW CAT:Odc5b961585570fc5c26e | L2054 | no manual edit
EN: [YEAH, I'VE JUST ENCOUNTERED ONE.]
BEFORE:   Yiffany: [嗯，我刚遇到过一个。]
AFTER:   Yiffany: [嗯，我刚遇到过一个。]
ROW CAT:Of78155718ca28fda2331 | L2055 | no manual edit
EN: [HOW'S MY SHIP BEEN SINCE I LEFT IT?]
BEFORE:   Yiffany: [我走之后我的飞船怎么样了？]
AFTER:   Yiffany: [我走之后我的飞船怎么样了？]
ROW CAT:O3afdccc791e26827d676 | L2056 | no manual edit
EN: [WE'VE USED SATELLITE R18 TO SET IT ON FOLLOW MODE]
BEFORE:   Tomcat: [我们用卫星 R18 把它设成了跟随模式，所以你应该能传送进你的飞船了，亲爱的。]
AFTER:   Tomcat: [我们用卫星 R18 把它设成了跟随模式，所以你应该能传送进你的飞船了，亲爱的。]
ROW CAT:O1b090142bf7ba0a1a7b4 | L2057 | no manual edit
EN: [SO YOU SHOULD BE ABLE TO TELEPORT INTO IT, DEAR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O514c2d447d240e2d1239 | L2058 | no manual edit
EN: [GREAT, I CAN'T WAIT TO FIND SOMETHING THAT'S A PROPER FU-]
BEFORE:   Yiffany: [太好了，我已经迫不及待想找到真正好用的——]
AFTER:   Yiffany: [太好了，我已经迫不及待想找到真正好用的——]
ROW CAT:O2ff2f1a05a930de19fd5 | L2059 | EDIT E05-013
EN: [HOLD ON THERE PUP. YOUR SHIP MAY BE BARELY WORKING]
BEFORE:   Bossu: [等一下，小子。你的飞船恐怕只能勉强运转，不过你只能贴地飞行。]
AFTER:   Bossu: [先等等，小家伙。你的飞船虽然还能勉强运转，但只能贴地飞行。]
ROW CAT:Of9acf15f2cd3923d03ce | L2060 | no manual edit
EN: [BUT YOU MAY ONLY FLY NAP-OF-THE- EARTH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O86f536e86784fb0b827c | L2061 | EDIT E05-014
EN: [WE CAN'T RISK YOU GETTING REDOWNED... OR WORSE.]
BEFORE:   Bossu: [我们不能冒着让你被击落……甚至更糟的风险。]
AFTER:   Bossu: [不能冒险让你再次被击落……甚至遭遇更糟的事。]
ROW CAT:O5ad8b2aab2f70dd7247d | L2062 | no manual edit
EN: [AWWW MAAAAAN!]
BEFORE:   Yiffany: [啊啊——！]
AFTER:   Yiffany: [啊啊——！]
ROW CAT:O1c866657d0ffc39bf30a | L2063 | no manual edit
EN: [NO GOING AFTER THOSE SCUM WITH GUNS BLAZING, GRRRL.]
BEFORE:   Tomcat: [不准开着枪冲去找那帮混蛋，丫头。] 
AFTER:   Tomcat: [不准开着枪冲去找那帮混蛋，丫头。] 
ROW CAT:O586346fdc55f7a63e897 | L2064 | no manual edit
EN: [THAT'S RIGHT! WE'RE RELYING SOLELY ON YOU NOW!]
BEFORE:   Mauser: [没错！现在我们只能指望你了！]
AFTER:   Mauser: [没错！现在我们只能指望你了！]
ROW CAT:O5cdb39ef8007f8764456 | L2065 | no manual edit
EN: [ALRIGHT ALRIGHT, I'LL TAKE THINGS SLOWLY...]
BEFORE:   Yiffany: [好吧好吧，我会慢慢来的……]
AFTER:   Yiffany: [好吧好吧，我会慢慢来的……]
ROW CAT:Oe8fdc08127e471475bdc | L2066 | no manual edit
EN: [GOOD GIRL. DON'T FORGET, WE'RE ALL HERE TO HELP YOU.]
BEFORE:   Bossu: [好姑娘。别忘了，我们都在这儿帮你。]
AFTER:   Bossu: [好姑娘。别忘了，我们都在这儿帮你。]
ROW CAT:O38a5ef8ea08a06c438d4 | L2067 | no manual edit
EN: [AND ON TOP OF THAT, THE HANGAR THAT THE OTHER AGENTS]
BEFORE:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
AFTER:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
ROW CAT:O89a22d001a7055f51007 | L2068 | no manual edit
EN: [WERE USING AS AN AUTOPILOT SERVICE STATION]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O5ac2fb5e90505790d5df | L2069 | no manual edit
EN: [SEEMS TO STILL BE RUNNING.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ocb48a990f34a29fe1270 | L2070 | no manual edit
EN: [YOU SHOULD STOP BY THERE AND SEE IF ANYONE'S AROUND!]
BEFORE:   Mauser: [你该去那边看看有没有人在！]
AFTER:   Mauser: [你该去那边看看有没有人在！]
ROW CAT:O21a45e74234b4c113f3f | L2071 | no manual edit
EN: [SOUNDS LIKE A GOOD IDEA. ROGER THAT!]
BEFORE:   Yiffany: [听起来不错。收到！]
AFTER:   Yiffany: [听起来不错。收到！]
### P05-008 | action=apply
原问题：女线当前把PUP叫“小子”，与该场Yiffany及后面的GOOD GIRL不符；同时“恐怕…不过…不过你只能”的说明重排为让步—限制—理由，不新增军衔。
本轮理由：受话人是Yiffany，PUP不译小子；完整保勉强运作、贴地限制和再被击落风险。
EDIT_IDS ["E05-013", "E05-014"]

## SC426f7f71c0aa693b | nsfw | datadf/all.ds | Mauser.Area0_map13_b noselect
CONTROL L1991 <Mauser.Area0_map13_b noselect>
ROW CAT:Oc88da03899f60c7d1b9b | L1992 | no manual edit
EN: [THE SOURCE OF THE TREMORS IS TO THE EAST OF YOU]
BEFORE:   Mauser: [震源在你的东边，但看起来有一座旧传输站就在你的西边！]
AFTER:   Mauser: [震源在你的东边，但看起来有一座旧传输站就在你的西边！]
ROW CAT:Oe8db2a26445ce9744123 | L1993 | no manual edit
EN: [BUT IT LOOKS LIKE THERE IS AN OLD TRANSMISSION]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O90c5dd8212ef94c7d63f | L1994 | no manual edit
EN: [STATION TO THE WEST OF YOU!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O30df66dc4acaba1f7104 | L1995 | no manual edit
EN: [DO YOU REMEMBER HOW TO USE THOSE?]
BEFORE:   Mauser: [你记得怎么使用那些东西吗？]
AFTER:   Mauser: [你记得怎么使用那些东西吗？]
ROW CAT:O09ce8a99f53ed7a84950 | L1996 | EDIT E05-015
EN: [THOSE WILL SAVE MY DATA IN CASE ANY THING HAPPENS]
BEFORE:   Yiffany: [那些东西会在出事时保存我的数据，对吧？]
AFTER:   Yiffany: [那些东西能先保存我的数据，以防万一出事，对吧？]
ROW CAT:Oe4de940304e31978c39e | L1997 | no manual edit
EN: [RIGHT?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofc83a1823e9b71ab80df | L1998 | no manual edit
EN: [THAT'S RIGHT! WE'RE COUNTING ON YOU AND YOUR DATA!]
BEFORE:   Mauser: [没错！我们就指望你和你的数据了！]
AFTER:   Mauser: [没错！我们就指望你和你的数据了！]
ROW CAT:O068b98ae57250dc15ce9 | L1999 | no manual edit
EN: [JUST MAKE SURE YOU STAND ON THE OLD PLATFORM]
BEFORE:   Mauser: [只要确保你站在旧平台上，然后手动启动数据传输。]
AFTER:   Mauser: [只要确保你站在旧平台上，然后手动启动数据传输。]
ROW CAT:O1df596e5998856b0c46f | L2000 | no manual edit
EN: [AND MANUALLY INITIATE THE DATA TRANSMISSION.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O36d690c61755adedaa6b | L2001 | no manual edit
EN: [THERE'S NO AUTO DATA COLLECTION LIKE NEW SYSTEMS HAVE!]
BEFORE:   Mauser: [这里可没有新系统那样的自动数据采集！]
AFTER:   Mauser: [这里可没有新系统那样的自动数据采集！]
### P05-009 | action=apply
原问题：in case 是预防性保存；当前“会在出事时保存”可能使玩家误认为出事自动存档，且后文明确要求站平台手动启动。
本轮理由：in case为预先存档防意外，不是出事时自动保存。
EDIT_IDS ["E05-015"]

## SCa1e42fd2a89cb4a7 | nsfw | datadf/all.ds | MauserHints_AreaE.AfterSeenLock
CONTROL L3634 <MauserHints_AreaE.AfterSeenLock>
CONTROL L3635   if { f(ctx_entered_room_AreaE_map23) } {
ROW CAT:Oda168f4d2a5a7f7785d1 | L3636 | no manual edit
EN: [THAT VAULT YOU FOUND IN THE NORTHEAST OF EXILE]
BEFORE:     Mauser: [你在流放东北发现的那座宝库，看起来确实很重要。]
AFTER:     Mauser: [你在流放东北发现的那座宝库，看起来确实很重要。]
ROW CAT:Ocdbdf9e283658ee3a4e2 | L3637 | no manual edit
EN: [SEEMS REALLY IMPORTANT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2d115ca64d6b31fc781a | L3638 | no manual edit
EN: [ANY IDEA HOW I COULD OPEN IT?]
BEFORE:     Yiffany: [有什么办法能让我打开它吗？]
AFTER:     Yiffany: [有什么办法能让我打开它吗？]
ROW CAT:O0b1cbd97cc7bf76b0568 | L3639 | no manual edit
EN: [IT SEEMS TO BE FENFEN TECH. SO IF YOU RUN INTO ANY]
BEFORE:     Mauser: [看起来是Fenfen的技术。所以你要是碰上他们，也许该留意他们对你说的话？]
AFTER:     Mauser: [看起来是Fenfen的技术。所以你要是碰上他们，也许该留意他们对你说的话？]
ROW CAT:Of0c902fc1440402f7fc0 | L3640 | no manual edit
EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L3641   }
### P05-037 | action=defer
原问题：Exile是绕Tutone的小行星名称；当前“在流放东北”把地名当普通动作名词，地点关系不清。此处暂保留英文专名，译名待统一裁决。
本轮理由：Q05-037：Exile为地名已证，但译名尚未裁定；不以本次局部修订强行撤换现用译名。待主控名称裁定后处理东北部表达。
EDIT_IDS []

## SC713dd4f4639c27ba | nsfw | datadf/all.ds | TomcatItems.KoboBody
CONTROL L4223 <TomcatItems.KoboBody>
ROW CAT:Of3908695aee1a237254a | L4224 | no manual edit
EN: [WOW, COME IN TOMCAT. YOU'RE NOT GONNA BELIEVE THIS.]
BEFORE:   Yiffany: [哇，汤姆猫请回答。你不会相信的。]
AFTER:   Yiffany: [哇，Tomcat请回答。你不会相信的。]
ROW CAT:Oc4ad3aea2549316c9c8e | L4225 | no manual edit
EN: [SIGH...]
BEFORE:   Tomcat: [叹气……]
AFTER:   Tomcat: [叹气……]
ROW CAT:Od4c3f0b750ed3fc416d9 | L4226 | no manual edit
EN: [YOU HAVE ANY IDEA WHAT I JUST PICKED UP?]
BEFORE:   Yiffany: [你知道我刚捡到什么吗？]
AFTER:   Yiffany: [你知道我刚捡到什么吗？]
ROW CAT:O6bc6260d8eb82af3ac3f | L4227 | no manual edit
EN: [...]
BEFORE:   Tomcat: [……]
AFTER:   Tomcat: [……]
ROW CAT:O94b8b333c22ea77771e4 | L4228 | EDIT E05-016
EN: [LOOK! ONE OF THOSE SCALE SUIT BODIES! LIKE WHEN WE WERE]
BEFORE:   Yiffany: [看！一件鳞片套装的身体！就像我们在学院那会儿，你参加的那个性社团！]
AFTER:   Yiffany: [看！是那种鳞片套装的衣身！跟学院那会儿，你参加的那个性社团用的一样！]
ROW CAT:O0f8c46b1579f62020441 | L4229 | no manual edit
EN: [IN THE ACADEMY AND YOU WERE PART OF THAT SEX CLUB!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O042d2b31045b7dfdb8b3 | L4230 | no manual edit
EN: [DO YOU HAVE TO BRING THIS UP ON COMPANY TIME?]
BEFORE:   Tomcat: [你非得在上班时间提这个吗？]
AFTER:   Tomcat: [你非得在上班时间提这个吗？]
ROW CAT:O655200c7d8d110f1a54b | L4231 | no manual edit
EN: [FIRST OF ALL, IT WASN'T A SEXUAL THING.]
BEFORE:   Tomcat: [首先，那不是性方面的事。]
AFTER:   Tomcat: [首先，那不是性方面的事。]
ROW CAT:O5f96724ab625790e471b | L4232 | no manual edit
EN: [MAAAYBE I FOOLED AROUND WITH ONE ON, SURE, WHATEVER.]
BEFORE:   Tomcat: [也——许我穿着一套胡闹过，当然，随便吧。]
AFTER:   Tomcat: [也——许我穿着一套胡闹过，当然，随便吧。]
ROW CAT:O1e35bfd285e291586de1 | L4233 | EDIT E05-017
EN: [BUT THAT WAS JUST KIND OF A JOKE AND IT WAS MOSTLY ABOUT]
BEFORE:   Tomcat: [但那大体上只是玩笑，主要是为了玩得开心、放开一点，就这样。拜托。]
AFTER:   Tomcat: [不过就是闹着玩，主要图个开心、放松一下罢了。拜托。]
ROW CAT:O2da2e4b9b5fbe923c345 | L4234 | no manual edit
EN: [HAVING FUN AND LET- TING LOOSE, THAT'S ALL. COME ON.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4173f8144606dad9a1db | L4235 | EDIT E05-018
EN: [LOOSE IS RIGHT. I REMEMBER THE SIZE OF SOME OF THOSE TOYS.]
BEFORE:   Yiffany: [放开是放开了。我可记得那些玩具有些有多大。]
AFTER:   Yiffany: [是够松的。我可记得有些玩具的尺寸。]
ROW CAT:O94bd4f18da048961941e | L4236 | no manual edit
EN: [S I G H]
BEFORE:   Tomcat: [叹 气]
AFTER:   Tomcat: [叹 气]
CONTROL L4238 ### Elf ###
### P05-010 | action=apply
原问题：“套装的身体”误作肉体，后半句“就像我们在学院那会儿，你参加的那个性社团”比较对象悬空；用回忆问句衔接随后的Tomcat辩解。
本轮理由：衣身与学院社团用品为比较关系，不新增回忆问句；社团性质仍属Yiffany调侃说辞。
EDIT_IDS ["E05-016"]
### P05-011 | action=apply
原问题：原文let loose/loose 是“放松／松”的反将一军；当前“放开是放开了”接不到玩具尺寸笑点。保留双方说辞，不把社团性质定为客观事实。
本轮理由：让Tomcat放松与Yiffany的松接上玩具尺寸反将一军，保双关归属，不扩大成客观社团史。
EDIT_IDS ["E05-017", "E05-018"]

## SCae76be512589a7df | nsfw | datadf/all.ds | TomcatItems.TazerTrainee
CONTROL L4059 <TomcatItems.TazerTrainee>
ROW CAT:Oe6fac8d45b8744c57828 | L4060 | no manual edit
EN: [OH WOW, IS THAT A ROOKIE'S LIGHTTAZER YOU GOT THERE?]
BEFORE:   Tomcat: [哇，你拿到的是新人的光电击枪？]
AFTER:   Tomcat: [哇，你拿到的是新人的光电击枪？]
ROW CAT:O382ee0935f1cf552493a | L4061 | no manual edit
EN: [YEAH, CAN'T WAIT TO FIND OUT WHOSE IT IS HAHA!]
BEFORE:   Yiffany: [是啊，真想赶紧知道是谁的，哈哈！]
AFTER:   Yiffany: [是啊，真想赶紧知道是谁的，哈哈！]
ROW CAT:O8328ac6799cf03e3027c | L4062 | no manual edit
EN: [YOU JUST KNOW THAT BOSSU IS GONNA CHEW OUT THE LITTLE BR-]
BEFORE:   Yiffany: [Bossu肯定会骂惨那个小混——]
AFTER:   Yiffany: [Bossu肯定会骂惨那个小混——]
ROW CAT:Ofdd5581717be23237118 | L4063 | no manual edit
EN: [PRETTY SURE THAT'S YOUR LITTLE BROTHERS LIGHTTAZER.]
BEFORE:   Tomcat: [我很确定，那是你弟弟的光电击枪。]
AFTER:   Tomcat: [我很确定，那是你弟弟的光电击枪。]
ROW CAT:O7b46f3da7734e84605d5 | L4064 | no manual edit
EN: [...]
BEFORE:   Yiffany: [……]
AFTER:   Yiffany: [……]
ROW CAT:Oe96abf697bbb84a5aeaa | L4065 | no manual edit
EN: [...YOU'RE KIDDING, RIGHT?]
BEFORE:   Yiffany: [……你在开玩笑吧？]
AFTER:   Yiffany: [……你在开玩笑吧？]
ROW CAT:O8aca8ee60760913cc9b1 | L4066 | no manual edit
EN: [NOOOOPE, SERIAL NUMBER ID-10-T-455. THAT'S YIFFAI'S.]
BEFORE:   Tomcat: [没——开玩笑，序列号ID-10-T-455。伊法伊的。]
AFTER:   Tomcat: [没——开玩笑，序列号ID-10-T-455。伊法伊的。]
ROW CAT:Ofc50086293b617d1b615 | L4067 | no manual edit
EN: [DAMMIT, MY SQUAD WON'T LET ME HEAR THE END OF THIS.]
BEFORE:   Yiffany: [可恶，队里那帮人肯定要笑我一辈子。]
AFTER:   Yiffany: [可恶，队里那帮人肯定要笑我一辈子。]
ROW CAT:Od71afefaeee707796a6f | L4068 | no manual edit
EN: [LOOK CAN YOU, I DUNNO, DELAY THAT REPORT FOR NOW?]
BEFORE:   Yiffany: [那个，你能不能，呃，先缓缓，别交报告？]
AFTER:   Yiffany: [那个，你能不能，呃，先缓缓，别交报告？]
ROW CAT:O1db07906286c7b26e218 | L4069 | EDIT E05-019
EN: [NO PURROMISES GIRL, BUT I'LL DO WHAT I CAN DO.]
BEFORE:   Tomcat: [姑娘，不敢喵喵保证，不过我会尽力。]
AFTER:   Tomcat: [姑娘，我不敢打包票，不过会尽力帮忙。]
ROW CAT:Of5b8cc24155fa975182b | L4070 | no manual edit
EN: [YOU'RE THE BEST, I OWE YOU ONE!]
BEFORE:   Yiffany: [你最棒了，欠你个人情！]
AFTER:   Yiffany: [你最棒了，欠你个人情！]
### P05-012 | action=apply
原问题：当前“不敢喵喵保证”既不成自然搭配，也把原文猫语双关机械展开成叠字叫声。这里只保留熟人帮忙但不承诺的意图，不新增固定喵口癖。
本轮理由：保持不承诺但尽力的同事支援；猫语双关不硬造叠字叫声。
EDIT_IDS ["E05-019"]

## SCb6f24971b727c80c | nsfw | datadf/all.ds | TomcatItems.VitMeat
CONTROL L3824 <TomcatItems.VitMeat>
ROW CAT:O2630734cd2aa61d9db81 | L3825 | EDIT E05-020
EN: [YESSSSSSS]
BEFORE:   Yiffany: [是啊啊啊啊啊啊啊]
AFTER:   Yiffany: [好——耶——！]
ROW CAT:O1f696aa413984ddacdf6 | L3826 | EDIT E05-021
EN: [OH THAT'S A REALLY HUGE CHUNK OF MEAT!]
BEFORE:   Tomcat: [哦，那真是好大的一块肉！]
AFTER:   Tomcat: [哇，好大一块肉！]
ROW CAT:Oa1360920373cc62575b8 | L3827 | EDIT E05-022
EN: [BIIIIIIIIIIIG]
BEFORE:   Yiffany: [大啊啊啊啊啊啊啊啊啊啊啊]
AFTER:   Yiffany: [好——大——]
ROW CAT:O609c94d2f7c2efaf2fbf | L3828 | EDIT E05-023
EN: [YOU REALLY LIKE BIG MEAT YOU CAN STICK IN YOUR MOUTH, HUH?]
BEFORE:   Tomcat: [你还真喜欢能塞进嘴里的大肉，嗯？]
AFTER:   Tomcat: [你还真喜欢能塞进嘴里的大肉，是吧？]
ROW CAT:Oebe86c0bf9e70cb07547 | L3829 | EDIT E05-024
EN: [WAAAARRRRRMMMM]
BEFORE:   Yiffany: [暖暖暖暖暖暖暖暖暖暖暖暖暖暖]
AFTER:   Yiffany: [热——乎——乎——]
ROW CAT:O53aca25ac4d84275c72a | L3830 | EDIT E05-025
EN: [WHEN IT'S THAT BIG DOES IT REMIND YOU OF THAT MISSION WH-]
BEFORE:   Tomcat: [它那么大时，会不会让你想起那次任务WH-]
AFTER:   Tomcat: [这么大，会不会让你想起那次任务，当——]
ROW CAT:O8ea8789b7602aa2c90b3 | L3831 | EDIT E05-026
EN: [GEETTTT INNN MEEEE]
BEFORE:   Yiffany: [进啊啊啊啊啊 到啊啊啊 我啊啊啊啊]
AFTER:   Yiffany: [快——进——我——肚——里——！]
ROW CAT:O923caecbd0927b645858 | L3832 | EDIT E05-027
EN: [UHH YOU KNOW WHAT?]
BEFORE:   Tomcat: [呃，你知道吗？]
AFTER:   Tomcat: [呃，算了。]
ROW CAT:Oc4545b656707f74fe07a | L3833 | EDIT E05-028
EN: [I'M JUST GONNA LEAVE YOU TWO ALONE FOR A MINUTE...]
BEFORE:   Tomcat: [我就让你们两个单独待一分钟……]
AFTER:   Tomcat: [我还是先让你俩单独待一分钟吧……]
### P05-013 | action=apply
原问题：场景是主角盯着肉拖长音、Tomcat越说越被无视；当前“是啊啊／进啊啊 到啊啊 我啊啊”无法成句，且WH-残留英语断词。建议保留夸张节奏和食物双关，不补具体任务内容。
本轮理由：按原九个非空槽保夸张拖音、肉食双关和被打断的任务开头；不猜WH后的具体事件，保一分钟意义。
EDIT_IDS ["E05-020", "E05-021", "E05-022", "E05-023", "E05-024", "E05-025", "E05-026", "E05-027", "E05-028"]

## SC1c0e8e24cfeaa003 | sfw | datadf/all.ds | TomcatItems.ZenerSquare
CONTROL L4348 <TomcatItems.ZenerSquare>
ROW SFW3fbdf76c5895b53c1e4ff932 | L4349 | no manual edit
EN: [SO, SAY I MANAGED TO PICK UP ANOTHER ORB THAT ISN'T]
BEFORE:   Yiffany: [那假如我又捡到一颗球体，而且是]
AFTER:   Yiffany: [那假如我又捡到一颗球体，而且是]
ROW SFWbb2ee4ebec069951c11e7e72 | L4350 | no manual edit
EN: [VISIBLE IN THE NEAR FIELD DATA AT ALL...]
BEFORE:   Yiffany: [在近场数据里完全看不到的……]
AFTER:   Yiffany: [在近场数据里完全看不到的……]
ROW SFW025cc77558375b5240e5753b | L4351 | no manual edit
EN: [WHAT SORT OF THINGS SHOULD I EXPECT TO HAPPEN?]
BEFORE:   Yiffany: [我该做好发生什么事的准备？]
AFTER:   Yiffany: [我该做好发生什么事的准备？]
ROW SFWf42f36a1fa46a058b52fda23 | L4352 | no manual edit
EN: [OH GEE, WHERE TO BEGIN WITH THAT?]
BEFORE:   Tomcat: [哎呀，这该从哪儿说起呢？]
AFTER:   Tomcat: [哎呀，这该从哪儿说起呢？]
ROW SFWf1c0b9eee93ab8a9a576ded7 | L4353 | EDIT E05-029
EN: [WHEN WE BEGAN RECEIVING REPORTS FROM AGENTS ABOUT]
BEFORE:   Tomcat: [当初我们开始收到特工们关于]
AFTER:   Tomcat: [当初特工们开始向我们报告，]
ROW SFW05db79540ca12bbd0e72f527 | L4354 | EDIT E05-030
EN: [SUPPOSED "PSY POWERS", WE BROUGHT IN PSYCHIATRISTS!]
BEFORE:   Tomcat: [所谓的“精神力异能”时，我们还请了精神科医生！]
AFTER:   Tomcat: [说自己有了所谓的“精神力异能”，我们还请来了精神科医生！]
ROW SFW3929c5a21767eb6df415039c | L4355 | EDIT E05-031
EN: [IT WAS HARD TO FATHOM THE CRAZY THINGS THAT AGENTS]
BEFORE:   Tomcat: [特工们说的那些怪事，实在难以想象]
AFTER:   Tomcat: [他们说的那些怪事实在难以想象……]
ROW SFW3db19849758c95117fd0d37c | L4356 | EDIT E05-032
EN: [TOLD US... SHOOTING STARS... ENERGY BLASTS...]
BEFORE:   Tomcat: [告诉我们的怪事……流星……能量弹……]
AFTER:   Tomcat: [发射星星……打出能量弹……]
ROW SFWc6a48905158c8cc5f193c8b8 | L4357 | EDIT E05-033
EN: [ONE CANINE FELLA EVEN SWORE THAT HE COULD TURN FERAL!]
BEFORE:   Tomcat: [有个犬族的家伙甚至发誓，他能变成野兽！]
AFTER:   Tomcat: [有个犬族的家伙甚至发誓，说自己能变成野兽！]
ROW SFW6ab96461b7c6633d9d0a564c | L4358 | no manual edit
EN: [W-WHAT? TURN FERAL??]
BEFORE:   Yiffany: [什、什么？变成野兽？？]
AFTER:   Yiffany: [什、什么？变成野兽？？]
ROW SFW36d4fafe5b254a65c39ffbcc | L4359 | no manual edit
EN: [YEAH, SAID HE GOT IN TOUCH WITH A SIDE OF HIMSELF THAT]
BEFORE:   Tomcat: [是啊，他说自己发现了自身的另一面，那一面]
AFTER:   Tomcat: [是啊，他说自己发现了自身的另一面，那一面]
ROW SFW90a6eac5e5dff83088a965ec | L4360 | no manual edit
EN: [HE NEVER KNEW. RUNNIN' AROUND, DIGGIN' HOLES]
BEFORE:   Tomcat: [他从来不知道。到处乱跑，挖洞，]
AFTER:   Tomcat: [他从来不知道。到处乱跑，挖洞，]
ROW SFW24e4b6642bae0225a07bfe07 | L4361 | no manual edit
EN: [EVEN IF OTHER AGENTS STORIES TURN OUT TO BE TRUE]
BEFORE:   Tomcat: [就算其他特工的故事都是真的]
AFTER:   Tomcat: [就算其他特工的故事都是真的]
ROW SFW638d23633d402b111763854e | L4362 | no manual edit
EN: [THERE'S NO WAY HIS STORY WOULD BE REAL!]
BEFORE:   Tomcat: [他那个故事怎么可能是真的！]
AFTER:   Tomcat: [他那个故事怎么可能是真的！]
ROW SFW4264765b35b477735315b291 | L4363 | no manual edit
EN: [Y-YEAH... THAT CAN'T BE A THING...HAHA...!!]
BEFORE:   Yiffany: [对、对啊……哪可能有这种事……哈哈……！！]
AFTER:   Yiffany: [对、对啊……哪可能有这种事……哈哈……！！]
ROW SFWef709969954d2c454d7e2db2 | L4364 | no manual edit
EN: [...DIGGING HOLES, HUH...]
BEFORE:   Yiffany: [……挖洞，是吧……]
AFTER:   Yiffany: [……挖洞，是吧……]
### P05-014 | action=apply
原问题：当前第一句缺“报告”，后面“特工们说的那些怪事…告诉我们的怪事”重复拼接；整段是总部不信怪力的回忆，接主角心虚，不应逐行保留残句。星星/能量弹按能力描述，不把shooting stars误设为天文观测。
本轮理由：五个有效槽分别承接报告、精神科医生、难信、能力例举、犬类形变；不跨角色或消费节点。
EDIT_IDS ["E05-029", "E05-030", "E05-031", "E05-032", "E05-033"]

## SC188abbfbd53fac7b | nsfw | datadf/all.ds | TomcatItems.ZenerTriangle
CONTROL L4530 <TomcatItems.ZenerTriangle>
ROW CAT:O620820b3e39b22ef6f09 | L4531 | no manual edit
EN: [WOAH, I JUST SAW ANOTHER SPIKE IN YOUR VITALS!]
BEFORE:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
AFTER:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
ROW CAT:Od1db16756c1efdfb1c5b | L4532 | no manual edit
EN: [LEMME GUESS: JUST TOUCHED A SENSOR DARK FLOATING ORB?]
BEFORE:   Tomcat: [让我猜猜：刚碰了一颗悬浮的暗色传感球？]
AFTER:   Tomcat: [让我猜猜：刚碰了一颗悬浮的暗色传感球？]
ROW CAT:Od892312dd4dbbcf049f0 | L4533 | EDIT E05-034
EN: [YEAH. I GET THE FEELING THIS POWER WILL MAKE ME]
BEFORE:   Yiffany: [是啊。我感觉这股力量会让我变得更硬，但降低我的战斗效能。]
AFTER:   Yiffany: [是啊。我感觉这股力量会让我更耐打，不过战斗能力会下降。]
ROW CAT:Ob7b09f3194f3f8559079 | L4534 | no manual edit
EN: [TOUGHER, BUT REDUCE MY COMBAT EFFECTIVENESS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc7840bac18957f00efbb | L4535 | no manual edit
EN: [WITH NO DATA, WE'LL HAVE TO TRUST YOUR INSTINCTS.]
BEFORE:   Tomcat: [没有数据，我们就只能相信你的直觉了。]
AFTER:   Tomcat: [没有数据，我们就只能相信你的直觉了。]
ROW CAT:O7ff95be65c68ca6d613e | L4536 | no manual edit
EN: [BUT BE CAREFUL WITH THAT, GIRL.]
BEFORE:   Tomcat: [但要小心那东西，姑娘。]
AFTER:   Tomcat: [但要小心那东西，姑娘。]
ROW CAT:O86067da83f50d2450549 | L4537 | no manual edit
EN: [YEAH. SEEMS LIKE A DOUBLE-EDGED SWORD. YIFFANY OUT.]
BEFORE:   Yiffany: [是啊。看来像把双刃剑。伊法妮通话结束。]
AFTER:   Yiffany: [是啊。看来像把双刃剑。伊法妮通话结束。]
CONTROL L4539 ### Misc Upgrades ###
### P05-015 | action=defer
原问题：sensor dark修饰对传感器不可见；当前“暗色传感球”反而将其说成有传感功能的暗色球，与同包ZenerSquare近场数据完全不可见、后文无数据呼应冲突。
本轮理由：Q05-015：sensor dark原文语法异常。近场不可见与无数据仅支持推测，尚不能确认sensor-dark复合修饰；须补原作意图/平行版本证据，不发明暗色传感设备。
EDIT_IDS []
### P05-016 | action=apply
原问题：tougher在能力利弊说明里指更能承受伤害，“变得更硬”容易误成硬度或色情双关；该段没有主角开荤笑的信号。
本轮理由：能力利弊是耐打与战斗效能，不发明硬度/成人暗示。
EDIT_IDS ["E05-034"]

## SCfb40649184a4a38a | nsfw | datadm/all.ds | AreaC_Slaver1.FakeMeat
CONTROL L1448 <AreaC_Slaver1.FakeMeat>
ROW CAT:O749c73d8511f7b0cec61 | L1449 | EDIT E05-004
EN: Oh? You want to try my special meat?
BEFORE:   * 哦？你想试试我的特别的肉？
AFTER:   * 哦？想尝尝我的特制肉？
ROW CAT:Offd2634e3cce5aedcec6 | L1450 | EDIT E05-005
EN: Can't say you don't have guts, heh-heh...
BEFORE:   * 不能说你没胆子，嘿嘿……
AFTER:   * 胆子倒是不小，嘿嘿……
### P05-003 | action=apply
原问题：男线为独立场景收据；同样的推销反话不必保留英语双重否定句法。
本轮理由：独立男线同义证据；各物理槽分别改，不合并。
EDIT_IDS ["E05-004", "E05-005"]

## SCbb24ffbfac0746d8 | sfw | datadm/all.ds | BossuDex.ClassicArcher
CONTROL L3139 <BossuDex.ClassicArcher>
ROW SFW6e7ffa47864e257d741d96fe | L3140 | EDIT E05-035
EN: [THE ELVES OF SCEAFYA MAY ALL BE FEMALE]
BEFORE:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
AFTER:   Bossu: [斯凯菲亚的精灵虽说全是女性，却并非个个都能长生不老。]
ROW SFW0cc7383cc2bfddc06602bbc5 | L3141 | no manual edit
EN: [BUT THEY AREN'T ALL IMMORTAL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW7fd49308950e0c5f571069ce | L3142 | EDIT E05-036
EN: [THEY'VE TAKEN ON MORE AND MORE MORTAL CHARACTERISTICS]
BEFORE:   Bossu: [她们便带上了越来越多的有朽特征]
AFTER:   Bossu: [她们身上凡人的特征越来越多，]
ROW SFWf116b4cccfb60b3418c9b385 | L3143 | EDIT E05-037
EN: [AS THE CENTURIES HAVE GONE BY.]
BEFORE:   Bossu: [在数百年的岁月流逝之中。]
AFTER:   Bossu: [几百年来一直如此。]
ROW SFW316e1a82b58dc7cf800f1a31 | L3144 | no manual edit
EN: [WAIT, SO THAT MEANS SOME OF THEM *ARE* IMMORTAL?]
BEFORE:   Yiffai: [等等，所以这意味着她们中有些*是*不朽的？]
AFTER:   Yiffai: [等等，所以这意味着她们中有些*是*不朽的？]
ROW SFWd6259d665bdaa2871112074f | L3145 | EDIT E05-038
EN: [INDEED, AS FAR AS WE CAN TELL.]
BEFORE:   Bossu: [的确，就我们所能看出的而言。]
AFTER:   Bossu: [据我们掌握的情况，确实如此。]
ROW SFWf8f58f26fc64c61547c6f6f4 | L3146 | EDIT E05-039
EN: [ANY ELF THAT IS OUT IN THE OPEN AND ENGAGING IN COMBAT]
BEFORE:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
AFTER:   Bossu: [那些公开现身、参加战斗的精灵，肯定都还年轻，最多也就一百岁。]
ROW SFWa5c7504173bd4555381b9838 | L3147 | no manual edit
EN: [WILL NO DOUBT BE A YOUNGSTER. A HUNDRED YEARS OLD AT MOST.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWedb6ed050a91358da387f4e3 | L3148 | no manual edit
EN: [THAT'S... WOW...]
BEFORE:   Yiffai: [这……哇……]
AFTER:   Yiffai: [这……哇……]
ROW SFWf6bf20d3bd9472ffc686f02c | L3149 | EDIT E05-040
EN: [DON'T GIVE IN TO AWE. YOU'LL NEED TO BE ON YOUR TOES]
BEFORE:   Bossu: [别向敬畏屈服。你得保持警觉，以便击退那些年幼精灵的攻击。]
AFTER:   Bossu: [别光顾着惊叹。打起精神，才能挡住那些年轻精灵的攻击。]
ROW SFW6d73310851f1937d6c8d3fff | L3150 | no manual edit
EN: [IN ORDER TO REPEL THE YOUNG ELVES' ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWa2f9e8c5bc97bb959cdc4afc | L3151 | no manual edit
EN: [RIGHT, GOTTA FOCUS.]
BEFORE:   Yiffai: [对，得专注。]
AFTER:   Yiffai: [对，得专注。]
### P05-017 | action=apply
原问题：may… but…为让步，当前“也许全是”弱化已在讲述的前提；“有朽特征／在数百年的岁月流逝之中”倒装生硬。此为Bossu报告说辞，不外推绝对设定。
本轮理由：may...but在此为让步；三个有效槽保全女性、非全不朽与数百年渐变，无跨SFW补成人交配原因。
EDIT_IDS ["E05-035", "E05-036", "E05-037"]
### P05-018 | action=apply
原问题：当前“就我们所能看出的而言”明显翻译腔；“年幼者”不如“还年轻”能自然接“一百岁”的寿命落差，不把youngster转为现实未成年判定。
本轮理由：保as far as we can tell知识限制及最多百岁；youngster不等同现实幼童。
EDIT_IDS ["E05-038", "E05-039"]
### P05-019 | action=apply
原问题：“别向敬畏屈服”把让人回神的提醒译成抽象服从关系；问答正在讲寿命惊讶与战斗专注。
本轮理由：惊叹寿命后的回神提醒，非抽象向敬畏屈服。
EDIT_IDS ["E05-040"]

## SC46fe33beaab2503d | nsfw | datadm/all.ds | BossuDex.ClassicFenfen
CONTROL L3123 <BossuDex.ClassicFenfen>
ROW CAT:O93747cb50f2482f26380 | L3124 | no manual edit
EN: [COME IN. BOSSU?]
BEFORE:   Yiffai: [波苏，我这就进来。]
AFTER:   Yiffai: [波苏，我这就进来。]
ROW CAT:O78f189f7c18c5738e817 | L3125 | no manual edit
EN: [I HOPE NOT, MY BOY.]
BEFORE:   Bossu: [希望别，孩子。]
AFTER:   Bossu: [希望别，孩子。]
ROW CAT:O04ac6de0bf590f7e53d4 | L3126 | no manual edit
EN: [WHAT?]
BEFORE:   Yiffai: [什么？]
AFTER:   Yiffai: [什么？]
ROW CAT:Ocebc18e2fdb80d2ff281 | L3127 | no manual edit
EN: [NOTHING. WHAT SEEMS TO BE THE PROBLEM?]
BEFORE:   Bossu: [没什么。遇到什么问题了？]
AFTER:   Bossu: [没什么。遇到什么问题了？]
ROW CAT:O93648470be272fe86a97 | L3128 | no manual edit
EN: [I'VE COME ACROSS A BI- PEDAL CANID SPECIES THAT SEEMS]
BEFORE:   Yiffai: [我遇到了一种双足的犬科物种，它好像完全无视我所有的沟通尝试！]
AFTER:   Yiffai: [我遇到了一种双足的犬科物种，它好像完全无视我所有的沟通尝试！]
ROW CAT:O14f56682dfea08af1dbe | L3129 | no manual edit
EN: [TO BE IGNORING ALL MY ATTEMPTS AT COMMUNICATION!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O0cca3e9dd0db11549850 | L3130 | no manual edit
EN: [NOT ONLY THAT, THEY'RE THROWING ROCKS AT ME!!]
BEFORE:   Yiffai: [而且它们还朝我扔石头！！]
AFTER:   Yiffai: [而且它们还朝我扔石头！！]
ROW CAT:O0214174cd6f73a2de989 | L3131 | no manual edit
EN: [THEY MAY LOOK ORGANIC, BUT BELIEVE IT OR NOT THOSE ARE]
BEFORE:   Bossu: [它们看着像有机生物，可你信不信，那些是图托恩某个物种的机械复制品——Fenfen。]
AFTER:   Bossu: [它们看着像有机生物，可你信不信，那些是图托恩某个物种的机械复制品——Fenfen。]
ROW CAT:O6f054d883f979f49e293 | L3132 | no manual edit
EN: [MECHANICAL COPIES OF A TUTONE SPECIES, THE FENFEN.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O633d0efb1169b5aff2f0 | L3133 | no manual edit
EN: [YOU MEAN LIKE... A DRONE, OR A TURRET?]
BEFORE:   Yiffai: [你是说……像无人机，或者炮塔那样？]
AFTER:   Yiffai: [你是说……像无人机，或者炮塔那样？]
ROW CAT:Oe051304ad4b668a4276a | L3134 | no manual edit
EN: [RIGHT. IF ANY FLESH AND FUR VARIETIES OF THAT SPECIES ARE]
BEFORE:   Bossu: [对。要是那物种还有血肉皮毛的真货留在这颗星球上，也还没有特工碰到过它们。]
AFTER:   Bossu: [对。要是那物种还有血肉皮毛的真货留在这颗星球上，也还没有特工碰到过它们。]
ROW CAT:Oa2f69c324c0999964566 | L3135 | no manual edit
EN: [STILL ON THE PLA- NET, NO AGENTS HAVE RUN INTO THEM YET.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O72c46d5d58897e28ada1 | L3136 | no manual edit
EN: [REPORTS OF FENFEN OUTFITS STREWN ABOUT ARE ALL WE HAVE.]
BEFORE:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
AFTER:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
ROW CAT:O429870245653e6c57714 | L3137 | no manual edit
EN: [THAT'S CRAZY...]
BEFORE:   Yiffai: [太离谱了……]
AFTER:   Yiffai: [太离谱了……]
### P05-020 | action=defer
原问题：无线电come in不是实体进入。当前“我这就进来”错置动作和意图；本NSFW分支紧跟I HOPE NOT为情色双关，后续整段精修需连同这句回话重建中文笑点，不能因此保留主句错译。
本轮理由：Q05-020：COME IN确为无线电呼叫，但紧邻Bossu的I HOPE NOT为成人接梗。当前两句须成组重建；尚无不增义而同时保通讯与性双关的可靠中文方案，整组暂缓，不单修首句留下失去落点的回复。
EDIT_IDS []

## SC54121e70d4d54642 | sfw | datadm/all.ds | BossuDex.ClassicFenfen
CONTROL L3062 <BossuDex.ClassicFenfen>
ROW SFW8c6266ed7ccfa1d589310215 | L3063 | EDIT E05-041
EN: [COME IN. BOSSU?]
BEFORE:   Yiffai: [波苏，我这就进来。]
AFTER:   Yiffai: [呼叫波苏，收到请回答？]
ROW SFW8b5625d63ef84e0b6fcce534 | L3064 | no manual edit
EN: [WHAT SEEMS TO BE THE PROBLEM?]
BEFORE:   Bossu: [似乎出了什么问题？]
AFTER:   Bossu: [似乎出了什么问题？]
ROW SFW1771bf7d803bb573f1e4b901 | L3065 | no manual edit
EN: [I'VE COME ACROSS A BI- PEDAL CANID SPECIES THAT SEEMS]
BEFORE:   Yiffai: [我遇到了一种双足的犬科物种，它好像完全无视我所有的沟通尝试！]
AFTER:   Yiffai: [我遇到了一种双足的犬科物种，它好像完全无视我所有的沟通尝试！]
ROW SFW1f1f8aba3ed098bfe173969a | L3066 | no manual edit
EN: [TO BE IGNORING ALL MY ATTEMPTS AT COMMUNICATION!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW50adc33da870d41702c06e5f | L3067 | no manual edit
EN: [NOT ONLY THAT, THEY'RE THROWING ROCKS AT ME!!]
BEFORE:   Yiffai: [而且它们还朝我扔石头！！]
AFTER:   Yiffai: [而且它们还朝我扔石头！！]
ROW SFW47326ffeaf3685647efb274d | L3068 | no manual edit
EN: [THEY MAY LOOK ORGANIC, BUT BELIEVE IT OR NOT THOSE ARE]
BEFORE:   Bossu: [它们看着像有机生物，可你信不信，那些是图托恩某个物种的机械复制品——Fenfen。]
AFTER:   Bossu: [它们看着像有机生物，可你信不信，那些是图托恩某个物种的机械复制品——Fenfen。]
ROW SFWd5daa0dae15bc89cd52e8878 | L3069 | no manual edit
EN: [MECHANICAL COPIES OF A TUTONE SPECIES, THE FENFEN.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW4b48a83c886552868e29e33b | L3070 | no manual edit
EN: [YOU MEAN LIKE... A DRONE, OR A TURRET?]
BEFORE:   Yiffai: [你是说……像无人机，或者炮塔那样？]
AFTER:   Yiffai: [你是说……像无人机，或者炮塔那样？]
ROW SFWf0b6383ef56b27d3918e6042 | L3071 | no manual edit
EN: [RIGHT. IF ANY FLESH AND FUR VARIETIES OF THAT SPECIES ARE]
BEFORE:   Bossu: [对。要是那物种还有血肉皮毛的真货留在这颗星球上，也还没有特工碰到过它们。]
AFTER:   Bossu: [对。要是那物种还有血肉皮毛的真货留在这颗星球上，也还没有特工碰到过它们。]
ROW SFW8affea2ab36cd54db391cb49 | L3072 | no manual edit
EN: [STILL ON THE PLA- NET, NO AGENTS HAVE RUN INTO THEM YET.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW58fcacb717e1d3c1e0d0f53b | L3073 | no manual edit
EN: [REPORTS OF FENFEN OUTFITS STREWN ABOUT ARE ALL WE HAVE.]
BEFORE:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
AFTER:   Bossu: [我们只有那些关于 FENFEN 服装散落各处的报告。]
ROW SFWed86c523f1e18f05dae2c931 | L3074 | no manual edit
EN: [THAT'S CRAZY...]
BEFORE:   Yiffai: [太离谱了……]
AFTER:   Yiffai: [太离谱了……]
### P05-021 | action=apply
原问题：SFW平行分支已删双关回复，此处纯粹呼叫；“我这就进来”不是无线电用语。单独记录，不与NSFW当作同场经历。
本轮理由：SFW自身已删成人回复，纯通讯呼叫，可独立确认应用。
EDIT_IDS ["E05-041"]

## SC553c64bb4bea4bc3 | nsfw | datadm/all.ds | BossuDex.ClassicKobold
CONTROL L3107 <BossuDex.ClassicKobold>
ROW CAT:O5e2945bc62d5649738d3 | L3108 | EDIT E05-042
EN: [BOSSU! I'VE RUN INTO SOME ANTHRO GREEN LIZARD UNITS]
BEFORE:   Yiffai: [波苏！我撞上了一些兽人绿色蜥蜴兵，但它们看着相当不友好！]
AFTER:   Yiffai: [波苏！我遇到一群人形的绿皮蜥蜴兵，看着很不友好！]
ROW CAT:O473d5114358e02fb364e | L3109 | no manual edit
EN: [BUT THEY SEEM DECIDEDLY UNFRIENDLY!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc46262f46143a5270b73 | L3110 | no manual edit
EN: [AHH YOU'VE RUN INTO SOME KOBOLDS DOWN THERE, HAVE YOU?]
BEFORE:   Bossu: [啊，你在下面撞上科博德了，是吧？]
AFTER:   Bossu: [啊，你在下面撞上科博德了，是吧？]
ROW CAT:O88a57be6a3f26f791a45 | L3111 | no manual edit
EN: [IS THAT WHAT THESE BIG LIZARD FOLKS ARE?]
BEFORE:   Yiffai: [这些大蜥蜴家伙就是科博德？]
AFTER:   Yiffai: [这些大蜥蜴家伙就是科博德？]
ROW CAT:O6dcb47d1f24f3f7b05a9 | L3112 | no manual edit
EN: [CORRECT. YOU BETTER GET USED TO TANGLING WITH THEM.]
BEFORE:   Bossu: [没错。你最好习惯跟他们缠斗。]
AFTER:   Bossu: [没错。你最好习惯跟他们缠斗。]
ROW CAT:O152354ab88dd9adae275 | L3113 | no manual edit
EN: [THOSE LIZARDS ARE A SLY BUNCH, KNOWN FOR PIRACY AND SLAVING]
BEFORE:   Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到最后能赚到LECT的营生！]  
AFTER:   Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到最后能赚到LECT的营生！]  
ROW CAT:Oaf7e7249cbc9b0040baf | L3114 | no manual edit
EN: [AND ANYTHING ELSE THAT HAS A LECT PAYOFF AT THE END!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O18d86a1694167ddd3e61 | L3115 | no manual edit
EN: [YOU'RE LIABLE TO RUN INTO THEM ON MOST ANY SORTIE.]
BEFORE:   Bossu: [你随便出趟任务都可能撞上他们。]
AFTER:   Bossu: [你随便出趟任务都可能撞上他们。]
ROW CAT:O4510cd8cb8af3734f037 | L3116 | no manual edit
EN: [I CAN HANDLE THEM! I'VE ALREADY TAKEN OUT, LIKE...]
BEFORE:   Yiffai: [我应付得了他们！我已经干掉了，大概……]
AFTER:   Yiffai: [我应付得了他们！我已经干掉了，大概……]
ROW CAT:Od0b71f7a304d1e93bb1f | L3117 | no manual edit
EN: [...A BUNCH!]
BEFORE:   Yiffai: [……一大把！]
AFTER:   Yiffai: [……一大把！]
ROW CAT:Oaf111d7b59e632558bb6 | L3118 | no manual edit
EN: [EARLY REPORTS WERE THAT MANY OF YOUR FELLOW AGENTS HAD]
BEFORE:   Bossu: [早期报告说，你的许多同僚特工都已经被科博德抓走了。能救就救，哪怕得花钱把他们赎回来。明白吗？]
AFTER:   Bossu: [早期报告说，你的许多同僚特工都已经被科博德抓走了。能救就救，哪怕得花钱把他们赎回来。明白吗？]
ROW CAT:O91e8680ba804a3f5d8a6 | L3119 | no manual edit
EN: [BEEN CAPTURED BY KOBOLDS. RESCUE THEM IF YOU CAN, EVEN IF]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6d945b547b56a73740c8 | L3120 | no manual edit
EN: [YOU HAVE TO PAY TO HAVE THEM FREED. UNDERSTOOD?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od2582ea0a87c40d0fce0 | L3121 | no manual edit
EN: [ROGER THAT, I'LL KEEP AN EYE OUT FOR ANY TRADERS.]
BEFORE:   Yiffai: [收到，我会留意任何商人的。]
AFTER:   Yiffai: [收到，我会留意任何商人的。]
### P05-022 | action=apply
原问题：“兽人绿色蜥蜴兵”分类叠放不自然，anthro在这里描述人形，并非另加一个兽人种族；接下句由Bossu识别为kobolds，保留先见外观后揭名。
本轮理由：先描人形绿蜥蜴外观，再由Bossu识别；不增兽人种族。
EDIT_IDS ["E05-042"]

## SCe0520bfb2096fa57 | nsfw | datadm/all.ds | Mauser.AreaE_map23 noselect
CONTROL L2571 <Mauser.AreaE_map23 noselect>
ROW CAT:O8240d76e1f0b65f34ac8 | L2572 | no manual edit
EN: [AGENT, COME IN. REQUESTING STATUS REPORT.]
BEFORE:   Mauser: [特工，请回话。请求状态报告。]
AFTER:   Mauser: [特工，请回话。请求状态报告。]
ROW CAT:Of37116e5520cb64e36c8 | L2573 | no manual edit
EN: [COSMOBREEDER YIFFAI, REPORTING!]
BEFORE:   Yiffai: [宇宙育种者伊法伊，报到！]
AFTER:   Yiffai: [宇宙育种者伊法伊，报到！]
ROW CAT:Oac8b4a813cbfb37fb1ba | L2574 | no manual edit
EN: [LOOKS LIKE I'M INSIDE OF SOME SORT OF VAULT]
BEFORE:   Yiffai: [看起来我在某个金库里面，但根本没有锁，只有一些画着奇怪符号的屏幕……]
AFTER:   Yiffai: [看起来我在某个金库里面，但根本没有锁，只有一些画着奇怪符号的屏幕……]
ROW CAT:Od03c0ba1c7de16846bda | L2575 | no manual edit
EN: [BUT INSTEAD OF A LOCK ALL I HAVE ARE SOME SCREENS WITH]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O180fd33b7e038390cc4f | L2576 | no manual edit
EN: [WEIRD SYMBOLS ON THEM...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of2462d35add8e285b618 | L2577 | EDIT E05-043
EN: [CAAAAN YOU DESCRIBE THEM ANY BETTER, PUPPEROO?]
BEFORE:   Tomcat: [能～～把它们描述得再具体些吗，PUPPEROO？]
AFTER:   Tomcat: [能——把它们描述得再具体点吗，小狗崽？]
ROW CAT:Obff967059a313625a5fd | L2578 | no manual edit
EN: [WELL, THEY LOOK PRETTY SIMILAR TO SOME OF THE SYMBOLS]
BEFORE:   Yiffai: [嗯，它们看着跟这一带矮矮小小的Fenfen们用的某些符号很像。]
AFTER:   Yiffai: [嗯，它们看着跟这一带矮矮小小的Fenfen们用的某些符号很像。]
ROW CAT:O31fcfe0ea7cb508a1a19 | L2579 | no manual edit
EN: [USED BY THE SHORT LITTLE FENFEN FOLKS AROUND HERE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od623fde9b95823517a96 | L2580 | no manual edit
EN: [HMM, WELL IF YOU EVER RUN INTO THESE FENFEN IN THE FLESH]
BEFORE:   Mauser: [嗯，如果你哪天亲眼碰到这些Fenfen，也许你该留意他们对你说的话？]
AFTER:   Mauser: [嗯，如果你哪天亲眼碰到这些Fenfen，也许你该留意他们对你说的话？]
ROW CAT:O24f6b6cc3f7b08c95fdf | L2581 | no manual edit
EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O747507f348c681541085 | L2582 | no manual edit
EN: [YEAH, LIKE MAUSER SAID.]
BEFORE:   Tomcat: [对，就像毛瑟说的那样。]
AFTER:   Tomcat: [对，就像毛瑟说的那样。]
ROW CAT:Ofc146922ab65eac1b06a | L2583 | no manual edit
EN: [MIGHT BE WORTH GOING OVER WHAT THE LOCAL FENFEN SAY.]
BEFORE:   Tomcat: [或许值得把这一带Fenfen说过的话再过一遍。]
AFTER:   Tomcat: [或许值得把这一带Fenfen说过的话再过一遍。]
ROW CAT:O17ed061ff64f7f90db01 | L2584 | no manual edit
EN: [YOU GUYS ARE RIGHT. THEY COULD BE THE KEY TO THIS ALL!]
BEFORE:   Yiffai: [你们说得对。它们说不定就是这一切的关键！]
AFTER:   Yiffai: [你们说得对。它们说不定就是这一切的关键！]
ROW CAT:O14393dc8309b2a290de3 | L2585 | no manual edit
EN: [I'LL KEEP ON TRYING TO CRACK THIS CODE. YIFFAI OUT.]
BEFORE:   Yiffai: [我会继续设法破解这套密码。伊法伊通话完毕。]
AFTER:   Yiffai: [我会继续设法破解这套密码。伊法伊通话完毕。]
### P05-023 | action=apply
原问题：PUPPEROO是Tomcat对男主的逗弄称呼，当前原样遗留使中文中断，不应当新专名；拖音只在原有处保留。
本轮理由：PUPPEROO是Tomcat对Yiffai的犬类昵称，非新名字；只保已有拖音。
EDIT_IDS ["E05-043"]

## SC87c3d069f4408f43 | nsfw | datadm/all.ds | Queen.AreaX_falling noselect noamendfreq
CONTROL L2657 <Queen.AreaX_falling noselect noamendfreq>
ROW CAT:O9c18eaee7b31bca1adff | L2658 | no manual edit
EN: [NO MORE INTERFERENCE FROM YOU, SPACE BUG!]
BEFORE:   Queen: [你休想再来碍事，太空虫子！]
AFTER:   Queen: [你休想再来碍事，太空虫子！]
ROW CAT:Oeb8a32bc42ecba035d69 | L2659 | no manual edit
EN: [ENJOY THE CAPTIVATING VIEW OF PLANET TUTONE...]
BEFORE:   Queen: [好好欣赏图托恩星的迷人景色吧……]
AFTER:   Queen: [好好欣赏图托恩星的迷人景色吧……]
ROW CAT:O481f0b5251d740a4f371 | L2660 | no manual edit
EN: [...AS IT RUSHES TO MEET YOU! HAH! HAH! HAH!]
BEFORE:   Queen: [……看它冲过来迎接你！哈！哈！哈！]
AFTER:   Queen: [……看它冲过来迎接你！哈！哈！哈！]
ROW CAT:O3b6a569f59394f5533ef | L2661 | no manual edit
EN: [YIFFAI, Y-YOU'RE FALLING FROM LOW PLANETARY ORBIT!]
BEFORE:   Mauser: [伊法伊，你、你正从低行星轨道坠落！]
AFTER:   Mauser: [伊法伊，你、你正从低行星轨道坠落！]
ROW CAT:O959a47c4a9de035da535 | L2662 | no manual edit
EN: [I... I DON'T...]
BEFORE:   Mauser: [我……我不……]
AFTER:   Mauser: [我……我不……]
ROW CAT:Oe4ccb78ae4940b9c8493 | L2663 | no manual edit
EN: [TOMCAT, EVAL.]
BEFORE:   Bossu: [汤姆猫，评估情况。]
AFTER:   Bossu: [Tomcat，评估情况。]
ROW CAT:O7680fc134078537c5d92 | L2664 | EDIT E05-044
EN: [ALREADY ON IT. STARSUIT PARACHUTE NOT AVAILABLE...]
BEFORE:   Tomcat: [已在处理。星际服降落伞无法使用……]
AFTER:   Tomcat: [已经在查。星际服的降落伞无法使用……]
ROW CAT:O3aa0dfd77aa3faf256c2 | L2665 | EDIT E05-045
EN: [KINETIC ARRESTORS INSUFFICIENT AT THIS ALTITUDE.]
BEFORE:   Tomcat: [此高度的动能制动器不足。]
AFTER:   Tomcat: [在这个高度，动能制动器的制动力不够。]
ROW CAT:O5bdc069245b1ad093f2a | L2666 | no manual edit
EN: [THE AGENT'S STARSHIP?]
BEFORE:   Bossu: [特工的星际飞船呢？]
AFTER:   Bossu: [特工的星际飞船呢？]
ROW CAT:O39f80fbcf82327fd5c18 | L2667 | no manual edit
EN: [DAMAGED. ITS AUTOPILOT WILL NOT EXIT THE ATMOSPHERE]
BEFORE:   Tomcat: [损坏了。以这艘船现在的状况，它的自动驾驶不会驶出大气层。]
AFTER:   Tomcat: [损坏了。以这艘船现在的状况，它的自动驾驶不会驶出大气层。]
ROW CAT:Ob111185b3ffa5911f841 | L2668 | no manual edit
EN: [WITH THE VESSEL IN THAT CONDITION.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O3f80a1412054e81ba8b9 | L2669 | no manual edit
EN: [UNDERSTOOD, TOMCAT. AGENT YIFFAI, WE WILL SEEK ANY-]
BEFORE:   Bossu: [明白，汤姆猫。特工伊法伊，我们会设法——]
AFTER:   Bossu: [明白，Tomcat。特工伊法伊，我们会设法——]
ROW CAT:O2738f28b14a723083ce9 | L2670 | EDIT E05-046
EN: [YOUR SIGNAL'S BREAKING UP... I CAN'T KEEP...!]
BEFORE:   Mauser: [你的信号在断……我撑不住……！]
AFTER:   Mauser: [你的信号断断续续的……我没法维持……！]
ROW CAT:O6cfdbe14e27cbf6d1a2d | L2671 | no manual edit
EN: [...SOMEONE THINK OF SOMETHING!!]
BEFORE:   Mauser: [……谁快想个办法！！]
AFTER:   Mauser: [……谁快想个办法！！]
### P05-024 | action=apply
原问题：紧急技术评估应说明设备制动能力不足，“此高度的动能制动器不足”像设备数量不足，定语关系生硬，降低救援判断清晰度。
本轮理由：两个独立有效槽保降落伞不可用及高度下制动能力不足，不写成设备数量不足。
EDIT_IDS ["E05-044", "E05-045"]
### P05-025 | action=apply
原问题：Mauser在总部接线，前半已明说信号衰减；“我撑不住”容易变成本人遭遇物理险境。原文省略keep宾语，建议仍保留未说完的省略，不擅补完整救援动作。
本轮理由：Mauser在总部接线，keep未完宾语仍不补全；维持指向信号而非肉体撑不住。
EDIT_IDS ["E05-046"]

## SC70adcf011b42bbeb | nsfw | datadm/all.ds | Tomcat.AreaA_map42_a noselect
CONTROL L2238 <Tomcat.AreaA_map42_a noselect>
ROW CAT:Ob8bb693ad28f263818d5 | L2239 | EDIT E05-047
EN: [NO ELEVATED HEART RATE...]
BEFORE:   Tomcat: [没有升高的心率……]
AFTER:   Tomcat: [心率没升高……]
ROW CAT:O712a52df9365d4eebef8 | L2240 | EDIT E05-048
EN: [HUH? WHAT? WHY'D YOU CALL ME U-]
BEFORE:   Yiffai: [啊？什么？你为什么叫我U-]
AFTER:   Yiffai: [啊？什么？你打电话来干什——]
ROW CAT:O53011c299271c5343c95 | L2241 | no manual edit
EN: [BLOOD PRESSURE'S FINE, NOT EVEN ANY EYE MOVEMENT...]
BEFORE:   Tomcat: [血压正常，连眼动都没有……]
AFTER:   Tomcat: [血压正常，连眼动都没有……]
ROW CAT:O06c29651e7f88b17d340 | L2242 | EDIT E05-049
EN: [BUT SOMETHING'S WRONG WITH YOU, PUP.]
BEFORE:   Tomcat: [但你有点不对劲，Pup。]
AFTER:   Tomcat: [可你不太对劲啊，小狗崽。]
ROW CAT:O9acd1acfd0332aac8c93 | L2243 | no manual edit
EN: [WHAT ARE YOU TALKING ABOUT?]
BEFORE:   Yiffai: [你在说什么？]
AFTER:   Yiffai: [你在说什么？]
ROW CAT:Oc62eb4fc6f3b74b075bf | L2244 | EDIT E05-050
EN: [ANY OTHER FIELD AGENT WHO SUDDENLY BECAME AN OWNER]
BEFORE:   Tomcat: [其他任何一个外勤特工，要是突然成了一双Mark IV Cosmoboots的主人，都会彻底歇斯底里！]
AFTER:   Tomcat: [换成别的外勤特工，突然弄到一双 Mark IV Cosmoboots，早就兴奋得发疯了！]
ROW CAT:Ocfb4fa707288ae30e46c | L2245 | no manual edit
EN: [OF A PAIR OF MARK IV COSMOBOOTS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O8dae3ad5bfb4e2dde929 | L2246 | no manual edit
EN: [WOULD BE ABSOLUTELY HYSTERICAL!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O6f5e2590d303c9aea2cb | L2247 | EDIT E05-051
EN: [...YOU MEAN THESE SHOES THAT I JUST HAD TOSSED AT ME?]
BEFORE:   Yiffai: [……你是说这双刚被朝我扔过来的鞋？]
AFTER:   Yiffai: [……你是说刚才被扔到我这儿的这双鞋？]
ROW CAT:O72fd3bea919a28685984 | L2248 | EDIT E05-052
EN: [THOSE AREN'T JUST SHOES]
BEFORE:   Mauser: [那些可不只是鞋]
AFTER:   Mauser: [那可不是普通鞋。]
ROW CAT:O0fbc90e8382621b1b79e | L2249 | no manual edit
EN: [NO?]
BEFORE:   Yiffai: [不是？]
AFTER:   Yiffai: [不是？]
ROW CAT:Of2f69df21e8cf0f42ca6 | L2250 | EDIT E05-053
EN: [YEAH, THEY'RE /EXPENSIVE/ SHOES! LIMITED EDITIONS!]
BEFORE:   Tomcat: [对，它们是/昂贵/的鞋！限量版！]
AFTER:   Tomcat: [对，那是/贵得要命/的鞋！限量版！]
ROW CAT:O0d3b37d57d9ae3bced35 | L2251 | no manual edit
EN: [COMPLETE WITH TRAJECTORAL BOOSTERS!]
BEFORE:   Tomcat: [还配有轨迹推进器！]
AFTER:   Tomcat: [还配有轨迹推进器！]
ROW CAT:O64700c98c8c11f5e5e6b | L2252 | no manual edit
EN: [BUT ON TOP OF THAT THEY'LL LET YOU DO COOL DIVE KICKS!]
BEFORE:   Mauser: [但除此之外，它们还能让你使出很酷的俯冲踢！]
AFTER:   Mauser: [但除此之外，它们还能让你使出很酷的俯冲踢！]
ROW CAT:Obb5fd4bc7e822edbfe21 | L2253 | no manual edit
EN: [YEAH, GIVE IT A TRY NEXT TIME YOU JUMP AROUND.]
BEFORE:   Tomcat: [对，下次你跳来跳去的时候试一下。]
AFTER:   Tomcat: [对，下次你跳来跳去的时候试一下。]
ROW CAT:Oeb5c0b7b759df6b6e0c8 | L2254 | EDIT E05-054
EN: [PRESS DOWN + JUMP WHILE ALREADY IN THE AIR]
BEFORE:   Tomcat: [已经在空中时按下 DOWN + JUMP，你就会做出一次俯冲踢；如果接触到任何会承受伤害的东西，还会把你向上弹起。]
AFTER:   Tomcat: [人在空中时按 DOWN + JUMP，就能使出俯冲踢。踢中能受伤的东西，还能借力向上弹起。]
ROW CAT:Ob33e28dadd7e5a62161a | L2255 | no manual edit
EN: [AND YOU'LL DO A DIVEKICK THAT WILL ALSO BOUNCE YOU UP]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7bd64f3795292d5bd714 | L2256 | no manual edit
EN: [IF YOU MAKE CONTACT WITH ANYTHING THAT TAKES DAMAGE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc5861e7aa6e7ae7df4d2 | L2257 | no manual edit
EN: [OH, NEAT, SO I CAN POGO OFF OF THINGS NOW?]
BEFORE:   Yiffai: [哦，不错，所以我现在能从东西上弹起来了？]
AFTER:   Yiffai: [哦，不错，所以我现在能从东西上弹起来了？]
ROW CAT:O76ccc5ab9c24e42ac47f | L2258 | no manual edit
EN: [YUP, JUST REMEMBER THAT DOWN + JUMP WILL ONLY DIVEKICK]
BEFORE:   Mauser: [对，只要记住：只有身处半空时，按 DOWN + JUMP 才会做出俯冲踢！]
AFTER:   Mauser: [对，只要记住：只有身处半空时，按 DOWN + JUMP 才会做出俯冲踢！]
ROW CAT:Obc8b0a9fa96e90a2d293 | L2259 | no manual edit
EN: [WHILE YOU'RE MID-AIR!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oe6563a08c845a4d27d95 | L2260 | no manual edit
EN: [DOWN + JUMP WHILE MID-AIR, GOT IT. TIME TO BOUNCE!]
BEFORE:   Yiffai: [半空时 DOWN + JUMP，知道了。该弹起来了！]
AFTER:   Yiffai: [半空时 DOWN + JUMP，知道了。该弹起来了！]
### P05-026 | action=apply
原问题：call me up在这里是打电话，当前“你为什么叫我U-”把短语尾词当台词字母；连同前后体征检查重建铺垫，Pup也不应残留为专名。
本轮理由：call up为打电话；原被打断功能保留，不残留字母U，不无端给专业检查添口吃。
EDIT_IDS ["E05-047", "E05-048", "E05-049"]
### P05-027 | action=apply
原问题：当前“成为…主人／彻底歇斯底里／昂贵的鞋”像履历与病症描述；这是装备迷见主角无反应后的夸张控诉，重写为自然兴奋并保留贵—限量的落点。品牌型号不擅改。
本轮理由：装备迷夸张兴奋而非病症，保Mark IV Cosmoboots型号与斜线强调，不改其他未裁定专名。
EDIT_IDS ["E05-050", "E05-051", "E05-052", "E05-053"]
### P05-028 | action=apply
原问题：当前整句按英语关系从句层层叠加，“接触到任何会承受伤害的东西”不易一听读懂；把输入、动作、反弹条件顺序讲清，不改按键和命中条件。
本轮理由：完整旧合句三源行均保留，输入/动作/命中可受伤物/反弹条件不变。
EDIT_IDS ["E05-054"]

## SCcfed64c6d940ad62 | nsfw | datadm/all.ds | TomcatItems.StatOctopus
CONTROL L3973 <TomcatItems.StatOctopus>
ROW CAT:O796de416215c9c6c3c38 | L3974 | no manual edit
EN: [DUDE.]
BEFORE:   Tomcat: [老兄。]
AFTER:   Tomcat: [老兄。]
ROW CAT:O2972be3743d80696fc1f | L3975 | no manual edit
EN: [OCTOPUS.]
BEFORE:   Tomcat: [章鱼。]
AFTER:   Tomcat: [章鱼。]
ROW CAT:Oa51c23211f1e5bead498 | L3976 | EDIT E05-055
EN: [I LOVE OCTOPUS.]
BEFORE:   Tomcat: [我爱章鱼。]
AFTER:   Tomcat: [我最爱章鱼了。]
ROW CAT:Ocb15089e2566c4856b7d | L3977 | EDIT E05-056
EN: [DUDE. BRO. GIMME.]
BEFORE:   Tomcat: [老兄。兄弟。给我。]
AFTER:   Tomcat: [老兄，兄弟，给我来点。]
ROW CAT:Oc720820f32b7455b4445 | L3978 | EDIT E05-057
EN: [IT MAKES YOU SMARTER TOO, I NEED IT.]
BEFORE:   Tomcat: [它也能让你更聪明，我需要它。]
AFTER:   Tomcat: [还能让人变聪明，我正需要呢。]
ROW CAT:O7bd91a7928d29114953d | L3979 | EDIT E05-058
EN: [D U D E . . .]
BEFORE:   Tomcat: [D U D E . . .]
AFTER:   Tomcat: [老——兄……]
### P05-029 | action=apply
原问题：末句D U D E为同一称呼拉长，不是专名；整段刻意短促地馋食讨要，最后原样英文打断重复催讨的笑点。不新增猫叫。
本轮理由：保短促讨食节奏，末句D U D E为称呼拉长而非名字，不添猫叫。
EDIT_IDS ["E05-055", "E05-056", "E05-057", "E05-058"]

## SCe2b05d5a4cb5a705 | nsfw | datav/dictionary.json | ui.breeding.Dwarf.affinity
ROW CAT:O5c6914e6eb5680f991cc | L- | no manual edit
EN: THE DWARF GLOWERS THROUGH|THE BARS, CHALLENGING YOU TO|MEET HIS GAZE.
BEFORE: 矮人透过栏杆怒视，|挑衅你|与他对视。
AFTER: 矮人透过栏杆怒视，|挑衅你|与他对视。
ROW CAT:O731e71de3518446fbac9 | L- | EDIT E05-060
EN: THE DWARF GRUMBLES ABOUT HIS|ACCOMMODATIONS, BUT OFFERS|YOU A GRUFF SMILE.
BEFORE: 矮人抱怨住处，|但给了你一个|粗声的笑。
AFTER: 矮人嘟囔着抱怨住处，|却还是冲你|粗犷地笑了笑。
ROW CAT:Oa062ad9c0d799a206c43 | L- | no manual edit
EN: THE DWARF WAGS HIS STUMPY|TAIL AS YOU APPROACH, EAGER|FOR YOUR ATTENTION.
BEFORE: 矮人在你走近时|摇着短尾巴，急切|想要你的关注。
AFTER: 矮人在你走近时|摇着短尾巴，急切|想要你的关注。
ROW CAT:Oa881fc8d5c1b5dbae41c | L- | no manual edit
EN: THE DWARF WANTS NO TREASURE|BEYOND YOUR COMPANIONSHIP.|WHAT A WONDERFUL PET!
BEFORE: 矮人不要财宝，|只要你的陪伴。|真是棒极了的宠物！
AFTER: 矮人不要财宝，|只要你的陪伴。|真是棒极了的宠物！
### P05-031 | action=apply
原问题：gruff smile不是有粗声音的笑；抱怨与笑之间的转折应自然落地，不新增亲密关系。
本轮理由：gruff为粗犷而非笑的声音粗；保抱怨与示好的转折及三段管线。
EDIT_IDS ["E05-060"]

## SC58ccd1b993ca1ca5 | sfw | datav/dictionary.json | ui.breeding.Kobold.affinity
ROW SFW15a19b12854acc3aec7db2c1 | L- | no manual edit
EN: THE KOBOLD SNARLS, BARING|HIS SHARP TEETH. HE WANTS|TO PUT *YOU* IN A CAGE!
BEFORE: 科博德咆哮着，|露出尖牙。他想|把*你*关进笼子！
AFTER: 科博德咆哮着，|露出尖牙。他想|把*你*关进笼子！
ROW SFW28a02cdeb21454bb0c1e793e | L- | no manual edit
EN: THE KOBOLD SNICKERS SOFTLY.|IS HE SCHEMING SOMETHING, OR|JUST HAPPY TO SEE YOU?!
BEFORE: 科博德轻声窃笑。|他在密谋什么，还是|只是见到你高兴？！
AFTER: 科博德轻声窃笑。|他在密谋什么，还是|只是见到你高兴？！
ROW SFWb62610a60cd111d1800a1671 | L- | EDIT E05-059
EN: THE KOBOLD CURLS UP,|BASKING IN YOUR PRESENCE.|WHAT A WONDERFUL PET!
BEFORE: 科博德蜷起来，|沐浴在你的存在里。|真是棒极了的宠物！
AFTER: 科博德蜷起身子，|享受着你的陪伴。|真是棒极了的宠物！
ROW SFWf58fb0e19d270c5744164ef6 | L- | no manual edit
EN: THE KOBOLD TILTS HIS HEAD|IN CURIOSITY. HE'S STARTING|TO FAVOR YOUR SCENT.
BEFORE: 科博德好奇地|歪着头。他开始|偏爱你的气味。
AFTER: 科博德好奇地|歪着头。他开始|偏爱你的气味。
### P05-030 | action=apply
原问题：bask in your presence是享受陪伴，当前“沐浴在你的存在里”抽象直译，破坏亲密度最高档的自然叙述。保留三段管线仅作段落提案，实际排版另验。
本轮理由：basking仅享受在场陪伴，不无据新增依偎接触；保三段管线。
EDIT_IDS ["E05-059"]

## SC87699368a000005b | nsfw | datav/dictionary.json | ui.data.f_AgentF03
ROW CAT:O8f8a542f2d29d6eef3a3 | L- | EDIT E05-061
EN: A SHY SCOUT LEARNS THE JOYS|OF DATA COLLECTION.
BEFORE: 害羞的侦察兵学会了|数据采集的乐趣。
AFTER: 害羞的侦察兵|体会到了数据采集的乐趣。
### P05-032 | action=apply
原问题：learn the joys是体验其中乐趣，不是“学会乐趣”；完整回忆菜单简介需成自然短段。
本轮理由：菜单为Kahr报告简介，体验乐趣不是学会乐趣；不冒充她亲口独白。
EDIT_IDS ["E05-061"]

## SCdb93fddeabca5d30 | nsfw | datav/dictionary.json | ui.data.m_ClassicWerepup
ROW CAT:O8239dcdd65652cac76e1 | L- | EDIT E05-062
EN: REMINISCING AND HESITATING|AFTER DEFEATING A SMALL PUP!
BEFORE: 回味着，又犹豫着|在打败一只小狼崽之后！
AFTER: 打败小狼崽后，|追忆往事，又犹豫不决！
### P05-033 | action=apply
原问题：当前把时间条件后置成“回味着，又犹豫着在打败…之后”，中文无法连读。只表达追忆与犹豫，不擅补回忆对象。
本轮理由：只将小狼崽战后追忆/犹豫依中文语序表达，不补回忆对象。
EDIT_IDS ["E05-062"]

## SC96a89c88351f6c03 | nsfw | datay/scripts_pack.json | /missionLog/female/2/header
ROW CAT:O6c8c72674ecd9051df36 | L- | no manual edit
EN: ACQUIRED ZENER WAVES
BEFORE: 获得泽纳波浪
AFTER: 获得泽纳波浪
### P05-034 | action=defer
原问题：wave在超能力/泽纳取得提示里为“波”，不是水的“波浪”。该nested值运行用途未验证；这是有条件文本提案，不宣称游戏中显示。
本轮理由：Q05-034：nested JSON运行用途未证，波浪/波的文本方向可疑但不越过用途核验直接回填。
EDIT_IDS []

## SC830eb1f5ee0725d9 | nsfw | datay/scripts_pack.json | /missionLog/male/13/text
ROW CAT:Oc0cc6e195ce90d6ab5fe | L- | no manual edit
EN: With ger ship downed and a  | storm brewing outside, agent| Yiffany had no choice but to| 
EN+ chance a journey into the   | depths of an abandoned alien| facility for shelter.       |
EN+ 
                            |
Her first order of business | should be to reestablish    |
EN+  communications with         | headquarters!
BEFORE: 飞船坠毁，|外面又风暴将至，|特工伊法妮|别无选择，|只能冒险深入废弃的外星设施|寻找庇护。|
                            |

BEFORE+ 她的第一要务是|恢复|与总部的|通讯！

AFTER: 飞船坠毁，|外面又风暴将至，|特工伊法妮|别无选择，|只能冒险深入废弃的外星设施|寻找庇护。|
                            |

AFTER+ 她的第一要务是|恢复|与总部的|通讯！

### P05-036 | action=defer
原问题：路径标male/13而源段写Yiffany/her；当前译文忠实女主身份。须核实际触发、测试数据与路径映射，不能以男线路径直接报中文错人。源中ger亦有拼写异常。
本轮理由：Q05-036：male路径与源Yiffany/her冲突，当前译文忠实源身份；未核运行映射，不能强改为Yiffai。
EDIT_IDS []

## SCd8d9edde0d88a8f5 | nsfw | datay/scripts_pack.json | /shops/male/Area0_Macsen1/products/2/displayName
ROW CAT:Ofd57d76ea1e8fff0645c | L- | no manual edit
EN: OLD JUNK
BEFORE: 旧货铺
AFTER: 旧货铺
### P05-035 | action=defer
原问题：路径是商品displayName，OLD JUNK指旧杂物/旧货，不是店铺。用途仍需运行验证，不能据资源位置声称已经可见。
本轮理由：Q05-035：OLD JUNK可能是商品名而非店铺，但nested JSON显示用途未证，不以路径推断作为应用批准。
EDIT_IDS []

## SC29248fbcf75fe78f | sfw | vsn/f_EndingGood/script.vsn | vsn/f_EndingGood/script.vsn
CONTROL L1 music: CutsceneE
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): Ending01
CONTROL L4 rewind!
ROW SFWedb93cce7c0c3615ac0c4623 | L5 | no manual edit
EN: Nooo! Curse you damn Yiffai siblings!
BEFORE: text: 不——！诅咒你们这该死的伊法伊姐弟！
AFTER: text: 不——！诅咒你们这该死的伊法伊姐弟！
ROW SFWb06d106d2c4e9b7d4d9d6625 | L6 | no manual edit
EN: I was supposed to rule the world... no... the Galaxy! 
BEFORE: text: 我本该统治世界的……不……是整个银河！ 
AFTER: text: 我本该统治世界的……不……是整个银河！ 
ROW SFWeb4a9023e660c4e6ebfbb45c | L7 | no manual edit
EN: And now... now...!
BEFORE: text: 而现在……现在……！
AFTER: text: 而现在……现在……！
ROW SFWd533e8ace9f1a7f16606fc0a | L8 | no manual edit
EN: ...............!!!
BEFORE: text: ...............!!!
AFTER: text: ...............!!!
ROW SFW59cfadc6960e0e30782c8e78 | L9 | no manual edit
EN: GAAAAARRRRRRRGGGGGGGHGHHHH!
BEFORE: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
AFTER: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
CONTROL L11 fadecut(0.266, 2): Ending02
CONTROL L12 rewind!
ROW SFW8f173e968433e0aa25dba076 | L13 | no manual edit
EN: Wow sis, did we really just... save a whole planet?
BEFORE: text: 哇，老姐，我们刚刚真的……拯救了一整颗星球？
AFTER: text: 哇，老姐，我们刚刚真的……拯救了一整颗星球？
ROW SFW11d1ee02084eb299068d7339 | L14 | no manual edit
EN: Yeah lil bro, I think we did! Par for the course on my missions, really.
BEFORE: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
AFTER: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
ROW SFWdfeba1ea855035b37dcfc3b6 | L15 | no manual edit
EN: Buuut pretty impressive for my baby bro's first real mission, so good going!
BEFORE: text: 不过——对我家小弟的第一次真正任务来说，已经很厉害了，干得漂亮！
AFTER: text: 不过——对我家小弟的第一次真正任务来说，已经很厉害了，干得漂亮！
CONTROL L17 fadecut(0.266, 2): Ending03
CONTROL L18 rewind!
ROW SFW0d6efdd9a483be4e811eb0fb | L19 | no manual edit
EN: The heroes of Tutone! They return!
BEFORE: text: 图托恩的英雄们！他们回来了！
AFTER: text: 图托恩的英雄们！他们回来了！
ROW SFW56a9b2eb16b8e6f8ee92e41e | L20 | no manual edit
EN: Traeh has been defeated, her psychic disturbances are no more and her minions flee!
BEFORE: text: 特蕾已经被击败，她的灵能扰动不复存在，她的爪牙正在逃窜！
AFTER: text: 特蕾已经被击败，她的灵能扰动不复存在，她的爪牙正在逃窜！
ROW SFW609f4827e4478e5ed332b381 | L21 | no manual edit
EN: Cheers for the heroes!
BEFORE: text: 为英雄们欢呼吧！
AFTER: text: 为英雄们欢呼吧！
CONTROL L23 fadecut(0.266, 2): Ending04A
CONTROL L24 rewind!
ROW SFW1abf77379154d6886ef9ec14 | L25 | EDIT E05-063
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: 汪！汪！万岁！
ROW SFW6ed8ca9dddd7913adfc5a51c | L26 | EDIT E05-064
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: 汪！汪！万岁！
ROW SFWd9699ecd9b660c95f8495f23 | L27 | EDIT E05-065
EN: BLESSED BE THE COSMOBREEDERS, SAVIORS OF OUR PLANET!
BEFORE: text: 愿宇宙育种者受颂，我们星球的救星！
AFTER: text: 赞颂宇宙育种者，我们星球的救星！
CONTROL L29 snap: Ending04B
ROW SFWb4c526dd43ca9ef7438722b3 | L30 | no manual edit
EN: Wow, good going you two! Clearing out a whole planet of baddies...
BEFORE: text: 哇，你们俩真棒！把整颗星球的坏蛋都清了个遍……
AFTER: text: 哇，你们俩真棒！把整颗星球的坏蛋都清了个遍……
ROW SFW50455f59c97de775e24dfb38 | L31 | no manual edit
EN: That's definitely gonna help the local fauna get back on track!
BEFORE: text: 这肯定能帮当地动物族群重回正轨！
AFTER: text: 这肯定能帮当地动物族群重回正轨！
CONTROL L33 snap: Ending04C
ROW SFWec435b6eefe8316ac4c67f63 | L34 | no manual edit
EN: I knew you two could do it. Never had a doubt in my mind.
BEFORE: text: 我就知道你们俩能行。我从没怀疑过。
AFTER: text: 我就知道你们俩能行。我从没怀疑过。
ROW SFW496a3aa168e4d8a88c57b130 | L35 | no manual edit
EN: Not even when one of you went AWOL and stopped responding to all communica-
BEFORE: text: 就连你们中有人擅离职守、不再回应任何通——
AFTER: text: 就连你们中有人擅离职守、不再回应任何通——
ROW SFW1d163a96f0a48c15382dc1eb | L36 | no manual edit
EN: -Ahem...
BEFORE: text: -嗯哼……
AFTER: text: -嗯哼……
ROW SFW2ea8567c19c70e1e8be2d232 | L37 | no manual edit
EN: This will definitely be a good report to have filed away, Agents!
BEFORE: text: 这份报告绝对值得归档留存，特工们！
AFTER: text: 这份报告绝对值得归档留存，特工们！
CONTROL L39 snap: Ending04D
ROW SFW00fcc5cde1c74fe3899b1857 | L40 | EDIT E05-066
EN: Nice one, grrrrl! You and your pup brother really cleaned up down there!
BEFORE: text: 真有你的，grrrrl！你和你弟弟在下面可把坏蛋清了个遍！
AFTER: text: 真有你的，姑——娘！你和你那小狗崽弟弟把下面收拾得真干净！
ROW SFW98727feab7330d80910e4ed0 | L41 | EDIT E05-067
EN: Just don't forget about us at HQ when all the fame goes to your heads, alright?
BEFORE: text: 等名声让你们飘飘然的时候，可别忘了我们总部的人，好吗？
AFTER: text: 可别出了名就飘飘然，把我们总部的人都忘了啊，好吗？
CONTROL L43 snap: Ending04E
ROW SFW18d13604f06cf5e4f1f8778c | L44 | no manual edit
EN: HOORAH FOR YIFFANY AND YIFFAI! STAR COSMOBREEDERS!
BEFORE: text: 为伊法妮和伊法伊欢呼！明星宇宙育种者！
AFTER: text: 为伊法妮和伊法伊欢呼！明星宇宙育种者！
ROW SFWd23be66dcca025fdd2f25608 | L45 | no manual edit
EN: H O O R A Y ! ! !
BEFORE: text: 好 耶 ！ ！ ！
AFTER: text: 好 耶 ！ ！ ！
CONTROL L47 fadecut(0.266, 2): Ending05
CONTROL L48 rewind!
ROW SFWf8f77e1746f90b2cb4da862f | L49 | no manual edit
EN: Heh, how about that, sis? We made a pretty good team, didn't we?
BEFORE: text: 嘿，瞧见没，老姐？我们配合得挺不错，不是吗？
AFTER: text: 嘿，瞧见没，老姐？我们配合得挺不错，不是吗？
ROW SFW8f7d96cce40f9594119c6aec | L50 | no manual edit
EN: Wellll... you did alright, bro. 
BEFORE: text: 嗯——……你还行啦，老弟。 
AFTER: text: 嗯——……你还行啦，老弟。 
ROW SFW156d7461873d4d6e6e44d7f4 | L51 | no manual edit
EN: ...for a pup. 
BEFORE: text: ……就一只小崽子而言。 
AFTER: text: ……就一只小崽子而言。 
CONTROL L53 fadecut(0.266, 2): Black
CONTROL L54 rewind!
ROW SFWad72d6a86e3611cc63332008 | L55 | no manual edit
EN: [SO ENDS THE REPORT ON PLANET TUTONE.]
BEFORE: text: [图托恩星球的报告到此结束。]
AFTER: text: [图托恩星球的报告到此结束。]
ROW SFWca4cca75f4de1abc5fbd11b0 | L56 | EDIT E05-068
EN: [A PLANET WITH A TUMULTUOUS HISTORY, FACING THE GREATEST CHALLENGES OF ITS TIME]
BEFORE: text: [这是一颗历史动荡的星球，直面着它所处时代最严峻的挑战]
AFTER: text: [这颗历经动荡的星球，面临着这个时代最严峻的挑战；]
ROW SFW373e610402c5eec060718799 | L57 | EDIT E05-069
EN: [SAVED BY THE VALIANT EFFORTS OF TWO BRAVE COSMOBREEDERS:]
BEFORE: text: [被两位勇敢的宇宙育种者奋勇拯救：]
AFTER: text: [两位勇敢的宇宙育种者奋战不懈，拯救了它：]
ROW SFW87ed6c61eb40d9235caa6b30 | L58 | EDIT E05-070
EN: [YIFFANY YIFFAI, ELDER SISTER AND SEASONED VETERAN WITH UNMATCHED COMBAT SKILL]
BEFORE: text: [伊法妮·伊法伊，姐姐，久经沙场的老兵，拥有无与伦比的战斗技巧]
AFTER: text: [姐姐伊法妮·伊法伊，久经沙场，战斗技巧无可匹敌；]
ROW SFWb80a63cde268c59750951ffd | L59 | EDIT E05-071
EN: [AND YIFFAI YIFFAI, THE YOUNGER BROTHER PRODIGY WITH UNENDING ENTHUSIASM]
BEFORE: text: [以及伊法伊·伊法伊，热情永不枯竭的天才弟弟]
AFTER: text: [弟弟伊法伊·伊法伊，天赋出众，始终热情满怀。]
ROW SFW6b84e2714c498964a87c22ea | L60 | EDIT E05-072
EN: [WITH THE TWO OF THEM TEAMED UP, THERE'S NO MISSION THAT THEY CAN'T HANDLE]
BEFORE: text: [两人携手，没有他们应付不来的任务]
AFTER: text: [两人携手，就没有应付不了的任务。]
ROW SFW8008639b335602c7471ecd91 | L61 | EDIT E05-073
EN: [AND THE PPP IS PROUD TO HAVE THEM AS AGENTS.]                      -SIGNED, BOSSU
BEFORE: text: [PPP很荣幸有他们两位这样出色的特工。]                      -署名，Bossu
AFTER: text: [PPP以拥有他们这样的特工为荣。]                      -署名，Bossu
CONTROL L63 fademusic(0.0, 1.0)
CONTROL L64 fadeout(1.0, 1.0, 4)
### P05-038 | action=apply
原问题：YIP/YIP/HOORAY把犬类叫声嵌进欢呼，当前原样YIP与“愿…受颂”均妨碍群众欢庆的中文节奏；不是证明所有说话者物种的证据。
本轮理由：犬叫嵌入欢呼而非群众物种鉴定，保祝颂宇宙育种者与救星意义。
EDIT_IDS ["E05-063", "E05-064", "E05-065"]
### P05-039 | action=apply
原问题：grrrrl是Tomcat拖长的girl称呼，不是人名；当前原样残留。合并角色同一发言短段，保持熟人调侃与弟弟犬类称呼，不提前否定成名仅是玩笑。
本轮理由：按参照此声为Tomcat，受话Yiffany及其弟Yiffai；两槽分别保赞扬和成名飘然后的提醒。
EDIT_IDS ["E05-066", "E05-067"]
### P05-040 | action=apply
原问题：结尾是Bossu署名报告，不是无归属的全知性格定论；当前“直面着…被…奋勇拯救”跨框连读僵硬。重建报告句法，保留原署名、姓名长幼与赞扬归属；实际控制标签和输出节点不得据此直接合并。
本轮理由：Bossu署名终报，保姐姐Yiffany Yiffai与弟弟Yiffai Yiffai全名、长幼、评价归属。逐槽重建，保原text前缀/方括号/末署名。
EDIT_IDS ["E05-068", "E05-069", "E05-070", "E05-071", "E05-072", "E05-073"]

## SC394405c5c61c5988 | nsfw | vsn/m_GameOverArea0/script.vsn | vsn/m_GameOverArea0/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 snap: ClassicGameOverArea0A
CONTROL L3 waitForCue!
CONTROL L4 rewind!
ROW CAT:O2a6ca029526e6ca9cf50 | L5 | no manual edit
EN: Ow, I didn't expect to take such a rough bump.
BEFORE: text: 嗷，没想到会挨这么重的一下。
AFTER: text: 嗷，没想到会挨这么重的一下。
ROW CAT:Obe184f28d26fde62e54d | L6 | EDIT E05-074
EN: Guess I can use this chance to practice writing an end-of-capture report!
BEFORE: text: 正好借机练习写被俘结束报告！
AFTER: text: 正好借机练习写获释后的被俘经历报告！
ROW CAT:O1c790ea6ecde62eb9f64 | L7 | EDIT E05-075
EN: Lessee, just gotta start paying attention and see if anything notable happens
BEFORE: text: 让我想想，得开始留神，看看从现在到这段小小的……结束之前，有没有值得记录的事。
AFTER: text: 我看看……只要从现在开始留心，看看这段短短的……结束前，会发生什么值得记录的事。
ROW CAT:O8ea28decb6f05ea4edca | L8 | no manual edit
EN: between now and the end of this short...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L10 fadeout(1.0, 1.0, 4)
CONTROL L11 cut(0.06): Black
ROW CAT:Oaee1dcba07b366ac8bf1 | L12 | no manual edit
EN: ...little...
BEFORE: text: ……稍微……
AFTER: text: ……稍微……
ROW CAT:O1328ba32c5865a8e7681 | L13 | no manual edit
EN: ...napzzzz...z...
BEFORE: text: ……睡觉……呼……噜……
AFTER: text: ……睡觉……呼……噜……
CONTROL L16 fade(9, 0, 1)
CONTROL L17 fadein(1.0, 4): ClassicGameOverArea0B
CONTROL L18 rewind!
ROW CAT:O84d6d27e71df1ef6dc12 | L19 | no manual edit
EN: Would you look at that? Must've slept for quite a while since I was all groggy
BEFORE: text: 瞧瞧这事！我肯定睡了挺久，醒来还迷迷糊糊的，一醒来就发现自己正被套上拘束具！
AFTER: text: 瞧瞧这事！我肯定睡了挺久，醒来还迷迷糊糊的，一醒来就发现自己正被套上拘束具！
ROW CAT:O507a42891a8b11de6197 | L20 | no manual edit
EN: and woke to find myself being locked into some restraints!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O0c7e16060c68bd51c8a2 | L21 | no manual edit
EN: Not only that, but the jerks that were locking me into these cuffs...
BEFORE: text: 不光如此，那些把我锁进镣铐的混蛋……
AFTER: text: 不光如此，那些把我锁进镣铐的混蛋……
ROW CAT:O6f5b76065b49781fd8b9 | L22 | no manual edit
EN: ...looked just like that shorty that stole my gear to begin with!!
BEFORE: text: ……居然跟一开始偷我装备的矮子长得一模一样！！
AFTER: text: ……居然跟一开始偷我装备的矮子长得一模一样！！
CONTROL L24 cut(0.06): ClassicGameOverArea0C
CONTROL L25 rewind!
ROW CAT:O45ddd0d9b52ea6d44fb7 | L26 | no manual edit
EN: As soon as they got me chained up in some sort of ramshackle den of theirs
BEFORE: text: 他们刚把我锁进那破破烂烂的窝里，就开始轮流操我。都不先请我吃顿饭！
AFTER: text: 他们刚把我锁进那破破烂烂的窝里，就开始轮流操我。都不先请我吃顿饭！
ROW CAT:O054abfd5d6f3e84758aa | L27 | no manual edit
EN: they started to take turns rutting me. Didn't even get me dinner first or anything!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9f11860750ebc2ab91b7 | L28 | no manual edit
EN: With the shorties being so small it wasn't much of a workout for a pro like me
BEFORE: text: 这些小矮子个头太小，对我这种老手根本算不上运动，不过我看得出，这些吱吱怪都急着发泄呢。
AFTER: text: 这些小矮子个头太小，对我这种老手根本算不上运动，不过我看得出，这些吱吱怪都急着发泄呢。
ROW CAT:O627e56d7ab36b74a7cc1 | L29 | no manual edit
EN: but I could tell that these squeakers were pretty desperate for some release.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L31 cut(0.06): ClassicGameOverArea0H
CONTROL L32 rewind!
ROW CAT:O760e94c13d66e796b76d | L33 | no manual edit
EN: It was actually kinda fun to see the little fellas go to town on my tail...heh!
BEFORE: text: 看这些小家伙对着我尾巴底下猛干，还挺有意思……嘿！
AFTER: text: 看这些小家伙对着我尾巴底下猛干，还挺有意思……嘿！
ROW CAT:O104917e5465a83e5688c | L34 | no manual edit
EN: One after another they took turns, must've been at least a dozen of them...
BEFORE: text: 他们一个接一个轮着来，少说也有十几个……
AFTER: text: 他们一个接一个轮着来，少说也有十几个……
CONTROL L36 cut(0.06): ClassicGameOverArea0G
CONTROL L37 rewind!
ROW CAT:O3f3582d00219206dc926 | L38 | no manual edit
EN: The little guys only bred me one at a time but you could tell they were pent up
BEFORE: text: 小家伙们一次只来一个，可光听他们吱吱喳喳，就知道都憋坏了。
AFTER: text: 小家伙们一次只来一个，可光听他们吱吱喳喳，就知道都憋坏了。
ROW CAT:O628b9883272661606f16 | L39 | no manual edit
EN: by all the squeaking and chittering they were doing.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O103f7adf70dad199625e | L40 | no manual edit
EN: Every now and again one would get squeaked at for delaying the line
BEFORE: text: 时不时就有一个因耽误排队，被吱吱叫着催促，还在射就被催着赶走了！
AFTER: text: 时不时就有一个因耽误排队，被吱吱叫着催促，还在射就被催着赶走了！
ROW CAT:O9631300463388ff9f0e7 | L41 | no manual edit
EN: and they'd get hurried along while still squirting!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L44 cut(0.06): ClassicGameOverArea0D
CONTROL L45 rewind!
ROW CAT:Obc8dda1a7f77e0665e2f | L46 | no manual edit
EN: Being the center of so much attention was actually kinda fun.
BEFORE: text: 被这么多家伙团团围着，其实还挺好玩。
AFTER: text: 被这么多家伙团团围着，其实还挺好玩。
ROW CAT:O46f0843438ad9267c262 | L47 | no manual edit
EN: Learned a lot about their breeding habits
BEFORE: text: 我学到了不少他们的交配习性，可惜没更大的个体供研究，我还真有点失望！
AFTER: text: 我学到了不少他们的交配习性，可惜没更大的个体供研究，我还真有点失望！
ROW CAT:O2ceac7a36524a318f658 | L48 | no manual edit
EN: but I was almost dis- appointed that there were no larger specimens to study!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L50 cut(0.06): ClassicGameOverArea0D2
CONTROL L51 rewind!
ROW CAT:O1f4a8db55c2d68175508 | L52 | no manual edit
EN: Almost, until I noticed that I was alone in the cell.
BEFORE: text: 差点就是了，直到我发现牢房只剩我一个。 
AFTER: text: 差点就是了，直到我发现牢房只剩我一个。 
ROW CAT:Oc1e95d2a7186b2b23c08 | L53 | no manual edit
EN: The little guys had left while I was getting lost in my thoughts, rude, right?
BEFORE: text: 那帮小个子趁我走神时溜了，很没礼貌吧？
AFTER: text: 那帮小个子趁我走神时溜了，很没礼貌吧？
CONTROL L56 cut(0.06): ClassicGameOverArea0I
CONTROL L57 rewind!
ROW CAT:O716eb56024fd6a580eb2 | L58 | no manual edit
EN: I was just about to break out of there when my ears picked up the soft sounds of
BEFORE: text: 我正准备逃出去，耳朵却捕捉到有人沿着石地悄悄靠近的轻微声响。
AFTER: text: 我正准备逃出去，耳朵却捕捉到有人沿着石地悄悄靠近的轻微声响。
ROW CAT:O71da3e4147999bba56b6 | L59 | no manual edit
EN: someone creeping along the stones.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O123877ac5383db8c04ab | L60 | no manual edit
EN: ...along with some low growling...
BEFORE: text: ……还伴着几声低吼……
AFTER: text: ……还伴着几声低吼……
CONTROL L63 cut(0.06): ClassicGameOverArea0E
CONTROL L64 rewind!
ROW CAT:O8d8d4afe55eccca55209 | L65 | no manual edit
EN: Suddenly, out of the shadows came a giant beast of a creature!
BEFORE: text: 突然，一头巨兽从阴影里走了出来！ 
AFTER: text: 突然，一头巨兽从阴影里走了出来！ 
ROW CAT:O852ef17c8e145f374312 | L66 | no manual edit
EN: A muscled feline that could have probably torn me in half!
BEFORE: text: 那只肌肉发达的大猫，恐怕能把我撕成两半！
AFTER: text: 那只肌肉发达的大猫，恐怕能把我撕成两半！
ROW CAT:O2b1a1b35cc1779210f17 | L67 | no manual edit
EN: But only because I was chained up!
BEFORE: text: 可那也只是因为我被锁住了！
AFTER: text: 可那也只是因为我被锁住了！
ROW CAT:O4075e2dcf60d7eeefa2e | L68 | no manual edit
EN: Fortunately for him it was clear fighting wasn't what he had in mind.
BEFORE: text: 算他走运，显然他没打算跟我打架。
AFTER: text: 算他走运，显然他没打算跟我打架。
CONTROL L70 cut(0.06): ClassicGameOverArea0J
CONTROL L71 rewind!
ROW CAT:O8cb4461f95254b380951 | L72 | no manual edit
EN: I let him grab me however he wanted, since I was feeling kinda rowdy too, you know?
BEFORE: text: 我任他想怎么抓就怎么抓，毕竟我也有点躁动了，懂吧？
AFTER: text: 我任他想怎么抓就怎么抓，毕竟我也有点躁动了，懂吧？
ROW CAT:Of172df5908e4697edd21 | L73 | no manual edit
EN: Those little punks earlier were barely a warm up and I needed more!
BEFORE: text: 之前那群小混蛋连热身都不够，我还没过瘾呢！
AFTER: text: 之前那群小混蛋连热身都不够，我还没过瘾呢！
ROW CAT:O53cf28e2f209349d79fe | L74 | no manual edit
EN: I tried to make it sound like I was having a rough time handling him, though...
BEFORE: text: 不过，我故意哼得好像很难应付他似的……
AFTER: text: 不过，我故意哼得好像很难应付他似的……
ROW CAT:O00d15791892862b17509 | L75 | no manual edit
EN: You know, pretending like those giant pliable barbs of his were driving me crazy
BEFORE: text: 你懂的，装作在他用壮实的腰臀狠狠往我里面撞时，被他那些又大又软的倒刺弄得快疯了……
AFTER: text: 你懂的，装作在他用壮实的腰臀狠狠往我里面撞时，被他那些又大又软的倒刺弄得快疯了……
ROW CAT:O600f6cf883555f743b83 | L76 | no manual edit
EN: as he plowed into me roughly with those great haunches of his...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L79 cut(0.06): ClassicGameOverArea0F
CONTROL L80 rewind!
ROW CAT:O418ffbc1fe7a7b7695f5 | L81 | no manual edit
EN: I was so busy pretending like I was losing myself in the sexual moment
BEFORE: text: 我光顾着装出沉醉在性爱里的样子，差点没注意又有几只色猫围了过来。
AFTER: text: 我光顾着装出沉醉在性爱里的样子，差点没注意又有几只色猫围了过来。
ROW CAT:O4487ec09b129e656c977 | L82 | no manual edit
EN: that I almost didn't notice the additional lusty cats circling around.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc86870a45d985ef66077 | L83 | no manual edit
EN: I... I figured it was probably a great opportunity to study the species more...
BEFORE: text: 我……我想这大概是进一步研究这物种的好机会…… 
AFTER: text: 我……我想这大概是进一步研究这物种的好机会…… 
ROW CAT:O9bbd805bfa0eac9ac462 | L84 | no manual edit
EN: Besides, it's not like I was in any rush!
BEFORE: text: 再说，我又不赶时间！
AFTER: text: 再说，我又不赶时间！
ROW CAT:O2bbd3b3ca56f8a56ab94 | L85 | no manual edit
EN: I knew I could break out of that cell and escape those brutes whenever I wanted to.
BEFORE: text: 我知道，只要想逃，随时都能破牢而出，甩掉那些蛮兽。
AFTER: text: 我知道，只要想逃，随时都能破牢而出，甩掉那些蛮兽。
CONTROL L87 cut(0.06): Black
CONTROL L88 rewind!
ROW CAT:O380f4ed0d11facd4e06b | L89 | no manual edit
EN: Uhh if you're viewing this report, I guess it means I lost track of time
BEFORE: text: 呃，你要是在看这份报告，想必是我忘了时间，然后有人正好撞见了逃到一半的我，是吧？
AFTER: text: 呃，你要是在看这份报告，想必是我忘了时间，然后有人正好撞见了逃到一半的我，是吧？
ROW CAT:O0be3bc3ab177662232fc | L90 | no manual edit
EN: and someone stumbled across me mid-escape, huh?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od8c12721adddea8c585c | L91 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O10b33577a49de9fedaba | L92 | no manual edit
EN: ...you believe me, right?
BEFORE: text: ……你信我的，对吧？
AFTER: text: ……你信我的，对吧？
CONTROL L94 wait: 0.2
CONTROL L95 fadeout(1.0, 1.0, 4)
### P05-041 | action=apply
原问题：“被俘结束报告”是机械名词串；接下来short/little/nap分次被昏睡打断，是故作专业后睡着的笑点，建议保持未完句，不跨Black控制把“打盹”提前补齐。
本轮理由：男主Yiffai故作专业的被俘回顾，报告是获释后记录；不越Black控制提前说打盹，不动消费空尾。
EDIT_IDS ["E05-074", "E05-075"]

