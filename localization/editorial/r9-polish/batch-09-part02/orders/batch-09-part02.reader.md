# batch-09-part02 精校工单：区域场景与条件分支（关卡救援与分支）（第 2／4 部分）

英文与当前中文都按整场连读；`current` 是构建候选的实际显示行（以本批参照摘录与 ORDER 记的候选为准）。
ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。

## SCae0a1fcaba5dc485 | nsfw | datadm/all.ds | AreaA_Cellar.Goodbye
CONTROL L294  <AreaA_Cellar.Goodbye>
ROW CAT:O0ae28fed2bfdd17b932a L295 * physical_line
  EN: Remember, this meat hoard is our little secret!
  ZH:   * 记住了，这一堆囤肉是咱们的小秘密！

## SC63325d4f67009179 | nsfw | datadm/all.ds | AreaA_Cellar.Hello
CONTROL L291  <AreaA_Cellar.Hello>
ROW CAT:O0cd036c7b1d26fdf82eb L292 * physical_line
  EN: Oh heeeello, welcome to my little meat cellar!
  ZH:   * 哦——你好呀，欢迎来我的小肉窖！

## SCb793a29ff7467d40 | nsfw | datadm/all.ds | AreaA_Cellar.Talk.meat
CONTROL L297  <AreaA_Cellar.Talk.meat>
ROW CAT:O1a98b3251b5ac587fbfd L298 * physical_line
  EN: You can take some meat, just don't tell anyone...
  ZH:   * 你可以拿点肉，只是别跟任何人说……

## SCf903ae70f8aff8b1 | nsfw | datadf/all.ds | AreaA_Macsen1.Goodbye
CONTROL L396  <AreaA_Macsen1.Goodbye>
ROW CAT:Oc03c16f3b15e183d1163 L397 * physical_line
  EN: Bye bye, come back with lots of lect!
  ZH:   * 拜拜，带着大把 lect 再来！

## SCa7c8f75704bd4ee6 | nsfw | datadf/all.ds | AreaA_Macsen1.GoodbyeNoID
CONTROL L410  <AreaA_Macsen1.GoodbyeNoID>
ROW CAT:Obad8718f9de4d5112adb L411 * physical_line
  EN: Bye bye, pup. Come back when you're older!
  ZH:   * 拜拜，小狗。等你长大点再来吧！

## SCb662e4662e01f8f0 | nsfw | datadm/all.ds | AreaA_Macsen1.PsyCoffee
CONTROL L422  <AreaA_Macsen1.PsyCoffee>
ROW CAT:O8aeed7d04ee7a9748b3d L423 * physical_line
  EN: If cola and tea aren't your speed, then how about some coffee?
  ZH:   * 如果可乐和茶都不合你口味，那来点咖啡怎么样？
ROW CAT:O3a46abe0bdb74952179e L424 * physical_line
  EN: It's from off-world beans, a real pick-me-up!
  ZH:   * 用外星咖啡豆做的，提神得很！
CONTROL L426  ### shared ###

## SC0567d1047b8169fe | sfw | datadm/all.ds | AreaA_Macsen1.PsyTea
CONTROL L419  <AreaA_Macsen1.PsyTea>
ROW SFW958aaae2719d75c9b07d80b9 L420 - physical_line
  EN: This stuff will quench your thirst and recover some PSY, but to be honest...
  ZH:   * 这东西能解渴，还能恢复些精神力，不过说真的……
ROW SFWd86332cf03deee2c786ac9e1 L421 - physical_line
  EN: ...it won't cool you down like a nice ICECOLA will! 
  ZH:   * ……可它没法像爽口的 ICECOLA 那样让你凉快下来！ 

## SCbbf42b8a33fa7743 | nsfw | datadm/all.ds | AreaA_Macsen1.Talk.placeholder
CONTROL L398  <AreaA_Macsen1.Talk.placeholder>
ROW CAT:O39182f8013901bb9b199 L399 * physical_line
  EN: It's too hot to talk, sorry!
  ZH:   * 太热了，实在没法说话，抱歉！

## SC14a7078a9de2f2a2 | nsfw | datadf/all.ds | AreaA_Macsen2.CancelPurchase
CONTROL L529  <AreaA_Macsen2.CancelPurchase>
CONTROL L530    if { !f(shop_juiced) } {
ROW CAT:O4ab0d96d48bcd8d7c0e7 L531 * physical_line
  EN: Can't blame ya. It's too hot down here to do business, right?
  ZH:     * 不能怪你。这下面热得要命，根本没法做生意，对吧？
CONTROL L532    } else {
ROW CAT:Ocda7c0d2a2c40d6809ff L533 * physical_line
  EN: That's a shame. Anything else?
  ZH:     * 真遗憾。还要点别的吗？
CONTROL L534    }

## SCd40680bf3e0cd4a8 | nsfw | datadm/all.ds | AreaA_Macsen2.Hello
CONTROL L463  <AreaA_Macsen2.Hello>
ROW CAT:O5ae4cc9bdf0e89e862ea L464 * physical_line
  EN: Whew, I thought you were a dwarf at first! Welcome!
  ZH:   * 呼，我一开始还以为你是个矮人呢！欢迎！

## SC8b9b4e57a1559d32 | nsfw | datadm/all.ds | AreaA_Macsen2.TazerPirate
CONTROL L469  <AreaA_Macsen2.TazerPirate>
ROW CAT:Of0a4f457e434e2a0d923 L470 * physical_line
  EN: Wanna become a space pirate? All you need is this Official Pirate Lighttazer!
  ZH:   * 想当太空海盗吗？你只需要这把官方海盗光电击器！
ROW CAT:O76a71b9ba7a62cfd6a03 L471 * physical_line
  EN: Plus a ship and a crew of outlaws, of course!
  ZH:   * 当然，还得有一艘飞船和一群亡命之徒！
ROW CAT:O2686fe3d085bb1197147 L472 * physical_line
  EN: ...just don't forget to equip it, it's not just for show, ya know.
  ZH:   * ……只是别忘了把它装备上，它可不是摆设，懂吧？

## SC90024f31413f36cf | sfw | datadf/all.ds | AreaA_Macsen2.ThanksForJuice
CONTROL L478  <AreaA_Macsen2.ThanksForJuice>
ROW SFW637c6f9874e968c9f6d83673 L479 - physical_line
  EN: Ahhh that's the stuff! Good and strong!
  ZH:   * 啊——就是这个味儿！够劲，够浓！
ROW SFWcc6177ad5f8f21d085b947be L480 - physical_line
  EN: I can finally stop being toasty and do some business! 
  ZH:   * 我终于不用再热得发烫，可以做点生意了！ 

## SCff7625c4e8dfa1ab | nsfw | datadm/all.ds | AreaA_Macsen2.VitDrumstick
CONTROL L474  <AreaA_Macsen2.VitDrumstick>
ROW CAT:O7be81314843f3a1c5da4 L475 * physical_line
  EN: Carved from ferocious beasties, slow roasted over lava! Restores vitality!
  ZH:   * 取自凶猛野兽的肉，在熔岩上慢火烤成！恢复活力！
ROW CAT:Oa4b99b3b2535fef36ef4 L476 * physical_line
  EN: In fact, it's almost too hot to handle... YEOWCH!
  ZH:   * 事实上，它烫得几乎没法上手……哎哟！

## SC212d5ffaa43d444a | nsfw | datadm/all.ds | AreaA_Prison1.CancelPurchase
CONTROL L567  <AreaA_Prison1.CancelPurchase>
CONTROL L568    if { hasItem(Key) } {
ROW CAT:O0bf464976c811070381f L569 * physical_line
  EN: Woah, like, what?
  ZH:     * 哇，什么情况？
CONTROL L570    } else {
ROW CAT:Of2ef26cae62a5876a778 L571 * physical_line
  EN: You're not trying to tease me, are ya, buddy?
  ZH:     * 哥们，你不是在耍我吧？
CONTROL L572    }

## SC65cbd9211754857c | nsfw | datadf/all.ds | AreaA_Prison1.CancelPurchase
CONTROL L568  <AreaA_Prison1.CancelPurchase>
CONTROL L569    if { hasItem(Key) } {
ROW CAT:Oea3462857f82e6c0ae34 L570 * physical_line
  EN: Is there something wrong? If you don't mind, I'd like to get out of here...
  ZH:     * 出什么事了吗？要是不介意的话，我想离开这里……
CONTROL L571    } else {
ROW CAT:O9a0d60f189e4c56ec180 L572 * physical_line
  EN: I'm sure I saw a key around here, while I was scouting.
  ZH:     * 我侦察的时候，肯定在这附近见过一把钥匙。
ROW CAT:Oac155115442eb8ad22b7 L573 * physical_line
  EN: If only I'd picked it up then! Darn!
  ZH:     * 当时要是把它捡起来就好了！可恶！
CONTROL L574    }

## SC6f9d49362a5ca0e1 | nsfw | datadf/all.ds | AreaA_Prison1.NoBoneForDog
CONTROL L559  <AreaA_Prison1.NoBoneForDog>
ROW CAT:Oc9ff07a4816cf41ae7f5 L560 * physical_line
  EN: Can you get your master to come back with a key? I'm locked up in here!
  ZH:   * 你能让你的主人带着钥匙回来吗？我被锁在这里面了！

## SC1c204a7ed5a14547 | sfw | datadf/all.ds | AreaA_Prison1.Rescue
CONTROL L576  <AreaA_Prison1.Rescue>
ROW SFW15f4d6ee82b3dc7d5808cf4e L577 - physical_line
  EN: W-we could open this cell if you had a k-k-key! You've got one, right?
  ZH:   * 你、你要是有钥、钥匙，就能打开这间牢房！你有的，对吧？

## SC60adaca3b363a3f3 | sfw | datadm/all.ds | AreaA_Prison1.SoldOut
CONTROL L586  <AreaA_Prison1.SoldOut>
ROW SFW9276a5cb7f48921e46ad57c4 L587 - physical_line
  EN: I'm like, fine now. Just some scuffs and a bruised ego, that's all!
  ZH:   * 我现在没事啦。就是擦破点皮，自尊心受了点伤，仅此而已！

## SC0ee1e4df36565910 | nsfw | datadf/all.ds | AreaA_Prison1.TalkAfterRescue.thanks
CONTROL L592  <AreaA_Prison1.TalkAfterRescue.thanks>
ROW CAT:O29bb885b80318384a8a6 L593 * physical_line
  EN: Thanks a bunch! I'm not used to being roughed up like THAT...
  ZH:   * 多谢啦！我可不太习惯被人那样粗暴对待……

## SC7e54132562c5bcb0 | sfw | datadf/all.ds | AreaA_Prison1.TalkAfterRescue.thanks
CONTROL L592  <AreaA_Prison1.TalkAfterRescue.thanks>
ROW SFW75ec3374267d5084b12af5ef L593 - physical_line
  EN: Thanks a bunch! I never thought I'd end up in alien jail.
  ZH:   * 太感谢了！没想到我竟会被关进外星监狱。

## SC6e73268397a8b0db | nsfw | datadm/all.ds | AreaA_Prison2.GoodbyeNotRescued
CONTROL L600  <AreaA_Prison2.GoodbyeNotRescued>
ROW CAT:O1823dafa9da691ff7005 L601 * physical_line
  EN: Where are you going?! You still haven't bred me yet!
  ZH:   * 你要去哪儿？！你还没跟我繁殖呢！

## SC3261048b8f9882eb | sfw | datadm/all.ds | AreaA_Prison2.GoodbyeNotRescued
CONTROL L601  <AreaA_Prison2.GoodbyeNotRescued>
ROW SFW588f8c2e983eea35171e2fdf L602 - physical_line
  EN: Where are you going?! You're supposed to mount a heroic rescue, you know!
  ZH:   * 你要去哪儿？！你该来场英雄救援才对啊！

## SC5e6ba896ccf2a886 | sfw | datadf/all.ds | AreaA_Prison2.Hello
CONTROL L594  <AreaA_Prison2.Hello>
ROW SFW8847dd95e3974b5a267ec4b4 L595 - physical_line
  EN: Well you aren't the person I was wanting to see!
  ZH:   * 哎，你可不是我想见的那个人呀！
ROW SFW0d7b5ab46216c084692c1e1c L596 - physical_line
  EN: Do you really think you're strong enough to break this barrier?
  ZH:   * 你真觉得自己有那么大力气，能打破这道屏障？

## SC63dac09b904f03d5 | nsfw | datadf/all.ds | AreaA_Prison2.HelloDog
CONTROL L604  <AreaA_Prison2.HelloDog>
ROW CAT:O62b7740d1fca7c297318 L605 * physical_line
  EN: Pft, a little dog.
  ZH:   * 噗，原来是条小狗。

## SC8dc44719b8e69cce | nsfw | datadf/all.ds | AreaA_Prison2.Purchased
CONTROL L623  <AreaA_Prison2.Purchased>
ROW CAT:O7bee297aee30ca707aa2 L624 * physical_line
  EN: Aaa...aaah! That hits the spot!
  ZH:   * 啊……啊啊！就是这个感觉！

## SC94c4f739233fad76 | nsfw | datadm/all.ds | AreaA_Prison2.Purchased
CONTROL L622  <AreaA_Prison2.Purchased>
ROW CAT:Od71c5e0a637cc05f8df4 L623 * physical_line
  EN: Oh! Miracle!
  ZH:   * 哦！奇迹！

## SCf40c95f47fba2a98 | sfw | datadm/all.ds | AreaA_Prison2.Rescue
CONTROL L619  <AreaA_Prison2.Rescue>
ROW SFWfae2ed7675b11ad64cac427a L620 - physical_line
  EN: I've tried everything to break that barrier, but it's no good!
  ZH:   * 我什么办法都试过了，就是打不破那道屏障！
ROW SFW582ffa5d10119449ed8ba90d L621 - physical_line
  EN: Maybe you could disrupt it with a tazer strike...?
  ZH:   * 也许你用电击器打一下，就能扰乱它……？

## SC2b46c7f79732062f | nsfw | datadm/all.ds | AreaA_Prison2.SoldOut
CONTROL L625  <AreaA_Prison2.SoldOut>
ROW CAT:Of01f4d54a9f579546b54 L626 * physical_line
  EN: Thanks lad. I'm fine now, just catching my breath...
  ZH:   * 谢啦，小子。我现在没事了，就是还在喘口气……

## SC218d0712a2259add | nsfw | datadm/all.ds | AreaA_Prison2.TalkAfterRescue.thanks
CONTROL L632  <AreaA_Prison2.TalkAfterRescue.thanks>
ROW CAT:O26b8a3fde538f0bf552b L633 * physical_line
  EN: Good heavens, I don't know what came over me!
  ZH:   * 天哪，我都不知道自己是怎么了！
ROW CAT:O8f8897f14a5716b254d9 L634 * physical_line
  EN: There was this blue light, and after that... I got so hot...
  ZH:   * 当时有一道蓝光，之后……我就浑身发烫……

## SC3bf1546196e1da59 | sfw | datadm/all.ds | AreaA_Prison2.TalkAfterRescue.thanks
CONTROL L633  <AreaA_Prison2.TalkAfterRescue.thanks>
ROW SFW6595373b47d69c1cb7a7700c L634 - physical_line
  EN: I'll be sure not to go poking my nose where it doesn't belong, next time!
  ZH:   * 下次我一定不再打探不该打探的事了！

## SCc81059a0b184badd | sfw | datadf/all.ds | AreaA_Prison2.TalkAfterRescue.thanks
CONTROL L634  <AreaA_Prison2.TalkAfterRescue.thanks>  
ROW SFW62ddb98568d887d5fd17b9bc L635 - physical_line
  EN: Yeah yeah... Don't go around all puffed up over this.
  ZH:   * 好啦好啦……别因为这点事就到处得意。

## SCf2f99fa348e01ca8 | sfw | datadm/all.ds | AreaA_Prison2.TalkBeforeRescue.bopped
CONTROL L629  <AreaA_Prison2.TalkBeforeRescue.bopped>
ROW SFW774b6b6f7e2c63fc3fabf939 L630 - physical_line
  EN: I was investigating this room for clues, when someone turned the barrier on...
  ZH:   * 我正在这个房间里找线索，不知谁就把屏障打开了……
