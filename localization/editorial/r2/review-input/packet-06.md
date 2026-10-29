# packet-06 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SC46a2115bf1481b1d | nsfw | datadf/all.ds | AreaC_MacsenDark.TazerRapier
CONTROL L1200 <AreaC_MacsenDark.TazerRapier>
ROW CAT:Of24f9a210926a61138ed | L1201 | no manual edit
EN: This is a pretty little elven letter opener, if I do say so myself!
BEFORE:   * 要我自己说，这可是一把精巧的精灵拆信刀！
AFTER:   * 要我自己说，这可是一把精巧的精灵拆信刀！
ROW CAT:O8e6665cfd503d0ced752 | L1202 | EDIT E06-001
EN: Feather light, just like how those dresses the elves craft will make you feel.
BEFORE:   * 轻得像羽毛，就像精灵们缝的那些裙子会让你感觉的那样。
AFTER:   * 轻得像羽毛，就跟穿上精灵缝的裙子一样轻盈。
ROW CAT:Oc852ffa3ecfea8166aa0 | L1203 | EDIT E06-002
EN: ...not that I would know anything about those!
BEFORE:   * ……那些裙子我一点都不了解！
AFTER:   * ……当然，那些裙子我可一点都不了解！
### P06-001 | action=apply
原问题：当前“就像……会让你感觉的那样”照搬从句，末句僵硬否认也削弱说漏嘴后的掩饰；重写整段保留轻盈比较和嘴硬，不认定商人的实际穿衣经历。
本轮理由：比较句应自然表达穿裙般轻盈，末句保留说漏嘴后的否认，不坐实穿衣经历。
EDIT_IDS ["E06-001", "E06-002"]

## SC69cf1fb9619b4227 | nsfw | datadf/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1713 <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1714   if { !f(ctx_maxed_any_pet_affinity) } {
ROW CAT:O8988e9c955b5e1662588 | L1715 | no manual edit
EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
BEFORE:     * 一定要给宠物一点关爱，并且好好喂它们！
AFTER:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW CAT:O24802e5dd74f0347e94f | L1716 | EDIT E06-003
EN: AFTER YOU'VE MAXXXED OUT AN AFFINITY, RETURN HERE FOR A SPECIAL REWARD.
BEFORE:     * 在你把一项亲密度MAXXXED到顶之后，回到这儿领一份特殊奖励。
AFTER:     * 把任意一只宠物的亲密度提升到最高，再回来领特别奖励。
CONTROL L1717   } else {
ROW CAT:O855a59c5a1c97f9bbd97 | L1718 | no manual edit
EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
BEFORE:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
AFTER:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW CAT:Ob0c580a571e9cf616874 | L1719 | EDIT E06-004
EN: JUST PET THEM WHILE THEY'RE AT MAX AFFINITY TO CHARGE THE CRYSTAL.
BEFORE:     * 只要在它们处于MAX亲密度时抚摸它们，就能给水晶充能。
AFTER:     * 只要在亲密度最高时抚摸它们，就能给水晶充能。
ROW CAT:Of3ec5506319e3159db81 | L1720 | no manual edit
EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
BEFORE:     * 每种生物给的力量都不同！都试试！
AFTER:     * 每种生物给的力量都不同！都试试！
CONTROL L1721   }
CONTROL L1723 ### shared ###
### P06-002 | action=apply
原问题：MAXXXED与MAX属于可译的程度，不是按键或资源ID；“一项亲密度”未把对象说清。建议分支分别使用对应短段，不把前后两个条件合成同次对话。
本轮理由：MAXXXED/MAX 是亲密度程度而非受保护命令；按原两个条件分支分别回填。
EDIT_IDS ["E06-003", "E06-004"]

