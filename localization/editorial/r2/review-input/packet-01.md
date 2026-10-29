# packet-01 实际节点独立复核

全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。
AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。
逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。

## SC0e868dca15f9cfba | nsfw | datadf/all.ds | Area0_Macsen2.Rock
CONTROL L129 <Area0_Macsen2.Rock>
ROW CAT:O7204795fc8b655390013 | L130 | no manual edit
EN: This rock fell on my head during those last tremors. It hurt!
BEFORE:   * 先前震动时，这块石头砸在我头上。好疼！ 
AFTER:   * 先前震动时，这块石头砸在我头上。好疼！ 
ROW CAT:O08d39bb06423e2cab310 | L131 | EDIT E01-001
EN: I'll let you have it for a good price!
BEFORE:   * 我就按好价钱把它让给你！
AFTER:   * 这石头便宜点卖给你！
### P01-001 | action=apply
原问题：好价钱让给你不自然；整段是拿砸头的石头做买卖的笑话，宜接成商贩招徕，不增加石头功能。
本轮理由：源文good price是商贩让价招徕；仅修不自然的“按好价钱”，砸头经历本来已清楚，不为整段提案再改正常头句，也不添问句。
EDIT_IDS ["E01-001"]

## SCac5b9f5097efca6e | nsfw | datadf/all.ds | AreaA_Prison3.GoodbyeDog
CONTROL L651 <AreaA_Prison3.GoodbyeDog>
ROW CAT:O865697caa77a7b551eed | L652 | no manual edit
EN: Seeya girl! Watch out for the Barkers!
BEFORE:   * 回见啦，姑娘！小心那些吠叫者！
AFTER:   * 回见啦，姑娘！小心那些吠叫者！
### P01-036 | action=reject
原问题：本包ui.breeding.Barker明确为吠犬，复数Barkers在犬形告别中指同类命名；吠叫者令同一名称无对应。仅本语境提案，不作全局词替换。
本轮理由：Barkers虽指该犬类，但“吠犬”只是R1建议暂译，当前上下文“吠叫者”亦能作为命名使用；本次没有终裁Barker译名。reject这条强制名称一致化提案，不用未终裁词表推动另一个专名替换；非否认对象为Barker。
EDIT_IDS []

## SC6714a4cc2319a591 | nsfw | datadf/all.ds | AreaC_MacsenDark.Hello
CONTROL L1188 <AreaC_MacsenDark.Hello>
ROW CAT:O432aa2e5b3edbea8883e | L1189 | EDIT E01-002
EN: Is that a flashlight in your hands, or are you just happy to see me?
BEFORE:   * 你手里那是手电筒，还是只是见到我就高兴？
AFTER:   * 你手里那根是手电筒，还是见到我就兴奋得翘起来了？
ROW CAT:Ob949308ba4e397af2f13 | L1190 | EDIT E01-003
EN: I kid! I kid! You and that torch are lifesavers.
BEFORE:   * 开玩笑！开玩笑！你和那支火把可是救星。
AFTER:   * 开玩笑！开玩笑！你和那支手电筒可是救星。
### P01-002 | action=apply
原问题：happy to see me是勃起双关，当前仅剩无落点的高兴问句；torch在本段接flashlight，不宜突然变火把。保留调侃后立即感谢。
本轮理由：flashlight与紧接的torch指同一手电；首句是物件突出形状/见面兴奋双关，局部写出翘起落点。保留I kid两次重复和随后感谢，不推广为全局荤梗规则。
EDIT_IDS ["E01-002", "E01-003"]