ROW SFW81d614aa1536e0a30d027ed1 L631 - physical_line
  EN: Trapped like a kit, how amateurish...
  ZH:   * 像只小猫一样被困住，真不专业……

## SCfb4b57ea9da4bed5 | nsfw | datadf/all.ds | AreaA_Prison3.Goodbye
CONTROL L639  <AreaA_Prison3.Goodbye>
ROW CAT:O0044b77e1a2e75fdb0cf L640 * physical_line
  EN: Fine, fine! I'll get back to work too!
  ZH:   * 好啦好啦！我也回去干活！

## SC68afd95f41550cf0 | sfw | datadm/all.ds | AreaA_Prison3.Goodbye
CONTROL L639  <AreaA_Prison3.Goodbye>
ROW SFW866c8e61078c1e9aed4773ea L640 - physical_line
  EN: Thank you Yiffai!
  ZH:   * 谢谢你，伊吠！

## SC6a5db3ffe4f4479e | sfw | datadf/all.ds | AreaA_Prison3.GoodbyeDog
CONTROL L651  <AreaA_Prison3.GoodbyeDog>
ROW SFWd8301c8af702880615c1342d L652 - physical_line
  EN: Seeya girl! Be careful out there!
  ZH:   * 再见啦，小姑娘！在外面小心点！

## SC85960aca229e654f | nsfw | datadm/all.ds | AreaA_Prison3.HelloDog
CONTROL L646  <AreaA_Prison3.HelloDog>
ROW CAT:Ocbc7efa54a05b0febcbe L647 * physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SCd70921b628f0f5ed | sfw | datadf/all.ds | AreaA_Prison3.HelloDog
CONTROL L645  <AreaA_Prison3.HelloDog>
ROW SFW1e1ed089df1f33039f328608 L646 - physical_line
  EN: Aww, it's a little dog!
  ZH:   * 哎呀，是只小狗！

## SC52b927619f260911 | nsfw | datadf/all.ds | AreaA_Prison3.Rescue
CONTROL L660  <AreaA_Prison3.Rescue>
ROW CAT:O75f41a47c82f2907b5b5 L661 * physical_line
  EN: Huh? You wanna rescue me?
  ZH:   * 咦？你是想救我吗？

## SCa60248cb1f5e07da | nsfw | datadm/all.ds | AreaA_Prison3.TalkBeforeRescue.bopped
CONTROL L678  <AreaA_Prison3.TalkBeforeRescue.bopped>
ROW CAT:O4d7cd95b9852904b98fa L679 * physical_line
  EN: I thought you were a dwarf at first. It got me... got me a little excited...
  ZH:   * 我一开始还以为你是矮人，害我……有点兴奋了……

## SCf9fd8c0e09990171 | nsfw | datadf/all.ds | AreaA_Prison3.TalkBeforeRescue.bopped
CONTROL L672  <AreaA_Prison3.TalkBeforeRescue.bopped>
ROW CAT:O830b3ef2e8c49cd06ce8 L673 * physical_line
  EN: It's been pretty nice down here, don't you think?
  ZH:   * 这下面待着还挺不错的，你不觉得吗？
ROW CAT:Ob06df14c36db584e5555 L674 * physical_line
  EN: Those kobolds are all sorts of wonderful, aren't they!
  ZH:   * 那些科博德真是样样都棒，对吧！

## SC2886d89df40af4d4 | nsfw | datadm/all.ds | AreaB_Macsen1.Goodbye
CONTROL L733  <AreaB_Macsen1.Goodbye>
ROW CAT:Ocf9d5b770be7acb96e6b L734 * physical_line
  EN: Bye bye! Come back with lots of Lect!
  ZH:   * 再见啦！下次记得多带点Lect来！

## SC102ef0723f41cf07 | sfw | datadm/all.ds | AreaB_Macsen1.Talk.digging
CONTROL L744  <AreaB_Macsen1.Talk.digging>
ROW SFWc493725819824072cebe2d29 L745 - physical_line
  EN: You look like a smart and eager dog!
  ZH:   * 你看起来真是只聪明又有干劲的狗！
ROW SFW98ad78f0e0091dccd4f77ac6 L746 - physical_line
  EN: Did you know that ferals are able to dig up dirt by pressing DOWN+ATTACK?
  ZH:   * 你知道野兽形态可以按DOWN+ATTACK挖开泥土吗？
ROW SFW74f87662f3a92214d476bd7a L747 - physical_line
  EN: It's just good info to know, ya know!
  ZH:   * 这可是实用的小知识，记着没坏处！

## SC02651320990de5d2 | nsfw | datadm/all.ds | AreaB_Macsen1.Talk.psychic
CONTROL L752  <AreaB_Macsen1.Talk.psychic>
ROW CAT:Of2b702814554b874dc29 L753 * physical_line
  EN: I've heard rumors of Espers running around nowadays! Ridiculous!
  ZH:   * 听说最近有超能力者四处活动！真是荒唐！
ROW CAT:O5e2b56994b05cde50c4c L754 * physical_line
  EN: They say some can even shoot energy to hit switches from far away, bah!
  ZH:   * 还说有些能发射能量，隔着老远打中开关，呸！

## SCfd1d3fdb486e196e | nsfw | datadm/all.ds | AreaB_Macsen2.Talk.macsenhard
CONTROL L807  <AreaB_Macsen2.Talk.macsenhard>
ROW CAT:O4d114b4e6c643524d725 L808 * physical_line
  EN: Running all these shops all over Tutone, all at once... it's hard work!
  ZH:   * 图托恩各处这么多店同时开着……真辛苦！
ROW CAT:Oc9b378982137fe4fe315 L809 * physical_line
  EN: Not nearly as hard as developing Cosmobreeder Yiffai, but hard work still!
  ZH:   * 没开发《宇宙育种者伊吠》苦，可挺累人！

## SC88782d785607efb5 | nsfw | datadf/all.ds | AreaB_Macsen2.Talk.macsenlect
CONTROL L798  <AreaB_Macsen2.Talk.macsenlect>
ROW CAT:O6fbd1c1c1c366f57badc L799 * physical_line
  EN: Take some lect, but don't tell anyone, alright?
  ZH:   * 拿点 lect 吧，可别跟人说，行吗？

## SC02a5fcd34757a0c1 | nsfw | datadf/all.ds | AreaB_MacsenBar.Goodbye
CONTROL L858  <AreaB_MacsenBar.Goodbye>
ROW CAT:O878aff1d70d3f4c1b9ae L859 * physical_line
  EN: Bye for now! You take care, you hear!
  ZH:   * 先这样啦！你多保重，听见没！

## SCaa21f88c465b7b03 | nsfw | datadm/all.ds | AreaB_MacsenBar.Hello
CONTROL L861  <AreaB_MacsenBar.Hello>
ROW CAT:Of5b7d188dce95b526399 L862 * physical_line
  EN: Hey there! Don't be a stranger, come on in!
  ZH:   * 嘿，你好！别见外，快进来吧！

## SC0444d990ee0d8a7a | nsfw | datadf/all.ds | AreaB_MacsenBar.Talk.main
CONTROL L861  <AreaB_MacsenBar.Talk.main>
CONTROL L862    if { !f(ClassicWerepup_defeated)} {
ROW CAT:O3ab10f899de502b7306d L863 * physical_line
  EN: You're kinda early! Come back later and we can chat and drink, alright?
  ZH:     * 你来得有点早！晚点再来，咱们喝点东西聊聊天，好吗？
CONTROL L864    } else {
ROW CAT:O031254b381ae84ab74d2 L865 * physical_line
  EN: Well! That last quake just wrecked my whole supply!
  ZH:     * 唉！上次地震把我的存货全毁了！
ROW CAT:Oc46c21647ea15ef08367 L866 * physical_line
  EN: I'll tell you what though, you seem like you're a good strong pupper.
  ZH:     * 不过说真的，你看着是只挺棒又壮实的狗狗。
ROW CAT:O22f07ef3a60a3d751fce L867 * physical_line
  EN: Another one of you cosmofellas came by muttering that they left
  ZH:     * 之前还来过一个跟你一样的太空伙计，嘴里嘀咕着说把武器落在这儿正北边了！ 
ROW CAT:O434628caa40bba19c819 L868 * physical_line
  EN: their weapon just north of here!
  ZH: 
ROW CAT:Ob8dbc4902ce1b85335ad L869 * physical_line
  EN: "Bottom, middle, middle, top..." is what they kept saying, whatever that means!
  ZH:     * 那家伙一直念叨着"下、中、中、上……"，谁知道是什么意思！
CONTROL L870    }

## SC7f3564da7c4a6f4f | nsfw | datadf/all.ds | AreaB_MacsenBar.Talk.weapon
CONTROL L872  <AreaB_MacsenBar.Talk.weapon>
CONTROL L873    if { f(ClassicWerepup_defeated) } {
ROW CAT:Ocd031afad8d2ed20943c L874 * physical_line
  EN: If nobody's claimed that ol' weapon yet, it's as good as yours, I say! Take it!
  ZH:     * 要是那把旧武器还没人认领，我说就归你了！拿去吧！
CONTROL L875    }
CONTROL L877  ### shared ###

## SCc295d0242e02aa69 | sfw | datadf/all.ds | AreaB_Prison1.CancelPurchase
CONTROL L935  <AreaB_Prison1.CancelPurchase>
ROW SFW580acda437f7c0571feb8609 L936 - physical_line
  EN: Oh... I guess you aren't going to let me out...?
  ZH:   * 哦……看来你不打算放我出去……？

## SC26ff0e59ade1d3c4 | nsfw | datadm/all.ds | AreaB_Prison1.Goodbye
CONTROL L923  <AreaB_Prison1.Goodbye>
ROW CAT:Oa442e1d877ecb0d1380d L924 * physical_line
  EN: I'll be right behind you. I'm just a little tied up right now!
  ZH:   * 我马上就跟在你后面。只是我现在有点脱不开身！

## SCcbf017b30c0a13e0 | sfw | datadf/all.ds | AreaB_Prison1.Goodbye
CONTROL L917  <AreaB_Prison1.Goodbye>
ROW SFW821fd530496636fb9a822f11 L918 - physical_line
  EN: I'll be right along, heheh! My leg kinda fell asleep...
  ZH:   * 我马上跟上，嘿嘿！腿好像有点麻了……

## SCcc36ac151e84a0cf | nsfw | datadf/all.ds | AreaB_Prison1.GoodbyeDog
CONTROL L929  <AreaB_Prison1.GoodbyeDog>
ROW CAT:Of3ff0bf884a5c8960b63 L930 * physical_line
  EN: That's right! You keep away from him!!!
  ZH:   * 这就对啦！给我离他远点！！！

## SCf6fa59a83a17aa0b | sfw | datadf/all.ds | AreaB_Prison1.GoodbyeDog
CONTROL L929  <AreaB_Prison1.GoodbyeDog>
ROW SFWb9f47c9f2c3ae592336cab32 L930 - physical_line
  EN: Oh, are you going to get help? Yay!
  ZH:   * 哦，你要去找人帮忙吗？太好啦！

## SC5a0d86eaf439f374 | sfw | datadf/all.ds | AreaB_Prison1.GoodbyeNotRescued
CONTROL L920  <AreaB_Prison1.GoodbyeNotRescued>
ROW SFWc46299324e398c2372272b33 L921 - physical_line
  EN: Bye bye! I'll be waiting...
  ZH:   * 再见啦！我会等着的……

## SCb46b5fe12eaad81e | nsfw | datadm/all.ds | AreaB_Prison1.Hello
CONTROL L920  <AreaB_Prison1.Hello>
ROW CAT:O2c8d2b527fca7676245c L921 * physical_line
  EN: I... I can explain! This isn't what it looks like!
  ZH:   * 我……我可以解释！不是你想的那样！

## SC51effdac124682a6 | sfw | datadm/all.ds | AreaB_Prison1.Hello
CONTROL L917  <AreaB_Prison1.Hello>
ROW SFW701295d1f3ec63a145e1f079 L918 - physical_line
  EN: Oh, hey! I was just about to break out of here!
  ZH:   * 哦，嗨！我正要从这里逃出去呢！

## SC3e907a66719a8ae8 | nsfw | datadm/all.ds | AreaB_Prison1.HelloDog
CONTROL L929  <AreaB_Prison1.HelloDog>
ROW CAT:O4221699e036d26cea6bd L930 * physical_line
  EN: Oh no, another one?!
  ZH:   * 哎呀，又来一个？！

## SC447edf58e9684975 | nsfw | datadm/all.ds | AreaB_Prison1.Purchased
CONTROL L949  <AreaB_Prison1.Purchased>
ROW CAT:Oe1d10b27c6bca87f690d L950 * physical_line
  EN: Aaah! I... I mean, th-thank you!
  ZH:   * 啊——！我……我是说，谢、谢谢你！

## SC6dbc84cf754d4768 | sfw | datadm/all.ds | AreaB_Prison1.Rescue
CONTROL L941  <AreaB_Prison1.Rescue>
ROW SFW6feeeca4005ff09021e165fe L942 - physical_line
  EN: I've just about got this door open.
  ZH:   * 我就快把这扇门弄开了。
ROW SFWb17b0c271e0297edbcb7a9f6 L943 - physical_line
  EN: But if you wanna try to break it down, I guess I can't complain...
  ZH:   * 不过你要想试着把门砸开，我也没什么好抱怨的……

## SCa79531ba58e731a1 | sfw | datadf/all.ds | AreaB_Prison1.Rescue
CONTROL L938  <AreaB_Prison1.Rescue>
ROW SFW5da56e301eaa55e5c5897a28 L939 - physical_line
  EN: I've been cooped up in here forever and it's sooo boring!
  ZH:   * 我被关在这里好久了，真是无聊透了！
ROW SFW102beffce3bf0dca14505fb0 L940 - physical_line
  EN: Will you let me out, pleeease?
  ZH:   * 放我出去好不好，求——你啦？

## SC9856d98bab0b75d6 | nsfw | datadf/all.ds | AreaB_Prison1.SoldOut
CONTROL L944  <AreaB_Prison1.SoldOut>
ROW CAT:O9e4db16cca89e609b886 L945 * physical_line
  EN: Thanks for double-checking, but we'll be fine!
  ZH:   * 谢谢你特地来确认，不过我们没事的！

## SC590caa365ebd459d | sfw | datadf/all.ds | AreaB_Prison1.SoldOut
CONTROL L945  <AreaB_Prison1.SoldOut>
ROW SFW5b53a9caa743a3a13afb7338 L946 - physical_line
  EN: Thanks for double-checking, but I'll be fine!
  ZH:   * 谢谢你又来确认，不过我没事啦！

## SC3937b79005755a5b | sfw | datadf/all.ds | AreaB_Prison2.CancelPurchase
CONTROL L976  <AreaB_Prison2.CancelPurchase>
CONTROL L977    if { hasItem(Key) } {
ROW SFW1745e272063ab8c1b761b845 L978 - physical_line
  EN: Don't tease me... please... just lemme out now!
  ZH:     * 别逗我了……求你……现在就放我出去吧！
CONTROL L979    } else {
ROW SFW73e63e9c71943d4ff00add62 L980 - physical_line
  EN: You'll need a key! I've tried... everything...
  ZH:     * 你得有钥匙！我已经……什么办法都试过了……
CONTROL L981    }

## SCc05323265c94270b | nsfw | datadm/all.ds | AreaB_Prison2.GoodbyeNotRescued
CONTROL L967  <AreaB_Prison2.GoodbyeNotRescued>
ROW CAT:Oe93afa769b6550bb218b L968 * physical_line
  EN: Recovering that key is your highest priority. Get to it!
  ZH:   * 找回那把钥匙是你最优先的任务。快去办！

## SC095a110a8d194b36 | nsfw | datadf/all.ds | AreaB_Prison2.Hello
CONTROL L953  <AreaB_Prison2.Hello>
ROW CAT:Odc364dc77ba6eefe8d87 L954 * physical_line
  EN: Ooo...oohhh! You're a sight for sore eyes! Haah!
  ZH:   * 哦……哦哦！看见你真是让我眼前一亮！哈啊！

