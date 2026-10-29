# batch-08-part05 精校工单：VSN 剧情场景脚本（结局与平行版本）（第 5／5 部分）

英文与当前中文都按整场连读；`current` 是构建候选的实际显示行（以本批参照摘录与 ORDER 记的候选为准）。
ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。

## SC409ec23e7cec48f7 | sfw | vsn/ClassicPreTitle/script.vsn | vsn/ClassicPreTitle/script.vsn
CONTROL L1  music: PreTitle
CONTROL L2  printsfx: true
CONTROL L3  fade(9, 0, 1)
CONTROL L4  fadein(0.5, 4): ClassicPreTitle01A
ROW SFWdbdbcd0b656b09661a86c076 L6 - physical_line
  EN: It is the age of faster than light travel and advanced cyber-robotics.
  ZH: auto(8.0): 这是超光速航行与先进赛博机器人技术的时代。
ROW SFWce2ad495ca09195bce02cfeb L7 - physical_line
  EN: [THE 3P ORGANIZATION] has become a driving force for space exploration.
  ZH: auto(8.0): [3P组织]已成为推动太空探索的一股重要力量。
CONTROL L9  fadeout(0.5, 0.5, 4)
CONTROL L11  fadein(0.5, 4): ClassicPretitle01B
ROW SFW2bca8f78a5e5eef89991e9e0 L13 - physical_line
  EN: Brave heroes are sent out by [THE 3P ORGANIZATION] to gather information.
  ZH: auto(8.0): [3P组织]派出英勇之士，前往各地收集情报。
ROW SFWedeacc7ee1a9a0612100692b L14 - physical_line
  EN: These [COSMOBREEDERS], as they are known, allow civilization to prosper.
  ZH: auto(8.0): 这些被称为[宇宙育种者]的英雄，让文明得以繁荣。
CONTROL L16  fadeout(0.5, 0.5, 4)
CONTROL L18  fadein(0.5, 4): ClassicPretitle01C
ROW SFW596185518a94d55c1b4f7009 L20 - physical_line
  EN: Traveling through the stars and making new discoveries is a life of adventure. 
  ZH: auto(8.0): 穿行群星，探寻未知，这就是冒险的人生。 
ROW SFW2099d32f8549a95fb54e57ab L21 - physical_line
  EN: Respected by all, many a child dreams of growing up to become a [COSMOBREEDER]
  ZH: auto(8.0): 人人敬仰，许多孩子梦想长大后成为[宇宙育种者]。
CONTROL L23  fadeout(0.5, 0.5, 4)
CONTROL L25  fadein(0.5, 4): ClassicPretitle01CToD
CONTROL L27  queue: ClassicPretitle01D
ROW SFW45c33164ea306e3ad0c0670c L28 - physical_line
  EN: Space travel and leaving the safety of home is not for the faint of heart, however.
  ZH: auto(8.0): 然而，离开安稳的家园、踏上星际旅途，绝非胆小者所能为。
CONTROL L30  sync!
ROW SFWfaee6460baf53d5462e8c3fd L32 - physical_line
  EN: For who can truly say what dangers await on distant, unknown planets...
  ZH: auto(8.0): 毕竟，谁又能说清遥远的未知星球上潜藏着什么危险……
CONTROL L34  fadeout(1.0, 1.0, 4)
CONTROL L35  wait: 2.0

## SC4d550b4a736dbb6d | nsfw | vsn/f_AgentF04/script.vsn | vsn/f_AgentF04/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L3  snap: AreaAFemale02A
CONTROL L4  rewind!
ROW CAT:Od57b1a51f3eb6ee4ec0f L5 narrator physical_line
  EN: Th-thanks! I needed that!
  ZH: text: 谢、谢谢！我正需要这个！
ROW CAT:Oc9406d45f280de641330 L6 narrator physical_line
  EN: I'm not usually this worked up, it's just that I've been locked up all alone
  ZH: text: 我平时没这么饥渴，只是一直被独自关着，再加上底下这鬼热的环境，快把我逼疯了！
ROW CAT:Oaaeeb1e89140e7fdddb5 L7 narrator physical_line
  EN: with this darn heat down here driving me crazy!
  ZH: 
CONTROL L9  cut(0.06): AreaAFemale02B
CONTROL L10  rewind!
ROW CAT:O50fe3980985d75207423 L11 narrator physical_line
  EN: I thought it was bad enough when the flames slowly licked away my uniform
  ZH: text: 火苗一点点舔掉我的制服，让我露出的地方越来越多时，我以为已经够糟了……
ROW CAT:O8b2a371360f131842d3e L12 narrator physical_line
  EN: leaving me more and more exposed...
  ZH: 
ROW CAT:Oc491f53bba366b95e425 L13 narrator physical_line
  EN: But the heat down here only seemed to get /worse/ as my poor uniform was burnt away.
  ZH: text: 可我那可怜的制服越烧越少，这里的热度反而/更甚/。
CONTROL L15  cut(0.06): AreaAFemale02C
CONTROL L16  rewind!
ROW CAT:O1e0726bab74d28a2c227 L17 narrator physical_line
  EN: By the time my bodysuit was little more than ash, I finally ran into company.
  ZH: text: 等紧身衣都快烧成灰时，我终于遇上了个伴。
ROW CAT:O0b6de20e5702d5fb31ba L18 narrator physical_line
  EN: This fella was cuddly, too! Came right in for a hug as soon as he saw me.
  ZH: text: 这家伙还挺黏人！一看见我就扑过来抱！
ROW CAT:Ob8ec2cac7f1a22f54ad6 L19 narrator physical_line
  EN: Raccoon reactions kicked in and I instinctually started to wrestle with him.
  ZH: text: 浣熊本能一下就上来了，我下意识地跟他扭打起来。
CONTROL L21  cut(0.06): AreaAFemale02D
CONTROL L22  rewind!
ROW CAT:Ob91cd2981ab35f8fb5c6 L23 narrator physical_line
  EN: Buuut after a few minutes of tussling, even my helmet and gloves got knocked off
  ZH: text: 不过才扭打了几分钟，连我的头盔和手套都被打掉了，又飞来了一大群爱抱抱的小伙子！
ROW CAT:O5dd746b30e7ecb3b9f08 L24 narrator physical_line
  EN: and a bunch of more airborne cuddly boys came by!
  ZH: 
ROW CAT:Oe6617a1e866ea46027ae L25 narrator physical_line
  EN: Actually, none of them came during the wrestling, but I was so crazed by the heat
  ZH: text: 其实摔跤时他们谁也没射，可我已经欲火焚身，那也只是早晚的事……
ROW CAT:O7cab09f5509eb34d9914 L26 narrator physical_line
  EN: that it was only gonna be a matter of time...
  ZH: 
CONTROL L28  cut(0.06): AreaAFemale02E
CONTROL L29  rewind!
ROW CAT:Of7fd34257c54175258c3 L30 narrator physical_line
  EN: ...if it weren't for someone coming in showing those Wyverns what-for!
  ZH: text: ……要不是有人赶来，好好教训了那些双足飞龙！
CONTROL L32  cut(0.06): AreaAFemale02F
CONTROL L33  rewind!
ROW CAT:O45a28cab43ee3d8ffdbc L34 narrator physical_line
  EN: I still have no idea how someone that large snuck up on me and the Wyverns
  ZH: text: 我至今不懂，那么大个家伙怎么悄悄摸近我和双足飞龙，还挺识趣，只揍我的抱抱伙伴，没动我。
ROW CAT:Of6ca9e225bd572074423 L35 narrator physical_line
  EN: and then had the good sense to only smack my cuddle buddies around and not me.
  ZH: 
ROW CAT:O70a94b20f0e2d58c25fc L36 narrator physical_line
  EN: No matter, there's only one thing that I could do with this turn of events!
  ZH: text: 无所谓！事情变成这样，我只有一件事可做！
CONTROL L38  cut(0.06): AreaAFemale02G
CONTROL L39  rewind!
ROW CAT:Of59b8aa9e87ad36614d0 L40 narrator physical_line
  EN: If that hunky hunk of meat wanted to spoil my fun with those flying fuckboys
  ZH: text: 要是那大块肌肉想搅了我和飞天炮友们的好事，那他就得负责满足我的需求。
ROW CAT:O00c22f07727bbf37e026 L41 narrator physical_line
  EN: then he was going to have to take responsibility for my needs.
  ZH: 
ROW CAT:O9692e2505d0e7b829bc7 L42 narrator physical_line
  EN: No two ways about it!
  ZH: text: 没得商量！
CONTROL L44  cut(0.06): AreaAFemale02H
CONTROL L45  rewind!
ROW CAT:O83394a87467ba5e9c5a1 L46 narrator physical_line
  EN: My groping of the big fella didn't seem to clue him in on what I was gonna do
  ZH: text: 我摸遍那大家伙，他却好像还不懂我想干什么，而且，他显然也不想聊天。
ROW CAT:Ofd0fae4025165a094026 L47 narrator physical_line
  EN: and talking sure wasn't something that he was interested in, either.
  ZH: 
ROW CAT:O838283b90c61083de47b L48 narrator physical_line
  EN: Finally, after I took a seat and showed him what EXACTLY I was trying to give him
  ZH: text: 最后，我坐下来，亮出自己到底想给他什么，他身上/某个部位/才开始明白。
ROW CAT:O0aa9b04707cdc1e29aa2 L49 narrator physical_line
  EN: did /part/ of him start to understand.
  ZH: 
CONTROL L51  cut(0.06): AreaAFemale02I
CONTROL L52  rewind!
ROW CAT:O5ad1b7cd998b9f3e6b48 L53 narrator physical_line
  EN: After his manhood got turned onto the idea, it was just a matter of time for his brain
  ZH: text: 他的鸡巴先对这主意起了劲，脑子迟早也会明白咱俩接下来要做什么。
ROW CAT:O09182c5a1253685fdbca L54 narrator physical_line
  EN: to catch up with what we were gonna do.
  ZH: 
ROW CAT:O11347012c3527c0683fb L55 narrator physical_line
  EN: Almost like a light switch getting flicked, everything seemed to dawn on the hunk
  ZH: text: 像突然开了灯似的，那猛男一下子全明白了，他一兴奋，差点把我撞到墙上！
ROW CAT:O44d145f7a224704db567 L56 narrator physical_line
  EN: and he almost slammed me into the wall in his excitement!
  ZH: 
CONTROL L58  cut(0.06): AreaAFemale02J
CONTROL L59  rewind!
ROW CAT:Ob48a6739b3b9d8f879f3 L60 narrator physical_line
  EN: ...I kinda liked that rough treatment...
  ZH: text: ……我还挺喜欢那种粗暴对待的…… 
ROW CAT:O6673ba4993252b75c569 L61 narrator physical_line
  EN: It was even better when he started fucking me just as roughly, mmh mh...!
  ZH: text: 等他也这么粗暴地开始操我，那就更爽了，嗯哼……！
ROW CAT:Ofecd7c2bc117a61a48c7 L62 narrator physical_line
  EN: Exactly what I needed after boiling away in this gosh darned heat for so long!
  ZH: text: 在这鬼热的地方煎熬这么久，这正是我需要的！
CONTROL L65  cut(0.06): AreaAFemale02L
CONTROL L66  rewind!
ROW CAT:Ofb7be3ee5773b8570e7f L67 narrator physical_line
  EN: Could have done without the part where he dumped me in this lonely cell
  ZH: text: 他那根粗鸡巴才干一轮，就把我扔进这孤零零的牢房，实在没必要嘛！我连肉结都没吃进去！
ROW CAT:O8ddfca6ec59ddb43118a L68 narrator physical_line
  EN: after only one round with that thick cock of his! I didn't even take the knot!
  ZH: 
ROW CAT:O79ee48e580dfd0fd34a6 L69 narrator physical_line
  EN: All I could do until you got here was think about what else that dog could've done
  ZH: text: 你来之前，我只能一直想，那条狗还能怎么玩我，还饥渴地蹭着这根性感的铁——
ROW CAT:Od1a09ff944b005b34944 L70 narrator physical_line
  EN: and needily grind myself against this hunky iro-
  ZH: 
ROW CAT:O396552068dd0413965eb L71 narrator physical_line
  EN: -I mean, hunk of iron...
  ZH: text: ——我是说，这块铁疙瘩……
CONTROL L73  cut(0.06): Black
CONTROL L74  rewind!
ROW CAT:O1cc75ab3709d2dae4473 L75 narrator physical_line
  EN: I'm m-mostly satisfied and ready to get back to work now, thanks again!
  ZH: text: 我基、基本满足了，能回去工作啦，再谢一次！
ROW CAT:O52edbbeed15e481c0ab9 L76 narrator physical_line
  EN: But say, where'd you find that key to the cell anyhow?
  ZH: text: 不过说起来，你到底在哪儿找到牢房钥匙的？
ROW CAT:O40a9f215a35fa0a4d90f L77 narrator physical_line
  EN: ...any hunky dogs around it...     heheh...?
  ZH: text: ……旁边有没有壮实的狗族帅哥……嘿嘿……？
CONTROL L79  fadeout(1.0, 1.0, 4)

## SC8559b2a4c2d88fb3 | nsfw | vsn/f_AgentF05/script.vsn | vsn/f_AgentF05/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L3  snap: AgentC01F01
CONTROL L4  rewind!
ROW CAT:Oda86e90cda64bacd6b96 L5 narrator physical_line
  EN: Ohmygawsh, that was like, so, totally...
  ZH: text: 天哪，刚才真是，简直太……
ROW CAT:O6461bc0ed93d382aeb99 L6 narrator physical_line
  EN: ...Amazing! But thanks for, like, saving me! Yer a doll!
  ZH: text: ……太棒了！不过，谢啦，救了我！你真贴心！
ROW CAT:Ocf637f0fcec00997ad22 L7 narrator physical_line
  EN: I feel like a totally new girl after all that happened!
  ZH: text: 经历这些事，我简直像换了个人！
ROW CAT:O672e85bd92d4626aff5d L8 narrator physical_line
  EN: Crazy to think this was the first planet I ever got, like, captured on.
  ZH: text: 想想还挺离谱的，这居然是我第一次被俘的星球。
CONTROL L10  cut(0.06): AgentC01F02
CONTROL L11  rewind!
ROW CAT:Oea9eb62c44501b26ab5b L12 narrator physical_line
  EN: I was like, totally scouting with this fox girl, Daleir! We were a team!
  ZH: text: 当时我和狐姑娘黛蕾一起侦察！咱俩一队！