## SC26dbe5fa7ee9cf03 | nsfw | datadf/all.ds | BossuDex.ClassicCannonWallC
CONTROL L3186 <BossuDex.ClassicCannonWallC>
ROW CAT:O6085643e2cb911f52bd9 | L3187 | EDIT E06-005
EN: [BOSSU, ARE THERE CANNONS STRONGER OR AM I WEAKER?]
BEFORE:   Yiffany: [波苏，是有更强的加农炮，还是我变弱了？]
AFTER:   Yiffany: [波苏，是这里的炮变强了，还是我变弱了？]
ROW CAT:O2ff91ac76b961e33d981 | L3188 | no manual edit
EN: [THESE CANNONS SEEM TO HAVE GONE A WHILE WITHOUT]
BEFORE:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
AFTER:   Bossu: [这些加农炮似乎已经有一段时间不需要自行修复了。]
ROW CAT:O81eaef6035131acf7d2a | L3189 | no manual edit
EN: [NEEDING TO BE SELF- REPAIRED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O80688506ec4fc937df37 | L3190 | no manual edit
EN: [CONSEQUENTLY THEY SEEM TO BE FIRING AT HIGHER POWER.]
BEFORE:   Bossu: [因此它们似乎正以更高的功率发射。]
AFTER:   Bossu: [因此它们似乎正以更高的功率发射。]
ROW CAT:O329f01983cd242f0b182 | L3191 | EDIT E06-006
EN: [GREEAAAAAT, JUST WHAT I NEEDED TO DEAL WITH...]
BEFORE:   Yiffany: [太——好了，正好是我需要应付的……]
AFTER:   Yiffany: [太——好了，还嫌麻烦不够多是吧……]
### P06-003 | action=apply
原问题：首问there疑为their源拼写异常，但中文可据后续these还原此处炮台比较；末句just what I needed是反讽抱怨，当前“正好是我需要应付的”落点生硬。建议保留seem，不加具体修复耗能机理。
本轮理由：后文 these 支持眼前炮台的比较；只修首问与反讽，保留原有自修解释及 seem。
EDIT_IDS ["E06-005", "E06-006"]

## SC11c65e57ae93baff | sfw | datadf/all.ds | Mauser.AreaB_map29_a noselect
CONTROL L2322 <Mauser.AreaB_map29_a noselect>
ROW SFW3c51dfd9670c87e373fac823 | L2323 | no manual edit
EN: [O-OW... MAUSER, COME IN.]
BEFORE:   Yiffany: [哎、哎哟……毛瑟，请回话。]
AFTER:   Yiffany: [哎、哎哟……毛瑟，请回话。]
ROW SFW2082432ad465844f8cfc0f12 | L2324 | no manual edit
EN: [MAUSER ORDERS IN... WHAT?]
BEFORE:   Yiffany: [毛瑟，请回答……什么？]
AFTER:   Yiffany: [毛瑟，请回答……什么？]
ROW SFW0693da2300425e8c045100d7 | L2325 | no manual edit
EN: [WHAT DID YOU NEED ASSISTANCE WITH, AGENT?] 
BEFORE:   Mauser: [你需要什么协助，特工？] 
AFTER:   Mauser: [你需要什么协助，特工？] 
ROW SFWb086899430b90cd5f72b482e | L2326 | no manual edit
EN: [I JUST WANTED TO ANALYZE THE DATA ON THAT LAST CREATURE]
BEFORE:   Yiffany: [我只是想分析一下最后那只生物的数据，这样我就能看出它是怎么让我变——成那样的。]
AFTER:   Yiffany: [我只是想分析一下最后那只生物的数据，这样我就能看出它是怎么让我变——成那样的。]
ROW SFW7b32c54db9c62e11d856c573 | L2327 | no manual edit
EN: [SO I COULD SEE HOW THEY MADE ME TRANS- FORM LIKE THAT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWda04d75df925ec74b0c3d76e | L2328 | no manual edit
EN: [TRANSFORM? WHAT ARE YOU TALKING ABOUT?]
BEFORE:   Mauser: [变形？你在说什么？]
AFTER:   Mauser: [变形？你在说什么？]
ROW SFW20f30447bda5c62828f011d0 | L2329 | no manual edit
EN: [THE SATELLITE  STOPPED TRANSMITTING DATA UNTIL JUST NOW]
BEFORE:   Tomcat: [那颗卫星直到刚才才恢复数据传输。]
AFTER:   Tomcat: [那颗卫星直到刚才才恢复数据传输。]
ROW SFW22ae0111da15a899e32914f1 | L2330 | no manual edit
EN: [PROBABLY DUE TO A SOLAR FLARE UP OR SOMESUCH]
BEFORE:   Tomcat: [大概是太阳耀斑之类的闹的]
AFTER:   Tomcat: [大概是太阳耀斑之类的闹的]
ROW SFW2dd1ebdda5c0cce928ded51a | L2331 | no manual edit
EN: [BUT WHAT'S THIS ABOUT... TRANSFORMING?]
BEFORE:   Tomcat: [不过你说的变形……是怎么回事？]
AFTER:   Tomcat: [不过你说的变形……是怎么回事？]
ROW SFW078083afebce43eac587a3ef | L2332 | no manual edit
EN: [THERE'S NO DATA SHOWING UP ON OUR END.]
BEFORE:   Mauser: [我们这边什么数据都没收到。]
AFTER:   Mauser: [我们这边什么数据都没收到。]
ROW SFW590c582c950e3849f0a3bd8d | L2333 | no manual edit
EN: [YOU SURE YOU DIDN'T JUST TAKE A ROUGH BUMP TO THE HEAD?]
BEFORE:   Mauser: [你确定不是脑袋刚被狠狠磕了一下？]
AFTER:   Mauser: [你确定不是脑袋刚被狠狠磕了一下？]
ROW SFW33a919047307e1959a98f304 | L2334 | no manual edit
EN: [I... WELL... YOU SEE....]
BEFORE:   Yiffany: [我……那个……你看嘛……]
AFTER:   Yiffany: [我……那个……你看嘛……]
ROW SFW1234d291bfc8daf76ef5dc1f | L2335 | no manual edit
EN: [NEVERMIND, FORGET I SAID ANYTHING.]
BEFORE:   Yiffany: [算了，当我什么都没说。]
AFTER:   Yiffany: [算了，当我什么都没说。]
ROW SFW39e257a8a03073cfeb070afc | L2336 | no manual edit
EN: [ALRIGHT, IF YOU SAY SO GIRL.]
BEFORE:   Tomcat: [行吧，你都这么说了姑娘。]
AFTER:   Tomcat: [行吧，你都这么说了姑娘。]
ROW SFWccf489e9cd2020328cd7ebae | L2337 | no manual edit
EN: [IF YOU'RE FEELING UP FOR IT, MAYBE YOU SHOULD HEAD EAST]
BEFORE:   Tomcat: [要是你还有精神，也许该往东边走]
AFTER:   Tomcat: [要是你还有精神，也许该往东边走]
ROW SFWe32af325b5c561369821ce45 | L2338 | no manual edit
EN: [WE JUST GOT A LOAD OF AGENT DISTRESS BEACONS FROM THERE.]
BEFORE:   Tomcat: [我们刚从那边收到一大堆特工的求救信标。]
AFTER:   Tomcat: [我们刚从那边收到一大堆特工的求救信标。]
ROW SFW201d515c8d1b36dd32504d6a | L2339 | no manual edit
EN: [HEAD TO THE EAST, GOT IT! YIFFANY OUT.]
BEFORE:   Yiffany: [往东边走，收到！伊法妮通话结束。]
AFTER:   Yiffany: [往东边走，收到！伊法妮通话结束。]
### P06-004 | action=defer
原问题：源句MAUSER ORDERS IN... WHAT?本身突兀且speaker为Yiffany，可能是故意复述/听错，也可能源异常；当前简化为再次呼叫丢失orders字面内容。需对照原JAR演出或音讯语境再定，不能凭NSFW对应场景删除本行。
本轮理由：源句 MAUSER ORDERS IN... WHAT? 与说话人、上下文的关系仍未获得演出证据；不能以另一内容版替换或删除。
EDIT_IDS []

## SCcbbefc7a63e6bd3c | nsfw | datadf/all.ds | Mauser.AreaC_map64_a noselect
CONTROL L2407 <Mauser.AreaC_map64_a noselect>
ROW CAT:O899141955aefe1d24c63 | L2408 | no manual edit
EN: [AGENT YIFFANY YIFFAI, COME IN.]
BEFORE:   Mauser: [特工伊法妮·伊法伊，请回话。]
AFTER:   Mauser: [特工伊法妮·伊法伊，请回话。]
ROW CAT:O63f4033ad42b131392d6 | L2409 | no manual edit
EN: [PROCEED WITH CAUTION, YIFFANY. WE'VE DETECTED...]
BEFORE:   Bossu: [请谨慎前进，伊法妮。我们探测到……]
AFTER:   Bossu: [请谨慎前进，伊法妮。我们探测到……]
ROW CAT:Of7e769d7086cfa4c0880 | L2410 | no manual edit
EN: [...ODD READINGS UP AHEAD.]
BEFORE:   Bossu: [……前方有异常读数。]
AFTER:   Bossu: [……前方有异常读数。]
ROW CAT:O07de952874c8567ec67e | L2411 | EDIT E06-007
EN: [WHAT DO YOU MEAN?]
BEFORE:   Yiffany: [你什么意思？]
AFTER:   Yiffany: [什么异常？]
ROW CAT:Of590992955d0fe782b50 | L2412 | no manual edit
EN: [WELL, NOT TO ALARM YOU... BUT...]
BEFORE:   Mauser: [嗯，不是要吓你……但是……]
AFTER:   Mauser: [嗯，不是要吓你……但是……]
ROW CAT:Oe58ce2f31ad70bbfb297 | L2413 | no manual edit
EN: [THERE SEEMS TO BE ANOTHER AGENT IN THE AREA.]
BEFORE:   Bossu: [这片区域里似乎还有另一名特工。]
AFTER:   Bossu: [这片区域里似乎还有另一名特工。]
ROW CAT:O3e2a6e069e410f66444e | L2414 | EDIT E06-008
EN: [AND THEY'VE BEEN MOVING ABOUT. FREELY.]
BEFORE:   Bossu: [而且他们一直在四处移动。自由地。]
AFTER:   Bossu: [而且对方一直在四处活动。行动不受限制。]
ROW CAT:O86b07077dd5ef649ab48 | L2415 | no manual edit
EN: [ANOTHER AGENT...]
BEFORE:   Yiffany: [另一名特工……]
AFTER:   Yiffany: [另一名特工……]
ROW CAT:Ob83e80b143bd0c54587f | L2416 | EDIT E06-009
EN: [WE'RE STILL TRYING TO HAIL THEM, BUT... WELL...]
BEFORE:   Mauser: [我们仍在尝试呼叫他们，但是……嗯……]
AFTER:   Mauser: [我们还在尝试呼叫对方，但是……嗯……]
ROW CAT:O8b488727c1bc9785c678 | L2417 | EDIT E06-010
EN: [NOW IT LOOKS LIKE THEIR RADIO HAS BEEN TURNED OFF.]
BEFORE:   Mauser: [而现在看来他们的无线电已经被关掉了。]
AFTER:   Mauser: [现在看来，对方的无线电已经关了。]
ROW CAT:Oeed0eb0be33f195f12a4 | L2418 | no manual edit
EN: [ONCE AGAIN, PROCEED WITH CAUTION, AGENT.]
BEFORE:   Bossu: [再次提醒，谨慎前进，特工。]
AFTER:   Bossu: [再次提醒，谨慎前进，特工。]
### P06-005 | action=apply
原问题：单一未知agent被反复译“他们”，且“自由地”孤立作补语不自然；核心是其他探员被捕时这位却能自由行动。改“对方”避免提前确定身份、性别和关机主体；末句也可保守译“对方的无线电已经关了”。
本轮理由：another agent 为单一身份未知者；用对方避免误译复数或提前揭身份，保留看来的不确定性。
EDIT_IDS ["E06-007", "E06-008", "E06-009", "E06-010"]

## SC30bbe99d4389a0bf | nsfw | datadf/all.ds | Tomcat.Area0_First_CosmoCard noselect
CONTROL L2088 <Tomcat.Area0_First_CosmoCard noselect>
ROW CAT:O3b725c800402875740df | L2089 | no manual edit
EN: [NICE! I DIDN'T KNOW YOU STILL COLLECTED COSMOCARDS!]
BEFORE:   Tomcat: [不错！我不知道你还在收集宇宙卡！]
AFTER:   Tomcat: [不错！我不知道你还在收集宇宙卡！]
ROW CAT:O44f65dc2df9317027b3a | L2090 | no manual edit
EN: [I DON'T! BUT IT SEEMS LIKE SOME DWEEB DROPPED ONE.]
BEFORE:   Yiffany: [我才不收！不过好像有个窝囊废掉了一张。]
AFTER:   Yiffany: [我才不收！不过好像有个窝囊废掉了一张。]
ROW CAT:Of5c8b5d91a32f42d4cfa | L2091 | no manual edit
EN: [AND IT LOOKS CONVENIENTLY LIKE SOME LOCAL FAUNA.]
BEFORE:   Yiffany: [而且碰巧长得像本地的某种动物。]
AFTER:   Yiffany: [而且碰巧长得像本地的某种动物。]
ROW CAT:Oc6d9bbb9042c30b5c9d4 | L2092 | no manual edit
EN: [THAT'S GREAT! OPEN YOUR P.A.W. TO THE COSMOCARD MENU]
BEFORE:   Tomcat: [太好了！打开你的 P.A.W.，进到宇宙卡菜单，你应该就能把卡片翻过来，这样就能提前知道你会怎么被干-]
AFTER:   Tomcat: [太好了！打开你的 P.A.W.，进到宇宙卡菜单，你应该就能把卡片翻过来，这样就能提前知道你会怎么被干-]
ROW CAT:O4d3aa06e1816074353d8 | L2093 | no manual edit
EN: [AND YOU SHOULD BE ABLE TO FLIP THE CARDS OVER]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O84062cf7bd225a6c75b1 | L2094 | no manual edit
EN: [WHICH WILL GIVE YOU A HEADS UP ON HOW YOU'LL BE FU-]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oebae81baa4cc1dc47c2e | L2095 | no manual edit
EN: [OH WOW IS THAT A TUTONE COSMOCARD? FOR REAL, AGENT?]
BEFORE:   Mauser: [哦哇，那是图托恩宇宙卡？真的吗，特工？]
AFTER:   Mauser: [哦哇，那是图托恩宇宙卡？真的吗，特工？]
ROW CAT:O653dfc5e38749fd4174a | L2096 | no manual edit
EN: [THOSE ARE PROLLY WORTH BIG CREDITS WHEN YOU RETURN]
BEFORE:   Mauser: [等你回去，那些大概值不少信用点，当然也会有对你任务有用的信息！]
AFTER:   Mauser: [等你回去，那些大概值不少信用点，当然也会有对你任务有用的信息！]
ROW CAT:O92cb5826b9fa5a52b92f | L2097 | no manual edit
EN: [AND OF COURSE WILL HAVE USEFUL INFO FOR YOUR MISSION!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O732b1c21b1cef85dffb5 | L2098 | no manual edit
EN: [NO DOUBT, SQUEAKS. YOU KNOW, TOMCAT IS A HUGE FAN]
BEFORE:   Yiffany: [那还用说，小吱吱。你知道，汤姆猫也超喜欢宇宙卡。你们俩何不聊聊这个？]
AFTER:   Yiffany: [那还用说，小吱吱。你知道，Tomcat也超喜欢宇宙卡。你们俩何不聊聊这个？]
ROW CAT:O7a5ff5a67be4f3d85dd1 | L2099 | no manual edit
EN: [OF COSMOCARDS TOO. WHY DON'T YOU TWO CHAT ABOUT EM?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc5994a9d0cec9ec3311e | L2100 | no manual edit
EN: [REALLY TOMCAT? I DIDN'T KNOW! LEMME GET MY COLLECTION]
BEFORE:   Mauser: [真的吗，汤姆猫？我不知道！我去拿我的收藏]
AFTER:   Mauser: [真的吗，Tomcat？我不知道！我去拿我的收藏]
ROW CAT:O8163db088c8c2df5cff6 | L2101 | no manual edit
EN: [I'VE GOT COMPLETE SETS OF MULTIPLE PLANETARY SYSTEMS-]
BEFORE:   Mauser: [我有好几个行星系的完整套装-]
AFTER:   Mauser: [我有好几个行星系的完整套装-]
ROW CAT:O0cfa5bde1146fdd6ecea | L2102 | no manual edit
EN: [AHHH, WELL... THAT SOUNDS... LIKE REAL FUN...]
BEFORE:   Tomcat: [啊，这个……听起来……真有意思……]
AFTER:   Tomcat: [啊，这个……听起来……真有意思……]
ROW CAT:O8aae634319d54de552e6 | L2103 | no manual edit
EN: [THANKS FOR HOOKING US UP, GRRRL...]
BEFORE:   Tomcat: [谢你牵线，丫头……]
AFTER:   Tomcat: [谢你牵线，丫头……]
ROW CAT:Oe9067aa09e6d84db3485 | L2104 | EDIT E06-011
EN: [ANYTIME, HAVE A NICE CARD DATE! TEEHEE!]
BEFORE:   Yiffany: [随时奉陪，卡片约会愉快！嘻嘻！]
AFTER:   Yiffany: [不客气，祝你们的卡片约会愉快！嘻嘻！]
### P06-006 | action=apply
原问题：Anytime回应同事“谢你牵线”，不是承诺自己随时参与约会；“随时奉陪”把应答转成自身参加，打乱两人被凑对的笑点。
本轮理由：Anytime 是回应牵线致谢，不是主角加入约会；保留凑对笑话。
EDIT_IDS ["E06-011"]

## SCfd1dd9245ceeeff1 | sfw | datadf/all.ds | Tomcat.Area0_First_CosmoCard noselect
CONTROL L2084 <Tomcat.Area0_First_CosmoCard noselect>
ROW SFWba809af5f62cbfb0c013e4d1 | L2085 | no manual edit
EN: [NICE! I DIDN'T KNOW YOU STILL COLLECTED COSMOCARDS!]
BEFORE:   Tomcat: [不错！我不知道你还在收集宇宙卡！]
AFTER:   Tomcat: [不错！我不知道你还在收集宇宙卡！]
ROW SFW03c7b421760c19721d6b3472 | L2086 | no manual edit
EN: [I DON'T! BUT IT SEEMS LIKE SOME DWEEB DROPPED ONE.]
BEFORE:   Yiffany: [我才不收！不过好像有个窝囊废掉了一张。]
AFTER:   Yiffany: [我才不收！不过好像有个窝囊废掉了一张。]
ROW SFW39d21229f3dbc18e6cb779ce | L2087 | no manual edit
EN: [AND IT LOOKS CONVENIENTLY LIKE SOME LOCAL FAUNA.]
BEFORE:   Yiffany: [而且碰巧长得像本地的某种动物。]
AFTER:   Yiffany: [而且碰巧长得像本地的某种动物。]
ROW SFWf880bf0863f2e007dcc1137a | L2088 | no manual edit
EN: [THAT'S GREAT! OPEN YOUR P.A.W. TO THE COSMOCARD MENU]
BEFORE:   Tomcat: [太好了！打开你的 P.A.W.，进到宇宙卡菜单]
AFTER:   Tomcat: [太好了！打开你的 P.A.W.，进到宇宙卡菜单]
ROW SFWaf72ec8688ee9e2899e1af8e | L2089 | no manual edit
EN: [AND YOU CAN TAKE A LOOK AT THEM.]
BEFORE:   Tomcat: [你就可以查看它们了。]
AFTER:   Tomcat: [你就可以查看它们了。]
ROW SFWd401ee8df0d5bd9214f3df74 | L2090 | no manual edit
EN: [THOSE ARE PROLLY WORTH BIG CREDITS WHEN YOU RETURN]
BEFORE:   Mauser: [等你回去，那些大概值不少信用点，当然也会有对你任务有用的信息！]
AFTER:   Mauser: [等你回去，那些大概值不少信用点，当然也会有对你任务有用的信息！]
ROW SFWee44951435629331020a23af | L2091 | no manual edit
EN: [AND OF COURSE WILL HAVE USEFUL INFO FOR YOUR MISSION!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW7e830c661f8d307913b9bfea | L2092 | no manual edit
EN: [NO DOUBT, SQUEAKS. YOU KNOW, TOMCAT IS A HUGE FAN]
BEFORE:   Yiffany: [那还用说，小吱吱。你知道，汤姆猫也超喜欢宇宙卡。你们俩何不聊聊这个？]
AFTER:   Yiffany: [那还用说，小吱吱。你知道，Tomcat也超喜欢宇宙卡。你们俩何不聊聊这个？]
ROW SFWb614481e0a33640b10e056f3 | L2093 | no manual edit
EN: [OF COSMOCARDS TOO. WHY DON'T YOU TWO CHAT ABOUT EM?]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWaefbd7d92aa28b42d8a165d3 | L2094 | no manual edit
EN: [REALLY TOMCAT? I DIDN'T KNOW! LEMME GET MY COLLECTION]
BEFORE:   Mauser: [真的吗，汤姆猫？我不知道！我去拿我的收藏]
AFTER:   Mauser: [真的吗，Tomcat？我不知道！我去拿我的收藏]
ROW SFW8fd4fd0bf1769764df4d3e61 | L2095 | no manual edit
EN: [I'VE GOT COMPLETE SETS OF MULTIPLE PLANETARY SYSTEMS-]
BEFORE:   Mauser: [我有好几个行星系的完整套装-]
AFTER:   Mauser: [我有好几个行星系的完整套装-]
ROW SFWf8d482e808178dbc687d17df | L2096 | no manual edit
EN: [AHHH, WELL... THAT SOUNDS... LIKE REAL FUN...]
BEFORE:   Tomcat: [啊，这个……听起来……真有意思……]
AFTER:   Tomcat: [啊，这个……听起来……真有意思……]
ROW SFWd41d7b3ce1be925a7a46a58d | L2097 | no manual edit
EN: [THANKS FOR HOOKING US UP, GRRRL...]
BEFORE:   Tomcat: [谢你牵线，丫头……]
AFTER:   Tomcat: [谢你牵线，丫头……]
ROW SFW531cc65eb7f4b72497d5aa18 | L2098 | EDIT E06-012
EN: [ANYTIME, HAVE A NICE CARD DATE! TEEHEE!]
BEFORE:   Yiffany: [随时奉陪，卡片约会愉快！嘻嘻！]
AFTER:   Yiffany: [不客气，祝你们的卡片约会愉快！嘻嘻！]
### P06-007 | action=apply
原问题：SFW独立场景中同样是在回应牵线致谢；保留本版未含成人卡背说明的结构，不与NSFW通话合并。
本轮理由：SFW 本版同样是回应牵线致谢，独立处理，不引入成人卡背内容。
EDIT_IDS ["E06-012"]

## SCa95fc07f154b4282 | sfw | datadf/all.ds | Tomcat.KoboPickup noselect noamendfreq
CONTROL L3735 <Tomcat.KoboPickup noselect noamendfreq>
ROW SFW6806ccdb7f0dc3b27f443e0a | L3736 | no manual edit
EN: [HELLO? OH! YOU AREN'T YIFFANY!]
BEFORE:   Tomcat: [喂？哦！你不是伊法妮！]
AFTER:   Tomcat: [喂？哦！你不是伊法妮！]
ROW SFW73278dff7c93fd2eb47620ec | L3737 | no manual edit
EN: [DID THAT GRRRL REALLY GET BEATEN UP BY SOME KOBOS]
BEFORE:   Tomcat: [那姑娘真被几只狗头人打败了，]
AFTER:   Tomcat: [那姑娘真被几只狗头人打败了，]
ROW SFW7af2be641cc852e5821d0598 | L3738 | EDIT E06-013
EN: [AND LOSE HER RADIO... YET AGAIN...]
BEFORE:   Tomcat: [又把收音机弄丢了……又一次……]
AFTER:   Tomcat: [又把无线电弄丢了……又一次……]
ROW SFW8421c222b3946fc833591068 | L3739 | no manual edit
EN: [...?!]
BEFORE:   Yiffany: [……？！]
AFTER:   Yiffany: [……？！]
ROW SFW43666f97e4b7ec27b2ed407e | L3740 | no manual edit
EN: [HOPE SHE FINDS IT AGAIN ONCE SHE COMES AROUND, SERIOUSLY]
BEFORE:   Tomcat: [说真的，希望她醒过来之后能再找到它。]
AFTER:   Tomcat: [说真的，希望她醒过来之后能再找到它。]
ROW SFW8a996a93019c9029f0d58880 | L3741 | no manual edit
EN: [...]
BEFORE:   Yiffany: [……]
AFTER:   Yiffany: [……]
### P06-008 | action=apply
原问题：当前“收音机”把可双向联络的任务radio说成单向收音设备；此处Tomcat误以为Kobo捡走通讯器。保留误认，不将台词改成已认出主角。
本轮理由：本场正在双向通话且误认对方捡到通讯设备，故无线电更准确；不据收音机一词自动判 A 类，也不改误认事实。
EDIT_IDS ["E06-013"]

## SCf17f3e7ace13c492 | nsfw | datadf/all.ds | TomcatItems.SpecialKeycard4
CONTROL L4313 <TomcatItems.SpecialKeycard4>
ROW CAT:O568359b36c79daa60a0b | L4314 | no manual edit
EN: [IN ORDER TO USE A KEYCARD, ALL YOU HAVE TO DO IS]
BEFORE:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
AFTER:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
ROW CAT:O24109df10e74505b50de | L4315 | no manual edit
EN: [WALK INTO AN ENERGY DOOR WHILE HOLDING ONE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obd59153df257ac321a56 | L4316 | no manual edit
EN: [YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!]
BEFORE:   Tomcat: [你能打开等级不超过门上所标数字的门！]
AFTER:   Tomcat: [你能打开等级不超过门上所标数字的门！]
### P06-009 | action=defer
原问题：本行源文them可指keycards或doors，字面“门上所标等级以内的门”成为自指，当前照译后无法说明门卡权限。本包同女线SpecialKeycard1已说明门终端是最低需求且高卡兼开低门。须核4级卡实际触发/显示对象，若them指卡建议“拿着门卡走进能量门就能开门；门的等级不超过门卡等级就行。”不能在本轮直接覆写源歧义。
本轮理由：them 的实际显示对象仍未核明；其他门卡说明不足以证明本处显示及触发对象，保留待核。
EDIT_IDS []

## SCa84ca531944c6858 | sfw | datadf/all.ds | TomcatItems.TazerPirate
CONTROL L4059 <TomcatItems.TazerPirate>
ROW SFW88e4d430628163cc46bda805 | L4060 | no manual edit
EN: [CHECK OUT THIS PIRATE TAZER, TOMCAT!]
BEFORE:   Yiffany: [快看这把海盗电击枪，汤姆猫！]
AFTER:   Yiffany: [快看这把海盗电击枪，Tomcat！]
ROW SFW26e5f4cab637454f86d039bb | L4061 | EDIT E06-014
EN: [WELL. THAT ONE DEFINITELY WOULDN'T PASS SPEC IN ANY]
BEFORE:   Tomcat: [嗯。这把在这个象限的任何系统里都绝对过不了规格。不过应急倒能用。]
AFTER:   Tomcat: [嗯。这把在这个象限的任何星系都过不了规格检验。不过应急倒能用。]
ROW SFW468ac7de16832e79dae71638 | L4062 | no manual edit
EN: [SYSTEM IN THIS QUADRANT. USEFUL IN A PINCH, THOUGH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWfa6d9bd1bbc44df82ff9be7c | L4063 | no manual edit
EN: [HEY, AS LONG AS IT DOESN'T EXPLODE ON ME!]
BEFORE:   Yiffany: [嘿，只要别在我手里炸掉就行！]
AFTER:   Yiffany: [嘿，只要别在我手里炸掉就行！]
ROW SFW0ef92582d6bc60c1e796a99e | L4064 | no manual edit
EN: [YEAH YOU CAN TAKE THAT RISK, NOT ME...]
BEFORE:   Tomcat: [行，你可以去冒这个险，我可不干……]
AFTER:   Tomcat: [行，你可以去冒这个险，我可不干……]
### P06-010 | action=apply
原问题：system为星系/辖属地域而非电脑系统，pass spec是符合规格；“任何系统里过不了规格”失去科技装备说明的自然表达。保留口语评估，不额外宣称具体违法条款。
本轮理由：quadrant 内的 system 在此是星系地域，pass spec 是通过规格检验；保留应急用途。
EDIT_IDS ["E06-014"]

## SC17d46a70f789c0a9 | nsfw | datadm/all.ds | Area0_Macsen1.Talk.hornets
CONTROL L66 <Area0_Macsen1.Talk.hornets>
ROW CAT:O5b01695aa91e9065af63 | L67 | EDIT E06-015
EN: If you find a radio out there, remember:
BEFORE:   * 要是在外面找到收音机，记住：在物品菜单里按SELECT就能使用收音机！
AFTER:   * 要是在外面找到无线电，记住：在物品菜单里按SELECT就能使用它！
ROW CAT:O62ab8003942a693c9bd7 | L68 | no manual edit
EN: Press SELECT in the item menu to use your radio!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P06-011 | action=apply
原问题：有SELECT使用提示且进入通讯系统，当前“收音机”错误限定为广播接收机；SELECT保留，不改按键。
本轮理由：物品菜单 SELECT 使用与上下文通讯设备相符；改称无线电但不凭该词夸大为严重误译，不增按键或功能。
EDIT_IDS ["E06-015"]

## SC1d927b426a0e5fa4 | nsfw | datadm/all.ds | Bossu.Area0_map10_a noselect noamendfreq
CONTROL L2006 <Bossu.Area0_map10_a noselect noamendfreq>
ROW CAT:Of8e35bbc4295b2bf6619 | L2007 | no manual edit
EN: [GOOD JOB SHOWING THAT MONSTER WHAT FOR, YIFFAI!]
BEFORE:   Bossu: [干得好，让那只怪物知道了厉害，伊法伊！]
AFTER:   Bossu: [干得好，让那只怪物知道了厉害，伊法伊！]
ROW CAT:O0da9425790ed4eeb70da | L2008 | no manual edit
EN: [THANKS! IT WAS NOTHING, REALLY!]
BEFORE:   Yiffai: [谢谢！这真的不算什么！]
AFTER:   Yiffai: [谢谢！这真的不算什么！]
ROW CAT:O62bb857afbda8b1eb6f2 | L2009 | no manual edit
EN: [EXCELLENT SHOW OF FORCE, BUT MAYBE YOU SHOULD]
BEFORE:   Bossu: [出色的武力展示，但也许你下次该把重点放在数据采集上。]
AFTER:   Bossu: [出色的武力展示，但也许你下次该把重点放在数据采集上。]
ROW CAT:Oc6afa04d3d28b34907c6 | L2010 | no manual edit
EN: [FOCUS ON DATA COLLECTION NEXT TIME.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od00964fe255c6771c86e | L2011 | EDIT E06-016
EN: [H-HEY! I JUST DON'T KNOW MY OWN STRENGTH!]
BEFORE:   Yiffai: [嘿-嘿！我就是不知道自己的力气有多大！]
AFTER:   Yiffai: [喂、喂！我只是没掌握好自己的力气！]
ROW CAT:O61d2b4824b8b3c980cfb | L2012 | EDIT E06-017
EN: [DON'T GET CAUGHT UP IN THE HEAT OF THE MOMENT]
BEFORE:   Bossu: [别被一时的热劲卷住]
AFTER:   Bossu: [别一时冲动就打昏了头。]
ROW CAT:O5dce2318c05ef968ed05 | L2013 | no manual edit
EN: [PRIORITIZE DATA COLLECTION IN YOUR NEXT ENCOUNTER.]
BEFORE:   Bossu: [下次遭遇时优先做数据采集。]
AFTER:   Bossu: [下次遭遇时优先做数据采集。]
ROW CAT:O89b96c25e307c5fe326d | L2014 | no manual edit
EN: [UNDERSTOOD, BOSSU! I WON'T LET YOU DOWN.]
BEFORE:   Yiffai: [明白，Bossu！我不会让你失望。]
AFTER:   Yiffai: [明白，Bossu！我不会让你失望。]
ROW CAT:Oa6d11b8a0dc25131cbc4 | L2015 | EDIT E06-018
EN: [GOOD BOY, LOOKING FORWARD TO SEEING THAT DATA!]
BEFORE:   Bossu: [好男孩，期待看到那份数据！]
AFTER:   Bossu: [好小子，期待看到那份数据！]
ROW CAT:Of735a180f72f63093247 | L2016 | no manual edit
EN: [IF YOU COME ACROSS ANY NEW CREATURES, FEEL FREE TO]
BEFORE:   Bossu: [如果你碰上任何新生物，尽管用频率27.850呼叫我。]
AFTER:   Bossu: [如果你碰上任何新生物，尽管用频率27.850呼叫我。]
ROW CAT:O830094b1449b8213c1e4 | L2017 | no manual edit
EN: [GIVE ME A CALL AT FREQUENCY 27.850.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4e066a473c3e2b9aef8e | L2018 | no manual edit
EN: [OH AND DON'T FORGET TO EQUIP YOUR NEW GEAR. OVER!]
BEFORE:   Bossu: [哦，还有，别忘了把新装备装上。完毕！]
AFTER:   Bossu: [哦，还有，别忘了把新装备装上。完毕！]
ROW CAT:Ob31df43cd88f8778dff1 | L2019 | EDIT E06-019
EN: [GEEZE I KNOW THAT, I AIN'T NO PUP...]
BEFORE:   Yiffai: [哎呀我知道，我才不是Pup...]
AFTER:   Yiffai: [知道了，我又不是小狗崽……]
### P06-012 | action=apply
原问题：H-HEY是急辩口吃，不是“嘿嘿”笑声；heat of moment是上头冲动，不是“热劲卷住”；末尾Pup未译使嘴硬回应失去落点。全段建议保持各人和频率节点，不按段落平均回填。
本轮理由：H-HEY 是急辩而非笑声，heat of the moment 是冲动，Pup 是本句犬类调侃；不把成年主角全局幼儿化，保留频率及原空槽。
EDIT_IDS ["E06-016", "E06-017", "E06-018", "E06-019"]

## SC8a64100509cd1232 | nsfw | datadm/all.ds | BossuDex.ClassicElf
CONTROL L3263 <BossuDex.ClassicElf>
ROW CAT:Oa299621be2e312a2d893 | L3264 | EDIT E06-020
EN: [THE ELVES OF SCEAFYA MAY ALL BE FEMALE]
BEFORE:   Bossu: [斯凯菲亚的精灵也许全是雌性，但她们并不全是不朽的。]
AFTER:   Bossu: [斯凯菲亚的精灵虽说全是雌性，却并不个个长生不老。]
ROW CAT:O9c1a9aa8e10289020dfc | L3265 | no manual edit
EN: [BUT THEY AREN'T ALL IMMORTAL.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O82887b0dca5cb11914c2 | L3266 | EDIT E06-021
EN: [AS THEY CAN BREED WITH ANY MALE OF ANY SPECIES]
BEFORE:   Bossu: [由于她们能与任何物种的任何雄性繁殖，她们便带上了越来越多的有朽特征。]
AFTER:   Bossu: [她们能与任何物种的雄性繁衍，因此逐渐带上了更多凡俗生物的特征。]
ROW CAT:O31be82e0e4a06e00e94d | L3267 | no manual edit
EN: [THEY'VE TAKEN ON MORE AND MORE MORTAL CHARACTERISTICS]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O304cc576325be34a1edd | L3268 | EDIT E06-022
EN: [WAIT, SO THAT MEANS SOME OF THEM *ARE* IMMORTAL?]
BEFORE:   Yiffai: [等等，所以这意味着她们中有些*是*不朽的？]
AFTER:   Yiffai: [等等，也就是说，她们中有些*真能*长生不老？]
ROW CAT:Ob0b3a83a351d58834c4b | L3269 | EDIT E06-023
EN: [INDEED, AS FAR AS WE CAN TELL.]
BEFORE:   Bossu: [的确，就我们所能看出的而言。]
AFTER:   Bossu: [没错，至少据我们目前所知是这样。]
ROW CAT:O0a069f5c33cb886cd2ee | L3270 | no manual edit
EN: [ANY ELF THAT IS OUT IN THE OPEN AND ENGAGING IN COMBAT]
BEFORE:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
AFTER:   Bossu: [任何一个在开阔处并且正在交战的精灵，无疑会是个年幼者。顶多一百岁。]
ROW CAT:O8325dc1136b8e0effa18 | L3271 | no manual edit
EN: [WILL NO DOUBT BE A YOUNGSTER. A HUNDRED YEARS OLD AT MOST.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7d2c4c6f4ef59a866e47 | L3272 | no manual edit
EN: [THAT'S... WOW...]
BEFORE:   Yiffai: [这……哇……]
AFTER:   Yiffai: [这……哇……]
ROW CAT:Oe38b2b70784cc3df5a55 | L3273 | EDIT E06-024
EN: [DON'T GIVE IN TO AWE. YOU'LL NEED TO BE ON YOUR TOES]
BEFORE:   Bossu: [别向敬畏屈服。你得保持警觉，以便击退那些年幼精灵的攻击。]
AFTER:   Bossu: [别光顾着惊叹。打起精神，才能挡住那些年轻精灵的攻击。]
ROW CAT:O7005f10b43f2f4051064 | L3274 | no manual edit
EN: [IN ORDER TO REPEL THE YOUNG ELVES' ATTACKS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O976d2e35aa12aa3e3ee6 | L3275 | no manual edit
EN: [RIGHT, GOTTA FOCUS.]
BEFORE:   Yiffai: [对，得专注。]
AFTER:   Yiffai: [对，得专注。]
### P06-013 | action=apply
原问题：may all be female在may...but结构作让步，不是独立不确定“也许全是雌性”；当前把让步误作概率。“有朽特征”“所能看出的而言”不自然。结论仍归Bossu资料，不宣称世界全知真理。
本轮理由：may...but 是让步；保留繁衍因果及总部知识边界，不把说辞升级全知事实。
EDIT_IDS ["E06-020", "E06-021", "E06-022", "E06-023"]
### P06-014 | action=apply
原问题：give in to awe在此是制止看呆、提醒战斗，当前“别向敬畏屈服”语域与上下句不接。保留警觉与防御目的，不增加侮辱或敌意。
本轮理由：提醒从惊叹回到战斗警觉，非向敬畏屈服；只修合句头并保留防御目的。
EDIT_IDS ["E06-024"]

## SC12557c972d930ead | nsfw | datadm/all.ds | DefeatHints.ClassicWerehund.transform
CONTROL L4863 <DefeatHints.ClassicWerehund.transform>
ROW CAT:O7cf6920b6d6e44368d47 | L4864 | EDIT E06-025
EN: DARN, YOUR HEALTH JUST DROPPED
BEFORE:   Tomcat: 可恶，你的生命值掉下来了
AFTER:   Tomcat: 糟了，你的生命值刚掉下去了。
ROW CAT:Oe159343ea8b60fff8a8a | L4865 | EDIT E06-026
EN: YOU THINK YOU CAN GET UP?
BEFORE:   Tomcat: 你以为你还能站起来吗？
AFTER:   Tomcat: 你还能站起来吗？
ROW CAT:Od4342181aec8b05370c5 | L4866 | no manual edit
EN: AGENT, DON'T FORGET TO OBSERVE
BEFORE:   Bossu: 特工，别忘了观察你的对手。
AFTER:   Bossu: 特工，别忘了观察你的对手。
ROW CAT:O80600f740723472ad1b0 | L4867 | no manual edit
EN: YOUR ADVERSARY.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O719249cd1c3b11818d44 | L4868 | no manual edit
EN: TAKE NOTE OF IMPORTANT CUES
BEFORE:   Bossu: 留意重要线索，以及可以进攻而不会招致反击的时机！
AFTER:   Bossu: 留意重要线索，以及可以进攻而不会招致反击的时机！
ROW CAT:O2996ec02f63a86a84acc | L4869 | no manual edit
EN: AND TIME WHERE YOU CAN ATTACK
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O74625e180bfb6e64e15d | L4870 | no manual edit
EN: WITHOUT REPERCUSSION!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P06-015 | action=apply
原问题：关切伤情、询问是否能起身，被译“你以为你还能站起来吗”成威胁或嘲讽；同场后续Bossu提供战术提示，明确是支援语境。
本轮理由：连续支援场景询问能否起身，是关切而非嘲讽；分别保留两个非空槽，不擅加方括号。
EDIT_IDS ["E06-025", "E06-026"]

## SC2c035a06b63b51a3 | nsfw | datadm/all.ds | Gitgud.Tip6
CONTROL L3387 <Gitgud.Tip6>
ROW CAT:O9353b7f70cf5c0ae23cc | L3388 | EDIT E06-027
EN: [PLENTY OF FOODS OUT THERE WILL HEAL YOU A BIT]
BEFORE:     Gitgud: [外面有不少食物能治疗你一点，有些甚至会提升你的属性！]
AFTER:     Gitgud: [外头不少食物都能帮你回点血，有些甚至能提升属性！]
ROW CAT:Oe34e4dc85c04e7f74f68 | L3389 | no manual edit
EN: [AND SOME WILL EVEN RAISE YOUR STATS!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc22baa07ce223597822d | L3390 | EDIT E06-028
EN: [STOCK UP IF SOME BEAST IS GIVING YOU A HARD TIME.]
BEFORE:     Gitgud: [如果某只野兽让你吃不消，就多囤一些。]
AFTER:     Gitgud: [要是有哪只野兽让你吃不消，就多备点吃的。]
### P06-016 | action=apply
原问题：“治疗你一点”是英语宾语结构硬搬；教程需自然说明恢复与备粮，不把吃不消扩大为强制购买。
本轮理由：恢复生命及备粮用自然教程语言，保留属性提升和条件，不追加必须购买。
EDIT_IDS ["E06-027", "E06-028"]

## SCd14e021c6ca16c23 | nsfw | datadm/all.ds | Hacker_Shared.Meeting
CONTROL L4969 <Hacker_Shared.Meeting>
ROW CAT:O52909c720e43010faa0b | L4970 | EDIT E06-029
EN: Greetings, Yiffai. You don't know me, but I kinda snooped your satlink.
BEFORE:   * 你好，伊法伊。你不认识我，不过我有点偷看了你的卫星链路。
AFTER:   * 你好，伊法伊。你不认识我，不过我偷偷窥探了你的卫星通讯。
ROW CAT:O90af7e4a58483015f82f | L4971 | no manual edit
EN: So I've actually been watching you for a while, and I have a proposition...
BEFORE:   * 所以其实我已经观察你有一阵子了，我有个提议……
AFTER:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:Oa61a078198bc4a8bf661 | L4972 | EDIT E06-030
EN: It's simple: You bring me those fancy chips you find out there,
BEFORE:   * 很简单：你把在外头找到的那些花哨芯片带给我，我就替你黑开门！显然，这是双赢！
AFTER:   * 很简单：把你在外头找到的那些高级芯片带给我，我就替你破解门锁！这不是双赢嘛！
ROW CAT:Oe84a9ddc8afbed7d9c71 | L4973 | no manual edit
EN: and I'll hack open doors for you! It's a win-win, obviously!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P06-017 | action=apply
原问题：“有点偷看了”逐词追随kinda，中文搭配不成立；snoop satlink对应私自接入/窥探通讯，不是目视查看链路。按共享黑客身份范围，不扩认所有测试黑客为The0。
本轮理由：snoop satlink 指窥探通讯；只按共享黑客场景修口语，不强认所有黑客身份。
EDIT_IDS ["E06-029", "E06-030"]

## SC5952f8f6e6829e90 | sfw | datadm/all.ds | TomcatItems.SpecialLeftmark
CONTROL L4211 <TomcatItems.SpecialLeftmark>
ROW SFW140cb0237451286b77c0ee20 | L4212 | no manual edit
EN: [OOOOOH, HOW YOU FEELING? YOUR BODY TEMP JUST SPIKED!]
BEFORE:   Tomcat: [哦哟，感觉如何？你体温突然飙升了！]
AFTER:   Tomcat: [哦哟，感觉如何？你体温突然飙升了！]
ROW SFW20664a50ae6da4f849fbeb5c | L4213 | no manual edit
EN: [I...I'M FINE...I THINK?] 
BEFORE:   Yiffai: [我……我没事……大概吧？] 
AFTER:   Yiffai: [我……我没事……大概吧？] 
ROW SFWecf9e33c519b2bdba500660f | L4214 | EDIT E06-031
EN: [I RAN INTO THIS GLOWING ORB AND IT LEFT A MARK ON ME.]
BEFORE:   Yiffai: [我碰到个球体，它在我身上留了个印记。]
AFTER:   Yiffai: [我碰到个发光的球体，它在我身上留了个印记。]
ROW SFWc9e3ffdd1983d4b56142fb90 | L4215 | no manual edit
EN: [MAYBE THAT HAS SOMETHING TO DO WITH THE ESPERS!]
BEFORE:   Tomcat: [说不定那跟超能力者有关！]
AFTER:   Tomcat: [说不定那跟超能力者有关！]
ROW SFW0eaf84cbb54279017ce1b11b | L4216 | no manual edit
EN: [ESPERS??]
BEFORE:   Yiffai: [超能力者？？]
AFTER:   Yiffai: [超能力者？？]
ROW SFWa2981d8ec429dc93c73e936d | L4217 | no manual edit
EN: [YEAH, THE PREVIOUS AGENTS LEFT BEHIND CLUES THAT THERE]
BEFORE:   Tomcat: [对，之前的特工留下的线索表明，这颗星球很久以前住着有超能力的生物。]
AFTER:   Tomcat: [对，之前的特工留下的线索表明，这颗星球很久以前住着有超能力的生物。]
ROW SFW43b497549e518a800f42cdae | L4218 | no manual edit
EN: [WERE BEINGS WITH ESP ON THAT PLANET LONG AGO.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWde0c5e76569214524f9029c1 | L4219 | no manual edit
EN: [THESE ESP SENSITIVE BEINGS, THE ESPERS, SURELY LEFT BEHIND]
BEFORE:   Tomcat: [这些拥有超感知觉的超能力者，肯定留下了一些古代科技！]
AFTER:   Tomcat: [这些拥有超感知觉的超能力者，肯定留下了一些古代科技！]
ROW SFW9e525fbee46f66842f2447d8 | L4220 | no manual edit
EN: [SOME OF THEIR ANCIENT TECHNOLOGY!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWe9cdc4a27090bc866b6719ac | L4221 | no manual edit
EN: [NOW THAT YOU MENTION IT, I DO FEEL STRONGER...]
BEFORE:   Yiffai: [你这么一说，我确实感觉更强了……]
AFTER:   Yiffai: [你这么一说，我确实感觉更强了……]
ROW SFW793682254aed8f7cfe37a129 | L4222 | no manual edit
EN: [IF YOU FIND ANY MORE ARTIFACTS, GIVE ME A HOLLER]
BEFORE:   Tomcat: [再找到什么遗物，就叫我一声，咱们一起解开这个谜团！]
AFTER:   Tomcat: [再找到什么遗物，就叫我一声，咱们一起解开这个谜团！]
ROW SFWf09f577c7b4f267caaaeb3cb | L4223 | no manual edit
EN: [AND WE CAN TRY TO SOLVE THIS MYSTERY TOGETHER!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
### P06-018 | action=apply
原问题：glowing明确可观察特征，当前丢失“发光”；该特征承接识别古代科技的后文，不宜删。
本轮理由：补回明确可见的 glowing，不添球体来源或机制。
EDIT_IDS ["E06-031"]

## SC91728abf50d61496 | nsfw | datav/dictionary.json | ui.breeding.Swiper.affinity
ROW CAT:O344fbbecf283cd4ece14 | L- | no manual edit
EN: THE SWIPER STUDIOUSLY AVOIDS|YOUR GAZE. YOU MIGHT AS WELL|NOT EXIST AT ALL...
BEFORE: 挥爪刻意避开|你的目光。你简直|像根本不存在……
AFTER: 挥爪刻意避开|你的目光。你简直|像根本不存在……
ROW CAT:O3dc237c9c664f79fca52 | L- | EDIT E06-032
EN: THE SWIPER PURRS POLITELY,|SHEATHING HIS MURDER MITTENS|AT YOUR APPROACH.
BEFORE: 挥爪礼貌地呼噜，|在你走近时收起|他的凶器肉垫。
AFTER: 挥爪客气地打着呼噜，|在你走近时收起|那双凶器般的利爪。
ROW CAT:O657ede64cc4a6c786575 | L- | no manual edit
EN: THE SWIPER CURLS HIS TAIL|INTO A QUESTION MARK, AS IF|ASKING YOU 'WHAT NOW?'
BEFORE: 挥爪把尾巴卷成|问号，仿佛在问你|'现在怎样？'
AFTER: 挥爪把尾巴卷成|问号，仿佛在问你|'现在怎样？'
ROW CAT:Od4bc3a9bd7fdb6af2b4a | L- | no manual edit
EN: THE SWIPER GREETS YOU WITH|A LOW, ADORABLE MEOW.|WHAT A WONDERFUL PET!
BEFORE: 挥爪用一声低低的、|可爱的喵迎接你。|真是棒极了的宠物！
AFTER: 挥爪用一声低低的、|可爱的喵迎接你。|真是棒极了的宠物！
### P06-019 | action=apply
原问题：murder mittens是对猫爪的幽默称法，sheathe为收爪；当前“收起凶器肉垫”像把肉垫收进身体。保留礼貌地收敛威胁的亲密度变化，不把整组状态合成一次动作。
本轮理由：murder mittens 为猫爪戏称；保留礼貌呼噜、靠近时收爪及三段 |，不添乖顺事件。
EDIT_IDS ["E06-032"]

## SC635055d78e091a5c | nsfw | datav/dictionary.json | ui.card.CosmoCardEnelye
ROW CAT:Oc436cd4d89a84d7abc0f | L- | no manual edit
EN: ENELYE   <ALPHA>
BEFORE: 恩莉耶  <阿尔法>
AFTER: 恩莉耶  <阿尔法>
### P06-020 | action=defer
原问题：本包同名Enelye在男线裙子通话为“恩内莉”，卡名及卡文为“恩莉耶”，女线失败C末尾又“恩内莉”。是同一原名的可追踪不一致，但本轮参照未终裁正式译名；请统一专名裁决后按身份与语境处理，暂不强选一个新译名。
本轮理由：同名译法确有不一致，但 Enelye 正式译名尚未裁决，不擅选译名。
EDIT_IDS []

## SC60978b8144431f79 | nsfw | datay/scripts_pack.json | /shops/female/Area0_Macsen1/products/2/displayName
ROW CAT:Oc8ef4bea4cf2538b81c0 | L- | no manual edit
EN: OLD JUNK
BEFORE: 旧货铺
AFTER: 旧货铺
### P06-021 | action=defer
原问题：该键明确位于shops/female/Area0_Macsen1/products/2/displayName，是商品名称；“旧货铺”把商品译成店铺。建议仅在商品字段写“旧杂货/旧货”，不改变店名或资源键。
本轮理由：OLD JUNK 所在嵌套商品字段的运行用途未证；可能是商品、交互入口或其他显示用途，不能只凭路径断定并强修。
EDIT_IDS []

## SCcf4e44e2dba4cfa6 | nsfw | vsn/f_AgentFZ5/script.vsn | vsn/f_AgentFZ5/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Female
CONTROL L4 rewind!
ROW CAT:O837d3f6056708de41762 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
AFTER: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW CAT:O150ca55d6cf87f5bc6ef | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放到我的手上。
AFTER: lang(Fox): 现在，把你的双手放到我的手上。
ROW CAT:Occ32ce6151696339e0d3 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
AFTER: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L10 cut(0.06): FenfenE01
CONTROL L11 rewind!
ROW CAT:Oe3f4e96c21e036dba02c | L12 | no manual edit
EN: As us Fenfen strove to rebuild our home and drive out the remnants of evil
BEFORE: lang(Fox): 当我们Fenfen奋力重建家园、驱逐邪恶残部时，
AFTER: lang(Fox): 当我们Fenfen奋力重建家园、驱逐邪恶残部时，
ROW CAT:O85711e688db6f81f0c99 | L13 | no manual edit
EN: some of us looked up into the sky and saw a shooting star coming down.
BEFORE: lang(Fox): 我们中有些人仰望天空，看见一颗流星正坠落而下。
AFTER: lang(Fox): 我们中有些人仰望天空，看见一颗流星正坠落而下。
ROW CAT:Ocbfe548689a476fad50c | L14 | no manual edit
EN: Perhaps Fate had sent us a hero, with which we could regain our peace?
BEFORE: lang(Fox): 也许是命运给我们派来了一位英雄，好让我们重获和平？
AFTER: lang(Fox): 也许是命运给我们派来了一位英雄，好让我们重获和平？
CONTROL L16 cut(0.06): FenfenE02
CONTROL L17 rewind!
ROW CAT:O8355fe3a8493c7b781c7 | L18 | no manual edit
EN: Or perhaps Fate had a more sinister joke to play on us suffering Fenfen
BEFORE: lang(Fox): 又或许，命运对受苦的我们Fenfen还有更阴险的玩笑要开，
AFTER: lang(Fox): 又或许，命运对受苦的我们Fenfen还有更阴险的玩笑要开，
ROW CAT:Oaf650d8d4960d3312844 | L19 | no manual edit
EN: for this visitor from the stars did not land on our planet proper...
BEFORE: lang(Fox): 因为这位来自群星的访客，并没有降落在星球本体上……
AFTER: lang(Fox): 因为这位来自群星的访客，并没有降落在星球本体上……
ROW CAT:O8f18520fa7b2fd54193f | L20 | no manual edit
EN: ...instead, they landed on the satellite rock that held Traeh's prison!
BEFORE: lang(Fox): ……而是落在了关押特蕾的囚牢所在的那座卫星岩上！
AFTER: lang(Fox): ……而是落在了关押特蕾的囚牢所在的那座卫星岩上！
CONTROL L22 cut(0.06): FenfenE03
CONTROL L23 rewind!
ROW CAT:O1ae550cc3b1225e51f81 | L24 | no manual edit
EN: As if destined for only a single purpose, the interstellar interloper
BEFORE: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
AFTER: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
ROW CAT:O67dc68ea520b452279e3 | L25 | no manual edit
EN: made their way to the very core of Traeh's prison.
BEFORE: lang(Fox): 一路来到了关押特蕾的囚牢核心。 
AFTER: lang(Fox): 一路来到了关押特蕾的囚牢核心。 
ROW CAT:O46d2c3f9a420ccf5adcd | L26 | no manual edit
EN: Had her psychic tendrils found their way into a poor fool's mind?
BEFORE: lang(Fox): 她的灵能触须，是否已经探入了某个可怜虫的脑中？
AFTER: lang(Fox): 她的灵能触须，是否已经探入了某个可怜虫的脑中？
CONTROL L28 cut(0.06): FenfenE04
CONTROL L29 rewind!
ROW CAT:O0d9331ea938a937db45e | L30 | no manual edit
EN: There is no way to know if it was dark ESPer power at work or merely curiosity
BEFORE: lang(Fox): 无从得知，究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇， 
AFTER: lang(Fox): 无从得知，究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇， 
ROW CAT:Odeb79c0023c3cb7885cd | L31 | no manual edit
EN: but this traveler made contact with the crystal prison that held Traeh...
BEFORE: lang(Fox): 但这位旅者确实触碰到了关押特蕾的水晶囚牢……
AFTER: lang(Fox): 但这位旅者确实触碰到了关押特蕾的水晶囚牢……
CONTROL L33 cut(0.06): FenfenE05
CONTROL L34 rewind!
ROW CAT:O5623e8fe43c17687fda3 | L35 | EDIT E06-033
EN: ...and so they became undone, unable to resist the dark ESPer forces.
BEFORE: lang(Fox): ……就这样，这名旅者崩溃了，无力抵挡黑暗的超能力者力量。
AFTER: lang(Fox): ……就这样，这名旅者崩溃了，无力抵挡那股黑暗的超能力量。
ROW CAT:O9419eb934b89590c09e8 | L36 | EDIT E06-034
EN: Power and pain coursed through the poor explorer
BEFORE: lang(Fox): 力量与痛苦奔涌过这名可怜的探索者全身， 
AFTER: lang(Fox): 力量与痛苦席卷这名可怜的探索者全身， 
ROW CAT:O4ee923435ea397993591 | L37 | EDIT E06-035
EN: until their mind was no longer their own.
BEFORE: lang(Fox): 直到那心智，再也不属于自己。
AFTER: lang(Fox): 直到连心智也不再由自己掌控。
CONTROL L39 cut(0.06): FenfenE06
CONTROL L40 rewind!
ROW CAT:O4d6fa299e087c6fbdc35 | L41 | EDIT E06-036
EN: No, from that moment forth they answered to a darker power...
BEFORE: lang(Fox): 不，从那一刻起，其便听命于一股更黑暗的力量……
AFTER: lang(Fox): 不，从那一刻起，这名旅者便听命于一股更黑暗的力量……
ROW CAT:Ofd9ced8703115dfa01c1 | L42 | EDIT E06-037
EN: They did as Traeh commanded!
BEFORE: lang(Fox): 特蕾吩咐什么，其便做什么！
AFTER: lang(Fox): 特蕾吩咐什么，这名旅者就做什么！
CONTROL L44 wait: 0.2
CONTROL L45 fadeout(1.0, 1.0, 4)
### P06-022 | action=apply
原问题：“其便”重复书面代词和“力量奔涌过”影响讲述连贯性。建议保留Fox历史讲述、触碰后失去自主的因果；不替前段好奇/操控动机终裁。每个cut前后段分别用，不跨演出合并。
本轮理由：按 cut 两侧原节点顺序修历史讲述，不跨演出；保留可怜探索者、失去自主和受命关系，沿用现有特蕾译名。
EDIT_IDS ["E06-033", "E06-034", "E06-035", "E06-036", "E06-037"]

## SCfabc28c6d25f68c7 | nsfw | vsn/m_AgentM0B/script.vsn | vsn/m_AgentM0B/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L3 snap: AgentPancor001A
CONTROL L4 rewind!
ROW CAT:O18a10500d7fc5bcf7c4e | L5 | no manual edit
EN: Thanks for freeing me! I was starting to get a little chilly here!
BEFORE: text: 谢谢你放我出来！我在这儿都有点冷了！
AFTER: text: 谢谢你放我出来！我在这儿都有点冷了！
ROW CAT:O12690c5b02eb3ae1fe81 | L6 | no manual edit
EN: Really though, I didn't mind the cool air after everything that happened.
BEFORE: text: 不过说真的，经历过那些事，吹点凉风也不错。
AFTER: text: 不过说真的，经历过那些事，吹点凉风也不错。
CONTROL L8 cut(0.06): AgentPancor001B
CONTROL L9 rewind!
ROW CAT:O82e1c2b22b9043b28624 | L10 | no manual edit
EN: I got separated from the rest of my group and was easily overpowered.
BEFORE: text: 我跟队友走散了，轻易就被制服了。
AFTER: text: 我跟队友走散了，轻易就被制服了。
ROW CAT:O1b1670e7db8baf868295 | L11 | no manual edit
EN: This mysterious robed canine pinned me down. Not that I resisted too much...
BEFORE: text: 这只神秘的长袍犬把我按倒了。倒也不是我多想反抗……
AFTER: text: 这只神秘的长袍犬把我按倒了。倒也不是我多想反抗……
ROW CAT:O433dd9e1d63168c13d4f | L12 | no manual edit
EN: Now, one thing about this big guy... is that I'm not sure they were a guy at all!
BEFORE: text: 不过这大个子嘛……我都不确定到底是不是男的！
AFTER: text: 不过这大个子嘛……我都不确定到底是不是男的！
ROW CAT:O952e59dc7db93037ea4c | L13 | no manual edit
EN: 'Been cosmobreeding a bit, and my butt's taken a dick or two in its time, get me?
BEFORE: text: 我也稍微干过点宇宙育种，屁股没少吃鸡巴，懂吧？
AFTER: text: 我也稍微干过点宇宙育种，屁股没少吃鸡巴，懂吧？
ROW CAT:Obe640e0d6480154a1137 | L14 | no manual edit
EN: So I could tell this one wasn't really... real. Just really big, hehee!
BEFORE: text: 所以我看得出，这根不算……真的。只是特别大，嘿嘿！
AFTER: text: 所以我看得出，这根不算……真的。只是特别大，嘿嘿！
CONTROL L16 cut(0.06): AgentPancor001C
CONTROL L17 rewind!
ROW CAT:O634b0f073add20c644e6 | L18 | no manual edit
EN: I even got a closer look at it, when the stranger shoved it in my face, telling me
BEFORE: text: 那陌生人把它怼到我脸前，我还仔细看了看，他叫我把它清理干净。那玩意还泛着蓝光……
AFTER: text: 那陌生人把它怼到我脸前，我还仔细看了看，他叫我把它清理干净。那玩意还泛着蓝光……
ROW CAT:O329ca5919c50cdf51f12 | L19 | no manual edit
EN: to clean it up. It was glowing with some kinda blue light...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O435d2cb71b9696ba050f | L20 | no manual edit
EN: I think the canine smelled kind of... girly? Me though, I'm a simple bunny...
BEFORE: text: 那犬科的气味有点……像女生？不过我嘛，就是只单纯的兔子…… 
AFTER: text: 那犬科的气味有点……像女生？不过我嘛，就是只单纯的兔子…… 
ROW CAT:O53d4e23e4e38773a2fe4 | L21 | no manual edit
EN: Shove a big dick in my face and say 'suck'? I'm not thinkin' about it too hard.
BEFORE: text: 大鸡巴往脸前一杵，叫我‘吸’？那我可不会多想。
AFTER: text: 大鸡巴往脸前一杵，叫我‘吸’？那我可不会多想。
ROW CAT:O48107db8c3888abf595a | L22 | no manual edit
EN: Something in my captor's hand glowed real oddly, but I was too focused on
BEFORE: text: 抓我的家伙手里有什么发着怪光，可我太专注于伺候那根发光的鸡巴，没顾上看清那是什么。
AFTER: text: 抓我的家伙手里有什么发着怪光，可我太专注于伺候那根发光的鸡巴，没顾上看清那是什么。
ROW CAT:Ofb075f86831d475235ff | L23 | no manual edit
EN: servicing that glowing cock to get a good look at what it was.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L25 cut(0.06): AgentPancor001D
CONTROL L26 rewind!
ROW CAT:Oe1339a10cc042e0a2705 | L27 | no manual edit
EN: Everything is kind of a blur after I had gotten that dick in my mouth.
BEFORE: text: 含住那根鸡巴后，一切就变得模模糊糊了。
AFTER: text: 含住那根鸡巴后，一切就变得模模糊糊了。
ROW CAT:Ocdbf6cd0f6b713e2e169 | L28 | no manual edit
EN: I remember being picked up by some other folks... I think?
BEFORE: text: 我记得后来有别的家伙把我抱起来了……大概吧？
AFTER: text: 我记得后来有别的家伙把我抱起来了……大概吧？
ROW CAT:O215456c443432796f22a | L29 | no manual edit
EN: Either way, I was being jammed down on this thick hot glowing dick repeatedly!
BEFORE: text: 反正他们不停把我往那根粗热、发光的鸡巴上猛按！
AFTER: text: 反正他们不停把我往那根粗热、发光的鸡巴上猛按！
CONTROL L31 cut(0.06): AgentPancor001E
CONTROL L32 rewind!
ROW CAT:O2ab5532659128ae06a89 | L33 | no manual edit
EN: I can't even recall how long I was bred for, but I sure felt drained after.
BEFORE: text: 记不清被干了多久，反正完事后我彻底被榨干了。
AFTER: text: 记不清被干了多久，反正完事后我彻底被榨干了。
ROW CAT:O53843c6af7f4a0fa6671 | L34 | no manual edit
EN: Too out of it to even see whose hands slipped me into shackles or lifted my tail.
BEFORE: text: 我恍惚得都看不清，是谁给我戴上镣铐、抬起尾巴。
AFTER: text: 我恍惚得都看不清，是谁给我戴上镣铐、抬起尾巴。
ROW CAT:O0f788ec6313961b96523 | L35 | no manual edit
EN: I couldn't even turn my head to see what was making lusty growling sounds either!
BEFORE: text: 我连转头看看是谁在色欲熏心地低吼都做不到！
AFTER: text: 我连转头看看是谁在色欲熏心地低吼都做不到！
CONTROL L37 cut(0.06): AgentPancor001F
CONTROL L38 rewind!
ROW CAT:O9bd468160497e5f12d7d | L39 | no manual edit
EN: It seems like not even magnificent specimens as the Swipers are immune
BEFORE: text: 看来连挥爪这种出色的物种，也挡不住这美味又完美的棉尾翘臀！！
AFTER: text: 看来连挥爪这种出色的物种，也挡不住这美味又完美的棉尾翘臀！！
ROW CAT:Oc01bf79f1c486a9a4786 | L40 | no manual edit
EN: to delectable perfect cotton tailed asses!!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oddd19bc67106db9375da | L41 | no manual edit
EN: Day after day they've taken turns, doing their best to keep me satisfied! Hee!Hee!
BEFORE: text: 他们天天轮着来，拼命让我满足！嘻！嘻！
AFTER: text: 他们天天轮着来，拼命让我满足！嘻！嘻！
CONTROL L43 cut(0.06): AgentPancor001G
CONTROL L44 rewind!
ROW CAT:O42abad4a4097bbea6b0f | L45 | EDIT E06-038
EN: They did a pretty good job, I gotta say. Definitely in my top three tops.
BEFORE: text: 不得不说，他们干得真不错，绝对排进我最爱的前三个上位。
AFTER: text: 不得不说，他们干得真不错，在我最喜欢的攻里绝对排得进前三。
ROW CAT:Oec35cbbfb6a6c3d697e7 | L46 | no manual edit
EN: Something about those barbs raking in and out juuuuust soooo... mmmh!
BEFORE: text: 那些倒刺来回刮蹭，恰——到好处……嗯唔！ 
AFTER: text: 那些倒刺来回刮蹭，恰——到好处……嗯唔！ 
CONTROL L48 cut(0.06): Black
CONTROL L49 rewind!
ROW CAT:O96cff6560e6709a99644 | L50 | no manual edit
EN: Boy, I hope you weren't too rough on the Swiper guarding me, Yiffai!
BEFORE: text: 伊法伊，你没把看守我的挥爪揍得太惨吧！
AFTER: text: 伊法伊，你没把看守我的挥爪揍得太惨吧！
ROW CAT:Oe4c23bfcdddb099447d1 | L51 | no manual edit
EN: I wouldn't mind one last date with him before I head out of here, hee-!
BEFORE: text: 离开前再跟他约会一次，我可不介意，嘻——！
AFTER: text: 离开前再跟他约会一次，我可不介意，嘻——！
CONTROL L53 wait: 0.2
CONTROL L54 fadeout(1.0, 1.0, 4)
### P06-023 | action=apply
原问题：top three tops为前三名性伴/攻方双关，当前“前三个上位”不是自然的性角色称呼且像体位排行。维持兔子回忆中的自述评价，不更改此前被制服的事实。
本轮理由：top three tops 是攻方排名双关，并非体位；只改排名句，不强加下一句的力道解释。
EDIT_IDS ["E06-038"]

## SCadcabd923d4535da | sfw | vsn/m_EndingGood/script.vsn | vsn/m_EndingGood/script.vsn
CONTROL L1 music: CutsceneE
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): Ending01
CONTROL L4 rewind!
ROW SFWf9fc5ac62e597a44bf552555 | L5 | no manual edit
EN: Nooo! Curse you damn Yiffai siblings!
BEFORE: text: 不要啊！诅咒你们，该死的伊法伊姐弟！
AFTER: text: 不要啊！诅咒你们，该死的伊法伊姐弟！
ROW SFWf041d173cb8f9e18c40a7100 | L6 | no manual edit
EN: I was supposed to rule the world... no... the Galaxy! 
BEFORE: text: 我本该统治世界的……不……是整个银河！ 
AFTER: text: 我本该统治世界的……不……是整个银河！ 
ROW SFW066ad03b7130d098cd9acf5b | L7 | no manual edit
EN: And now... now...!
BEFORE: text: 而现在……现在……！
AFTER: text: 而现在……现在……！
ROW SFW50d5b3bb788d1601ba7c244c | L8 | no manual edit
EN: ...............!!!
BEFORE: text: ...............!!!
AFTER: text: ...............!!!
ROW SFWf758c1430899b4c6045670b0 | L9 | no manual edit
EN: GAAAAARRRRRRRGGGGGGGHGHHHH!
BEFORE: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
AFTER: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
CONTROL L11 fadecut(0.266, 2): Ending02
CONTROL L12 rewind!
ROW SFWc3b33edcc4a0d0fa7527b643 | L13 | no manual edit
EN: Wow sis, did we really just... save a whole planet?
BEFORE: text: 哇，姐姐，我们刚才真的……救了整整一颗星球？
AFTER: text: 哇，姐姐，我们刚才真的……救了整整一颗星球？
ROW SFW7bec90e9dcd94b49a6c6e8b5 | L14 | no manual edit
EN: Yeah lil bro, I think we did! Par for the course on my missions, really.
BEFORE: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
AFTER: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
ROW SFWe69c2cf3fbfb859ac136d255 | L15 | no manual edit
EN: Buuut pretty impressive for my baby bro's first real mission, so good going!
BEFORE: text: 不——过嘛，对我家小弟的第一次真正任务来说已经相当厉害了，干得漂亮！
AFTER: text: 不——过嘛，对我家小弟的第一次真正任务来说已经相当厉害了，干得漂亮！
CONTROL L17 fadecut(0.266, 2): Ending03
CONTROL L18 rewind!
ROW SFW33f1a416c8e60ba06a20495d | L19 | no manual edit
EN: The heroes of Tutone! They return!
BEFORE: text: 图托恩的英雄们！他们回来了！
AFTER: text: 图托恩的英雄们！他们回来了！
ROW SFWcbfab55e18d300e3ddc714a9 | L20 | no manual edit
EN: Traeh has been defeated, her psychic disturbances are no more and her minions flee!
BEFORE: text: 特蕾已被击败，她的灵能扰动不复存在，她的手下四散逃窜！
AFTER: text: 特蕾已被击败，她的灵能扰动不复存在，她的手下四散逃窜！
ROW SFW76b9ddb521ad75be2859ef88 | L21 | no manual edit
EN: Cheers for the heroes!
BEFORE: text: 为英雄们欢呼！
AFTER: text: 为英雄们欢呼！
CONTROL L23 fadecut(0.266, 2): Ending04A
CONTROL L24 rewind!
ROW SFWcb5808c37b631d1db0804d2f | L25 | EDIT E06-039
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: 汪！汪！万岁！
ROW SFWff91b3544ea0d221adac2d01 | L26 | EDIT E06-040
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: 汪！汪！万岁！
ROW SFW087e40cb605e1c37ece4b602 | L27 | EDIT E06-041
EN: BLESSED BE THE COSMOBREEDERS, SAVIORS OF OUR PLANET!
BEFORE: text: 愿宇宙育种者受颂，我们星球的救星！
AFTER: text: 赞颂宇宙育种者，我们星球的救星！
CONTROL L29 snap: Ending04B
ROW SFWc6b7dc77af01c3ea53820f57 | L30 | no manual edit
EN: Wow, good going you two! Clearing out a whole planet of baddies...
BEFORE: text: 哇，你们俩真棒！把整颗星球的坏蛋都清理干净了……
AFTER: text: 哇，你们俩真棒！把整颗星球的坏蛋都清理干净了……
ROW SFW96ba56148d72dbcc492b4d73 | L31 | no manual edit
EN: That's definitely gonna help the local fauna get back on track!
BEFORE: text: 这肯定能帮当地的动物们重回正轨！
AFTER: text: 这肯定能帮当地的动物们重回正轨！
CONTROL L33 snap: Ending04C
ROW SFWa434307d25c239b7fa26a51f | L34 | no manual edit
EN: I knew you two could do it. Never had a doubt in my mind.
BEFORE: text: 我就知道你们俩能做到。我心里从没怀疑过。
AFTER: text: 我就知道你们俩能做到。我心里从没怀疑过。
ROW SFW8fc157988339c93fcc8959c4 | L35 | no manual edit
EN: Not even when one of you went AWOL and stopped responding to all communica-
BEFORE: text: 就连你们中有人擅离职守、不再回应任何通——
AFTER: text: 就连你们中有人擅离职守、不再回应任何通——
ROW SFW915927655dfd6c6309ed3abb | L36 | no manual edit
EN: -Ahem...
BEFORE: text: -嗯哼……
AFTER: text: -嗯哼……
ROW SFWa4bbea1552abf835981c9b65 | L37 | no manual edit
EN: This will definitely be a good report to have filed away, Agents!
BEFORE: text: 这份报告绝对值得归档留存，特工们！
AFTER: text: 这份报告绝对值得归档留存，特工们！
CONTROL L39 snap: Ending04D
ROW SFWb8b5b91d7b8146472d52d7e2 | L40 | EDIT E06-042
EN: Nice one, grrrrl! You and your pup brother really cleaned up down there!
BEFORE: text: 干得漂亮，grrrrl！你和你的小狗弟弟在下面真把坏蛋都清理光了！
AFTER: text: 干得漂亮，姑娘！你和你那小狗崽弟弟在下面可真把坏蛋收拾干净了！
ROW SFWe2ecf2747327e2b6c54e2ec0 | L41 | no manual edit
EN: Just don't forget about us at HQ when all the fame goes to your heads, alright?
BEFORE: text: 只是等名气让你们忘乎所以的时候，可别忘了还在总部的我们，好吗？
AFTER: text: 只是等名气让你们忘乎所以的时候，可别忘了还在总部的我们，好吗？
CONTROL L43 snap: Ending04E
ROW SFW43071516f1a6be5aab497452 | L44 | no manual edit
EN: HOORAH FOR YIFFANY AND YIFFAI! STAR COSMOBREEDERS!
BEFORE: text: 为伊法妮和伊法伊欢呼！明星级宇宙育种者！
AFTER: text: 为伊法妮和伊法伊欢呼！明星级宇宙育种者！
ROW SFW109a5ef182c7c01a1efabb82 | L45 | no manual edit
EN: H O O R A Y ! ! !
BEFORE: text: 好 耶 ！ ！ ！
AFTER: text: 好 耶 ！ ！ ！
CONTROL L47 fadecut(0.266, 2): Ending05
CONTROL L48 rewind!
ROW SFWce570f768d19860ec0a25ae2 | L49 | no manual edit
EN: Heh, how about that, sis? We made a pretty good team, didn't we?
BEFORE: text: 嘿，瞧见没，姐姐？我们配合得挺不错，不是吗？
AFTER: text: 嘿，瞧见没，姐姐？我们配合得挺不错，不是吗？
ROW SFWfe7d9f60627770c40ce66faf | L50 | no manual edit
EN: Wellll... you did alright, bro. 
BEFORE: text: 嗯——……你还行啦，老弟。 
AFTER: text: 嗯——……你还行啦，老弟。 
ROW SFW8113b754b340cb850ce93de4 | L51 | no manual edit
EN: ...for a pup. 
BEFORE: text: ……就一只小崽子而言。 
AFTER: text: ……就一只小崽子而言。 
CONTROL L53 fadecut(0.266, 2): Black
CONTROL L54 rewind!
ROW SFWd05e3f00fe160d47e14ae116 | L55 | no manual edit
EN: [SO ENDS THE REPORT ON PLANET TUTONE.]
BEFORE: text: [图托恩星球的报告至此结束。]
AFTER: text: [图托恩星球的报告至此结束。]
ROW SFW929dae703ef1615e24aedcfe | L56 | no manual edit
EN: [A PLANET WITH A TUMULTUOUS HISTORY, FACING THE GREATEST CHALLENGES OF ITS TIME]
BEFORE: text: [一颗历史动荡、正面临其时代最严峻挑战的星球]
AFTER: text: [一颗历史动荡、正面临其时代最严峻挑战的星球]
ROW SFW284b92c82f18ebd3b384c5fc | L57 | no manual edit
EN: [SAVED BY THE VALIANT EFFORTS OF TWO BRAVE COSMOBREEDERS:]
BEFORE: text: [因两位勇敢的宇宙育种者的英勇努力而获救：]
AFTER: text: [因两位勇敢的宇宙育种者的英勇努力而获救：]
ROW SFW2705ebda04dbdaa75bda8f67 | L58 | no manual edit
EN: [YIFFANY YIFFAI, ELDER SISTER AND SEASONED VETERAN WITH UNMATCHED COMBAT SKILL]
BEFORE: text: [伊法妮·伊法伊，姐姐，久经沙场的老兵，拥有无与伦比的战斗技巧]
AFTER: text: [伊法妮·伊法伊，姐姐，久经沙场的老兵，拥有无与伦比的战斗技巧]
ROW SFW2c3fa5e50e4dee79b6c60a0a | L59 | no manual edit
EN: [AND YIFFAI YIFFAI, THE YOUNGER BROTHER PRODIGY WITH UNENDING ENTHUSIASM]
BEFORE: text: [以及伊法伊·伊法伊，热情永不枯竭的天才弟弟]
AFTER: text: [以及伊法伊·伊法伊，热情永不枯竭的天才弟弟]
ROW SFW270896d114970342a61b9723 | L60 | no manual edit
EN: [WITH THE TWO OF THEM TEAMED UP, THERE'S NO MISSION THAT THEY CAN'T HANDLE]
BEFORE: text: [两人联手，没有他们应付不了的任务]
AFTER: text: [两人联手，没有他们应付不了的任务]
ROW SFW05ede55e41f0e05daf2b43bf | L61 | EDIT E06-043
EN: [AND THE PPP IS PROUD TO HAVE THEM AS AGENTS.]                      -SIGNED, BOSSU
BEFORE: text: [PPP很荣幸能有他们两位作为特工。]                      -SIGNED, BOSSU
AFTER: text: [PPP以有这两位特工为荣。]                      ——署名：Bossu
CONTROL L64 fademusic(0.0, 1.0)
CONTROL L65 fadeout(1.0, 1.0, 4)
### P06-024 | action=apply
原问题：Yip呼应犬类欢呼并仿hip hip hooray，当前残留YIP和“愿……受颂”不自然。建议保留两次重复和庆典语气，不当角色常态犬吠口癖。
本轮理由：YIP 与欢呼双关可译犬吠欢呼；保留两次重复及救星赞颂，不推广为口癖。
EDIT_IDS ["E06-039", "E06-040", "E06-041"]
### P06-025 | action=apply
原问题：grrrrl为拉长girl，不是受保护词；结局祝贺中原样留英文破坏同事口吻。只按本句译姑娘，不全局固定妞/喵。
本轮理由：grrrrl 是本句拉长 girl，译姑娘；保留小狗崽弟弟的局部调侃，不作年龄设定。
EDIT_IDS ["E06-042"]
### P06-026 | action=apply
原问题：-SIGNED, BOSSU是报告署名而非控制命令，当前未译破坏中文报告收尾；名字沿本包既有暂译，仅为提案不裁最终专名。
本轮理由：SIGNED 是报告署名正文非脚本命令，保留署名空格及现用英文 Bossu，不另裁新名字。
EDIT_IDS ["E06-043"]

## SC28990ff79109edc4 | nsfw | vsn/m_GameOverAreaA/script.vsn | vsn/m_GameOverAreaA/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 snap: ClassicGameOverAreaAA
CONTROL L3 waitForCue!
CONTROL L4 rewind!
ROW CAT:O7a2e884766ac875bf370 | L5 | no manual edit
EN: ...ahhh, what a nice soft piece of rocky ground here.
BEFORE: text: ……啊，这块石地真是又软又舒服。
AFTER: text: ……啊，这块石地真是又软又舒服。
ROW CAT:O85845b039bb8d32c29af | L6 | no manual edit
EN: Much more comfy than getting smacked around repeatedly!
BEFORE: text: 比被一顿接一顿地揍舒服多了！
AFTER: text: 比被一顿接一顿地揍舒服多了！
ROW CAT:O63acfac3df3351d31d97 | L7 | no manual edit
EN: So comfy that I might just take a little...
BEFORE: text: 舒服得让我想稍微……
AFTER: text: 舒服得让我想稍微……
CONTROL L9 cut (0.06): Black
ROW CAT:O8c87665013b5388896f7 | L10 | no manual edit
EN: ...nappyroo...
BEFORE: text: ……睡个觉觉……
AFTER: text: ……睡个觉觉……
CONTROL L12 cut(0.06): ClassicGameOverAreaAB
CONTROL L13 rewind!
ROW CAT:O7772fbf74fc9c81213f6 | L14 | no manual edit
EN: Oh man, I must've slept for too long or something. My head's all fuzzy...
BEFORE: text: 天哪，我是不是睡太久了，脑袋迷迷糊糊的……
AFTER: text: 天哪，我是不是睡太久了，脑袋迷迷糊糊的……
ROW CAT:Oe2076960dbb6b7ff96ab | L15 | no manual edit
EN: I mean, it's usually fuzzy... but now it's fuzzy on the /inside/...
BEFORE: text: 我是说，平时也毛茸茸的……但现在/里面/也毛乎乎的……
AFTER: text: 我是说，平时也毛茸茸的……但现在/里面/也毛乎乎的……
ROW CAT:O28ed2946271c8258ebd4 | L16 | no manual edit
EN: Just gotta make my way out of here nice and easy, one step at a ti-
BEFORE: text: 只要慢慢离开这里就好，一步一——
AFTER: text: 只要慢慢离开这里就好，一步一——
CONTROL L18 cut(0.06): ClassicGameOverAreaAC
CONTROL L19 rewind!
ROW CAT:O72aabd56970cc49c578d | L20 | no manual edit
EN: -WAHHH!
BEFORE: text: ——哇啊啊！
AFTER: text: ——哇啊啊！
ROW CAT:O29ef94bfc38c2bcef673 | L21 | no manual edit
EN: Ow! My manly chiselled posterior! What fiend could be responsible
BEFORE: text: 嗷！我那阳刚雕塑般的翘臀！是哪个恶徒趁我虚弱时，狠狠把我撞翻在地？？
AFTER: text: 嗷！我那阳刚雕塑般的翘臀！是哪个恶徒趁我虚弱时，狠狠把我撞翻在地？？
ROW CAT:Odb4a63bb744fe797dd15 | L22 | no manual edit
EN: for violently knocking me off my feet in my moment of weakness??
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L24 cut(0.06): ClassicGameOverAreaAD
CONTROL L25 rewind!
ROW CAT:Oe75de40d12d0e4255fc8 | L26 | no manual edit
EN: ...oh, it's just some sort of weird goop. Blech!
BEFORE: text: ……哦，只是些奇怪的黏糊玩意。呸！
AFTER: text: ……哦，只是些奇怪的黏糊玩意。呸！
ROW CAT:O4bd6e7b12a28017a6459 | L27 | no manual edit
EN: This stuff is both slimy AND sticky somehow.
BEFORE: text: 这玩意怎么又滑又黏的。
AFTER: text: 这玩意怎么又滑又黏的。
ROW CAT:O108500447bd89f615ec4 | L28 | no manual edit
EN: Ugh, it's almost like it's building up the more I struggle.
BEFORE: text: 呃，简直像是我越挣扎，它就积得越多。
AFTER: text: 呃，简直像是我越挣扎，它就积得越多。
ROW CAT:Of3c1302b9764dc9eebbf | L29 | no manual edit
EN: B-back off slime! Let go of me already! D-don't wiggle into my lap!!
BEFORE: text: 退、退开，史莱姆！快放开我！别、别往我腿上钻！！
AFTER: text: 退、退开，史莱姆！快放开我！别、别往我腿上钻！！
CONTROL L31 cut(0.06): ClassicGameOverAreaAE
CONTROL L32 rewind!
ROW CAT:O7861ceb57f8694d0317e | L34 | no manual edit
EN: Ahh! Ahh!
BEFORE: text: 啊！啊！
AFTER: text: 啊！啊！
ROW CAT:O630c66f9b5f1bb12eb95 | L35 | no manual edit
EN: Stop that! That's a n-naughty place for slime to beeeennngh...!
BEFORE: text: 住手！史莱姆不、不该钻进那种羞人的地方啊嗯……！
AFTER: text: 住手！史莱姆不、不该钻进那种羞人的地方啊嗯……！
ROW CAT:Ob592851d7a229c588055 | L36 | no manual edit
EN: I-if only I could use my hands to hold onto you, t-then I could show you
BEFORE: text: 要、要是双手能抱住你，我、我就能让你见识宇宙育种者真正的本事！
AFTER: text: 要、要是双手能抱住你，我、我就能让你见识宇宙育种者真正的本事！
ROW CAT:O5f600902617d3e1e8a85 | L37 | no manual edit
EN: what a Cosmobreeder is REALLY capable of!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L39 cut(0.06): ClassicGameOverAreaAF
CONTROL L40 rewind!
ROW CAT:O2f25c140aede81f32d4b | L42 | no manual edit
EN: My... my hands are free? I should... I should...
BEFORE: text: 我……我的手自由了？我该……我该……
AFTER: text: 我……我的手自由了？我该……我该……
ROW CAT:Ofae5a37c6e2a01365458 | L43 | no manual edit
EN: I should run... but this feels too good! Nnngh!
BEFORE: text: 我该逃的……可这也太舒服了！嗯呃！
AFTER: text: 我该逃的……可这也太舒服了！嗯呃！
ROW CAT:O3ae1ce78cef161d7930f | L44 | no manual edit
EN: My Cosmohips can't stop moving on their own, this jelly feels too good.
BEFORE: text: 我的宇宙翘臀自己动个不停，这胶冻也太爽了。
AFTER: text: 我的宇宙翘臀自己动个不停，这胶冻也太爽了。
ROW CAT:Oa45629f0cc920293edf7 | L45 | no manual edit
EN: It's like a toy for me to thrust into. Nnngh! So.... so good! Ahh!
BEFORE: text: 简直像个任我插的玩具。嗯呃！好……好爽！啊！ 
AFTER: text: 简直像个任我插的玩具。嗯呃！好……好爽！啊！ 
CONTROL L47 cut(0.06): ClassicGameOverAreaAG
CONTROL L48 rewind!
ROW CAT:Odec13f21f44510030ebb | L50 | no manual edit
EN: Huff... okay... now to take the chance to escaWAHH!
BEFORE: text: 呼……好……现在趁机逃——哇啊！
AFTER: text: 呼……好……现在趁机逃——哇啊！
ROW CAT:Oc768d659a42898d95b2b | L51 | no manual edit
EN: Slimes don't even have dicks! Why are y-you trying to penetrate...
BEFORE: text: 史莱姆连鸡巴都没有！你、你还想插进……
AFTER: text: 史莱姆连鸡巴都没有！你、你还想插进……
ROW CAT:Oc32705bc05165f8ab53e | L52 | no manual edit
EN: Ahh! Don't press there! You're... oh gosh... you're making me squirt...!
BEFORE: text: 啊！别按那里！你……天哪……你弄得我要射了……！
AFTER: text: 啊！别按那里！你……天哪……你弄得我要射了……！
ROW CAT:O09bf45feb7d80bfe9d5a | L53 | no manual edit
EN: No no! I'm done humping! I don't need help to s-squirt more... Stop making me...
BEFORE: text: 不不！我已经干完了！不用帮我再、再射了……别再弄得我……
AFTER: text: 不不！我已经干完了！不用帮我再、再射了……别再弄得我……
CONTROL L55 cut (0.06): Black
ROW CAT:O5bab555d095c0c215784 | L56 | no manual edit
EN: ...squirt...
BEFORE: text: ……喷出来……
AFTER: text: ……喷出来……
ROW CAT:Of62cc9fe165c57a8ad0b | L57 | no manual edit
EN: ...over and over...
BEFORE: text: ……一次又一次……
AFTER: text: ……一次又一次……
ROW CAT:O28351f1abb82c6c0d492 | L58 | no manual edit
EN: ...
BEFORE: text: ……
AFTER: text: ……
ROW CAT:Of4ba6390e8fbe1582cd6 | L59 | no manual edit
EN: ...help...!
BEFORE: text: ……救命……！
AFTER: text: ……救命……！
CONTROL L61 cut(0.06): ClassicGameOverAreaAH
CONTROL L62 rewind!
ROW CAT:O952759de9bbab3454842 | L63 | no manual edit
EN: Are you... are you finally done, slimer?
BEFORE: text: 你……你总算完事了吗，史莱姆？
AFTER: text: 你……你总算完事了吗，史莱姆？
ROW CAT:O9b59894ed928cb9f67ef | L64 | no manual edit
EN: F-finally, now I can rest a moment... huff...
BEFORE: text: 终、终于能歇口气了……呼……
AFTER: text: 终、终于能歇口气了……呼……
ROW CAT:Obec274f14b61a920449b | L65 | no manual edit
EN: I should be fine to continue rescuing other agents, so long as can catch my breath
BEFORE: text: 只要喘匀气，我应该就能继续营救其他特工了
AFTER: text: 只要喘匀气，我应该就能继续营救其他特工了
CONTROL L67 snap: ClassicGameOverAreaAH3
CONTROL L68 rewind!
ROW CAT:O589164a7178aa860e29b | L69 | no manual edit
EN: ...all I need is a moment...
BEFORE: text: ……我只需要一点时间……
AFTER: text: ……我只需要一点时间……
CONTROL L71 snap: ClassicGameOverAreaAH4
CONTROL L72 rewind!
ROW CAT:O7ec7e08d253b986e70ca | L73 | no manual edit
EN: ...a nice, enemy free moment...
BEFORE: text: ……美好又没敌人打扰的片刻……
AFTER: text: ……美好又没敌人打扰的片刻……
CONTROL L75 snap: ClassicGameOverAreaAH5
CONTROL L76 rewind!
ROW CAT:O4cb7761dc58430505434 | L77 | no manual edit
EN: ...to recuperate...
BEFORE: text: ……恢复体力……
AFTER: text: ……恢复体力……
CONTROL L79 snap: ClassicGameOverAreaAH2
CONTROL L80 rewind!
ROW CAT:Ob60e546072e247f6bd9e | L81 | no manual edit
EN: ..and I can get back to being a hero!
BEFORE: text: ……我就能继续当英雄了！
AFTER: text: ……我就能继续当英雄了！
CONTROL L83 cut(0.06): ClassicGameOverAreaAI
CONTROL L84 rewind!
ROW CAT:O4701442807cb48460c96 | L85 | EDIT E06-044
EN: OH DEAR SPACE LORD, YOU HAVE GOT TO BE KIDDING ME!
BEFORE: text: 太空神在上，你他妈逗我呢！
AFTER: text: 我的太空神啊，你开什么玩笑！
ROW CAT:Od3ebab642e3079d17ec0 | L86 | no manual edit
EN: L-let go of me! Back, Flayer! I'm not some battery for you to jlust yuse
BEFORE: text: 放、放开我！退后，剥心魔！我才不是任你随便用的电池，
AFTER: text: 放、放开我！退后，剥心魔！我才不是任你随便用的电池，
ROW CAT:Od9d6ac34f8eb54b53efb | L87 | no manual edit
EN: slike shlum sworts offff...
BEFORE: text: 像、像什摸……那种……
AFTER: text: 像、像什摸……那种……
ROW CAT:Odbd1fe4c90e8dac5b3f5 | L88 | no manual edit
EN: shum hort awffff...
BEFORE: text: 什、什么……种、种类的……
AFTER: text: 什、什么……种、种类的……
CONTROL L90 cut(0.06): ClassicGameOverAreaAJ
CONTROL L91 rewind!
ROW CAT:O351e8277187a262cccaa | L92 | no manual edit
EN: Rrrrrfff, morressh pluhszzzzz... dheeepeear iehnnnnn....
BEFORE: text: 呜噜……再、再多点嘛啊……进、进得更深呜……
AFTER: text: 呜噜……再、再多点嘛啊……进、进得更深呜……
ROW CAT:O0e8aec9197dd0ec98617 | L93 | no manual edit
EN: [EDITOR'S NOTE: From this point on nothing intelligent is discernible.]
BEFORE: text: [编者注：从这里起，再也听不出任何有意义的话语。]
AFTER: text: [编者注：从这里起，再也听不出任何有意义的话语。]
ROW CAT:O1f16192cf3f1b2028075 | L94 | no manual edit
EN: [There's nothing left on this recording beyond the sound of sexual grunting]
BEFORE: text: [此后的录音里只剩交媾时的喘哼声，]
AFTER: text: [此后的录音里只剩交媾时的喘哼声，]
ROW CAT:O5903e1503397b0f7cefd | L95 | no manual edit
EN: [and the slimy sounds of appendages doing whatever they desired to the agent.]
BEFORE: text: [以及触肢肆意玩弄特工时黏滑的声响。]
AFTER: text: [以及触肢肆意玩弄特工时黏滑的声响。]
CONTROL L97 cut(0.06): ClassicGameOverAreaAK
CONTROL L98 rewind!
ROW CAT:O95ce7cc496915963f931 | L99 | no manual edit
EN: [As far as we here at PPP can make out, Agent Yiffai's mind was fully flayed.]
BEFORE: text: [据PPP所知，伊法伊特工的心智已被彻底剥空。]
AFTER: text: [据PPP所知，伊法伊特工的心智已被彻底剥空。]
ROW CAT:Oe4ed5cbbc192b5a088b5 | L100 | no manual edit
EN: [After the Flayer had taken whatever cohesive thoughts remained of the agent]
BEFORE: text: [剥心魔吞尽了特工所剩的一切连贯思绪后]
AFTER: text: [剥心魔吞尽了特工所剩的一切连贯思绪后]
ROW CAT:O852cde3af14c03efd322 | L101 | no manual edit
EN: [the hollow husk of the agent was passed off to another Tutone creature.]
BEFORE: text: [特工那具空壳被转交给了另一只图托恩生物。]
AFTER: text: [特工那具空壳被转交给了另一只图托恩生物。]
ROW CAT:O32df1fe2a4771390b533 | L102 | no manual edit
EN: [Interestingly, it seems like the two tentacle-based energy draining beings]
BEFORE: text: [有趣的是，这两种靠触手吸取能量的生物似乎]
AFTER: text: [有趣的是，这两种靠触手吸取能量的生物似乎]
ROW CAT:Ode8977e970c4245d2ea4 | L103 | no manual edit
EN: [engage in a form of sybmiotic cooperation, as they each prefer to drain]
BEFORE: text: [进行着某种共生合作，因为它们各自偏好吸取]
AFTER: text: [进行着某种共生合作，因为它们各自偏好吸取]
ROW CAT:O485041fd474637c15ee4 | L104 | no manual edit
EN: [a different types of energy. Very fascinating!]
BEFORE: text: [不同种类的能量。真有意思！]
AFTER: text: [不同种类的能量。真有意思！]
CONTROL L107 cut(0.06): ClassicGameOverAreaAL
CONTROL L108 rewind!
ROW CAT:O69675a06a4e4b3da773f | L109 | no manual edit
EN: [Agent Yiffai will no doubt appreciate the findings that he helped discover.]
BEFORE: text: [伊法伊特工无疑会欣慰于自己协助取得的研究成果。]
AFTER: text: [伊法伊特工无疑会欣慰于自己协助取得的研究成果。]
ROW CAT:Occf0d2b86ef7038d8760 | L110 | EDIT E06-045
EN: [Unfortunately, when he was found in a tentacle pit, he  was in no shape to]
BEFORE: text: [遗憾的是，在触手坑里找到他时，他的状态已无法，]
AFTER: text: [遗憾的是，在触手坑里找到他时，他已经无力体会别的了，]
ROW CAT:Oa09b134a142bba7d4930 | L111 | EDIT E06-046
EN: [appreciate anything other than being a living battery that was placated]
BEFORE: text: [除了当一块被安抚着的活体电池外，对别的都提不起兴趣，]
AFTER: text: [只知道充当一块活体电池，]
ROW CAT:Ob2dc86f64415e0b6d32c | L112 | EDIT E06-047
EN: [with non-stop sexual pleasure.]
BEFORE: text: [靠无休止的性快感来安抚。]
AFTER: text: [靠无休止的性快感获得安抚。]
CONTROL L114 cut (0.06): Black
CONTROL L115 rewind!
ROW CAT:Oa2eeb3897370b72e0f42 | L116 | no manual edit
EN: [We here at PPP believe that we can restore his mind to its rightful state.]
BEFORE: text: [我们PPP相信，能让他的心智恢复正常。]
AFTER: text: [我们PPP相信，能让他的心智恢复正常。]
ROW CAT:O194eff8fb8a30d4ef59f | L117 | no manual edit
EN: [As soon as further information on how Flayers operate is available.]
BEFORE: text: [只待进一步查明剥心魔的运作方式。]
AFTER: text: [只待进一步查明剥心魔的运作方式。]
ROW CAT:O2977053ba936be407e02 | L118 | no manual edit
EN: [Until then, Agent Yiffai's file is "temporarily" on hold. -EDITOR]
BEFORE: text: [在此之前，伊法伊特工的档案“暂时”搁置。——编辑]
AFTER: text: [在此之前，伊法伊特工的档案“暂时”搁置。——编辑]
CONTROL L120 wait: 0.2
CONTROL L121 fadeout(1.0, 1.0, 4)
### P06-027 | action=apply
原问题：当前凭空添“他妈”，原句夸张但无对应粗口；此处保留高声惊呼与荒诞信仰套语即可，不把Yiffai统一升级粗俗程度。
本轮理由：去掉无源粗口，保留太空神套语及惊呼；不擅加对白方括号。
EDIT_IDS ["E06-044"]
### P06-028 | action=apply
原问题：当前“状态已无法，”“除了……外，对别的”拼接断裂，安抚又重复。整段须保留前句冷幽默与后句残酷反差；不是宣称他已恢复、也不替PPP后文的恢复希望打包票。控制cut不跨越回填。
本轮理由：修三个非空续句的中文衔接，保留前句研究冷幽默、活体电池及性快感安抚；不改写为已经康复。
EDIT_IDS ["E06-045", "E06-046", "E06-047"]

