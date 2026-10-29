# packet-09 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SC42015eed937529ef | nsfw | datadf/all.ds | Area0_Macsen2.DoggyHead
CONTROL L125 <Area0_Macsen2.DoggyHead>
ROW CAT:Oa5eca1f1d4398acff253 | L126 | EDIT E09-001
EN: A garment that I don't wear much anymore. It'd
BEFORE:   * 一件我已经不怎么穿的衣服。它大概会刚——刚好合身！ 
AFTER:   * 一件我已经不怎么穿的衣服。给你穿，大概正——合适！ 
ROW CAT:O440e5d61464076e410c7 | L127 | no manual edit
EN: probably fit you juuuuust fine!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P09-001 | action=apply
原问题：拉长juuuuust是商贩拖音，不是“刚——刚好”的结巴；保留推销语气和合句空尾。
本轮理由：保留probably的推测与商贩拖音，撤销重复“刚”造成的结巴；旧头行两句全部保留。
EDIT_IDS ["E09-001"]

## SCcbf017b30c0a13e0 | sfw | datadf/all.ds | AreaB_Prison1.Goodbye
CONTROL L917 <AreaB_Prison1.Goodbye>
ROW SFW821fd530496636fb9a822f11 | L918 | EDIT E09-002
EN: I'll be right along, heheh! My leg kinda fell asleep...
BEFORE:   * 我马上跟来，嘿嘿！腿好像有点睡麻了……
AFTER:   * 我马上跟上，嘿嘿！腿好像有点麻了……
### P09-002 | action=apply
原问题：fell asleep是腿麻；“睡麻”不自然且引入睡觉经历。
本轮理由：已对完整场景复审：fell asleep是腿麻；“睡麻”不自然且引入睡觉经历。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-002"]

## SC753054d754f9793e | nsfw | datadf/all.ds | AreaC_Prison3.CancelPurchase
CONTROL L1367 <AreaC_Prison3.CancelPurchase>
CONTROL L1368   if { hasItem(Key) } {
ROW CAT:O0a79851b14a886b93152 | L1369 | no manual edit
EN: Ohmygod stop being so harsh!
BEFORE:     * 我的天，别这么凶嘛！
AFTER:     * 我的天，别这么凶嘛！
CONTROL L1370   } else {
ROW CAT:Ode05741f78db308da3f2 | L1371 | EDIT E09-003
EN: You're gonna need like, a key, you know...?
BEFORE:     * 你需要那种，钥匙，你懂吧……？
AFTER:     * 你得有把钥匙才行，懂吧……？
CONTROL L1372   }
### P09-003 | action=apply
原问题：like是口语填充，不是“那种”；当前破坏救援提示的表达。
本轮理由：已对完整场景复审：like是口语填充，不是“那种”；当前破坏救援提示的表达。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-003"]

## SCa6c44bc03317898b | nsfw | datadf/all.ds | AreaC_Prison3.NotEnoughMoney
CONTROL L1380 <AreaC_Prison3.NotEnoughMoney>
ROW CAT:Oaa47a377b951f58f1c56 | L1381 | EDIT E09-004
EN: You're gonna need like, a key, you know...?
BEFORE:   * 你需要那种，钥匙，你懂吧……？
AFTER:   * 你得有把钥匙才行，懂吧……？
### P09-004 | action=apply
原问题：like是口语填充，不是“那种”；当前破坏救援提示的表达。
本轮理由：已对完整场景复审：like是口语填充，不是“那种”；当前破坏救援提示的表达。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-004"]

## SCe121946bba2b1c8e | nsfw | datadf/all.ds | AreaH_MacsenBreeding.Hello
CONTROL L1692 <AreaH_MacsenBreeding.Hello>
ROW CAT:Odfb0188d434a99f9320f | L1693 | EDIT E09-005
EN: COME ON IN, FELLOW BREEDER!
BEFORE:   * 进来吧，同行育种者！
AFTER:   * 进来吧，搞育种的同行！
### P09-005 | action=apply
原问题：fellow breeder是招呼同行，不是生硬的职位组合。
本轮理由：已对完整场景复审：fellow breeder是招呼同行，不是生硬的职位组合。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-005"]