## SCb142bdb931cd2d13 | nsfw | datadm/all.ds | AreaB_Prison2.HelloDog
CONTROL L970  <AreaB_Prison2.HelloDog>
ROW CAT:Ob2396f8059ceea0963c3 L971 * physical_line
  EN: A dog, really?
  ZH:   * 真的是条狗？

## SC549182dd21184f47 | sfw | datadf/all.ds | AreaB_Prison2.NotEnoughMoney
CONTROL L989  <AreaB_Prison2.NotEnoughMoney>
ROW SFW3f3438dced91223a45c927f6 L990 - physical_line
  EN: You'll need a key! I've tried... everything...
  ZH:   * 你得有钥匙！我已经……什么办法都试过了……

## SC40bbf66c1e6fbe63 | nsfw | datadf/all.ds | AreaB_Prison2.Purchased
CONTROL L986  <AreaB_Prison2.Purchased>
ROW CAT:O7c1ec0157eaf4a0abbb2 L987 * physical_line
  EN: H-haaah... aaah... hhhh... Th-thanks...
  ZH:   * 哈——啊……啊啊……呼……谢、谢谢……

## SC7bf9e5d136190146 | nsfw | datadf/all.ds | AreaB_Prison2.Rescue
CONTROL L982  <AreaB_Prison2.Rescue>
ROW CAT:Of0edc66325fa329f2fed L983 * physical_line
  EN: There's a little keyhole on this r-robot... It's the only... nnnh...
  ZH:   * 机、机器人上有个小锁孔……这是唯一……唔嗯……
ROW CAT:O22abb7d78d813f870473 L984 * physical_line
  EN: ...the only way to disable it..!
  ZH:   * ……唯一能让它停下来的办法..！

## SCbcee963a8e061333 | nsfw | datadm/all.ds | AreaB_Prison2.TalkAfterRescue.thanks
CONTROL L1004  <AreaB_Prison2.TalkAfterRescue.thanks>
ROW CAT:O106a9479b910b4b26c5f L1005 * physical_line
  EN: Tch, should have just done this myself! Now don't you have errands to run, rookie?
  ZH:   * 啧，早该自己动手的！你手上不是还有跑腿的活儿吗，菜鸟？

## SC9ef89339d0723201 | sfw | datadf/all.ds | AreaB_Prison2.TalkAfterRescue.thanks
CONTROL L999  <AreaB_Prison2.TalkAfterRescue.thanks>
ROW SFW7968bccea81b785fea25b575 L1000 - physical_line
  EN: Actually I feel like my legs are kinda cramped now...
  ZH:   * 其实现在感觉腿好像有点抽筋了……
ROW SFWe28c7b674b769e66cfa15ec0 L1001 - physical_line
  EN: So I'll probably just make my way back to the hangar and relax.
  ZH:   * 所以我大概会先慢慢回机库，休息一下。

## SC2e75838ad73cb4b9 | sfw | datadf/all.ds | AreaB_Prison2.TalkBeforeRescue.bopped
CONTROL L995  <AreaB_Prison2.TalkBeforeRescue.bopped>
ROW SFWf4d32aac31854d47f0299307 L996 - physical_line
  EN: They locked me up in this cell as soon as we landed!
  ZH:   * 我们刚降落，他们就把我关进了这间牢房！
ROW SFW6f49a34b05b3a6e65ab1c23f L997 - physical_line
  EN: I'm going stir crazy in here! I just wanna ruuun!
  ZH:   * 我被关得都快疯了！我只想出去跑——啊！

## SC386e9764643b6fe3 | nsfw | datadm/all.ds | AreaB_Slaver2.FakeDrumstick
CONTROL L1041  <AreaB_Slaver2.FakeDrumstick>
ROW CAT:O673b32ac7787ca271098 L1042 * physical_line
  EN: The slaves always gimme lip about the flies. Extra protein, I say!
  ZH:   * 奴隶老跟我抱怨苍蝇。我说这叫加餐补蛋白！

## SC1c6c48638a76ce0c | nsfw | datadf/all.ds | AreaB_Slaver2.FakeMilk
CONTROL L1039  <AreaB_Slaver2.FakeMilk>
ROW CAT:Obb3250c1c0e9794db4d8 L1040 * physical_line
  EN: I gotta be honest with you, I don't know what animal this is from.
  ZH:   * 说实话，我也不知道这是从哪种动物身上弄来的。
ROW CAT:O7c23f6cc37b162a9757c L1041 * physical_line
  EN: Makes for good drinkin' if you're *real* thirsty though.
  ZH:   * 不过你要是*真*渴得不行，喝着倒还不错。

## SC42a73ad2c2101977 | nsfw | datadm/all.ds | AreaB_Slaver2.Goodbye
CONTROL L1013  <AreaB_Slaver2.Goodbye>
CONTROL L1014    if { !koboCostume() } {
ROW CAT:Oc160a9542b78467eede5 L1015 * physical_line
  EN: Be seeing you. Heh-heh...
  ZH:     * 回头见。嘿嘿……
CONTROL L1016    } else {
ROW CAT:O0d856bb0dca247e329be L1017 * physical_line
  EN: Take care out there. Ole Tutone's a rough place these days.
  ZH:     * 出去小心点。如今的图托恩可不太平。
CONTROL L1018    }

## SC03630a78f7879b43 | nsfw | datadf/all.ds | AreaB_Slaver2.GoodbyeDog
CONTROL L1069  <AreaB_Slaver2.GoodbyeDog>
ROW CAT:Oa5065ec95ae9fde4c5ad L1070 * physical_line
  EN: Scram, mutt! Get back in the cage!
  ZH:   * 滚开，杂种狗！回笼子里去！

## SC99270b5c8b9b035e | nsfw | datadm/all.ds | AreaB_Slaver2.Hello
CONTROL L1006  <AreaB_Slaver2.Hello>
CONTROL L1007    if { !koboCostume() } {
ROW CAT:O325d443ba58f267f7a70 L1008 * physical_line
  EN: Well hey there, boy. I gots some real pree-mo dining here.
  ZH:     * 哟，小子。我这儿有真正的顶——级美食。
CONTROL L1009    } else {
ROW CAT:Oa8c38f65b94b33cea528 L1010 * physical_line
  EN: Well look what we have here! Come in, come in! Welcome to my junk shop!
  ZH:     * 哟，瞧瞧谁来了！快进来！欢迎光临我的废品铺！
CONTROL L1011    }

## SC9622df486cad4f14 | nsfw | datadm/all.ds | AreaB_Slaver2.NoInventorySpace
CONTROL L1037  <AreaB_Slaver2.NoInventorySpace>
ROW CAT:Oee9c67b7f01448678b0f L1038 * physical_line
  EN: Hey, you don't even have room for that!
  ZH:   * 喂，你都没地方装这个了！
CONTROL L1040  ### as anthro:

## SCa55d756c24dca8e1 | nsfw | datadf/all.ds | AreaB_Slaver2.NoInventorySpace
CONTROL L1032  <AreaB_Slaver2.NoInventorySpace>
ROW CAT:O11f986326d9ddae6764e L1033 * physical_line
  EN: Hey, you don't even have room for that!
  ZH:   * 喂，你都没地方装这个了！
CONTROL L1035  ### as anthro:

## SCdfe0175e853510bf | nsfw | datadf/all.ds | AreaB_Slaver2.Purchased
CONTROL L1015  <AreaB_Slaver2.Purchased>
CONTROL L1016    if { !koboCostume() } {
ROW CAT:Od5552526db335bcbe06e L1017 * physical_line
  EN: Remember, no refunds! What else you need? He! He! He!
  ZH:     * 记住，概不退款！还要什么？嘿！嘿！嘿！
CONTROL L1018    } else {
ROW CAT:Oeb07049b58c46820395d L1019 * physical_line
  EN: Thanks for taking that off my hands.
  ZH:     * 多谢你帮我把这东西脱手。
ROW CAT:O6c719303b0316d026c91 L1020 * physical_line
  EN: They get a bit uppity at 3P stations when you gots stolen equipment...
  ZH:     * 带着偷来的装备去3P站点，那帮人可就要摆脸色了……
CONTROL L1021    }

## SCfcb71b54b51a9117 | nsfw | datadf/all.ds | AreaC_Macsen1.Goodbye
CONTROL L1120  <AreaC_Macsen1.Goodbye>
ROW CAT:O13c287cbb149c3ca5047 L1121 * physical_line
  EN: Grrr, bring more Lect with you next time, ya scoundrel!
  ZH:   * 咕呜，下次多带点 Lect 来，你这混蛋！

## SC8d807151c05c32e6 | nsfw | datadm/all.ds | AreaC_Macsen1.Hello
CONTROL L1123  <AreaC_Macsen1.Hello>
ROW CAT:O38e80918cf40fa4f5bd6 L1124 * physical_line
  EN: Rawr! Come right on in, but only if you have plenty of Lect on you! Rawr!
  ZH:   * 嗷！尽管进来，不过身上得带够Lect才行！嗷！

## SCe07f941205affd55 | nsfw | datadf/all.ds | AreaC_Macsen1.KoboHead
CONTROL L1123  <AreaC_Macsen1.KoboHead>
ROW CAT:Oc80241481615af86b42f L1124 * physical_line
  EN: Look I know it's hard to believe, but I'm not actually a Kobold pirate!
  ZH:   * 听着，我知道这很难相信，但我其实不是科博德海盗！
ROW CAT:Ob9d16ca25e6e628e52b8 L1125 * physical_line
  EN: It's true! But if you want a disguise as good as mine, you can buy this.
  ZH:   * 真的！不过你要是想弄一身跟我一样好的伪装，可以买这个。
ROW CAT:Oc0ae38cfcc232a3a0d02 L1126 * physical_line
  EN: You'll need the full set in order to fool folks, but trust me...
  ZH:   * 想骗过别人，你得凑齐一整套，不过相信我……
ROW CAT:Occd5010f21ae33c7a996 L1127 * physical_line
  EN: ...it's the only way to get the GOOD goods from the slavers, hehe!
  ZH:   * ……这是从奴隶贩子那儿弄到「好货」的唯一办法，嘿嘿！
ROW CAT:O950c8a72d163d6803c09 L1128 * physical_line
  EN: Plus, I'll throw in a map to the other disguise parts too!
  ZH:   * 另外，我还会顺带送你一张标注其他伪装部件的地图！

## SC20a7eadc70024510 | nsfw | datadf/all.ds | AreaC_Macsen1.PsyUp
CONTROL L1130  <AreaC_Macsen1.PsyUp>
ROW CAT:Ob4c83a8a09d808080eab L1131 * physical_line
  EN: A real live psy crystal, just like those espers use!
  ZH:   * 货真价实的精神力水晶，跟那些超能力者用的一样！

## SCfb5ce47a844e2ed2 | nsfw | datadm/all.ds | AreaC_Macsen1.VitHam
CONTROL L1139  <AreaC_Macsen1.VitHam>
ROW CAT:O4917792d64f1ae457641 L1140 * physical_line
  EN: Just look at this thick and meaty shank! Juicy and VIT-filling!
  ZH:   * 瞧瞧这粗壮又多肉的腿肉！鲜嫩多汁，还能补充活力！

## SC8f0d020e73951eba | nsfw | datadf/all.ds | AreaC_MacsenDark.Goodbye
CONTROL L1192  <AreaC_MacsenDark.Goodbye>
ROW CAT:O50cab305f13527255960 L1193 * physical_line
  EN: If you come across a lantern or something, come share some light with me, eh?
  ZH:   * 要是找到灯笼什么的，就来给我也照个亮，好吗？

## SC47ecd174fae5a977 | sfw | datadf/all.ds | AreaC_MacsenDark.Hello
CONTROL L1189  <AreaC_MacsenDark.Hello>
ROW SFW86ecd119fcc94599708e4a5b L1190 - physical_line
  EN: And here you are, to brighten up my day!
  ZH:   * 你一来，我这一天都亮堂了！
ROW SFWb2b5e749e9cbab9e54b4f428 L1191 - physical_line
  EN: You and that torch are lifesavers.
  ZH:   * 你和那支手电筒真是救星。

## SC534b27bb191911f5 | nsfw | datadf/all.ds | AreaC_MacsenDark.Talk.dark
CONTROL L1210  <AreaC_MacsenDark.Talk.dark>
CONTROL L1211    if { !hasItem(SpecialTorch) } {
ROW CAT:Ob95ef78e84ba798884ae L1212 * physical_line
  EN: This is just my luck, isn't it?
  ZH:     * 我的运气还真是好啊，是吧？ 
ROW CAT:Oa8a4fb600f3df8be180f L1213 * physical_line
  EN: First somewan stole my hookshot so I have to walk around on these tiny legs...
  ZH:     * 先是有人偷了我的钩索，害我只能靠这两条小短腿走路……
ROW CAT:O77ebcefd2800f088d273 L1214 * physical_line
  EN: ...and now the power is out and my flashlight is missing! Bah!
  ZH:     * ……而现在又停电了，手电筒也不见了！哼！
CONTROL L1215    } else {
ROW CAT:O654b8158137a8aeb684e L1216 * physical_line
  EN: It's been getting ruffer and ruffer to do business around these parts, let me tell ya.
  ZH:     * 跟你说吧，在这一带做生意是越来越难了。
ROW CAT:O4113d2ae60c091d2536f L1217 * physical_line
  EN: Earthquakes happen every other hour and the monsters are rowdier than ever...
  ZH:     * 隔一个小时就地震一次，魔物也比以前更闹腾了……
ROW CAT:Od5947bec4d6c7770a0c6 L1218 * physical_line
  EN: ...it almost feels like things are building up to something!
  ZH:     * ……总觉得好像有什么大事要发生了！
CONTROL L1219    }

## SC5bfd0cc89033dc2e | nsfw | datadm/all.ds | AreaC_MacsenDark.Vitamin
CONTROL L1211  <AreaC_MacsenDark.Vitamin>
ROW CAT:O60f31ccb7a6c251f0d9b L1212 * physical_line
  EN: This here little pill will perk you up, thicken your hair, straighten yer back...
  ZH:   * 这颗小药丸能让你精神抖擞、毛发浓密、腰板挺直……
ROW CAT:O10872fe59d216a56591c L1213 * physical_line
  EN: ...and even increase your vitality!
  ZH:   * ……甚至还能提升你的活力！
ROW CAT:O925c6201d544d909308b L1214 * physical_line
  EN: Now how about that?
  ZH:   * 怎么样，厉害吧？

## SCa3c895be8d0fec9a | nsfw | datadf/all.ds | AreaC_MacsenDark.Vitamin
CONTROL L1205  <AreaC_MacsenDark.Vitamin>
ROW CAT:O3f5564dfc1be9fda9935 L1206 * physical_line
  EN: This here little pill will perk you up, thicken your hair, straighten yer back...
  ZH:   * 这颗小药丸能让你精神抖擞、毛发浓密、腰板挺直……
ROW CAT:O5104dac36ef53a906e77 L1207 * physical_line
  EN: ...and even increase your vitality!
  ZH:   * ……甚至还能提升你的活力！
ROW CAT:O4b48aa7f81ac2bf52616 L1208 * physical_line
  EN: Now how about that?
  ZH:   * 怎么样，厉害吧？

## SC51771f2833901b07 | nsfw | datadm/all.ds | AreaC_Prison1.GoodbyeNotRescued
CONTROL L1278  <AreaC_Prison1.GoodbyeNotRescued>
ROW CAT:Oce8d56f5208d12d69a24 L1279 * physical_line
  EN: Now this ain't funny, pup! You get back here!
  ZH:   * 这可不好笑，小狗！给我回来！

## SCd55b475708227a41 | nsfw | datadm/all.ds | AreaC_Prison1.Hello
CONTROL L1272  <AreaC_Prison1.Hello>
ROW CAT:O44500c43a3eabb68e6a6 L1273 * physical_line
  EN: H-howdy friend! I'd give ya a warm welcome, but I'm awful bound up!
  ZH:   * 你、你好啊朋友！我本想热情欢迎你，可我实在被绑得死死的！