ROW CAT:O08b097736a1f61c6910a L13 narrator physical_line
  EN: She's been on, like, a ton of missions, right? And she just got off of desk duty
  ZH: text: 她出过超多次任务，对吧？而且才刚结束文职工作，所以我们就搭档来找那些失踪特工啦，对吧？
ROW CAT:Oa7236e864f5126238824 L14 narrator physical_line
  EN: so we got paired up to find some of the, like, missing agents right?
  ZH: 
ROW CAT:O4b351b208d461bf4d255 L15 narrator physical_line
  EN: I don't have much combat experience so Daleir like, totally gave me some hints
  ZH: text: 我没什么战斗经验，黛蕾就给了我不少指点，比如侦察时可以不穿制服、不带装备！更加隐蔽！
ROW CAT:O1faff9cce81933e6ec74 L16 narrator physical_line
  EN: like how you can go without a uniform or equipment when scouting! For extra stealth!
  ZH: 
CONTROL L18  cut(0.06): AgentC01F03
CONTROL L19  rewind!
ROW CAT:Of0d8c958888c26dd4864 L20 narrator physical_line
  EN: It worked out real good for the first couple of scouting runs, but then...
  ZH: text: 头几次侦察顺利得很，谁知道后来……
ROW CAT:O2f991b3c8680f9c1d8b2 L21 narrator physical_line
  EN: ...one of the creepy jungle monster things caught me!
  ZH: text: ……一只吓人的丛林怪物抓住我了！ 
ROW CAT:O7c9dbd885f58ee3a8ba5 L22 narrator physical_line
  EN: I didn't see them in the pre- mission briefings so I was like, totally lost
  ZH: text: 任务简报里没见过它们，我当时完全懵了，幸好黛蕾很清醒，叫我使劲踢开他们！
ROW CAT:O25c88ef088fe0c5bcf3c L23 narrator physical_line
  EN: but thankfully Daleir had a real clear head and told me to kick away at them!
  ZH: 
CONTROL L25  cut(0.06): AgentC01F04
CONTROL L26  rewind!
ROW CAT:O20ba0e5365225e52d28a L27 narrator physical_line
  EN: S-she said I was doing, like, a real great job...
  ZH: text: 她、她说我干得，嗯，特别好……
ROW CAT:O2c9c6aec60a25ec899eb L28 narrator physical_line
  EN: But it kinda seemed like it was just turning on the creepo monster? Like WTF?
  ZH: text: 可那好像只让变态怪物更兴奋了？这他妈什么鬼？
ROW CAT:Oda2d83446b521d9e7d42 L29 narrator physical_line
  EN: I dunno, sometime during my wrestling with that beast Daleir like, disappeared?
  ZH: text: 我也不懂，跟那野兽扭打时，黛蕾不知怎么就不见了？
ROW CAT:O0bc47f5284d0ee905ca6 L30 narrator physical_line
  EN: I was crawling around trying to look for her but...
  ZH: text: 我到处爬着想找她，可是……
CONTROL L32  cut(0.06): AgentC01F05
CONTROL L33  rewind!
ROW CAT:O0db698cd0802c9c22509 L34 narrator physical_line
  EN: ...that monster lifted me up and decided I was like, a fuckbuddy now???
  ZH: text: ……那怪物把我抱起来，就直接把我当炮友了？？？
ROW CAT:Od0b6489f976dbab3c7bf L35 narrator physical_line
  EN: I have nooo clue what got him so rowdy but I continued to try fight back
  ZH: text: 完全搞不懂他怎么这么疯，不过我还是继续反抗，就像黛蕾叮嘱我的那样……
ROW CAT:O6657673d718061e86ba1 L36 narrator physical_line
  EN: just like Daleir had told me to...
  ZH: 
ROW CAT:Oc829337922042f68c68e L37 narrator physical_line
  EN: ...but it was SERIOUSLY starting to seem like a, like, bad idea!
  ZH: text: ……可我真的越来越觉得，这主意糟透了！
CONTROL L39  cut(0.06): AgentC01F06
CONTROL L40  rewind!
ROW CAT:Oc300a0ed088024fd330c L41 narrator physical_line
  EN: Even when I tried to crawl away the slimy punk couldn't, like, take a hint.
  ZH: text: 我都想爬走了，那黏糊糊的混蛋还不懂我的意思。
ROW CAT:O4849423cc84dca588348 L42 narrator physical_line
  EN: Gotta admit that his tongue was, like, pretty good...
  ZH: text: 不过得承认，他的舌头，怎么说呢，还挺厉害……
ROW CAT:O2f19495d12af1cf861d3 L43 narrator physical_line
  EN: Real slimy, but in a /fun/ way, you know? Like, not a gross sort of way that...
  ZH: text: 滑溜溜的，但滑得/有趣/，懂吧？不是恶心的那种……
ROW CAT:O0ecc15bc3fc81126fe30 L44 narrator physical_line
  EN: ...no wait, no getting distracted!
  ZH: text: ……不对，等等，不能分心！
CONTROL L46  cut(0.06): AgentC01F07
CONTROL L47  rewind!
ROW CAT:Obec05c9dce168c5ce7c4 L48 narrator physical_line
  EN: Yeah I finally got tired of the guy after, like, not seeing Daleir around
  ZH: text: 是啊，一直没见黛蕾回来，我终于腻了那家伙，心想是时候亲爪处理这件事了！
ROW CAT:Oed32d7b1a30b242db624 L49 narrator physical_line
  EN: figured it was time to take things into my own paws!
  ZH: 
ROW CAT:O5cddc7fd0c3f5c021d4a L50 narrator physical_line
  EN: ...so I took a branch into my own paws!
  ZH: text: ……所以我就亲爪抄起一根树枝！
ROW CAT:O1e9eff8dbd095d46d7b2 L51 narrator physical_line
  EN: ...and then I, like, applied the branch to the creepo guy's head!
  ZH: text: ……然后嘛，我就把树枝招呼到那恶心家伙脑袋上！ 
CONTROL L53  cut(0.06): AgentC01F08
CONTROL L54  rewind!
ROW CAT:O3ac2ae494c62b6550925 L55 narrator physical_line
  EN: A good smack got them like, totally dazed. And off I, like, went!
  ZH: text: 狠狠一敲，就把他们敲晕乎了。然后我就溜啦！
ROW CAT:O89f7f8e76169c902eba3 L56 narrator physical_line
  EN: They're like, creepy and crawly and got a vicious tail, but those monsters
  ZH: text: 那些怪物爬来爬去怪吓人的，尾巴还很凶，不过它们追起姑娘来可就差——远了。
ROW CAT:Od45d7aeb1d20f59feb39 L57 narrator physical_line
  EN: aren't real good at following a girl at alllllll.
  ZH: 
ROW CAT:Odc0d596c6bafd5225a76 L58 narrator physical_line
  EN: Lost them pretty easily by dipping into this old unused cell!
  ZH: text: 往这间废旧牢房一钻，就轻松甩掉他们啦！
CONTROL L60  cut(0.06): AgentC01F09
CONTROL L61  rewind!
ROW CAT:O75b167fdff0b950e5372 L62 narrator physical_line
  EN: Aaaaand then I found out why it was old and unused when these, like, tentacles
  ZH: text: 然后——我才搞懂这间旧牢房为何一直空置，那些触手竟然就开始缠住我，抚摸起来！
ROW CAT:O4f88bc94e244d3f46e59 L63 narrator physical_line
  EN: just started wrapping around and caressing me!
  ZH: 
ROW CAT:Oe2bfd091c84c8f69affe L64 narrator physical_line
  EN: I swear, ohmygawsh, that these things were actually horny! Like, for real!
  ZH: text: 天呐，我发誓，那些东西真会发情！真的！
CONTROL L66  cut(0.06): AgentC01F10
CONTROL L67  rewind!
ROW CAT:O98d4f143b2cf169a87fe L68 narrator physical_line
  EN: I've just been stuck here for like, hours? Days? I can't really remember...
  ZH: text: 我困在这里多久了，几小时？几天？真记不清了……
ROW CAT:O8b2e0e96d962e2d4912f L69 narrator physical_line
  EN: ...it's just been like, orgasm after orgasm...
  ZH: text: ……就那么，高潮接着高潮……
ROW CAT:Obc8700ad0b1069ce264e L70 narrator physical_line
  EN: Almost like being surrounded by a wall of those monsters' tongues, you know?
  ZH: text: 简直像被那些怪物的舌头围成的墙裹住了，懂吗？ 
ROW CAT:O4601e78347bae4f3c4b4 L71 narrator physical_line
  EN: Like, it sounds gross, but it also felt really good and then...
  ZH: text: 就是，听着挺恶心，可感觉真的很舒服，然后……
CONTROL L73  cut(0.06): Black
CONTROL L74  rewind!
ROW CAT:O9fb530c44d847f3f59d4 L75 narrator physical_line
  EN: ...hey wait, didn't I have a mission I was supposed to be doing?
  ZH: text: ……哎等等，我是不是还有任务要做来着？ 
ROW CAT:Obff4a8b47a1b1d34dbef L76 narrator physical_line
  EN: What was it that, like, I was supposed to even be helping out with...
  ZH: text: 我本来到底是要帮忙干什么来着……
ROW CAT:O89dc41f8277a87e8f6f3 L77 narrator physical_line
  EN: Daleir just said that she was gonna get us taken care of, but then this happened
  ZH: text: 黛蕾说她会把咱们安顿好，结果就出了这事，所以剩下的工作就交给你和她啦！
ROW CAT:Oe4c0943d06bfb071cd11 L78 narrator physical_line
  EN: so I guess I'll leave the rest of the job up to you and her!
  ZH: 
CONTROL L80  fadeout(1.0, 1.0, 4)

## SC960d377d64349226 | nsfw | vsn/f_AgentF06/script.vsn | vsn/f_AgentF06/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L3  snap: AgentC02F01
CONTROL L4  rewind!
ROW CAT:O074b0061b33542b7204e L5 narrator physical_line
  EN: Awww, you didn't have to beat up those lil ol' tentacles!
  ZH: text: 哎呀，你不用揍那些小触手的！ 
ROW CAT:O29ae9d62ceba2ea3d567 L6 narrator physical_line
  EN: They weren't hurting me, just helping to keep me warm and cozy, eh-heh!
  ZH: text: 它们没伤我，只是让我暖暖和和、舒舒服服的，嘿嘿！
ROW CAT:O9c7b2a3fcac69848a483 L7 narrator physical_line
  EN: I guuuuess I oughtta give you the report while I'm out, huh? So here ya go:
  ZH: text: 我想——既然脱身了，总该把报告交给你吧？喏，拿好：
CONTROL L9  cut(0.06):AgentC01F02
CONTROL L10  rewind!
ROW CAT:Oe3ad7a379fb99ca55e45 L11 narrator physical_line
  EN: Not sure where she is now, but I actually started out down here with a partner!
  ZH: text: 不知她现在在哪，但我刚来这下面时，其实有个搭档！
ROW CAT:O30dbbb5e43a920faa6ce L12 narrator physical_line
  EN: Erma the otter and me, Daleir the fox! What a team we were!
  ZH: text: 水獭艾玛，还有我，狐狸黛蕾！多棒的搭档啊！ 
ROW CAT:O31b14220809228310f6c L13 narrator physical_line
  EN: I've been on lotsa missions and fights but Erma never saw much combat...
  ZH: text: 我出过不少任务，打过不少仗，可艾玛没怎么实战过……
ROW CAT:O5c1ea29a7a26b827f669 L14 narrator physical_line
  EN: ...so I was around to give her some pointers in case we ran into anyone!
  ZH: text: ……所以我陪着她，遇上谁也好指点她几招！ 
CONTROL L16  cut(0.06):Black
CONTROL L17  rewind!
ROW CAT:O327617c73f0132c34e83 L18 narrator physical_line
  EN: I can't remember whaaaat exactly happened, but we got separated at some point...
  ZH: text: 具体发——生了什么我记不清了，反正我们后来走散了……
ROW CAT:Odbf62c8dffeaf864c2de L19 narrator physical_line
  EN: ...yeah, that's it... I started looking around for her...
  ZH: text: ……对，就是这样……我开始到处找她……
ROW CAT:Oc987cbfc0606d7c8c012 L20 narrator physical_line
  EN: Eventually I heard her cry out, so I tried to quietly make my way to her!
  ZH: text: 后来听见她叫，我就试着悄悄摸过去！
CONTROL L22  cut(0.06): AgentC02F02
CONTROL L23  rewind!
ROW CAT:Ofb5d314a92e18949798a L24 narrator physical_line
  EN: And, well, wouldn't you know it! I didn't have to give Erma any pointers at all!
  ZH: text: 结果你猜怎么着！我压根不用指点艾玛！
ROW CAT:Oc80acd60f150d9024132 L25 narrator physical_line
  EN: The girl was a natural at Cosmobreeding!
  ZH: text: 那姑娘做宇宙育种简直是天生的！
ROW CAT:O77e2922a5dfff1c6d4c8 L26 narrator physical_line
  EN: She knew how to kick and struggle juuust right to arouse the local fauna
  ZH: text: 她踢腿挣扎的劲儿恰到好处，正好能挑起当地生物的欲火，可出发前的简报里压根没提过这物种！哇！
ROW CAT:Oe0289fec12b0eb7ef98c L27 narrator physical_line
  EN: even though this species wasn't even in any of our pre-sortie briefings! Wow!
  ZH: 
CONTROL L29  cut(0.06): AgentC02F03
CONTROL L30  rewind!
ROW CAT:O6c2cd9e5527a8e6e76b6 L31 narrator physical_line
  EN: Seeing the way she egged on this alien creature with her rough foreplay...
  ZH: text: 看她用粗暴的前戏挑逗那外星生物的样子……
ROW CAT:Oea5141006a4eace1ae81 L32 narrator physical_line
  EN: ...and seeing how hard that creature was getting... eh-hehehe...
  ZH: text: ……再看看那异星生物硬成什么样……诶嘿嘿嘿……
ROW CAT:O2e0e205bb624b467883b L33 narrator physical_line
  EN: ...I knew I had to find myself one of them boys!
  ZH: text: ……我就知道，得找一个那样的汉子！