## SC99af28f8ddc2906b | nsfw | datadf/all.ds | BossuDex.ClassicSpikeball
CONTROL L3101 <BossuDex.ClassicSpikeball>
ROW CAT:Od2e7c3556bff4031d1b3 | L3102 | no manual edit
EN: [WATCH OUT FOR THOSE PRICKLY DRONES PATHING AROUND]
BEFORE:   Bossu: [小心那些四处巡逻的带刺无人机]
AFTER:   Bossu: [小心那些四处巡逻的带刺无人机]
ROW CAT:Odd7e2d9bf5a555428b30 | L3103 | EDIT E01-004
EN: [THEY'RE LITERALLY IMPOSSIBLE TO DESTROY!]
BEFORE:   Bossu: [它们根本就不可能被摧毁！]
AFTER:   Bossu: [它们是真的打不坏！]
ROW CAT:Ob557f8c94d72bee6b80e | L3104 | EDIT E01-005
EN: [LITERALLY? YOU MEAN THAT... FIGURATIVELY RIGHT?]
BEFORE:   Yiffany: [字面意思？你是说……比喻而已，对吧？]
AFTER:   Yiffany: [真的？你是说……只是夸张一下吧？]
ROW CAT:O3643a808790ca558ec3a | L3105 | no manual edit
EN: [BECAUSE I JUST FINISHED TAK-]
BEFORE:   Yiffany: [因为我刚刚才干掉——]
AFTER:   Yiffany: [因为我刚刚才干掉——]
ROW CAT:O54878ca2a6ce667889e8 | L3106 | no manual edit
EN: [WAIT, YOU MANAGED TO DESTROY ONE OF THEM??]
BEFORE:   Bossu: [等等，你居然摧毁了一只？？]
AFTER:   Bossu: [等等，你居然摧毁了一只？？]
ROW CAT:O782e10ba2448cc437480 | L3107 | no manual edit
EN: [WE HAVE NO RECORDS OF ANY WAY TO INCAPACITATE THOSE]
BEFORE:   Bossu: [我们没有记录表明，有什么办法能瘫痪那些刺球，更别提摧毁它们了！]
AFTER:   Bossu: [我们没有记录表明，有什么办法能瘫痪那些刺球，更别提摧毁它们了！]
ROW CAT:Ob86f8f60771d094465da | L3108 | no manual edit
EN: [SPIKEBALLS, MUCH LESS DESTROY THEM!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od88929632d6a64cee23e | L3109 | no manual edit
EN: [IF I DIDN'T KNOW BETTER, I'D SUSPECT YOU OF CHEATING...]
BEFORE:   Bossu: [要不是我心里有数，我真要怀疑你作弊了……]
AFTER:   Bossu: [要不是我心里有数，我真要怀疑你作弊了……]
ROW CAT:O79d72b0a7eafbf28730d | L3110 | no manual edit
EN: [H-HAHA, WELL, UHHH, YOU SEE...]
BEFORE:   Yiffany: [哈、哈哈，嗯，呃，你看……]
AFTER:   Yiffany: [哈、哈哈，嗯，呃，你看……]
ROW CAT:Ocf032c28eea538de6055 | L3111 | no manual edit
EN: [...GOTTA GO, BYE!!]
BEFORE:   Yiffany: [……得走了，拜拜！！]
AFTER:   Yiffany: [……得走了，拜拜！！]
ROW CAT:O2f47100681594922ae89 | L3112 | no manual edit
EN: [...]
BEFORE:   Bossu: [……]
AFTER:   Bossu: [……]
ROW CAT:O87793ecc0ff83f3b8764 | L3113 | no manual edit
EN: [...ABSOLUTELY SHAMEFUL...]
BEFORE:   Bossu: [……真是太不像话了……]
AFTER:   Bossu: [……真是太不像话了……]
### P01-003 | action=apply
原问题：当前上句不使用字面/比喻表达，下句却突兀问字面意思；整段应建立真的打不坏—只是夸张吧—我刚打坏的递进。
本轮理由：完整entry中主角质疑literally并被打断；改成“真的打不坏—只是夸张吧”建立中文衔接，保留后续刚干掉的中断、总部记录限定和作弊反转，不改正常警告句。
EDIT_IDS ["E01-004", "E01-005"]

## SC56eac4767b4dbc1a | nsfw | datadf/all.ds | BossuDex.ClassicSpikeballZero
CONTROL L2870 <BossuDex.ClassicSpikeballZero>
ROW CAT:Oe8390f2ba6e9527ea456 | L2871 | no manual edit
EN: [WATCH OUT FOR THOSE PRICKLY DRONES PATHING AROUND]
BEFORE:   Bossu: [小心那些四处巡逻的带刺无人机]
AFTER:   Bossu: [小心那些四处巡逻的带刺无人机]
ROW CAT:Od13c8c95fe58a1101798 | L2872 | EDIT E01-006
EN: [THEY'RE LITERALLY IMPOSSIBLE TO DESTROY!]
BEFORE:   Bossu: [它们根本就不可能被摧毁！]
AFTER:   Bossu: [它们是真的打不坏！]
ROW CAT:O32f80dd2880f79aa9b88 | L2873 | EDIT E01-007
EN: [LITERALLY? YOU MEAN THAT... FIGURATIVELY RIGHT?]
BEFORE:   Yiffany: [字面意思？你是说……比喻而已，对吧？]
AFTER:   Yiffany: [真的？你是说……只是夸张一下吧？]
ROW CAT:O163ea204ad84ad3cd87b | L2874 | no manual edit
EN: [BECAUSE I JUST FINISHED TAK-]
BEFORE:   Yiffany: [因为我刚刚才干掉——]
AFTER:   Yiffany: [因为我刚刚才干掉——]
ROW CAT:O078cf195b0e5ecd86a01 | L2875 | no manual edit
EN: [WAIT, YOU MANAGED TO DESTROY ONE OF THEM??]
BEFORE:   Bossu: [等等，你居然摧毁了一只？？]
AFTER:   Bossu: [等等，你居然摧毁了一只？？]
ROW CAT:O683a552a882b138b5d5f | L2876 | no manual edit
EN: [WE HAVE NO RECORDS OF ANY WAY TO INCAPACITATE THOSE]
BEFORE:   Bossu: [我们没有记录表明，有什么办法能瘫痪那些刺球，更别提摧毁它们了！]
AFTER:   Bossu: [我们没有记录表明，有什么办法能瘫痪那些刺球，更别提摧毁它们了！]
ROW CAT:O78b910982c9ec7fef660 | L2877 | no manual edit
EN: [SPIKEBALLS, MUCH LESS DESTROY THEM!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Occebf7db9ad95ca23736 | L2878 | no manual edit
EN: [IF I DIDN'T KNOW BETTER, I'D SUSPECT YOU OF CHEATING...]
BEFORE:   Bossu: [要不是我心里有数，我真要怀疑你作弊了……]
AFTER:   Bossu: [要不是我心里有数，我真要怀疑你作弊了……]
ROW CAT:Oadabd3dfde51fbbb144a | L2879 | no manual edit
EN: [H-HAHA, WELL, UHHH, YOU SEE...]
BEFORE:   Yiffany: [哈、哈哈，嗯，呃，你看……]
AFTER:   Yiffany: [哈、哈哈，嗯，呃，你看……]
ROW CAT:Od19603bcfc12f91bda1a | L2880 | no manual edit
EN: [...GOTTA GO, BYE!!]
BEFORE:   Yiffany: [……得走了，拜拜！！]
AFTER:   Yiffany: [……得走了，拜拜！！]
ROW CAT:O25702ed2a93cb6e7e1a3 | L2881 | no manual edit
EN: [...]
BEFORE:   Bossu: [……]
AFTER:   Bossu: [……]
ROW CAT:Obce741235145f66a8702 | L2882 | no manual edit
EN: [...ABSOLUTELY SHAMEFUL...]
BEFORE:   Bossu: [……真是太不像话了……]
AFTER:   Bossu: [……真是太不像话了……]
### P01-004 | action=apply
原问题：Zero为独立entry，同一语用问题单独留ID，不合并经历。
本轮理由：Zero为独立entry，完整后续同样有摧毁/作弊反转；仅在本entry修“真的—夸张”衔接，不据另一个entry合并经历。
EDIT_IDS ["E01-006", "E01-007"]

## SCa197a0c5cb30c447 | nsfw | datadf/all.ds | DefeatHints.Generic.shop
CONTROL L4921 <DefeatHints.Generic.shop>
ROW CAT:O4c89346fd770a2198a1f | L4922 | EDIT E01-008
EN: GEE, YOU TOOK A WALLOP...
BEFORE:   Mauser: 天哪，你挨了重重一下……
AFTER:   Mauser: 哎呀，你这下挨得可不轻……
ROW CAT:O97a9a29c21457120e126 | L4923 | EDIT E01-009
EN: MAYBE YOU SHOULD LOOK FOR A SHOP
BEFORE:   Mauser: 也许你该找家商店，去买装备和回复道具！
AFTER:   Mauser: 不如找家店，买点装备或回复道具吧！
ROW CAT:Ob60df102a4de6818d8ad | L4924 | no manual edit
EN: TO BUY GEAR OR HEALING ITEMS!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O524b070af767cc725faf | L4925 | EDIT E01-010
EN: YOU CAN EVEN STOCK UP FOR TOUGH FIGHTS
BEFORE:   Tomcat: 你甚至可以为硬仗囤好货
AFTER:   Tomcat: 碰上硬仗前，还可以多备些补给。
### P01-005 | action=apply
原问题：挨了重重一下、你甚至可以为硬仗囤好货机械且节奏不顺；这是败北后的具体补给建议，并非夸赞囤货能力。
本轮理由：败北后先关切再建议采购，最后为硬仗备补给；修机械搭配并将源or恢复为“或”，购买与备货仍各归原说话人，已合句尾槽不恢复。
EDIT_IDS ["E01-008", "E01-009", "E01-010"]

## SC0455d784def8c84b | nsfw | datadf/all.ds | Mauser.AreaB_map11_a noselect
CONTROL L2353 <Mauser.AreaB_map11_a noselect>
ROW CAT:Od208c9cc13707f70779e | L2354 | no manual edit
EN: [SURE IS A LOT OF DIRT AROUND THERE, ISN'T THERE?]
BEFORE:   Mauser: [那周围果然有不少泥土，不是吗？]
AFTER:   Mauser: [那周围果然有不少泥土，不是吗？]
ROW CAT:O3ae5474511f80c7297bc | L2355 | no manual edit
EN: [YUUUP, MAKES ME WISH I BROUGHT A SHOVEL WITH ME...]
BEFORE:   Yiffany: [是啊，害得我真希望自己带了把铲子……]
AFTER:   Yiffany: [是啊，害得我真希望自己带了把铲子……]
ROW CAT:O9a641edef3adc4f62a71 | L2356 | no manual edit
EN: [DIDN'T YOU? THERE'S A SHOVEL IN EVERY STANDARD COSMO KIT!]
BEFORE:   Mauser: [你没带吗？每个标准COSMO套件里都有一把铲子！]
AFTER:   Mauser: [你没带吗？每个标准COSMO套件里都有一把铲子！]
ROW CAT:O96aca66a0487f9dae163 | L2357 | no manual edit
EN: [NOT ONLY THAT, BUT THERE SHOULD BE A BACKUP SHOVEL]
BEFORE:   Mauser: [不止如此，右舷机翼后方的储物舱里应该还有一把备用铲子。]
AFTER:   Mauser: [不止如此，右舷机翼后方的储物舱里应该还有一把备用铲子。]
ROW CAT:O3d46f7e7bc0e2cdf0f94 | L2358 | no manual edit
EN: [IN THE STARBOARD WING'S REAR STORAGE COMPARTMENT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O707ed03be31bdc81fd2b | L2359 | no manual edit
EN: [...CAN YOU STOP, PLEASE?]
BEFORE:   Yiffany: [……你能就此打住吗，拜托？]
AFTER:   Yiffany: [……你能就此打住吗，拜托？]
ROW CAT:O2765856090b02dfb98e0 | L2360 | EDIT E01-011
EN: [BARRING ACTUALLY HAVING THE GEAR WE PACKED FOR YOU]
BEFORE:   Tomcat: [除非你真带着我们给你打包的装备，不然也许你就该四肢着地自己挖？哈！]
AFTER:   Tomcat: [既然我们给你备的装备不在手边，不如干脆四肢着地自己挖？哈！]
ROW CAT:O8f6d73249551bde12c43 | L2361 | no manual edit
EN: [MAYBE YOU SHOULD JUST GET DOWN ON ALL FOURS AND DIG? HA!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oc279936da4551da85176 | L2362 | no manual edit
EN: [NOT A BAD IDEA, ACTUALLY...]
BEFORE:   Yiffany: [其实，这主意还不错……]
AFTER:   Yiffany: [其实，这主意还不错……]
### P01-006 | action=apply
原问题：barring在此承接铲子和备用铲子都不在身边，不是设置除非带着装备的假条件；按对话落回犬类挖掘笑话。
本轮理由：铲子与备用铲子均不在手边后，barring排除现有装备方案而接徒手挖掘；旧“除非”逻辑倒置。仅修完整合句头，保留四肢着地的犬类笑话。
EDIT_IDS ["E01-011"]

## SC62b1cef19f673dfc | nsfw | datadf/all.ds | Test_Slaver1.GoodbyeDog
CONTROL L5287 <Test_Slaver1.GoodbyeDog>
ROW CAT:Occ652a7307e138adf87d | L5288 | EDIT E01-012
EN: Get out of here mutt! The other dogs got to these slaves first!
BEFORE:   * 从这儿滚出去，杂种狗！别的狗已经先得手这些奴隶了！
AFTER:   * 从这儿滚出去，杂种狗！这些奴隶已经让别的狗抢先占了！
### P01-007 | action=apply
原问题：先得手这些奴隶语法不成立；保留抢先占有含义，不猜具体动作或触发。
本轮理由：got to ... first说明别的狗已抢先占到；修“先得手这些”的动宾病句，保留驱赶与粗鲁称呼，不猜具体动作。
EDIT_IDS ["E01-012"]

## SCe4cad5e13991e734 | sfw | datadf/all.ds | Tomcat.FeralPickup noselect noamendfreq
CONTROL L3692 <Tomcat.FeralPickup noselect noamendfreq>
ROW SFWcc745ad90bd2906e2c8439cc | L3693 | no manual edit
EN: [HEY GIRL, GOT SOME NEWS TO REPO-]
BEFORE:   Tomcat: [嘿，姑娘，有消息要报-]
AFTER:   Tomcat: [嘿，姑娘，有消息要报-]
ROW SFW49f9e8541e39c7a7a9e81b73 | L3694 | no manual edit
EN: [BARK?]
BEFORE:   Yiffany: [汪？]
AFTER:   Yiffany: [汪？]
ROW SFWe0a9ef4708dc97d8790fc19e | L3695 | EDIT E01-013
EN: [COOOOME OOOOOON, REALLY GIRL?]
BEFORE:   Tomcat: [求——你——了，真的吗，姑娘？]
AFTER:   Tomcat: [不是吧——姑娘，你认真的？]
ROW SFWbeffa886a0ccdf8c8f84642d | L3696 | no manual edit
EN: [BARK BARK?]
BEFORE:   Yiffany: [汪汪？]
AFTER:   Yiffany: [汪汪？]
ROW SFW8ce67cb678104b774f78c9c8 | L3697 | no manual edit
EN: [ALRIGHT, YIFFANY, IF YOU CAN HEAR ME WHILE YOUR PET]
BEFORE:   Tomcat: [好吧，伊法妮，要是你的宠物替你接无线电时你还能听见我……有工作要做！]
AFTER:   Tomcat: [好吧，伊法妮，要是你的宠物替你接无线电时你还能听见我……有工作要做！]
ROW SFW2dcbf9e39030765a9e507275 | L3698 | no manual edit
EN: [ANSWERS YOUR RADIO FOR YOU... THERE'S WORK TO DO!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFWdc0453f4c0508d2b58857b14 | L3699 | no manual edit
EN: [...BARK?]
BEFORE:   Yiffany: [……汪？]
AFTER:   Yiffany: [……汪？]
ROW SFWbd0bc65993016431dc092014 | L3700 | EDIT E01-014
EN: [YEAH ALRIGHT, WHATEVER. HOPE THAT DARN GIRL PICKS UP]
BEFORE:   Tomcat: [行行行，随便吧。希望那该死的姑娘接电话]
AFTER:   Tomcat: [行行行，随便吧。等那丫头胡闹完了，]
ROW SFWfc542e61ad1d15a86488c07c | L3701 | EDIT E01-015
EN: [AFTER SHE'S DONE FOOLING AROUND...]
BEFORE:   Tomcat: [等她胡闹完了之后……]
AFTER:   Tomcat: [希望她肯接电话……]
ROW SFWc0783d95597f02af3b84ef1c | L3702 | no manual edit
EN: [...]
BEFORE:   Yiffany: [……]
AFTER:   Yiffany: [……]
### P01-008 | action=apply
原问题：come on是无奈抗议，不是求你；darn girl译该死的姑娘过重，且最后两行倒挂。保留误认宠物接听，不替其认出变身。
本轮理由：Feral原文come on是无奈抗议而非求告；darn按熟人抱怨减轻。“等胡闹完—希望接听”在两现有非空槽重排，仍是误认宠物替接，不改为识破变身。
EDIT_IDS ["E01-013", "E01-014", "E01-015"]

## SCe21f2978a46f98f3 | sfw | datadf/all.ds | Tomcat.SlimePickup noselect noamendfreq
CONTROL L3713 <Tomcat.SlimePickup noselect noamendfreq>
ROW SFW711f702bdf61a64baa421ae3 | L3714 | no manual edit
EN: [HEY GIRL, GOT SOME NEWS TO REPO-]
BEFORE:   Tomcat: [嘿，姑娘，有消息要报-]
AFTER:   Tomcat: [嘿，姑娘，有消息要报-]
ROW SFWd24ae64718f5f3acd1badd25 | L3715 | no manual edit
EN: [GLUG?]
BEFORE:   Yiffany: [咕噜？]
AFTER:   Yiffany: [咕噜？]
ROW SFWe1bc93538d650be7508d9cad | L3716 | EDIT E01-016
EN: [COOOOME OOOOOON, REALLY GIRL?]
BEFORE:   Tomcat: [求——你——了，真的吗，姑娘？]
AFTER:   Tomcat: [不是吧——姑娘，你认真的？]
ROW SFWe0749d1011c60414b66381c4 | L3717 | no manual edit
EN: [GLOOP?]
BEFORE:   Yiffany: [咕叽？]
AFTER:   Yiffany: [咕叽？]
ROW SFW2b5195812de76fafd8544c45 | L3718 | no manual edit
EN: [ALRIGHT, YIFFANY, IF YOU CAN HEAR ME WHILE YOUR PET]
BEFORE:   Tomcat: [好吧，伊法妮，要是你的宠物替你接无线电时你还能听见我……有工作要做！]
AFTER:   Tomcat: [好吧，伊法妮，要是你的宠物替你接无线电时你还能听见我……有工作要做！]
ROW SFW5d3fa090560b6bdbee78a218 | L3719 | no manual edit
EN: [ANSWERS YOUR RADIO FOR YOU... THERE'S WORK TO DO!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW7442cd6752de82f7a8b30e16 | L3720 | EDIT E01-017
EN: [...GOOP?]
BEFORE:   Yiffany: [……黏糊？]
AFTER:   Yiffany: [……咕叽？]
ROW SFW969316afb37e0e9afa0ca91c | L3721 | EDIT E01-018
EN: [YEAH ALRIGHT, WHATEVER. HOPE THAT DARN GIRL PICKS UP]
BEFORE:   Tomcat: [行行行，随便吧。希望那该死的姑娘接电话]
AFTER:   Tomcat: [行行行，随便吧。等那丫头胡闹完了，]
ROW SFW8c31b3667adba40e1e68e95a | L3722 | EDIT E01-019
EN: [AFTER SHE'S DONE FOOLING AROUND...]
BEFORE:   Tomcat: [等她胡闹完了之后……]
AFTER:   Tomcat: [希望她肯接电话……]
ROW SFW9a79eb1c80db90f0729dc93d | L3723 | no manual edit
EN: [...]
BEFORE:   Yiffany: [……]
AFTER:   Yiffany: [……]
### P01-009 | action=apply
原问题：独立Slime分支；GOOP是该形态发声，不是说出黏糊这一形容词。其余同为无奈抗议和倒挂语序。
本轮理由：Slime分支独立复审：come on同为无奈，GOOP为发声而非形容词；末尾条件/希望按自然意群分给两现有槽，宠物替接的认知未变。
EDIT_IDS ["E01-016", "E01-017", "E01-018", "E01-019"]

## SC6c3b75ae520ac8a6 | nsfw | datadf/all.ds | TomcatItems.SpecialGeiger
CONTROL L4452 <TomcatItems.SpecialGeiger>
ROW CAT:O510e50267c3833b4e3b5 | L4453 | no manual edit
EN: [THAT'S *NOT* A STANDARD RADIO YOU'RE USING, GIRL!]
BEFORE:   Tomcat: [你用的*不是*标准无线电，姑娘！]
AFTER:   Tomcat: [你用的*不是*标准无线电，姑娘！]
ROW CAT:O3d0327c2905500b9c84a | L4454 | no manual edit
EN: [WHAT, CAN'T GET A GOOD LOCK ON ITS SIGNAL?]
BEFORE:   Yiffany: [怎么，锁不住它的信号？]
AFTER:   Yiffany: [怎么，锁不住它的信号？]
ROW CAT:O5b16390515e205f98f96 | L4455 | no manual edit
EN: [NO THE SIGNAL IS FINE AND ALL. AND IT LOOKS LIKE IT HAS]
BEFORE:   Tomcat: [不，信号本身没问题。而且看起来它装了先进传感器，能帮你执行任务！]
AFTER:   Tomcat: [不，信号本身没问题。而且看起来它装了先进传感器，能帮你执行任务！]
ROW CAT:Oc71d6cff8ed179a50a96 | L4456 | no manual edit
EN: [ADVANCED SENSORS INSTALLED THAT WILL HELP YOUR MISSION!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O45879dc3446e41b0aa97 | L4457 | EDIT E01-020
EN: [YEAH. SHOULD HELP WITH FINISHING THE MISSION.]
BEFORE:   Yiffany: [是啊。应该能帮上把任务做完。]
AFTER:   Yiffany: [是啊。应该能帮我完成任务。]
### P01-010 | action=apply
原问题：最后一句帮上把任务做完语法断裂；整段应接信号正常—传感器用途—主角简短回应。
本轮理由：源最后回应仅确认对完成任务有帮助；旧“帮上把任务做完”句法断裂，其他信号和传感器完整合句已通顺，保持不动及*强调*。
EDIT_IDS ["E01-020"]

## SCd91383674653c59a | nsfw | datadf/all.ds | TomcatItems.SpecialKeycard3
CONTROL L4308 <TomcatItems.SpecialKeycard3>
ROW CAT:Ob1dbfcc61e48557094e1 | L4309 | no manual edit
EN: [IN ORDER TO USE A KEYCARD, ALL YOU HAVE TO DO IS]
BEFORE:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
AFTER:   Tomcat: [要用门卡的话，你只要拿着一张走进能量门就行。]
ROW CAT:O41f52b1f24b277bd0ed2 | L4310 | no manual edit
EN: [WALK INTO AN ENERGY DOOR WHILE HOLDING ONE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O29c5679a0cbeffae1c70 | L4311 | EDIT E01-077
EN: [YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!]
BEFORE:   Tomcat: [你能打开等级不超过门上所标数字的门！]
AFTER:   Tomcat: [这张门卡能开启同等级或更低等级的门！]
### P01-033 | action=apply
原问题：Q待核；severity仅标潜在风险，并非确认错译。up to the level displayed on them指代可疑；当前门上所标数字的门无法明确门卡上限。仅记原文/玩法待核，不擅改规则。
本轮理由：补读女线原blob L4298–4302：门终端数字是最低所需门卡等级，高卡也开低门。故可修为“这张门卡能开同等级或更低等级门”，不裁决them究竟指卡面还是门面，也不宣称已实测玩法。
EDIT_IDS ["E01-077"]

## SC402d4d6938e5e2f8 | nsfw | datadf/all.ds | TomcatItems.TazerPirate
CONTROL L4167 <TomcatItems.TazerPirate>
ROW CAT:O3c3b292e1700cf663987 | L4168 | no manual edit
EN: [CHECK OUT THIS PIRATE TAZER, TOMCAT!]
BEFORE:   Yiffany: [快看这把海盗电击枪，汤姆猫！]
AFTER:   Yiffany: [快看这把海盗电击枪，Tomcat！]
ROW CAT:O4c2877c71e6cbf5a55e3 | L4169 | EDIT E01-021
EN: [WELL. THAT ONE DEFINITELY WOULDN'T PASS SPEC IN ANY]
BEFORE:   Tomcat: [嗯。这把在这个象限的任何系统里都绝对过不了规格。不过应急倒能用。]
AFTER:   Tomcat: [嗯。这把在这个象限的哪个星系都过不了规格检查，不过应急倒能用。]
ROW CAT:O17fe70b390459e4d785a | L4170 | no manual edit
EN: [SYSTEM IN THIS QUADRANT. USEFUL IN A PINCH, THOUGH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O5b04f565832c0afe4716 | L4171 | no manual edit
EN: [JUST HOLDING IT, I CAN IMAGINE THE BIG STRONG PIRATE IT]
BEFORE:   Yiffany: [光是握着它，我就能想象它原来属于的那个高大强壮的海盗。那种清楚自己想要什么，而且就会动手去夺的人，必要时还会来粗的……呵……]
AFTER:   Yiffany: [光是握着它，我就能想象它原来属于的那个高大强壮的海盗。那种清楚自己想要什么，而且就会动手去夺的人，必要时还会来粗的……呵……]
ROW CAT:Ofbe1fa092190130628d3 | L4172 | no manual edit
EN: [BELONGED TO. THE KINDA GUY WHO KNEW WHAT HE WANTED AND]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4e1b61d3a4f94b6225f5 | L4173 | no manual edit
EN: [WAS WILLING TO TAKE IT. ROUGHLY, IF NECESSARY... HEH...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O138ff98867ef21f03d02 | L4174 | no manual edit
EN: [UM? Y-YEAH, THAT SOUNDS LIKE A PIRATE TO ME...]
BEFORE:   Tomcat: [呃？是、是啊，听着确实像个海盗……]
AFTER:   Tomcat: [呃？是、是啊，听着确实像个海盗……]
ROW CAT:Obf8c5c7f055e09349775 | L4175 | no manual edit
EN: [OH! HE OVERDROVE THE POWER RAIL ON THIS THING SO]
BEFORE:   Yiffany: [哦！他把这东西的供电轨超载驱动了，所以枪柄又烫又有点震。嗯唔……]
AFTER:   Yiffany: [哦！他把这东西的供电轨超载驱动了，所以枪柄又烫又有点震。嗯唔……]
ROW CAT:Of786b9d676e8b5612172 | L4176 | no manual edit
EN: [THE HILT GETS ALL HOT AND BUZZES A BIT. HMMMM...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7c4a7d062d3b65605b6b | L4177 | no manual edit
EN: [HEY! KEEP YOUR MIND ON THE MISSION, GIRL!]
BEFORE:   Tomcat: [嘿！姑娘，心思放在任务上！]
AFTER:   Tomcat: [嘿！姑娘，心思放在任务上！]
ROW CAT:Oa623cd7bd3dc98c34f81 | L4178 | no manual edit
EN: [... OH, YEAH OF COURSE...]
BEFORE:   Yiffany: [……哦，对，当然……]
AFTER:   Yiffany: [……哦，对，当然……]
### P01-011 | action=apply
原问题：system在宇宙象限语境指星系，当前任何系统里过不了规格像软件兼容性；保留不合规格但能应急的对比。
本轮理由：完整句为this quadrant内any system的规格标准，是宇宙星系而非软件系统；保留任何星系都不合规与应急可用两层含义，不动该场另一个大合句。
EDIT_IDS ["E01-021"]

## SC3eca555452e3d9dd | nsfw | datadf/all.ds | TomcatItems.ZenerCross
CONTROL L4521 <TomcatItems.ZenerCross>
ROW CAT:Of6b6e43610df88e682ba | L4522 | no manual edit
EN: [WOAH, I JUST SAW ANOTHER SPIKE IN YOUR VITALS!]
BEFORE:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
AFTER:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
ROW CAT:O8b1a55c2b90251efb505 | L4523 | no manual edit
EN: [LEMME GUESS: JUST TOUCHED A SENSOR DARK FLOATING ORB?]
BEFORE:   Tomcat: [让我猜猜：刚碰了一颗悬浮的暗色传感球？]
AFTER:   Tomcat: [让我猜猜：刚碰了一颗悬浮的暗色传感球？]
ROW CAT:Odaf8ded0bcadc9ca2d53 | L4524 | no manual edit
EN: [YEAH. THIS POWER... I GET THE FEELING THAT IT WILL MAKE]
BEFORE:   Yiffany: [是啊。这股力量……我有种感觉，它会让我变得更强，但同时也更容易受到攻击……]
AFTER:   Yiffany: [是啊。这股力量……我有种感觉，它会让我变得更强，但同时也更容易受到攻击……]
ROW CAT:O5e9106c8c7d6a52e6225 | L4525 | no manual edit
EN: [ME STRONGER, BUT ALSO MORE VULNERABLE TO ATTACK...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O98afcbac73bf6fd4addb | L4526 | no manual edit
EN: [WITH NO DATA, WE'LL HAVE TO TRUST YOUR INSTINCTS.]
BEFORE:   Tomcat: [没有数据，我们就只能相信你的直觉了。]
AFTER:   Tomcat: [没有数据，我们就只能相信你的直觉了。]
ROW CAT:Obc07b425f26c6842c731 | L4527 | no manual edit
EN: [BUT BE CAREFUL WITH THAT, GIRL.]
BEFORE:   Tomcat: [但要小心那东西，姑娘。]
AFTER:   Tomcat: [但要小心那东西，姑娘。]
ROW CAT:Ofee95a392931cffd067e | L4528 | no manual edit
EN: [YEAH. SEEMS LIKE A DOUBLE-EDGED SWORD. YIFFANY OUT.]
BEFORE:   Yiffany: [是啊。看来像把双刃剑。伊法妮通话结束。]
AFTER:   Yiffany: [是啊。看来像把双刃剑。伊法妮通话结束。]
### P01-034 | action=defer
原问题：Q待核；severity仅标潜在风险，并非确认错译。SENSOR DARK FLOATING ORB语法异常，当前硬解释成传感球可能把残错当科技设定。必须查源文或演出/物件证据，不能仅凭其他球体描述推定。
本轮理由：原blob确为SENSOR DARK异常搭配；没有物件/演出证据证明sensor科技属性或原意，不能从ZenerCross条目名及其他球体猜补。继续defer。
EDIT_IDS []

## SCc50d167569027719 | nsfw | datadm/all.ds | AreaE_Macsen1.Talk.mags
CONTROL L1511 <AreaE_Macsen1.Talk.mags>
ROW CAT:O7756d6a8664d0f0f0101 | L1512 | no manual edit
EN: The worst part about all this space walking is having to wear a space suit.
BEFORE:   * 太空行走最糟的，就是得穿宇航服。
AFTER:   * 太空行走最糟的，就是得穿宇航服。
ROW CAT:O0f3732f0a672b2279b3e | L1513 | no manual edit
EN: Don't worry though, there's extra MAGs in the back here if you need them!
BEFORE:   * 不过别担心，后面还有备用弹匣，需要就拿。
AFTER:   * 不过别担心，后面还有备用弹匣，需要就拿。
CONTROL L1515 ### shared ###
### P01-035 | action=defer
原问题：Q待核；severity仅标潜在风险，并非确认错译。宇航服话题后接备用MAGs，不能仅凭缩写判弹匣。需商店库存或道具定义证据；当前译文可能改变物品类别，暂不自动改。
本轮理由：宇航服/太空行走话题的MAGs缩写未展开，库存/物件身份未证，弹匣和其他解释都不能据常识替换。继续defer，保留可追踪的类别风险。
EDIT_IDS []

## SCeb32d4e75518d767 | nsfw | datadm/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1723 <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1724   if { !f(ctx_maxed_any_pet_affinity) } {
ROW CAT:Oa31868bc6212a6162810 | L1725 | no manual edit
EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
BEFORE:     * 一定要给宠物一点关爱，并且好好喂它们！
AFTER:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW CAT:O08e4dfd7a28b6e81c731 | L1726 | EDIT E01-022
EN: AFTER YOU'VE MAXXXED OUT AN AFFINITY, RETURN HERE FOR A SPECIAL REWARD.
BEFORE:     * 在你把一项亲密度MAXXXED到顶之后，回到这儿领一份特殊奖励。
AFTER:     * 把一只宠物的亲密度培养到最高后，就回来领一份特别奖励吧。
CONTROL L1727   } else {
ROW CAT:Oe433a6739244906e438f | L1728 | no manual edit
EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
BEFORE:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
AFTER:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW CAT:O2bc73708db965c04f1ef | L1729 | EDIT E01-023
EN: JUST PET THEM WHILE THEY'RE AT MAX AFFINITY TO CHARGE THE CRYSTAL.
BEFORE:     * 只要在它们处于MAX亲密度时抚摸它们，就能给水晶充能。
AFTER:     * 只要在它们亲密度满了的时候抚摸它们，就能给水晶充能。
ROW CAT:Occ847a03a1c84f586059 | L1730 | no manual edit
EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
BEFORE:     * 每种生物给的力量都不同！都试试！
AFTER:     * 每种生物给的力量都不同！都试试！
CONTROL L1731   }
CONTROL L1733 ### shared ###
### P01-012 | action=apply
原问题：MAXXXED到顶和MAX亲密度残留英文且对象不清，玩家指令应直接说明任一宠物满亲密度。两条件分支不可串成一次对话。
本轮理由：源affinity/max及条件!ctx_maxed_any_pet_affinity支持任一宠物满亲密度后领奖；另一个else分支为满亲密度时抚摸充能。只去掉两处英文残留，不跨条件移句。
EDIT_IDS ["E01-022", "E01-023"]

## SCae78e1dc49c532a6 | nsfw | datadm/all.ds | Mauser.Area0Transportal1 noselect
CONTROL L2054 <Mauser.Area0Transportal1 noselect>
ROW CAT:O87449b6a212b16edd0dc | L2055 | no manual edit
EN: [THAT PLATFORM RIGHT THERE IS A TELEPORTAL, YIFFAI!]
BEFORE:   Mauser: [就在那边的平台是传送门，伊法伊！]
AFTER:   Mauser: [就在那边的平台是传送门，伊法伊！]
ROW CAT:O85b78ecb15bab6954f4d | L2056 | no manual edit
EN: [ACTIVATE IT TO BE TAKEN DIRECTLY TO YOUR SHIP.]
BEFORE:   Mauser: [启动它就能直接把你送到你的飞船。]
AFTER:   Mauser: [启动它就能直接把你送到你的飞船。]
ROW CAT:O462b31fcd472111c8a46 | L2057 | no manual edit
EN: [WHAT... TO MY SHIP???]
BEFORE:   Yiffai: [什么……到我的飞船？？？]
AFTER:   Yiffai: [什么……到我的飞船？？？]
ROW CAT:Oca9f490d09a60cd3a2f8 | L2058 | no manual edit
EN: [THAT'S RIGHT BUDDY BOY, THANKS TO SATELLITE R18]
BEFORE:   Tomcat: [没错，老弟，多亏了卫星 R18，我们成功把它设成自动跟随你了。]
AFTER:   Tomcat: [没错，老弟，多亏了卫星 R18，我们成功把它设成自动跟随你了。]
ROW CAT:Oa9a0c91437c4693c7267 | L2059 | no manual edit
EN: [WE WERE ABLE TO SET IT TO AUTOMATICALLY FOLLOW YOU]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oa7e10c9b082ce985c76e | L2060 | EDIT E01-024
EN: [SO THAT MEANS I CAN GO AFTER THOSE BAST-]
BEFORE:   Yiffai: [那是不是意味着我可以去找那些 BAST——]
AFTER:   Yiffai: [那我就能去找那帮混——]
ROW CAT:O4c165841dae510edd6e6 | L2061 | EDIT E01-025
EN: [HOLD ON THERE PUP. YOUR SHIP MAY BE BARELY WORKING]
BEFORE:   Bossu: [等一下，小子。你的飞船恐怕只能勉强运转，不过你只能贴地飞行。]
AFTER:   Bossu: [先等等，小狗崽。你的飞船虽然勉强能开，但也只能贴地飞行。]
ROW CAT:Obce59048bc589bdb93ee | L2062 | no manual edit
EN: [BUT YOU MAY ONLY FLY NAP-OF-THE- EARTH.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ode1bdc9483c5b03b82c7 | L2063 | EDIT E01-026
EN: [WE CAN'T RISK YOU GETTING REDOWNED... OR WORSE.]
BEFORE:   Bossu: [我们不能冒着让你被击落……甚至更糟的风险。]
AFTER:   Bossu: [我们不能冒险让你再次被击落……甚至遭遇更糟的事。]
ROW CAT:Of600ec1a364a9e1aceef | L2064 | no manual edit
EN: [AWWW MAAAAAN! SERIOUSLY?]
BEFORE:   Yiffai: [啊啊——！真的假的？]
AFTER:   Yiffai: [啊啊——！真的假的？]
ROW CAT:O360a8c05ba82c868f275 | L2065 | no manual edit
EN: [AS OUR ONLY ACTIVE AGENT NOW, YOU CAN'T BE SO RISKY!]
BEFORE:   Mauser: [你现在是我们唯一的现役特工，不能这么冒险！]
AFTER:   Mauser: [你现在是我们唯一的现役特工，不能这么冒险！]
ROW CAT:Obfbe9a4bdd9340fca56d | L2066 | EDIT E01-027
EN: [YEAH PUP, PUT ON YOUR BIG BOY PANTS AND TAKE IT SLOWLY.]
BEFORE:   Tomcat: [就是啊小子，把你的大号短裤穿上，慢慢来。]
AFTER:   Tomcat: [就是啊，小狗崽，穿大人的裤子，就得稳着点来。]
ROW CAT:O064b95f6deb1f28872ca | L2067 | EDIT E01-028
EN: [...OH WAIT YOU LOST THOSE.]
BEFORE:   Tomcat: [……哦等等，你把那些弄丢了。]   
AFTER:   Tomcat: [……哦，等等，你把裤子弄丢了。]   
ROW CAT:Oaaeb46661c5d0f2852fc | L2068 | EDIT E01-029
EN: [OKAY, OKAY! I'LL TRY AND BE A BIT MORE STRATEGIMICAL.]
BEFORE:   Yiffai: [好好好！我会试着更有点策略一点。]
AFTER:   Yiffai: [好好好！我会试着更有点战策性的。]
ROW CAT:Oc057f1b5f737f00fe957 | L2069 | no manual edit
EN: [GOOD LAD. DON'T FORGET, WE'RE ALL HERE TO HELP YOU.]
BEFORE:   Bossu: [好小子。别忘了，我们都在这儿帮你。]
AFTER:   Bossu: [好小子。别忘了，我们都在这儿帮你。]
ROW CAT:O13f26427579f3b39e3b4 | L2070 | no manual edit
EN: [AND ON TOP OF THAT, THE HANGAR THAT THE OTHER AGENTS]
BEFORE:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
AFTER:   Bossu: [而且除此之外，其他特工当作自动驾驶服务站使用的那个机库，似乎还在运行。]
ROW CAT:O3d2ce0f7917714b15921 | L2071 | no manual edit
EN: [WERE USING AS AN AUTOPILOT SERVICE STATION]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Obf6f771f079d51fa41f9 | L2072 | no manual edit
EN: [SEEMS TO STILL BE RUNNING.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oea0f80dda5facba6b49d | L2073 | no manual edit
EN: [YOU SHOULD STOP BY THERE AND SEE IF ANYONE'S AROUND!]
BEFORE:   Mauser: [你该去那边看看有没有人在！]
AFTER:   Mauser: [你该去那边看看有没有人在！]
ROW CAT:Oac532fb124dfc1d1777f | L2074 | no manual edit
EN: [SOUNDS LIKE A GOOD IDEA. ROGER THAT!]
BEFORE:   Yiffai: [听起来不错。收到！]
AFTER:   Yiffai: [听起来不错。收到！]
### P01-013 | action=apply
原问题：BAST是被截断粗口，不是专名；big boy pants是成熟行事的习语，又被下句丢裤子字面化，当前大号短裤只剩尺寸。保留双层笑点；STRATEGIMICAL为滑稽造词，建议局部磕绊而不设固定口癖。
本轮理由：追敌冲动后的限制、成熟行事习语及裤子丢失反转须顺序保留；用“大人的裤子”作比喻，只让下一槽点明弄丢，不额外插入“先把裤子穿好”动作。BAST只译被截断的“混——”，不补全。STRATEGIMICAL以局部滑稽造词“战策性”保留装专业的错词功能，禁止无源口吃；再被击落和贴地飞行仍完整。
EDIT_IDS ["E01-024", "E01-025", "E01-026", "E01-027", "E01-028", "E01-029"]

## SCad11a1122fdc124a | sfw | datadm/all.ds | Mauser.AreaA_map34_a noamendfreq
CONTROL L2170 <Mauser.AreaA_map34_a noamendfreq>
ROW SFW5f8a5ceb0952154ab8c78294 | L2171 | no manual edit
EN: [G...D JOB DEF...ING TH...A...ET...AI!]
BEFORE:   Mauser: [G...D JOB DEF...ING TH...A...ET...AI!]
AFTER:   Mauser: [G...D JOB DEF...ING TH...A...ET...AI!]
ROW SFW905103e355dff2cbda08e0b3 | L2172 | no manual edit
EN: [...WHAT WAS THAT...?]
BEFORE:   Yiffai: [……你说什么……？]
AFTER:   Yiffai: [……你说什么……？]
ROW SFWc11c9d73ebcce89eab847772 | L2173 | no manual edit
EN: [...SAID... B...IG... ...TEN... ...END!]
BEFORE:   Mauser: [...SAID... B...IG... ...TEN... ...END!]
AFTER:   Mauser: [...SAID... B...IG... ...TEN... ...END!]
ROW SFW3810a9f50f361a939af647e3 | L2174 | no manual edit
EN: [YOU'RE BREAKING UP WAY TOO MUCH, LET ME GET OUT OF HERE]
BEFORE:   Yiffai: [你那边断断续续的太严重了，等我先出去，]
AFTER:   Yiffai: [你那边断断续续的太严重了，等我先出去，]
ROW SFWde31979715b94db5e616ee34 | L2175 | no manual edit
EN: [AND THEN YOU CAN TELL ME ABOUT THE BIG TEN...]
BEFORE:   Yiffai: [然后你再跟我说说那个BIG TEN...]
AFTER:   Yiffai: [然后你再跟我说说那个BIG TEN...]
### P01-032 | action=defer
原问题：Q待核；severity仅标潜在风险，并非确认错译。信号残片多数保留英文，末尾BIG TEN又为角色复述；不能按后续剧情猜成完整信息。需整段失真字幕方案和源文确认。
本轮理由：失真广播仅足以识别残片及主角BIG TEN复述，未获得既不补全断信又保留误听笑点的可靠中文方案；继续defer，不按后文猜补完整信息。
EDIT_IDS []

## SC9297d69003500efa | nsfw | datadm/all.ds | Mauser.AreaB_map11_a noselect
CONTROL L2362 <Mauser.AreaB_map11_a noselect>
ROW CAT:O392e7d2ad5b6c2a2a92e | L2363 | no manual edit
EN: [SURE IS A LOT OF DIRT AROUND THERE, ISN'T THERE?]
BEFORE:   Mauser: [那周围果然有不少泥土，不是吗？]
AFTER:   Mauser: [那周围果然有不少泥土，不是吗？]
ROW CAT:O4d59b0678d5d9e5e69ac | L2364 | no manual edit
EN: [CURRENTLY EXPLORING OPTIONS FOR DIRT REMOVAL.]
BEFORE:   Yiffai: [正在研究清除泥土的方案。]
AFTER:   Yiffai: [正在研究清除泥土的方案。]
ROW CAT:Oed74962018dc305e33bd | L2365 | no manual edit
EN: [FIRST OPTION IS TO WISH THAT I HAD A SHOVEL ON ME...]
BEFORE:   Yiffai: [第一个方案是希望自己身上有把铲子……]
AFTER:   Yiffai: [第一个方案是希望自己身上有把铲子……]
ROW CAT:Ob1a5ceb731ae10efc0d8 | L2366 | no manual edit
EN: [DON'T YOU? THERE'S A SHOVEL IN EVERY STANDARD COSMO KIT!]
BEFORE:   Mauser: [你没有吗？每个标准COSMO套件里都有一把铲子！]
AFTER:   Mauser: [你没有吗？每个标准COSMO套件里都有一把铲子！]
ROW CAT:O799a8f5f29f450a56ced | L2367 | no manual edit
EN: [NOT ONLY THAT, BUT THERE SHOULD BE A BACKUP SHOVEL]
BEFORE:   Mauser: [不止如此，右舷机翼后方的储物舱里还应该有一把备用铲子。]
AFTER:   Mauser: [不止如此，右舷机翼后方的储物舱里还应该有一把备用铲子。]
ROW CAT:O7aaa323b546859ac0402 | L2368 | no manual edit
EN: [IN THE STARBOARD WING'S REAR STORAGE COMPARTMENT.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Ofe0b0d238dde37a0e6db | L2369 | EDIT E01-030
EN: [...THE KIT AND FU- LLY STOCKED SHIP I TOTALLY HAVE...]
BEFORE:   Yiffai: [……那套装备，还有我这艘补给充足的船，我当然有……]
AFTER:   Yiffai: [……说得好像那套装备、那艘补给齐全的飞船都还在我手里似的……]
ROW CAT:Oee0b7e227f482df774ef | L2370 | EDIT E01-031
EN: [BARRING ACTUALLY HAVING THE GEAR WE PACKED FOR YOU]
BEFORE:   Tomcat: [除非你真带着我们给你打包的装备，不然也许你就该四肢着地自己挖？哈！]
AFTER:   Tomcat: [既然我们给你备的装备不在手边，不如干脆四肢着地自己挖？哈！]
ROW CAT:O8394778503731b748f69 | L2371 | no manual edit
EN: [MAYBE YOU SHOULD JUST GET DOWN ON ALL FOURS AND DIG? HA!]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O25e0212f398a186ad2cc | L2372 | EDIT E01-032
EN: [W-WELL, NOW THAT YOU MENTION IT...]
BEFORE:   Yiffai: [那-那，既然你都这么说了……]
AFTER:   Yiffai: [那、那你这么一说……]
### P01-014 | action=apply
原问题：主角totally have是反话，当前肯定句落点生硬；Tomcat接丢装备现状建议犬形挖掘，不是除非有装备才四肢着地。
本轮理由：完整铲子对话和装备遗失使totally have成为反讽；barring接排除装备后四肢着地的建议。保留W-WELL局部重复，不把FU- LLY的排版断词造为口吃。
EDIT_IDS ["E01-030", "E01-031", "E01-032"]

## SCed2ed7626a701a34 | nsfw | datadm/all.ds | Mauser.AreaC_map64_a noselect
CONTROL L2417 <Mauser.AreaC_map64_a noselect>
ROW CAT:O48f7a51a83f536845ba8 | L2418 | no manual edit
EN: [AGENT YIFFAI YIFFAI, COME IN.]
BEFORE:   Mauser: [特工伊法伊·伊法伊，请回话。]
AFTER:   Mauser: [特工伊法伊·伊法伊，请回话。]
ROW CAT:O01dfb2670a810cd54a14 | L2419 | no manual edit
EN: [PROCEED WITH CAUTION, YIFFAI. WE'VE DETECTED...]
BEFORE:   Bossu: [请谨慎前进，伊法伊。我们探测到……]
AFTER:   Bossu: [请谨慎前进，伊法伊。我们探测到……]
ROW CAT:Ob515d7a065b8f26f4ec9 | L2420 | no manual edit
EN: [...ODD READINGS UP AHEAD.]
BEFORE:   Bossu: [……前方有异常读数。]
AFTER:   Bossu: [……前方有异常读数。]
ROW CAT:Ofc5403fb3c4a90a98cf4 | L2421 | no manual edit
EN: [WHAT DO YOU MEAN?]
BEFORE:   Yiffai: [你什么意思？]
AFTER:   Yiffai: [你什么意思？]
ROW CAT:Od700c0edd28a875e3af8 | L2422 | no manual edit
EN: [WELL, NOT TO ALARM YOU... BUT...]
BEFORE:   Mauser: [嗯，不是要吓你……但是……]
AFTER:   Mauser: [嗯，不是要吓你……但是……]
ROW CAT:O9a6b393d137bda56d4a4 | L2423 | no manual edit
EN: [THERE SEEMS TO BE ANOTHER AGENT IN THE AREA.]
BEFORE:   Bossu: [这片区域里似乎还有另一名特工。]
AFTER:   Bossu: [这片区域里似乎还有另一名特工。]
ROW CAT:Od022e755fbdf87bfa81c | L2424 | EDIT E01-033
EN: [AND THEY'VE BEEN MOVING ABOUT. FREELY.]
BEFORE:   Bossu: [而且他们一直在四处移动。自由地。]
AFTER:   Bossu: [而且对方一直在四处活动。没有受到限制。]
ROW CAT:O409fde92afe9aba095a0 | L2425 | no manual edit
EN: [ANOTHER AGENT...]
BEFORE:   Yiffai: [另一名特工……]
AFTER:   Yiffai: [另一名特工……]
ROW CAT:Oc7202cc60369296e25b7 | L2426 | EDIT E01-034
EN: [WE'RE STILL TRYING TO HAIL THEM, BUT... WELL...]
BEFORE:   Mauser: [我们仍在尝试呼叫他们，但是……嗯……]
AFTER:   Mauser: [我们仍在尝试呼叫对方，但是……嗯……]
ROW CAT:O2139711e40d99999b631 | L2427 | EDIT E01-035
EN: [NOW IT LOOKS LIKE THEIR RADIO HAS BEEN TURNED OFF.]
BEFORE:   Mauser: [而现在看来他们的无线电已经被关掉了。]
AFTER:   Mauser: [而现在看来，对方的无线电已经被关掉了。]
ROW CAT:O7135de2fec059c454176 | L2428 | no manual edit
EN: [ONCE AGAIN, PROCEED WITH CAUTION, AGENT.]
BEFORE:   Bossu: [再次提醒，谨慎前进，特工。]
AFTER:   Bossu: [再次提醒，谨慎前进，特工。]
### P01-015 | action=apply
原问题：另一名是单人未定性别的they，译成他们连续造成多人判断。保留身份未明和受困/自由活动的对比，不提前确认姐姐。
本轮理由：another agent为单人未定身份，they需译“对方”；freely为活动未受限制。has been turned off是被动且now looks like有限定，只写“看来对方的无线电已经被关掉”，不添对方主动关机的施事、不提前指姐姐。
EDIT_IDS ["E01-033", "E01-034", "E01-035"]

## SC698a97944b765f72 | nsfw | datadm/all.ds | Test_Hacker1.Meeting
CONTROL L5188 <Test_Hacker1.Meeting>
ROW CAT:O9c768748058f63dd1e7e | L5189 | EDIT E01-036
EN: Greetings, Yiffai. You don't know me, but I kinda snooped your satlink.
BEFORE:   * 你好，伊法伊。你不认识我，不过我有点偷看了你的卫星链路。
AFTER:   * 你好，伊法伊。你不认识我，不过我偷偷探过你的卫星链路。
ROW CAT:O8eadbb6bce9207e6b106 | L5190 | no manual edit
EN: So I've actually been watching you for a while, and I have a proposition...
BEFORE:   * 所以其实我已经观察你有一阵子了，我有个提议……
AFTER:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:O8008ff60ecbed0c19f1f | L5191 | no manual edit
EN: It's simple: You bring me those fancy chips you find out there,
BEFORE:   * 很简单：你把在外头找到的那些花哨芯片带给我，
AFTER:   * 很简单：你把在外头找到的那些花哨芯片带给我，
ROW CAT:O3821a3bbfc1edd63ce33 | L5192 | EDIT E01-037
EN: and I'll hack open doors for you! It's a win-win, obviously!
BEFORE:   * 我就替你黑开门！显然，这是双赢！
AFTER:   * 我就替你破解门禁！这显然是双赢！
### P01-016 | action=apply
原问题：有点偷看链路、黑开门不自然；重写完整自我介绍和交换条件，但Test条目身份不据共用黑客话术强认The0。
本轮理由：satlink被偷偷窥探，hack open是破解门禁；两处直译病句可确认。观察一阵、芯片交换条件仍保留在原槽，不因测试黑客话术强认The0。
EDIT_IDS ["E01-036", "E01-037"]

## SC80c8667bd7fac785 | sfw | datadm/all.ds | Tomcat.Area0_map16_a noselect noamendfreq
CONTROL L1963 <Tomcat.Area0_map16_a noselect noamendfreq>
ROW SFW2861002ea7edc1a3e205652b | L1964 | no manual edit
EN: [HELLO THERE AGENT Y, THIS IS TOMCAT REPORTING IN!]
BEFORE:   Tomcat: [你好呀，Y特工，汤姆猫前来报到！]
AFTER:   Tomcat: [你好呀，Y特工，Tomcat前来报到！]
ROW SFW467b493b35712d5ffe45abdf | L1965 | no manual edit
EN: [WHAT YOU JUST PICKED UP THERE IS AN OL' KEYCARD]
BEFORE:   Tomcat: [你刚捡到的是张老式门卡。]
AFTER:   Tomcat: [你刚捡到的是张老式门卡。]
ROW SFW1e75b5f85c2fdc3e55e63eef | L1966 | no manual edit
EN: [THOSE OLD FASHIONED THINGS HAVE LONG SINCE BEEN RETIRED]
BEFORE:   Tomcat: [那些老古董早就淘汰了，都改用生物识别了。]
AFTER:   Tomcat: [那些老古董早就淘汰了，都改用生物识别了。]
ROW SFW5be6c1761a216f1285cb645c | L1967 | no manual edit
EN: [IN FAVOR OF BIOMETRICS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW1075c0f430275611a998b028 | L1968 | no manual edit
EN: [GOOD TO KNOW, BUT... HOW DID YOU KNOW I GOT IT?]
BEFORE:   Yiffai: [明白了，可是……你怎么知道我捡到了？]
AFTER:   Yiffai: [明白了，可是……你怎么知道我捡到了？]
ROW SFW3ac6cea621b64e59ae4c1e3e | L1969 | no manual edit
EN: [THERE'S A LOW LATENCY SMALL DATA STREAM SATELLITE]
BEFORE:   Tomcat: [有颗低延迟、低数据量的通信卫星，刚——好能联系到你那边。]
AFTER:   Tomcat: [有颗低延迟、低数据量的通信卫星，刚——好能联系到你那边。]
ROW SFWadfe1d08ce0f3d5012d20be6 | L1970 | no manual edit
EN: [JUUUUST ABLE TO CONNECT WITH YOU OUT THERE.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW SFW5d1ca388a31e6b740859f6ae | L1971 | EDIT E01-038
EN: [THE SATELLITE IS SENDING A CONSTANT STREAM OF YOUR]
BEFORE:   Tomcat: [卫星正在源源不断地传来你的]
AFTER:   Tomcat: [卫星会把你的近场数据]
ROW SFW03ba0b2e3da1f057a3ce240a | L1972 | EDIT E01-039
EN: [NEAR-FIELD DATA BACK HERE TO HEADQUARTERS.]
BEFORE:   Tomcat: [近场数据持续传回总部。]
AFTER:   Tomcat: [源源不断地传回总部。]
ROW SFW77d6a9965945096d4a9b827e | L1973 | no manual edit
EN: [INTERPRETTING YOUR EQUIPMENT SITUATION IS MY JOB!]
BEFORE:   Tomcat: [分析你的装备情况就是我的工作！]
AFTER:   Tomcat: [分析你的装备情况就是我的工作！]
ROW SFW5821a75e3880252a5b4a6a26 | L1974 | no manual edit
EN: [NEAT, SO YOU CAN FILL ME IN ON ANY NEW GEAR I GET?]
BEFORE:   Yiffai: [不错！捡到新装备都能找你了解？]
AFTER:   Yiffai: [不错！捡到新装备都能找你了解？]
ROW SFW664b9a9c649f14a4c9456816 | L1975 | no manual edit
EN: [THAAAT'S RIGHT! 28.880 IS MY FREQUENCY.]
BEFORE:   Tomcat: [没——错！我的频率是28.880。]
AFTER:   Tomcat: [没——错！我的频率是28.880。]
ROW SFW588ee784581fca6b993016d3 | L1976 | no manual edit
EN: [GOOD LUCK OUT THERE!]
BEFORE:   Tomcat: [祝你在外面好运！]
AFTER:   Tomcat: [祝你在外面好运！]
### P01-017 | action=apply
原问题：两行当前拼成源源不断地传来你的近场数据持续传回总部，谓语重复错接；按连续信息合成完整句。
本轮理由：源为一个持续传回近场数据的过程；旧两槽谓语重叠且错接，按“传送对象—传回总部”分配两个现有非空槽，不并成一行，也不新增信息。
EDIT_IDS ["E01-038", "E01-039"]

## SCc03069cb0055411f | nsfw | datadm/all.ds | Tomcat.AreaH_map02_a noselect
CONTROL L2611 <Tomcat.AreaH_map02_a noselect>
ROW CAT:Ob3062b35663ac30c0446 | L2612 | no manual edit
EN: [CAREFUL THERE, YIFFAI.]
BEFORE:   Tomcat: [小心点，伊法伊。]
AFTER:   Tomcat: [小心点，伊法伊。]
ROW CAT:O7c50483eb84ec2f0a225 | L2613 | no manual edit
EN: [WHAT?!]
BEFORE:   Yiffai: [什么？！]
AFTER:   Yiffai: [什么？！]
ROW CAT:Oa77d8a04307ad0a69207 | L2614 | EDIT E01-040
EN: [I CAN SEE SOMETHING STARTED TO GET YOU EXCITED UP THERE]
BEFORE:   Tomcat: [我能看见有东西开始让你在上面兴奋了]
AFTER:   Tomcat: [看得出来，有什么东西让你在那边兴奋起来了。]
ROW CAT:O154d658fe941fe5ec590 | L2615 | no manual edit
EN: [WHAT WAS IT? FINALLY FIND A TRAINER TAZER?]
BEFORE:   Tomcat: [是什么？终于找到驯兽电击枪了？]
AFTER:   Tomcat: [是什么？终于找到驯兽电击枪了？]
ROW CAT:Oc175d4efdb590efef1b4 | L2616 | EDIT E01-041
EN: [H-HOW DID YOU KNOW...]
BEFORE:   Yiffai: [怎-怎么知道的……]
AFTER:   Yiffai: [你、你怎么知道……]
ROW CAT:O5880cf9de5c37c07d123 | L2617 | EDIT E01-042
EN: [THERE'S ONLY ONE THING THAT MAKES A PUP LIKE YOU]
BEFORE:   Tomcat: [只有一件事，能让你这样的Pup把像/这样/的指标送到指挥中心。]
AFTER:   Tomcat: [能让你这小狗崽把/这种/体征数据传回指挥中心的，还能有什么？]
ROW CAT:Of800439497071ec955d8 | L2618 | no manual edit
EN: [SEND METRICS LIKE /THIS/ TO COMMAND CENTER.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O932d7baf5aa57139de0c | L2619 | no manual edit
EN: [NOTHING TO BE ASHAMED ABOUT. JUST REMEMBER, AGENT.]
BEFORE:   Bossu: [没什么好羞愧的。只要记住，特工。]
AFTER:   Bossu: [没什么好羞愧的。只要记住，特工。]
ROW CAT:O6c1ee8f2e41787ea6504 | L2620 | no manual edit
EN: [IN ORDER TO STUDY LOCAL LIFE CLOSELY, YOU MUST DEFEAT]
BEFORE:   Bossu: [为了就近研究当地生命，你必须在战斗中使用驯兽电击枪击败它们。]
AFTER:   Bossu: [为了就近研究当地生命，你必须在战斗中使用驯兽电击枪击败它们。]
ROW CAT:O187e6e29b4aaadfd454a | L2621 | no manual edit
EN: [THEM IN COMBAT USING THE TRAINER TAZER.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O627ad7b3a8a3193afe65 | L2622 | no manual edit
EN: [DOING SO ALLOWS THE OBSERVATION UNITS TO PICK UP FAUNA]
BEFORE:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
AFTER:   Bossu: [这样观察单元才能收容那些生物，好让你在机库里更近地观察它们。]
ROW CAT:Oec8c526e6233815f798c | L2623 | no manual edit
EN: [SO THAT YOU MAY OBSERVE THEM CLOSER IN THE HANGAR.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Od2a0b976c337d0e21de2 | L2624 | no manual edit
EN: [UNDERSTOOD! STAND- ARD COSMOBREEDER PROTOCOL! GOT IT!]
BEFORE:   Yiffai: [明白！标准的宇宙育种者规程！知道了！]
AFTER:   Yiffai: [明白！标准的宇宙育种者规程！知道了！]
ROW CAT:O25cedba8d6fdd2231429 | L2625 | EDIT E01-043
EN: [MAYBE GIVE YOURSELF A MINUTE SO THAT YOUR "EXCITEMENT"]
BEFORE:   Tomcat: [也许给自己一分钟，好让你的"兴奋"下去，嗯，Pup？你可不想吓到当地的那些。]
AFTER:   Tomcat: [先缓一分钟，等你的"兴奋"消下去吧，小狗崽。可别吓着当地那些家伙。]
ROW CAT:O4f631a7b10e494a7a5f3 | L2626 | no manual edit
EN: [GOES DOWN, EH PUP? DON'T WANNA SCARE THE LOCALS.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O5634e0799263319247d9 | L2627 | EDIT E01-044
EN: [I D-DON'T KNOW WHAT YOU'RE TALKING ABOUT...]
BEFORE:   Yiffai: [我不-不知道你在说什么……]
AFTER:   Yiffai: [我不、不知道你在说什么……]
### P01-018 | action=apply
原问题：上面兴奋、像/这样/的指标送到指挥中心逐字且不成句；体征监控是调侃依据，不补具体生理数值。
本轮理由：完整场景以体征监控调侃兴奋，up there为那边而非身体上部；保留H-HOW为“你、你怎么知道”，保留/THIS/样式为/这种/，不补具体体征数值。
EDIT_IDS ["E01-040", "E01-041", "E01-042"]
### P01-019 | action=apply
原问题：当地的那些悬空，Pup残留破坏熟人逗弄；保留兴奋下去双关和急辩，不另加羞辱。
本轮理由：原合句包括等兴奋下降及别吓当地对象，必须全部回填；Pup作本场逗弄。D-DONT用“我不、不知道”保留局部重复，不采用被退修的“我、不知道”。
EDIT_IDS ["E01-043", "E01-044"]

## SC0c36a41f62a4e9af | nsfw | datadm/all.ds | Tomcat.AreaX_fenfen_rescued noselect
CONTROL L2639 <Tomcat.AreaX_fenfen_rescued noselect>
ROW CAT:Obd03668649488988240f | L2640 | no manual edit
EN: [OKAY PUP, SPILL IT. WHAT JUST HAP- PENED OVER THERE?]
BEFORE:   Tomcat: [好吧小家伙，说来听听。刚才那边发生了什么事？]
AFTER:   Tomcat: [好吧小家伙，说来听听。刚才那边发生了什么事？]
ROW CAT:O6d565003d19d6511091b | L2641 | EDIT E01-045
EN: [I... I JUST HELPED A LIL FELLA ESCAPE FROM A PRISON]
BEFORE:   Yiffai: [我……我只是帮一个小家伙从监狱里逃了出来，但是当他碰到我的手，我就……]
AFTER:   Yiffai: [我……我刚帮一个小家伙逃出了监狱，可他一碰我的手，我就……]
ROW CAT:O69be429bc0fa40670d29 | L2642 | no manual edit
EN: [BUT WHEN HE TOUCHED MY HANDS, I...]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O86710515b445ab04825e | L2643 | no manual edit
EN: [JUST THE TOUCH OF THEIR HANDS SPIKED YOUR VITALS?]
BEFORE:   Tomcat: [只是碰到他的手，就让你的生命体征飙上去了？]
AFTER:   Tomcat: [只是碰到他的手，就让你的生命体征飙上去了？]
ROW CAT:O63d5fd68e71c5151bede | L2644 | no manual edit
EN: [THEY MUST'VE BEEN ONE HECK OF A HUNK TO DO THA-]
BEFORE:   Tomcat: [得是相当极品的猛男才办得到这-]
AFTER:   Tomcat: [得是相当极品的猛男才办得到这-]
ROW CAT:O3d6489ddd13985ec7069 | L2645 | EDIT E01-046
EN: [NO! NOTHING LIKE THAT! THEY SENT...]
BEFORE:   Yiffai: [不！才不是那样！他们发来……]
AFTER:   Yiffai: [不！才不是那样！对方把……]
ROW CAT:O292c27977d6b83fc9e20 | L2646 | EDIT E01-047
EN: [THEY SENT IMAGES DIRECTLY INTO MY BRAIN, SOMEHOW!]
BEFORE:   Yiffai: [他们不知怎么就直接把图像送进了我脑子里！]
AFTER:   Yiffai: [对方不知怎么就把图像直接传进了我脑子里！]
ROW CAT:O3f28595623b5c9ad9f39 | L2647 | EDIT E01-048
EN: [IT FELT LIKE I WAS LIVING THROUGH ALL THAT THEY DID.]
BEFORE:   Yiffai: [感觉就像我亲身经历了他们做过的一切。]
AFTER:   Yiffai: [感觉就像我亲身经历了对方经历过的一切。]
ROW CAT:Oafac56753a469941c838 | L2648 | EDIT E01-049
EN: [IT'S TRUE, TOMCAT. THE P.A.W. EVEN MANAGED TO RECORD]
BEFORE:   Mauser: [是真的，汤姆猫。P.A.W. 甚至还录下了伊法伊经历的一切。]
AFTER:   Mauser: [是真的，Tomcat。P.A.W. 甚至还录下了伊法伊经历的一切。]
ROW CAT:O01624c810372335b460c | L2649 | no manual edit
EN: [EVERYTHING THAT YIFFAI EXPERIENCED.]
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O7c4bacd080280df00472 | L2650 | no manual edit
EN: [WOAH, CRAZY...]
BEFORE:   Tomcat: [哇，真够疯的……]
AFTER:   Tomcat: [哇，真够疯的……]
ROW CAT:Oa2c25aa272cac82bc2af | L2651 | EDIT E01-050
EN: [I FEEL LIKE I ONLY HEARD A SNIPPET OF THEIR STORY]
BEFORE:   Yiffai: [我感觉只听到了他们故事的一小片段]
AFTER:   Yiffai: [我感觉只听到了对方故事的一小段。]
ROW CAT:Oc2d2882433649d3730c4 | L2652 | no manual edit
EN: [BUT IF I FIND OTHER LOCALS IMPRISONED...]
BEFORE:   Yiffai: [不过，如果我发现还有别的当地人被关着……]
AFTER:   Yiffai: [不过，如果我发现还有别的当地人被关着……]
ROW CAT:O679c3309dd7bafb789ac | L2653 | no manual edit
EN: [UNDERSTOOD, AGENT. KEEP A LOOK OUT FOR OTHERS LIKE THEM.]
BEFORE:   Bossu: [明白，特工。留意其他和他们一样的人。]
AFTER:   Bossu: [明白，特工。留意其他和他们一样的人。]
ROW CAT:O3a301e419787c614bd65 | L2654 | no manual edit
EN: [THEY MAY PROVE TO BE IMPORTANT TO THE MISSION.]
BEFORE:   Bossu: [他们可能会对这次任务很重要。]
AFTER:   Bossu: [他们可能会对这次任务很重要。]
ROW CAT:Oe6da9ed0f975f9907092 | L2655 | no manual edit
EN: [ROGER THAT, WILL KEEP YOU POSTED.]
BEFORE:   Yiffai: [收到，我会随时向你汇报。]
AFTER:   Yiffai: [收到，我会随时向你汇报。]
### P01-020 | action=apply
原问题：同一被救者先他后他们，误变多人；all they did在记忆情境是所经历而非做过的一切。用对方保持指代不猜物种/身份。
本轮理由：此前a lil fella/he/one hunk支持被救者为单人，改对方而非他们；all they did在手触手传图语境为所经历。首句我……我及另两槽“对方把……对方”重复都保留；不改后面的others复数。Mauser合句保留P.A.W.和记录全部经历，正文Tomcat英文。
EDIT_IDS ["E01-045", "E01-046", "E01-047", "E01-048", "E01-049", "E01-050"]

## SC1152b760ddce4ff4 | nsfw | datadm/all.ds | TomcatItems.StatFishtaco
CONTROL L3916 <TomcatItems.StatFishtaco>
ROW CAT:O625e7d09ebbfa3e57013 | L3917 | no manual edit
EN: [OH, A FISH TACO! THOSE SWIPERS HAVE GOOD TASTE!]
BEFORE:   Tomcat: [哦，鱼肉塔可！那些挥爪挺有品味！]
AFTER:   Tomcat: [哦，鱼肉塔可！那些挥爪挺有品味！]
ROW CAT:Oc35823fd7a3a588a2a85 | L3918 | EDIT E01-051
EN: [BEEN A WHILE SINCE YOU'VE HAD ONE OF THOSE, HUH?]
BEFORE:   Tomcat: [你有一阵没再有过那种了吧，嗯？]
AFTER:   Tomcat: [你好久没尝过那种滋味了吧，嗯？]
ROW CAT:O7b4e504c74d85cedf696 | L3919 | no manual edit
EN: [OH, UMM... I GUESS SO...?]
BEFORE:   Yiffai: [哦，嗯……我想是吧……？]
AFTER:   Yiffai: [哦，嗯……我想是吧……？]
ROW CAT:O761cfff2f54e3966ae0d | L3920 | EDIT E01-052
EN: [MAKES YOU LOOK FORWARD TO SEEING Y'ER SIS AGAIN, EH?]
BEFORE:   Tomcat: [会让你盼着再见到你姐妹吧，嗯？]
AFTER:   Tomcat: [是不是更盼着再见到你姐姐了，嗯？]
ROW CAT:O65e2e6b61ccbfd63ad4d | L3921 | EDIT E01-053
EN: [I'M NOT SURE I KNOW WHAT... YOU...WAIT...]
BEFORE:   Yiffai: [我不太确定我知道什么…… 你……等等……]
AFTER:   Yiffai: [我不太懂你在说什……你……等等……]
ROW CAT:O47add33de9db91de4685 | L3922 | no manual edit
EN: [HEH, I WON'T TELL ANYONE ABOUT YOUR TEMP RISING!]
BEFORE:   Tomcat: [呵，我不会跟任何人说你体温升高！]
AFTER:   Tomcat: [呵，我不会跟任何人说你体温升高！]
ROW CAT:O622401cebce8f94820b9 | L3923 | EDIT E01-054
EN: [T-THANKS...GRR...]
BEFORE:   Yiffai: [谢-谢谢...GRR...]
AFTER:   Yiffai: [谢、谢谢……哼……]
### P01-021 | action=apply
原问题：sis在男线已确认是姐姐，不是你姐妹；I am not sure I know what为没听懂对方暗示，当前我知道什么把问答拆坏。保留荤话暗示但不替人物认定亲密经历。
本轮理由：男线sis为已证姐姐；主角逐渐领会暗示而非问自己知道什么。只修不自然暗示回应及GRR残留，保留谢、谢谢和恼声，不认证姐弟既往亲密经历，不另改Swiper未终裁名称。
EDIT_IDS ["E01-051", "E01-052", "E01-053", "E01-054"]

## SC324634902c5c27dd | nsfw | datadm/all.ds | TomcatItems.VitMeat
CONTROL L3874 <TomcatItems.VitMeat>
ROW CAT:O3498f8d0e3ea2ad7bbee | L3875 | EDIT E01-055
EN: [YESSSSSSS]
BEFORE:   Yiffai: [是啊啊啊啊啊啊啊]
AFTER:   Yiffai: [太——棒了！]
ROW CAT:O272377979a1c88dbc600 | L3876 | no manual edit
EN: [OH THAT'S A REALLY HUGE CHUNK OF MEAT!]
BEFORE:   Tomcat: [哦，那真是好大的一块肉！]
AFTER:   Tomcat: [哦，那真是好大的一块肉！]
ROW CAT:Oa98e8a8481a648309031 | L3877 | EDIT E01-056
EN: [SOOO BIIIIIIGGGGGG]
BEFORE:   Yiffai: [好啊啊啊 大啊啊啊啊啊啊啊啊啊啊啊啊啊]
AFTER:   Yiffai: [好——大——！]
ROW CAT:O1632c04c02665541e8b8 | L3878 | no manual edit
EN: [YOU REALLY LIKE BIG MEAT YOU CAN STICK IN YOUR MOUTH, HUH?]
BEFORE:   Tomcat: [你还真喜欢能塞进嘴里的大肉，嗯？]
AFTER:   Tomcat: [你还真喜欢能塞进嘴里的大肉，嗯？]
ROW CAT:O65552af0cccdb8cc8c16 | L3879 | EDIT E01-057
EN: [HUUUUUUUUUUGE]
BEFORE:   Yiffai: [巨啊啊啊啊啊啊啊啊啊啊]
AFTER:   Yiffai: [大得不得了——！]
ROW CAT:O4084b302931729683c11 | L3880 | EDIT E01-058
EN: [DOES IT REMIND YOU OF OTHER THINGS IN YOUR MOUTH, LI-]
BEFORE:   Tomcat: [会不会让你想起嘴里的其他东西，LI-]
AFTER:   Tomcat: [会不会让你想起嘴里的别的东西，比——]
ROW CAT:Od8dd3cad7fdfb6e78384 | L3881 | EDIT E01-059
EN: [JUIIIIIIICCEEEEEYY]
BEFORE:   Yiffai: [汁汁汁汁汁汁汁汁汁汁汁汁汁汁汁汁汁汁]
AFTER:   Yiffai: [汁水真——足——！]
ROW CAT:O755db971f6aedd3e979f | L3882 | no manual edit
EN: [UHH YOU KNOW WHAT?]
BEFORE:   Tomcat: [呃，你知道吗？]
AFTER:   Tomcat: [呃，你知道吗？]
ROW CAT:Oa82cc88770bd27967576 | L3883 | no manual edit
EN: [I'M JUST GONNA LEAVE YOU TWO ALONE FOR A MINUTE...]
BEFORE:   Tomcat: [我就让你们两个单独待一分钟……]
AFTER:   Tomcat: [我就让你们两个单独待一分钟……]
### P01-022 | action=apply
原问题：当前好啊啊大啊啊、巨啊啊和重复汁机械拉长单字，欢呼与食物描述均不成中文，LI-也不应当作未译专名。整段让Tomcat试着开荤玩笑，却被专心吃肉的回应打断。
本轮理由：完整段落是Yiffai沉迷肉大、多汁而Tomcat荤话被打断；改机械啊/汁串为自然拖音。LI-仅留下相当于“比如”的中断“比——”，不补全后文；最后保留一分钟的语义数字，两槽仍分别是转话和离开。
EDIT_IDS ["E01-055", "E01-056", "E01-057", "E01-058", "E01-059"]

## SC6b9b4091349eca10 | nsfw | datadm/all.ds | TomcatItems.ZenerTriangle
CONTROL L4541 <TomcatItems.ZenerTriangle>
ROW CAT:O6fff22370eb029a977d7 | L4542 | no manual edit
EN: [WOAH, I JUST SAW ANOTHER SPIKE IN YOUR VITALS!]
BEFORE:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
AFTER:   Tomcat: [哇，我刚看到你的生命体征又出现一次飙升！]
ROW CAT:O6a9f84678c8093b93c5c | L4543 | no manual edit
EN: [YOU MESSING WITH ANOMALOUS 'POWERS' AGAIN, PUP?]
BEFORE:   Tomcat: [你又在摆弄那些异常的'力量'了，小狗？]
AFTER:   Tomcat: [你又在摆弄那些异常的'力量'了，小狗？]
ROW CAT:Oab7bd0814a5c8ec11bfa | L4544 | no manual edit
EN: [HEY, THE ORB WAS JUST FLOATING RIGHT THERE!]
BEFORE:   Yiffai: [嘿，那球就正好悬浮在那儿呢！]
AFTER:   Yiffai: [嘿，那球就正好悬浮在那儿呢！]
ROW CAT:O7dff8dcce1fb7ef5706b | L4545 | EDIT E01-060
EN: [IT SEEMS... THIS POWER MIGHT MAKE ME TOUGHER? BUT...]
BEFORE:   Yiffai: [看来……这股力量也许会让我更硬？但是……]
AFTER:   Yiffai: [看来……这股力量也许能让我更耐打？但是……]
ROW CAT:Ofebffd735536dad5e505 | L4546 | EDIT E01-061
EN: [WITH A TRADEOFF, ATTACKING THREATS... HURTS THEM LESS?]
BEFORE:   Yiffai: [要有取舍：去攻击那些威胁……造成的伤害会更小？]
AFTER:   Yiffai: [也有代价：打起敌人来……造成的伤害会变小？]
ROW CAT:Odfc6ec73d001f74e7a98 | L4547 | no manual edit
EN: [STARS HELP US, BUT I THINK YOU'RE THE EXPERT HERE.]
BEFORE:   Tomcat: [星辰保佑我们，但我觉得你才是这里的专家。]
AFTER:   Tomcat: [星辰保佑我们，但我觉得你才是这里的专家。]
ROW CAT:Od333eb79267fe7f44155 | L4548 | no manual edit
EN: [JUST BE CAREFUL, KIDDO...]
BEFORE:   Tomcat: [小心点就是了，小家伙……]
AFTER:   Tomcat: [小心点就是了，小家伙……]
ROW CAT:Oadabdf5f4c875d03e3d4 | L4549 | no manual edit
EN: [I'LL TRY TO BE. YIFFAI OUT.]
BEFORE:   Yiffai: [我会尽量小心的。伊法伊通话结束。]
AFTER:   Yiffai: [我会尽量小心的。伊法伊通话结束。]
CONTROL L4551 ### Misc Upgrades ###
### P01-023 | action=apply
原问题：更硬可能偏成性双关而模糊防御增强；原段解释耐打/输出下降的权衡，无数据确认仍保留主角疑问语气。
本轮理由：tougher与hurts them less在本段是防御/输出取舍，修“更硬”歧义及生硬“取舍”句法；保留看来、也许和问句，不编倍率、不顺手改其他正常句。
EDIT_IDS ["E01-060", "E01-061"]

## SC8ca974932cebe3c3 | nsfw | vsn/f_AgentF02/script.vsn | vsn/f_AgentF02/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L3 snap: AreaBSlaveF06
CONTROL L4 rewind!
ROW CAT:O4d53e9afe712d9f6909b | L5 | no manual edit
EN: Owwie... Thanks for dealing with that nasty robo fella.
BEFORE: text: 哎哟……多谢你收拾了那讨厌的机器人。
AFTER: text: 哎哟……多谢你收拾了那讨厌的机器人。
ROW CAT:O0fbc66b145fd78708bed | L6 | no manual edit
EN: Hard to imagine that this... uhh... still wiggling... appendage thing...
BEFORE: text: 真难想象这条……呃……还在蠕动的……附肢……
AFTER: text: 真难想象这条……呃……还在蠕动的……附肢……
ROW CAT:Ob4c320eb1192bb83e344 | L7 | no manual edit
EN: ...was able to force me to the big-O over and over...!
BEFORE: text: ……竟能逼得我一遍遍高潮……！
AFTER: text: ……竟能逼得我一遍遍高潮……！
ROW CAT:Ob926fc921a341422e49a | L8 | no manual edit
EN: Usually I'm pretty good at evading capture, but I got sloppy down here on Tutone.
BEFORE: text: 平时我很擅长躲避抓捕，但在图托恩大意了。
AFTER: text: 平时我很擅长躲避抓捕，但在图托恩大意了。
CONTROL L10 cut(0.06): AreaBSlaveF02
CONTROL L11 rewind!
ROW CAT:Odbaa97f8ad38565b6b69 | L12 | no manual edit
EN: First I got bumped into by some space pirates. No biggy, right?
BEFORE: text: 起先撞见几个太空海盗。没什么大不了，对吧？ 
AFTER: text: 起先撞见几个太空海盗。没什么大不了，对吧？ 
ROW CAT:O49307af89875da2ecde4 | L13 | no manual edit
EN: Could've easily taken them out, even if I was scouting around nude and all.
BEFORE: text: 就算我光着身子侦察，也能轻松收拾他们。
AFTER: text: 就算我光着身子侦察，也能轻松收拾他们。
ROW CAT:Oe6f71c21d75b4d6c73f1 | L14 | no manual edit
EN: ...'cept I couldn't help but notice it wasn't a /fight/ these boys were after!
BEFORE: text: ……不过我还是看出来了，这帮男人想要的可不是/打架/！
AFTER: text: ……不过我还是看出来了，这帮男人想要的可不是/打架/！
CONTROL L16 cut(0.06): AreaBSlaveF03
CONTROL L17 rewind!
ROW CAT:Obd97bb08ed5a9300cbfd | L18 | no manual edit
EN: I settled down a liiiiittle, just enough to let them think they won the tussle
BEFORE: text: 我稍——微安分了一点，刚好让他们以为自己打赢了。你猜怎么着？砰！一个家伙抓住我双臂，直接/开干/了！
AFTER: text: 我稍——微安分了一点，刚好让他们以为自己打赢了。你猜怎么着？砰！一个家伙抓住我双臂，直接/开干/了！
ROW CAT:O2d5d225aa69280400430 | L19 | no manual edit
EN: and wouldn't you know it? Wham! One of them grabbed my arms and just /went/ for it!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O8e573572a049b63ae705 | L20 | no manual edit
EN: No lie, it'd been a hot minute since I got myself laid.
BEFORE: text: 不骗你，我还真有段日子没做爱了。 
AFTER: text: 不骗你，我还真有段日子没做爱了。 
ROW CAT:O226b128e0360f1b4b9d5 | L21 | EDIT E01-062
EN: Before even coming on down to this planet, right? So I was all for a lil gangbang.
BEFORE: text: 甚至在下到这颗星球之前，对吧？所以我很乐意来场小群交。
AFTER: text: 上次还是来这颗星球之前呢，对吧？所以来场小群交，我可求之不得。
CONTROL L23 cut(0.06): AreaBSlaveF04
CONTROL L24 rewind!
ROW CAT:Ofe8c0232a33c7bccaf1a | L25 | no manual edit
EN: After they saw that I wasn't gonna run, the boys just let me handle them as I pleased
BEFORE: text: 看我不打算逃，那帮家伙就任我随意摆弄了，他们只管把鸡巴往我这边一递，怎么伺候就由我来定！
AFTER: text: 看我不打算逃，那帮家伙就任我随意摆弄了，他们只管把鸡巴往我这边一递，怎么伺候就由我来定！
ROW CAT:O3c886a018f0f10ee18d1 | L26 | no manual edit
EN: they'd just shove their dick in my direction and I'd sort out what to do with 'em!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:Oe9e58754c69b9a1cc39a | L27 | no manual edit
EN: Oral, anal, vaginal...
BEFORE: text: 口交、肛交、阴道交……
AFTER: text: 口交、肛交、阴道交……
ROW CAT:O53eb28d830093301c536 | L28 | no manual edit
EN: The group of them weren't picky, and neither was I!
BEFORE: text: 他们这群家伙都不挑，我也一样！
AFTER: text: 他们这群家伙都不挑，我也一样！
CONTROL L30 cut(0.06): AreaBSlaveF05
CONTROL L31 rewind!
ROW CAT:O3e3e35fa98b51f273867 | L32 | no manual edit
EN: I stuck around for a few nights, really working through my pent up energy.
BEFORE: text: 我留下过了几夜，彻底发泄了积压的精力。
AFTER: text: 我留下过了几夜，彻底发泄了积压的精力。
ROW CAT:O25aac6350f03509b6cda | L33 | no manual edit
EN: Reminded me of my academy days, almost!
BEFORE: text: 简直让我想起了在学院的日子！ 
AFTER: text: 简直让我想起了在学院的日子！ 
ROW CAT:Oa0c13d77a416bdb9ac8a | L34 | no manual edit
EN: As many boys to fill you as you wanted, food and drink coming in from... somewhere?
BEFORE: text: 想要多少男人填满你就有多少，吃喝也不知从哪儿送来？
AFTER: text: 想要多少男人填满你就有多少，吃喝也不知从哪儿送来？
ROW CAT:Obd906925198633290848 | L35 | no manual edit
EN: You ever try that sour milk stuff the pirates make?
BEFORE: text: 你尝过海盗酿的那种酸奶吗？ 
AFTER: text: 你尝过海盗酿的那种酸奶吗？ 
ROW CAT:Obc91f131e6dbeed03ff9 | L36 | no manual edit
EN: Stuff is wild, it'll make you feel like you're made of jelly if you drink enough!
BEFORE: text: 那玩意可猛了，喝多了，整个人都软得像果冻！
AFTER: text: 那玩意可猛了，喝多了，整个人都软得像果冻！
CONTROL L38 cut(0.06): AreaBSlaveF01
CONTROL L39 rewind!
ROW CAT:O84f5f2dfcb5bf121ed89 | L40 | no manual edit
EN: Anyways, where was I...
BEFORE: text: 总之，我说到哪了…… 
AFTER: text: 总之，我说到哪了…… 
ROW CAT:O63fa7adcf51c2ab011d1 | L41 | no manual edit
EN: Oh yeah! Eventually I bid farewell to the party animals.
BEFORE: text: 哦，对！最后我跟那群狂欢的野兽告别了。
AFTER: text: 哦，对！最后我跟那群狂欢的野兽告别了。
ROW CAT:O6c2a807a3336917b2227 | L42 | no manual edit
EN: I did have a mission to complete, right?
BEFORE: text: 我毕竟还有任务要完成，对吧？
AFTER: text: 我毕竟还有任务要完成，对吧？
ROW CAT:O2be3ade7391ee1f86a8a | L43 | no manual edit
EN: Fortunately the space pirates seemed to have another plaything ready
BEFORE: text: 幸好那帮太空海盗似乎已经备好了另一个玩物，所以他们也没怎么为难我，吹一吹、撸一撸，我就走了。
AFTER: text: 幸好那帮太空海盗似乎已经备好了另一个玩物，所以他们也没怎么为难我，吹一吹、撸一撸，我就走了。
ROW CAT:Ob23303eab4d12b684010 | L44 | no manual edit
EN: so they didn't give me much guff. Just a quick blowy and handy and off I went.
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L46 cut(0.06): AreaBSlaveF07
CONTROL L47 rewind!
ROW CAT:O887f9432eca7a8168c62 | L48 | no manual edit
EN: And wouldn't you know it! Shortly after leaving I bumped into more Tutoners!
BEFORE: text: 你猜怎么着！离开没多久，我又撞见了图托恩人！
AFTER: text: 你猜怎么着！离开没多久，我又撞见了图托恩人！
ROW CAT:O2af747c96da4ae7fbd8a | L49 | EDIT E01-063
EN: Short with big ears... This must've been one of those Fenfen fellas!
BEFORE: text: 个子小，耳朵大……这肯定就是Fenfen的家伙了！
AFTER: text: 个子小，耳朵大……这肯定就是那些Fenfen中的一个了！
ROW CAT:O199227d31537be4e16d5 | L50 | no manual edit
EN: Heard about them from the local barkeep around these parts.
BEFORE: text: 我听这附近的酒保说起过他们。 
AFTER: text: 我听这附近的酒保说起过他们。 
ROW CAT:O70fb5ce5d5a09822b97e | L51 | no manual edit
EN: Was told that I should maybe give them a hand if I could, and now here one was!
BEFORE: text: 有人说力所能及就帮帮他们，这不，眼前就有一个！
AFTER: text: 有人说力所能及就帮帮他们，这不，眼前就有一个！
CONTROL L53 cut(0.06): AreaBSlaveF08
CONTROL L54 rewind!
ROW CAT:O363609fb3bab5e430f2b | L55 | no manual edit
EN: ...but I was wrong.
BEFORE: text: ……可我错了。
AFTER: text: ……可我错了。
ROW CAT:O3a8e0a31ba59890c7c78 | L56 | no manual edit
EN: ...VERY wrong.
BEFORE: text: ……错得离谱。
AFTER: text: ……错得离谱。
ROW CAT:O8be40bcdea05fc8e95ba | L57 | no manual edit
EN: This little fella just had cold robotic eyes, and they weren't no friend.
BEFORE: text: 这小家伙只有冰冷的机械眼，绝不是什么朋友。
AFTER: text: 这小家伙只有冰冷的机械眼，绝不是什么朋友。
ROW CAT:O499645554da45492422f | L58 | no manual edit
EN: By the time I parsed what I was really looking at, it was too late for me...
BEFORE: text: 等我弄明白自己究竟看到了什么时，已经太迟了……
AFTER: text: 等我弄明白自己究竟看到了什么时，已经太迟了……
CONTROL L60 cut(0.06): AreaBSlaveF09
CONTROL L61 rewind!
ROW CAT:O01667833586c1ebae780 | L62 | no manual edit
EN: So yeah! I've been stuck in this cell with these mechanical molesters
BEFORE: text: 总之就是这样！我一直跟这群机械色魔困在牢房里，一天到晚就这么被操……
AFTER: text: 总之就是这样！我一直跟这群机械色魔困在牢房里，一天到晚就这么被操……
ROW CAT:O0588b8f5867dc2a93ff5 | L63 | no manual edit
EN: just getting rutted in day in and day out...
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
ROW CAT:O4052ec467c567a7bf275 | L64 | EDIT E01-064
EN: ...never thought I'd get sick of just getting good dick constantly
BEFORE: text: ……没想到天天有好鸡巴可挨，也会腻可偏偏就腻了！
AFTER: text: ……没想到，天天有好鸡巴可挨也会腻。可偏偏就腻了！
ROW CAT:Ocf8bc9813013fbcb6161 | L65 | no manual edit
EN: but here we are!
BEFORE: <EMPTY;合句消费尾>
AFTER: <EMPTY;合句消费尾>
CONTROL L67 cut(0.06): Black
CONTROL L68 rewind!
ROW CAT:O84e2741cf09395fc0cd7 | L69 | no manual edit
EN: Alright, you know, I think I've had enough of this planet.
BEFORE: text: 好吧，说真的，这星球我待够了。
AFTER: text: 好吧，说真的，这星球我待够了。
ROW CAT:Od454389355d18296fc1e | L70 | no manual edit
EN: Going from underdicked to oversexed in the span of a week is just...
BEFORE: text: 才一周，就从缺鸡巴干变成被干过头，实在是……
AFTER: text: 才一周，就从缺鸡巴干变成被干过头，实在是……
ROW CAT:O9c90bff93ae8a08b4382 | L71 | no manual edit
EN: ...yeah, I'm out! Good luck with your own mission!
BEFORE: text: ……算了，我撤啦！你的任务加油！
AFTER: text: ……算了，我撤啦！你的任务加油！
CONTROL L73 wait: 0.2
CONTROL L74 fadeout(1.0, 1.0, 4)
### P01-024 | action=apply
原问题：甚至在下到这颗星球之前是悬空时间状语；连上上一句有段日子没做爱，才能清楚解释为何愿意留下。
本轮理由：上句一段时间没上床，与下句before coming连成“上次在到此之前”，方能解释同意群交；保留报告者自述和right问句，两非空槽按自然意群分配。
EDIT_IDS ["E01-062"]
### P01-025 | action=apply
原问题：这肯定就是Fenfen的家伙语法不成立；连续回忆应连起外貌—此前听说—决定帮助，且只保留当时误判，后段机械眼揭示不能提前说破。
本轮理由：当时依据小个大耳误判Fenfen，后段VERY wrong/机械眼仍作后揭；仅修“Fenfen的家伙”的中文，保留此前听说及被告知帮助的原槽，不把误认写成客观身份，也不擅把未明施事指定为酒保。
EDIT_IDS ["E01-063"]
### P01-026 | action=apply
原问题：也会腻可偏偏就腻了少断句且转折撞接；连接被困遭遇与过量后厌倦，保留原先喜欢、后来受够的反差。
本轮理由：旧合句头含never thought与but here we are两层，缺标点导致相撞；完整保留天天被干由喜欢转厌倦的反差，只修该合句头，不删上一个被困合句内容。
EDIT_IDS ["E01-064"]

## SC8c2a5c414a297776 | nsfw | vsn/f_AgentFZ2/script.vsn | vsn/f_AgentFZ2/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Female
CONTROL L4 rewind!
ROW CAT:Obdf83e8a6bf73e5fd9bd | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
AFTER: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW CAT:O25fe2ab809467a265940 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放到我的手上。
AFTER: lang(Fox): 现在，把你的双手放到我的手上。
ROW CAT:O1a2096ad65aae5100c13 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
AFTER: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L9 cut(0.06): FenfenB01
CONTROL L10 rewind!
ROW CAT:O64c282165c424cfd7ad6 | L11 | no manual edit
EN: When Traeh turned her aggressions to us remaining members of the ESPer council
BEFORE: lang(Fox): 当特蕾把矛头转向我们超能力者议会的其余成员时， 
AFTER: lang(Fox): 当特蕾把矛头转向我们超能力者议会的其余成员时， 
ROW CAT:Ob2ebb3d6cf8fcc0a95b6 | L12 | no manual edit
EN: it was unlike anything that we had ever encountered.
BEFORE: lang(Fox): 那是我们从未遭遇过的情形。
AFTER: lang(Fox): 那是我们从未遭遇过的情形。
ROW CAT:Ode0af63219fa39885e7a | L13 | no manual edit
EN: We were a peaceful, though perhaps squabbly, folk!
BEFORE: lang(Fox): 我们本是爱好和平的族群，虽说偶尔也爱拌拌嘴！
AFTER: lang(Fox): 我们本是爱好和平的族群，虽说偶尔也爱拌拌嘴！
ROW CAT:Oac4ce7ed07a9fc7cdd10 | L14 | no manual edit
EN: Violence and ESPer powered aggression were unknown to us!
BEFORE: lang(Fox): 暴力，以及超能力者力量驱动的攻击，我们闻所未闻！
AFTER: lang(Fox): 暴力，以及超能力者力量驱动的攻击，我们闻所未闻！
CONTROL L16 cut(0.06): FenfenB02
CONTROL L17 rewind!
ROW CAT:O6f28a94c58171b7bfbb9 | L18 | no manual edit
EN: Traeh was not alone in her new ambitions, however.
BEFORE: lang(Fox): 然而，怀有这番新野心的并非只有特蕾。 
AFTER: lang(Fox): 然而，怀有这番新野心的并非只有特蕾。 
ROW CAT:Ofe7442510b0c801e46e9 | L19 | no manual edit
EN: Formerly placable creatures began to rise up as though answering her call.
BEFORE: lang(Fox): 向来温顺易处的生灵也纷纷起身，仿佛在响应她的召唤。
AFTER: lang(Fox): 向来温顺易处的生灵也纷纷起身，仿佛在响应她的召唤。
ROW CAT:Of36d21bea7c4bb2e028a | L20 | no manual edit
EN: Their combined powers were frightening...
BEFORE: lang(Fox): 它们汇聚起来的力量令人胆寒……
AFTER: lang(Fox): 它们汇聚起来的力量令人胆寒……
CONTROL L22 cut(0.06): FenfenB03
CONTROL L23 rewind!
ROW CAT:O7f6fe40f135a73ec8dee | L24 | no manual edit
EN: ...and it seemed as if all hope was lost!
BEFORE: lang(Fox): ……而一切希望仿佛就此落空！
AFTER: lang(Fox): ……而一切希望仿佛就此落空！
ROW CAT:Oe3b3bf4b7d7e75f299a2 | L25 | no manual edit
EN: No amount of reason nor pleading would stop the newly emboldened creatures
BEFORE: lang(Fox): 无论讲道理还是苦苦哀求，都挡不住那些陡然壮了胆的生灵
AFTER: lang(Fox): 无论讲道理还是苦苦哀求，都挡不住那些陡然壮了胆的生灵
ROW CAT:O5c9c3ad5986afa329daa | L26 | no manual edit
EN: and even our cries for mercy went unanswered.
BEFORE: lang(Fox): 连我们求饶的呼声也得不到半点回应。
AFTER: lang(Fox): 连我们求饶的呼声也得不到半点回应。
CONTROL L29 cut(0.06): FenfenB04
CONTROL L30 rewind!
ROW CAT:Oc1ee754d8c4b9a48e1be | L31 | no manual edit
EN: Those very cries seemed to only fuel Traeh's power and ambition even more.
BEFORE: lang(Fox): 那些哀嚎，似乎反而助长了特蕾的力量与野心。
AFTER: lang(Fox): 那些哀嚎，似乎反而助长了特蕾的力量与野心。
ROW CAT:O47316e1ad8b605df01ef | L32 | no manual edit
EN: With each new section of Tutone conquered she would set her eyes on another
BEFORE: lang(Fox): 每征服图托恩一片土地，她便盯上下一片，
AFTER: lang(Fox): 每征服图托恩一片土地，她便盯上下一片，
ROW CAT:O7a3703025b55b85c2abd | L33 | no manual edit
EN: until it seemed that the very planet itself would bend to her will.
BEFORE: lang(Fox): 直到仿佛整颗行星本身都要屈从于她的意志。
AFTER: lang(Fox): 直到仿佛整颗行星本身都要屈从于她的意志。
CONTROL L35 cut(0.06): FenfenB05
CONTROL L36 rewind!
ROW CAT:Od2d6ee9add8ecc9721ec | L37 | EDIT E01-065
EN: Any Fenfen that couldn't hide in the shadows of what we once called home
BEFORE: lang(Fox): 任何无法躲进我们曾称之为家的阴影之下的Fenfen
AFTER: lang(Fox): 凡是没能藏进旧日家园阴暗处的Fenfen，
ROW CAT:Of7da73f5be1167ab62b2 | L38 | no manual edit
EN: became enslaved to do the bidding of the new conquerors.
BEFORE: lang(Fox): 都沦为奴隶，听命于新的征服者。
AFTER: lang(Fox): 都沦为奴隶，听命于新的征服者。
ROW CAT:O80cd7e8b0c722b0f54f5 | L39 | EDIT E01-066
EN: This was no longer a quiet and modest life for us...
BEFORE: lang(Fox): 我们的生活，再也谈不上安静谦逊了…… 
AFTER: lang(Fox): 我们从前平静、简朴的生活，就这样一去不返了…… 
CONTROL L41 cut(0.06): FenfenB06
CONTROL L42 rewind!
ROW CAT:O875dd288abc90346e539 | L43 | no manual edit
EN: Yes, our very home seemed destined to fall under the cruel fist of Traeh.
BEFORE: lang(Fox): 没错，我们的家园仿佛注定落入特蕾的残暴铁拳。
AFTER: lang(Fox): 没错，我们的家园仿佛注定落入特蕾的残暴铁拳。
ROW CAT:O77ba4f507fd03ac4580f | L44 | no manual edit
EN: It was a level of cruelty that was unknown in the long history of us Fenfen
BEFORE: lang(Fox): 这种残酷在我们Fenfen的漫长历史上前所未见
AFTER: lang(Fox): 这种残酷在我们Fenfen的漫长历史上前所未见
ROW CAT:O2d76260a8b221350040d | L45 | no manual edit
EN: and it seemed as if all hope were lost...
BEFORE: lang(Fox): 而一切希望仿佛都已不复存在……
AFTER: lang(Fox): 而一切希望仿佛都已不复存在……
CONTROL L47 wait: 0.2
CONTROL L48 fadeout(1.0, 1.0, 4)
### P01-027 | action=apply
原问题：modest life是简朴生活，不是生活谦逊；家本身不是阴影，整句应说家园阴暗处藏身。保留Fox的经历叙述，不升级全知。
本轮理由：modest life为简朴生活而非谦逊；家园阴暗处藏身接未藏者被奴役。沿现有槽保留自然意群，中间奴役句已通顺不再改，保持Fenfen自述与征服者差遣，不添抓捕动作。
EDIT_IDS ["E01-065", "E01-066"]

## SCde64a3347a222a67 | sfw | vsn/f_AgentFZ5/script.vsn | vsn/f_AgentFZ5/script.vsn
CONTROL L1 music: FenfenBGM
CONTROL L3 snap: FenfenIntro01Female
CONTROL L4 rewind!
ROW SFW1a15edd75322d015053e0552 | L5 | no manual edit
EN: Oh brave hero, thank you for rescuing me and proving your courage.
BEFORE: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
AFTER: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFWde95ec349ade82bfd0de77c2 | L6 | no manual edit
EN: Now, place your hands upon mine.
BEFORE: lang(Fox): 现在，把你的双手放到我的手上。
AFTER: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFWd6c9a4fb6d8ab6d91c9eca76 | L7 | no manual edit
EN: Turn your mind inward and witness the events that have shaped these lands...
BEFORE: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
AFTER: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L10 cut(0.06): FenfenE01
CONTROL L11 rewind!
ROW SFW1763b33c782a9254d9104062 | L12 | no manual edit
EN: As us Fenfen strove to rebuild our home and drive out the remnants of evil
BEFORE: lang(Fox): 当我们Fenfen奋力重建家园、驱逐邪恶残部时，
AFTER: lang(Fox): 当我们Fenfen奋力重建家园、驱逐邪恶残部时，
ROW SFW9d124cf7a2efd95a4d9800a5 | L13 | no manual edit
EN: some of us looked up into the sky and saw a shooting star coming down.
BEFORE: lang(Fox): 我们中有些人仰望天空，看见一颗流星正坠落而下。
AFTER: lang(Fox): 我们中有些人仰望天空，看见一颗流星正坠落而下。
ROW SFWc733233cb65b22d3556b588f | L14 | no manual edit
EN: Perhaps Fate had sent us a hero, with which we could regain our peace?
BEFORE: lang(Fox): 也许是命运给我们派来了一位英雄，好让我们重获和平？
AFTER: lang(Fox): 也许是命运给我们派来了一位英雄，好让我们重获和平？
CONTROL L16 cut(0.06): FenfenE02
CONTROL L17 rewind!
ROW SFWc51b6d96a52b47532a213a8e | L18 | no manual edit
EN: Or perhaps Fate had a more sinister joke to play on us suffering Fenfen
BEFORE: lang(Fox): 又或许，命运对受苦的我们Fenfen还有更阴险的玩笑要开，
AFTER: lang(Fox): 又或许，命运对受苦的我们Fenfen还有更阴险的玩笑要开，
ROW SFWae3ea33ae72b936a6f5836c7 | L19 | no manual edit
EN: for this visitor from the stars did not land on our planet proper...
BEFORE: lang(Fox): 因为这位来自群星的访客，并没有降落在星球本体上……
AFTER: lang(Fox): 因为这位来自群星的访客，并没有降落在星球本体上……
ROW SFWf448bf2cf3b2105430675f5c | L20 | no manual edit
EN: ...instead, they landed on the satellite rock that held Traeh's prison!
BEFORE: lang(Fox): ……而是落在了关押特蕾的囚牢所在的那座卫星岩上！
AFTER: lang(Fox): ……而是落在了关押特蕾的囚牢所在的那座卫星岩上！
CONTROL L22 cut(0.06): FenfenE03
CONTROL L23 rewind!
ROW SFW9b38cb8d192e7d5e99b8d879 | L24 | no manual edit
EN: As if destined for only a single purpose, the interstellar interloper
BEFORE: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
AFTER: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
ROW SFW629e454d01a54e4bf0d719ab | L25 | no manual edit
EN: made their way to the very core of Traeh's prison. 
BEFORE: lang(Fox): 一路来到了关押特蕾的囚牢核心。 
AFTER: lang(Fox): 一路来到了关押特蕾的囚牢核心。 
ROW SFWd5fa57463f6b6d00b4f714e6 | L26 | no manual edit
EN: Had her psychic tendrils found their way into a poor fool's mind?
BEFORE: lang(Fox): 她的灵能触须，是否已经探入了某个可怜虫的脑中？
AFTER: lang(Fox): 她的灵能触须，是否已经探入了某个可怜虫的脑中？
CONTROL L28 cut(0.06): FenfenE04
CONTROL L29 rewind!
ROW SFWf22d973e836f41586d753cf7 | L30 | no manual edit
EN: There is no way to know if it was dark ESPer power at work or merely curiosity 
BEFORE: lang(Fox): 无从得知，究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇， 
AFTER: lang(Fox): 无从得知，究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇， 
ROW SFW221d2528aea571150ddae37a | L31 | no manual edit
EN: but this traveler made contact with the crystal prison that held Traeh...
BEFORE: lang(Fox): 但这位旅者确实触碰到了关押特蕾的水晶囚牢……
AFTER: lang(Fox): 但这位旅者确实触碰到了关押特蕾的水晶囚牢……
CONTROL L33 cut(0.06): FenfenE05
CONTROL L34 rewind!
ROW SFWe8611f80512467a444052b83 | L35 | no manual edit
EN: ...and so they became undone, unable to resist the dark ESPer forces.
BEFORE: lang(Fox): ……就这样，这名旅者崩溃了，无力抵挡黑暗的超能力者力量。
AFTER: lang(Fox): ……就这样，这名旅者崩溃了，无力抵挡黑暗的超能力者力量。
ROW SFW445519cb56eb078c7f834b59 | L36 | no manual edit
EN: Power and pain coursed through the poor explorer 
BEFORE: lang(Fox): 力量与痛苦奔涌过这名可怜的探索者全身， 
AFTER: lang(Fox): 力量与痛苦奔涌过这名可怜的探索者全身， 
ROW SFW79a7cfb7c4f1b9f13529632a | L37 | no manual edit
EN: until their mind was no longer their own.
BEFORE: lang(Fox): 直到那心智，再也不属于自己。
AFTER: lang(Fox): 直到那心智，再也不属于自己。
CONTROL L39 cut(0.06): FenfenE06
CONTROL L40 rewind!
ROW SFWdeadc2a8ac2ca860077c0086 | L41 | EDIT E01-067
EN: No, from that moment forth they answered to a darker power...
BEFORE: lang(Fox): 不，从那一刻起，其便听命于一股更黑暗的力量……
AFTER: lang(Fox): 不，从那一刻起，那位旅者便听命于一股更黑暗的力量……
ROW SFW0ec990c8871d095be01d3c2c | L42 | EDIT E01-068
EN: They did as Traeh commanded!
BEFORE: lang(Fox): 特蕾吩咐什么，其便做什么！
AFTER: lang(Fox): 特蕾吩咐什么，那位旅者就照做！
CONTROL L44 wait: 0.2
CONTROL L45 fadeout(1.0, 1.0, 4)
### P01-028 | action=apply
原问题：其便在中文口头记忆讲述中明显生硬，且隐去人的被支配状态；用旅者承接前段，不猜性别或身份。
本轮理由：完整前文为单一旅者心智被夺，不为性别/身份下结论；两句用那位旅者替文言“其”，保留听命与执行命令，不添加只能/主动意愿。
EDIT_IDS ["E01-067", "E01-068"]

## SCa2d5d1f6d5944926 | nsfw | vsn/f_EndingGood/script.vsn | vsn/f_EndingGood/script.vsn
CONTROL L1 music: CutsceneE
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): Ending01
CONTROL L4 rewind!
ROW CAT:Of28962646a30bb2f30da | L5 | no manual edit
EN: Nooo! Curse you damn Yiffai siblings!
BEFORE: text: 不——！诅咒你们这该死的伊法伊姐弟！
AFTER: text: 不——！诅咒你们这该死的伊法伊姐弟！
ROW CAT:Od2b282ee14234cadc6c6 | L6 | no manual edit
EN: I was supposed to rule the world... no... the Galaxy!
BEFORE: text: 我本该统治世界的……不……是整个银河！ 
AFTER: text: 我本该统治世界的……不……是整个银河！ 
ROW CAT:O261be934e39fce0c0ccc | L7 | no manual edit
EN: And now... now...!
BEFORE: text: 而现在……现在……！
AFTER: text: 而现在……现在……！
ROW CAT:O80475490fe47332a65a4 | L8 | no manual edit
EN: ...............!!!
BEFORE: text: ...............!!!
AFTER: text: ...............!!!
ROW CAT:Od4455cc164860d2b9c53 | L9 | no manual edit
EN: GAAAAARRRRRRRGGGGGGGHGHHHH!
BEFORE: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
AFTER: text: 嘎啊啊啊——呜噢噢噢——呃呃呃！
CONTROL L11 fadecut(0.266, 2): Ending02
CONTROL L12 rewind!
ROW CAT:O3d698609a6418af33b67 | L13 | no manual edit
EN: Wow sis, did we really just... save a whole planet?
BEFORE: text: 哇，老姐，我们刚刚真的……拯救了一整颗星球？
AFTER: text: 哇，老姐，我们刚刚真的……拯救了一整颗星球？
ROW CAT:O12987d71a89056374c88 | L14 | no manual edit
EN: Yeah lil bro, I think we did! Par for the course on my missions, really.
BEFORE: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
AFTER: text: 是啊，小弟，我想是的！在我执行的任务里这都算家常便饭了。
ROW CAT:O5bef5a80aaf025967f0f | L15 | no manual edit
EN: Buuut pretty impressive for my baby bro's first real mission, so good going!
BEFORE: text: 不过——对我家小弟的第一次真正任务来说，已经很厉害了，干得漂亮！
AFTER: text: 不过——对我家小弟的第一次真正任务来说，已经很厉害了，干得漂亮！
CONTROL L17 fadecut(0.266, 2): Ending03
CONTROL L18 rewind!
ROW CAT:Ocf334183a7064dfc73d1 | L19 | no manual edit
EN: The heroes of Tutone! They return!
BEFORE: text: 图托恩的英雄们！他们回来了！
AFTER: text: 图托恩的英雄们！他们回来了！
ROW CAT:O643276aba067e4c9fe99 | L20 | no manual edit
EN: Traeh has been defeated, her psychic disturbances are no more and her minions flee!
BEFORE: text: 特蕾已经被击败，她的灵能扰动不复存在，她的爪牙正在逃窜！
AFTER: text: 特蕾已经被击败，她的灵能扰动不复存在，她的爪牙正在逃窜！
ROW CAT:O5f008977140c8380ca20 | L21 | no manual edit
EN: Cheers for the heroes!
BEFORE: text: 为英雄们欢呼吧！
AFTER: text: 为英雄们欢呼吧！
CONTROL L23 fadecut(0.266, 2): Ending04A
CONTROL L24 rewind!
ROW CAT:Ofcaf4f3ba3ebc9a993e5 | L25 | no manual edit
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: YIP！YIP！好耶！
ROW CAT:O41a605e9b487a5783c75 | L26 | no manual edit
EN: YIP! YIP! HOORAY!
BEFORE: text: YIP！YIP！好耶！
AFTER: text: YIP！YIP！好耶！
ROW CAT:O57a4e52c797a3263d838 | L27 | no manual edit
EN: BLESSED BE THE COSMOBREEDERS, SAVIORS OF OUR PLANET!
BEFORE: text: 愿宇宙育种者受颂，我们星球的救星！
AFTER: text: 愿宇宙育种者受颂，我们星球的救星！
CONTROL L29 snap: Ending04B
ROW CAT:O63eccd2485abcad04d3d | L30 | no manual edit
EN: Wow, good going you two! Clearing out a whole planet of baddies...
BEFORE: text: 哇，你们俩真棒！把整颗星球的坏蛋都清了个遍……
AFTER: text: 哇，你们俩真棒！把整颗星球的坏蛋都清了个遍……
ROW CAT:Oa20a109f9b56a07e7853 | L31 | no manual edit
EN: That's definitely gonna help the local fauna get back on track!
BEFORE: text: 这肯定能帮当地动物族群重回正轨！
AFTER: text: 这肯定能帮当地动物族群重回正轨！
CONTROL L33 snap: Ending04C
ROW CAT:O8393772061427b6ff474 | L34 | no manual edit
EN: I knew you two could do it. Never had a doubt in my mind.
BEFORE: text: 我就知道你们俩能行。我从没怀疑过。
AFTER: text: 我就知道你们俩能行。我从没怀疑过。
ROW CAT:Oa8125b4b105236951d68 | L35 | no manual edit
EN: Not even when one of you went AWOL and stopped responding to all communica-
BEFORE: text: 就连你们中有人擅离职守、不再回应任何通——
AFTER: text: 就连你们中有人擅离职守、不再回应任何通——
ROW CAT:O9b102edb47da0d82ef05 | L36 | no manual edit
EN: -Ahem...
BEFORE: text: -嗯哼……
AFTER: text: -嗯哼……
ROW CAT:Oa03a6fd6435340e73f54 | L37 | no manual edit
EN: This will definitely be a good report to have filed away, Agents!
BEFORE: text: 这份报告绝对值得归档留存，特工们！
AFTER: text: 这份报告绝对值得归档留存，特工们！
CONTROL L39 snap: Ending04D
ROW CAT:Oa1b9076fadb1ae699809 | L40 | EDIT E01-069
EN: Nice one, grrrrl! You and your pup brother really cleaned up down there!
BEFORE: text: 真有你的，grrrrl！你和你弟弟在下面可把坏蛋清了个遍！
AFTER: text: 真有你的，姑——娘！你和你那小狗崽弟弟，把下面的坏蛋收拾得够彻底！
ROW CAT:O84ff961632ed382a8b6d | L41 | no manual edit
EN: Just don't forget about us at HQ when all the fame goes to your heads, alright?
BEFORE: text: 等名声让你们飘飘然的时候，可别忘了我们总部的人，好吗？
AFTER: text: 等名声让你们飘飘然的时候，可别忘了我们总部的人，好吗？
CONTROL L43 snap: Ending04E
ROW CAT:O378ddc367c0dcd45230b | L44 | no manual edit
EN: HOORAH FOR YIFFANY AND YIFFAI! STAR COSMOBREEDERS!
BEFORE: text: 为伊法妮和伊法伊欢呼！明星宇宙育种者！
AFTER: text: 为伊法妮和伊法伊欢呼！明星宇宙育种者！
ROW CAT:O8ab1961c6882e2ad8dfb | L45 | no manual edit
EN: H O O R A Y ! ! !
BEFORE: text: 好 耶 ！ ！ ！
AFTER: text: 好 耶 ！ ！ ！
CONTROL L47 fadecut(0.266, 2): Ending05
CONTROL L48 rewind!
ROW CAT:O54310133683eb09acefb | L49 | no manual edit
EN: Heh, how about that, sis? We made a pretty good team, didn't we?
BEFORE: text: 嘿，瞧见没，老姐？我们配合得挺不错，不是吗？
AFTER: text: 嘿，瞧见没，老姐？我们配合得挺不错，不是吗？
ROW CAT:O190c6fd296b57b703b78 | L50 | no manual edit
EN: Wellll... you did alright, bro.
BEFORE: text: 嗯——……你还行啦，老弟。 
AFTER: text: 嗯——……你还行啦，老弟。 
ROW CAT:Oac2505879521dbda2d20 | L51 | no manual edit
EN: ...for a pup.
BEFORE: text: ……就一只小崽子而言。 
AFTER: text: ……就一只小崽子而言。 
CONTROL L53 fadecut(0.266, 2): Black
CONTROL L54 rewind!
ROW CAT:O217c8ef12644fc162c93 | L55 | no manual edit
EN: [SO ENDS THE REPORT ON PLANET TUTONE.]
BEFORE: text: [图托恩星球的报告到此结束。]
AFTER: text: [图托恩星球的报告到此结束。]
ROW CAT:Of2fe5c5e0569abc89ad4 | L56 | EDIT E01-070
EN: [A PLANET WITH A TUMULTUOUS HISTORY, FACING THE GREATEST CHALLENGES OF ITS TIME]
BEFORE: text: [这是一颗历史动荡的星球，直面着它所处时代最严峻的挑战]
AFTER: text: [这颗历经动荡的星球，面临着这个时代最严峻的挑战，]
ROW CAT:O396f7b35d356aa3ef852 | L57 | EDIT E01-071
EN: [SAVED BY THE VALIANT EFFORTS OF TWO BRAVE COSMOBREEDERS:]
BEFORE: text: [被两位勇敢的宇宙育种者奋勇拯救：]
AFTER: text: [最终由两位勇敢的宇宙育种者奋力拯救：]
ROW CAT:O809514c7c67bbbb6524d | L58 | EDIT E01-072
EN: [YIFFANY YIFFAI, ELDER SISTER AND SEASONED VETERAN WITH UNMATCHED COMBAT SKILL]
BEFORE: text: [伊法妮·伊法伊，姐姐，久经沙场的老兵，拥有无与伦比的战斗技巧]
AFTER: text: [姐姐伊法妮·伊法伊，身经百战，战技无人能及；]
ROW CAT:O75cd8b6da7823140cbda | L59 | EDIT E01-073
EN: [AND YIFFAI YIFFAI, THE YOUNGER BROTHER PRODIGY WITH UNENDING ENTHUSIASM]
BEFORE: text: [以及伊法伊·伊法伊，热情永不枯竭的天才弟弟]
AFTER: text: [弟弟伊法伊·伊法伊，天赋出众，热情不竭。]
ROW CAT:O67d0e21024372bc9cc46 | L60 | no manual edit
EN: [WITH THE TWO OF THEM TEAMED UP, THERE'S NO MISSION THAT THEY CAN'T HANDLE]
BEFORE: text: [两人携手，没有他们应付不来的任务]
AFTER: text: [两人携手，没有他们应付不来的任务]
ROW CAT:O7d47a8f4843f68747af5 | L61 | EDIT E01-074
EN: [AND THE PPP IS PROUD TO HAVE THEM AS AGENTS.]                      -SIGNED, BOSSU
BEFORE: text: [PPP很荣幸有他们两位这样出色的特工。]                      -署名，Bossu
AFTER: text: [PPP以拥有这两位特工为荣。]                      -署名，Bossu
CONTROL L63 fademusic(0.0, 1.0)
CONTROL L64 fadeout(1.0, 1.0, 4)
### P01-029 | action=apply
原问题：grrrrl是Tomcat拖音称呼，不是人名；当前英文残留令祝贺对话突然中断。熟人玩笑但不加固定喵口癖。
本轮理由：grrrrl为拖音熟人称呼非名字；转成姑——娘并保留pup brother局部逗弄。下一节点名声飘然与勿忘总部已通顺，不为凑改动重写。
EDIT_IDS ["E01-069"]
### P01-030 | action=apply
原问题：当前报告被两位…拯救悬挂被动句，姐姐/老兵/技巧名词堆叠；整段是Bossu署名总结，需按中文报告连贯收束，保留原文夸赞而不拿夸赞证明精确履历。
本轮理由：报告的星球—挑战—获救在原连续槽理顺，避免悬空被动；保留“这个时代”而不升级成有史以来，seasoned/unmatched及prodigy/enthusiasm均保留。全名重复、姐弟长幼、两人任务夸赞和署名空格都保护；不将报告赞辞认证为旁白履历。
EDIT_IDS ["E01-070", "E01-071", "E01-072", "E01-073", "E01-074"]

## SCfd5dbc6a5b6f9666 | sfw | vsn/m_ClassicWerepup/script.vsn | vsn/m_ClassicWerepup/script.vsn
CONTROL L1 music: CutsceneX
CONTROL L2 fade(9, 0, 1)
CONTROL L3 fadein(1.0, 4): ClassicAreaB01A
CONTROL L4 rewind!
ROW SFWec54afa2e9a17e671bf79bcc | L5 | no manual edit
EN: Awww, look at you! You're adorable! And small!
BEFORE: text: 哎呀，瞧瞧你！真可爱！还这么小！
AFTER: text: 哎呀，瞧瞧你！真可爱！还这么小！
ROW SFW926fd910da06f717f586a1dd | L6 | no manual edit
EN: What made you decide to start roughhousing with me, lil guy?
BEFORE: text: 小家伙，你怎么会想来跟我打闹呢？
AFTER: text: 小家伙，你怎么会想来跟我打闹呢？
CONTROL L8 fadecut(0.266, 2): Asset01
CONTROL L9 rewind!
ROW SFWe1d432f59992a887a662d122 | L10 | no manual edit
EN: You're lucky that it was only me that you started tussling with
BEFORE: text: 算你走运，你惹上的只是我，
AFTER: text: 算你走运，你惹上的只是我，
ROW SFW805dcdd33457c5e75f8bdf64 | L11 | no manual edit
EN: and not any of the more vicious creatures down here!
BEFORE: text: 而不是这下面那些更凶狠的生物！
AFTER: text: 而不是这下面那些更凶狠的生物！
ROW SFWe9c1cb0e864a41c152deaeed | L12 | no manual edit
EN: Some of them are pretty nasty, you know?
BEFORE: text: 有些家伙可相当凶，你知道吗？
AFTER: text: 有些家伙可相当凶，你知道吗？
CONTROL L14 fadecut(0.266, 2): Asset02
CONTROL L15 rewind!
ROW SFW19ce69bc4d555031958364e9 | L16 | no manual edit
EN: Awww but you don't know what I'm going on about, do you?
BEFORE: text: 哎呀，不过你听不懂我在说什么，对吧？
AFTER: text: 哎呀，不过你听不懂我在说什么，对吧？
ROW SFWab8c72a924fa676c0fd1a4fd | L17 | EDIT E01-075
EN: A cute little guy like you just wants to run and jump around...
BEFORE: text: 你这么可爱的小家伙，就该四处跑跑跳跳……
AFTER: text: 你这么可爱的小家伙，只想四处跑跑跳跳……
ROW SFWb8abd9876513752c5372a518 | L18 | EDIT E01-076
EN: ...and that's what you should be allowed to do!
BEFORE: text: ……而你就应该能自由自在地这么做！
AFTER: text: ……就该让你自由自在地这么做才对！
CONTROL L20 fadecut(0.266, 2): ClassicAreaB01L
CONTROL L21 rewind!
ROW SFW470bb6bdbbfcd983edef9de2 | L22 | no manual edit
EN: Go on lil guy! Have more fun out there!
BEFORE: text: 去吧，小家伙！到外面多玩玩！
AFTER: text: 去吧，小家伙！到外面多玩玩！
ROW SFW26ecf22f950cd983af6b1086 | L23 | no manual edit
EN: Your big ol' uncle Yiffai will be around if you get into trouble
BEFORE: text: 要是碰上麻烦，你的伊法伊大叔就在附近，
AFTER: text: 要是碰上麻烦，你的伊法伊大叔就在附近，
ROW SFW5d90b611c4c728eb70c806bf | L24 | no manual edit
EN: so don't hesitate to bark out for help! I'll come a'runnin.
BEFORE: text: 尽管汪汪叫着求救！我会跑过来的。
AFTER: text: 尽管汪汪叫着求救！我会跑过来的。
CONTROL L26 fadecut(0.266, 2): ClassicAreaB01M
CONTROL L27 rewind!
ROW SFWc4f29441db5382d02a64a4e2 | L28 | no manual edit
EN: O-oh hey! That's some pretty mighty digging you're doing...
BEFORE: text: 哦、哦嘿！你挖得可真起劲……
AFTER: text: 哦、哦嘿！你挖得可真起劲……
ROW SFW4ebd6b0b75a8a2f88b6f9563 | L29 | no manual edit
EN: Did you forget a bone or maybe a ball or something...
BEFORE: text: 你是不是忘了骨头，或者球之类的什么东西……
AFTER: text: 你是不是忘了骨头，或者球之类的什么东西……
ROW SFWf1afc815e3c6e516bd91671f | L30 | no manual edit
EN: Or... or...
BEFORE: text: 还是……还是……
AFTER: text: 还是……还是……
CONTROL L32 fadecut(0.266, 2): ClassicAreaB01N
CONTROL L33 rewind!
ROW SFW33fabd6fe06e7ea74f3747cd | L34 | no manual edit
EN: ...or is that a Level 1 Keycard? And you're giving it to me!?
BEFORE: text: ……还是说，那是张1级门卡？而你要把它送给我！？
AFTER: text: ……还是说，那是张1级门卡？而你要把它送给我！？
ROW SFW28b100e9518977b0d7074fed | L35 | no manual edit
EN: Well heck! Ain't you just the best little nephew Uncle Yiffai could want?
BEFORE: text: 哎呀！伊法伊大叔哪还能找到比你更棒的小侄子？
AFTER: text: 哎呀！伊法伊大叔哪还能找到比你更棒的小侄子？
ROW SFW4f6066a9df5c632f70444078 | L36 | no manual edit
EN: Thanks pupperoo, I won't forget it!
BEFORE: text: 谢谢你，小狗崽，我不会忘记的！
AFTER: text: 谢谢你，小狗崽，我不会忘记的！
CONTROL L38 fadeout(1.0, 1.0, 4)
### P01-031 | action=apply
原问题：当前前句已将just wants改成就该，后句又重复应该；恢复想做—理应获准的递进。独立SFW场景，不从NSFW补年龄或回忆。
本轮理由：SFW全文just wants是想跑跳，下一句才是理应获准；恢复愿望—允许的递进，不从NSFW补年龄或成人回忆。
EDIT_IDS ["E01-075", "E01-076"]