## SCb4b182f56b8fa17b | sfw | datadm/all.ds | AreaC_Prison1.Hello
CONTROL L1268  <AreaC_Prison1.Hello>
ROW SFW322bb33cdeeb3117bc7f21ac L1269 - physical_line
  EN: H-howdy friend! I'd give ya a warm welcome, but I'm awful cooped up!
  ZH:   * 你、你好啊，朋友！我倒想热情招呼你，可我被关在这儿，实在施展不开！

## SC9a40976d513b08e3 | sfw | datadm/all.ds | AreaC_Prison1.HelloDog
CONTROL L1277  <AreaC_Prison1.HelloDog>
ROW SFW610df8ea20f03af18e3f4240 L1278 - physical_line
  EN: Well hii there, little doggy! 
  ZH:   * 哎呀，你好呀，小狗狗！ 

## SC10c0f7244e98578c | nsfw | datadm/all.ds | AreaC_Prison1.SoldOut
CONTROL L1302  <AreaC_Prison1.SoldOut>
ROW CAT:Od822bc9eef9b1e1f4837 L1303 * physical_line
  EN: Awful kind of ya, helpin' me, but I'm doin' alright now.
  ZH:   * 你可真够意思，还来帮我；不过我现在已经好多了。

## SC12b5070c6e2b2613 | nsfw | datadf/all.ds | AreaC_Prison1.SoldOut
CONTROL L1296  <AreaC_Prison1.SoldOut>
ROW CAT:O2f4fae9812e8f524f7e9 L1297 * physical_line
  EN: No need. I'll take it from here.
  ZH:   * 不用了。接下来交给我吧。

## SC96fdc8a6cb5c73de | nsfw | datadf/all.ds | AreaC_Prison1.TalkBeforeRescue.bopped
CONTROL L1299  <AreaC_Prison1.TalkBeforeRescue.bopped>
ROW CAT:O3a126abecb8fa91d92e8 L1300 * physical_line
  EN: Look, as nice as it is to chit-chat...
  ZH:   * 听着，闲聊虽然不错…… 
ROW CAT:O55bb16136b34552e285d L1301 * physical_line
  EN: ...we've both got better things to be doing, right?
  ZH:   * ……可我们都有更要紧的事要做，对吧？

## SC6c70b9a5caec10b0 | sfw | datadm/all.ds | AreaC_Prison1.TalkBeforeRescue.bopped
CONTROL L1301  <AreaC_Prison1.TalkBeforeRescue.bopped>
ROW SFWa4420a2f59d17f6e43dc93b7 L1302 - physical_line
  EN: Now why would someone go lockin' up an innocent tod like me?
  ZH:   * 到底谁会把我这么无辜的公狐狸关起来啊？

## SCfb68d7fefb6185af | nsfw | datadf/all.ds | AreaC_Prison2.CancelPurchase
CONTROL L1327  <AreaC_Prison2.CancelPurchase>
ROW CAT:Oc79c734973bfa405d52a L1328 * physical_line
  EN: Meep... Mmmhn... <3
  ZH:   * 嘤……唔嗯……<3

## SC41c8c647818eb3b1 | nsfw | datadm/all.ds | AreaC_Prison2.Goodbye
CONTROL L1314  <AreaC_Prison2.Goodbye>
ROW CAT:Oedc404756cca377cd829 L1315 * physical_line
  EN: Just wait 'til I limber up, those elves won't know what hit 'em!
  ZH:   * 等我活动开筋骨，准让那些精灵吃不了兜着走！

## SCf531148c5a6d7eea | sfw | datadf/all.ds | AreaC_Prison2.GoodbyeNotRescued
CONTROL L1313  <AreaC_Prison2.GoodbyeNotRescued>
ROW SFWb29ff245cf1b7621cdccf41b L1314 - physical_line
  EN: Don't worry about me, ehehe...
  ZH:   * 不用担心我，诶嘿嘿……

## SC478739c707026dda | sfw | datadf/all.ds | AreaC_Prison2.NoBoneForDog
CONTROL L1319  <AreaC_Prison2.NoBoneForDog>
ROW SFWa212b7fe5f6dadc7d6d722e2 L1320 - physical_line
  EN: Do you wanna hang out and enjoy the forest with me?
  ZH:   * 想留下来，和我一起享受森林吗？

## SC231f4f1ca14d5da0 | nsfw | datadm/all.ds | AreaC_Prison2.Rescue
CONTROL L1335  <AreaC_Prison2.Rescue>
ROW CAT:Ofafcac3e3acaf9c37867 L1336 * physical_line
  EN: Mmmh... Hmp.. Hmf?
  ZH:   * 唔嗯……唔噗.. 唔夫？

## SC523dae9fdce26cb8 | sfw | datadm/all.ds | AreaC_Prison2.Rescue
CONTROL L1330  <AreaC_Prison2.Rescue>
ROW SFWc9c439603e6a6538472f15a3 L1331 - physical_line
  EN: I guess if you *really* want to help...
  ZH:   * 我想，要是你*真的*那么想帮忙……

## SC2f7aaefb84a19bd6 | nsfw | datadm/all.ds | AreaC_Prison2.SoldOut
CONTROL L1341  <AreaC_Prison2.SoldOut>
ROW CAT:O49678a2f22762b2c863e L1342 * physical_line
  EN: No more need for your tazer! I'll take it from here!
  ZH:   * 用不着你的电击枪了！接下来交给我！

## SCc459a4dfb2992bc7 | sfw | datadm/all.ds | AreaC_Prison2.TalkAfterRescue.thanks
CONTROL L1343  <AreaC_Prison2.TalkAfterRescue.thanks>
ROW SFWc5eb9fa1dc102fb3019cc358 L1344 - physical_line
  EN: Getting the best of these Sceafyan elves is a real workout!
  ZH:   * 要压过这些斯凯菲亚精灵，还真挺费劲！
ROW SFWce870641832de5493cd9b946 L1345 - physical_line
  EN: But don't worry about me, trainee. I'll be fine.
  ZH:   * 不过别担心我，见习生。我会没事的。

## SC753054d754f9793e | nsfw | datadf/all.ds | AreaC_Prison3.CancelPurchase
CONTROL L1367  <AreaC_Prison3.CancelPurchase>
CONTROL L1368    if { hasItem(Key) } {
ROW CAT:O0a79851b14a886b93152 L1369 * physical_line
  EN: Ohmygod stop being so harsh!
  ZH:     * 我的天，别这么凶嘛！
CONTROL L1370    } else {
ROW CAT:Ode05741f78db308da3f2 L1371 * physical_line
  EN: You're gonna need like, a key, you know...?
  ZH:     * 你得有把钥匙才行，懂吧……？
CONTROL L1372    }

## SCa905db7f03b1c52a | nsfw | datadm/all.ds | AreaC_Prison3.CancelPurchase
CONTROL L1374  <AreaC_Prison3.CancelPurchase>
CONTROL L1375    if { hasItem(Key) } {
ROW CAT:O501dc825e2bcd5990c96 L1376 * physical_line
  EN: Are you teasing me or something? Want me to b-beg for it?
  ZH:     * 你是在逗我还是怎么的？想让我求、求你吗？
CONTROL L1377    } else {
ROW CAT:Off9c6d61c94cb8e5bef5 L1378 * physical_line
  EN: Cute. But unless you're a master locksmith I think you'll need a key.
  ZH:     * 可爱。但除非你是开锁大师，否则我看你得要钥匙。
CONTROL L1379    }

## SC0cc24392c27b5c50 | nsfw | datadf/all.ds | AreaC_Prison3.Goodbye
CONTROL L1349  <AreaC_Prison3.Goodbye>
ROW CAT:O2a5cd521984428a75873 L1350 * physical_line
  EN: You're like, totally awesome, you know?
  ZH:   * 你简直就是超厉害的，你知道吗？

## SC095b00c95c92fbaf | sfw | datadm/all.ds | AreaC_Prison3.GoodbyeNotRescued
CONTROL L1353  <AreaC_Prison3.GoodbyeNotRescued>
ROW SFWa4f41eb35ae910d85ac44fb5 L1354 - physical_line
  EN: Take your time... us senior agents know how to keep our cool.
  ZH:   * 慢慢来……我们这些资深特工，最懂得保持冷静。

## SC003b30ed8f113b7b | nsfw | datadf/all.ds | AreaC_Prison3.Hello
CONTROL L1346  <AreaC_Prison3.Hello>
ROW CAT:Od6e9002251df9bcb48be L1347 * physical_line
  EN: Ohmygawd, it's like, another cosmo-girl! Heeey!
  ZH:   * 天哪，居然又来了个太空女孩！嗨——！

## SC4288d17e43179e2e | nsfw | datadm/all.ds | AreaC_Prison3.Hello
CONTROL L1351  <AreaC_Prison3.Hello>
ROW CAT:O845e6b420d23d764094e L1352 * physical_line
  EN: Oh h-hey, I've been waiting for another agent to stop by.
  ZH:   * 哦，嗨、嗨，我一直在等别的特工过来。
ROW CAT:O6194fde9957d3358e902 L1353 * physical_line
  EN: Got into a spot of trouble. You know how it is... right?
  ZH:   * 遇上了点麻烦。你懂的……对吧？

## SCbbab6a37448de05f | nsfw | datadf/all.ds | AreaC_Prison3.HelloDog
CONTROL L1355  <AreaC_Prison3.HelloDog>
ROW CAT:Od19db865e568b7a6523c L1356 * physical_line
  EN: Oh, it's like, a dog...
  ZH:   * 哦，原来是条狗啊……

## SC955f79d009f4bd08 | sfw | datadm/all.ds | AreaC_Prison3.Purchased
CONTROL L1378  <AreaC_Prison3.Purchased>
ROW SFW0b8c514c279f90d895c4edd2 L1379 - physical_line
  EN: There! We make a great team, with you doing all the work, haha!
  ZH:   * 瞧！我们真是绝佳搭档，活儿全让你干了，哈哈！

## SC36ed87e8e97e4631 | sfw | datadf/all.ds | AreaC_Prison3.TalkAfterRescue.thanks
CONTROL L1392  <AreaC_Prison3.TalkAfterRescue.thanks>
ROW SFW0588c42333a99e5da2d84364 L1393 - physical_line
  EN: You know, I'm gonna miss chilling out here in the forest. 
  ZH:   * 说真的，我会想念在森林里悠闲度日的时光。 
ROW SFWfeb1c4838815e72594c9ac7c L1394 - physical_line
  EN: It's got some totally rad vibes!
  ZH:   * 这里的氛围简直棒极了！

## SCe85d31ce43973a39 | nsfw | datadm/all.ds | AreaC_Prison3.TalkBeforeRescue.bopped
CONTROL L1396  <AreaC_Prison3.TalkBeforeRescue.bopped>
ROW CAT:Oe931d2039905cf021a0e L1397 * physical_line
  EN: Really... I'm a pretty c-cool cat. No rush on the rescue.
  ZH:   * 真的……我这猫可淡、淡定了。不用急着救我。
ROW CAT:Oe7391a2b189ab368554f L1398 * physical_line
  EN: I was the senior top agent deployed to this planet.
  ZH:   * 我可是派驻这颗星球的资深上位特工。
ROW CAT:O28101a2e9a38018277c4 L1399 * physical_line
  EN: If you bust me out of here, I'll turn you a tr- I mean show you a few tricks, haha!
  ZH:   * 把我救出去，我就卖身报——我是说，教你几招，哈哈！

## SCb593a77c58d4a298 | sfw | datadm/all.ds | AreaC_Prison3.TalkBeforeRescue.bopped
CONTROL L1387  <AreaC_Prison3.TalkBeforeRescue.bopped>
ROW SFWf83a7423fd2cba06696746f3 L1388 - physical_line
  EN: Really... I'm a pretty cool cat. No rush on the rescue.
  ZH:   * 真的……我可是只淡定的猫。救援不着急。
ROW SFWb88496ee5d78c21efb073222 L1389 - physical_line
  EN: I was the senior top agent deployed to this planet.
  ZH:   * 我可是派驻这颗星球的资深精英特工。
ROW SFW8378d044b1178c63eceecb36 L1390 - physical_line
  EN: If you bust me out of here, I'll show you a few tricks, haha!
  ZH:   * 你要是把我弄出去，我就教你几招，哈哈！

## SC2f14202d62634a5c | nsfw | datadf/all.ds | AreaC_Slaver1.ElfHead
CONTROL L1433  <AreaC_Slaver1.ElfHead>
ROW CAT:O26a4e208d7d42710ffe2 L1434 * physical_line
  EN: What? You're interested in THAT?
  ZH:   * 什么？你对那玩意儿感兴趣？
ROW CAT:O5fb27cf060d17622e6a3 L1435 * physical_line
  EN: I have the finest food this side of the seven swamps, and you want THAT garbage?
  ZH:   * 我这儿的吃食是七片沼泽这一带最好的，你却想要那种垃圾？
ROW CAT:Ode718f4dfb9c456ea42b L1436 * physical_line
  EN: Fine, but it'll cost ya...
  ZH:   * 行吧，不过这可要花你钱的……

## SC0a3e6e67341ad287 | nsfw | datadf/all.ds | AreaC_Slaver1.HelloDog
CONTROL L1468  <AreaC_Slaver1.HelloDog>
ROW CAT:Of8d66e71900910922902 L1469 * physical_line
  EN: What the-? A dog?!
  ZH:   * 什么鬼——？一条狗？！

## SC385cae2b1c5dce2c | nsfw | datadm/all.ds | AreaC_Slaver1.Purchased
CONTROL L1419  <AreaC_Slaver1.Purchased>
CONTROL L1420    if { !koboCostume() } {
ROW CAT:Obea51e4a16ebaa63f468 L1421 * physical_line
  EN: Remember, no refunds! What else you need? He! He! He!
  ZH:     * 记住，概不退款！还要点啥？嘿！嘿！嘿！
CONTROL L1422    } else {
ROW CAT:O0002aa712c41167c0866 L1423 * physical_line
  EN: Wow, thanks! I didn't think I'd ever find a kobold to buy these!
  ZH:     * 哇，多谢！我还以为找不到肯买这些的科博德呢！
CONTROL L1424    }

## SCd56d415be4e61249 | sfw | datadm/all.ds | AreaC_Slaver1.Talk.pirate
CONTROL L1446  <AreaC_Slaver1.Talk.pirate>
CONTROL L1447    if { !koboCostume() } {
ROW SFW3d05fe4721e393148c76ebd8 L1448 - physical_line
  EN: You ever think about becoming a space pirate?
  ZH:     * 你有没有想过成为太空海盗？
ROW SFW7d0fadb807d2a944e3c36760 L1449 - physical_line
  EN: Lot more loot in it than being a cosmo agent, hen-heh...
  ZH:     * 比当宇宙特工能捞到的好处多多了，嘿嘿……
CONTROL L1450    }
CONTROL L1452  ### as kobo:

## SC3380c585541b394c | nsfw | datadf/all.ds | AreaC_Slaver1.Talk.psy
CONTROL L1458  <AreaC_Slaver1.Talk.psy>
CONTROL L1459    if { koboCostume() && hasItem(SpecialPsycards) } {
ROW CAT:O7d30fc1345309b3d1bcf L1460 * physical_line
  EN: I'll be honest: all this PSY stuff gives me the creeps.
  ZH:     * 老实说：这些精神力的东西让我发毛。
ROW CAT:O3b4757e27a43f4e0fe4d L1461 * physical_line
  EN: Jus' don't blow me up and we'll be golden, okay?
  ZH:     * 就别把我炸了，咱们就妥了，好吗？
CONTROL L1462    } else {
ROW CAT:O5d01f6f586123147433c L1463 * physical_line
  EN: Most kobolds don't really do all these mind games. I get it if y'ain't interested.
  ZH:     * 大多数科博德都不怎么搞这些精神把戏。你要是没兴趣，我理解。
ROW CAT:O0e7f67f7227459bfd079 L1464 * physical_line
  EN: Any ole club and a length of rope'll do me just fine... All direct-like, ya-know?
  ZH:     * 随便一根棍子、一截绳子就够我用了……直接动手，懂吧？
CONTROL L1465    }
CONTROL L1467  ### dog handling