## SCb18d51254d264ab3 | sfw | datadf/all.ds | Bossu.TransitionAreaEAirlock1 noselect
CONTROL L2527 <Bossu.TransitionAreaEAirlock1 noselect>
ROW SFWb561c37a8886b739a93388a2 | L2528 | no manual edit
EN: [GOT YOUR COSMOSUIT ON, AGENT?]
BEFORE:   Bossu: [特工，宇宙服穿上了吗？]
AFTER:   Bossu: [特工，宇宙服穿上了吗？]
ROW SFWceb0e77211f0d9770692d4be | L2529 | no manual edit
EN: [HUH? WHAT'S THAT?]
BEFORE:   Yiffany: [咦？什么呀？]
AFTER:   Yiffany: [咦？什么呀？]
ROW SFW25ec98d4f759874d27acf5c6 | L2530 | no manual edit
EN: [YOU'RE IN THINNER AIR NOW.]
BEFORE:   Bossu: [你现在待的地方空气更稀薄了。]
AFTER:   Bossu: [你现在待的地方空气更稀薄了。]
ROW SFW041a290cd3f66966eb7b0d8f | L2531 | EDIT E09-006
EN: [THAT'S RIGHT, THAT GROUND BENEATH YOUR FEET BELONGS]
BEFORE:   Mauser: [没错，你脚下这块地面属于]
AFTER:   Mauser: [没错，你脚下这块地面，其实就在一颗低轨道卫星上。]
ROW SFWa6fa64113891982e15ad242c | L2532 | EDIT E09-007
EN: [TO A LOW ORBITING MOON THAT SEEMS TO HAVE BEEN A PRISON?]
BEFORE:   Mauser: [到了那颗低轨道卫星，看起来那里以前是监狱？]
AFTER:   Mauser: [看起来，这颗卫星以前还是座监狱？]
ROW SFW2b5e8e09c1eafc23caae67ec | L2533 | no manual edit
EN: [A PRISON THAT SPACE PIRATES SEEMED FIT TO BUILD A STATION]
BEFORE:   Bossu: [一座监狱，太空海盗似乎觉得在它周围建个据点挺合适，直到有什么东西把他们赶走了。]
AFTER:   Bossu: [一座监狱，太空海盗似乎觉得在它周围建个据点挺合适，直到有什么东西把他们赶走了。]
ROW SFWd4cf8a2e2f18d448fa8355a6 | L2534 | no manual edit
EN: [AROUND, UNTIL SOMETHING DROVE THEM AWAY.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW146c0b18b2b58fbf43a8c78e | L2535 | no manual edit
EN: [EITHER WAY, YOU'LL NEED TO GET YOUR COSMOSUIT ON.]
BEFORE:   Bossu: [总之，你得把宇宙服穿上。]
AFTER:   Bossu: [总之，你得把宇宙服穿上。]
ROW SFW5208873fa2fa69fd190757e8 | L2536 | EDIT E09-008
EN: [SO MAKE SURE NOBODY'S SNUCK AWAY WITH IT.]
BEFORE:   Bossu: [所以先确认一下没人偷偷把它穿走。]
AFTER:   Bossu: [所以先确认一下，没人偷偷把它拿走。]
ROW SFW1f4c1a239f9085564ff0587a | L2537 | no manual edit
EN: [RIIIIIIIGHT...]
BEFORE:   Yiffany: [明——白——了……]
AFTER:   Yiffany: [明——白——了……]
### P09-006 | action=apply
原问题：“属于／到了那颗”接不成中文句；须整段重排，保留低轨与监狱推测。
本轮理由：按两个现存非空槽重排卫星归属和监狱推测，不新增合句；不跨Bossu接话移动内容。
EDIT_IDS ["E09-006", "E09-007"]
### P09-007 | action=apply
原问题：snuck away with it是偷拿走装备，不限于穿走；两主角独立提案。
本轮理由：已对完整场景复审：snuck away with it是偷拿走装备，不限于穿走；两主角独立提案。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-008"]

## SCb00e0afe598df446 | sfw | datadf/all.ds | BossuDex.ClassicArcher
CONTROL L3092 <BossuDex.ClassicArcher>
ROW SFW3fd827e0e89e9eeb832ac5ac | L3093 | no manual edit
EN: [THE ELVES OF SCEAFYA MAY ALL BE FEMALE]
BEFORE:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
AFTER:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
ROW SFW1544df1f43d4562a78c5db39 | L3094 | no manual edit
EN: [BUT THEY AREN'T ALL IMMORTAL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWe70dd3a9d267e1e2c9920d31 | L3095 | EDIT E09-010
EN: [THEY'VE TAKEN ON MORE AND MORE MORTAL CHARACTERISTICS]
BEFORE:   Bossu: [她们便带上了越来越多的有朽特征]
AFTER:   Bossu: [几百年过去，]
ROW SFW5cea39eb7b8a706521df83f7 | L3096 | EDIT E09-011
EN: [AS THE CENTURIES HAVE GONE BY.]
BEFORE:   Bossu: [在数百年的岁月流逝之中。]
AFTER:   Bossu: [她们身上逐渐多了凡俗生灵的特征。]
ROW SFW572570bb009714c4332d0ac1 | L3097 | no manual edit
EN: [WAIT, SO THAT MEANS SOME OF THEM *ARE* IMMORTAL?]
BEFORE:   Yiffany: [等等，所以这意味着她们中有些*是*不朽的？]
AFTER:   Yiffany: [等等，所以这意味着她们中有些*是*不朽的？]
ROW SFW79ec1ce25523c784aed0c8a7 | L3098 | EDIT E09-012
EN: [INDEED, AS FAR AS WE CAN TELL.]
BEFORE:   Bossu: [的确，就我们所能看出的而言。]
AFTER:   Bossu: [没错，至少据我们目前了解是这样。]
ROW SFW18df94316a203990f187d1af | L3099 | no manual edit
EN: [ANY ELF THAT IS OUT IN THE OPEN AND ENGAGING IN COMBAT]
BEFORE:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
AFTER:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
ROW SFW5d94d5020e0a5a970415cb9d | L3100 | no manual edit
EN: [WILL NO DOUBT BE A YOUNGSTER. A HUNDRED YEARS OLD AT MOST.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWe157a1fadc108bc4088056b8 | L3101 | no manual edit
EN: [THAT'S... WOW...]
BEFORE:   Yiffany: [这……哇……]
AFTER:   Yiffany: [这……哇……]
ROW SFW0baa1d12e27075ea192340c8 | L3102 | EDIT E09-013
EN: [DON'T GIVE IN TO AWE. YOU'LL NEED TO BE ON YOUR TOES]
BEFORE:   Bossu: [别向敬畏屈服。你得保持警觉，以便击退那些年幼精灵的攻击。]
AFTER:   Bossu: [别光顾着惊叹。要时刻保持警觉，才能击退那些年轻精灵的攻击。]
ROW SFWaa96fab984366df6c3275620 | L3103 | no manual edit
EN: [IN ORDER TO REPEL THE YOUNG ELVES' ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW16504d6a5069ed2133341c80 | L3104 | no manual edit
EN: [RIGHT, GOTTA FOCUS.]
BEFORE:   Yiffany: [对，得专注。]
AFTER:   Yiffany: [对，得专注。]
### P09-009 | action=apply
原问题：“有朽特征／就我们所能看出的而言／别向敬畏屈服”逐词痕迹重；专业说明和提醒应连贯自然。三个独立发言节点只分别重写，不实际合并跨人台词。
本轮理由：时间状语前置占原槽，后槽承接凡俗特征；保留总部认知边界和防御提醒。
EDIT_IDS ["E09-010", "E09-011", "E09-012", "E09-013"]

## SC46b40e6ec47e8a6d | nsfw | datadf/all.ds | BossuDex.ClassicCannonFloorC
CONTROL L3179 <BossuDex.ClassicCannonFloorC>
ROW CAT:Od2b2e28d1b268cd6156e | L3180 | EDIT E09-014
EN: [BOSSU, ARE THERE CANNONS STRONGER OR AM I WEAKER?]
BEFORE:   Yiffany: [波苏，是有更强的加农炮，还是我变弱了？]
AFTER:   Yiffany: [波苏，是这些加农炮变强了，还是我变弱了？]
ROW CAT:Of82b8d48b614f220cba2 | L3181 | no manual edit
EN: [THESE CANNONS SEEM TO HAVE GONE A WHILE WITHOUT]
BEFORE:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
AFTER:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
ROW CAT:O83123c0294409c7aa5d6 | L3182 | no manual edit
EN: [NEEDING TO BE SELF- REPAIRED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4a8b2042db90c805276d | L3183 | no manual edit
EN: [CONSEQUENTLY THEY SEEM TO BE FIRING AT HIGHER POWER.]
BEFORE:   Bossu: [因此它们似乎正以更高的功率发射。]
AFTER:   Bossu: [因此它们似乎正以更高的功率发射。]
ROW CAT:O631c768a080853eab01a | L3184 | EDIT E09-015
EN: [GREEAAAAAT, JUST WHAT I NEEDED TO DEAL WITH...]
BEFORE:   Yiffany: [太——好了，正好是我需要应付的……]
AFTER:   Yiffany: [太——好了，偏偏又摊上这种麻烦……]
### P09-010 | action=apply
原问题：原文there疑为these笔误，后文明确谈眼前炮台；“是有更强的”问非所指。末句是反讽，不是正好需要应付。
本轮理由：已对完整场景复审：原文there疑为these笔误，后文明确谈眼前炮台；“是有更强的”问非所指。末句是反讽，不是正好需要应付。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-014", "E09-015"]

## SCfae065df9d829e6c | sfw | datadf/all.ds | BossuDex.ClassicSpikebot
CONTROL L2955 <BossuDex.ClassicSpikebot>
ROW SFW01c279ac5b41aa55ec6a42b2 | L2956 | EDIT E09-018
EN: [THE LITTLE WHEELED DRONES WERE ONCE USED TO FERRY]
BEFORE:   Bossu: [那些小小的轮式无人机曾经用来运送矿井里的矿石和工具，但这些单元已经被加上简陋尖刺和搜寻入侵者的逻辑，经过了改装。]
AFTER:   Bossu: [这些小型轮式无人机原本用来在矿井里运送矿石和工具。不过，这些机器已经过改装，装上了粗陋的尖刺，还加入了搜寻入侵者的程序。]
ROW SFW83cf8115acbba69c7989f3ce | L2957 | no manual edit
EN: [ORE AND TOOLS IN THE MINES, BUT THESE UNITS HAVE BEEN]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW6bfe7a28eefb56ce5eac7d14 | L2958 | no manual edit
EN: [MODDED WITH CRUDE SPIKES AND INTRUDER- SEEKING LOGIC.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW8c8bf9a9fe3397af44018f48 | L2959 | EDIT E09-019
EN: [SO SOMEONE *REALLY* DOESN'T LIKE PEOPLE SNIFFING AROUND]
BEFORE:   Yiffany: [所以有人*真的*不喜欢别人嗅探]
AFTER:   Yiffany: [看来，有人*真的*不想让外人]
ROW SFW7cee9fcb43ff129b000791df | L2960 | EDIT E09-020
EN: [THE MINES HERE.]
BEFORE:   Yiffany: [这里的矿井。]
AFTER:   Yiffany: [到这里的矿井探个究竟。]
### P09-012 | action=apply
原问题：整段把改装堆叠语和“嗅探／这里的矿井”断裂改成正常技术说明→人物判断；不把入侵者逻辑误成生物本能。
本轮理由：完整保留运输用途、尖刺和搜寻程序；主角两槽按中文动宾意群衔接，强调标记保留。
EDIT_IDS ["E09-018", "E09-019", "E09-020"]

## SC3d40dc4f2e053d40 | nsfw | datadf/all.ds | Mauser.AreaE_map23 noselect
CONTROL L2551 <Mauser.AreaE_map23 noselect>
ROW CAT:O15dbb1b5257f5650405e | L2552 | no manual edit
EN: [AGENT, COME IN. REQUESTING STATUS REPORT.]
BEFORE:   Mauser: [特工，请回话。请求状态报告。]
AFTER:   Mauser: [特工，请回话。请求状态报告。]
ROW CAT:O3cc9863d7cbd0f6d018e | L2553 | no manual edit
EN: [HEY THERE SQUEAKS. CURRENTLY STARING AT SOME SCREENS.]
BEFORE:   Yiffany: [嘿，小吱吱。我正盯着几块屏幕看。]
AFTER:   Yiffany: [嘿，小吱吱。我正盯着几块屏幕看。]
ROW CAT:Ob203cd230f9c1ded6a77 | L2554 | no manual edit
EN: [ALMOST LIKE WE'RE DOING THE SAME JOB RIGHT NOW!]
BEFORE:   Yiffany: [简直就像我们此刻在干同一份工作！]
AFTER:   Yiffany: [简直就像我们此刻在干同一份工作！]
ROW CAT:O93fa12dc32fc9eb16c0d | L2555 | no manual edit
EN: [W-WHAT? WHAT DO YOU M-MEAN...?]
BEFORE:   Mauser: [什、什么？你这话意、意思是什么……？]
AFTER:   Mauser: [什、什么？你这话意、意思是什么……？]
ROW CAT:O3b7c91ebfb368b03934d | L2556 | no manual edit
EN: [LOOKS LIKE I'M INSIDE OF SOME SORT OF VAULT]
BEFORE:   Yiffany: [看起来我在某个金库里面，但根本没有锁，只有一些画着奇怪符号的屏幕……]
AFTER:   Yiffany: [看起来我在某个金库里面，但根本没有锁，只有一些画着奇怪符号的屏幕……]
ROW CAT:O593131b35c0600e204d9 | L2557 | no manual edit
EN: [BUT INSTEAD OF A LOCK ALL I HAVE ARE SOME SCREENS WITH]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O0c48646c7e8aad4f9456 | L2558 | no manual edit
EN: [WEIRD SYMBOLS ON THEM...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9d5e018b8a823464e0f3 | L2559 | no manual edit
EN: [WHAT SORT OF VIBES ARE THEY GIVIN' YA?]
BEFORE:   Tomcat: [它们给你什么样的感觉？]
AFTER:   Tomcat: [它们给你什么样的感觉？]
ROW CAT:Odadb5aa2cc23c4df71ad | L2560 | no manual edit
EN: [WELL, THEY LOOK PRETTY SIMILAR TO SOME OF THE SYMBOLS]
BEFORE:   Yiffany: [嗯，它们看着跟这一带矮矮小小的Fenfen们用的某些符号很像。]
AFTER:   Yiffany: [嗯，它们看着跟这一带矮矮小小的Fenfen们用的某些符号很像。]
ROW CAT:Occb5e68b2959cf4e84e8 | L2561 | no manual edit
EN: [USED BY THE SHORT LITTLE FENFEN FOLKS AROUND HERE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofe6a4def12c21550f8fa | L2562 | no manual edit
EN: [HMM, WELL IF YOU EVER RUN INTO THESE FENFEN IN THE FLESH]
BEFORE:   Mauser: [嗯，如果你哪天亲眼碰到这些Fenfen，也许你该留意他们对你说的话？]
AFTER:   Mauser: [嗯，如果你哪天亲眼碰到这些Fenfen，也许你该留意他们对你说的话？]
ROW CAT:O5b684bc2d8d6177021cf | L2563 | no manual edit
EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O739018bfc7ca42e0dd84 | L2564 | EDIT E09-021
EN: [YEAH, LIKE CHEESE BREATH SAID.]
BEFORE:   Tomcat: [对，就像CHEESE BREATH说的那样。]
AFTER:   Tomcat: [对，那个满嘴奶酪味的家伙说得没错。]
ROW CAT:Oaea01a20d1764718bae7 | L2565 | no manual edit
EN: [MIGHT BE WORTH GOING OVER WHAT THE LOCAL FENFEN SAY.]
BEFORE:   Tomcat: [或许值得把这一带Fenfen说过的话再过一遍。]
AFTER:   Tomcat: [或许值得把这一带Fenfen说过的话再过一遍。]
ROW CAT:O4194cc70662fde0efc5a | L2566 | no manual edit
EN: [YOU GUYS ARE RIGHT. THEY COULD BE THE KEY TO THIS ALL!]
BEFORE:   Yiffany: [你们说得对。它们说不定就是这一切的关键！]
AFTER:   Yiffany: [你们说得对。它们说不定就是这一切的关键！]
ROW CAT:Of83f563a107933c59f00 | L2567 | no manual edit
EN: [I'LL KEEP ON TRYING TO CRACK THIS CODE. YIFFANY OUT.]
BEFORE:   Yiffany: [我会继续设法破解这套密码。伊法妮通话完毕。]
AFTER:   Yiffany: [我会继续设法破解这套密码。伊法妮通话完毕。]
### P09-013 | action=apply
原问题：CHEESE BREATH是Tomcat损Mauser的外号，不是需要英文保留的新人物；保留插科打诨后回到解谜提示。
本轮理由：已对完整场景复审：CHEESE BREATH是Tomcat损Mauser的外号，不是需要英文保留的新人物；保留插科打诨后回到解谜提示。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-021"]

## SC24fd938ea56dbe72 | nsfw | datadf/all.ds | MauserHints_AreaA.DragonHint noselect
CONTROL L3461 <MauserHints_AreaA.DragonHint noselect>
ROW CAT:O7f7cb9d899c5e25ff614 | L3462 | EDIT E09-022
EN: [IT'S DIFFICULT TO GET CLEAN SCANS THAT DEEP IN THE PLANET]
BEFORE:   Mauser: [在星球那么深的地方，很难得到干净的扫描，不过我探测到矿井更深处好几处安全门的信号特征。你的新门卡应该能让你通行。]
AFTER:   Mauser: [地底那么深，很难扫描清楚。不过，我在矿井更深处探测到了几道安全门的信号。你的新门卡应该能让你通过。]
ROW CAT:O7eeaf5eef10369a62c6d | L3463 | no manual edit
EN: [BUT I'M DETECTING SEVERAL SIGNATURES FOR SECURITY DOORS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa46f294bf5c16f9f5845 | L3464 | no manual edit
EN: [IN THE DEEPER PARTS OF THE MINES. YOUR NEW KEYCARD SHOULD]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2d40705fe66aff2b7a53 | L3465 | no manual edit
EN: [GRANT YOU ACCESS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O95a12269f35b10e126ff | L3466 | no manual edit
EN: [OKAY. I'LL CHECK THOSE OUT.]
BEFORE:   Yiffany: [好。我去查看一下。]
AFTER:   Yiffany: [好。我去查看一下。]
CONTROL L3468 # salamanders dialogue - used in multiple scripts
### P09-014 | action=apply
原问题：clean scans不是“干净的扫描”；整段明确探测限制→发现门→门卡用途。
本轮理由：已对完整场景复审：clean scans不是“干净的扫描”；整段明确探测限制→发现门→门卡用途。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-022"]

## SC2d557c5f86ef9923 | nsfw | datadf/all.ds | MauserHints_AreaC.EnelyeHint noselect
CONTROL L3577 <MauserHints_AreaC.EnelyeHint noselect>
ROW CAT:Oa25783c6c24481283640 | L3578 | EDIT E09-023
EN: [THERE'S A LOT OF HIGH LEVEL DOORS AROUND THERE]
BEFORE:   Mauser: [那附近高级门很多，那肯定说明哪儿有一张高级门卡！]
AFTER:   Mauser: [那附近有不少高等级门，肯定也有张高等级门卡藏在某处！]
ROW CAT:O04cab93fd9753c78b983 | L3579 | no manual edit
EN: [WHICH MUST MEAN THERE'S A HIGH LEVEL KEYCARD SOMEWHERE!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O526c59a28f5a2c36e766 | L3580 | EDIT E09-024
EN: [YOUR BEST BET IS TO FIND THAT AND SEE WHERE IT'LL TAKE YA]
BEFORE:   Mauser: [最靠谱就是找到它，看它能带你去哪儿]
AFTER:   Mauser: [最好的办法就是先找到它，看看能通往哪些地方。]
### P09-015 | action=apply
原问题：“高级门／带你去哪”生硬且等级信息不直观；保留must和best bet的提示语气。
本轮理由：已对完整场景复审：“高级门／带你去哪”生硬且等级信息不直观；保留must和best bet的提示语气。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-023", "E09-024"]

## SC692b79fe52f83d3f | nsfw | datadf/all.ds | Tomcat.Feral noselect noamendfreq
CONTROL L3730 <Tomcat.Feral noselect noamendfreq>
ROW CAT:Odfd01b6f728c0e673c6a | L3731 | EDIT E09-025
EN: [OH WHAT? IS THIS SOME KINDA JOKE?]
BEFORE:   Tomcat: [哦什么？这是某种玩笑吗？]
AFTER:   Tomcat: [什么情况？这是在开玩笑吗？]
ROW CAT:Od3844a3781d6030559f6 | L3732 | no manual edit
EN: [BARK!]
BEFORE:   Yiffany: [汪！]
AFTER:   Yiffany: [汪！]
ROW CAT:O96b2052bb173b5ce126a | L3733 | EDIT E09-026
EN: [YEAH HAR HAR, COME ON GIRL I KNOW YOU'RE THERE]
BEFORE:   Tomcat: [是啊哈哈，拜托，姑娘，我知道你在那儿，对着这通恶作剧电话笑得尾巴都要掉了。]
AFTER:   Tomcat: [行了行了，真好笑。姑娘，我知道你就在那儿，为这通恶作剧电话笑得尾巴都要掉了。]
ROW CAT:Od336afc3b880c5e19a8b | L3734 | no manual edit
EN: [LAUGHING YOUR TAIL OFF TO THIS PRANK CALL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O1e1a6d7726f0ba5cf755 | L3735 | no manual edit
EN: [BARK BARK!]
BEFORE:   Yiffany: [汪汪！]
AFTER:   Yiffany: [汪汪！]
ROW CAT:Ob5a79c984b101edee329 | L3736 | EDIT E09-027
EN: [SOME OF US HAVE WORK TO DO YOU KNOW! HEY, PUP.]
BEFORE:   Tomcat: [有些人可是有工作要做的！嘿，小狗。]
AFTER:   Tomcat: [我这儿可还得工作呢！喂，小狗。]
ROW CAT:O4e73429a4a1184f377f2 | L3737 | EDIT E09-028
EN: [TELL YOUR OWNER THAT SHE NEEDS A NEW SENSE OF HUMOR!]
BEFORE:   Tomcat: [告诉你主人，她该换点幽默感了！]
AFTER:   Tomcat: [告诉你主人，她这笑话可一点都不好笑！]
ROW CAT:Oc68183206b9914926037 | L3738 | no manual edit
EN: [...]
BEFORE:   Yiffany: [……]
AFTER:   Yiffany: [……]
### P09-016 | action=apply
原问题：“哦什么／是啊哈哈／换点幽默感”不自然；Tomcat误认狗与主人分离须保留，不把主角真的拆成两人。
本轮理由：已对完整场景复审：“哦什么／是啊哈哈／换点幽默感”不自然；Tomcat误认狗与主人分离须保留，不把主角真的拆成两人。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-025", "E09-026", "E09-027", "E09-028"]

## SC6b2494bddfad8bc0 | sfw | datadf/all.ds | TomcatItems.JudoBody
CONTROL L4013 <TomcatItems.JudoBody>
ROW SFWfc486a55b7acdc46d3abd289 | L4014 | no manual edit
EN: [NOW THIS BRINGS BACK MEMORIES.]
BEFORE:   Yiffany: [这可勾起回忆了。]
AFTER:   Yiffany: [这可勾起回忆了。]
ROW SFW437bc3e2c37191d6fe921b73 | L4015 | no manual edit
EN: [LOOKATHAT. AN OLD JUDO GI!]
BEFORE:   Tomcat: [瞧这个。一件旧柔道服！]
AFTER:   Tomcat: [瞧这个。一件旧柔道服！]
ROW SFWdf400fa38aea4c62e2569a5f | L4016 | EDIT E09-029
EN: [IT ALWAYS MADE ME FEEL LIKE A FIGHTER WHEN I WORE MINE]
BEFORE:   Yiffany: [我穿上自己的那套时，总觉得自己像个格斗家。]
AFTER:   Yiffany: [以前我穿着自己那套柔道服，随随便便在学院里走动，]
ROW SFWde3589430efca2e3af910b1e | L4017 | EDIT E09-030
EN: [JUST CASUALLY AROUND THE ACADEMY.]
BEFORE:   Yiffany: [总觉得自己很猛。]
AFTER:   Yiffany: [都觉得自己像个格斗家。]
ROW SFWed0fd4451ab500cd73ea1d20 | L4018 | no manual edit
EN: [MAYBE THAT'S WHY YOU KEPT GET'N INTO FIGHTS ALL THE TIME]
BEFORE:   Tomcat: [也许这就是你老是打起来的原因]
AFTER:   Tomcat: [也许这就是你老是打起来的原因]
ROW SFW7d4762fed2552ea3c213cf23 | L4019 | no manual edit
EN: [JUST DON'T FORGET THAT YOU HAVE A LIGHTTAZER ON YOU]
BEFORE:   Tomcat: [别忘了你身上有光电击枪]
AFTER:   Tomcat: [别忘了你身上有光电击枪]
ROW SFW98703616027388acbcc60871 | L4020 | no manual edit
EN: [NO REASON TO DRESS UP AND GO BAREHANDED DOWN THERE.]
BEFORE:   Tomcat: [没必要穿成这样赤手下场。]
AFTER:   Tomcat: [没必要穿成这样赤手下场。]
ROW SFWd5380624e710295ac2702306 | L4021 | no manual edit
EN: [EVEN IF IT MAKES YOU FEEL LIKE A FIGHTER AGAIN!]
BEFORE:   Tomcat: [就算它又让你觉得自己是个格斗家也一样！]
AFTER:   Tomcat: [就算它又让你觉得自己是个格斗家也一样！]
CONTROL L4024 ### Tribal ###
### P09-017 | action=apply
原问题：JUST CASUALLY AROUND THE ACADEMY丢失，当前第二行重复“猛”；恢复日常穿柔道服的自信笑点。
本轮理由：恢复在学院随意日常穿着柔道服的限定，不添“爱逛”等习惯；格斗家感受放后一有效槽。
EDIT_IDS ["E09-029", "E09-030"]

## SCfb0717823b73e65d | nsfw | datadf/all.ds | TomcatItems.PsyJuice
CONTROL L3845 <TomcatItems.PsyJuice>
ROW CAT:Obb4be53958eee5bc8525 | L3846 | no manual edit
EN: [AWWW LOOK AT THIS ADORABLE LITTLE JUICE BOX!]
BEFORE:   Yiffany: [哎呀，看这可爱的小果汁盒！]
AFTER:   Yiffany: [哎呀，看这可爱的小果汁盒！]
ROW CAT:O1df44c7ff268d1fc6754 | L3847 | no manual edit
EN: [I HAVEN'T HAD THESE SINCE I WAS A PUPPY!]
BEFORE:   Yiffany: [我从幼犬时期就没喝过这些了！]
AFTER:   Yiffany: [我从幼犬时期就没喝过这些了！]
ROW CAT:O35d63f1fefa75b514478 | L3848 | no manual edit
EN: [DID YOU EVER ACTUALLY DRINK ONE OF THOSE?]
BEFORE:   Tomcat: [你真的喝过这种吗？]
AFTER:   Tomcat: [你真的喝过这种吗？]
ROW CAT:O023ecd2d3dfe023d7463 | L3849 | EDIT E09-031
EN: [REMEMBER, YOU USED TO ALWAYS TRADE THEM OFF FOR MEAT.]
BEFORE:   Tomcat: [记得吧，你以前总拿它们跟我换肉。]
AFTER:   Tomcat: [记得吧，你以前总拿它们去换肉。]
ROW CAT:O958bbe94b3ab08a7acf4 | L3850 | EDIT E09-032
EN: [UNTIL YOU GOT OLDER AND LEARNED THAT IT WAS EASIER TO TRAD-]
BEFORE:   Tomcat: [直到你长大，才学会了更容易去换-]
AFTER:   Tomcat: [后来长大了，才发现还有更省事的换——]
ROW CAT:O0fc6fbb04d9a0018a9ba | L3851 | EDIT E09-033
EN: [-TRADE MONEY FOR MORE MEAT AT THE STORE, YUP!]
BEFORE:   Yiffany: [-用钱在店里换更多肉，对！]
AFTER:   Yiffany: [——用钱去店里换更多肉，没错！]
ROW CAT:O2d17ea3c07d6cd0b16f8 | L3852 | no manual edit
EN: [O RLY]
BEFORE:   Tomcat: [哦是吗]
AFTER:   Tomcat: [哦是吗]
ROW CAT:Oac11bd8274966a8e4b38 | L3853 | no manual edit
EN: [TOTALLY! JUST A SHAME I WAS TOO BUSY FUCKING CLASSMATES]
BEFORE:   Yiffany: [当然！只可惜我忙着操同学，没怎么去成店里，哈哈！]
AFTER:   Yiffany: [当然！只可惜我忙着操同学，没怎么去成店里，哈哈！]
ROW CAT:O3f7fc58f0766dd5ec5f9 | L3854 | no manual edit
EN: [TO GET DOWN TO THE STORE MUCH HAHA!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O33087fdd7f4d5cc2becc | L3855 | no manual edit
EN: [H-HAHA... YOU'RE TALKING ABOUT COLLEGE NOW, RIGHT?]
BEFORE:   Tomcat: [哈、哈哈……你现在说的是大学吧？]
AFTER:   Tomcat: [哈、哈哈……你现在说的是大学吧？]
ROW CAT:O2f947b57f5eb9b0bf5b1 | L3856 | no manual edit
EN: [SORRY CAN'T HEAR YOU. TOO BUSY JUICING!!!]
BEFORE:   Yiffany: [抱歉听不见。忙着榨汁呢！！！]
AFTER:   Yiffany: [抱歉听不见。忙着榨汁呢！！！]
ROW CAT:O79d6fcc07e8683d0659d | L3857 | no manual edit
EN: [SLRRRP]
BEFORE:   Yiffany: [吸溜]
AFTER:   Yiffany: [吸溜]
### P09-018 | action=apply
原问题：原文没有“跟我”这个交易对象；保留Tomcat未说完、姐姐抢话掩饰的接梗结构，不擅补被截断的真正内容。
本轮理由：删除无源交易对象，保留长大后的发现及被抢话截断，不猜被打断的真实交易。
EDIT_IDS ["E09-031", "E09-032", "E09-033"]

## SC48a4bc82fca232b0 | sfw | datadf/all.ds | TomcatItems.SpecialTorch
CONTROL L4293 <TomcatItems.SpecialTorch>
ROW SFW715e57e1c3189b9725232d26 | L4294 | EDIT E09-034
EN: [THAT FLASHLIGHT - OR TORCH, AS BOSSU CALLS IT - WILL]
BEFORE:   Tomcat: [那把手电筒——Bossu管它叫火把——会]
AFTER:   Tomcat: [那把手电筒——Bossu习惯叫它torch——]
ROW SFWbd6fad37e2507f17bf27ffc2 | L4295 | EDIT E09-035
EN: [ILLUMINATE LOW-LIGHT AREAS AUTOMATICALLY.]
BEFORE:   Tomcat: [自动照亮昏暗的地方。]
AFTER:   Tomcat: [会自动照亮昏暗的地方。]
ROW SFWbb5bd90f1aa4b0e06465963f | L4296 | no manual edit
EN: [I DON'T HAVE TO DO ANYTHING SPECIAL TO USE IT, RIGHT?]
BEFORE:   Yiffany: [用它不需要特别操作，对吧？]
AFTER:   Yiffany: [用它不需要特别操作，对吧？]
ROW SFW7c81fa846ac166fb3aa50aba | L4297 | no manual edit
EN: [THAAT'S RIGHT, JUST LEAVE IT ON AND LET IT WORK ITS MAGIC!]
BEFORE:   Tomcat: [没——错，开着就行，它自己会发挥作用！]
AFTER:   Tomcat: [没——错，开着就行，它自己会发挥作用！]
### P09-019 | action=apply
原问题：torch与flashlight是同一物；译为火把制造错误道具差异。中文按笑话功能重写，正式落地需再按显示节点分配。
本轮理由：保留Bossu异名用语的笑话，以torch原词呈现其称法，明确同一把手电；不改墙上火把。
EDIT_IDS ["E09-034", "E09-035"]

## SC8b9b4e57a1559d32 | nsfw | datadm/all.ds | AreaA_Macsen2.TazerPirate
CONTROL L469 <AreaA_Macsen2.TazerPirate>
ROW CAT:Of0a4f457e434e2a0d923 | L470 | EDIT E09-036
EN: Wanna become a space pirate? All you need is this Official Pirate Lighttazer!
BEFORE:   * 想当太空海盗吗？你需要的只是这支官方海盗光速枪！
AFTER:   * 想当太空海盗吗？你只需要这把官方海盗光电击器！
ROW CAT:O76a71b9ba7a62cfd6a03 | L471 | no manual edit
EN: Plus a ship and a crew of outlaws, of course!
BEFORE:   * 当然，还得有一艘飞船和一群亡命之徒！
AFTER:   * 当然，还得有一艘飞船和一群亡命之徒！
ROW CAT:O2686fe3d085bb1197147 | L472 | no manual edit
EN: ...just don't forget to equip it, it's not just for show, ya know.
BEFORE:   * ……只是别忘了把它装备上，它可不是摆设，懂吧？
AFTER:   * ……只是别忘了把它装备上，它可不是摆设，懂吧？
### P09-020 | action=apply
原问题：lighttazer不表示光速枪；保留“官方海盗”商贩推销反差，与装备分析对照。
本轮理由：Lighttazer不含速度含义，改为光电击器；其余飞船、亡命徒船员和装备提醒已正确，保持原节点。
EDIT_IDS ["E09-036"]

## SC0961d1327c965343 | nsfw | datadm/all.ds | AreaC_MacsenDark.Hello
CONTROL L1194 <AreaC_MacsenDark.Hello>
ROW CAT:Oe99a7ec1e425b7bdc803 | L1195 | EDIT E09-037
EN: Is that a flashlight in your hands, or are you just happy to see me?
BEFORE:   * 你手里那是手电筒，还是只是见到我就高兴？
AFTER:   * 你手里那是手电筒，还是见了我太兴奋了？
ROW CAT:O02666543ba437240d45d | L1196 | EDIT E09-038
EN: I kid! I kid! You and that torch are lifesavers.
BEFORE:   * 开玩笑！开玩笑！你和那支火把可是救星。
AFTER:   * 逗你的，逗你的！你和那把手电筒可真是救星。
### P09-021 | action=apply
原问题：同一段flashlight/torch不可译成两个物品；首句保留俏皮双关，不为直白另加身体器官。
本轮理由：已对完整场景复审：同一段flashlight/torch不可译成两个物品；首句保留俏皮双关，不为直白另加身体器官。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-037", "E09-038"]

## SCb4b182f56b8fa17b | sfw | datadm/all.ds | AreaC_Prison1.Hello
CONTROL L1268 <AreaC_Prison1.Hello>
ROW SFW322bb33cdeeb3117bc7f21ac | L1269 | EDIT E09-039
EN: H-howdy friend! I'd give ya a warm welcome, but I'm awful cooped up!
BEFORE:   * 你、你好啊，朋友！我倒想热情欢迎你，可这里实在太挤了！
AFTER:   * 你、你好啊，朋友！我倒想热情招呼你，可我被关在这儿，实在施展不开！
### P09-022 | action=apply
原问题：cooped up是被关/困着，不是单纯空间太挤。
本轮理由：已对完整场景复审：cooped up是被关/困着，不是单纯空间太挤。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-039"]

## SCb593a77c58d4a298 | sfw | datadm/all.ds | AreaC_Prison3.TalkBeforeRescue.bopped
CONTROL L1387 <AreaC_Prison3.TalkBeforeRescue.bopped>
ROW SFWf83a7423fd2cba06696746f3 | L1388 | no manual edit
EN: Really... I'm a pretty cool cat. No rush on the rescue.
BEFORE:   * 真的……我可是只淡定的猫。救援不着急。
AFTER:   * 真的……我可是只淡定的猫。救援不着急。
ROW SFWb88496ee5d78c21efb073222 | L1389 | EDIT E09-040
EN: I was the senior top agent deployed to this planet.
BEFORE:   * 我可是派驻这颗星球的资深上位特工。
AFTER:   * 我可是派驻这颗星球的资深精英特工。
ROW SFW8378d044b1178c63eceecb36 | L1390 | no manual edit
EN: If you bust me out of here, I'll show you a few tricks, haha!
BEFORE:   * 你要是把我弄出去，我就教你几招，哈哈！
AFTER:   * 你要是把我弄出去，我就教你几招，哈哈！
### P09-023 | action=apply
原问题：SFW上下文是自夸资历能力，“资深上位特工”平白造职位/性角色；不把NSFW或Top自称全局套入。
本轮理由：只修senior top的资深精英自夸，不造“上位”职位或从成人版本强带性角色；猫自称及教招保留。
EDIT_IDS ["E09-040"]

## SCd557a750eabd9d1c | sfw | datadm/all.ds | Bossu.Area0_map10_a noselect noamendfreq
CONTROL L1995 <Bossu.Area0_map10_a noselect noamendfreq>
ROW SFW1115f95c458e67de2fa6733d | L1996 | no manual edit
EN: [GOOD JOB SHOWING THAT BRUTE WHAT FOR, YIFFAI!]
BEFORE:   Bossu: [干得好，伊法伊，给了那蛮横的大块头一点颜色看看！]
AFTER:   Bossu: [干得好，伊法伊，给了那蛮横的大块头一点颜色看看！]
ROW SFWad767ee79e372fce2feac664 | L1997 | no manual edit
EN: [THANKS BOSSU, I JUST WISH HE DIDN'T RUN AWAY]
BEFORE:   Yiffai: [谢谢，波苏，可惜他逃走了。]
AFTER:   Yiffai: [谢谢，波苏，可惜他逃走了。]
ROW SFW685b828feaef238e438d4f17 | L1998 | no manual edit
EN: [THAT'S GONNA MAKE IT EXTRA HARD TO CALM HIM DOWN...]
BEFORE:   Yiffai: [这样一来，要让他冷静下来就更难了……]
AFTER:   Yiffai: [这样一来，要让他冷静下来就更难了……]
ROW SFW4f384e740bda39535f87f4d5 | L1999 | no manual edit
EN: [DO YOUR BEST UNTIL YOU MANAGE TO GET PROPER EQUIPMENT]
BEFORE:   Bossu: [在设法找到合适装备之前，先尽你所能，]
AFTER:   Bossu: [在设法找到合适装备之前，先尽你所能，]
ROW SFW1c0022bb6f46bb40e69c25ea | L2000 | no manual edit
EN: [SO THAT WE CAN HELP OUT THESE CREATURES ON TUTONE.]
BEFORE:   Bossu: [这样我们才能帮助图托恩的这些生物。]
AFTER:   Bossu: [这样我们才能帮助图托恩的这些生物。]
ROW SFW118166975e67629e2656f5c6 | L2001 | no manual edit
EN: [OF COURSE, I'LL SEE IF I CAN TRACK HIM DOWN AGAIN.]
BEFORE:   Yiffai: [当然，我会再试着找到他的下落。]
AFTER:   Yiffai: [当然，我会再试着找到他的下落。]
ROW SFW179934b1d5a42a73a1099914 | L2002 | EDIT E09-041
EN: [GOOD BOY, LOOKING FORWARD TO SEEING THAT DATA!]
BEFORE:   Bossu: [好男孩，期待看到那份数据！]
AFTER:   Bossu: [乖，等着看你的数据！]
ROW SFW559c366e4db9cc65c118b75f | L2003 | no manual edit
EN: [IF YOU COME ACROSS ANY NEW CREATURES, FEEL FREE TO]
BEFORE:   Bossu: [如果你碰上任何新生物，尽管用频率27.850呼叫我。]
AFTER:   Bossu: [如果你碰上任何新生物，尽管用频率27.850呼叫我。]
ROW SFW034da368f7aa47147d8a7ae6 | L2004 | no manual edit
EN: [GIVE ME A CALL AT FREQUENCY 27.850.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW0d8e361625d6da8b707169ac | L2005 | no manual edit
EN: [OH AND DON'T FORGET TO EQUIP YOUR NEW GEAR. OVER!]
BEFORE:   Bossu: [哦，还有，别忘了把新装备装上。完毕！]
AFTER:   Bossu: [哦，还有，别忘了把新装备装上。完毕！]
ROW SFW815bf41357d8a0501b11f43b | L2006 | EDIT E09-042
EN: [GEEZE I KNOW THAT, I AIN'T NO PUP...]
BEFORE:   Yiffai: [哎呀我知道，我才不是Pup...]
AFTER:   Yiffai: [哎呀，知道啦，我又不是小狗崽……]
### P09-024 | action=apply
原问题：Good boy和pup形成被当幼犬→嘴硬的笑点；“好男孩／Pup”残留使口语和回嘴落点失效。
本轮理由：保留上级good boy式表扬与主角否认小狗崽的回嘴，不将其变成未成年身份；装备指示不必改。
EDIT_IDS ["E09-041", "E09-042"]

## SCb19035363d3c7b1f | nsfw | datadm/all.ds | Bossu.AreaBTransportal2_a noselect
CONTROL L2374 <Bossu.AreaBTransportal2_a noselect>
ROW CAT:O2c1f7a2ac774cf18d4ff | L2375 | no manual edit
EN: [COMMAND, THIS IS AGENT YIFFAI. I'VE ENCOUNTERED ANOTHER]
BEFORE:   Yiffai: [指挥部，这里是特工伊法伊。我又遇到了另一座传送门。我获准出击了吗？]
AFTER:   Yiffai: [指挥部，这里是特工伊法伊。我又遇到了另一座传送门。我获准出击了吗？]
ROW CAT:O84cb4334b4819ba73248 | L2376 | no manual edit
EN: [TELEPORTAL. DO I HAVE PERMISSION TO SORTIE?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ocdc4f14f4a684ee7d818 | L2377 | EDIT E09-043
EN: [NEGATIVE, AGENT. NAP-OF-THE-EARTH RE- STRICTIONS PERSIST]
BEFORE:   Bossu: [否定，特工。贴地飞行的限——制仍在持续，不过，你的飞船已安然无恙地驶到你身边。]
AFTER:   Bossu: [不批准，特工。贴地飞行限制仍然有效。不过，你的飞船已经顺利抵达你的位置，没有受到袭扰。]
ROW CAT:Obf14fb92146b87ed170e | L2378 | no manual edit
EN: [HOWEVER, YOUR SHIP HAS NAVIGATED TO YOU UNMOLESTED]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O428120c7f4dfaada5ad7 | L2379 | no manual edit
EN: [NOT ONLY THAT, BUT NOW THAT YOU'VE VISUALLY CONFIRMED]
BEFORE:   Bossu: [不止如此，既然你已经亲眼确认了这座传送门的地面坐标，应该就能随心所欲地回到那里了。]
AFTER:   Bossu: [不止如此，既然你已经亲眼确认了这座传送门的地面坐标，应该就能随心所欲地回到那里了。]
ROW CAT:Od404e7f50d59aaa5248d | L2380 | no manual edit
EN: [THIS TELEPORTAL'S GROUND COORDINATES YOU SHOULD BE]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O047f34428d2c9e713fc3 | L2381 | no manual edit
EN: [ABLE TO RETURN TO IT AS YOU DESIRE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oe08775f8cd909035b689 | L2382 | no manual edit
EN: [IS VISUAL CONFIRMATION REALLY NECESSARY, SIR?]
BEFORE:   Yiffai: [真的有必要亲眼确认吗，长官？]
AFTER:   Yiffai: [真的有必要亲眼确认吗，长官？]
ROW CAT:O389bdab58f66cc01eb7f | L2383 | no manual edit
EN: [CAN'T I JUST USE THE TELEPORTAL COORDINATES FROM]
BEFORE:   Yiffai: [我就不能直接沿用之前那些特工的传送门坐标吗？]
AFTER:   Yiffai: [我就不能直接沿用之前那些特工的传送门坐标吗？]
ROW CAT:Od62c698a65fa77c2414f | L2384 | no manual edit
EN: [THE PREVIOUS AGENTS?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oe50425a960f590eded1e | L2385 | no manual edit
EN: [SORRY, WE CAN'T RI- SK YOU PORTING INTO A SOLID SURFACE]
BEFORE:   Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的唯一希望。]
AFTER:   Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的唯一希望。]
ROW CAT:O0a21f0ba60c3b9dd8401 | L2386 | no manual edit
EN: [ESPECIALLY AS YOU ARE OUR ONLY HOPE LEFT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Of0aa61857047c59585d7 | L2387 | no manual edit
EN: [ALRIGHT, UNDERSTOOD. YIFFAI OUT!]
BEFORE:   Yiffai: [明白了。伊法伊结束通话！] 
AFTER:   Yiffai: [明白了。伊法伊结束通话！] 
### P09-025 | action=apply
原问题：RE- STRICTIONS为排版断词，不是限——制的表演拖音；NEGATIVE在此是拒绝行动申请。
本轮理由：拒绝出击许可，排版断词不拖音；同一头行内抵达及未受袭扰信息完整保留，特工沿用。
EDIT_IDS ["E09-043"]

## SCad10f274abd694b4 | nsfw | datadm/all.ds | Bossu.TransitionAreaEAirlock1 noselect
CONTROL L2559 <Bossu.TransitionAreaEAirlock1 noselect>
ROW CAT:O47d7e07e127632172c78 | L2560 | no manual edit
EN: [GOT YOUR COSMOSUIT ON, AGENT?]
BEFORE:   Bossu: [特工，宇宙服穿上了吗？]
AFTER:   Bossu: [特工，宇宙服穿上了吗？]
ROW CAT:Oedb67591774dd8ff047b | L2561 | no manual edit
EN: [W-WHA? MY COSMOSUIT?]
BEFORE:   Yiffai: [什、什么？我的宇宙服？]
AFTER:   Yiffai: [什、什么？我的宇宙服？]
ROW CAT:O764b8f5fa5cd130f81bb | L2562 | no manual edit
EN: [YES, YOUR COSMOSUIT. YOU'RE IN THINNER AIR NOW.]
BEFORE:   Bossu: [对，你的宇宙服。你现在待的地方空气更稀薄了。]
AFTER:   Bossu: [对，你的宇宙服。你现在待的地方空气更稀薄了。]
ROW CAT:Oc1b58dc3bb8dfca993ec | L2563 | no manual edit
EN: [THAT'S RIGHT, THAT GROUND BENEATH YOUR FEET BELONGS]
BEFORE:   Mauser: [没错，你脚下这块地面属于一颗轨道很低的卫星——看起来它以前是座监狱？]
AFTER:   Mauser: [没错，你脚下这块地面属于一颗轨道很低的卫星——看起来它以前是座监狱？]
ROW CAT:O42943302da0acacc896c | L2564 | no manual edit
EN: [TO A LOW ORBITTING MOON THAT SEEMS TO HAVE BEEN A PRISON?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7b6dbea32e2c043939c6 | L2565 | no manual edit
EN: [A PRISON THAT SPACE PIRATES SEEMED FIT TO BUILD A STATION]
BEFORE:   Bossu: [一座监狱，太空海盗似乎觉得在它周围建个据点挺合适，直到有什么东西把他们赶走了。]
AFTER:   Bossu: [一座监狱，太空海盗似乎觉得在它周围建个据点挺合适，直到有什么东西把他们赶走了。]
ROW CAT:O68173dc7ae437dcc3ea0 | L2566 | no manual edit
EN: [AROUND, UNTIL SOMETHING DROVE THEM AWAY.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9ddff25b7395562be9e6 | L2567 | no manual edit
EN: [EITHER WAY, YOU'LL NEED TO GET YOUR COSMOSUIT ON.]
BEFORE:   Bossu: [总之，你得把宇宙服穿上。]
AFTER:   Bossu: [总之，你得把宇宙服穿上。]
ROW CAT:O9fd125d4a29be1498759 | L2568 | EDIT E09-009
EN: [SO MAKE SURE NOBODY'S SNUCK AWAY WITH IT.]
BEFORE:   Bossu: [所以先确认一下没人偷偷把它穿走。]
AFTER:   Bossu: [所以先确认一下，没人偷偷把它拿走。]
ROW CAT:Of126227a28e0400cfd87 | L2569 | no manual edit
EN: [UHHH YEAH, RIGHT! OF COURSE! GOT IT!!!]
BEFORE:   Yiffai: [呃、对！没错！当然！懂了！！！]
AFTER:   Yiffai: [呃、对！没错！当然！懂了！！！]
### P09-008 | action=apply
原问题：snuck away with it是偷拿走装备，不限于穿走；两主角独立提案。
本轮理由：已对完整场景复审：snuck away with it是偷拿走装备，不限于穿走；两主角独立提案。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-009"]

## SCbbbce3c2e89f8789 | nsfw | datadm/all.ds | BossuDex.ClassicCannonFloorC
CONTROL L3249 <BossuDex.ClassicCannonFloorC>
ROW CAT:O01457a3025341491886c | L3250 | EDIT E09-016
EN: [BOSSU, ARE THERE CANNONS STRONGER OR AM I WEAKER?]
BEFORE:   Yiffai: [波苏，是有更强的加农炮，还是我变弱了？]
AFTER:   Yiffai: [波苏，是这些加农炮变强了，还是我变弱了？]
ROW CAT:O5ff6e3f0d8992247dc01 | L3251 | no manual edit
EN: [THESE CANNONS SEEM TO HAVE GONE A WHILE WITHOUT]
BEFORE:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
AFTER:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
ROW CAT:Oe505f7e040192dd5b356 | L3252 | no manual edit
EN: [NEEDING TO BE SELF- REPAIRED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O78f60dcf892355bb99a9 | L3253 | no manual edit
EN: [CONSEQUENTLY THEY SEEM TO BE FIRING AT HIGHER POWER.]
BEFORE:   Bossu: [因此它们似乎正以更高的功率发射。]
AFTER:   Bossu: [因此它们似乎正以更高的功率发射。]
ROW CAT:O665c6f01de452f1807d6 | L3254 | EDIT E09-017
EN: [GREEAAAAAT, JUST WHAT I NEEDED TO DEAL WITH...]
BEFORE:   Yiffai: [太——好了，正好是我需要应付的……]
AFTER:   Yiffai: [太——好了，偏偏又摊上这种麻烦……]
### P09-011 | action=apply
原问题：原文there疑为these笔误，后文明确谈眼前炮台；“是有更强的”问非所指。末句是反讽，不是正好需要应付。
本轮理由：已对完整场景复审：原文there疑为these笔误，后文明确谈眼前炮台；“是有更强的”问非所指。末句是反讽，不是正好需要应付。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-016", "E09-017"]

## SCb6f36febbdf9e0cd | nsfw | datadm/all.ds | BossuDex.ClassicMine
CONTROL L3065 <BossuDex.ClassicMine>
ROW CAT:Oee7354e31cf62666ff01 | L3066 | no manual edit
EN: [WOAH! DID YOU PICK UP THAT EXPLOSION AT HQ?!]
BEFORE:   Yiffai: [哇哦！总部那边有接到那声爆炸吗？！]
AFTER:   Yiffai: [哇哦！总部那边有接到那声爆炸吗？！]
ROW CAT:Oa0269f1397b535ef1499 | L3067 | EDIT E09-044
EN: [INDEED, IT APPEARS THE MINES OF TUTONE HAVE BEEN MINED.]
BEFORE:   Bossu: [确实，看来图托恩的矿山都已经布上了雷。]
AFTER:   Bossu: [确实，看来图托恩的矿区，处处都是“雷区”。]
ROW CAT:O51bbf635a96c12cb2f4e | L3068 | EDIT E09-045
EN: [...? WELL SURE, BUT WHAT'S THAT GOTTA DO WITH EXPLOSIONS?]
BEFORE:   Yiffai: [……? 好吧，可那跟爆炸有什么关系？]
AFTER:   Yiffai: [……？挖矿有那么多忌讳？可这跟爆炸有什么关系？]
ROW CAT:Of7e3b1d609c2cb601640 | L3069 | EDIT E09-046
EN: [THE EXPLOSIONS FROM THE MINES.]
BEFORE:   Bossu: [是那些矿区传来的爆炸。]
AFTER:   Bossu: [我是说，雷区里的雷炸了。]
ROW CAT:Oe81782a65b516d3cfb78 | L3070 | EDIT E09-047
EN: [YEAH! IT WAS IN THE MINES, BUT-]
BEFORE:   Yiffai: [对啊！那是在矿坑里，但是-]
AFTER:   Yiffai: [对啊！矿区里炸了，可是——]
ROW CAT:Oe81cc78aa97885e0f5de | L3071 | EDIT E09-048
EN: [WHAT BOSSU MEANS IS THAT THOSE OLD MINERS PLACED]
BEFORE:   Mauser: [Bossu的意思是，那些老矿工当年在他们自己的矿里埋了地雷，好喊一声“这是我的！”]
AFTER:   Mauser: [Bossu是说，那些老矿工在自家的矿井里埋了地雷，意思是：“这是我的矿，谁也别碰！”]
ROW CAT:Oc55856c16103acb09a06 | L3072 | no manual edit
EN: [MINES IN THEIR MINES, AS A WAY TO SAY "THAT'S MINE!"]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2d626bedb667308b3b31 | L3073 | no manual edit
EN: [WHAT...?! I'LL JUST AVOID THEM, OKAY?! Y-YIFFAI OUT!]
BEFORE:   Yiffai: [什么……？！那我就躲开它们，行吧？！伊、伊法伊通话完毕！]
AFTER:   Yiffai: [什么……？！那我就躲开它们，行吧？！伊、伊法伊通话完毕！]
### P09-026 | action=apply
原问题：现译先明确布雷，主角却问爆炸关系；后句又把地雷译回矿区，问答逻辑崩。建议以“爆破/地雷”中文误解重建双关节奏，不逐词硬凑mine/mine/mine；属改编提案须独立复审。
本轮理由：全场同人槽重建雷区（忌讳／地雷）误解问答与矿井回话；Mauser说明矿工埋雷宣示所有权，不添实际抢夺事件，不逐字硬凑英文同形梗。
EDIT_IDS ["E09-044", "E09-045", "E09-046", "E09-047", "E09-048"]

## SC9bb714108286af8a | nsfw | datadm/all.ds | TomcatItems.SpecialKeycard3
CONTROL L4317 <TomcatItems.SpecialKeycard3>
ROW CAT:Oa2fc40d8e78a4887a8a9 | L4318 | no manual edit
EN: [IN ORDER TO USE A KEYCARD, ALL YOU HAVE TO DO IS]
BEFORE:   Tomcat: [要使用门卡，只需要带着卡走向能量门就行。]
AFTER:   Tomcat: [要使用门卡，只需要带着卡走向能量门就行。]
ROW CAT:O7b788b8feab4658ae3d5 | L4319 | no manual edit
EN: [WALK INTO AN ENERGY DOOR WHILE HOLDING ONE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oeadecefbeda24f7a1a78 | L4320 | EDIT E09-049
EN: [YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!]
BEFORE:   Tomcat: [可打开等级不高于门上所标数字的门！]
AFTER:   Tomcat: [门卡上标着等级，不高于这个等级的门都能打开！]
### P09-027 | action=apply
原问题：“可打开等级不高于门上所标数字的门”把门和卡的比较对象写乱，近乎同义反复；结合本包Keycard1的最低等级说明校正提示，不编新机制。
本轮理由：卡上标示的是可通行最高等级，门等级须不高于卡等级；未改变带卡走向能量门的原头行及空尾。
EDIT_IDS ["E09-049"]

## SC0010041113ecb2fa | nsfw | datadm/all.ds | TomcatItems.SpecialLeftmark
CONTROL L4327 <TomcatItems.SpecialLeftmark>
ROW CAT:O5f22669ca9b533a9d9f0 | L4328 | no manual edit
EN: [OOOOOH, HOW YOU FEELING? YOUR BODY TEMP JUST SPIKED!]
BEFORE:   Tomcat: [哦哟，感觉如何？你体温突然飙升了！]
AFTER:   Tomcat: [哦哟，感觉如何？你体温突然飙升了！]
ROW CAT:O1e05697377603e084528 | L4329 | no manual edit
EN: [I...I'M FINE...I THINK?]
BEFORE:   Yiffai: [我……我没事……大概吧？] 
AFTER:   Yiffai: [我……我没事……大概吧？] 
ROW CAT:Odcc78a53b3a60730dce4 | L4330 | EDIT E09-050
EN: [I RAN INTO THIS GLOWING ORB AND IT LEFT A MARK ON ME.]
BEFORE:   Yiffai: [我碰到个球体，它在我身上留了个印记。]
AFTER:   Yiffai: [我碰到个发光的球体，它在我身上留了个印记。]
ROW CAT:O256a78e4ecea1fc663b1 | L4331 | no manual edit
EN: [MAYBE THAT HAS SOMETHING TO DO WITH THE ESPERS!]
BEFORE:   Tomcat: [说不定那跟超能力者有关！]
AFTER:   Tomcat: [说不定那跟超能力者有关！]
ROW CAT:O4e943dad397c71370750 | L4332 | no manual edit
EN: [ESPERS??]
BEFORE:   Yiffai: [超能力者？？]
AFTER:   Yiffai: [超能力者？？]
ROW CAT:O897f7a2377cdca7d5603 | L4333 | no manual edit
EN: [YEAH, THE PREVIOUS AGENTS LEFT BEHIND CLUES THAT THERE]
BEFORE:   Tomcat: [对，之前的特工留下的线索表明，这颗星球很久以前住着有超能力的生物。]
AFTER:   Tomcat: [对，之前的特工留下的线索表明，这颗星球很久以前住着有超能力的生物。]
ROW CAT:O4edb807684e54563c565 | L4334 | no manual edit
EN: [WERE BEINGS WITH ESP ON THAT PLANET LONG AGO.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa364b3919a3dfb017bdc | L4335 | no manual edit
EN: [THESE ESP SENSITIVE BEINGS, THE ESPERS, SURELY LEFT BEHIND]
BEFORE:   Tomcat: [这些拥有超感知觉的超能力者，肯定留下了一些古代科技！]
AFTER:   Tomcat: [这些拥有超感知觉的超能力者，肯定留下了一些古代科技！]
ROW CAT:O5ec188e9f67529f3e830 | L4336 | no manual edit
EN: [SOME OF THEIR ANCIENT TECHNOLOGY!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O3e6bfd0e42816351a9f7 | L4337 | no manual edit
EN: [NOW THAT YOU MENTION IT, I DO FEEL STRONGER...]
BEFORE:   Yiffai: [你这么一说，我确实感觉更强了……]
AFTER:   Yiffai: [你这么一说，我确实感觉更强了……]
ROW CAT:Of232ffb0b01fb30ce4e1 | L4338 | no manual edit
EN: [IF YOU FIND ANY MORE ARTIFACTS, GIVE ME A HOLLER]
BEFORE:   Tomcat: [再找到什么遗物，就叫我一声，咱们一起解开这个谜团！]
AFTER:   Tomcat: [再找到什么遗物，就叫我一声，咱们一起解开这个谜团！]
ROW CAT:O29b4a802eeef9e38032a | L4339 | no manual edit
EN: [AND WE CAN TRY TO SOLVE THIS MYSTERY TOGETHER!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P09-028 | action=apply
原问题：glowing漏义；这是球体视觉特征，不应因后文探测不到就删掉。
本轮理由：已对完整场景复审：glowing漏义；这是球体视觉特征，不应因后文探测不到就删掉。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-050"]

## SC6e4d979cdf3f0678 | sfw | datadm/all.ds | TomcatItems.TribalBody
CONTROL L4065 <TomcatItems.TribalBody>
ROW SFW93964b22e121f11340e2ba2a | L4066 | no manual edit
EN: [HEY TOMCAT, WHAT'S THIS VEST-THINGIE?]
BEFORE:   Yiffai: [嘿，汤姆猫，这件像背心的东西是什么？]
AFTER:   Yiffai: [嘿，Tomcat，这件像背心的东西是什么？]
ROW SFW767bb9716f59b9d6741deb32 | L4067 | no manual edit
EN: [IT SEEMS TO BE A TRADITIONAL BATTLE GARB DEVELOPED BY]
BEFORE:   Tomcat: [这似乎是图托恩本土的一种犬科物种制作的传统战服，而且完好无损！异星考古部一定会——]
AFTER:   Tomcat: [这似乎是图托恩本土的一种犬科物种制作的传统战服，而且完好无损！异星考古部一定会——]
ROW SFW30abc5ed64e0006e966af700 | L4068 | no manual edit
EN: [A CANID SPECIES NATIVE TO TUTONE, AND IT'S IN PERFECT]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWedd48843cad27bda742663ce | L4069 | no manual edit
EN: [CONDITION! THE XENO-ARCHAEOLOGY DEPARTMENT WILL-]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW6941f3257d43114d7fe79fef | L4070 | no manual edit
EN: [HAH, THIS WILL PROTECT ME PRETTY GOOD *AND* EVERYONE]
BEFORE:   Yiffai: [哈，这既能好好保护我，*又*能让大家]
AFTER:   Yiffai: [哈，这既能好好保护我，*又*能让大家]
ROW SFW171869b9e4c20cd1c953d733 | L4071 | EDIT E09-051
EN: [WILL THINK I LOOK COOL! THAT'S AWESOME!]
BEFORE:   Yiffai: [会觉得我很酷！太棒了！]
AFTER:   Yiffai: [觉得我很酷！太棒了！]
ROW SFW31cd96bb1d04bd85afbe982e | L4072 | no manual edit
EN: [T-THAT TOO, PUP. THAT TOO...]
BEFORE:   Tomcat: [也、也是，小狗。也是……]
AFTER:   Tomcat: [也、也是，小狗。也是……]
CONTROL L4074 ### Pirate ###
### P09-029 | action=apply
原问题：“又能让大家／会觉得”串联成病句，整句恢复显摆与实用并存。
本轮理由：已对完整场景复审：“又能让大家／会觉得”串联成病句，整句恢复显摆与实用并存。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-051"]

## SC6b99892905a98a17 | nsfw | datav/dictionary.json | JudoHead
ROW CAT:O02e8fba73a0cb3526068 | L- | EDIT E09-052
EN: SMELLS LIKE A|FIGHTING GUSTO
BEFORE: 闻起来像|好斗的劲头
AFTER: 闻着就有|格斗的干劲
ROW CAT:Oe6c7d9995173f6c5b4a2 | L- | no manual edit
EN: HEADBAND
BEFORE: 头带
AFTER: 头带
### P09-030 | action=apply
原问题：气味/战斗劲头的诙谐比喻可保留，但“闻起来像好斗的劲头”搭配不成中文。保留两行控制分隔。
本轮理由：保留嗅觉比喻和原两行分隔，避免把格斗干劲解释成真实气味种类。
EDIT_IDS ["E09-052"]

## SC86e3980ef25f719b | nsfw | datav/dictionary.json | SpecialFap.ElfBuff
ROW CAT:O0b9052253e0b7a0ed16d | L- | no manual edit
EN: ELF RECHARGES|PSY WHEN IDLE
BEFORE: 精灵闲置时|回复精神力
AFTER: 精灵闲置时|回复精神力
### P09-031 | action=defer
原问题：原UI把ELF写成主语，容易理解为精灵自己回复；这是SpecialFap.ElfBuff效果名，但idle具体判定未核，暂不写“静止/未输入几秒”。
本轮理由：仅知精灵加成说明，idle触发与回复归属未完成实际机制取证，不能把草案当确认修复。
EDIT_IDS []

## SCd1604a5e213330b8 | nsfw | datav/dictionary.json | ui.card.CosmoCardSwiper.desc
ROW CAT:O6c840239cc755c02926d | L- | no manual edit
EN: Bulky and slow  | (unusual for a  | feline species) | the Swiper is   | only a danger if| 
EN+ passed directly | in their front. | They will not   | hesitate to claw| the way clear in| 
EN+ front of them!
BEFORE: 又壮又慢|（对猫科来说|很不寻常）。|挥爪只有在|有人从正面|直接经过时|才危险。|它们会毫不犹豫|用爪子|清开面前的路|！

AFTER: 又壮又慢|（对猫科来说|很不寻常）。|挥爪只有在|有人从正面|直接经过时|才危险。|它们会毫不犹豫|用爪子|清开面前的路|！

ROW CAT:Oaf2dc898dc09544cf751 | L- | EDIT E09-053
EN: Covered with    | front-facing    | barbs, the penis| of the Swiper   | is known to have| 
EN+ many agents as  | fans. Soft and  | pliable, the    | barbs act to st-| imulate agents  | 
EN+ in exciting ways| while the cat's | thick legs allow| invigoratingly  | hard thrusting.
BEFORE: 挥爪的阴茎|覆满|朝前的|倒刺，|据说有不少|特工是粉丝。|倒刺柔软|可弯，|会以兴奋的方式|刺激特工，|而这只猫|粗壮的双腿|则让|十分带劲的|用力抽插成为可能。 

AFTER: 挥爪的阴茎|长满朝前的|肉刺，|据说很受|不少特工欢迎。|这些肉刺|柔软可弯，|能给特工带来|令人兴奋的|刺激；|它粗壮的双腿|则能支撑|猛烈的抽插，|让人倍感|畅快。 

### P09-032 | action=apply
原问题：“以兴奋的方式／抽插成为可能”逐词腔拖长科普段；重写因果和主宾，保留柔软与朝向，不把barbs一律写反向倒刺。
本轮理由：保留朝前、柔软可弯、据说受不少特工欢迎及双腿支撑猛烈抽插的全部含义；原15行结构与末尾换行保留。
EDIT_IDS ["E09-053"]

## SCff66aeccebc5f999 | nsfw | datav/dictionary.json | ui.data.f_GameOverAreaB
ROW CAT:O731ba8e10998a4e85c22 | L- | EDIT E09-054
EN: EXPERT BITCHES CAN ONLY TAKE|SO MUCH TEASING BEFORE...
BEFORE: 老练的母狗也只能受|这么多逗弄，然后…… 
AFTER: 再老练的母狗|也经不起一再撩拨…… 
### P09-033 | action=apply
原问题：can only take so much是忍耐有极限；“只能受这么多，然后”未给数量又悬断，预告语应保留后果省略。
本轮理由：已对完整场景复审：can only take so much是忍耐有极限；“只能受这么多，然后”未给数量又悬断，预告语应保留后果省略。 按原有效节点自然改写，未改事实与控制。
EDIT_IDS ["E09-054"]

## SC21fefe59ec8bd90b | nsfw | datav/dictionary.json | ui.data.m_AgentM08
ROW CAT:Ofac15312bf142581e347 | L- | EDIT E09-055
EN: AGENT-TURNED-SLAVE VULPINE|SHOWS HE CAN OUTFOX EM ALL|UNTIL A STRANGER APPEARS...
BEFORE: 由特工变成奴隶的狐|显出他能智胜所有人|直到一个陌生人出现……
AFTER: 沦为奴隶的狐族特工|智胜众人、大显身手，|直到一位陌生人现身……
### P09-034 | action=apply
原问题：“由特工变成奴隶的狐／显出他能智胜”生硬；outfox双关依靠狐族身份即可承接。自以为是预告的反转语气提案，不当客观能力认证。
本轮理由：菜单预告是显示智胜众人的叙述，不按草案添加“自以为”；保留狐族和陌生人反转，三行结构不变。
EDIT_IDS ["E09-055"]

## SC6649f2ce601a031d | nsfw | datay/scripts_pack.json | /missionLog/female/13/text
ROW CAT:O68930cba591af56729bc | L- | no manual edit
EN: With his ship downed and a  | storm brewing outside, agent| Yiffai had no choice but to | 
EN+ chance a journey into the   | depths of an abandoned alien| facility for shelter.       |
EN+ 
                            |
His first order of business | should be to reestablish    |
EN+  communications with         | headquarters!
BEFORE: 飞船坠毁，|外面又风暴大作，|特工伊法伊别无选择，|只能冒险深入一座|废弃外星设施的深处|寻找庇护。|
                            |

BEFORE+ 他的首要任务，|就是与总部|重新建立|通信！

AFTER: 飞船坠毁，|外面又风暴大作，|特工伊法伊别无选择，|只能冒险深入一座|废弃外星设施的深处|寻找庇护。|
                            |

AFTER+ 他的首要任务，|就是与总部|重新建立|通信！

### P09-035 | action=defer
原问题：路径为female，但英文连续写his/Yiffai；中文忠于当前源文，不能直接报女主误译。须查该nested_json的实际调用与female/male选择，风险为主角/版本串线。
本轮理由：female路径内源文明确his/Yiffai，当前中文忠于源；嵌套JSON实际调用与主角选择未证，留置源/用途Q，不按目录强改。
EDIT_IDS []

## SCa4f1ced2b88fd910 | nsfw | vsn/f_GameOverAreaA/script.vsn | vsn/f_GameOverAreaA/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 snap: ClassicGameOverAreaAA
CONTROL L3 waitForCue!
CONTROL L4 rewind!
ROW CAT:O02027190d47bd8db1a65 | L5 | no manual edit
EN: You'd think I'd have learned better than to risk a bump on the head
BEFORE: text: 干了这么多年育种工作，按说我早该学乖，别再冒险撞到脑袋了。
AFTER: text: 干了这么多年育种工作，按说我早该学乖，别再冒险撞到脑袋了。
ROW CAT:O6796857e1865fdd33447 | L6 | no manual edit
EN: after all these years of 'breeding.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O3c8fa83218e66ab728bf | L7 | no manual edit
EN: ...But you'd be wrong! That's not how you make a good impression!
BEFORE: text: ……那你就错了！那可不是留下好印象的办法！
AFTER: text: ……那你就错了！那可不是留下好印象的办法！
CONTROL L9 cut(0.06): ClassicGameOverAreaAB
CONTROL L10 rewind!
ROW CAT:O6e0d7168a765860a7622 | L11 | no manual edit
EN: Oof, that was a rough hit though. Gonna take a while to warm back up
BEFORE: text: 嘶，那一下可真狠。得缓一会儿才能恢复状态，再继续我的救援工作。
AFTER: text: 嘶，那一下可真狠。得缓一会儿才能恢复状态，再继续我的救援工作。
ROW CAT:Of6a10c2f3d354ddfebfe | L12 | no manual edit
EN: and get back to all this rescuing business.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O2fc798d418d51d7bebf5 | L13 | no manual edit
EN: Just gotta remember what I was doing before getting roughed up.
BEFORE: text: 只要想起被折腾之前我在干什么就好。
AFTER: text: 只要想起被折腾之前我在干什么就好。
ROW CAT:O7789a8f4920cb39107a1 | L14 | no manual edit
EN: Lessee, pretty sure I was on my way over to th-
BEFORE: text: 让我想想，我记得当时正要去那——
AFTER: text: 让我想想，我记得当时正要去那——
CONTROL L16 cut(0.06): ClassicGameOverAreaAC
CONTROL L17 rewind!
ROW CAT:O2ff50158f903fd5a344f | L18 | no manual edit
EN: -hey! Ow! That's my BUTT, you jerk!
BEFORE: text: —喂！疼！那是我的屁股，混蛋！
AFTER: text: —喂！疼！那是我的屁股，混蛋！
ROW CAT:O7f89b06fef2b1c7e0bc6 | L19 | no manual edit
EN: As soon as I get back on my feet, I'm gonna turn you into jelly!
BEFORE: text: 等我站起来，就把你打成果冻！
AFTER: text: 等我站起来，就把你打成果冻！
CONTROL L21 cut(0.06): ClassicGameOverAreaAD
CONTROL L22 rewind!
ROW CAT:O482415dee828fbd8b38c | L23 | no manual edit
EN: Orrrr maybe you're already jelly?
BEFORE: text: 还——是说，你已经软成一滩果冻了？ 
AFTER: text: 还——是说，你已经软成一滩果冻了？ 
ROW CAT:O8058bb4e5df1b6398ec2 | L24 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O606543a1e8b8d92e87d6 | L25 | no manual edit
EN: ...my butt isn't that fat, is it? You must've already been jelly!
BEFORE: text: ……我屁股没那么肥吧？你本来就软成一摊了吧！
AFTER: text: ……我屁股没那么肥吧？你本来就软成一摊了吧！
ROW CAT:Oc1c90dccd96d1eb6ead8 | L26 | no manual edit
EN: Weird to see one of you Slimers are spread out like this. Usually you only
BEFORE: text: 真少见，你们史莱姆居然摊成这样。一般只有想困住谁的时候，才会分裂开来。
AFTER: text: 真少见，你们史莱姆居然摊成这样。一般只有想困住谁的时候，才会分裂开来。
ROW CAT:O1c73d7fd0249283b81de | L27 | no manual edit
EN: break up if you're gonna try trap someone.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L29 cut(0.06): ClassicGameOverAreaAE
CONTROL L30 rewind!
ROW CAT:Od7a91b427d92cce66872 | L31 | no manual edit
EN: Oh! Duh! That's EXACTLY what you were doing!
BEFORE: text: 哦！真笨！你刚才干的就是这个！ 
AFTER: text: 哦！真笨！你刚才干的就是这个！ 
ROW CAT:O62606326263244fec406 | L32 | no manual edit
EN: If only my head wasn't so fuzzy after getting it bumped earlier
BEFORE: text: 要不是刚才脑袋撞得晕晕乎乎的，我本来能趁事态还没失控就逃出去——呀啊啊！！
AFTER: text: 要不是刚才脑袋撞得晕晕乎乎的，我本来能趁事态还没失控就逃出去——呀啊啊！！
ROW CAT:O3acdd36defb0852969b4 | L33 | no manual edit
EN: I could've ran before this started to get out of haaaaaYYYYYOH!!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc11b9a178f860f42e4df | L34 | no manual edit
EN: F-fu...damn! You're a rowdy bastard, just going for it right away...
BEFORE: text: 操、操……该死！你这混蛋真野，一上来就直奔主题……
AFTER: text: 操、操……该死！你这混蛋真野，一上来就直奔主题……
ROW CAT:Oeedb9cf792a7ed61920a | L35 | no manual edit
EN: ...ohmygosh...
BEFORE: text: ……天哪……
AFTER: text: ……天哪……
CONTROL L37 cut(0.06): ClassicGameOverAreaAF
CONTROL L38 rewind!
ROW CAT:O6848a9f7ae22d76267b5 | L39 | no manual edit
EN: D-damn slimy rascal, you're good at this, aren't ya? F-fine, I'll give you a try.
BEFORE: text: 该、该死的黏滑坏蛋，还挺有两下子？好、好吧，让你试试。
AFTER: text: 该、该死的黏滑坏蛋，还挺有两下子？好、好吧，让你试试。
ROW CAT:O75cd807e244f06d53a8a | L40 | no manual edit
EN: Just gotta get my hands free so I can show you how to angle properly...
BEFORE: text: 先把手挣出来，我再教你怎么找准角度……
AFTER: text: 先把手挣出来，我再教你怎么找准角度……
ROW CAT:O4a4d94b1d93e4e6ab1a9 | L41 | no manual edit
EN: Mmmf, there... Tricky to slip out of you Slimers, but I ain't no rookie!
BEFORE: text: 唔，好了……想从你们史莱姆体内抽出来可不容易，但我可不是新手！
AFTER: text: 唔，好了……想从你们史莱姆体内抽出来可不容易，但我可不是新手！
ROW CAT:O4a0b085ac919f12b4984 | L42 | no manual edit
EN: Ahh yeah see, just get down a bit more... Yeah... just about...
BEFORE: text: 啊，对，就是这样，再往下一点……对……就快……
AFTER: text: 啊，对，就是这样，再往下一点……对……就快……
CONTROL L44 cut(0.06): ClassicGameOverAreaAG
CONTROL L45 rewind!
ROW CAT:O9a298c1c02fbd3a2b205 | L46 | no manual edit
EN: Gah! Not quite that low! Woooooah boy. What is this, 3PC Academy all over again?
BEFORE: text: 呀！别那么下面！哇啊，乖乖。这是又回3PC学院了？
AFTER: text: 呀！别那么下面！哇啊，乖乖。这是又回3PC学院了？
ROW CAT:O72c9bf7d618cccfccd10 | L47 | no manual edit
EN: I'm a pro, so it's not like I can't handle a bit of undertail action or anything
BEFORE: text: 我可是专业的，来点后入式的也不在话下，但你好歹该先打个招呼吧！
AFTER: text: 我可是专业的，来点后入式的也不在话下，但你好歹该先打个招呼吧！
ROW CAT:O61b32346a7cc58bd44de | L48 | no manual edit
EN: but a bit of warning would've been nice!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oceb3078e62d43f81dc73 | L49 | no manual edit
EN: Let's see if we can't tire out your non-existing bones now, shall we?
BEFORE: text: 来看看，能不能把你那不存在的骨头都折腾散架？
AFTER: text: 来看看，能不能把你那不存在的骨头都折腾散架？
CONTROL L51 cut(0.06): Black
CONTROL L52 rewind!
ROW CAT:O2cfa065138fbca0c353a | L53 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O3b8e78051bd8ee51c0f0 | L54 | no manual edit
EN: ...okay you have more stamina than I thought.
BEFORE: text: ……好吧，你比我想的更持久。
AFTER: text: ……好吧，你比我想的更持久。
ROW CAT:O1b140ebef68ae2ac669f | L55 | no manual edit
EN: ...ow...
BEFORE: text: ……疼……
AFTER: text: ……疼……
CONTROL L57 cut(0.06): ClassicGameOverAreaAH
CONTROL L58 rewind!
ROW CAT:O53eb52207e80ebb4e45d | L59 | no manual edit
EN: Hah... Hah... I think I need a moment to recover from that.
BEFORE: text: 哈……哈……我得缓一会儿才能恢复。
AFTER: text: 哈……哈……我得缓一会儿才能恢复。
ROW CAT:Obbcae1460c02613effdc | L60 | no manual edit
EN: My head feels plenty fine now, but darn did you do a number on my poor hips.
BEFORE: text: 脑袋是没事了，可怜的胯却被你折腾惨了。
AFTER: text: 脑袋是没事了，可怜的胯却被你折腾惨了。
ROW CAT:O711383e99db5979acdd2 | L61 | no manual edit
EN: You can't just bounce a girl around for that long! But at least you're satisfied.
BEFORE: text: 哪有把姑娘颠来颠去这么久的！不过至少你满足了。
AFTER: text: 哪有把姑娘颠来颠去这么久的！不过至少你满足了。
CONTROL L63 snap: ClassicGameOverAreaAH3
CONTROL L64 rewind!
ROW CAT:O16ce3b0452ea4f52c7af | L65 | no manual edit
EN: I just need a minute for my spine to straighten out again here.
BEFORE: text: 给我一分钟，让脊椎重新挺直就行。 
AFTER: text: 给我一分钟，让脊椎重新挺直就行。 
CONTROL L67 snap: ClassicGameOverAreaAH4
CONTROL L68 rewind!
ROW CAT:O48948e04cf4f742cf72a | L69 | no manual edit
EN: A nice, quiet minute with nothing interrupting me.
BEFORE: text: 安安静静歇一会儿，什么也不来打扰。
AFTER: text: 安安静静歇一会儿，什么也不来打扰。
CONTROL L71 snap: ClassicGameOverAreaAH5
CONTROL L72 rewind!
ROW CAT:O441b0c18c32c969c790b | L73 | no manual edit
EN: Yeah, that sounds like it should be all I need...
BEFORE: text: 嗯，听起来这样就够了……
AFTER: text: 嗯，听起来这样就够了……
CONTROL L75 snap: ClassicGameOverAreaAH2
CONTROL L76 rewind!
ROW CAT:O4b3a8f7cbcdd0f1b5850 | L77 | no manual edit
EN: ..and then back to rescuing all these other agents I can go!
BEFORE: text: ……然后就能继续救其他特工啦！
AFTER: text: ……然后就能继续救其他特工啦！
CONTROL L79 cut(0.06): ClassicGameOverAreaAI
CONTROL L80 rewind!
ROW CAT:O5dce76e5f2c05ed14959 | L81 | no manual edit
EN: Awwwwww heck. Hecking heck heck heckeroos!
BEFORE: text: 啊——见鬼。真见鬼，见鬼见鬼，见了个大头鬼！
AFTER: text: 啊——见鬼。真见鬼，见鬼见鬼，见了个大头鬼！
ROW CAT:O785f9a2965879b4f4edd | L82 | no manual edit
EN: Don't you wobbly eye me, you hecking Flayer! I ain't falling for it!
BEFORE: text: 别拿那晃眼的招数对付我，混账剥心魔！我才不上当！
AFTER: text: 别拿那晃眼的招数对付我，混账剥心魔！我才不上当！
ROW CAT:O846a6aeb60301bb2b19d | L83 | no manual edit
EN: You think I'm some rookie whose brain is gonna melt just because you're staring
BEFORE: text: 你以为我是那种被你使劲瞪着看，就会脑袋融化的菜鸟？想得美！我的脑子可不是你的午间零食！
AFTER: text: 你以为我是那种被你使劲瞪着看，就会脑袋融化的菜鸟？想得美！我的脑子可不是你的午间零食！
ROW CAT:Oe71c11ee2aabc4a9fa71 | L84 | no manual edit
EN: at me too real hard? Think again! My mind isn't your midday snack!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L86 cut(0.06): ClassicGameOverAreaAJ
CONTROL L87 rewind!
ROW CAT:Oe3a19790694ab7e52fc6 | L88 | no manual edit
EN: Gyah, putting those tentacles to use too are ya? Well it'sh no ushe.
BEFORE: text: 呀啊，你连触手也用上了？哼，没用的。
AFTER: text: 呀啊，你连触手也用上了？哼，没用的。
ROW CAT:O9eeff8cc7b6c9b80dcc6 | L89 | no manual edit
EN: ShI'mn owt ohnnah get maeh mindh yeathen...
BEFORE: text: 窝才不会让你把脑纸吃掉……
AFTER: text: 窝才不会让你把脑纸吃掉……
ROW CAT:O6a6e2a729478a4ee6fde | L90 | no manual edit
EN: ooOOoooohhoHHhHh...!
BEFORE: text: 哦哦噢噢啊啊啊……！
AFTER: text: 哦哦噢噢啊啊啊……！
CONTROL L92 cut(0.06): Black
CONTROL L93 rewind!
ROW CAT:O9ccb7cef6a45f4b5cef3 | L94 | no manual edit
EN: [EDITOR'S NOTE: Agent Yiffany Yiffai did indeed succumb to the Mind Flayer.]
BEFORE: text: [编者注：特工伊法妮·伊法伊确实败给了剥心魔。]
AFTER: text: [编者注：特工伊法妮·伊法伊确实败给了剥心魔。]
ROW CAT:Ocae28da83b7708e1429e | L95 | no manual edit
EN: [Despite her impressive resiliance to the Flayer's hypnotic eye, the Agent]
BEFORE: text: [这名特工虽对剥心魔的催眠眼展现出惊人的抵抗力，]
AFTER: text: [这名特工虽对剥心魔的催眠眼展现出惊人的抵抗力，]
ROW CAT:O4e427bb1f3d7496d3d57 | L96 | no manual edit
EN: [was still not able to overcome the namesake flaying of the mind.]
BEFORE: text: [仍未能抵御那令剥心魔得名的心智剥离。]
AFTER: text: [仍未能抵御那令剥心魔得名的心智剥离。]
CONTROL L98 cut(0.06): ClassicGameOverAreaAK
CONTROL L99 rewind!
ROW CAT:Oc0a688827663fa49a237 | L100 | EDIT E09-056
EN: [The rest of the Agent's experience seems to consist of them having been]
BEFORE: text: [此后，该特工的经历似乎便是先被]
AFTER: text: [此后，这名特工似乎先被抽干心智，]
ROW CAT:O97567834bd9e5dba83c5 | L101 | EDIT E09-057
EN: [mentally drained and then passed off to another local fauna of Tutone.]
BEFORE: text: [被抽干心智，再转交给图托恩的另一只本土生物。]
AFTER: text: [再被交给图托恩的另一种本土生物。]
ROW CAT:O084645f5143d4d9041fd | L102 | EDIT E09-058
EN: [In a sort of symbiotic cooperation, Flayers seem to mentally drain a victim]
BEFORE: text: [剥心魔似乎先抽干受害者的心智，以此形成共生合作，]
AFTER: text: [两者似乎有着某种共生关系：剥心魔先抽干受害者的心智，]
ROW CAT:Of4cd394abe8237db6c0b | L103 | EDIT E09-059
EN: [before allowing another creature to keep the victim as an energy source.]
BEFORE: text: [再让另一种生物将受害者圈养为能量来源。]
AFTER: text: [再交由另一种生物圈养，充作能量来源。]
CONTROL L105 cut(0.06): ClassicGameOverAreaAL
CONTROL L106 rewind!
ROW CAT:O33a09ffe391842c649e7 | L107 | no manual edit
EN: [With mental incapacitation complete, the victim is nestled into a tentacle bed]
BEFORE: text: [待受害者心智彻底失能，便会被安置进触手床中]
AFTER: text: [待受害者心智彻底失能，便会被安置进触手床中]
ROW CAT:O73111cc2ebd907235bd3 | L108 | no manual edit
EN: [where constant sexual gratification keeps them placated.]
BEFORE: text: [持续不断的性满足让受害者安分下来。]
AFTER: text: [持续不断的性满足让受害者安分下来。]
ROW CAT:O3d87c9e9c47d6d3711f9 | L109 | no manual edit
EN: [These are extraordinary findings that the Agent will no doubt appreciate]
BEFORE: text: [这些非凡的发现，想必会让该特工十分欣喜，]
AFTER: text: [这些非凡的发现，想必会让该特工十分欣喜，]
ROW CAT:Ofa6dfe84d7b5b44296f4 | L110 | no manual edit
EN: [as soon as their mental facilities are returned to them!]
BEFORE: text: [等她恢复心智能力后！]
AFTER: text: [等她恢复心智能力后！]
CONTROL L112 cut(0.06): Black
CONTROL L113 rewind!
ROW CAT:O86eca48226ca570a70aa | L114 | no manual edit
EN: [We have many additional agents heading to Tutone to investigate further]
BEFORE: text: [我们正增派多名特工前往图托恩，展开进一步调查]
AFTER: text: [我们正增派多名特工前往图托恩，展开进一步调查]
ROW CAT:O4cb30aadaebdae0cc998 | L115 | no manual edit
EN: [so that we can return Yiffany, one of our most prized Agents,]
BEFORE: text: [以便让我们最珍视的特工之一，伊法妮，]
AFTER: text: [以便让我们最珍视的特工之一，伊法妮，]
ROW CAT:Of30e7e09c1d0f16cabb5 | L116 | no manual edit
EN: [to her previous state.]
BEFORE: text: [恢复到原先的状态。]
AFTER: text: [恢复到原先的状态。]
ROW CAT:Oa39945aad2f6f988b45b | L117 | no manual edit
EN: [Until Yiffany is capable once more, her file will be placed on hold. -EDITOR]
BEFORE: text: [伊法妮恢复行动能力前，本档案暂缓更新。——编者]
AFTER: text: [伊法妮恢复行动能力前，本档案暂缓更新。——编者]
CONTROL L119 wait: 0.2
CONTROL L120 fadeout(1.0, 1.0, 4)
### P09-036 | action=apply
原问题：“先被／被”重复；原文another local fauna泛指另一种本土生物，不必限定一只；共生为seem阶段判断，不改成因果“以此形成”。各原发言节点分别回填，不跨cut合句。
本轮理由：逐现存text槽修重复被动，保留seems及另一种本土生物；共生仍是报告推断，cut前后不挪义。
EDIT_IDS ["E09-056", "E09-057", "E09-058", "E09-059"]

## SCc2e08d1dfc6c98fd | nsfw | vsn/m_AgentMZ3/script.vsn | vsn/m_AgentMZ3/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Male
CONTROL L4 rewind!
ROW CAT:Oc52cb2e4a7a34a2a5c69 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
AFTER: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
ROW CAT:O8a969fc2315af25618a1 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放在我的手上。
AFTER: lang(Fox): 现在，把你的双手放在我的手上。
ROW CAT:Oc0a3ea5b78a7f7e92599 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
AFTER: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
CONTROL L9 cut(0.06): FenfenC01
CONTROL L10 rewind!
ROW CAT:O13a0923237a1a26ba975 | L11 | no manual edit
EN: As dark forces descended on all Fenfen, young and old alike,
BEFORE: lang(Fox): 当黑暗势力降临到全体Fenfen——无论老幼——头上时，
AFTER: lang(Fox): 当黑暗势力降临到全体Fenfen——无论老幼——头上时，
ROW CAT:O96bcd8bf2d7d36f45bba | L12 | no manual edit
EN: it truly did seem like all hope was lost.
BEFORE: lang(Fox): 那时，仿佛一切希望都已破灭。
AFTER: lang(Fox): 那时，仿佛一切希望都已破灭。
ROW CAT:O1f8756cc3ba93c0230af | L13 | EDIT E09-060
EN: Powerful though the ESPers of our people may have been, violence was unknown to us.
BEFORE: lang(Fox): 我们族中的超能力者纵然或许强大，暴力对我们却全然陌生。
AFTER: lang(Fox): 我们族中的超能力者力量虽强，但我们从未接触过暴力。
CONTROL L15 cut(0.06): FenfenC02
CONTROL L16 rewind!
ROW CAT:Obb9c493d38b7128a736e | L17 | no manual edit
EN: Only when pushed to the end of options, when even surrender seemed impossible
BEFORE: lang(Fox): 直到被逼得走投无路，甚至连投降都不可能时，
AFTER: lang(Fox): 直到被逼得走投无路，甚至连投降都不可能时，
ROW CAT:O6e5722108c3d24c2bef3 | L18 | no manual edit
EN: did the first of us strike out...
BEFORE: lang(Fox): 我们中才终于有人率先反击……
AFTER: lang(Fox): 我们中才终于有人率先反击……
CONTROL L20 cut(0.06): FenfenC03
CONTROL L21 rewind!
ROW CAT:O15ac4200473b3e5aaad3 | L22 | no manual edit
EN: ...and retaliate!
BEFORE: lang(Fox): ……并奋起反击！
AFTER: lang(Fox): ……并奋起反击！
ROW CAT:O10709b36a90c1ccab9c7 | L23 | no manual edit
EN: Psychic abilities once turned only towards a common good
BEFORE: lang(Fox): 曾经只用于共同福祉的心灵能力，
AFTER: lang(Fox): 曾经只用于共同福祉的心灵能力，
ROW CAT:O48849d0845701f2fb9d3 | L24 | no manual edit
EN: would now be turned against those who would try to subjugate us Fenfen!
BEFORE: lang(Fox): 如今要用来反抗那些妄图奴役我们Fenfen的敌人！
AFTER: lang(Fox): 如今要用来反抗那些妄图奴役我们Fenfen的敌人！
CONTROL L26 cut(0.06): FenfenC04
CONTROL L27 rewind!
ROW CAT:Oaae286b0a978ae8937b2 | L28 | EDIT E09-061
EN: An arsenal of ESPer abilities became harnessed as weapons of war.
BEFORE: lang(Fox): 超能力者的能力武库被征用为战争的武器。
AFTER: lang(Fox): 各种超能力就这样被用作战争的武器。
ROW CAT:O823e610ef2e8475e9e37 | L29 | no manual edit
EN: Explosive psychic projectiles blasted away foes.
BEFORE: lang(Fox): 爆裂的灵能弹将敌人轰飞。 
AFTER: lang(Fox): 爆裂的灵能弹将敌人轰飞。 
ROW CAT:Oc5a9b8d75fc57b74e78e | L30 | no manual edit
EN: Punishing waves of telekinetic force prevented advancement of armies.
BEFORE: lang(Fox): 强劲的念动力波阻住了大军的推进。
AFTER: lang(Fox): 强劲的念动力波阻住了大军的推进。
ROW CAT:O42cf30a05bd9e3c9634b | L31 | no manual edit
EN: Some even went so far as to transform their very bodies into tools for combat.
BEFORE: lang(Fox): 有些人甚至把自己的身体变成了战斗兵器。
AFTER: lang(Fox): 有些人甚至把自己的身体变成了战斗兵器。
CONTROL L34 cut(0.06): FenfenC05
CONTROL L35 rewind!
ROW CAT:O2be23999eb5bb476efd5 | L36 | no manual edit
EN: Ancient beings heard the cries of mental anguish that rang throughout the planet
BEFORE: lang(Fox): 古老的存在们听见了回荡于整颗星球的精神痛呼，
AFTER: lang(Fox): 古老的存在们听见了回荡于整颗星球的精神痛呼，
ROW CAT:Of446a992cccffe3321cb | L37 | no manual edit
EN: Some, like the noble Elves, took up ancient weapons in order to aid us Fenfen...
BEFORE: lang(Fox): 有些如高贵的精灵，拿起古老兵器援助我们Fenfen……
AFTER: lang(Fox): 有些如高贵的精灵，拿起古老兵器援助我们Fenfen……
CONTROL L40 cut(0.06): FenfenC06
CONTROL L41 rewind!
ROW CAT:O99a785e3663c0867c7a5 | L42 | no manual edit
EN: ...while other ancient beings, from deep within the bowels of the planet
BEFORE: lang(Fox): ……而其他古老的存在，则从这颗星球最深的地底，
AFTER: lang(Fox): ……而其他古老的存在，则从这颗星球最深的地底，
ROW CAT:Oe258812f94ef6eacff4c | L43 | no manual edit
EN: awoke with a desire for vengeance and domination of their own...
BEFORE: lang(Fox): 带着属于它们自己的复仇与征服欲望苏醒了……
AFTER: lang(Fox): 带着属于它们自己的复仇与征服欲望苏醒了……
CONTROL L46 wait: 0.2
CONTROL L47 fadeout(1.0, 1.0, 4)
### P09-037 | action=apply
原问题：may have been在让步句不必生硬“纵然或许”；“能力武库被征用为武器”名词堆砌。两个独立节点分别润写。
本轮理由：让步句自然化，不把may机械重复成或许；能力用作战争武器，不新增征用者。
EDIT_IDS ["E09-060", "E09-061"]

## SCb9a3af2c476d7f1b | nsfw | vsn/m_AgentMZ5/script.vsn | vsn/m_AgentMZ5/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Male
CONTROL L4 rewind!
ROW CAT:O9b3a42d9ed099591e1ef | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
AFTER: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
ROW CAT:Oc7ea94f838a846016550 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放在我的手上。
AFTER: lang(Fox): 现在，把你的双手放在我的手上。
ROW CAT:O4939f2548afb40679b82 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
AFTER: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
CONTROL L10 cut(0.06): FenfenE01
CONTROL L11 rewind!
ROW CAT:O4056e2e0fffe6f8836bd | L12 | no manual edit
EN: As us Fenfen strove to rebuild our home and drive out the remnants of evil
BEFORE: lang(Fox): 当我们Fenfen努力重建家园、驱逐邪恶的残余势力时，
AFTER: lang(Fox): 当我们Fenfen努力重建家园、驱逐邪恶的残余势力时，
ROW CAT:O7ed730210da1321ffefa | L13 | no manual edit
EN: some of us looked up into the sky and saw a shooting star coming down.
BEFORE: lang(Fox): 我们当中有人仰望天空，看见一颗流星正向下坠落。
AFTER: lang(Fox): 我们当中有人仰望天空，看见一颗流星正向下坠落。
ROW CAT:O31085719ed6588717323 | L14 | no manual edit
EN: Perhaps Fate had sent us a hero, with which we could regain our peace?
BEFORE: lang(Fox): 或许是命运为我们送来了一位英雄，让我们能借助这位英雄重获安宁？
AFTER: lang(Fox): 或许是命运为我们送来了一位英雄，让我们能借助这位英雄重获安宁？
CONTROL L16 cut(0.06): FenfenE02
CONTROL L17 rewind!
ROW CAT:O8c032b357a3311e85516 | L18 | no manual edit
EN: Or perhaps Fate had a more sinister joke to play on us suffering Fenfen
BEFORE: lang(Fox): 又或许，命运还想对饱受苦难的我们Fenfen开一个更加阴险的玩笑，
AFTER: lang(Fox): 又或许，命运还想对饱受苦难的我们Fenfen开一个更加阴险的玩笑，
ROW CAT:O0d4b69ffb49b865152e8 | L19 | no manual edit
EN: for this visitor from the stars did not land on our planet proper...
BEFORE: lang(Fox): 因为这位来自群星的访客并没有降落在我们的星球本身……
AFTER: lang(Fox): 因为这位来自群星的访客并没有降落在我们的星球本身……
ROW CAT:Oc159e7e8d31729a94321 | L20 | no manual edit
EN: ...instead, they landed on the satellite rock that held Traeh's prison!
BEFORE: lang(Fox): ……而是降落在了那颗设有特蕾监牢的岩石卫星上！
AFTER: lang(Fox): ……而是降落在了那颗设有特蕾监牢的岩石卫星上！
CONTROL L22 cut(0.06): FenfenE03
CONTROL L23 rewind!
ROW CAT:Oe3885a501f819ab5b70c | L24 | no manual edit
EN: As if destined for only a single purpose, the interstellar interloper
BEFORE: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
AFTER: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
ROW CAT:Oc1f5ad2ac35cc0641dd8 | L25 | no manual edit
EN: made their way to the very core of Traeh's prison.
BEFORE: lang(Fox): 一路来到了特蕾监牢的最深处。 
AFTER: lang(Fox): 一路来到了特蕾监牢的最深处。 
ROW CAT:Odeb0228d78f7f9e2dc73 | L26 | no manual edit
EN: Had her psychic tendrils found their way into a poor fool's mind?
BEFORE: lang(Fox): 难道她的灵能触须已经伸进了某个可怜傻瓜的脑海？
AFTER: lang(Fox): 难道她的灵能触须已经伸进了某个可怜傻瓜的脑海？
CONTROL L28 cut(0.06): FenfenE04
CONTROL L29 rewind!
ROW CAT:O4173727f7c3cad086599 | L30 | EDIT E09-062
EN: There is no way to know if it was dark ESPer power at work or merely curiosity
BEFORE: lang(Fox): 究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇，已经无从知晓， 
AFTER: lang(Fox): 究竟是黑暗灵能在作祟，还是单纯出于好奇，已经无从知晓， 
ROW CAT:O4644dd8c37749ecd2f0b | L31 | no manual edit
EN: but this traveler made contact with the crystal prison that held Traeh...
BEFORE: lang(Fox): 但这位旅人触碰了囚禁特蕾的水晶监牢……
AFTER: lang(Fox): 但这位旅人触碰了囚禁特蕾的水晶监牢……
CONTROL L33 cut(0.06): FenfenE05
CONTROL L34 rewind!
ROW CAT:O178390dab078d70aa25a | L35 | no manual edit
EN: ...and so they became undone, unable to resist the dark ESPer forces.
BEFORE: lang(Fox): ……就这样，这位旅人无力抵抗黑暗的超能力者力量，最终沦陷了。
AFTER: lang(Fox): ……就这样，这位旅人无力抵抗黑暗的超能力者力量，最终沦陷了。
ROW CAT:Od30286b601f604e0a209 | L36 | no manual edit
EN: Power and pain coursed through the poor explorer
BEFORE: lang(Fox): 力量与痛苦流遍了这位可怜的探险者全身， 
AFTER: lang(Fox): 力量与痛苦流遍了这位可怜的探险者全身， 
ROW CAT:Oc9e699fe79ebe4dd8bb3 | L37 | no manual edit
EN: until their mind was no longer their own.
BEFORE: lang(Fox): 直到心智再也不属于自己。
AFTER: lang(Fox): 直到心智再也不属于自己。
CONTROL L39 cut(0.06): FenfenE06
CONTROL L40 rewind!
ROW CAT:Obbfd12f2bd3bbd0873e4 | L41 | no manual edit
EN: No, from that moment forth they answered to a darker power...
BEFORE: lang(Fox): 不，从那一刻起，这位旅人听命于一股更黑暗的力量……
AFTER: lang(Fox): 不，从那一刻起，这位旅人听命于一股更黑暗的力量……
ROW CAT:O543809c794607242ef96 | L42 | no manual edit
EN: They did as Traeh commanded!
BEFORE: lang(Fox): 特蕾吩咐什么，其便做什么！
AFTER: lang(Fox): 特蕾吩咐什么，其便做什么！
CONTROL L44 wait: 0.2
CONTROL L45 fadeout(1.0, 1.0, 4)
### P09-038 | action=apply
原问题：“黑暗的超能力者力量”不自然；保留动机不明，不以访客接触水晶推断故意受控。
本轮理由：只修不自然力量术语；源文动机无从确定保留，下一槽触碰水晶及暂名原样，不追加已定动机。
EDIT_IDS ["E09-062"]

## SC8a7eb1951fe9843f | nsfw | vsn/m_ClassicWerehund/script.vsn | vsn/m_ClassicWerehund/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L3 fade(9, 0, 1)
CONTROL L4 fadein(1.0, 4): YiffaiCloseupGrin
CONTROL L5 rewind!
ROW CAT:Oceff2422891220ec79d7 | L6 | no manual edit
EN: There we go! You must be related to that lil pupper running around here, huh?
BEFORE: text: 搞定！你肯定跟这附近乱跑的小狗崽有亲戚关系吧？
AFTER: text: 搞定！你肯定跟这附近乱跑的小狗崽有亲戚关系吧？
ROW CAT:O094db83d895b7fe94718 | L7 | no manual edit
EN: Doesn't matter if you're two or ten times the size as that little guy,
BEFORE: text: 不管你是那小家伙的两倍，还是十倍大，就没有我驯服不了的兽形——
AFTER: text: 不管你是那小家伙的两倍，还是十倍大，就没有我驯服不了的兽形——
ROW CAT:O7e5638a90e06bafce805 | L8 | no manual edit
EN: there isn't ANY feral that I can't ta-
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L10 fadecut(0.266, 2): ClassicAreaB01N
CONTROL L11 rewind!
ROW CAT:Oe23bfe0d4d2ef531a721 | L12 | no manual edit
EN: Ow what?? I thought you were down for the count!
BEFORE: text: 嗷，什么？！我以为你已经倒下了！
AFTER: text: 嗷，什么？！我以为你已经倒下了！
ROW CAT:O9d0e3ef172ced746bfce | L13 | no manual edit
EN: H-hey, wait a sec! Lemme get ready before y-you...
BEFORE: text: 喂、喂，等一下！让我准备好，你、你再……
AFTER: text: 喂、喂，等一下！让我准备好，你、你再……
CONTROL L15 fadecut(0.266, 2): ClassicAreaB01A
CONTROL L16 rewind!
CONTROL L17 sfxcue: ClassicAreaB01A {
CONTROL L18   play [ClassicYiffaiXSlap5] at [2]
CONTROL L19 }
ROW CAT:O79bfc9e8abb0a9623cad | L20 | no manual edit
EN: Gee, wow...!
BEFORE: text: 哇，天哪……！
AFTER: text: 哇，天哪……！
ROW CAT:Oab93d97691280de5c5c4 | L21 | no manual edit
EN: Ready to go without wasting any time, just like me huh?
BEFORE: text: 跟我一样，半点时间都不想浪费，随时能上，是吧？
AFTER: text: 跟我一样，半点时间都不想浪费，随时能上，是吧？
ROW CAT:O18506ed83e3c41ca99c7 | L22 | no manual edit
EN: It's almost like you were reading my mind...
BEFORE: text: 你简直像会读心一样……
AFTER: text: 你简直像会读心一样……
CONTROL L24 fadecut(0.266, 2): ClassicAreaB01BShort
CONTROL L25 rewind!
CONTROL L26 sfxcue: ClassicAreaB01BShort {
CONTROL L27   play [ClassicYiffaiXSlap8] at [4, 9, 14, 19]
CONTROL L28 }
ROW CAT:Oc71ad54e66c30560f293 | L29 | no manual edit
EN: Hey! Watch the claws! You don't have to hold onto me so tight.
BEFORE: text: 嘿！小心爪子！不用抓那么紧。
AFTER: text: 嘿！小心爪子！不用抓那么紧。
ROW CAT:O3d0b33ddeb5600286751 | L30 | no manual edit
EN: I've got a job to do too, so it's not like I'm going anywhere!
BEFORE: text: 我也有工作要做，又不会跑！
AFTER: text: 我也有工作要做，又不会跑！
ROW CAT:O88c9d4effa41aa79a1df | L31 | no manual edit
EN: HQ needs to know allll the details of what you're doing.
BEFORE: text: 总部得知道你行动的每——个细节。
AFTER: text: 总部得知道你行动的每——个细节。
CONTROL L33 fadecut(0.266, 2): ClassicAreaB01DShort
CONTROL L34 rewind!
CONTROL L35 sfxcue: ClassicAreaB01DShort {
CONTROL L36   play [ClassicYiffaiXSlap5] at [6]
CONTROL L37 }
ROW CAT:O4ce62c2666aef02fee07 | L38 | no manual edit
EN: Details like how you're barely even rutting me so far!
BEFORE: text: 比如你到现在都还没怎么干我！
AFTER: text: 比如你到现在都还没怎么干我！
ROW CAT:Oeda0fc1ad684f6a1d25b | L39 | no manual edit
EN: You feral canids always start off so small that you can barely poke in
BEFORE: text: 不管抽插得多快，你们兽形犬族起初总那么小，几乎都插不进去！
AFTER: text: 不管抽插得多快，你们兽形犬族起初总那么小，几乎都插不进去！
ROW CAT:Ofe2143dbdef970d0ef7c | L40 | no manual edit
EN: despite how fast you hump away!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L42 fadecut(0.266, 2): ClassicAreaB01EShort
CONTROL L43 rewind!
CONTROL L44 sfxcue: ClassicAreaB01EShort {
CONTROL L45   play [ClassicYiffaiXSlap7] at [1]
CONTROL L46 }
ROW CAT:Oc89256d39848f16878b5 | L47 | no manual edit
EN: Soon enough, your bulbus glandis will engorge and lock you inside me
BEFORE: text: 再过一会儿，你的龟头球就会胀大，把你锁在我体内，这样我就能观察你交配后的行为了。这很重要！
AFTER: text: 再过一会儿，你的龟头球就会胀大，把你锁在我体内，这样我就能观察你交配后的行为了。这很重要！
ROW CAT:O63eb76958698504d4f7e | L48 | no manual edit
EN: and I'll get to observe your post-coital behaviour. Very important!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O336d25e126a62d59a625 | L49 | no manual edit
EN: Aww, you're not getting embarrassed, are ya? You don't have to slow down!
BEFORE: text: 哎呀，你该不会害羞了吧？不用慢下来呀！
AFTER: text: 哎呀，你该不会害羞了吧？不用慢下来呀！
CONTROL L51 fadecut(0.266, 2): ClassicAreaB01B
CONTROL L52 rewind!
CONTROL L53 sfxcue: ClassicAreaB01B {
CONTROL L54   play [ClassicYiffaiXSlap8] at [2]
CONTROL L55 }
ROW CAT:O80114b5e074d66b09e3a | L56 | no manual edit
EN: Mmmf, guess you won't even even tie me properly after all. Canid types always
BEFORE: text: 嗯哼，看来你到底没法好好锁住我。犬族总是肉结一涨大，就停止抽插……
AFTER: text: 嗯哼，看来你到底没法好好锁住我。犬族总是肉结一涨大，就停止抽插……
ROW CAT:O46db857e9aca2e4c97bd | L57 | no manual edit
EN: stop thrusting once their knotty swells up...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oed4ff5471dc4225a4c91 | L58 | no manual edit
EN: ...hm?
BEFORE: text: ……嗯？
AFTER: text: ……嗯？
ROW CAT:O2e5c487a0144849c9fb1 | L59 | no manual edit
EN: Y-you're not cumming yet?
BEFORE: text: 你、你还不射吗？
AFTER: text: 你、你还不射吗？
CONTROL L61 fadecut(0.266, 2): ClassicAreaB01DDeep
CONTROL L62 rewind!
CONTROL L63 sfxcue: ClassicAreaB01DDeep {
CONTROL L64   play [ClassicYiffaiXSlap1] at [4]
CONTROL L65 }
ROW CAT:Oa44b21bce3204223fa2e | L66 | no manual edit
EN: W-woah, you're getting pretty large now...
BEFORE: text: 哇、哇哦，你现在变得好大……
AFTER: text: 哇、哇哦，你现在变得好大……
ROW CAT:Of27d490d115ede92b290 | L67 | no manual edit
EN: You're starting to... nnfgh... rub me in a good way, too...
BEFORE: text: 你也开始……嗯呃……磨得我很舒服了……
AFTER: text: 你也开始……嗯呃……磨得我很舒服了……
ROW CAT:Oee3b3d2d4009301f2c1e | L68 | no manual edit
EN: Did somebody else train you to do this or what?
BEFORE: text: 你这是跟谁学的，还是怎么着？
AFTER: text: 你这是跟谁学的，还是怎么着？
CONTROL L70 fadecut(0.266, 2): ClassicAreaB01E
CONTROL L71 rewind!
CONTROL L72 sfxcue: ClassicAreaB01E {
CONTROL L73   play [ClassicYiffaiXSlap7] at [1]
CONTROL L74 }
ROW CAT:Oc2d298dc237b67262e38 | L75 | no manual edit
EN: This isn't b-because of what I said, is it?
BEFORE: text: 该不会是因、因为我刚才说的话吧？ 
AFTER: text: 该不会是因、因为我刚才说的话吧？ 
ROW CAT:O3399aa875e5fa3ce0dcd | L76 | no manual edit
EN: Y-you don't have to try impress me! HQ might get suspicious, even.
BEFORE: text: 你、你不用费劲给我留好印象！总部说不定还会起疑。
AFTER: text: 你、你不用费劲给我留好印象！总部说不定还会起疑。
ROW CAT:O2a484a0501f04e0b1967 | L77 | no manual edit
EN: Falsifying data is a huge no-no for us Cosmobreeders!
BEFORE: text: 对我们宇宙育种者来说，伪造数据可是大忌！
AFTER: text: 对我们宇宙育种者来说，伪造数据可是大忌！
CONTROL L79 fadecut(0.266, 2): ClassicAreaB01O
CONTROL L80 rewind!
CONTROL L81 sfxcue: ClassicAreaB01O {
CONTROL L82   play [ClassicYiffaiXBlink1] at [4]
CONTROL L83 }
ROW CAT:O3f771d9790e27628914e | L84 | no manual edit
EN: Wait, w-wait wait a s-sec...
BEFORE: text: 等、等、等一下……
AFTER: text: 等、等、等一下……
ROW CAT:Ofd5cca2217c915d3f0a8 | L85 | no manual edit
EN: ...are you getting even larger? Oh my gosh...
BEFORE: text: ……你还在变大？天哪……
AFTER: text: ……你还在变大？天哪……
ROW CAT:O0a6c2481d57e01ca767d | L86 | no manual edit
EN: That... this... no way...! Slow down!
BEFORE: text: 那……这……不行……！慢点！
AFTER: text: 那……这……不行……！慢点！
CONTROL L88 fadecut(0.266, 2): ClassicAreaB01DDeep2
CONTROL L89 rewind!
CONTROL L90 sfxcue: ClassicAreaB01DDeep2 {
CONTROL L91   play [ClassicYiffaiXSlap1] at [3]
CONTROL L92 }
ROW CAT:Oa1b9d5ad0cbd882536b9 | L93 | no manual edit
EN: Down boy! Down! You're getting too rough with the...
BEFORE: text: 趴下，乖狗！趴下！你对我的……太粗暴了……
AFTER: text: 趴下，乖狗！趴下！你对我的……太粗暴了……
ROW CAT:O563802fa7813f303ca5a | L94 | no manual edit
EN: ...with the...!!
BEFORE: text: ……对我的……！！
AFTER: text: ……对我的……！！
CONTROL L96 sync!
CONTROL L97 queue: ClassicAreaB01D3DeepToCum
CONTROL L98 sfxcue: ClassicAreaB01D3DeepToCum {
CONTROL L99   play [ClassicYiffaiXSlap1] at [3, 11, 15, 19]
CONTROL L100     play [ClassicYiffaiXTwitch2] at [22, 24, 30, 34, 38, 42]
CONTROL L101   play [ClassicYiffaiXShoot1] at [46]
CONTROL L102 }
CONTROL L104 sync!
CONTROL L105 queue: ClassicAreaB01D2Cum
CONTROL L106 rewind!
CONTROL L107 sfxcue: ClassicAreaB01D2Cum {
CONTROL L108   play [ClassicYiffaiXTwitch2] at [6, 24]
CONTROL L109   play [ClassicYiffaiXShoot1] at [17]
CONTROL L110 }
ROW CAT:Of76ec8ae153c195f0526 | L111 | no manual edit
EN: ...o-ow...!
BEFORE: text: ……好、好痛……！
AFTER: text: ……好、好痛……！
ROW CAT:Ocf0804d027c518ca22b1 | L112 | no manual edit
EN: I... I thought your knot was a-already fully out before, b-but...
BEFORE: text: 我……我以为你的结刚才就、就已经全胀起来了，可、可是……
AFTER: text: 我……我以为你的结刚才就、就已经全胀起来了，可、可是……
ROW CAT:O31efe67420c12a1857cc | L113 | no manual edit
EN: B-but my butt... wow...
BEFORE: text: 可、可我的屁股……哇……
AFTER: text: 可、可我的屁股……哇……
CONTROL L115 fadecut(0.266, 2): ClassicAreaB01H
CONTROL L116 rewind!
ROW CAT:O86473f75c3c34b5d5f7e | L117 | no manual edit
EN: A-at least now you can say that we t-tied, unlike during the fight.
BEFORE: text: 至、至少现在算扯平了……还真“结”住了，不像刚才那场架。
AFTER: text: 至、至少现在算扯平了……还真“结”住了，不像刚才那场架。
ROW CAT:O99b85a5e7d47c79efad3 | L118 | no manual edit
EN: If we have a rematch and I don't hold back, will you hump me even harder
BEFORE: text: 要是再打一场，我不留手，你会操我操得更狠，还是说，野兽先生，你会招架不住我呢？
AFTER: text: 要是再打一场，我不留手，你会操我操得更狠，还是说，野兽先生，你会招架不住我呢？
ROW CAT:O6b3f838051caaeb86efa | L119 | no manual edit
EN: or would I be too much for you, Mister Feral?
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L121 fadecut(0.266, 2): ClassicAreaB01J
CONTROL L122 rewind!
ROW CAT:Oa1a5a2668f3f2ff2e746 | L123 | no manual edit
EN: [My young friend, if we have a rematch it'll be very unfortunate]
BEFORE: text: [年轻的朋友，再比一场可就不妙了。]
AFTER: text: [年轻的朋友，再比一场可就不妙了。]
ROW CAT:O6173ee7556168d7d9c63 | L124 | no manual edit
EN: [as a father, I have much experience play fighting with you little pups]
BEFORE: text: [身为父亲，我很有陪你们这些小狗崽打闹的经验]
AFTER: text: [身为父亲，我很有陪你们这些小狗崽打闹的经验]
ROW CAT:O9e76ab7828cdcc7fb19a | L125 | no manual edit
EN: [and merely needed to ascertain your character.]
BEFORE: text: [只不过需要确认一下你的为人。]
AFTER: text: [只不过需要确认一下你的为人。]
ROW CAT:Oe818ad7864f6005a1221 | L126 | no manual edit
EN: [For now, witness a fraction of what I can do!]
BEFORE: text: [现在，先见识一下我力量的冰山一角吧！]
AFTER: text: [现在，先见识一下我力量的冰山一角吧！]
CONTROL L128 sync!
CONTROL L129 queue: ClassicAreaB01J2
CONTROL L130 sfxcue: ClassicAreaB01J2 {
CONTROL L131   play [YiffaiPsyAbility] at [4]
CONTROL L132 }
CONTROL L134 sync!
CONTROL L135 fadecut(0.266, 2): ClassicAreaB01H2
CONTROL L136 rewind!
ROW CAT:Oe5406ff742022480c674 | L137 | no manual edit
EN: ...?!?
BEFORE: text: ……？！？
AFTER: text: ……？！？
ROW CAT:Oe24b72142091815e510c | L138 | no manual edit
EN: ...bark?!??!
BEFORE: text: ……汪？！？！
AFTER: text: ……汪？！？！
ROW CAT:Oa1ed80c76f803c9f1ef4 | L139 | no manual edit
EN: [That's right, Yiffai. You have indeed become a feral yourself.]
BEFORE: text: [没错，伊法伊。你自己也变成野兽了。]
AFTER: text: [没错，伊法伊。你自己也变成野兽了。]
ROW CAT:Oef2f0ab571fa00870596 | L140 | no manual edit
EN: [A feral much the same size as my son whom you ruffhoused with earlier.]
BEFORE: text: [一只兽形犬，大小跟你先前打闹过的我儿子差不多。]
AFTER: text: [一只兽形犬，大小跟你先前打闹过的我儿子差不多。]
ROW CAT:O91778a3649d8cb4eaf92 | L141 | no manual edit
EN: [The Zener power that flows though me allows me to transform at will]
BEFORE: text: [我体内流淌的泽纳之力，能让我随意变形。]
AFTER: text: [我体内流淌的泽纳之力，能让我随意变形。]
ROW CAT:O9b51e888932a1f2970dd | L142 | no manual edit
EN: [and now that you've taken my seed, so too shall you have the power!]
BEFORE: text: [如今你接下了我的精种，也将拥有这力量！]
AFTER: text: [如今你接下了我的精种，也将拥有这力量！]
CONTROL L144 fadecut(0.266, 2): ClassicAreaB01F
CONTROL L145 rewind!
ROW CAT:Of16666f0a7e1ce7d55f6 | L146 | no manual edit
EN: [Let us put your new form through its paces, shall we?]
BEFORE: text: [来试试你这副新身体的能耐，如何？]
AFTER: text: [来试试你这副新身体的能耐，如何？]
ROW CAT:O2515de83ea04a6e720b6 | L147 | EDIT E09-063
EN: [I believe you wanted a rematch, though I fear you would not enjoy it.]
BEFORE: text: [吾记得汝想再战一回，只怕汝不会喜欢。]
AFTER: text: [我记得你想再比一场，不过恐怕你不会喜欢。]
ROW CAT:O797a51aafb8183c329a2 | L148 | no manual edit
EN: [...perhaps your rump could appreciate a "rematch" of sorts, however...]
BEFORE: text: [……不过，你的屁股或许会喜欢另一种“再战”……]
AFTER: text: [……不过，你的屁股或许会喜欢另一种“再战”……]
CONTROL L150 fadecut(0.266, 2): ClassicAreaBlackAnimation
CONTROL L151 rewind!
CONTROL L152 sfxcue: ClassicAreaBlackAnimation {
CONTROL L153   play [ClassicYiffaiXSlap3] at [6]
CONTROL L154 }
ROW CAT:O019228a2a5cdada95e32 | L155 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O38288d0f80647d97ea21 | L156 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:O1c929395857827afbf93 | L157 | no manual edit
EN: ...*whine*...
BEFORE: text: ……*呜咽*……
AFTER: text: ……*呜咽*……
CONTROL L159 fadecut(0.266, 2): ClassicAreaB01Q
CONTROL L160 rewind!
ROW CAT:O99da62618466c662ace7 | L161 | no manual edit
EN: O-okay, I can turn back now... o-ow...
BEFORE: text: 好、好了，我能变回来了……疼、疼……
AFTER: text: 好、好了，我能变回来了……疼、疼……
ROW CAT:O00c4f7439c07fb0fe836 | L162 | no manual edit
EN: Time to continue d-dominating... ow...
BEFORE: text: 该继续征、征服了……疼……
AFTER: text: 该继续征、征服了……疼……
ROW CAT:Od5f3558e30433373cad0 | L163 | no manual edit
EN: ...dominating all the creatures down here...
BEFORE: text: ……征服这里所有的生物……
AFTER: text: ……征服这里所有的生物……
CONTROL L165 sync!
CONTROL L166 queue: ClassicAreaB01QToQ2
CONTROL L168 sync!
CONTROL L169 queue: ClassicAreaB01Q2
CONTROL L170 rewind!
ROW CAT:Ob6ab0d19459125c866cb | L171 | no manual edit
EN: You're sure that yellow dog man is the chosen one, papa?
BEFORE: text: 爸爸，你确定那个黄毛狗人就是天选之人？
AFTER: text: 爸爸，你确定那个黄毛狗人就是天选之人？
ROW CAT:O7fa660582e14adce91c8 | L172 | no manual edit
EN: That's right, son.
BEFORE: text: 没错，儿子。
AFTER: text: 没错，儿子。
CONTROL L174 fadecut(0.266, 2): ClassicAreaB01R
CONTROL L175 rewind!
ROW CAT:Oe69f5b1c9c623d8b51bf | L176 | no manual edit
EN: That man, Yiffai, mastered one of the Zener powers in record time
BEFORE: text: 那位伊法伊，以破纪录的速度掌握了一种泽纳之力，所以我毫不怀疑，解放这星球的人就是他。
AFTER: text: 那位伊法伊，以破纪录的速度掌握了一种泽纳之力，所以我毫不怀疑，解放这星球的人就是他。
ROW CAT:O9e81fe3e7f5e060990c5 | L177 | no manual edit
EN: so I have no doubt that he will be the one to set this planet free.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O9bf0cdb0f60877e51979 | L178 | no manual edit
EN: That sounds so cool! He's a real superhero, isn't he dad?
BEFORE: text: 听起来太酷了！爸爸，他是真正的超级英雄，对吧？
AFTER: text: 听起来太酷了！爸爸，他是真正的超级英雄，对吧？
ROW CAT:Ob7ec43e923749f1620d6 | L179 | no manual edit
EN: I wish I could train with him next time. Can I dad? Can I??
BEFORE: text: 真希望下次能跟他训练。可以吗，爸爸？可以吗？？
AFTER: text: 真希望下次能跟他训练。可以吗，爸爸？可以吗？？
CONTROL L181 fadecut(0.266, 2): Black
CONTROL L182 rewind!
ROW CAT:O0df0cad53275c58b0e81 | L183 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:Of843d7458e52815a2868 | L184 | no manual edit
EN: ...maybe when you're older, son.
BEFORE: text: ……等你再大些吧，儿子。
AFTER: text: ……等你再大些吧，儿子。
CONTROL L186 fadeout(1.0, 1.0, 4)
### P09-039 | action=apply
原问题：同一父亲连续发言突然“吾汝”与前后现代语域脱节；此处不是Pigobin古语分支，不搬其文风。
本轮理由：仅撤除Werehund父亲孤立吾汝，保留有礼与调侃；这不是禁止Pigobin原有古语。
EDIT_IDS ["E09-063"]