CONTROL L35  cut(0.06): AgentC02F04
CONTROL L36  rewind!
ROW CAT:O3623bad682528dca3060 L37 narrator physical_line
  EN: After trudging around loudly, I finally found a lone creepy crawly buddy
  ZH: text: 我踩着响步走了好久，终于找到一个落单的虫虫伙伴，于是我慢慢悠悠、和和气气地让他发现了我。
ROW CAT:O533463d4b3a0740c6dab L38 narrator physical_line
  EN: so I made myself known to him, nice and slowly-like.
  ZH: 
ROW CAT:O00214dc1f3fb6ae59e2b L39 narrator physical_line
  EN: It's important not to look too aggressive, when you're trying to get cosmobred!
  ZH: text: 想让人给自己育种，可千万别显得太凶！
ROW CAT:O79a817eedffffd0be84e L40 narrator physical_line
  EN: Definitely didn't want him to think I was challenging him to a fight!!! At all!
  ZH: text: 我绝不想让他以为我在挑衅！！！一点也不想！
CONTROL L42  cut(0.06): AgentC02F05
CONTROL L43  rewind!
ROW CAT:O3716acfa5463901d45b3 L44 narrator physical_line
  EN: Despite my attempts to be nice and friendly I could tell that my would-be friend
  ZH: text: 尽管我努力友好相待，可我看得出这位准朋友没打算让我这么容易就爽到……诶嘿……
ROW CAT:O91a06a90f4a94df940bf L45 narrator physical_line
  EN: was not about to let me get off easily... Eh-heh...
  ZH: 
ROW CAT:Oa70cff3a9f4a8fb1b066 L46 narrator physical_line
  EN: I was gonna have to work to get off this time! I mean, get away this time!!!
  ZH: text: 这回想爽到可得卖力了！我是说，想脱身！！！
CONTROL L48  cut(0.06): AgentC02F06
CONTROL L49  rewind!
ROW CAT:Oe358296b190b222ac5f7 L50 narrator physical_line
  EN: One blood-curdling scream from the alien later and I found myself on my back!
  ZH: text: 那外星生物一声骇人的尖叫，我就被掀翻在地！
ROW CAT:O8b923c7c6e3f201463fb L51 narrator physical_line
  EN: Wow could these boys move fast, I'd hate to come across one in the dark.
  ZH: text: 哇，这帮家伙动作真快，我可不想在暗处碰上其中一只。
ROW CAT:Of826677db2b056778869 L52 narrator physical_line
  EN: He'd be on top of you and pounding away before you even saw him...
  ZH: text: 你还没看见他，他就已经压着你猛干了……
ROW CAT:O4026d1293297f086baa2 L53 narrator physical_line
  EN: -Anyway! He was real grabby, and I had to do all I could to try to beat him off!
  ZH: text: ——总之！他手脚很不老实，我只好使尽浑身解数把他打退！
CONTROL L55  cut(0.06): AgentC02F07
CONTROL L56  rewind!
ROW CAT:O874ad484601b18d01773 L57 narrator physical_line
  EN: After a few minutes of clawing and kicking, I turned and hiked my tail-
  ZH: text: 又抓又踢了几分钟后，我转身翘起尾巴—— 
ROW CAT:O3c9c5ddc74a101a03d69 L58 narrator physical_line
  EN: -I mean, turned over and tried to scramble away...!
  ZH: text: ——我是说，翻过身想爬走……！
ROW CAT:O886c88e08a1915e7b275 L59 narrator physical_line
  EN: Only too late did I realize I had started to follow Erma's example... heh...
  ZH: text: 等我发现自己开始学艾玛那样时，已经太迟了……嘿……
ROW CAT:Oe003aea28ad1ba363612 L60 narrator physical_line
  EN: ...the example she set totally on her own all by herself like a natural!!!
  ZH: text: ……她完全自发、独立、无师自通树立的榜样！！！
CONTROL L62  cut(0.06): AgentC02F08
CONTROL L63  rewind!
ROW CAT:Oddb02aeb1b3361a19844 L64 narrator physical_line
  EN: These alien creatures really don't mess around, once you stop fighting back
  ZH: text: 这些异星生物可真不含糊，你一停止反抗，他们就抓住你的胯、肚子……反正哪儿都抓！
ROW CAT:O246ce6c2515722f1f551 L65 narrator physical_line
  EN: they'll just grab you by the hips or belly... or anywhere, really!
  ZH: 
ROW CAT:O4d76abd96c17549df632 L66 narrator physical_line
  EN: They'll scratch up your hips a bit if you aren't careful...
  ZH: text: 稍不留神，他们就会把你的胯抓花……
ROW CAT:Od74db93c1e725b2f16e7 L67 narrator physical_line
  EN: ...or if you want them to...
  ZH: text: ……或者你就想让他们挠……
ROW CAT:O24dab7fe935395e0055a L68 narrator physical_line
  EN: ...but then their ridged cocks will just jam inside of you mercilessly!
  ZH: text: ……可接着，那些带棱的鸡巴就会毫不留情地塞进你体内！
ROW CAT:Oe68fa679eca249d7fa7c L69 narrator physical_line
  EN: I almost feel sorry for tricking-
  ZH: text: 骗了人，我都快有点过意不去——
ROW CAT:O814b1c25bcf7d7584dcf L70 narrator physical_line
  EN: -I mean...
  ZH: text: ——我是说……
ROW CAT:O445f74c841728ae37a7e L71 narrator physical_line
  EN: -for getting Erma into this kinda situation!
  ZH: text: ——让艾玛陷进这种处境！
CONTROL L73  cut(0.06): AgentC02F09
CONTROL L74  rewind!
ROW CAT:O037208a7b4249b077403 L75 narrator physical_line
  EN: That poor otter girl probably got filled up reaaal good. I know I did <3
  ZH: text: 那可怜的水獭姑娘肯定被灌得饱饱的。反正我是 <3
ROW CAT:Odb6abe1b7e293167cf85 L76 narrator physical_line
  EN: Over and over that cock slammed into me, seed being pumped in almost endlessly!
  ZH: text: 那根鸡巴一次次猛撞进来，精液几乎无穷无尽地灌入！
ROW CAT:O1a32df97b7fe1e635fba L77 narrator physical_line
  EN: Gosh... Imagine, there's probably a planet out there filled with these studs...
  ZH: text: 天哪……想想看，可能有颗星球全是这种猛男……
CONTROL L79  cut(0.06):Black
CONTROL L80  rewind!
ROW CAT:O205645e5c914c73775f0 L81 narrator physical_line
  EN: At some point I must've passed out in between all the orgasms...
  ZH: text: 不知哪次高潮过后，我一定是昏过去了……
ROW CAT:O396892c09ae972207b1e L82 narrator physical_line
  EN: The next thing I remember is being in here, surrounded by these lovely tentacles.
  ZH: text: 接下来我记得的，就是我已经在这儿，被可爱的触手围着了。
CONTROL L84  cut(0.06): AgentC02F10
CONTROL L85  rewind!
ROW CAT:O0e3e3c1b76e7741951db L86 narrator physical_line
  EN: No clue if these aliens have eyes...
  ZH: text: 也不知道这些外星生物长没长眼睛…… 
ROW CAT:O23771fe51f58d6d66938 L87 narrator physical_line
  EN: ...but they must've seen that I'd be a lovely mom, eh-heh!
  ZH: text: ……但它们肯定看出我会是个好妈妈，嘿嘿！
ROW CAT:O90ac5d0b471d6bd6ee27 L88 narrator physical_line
  EN: Every now and again they'd take me out of the lovely squirming nest made for me
  ZH: text: 隔三差五，他们会把我抱出那专为我造的可爱蠕动巢穴，再好好操我一顿，算是额外添上的。
ROW CAT:Odd5ac6c7d6fe26b30bd5 L89 narrator physical_line
  EN: and give me a nice rutting, just for good measure.
  ZH: 
ROW CAT:O928765560df15822641a L90 narrator physical_line
  EN: Even when I started to get a belly showing, they'd keep on giving me a visit <3
  ZH: text: 就连肚子开始显怀了，他们也照样来找我 <3
CONTROL L92  cut(0.06): AgentC02F11
CONTROL L93  rewind!
ROW CAT:O72ed3203fa73e17896f0 L94 narrator physical_line
  EN: After each rut, I'd get to stretch my legs and then get put back into the nest
  ZH: text: 每次干完，我能伸伸腿，然后就又被放回那暖乎乎、扭来扭去的巢里，那些触手像是知道怎么让我舒——服……
ROW CAT:O993c202ff453fec61810 L95 narrator physical_line
  EN: all warm and wiggly, it's like the tentacles knew how to make me feel goooood...
  ZH: 
ROW CAT:O5fea1d2637c05e80cebc L96 narrator physical_line
  EN: ...which is why it was kinda rude for you to just smack them like that!
  ZH: text: ……所以你那样揍它们，实在有点没礼貌！
CONTROL L98  cut(0.06):Black
CONTROL L99  rewind!
ROW CAT:Ob3046ec8bc83518186a9 L100 narrator physical_line
  EN: Buuut now that I'm out of there I guess I should go and file my reports
  ZH: text: 不过嘛，既然出来了，我也该去交报告了，毕竟看来我还得再歇一阵，才能重返外勤……
ROW CAT:O1f4c0e86b2578c5066b2 L101 narrator physical_line
  EN: since it seems like I'm gonna be out of field duty for a little longer yet...
  ZH: 
ROW CAT:Ob1b6de64c132a56fdd14 L102 narrator physical_line
  EN: ...but next time I'll try tracking down the mystery stud planet... eh-hehehe...!
  ZH: text: ……不过下次，我要找找那颗神秘的猛男星球……嘿嘿嘿……！
CONTROL L104  fadeout(1.0, 1.0, 4)

## SC9f1bb2ff4b29b7d6 | sfw | vsn/f_AgentFZ1/script.vsn | vsn/f_AgentFZ1/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntroFemale
CONTROL L4  rewind!
ROW SFWf876d45a18aa1768b1c12906 L5 Fox physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFWcca68082adf0ca84d8446efe L6 Fox physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFWec8792bf3a9f538befd710bf L7 Fox physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L10  cut(0.06): Black
CONTROL L11  rewind!
ROW SFW2ae5d491ef2c2cab4121a3ca L12 - physical_line
  EN: ...I can see...!
  ZH: text: ……我看见了……！
CONTROL L14  cut(0.06): FenfenA01
CONTROL L15  rewind!
ROW SFW5c66b156c5a504e0d4800235 L16 Fox physical_line
  EN: We, the Fenfen, have lived for eons on this planet that you know as "Tutone".
  ZH: lang(Fox): 我们Fenfen，在这颗你们称为「图托恩」的星球上，已经生活了无数纪元。
ROW SFW700ba52bc924dc1019e2d381 L17 Fox physical_line
  EN: Having eschewed the sort of technological advances that your culture thrives on
  ZH: lang(Fox): 摒弃了你们的文化赖以繁荣的那类技术进步之后，
ROW SFW441c41afe5bc58fd3e9343ca L18 Fox physical_line
  EN: we have lived simple, satisfying lives in harmony with the planet itself.
  ZH: lang(Fox): 我们与这颗星球和谐共生，过着简单而满足的生活。
CONTROL L20  cut(0.06): FenfenA02
CONTROL L21  rewind!
ROW SFW6a0c6596aeb1e6fc69e0f856 L22 Fox physical_line
  EN: Quiet and modest are the best ways to describe us Fenfen.
  ZH: lang(Fox): 安静谦逊，最适合形容我们Fenfen。
ROW SFW25bf347341e6feb42c079492 L23 Fox physical_line
  EN: All major quarrels were sorted out by a council of the wisest ESPers we had.
  ZH: lang(Fox): 所有重大纷争，都由我们中最睿智的超能力者所组成的理事会来化解。
ROW SFW3e580ed93488a1903e9fb5d9 L24 Fox physical_line
  EN: With our highly attuned senses and powers, we were able to find solutions that 
  ZH: lang(Fox): 凭借我们高度敏锐的感官与力量，我们总能找到解决之道，这些方案 
ROW SFW29d51caf4f61cf7f02488c1c L25 Fox physical_line
  EN: benefitted all of society at once.
  ZH: lang(Fox): 能让整个社会同时受益。
CONTROL L27  cut(0.06): FenfenA03
CONTROL L28  rewind!
ROW SFWa0134e4f76abe7088cc41a3b L29 Fox physical_line
  EN: However, even with our attunement...
  ZH: lang(Fox): 然而，即便有着这份感应力……
ROW SFWc967cdf98ec2d4e3ab36b5d3 L30 Fox physical_line
  EN: ...we were not able to sense that amongst us ESPers lay one whose ambitions
  ZH: lang(Fox): ……我们竟未察觉，超能力者之中藏着一人，其野心
ROW SFW8bb44b4bc6f59989fc8c98f8 L31 Fox physical_line
  EN: would throw the very planet itself into chaos...
  ZH: lang(Fox): 会将整颗星球本身都拖入混沌……
ROW SFW0d89cf518ebee0e172567015 L32 Fox physical_line
  EN: ...
  ZH: lang(Fox): ……
ROW SFWda3a7e10d6b522f535afd684 L33 Fox physical_line
  EN: ...her name was Traeh.
  ZH: lang(Fox): ……她的名字是Traeh。
CONTROL L35  cut(0.06): FenfenA04
CONTROL L36  rewind!
ROW SFWca8871ff16d6887c22c9c67a L37 Fox physical_line
  EN: Gifted beyond her years, with an uncanny ability to find solutions others missed
  ZH: lang(Fox): 天赋远超其年纪，又有着总能找到他人所遗漏之解法的非凡本事，
ROW SFWeeb59be654b08c658081b06a L38 Fox physical_line
  EN: the ESPer Traeh seemed like a fine addition to the council.
  ZH: lang(Fox): 超能力者Traeh，看上去是议会的一位出色新成员。
ROW SFW3107d596bada87622d10f48f L39 Fox physical_line
  EN: She was readily granted access to the stores of power that we Fenfen kept.
  ZH: lang(Fox): 她很轻易便获准接触我们Fenfen所封存的力量贮藏。
CONTROL L41  snap: FenfenA05
ROW SFW0826dcb635b1c4b1deef45d0 L42 Fox physical_line
  EN: Power... that she then proceeded to corrupt.
  ZH: lang(Fox): 力量……而她随即着手将其腐化。