## SC5a2ee864f08aee86 | sfw | datadm/all.ds | AreaE_Macsen1.Goodbye
CONTROL L1481  <AreaE_Macsen1.Goodbye>
CONTROL L1482    if { !inCosmoSuit() } {
ROW SFW882feb4f046a6fb624dc834d L1483 - physical_line
  EN: You're real daring, going out without a spacesuit on! 
  ZH:     * 不穿宇航服就往外跑，你胆子可真大！ 
ROW SFWddbcd81ba4e116b951590a7c L1484 - physical_line
  EN: You get 'em, tiger!
  ZH:     * 加油，猛将，去收拾他们吧！
CONTROL L1485    } else {
ROW SFWac9d0d6bdf1ec4fbda02de47 L1486 - physical_line
  EN: Bye! I'd toast to your health, but I know you can't drink with that helm on!
  ZH:     * 再见！本想举杯祝你健康，可我知道你戴着那头盔没法喝！
CONTROL L1487    }

## SCa256d2b7a4a5d415 | nsfw | datadm/all.ds | AreaH_Cellar.Goodbye
CONTROL L1559  <AreaH_Cellar.Goodbye>
ROW CAT:O087f2da7ac2be0bbd0c9 L1560 * physical_line
  EN: Buh bye! I know we'll meat again!
  ZH:   * 拜拜啦！我知道我们还会再见的！

## SC91ba8dd2328e026d | nsfw | datadf/all.ds | AreaH_Cellar.Hello
CONTROL L1542  <AreaH_Cellar.Hello>
CONTROL L1543    if { agentsRescued() == 0 } {
ROW CAT:Occb6b747b7aef84887dd L1544 * physical_line
  EN: Oh hi! Haven't seen one of you cosmo fellas in a while!
  ZH:     * 哦，你好！好久没见到你们这种宇宙来的家伙了！
CONTROL L1545    } else {
ROW CAT:O2a992118b50b4666398f L1546 * physical_line
  EN: Welcome welcome! Bring your appetite! And your Lect!
  ZH:     * 欢迎欢迎！带上你的胃口！还有你的 Lect！
CONTROL L1547    }

## SC93c89e09b39b160d | nsfw | datadf/all.ds | AreaH_Cellar.NotEnoughMoney
CONTROL L1610  <AreaH_Cellar.NotEnoughMoney>
ROW CAT:O2b4fafcfd99129301c96 L1611 * physical_line
  EN: Doesn't your boss pay ya? Come back with some more Lect!
  ZH:   * 你老板不给你发钱吗？多带点Lect再来！

## SC741e5ab2f9eee4ad | sfw | datadm/all.ds | AreaH_Cellar.VitDrumstick
CONTROL L1552  <AreaH_Cellar.VitDrumstick>
ROW SFW2a0ae50c7604c0007f223def L1553 - physical_line
  EN: Fried to perfection, this little snack will fill you with vigor! 
  ZH:   * 这份小吃炸得恰到好处，吃了让你活力满满！ 

## SC5c6de1250a079e59 | nsfw | datadm/all.ds | AreaH_Cellar.VitMeat
CONTROL L1565  <AreaH_Cellar.VitMeat>
ROW CAT:O6499fd67c045a417608a L1566 * physical_line
  EN: Ahh, in need of something a bit more substantial, are ya? Good choice!
  ZH:   * 啊，想来点更顶饱的，是吧？好眼光！
ROW CAT:O6f6e3512531b4967d826 L1567 * physical_line
  EN: This premium slab of meat will get you back on your feet in no time!
  ZH:   * 这块上等好肉能让你立马恢复精神！

## SCa954e3dd6e041fd2 | nsfw | datadm/all.ds | AreaH_MacsenBar.BarLectReward
CONTROL L1645  <AreaH_MacsenBar.BarLectReward>
ROW CAT:O21a5a21889210264ebf0 L1646 * physical_line
  EN: I'm all out of fancy stones and meds now...
  ZH:   * 我现在已经没有那些稀奇的石头和药品了……
ROW CAT:Oaf6cfff0e20c2a225120 L1647 * physical_line
  EN: ...but you know, you Cosmobreeders have been good to me
  ZH:   * ……不过，你们这些宇宙育种者一直待我不错，所以从我赚的钱里拿一小份吧，怎么样？这是你应得的！
ROW CAT:O336780cd33e4efeb7929 L1648 * physical_line
  EN: so why not take a little cut of what I've earned, huh? You deserve it!
  ZH: 

## SC65c922b16e875f98 | nsfw | datadf/all.ds | AreaH_MacsenBar.SoldOut
CONTROL L1690  <AreaH_MacsenBar.SoldOut>
ROW CAT:Ob2b965438932ffdfd958 L1691 * physical_line
  EN: I'm out now, sorry! If I had more I'd gladly give 'em to ya!
  ZH:   * 抱歉，现在没货了！要是还有，我很乐意给你！

## SC23766530c1074c47 | nsfw | datadf/all.ds | AreaH_MacsenBar.Talk.bar1
CONTROL L1647  <AreaH_MacsenBar.Talk.bar1>
ROW CAT:Oe781dd037f6678d21498 L1648 * physical_line
  EN: Sure are a lot of agents to rescue out there, huh?
  ZH:   * 外面要救的特工可真不少，是吧？
ROW CAT:Obddea0b51f2675deff48 L1649 * physical_line
  EN: Come back here after you've saved a bunch of 'em
  ZH:   * 等你多救些特工，再回来找我，我就给你点好东西……嘿嘿嘿！
ROW CAT:O361d9e8f1f60ef44353a L1650 * physical_line
  EN: and I'll give you a little somethin somethin... He!He!He!
  ZH: 

## SC4cc23376db878533 | nsfw | datadm/all.ds | AreaH_MacsenBar.Vitamin
CONTROL L1639  <AreaH_MacsenBar.Vitamin>
ROW CAT:Oad38b0f8acf9f9c41e71 L1640 * physical_line
  EN: You been working real hard to rescue everyone, haven't you?
  ZH:   * 为了救大家，你一直很拼命吧？
ROW CAT:O54fda9792bea3d56510f L1641 * physical_line
  EN: I've been busy running around from shop to shop making sure the lect flows
  ZH:   * 我忙着跑遍各家店，确保 lect 流转，不过偶尔我也得靠这个提提神！
ROW CAT:Oe26ede26da6a5dd8f312 L1642 * physical_line
  EN: but every once in a while I need one of THESE as a lil pick-me-up!
  ZH: 
ROW CAT:O6bbdc698e5667f311015 L1643 * physical_line
  EN: I reckon you could use one yourself about now, huh?
  ZH:   * 我寻思你这会儿也该来一份，嗯？

## SCe121946bba2b1c8e | nsfw | datadf/all.ds | AreaH_MacsenBreeding.Hello
CONTROL L1692  <AreaH_MacsenBreeding.Hello>
ROW CAT:Odfb0188d434a99f9320f L1693 * physical_line
  EN: COME ON IN, FELLOW BREEDER!
  ZH:   * 进来吧，搞育种的同行！

## SCc948bf3eea745d6b | nsfw | datadf/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1708  <AreaH_MacsenBreeding.SpecialFap>
ROW CAT:Ob2e7374a4e7d4ffa2477 L1709 * physical_line
  EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
  ZH:   * 既然你已经跟其中一只生物很亲近了，这个拿去！
ROW CAT:O8c8eb7a9f3a40f14e988 L1710 * physical_line
  EN: GET REAL CLOSE AND AFFECTIONATE TO THEM ONE MORE TIME WHILE HOLDING THIS
  ZH:   * 拿着这个，再跟它们好好亲近一回，说不定就能感到一股力量流遍全身……
ROW CAT:Ocd3254ce5b97ddbc7f05 L1711 * physical_line
  EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
  ZH: 

## SC3e48a3eb51cded0c | sfw | datadm/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1708  <AreaH_MacsenBreeding.SpecialFap>
ROW SFWbbe960d1cef5ebc2b49691c3 L1709 - physical_line
  EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
  ZH:   * 既然你已经和那些生物中的一个变得非常亲近了，把这个拿去！
ROW SFW14ff83c8515d7941dd255f06 L1710 - physical_line
  EN: GIVE THEM SOME ATTENTION AND PETS ONE MORE TIME WHILE HOLDING THIS CRYSTAL
  ZH:   * 拿着这块水晶，再关心它们一次、摸摸它们。
ROW SFW7431b039c7c08aa6ee629a6a L1711 - physical_line
  EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
  ZH:   * 并且你也许会感到某种力量流经你……

## SCd01d5a6a1d077677 | sfw | datadf/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1710  <AreaH_MacsenBreeding.SpecialFap>
ROW SFW7d0e0bd69cec7fca2500391b L1711 - physical_line
  EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
  ZH:   * 既然你已经跟其中一只生物很亲近了，这个给你！
ROW SFWbb67b2b36731c41900aa856f L1712 - physical_line
  EN: GIVE THEM SOME ATTENTION AND PETS ONE MORE TIME WHILE HOLDING THIS CRYSTAL
  ZH:   * 拿着这块水晶，再去陪陪它、摸摸它，
ROW SFWd4238c82798f14676f9097e0 L1713 - physical_line
  EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
  ZH:   * 说不定就能感到一股力量流遍全身……

## SCf38122ca50445f16 | sfw | datadm/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1713  <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1714    if { !f(ctx_maxed_any_pet_affinity) } {
ROW SFW6a5c02988a668da45adba78d L1715 - physical_line
  EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
  ZH:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW SFWc60fa50be70267660fe8ba26 L1716 - physical_line
  EN: AFTER YOU'VE MAXED A PET'S CONFIDENCE, RETURN HERE FOR A SPECIAL REWARD.
  ZH:     * 把宠物的自信提升到最高后，回来领取特别奖励。
CONTROL L1717    } else {
ROW SFW8e4878b96011e3e34906385a L1718 - physical_line
  EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
  ZH:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW SFWace2e46df84ee38b7104acec L1719 - physical_line
  EN: JUST PET THEM WHILE THEY'RE AT FULL CONFIDENCE TO CHARGE THE CRYSTAL.
  ZH:     * 在它们自信满满时抚摸它们，就能给水晶充能。
ROW SFW89cda79cd9696cb1ae3f5cf9 L1720 - physical_line
  EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
  ZH:     * 每种生物给的力量都不同！都试试！
CONTROL L1721    }
CONTROL L1723  ### shared ###

## SCd3b89da396a609bf | nsfw | datadf/all.ds | AreaH_MacsenMechanic.Goodbye
CONTROL L1764  <AreaH_MacsenMechanic.Goodbye>
ROW CAT:O130ea943e2f0ece62bdc L1765 * physical_line
  EN: Bye for now! You take care, you hear!
  ZH:   * 先这样啦！你多保重，听见没！

## SCa5c90608adc5d4fe | nsfw | datadm/all.ds | AreaH_MacsenMechanic.Hello
CONTROL L1770  <AreaH_MacsenMechanic.Hello>
ROW CAT:O7518ec7bb290a9dd8547 L1771 * physical_line
  EN: Welcome to my little shop!
  ZH:   * 欢迎光临我的小店！
ROW CAT:O1a15cec6b15922372c34 L1772 * physical_line
  EN: ...no, not that kind of shop! This is an auto shop!
  ZH:   * ……不，不是那种店！这是汽车修理店！

## SC86a162ee3099dd1b | nsfw | datadm/all.ds | AreaH_MacsenMechanic.Talk.PartHints
CONTROL L1777  <AreaH_MacsenMechanic.Talk.PartHints>
CONTROL L1778    if { f(ClassicStarkillV3_defeated) } {
CONTROL L1779      if { !hasItem(ShipGun) } {
CONTROL L1780        do { give(MapDataShipGunHint, 1) }
ROW CAT:Odf57469777953d3d511f L1781 * physical_line
  EN: I've asked around, and my sources say...
  ZH:       * 我打听了一圈，我的消息来源说……
ROW CAT:Oce75ea694f62d58630e2 L1782 * physical_line
  EN: The southern part of Depot B holds a nice Ship Gun!
  ZH:       * B号仓库的南部有一门不错的飞船炮！
ROW CAT:O79e55d7a3c913ac9af48 L1783 * physical_line
  EN: It's right underneath the area where the lights go out
  ZH:       * 它就在那片灯光熄灭区域的正下方，但你得有高级门卡才能进去！
ROW CAT:Oc2e7a0f42e4568356ea0 L1784 * physical_line
  EN: but you'll need a high level keycard to access it!
  ZH: 
CONTROL L1785      } else if { !hasItem(ShipShield) } {
CONTROL L1786        do { give(MapDataShipShieldHint, 1) }
ROW CAT:Oe4a764218ba60f5fbe72 L1787 * physical_line
  EN: I've asked around, and my sources say...
  ZH:       * 我打听了一圈，我的消息来源说……
ROW CAT:O9c19dfcd478ede827c81 L1788 * physical_line
  EN: Way down at the bottom of Ayskammr lies a nice Ship Shield!
  ZH:       * 在艾斯卡姆尔的最深处，躺着一面不错的飞船护盾！
ROW CAT:O9004a6a3357dc7bf3871 L1789 * physical_line
  EN: It's in a spooky dark cave, so try to take a light with ya!
  ZH:       * 它在一个阴森黑暗的洞穴里，所以记得带上照明！
CONTROL L1790      } else if { !hasItem(ShipRadar) } {
CONTROL L1791        do { give(MapDataShipRadarHint, 1) }
ROW CAT:O70fc090a518d5b91c0d2 L1792 * physical_line
  EN: I've asked around, and my sources say...
  ZH:       * 我打听了一圈，我的消息来源说……
ROW CAT:Oc1276eae1e8b43663106 L1793 * physical_line
  EN: The Elves of Sceafya have stowed away a Ship Radar!
  ZH:       * 斯凯菲亚的精灵们藏起了一台飞船雷达！
ROW CAT:Ocac2772b37729c70e503 L1794 * physical_line
  EN: Apparently it's in a tricky position...
  ZH:       * 据说它在一个很刁钻的位置……
ROW CAT:O44fe1f3207210c575287 L1795 * physical_line
  EN: You're gonna have to be a magician or psychic to reach it!
  ZH:       * 你得是魔术师或者通灵者才够得着它！
CONTROL L1796      } else if { !hasItem(ShipTurbo) } {
CONTROL L1797        do { give(MapDataShipTurboHint, 1) }
ROW CAT:Oc1c42dc34171f556bd31 L1798 * physical_line
  EN: I've asked around, and my sources say...
  ZH:       * 我打听了一圈，我的消息来源说……
ROW CAT:O61856b24fe1c48c7c2d0 L1799 * physical_line
  EN: Zeronia's really taken a beating since you got here!
  ZH:       * 自从你来了之后，泽罗尼亚可真是饱受摧残！
ROW CAT:O0206d410c9748cbe8cf6 L1800 * physical_line
  EN: Supposedly an old cache that held a Ship Turbo got revealed
  ZH:       * 据说最近那几场地震让一个装有飞船涡轮的旧藏匿点露了出来！快去拿吧！
ROW CAT:Of6767d1bc9085b3f2354 L1801 * physical_line
  EN: during the last batch of earthquakes! Go get it!
  ZH: 
CONTROL L1802      } else {
ROW CAT:Oa1031f6c2c91fab96f96 L1803 * physical_line
  EN: Wow! You got a whole set of parts for this ol' ship of yours!
  ZH:       * 哇！你这艘老船的整套零件都齐了！
ROW CAT:O350b97074a08d98227b2 L1804 * physical_line
  EN: I'll need time to install them, but it'll all work out now!
  ZH:       * 我需要时间把它们装上，不过现在一切都能搞定了！
CONTROL L1805      }
CONTROL L1806    } else {
ROW CAT:O3ccbdffe8bbc02a4f058 L1807 * physical_line
  EN: If you come across any nice upgrades for your ship out there
  ZH:     * 如果你在外面碰上什么不错的飞船升级件，我就免费替你装上！
ROW CAT:O7bbc3b62846bb8b56848 L1808 * physical_line
  EN: I'll install them for you, free of charge!
  ZH: 
ROW CAT:O941926cce065ce99bc94 L1809 * physical_line
  EN: ...well, not really free. Your boss paid me already!
  ZH:     * ……嗯，也不算真免费。你的老板已经付过我钱了！
CONTROL L1810    }