ROW SFWd2eeb4b4ca0b263109bb59b3 L43 Fox physical_line
  EN: Absorbing ancient caches of ESPer power that were left by previous generations
  ZH: lang(Fox): 吸收了前代遗留下来的古老超能力者力量贮藏之后，
ROW SFWcec229693a00c8232b8723b6 L44 Fox physical_line
  EN: Traeh was left deeply disfigured, down to her very core.
  ZH: lang(Fox): Traeh从外貌到内心，都已扭曲得面目全非。
CONTROL L46  cut(0.06): FenfenA06
CONTROL L47  rewind!
ROW SFWd71e72295232c74e086ea655 L48 Fox physical_line
  EN: Maybe if we, the remaining elder ESPers of the council, reacted faster
  ZH: lang(Fox): 也许我们议会中剩下的超能力者长老若能更快应对
ROW SFWcce451317f2adb62ff93c1f3 L49 Fox physical_line
  EN: then we could've prevented the calamity that was about to befall our people.
  ZH: lang(Fox): 就本可以阻止那场即将降临到我们族人头上的灾难。
ROW SFW41ddae66840c6d7e23751f79 L50 Fox physical_line
  EN: Alas, we did not, and that will forever be our greatest failing...
  ZH: lang(Fox): 可惜，我们没有，而这将永远是我们最大的过错……
CONTROL L52  cut(0.06): Black
CONTROL L53  rewind!
ROW SFW1dcf7b4e207a195555220da9 L54 Fox physical_line
  EN: Now go, destined hero.
  ZH: lang(Fox): 去吧，命中注定的英雄。
ROW SFW22f24cf649825d9aa034c452 L55 Fox physical_line
  EN: Free my brothers and sisters and restore peace to the land!
  ZH: lang(Fox): 解放我的兄弟姐妹，让这片土地重归和平！
CONTROL L57  wait: 0.2
CONTROL L58  fadeout(1.0, 1.0, 4)

## SC5aaca5284184e89a | sfw | vsn/f_AgentFZ2/script.vsn | vsn/f_AgentFZ2/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntro01Female
CONTROL L4  rewind!
ROW SFW1fce43e7477f79ab45c58a60 L5 Fox physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFW101c2baf84c787135e1b20e2 L6 Fox physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFW452dae5f66e268b4a91cea1d L7 Fox physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L9  cut(0.06): FenfenB01
CONTROL L10  rewind!
ROW SFW1633c8e547bafe8833494d6d L11 Fox physical_line
  EN: When Traeh turned her aggressions to us remaining members of the ESPer council 
  ZH: lang(Fox): 当Traeh把矛头转向我们超能力者议会的其余成员时， 
ROW SFWa9fd1cd689a3c47595e479de L12 Fox physical_line
  EN: it was unlike anything that we had ever encountered.
  ZH: lang(Fox): 那是我们从未遭遇过的情形。
ROW SFW2c2be029bcdb98814d813bf8 L13 Fox physical_line
  EN: We were a peaceful, though perhaps squabbly, folk!
  ZH: lang(Fox): 我们本是爱好和平的族群，虽说偶尔也爱拌拌嘴！
ROW SFW66082272acef93dee17ef23f L14 Fox physical_line
  EN: Violence and ESPer powered aggression were unknown to us!
  ZH: lang(Fox): 暴力，以及超能力者力量驱动的攻击，我们闻所未闻！
CONTROL L16  cut(0.06): FenfenB02
CONTROL L17  rewind!
ROW SFWea05b7758a3762f56db402ea L18 Fox physical_line
  EN: Traeh was not alone in her new ambitions, however. 
  ZH: lang(Fox): 然而，怀有这番新野心的并非只有Traeh。 
ROW SFWe27f183afc78c2f14810585a L19 Fox physical_line
  EN: Formerly placable creatures began to rise up as though answering her call.
  ZH: lang(Fox): 向来温顺易处的生灵也纷纷起身，仿佛在响应她的召唤。
ROW SFW86b53dae62c0dd3f1cbb9fff L20 Fox physical_line
  EN: Their combined powers were frightening...
  ZH: lang(Fox): 它们汇聚起来的力量令人胆寒……
CONTROL L22  cut(0.06): FenfenB03S
CONTROL L23  rewind!
ROW SFW4624dd431ade8f2296ff7f7a L24 Fox physical_line
  EN: ...and it seemed as if all hope was lost!
  ZH: lang(Fox): ……而一切希望仿佛就此落空！
ROW SFW4ca3643b45d63faa7b6e3f26 L25 Fox physical_line
  EN: No amount of reason nor pleading would stop the newly emboldened creatures
  ZH: lang(Fox): 无论讲道理还是苦苦哀求，都挡不住那些陡然壮了胆的生灵
ROW SFW8779ad147e8e573bd9ad7d9b L26 Fox physical_line
  EN: and even our cries for mercy went unanswered.
  ZH: lang(Fox): 连我们求饶的呼声也得不到半点回应。
CONTROL L28  cut(0.06): FenfenB04
CONTROL L29  rewind!
ROW SFW1ad64f73d2dd51ce82f8bfcd L30 Fox physical_line
  EN: Those very cries seemed to only fuel Traeh's power and ambition even more.
  ZH: lang(Fox): 那些哀嚎，似乎反而助长了Traeh的力量与野心。
ROW SFWdb126de7982cfd675b57dd3f L31 Fox physical_line
  EN: With each new section of Tutone conquered she would set her eyes on another
  ZH: lang(Fox): 每征服图托恩一片土地，她便盯上下一片，
ROW SFW9e6d77db77e2302d24fec789 L32 Fox physical_line
  EN: until it seemed that the very planet itself would bend to her will.
  ZH: lang(Fox): 直到仿佛整颗行星本身都要屈从于她的意志。
CONTROL L34  cut(0.06): FenfenB05
CONTROL L35  rewind!
ROW SFW347b8910e4b908cca0230271 L36 Fox physical_line
  EN: Any Fenfen that couldn't hide in the shadows of what we once called home
  ZH: lang(Fox): 任何无法躲进我们曾称之为家的阴影之下的Fenfen
ROW SFWa99c0b8fa300f25fcccc323f L37 Fox physical_line
  EN: became enslaved to do the bidding of the new conquerors.
  ZH: lang(Fox): 都沦为奴隶，听命于新的征服者。
ROW SFW9807e68cafecb67e0c63251e L38 Fox physical_line
  EN: This was no longer a quiet and modest life for us... 
  ZH: lang(Fox): 我们的生活，再也谈不上安静谦逊了…… 
CONTROL L40  cut(0.06): FenfenB06
CONTROL L41  rewind!
ROW SFWd4868aef8051d19da98ef7ba L42 Fox physical_line
  EN: Yes, our very home seemed destined to fall under the cruel fist of Traeh.
  ZH: lang(Fox): 没错，我们的家园仿佛注定落入Traeh的残暴铁拳。
ROW SFW3eabad8dd4e1ea300da90ef0 L43 Fox physical_line
  EN: It was a level of cruelty that was unknown in the long history of us Fenfen
  ZH: lang(Fox): 这种残酷在我们Fenfen的漫长历史上前所未见
ROW SFW7882cdb40edc90135f5bc668 L44 Fox physical_line
  EN: and it seemed as if all hope were lost...
  ZH: lang(Fox): 而一切希望仿佛都已不复存在……
CONTROL L46  wait: 0.2
CONTROL L47  fadeout(1.0, 1.0, 4)

## SC9e9ceda84c287300 | nsfw | vsn/f_AgentFZ3/script.vsn | vsn/f_AgentFZ3/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntro01Female
CONTROL L4  rewind!
ROW CAT:O07d22e4d9da0b7cffcdb L5 narrator physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW CAT:O4898671c9de36ee92370 L6 narrator physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放到我的手上。
ROW CAT:O26bd4a919f361b07e6e6 L7 narrator physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L9  cut(0.06): FenfenC01
CONTROL L10  rewind!
ROW CAT:O22dc7561e3ae3310e13a L11 narrator physical_line
  EN: As dark forces descended on all Fenfen, young and old alike,
  ZH: lang(Fox): 当黑暗势力降临到全体Fenfen——无论老幼——头上时，
ROW CAT:O9ac33d8bcc81df3c9143 L12 narrator physical_line
  EN: it truly did seem like all hope was lost.
  ZH: lang(Fox): 一切希望看起来当真都已破灭。
ROW CAT:O31932bb872bfecc9014c L13 narrator physical_line
  EN: Powerful though the ESPers of our people may have been, violence was unknown to us.
  ZH: lang(Fox): 我们族中的超能力者纵然或许强大，暴力对我们却全然陌生。
CONTROL L15  cut(0.06): FenfenC02
CONTROL L16  rewind!
ROW CAT:O082136094a09159d8efd L17 narrator physical_line
  EN: Only when pushed to the end of options, when even surrender seemed impossible
  ZH: lang(Fox): 只有当被逼至绝路，连投降似乎都变得不可能时，
ROW CAT:Oafbc9c849c84d2de1102 L18 narrator physical_line
  EN: did the first of us strike out...
  ZH: lang(Fox): 我们中才有人第一个出手反抗……
CONTROL L20  cut(0.06): FenfenC03
CONTROL L21  rewind!
ROW CAT:Oa8e4cb5cd58ae28cc744 L22 narrator physical_line
  EN: ...and retaliate!
  ZH: lang(Fox): ……并予以还击！
ROW CAT:O0bc3c477d97287d3bb03 L23 narrator physical_line
  EN: Psychic abilities once turned only towards a common good
  ZH: lang(Fox): 曾经只用于共同福祉的心灵能力，
ROW CAT:O5d2d560c47ac750b3455 L24 narrator physical_line
  EN: would now be turned against those who would try to subjugate us Fenfen!
  ZH: lang(Fox): 如今要对准那些企图征服我们Fenfen的人！
CONTROL L26  cut(0.06): FenfenC04
CONTROL L27  rewind!
ROW CAT:O66f6b0f7415ea8f2c383 L28 narrator physical_line
  EN: An arsenal of ESPer abilities became harnessed as weapons of war.
  ZH: lang(Fox): 各式各样的超能力，都被用作战争武器。
ROW CAT:O5e3999ec0497f3de3152 L29 narrator physical_line
  EN: Explosive psychic projectiles blasted away foes.
  ZH: lang(Fox): 爆裂的灵能弹将敌人轰退。 
ROW CAT:Of46fb112c94cb3480dda L30 narrator physical_line
  EN: Punishing waves of telekinetic force prevented advancement of armies.
  ZH: lang(Fox): 一波波慑人的念动力浪潮，挡住了大军的推进。
ROW CAT:O63a4ebed27b065fd6ccc L31 narrator physical_line
  EN: Some even went so far as to transform their very bodies into tools for combat.
  ZH: lang(Fox): 有些人甚至改变自己的身体，将其化作战斗的工具。
CONTROL L34  cut(0.06): FenfenC05
CONTROL L35  rewind!
ROW CAT:O5d2f9d0fa802209e659b L36 narrator physical_line
  EN: Ancient beings heard the cries of mental anguish that rang throughout the planet
  ZH: lang(Fox): 古老的存在们听见了回荡于整颗星球的精神痛呼，
ROW CAT:O3097f924a69022f9c990 L37 narrator physical_line
  EN: Some, like the noble Elves, took up ancient weapons in order to aid us Fenfen...
  ZH: lang(Fox): 其中一些，比如高贵的Elves，拿起了古老的武器来援助我们Fenfen……
CONTROL L40  cut(0.06): FenfenC06
CONTROL L41  rewind!
ROW CAT:O40e68ef27b67bb1d4961 L42 narrator physical_line
  EN: ...while other ancient beings, from deep within the bowels of the planet
  ZH: lang(Fox): ……而其他古老的存在，则从这颗星球最深的地底，
ROW CAT:O2c6e88d327c3145d1047 L43 narrator physical_line
  EN: awoke with a desire for vengeance and domination of their own...
  ZH: lang(Fox): 带着属于它们自己的复仇与征服欲望苏醒了……
CONTROL L46  wait: 0.2
CONTROL L47  fadeout(1.0, 1.0, 4)

## SCf793f8e2f2b5b70f | sfw | vsn/f_AgentFZ4/script.vsn | vsn/f_AgentFZ4/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntro01Female
CONTROL L4  rewind!
ROW SFW949e56ed11f24c03c014796a L5 Fox physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFWdf6668a8188e0b604d152fce L6 Fox physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFWb013bfd804ef2d3642114a82 L7 Fox physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L10  cut(0.06): FenfenD01
CONTROL L11  rewind!
ROW SFW304047fb362633755ac9964a L12 Fox physical_line
  EN: The great war waged for years between the evil forces of Traeh
  ZH: lang(Fox): 这场大战持续多年，交战双方是Traeh的邪恶势力
ROW SFW70b65e8d2ff534f4e165bdf2 L13 Fox physical_line
  EN: and the formerly peaceful Fenfen that inhabited this land.
  ZH: lang(Fox): 与曾经和平、居住在这片土地上的Fenfen。
ROW SFW5d409c75a4f379ad56e9b0ff L14 Fox physical_line
  EN: It seemed to all that this war might go on forever, with no decisive victories.
  ZH: lang(Fox): 在所有人看来，这场战争或许会永远打下去，谁也无法取得决定性胜利。
CONTROL L16  cut(0.06): FenfenD02
CONTROL L17  rewind!
ROW SFWa54fe24a623f359bd79919ae L18 Fox physical_line
  EN: Without a vital member of the Fenfen council representing a vital force
  ZH: lang(Fox): 议会失去了一位代表重要力量的 Fenfen 核心成员，
ROW SFW5ed5485a67e0496d4eed69d2 L19 Fox physical_line
  EN: the remaining councilors were hamstrung.
  ZH: lang(Fox): 余下的议员便处处受制。
ROW SFWcce2ce07edd20c9f7490d3cc L20 Fox physical_line
  EN: The psychic bonds between the members still held, requiring constant vigilance
  ZH: lang(Fox): 成员之间的灵能联结依然维系着，只是需要时刻保持警觉，
ROW SFW5f84f771411c8f8917c45d90 L21 Fox physical_line
  EN: to keep dark forces from consuming more ESPers.  
  ZH: lang(Fox): 以免黑暗力量吞噬更多超能力者。  
CONTROL L23  cut(0.06): Black
CONTROL L24  rewind!
ROW SFW4d134115ed70b002913840de L25 Fox physical_line
  EN: ...but then, one day, an opportunity arose...
  ZH: lang(Fox): ……可是有一天，一个机会出现了……
CONTROL L27  cut(0.06): FenfenD03
CONTROL L28  rewind!
ROW SFW0ec847a57db93dba046bdac2 L29 Fox physical_line
  EN: A moment of psychic weakness left Traeh disarmed and distracted for but a moment
  ZH: lang(Fox): 心灵上的一时虚弱，让Traeh卸下防备、分了神，哪怕只有一瞬，
ROW SFWb1a4870c824100b787e67f75 L30 Fox physical_line
  EN: and in that moment the remaining members of the council struck!
  ZH: lang(Fox): 就在那一刻，其余议员出手了！
ROW SFWcfd0ee8b82ba7b04440511dc L31 Fox physical_line
  EN: Unable to overcome the psychic disturbance and deal a final blow, 
  ZH: lang(Fox): 无法克服这股灵能扰动、给出致命一击， 
ROW SFWded102fada1ec20cb0fc4cd5 L32 Fox physical_line
  EN: the councilors instead froze Traeh in a crystal prison.
  ZH: lang(Fox): 议员们转而将Traeh封冻在一座水晶囚牢之中。
CONTROL L34  cut(0.06): FenfenD04
CONTROL L35  rewind!
ROW SFW366784170249e58fd5be1687 L36 Fox physical_line
  EN: With no fierce leader to guide them, the oppor- tunistic hordes broke apart
  ZH: lang(Fox): 没有了凶悍首领的指引，那群见风转舵的乌合之众土崩瓦解，
ROW SFW3840c04d50de9a060aa17ace L37 Fox physical_line
  EN: fleeing from the powers of the Fenfen council.
  ZH: lang(Fox): 纷纷逃离Fenfen理事会的力量。
ROW SFW9589795e17a1a5fb04b9e6c1 L38 Fox physical_line
  EN: This is not to say that it was a triumphant moment for the Fenfen...
  ZH: lang(Fox): 这并不是说，对Fenfen而言这是一个凯旋的时刻……
CONTROL L40  cut(0.06): FenfenD05
CONTROL L41  rewind!
ROW SFWf9f712d8cd9d9a46a8fe7cc0 L42 Fox physical_line
  EN: Indeed, heavy prices were paid on both sides of the conflict.
  ZH: lang(Fox): 事实上，冲突的双方都付出了惨重的代价。
ROW SFW65a78102b2a916c88a79b6ca L43 Fox physical_line
  EN: The planet you landed on is no longer the peaceful home of the Fenfen
  ZH: lang(Fox): 你所登陆的这颗星球，已不再是Fenfen那宁静的家园，
ROW SFW1a47b7887998c99c683b56a8 L44 Fox physical_line
  EN: but merely a chaotic shadow of its former self.
  ZH: lang(Fox): 而只是往日模样的一个混沌残影。
ROW SFW9c282a680e4cd8b44dad03c7 L45 Fox physical_line
  EN: Many Fenfen as of yet are held captive by remnants of the would-be conquerors
  ZH: lang(Fox): 至今仍有许多Fenfen被那些妄图征服者的残部俘虏着，
ROW SFW5f971665c2a8cdcd93d5be79 L46 Fox physical_line
  EN: awaiting the day that a hero will free them...
  ZH: lang(Fox): 等待着有朝一日，一位英雄前来解救他们……
CONTROL L48  wait: 0.2
CONTROL L49  fadeout(1.0, 1.0, 4)

## SCde64a3347a222a67 | sfw | vsn/f_AgentFZ5/script.vsn | vsn/f_AgentFZ5/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntro01Female
CONTROL L4  rewind!
ROW SFW1a15edd75322d015053e0552 L5 Fox physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。
ROW SFWde95ec349ade82bfd0de77c2 L6 Fox physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放到我的手上。
ROW SFWd6c9a4fb6d8ab6d91c9eca76 L7 Fox physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……
CONTROL L10  cut(0.06): FenfenE01
CONTROL L11  rewind!
ROW SFW1763b33c782a9254d9104062 L12 Fox physical_line
  EN: As us Fenfen strove to rebuild our home and drive out the remnants of evil
  ZH: lang(Fox): 当我们Fenfen奋力重建家园、驱逐邪恶残部时，
ROW SFW9d124cf7a2efd95a4d9800a5 L13 Fox physical_line
  EN: some of us looked up into the sky and saw a shooting star coming down.
  ZH: lang(Fox): 我们中有些人仰望天空，看见一颗流星正坠落而下。
ROW SFWc733233cb65b22d3556b588f L14 Fox physical_line
  EN: Perhaps Fate had sent us a hero, with which we could regain our peace?
  ZH: lang(Fox): 也许是命运给我们派来了一位英雄，好让我们重获和平？
CONTROL L16  cut(0.06): FenfenE02
CONTROL L17  rewind!
ROW SFWc51b6d96a52b47532a213a8e L18 Fox physical_line
  EN: Or perhaps Fate had a more sinister joke to play on us suffering Fenfen
  ZH: lang(Fox): 又或许，命运对受苦的我们Fenfen还有更阴险的玩笑要开，
ROW SFWae3ea33ae72b936a6f5836c7 L19 Fox physical_line
  EN: for this visitor from the stars did not land on our planet proper...
  ZH: lang(Fox): 因为这位来自群星的访客，并没有降落在星球本体上……
ROW SFWf448bf2cf3b2105430675f5c L20 Fox physical_line
  EN: ...instead, they landed on the satellite rock that held Traeh's prison!
  ZH: lang(Fox): ……而是落在了关押Traeh的囚牢所在的那座卫星岩上！
CONTROL L22  cut(0.06): FenfenE03
CONTROL L23  rewind!
ROW SFW9b38cb8d192e7d5e99b8d879 L24 Fox physical_line
  EN: As if destined for only a single purpose, the interstellar interloper
  ZH: lang(Fox): 仿佛注定只有一个目的，那位星际闯入者
ROW SFW629e454d01a54e4bf0d719ab L25 Fox physical_line
  EN: made their way to the very core of Traeh's prison. 
  ZH: lang(Fox): 一路来到了关押Traeh的囚牢核心。 
ROW SFWd5fa57463f6b6d00b4f714e6 L26 Fox physical_line
  EN: Had her psychic tendrils found their way into a poor fool's mind?
  ZH: lang(Fox): 她的灵能触须，是否已经探入了某个可怜虫的脑中？
CONTROL L28  cut(0.06): FenfenE04
CONTROL L29  rewind!
ROW SFWf22d973e836f41586d753cf7 L30 Fox physical_line
  EN: There is no way to know if it was dark ESPer power at work or merely curiosity 
  ZH: lang(Fox): 无从得知，究竟是黑暗的超能力者力量在作祟，还是仅仅出于好奇， 
ROW SFW221d2528aea571150ddae37a L31 Fox physical_line
  EN: but this traveler made contact with the crystal prison that held Traeh...
  ZH: lang(Fox): 但这位旅者确实触碰到了关押Traeh的水晶囚牢……
CONTROL L33  cut(0.06): FenfenE05
CONTROL L34  rewind!
ROW SFWe8611f80512467a444052b83 L35 Fox physical_line
  EN: ...and so they became undone, unable to resist the dark ESPer forces.
  ZH: lang(Fox): ……就这样，这名旅者崩溃了，无力抵挡黑暗的超能力者力量。
ROW SFW445519cb56eb078c7f834b59 L36 Fox physical_line
  EN: Power and pain coursed through the poor explorer 
  ZH: lang(Fox): 力量与痛苦奔涌过这名可怜的探索者全身， 
ROW SFW79a7cfb7c4f1b9f13529632a L37 Fox physical_line
  EN: until their mind was no longer their own.
  ZH: lang(Fox): 直到那心智，再也不属于自己。
CONTROL L39  cut(0.06): FenfenE06
CONTROL L40  rewind!
ROW SFWdeadc2a8ac2ca860077c0086 L41 Fox physical_line
  EN: No, from that moment forth they answered to a darker power...
  ZH: lang(Fox): 不，从那一刻起，那位旅者便听命于一股更黑暗的力量……
ROW SFW0ec990c8871d095be01d3c2c L42 Fox physical_line
  EN: They did as Traeh commanded!
  ZH: lang(Fox): Traeh吩咐什么，那位旅者就照做！
CONTROL L44  wait: 0.2
CONTROL L45  fadeout(1.0, 1.0, 4)

## SCf72bb408100fe80c | nsfw | vsn/f_ClassicStarkillV3/script.vsn | vsn/f_ClassicStarkillV3/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L2  fade(9, 0, 1)
CONTROL L3  fadein(1.0, 4): Asset16
CONTROL L4  rewind!
ROW CAT:Obb28d40545e60e42b0b9 L5 narrator physical_line
  EN: Now... Yiffai, you're gonna have to wake up for me!
  ZH: text: 现在……伊吠，你一定要醒过来啊！
ROW CAT:O90f8fc69ec0d50da7761 L6 narrator physical_line
  EN: If you're not still in there... I don't, I don't know what I'd do!!
  ZH: text: 要是你已经不在里面了……我不，我不知道该怎么办！！
CONTROL L8  fadecut(0.266, 2): Asset17
CONTROL L9  rewind!
ROW CAT:Od388cc527d1c772bd685 L10 narrator physical_line
  EN: Uuhn... big sis... I remember you...
  ZH: text: 唔……姐姐……我记得你……
ROW CAT:Oc45b560b4e897e5e2645 L11 narrator physical_line
  EN: In fact, getting knocked to the darn ground like this again...
  ZH: text: 说真的，又像这样被狠狠打倒在地……
ROW CAT:Oce6d06a0378b9979b48a L12 narrator physical_line
  EN: ...is makin' me remember you even more.
  ZH: text: ……反而让我更想起你了。
CONTROL L14  fadecut(0.266, 2): Asset18
CONTROL L15  rewind!
ROW CAT:O9a83a5e3bc0ad3d9b356 L16 narrator physical_line
  EN: Like when we used to tussle... heh, you never did gimme a break...
  ZH: text: 就像以前我们打闹的时候……嘿，你可从来没让过我……
ROW CAT:Oc10cf2951debc2fe1f7f L17 narrator physical_line
  EN: ...my tough big sis, who taught me everything... and always looked out for me...
  ZH: text: ……我那厉害的姐姐，什么都教给了我……也一直护着我……
CONTROL L19  fadecut(0.266, 2): Asset21
CONTROL L20  rewind!
ROW CAT:Oaa8874f807c328ebb9d9 L21 narrator physical_line
  EN: Yiffai... y-you're back!
  ZH: text: 伊吠……你、你回来了！
ROW CAT:Of79b8725cd9b8c7aec40 L22 narrator physical_line
  EN: I can't believe it... I thought... I thought I might have to...
  ZH: text: 真不敢相信……我以为……我以为自己可能不得不……
ROW CAT:Oa986e8fe62d47218b5a4 L23 narrator physical_line
  EN: But now you're safe again!
  ZH: text: 不过现在你又安全了！
CONTROL L25  fadecut(0.266, 2): Asset20
CONTROL L26  rewind!
ROW CAT:Oe503856b65d23ff5d5bd L27 narrator physical_line
  EN: Nnf... might need a little help standing.
  ZH: text: 唔……可能得扶我一把才能站起来。 
ROW CAT:O9b61f57136773704fb56 L28 narrator physical_line
  EN: That beating you dished out was one thing... but that's not all...
  ZH: text: 你把我揍成这样是一回事……但还不止如此……
ROW CAT:Oc31a0c8a6f2b5daa13aa L29 narrator physical_line
  EN: I was under the control of... a queen. Dark and cruel.
  ZH: text: 我之前被……一位女王控制着。她阴暗又残忍。
ROW CAT:O4367dd3284b437a6a49a L30 narrator physical_line
  EN: Feels like she sapped most of the energy I had left, when her will left me.
  ZH: text: 感觉她的意志离开我时，把我剩下的大半力气也抽走了。
CONTROL L32  fadecut(0.266, 2): Asset19
CONTROL L33  rewind!
ROW CAT:Ob2bf375645facb709539 L34 narrator physical_line
  EN: I might not be able to swing a tazer for a while... but here, take this.
  ZH: text: 我可能有一阵子挥不动电击枪了……不过，来，拿着这个。
ROW CAT:O1eafa04f72395a13e75d L35 narrator physical_line
  EN: It's dad's old whistle. You gave it to me for my first mission, remember...?
  ZH: text: 这是爸爸的旧哨子。我第一次出任务时，你把它给了我，还记得吗……？
ROW CAT:O4ed0622efdcf9a4aa9ad L36 narrator physical_line
  EN: I'll pilot your ship, and wherever you blow the whistle, I'll pick you up!
  ZH: text: 我来驾驶你的飞船，不管你在哪儿吹响哨子，我都会去接你！
ROW CAT:O84dc975ecaaa70ec5246 L37 narrator physical_line
  EN: That's the least I can do for saving me, right...?
  ZH: text: 你救了我，这至少是我该做的，对吧……？
CONTROL L39  fadeout(1.0, 1.0, 4)

## SCf1e352091c207f10 | nsfw | vsn/m_AgentM04/script.vsn | vsn/m_AgentM04/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L3  snap: AreaAMale02A
CONTROL L4  rewind!
ROW CAT:O8c9180a5c85ca65f5d39 L5 narrator physical_line
  EN: Ahh! Sorry lad! I don't know what came over me there!
  ZH: text: 啊！抱歉，小伙子！我也不知道刚才怎么鬼迷心窍了！ 
ROW CAT:Of59c439236ca6381cf94 L6 narrator physical_line
  EN: ...Or what came over my tazer, for that matter...
  ZH: text: ……或者该问，我的电击枪又是怎么了……
ROW CAT:O34595bdb5a13b322828b L7 narrator physical_line
  EN: ...wait no that was me...
  ZH: text: ……等等，不对，那是我……
ROW CAT:O155cc4ba4f0eb0ede061 L8 narrator physical_line
  EN: Let's start at the beginning, shall we?
  ZH: text: 咱们从头说起，好吗？