## SC2a9e7e815d78c579 | nsfw | datadf/all.ds | AreaH_Ship.Hello
CONTROL L1845  <AreaH_Ship.Hello>
ROW CAT:O6747033ba8168f3d2ff3 L1846 * physical_line
  EN: Heyo sis! Welcome aboard!
  ZH:   * 嘿，姐！欢迎登船！

## SC48cc4c9accffe5d3 | nsfw | datadm/all.ds | AreaH_Ship.Talk.Queen
CONTROL L1862  <AreaH_Ship.Talk.Queen>
ROW CAT:Of0301f5bc9ff21bb73d5 L1863 * physical_line
  EN: I can't believe that I did that evil Queen's bidding...
  ZH:   * 真不敢相信，我竟然替那个邪恶女王卖命……
ROW CAT:O046386da5743ecd4d292 L1864 * physical_line
  EN: She almost has enough power to take over a new body
  ZH:   * 她几乎已经有足够的力量占据一具新的身体了，所以咱们得赶快出击，趁还来得及！
ROW CAT:Oe91557847e87d65d423b L1865 * physical_line
  EN: so we gotta hurry and strike before it's too late!
  ZH: 

## SC00d6fd73be5dab06 | nsfw | datadm/all.ds | AreaX_Upgrade.Goodbye
CONTROL L1886  <AreaX_Upgrade.Goodbye>
ROW CAT:Oa0fac26c2bd955430502 L1887 * physical_line
  EN: Bye bye, agent!
  ZH:   * 拜拜啦，特工！

## SCc26f043a33d848e6 | nsfw | datadm/all.ds | AreaX_Upgrade.GoodbyeKobo
CONTROL L1900  <AreaX_Upgrade.GoodbyeKobo>
ROW CAT:O8cd42018c8c46cafdd01 L1901 * physical_line
  EN: -wait a sec, you're not the delivery guy! G-get out of here right now!
  ZH:   * -等等，你可不是送货那家伙！快、快给我出去！

## SCef60c13b152f4038 | nsfw | datadm/all.ds | AreaX_Upgrade.Hello
CONTROL L1883  <AreaX_Upgrade.Hello>
ROW CAT:O6a05b4b2e8c5a04c2ea7 L1884 * physical_line
  EN: Heya Yiffai! How can I help you?
  ZH:   * 嘿，伊吠！有什么我能帮你的吗？

## SC8ede406152761b6c | nsfw | datadm/all.ds | AreaX_Upgrade.HelloDog
CONTROL L1889  <AreaX_Upgrade.HelloDog>
ROW CAT:O1654ddf2ae3fdd45b1ff L1890 * physical_line
  EN: Hello there Mr. Puppy! Do you want to be my rubber ducky?
  ZH:   * 你好呀，小狗先生！你想当我的橡皮鸭吗？
ROW CAT:O3116bb44e70e1578ea69 L1891 * physical_line
  EN: All you have do is stay here and listen to me talk about computers all day!
  ZH:   * 你只要待在这里，听我一整天聊电脑就行！

## SC3a799c85eb00c2fb | nsfw | datadf/all.ds | AreaX_Upgrade.HelloKobo
CONTROL L1885  <AreaX_Upgrade.HelloKobo>
ROW CAT:O7423f4aca5eb0923ff6f L1886 * physical_line
  EN: Are you delivering my weekly supplies? I still have some leftover.
  ZH:   * 你是来送每周补给的？我还剩着一些呢。
ROW CAT:O8846c9a9d2010bd22ae4 L1887 * physical_line
  EN: Since last cycle, I've been increasing my efficiency coefficient while usin-
  ZH:   * 从上个周期起，我一直在提高自己的效率系数，同时用——

## SC1688edd7961e362d | nsfw | datadm/all.ds | AreaX_Upgrade.Meeting
CONTROL L1878  <AreaX_Upgrade.Meeting>
ROW CAT:O21bd5c0d2d2a2ca67053 L1879 * physical_line
  EN: Heya Yiffai! Nice to see you up here in my brand new spacelab!
  ZH:   * 嘿，伊吠！很高兴你能上来，看看我全新的太空实验室！
ROW CAT:Ofcc19fdc75fbc098c9f5 L1880 * physical_line
  EN: Heheh... I guess this used to be your sister's ship though, huh?
  ZH:   * 嘿嘿……不过我想，这以前是你姐姐的飞船吧？
ROW CAT:Oc0058d264996e559a686 L1881 * physical_line
  EN: Pirates already looted most of it, but I found a working equipment repair bay!
  ZH:   * 海盗已经把大部分东西都抢走了，但我找到了一台还能用的装备修理舱！

## SC9de6554e5b292985 | nsfw | datadf/all.ds | AreaX_Upgrade.Meeting
CONTROL L1867  <AreaX_Upgrade.Meeting>
ROW CAT:O6d0ec1c40632ca79b182 L1868 * physical_line
  EN: Heya Yiffany! Nice to see you up here in my brand new spacelab!
  ZH:   * 嘿，伊吠妮！很高兴在我全新的太空实验室里见到你！
ROW CAT:O27f22287ff0cc2fff195 L1869 * physical_line
  EN: Heheh... I guess this used to be your brother's ship though, huh?
  ZH:   * 嘿嘿……不过我猜这艘船以前是你弟弟的吧，嗯？
ROW CAT:O42a3fa3d40f4ac0eefa0 L1870 * physical_line
  EN: Pirates already looted most of it, but I found a working equipment repair bay!
  ZH:   * 海盗已经把大部分东西都抢走了，但我找到了一台还能用的装备修理舱！

## SC35f4aca530d555a1 | nsfw | datadf/all.ds | AreaX_Upgrade.Talk.macsen
CONTROL L1940  <AreaX_Upgrade.Talk.macsen>
CONTROL L1941    if { !f(upgraded_TazerAttuned) } {
ROW CAT:O2aedb1f5b5259b379971 L1942 * physical_line
  EN: Have you found all the Chips laying around yet?
  ZH:     * 你已经把散落在各处的芯片都找到了吗？
ROW CAT:Oedc88916d06a08fffde4 L1943 * physical_line
  EN: We'll need all of them in order to get this repair bay working again!
  ZH:     * 要让这台修理舱重新运转，我们需要全部芯片！
ROW CAT:Ob627c4f57bb0c368c6f2 L1944 * physical_line
  EN: If you need help finding more Chips, there's a weird old dog in the area
  ZH:     * 如果你需要帮忙找更多芯片，这一带有一只奇怪的老狗，卖着一件挺不错的装备，能帮你找到它们！
ROW CAT:Ofd99b66cb17bcda9a1ac L1945 * physical_line
  EN: that sells a neat piece of gear that will help you find them!
  ZH: 
CONTROL L1946    }

## SC86418c768818a976 | nsfw | datadm/all.ds | AreaX_Upgrade.Talk.power
CONTROL L1940  <AreaX_Upgrade.Talk.power>
ROW CAT:Ofc018d48062d82f4f4f5 L1941 * physical_line
  EN: Did you know this whole asteroid is actually wired with an advanced power grid?
  ZH:   * 你知道吗，这整颗小行星其实都铺设了先进的电网？
ROW CAT:O4a2afcd3a32485ce1bd7 L1942 * physical_line
  EN: It's pretty awesome... and guess what? Something buried in this rock seems to be
  ZH:   * 相当厉害吧……你猜怎么着？这块岩石里埋着的什么东西似乎也在猛耗电力……不过，我还未能确定它的位置。
ROW CAT:O732757163c3595d8fb0a L1943 * physical_line
  EN: drawing a load of power too... I haven't been able to localize it yet, though.
  ZH: 

## SC96baa13ee76df1af | nsfw | datadf/all.ds | AreaX_Upgrade.Talk.repair
CONTROL L1934  <AreaX_Upgrade.Talk.repair>
CONTROL L1935    if { !f(upgraded_TazerAttuned) } {
ROW CAT:O937a1a082b33efffad54 L1936 * physical_line
  EN: If you collect enough chips, I could hack into the power grid and get this
  ZH:     * 只要你收集到足够的芯片，我就能侵入电网，让这个维修区重新上线。
ROW CAT:O176949ac76835993be16 L1937 * physical_line
  EN: repair bay back online.
  ZH: 
CONTROL L1938    }

## SCe22562e35aecb90d | nsfw | datadm/all.ds | AreaX_Upgrade.TechBabble.trashed
CONTROL L1959  <AreaX_Upgrade.TechBabble.trashed>
ROW CAT:O1c832e71df18f85685d3 L1960 * physical_line
  EN: Wow, this thing is really *trashed*, but I can tell it used to be top of the line.
  ZH:   * 哇，这东西真是*烂透了*，不过我看得出它从前是顶级货。
ROW CAT:Oa72102c94dd020c6e5be L1961 * physical_line
  EN: Throw me those chips and let's see what this repair bay can do!
  ZH:   * 把那些芯片丢给我，看看这个维修区能有什么本事！

## SC5de682869c350367 | nsfw | datadm/all.ds | Fenfen_Shared.Hello
CONTROL L4964  <Fenfen_Shared.Hello>
ROW CAT:Oc375b388514931c5810e L4965 Anon/Fox physical_line
  EN: Help, I'm trapped in here!
  ZH:   Anon/Fox: 救命，我被困在这儿了！

## SCfda927e5a4898c16 | nsfw | datadm/all.ds | Gitgud.Tip1
CONTROL L3366  <Gitgud.Tip1>
ROW CAT:O8967dcd32c6a279f5ddb L3367 Gitgud physical_line
  EN: [YOU MAY NOT BE ABLE TO WALK WHILE ATTACKING]
  ZH:     Gitgud: [攻击时你可能无法走动，但挥击恢复期间你可以跳跃，并重新获得一些机动性！]
ROW CAT:O859f86aa303c548b6d1d L3368 Gitgud physical_line
  EN: [BUT YOU CAN JUMP WHILE RECOVERING FROM THE SWING]
  ZH: 
ROW CAT:O960b731d5e14ebd2637b L3369 Gitgud physical_line
  EN: [AND REGAIN SOME MOBILITY!]
  ZH: 

## SCd1e8a86959dbb143 | nsfw | datadf/all.ds | Gitgud.Tip4
CONTROL L3312  <Gitgud.Tip4>
ROW CAT:O60223f41ba5aac30bc06 L3313 Gitgud physical_line
  EN: [THE TORCHES THAT LINE THE WALLS CAN BE BROKEN]
  ZH:     Gitgud: [沿着墙壁排列的火把可以被打破，里面可能还有一点零钱！]
ROW CAT:O222a74946f9731997f84 L3314 Gitgud physical_line
  EN: [AND MAY HAVE A LITTLE POCKET CHANGE IN THEM!]
  ZH: 

## SC2c035a06b63b51a3 | nsfw | datadm/all.ds | Gitgud.Tip6
CONTROL L3387  <Gitgud.Tip6>
ROW CAT:O9353b7f70cf5c0ae23cc L3388 Gitgud physical_line
  EN: [PLENTY OF FOODS OUT THERE WILL HEAL YOU A BIT]
  ZH:     Gitgud: [外头不少食物都能帮你回点血，有些甚至能提升属性！]
ROW CAT:Oe34e4dc85c04e7f74f68 L3389 Gitgud physical_line
  EN: [AND SOME WILL EVEN RAISE YOUR STATS!]
  ZH: 
ROW CAT:Oc22baa07ce223597822d L3390 Gitgud physical_line
  EN: [STOCK UP IF SOME BEAST IS GIVING YOU A HARD TIME.]
  ZH:     Gitgud: [要是有哪只野兽让你吃不消，就多备点吃的。]

## SC15a9fb139a76e0c7 | nsfw | datadm/all.ds | Gitgud.Tip7
CONTROL L3392  <Gitgud.Tip7>
ROW CAT:Of51c8eb87b4496fe7308 L3393 Gitgud physical_line
  EN: [WHAT, ARE YOU HAVING A HARD TIME WITH THE MISSION?]
  ZH:     Gitgud: [怎么，任务让你吃不消了吗？]