CONTROL L10  cut(0.06): AreaAMale02B
CONTROL L11  rewind!
ROW CAT:O48edb39c13f2ea6f5ffa L12 narrator physical_line
  EN: A shame you had to see me like that, but it's not really my fault.
  ZH: text: 可惜让你看见我那副样子，可这真不是我的错。
ROW CAT:Oa2cd57135fc44f946e46 L13 narrator physical_line
  EN: It all began when I stumbled upon a group of Dwarves in the midst of scouting.
  ZH: text: 一切都始于侦察时，我偶遇了一群矮人。
ROW CAT:O55a7b36ff988ca787714 L14 narrator physical_line
  EN: I was too engrossed in mapping out this large mine area that they call Ayskammr
  ZH: text: 我太专心绘制那片叫艾斯卡姆的大矿区地图了，所以壮汉们突然撕扯我的制服，让我措手不及！
ROW CAT:O156b7a635b65486d3b53 L15 narrator physical_line
  EN: so I was caught off guard as the burly boys started to tear at my uniform!
  ZH: 
CONTROL L17  cut(0.06): AreaAMale02C
CONTROL L18  rewind!
ROW CAT:O63afc322520f4e19b369 L19 narrator physical_line
  EN: I probably don't have to explain it, but I of course held back while fighting
  ZH: text: 这大概不用解释，打斗时我当然手下留情了。我壮得如此惊人，当然担心伤着那些可怜的矮人。他们显然对练肌肉也只是稍有兴趣，但可惜，他们跟我根本没法比。
ROW CAT:Oc7956838c9af742dcfb2 L20 narrator physical_line
  EN: being as prodigiously buff as I am, I worried about hurting the poor Dwarves
  ZH: 
ROW CAT:O7e58216feb0ebfff64c6 L21 narrator physical_line
  EN: they clearly had taken a passing interest in muscular development, but alas
  ZH: 
ROW CAT:Obed49bf6e0e80f6e46d0 L22 narrator physical_line
  EN: there was just no comparison between us.
  ZH: 
ROW CAT:O07d7803f6c239ad1b344 L23 narrator physical_line
  EN: While holding back, one of the boys quite rudely grabbed my tail. Scandalous!
  ZH: text: 我正手下留情，一个家伙却无礼地抓住我的尾巴。太不像话！
CONTROL L25  cut(0.06): AreaAMale02D
CONTROL L26  rewind!
ROW CAT:O9d0760fc16df25928b41 L27 narrator physical_line
  EN: Such rudeness was no way to repay the kindness that I showed them. Nosirree.
  ZH: text: 我好心待他们，他们却这么无礼，哪有这种道理！
ROW CAT:Oa1f2426f4091adb0d5b9 L28 narrator physical_line
  EN: It was enough to make a man consider teaching the brash lad a /proper/ lesson.
  ZH: text: 真让人想给那冒失小子一个/像样/的教训。
ROW CAT:O2d3ed9707eea95dfa8ba L29 narrator physical_line
  EN: As I considered a fitting punishment, the Dwarf seemed inclined to escalate things
  ZH: text: 我正琢磨该怎么惩罚，那矮人似乎还想得寸进尺，也就是那时，我决定认真起来。
ROW CAT:O41a384ff32b5fccb84c7 L30 narrator physical_line
  EN: and it was at that point that I decided to take things seriously.
  ZH: 
CONTROL L32  cut(0.06): AreaAMale02E
CONTROL L33  rewind!
ROW CAT:O67dfb289ebb02fc4375a L34 narrator physical_line
  EN: Treating me like I was a common boylass for them to enjoy, such nerve.
  ZH: text: 竟把我当成随便给他们玩弄的男婊子，真是放肆。
ROW CAT:Oe947d2a31817e4963a47 L35 narrator physical_line
  EN: In a burst of fairness I tried to warn the crudes that they were about to be
  ZH: text: 出于公平，我还好心警告那群粗人，接下来他们就要承受我使出全力的一击。
ROW CAT:O3d8950ccd17a268d1a4d L36 narrator physical_line
  EN: on the receiving end of my full power.
  ZH: 
ROW CAT:Ocd5ab7b73d16f7ae590d L37 narrator physical_line
  EN: The poor kids didn't know what they were bringing on themselves...
  ZH: text: 那帮可怜的小子，根本不知自己惹上了什么……
CONTROL L39  cut(0.06): AreaAMale02F
CONTROL L40  rewind!
ROW CAT:O826e37513f2e5c6d6c38 L41 narrator physical_line
  EN: Luckily for the brats, an interloper came along before I showed them whatfor!
  ZH: text: 算那帮崽子走运，我正要教训他们，就来了个搅局的！
ROW CAT:O009519e2ee18d74caaca L42 narrator physical_line
  EN: I unclenched my... fist... and breathed a sigh of relief.
  ZH: text: 我松开紧握的……拳头……长舒了一口气。
ROW CAT:Od44b8626c0255fb88c3d L43 narrator physical_line
  EN: A gentleman such as I hates to resort to violence, as should be apparent.
  ZH: text: 像我这样的绅士，显然最不愿诉诸暴力。
CONTROL L45  cut(0.06): AreaAMale02G
CONTROL L46  rewind!
ROW CAT:Obaa241aa92e487c94c4f L47 narrator physical_line
  EN: It was then that the youngsters decided to hightail out of the vicinity
  ZH: text: 看清自己面对的是什么后，那帮小子都吓破了胆，决定夹着尾巴逃离此地。
ROW CAT:O3c7438246d3fda547760 L48 narrator physical_line
  EN: being overcome with coward- ice once they realized what they were up against.
  ZH: 
ROW CAT:O67ac61baef2969b46a52 L49 narrator physical_line
  EN: I gave them a word or two of advice while they retreated, for good measure.
  ZH: text: 他们撤退时，我还好心补了几句忠告。
CONTROL L51  cut(0.06): Black
CONTROL L52  rewind! 
ROW CAT:O1caf7afab764edd5020a L53 narrator physical_line
  EN: Now this is where things start to get a bit hazy. Uncharacteristically so...
  ZH: text: 从这儿起，记忆就有点模糊了。这可不像我平时的记性……
ROW CAT:Od3f23f6b049f0ab02d7b L54 narrator physical_line
  EN: I turned to introduce myself to the fella that had chanced upon the scene
  ZH: text: 我转身向那个碰巧路过的家伙自我介绍，然后……我就记不太清了……
ROW CAT:O407e697bbd8dba3d4feb L55 narrator physical_line
  EN: and then... I can't recall much...
  ZH: 
ROW CAT:Oc827b8fa53847e6d87e9 L56 narrator physical_line
  EN: ...some mesmerizing light... ...warm and... grabby...?
  ZH: text: ……某种迷人的光……暖暖的……还会乱摸……？
CONTROL L58  cut(0.06): AreaAMale02H
CONTROL L59  rewind!
ROW CAT:O0d3c2740c0cfcfbf0c0d L60 narrator physical_line
  EN: Yes that's right, I was just about to warn the fella to leave the fighting to me
  ZH: text: 对，没错，我正要叫那家伙把战斗交给我，可我记得自己好像被……几只幽灵手抓住了？
ROW CAT:O38b18924a65cb2573784 L61 narrator physical_line
  EN: but I think I was in the clutches of... some ghostly hands?
  ZH: 
ROW CAT:O944b89c8813c207c0817 L62 narrator physical_line
  EN: No, that can't be right. I think there was some weapon that he may have aimed at me
  ZH: text: 不，不可能。我想他或许拿某种武器对准了我，当然，也不是说有什么武器是我应付不了的。
ROW CAT:Oa66cda4c4c90a6ed9e3b L63 narrator physical_line
  EN: not that there's no weapon I can't handle, of course.
  ZH: 
CONTROL L65  cut(0.06): AreaAMale02I
CONTROL L66  rewind!
ROW CAT:Oad80f00d07b618f57ae5 L67 narrator physical_line
  EN: Right, of course, that must have been it. The cad sudd- enly engaged in shenanigans
  ZH: text: 对，没错，肯定是这样。那无赖突然耍起花招，逼得我只好一遍遍用手“回敬”他！
ROW CAT:Od327401b9acce5d13ba7 L68 narrator physical_line
  EN: and I was forced to beat him off repeatedly!
  ZH: 
ROW CAT:O4d08b7392d3679af8557 L69 narrator physical_line
  EN: If memory serves me correct, I was doing such a good job at defending myself
  ZH: text: 没记错的话，我的自卫实在太出色，连那位大人都夸我是个乖孩子。真是光荣时刻！
ROW CAT:O310441d8d2f27937beae L70 narrator physical_line
  EN: that his lordship considered me to be a very good boy. A proud hour!
  ZH: 
CONTROL L72  cut(0.06): AreaAMale02J
CONTROL L73  rewind!
ROW CAT:O4175b26ebed929519053 L74 narrator physical_line
  EN: Hold on, no... what? Why would I be a good boy...
  ZH: text: 等等，不……什么？我怎么会是乖孩子……
ROW CAT:O126165e01946807d86b0 L75 narrator physical_line
  EN: why would those words fill me with glee, even now...
  ZH: text: 为什么就算现在，听到这话还是会满心欢喜……
ROW CAT:O2c4af6c2e52ea85a263e L76 narrator physical_line
  EN: Disregard whatever nonsense was recorded then, clearly it's unreliable.
  ZH: text: 那时候录下的胡话别当真，显然不可靠。
CONTROL L78  cut(0.06): AreaAMale02K
CONTROL L79  rewind!
ROW CAT:O7a54eedc2c9335c6e0d2 L80 narrator physical_line
  EN: The important thing is that when you found me, I had been left alone in this cell
  ZH: text: 重点是，你找到我时，我已被独自丢在这间牢房里，除了那把没电的电击枪，什么消遣也没有，只有那挥不去的渴望，想再被夸一句乖孩子。
ROW CAT:O3928e293e543ee2d3e9e L81 narrator physical_line
  EN: with naught to entertain myself with but my de-energized tazer
  ZH: 
ROW CAT:O73e2514db670464f2d07 L82 narrator physical_line
  EN: and a lingering desire to be called a good boy once more.
  ZH: 
CONTROL L84  cut(0.06): Black
CONTROL L85  rewind!
ROW CAT:Oa06b818257839a1d0fb4 L86 narrator physical_line
  EN: Thankfully, a good bop on the snout returned me to my rightful state of mind!
  ZH: text: 幸好鼻头挨了一记，我就彻底清醒了！
ROW CAT:Oc057c47b03ed955b0c4a L87 narrator physical_line
  EN: If you find any map data disks out in these mines, there's no need to thank me.
  ZH: text: 要是你在矿井里找到地图数据盘，不用谢我。
ROW CAT:Ocdbec35343720fc11098 L88 narrator physical_line
  EN: It's all in a day's work for this...
  ZH: text: 对我这个……来说，都只是分内的工作……
ROW CAT:O7f9ae1cc96f8492f1c10 L89 narrator physical_line
  EN: good...
  ZH: text: 乖…… 
ROW CAT:Oa27ea73cca8fc7422640 L90 narrator physical_line
  EN: boy...?
  ZH: text: 孩子……？
CONTROL L92  fadeout(1.0, 1.0, 4)

## SCba223e0dcbb46a0c | nsfw | vsn/m_AgentM06/script.vsn | vsn/m_AgentM06/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L3  snap: AreaCAgentM01A
CONTROL L4  rewind!
ROW CAT:O98617ad11017288497ab L5 narrator physical_line
  EN: Eep! Sorry! I mean... t-thanks!
  ZH: text: 呀！抱歉！我是说……呃，谢、谢谢！
ROW CAT:Oe0406abda85b254f4b9c L6 narrator physical_line
  EN: Been a while since I got to give my legs a good stretch!
  ZH: text: 好久没机会好好伸展一下双腿了！
ROW CAT:O84382542c60cac88d12d L7 narrator physical_line
  EN: Not that those vines weren't comfy or anything, after you get used to them...
  ZH: text: 也不能说那些藤蔓不舒服吧，等你习惯了之后……
ROW CAT:Ode696636373ff35f2d17 L8 narrator physical_line
  EN: ...not that I was here long, mind you!
  ZH: text: ……不过提醒你一句，我在这儿可没待多久。
CONTROL L10  cut(0.06): AreaCAgentM01B
CONTROL L11  rewind!
ROW CAT:O1c98a1cef40f702aaee5 L12 narrator physical_line
  EN: Last time I was able to stretch my legs properly was just after entering Sceafya
  ZH: text: 我上一次能好好伸展双腿，还是刚进斯凯菲亚的时候，在那片灌木丛里爬来爬去，好把这片地方摸清楚。
ROW CAT:O6f053ccf149e18c0d54a L13 narrator physical_line
  EN: crawling through all this shrubbery in order to scope out the area.
  ZH: 
ROW CAT:Oe1263d4c4dec9f1864ab L14 narrator physical_line
  EN: I thought I was doing real good to have gotten this far without getting caught!
  ZH: text: 我还以为自己干得漂亮，能一路走到这儿都没被发现！
CONTROL L16  cut(0.06): AreaCAgentM01C
CONTROL L17  rewind!
ROW CAT:O26f5e6de9a53e342d7cd L18 narrator physical_line
  EN: ...but there was someone behind me for who-knows-how-long
  ZH: text: ……可我身后不知什么时候多了个人，谁知道已经跟了多久，也许从我开始自以为在潜行时就在了，呀！
ROW CAT:O9b096e4acda80f852250 L19 narrator physical_line
  EN: maybe for the whole time I thought I was being stealthy for, eep!
  ZH: 
ROW CAT:O6a38add863548c5512c9 L20 narrator physical_line
  EN: I'm not really one for direct combat, but as far as I could tell
  ZH: text: 我其实不太擅长正面冲突，不过据我判断，这一次实在别无选择……
ROW CAT:O5b02362f5c7537aa5649 L21 narrator physical_line
  EN: I had no choice this time around...
  ZH: 
CONTROL L23  cut(0.06): AreaCAgentM01D
CONTROL L24  rewind!
ROW CAT:Oc8d588c5751c9ca9e94d L25 narrator physical_line
  EN: This poor Elven gal thought she had the upper hand and didn't even try to attack
  ZH: text: 这个可怜的精灵姑娘以为自己占了上风，连攻击都没试着来一下，可我偏偏摆出了小熊猫族的传统战斗姿势！
ROW CAT:O761f0e014c97d91e5d37 L26 narrator physical_line
  EN: but I went and assumed the traditional combat pose of the Red Pandarians!
  ZH: 
ROW CAT:O1d51c6656a850388bb17 L27 narrator physical_line
  EN: She knew that she made a possibly fatal mistake, because shortly after that
  ZH: text: 她知道自己可能犯了个要命的错误，因为没过多久，她便拔出了她的精灵剑，剑尖朝向我。
ROW CAT:Oed8c09b808b21f9669b4 L28 narrator physical_line
  EN: she drew her Elven blade and pointed it my way.
  ZH: 
CONTROL L31  cut(0.06): AreaCAgentM01E
CONTROL L32  rewind!
ROW CAT:Of232975cde42411c4faa L33 narrator physical_line
  EN: I offered her the opportunity to surrender before I unleashed a fury
  ZH: text: 在我大发雷霆之前，我给了她投降的机会，唯一的要求，就是她得带我去她的营地。
ROW CAT:O5764bcacf90c76bc58cd L34 narrator physical_line
  EN: with the only stipulation being that she take me to her encampment.
  ZH: 
ROW CAT:O536b9302ac7f65e6c6d7 L35 narrator physical_line
  EN: To nobody's surprise, of course, she instantly gave up and gave in
  ZH: text: 当然，不出所料，她马上就放弃抵抗、屈服了，甚至还招呼朋友来帮忙，把我固定在他们传统的那种箩筐上！
ROW CAT:O8d3248850cd472660a5d L36 narrator physical_line
  EN: even hailing for friends to help affix me to their traditional hamper of sorts!
  ZH: 
ROW CAT:Ocaf0254f59ee61b484ae L37 narrator physical_line
  EN: Not one to deny courtesies, I allowed them to do as they wished.
  ZH: text: 我从来不会推辞人家的礼数，就由着他们想怎样就怎样。
ROW CAT:Ocdeb8f62d531d4a6aef6 L38 narrator physical_line
  EN: And I must say they treated me like a proper victor, they did!
  ZH: text: 而且我得说，他们确实把我当成了真正的胜者！
CONTROL L40  cut(0.06): AreaCAgentM01F
CONTROL L41  rewind!
ROW CAT:O339830336cc1c49a1092 L42 narrator physical_line
  EN: Once in their encampment, I was quickly showered with affection and gifts
  ZH: text: 一进他们的营地，我就立刻被关爱和礼物包围了。刚从箩筐里解开、才要安顿下来，他们就给我按摩肩膀，还让我变得……咳咳……
ROW CAT:O9bc0925f61e4d786f09b L43 narrator physical_line
  EN: barely managed to make myself at home after being undone from the hamper
  ZH: 
ROW CAT:Od292e507f50ec1caaa42 L44 narrator physical_line
  EN: that I was being given shoulder massages and being made... ahem...
  ZH: 
ROW CAT:O7db9fd771dcb222d705a L45 narrator physical_line
  EN: ...even more /comfortable/...
  ZH: text: ……更加/舒服/……
CONTROL L47  cut(0.06): AreaCAgentM01G
CONTROL L48  rewind!
ROW CAT:O41a184c908ace58d87c1 L49 narrator physical_line
  EN: Ahh the ladies, that is to say, the Elves... for they're all ladies...
  ZH: text: 啊哈，那些女士——也就是说，精灵……毕竟她们全都是女士……
ROW CAT:O7d0775b0b4264530ae98 L50 narrator physical_line
  EN: they were most insistent on making me comfortable in all manner of ways!
  ZH: text: 她们可是用尽各种法子，非要让我舒服不可！
ROW CAT:O73e2682b607b51312f9f L51 narrator physical_line
  EN: I did my best to make it known that I was a merciful victor
  ZH: text: 我尽力让她们知道，我是个仁慈的胜者，也表明她们不该做任何自己不舒服的事……
ROW CAT:O3729d2b24f4fe43dc22f L52 narrator physical_line
  EN: and that they shouldn't do anything they weren't comfortable with...
  ZH: 
ROW CAT:O73ca37d61ae60f1f591c L53 narrator physical_line
  EN: ...but it seems that my prowess impressed upon them far too strongly.
  ZH: text: ……不过看来，我那番本事给她们留下的印象实在太过深刻。
CONTROL L55  cut(0.06): AreaCAgentM01H
CONTROL L56  rewind!
ROW CAT:Oa06a154e2608f8089b4a L57 narrator physical_line
  EN: Yes, even into the wee hours of the night, the Elves insisted on comforting me
  ZH: text: 没错，就连夜深人静的时候，精灵们也坚持要安抚我。我想也是，她们遇到的英雄都该是强壮又雄健的。
ROW CAT:O06ec7d10838dd34ae43d L58 narrator physical_line
  EN: I suppose it's expected that all heroes they meet would be strong and virile.
  ZH: 
ROW CAT:Oabe34b6226eecd67c458 L59 narrator physical_line
  EN: It's not as if I'm not without an appetite, of course.
  ZH: text: 当然，我也不是没有胃口。 
ROW CAT:Oa85a54d391b3a5fef0cc L60 narrator physical_line
  EN: My power and physique aren't compensation for any other male aspects!
  ZH: text: 我的力量和体格，可不是在弥补我男性方面其他地方的不足！
CONTROL L62  cut(0.06): AreaCAgentM01I
CONTROL L63  rewind!
ROW CAT:Oce76c6629c5b50836c6d L64 narrator physical_line
  EN: There was hardly a moment when any Elven maid wasn't around to tend to my needs
  ZH: text: 几乎每一刻，都有精灵女仆在我身边照料我的需求。就连我想继续执行任务时，精灵们也紧紧跟在我身后，可以说，她们简直对伟大英雄的种子上了瘾！
ROW CAT:O8c6d53953ee40267590f L65 narrator physical_line
  EN: even when I attempted to continue with my mission, the Elves were at my heels
  ZH: 
ROW CAT:O8b50be45f60814c31bc9 L66 narrator physical_line
  EN: seemingly addicted to the seed of a great Hero, one might say!
  ZH: 
ROW CAT:Of00cc31538992f857fc4 L67 narrator physical_line
  EN: It almost seemed like I'd never continue with the sortie...
  ZH: text: 看起来我几乎再也没法继续这次出击了……
CONTROL L69  cut(0.06): Black
CONTROL L70  rewind!
ROW CAT:O59653e2b62a443edb52e L71 narrator physical_line
  EN: If it weren't the height of rudeness to sneak away, I would have done so
  ZH: text: 要不是偷偷溜走实在太过失礼，我早就溜了，因为我开始担心其他特工出了什么事。
ROW CAT:O811537d1ac6b67fd1241 L72 narrator physical_line
  EN: for I was beginning to worry about what was happening with the other agents.
  ZH: 
ROW CAT:O582cb628e5c01a274046 L73 narrator physical_line
  EN: Obviously not all Cosmobreeders are as strong as I am, clearly.
  ZH: text: 显然不是所有宇宙育种者都像我这么强，这很明显。
ROW CAT:Oc0c114ed0d82cb02dec5 L74 narrator physical_line
  EN: And it's those sorts of thoughts that occupied me off and on, day after day...
  ZH: text: 这类念头就这样断断续续地占据着我，一天又一天……
CONTROL L76  cut(0.06): AreaCAgentM01K
CONTROL L77  rewind!
ROW CAT:O24cf5ff8f747fb5d8a40 L78 narrator physical_line
  EN: It was in the midst one such line of thinking that I came to realize...
  ZH: text: 正想着这些，我才突然发现……
ROW CAT:Ob62bdc8e362ce2a79b1c L79 narrator physical_line
  EN: ...the Elves were gone!
  ZH: text: ……精灵们不见了！ 
ROW CAT:O5530d8b75a150a75ca5f L80 narrator physical_line
  EN: ...but I was stuck! The treacherous vixens only pretended to surrender!
  ZH: text: ……可我还被困着！那些背信弃义的泼妇，原来只是假装投降！
ROW CAT:Oa3f77313c8bdfa74e308 L81 narrator physical_line
  EN: Before they moved camp, they left me here in this tentacle-ridden cell
  ZH: text: 她们转移营地前，把我留在了这间满是触手的牢房里。
ROW CAT:Of187589032afa12c03ca L82 narrator physical_line
  EN: Well! The nerve of them!
  ZH: text: 好哇！她们竟敢这样！
CONTROL L84  cut(0.06): Black
CONTROL L85  rewind!
ROW CAT:O1b0302bfaa09f1dc57e4 L86 narrator physical_line
  EN: I was just about to break free from these dastardly noodles before you showed up
  ZH: text: 在你出现之前，我眼看就要从这些可恶的面条里挣脱出来了。啊啊，而且我想，让你又能往成就清单上添一笔“救援”，对你这样的新特工来说，也更体面些，不是吗？
ROW CAT:Odfe0810ebbf62a5f6d8a L87 narrator physical_line
  EN: aaaand I suppose it looks better for a new agent such as yourself
  ZH: 
ROW CAT:O48492f863b6761856fd6 L88 narrator physical_line
  EN: if you get to add another "rescue" to your list of accomplishments, no?
  ZH: 
ROW CAT:O5233de5f6e0523bf9b96 L89 narrator physical_line
  EN: Well go on, I'll be right along after stretching my legs.
  ZH: text: 快去吧，我伸展完双腿就跟上。
ROW CAT:Ofdf95463ad80ad6033b1 L90 narrator physical_line
  EN: Heck, maybe you deserve the chance to try save this planet first
  ZH: text: 哼，新人，算我今天大方，也许该让你先去试着拯救这颗星球……
ROW CAT:Oc7f64c649096b51e3bde L91 narrator physical_line
  EN: now that I'm feeling generous to you, newbie...
  ZH: 
CONTROL L93  fadeout(1.0, 1.0, 4)

## SCe240b1877125bd63 | sfw | vsn/m_AgentMZ4/script.vsn | vsn/m_AgentMZ4/script.vsn
CONTROL L1  music: FenfenBGM
CONTROL L3  snap: FenfenIntro01Male
CONTROL L4  rewind!
ROW SFWc6cbb0ea773c2fb4bacad389 L5 Fox physical_line
  EN: Oh brave hero, thank you for rescuing me and proving your courage.
  ZH: lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。
ROW SFWa429aaa9ed2884fe23d62160 L6 Fox physical_line
  EN: Now, place your hands upon mine.
  ZH: lang(Fox): 现在，把你的双手放在我的手上。
ROW SFW7f21b66c1b380776a669929d L7 Fox physical_line
  EN: Turn your mind inward and witness the events that have shaped these lands...
  ZH: lang(Fox): 将心神转向内在，见证塑造这片土地的往事……
CONTROL L10  cut(0.06): FenfenD01
CONTROL L11  rewind!
ROW SFW74cae508eb4effc519ae6fca L12 Fox physical_line
  EN: The great war waged for years between the evil forces of Traeh
  ZH: lang(Fox): 这场大战持续多年，交战双方是Traeh的邪恶势力
ROW SFW65aa28ef538c847d31da1b55 L13 Fox physical_line
  EN: and the formerly peaceful Fenfen that inhabited this land.
  ZH: lang(Fox): 和这片土地上原本爱好和平的Fenfen。
ROW SFW5a77bbfeb53138e053807c56 L14 Fox physical_line
  EN: It seemed to all that this war might go on forever, with no decisive victories.
  ZH: lang(Fox): 所有人都觉得，这场战争也许永无休止，谁也无法彻底取胜。
CONTROL L16  cut(0.06): FenfenD02
CONTROL L17  rewind!
ROW SFWda2dd5b02bcb6b0b6dd1f095 L18 Fox physical_line
  EN: Without a vital member of the Fenfen council representing a vital force
  ZH: lang(Fox): 议会失去了一位代表重要力量的 Fenfen 核心成员，
ROW SFW85bdfbc50638df33c8d53432 L19 Fox physical_line
  EN: the remaining councilors were hamstrung.
  ZH: lang(Fox): 余下的议员便处处受制。
ROW SFW94eb9f77b59b379685104327 L20 Fox physical_line
  EN: The psychic bonds between the members still held, requiring constant vigilance
  ZH: lang(Fox): 成员之间的灵能联结依然维系着，只是需要时刻保持警觉，
ROW SFWdd2b5e1b0e070c5ecba1d74f L21 Fox physical_line
  EN: to keep dark forces from consuming more ESPers.  
  ZH: lang(Fox): 以免黑暗力量吞噬更多超能力者。  
CONTROL L23  cut(0.06): Black
CONTROL L24  rewind!
ROW SFWc37ae1ad48aab6d288cef274 L25 Fox physical_line
  EN: ...but then, one day, an opportunity arose...
  ZH: lang(Fox): ……但有一天，机会终于来了……
CONTROL L27  cut(0.06): FenfenD03
CONTROL L28  rewind!
ROW SFW0c142b5a497db773331a0e1e L29 Fox physical_line
  EN: A moment of psychic weakness left Traeh disarmed and distracted for but a moment
  ZH: lang(Fox): 心灵上的一时虚弱，让Traeh卸下防备、分了神，哪怕只有一瞬，
ROW SFW3f0dc6d0f59c0b87ec0f3b4f L30 Fox physical_line
  EN: and in that moment the remaining members of the council struck!
  ZH: lang(Fox): 就在那一刻，其余议员出手了！
ROW SFW26e60b551278d5aaa880ada8 L31 Fox physical_line
  EN: Unable to overcome the psychic disturbance and deal a final blow, 
  ZH: lang(Fox): 议员们无法克服这股灵能扰动，给她致命一击，
ROW SFW57fafbcc5ded09fad32122d8 L32 Fox physical_line
  EN: the councilors instead froze Traeh in a crystal prison.
  ZH: lang(Fox): 只好改将Traeh封冻在水晶牢笼里。
CONTROL L34  cut(0.06): FenfenD04
CONTROL L35  rewind!
ROW SFW817abda736bb4166386a9297 L36 Fox physical_line
  EN: With no fierce leader to guide them, the oppor- tunistic hordes broke apart
  ZH: lang(Fox): 失去凶悍首领的指挥，那群投机者便四散溃逃，
ROW SFWc1f748d306c7e4c7886b19b9 L37 Fox physical_line
  EN: fleeing from the powers of the Fenfen council.
  ZH: lang(Fox): 躲避Fenfen议会的力量。