ROW CAT:O873656b797926cfe6410 L3394 Gitgud physical_line
  EN: [WHY DON'T YOU JUST ENABLE SOME CHEAT CODES, WEAKLING?]
  ZH:     Gitgud: [你为什么不直接开启一些秘籍代码呢，弱者？]
ROW CAT:Od5ce150c21e913989dee L3395 Gitgud physical_line
  EN: [THE UNLISTED CHEAT CODES ARE THE STRONGEST]
  ZH:     Gitgud: [未列出来的秘籍代码是最强的，但它们被藏在了世界某处……]
ROW CAT:Ocdd115fdb11784325102 L3396 Gitgud physical_line
  EN: [BUT THEY'VE BEEN HIDDEN SOMEWHERE IN THE WORLD...]
  ZH: 

## SCce1d52e5b7fdecd2 | nsfw | datadm/all.ds | Hacker_Shared.Goodbye
CONTROL L4978  <Hacker_Shared.Goodbye>
ROW CAT:O6d6b2f88d9775f7119b4 L4979 * physical_line
  EN: Bye bye, agent! Bring me more of those chips!
  ZH:   * 拜拜，特工！再给我多带些那种芯片来！

## SC3c1ce79c8d1fad83 | nsfw | datadf/all.ds | Hacker_Shared.Meeting
CONTROL L4956  <Hacker_Shared.Meeting>
ROW CAT:Ocbc67d8d8526f8a2febe L4957 * physical_line
  EN: Greetings, Yiffany. You don't know me, but I kinda snooped your satlink.
  ZH:   * 你好，伊吠妮。你不认识我，但我稍微窥探了你的卫星链路。
ROW CAT:O9c274c01083d39b141e4 L4958 * physical_line
  EN: So I've actually been watching you for a while, and I have a proposition...
  ZH:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:Ob73ff9e30e2928c902f9 L4959 * physical_line
  EN: It's simple: You bring me those fancy chips you find out there,
  ZH:   * 很简单：你把在外头找到的那些花哨芯片带给我，我就替你黑开门！显然，这是双赢！
ROW CAT:Od9b414ed7aac1bf86bed L4960 * physical_line
  EN: and I'll hack open doors for you! It's a win-win, obviously!
  ZH: 

## SC460962f6053b7384 | nsfw | datadf/all.ds | Hacker_Shared.SoldOut
CONTROL L4990  <Hacker_Shared.SoldOut>
ROW CAT:Odf7cafa57b3798aeec21 L4991 * physical_line
  EN: Hey wait! I already hacked this one!
  ZH:   * 嘿，等等！这个我已经黑过了！
ROW CAT:O61ca4a88ee0610d447cc L4992 * physical_line
  EN: Is it spontaneously closing on you? I hate when that happens!
  ZH:   * 它会自己关掉吗？我最讨厌这种事了！

## SCb8ec8563ec77b970 | nsfw | datadm/all.ds | Hacker_Shared.SoldOut
CONTROL L5003  <Hacker_Shared.SoldOut>
ROW CAT:O1088f470f3fd71a7bd7d L5004 * physical_line
  EN: Hey wait! I already hacked this one!
  ZH:   * 嘿，等等！这个我已经黑过了！
ROW CAT:O2a93bfdf0065433c0d64 L5005 * physical_line
  EN: Is it spontaneously closing on you? I hate when that happens!
  ZH:   * 它会自己关掉吗？我最讨厌这种事了！

## SC08e8e1c27b8a7f5f | nsfw | datadf/all.ds | Hacker_Shared.Talk.hacking
CONTROL L4999  <Hacker_Shared.Talk.hacking>
ROW CAT:O2de32367a5e5d458f67e L5000 * physical_line
  EN: These cyber doors around here are really fun to hack!
  ZH:   * 这附近的赛博门黑起来可真有意思！
ROW CAT:Oc015c1b56ca3fb68c888 L5001 * physical_line
  EN: If you can furnish the requisite components, I'll open them right up!
  ZH:   * 只要你能提供所需的部件，我就立刻把它们打开！

## SCa624d09e7708052b | nsfw | datadf/all.ds | Macsen_Shared.BoneTheDog
CONTROL L5011  <Macsen_Shared.BoneTheDog>
ROW CAT:O678c9c856b7b0002d650 L5012 * physical_line
  EN: Do you want my bone, girl? Do ya?
  ZH:   * 想要我的骨头吗，姑娘？想不想？

## SCf6818d7f67d5f61f | sfw | datadf/all.ds | Macsen_Shared.BoneTheDog
CONTROL L4829  <Macsen_Shared.BoneTheDog>
ROW SFW08799110b05f0301dcfd5377 L4830 - physical_line
  EN: Do you want a treat, girl? Do ya?
  ZH:   * 想吃点零食吗，小姑娘？想不想呀？

## SCe9ade09a8cedbef1 | nsfw | datadf/all.ds | Macsen_Shared.HelloDog
CONTROL L5008  <Macsen_Shared.HelloDog>
ROW CAT:Od864ffaa57e05eff504f L5009 * physical_line
  EN: Hel-oh! You're just a dog!
  ZH:   * 你——好！原来只是条狗啊！

## SCfd2fc702e0b36f43 | nsfw | datadm/all.ds | Macsen_Shared.HelloDog
CONTROL L5021  <Macsen_Shared.HelloDog>
ROW CAT:O4c256b16924e06606391 L5022 * physical_line
  EN: Hel-oh! You're just a dog!
  ZH:   * 你、你好啊！原来你只是条狗啊！

## SCbfe0b283ab3cbcb1 | nsfw | datadf/all.ds | Macsen_Shared.HelloKobo
CONTROL L5022  <Macsen_Shared.HelloKobo>
ROW CAT:O287b521d8afe2367ab26 L5023 * physical_line
  EN: Hmph! What do you want?
  ZH:   * 哼！你想干什么？
ROW CAT:Ob86e2506ec3dea2150be L5024 * physical_line
  EN: Lot of nerve showing your face around here, slaver scoundrel!
  ZH:   * 亏你还敢在这儿露面，奴隶贩子混蛋！

## SCe9634624dc4d7eda | nsfw | datadf/all.ds | Macsen_Shared.NoInventorySpace
CONTROL L5045  <Macsen_Shared.NoInventorySpace>
ROW CAT:O25d3cfcfae712e65c941 L5046 * physical_line
  EN: Sorry, you are over-encumbered!
  ZH:   * 抱歉，你已经超重了！
ROW CAT:O393900e36b4bb3b848f6 L5047 * physical_line
  EN: Do you want anything else?
  ZH:   * 你还想要点别的吗？

## SC8d711938d69b00f9 | nsfw | datadf/all.ds | Macsen_Shared.NotEnoughMoney
CONTROL L5041  <Macsen_Shared.NotEnoughMoney>
ROW CAT:O135598afc09bbf04b2af L5042 * physical_line
  EN: No Lect, no sale. And no discounts!
  ZH:   * 没有 Lect，就没有交易。而且绝不打折！
ROW CAT:O5e352f5a452dad155a1f L5043 * physical_line
  EN: Do you want anything else?
  ZH:   * 你还想要点别的吗？

## SCc1aa50eef366f517 | nsfw | datadm/all.ds | Macsen_Shared.NotEnoughMoney
CONTROL L5054  <Macsen_Shared.NotEnoughMoney>
ROW CAT:O27d3e0de639a39bcd834 L5055 * physical_line
  EN: No Lect, no sale. And no discounts!
  ZH:   * 没 Lect 就不卖。而且不打折！
ROW CAT:Occ8455f79c01cac2a0dc L5056 * physical_line
  EN: Do you want anything else?
  ZH:   * 还想要点别的吗？

## SCef7a0ad8d2405ff4 | nsfw | datadm/all.ds | Macsen_Shared.SoldOut
CONTROL L5062  <Macsen_Shared.SoldOut>
ROW CAT:Ofc0b2101b3b6525fde7b L5063 * physical_line
  EN: Sorry! That was the only one I had. I'm cleared out!
  ZH:   * 抱歉！我就那么一件，已经卖光啦！
ROW CAT:O6676e6555a81885758ed L5064 * physical_line
  EN: Do you want anything else?
  ZH:   * 还想要点别的吗？

## SC588ed8faaa6ba20e | nsfw | datadf/all.ds | Prison_Shared.NoKobo
CONTROL L5052  <Prison_Shared.NoKobo>
ROW CAT:Oa5e257d1550a92392ef7 L5053 * physical_line
  EN: Darn it! I'm in a tough enough spot as it is!
  ZH:   * 真是的！我的处境已经够艰难了！
ROW CAT:Oc2a2aab1e650ba5e90c1 L5054 * physical_line
  EN: The last thing I need to deal with is a darn kobold all of a sudden!
  ZH:   * 我最不想应付的，就是突然冒出一只该死的科博德！
ROW CAT:Oe5cc9856da5c62c350f9 L5055 * physical_line
  EN: Shoo! Go on! Get out!
  ZH:   * 走开！快走！出去！

## SC14dd7e984ce79d79 | nsfw | datadm/all.ds | Proto_Fenfen.Goodbye
CONTROL L5072  <Proto_Fenfen.Goodbye>
ROW CAT:O443338237f24874e0d6f L5073 Anon/Fox physical_line
  EN: Thank you Yiffai!
  ZH:   Anon/Fox: 谢谢你，伊吠！

## SCf50c90a506b01b46 | nsfw | datadm/all.ds | Proto_Fenfen.HelloDog
CONTROL L5078  <Proto_Fenfen.HelloDog>
ROW CAT:Of6688102e10c46375f5a L5079 Anon/Fox physical_line
  EN: Oh, it's a dog!
  ZH:   Anon/Fox: 哦，是只狗！

## SC7281457e7d7616b6 | nsfw | datadm/all.ds | Proto_Fenfen.NoBoneForDog
CONTROL L5081  <Proto_Fenfen.NoBoneForDog>
ROW CAT:O74b4fb85b28121e0a9f7 L5082 Anon/Fox physical_line
  EN: Can you get your master to come and help me?
  ZH:   Anon/Fox: 你能让你的主人过来帮我吗？

## SC1fe057a073bfd3a9 | nsfw | datadf/all.ds | Proto_Fenfen.Rescue
CONTROL L5077  <Proto_Fenfen.Rescue>
ROW CAT:O6dedebfa000abd7d2247 L5078 Anon/Fox physical_line
  EN: These shackles are damaged. You should be able to break them with a few good whacks!
  ZH:   Anon/Fox: 这些镣铐坏了。你好好砸几下应该就能砸开！

## SC99762438737ce782 | nsfw | datadm/all.ds | Proto_Fenfen.Rescue
CONTROL L5090  <Proto_Fenfen.Rescue>
ROW CAT:Ode95ad7be5b53bfd6c31 L5091 Anon/Fox physical_line
  EN: These shackles are damaged. You should be able to break them with a few good whacks!
  ZH:   Anon/Fox: 这些镣铐坏了。你好好砸几下应该就能砸开！

## SC570d714b17799c3e | nsfw | datadf/all.ds | Proto_Fenfen.SoldOut
CONTROL L5083  <Proto_Fenfen.SoldOut>
ROW CAT:O390b4c351253f229b5c6 L5084 Anon/Fox physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   Anon/Fox: 谢谢，不过我已经被救出来了！

## SC3f3456d75cf51aa3 | nsfw | datadm/all.ds | Proto_Fenfen.TalkBeforeRescue.bopped
CONTROL L5099  <Proto_Fenfen.TalkBeforeRescue.bopped>
ROW CAT:O2fa8f750d04619a5b2c2 L5100 Anon/Fox physical_line
  EN: I'm so glad to see another cosmobreeder, even if I'm just a placeholder!
  ZH:   Anon/Fox: 能见到另一位宇宙育种者，我太高兴了，哪怕我只是个占位角色！

## SC0b2e5351994d5ca8 | nsfw | datadm/all.ds | Proto_PrisonKey.CancelPurchase
CONTROL L5125  <Proto_PrisonKey.CancelPurchase>
CONTROL L5126    if { hasItem(Key) } {
ROW CAT:O78f71afe9159cf00c821 L5127 * physical_line
  EN: Hey! Quit fooling around and help me out!
  ZH:     * 嘿！别胡闹了，快帮帮我！
CONTROL L5128    } else {
ROW CAT:O3f02c434dc0b2a84e818 L5129 * physical_line
  EN: Please hurry up and find that key, Yiffai!
  ZH:     * 请快点找到那把钥匙，伊吠！
CONTROL L5130    }

## SC4ec40754b8e4a8b1 | nsfw | datadf/all.ds | Proto_PrisonKey.CancelPurchase
CONTROL L5112  <Proto_PrisonKey.CancelPurchase>
CONTROL L5113    if { hasItem(Key) } {
ROW CAT:Oe2d8d4c6de29b48001d0 L5114 * physical_line
  EN: Hey! Quit fooling around and help me out!
  ZH:     * 嘿！别胡闹了，快帮帮我！
CONTROL L5115    } else {
ROW CAT:O1c71716a2d60260fba54 L5116 * physical_line
  EN: Please hurry up and find that key, Yiffany!
  ZH:     * 请快点找到那把钥匙，伊吠妮！
CONTROL L5117    }

## SC9cd79fb5aae487cd | nsfw | datadm/all.ds | Proto_PrisonKey.Goodbye
CONTROL L5107  <Proto_PrisonKey.Goodbye>
ROW CAT:O193a6b896c907d6da586 L5108 * physical_line
  EN: Thank you Yiffai!
  ZH:   * 谢谢你，伊吠！

## SC57cb783d122366f4 | nsfw | datadm/all.ds | Proto_PrisonKey.GoodbyeNotRescued
CONTROL L5110  <Proto_PrisonKey.GoodbyeNotRescued>
ROW CAT:Ob065d029d7da5d3c2294 L5111 * physical_line
  EN: Please come back soon!
  ZH:   * 请早点回来！

## SC6dbf7099ba6b2638 | nsfw | datadf/all.ds | Proto_PrisonKey.Hello
CONTROL L5091  <Proto_PrisonKey.Hello>
ROW CAT:Oc7b7ee3a380118360f0d L5092 * physical_line
  EN: Help, I'm locked up in here!
  ZH:   * 救命，我被锁在这里面了！

## SC721d4bc0c153d6a1 | nsfw | datadm/all.ds | Proto_PrisonKey.Hello
CONTROL L5104  <Proto_PrisonKey.Hello>
ROW CAT:O2132ad221425a14d3739 L5105 * physical_line
  EN: Help, I'm locked up in here!
  ZH:   * 救命，我被锁在这里面了！

## SC5c44dd4d7c5fe273 | nsfw | datadm/all.ds | Proto_PrisonKey.NotEnoughMoney
CONTROL L5138  <Proto_PrisonKey.NotEnoughMoney>
ROW CAT:Oa1bb6fe3915338476b62 L5139 * physical_line
  EN: There's no way to get this lock open without a key. Please try and find one.
  ZH:   * 没有钥匙就没办法打开这把锁。请设法找一把来。

## SCa4c8bb46da47674e | nsfw | datadf/all.ds | Proto_PrisonKey.NotEnoughMoney
CONTROL L5125  <Proto_PrisonKey.NotEnoughMoney>
ROW CAT:O0a31368275c5c185c170 L5126 * physical_line
  EN: There's no way to get this lock open without a key. Please try and find one.
  ZH:   * 没有钥匙就没办法打开这把锁。请设法找一把来。

## SC238211f417c60f2b | nsfw | datadm/all.ds | Proto_PrisonKey.Purchased
CONTROL L5135  <Proto_PrisonKey.Purchased>
ROW CAT:Oad118960bce52f9e4b06 L5136 * physical_line
  EN: Thank you!
  ZH:   * 谢谢！

## SCb7faebda1c1a887c | nsfw | datadf/all.ds | Proto_PrisonKey.Purchased
CONTROL L5122  <Proto_PrisonKey.Purchased>
ROW CAT:O0a40299095ad2442eff1 L5123 * physical_line
  EN: Thank you!
  ZH:   * 谢谢！

## SCb9f465a7e6a20eb3 | nsfw | datadm/all.ds | Proto_PrisonKey.TalkAfterRescue.thanks
CONTROL L5148  <Proto_PrisonKey.TalkAfterRescue.thanks>
ROW CAT:O43d9ae4226e00a83a1e3 L5149 * physical_line
  EN: I'm sorry I don't have any data for you. I'm just a placeholder...
  ZH:   * 抱歉，我没有什么数据可以给你。我只是个占位角色……

## SC3ff2fa56287b0594 | nsfw | datadf/all.ds | Proto_PrisonTazer.CancelPurchase
CONTROL L5158  <Proto_PrisonTazer.CancelPurchase>
ROW CAT:Oa28d360db586aa28d9b4 L5159 * physical_line
  EN: Hey, help a placeholder out here!
  ZH:   * 嘿，帮帮这个占位角色啊！

## SCd39b31fcf8ed8535 | nsfw | datadm/all.ds | Proto_PrisonTazer.CancelPurchase
CONTROL L5171  <Proto_PrisonTazer.CancelPurchase>
ROW CAT:O018c1a0c1771ad83d39e L5172 * physical_line
  EN: Hey, help a placeholder out here!
  ZH:   * 嘿，帮这个占位角色一把吧！

## SC6e09c09d831bd2bf | nsfw | datadm/all.ds | Proto_PrisonTazer.Goodbye
CONTROL L5153  <Proto_PrisonTazer.Goodbye>
ROW CAT:Of5024d9450327baca4fe L5154 * physical_line
  EN: Thank you Yiffai!
  ZH:   * 谢谢你，伊吠！

## SCe786d702a947589d | nsfw | datadf/all.ds | Proto_PrisonTazer.Goodbye
CONTROL L5140  <Proto_PrisonTazer.Goodbye>
ROW CAT:O397a3c10639870f7bdbe L5141 * physical_line
  EN: Thank you Yiffany!
  ZH:   * 谢谢你，伊吠妮！

## SC7c592434c3b9e011 | nsfw | datadm/all.ds | Proto_PrisonTazer.GoodbyeDog
CONTROL L5165  <Proto_PrisonTazer.GoodbyeDog> 
ROW CAT:O457b3906f82f5ff377fe L5166 * physical_line
  EN: Please come back soon with your master!
  ZH:   * 请早点带着你的主人回来！

## SC9ad99c76b00a6470 | nsfw | datadm/all.ds | Proto_PrisonTazer.Hello
CONTROL L5150  <Proto_PrisonTazer.Hello>
ROW CAT:O3dd3defe276a60278405 L5151 * physical_line
  EN: Help, I'm trapped in here!
  ZH:   * 救命，我被困在这儿了！

## SC3624cea09de3f171 | nsfw | datadf/all.ds | Proto_PrisonTazer.HelloDog
CONTROL L5146  <Proto_PrisonTazer.HelloDog>
ROW CAT:Oe3c0bcd6d95cdc7067c3 L5147 * physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SCdfbe1d631aa247c1 | nsfw | datadm/all.ds | Proto_PrisonTazer.HelloDog
CONTROL L5159  <Proto_PrisonTazer.HelloDog>
ROW CAT:Oc9d4f29ad7ea6ce27c2a L5160 * physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SC63135bccb58388bf | nsfw | datadm/all.ds | Proto_PrisonTazer.NoBoneForDog
CONTROL L5162  <Proto_PrisonTazer.NoBoneForDog>
ROW CAT:Oaedafa0c3d26306b7def L5163 * physical_line
  EN: Can you get your master to come and help me?
  ZH:   * 你能让你的主人过来帮我吗？

## SCa650848d84eccb6a | nsfw | datadf/all.ds | Proto_PrisonTazer.Rescue
CONTROL L5161  <Proto_PrisonTazer.Rescue>
ROW CAT:Occ90348a3beca58da982 L5162 * physical_line
  EN: These shackles are damaged. You should be able to break them with a few good whacks!
  ZH:   * 这些镣铐坏了。你好好砸几下应该就能砸开！

## SCd5a4cb02c0bd6604 | nsfw | datadm/all.ds | Proto_PrisonTazer.TalkBeforeRescue.bopped
CONTROL L5183  <Proto_PrisonTazer.TalkBeforeRescue.bopped>
ROW CAT:Oe6d37582883c9b33ae35 L5184 * physical_line
  EN: I'm so glad to see another cosmobreeder, even if I'm just a placeholder!
  ZH:   * 能见到另一位宇宙育种者，我太高兴了，哪怕我只是个占位角色！

## SCdf8c740516154c40 | nsfw | datadf/all.ds | Queen.AreaX_falling noselect noamendfreq
CONTROL L2643  <Queen.AreaX_falling noselect noamendfreq>
ROW CAT:O576b2a28eefbd64a42dc L2644 Queen physical_line
  EN: [NO MORE INTERFERENCE FROM YOU, SPACE BUG!]
  ZH:   Queen: [你休想再来碍事，太空虫子！]
ROW CAT:Off8327a2e4051f10ccd8 L2645 Queen physical_line
  EN: [ENJOY THE CAPTIVATING VIEW OF PLANET TUTONE...]
  ZH:   Queen: [好好欣赏图托恩星这迷人的景色吧……]
ROW CAT:O3776d9b99936ce6bfeb2 L2646 Queen physical_line
  EN: [...AS IT RUSHES TO MEET YOU! HAH! HAH! HAH!]
  ZH:   Queen: [……它正冲上来迎接你！哈！哈！哈！]
ROW CAT:O00fe52b2e667cf62eb92 L2647 Mauser physical_line
  EN: [YIFFANY, Y-YOU'RE FALLING FROM LOW PLANETARY ORBIT!]
  ZH:   Mauser: [伊吠妮，你、你正在从低行星轨道坠落！]
ROW CAT:O58a1541b30f04e2ceb70 L2648 Mauser physical_line
  EN: [I... I DON'T...]
  ZH:   Mauser: [我……我没……]
ROW CAT:O9bbe95abac587acaa0dd L2649 Bossu physical_line
  EN: [TOMCAT, EVAL.]
  ZH:   Bossu: [雄猫，评估。]
ROW CAT:Obdeed4fceb050bc53e5a L2650 Tomcat physical_line
  EN: [ALREADY ON IT. STARSUIT PARACHUTE NOT AVAILABLE...]
  ZH:   Tomcat: [已经在办了。星服降落伞不可用……]
ROW CAT:O83026a76afb34fa2fefe L2651 Tomcat physical_line
  EN: [KINETIC ARRESTORS INSUFFICIENT AT THIS ALTITUDE.]
  ZH:   Tomcat: [动能制动器在这个高度不够用。]
ROW CAT:O16c1c94a255cc1586090 L2652 Bossu physical_line
  EN: [THE AGENT'S STARSHIP?]
  ZH:   Bossu: [特工的星舰？]
ROW CAT:Oda0fc5d5bb9fe8353ea3 L2653 Tomcat physical_line
  EN: [DAMAGED. ITS AUTOPILOT WILL NOT EXIT THE ATMOSPHERE]
  ZH:   Tomcat: [损坏了。以这艘船现在的状况，它的自动驾驶不会驶出大气层。]
ROW CAT:O4ea5178c04a03572262d L2654 Tomcat physical_line
  EN: [WITH THE VESSEL IN THAT CONDITION.]
  ZH: 
ROW CAT:O05c0a64cc35acdf54530 L2655 Bossu physical_line
  EN: [UNDERSTOOD, TOMCAT. AGENT YIFFANY, WE WILL SEEK ANY-]
  ZH:   Bossu: [明白，雄猫。特工伊吠妮，我们会尽一切——]
ROW CAT:Ocd15af9a19cb812684a8 L2656 Mauser physical_line
  EN: [YOUR SIGNAL'S BREAKING UP... I CAN'T KEEP...!]
  ZH:   Mauser: [你的信号在断……我维持不住……！]
ROW CAT:O43bcfb47ca2ddb79c678 L2657 Mauser physical_line
  EN: [...SOMEONE THINK OF SOMETHING!!]
  ZH:   Mauser: [……谁来想个办法啊！！]

## SCb005606d6a356fb7 | nsfw | datadf/all.ds | Test_Hacker1.CancelPurchase
CONTROL L5205  <Test_Hacker1.CancelPurchase>
ROW CAT:Of0fd0ae5bc7a27ff5b77 L5206 * physical_line
  EN: Are you worried about voiding the warranty? Pft.
  ZH:   * 你是担心会让保修失效吗？噗。
ROW CAT:O47b45f77d44882d93669 L5207 * physical_line
  EN: Oh well. Have you got something else for me to work on?
  ZH:   * 算了。你还有别的活儿要我干吗？

## SCb6a8079e056c9173 | nsfw | datadm/all.ds | Test_Hacker1.Goodbye
CONTROL L5197  <Test_Hacker1.Goodbye>
ROW CAT:O71096ac894feb9fd13c7 L5198 * physical_line
  EN: Bye bye, agent! Bring me something to play wi- I mean upgrade!
  ZH:   * 拜拜，特工！给我带点东西来玩——我是说升级！

## SCcbcffcaa86890a08 | nsfw | datadm/all.ds | Test_Hacker1.GoodbyeDog
CONTROL L5204  <Test_Hacker1.GoodbyeDog>
ROW CAT:O180f289d5a344368a96a L5205 * physical_line
  EN: Hey! Where are you going ducky?! We've got refactoring to do!
  ZH:   * 喂！你要去哪儿啊，小鸭子？！我们还有重构要做呢！

## SC8bfd024d82f7192b | nsfw | datadf/all.ds | Test_Hacker1.GoodbyeKobo
CONTROL L5198  <Test_Hacker1.GoodbyeKobo>
ROW CAT:O7815ebba25c48bc8288e L5199 * physical_line
  EN: -wait a sec, you're not the delivery guy! G-get out of here right now!
  ZH:   * -等等，你不是送货的！快、快给我出去！

## SC47d0eb6a9d4237de | nsfw | datadm/all.ds | Test_Hacker1.Hack
CONTROL L5238  <Test_Hacker1.Hack>
ROW CAT:O43c6ec83afe6d1b9f48a L5239 * physical_line
  EN: Ready to hack it?
  ZH:   * 准备好黑掉它了吗？

## SC698a97944b765f72 | nsfw | datadm/all.ds | Test_Hacker1.Meeting
CONTROL L5188  <Test_Hacker1.Meeting>
ROW CAT:O9c768748058f63dd1e7e L5189 * physical_line
  EN: Greetings, Yiffai. You don't know me, but I kinda snooped your satlink.
  ZH:   * 你好，伊吠。你不认识我，不过我偷偷探过你的卫星链路。
ROW CAT:O8eadbb6bce9207e6b106 L5190 * physical_line
  EN: So I've actually been watching you for a while, and I have a proposition...
  ZH:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:O8008ff60ecbed0c19f1f L5191 * physical_line
  EN: It's simple: You bring me those fancy chips you find out there,
  ZH:   * 很简单：你把在外头找到的那些花哨芯片带给我，
ROW CAT:O3821a3bbfc1edd63ce33 L5192 * physical_line
  EN: and I'll hack open doors for you! It's a win-win, obviously!
  ZH:   * 我就替你破解门禁！这显然是双赢！

## SCd20e823274383808 | nsfw | datadm/all.ds | Test_Hacker1.Purchased
CONTROL L5214  <Test_Hacker1.Purchased>
ROW CAT:O8925918d80c34c96e36d L5215 * physical_line
  EN: According to my calculations, that door should be open!
  ZH:   * 根据我的计算，那扇门现在应该开了！
ROW CAT:Oa3a956142b6c90f350a6 L5216 * physical_line
  EN: That one was fun! Got anything else for me?
  ZH:   * 那扇挺有意思的！还有别的要给我吗？

## SC37afac3718ef5e46 | nsfw | datadf/all.ds | Test_Hacker1.SoldOut
CONTROL L5209  <Test_Hacker1.SoldOut>
ROW CAT:Ocde8b9e44db144e0f4ee L5210 * physical_line
  EN: Hey wait! I already flashed that one.
  ZH:   * 嘿，等等！那个我已经刷过了。
ROW CAT:O3e2460a9aa2a7d0454e3 L5211 * physical_line
  EN: Is it spontaneously closing on you? I hate when that happens!
  ZH:   * 它会自己关掉吗？我最讨厌这种事了！

## SCc43b2b87c5051c92 | nsfw | datadf/all.ds | Test_Hacker1.Talk.radio
CONTROL L5222  <Test_Hacker1.Talk.radio>
ROW CAT:O350bbec3f8fc9ec39c6d L5223 * physical_line
  EN: Call me at frequency 28.250 if you need help finding those chips!
  ZH:   * 如果你需要帮忙找那些芯片，就用频率28.250呼我！

## SC116e2228a4a161b2 | nsfw | datadm/all.ds | Test_Hacker1.Talk.upgrade
CONTROL L5231  <Test_Hacker1.Talk.upgrade>
ROW CAT:Od81823f50b235b273dde L5232 * physical_line
  EN: Does your gear feel weak? Mediocre? Sub-optimal, even?
  ZH:   * 你的装备感觉很弱吗？平庸？甚至不够优化？
ROW CAT:O55c8aaf63e1ff291458d L5233 * physical_line
  EN: Well if you can furnish the requisite components, I'll tune it right up!
  ZH:   * 嗯，要是你能提供所需的部件，我就把它调好！

## SC23e089289bd28c10 | nsfw | datadm/all.ds | Test_Prison1.GoodbyeNotRescued
CONTROL L5246  <Test_Prison1.GoodbyeNotRescued>
ROW CAT:O4d807bd3fd2bd2463c84 L5247 * physical_line
  EN: [Try not to take too long!]
  ZH:   * [别拖太久！]

## SCff9950a2030921ae | nsfw | datadm/all.ds | Test_Prison1.NoBoneForDog
CONTROL L5252  <Test_Prison1.NoBoneForDog>
ROW CAT:O66a2ab351d31cd8a0302 L5253 * physical_line
  EN: [Y-you're a nice dog, right? Not gonna bite me or... something...]
  ZH:   * [你、你是只好狗狗，对吧？不会咬我，或者……什么的……]
ROW CAT:O9b645ac89e59f3a9e964 L5254 * physical_line
  EN: [You wanna be a good boy for me? Go get someone to help?]
  ZH:   * [想当我的乖狗狗吗？去找人来帮忙？]

## SC49e7d68778ae7066 | nsfw | datadm/all.ds | Test_Prison1.TalkAfterRescue.thanks
CONTROL L5285  <Test_Prison1.TalkAfterRescue.thanks>
ROW CAT:Ofd695d92dcb0b80689ae L5286 * physical_line
  EN: [I don't know what I would have done if you hadn't shown up!]
  ZH:   * [要是你没出现，我真不知道该怎么办！]

## SC674c1f273752aad2 | nsfw | datadf/all.ds | Test_Slaver1.AgentF0C
CONTROL L5340  <Test_Slaver1.AgentF0C>
ROW CAT:Ofc61bbaf58bb7350abf8 L5341 * physical_line
  EN: Little yiffer here isn't worth much, just take it! Just like he did ;3!
  ZH:   * 这儿这个小色狼不值钱，拿走吧！就像他那样做的 ;3！

## SC92ca510894cc3e28 | nsfw | datadf/all.ds | Test_Slaver1.BoneTheDog
CONTROL L5280  <Test_Slaver1.BoneTheDog>
ROW CAT:Obd3a87c57c55d70dffd5 L5281 * physical_line
  EN: Do you want my bone, boy? Do ya?
  ZH:   * 想要我的骨头吗，小子？想不想？

## SCf9535ec55b01cd65 | nsfw | datadm/all.ds | Test_Slaver1.ConfirmPurchase
CONTROL L5335  <Test_Slaver1.ConfirmPurchase>
ROW CAT:O278dee5694aadd584e09 L5336 * physical_line
  EN: You want that?
  ZH:   * 想要那个？

## SC1a13ebe1116caf56 | nsfw | datadm/all.ds | Test_Slaver1.GoodbyeDog
CONTROL L5300  <Test_Slaver1.GoodbyeDog>
ROW CAT:Oc43fc54434e55578f697 L5301 * physical_line
  EN: Get out of here mutt! The other dogs got to these slaves first!
  ZH:   * 从这儿滚出去，杂种狗！别的狗已经先得手这些奴隶了！

## SCcdfb0a2cabf90672 | nsfw | datadm/all.ds | Test_Slaver1.HasID
CONTROL L5328  <Test_Slaver1.HasID>
ROW CAT:Ob55e5295cffff2471159 L5329 * physical_line
  EN: Hmm... twenty one years old. Looks legitimate.
  ZH:   * 嗯……二十一岁。看起来没问题。
ROW CAT:O4e592bb2a0a6ba5ade77 L5330 * physical_line
  EN: Alright, can I get you something?
  ZH:   * 好了，要我给你来点什么吗？

## SC3808fa18b4a4fae7 | nsfw | datadf/all.ds | Test_Slaver1.NoBoneForDog
CONTROL L5283  <Test_Slaver1.NoBoneForDog>
ROW CAT:O924156630e4e59689314 L5284 * physical_line
  EN: What? Are you expecting another bone already?
  ZH:   * 什么？你还想再要一根骨头？
ROW CAT:Of08d70ab207e4e39604c L5285 * physical_line
  EN: I'd bone myself out of house and home at this rate!
  ZH:   * 照这速度，我非得为了骨头把家底都赔光不可！

## SC912d2cdab276661d | nsfw | datadm/all.ds | Test_Slaver1.Pickaxe
CONTROL L5350  <Test_Slaver1.Pickaxe>
ROW CAT:O328a60efc703a8e6a606 L5351 * physical_line
  EN: [Pickaxe description]
  ZH:   * [镐子描述]

## SCcce7bb996ca56977 | nsfw | datadf/all.ds | Test_Slaver1.SoldOut
CONTROL L5371  <Test_Slaver1.SoldOut>
ROW CAT:Oc7f242ad3a8cf1b17cf1 L5372 * physical_line
  EN: Flaunting your money now huh punk?!
  ZH:   * 现在显摆起钱来了是吧，小子？！
ROW CAT:Ob99db32d10fc6ab7fc05 L5373 * physical_line
  EN: Come back when I catch another mangy play thing!
  ZH:   * 等我再抓到一只癞皮玩物再来！

## SC80af86bbb34bdd41 | nsfw | datadm/all.ds | Test_Slaver1.Talk.hornets
CONTROL L5376  <Test_Slaver1.Talk.hornets>
ROW CAT:O0d0e96cf59112092b7e0 L5377 * physical_line
  EN: I'm glad there aren't any hornets around here.
  ZH:   * 幸好这儿没有大黄蜂。
ROW CAT:O7a853f848f09e4625790 L5378 * physical_line
  EN: The last place I was in, man...
  ZH:   * 我上一个待的地方啊……

## SCb56f05146b2c3c81 | nsfw | datadm/all.ds | Test_Slaver1.ThrowKnife
CONTROL L5347  <Test_Slaver1.ThrowKnife>
ROW CAT:O30d1a527e4168b74118e L5348 * physical_line
  EN: [ThrowKnife description]
  ZH:   * [ThrowKnife 描述]

## SC0af81e2468363076 | nsfw | datadm/all.ds | Test_Slaver1.Vitamin
CONTROL L5341  <Test_Slaver1.Vitamin>
ROW CAT:O50370a5ff6e60fcd071a L5342 * physical_line
  EN: This vitamin will increase your vitality!
  ZH:   * 这维生素能提高你的活力！