ROW SFW2500bbe9f5885a583a6ddfcb L38 Fox physical_line
  EN: This is not to say that it was a triumphant moment for the Fenfen...
  ZH: lang(Fox): 但这并不意味着Fenfen迎来了凯旋时刻……
CONTROL L40  cut(0.06): FenfenD05
CONTROL L41  rewind!
ROW SFWdd9433262f31100fc341b0bf L42 Fox physical_line
  EN: Indeed, heavy prices were paid on both sides of the conflict.
  ZH: lang(Fox): 确实，冲突双方都付出了惨重代价。
ROW SFW4a77f56ab3ae58134483963f L43 Fox physical_line
  EN: The planet you landed on is no longer the peaceful home of the Fenfen
  ZH: lang(Fox): 你降落的这颗星球，已不再是Fenfen宁静的家园，
ROW SFW824ad0523e5ddb5767b698c8 L44 Fox physical_line
  EN: but merely a chaotic shadow of its former self.
  ZH: lang(Fox): 只剩下往日家园支离混乱的影子。
ROW SFW1202507c265fc2a9505ffa9a L45 Fox physical_line
  EN: Many Fenfen as of yet are held captive by remnants of the would-be conquerors
  ZH: lang(Fox): 至今，仍有许多Fenfen被那些妄图征服我们的残党囚禁
ROW SFWb720eb72d238ff3f446a08ca L46 Fox physical_line
  EN: awaiting the day that a hero will free them...
  ZH: lang(Fox): 等待着英雄前来解救的那一天……
CONTROL L48  wait: 0.2
CONTROL L49  fadeout(1.0, 1.0, 4)

## SCcba1968e6380c012 | sfw | vsn/m_ClassicBossRedbull/script.vsn | vsn/m_ClassicBossRedbull/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L2  fade(9, 0, 1)
CONTROL L3  fadein(1.0, 4): ClassicAreaA01
CONTROL L4  rewind!
ROW SFW63fae70c4614d234c7743a9f L5 - physical_line
  EN: Heh! Heh! Heh!
  ZH: text: 嘿！嘿！嘿！
ROW SFWea0f92b422cdc58dfd4b68b6 L6 - physical_line
  EN: Some of you little folks have some proper fight in you... Heh!
  ZH: text: 你们这帮小个子里，还真有几个能打的……嘿！
ROW SFW0aaa52d16ace3938f51698dc L7 - physical_line
  EN: I'd almost thought that the lot of you were merely an annoyance
  ZH: text: 我差点以为你们这群家伙只会惹人烦，没想到还真有个打中了我。呵！
ROW SFW73442eec5b63b15ec4a9eafc L8 - physical_line
  EN: but here's one that actually manged to hit me. Heh!
  ZH: 
ROW SFW5d81916a84e154306f70072b L9 - physical_line
  EN: What's next, one of you coming along and knocking me down to- 
  ZH: text: 接下来呢，你们还想来一个把我也撞—— 
CONTROL L11  fadecut(0.266, 2): ClassicAreaA02
CONTROL L12  rewind!
ROW SFW8802f3635fc50d5a845121af L13 - physical_line
  EN: Come on, I beat you fair and square! Stop trying to act cool.
  ZH: text: 得了，我可是堂堂正正打赢你的！别装酷了。
ROW SFWf65c9cabd155cbeece626711 L14 - physical_line
  EN: You know I'm a better fighter, and I accept your defeat.
  ZH: text: 你知道我身手更强，我也接受你的认输。
ROW SFW679414aafeaffbc57850c630 L15 - physical_line
  EN: No more harm will come to you so long as you tell me whe-
  ZH: text: 不会再伤你，只要告诉我在—
CONTROL L17  snap: ClassicAreaA03
CONTROL L18  rewind!
ROW SFW3c40c1ea5cd441ce0c680992 L19 - physical_line
  EN: W-what?? How did you get behind me so fast???
  ZH: text: 什、什么？？你怎么一下就到我背后了？？？
ROW SFW71b087089cbb1574aca2d8c0 L20 - physical_line
  EN: Harm? My little yellow furred companion? You wish to tell me of harm?
  ZH: text: 伤害？黄毛小朋友，你要跟我谈伤害？
ROW SFW3999fc732331abe579144e6e L21 - physical_line
  EN: Perhaps you'd like a lesson in just such a topic as "harm"
  ZH: text: 也许你想亲自上一堂关于“伤害”的课
ROW SFWd2ef1db23767bd163e86c814 L22 - physical_line
  EN: and then you can recite it to me, no?
  ZH: text: 然后再背给我听，如何？
CONTROL L24  sync!
CONTROL L25  queue: BlackTiming
CONTROL L26  rewind!
CONTROL L27  sfxcue: BlackTiming {
CONTROL L28    play [LeverActivate] at [1]
CONTROL L29  }
CONTROL L30  sync!
CONTROL L32  fadecut(0.266, 2): Asset06
CONTROL L33  rewind!
ROW SFW53aea7ff229154b60c4bc9d4 L34 - physical_line
  EN: ...ow...
  ZH: text: ……好痛……
CONTROL L36  fadecut(0.266, 2): Asset07
CONTROL L37  rewind!
ROW SFW48341ac89362830d9abed38c L38 - physical_line
  EN: Y-yeah... I can... I can tell you a lot about harm... now.... oow....
  ZH: text: 是、是啊……现在……伤害这事，我懂得可多了……嗷……
ROW SFWb3fed9e77f06db11501356f0 L39 - physical_line
  EN: ...j-just lemme get my breath back...
  ZH: text: ……就、就让我喘口气……
CONTROL L41  fadecut(0.266, 2): Asset08
CONTROL L42  rewind!
ROW SFW2261d43c3dc2fdd65b6976c9 L43 - physical_line
  EN: Here, spunky yellow boy. Take your leave of my domain.
  ZH: text: 好吧，有股冲劲的黄毛小子，离开我的领地吧。
ROW SFW3cd950853c08b36c461d327e L44 - physical_line
  EN: And while you're at it, take this garbage that a fellow small fighter left
  ZH: text: 顺便，把另一个小个子战士留下的垃圾带走。我当时给他的教训，可比给你的还要狠。
ROW SFWa4c90be3ab039b6ad14a9633 L45 - physical_line
  EN: after I had given him an even rougher lesson than yours.
  ZH: 
CONTROL L47  fadecut(0.266, 2): Black
CONTROL L48  rewind!
ROW SFW8b9f709b88f1f91748823e42 L49 - physical_line
  EN: With shoes in hand, Yiffai scrambles out as the Redbull drops deeper into the mines
  ZH: text: 伊吠拿着靴子爬出去，红牛则深入矿井，他泛着红光的鬃毛诡异地隐入黑暗……
ROW SFWecb4f230849d7b02a2a8e1b6 L50 - physical_line
  EN: his glowing red mane fading eerily into the dark...
  ZH: 
CONTROL L52  fadeout(1.0, 1.0, 4)

## SC9ac2eccd1d8bd48f | nsfw | vsn/m_ClassicPigobinV3/script.vsn | vsn/m_ClassicPigobinV3/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L2  fade(9, 0, 1)
CONTROL L3  fadein(1.0, 4): Asset12
CONTROL L4  rewind!
ROW CAT:Oc5a2e346c20c75d21319 L5 narrator physical_line
  EN: Thou hast fought a fair round for such an untrained hand.
  ZH: lang(HardFox): 汝虽未经锤炼，这一战却也打得不差。
ROW CAT:O01f66c19dac1380c0a11 L6 narrator physical_line
  EN: Pray, tell me thine name so that I may honor thee.
  ZH: lang(HardFox): 敢问阁下尊姓大名，好让吾致以敬意。
ROW CAT:O0edf3102165f6169bdfa L7 narrator physical_line
  EN: ...ahh, but the people of thy land do not speaketh my tongue...
  ZH: lang(HardFox): ……啊，然而汝故土之民，并不通晓吾之言语……
CONTROL L9  fadecut(0.266, 2): Asset13
CONTROL L10  rewind!
ROW CAT:O009d9a75e47b04f0b26e L11 narrator physical_line
  EN: W-what? No matter how much I fight... There's just no winning!
  ZH: text: 什、什么？再怎么打……都赢不了！
ROW CAT:Od53a455fe574739c9f8a L12 narrator physical_line
  EN: Who are you? W-what are you doing down here?
  ZH: text: 你是谁？你、你在下面做什么？
CONTROL L14  fadecut(0.266, 2): Asset14
CONTROL L15  rewind!
ROW CAT:O9d2238b20bf20218616c L16 narrator physical_line
  EN: I need not speaketh your crude tongue in order to understand your crude desire
  ZH: lang(HardFox): 无需说汝那粗鄙之语，吾亦明了汝粗鄙之欲
ROW CAT:O9e9bbd40479ffb2904de L17 narrator physical_line
  EN: So struggle not as I placeth a most useful trinket upon thee.
  ZH: lang(HardFox): 莫要挣扎，且让吾为汝戴上这实用的小饰物。
CONTROL L19  fadecut(0.266, 2): Asset13B
CONTROL L20  rewind!
ROW CAT:Ob0bbb26d63de392a3df6 L21 narrator physical_line
  EN: H-hey! What the hell is this? I'm not some darn pet of yours to collar!
  ZH: text: 喂、喂！搞什么鬼？我又不是你家宠物，戴什么项圈！
ROW CAT:O57239bc248b180262cdd L22 narrator physical_line
  EN: I'll find a way to bring you down, just give me a minute and I'll-
  ZH: text: 我会想办法打倒你的，给我一分钟，我就——
CONTROL L24  fadecut(0.266, 2): Asset06
CONTROL L25  rewind!
ROW CAT:Offa44929d7fb73142bcb L26 narrator physical_line
  EN: And thou shall do what, fairest knight?
  ZH: text: 那么，俊美的骑士，汝又待如何？ 
CONTROL L28  fadecut(0.266, 2): Asset15
CONTROL L29  rewind!
ROW CAT:O46c5a1d8ea1bc27b4b04 L30 narrator physical_line
  EN: Mine powers are ancient and forgotten, and thou are but a pup lost in the dark.
  ZH: text: 吾之力量古老而被世人遗忘，汝不过是迷失黑暗的小犬。
ROW CAT:O204bf950778aa6f0611e L31 narrator physical_line
  EN: Prayeth that I overlook your ill mannered outburst, as the generous host I am.
  ZH: text: 祈求吾这位宽宏的主人，不计较汝方才的无礼罢。
ROW CAT:Od2892bfc4fd59de564fa L32 narrator physical_line
  EN: Now taketh this necklace so that you may understand others of this land
  ZH: text: 且收下这项链，好让汝听懂此地众人的话语……也省得旁人再领教汝的无礼……呵呵呵呵……
ROW CAT:O85026b9f341aee1ec642 L33 narrator physical_line
  EN: ...and spareth them from your ill manners...eh heh heh heh...
  ZH: 
CONTROL L35  fadecut(0.266, 2): Black
CONTROL L36  rewind!
ROW CAT:O7278f720ffee370e0770 L37 narrator physical_line
  EN: And with a gutteral laugh, the demonic form faded back into the darkest darks
  ZH: text: 伴着喉间一阵低笑，那魔影退回了最深的黑暗，只留下一个吓坏了的小狗崽……
ROW CAT:O07fa4e79e39c930c0770 L38 narrator physical_line
  EN: leaving nought but a scared pup in his wake...
  ZH: 
CONTROL L40  fadeout(1.0, 1.0, 4)

## SCe68f2e03acd6f17b | nsfw | vsn/m_ClassicSqueakerBoss/script.vsn | vsn/m_ClassicSqueakerBoss/script.vsn
CONTROL L1  music: CutsceneX
CONTROL L2  fade(9, 0, 1)
CONTROL L3  fadein(1.0, 4): Asset22A
CONTROL L4  rewind!
ROW CAT:O0b15430051d27c9823e6 L5 narrator physical_line
  EN: Now WHY did you have to go and do that, huh?
  ZH: text: 现在，你干嘛非得去干那种事，嗯？
ROW CAT:Oc09b61265d10a8dc61ae L6 narrator physical_line
  EN: One of you sorts went and ransacked all my belongings right after I landed
  ZH: text: 你们这种家伙前脚在我刚落地时把我的所有家当翻了个精光，如今你又想在一对一单挑里把我打倒？
ROW CAT:Ob86bf9c51ac943c3ead7 L7 narrator physical_line
  EN: and now you're trying to take me down in one-on-one combat?
  ZH: 
ROW CAT:O671c452929f5604d0458 L8 narrator physical_line
  EN: No chance! I've just about had enough of you little bra-
  ZH: text: 没门！我真是受够了你们这些小混-
CONTROL L10  snap: Asset22B
CONTROL L11  rewind!
ROW CAT:O7188e11ab7cd06c3e395 L12 narrator physical_line
  EN: -hey...
  ZH: text: -嘿……
ROW CAT:O1364d8857165c433f58e L13 narrator physical_line
  EN: Is that... No way...
  ZH: text: 那是……不可能吧……
ROW CAT:Obfc9f8da375d35c46fa9 L14 narrator physical_line
  EN: ...
  ZH: text: ……
ROW CAT:O377a9af5891337c01e23 L15 narrator physical_line
  EN: ...but YES way!
  ZH: text: ……可偏偏就是！
CONTROL L17  fadecut(0.266, 2): Asset23
CONTROL L18  rewind!
ROW CAT:O670c59a52e7d88ed0538 L19 narrator physical_line
  EN: It's my Cosmohelm! It got all the way over here somehow!
  ZH: text: 是我的Cosmohelm！它不知怎么一路跑到这边来了！
ROW CAT:O89c349c8e6123e4f43f7 L20 narrator physical_line
  EN: This'll be real good to have in case I ever have to go into space or something!
  ZH: text: 万一哪天我得上太空什么的，这玩意儿可就派上大用场了！
ROW CAT:Oaea9196d5c151cdad1dd L21 narrator physical_line
  EN: Just need to keep an eye out for the Cosmosuit portion...
  ZH: text: 只要再留心Cosmosuit那一部分就好...
ROW CAT:Oe5f0ee057ad8e11e594a L22 narrator physical_line
  EN: ...and I'll be able to have a nice proper airtight outfit! Hoorah!
  ZH: text: ……我就能凑齐一套像样的气密装备啦！好耶！
CONTROL L24  fadeout(1.0, 1.0, 4)

