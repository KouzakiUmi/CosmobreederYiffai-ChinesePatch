# batch-09-part03 精校工单：区域场景与条件分支（关卡救援与分支）（第 3／4 部分）

英文与当前中文都按整场连读；`current` 是构建候选的实际显示行（以本批参照摘录与 ORDER 记的候选为准）。
ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。

## SCe4a5c703d204367e | nsfw | datadf/all.ds | AreaA_Cellar.Goodbye
CONTROL L295  <AreaA_Cellar.Goodbye>
ROW CAT:O3a2e75d9486329e6015e L296 * physical_line
  EN: Remember, this meat hoard is our little secret!
  ZH:   * 记住，这堆肉可是咱俩的小秘密！

## SC109f5bcb5a8c4d7a | nsfw | datadm/all.ds | AreaA_Cellar.Talk.chew
CONTROL L300  <AreaA_Cellar.Talk.chew>
ROW CAT:Od1f97281b131547b9b3b L301 * physical_line
  EN: Whew! Sure is a lot of work to carve up a dragon.
  ZH:   * 呼！把龙切开还真费劲。
ROW CAT:Odff9f9d40f48c9249ccd L302 * physical_line
  EN: ...and don't even get me started on how tough it was to SLAY the things!
  ZH:   * ……更别提宰掉那些家伙有多难了！

## SCad4153c2431286dc | nsfw | datadm/all.ds | AreaA_Cellar.Talk.meatcode
CONTROL L304  <AreaA_Cellar.Talk.meatcode>
ROW CAT:O0c2b21292b351963d0fa L305 * physical_line
  EN: What? You want something else?
  ZH:   * 什么？你还想要点别的？
ROW CAT:O7cb803b159fbe6f0c03e L306 * physical_line
  EN: Well, alright... I can give you access to my secret cartoon and card stash...
  ZH:   * 好吧，行吧……我可以让你取用我藏起来的秘密漫画和卡牌……
ROW CAT:O5f71b8af9a1cce04dd34 L307 * physical_line
  EN: All you gotta do is... TAEGXLAA... if you know what I mean... He! He! He!
  ZH:   * 你要做的只是……TAEGXLAA……如果你懂我意思的话……嘿！嘿！嘿！
CONTROL L309  ### shared ###

## SC682ec778a224c4e4 | nsfw | datadm/all.ds | AreaA_Macsen1.HelloIDPlease
CONTROL L401  <AreaA_Macsen1.HelloIDPlease>
ROW CAT:O26436bf2eb59b1b1d53d L402 * physical_line
  EN: Oh hey there, I'm gonna need to see some ID.
  ZH:   * 哦，你好啊，我得先看看你的证件。
ROW CAT:Of71bf3cf67e15aa195b2 L403 * physical_line
  EN: No pups allowed in here!
  ZH:   * 这里不许小狗进来！

## SCea0d0c81537390bf | nsfw | datadf/all.ds | AreaA_Macsen1.IceCola
CONTROL L416  <AreaA_Macsen1.IceCola>
ROW CAT:O892019a03c557f49b9bb L417 * physical_line
  EN: It's my special recipe! The tastiest, coolest drink on this planet!
  ZH:   * 这是我的独家配方！这个星球上最美味、最冰凉的饮料！

## SCde1eaeed73a9a71f | nsfw | datadf/all.ds | AreaA_Macsen1.PsyCoffee
CONTROL L423  <AreaA_Macsen1.PsyCoffee>
ROW CAT:O833bcbc1b6049697acdb L424 * physical_line
  EN: If cola and tea aren't your speed, then how about some coffee?
  ZH:   * 如果可乐和茶都不合你口味，那来点咖啡怎么样？
ROW CAT:O2c5eb62750e25ff97a1f L425 * physical_line
  EN: It's from off-world beans, a real pick-me-up!
  ZH:   * 用外星咖啡豆做的，提神得很！
CONTROL L427  ### shared ###

## SC27fcdb72e9abdeeb | nsfw | datadm/all.ds | AreaA_Macsen1.PsyTea
CONTROL L418  <AreaA_Macsen1.PsyTea>
ROW CAT:O6603e9b08ec4ea50501c L419 * physical_line
  EN: This stuff will quench your thirst and recover some PSY, but to be honest...
  ZH:   * 这东西能解渴，还能恢复些精神力，不过说真的……
ROW CAT:Ob80860e748600137cad2 L420 * physical_line
  EN: ...it won't cool you down like a nice ICECOLA will!
  ZH:   * ……可它没法像爽口的 ICECOLA 那样让你凉快下来！ 

## SCe7467a8003c6322b | nsfw | datadf/all.ds | AreaA_Macsen1.Talk.placeholder
CONTROL L399  <AreaA_Macsen1.Talk.placeholder>
ROW CAT:Oe82479e390459d0eb333 L400 * physical_line
  EN: It's too hot to talk, sorry!
  ZH:   * 太热了，没法说话，抱歉！

## SC2c79ce8dd7bbcbae | nsfw | datadm/all.ds | AreaA_Macsen2.CancelPurchase
CONTROL L527  <AreaA_Macsen2.CancelPurchase>
CONTROL L528    if { !f(shop_juiced) } {
ROW CAT:O42be7687ee7c9279d171 L529 * physical_line
  EN: Can't blame ya. It's too hot down here to do business, right?
  ZH:     * 不能怪你。这下面热得要命，根本没法做生意，对吧？
CONTROL L530    } else {
ROW CAT:Of04d23d06185be8f6810 L531 * physical_line
  EN: That's a shame. Anything else?
  ZH:     * 真遗憾。还要点别的吗？
CONTROL L532    }

## SCe3ee0ccd59f9ac12 | nsfw | datadm/all.ds | AreaA_Macsen2.Goodbye
CONTROL L466  <AreaA_Macsen2.Goodbye>
ROW CAT:O1e663c987b33b4551620 L467 * physical_line
  EN: Good luck with the heat out there!
  ZH:   * 外头热得很，祝你好运！

## SC17d15dd3f9169339 | nsfw | datadf/all.ds | AreaA_Macsen2.GoodbyeNoJuice
CONTROL L474  <AreaA_Macsen2.GoodbyeNoJuice>
ROW CAT:O51b81bc8acf3b90c04b4 L475 * physical_line
  EN: Take care with the heat out there!
  ZH:   * 外头这么热，多当心！ 
ROW CAT:O1e13ecbdb73f5a942d47 L476 * physical_line
  EN: Wish I could go out and get a nice ICECOLA to beat this heat. Whew!
  ZH:   * 真希望能出去弄瓶上好的 ICECOLA 来压压这暑气。呼！

## SCc37272a31b3d2913 | nsfw | datadm/all.ds | AreaA_Macsen2.GoodbyeNoJuice
CONTROL L492  <AreaA_Macsen2.GoodbyeNoJuice>
ROW CAT:Ob186171113e84690efc6 L493 * physical_line
  EN: Take care with the heat out there!
  ZH:   * 外面那么热，你可当心！ 
ROW CAT:O607ada594f6a3cbc199f L494 * physical_line
  EN: Wish I could go out and get a nice ICECOLA to beat this heat. Whew!
  ZH:   * 真想出去买瓶ICECOLA消消暑。呼！

## SCf5f8613e86ca3581 | sfw | datadm/all.ds | AreaA_Macsen2.GoodbyeNoJuice
CONTROL L493  <AreaA_Macsen2.GoodbyeNoJuice>
ROW SFW7dd2ca497a0b83ef1220f6db L494 - physical_line
  EN: Take care with the heat out there! 
  ZH:   * 外面那么热，你可当心！ 
ROW SFW2f239ef4696e75be159b4769 L495 - physical_line
  EN: Wish I could go out and get a nice ICECOLA to beat this heat. Whew!
  ZH:   * 真想出去买瓶ICECOLA消消暑。呼！

## SCcb11bc0209257bca | nsfw | datadf/all.ds | AreaA_Macsen2.HelloNoJuice
CONTROL L470  <AreaA_Macsen2.HelloNoJuice>
ROW CAT:Ob776c4174fa877e1237b L471 * physical_line
  EN: Oh hey there, It's too hot to do any business right now!
  ZH:   * 哦，你好呀，现在太热了，什么生意都做不了！
ROW CAT:O9919f826540a3d1f7dc3 L472 * physical_line
  EN: You're free to browse until I get my paws on a nice cool drink...
  ZH:   * 在我弄到一杯冰凉的饮料之前，你随便看……

## SC301b3a3631022e27 | nsfw | datadm/all.ds | AreaA_Macsen2.NoJuiceNoPurchase
CONTROL L500  <AreaA_Macsen2.NoJuiceNoPurchase>
ROW CAT:O83d513f345b5c71ae32d L501 * physical_line
  EN: Sorry! It's too hot to do any business down here!
  ZH:   * 抱歉！这下面热得没法做生意！
ROW CAT:O75ef01760b97d5170c2e L502 * physical_line
  EN: I can't count money properly until I'm cooled off, ya know?
  ZH:   * 不凉快下来，我连钱都数不清，懂吧？
CONTROL L504  ### shared ###

## SC4076beeaefb8d1a0 | nsfw | datadf/all.ds | AreaA_Prison1.Goodbye
CONTROL L550  <AreaA_Prison1.Goodbye>
ROW CAT:Oa6d3c1cb648a4b027c83 L551 * physical_line
  EN: Thank you Yiffany!
  ZH:   * 谢谢你，伊吠妮！

## SC3b142b17233981e8 | sfw | datadm/all.ds | AreaA_Prison1.Goodbye
CONTROL L550  <AreaA_Prison1.Goodbye>
ROW SFW0d0ab6971ed6870cc5ac46a7 L551 - physical_line
  EN: Th-thanks pal! Good luck rescuing the others!
  ZH:   * 谢、谢谢你，伙计！祝你救其他人时一切顺利！

## SC4921979552224eba | nsfw | datadf/all.ds | AreaA_Prison1.GoodbyeDog
CONTROL L562  <AreaA_Prison1.GoodbyeDog>
ROW CAT:O355f1667c546e4c58262 L563 * physical_line
  EN: Please come back soon with your master, and a key!
  ZH:   * 请快些带着你的主人和一把钥匙回来！

## SC37a6c6282fcece99 | nsfw | datadm/all.ds | AreaA_Prison1.Hello
CONTROL L545  <AreaA_Prison1.Hello>
ROW CAT:Odc7e38db4f88f13a6c3d L546 * physical_line
  EN: Oh h-hey! Wasn't expecting another agent to get in here!
  ZH:   * 哦，嗨、嗨！没想到还有别的特工能进来！
ROW CAT:Oe5b571487f96c890570d L547 * physical_line
  EN: I might have myself in a sliight bit of trouble with some wyverns...
  ZH:   * 我可能跟几只双足飞龙惹上了那么一丁点儿麻烦…… 

## SCcbf136ff29befb0d | nsfw | datadm/all.ds | AreaA_Prison1.NoBoneForDog
CONTROL L558  <AreaA_Prison1.NoBoneForDog>
ROW CAT:O9bb68b9d747564d7281d L559 * physical_line
  EN: Can you get your master to come back with a key? I'm in a lot of trouble!
  ZH:   * 你能让你主人带把钥匙回来吗？我麻烦大了！

## SCbeffacca4b954dd1 | nsfw | datadf/all.ds | AreaA_Prison1.SoldOut
CONTROL L585  <AreaA_Prison1.SoldOut>
ROW CAT:O7a5d0c4a5c5ed3098bbc L586 * physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   * 谢谢，不过我已经被救出来了！

## SCe1e0758cb665759f | nsfw | datadm/all.ds | AreaA_Prison1.SoldOut
CONTROL L585  <AreaA_Prison1.SoldOut>
ROW CAT:Od57d51da9454a868bd41 L586 * physical_line
  EN: I'm like, fine now. Just some scratches and a bruised ego, that's all!
  ZH:   * 我现在嘛，没事了。就是擦破点皮，外加自尊心受了点伤，仅此而已！

## SCab83f4002d65c87d | nsfw | datadm/all.ds | AreaA_Prison1.TalkAfterRescue.thanks
CONTROL L591  <AreaA_Prison1.TalkAfterRescue.thanks>
ROW CAT:O3ca371b1d4a0cdcf4702 L592 * physical_line
  EN: Y-yay! I'm fine now, just give me a moment to catch my breath.
  ZH:   * 太、太好了！我现在没事了，让我缓口气就好。

## SC181e8bd3e7f593e1 | nsfw | datadf/all.ds | AreaA_Prison1.TalkBeforeRescue.wip
CONTROL L588  <AreaA_Prison1.TalkBeforeRescue.wip>
ROW CAT:Odc8d67c01f2c051dcce9 L589 * physical_line
  EN: H-how do you agents take this kind of abuse? I'm just a scout!
  ZH:   * 你、你们特工是怎么受得了这种折磨的？我只是个侦察兵啊！
ROW CAT:O1449bbb8462d494ae40b L590 * physical_line
  EN: Get me out of here!!
  ZH:   * 快把我弄出去！！

## SC726a36b62298199d | nsfw | datadm/all.ds | AreaA_Prison1.TalkBeforeRescue.wip
CONTROL L588  <AreaA_Prison1.TalkBeforeRescue.wip>
ROW CAT:Off3ea5097f145c41c223 L589 * physical_line
  EN: I was getting so much topping in before I ended up in here, I swear!
  ZH:   * 我发誓，被关进来之前，我可是一直在当攻操人！ 

## SCee194e5d1a248d58 | sfw | datadf/all.ds | AreaA_Prison1.TalkBeforeRescue.wip
CONTROL L588  <AreaA_Prison1.TalkBeforeRescue.wip>
ROW SFW3bb48bed09811085098a9184 L589 - physical_line
  EN: W-why did they lock me up? I'm just a scout!
  ZH:   * 他、他们为什么把我关起来？我只是个侦察兵啊！
ROW SFW80d9bd2392a632ada4b22daa L590 - physical_line
  EN: Get me out of here!!
  ZH:   * 快把我弄出去！！

## SCbfac1cd7cb210faa | nsfw | datadf/all.ds | AreaA_Prison2.CancelPurchase
CONTROL L616  <AreaA_Prison2.CancelPurchase>
ROW CAT:Oe85a830cf5ef188113db L617 * physical_line
  EN: Are you gonna help me get off, or just stand there lookin'?
  ZH:   * 你是来帮我爽一把，还是就站在那儿看着？

## SC1c78db157d84a15f | nsfw | datadm/all.ds | AreaA_Prison2.Goodbye
CONTROL L597  <AreaA_Prison2.Goodbye>
ROW CAT:Obd4650aa9455a8af652f L598 * physical_line
  EN: I'll... be right behind you. Kinda have to take care of something still...
  ZH:   * 我……马上就跟在你后面。还有点事得先处理一下……

## SCfa64733892dcbfcd | sfw | datadm/all.ds | AreaA_Prison2.Goodbye
CONTROL L598  <AreaA_Prison2.Goodbye>
ROW SFW7bfe19980cf5e79d902817f9 L599 - physical_line
  EN: I'll be right behind you!
  ZH:   * 我马上跟在你后面！

## SC965a794cb38022f8 | nsfw | datadm/all.ds | AreaA_Prison2.GoodbyeDog
CONTROL L609  <AreaA_Prison2.GoodbyeDog> 
ROW CAT:Obe8331efea3bed83f2c7 L610 * physical_line
  EN: Hey, where you going?! Don't be scared!!
  ZH:   * 嘿，你去哪儿啊？！别害怕啊！！

## SC6976667333d688f5 | sfw | datadf/all.ds | AreaA_Prison2.GoodbyeDog
CONTROL L611  <AreaA_Prison2.GoodbyeDog> 
ROW SFW2b7b6bd0ade00ee55a74c337 L612 - physical_line
  EN: Bye bye. If you wanna help, go find someone strong!
  ZH:   * 再见。想帮忙的话，就去找个力气大的来！

## SC03c2f4925eaf9031 | nsfw | datadf/all.ds | AreaA_Prison2.GoodbyeNotRescued
CONTROL L600  <AreaA_Prison2.GoodbyeNotRescued>
ROW CAT:Ofdde12fa5ca45dbe6d22 L601 * physical_line
  EN: If you spot any of those hunky dwarves, send 'em my way!
  ZH:   * 看到那种壮实的矮人，就叫他们来找我！
ROW CAT:O951e2601c0adb504c9bf L602 * physical_line
  EN: Toll 'em I know how to give a guy some relief after a long day in the mines...
  ZH:   * 跟他们讲，矿工累了一天，我懂怎么解乏……

## SC4789d2fe122af33a | sfw | datadf/all.ds | AreaA_Prison2.GoodbyeNotRescued
CONTROL L601  <AreaA_Prison2.GoodbyeNotRescued>
ROW SFW1a13f3353ddd010bdda98909 L602 - physical_line
  EN: If you spot any of those strong dwarves, send 'em my way!
  ZH:   * 要是见到那种力气大的矮人，叫他们来找我！
ROW SFWc27380b38df15e579860d8ad L603 - physical_line
  EN: I bet one of them could break me out!
  ZH:   * 我敢说他们肯定能把我弄出去！

## SC8797c0e3770b64f0 | nsfw | datadm/all.ds | AreaA_Prison2.Hello
CONTROL L593  <AreaA_Prison2.Hello>
ROW CAT:Of49587c20639bd959af7 L594 * physical_line
  EN: Oh hhh...hello. I've been waiting for someone to come along...
  ZH:   * 噢，嗯……你、你好。我一直等着有人来……
ROW CAT:O5a8318941845b186bb80 L595 * physical_line
  EN: Someone... to fuck me!
  ZH:   * 等个人……来操我！

## SC1506f118e279b90b | sfw | datadf/all.ds | AreaA_Prison2.Purchased
CONTROL L624  <AreaA_Prison2.Purchased>
ROW SFW4672efd31b85b180c40fc8f1 L625 - physical_line
  EN: Well then, I guess you're stronger than I thought!
  ZH:   * 好吧，看来你的力气比我想的大！

## SCf28ebc4b7e557ece | sfw | datadm/all.ds | AreaA_Prison2.Purchased
CONTROL L623  <AreaA_Prison2.Purchased>
ROW SFW0fe69c56df57e0c08fce1f30 L624 - physical_line
  EN: Wow!! That was awesome!
  ZH:   * 哇！！太厉害了！

## SCdf51cbd65aa71759 | nsfw | datadf/all.ds | AreaA_Prison2.SoldOut
CONTROL L626  <AreaA_Prison2.SoldOut>
ROW CAT:O4ae356f3d302980fa122 L627 * physical_line
  EN: I'm okay now, just baskin' in the afterglow.
  ZH:   * 我现在没事了，正沉浸在余韵里呢。

## SCe6e4d4a420855b49 | sfw | datadm/all.ds | AreaA_Prison2.SoldOut
CONTROL L626  <AreaA_Prison2.SoldOut>
ROW SFWf8709297b7723e1a2437c4a2 L627 - physical_line
  EN: Thanks lad. I'll head back to the hangar in a little while.
  ZH:   * 谢谢，小伙子。我过一会儿就回机库。

## SC46a571677d256cf9 | nsfw | datadm/all.ds | AreaA_Prison2.TalkBeforeRescue.bopped
CONTROL L628  <AreaA_Prison2.TalkBeforeRescue.bopped>
ROW CAT:Oe256e4da229a99acd28e L629 * physical_line
  EN: Impressed by how deep I take this toy?
  ZH:   * 这玩具我能吞得这么深，佩服吗？
ROW CAT:Od995bb695900f95c46f6 L630 * physical_line
  EN: Next, why don't we find out how deep I can take... you!
  ZH:   * 接下来，试试我能把……你吞多深，怎么样！

## SCce940831fc43c17e | nsfw | datadm/all.ds | AreaA_Prison3.CancelPurchase
CONTROL L658  <AreaA_Prison3.CancelPurchase>
CONTROL L659    if { hasItem(Key) } {
ROW CAT:O305773f424a265ea33ab L660 * physical_line
  EN: B-b-but you already have a key! Was it something I said? Sorry!
  ZH:     * 可、可、可是你已经有钥匙了！是我说错什么了吗？对不起！
CONTROL L661    } else {
ROW CAT:O424cc4ed4d34c75d60e4 L662 * physical_line
  EN: I've... already tried picking the lock. I'm afraid you'll have to find a key...
  ZH:     * 我……已经试过撬锁了。恐怕你得去找把钥匙……
CONTROL L663    }

## SCef4ea3e364baa68a | nsfw | datadm/all.ds | AreaA_Prison3.Goodbye
CONTROL L640  <AreaA_Prison3.Goodbye>
ROW CAT:O5579f44c2629698fd6c3 L641 * physical_line
  EN: Aww, are you s-sure you don't wanna play...?
  ZH:   * 哎呀，你、你确定不想再玩一会儿……？

## SCac5b9f5097efca6e | nsfw | datadf/all.ds | AreaA_Prison3.GoodbyeDog
CONTROL L651  <AreaA_Prison3.GoodbyeDog>
ROW CAT:O865697caa77a7b551eed L652 * physical_line
  EN: Seeya girl! Watch out for the Barkers!
  ZH:   * 回见啦，姑娘！小心那些吠叫者！

## SC58290972e18056e2 | sfw | datadm/all.ds | AreaA_Prison3.GoodbyeNotRescued
CONTROL L642  <AreaA_Prison3.GoodbyeNotRescued>
ROW SFW52d4f73f263db4f5b830a855 L643 - physical_line
  EN: I guess I'm not getting rescued today? O-okay, well... I'll be waiting.
  ZH:   * 看来今天是没人来救我了？好、好吧，那……我会等着。

## SC48c491b9bb11d6cf | nsfw | datadf/all.ds | AreaA_Prison3.Hello
CONTROL L636  <AreaA_Prison3.Hello>
ROW CAT:O34fba6f36da392d124ad L637 * physical_line
  EN: Oh heya! What brings you over here?
  ZH:   * 哦，嗨呀！什么风把你吹到这儿来了？

## SC94a7f0211b18dcf1 | nsfw | datadf/all.ds | AreaA_Prison3.NoBoneForDog
CONTROL L648  <AreaA_Prison3.NoBoneForDog>
ROW CAT:O9d43d33ebdda7e31efb1 L649 * physical_line
  EN: You're a real cute doggie and all, but what are you doing here?!
  ZH:   * 你是挺可爱的小狗狗没错啦，可你跑这儿来干什么呀？！

## SC9b53a7e2c23905c8 | nsfw | datadf/all.ds | AreaA_Prison3.NotEnoughMoney
CONTROL L666  <AreaA_Prison3.NotEnoughMoney>
ROW CAT:O4258b905b7fa997fb23c L667 * physical_line
  EN: What's up? Missing something?
  ZH:   * 怎么了？是缺什么东西吗？

## SCa66a2bf9847fab8c | sfw | datadm/all.ds | AreaA_Prison3.Purchased
CONTROL L667  <AreaA_Prison3.Purchased>
ROW SFW461509950827abd2f0028bbd L668 - physical_line
  EN: W-wow! Thanks!
  ZH:   * 哇、哇哦！谢谢！

## SCc627256dde05a68c | sfw | datadf/all.ds | AreaA_Prison3.Purchased
CONTROL L663  <AreaA_Prison3.Purchased>
ROW SFW4cc1d39df23b851809af59d8 L664 - physical_line
  EN: ...eh, fiiine. I guess this vacation had to end sooner or later.
  ZH:   * ……唉，好——吧。我想这假期迟早也得结束。

## SCc83fcd159960bdc3 | nsfw | datadm/all.ds | AreaA_Prison3.Rescue
CONTROL L665  <AreaA_Prison3.Rescue>
ROW CAT:Oec51fcb00b35e029578f L666 * physical_line
  EN: Oh? Are you gonna let me out?!
  ZH:   * 哦？你是要放我出去吗？！

## SCd26ac691afa4c235 | nsfw | datadm/all.ds | AreaA_Prison3.SoldOut
CONTROL L675  <AreaA_Prison3.SoldOut>
ROW CAT:Oe91eeaf826a7329a9c79 L676 * physical_line
  EN: I... I think I can take it from here. I could even t-take it from *you*! <3
  ZH:   * 我……我想接下来自己就能应付了。要是换成*你*来，我、我也吃得消！<3

## SC1d36cfdcc80eea2b | nsfw | datadf/all.ds | AreaA_Prison3.TalkAfterRescue.thanks
CONTROL L676  <AreaA_Prison3.TalkAfterRescue.thanks>
ROW CAT:Of50894effd45a1f8d713 L677 * physical_line
  EN: Guess HQ is telling you to get me back to work, huh?
  ZH:   * 看样子总部让你催我回去干活了，是吧？
ROW CAT:Oee44b936d17745ca7631 L678 * physical_line
  EN: Fiiiiine, I'll get my reports in and all that...
  ZH:   * 好——啦，我会把报告交上去什么的啦……

## SCc71a41293028bc8b | nsfw | datadm/all.ds | AreaA_Prison3.TalkAfterRescue.thanks
CONTROL L681  <AreaA_Prison3.TalkAfterRescue.thanks>
ROW CAT:O04af1a8f4d796067490d L682 * physical_line
  EN: You know, I've developed a r-real taste for doggies since I landed.
  ZH:   * 你知道吗，自从落地后，我就真、真的越来越喜欢狗狗了。
ROW CAT:O4e52d3472a903e30caf7 L683 * physical_line
  EN: I can't help but notice that you're a dog...
  ZH:   * 说起来，你不就是狗狗嘛……

## SCe46f9a3291d3b7f9 | nsfw | datadf/all.ds | AreaB_Macsen1.JudoHead
CONTROL L731  <AreaB_Macsen1.JudoHead>
ROW CAT:O68681a09c8777c8a4a92 L732 * physical_line
  EN: Gee, this would go real well with a gi, wouldn't it?
  ZH:   * 哎呀，这玩意儿配道服正合适，不是吗？
ROW CAT:Ocf1f05f702633ad3fc0c L733 * physical_line
  EN: Why, who even needs a tazer when you'd be kitted out like that!
  ZH:   * 哎呀，你这身装备还用得着电击枪吗！

## SC8a68ed72a579e1e2 | sfw | datadf/all.ds | AreaB_Macsen1.Talk.digging
CONTROL L742  <AreaB_Macsen1.Talk.digging>
ROW SFW8e84888f21c97cd49e0f793d L743 - physical_line
  EN: You look like a smart and eager dog!
  ZH:   * 你看起来真是只聪明又有干劲的狗！
ROW SFW18f602fbe47294a8bb3c7c0c L744 - physical_line
  EN: Did you know that ferals are able to dig up dirt by pressing DOWN+ATTACK?
  ZH:   * 你知道野兽形态可以按DOWN+ATTACK挖开泥土吗？
ROW SFWb27ef37e7378f3eff7c7e976 L745 - physical_line
  EN: It's just good info to know, ya know!
  ZH:   * 这可是实用的小知识，记着没坏处！

## SCf04eda3151f1d482 | nsfw | datadf/all.ds | AreaB_Macsen1.Talk.food
CONTROL L751  <AreaB_Macsen1.Talk.food>
ROW CAT:O8b5740bb2f2773a68b55 L752 * physical_line
  EN: It's just one crazy rumor after another out here, I tell ya.
  ZH:   * 跟你说，这儿的离谱传闻真是一个接一个。
ROW CAT:O7dc18df178ae2af82748 L753 * physical_line
  EN: Somebody was telling me that they saw a Werehund in the lower levels, even.
  ZH:   * 甚至有人跟我说，在下层看见了一只狼犬。
CONTROL L755  ### shared ###

## SC03d179d042247e27 | nsfw | datadf/all.ds | AreaB_Macsen2.Goodbye
CONTROL L795  <AreaB_Macsen2.Goodbye>
ROW CAT:O96efe21c61738e0a91ae L796 * physical_line
  EN: Remember, this is our little secret!
  ZH:   * 记住了，这是咱们俩的小秘密！

## SC6b1237341341f71f | nsfw | datadm/all.ds | AreaB_Macsen2.Talk.macsenlect
CONTROL L804  <AreaB_Macsen2.Talk.macsenlect>
ROW CAT:O1f08b0cd6d23613c673d L805 * physical_line
  EN: Take some lect, but don't tell anyone, alright?
  ZH:   * 拿点 lect 吧，可别跟人说，行吗？

## SC14fe05436fb43406 | nsfw | datadm/all.ds | AreaB_Macsen2.Talk.macsenmoneycode2
CONTROL L815  <AreaB_Macsen2.Talk.macsenmoneycode2>
ROW CAT:O89001d2fae78fdc4323d L816 * physical_line
  EN: Didn't you hear me? There's nothing left!
  ZH:   * 你没听见我说话吗？什么都没剩下了！
ROW CAT:Oeca3e772c1bc0e6fd327 L817 * physical_line
  EN: Go be greedy somewhere else!
  ZH:   * 想贪，就去别处贪！

## SC8e1ed5d31491bfbc | nsfw | datadf/all.ds | AreaB_MacsenBar.Hello
CONTROL L855  <AreaB_MacsenBar.Hello>
ROW CAT:O015a54bbd649854a70b9 L856 * physical_line
  EN: Hey there! Don't be a stranger, come on in!
  ZH:   * 嘿，你好！别见外，快进来吧！

## SC17cc2156161f94a5 | sfw | datadf/all.ds | AreaB_MacsenBar.Talk.main
CONTROL L861  <AreaB_MacsenBar.Talk.main>
CONTROL L862    if { !f(ClassicWerepup_defeated)} {
ROW SFWa25bf8c3ae861321e4392dab L863 - physical_line
  EN: You're kinda early! Come back later and we can chat and drink, alright?
  ZH:     * 你来得有点早！晚点再来，咱们喝点东西聊聊天，好吗？
CONTROL L864    } else {
ROW SFWcf24523ef08bf6e1997dab4e L865 - physical_line
  EN: Well! That last quake just wrecked my whole supply!
  ZH:     * 唉！上次地震把我的存货全毁了！
ROW SFW93a5461d7fb1cc38574c8f76 L866 - physical_line
  EN: I'll tell you what though, you seem like you're a good strong pupper.
  ZH:     * 不过说真的，你看着是只挺棒又壮实的狗狗。
ROW SFWcc5bfd37fc5990d137a3b4d0 L867 - physical_line
  EN: Another one of you cosmofellas came by muttering that they left 
  ZH:     * 之前还来过一个跟你一样的太空伙计，嘴里嘀咕着说把武器落在这儿正北边了！ 
ROW SFWfd8712bb1940999b829816b8 L868 - physical_line
  EN: their weapon just north of here!
  ZH: 
ROW SFWffdc410021ee11aa3d6ecbb1 L869 - physical_line
  EN: "Bottom, middle, middle, top..." is what they kept saying, whatever that means!
  ZH:     * 那家伙一直念叨着"下、中、中、上……"，谁知道是什么意思！
CONTROL L870    }

## SCd7699dd41f4732f4 | nsfw | datadf/all.ds | AreaB_Prison1.Goodbye
CONTROL L917  <AreaB_Prison1.Goodbye>
ROW CAT:O3076fe3bf25c2c0a6f2d L918 * physical_line
  EN: I'll be right along! Just as soon I can get away from my buddy here, hehe...
  ZH:   * 我马上就跟上来！只要我能从旁边这位伙计那儿脱开身，嘿嘿……

## SC97b6e425003ec30d | sfw | datadm/all.ds | AreaB_Prison1.GoodbyeDog
CONTROL L932  <AreaB_Prison1.GoodbyeDog>
ROW SFW4af0668b56657915cbc967db L933 - physical_line
  EN: Good boy! Come back with your master!
  ZH:   * 乖孩子！带你的主人回来！

## SCbdec84ebe60d6384 | sfw | datadm/all.ds | AreaB_Prison1.NoBoneForDog
CONTROL L929  <AreaB_Prison1.NoBoneForDog>
ROW SFWe666178d968da0aabba161bd L930 - physical_line
  EN: Huh? Are you a good dog? Can you go get someone to help?
  ZH:   * 嗯？你是条好狗狗吗？能去找人来帮忙吗？

## SC6328cfd1a333261a | sfw | datadm/all.ds | AreaB_Prison1.SoldOut
CONTROL L948  <AreaB_Prison1.SoldOut>
ROW SFWfdeb257b8001e78e5dda7a9f L949 - physical_line
  EN: I think I can handle this from here.
  ZH:   * 接下来我想自己能搞定了。

## SC4734965f1d105f7e | nsfw | datadm/all.ds | AreaB_Prison1.TalkAfterRescue.thanks
CONTROL L959  <AreaB_Prison1.TalkAfterRescue.thanks>
ROW CAT:O800ef7847eefa154fdb9 L960 * physical_line
  EN: Ngh... just... need a bit. Th-thanks.
  ZH:   * 唔……只是……得歇一会儿。谢、谢谢。

## SCa6aaeb37b15a8c99 | sfw | datadm/all.ds | AreaB_Prison1.TalkAfterRescue.thanks
CONTROL L955  <AreaB_Prison1.TalkAfterRescue.thanks>
ROW SFW06054fd330b2f81429847f8b L956 - physical_line
  EN: Hmm... if I could have just gotten into that panel...
  ZH:   * 嗯……要是能打开那个面板就好了……
ROW SFW47215fa2ee4fedb926bc30d2 L957 - physical_line
  EN: Well, thanks anyway.
  ZH:   * 总之，还是谢谢你。

## SC86572c4386d4b135 | sfw | datadf/all.ds | AreaB_Prison1.TalkBeforeRescue.bopped
CONTROL L948  <AreaB_Prison1.TalkBeforeRescue.bopped>
ROW SFWa831055d27dc24243cba3eb1 L949 - physical_line
  EN: Some big kobolds locked me up in here.
  ZH:   * 几个大块头狗头人把我关在这里了。
ROW SFW8941423e0264cdca50944718 L950 - physical_line
  EN: And I thought they were my friends...
  ZH:   * 我还以为他们是我的朋友呢……

## SCdc2b971814220efc | nsfw | datadm/all.ds | AreaB_Prison2.CancelPurchase
CONTROL L982  <AreaB_Prison2.CancelPurchase>
ROW CAT:O78311ef0f3dd8bc04136 L983 * physical_line
  EN: It's pretty basic, rook. Put the key in the lock and *turn*.
  ZH:   * 挺简单的，菜鸟。把钥匙插进锁里，*转*。
ROW CAT:Ob52023abe2f0cc41a2ae L984 * physical_line
  EN: Do I have to explain it to you again?
  ZH:   * 还得我再给你解释一遍吗？

## SCe113daeb4bc2fe2c | sfw | datadf/all.ds | AreaB_Prison2.GoodbyeDog
CONTROL L970  <AreaB_Prison2.GoodbyeDog>
ROW SFW36f249df0fc41d5ed6201dbc L971 - physical_line
  EN: Come back soon! I can't take much more of this boring room!
  ZH:   * 快点回来！这无聊的房间我真的快待不下去了！

## SC426bff72d76c658d | nsfw | datadm/all.ds | AreaB_Prison2.Hello
CONTROL L961  <AreaB_Prison2.Hello>
ROW CAT:O44deb18bb1ca52b09659 L962 * physical_line
  EN: Listen up, rookie! Your immediate assistance is required.
  ZH:   * 听好了，新兵！现在需要你立刻来支援。

## SC61bcff6f7f8c067b | sfw | datadf/all.ds | AreaB_Prison2.HelloDog
CONTROL L964  <AreaB_Prison2.HelloDog>
ROW SFWc8d9bba389d7a783aa605180 L965 - physical_line
  EN: I... a dog?!
  ZH:   * 我……一只狗？！

## SCc766deac692637c4 | nsfw | datadf/all.ds | AreaB_Prison2.NoBoneForDog
CONTROL L966  <AreaB_Prison2.NoBoneForDog>
ROW CAT:Off425ba9fe7dc634a57c L967 * physical_line
  EN: Please help me, you guh... aaaah! ... gotta find someone...
  ZH:   * 求求你帮帮我，你这……呃啊！……得找个人来……

## SC8943aa35796a1606 | nsfw | datadf/all.ds | AreaB_Prison2.NotEnoughMoney
CONTROL L989  <AreaB_Prison2.NotEnoughMoney>
ROW CAT:Ob1713009347f09b3feee L990 * physical_line
  EN: You'll need a key! I've... aaahng! T-tried everything...
  ZH:   * 你需要钥匙！我……啊嗯！什、什么都试过了……

## SC9e717b3c9b09a003 | nsfw | datadm/all.ds | AreaB_Prison2.Purchased
CONTROL L989  <AreaB_Prison2.Purchased>
ROW CAT:O917305385c54b5891a86 L990 * physical_line
  EN: Aagh! Can't you do anything right?
  ZH:   * 啊！你连一件事都做不好吗？

## SC1056a39770dc4ae9 | sfw | datadm/all.ds | AreaB_Prison2.Purchased
CONTROL L986  <AreaB_Prison2.Purchased>
ROW SFW4c90eb02e63d0cfee61ef12a L987 - physical_line
  EN: Wow, *good job*. Want me to ask command to give you a gold star?
  ZH:   * 哇，*真能干*。要不要我请指挥部给你颁颗小金星？

## SC1f61d9eddf06a87c | sfw | datadf/all.ds | AreaB_Prison2.SoldOut
CONTROL L992  <AreaB_Prison2.SoldOut>
ROW SFWf5f7191c3c565d9a86e385e2 L993 - physical_line
  EN: I'm fine now. Just need a minute to stretch my legs.
  ZH:   * 我现在没事了。只需要点时间活动活动腿脚。

## SCa178fad55d5a3a16 | nsfw | datadf/all.ds | AreaB_Prison2.TalkAfterRescue.thanks
CONTROL L999  <AreaB_Prison2.TalkAfterRescue.thanks>
ROW CAT:O0b38fb374ff10b005f04 L1000 * physical_line
  EN: Nnngh... hard to believe a machine could make me cum that much...
  ZH:   * 嗯呃……真不敢相信，一台机器能让我高潮那么多……

## SC82c4a5695baff807 | nsfw | datadm/all.ds | AreaB_Slaver2.CancelPurchase
CONTROL L1028  <AreaB_Slaver2.CancelPurchase>
ROW CAT:Obdc7cb3051b481762804 L1029 * physical_line
  EN: Well are you buying or not? Don't waste my time...
  ZH:   * 到底买不买？别浪费我时间……

## SC2fb014a060b34fa9 | nsfw | datadm/all.ds | AreaB_Slaver2.FakeMilk
CONTROL L1044  <AreaB_Slaver2.FakeMilk>
ROW CAT:Ocf3e514af132d78de604 L1045 * physical_line
  EN: I gotta be honest with you, I don't know what animal this is from.
  ZH:   * 说实话，我也不知道这是从哪种动物身上弄来的。
ROW CAT:Oe2b8b2a366f8f4b61f99 L1046 * physical_line
  EN: Makes for good drinkin' if you're *real* thirsty though.
  ZH:   * 不过你要是*真的*渴坏了，喝着还挺不错。

## SC7eee9c3ea3ab595c | nsfw | datadf/all.ds | AreaB_Slaver2.Goodbye
CONTROL L1008  <AreaB_Slaver2.Goodbye>
CONTROL L1009    if { !koboCostume() } {
ROW CAT:Of3e8bfb47cdbfcae67ad L1010 * physical_line
  EN: Be seeing you. Heh-heh...
  ZH:     * 回头见。嘿嘿……
CONTROL L1011    } else {
ROW CAT:O308097b5cb078c62dc34 L1012 * physical_line
  EN: Take care out there. Ole Tutone's a rough place these days.
  ZH:     * 出门小心点。如今这老图托恩可不太平。
CONTROL L1013    }

## SC048046829ebef139 | nsfw | datadf/all.ds | AreaB_Slaver2.Hello
CONTROL L1001  <AreaB_Slaver2.Hello>
CONTROL L1002    if { !koboCostume() } {
ROW CAT:O021e5aa387bb33d4ec13 L1003 * physical_line
  EN: Well hey there, little lady. I gots some real pree-mo dining here.
  ZH:     * 哟，小妞。我这儿可有顶级好菜。
CONTROL L1004    } else {
ROW CAT:O8a0be46c26d9de40683d L1005 * physical_line
  EN: Well look what we have here! Come in, come in! Welcome to my junk shop!
  ZH:     * 哟，瞧瞧谁来了！进来进来！欢迎光临我的杂货铺！
CONTROL L1006    }

## SC4a1668ddd6627fd0 | nsfw | datadm/all.ds | AreaB_Slaver2.HelloDog
CONTROL L1071  <AreaB_Slaver2.HelloDog>
ROW CAT:O1c95f7c22e66462dc431 L1072 * physical_line
  EN: What the-? A dog?!
  ZH:   * 什么鬼——？一条狗？！

## SC01a8c3f2132c4f83 | nsfw | datadm/all.ds | AreaB_Slaver2.NotEnoughMoney
CONTROL L1034  <AreaB_Slaver2.NotEnoughMoney>
ROW CAT:O507596d9e992a1d0745f L1035 * physical_line
  EN: This ain't a peepshow, punk! Show me the lect or get out!
  ZH:   * 这儿可不是给你白看的，混蛋！拿出LECT来，不然滚蛋！

## SC72617ff7b3fd0c1e | nsfw | datadf/all.ds | AreaB_Slaver2.SoldOut
CONTROL L1026  <AreaB_Slaver2.SoldOut>
ROW CAT:O7e39575453c90fab9df6 L1027 * physical_line
  EN: You stupid or something?! That was my last one!
  ZH:   * 你傻了还是咋的？！那是最后一个！

## SC60b2521ed8918dd3 | nsfw | datadf/all.ds | AreaB_Slaver2.Talk.kobo
CONTROL L1060  <AreaB_Slaver2.Talk.kobo>
CONTROL L1061    if { koboCostume() } {
ROW CAT:O74e8ea2524757a3baa1b L1062 * physical_line
  EN: You smell pretty cute for a kobold, heh-heh. What crew you fly in with?
  ZH:     * 你这科博德，闻起来倒挺讨人喜欢，嘿嘿。你跟哪支船队来的？
CONTROL L1063    }
CONTROL L1065  ### dog handling

## SCfd3a35d14d8646de | nsfw | datadm/all.ds | AreaB_Slaver2.Talk.kobo
CONTROL L1065  <AreaB_Slaver2.Talk.kobo>
CONTROL L1066    if { koboCostume() } {
ROW CAT:O4c25f65c290e84e68628 L1067 * physical_line
  EN: You smell pretty cute for a kobold, heh-heh. What crew you fly in with?
  ZH:     * 作为科博德，你闻着还挺可爱的，嘿嘿。你跟哪伙船员来的？
CONTROL L1068    }
CONTROL L1070  ### dog handling

## SCc9fbd617723c539d | nsfw | datadm/all.ds | AreaB_Slaver2.Talk.spacebrats
CONTROL L1048  <AreaB_Slaver2.Talk.spacebrats>
CONTROL L1049    if { !koboCostume() } {
ROW CAT:Od3239a32d9102d0a0a5d L1050 * physical_line
  EN: Business been pretty good lately, what with all you spacebrats wandering around.
  ZH:     * 最近生意不错，多亏你们这些太空小鬼到处晃悠。
CONTROL L1051    }
CONTROL L1053  ### as kobo

## SCb4c2db1ad75e6b65 | nsfw | datadm/all.ds | AreaB_Slaver2.TazerAttuned
CONTROL L1054  <AreaB_Slaver2.TazerAttuned>
ROW CAT:O524dadca896f3a6c27e6 L1055 * physical_line
  EN: This here? One of them tazers those cute lil spacebrats carry around.
  ZH:   * 这个？就是那些可爱的太空小混蛋随身带的电击枪。
ROW CAT:Oe04f7adc1a1e4022dc3d L1056 * physical_line
  EN: Seemed like a pretty good one, until we broke it... the tazer, I mean.
  ZH:   * 没被我们玩坏前还挺好用……我说电击枪。
ROW CAT:Oe230660309689b540bde L1057 * physical_line
  EN: But the scrap alone will go for a thousand lect, off world. How about it?
  ZH:   * 可光卖废料，拿到外星都能卖一千LECT。怎么样？

## SC34de39f5b8eb80a6 | nsfw | datadm/all.ds | AreaC_Macsen1.Goodbye
CONTROL L1126  <AreaC_Macsen1.Goodbye>
ROW CAT:O4cb84146358eed3c3de3 L1127 * physical_line
  EN: Grrr, bring more Lect with you next time, ya scoundrel!
  ZH:   * 咕呜，下次多带点 Lect 来，你这混蛋！

## SCa385d50f5df37cf0 | nsfw | datadf/all.ds | AreaC_Macsen1.Talk.forest2
CONTROL L1140  <AreaC_Macsen1.Talk.forest2>
ROW CAT:Oc508a477cf17183a1a8c L1141 * physical_line
  EN: The scariest part about this outfit...
  ZH:   * 这身行头最吓人的地方……
ROW CAT:O4a1cfd04117d0721adb9 L1142 * physical_line
  EN: ...is that sometimes the zipper gets stuck!
  ZH:   * ……就是拉链有时候会卡住！

## SC43472e1c4f8e5c08 | nsfw | datadf/all.ds | AreaC_Macsen1.Talk.forest3
CONTROL L1144  <AreaC_Macsen1.Talk.forest3>
ROW CAT:Ob8d065388a1505e69a54 L1145 * physical_line
  EN: Don't forget to take some food for your pets!
  ZH:   * 别忘了给你的宠物带点吃的！
CONTROL L1147  ### shared ###

## SCfd4ab3dc2ab0c65b | nsfw | datadm/all.ds | AreaC_MacsenDark.DarkNoPurchase
CONTROL L1201  <AreaC_MacsenDark.DarkNoPurchase>
ROW CAT:O03765fc843c2231400c0 L1202 * physical_line
  EN: Look buddy, if I could see where anything is I'd gladly sell that to you
  ZH:   * 听着，老兄，要是我能看清东西在哪儿，我很乐意卖给你，但我每次一动，好像都会踩到什——嗷呜！
ROW CAT:Od8ce6cac591b63813e30 L1203 * physical_line
  EN: But every time I move I seem to step on somethi-YEOWCH!
  ZH: 
ROW CAT:Ofae9ddcc07cd35a3f42b L1204 * physical_line
  EN: Nope, no sales until the lights are back on. Sorry!
  ZH:   * 不行，灯亮之前不卖东西。抱歉！

## SC1d9a1c61cec5875e | sfw | datadf/all.ds | AreaC_MacsenDark.Talk.dark
CONTROL L1211  <AreaC_MacsenDark.Talk.dark>
CONTROL L1212    if { !hasItem(SpecialTorch) } {
ROW SFW8e3768b102f1a28f4d19af57 L1213 - physical_line
  EN: This is just my luck, isn't it? 
  ZH:     * 我的运气还真是好啊，是吧？ 
ROW SFW267f2fc596449b95d0209b5e L1214 - physical_line
  EN: First somewan stole my hookshot so I have to walk around on these tiny legs...
  ZH:     * 先是有人偷了我的钩索，害我只能靠这两条小短腿走路……
ROW SFW180edc3dbcd60485ff8c149f L1215 - physical_line
  EN: ...and now the power is out and my flashlight is missing! Bah!
  ZH:     * ……而现在又停电了，手电筒也不见了！哼！
CONTROL L1216    } else {
ROW SFWc06a1fcd7c7939c3f58c2b45 L1217 - physical_line
  EN: It's been getting ruffer and ruffer to do business around these parts, let me tell ya.
  ZH:     * 跟你说吧，在这一带做生意是越来越难了。
ROW SFW1d93fe5dca7d5a544838cb3a L1218 - physical_line
  EN: Earthquakes happen every other hour and the monsters are rowdier than ever...
  ZH:     * 隔一个小时就地震一次，魔物也比以前更闹腾了……
ROW SFW01f5feecc031fb92d84d2a96 L1219 - physical_line
  EN: ...it almost feels like things are building up to something!
  ZH:     * ……总觉得好像有什么大事要发生了！
CONTROL L1220    }

## SCe338b7546a4c96ff | nsfw | datadm/all.ds | AreaC_MacsenDark.Talk.dress
CONTROL L1227  <AreaC_MacsenDark.Talk.dress>
CONTROL L1228    if { hasItem(SpecialTorch) } {
ROW CAT:O6a4b2efc61a98356ef15 L1229 * physical_line
  EN: So anyways, you ever wear an Elven dress before? You look like the sort!
  ZH:     * 话说回来，你以前穿过精灵连衣裙吗？你看着就像会穿的！
ROW CAT:Oab0ac4995f0674aabb5c L1230 * physical_line
  EN: Rumors say they prevent blocks from crumbling beneath your feet
  ZH:     * 听说它们靠某种纳米机器，能防止脚下的方块崩塌……
ROW CAT:Oc94afb9c61ec9ad5704c L1231 * physical_line
  EN: thanks to some sort of nano machines...
  ZH: 
ROW CAT:O65a29976c0fe903ea2c4 L1232 * physical_line
  EN: ...but I think it's actually just magic!
  ZH:     * ……不过我觉得其实就是魔法！
CONTROL L1233    }
CONTROL L1235  ### shared ###

## SCce26cc53dbd39f07 | nsfw | datadm/all.ds | AreaC_MacsenDark.TazerRapier
CONTROL L1206  <AreaC_MacsenDark.TazerRapier>
ROW CAT:O06ed0e4e63f85b7cc02a L1207 * physical_line
  EN: This is a pretty little elven letter opener, if I do say so myself!
  ZH:   * 要我自己说，这可是一把精巧的精灵拆信刀！
ROW CAT:O25aa1989ac563f073a4f L1208 * physical_line
  EN: Feather light, just like how those dresses the elves craft will make you feel.
  ZH:   * 轻得像羽毛，就跟穿上精灵做的裙子时那种轻盈的感觉一样。
ROW CAT:O3cdd39af6e8eee373ebb L1209 * physical_line
  EN: ...not that I would know anything about those!
  ZH:   * ……当然，那些裙子我一点都不了解！

## SC1f2cdbf8d0c95817 | nsfw | datadf/all.ds | AreaC_Prison1.Goodbye
CONTROL L1269  <AreaC_Prison1.Goodbye>
ROW CAT:O943efce4b0c2cb44a72d L1270 * physical_line
  EN: Those Kobo-curs will be mine again!
  ZH:   * 那些科博杂种还会再落到我手里的！

## SCb249d6a43bf9809a | sfw | datadf/all.ds | AreaC_Prison1.Goodbye
CONTROL L1270  <AreaC_Prison1.Goodbye>
ROW SFWc456e1c966f743994af26c5e L1271 - physical_line
  EN: Those space pirates are gonna regret crossing me...
  ZH:   * 那些太空海盗一定会后悔招惹我……

## SCb0171d050ddabc67 | nsfw | datadf/all.ds | AreaC_Prison1.Hello
CONTROL L1266  <AreaC_Prison1.Hello>
ROW CAT:O25790f0aaafe2a6d88ce L1267 * physical_line
  EN: Well, about time. I've been waiting for backup!
  ZH:   * 总算来了。我等增援都等好久了！

## SC5914fe80ff23695a | nsfw | datadf/all.ds | AreaC_Prison1.HelloDog
CONTROL L1275  <AreaC_Prison1.HelloDog>
ROW CAT:Oe4579c0123633130cec8 L1276 * physical_line
  EN: Damn, just a dog.
  ZH:   * 该死，原来只是条狗。

## SC685ffbb7627c1908 | nsfw | datadf/all.ds | AreaC_Prison1.Rescue
CONTROL L1290  <AreaC_Prison1.Rescue>
ROW CAT:O8fc6b223c5141eb8d6d7 L1291 * physical_line
  EN: It's a basic forcefield, girl. Your tazer will make short work of it.
  ZH:   * 这就是个基本款力场，姑娘。你的电击枪一下就能搞定它。

## SC29c980297ec6a92d | nsfw | datadf/all.ds | AreaC_Prison1.TalkAfterRescue.thanks
CONTROL L1303  <AreaC_Prison1.TalkAfterRescue.thanks>
ROW CAT:Oa73c42fea2603dee8258 L1304 * physical_line
  EN: Time for some payback! I'll be queen of the space pirates yet!
  ZH:   * 是时候报仇了！我终会成为太空海盗女王！
ROW CAT:O4fdbaa9075e2b3e63204 L1305 * physical_line
  EN: ...metaphorically. I'm not hanging up my cosmosuit or anything.
  ZH:   * ……只是个比喻。我还没打算把宇宙服挂起来退役呢。

## SCbe1361ac1562509a | sfw | datadf/all.ds | AreaC_Prison1.TalkBeforeRescue.bopped
CONTROL L1300  <AreaC_Prison1.TalkBeforeRescue.bopped>
ROW SFWe37ce00fbf5598e24609ec04 L1301 - physical_line
  EN: Look, as nice as it is to chit-chat... 
  ZH:   * 听着，闲聊虽然不错…… 
ROW SFWf7f5de3f2fc3951ed5235662 L1302 - physical_line
  EN: ...we've both got better things to be doing, right?
  ZH:   * ……可我们都有更要紧的事要做，对吧？

## SC87b461bbd1adbfbf | sfw | datadf/all.ds | AreaC_Prison2.CancelPurchase
CONTROL L1328  <AreaC_Prison2.CancelPurchase>
ROW SFWd8c0b9b2654a3c3fef6fb860 L1329 - physical_line
  EN: Really, no need to bust things up on my account. I'm doing great, eh-heh.
  ZH:   * 真的，没必要为了我砸坏东西。我过得挺好的，诶嘿。

## SC52e382060bd7ecd9 | nsfw | datadf/all.ds | AreaC_Prison2.Goodbye
CONTROL L1309  <AreaC_Prison2.Goodbye>
ROW CAT:O278a162bf93974a7daa9 L1310 * physical_line
  EN: I guess I'll get back to to hangar and start filing my reports...
  ZH:   * 我猜我得回机库去，开始写我的报告了……

## SC84f801d0a564c1c6 | nsfw | datadm/all.ds | AreaC_Prison2.GoodbyeDog
CONTROL L1326  <AreaC_Prison2.GoodbyeDog>
ROW CAT:O325650a974cccfc497cc L1327 * physical_line
  EN: Hhh... hhhf...
  ZH:   * 呼……呼夫……

## SC7388aaddbb0577a5 | sfw | datadm/all.ds | AreaC_Prison2.GoodbyeDog
CONTROL L1321  <AreaC_Prison2.GoodbyeDog>
ROW SFW22a51490079258cd7d69f065 L1322 - physical_line
  EN: Nooo? That's a shame...
  ZH:   * 不——想？真可惜……

## SC9f6764bfb6c96ee1 | sfw | datadf/all.ds | AreaC_Prison2.GoodbyeDog
CONTROL L1322  <AreaC_Prison2.GoodbyeDog>
ROW SFWad27ce4be6fd42df83d0ade2 L1323 - physical_line
  EN: I guess not, huh?
  ZH:   * 看来是不想，是吧？

## SC22f4e48cd7d57dbf | nsfw | datadf/all.ds | AreaC_Prison2.Hello
CONTROL L1306  <AreaC_Prison2.Hello>
ROW CAT:Obe01c048ff1251eecd77 L1307 * physical_line
  EN: Mmmmn... mmmhph <3 Meep!
  ZH:   * 唔嗯……唔姆呼 <3 叽！

## SC35d12e35e6fef0a6 | sfw | datadf/all.ds | AreaC_Prison2.Hello
CONTROL L1307  <AreaC_Prison2.Hello>
ROW SFW3efb9c4d74dc249c26c58c06 L1308 - physical_line
  EN: Oh hey, what brings you here?
  ZH:   * 哦，嗨，你怎么来了？

## SC1571c0f43302ead5 | sfw | datadf/all.ds | AreaC_Prison2.HelloDog
CONTROL L1316  <AreaC_Prison2.HelloDog>
ROW SFW200af80345b089b67e694aa2 L1317 - physical_line
  EN: Heey there doggy.
  ZH:   * 嗨——小狗狗。

## SC7ce014e009234349 | nsfw | datadm/all.ds | AreaC_Prison2.NoBoneForDog
CONTROL L1323  <AreaC_Prison2.NoBoneForDog>
ROW CAT:O17c1d1699643fa19e798 L1324 * physical_line
  EN: Nnnn... hmmph!
  ZH:   * 唔嗯嗯……唔姆夫！

## SCf7a97f8f43eeab37 | sfw | datadf/all.ds | AreaC_Prison2.Rescue
CONTROL L1331  <AreaC_Prison2.Rescue>
ROW SFW3881cd14a54820f2c5661110 L1332 - physical_line
  EN: Really? Do you *have* to bust me out of here?
  ZH:   * 真的？你*非得*把我弄出去吗？

## SC705996558cbc2481 | nsfw | datadf/all.ds | AreaC_Prison2.SoldOut
CONTROL L1336  <AreaC_Prison2.SoldOut>
ROW CAT:O6dcb047d84a99151a558 L1337 * physical_line
  EN: Hmf! You've done quite enough already! Those poor little tentacles...
  ZH:   * 哼！你已经做得够多了！那些可怜的小触手…… 
ROW CAT:O721c792cf9aee13e3ae8 L1338 * physical_line
  EN: So warm and wiggly... eheheh...
  ZH:   * 又暖又扭来扭去……嘿嘿嘿……

## SC71cbd357ce11324a | sfw | datadf/all.ds | AreaC_Prison2.SoldOut
CONTROL L1337  <AreaC_Prison2.SoldOut>
ROW SFWf355319206359b509bbb37b2 L1338 - physical_line
  EN: Yeah yeah, I'll start working on my paperwork...
  ZH:   * 好啦好啦，我会开始处理文书的……

## SC0c01d9127791aee9 | nsfw | datadf/all.ds | AreaC_Prison2.TalkAfterRescue.thanks
CONTROL L1343  <AreaC_Prison2.TalkAfterRescue.thanks>
ROW CAT:Oe45f51d12d707c5b34ca L1344 * physical_line
  EN: Did I look like I was in trouble or something? No way!
  ZH:   * 我看上去像是有麻烦还是怎么的？才没有！
ROW CAT:O539d27b234ddf47f5828 L1345 * physical_line
  EN: These grabby Tutone tentacles are the best! Eh-heh!
  ZH:   * 这些爱乱抓的图托恩触手最棒了！诶嘿！

## SCc545fa7efa5e673c | sfw | datadf/all.ds | AreaC_Prison2.TalkAfterRescue.thanks
CONTROL L1344  <AreaC_Prison2.TalkAfterRescue.thanks>
ROW SFW5c701e8497b4b7a4f2af33a7 L1345 - physical_line
  EN: Did I really look like I was in trouble or something?
  ZH:   * 我看起来真的像遇上麻烦了吗？
ROW SFW5e16dbeec84fc7e753ade5f8 L1346 - physical_line
  EN: Sceafya is really lovely...
  ZH:   * 斯凯菲亚真的很美……

## SC437778e021733d40 | nsfw | datadf/all.ds | AreaC_Prison2.TalkBeforeRescue.bopped
CONTROL L1340  <AreaC_Prison2.TalkBeforeRescue.bopped>
ROW CAT:O00944fd5c67543cc1942 L1341 * physical_line
  EN: Mmmmrff... meep... <3
  ZH:   * 嗯呜呜……吱……<3

## SC74b6351962af668f | sfw | datadm/all.ds | AreaC_Prison3.CancelPurchase
CONTROL L1368  <AreaC_Prison3.CancelPurchase>
CONTROL L1369    if { hasItem(Key) } {
ROW SFW986a6f2d86f9a62c24121d2d L1370 - physical_line
  EN: Are you playing around or something? Cut it out!
  ZH:     * 你是在玩我吗？别闹了！
CONTROL L1371    } else {
ROW SFWce97251649721ca00e25894e L1372 - physical_line
  EN: Cute. But unless you're a master locksmith I think you'll need a key.
  ZH:     * 可爱。但除非你是开锁大师，否则我看你得要钥匙。
CONTROL L1373    }

## SCab49b8b5b73d70f7 | nsfw | datadm/all.ds | AreaC_Prison3.GoodbyeNotRescued
CONTROL L1358  <AreaC_Prison3.GoodbyeNotRescued>
ROW CAT:O30101a45537c5165a064 L1359 * physical_line
  EN: Take your time... us top agents know how to keep our cool.
  ZH:   * 慢慢来……我们这些上位特工最懂得保持冷静。

## SC67bf1ebd88bcfa11 | nsfw | datadm/all.ds | AreaC_Prison3.Purchased
CONTROL L1385  <AreaC_Prison3.Purchased>
ROW CAT:O1df62f2b2459bb5ade17 L1386 * physical_line
  EN: There! N-now I can thank you properly!!
  ZH:   * 好啦！这、这下我可以好好谢谢你了！！

## SCfe805a7703928857 | nsfw | datadf/all.ds | AreaC_Prison3.Purchased
CONTROL L1377  <AreaC_Prison3.Purchased>
ROW CAT:O8016083af5f43fc86df1 L1378 * physical_line
  EN: Ohmygosh thank you!
  ZH:   * 天哪，谢谢你！

## SC8f149add49a8a5b2 | nsfw | datadm/all.ds | AreaC_Prison3.Rescue
CONTROL L1381  <AreaC_Prison3.Rescue>
ROW CAT:Oa599314d9bc0437c136f L1382 * physical_line
  EN: Oh! You're gonna rescue me? I'm looking forward to getting a deep-
  ZH:   * 哦！你要救我？我正盼着被狠狠干——
ROW CAT:Oa89867a85947dbe9b84a L1383 * physical_line
  EN: I mean getting out and d-doing top agent things. F-f-fucking fauna, right!
  ZH:   * 我是说，出去干、干些上位特工该干的事。操、操、操当地生物，对！

## SC4e2f928be3cecc89 | nsfw | datadm/all.ds | AreaC_Prison3.TalkAfterRescue.thanks
CONTROL L1401  <AreaC_Prison3.TalkAfterRescue.thanks>
ROW CAT:O14c3b62414fba7fe5f79 L1402 * physical_line
  EN: Look, I know you're a bottom agent... but can't you make... hff...!
  ZH:   * 我知道你是下位特工……但能不能……呼……！ 
ROW CAT:Od3998e3610b64f563969 L1403 * physical_line
  EN: ...just one little exception? P-punish me I've been a real bad kitty!!
  ZH:   * ……就破一次小例？惩、惩罚我吧，我是只坏猫咪！！

## SC8b239d183bde88dd | sfw | datadm/all.ds | AreaC_Prison3.TalkAfterRescue.thanks
CONTROL L1392  <AreaC_Prison3.TalkAfterRescue.thanks>
ROW SFW4ae7963f6866672756d7662f L1393 - physical_line
  EN: Thanks for rescuing me!
  ZH:   * 谢谢你救了我！

## SC51b737558bc257e4 | nsfw | datadf/all.ds | AreaC_Slaver1.FakeMeat
CONTROL L1438  <AreaC_Slaver1.FakeMeat>
ROW CAT:Of1a1a7123907891803e4 L1439 * physical_line
  EN: Oh? You want to try my special meat?
  ZH:   * 哦？想尝尝我的特制肉？
ROW CAT:O27aecbe4010c8c073ec7 L1440 * physical_line
  EN: Can't say you don't have guts, heh-heh...
  ZH:   * 胆子倒是不小，嘿嘿……

## SC1bf325e240aac02a | nsfw | datadf/all.ds | AreaC_Slaver1.FakeTea
CONTROL L1442  <AreaC_Slaver1.FakeTea>
ROW CAT:Oeb522f1a40b729a4907e L1443 * physical_line
  EN: We boiled it for so long we forgot what it was.
  ZH:   * 我们煮了太久，都忘了它是什么。
ROW CAT:O617612293007ea06214a L1444 * physical_line
  EN: But a little sip never hurt anyone, right?
  ZH:   * 不过喝一小口从来不会伤到谁，对吧？

## SC3e89c6e314b4824c | nsfw | datadm/all.ds | AreaC_Slaver1.Goodbye
CONTROL L1412  <AreaC_Slaver1.Goodbye>
CONTROL L1413    if { !koboCostume() } {
ROW CAT:O8cd9fface0cd854bad44 L1414 * physical_line
  EN: Be seeing you. Heh-heh...
  ZH:     * 回头见。嘿嘿……
CONTROL L1415    } else {
ROW CAT:Od8b6b5b91adf0bec81dd L1416 * physical_line
  EN: Take care out there. Ole Tutone's a rough place these days.
  ZH:     * 出去小心点。如今的图托恩可不太平。
CONTROL L1417    }

## SC3d4954aac281118d | nsfw | datadf/all.ds | AreaC_Slaver1.GoodbyeDog
CONTROL L1471  <AreaC_Slaver1.GoodbyeDog>
ROW CAT:O652a8d6fa344d2eee719 L1472 * physical_line
  EN: Scram, mutt! You're not getting any food from me!
  ZH:   * 滚开，杂种狗！我这儿一点吃的都不会给你！

## SC79a07666505d700f | nsfw | datadm/all.ds | AreaC_Slaver1.GoodbyeDog
CONTROL L1481  <AreaC_Slaver1.GoodbyeDog>
ROW CAT:O96b8198c19f13d0353fe L1482 * physical_line
  EN: Scram, mutt! You're not getting any food from me!
  ZH:   * 滚开，杂种狗！我这儿一点吃的都不会给你！

## SCcb5a13b1b4c21f25 | nsfw | datadm/all.ds | AreaC_Slaver1.Hello
CONTROL L1404  <AreaC_Slaver1.Hello>
CONTROL L1405    if { !koboCostume() } {
ROW CAT:O6ae060dcf8288b352e6c L1406 * physical_line
  EN: Nice night in the forest huh?
  ZH:     * 森林里今晚夜色不错，是吧？ 
ROW CAT:O38c9f0e52f942c44c1f0 L1407 * physical_line
  EN: A fine night to enjoy some fine dining, wouldn't you say?
  ZH:     * 这样的夜晚正适合享用一顿美餐，你说是不是？
CONTROL L1408    } else {
ROW CAT:Od0c8ecf5bbd2d569dc1a L1409 * physical_line
  EN: Well lookee here, a friendly face. Welcome to the black market!
  ZH:     * 哟，瞧瞧这儿，一张友善的面孔。欢迎来到黑市！
CONTROL L1410    }

## SC64b36748fff25fef | sfw | datadf/all.ds | AreaC_Slaver1.Hello
CONTROL L1395  <AreaC_Slaver1.Hello>
CONTROL L1396    if { !koboCostume() } {
ROW SFW20f1507b76fb5058ffaf9af7 L1397 - physical_line
  EN: Nice night in the forest huh? 
  ZH:     * 森林里今晚夜色不错，是吧？ 
ROW SFW5b205e8c18729de2b024a45b L1398 - physical_line
  EN: A fine night to enjoy some fine dining, wouldn't you say?
  ZH:     * 这样的夜晚正适合享用一顿美餐，你说是不是？
CONTROL L1399    } else {
ROW SFW951fa7e30997a4ce1ee28ed6 L1400 - physical_line
  EN: Well lookee here, a friendly face. Welcome to the black market!
  ZH:     * 哟，瞧瞧这儿，一张友善的面孔。欢迎来到黑市！
CONTROL L1401    }

## SCf4a41434b72faab2 | nsfw | datadm/all.ds | AreaC_Slaver1.NoInventorySpace
CONTROL L1439  <AreaC_Slaver1.NoInventorySpace>
ROW CAT:O51f04d3b168fb3dc55b6 L1440 * physical_line
  EN: Hey, you don't even have room for that!
  ZH:   * 喂，你都没地方装这个了！
CONTROL L1442  ### as anthro:

## SCd3f0124bec7a8c00 | nsfw | datadm/all.ds | AreaC_Slaver1.SoldOut
CONTROL L1429  <AreaC_Slaver1.SoldOut>
CONTROL L1430    if { !koboCostume() } {
ROW CAT:O94754bc60610d8cc3c20 L1431 * physical_line
  EN: Just have fun with your trash and leave me be, okay?!
  ZH:     * 你就拿着你的破烂玩去吧，别来烦我，行吗？！
CONTROL L1432    } else {
ROW CAT:O68dfbbb25ca1e51fe1e8 L1433 * physical_line
  EN: Nope, no take-backs! I don't care how much those cards tingle in your pocket.
  ZH:     * 不行，没有反悔这回事！我才不管那些卡在你兜里有多让人发麻。
CONTROL L1434    }

## SCd695aba8ae606a57 | nsfw | datadm/all.ds | AreaC_Slaver1.SpecialPsycards
CONTROL L1463  <AreaC_Slaver1.SpecialPsycards>
ROW CAT:O8a9bf9c9bde3a8051f9e L1464 * physical_line
  EN: Just looks like a deck of weird little cards... right? Think again!
  ZH:   * 看起来不过是一叠古怪的小卡片……对吧？那你可想错了！
ROW CAT:Ofb999141569a415c5627 L1465 * physical_line
  EN: One touch, and you can feel the PSY power leaching off of them.
  ZH:   * 只要碰一下，你就能感觉到精神力正从上面渗出来。
ROW CAT:O241658d4ee05dd7a7012 L1466 * physical_line
  EN: It's said that a skilled ESPer could *use* this power.
  ZH:   * 据说熟练的超能力者能够*使用*这种力量。

## SC6da032e709d7c8fc | nsfw | datadf/all.ds | AreaC_Slaver1.Talk.pirate
CONTROL L1446  <AreaC_Slaver1.Talk.pirate>
CONTROL L1447    if { !koboCostume() } {
ROW CAT:O5aafd560ef846b334166 L1448 * physical_line
  EN: You ever think about becoming a space pirate?
  ZH:     * 你有没有想过成为太空海盗？
ROW CAT:O10bbd773b3f36a154edf L1449 * physical_line
  EN: I know a crew who's lookin' for a cabin-girl, heh-heh...
  ZH:     * 我认识一伙正在找船舱女侍的船员，嘿嘿……
CONTROL L1450    }
CONTROL L1452  ### as kobo:

## SC549e89ef8f0305a6 | nsfw | datadm/all.ds | AreaE_Macsen1.Goodbye
CONTROL L1491  <AreaE_Macsen1.Goodbye>
CONTROL L1492    if { !inCosmoSuit() } {
ROW CAT:Of439de065c0942c71621 L1493 * physical_line
  EN: You're real daring, going out without a spacesuit on!
  ZH:     * 不穿宇航服就往外跑，你胆子可真大！ 
ROW CAT:O2201dab5e96c4590d6ac L1494 * physical_line
  EN: You get 'em, tiger!
  ZH:     * 加油，猛将，去收拾他们吧！
CONTROL L1495    } else {
ROW CAT:O08cf1024dde039b787f3 L1496 * physical_line
  EN: Bye! I'd toast to your health, but I know you can't drink with that helm on!
  ZH:     * 再见！本想举杯祝你健康，可我知道你戴着那头盔没法喝！
CONTROL L1497    }

## SC94bfce801b6b1703 | nsfw | datadm/all.ds | AreaE_Macsen1.Hello
CONTROL L1488  <AreaE_Macsen1.Hello>
ROW CAT:Ob6fec4a35b89f36d9efc L1489 * physical_line
  EN: Whew! What a climb up here huh? Really takes the wind out of ya!
  ZH:   * 呼！爬上来这一趟够呛吧？真是累得人喘不上气！

## SCa77905dd8a62d2c1 | nsfw | datadf/all.ds | AreaE_Macsen1.SpecialGeiger
CONTROL L1489  <AreaE_Macsen1.SpecialGeiger>
ROW CAT:O29eb1359daf5d9a70643 L1490 * physical_line
  EN: Fancy yourself an explorer?
  ZH:   * 觉得自己是个探险家？ 
ROW CAT:O6c6220f6c35aed4b885a L1491 * physical_line
  EN: Then you probably aren't interested in this...
  ZH:   * 那你大概对这东西没兴趣……
ROW CAT:O9e034484640c50762e2d L1492 * physical_line
  EN: This little doohicky will detect anomalies
  ZH:   * 这小玩意儿能探测异常，还能在你的导航地图上标出重要的东西！ 
ROW CAT:Oaeffc17e5b1067de3f38 L1493 * physical_line
  EN: and it'll even mark important things on your Navmap!
  ZH: 
ROW CAT:O15d9941da34cba8e3c7d L1494 * physical_line
  EN: Great for cleaning up all the areas you've been to.
  ZH:   * 用来查漏补缺、扫遍去过的区域再合适不过了。

## SC457bf0e86885490a | sfw | datadf/all.ds | AreaE_Macsen1.SpecialGeiger
CONTROL L1491  <AreaE_Macsen1.SpecialGeiger>
ROW SFW2c71c3ebc7de3f8297a39dce L1492 - physical_line
  EN: Fancy yourself an explorer? 
  ZH:   * 觉得自己是个探险家？ 
ROW SFW04e224bb8f8d9da37b460a7d L1493 - physical_line
  EN: Then you probably aren't interested in this...
  ZH:   * 那你大概对这东西没兴趣……
ROW SFWc765ffa051443f5cb6ab3ca3 L1494 - physical_line
  EN: This little doohicky will detect anomalies 
  ZH:   * 这小玩意儿能探测异常，还能在你的导航地图上标出重要的东西！ 
ROW SFWf5a59f9d7011f052dbd15da8 L1495 - physical_line
  EN: and it'll even mark important things on your Navmap!
  ZH: 
ROW SFW3c571b3b54780a6d910337c5 L1496 - physical_line
  EN: Great for cleaning up all the areas you've been to.
  ZH:   * 用来查漏补缺、扫遍去过的区域再合适不过了。

## SC6f94d186de68761e | nsfw | datadm/all.ds | AreaE_Macsen1.Talk.geiger
CONTROL L1507  <AreaE_Macsen1.Talk.geiger>
ROW CAT:O508c3108bc3d7da43b74 L1508 * physical_line
  EN: Isn't technology great? This new G+RADIO is a radio and anomaly detector...
  ZH:   * 科技真棒，不是吗？这款新G+RADIO既是收音机，也是异常探测器……
ROW CAT:Ob6d5047a5a654a66297b L1509 * physical_line
  EN: ...and it even has a calculator built in!
  ZH:   * ……甚至还内置了计算器！

## SC19794b1831fbbb35 | sfw | datadf/all.ds | AreaE_Macsen1.Talk.mags
CONTROL L1503  <AreaE_Macsen1.Talk.mags>
ROW SFW31c8b89db7e80686324ae472 L1504 - physical_line
  EN: The worst part about all this space walking is having to wear a space suit.
  ZH:   * 太空行走最糟的，就是得穿宇航服。
ROW SFW72869d6f203027ccd0cf0c90 L1505 - physical_line
  EN: It gets my fur all mussed up!
  ZH:   * 弄得我的毛全乱了！
CONTROL L1507  ### shared ###

## SC1171e8673dc5346c | nsfw | datadm/all.ds | AreaH_Cellar.Hello
CONTROL L1552  <AreaH_Cellar.Hello>
CONTROL L1553    if { agentsRescued() == 0 } {
ROW CAT:O7ecc70d544b872b90795 L1554 * physical_line
  EN: Oh hi! Haven't seen one of you cosmo fellas in a while!
  ZH:     * 哦，你好！好久没见到你们这种宇宙来的家伙了！
CONTROL L1555    } else {
ROW CAT:O74b7b5e1b74ad3062fa9 L1556 * physical_line
  EN: Welcome welcome! Bring your appetite! And your Lect!
  ZH:     * 欢迎欢迎！带上你的胃口！还有你的 Lect！
CONTROL L1557    }

## SCb2867bb1d623d8d9 | nsfw | datadf/all.ds | AreaH_Cellar.Purchased
CONTROL L1607  <AreaH_Cellar.Purchased>
ROW CAT:O3e546ea93493e53eec29 L1608 * physical_line
  EN: There you go! Eat up!
  ZH:   * 给你！尽情吃吧！

## SCf3cb45071658dd85 | nsfw | datadm/all.ds | AreaH_Cellar.Talk.food
CONTROL L1572  <AreaH_Cellar.Talk.food>
CONTROL L1573    if { agentsRescued() >= 7 } {
ROW CAT:Oee1a6423fad940ddf5aa L1574 * physical_line
  EN: Heyhey, if it isn't the great hero of Tutone!
  ZH:     * 嘿嘿，这不是图托恩的大英雄嘛！
ROW CAT:O8d1f8140bbd8e7ca6416 L1575 * physical_line
  EN: With all these folks recovering here, business has been booming!
  ZH:     * 有这么多人在这儿养伤，生意红火得很！
ROW CAT:O50b48c497663c3829e1f L1576 * physical_line
  EN: Feel free to buy as much meat as you need, stocks won't run out.
  ZH:     * 想买多少肉尽管买，存货管够。
CONTROL L1577    } else if  { agentsRescued() >= 4 } {
ROW CAT:Od7044a0c1ae7973b5d5b L1578 * physical_line
  EN: Starting to get lively in here, isn't it?
  ZH:     * 这儿总算开始热闹起来了，对吧？
ROW CAT:O824e1d0b9066865a0f9e L1579 * physical_line
  EN: I keep bringing in food, and you fellas keep on eating it up!
  ZH:     * 我一批批把吃的运进来，你们这帮家伙就一个劲地吃光！
ROW CAT:O6d86f27af6509179c659 L1580 * physical_line
  EN: Almost makes me think that I should bring in some of the GOOD stuff...
  ZH:     * 都快让我觉得该进点“好东西”了……
CONTROL L1581    } else if { agentsRescued() >= 1 } {
ROW CAT:O86d4af3d1d1635711971 L1582 * physical_line
  EN: There's not much reason to stock a lot of food right now
  ZH:     * 眼下没什么理由囤太多吃的
ROW CAT:O6c0936331a36d1037d06 L1583 * physical_line
  EN: But you know, if there were more folks resting up in this hangar
  ZH:     * 可你知道，要是这机库里多些人休整，我倒也许该多运些补给进来……
ROW CAT:Ob6afe740f167fd7e3e3f L1584 * physical_line
  EN: I could probably stand to bring in more provisions...
  ZH: 
CONTROL L1585    } else {
ROW CAT:Oa77aae8b9823089a86a1 L1586 * physical_line
  EN: It's been so long since I saw another one of you agent sorts here
  ZH:     * 我好久没在这儿见到你们这种探员了，连存货都没顾上补！
ROW CAT:Oc0803f24a73d4c835aab L1587 * physical_line
  EN: that I haven't even kept the stocks up!
  ZH: 
ROW CAT:Oceff5521dc2d286eb105 L1588 * physical_line
  EN: Maybe if there were folks to eat the food, I could bring some in...
  ZH:     * 要是有谁来吃这些东西，也许我就能进些货……
CONTROL L1589    }
CONTROL L1591  ### shared ###

## SC57698af9183051b1 | sfw | datadf/all.ds | AreaH_Cellar.Talk.food
CONTROL L1564  <AreaH_Cellar.Talk.food>
CONTROL L1565    if { agentsRescued() >= 7 } {
ROW SFW4541a8f19be88ae33c4e0a07 L1566 - physical_line
  EN: Heyhey, if it isn't the great hero of Tutone!
  ZH:     * 嘿嘿，这不是图托恩的大英雄嘛！
ROW SFW0d994c6c378d44377e9fe222 L1567 - physical_line
  EN: With all these folks recovering here, business has been booming!
  ZH:     * 有这么多人在这一带养伤，生意可真是红火！
ROW SFW23856b4de134a3b507b6cd7e L1568 - physical_line
  EN: Feel free to buy as much meat as you need, stocks won't run out.
  ZH:     * 想买多少肉尽管买，存货管够。
CONTROL L1569    } else if  { agentsRescued() >= 4 } {
ROW SFWbebee97d4b8b66c3cb374666 L1570 - physical_line
  EN: Starting to get lively in here, isn't it?
  ZH:     * 这儿开始热闹起来了，是吧？
ROW SFWeedd0790e43fe13f1247235f L1571 - physical_line
  EN: I keep bringing in food, and you fellas keep on eating it up!
  ZH:     * 我一批批把吃的运进来，你们这帮家伙就一个劲地吃光！
ROW SFW7db8859d06fc6d63dd7a8913 L1572 - physical_line
  EN: Almost makes me think that I should bring in some of the GOOD stuff...
  ZH:     * 都快让我觉得该进点“好东西”了……
CONTROL L1573    } else if { agentsRescued() >= 1 } {
ROW SFW4112ad830ab1d820e47c3c40 L1574 - physical_line
  EN: There's not much reason to stock a lot of food right now
  ZH:     * 眼下没什么理由囤太多吃的
ROW SFW35ec48acd2ffafc0a18fe02a L1575 - physical_line
  EN: But you know, if there were more folks resting up in this hangar
  ZH:     * 不过你知道，要是这机库里歇着的人再多些，我倒也许该多运些补给进来……
ROW SFWfd4a8e042507b38b7310f24c L1576 - physical_line
  EN: I could probably stand to bring in more provisions...
  ZH: 
CONTROL L1577    } else {
ROW SFWf36a73288b6064869cf953a0 L1578 - physical_line
  EN: It's been so long since I saw another one of you agent sorts here
  ZH:     * 我已经很久没在这儿见到你们这种特工了，连存货都没顾上补！
ROW SFW7ccb543843ac015f276ebb48 L1579 - physical_line
  EN: that I haven't even kept the stocks up! 
  ZH: 
ROW SFW1a8eb9a424b424116983dfc0 L1580 - physical_line
  EN: Maybe if there were folks to eat the food, I could bring some in...
  ZH:     * 要是有谁来吃这些东西，也许我就能进些货……
CONTROL L1581    }
CONTROL L1583  ### shared ###

## SC5f726caaf3a153c4 | nsfw | datadm/all.ds | AreaH_Cellar.VitDrumstick
CONTROL L1562  <AreaH_Cellar.VitDrumstick>
ROW CAT:O90db81a9c69d07126d68 L1563 * physical_line
  EN: Fried to perfection, this little snack will fill you with vigor!
  ZH:   * 这份小吃炸得恰到好处，吃了让你活力满满！ 

## SC72f69b25755789ac | nsfw | datadf/all.ds | AreaH_Cellar.VitDrumstick
CONTROL L1552  <AreaH_Cellar.VitDrumstick>
ROW CAT:Oe4cb5b832c97bbb18648 L1553 * physical_line
  EN: Fried to perfection, this little snack will fill you with vigor!
  ZH:   * 这份小吃炸得恰到好处，吃了让你活力满满！ 

## SCde46c970601e89d8 | nsfw | datadm/all.ds | AreaH_Cellar.VitHam
CONTROL L1569  <AreaH_Cellar.VitHam>
ROW CAT:Ob96f8babfe60600291a7 L1570 * physical_line
  EN: Just look at this thick and meaty shank! Juicy and VIT-filling!
  ZH:   * 瞧瞧这粗壮又多肉的腿肉！鲜嫩多汁，还能补充活力！

## SCad64b28a0cedd27b | nsfw | datadm/all.ds | AreaH_MacsenBar.PsyUp
CONTROL L1634  <AreaH_MacsenBar.PsyUp>
ROW CAT:O9992e3e4101f38c796ef L1635 * physical_line
  EN: You come across any of these crazy crystals out there in the world?
  ZH:   * 你在外头见过这种神奇的水晶吗？
ROW CAT:O7e40c606ea76f3661a46 L1636 * physical_line
  EN: They say that if an Esper gets one of these, it'd boost their psychic capacity
  ZH:   * 听说超能力者得到一颗，就能提升灵能容量，可我只是条普通的狗，这东西对我没用。送你吧！
ROW CAT:Ofb304d3d592419548b0b L1637 * physical_line
  EN: but I'm just a simple dog, so it does nothing for me. You can have it!
  ZH: 

## SCbc27a3526ff2c7f8 | nsfw | datadf/all.ds | AreaH_MacsenBar.Purchased
CONTROL L1681  <AreaH_MacsenBar.Purchased>
ROW CAT:O7075fc02783b3a9b9ab3 L1682 * physical_line
  EN: There you go pal. You deserve it!
  ZH:   * 拿好了，伙计。这是你应得的！

## SC8cf80b11c314c9d0 | nsfw | datadm/all.ds | AreaH_MacsenBar.Talk.bar1
CONTROL L1657  <AreaH_MacsenBar.Talk.bar1>
ROW CAT:O14f390396f907ab8f645 L1658 * physical_line
  EN: Sure are a lot of agents to rescue out there, huh?
  ZH:   * 外面要救的特工可真不少，是吧？
ROW CAT:O9013c473af08f2b497d5 L1659 * physical_line
  EN: Come back here after you've saved a bunch of 'em
  ZH:   * 等你救了一大批他们之后再回到这儿，我就给你一点那个那个……嘿！嘿！嘿！
ROW CAT:O8798999d2b008e52b3d2 L1660 * physical_line
  EN: and I'll give you a little somethin somethin... He!He!He!
  ZH: 

## SCcc40787614a1caeb | nsfw | datadm/all.ds | AreaH_MacsenBar.Talk.zener1
CONTROL L1650  <AreaH_MacsenBar.Talk.zener1>
ROW CAT:O866ff48af41105fc79e5 L1651 * physical_line
  EN: You ever hear about these ol' PSY powers that some folks be gettin' these days?
  ZH:   * 听说过最近有些人得到的那些精神力异能没？
ROW CAT:O89669b33c2c692503517 L1652 * physical_line
  EN: The say Triangle powers will boost your defense while lowering your attack a bit
  ZH:   * 听说三角能力能增强防御，不过攻击会稍微降低，而十字之力则刚好相反！挨打更疼，打人也更疼！
ROW CAT:Odca9d53dc18371e4cb29 L1653 * physical_line
  EN: while a Cross power will do the opposite! Take AND deal more damage!
  ZH: 
ROW CAT:Of9a7e83ad29e530cf2c5 L1654 * physical_line
  EN: Not only that, but they say... they say...
  ZH:   * 不止如此，他们还说……还说……
ROW CAT:Oa16d5f3a2c89893c6755 L1655 * physical_line
  EN: ...nevermind, I forgot what they say about the other powers...
  ZH:   * ……算了，其他能力的传闻我给忘了……

## SCd72de44a1c956936 | nsfw | datadf/all.ds | AreaH_MacsenBreeding.Goodbye
CONTROL L1695  <AreaH_MacsenBreeding.Goodbye>
ROW CAT:O7bca5b486fc99154d1ab L1696 * physical_line
  EN: BYE-OH! DON'T FORGET TO COME OFTEN!
  ZH:   * 拜拜！别忘了常来啊！

## SCeb32d4e75518d767 | nsfw | datadm/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1723  <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1724    if { !f(ctx_maxed_any_pet_affinity) } {
ROW CAT:Oa31868bc6212a6162810 L1725 * physical_line
  EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
  ZH:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW CAT:O08e4dfd7a28b6e81c731 L1726 * physical_line
  EN: AFTER YOU'VE MAXXXED OUT AN AFFINITY, RETURN HERE FOR A SPECIAL REWARD.
  ZH:     * 把一只宠物的亲密度培养到最高后，就回来领一份特别奖励吧。
CONTROL L1727    } else {
ROW CAT:Oe433a6739244906e438f L1728 * physical_line
  EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
  ZH:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW CAT:O2bc73708db965c04f1ef L1729 * physical_line
  EN: JUST PET THEM WHILE THEY'RE AT MAX AFFINITY TO CHARGE THE CRYSTAL.
  ZH:     * 只要在它们亲密度满了的时候抚摸它们，就能给水晶充能。
ROW CAT:Occ847a03a1c84f586059 L1730 * physical_line
  EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
  ZH:     * 每种生物给的力量都不同！都试试！
CONTROL L1731    }
CONTROL L1733  ### shared ###

## SC7e22fbb58bd67e8e | nsfw | datadf/all.ds | AreaH_MacsenBreeding.TazerTrainee
CONTROL L1704  <AreaH_MacsenBreeding.TazerTrainee>
ROW CAT:Oeef64260784606b65585 L1705 * physical_line
  EN: NOT INTERESTED IN CAPTURING CREATURES? SURE, WE CAN TRADE BACK.
  ZH:   * 对捕捉生物没兴趣？没问题，我们可以换回来。
ROW CAT:O413c60b8305a9c1b0f00 L1706 * physical_line
  EN: YOU'RE WELCOME TO GET THE TRAINER TAZER AGAIN LATER, OF COURSE!
  ZH:   * 当然，以后想再拿驯兽电击枪，随时欢迎！

## SC24aaa72712a48cf2 | nsfw | datadf/all.ds | AreaH_MacsenMechanic.Talk.PartHints2
CONTROL L1802  <AreaH_MacsenMechanic.Talk.PartHints2>
CONTROL L1803    if { f(ClassicStarkillV3_defeated) && (!hasItem(ShipGun) || !hasItem(ShipShield) || !hasItem(ShipRadar) || !hasItem(ShipTurbo)) } {
ROW CAT:Oc68de71fd92f6853a431 L1804 * physical_line
  EN: Don't worry about memorizing what I just told ya...
  ZH:     * 别费劲记我刚才说的那些……
ROW CAT:Od9b0d4e27e115cf88f52 L1805 * physical_line
  EN: ...I marked it on your Navmap already! Go check it out!
  ZH:     * ……我已经在你的导航地图上标好了！去看看吧！
CONTROL L1806    }
CONTROL L1808  ### shared ###

## SCa5849f3f71d4d180 | nsfw | datadf/all.ds | AreaX_Upgrade.CancelPurchase
CONTROL L1901  <AreaX_Upgrade.CancelPurchase>
ROW CAT:Oc1241c8ab4cf4fb5b8f5 L1902 * physical_line
  EN: Are you worried about voiding the warranty? Pft.
  ZH:   * 你是担心会让保修失效吗？噗。
ROW CAT:O5ae0a4860a2e451d34de L1903 * physical_line
  EN: Oh well. Have you got something else for me to work on?
  ZH:   * 算了。你还有别的活儿要我干吗？

## SC3d8c2d95212ec4b0 | nsfw | datadf/all.ds | AreaX_Upgrade.GoodbyeDog
CONTROL L1882  <AreaX_Upgrade.GoodbyeDog>
ROW CAT:O4c32ac6036e91fbfce05 L1883 * physical_line
  EN: Hey! Where are you going ducky?! We've got refactoring to do!
  ZH:   * 嘿！你要去哪儿啊，小鸭鸭？！咱们还有重构要做呢！

## SC0ad0638f9309545b | nsfw | datadf/all.ds | AreaX_Upgrade.Hack
CONTROL L1916  <AreaX_Upgrade.Hack>
ROW CAT:O630ffcbe9d33fd52e291 L1917 * physical_line
  EN: I see you've been having some real trouble finding those chips.
  ZH:   * 我看你找那些芯片可真是费了不少劲。
ROW CAT:Oa38c558339cfdbe3494a L1918 * physical_line
  EN: Fortunately, I've got a solution... well, I think!
  ZH:   * 幸好我有个办法……嗯，我觉得有！
ROW CAT:Odb8b5f415c2c145670cb L1919 * physical_line
  EN: With my novel algorithms - and the energy afforded by this site - I believe
  ZH:   * 凭我新颖的算法——以及此地供给的能量——我相信我能侵入驱动我们这个现实的模拟程序……
ROW CAT:Od7296f7f11e0489fae39 L1920 * physical_line
  EN: I can hack into the simulation that drives our very reality...
  ZH: 
ROW CAT:Oc6bad5d530db7e878c60 L1921 * physical_line
  EN: Then we could have all the chips we'd ever need, with no downsides probably!
  ZH:   * 那样我们就有永远用不完的芯片了，而且大概没有任何坏处！
ROW CAT:Ocfb401d1a45ab364e639 L1922 * physical_line
  EN: How about it? Wanna try?! Let's hack the world!
  ZH:   * 怎么样？想试试？！我们来黑掉这个世界吧！

## SCea91795e500c65d8 | nsfw | datadf/all.ds | AreaX_Upgrade.HelloDog
CONTROL L1878  <AreaX_Upgrade.HelloDog>
ROW CAT:Oddee19ec1313e54a2939 L1879 * physical_line
  EN: Hello there Mr. Puppy! Do you want to be my rubber ducky?
  ZH:   * 你好呀，小狗先生！你想当我的橡皮鸭吗？
ROW CAT:Od45b315bf866912aea4e L1880 * physical_line
  EN: All you have do is stay here and listen to me talk about computers all day!
  ZH:   * 你只要待在这里，听我一整天聊电脑就行！

## SCc950a3108960769a | nsfw | datadm/all.ds | AreaX_Upgrade.HelloKobo
CONTROL L1896  <AreaX_Upgrade.HelloKobo>
ROW CAT:O4868ec1e60e4cca42e31 L1897 * physical_line
  EN: Are you delivering my weekly supplies? I still have some leftover.
  ZH:   * 你是来送我这周的补给的吗？我还剩下一些。
ROW CAT:Oe34ef1d6568b07d8d33b L1898 * physical_line
  EN: Since last cycle, I've been increasing my efficiency coefficient while usin-
  ZH:   * 从上个周期起，我一直在提高自己的效率系数，同时用——

## SCecea8ac84823cd0b | nsfw | datadf/all.ds | AreaX_Upgrade.Purchased
CONTROL L1892  <AreaX_Upgrade.Purchased>
CONTROL L1893    if { f(ctx_hack_the_world) } {
ROW CAT:Ofcd23485194d3c83589c L1894 * physical_line
  EN: Huh... nothing happened? I'm sure I debugged everything.
  ZH:     * 咦……什么都没发生？我确定我把所有东西都调试过了。 
ROW CAT:O1ea7bfca28361941d784 L1895 * physical_line
  EN: Maybe reality isn't actually a simulation after all...?
  ZH:     * 也许现实其实并不是模拟出来的……？
CONTROL L1896    } else {
ROW CAT:Oeb0b4ed15cd1ff7ca676 L1897 * physical_line
  EN: According to my calculations, your tazer should be fully repaired!
  ZH:     * 根据我的计算，你的电击枪应该已经完全修好了！
ROW CAT:O27be5a939af12dc02160 L1898 * physical_line
  EN: With a few modifications by yours truly, probably better than it ever was, in fact!
  ZH:     * 加上我亲自做的改动，说不定比原来更好用！ 
CONTROL L1899    }

## SC633463ad4a008015 | sfw | datadm/all.ds | AreaX_Upgrade.Purchased
CONTROL L1893  <AreaX_Upgrade.Purchased>
CONTROL L1894    if { f(ctx_hack_the_world) } {
ROW SFW9f95683c7f05bed8157170c5 L1895 - physical_line
  EN: Huh... nothing happened? I'm sure I debugged everything. 
  ZH:     * 咦……什么都没发生？我确定我把所有东西都调试过了。 
ROW SFW6e31955bffa34868dc25ef67 L1896 - physical_line
  EN: Maybe reality isn't actually a simulation after all...?
  ZH:     * 也许现实其实并不是模拟出来的……？
CONTROL L1897    } else {
ROW SFWc7001bbcd48c36d29b5f5759 L1898 - physical_line
  EN: According to my calculations, your tazer should be fully repaired!
  ZH:     * 按我的计算，你的电击枪应该完全修好了！
ROW SFW020953c28f50d68722a0477c L1899 - physical_line
  EN: With a few modifications by yours truly, probably better than it ever was, in fact! 
  ZH:     * 加上我亲自做的改动，说不定比原来更好用！ 
CONTROL L1900    }

## SC399fdb296cc4b547 | nsfw | datadm/all.ds | AreaX_Upgrade.SoldOut
CONTROL L1916  <AreaX_Upgrade.SoldOut>
CONTROL L1917    if { f(ctx_hack_e_hack) } {
ROW CAT:Od238cda1b5d19ebe507b L1918 * physical_line
  EN: That should have worked! I'm sure of it!!
  ZH:     * 那本该起作用的！我很确定！！
ROW CAT:Oc5f105c02d8b0f1f3493 L1919 * physical_line
  EN: I'll need to run more simulations before we try again!
  ZH:     * 在我们再试一次之前，我得先跑更多模拟！
ROW CAT:Ocaafa3b59093cce77749 L1920 * physical_line
  EN: Hang tight, this should only take two more weeks...
  ZH:     * 再撑一下，这应该只需要再多两个星期……
CONTROL L1921    } else {
ROW CAT:O6789be1e4b5066ca1268 L1922 * physical_line
  EN: Hey wait! I already fixed that for you!
  ZH:     * 嘿，等等！我已经帮你修好了！
ROW CAT:O01671fc68cf777f4f96a L1923 * physical_line
  EN: If I overclock it any more it'll probably catch fire...
  ZH:     * 如果我再继续超频，它大概会着火……
ROW CAT:Oe18eab18043ba970f99d L1924 * physical_line
  EN: How about we do something else?
  ZH:     * 我们做点别的怎么样？
CONTROL L1925    }

## SC591eb00fae1bff09 | nsfw | datadm/all.ds | AreaX_Upgrade.Talk.macsen
CONTROL L1951  <AreaX_Upgrade.Talk.macsen>
CONTROL L1952    if { !f(upgraded_TazerAttuned) } {
ROW CAT:Ofe566435840d96c41214 L1953 * physical_line
  EN: Have you found all the Chips laying around yet?
  ZH:     * 你找到散落各处的芯片了吗？
ROW CAT:O29fa4538badffb15c3d6 L1954 * physical_line
  EN: We'll need all of them in order to get this repair bay working again!
  ZH:     * 要让这间维修舱重新运转，就得集齐全部！
ROW CAT:O2a77eb9960149193faf0 L1955 * physical_line
  EN: If you need help finding more Chips, there's a weird old dog in the area
  ZH:     * 如果你需要帮忙找更多芯片，这一带有一只奇怪的老狗，他卖一件挺不错的装备，能帮你找到它们！
ROW CAT:O8ce87b1a95d71f4cbd12 L1956 * physical_line
  EN: that sells a neat piece of gear that will help you find them!
  ZH: 
CONTROL L1957    }

## SC5a6089db81efd081 | nsfw | datadm/all.ds | AreaX_Upgrade.Talk.repair
CONTROL L1945  <AreaX_Upgrade.Talk.repair>
CONTROL L1946    if { !f(upgraded_TazerAttuned) } {
ROW CAT:Od93205c4a8f35bb9371a L1947 * physical_line
  EN: If you collect enough chips, I could hack into the power grid and get this
  ZH:     * 只要你收集到足够的芯片，我就能侵入电网，让这个维修区重新上线。
ROW CAT:O3270d81509a41c67d980 L1948 * physical_line
  EN: repair bay back online.
  ZH: 
CONTROL L1949    }

## SCf340f0808e10d1fd | nsfw | datadf/all.ds | Fenfen_Shared.Goodbye
CONTROL L4954  <Fenfen_Shared.Goodbye>
ROW CAT:O3a6a7120c1b1eff8a30b L4955 Anon/Fox physical_line
  EN: Thank you Yiffany!
  ZH:   Anon/Fox: 谢谢你，伊吠妮！

## SCf84d3bb202657af6 | nsfw | datadm/all.ds | Gitgud.Tip4
CONTROL L3379  <Gitgud.Tip4>
ROW CAT:O67cb49b4b543286535dc L3380 Gitgud physical_line
  EN: [THE TORCHES THAT LINE THE WALLS CAN BE BROKEN]
  ZH:     Gitgud: [沿着墙壁排列的火把可以被打破，里面可能还有一点零钱！]
ROW CAT:O582bb100de53aed53565 L3381 Gitgud physical_line
  EN: [AND MAY HAVE A LITTLE POCKET CHANGE IN THEM!]
  ZH: 

## SCafde0627f237c71b | nsfw | datadm/all.ds | Gitgud.Tip5
CONTROL L3383  <Gitgud.Tip5>
ROW CAT:O43b67813f33e30d505ed L3384 Gitgud physical_line
  EN: [MANY ENEMIES GET STUNNED WHEN THE LIGHTTAZER STRIKES]
  ZH:     Gitgud: [许多敌人在光电击枪击中时会眩晕，这给了你跳开躲避的机会！]
ROW CAT:Oa1eb9ec9987d7ee2eac9 L3385 Gitgud physical_line
  EN: [WHICH GIVES YOU A CHANCE TO JUMP OUT OF THE WAY!]
  ZH: 

## SC46e420c31949af46 | nsfw | datadm/all.ds | Hacker_Shared.GoodbyeKobo
CONTROL L4992  <Hacker_Shared.GoodbyeKobo>
ROW CAT:Oab7f66dedbe5b9026fe6 L4993 * physical_line
  EN: -wait a sec, you're not the delivery guy! G-get out of here right now!
  ZH:   * -等等，你可不是送货那家伙！快、快给我出去！

## SC2d46d51e72d017b5 | nsfw | datadm/all.ds | Hacker_Shared.Hello
CONTROL L4975  <Hacker_Shared.Hello>
ROW CAT:Oedf94bd2b832b045f725 L4976 * physical_line
  EN: Heya Yiffai! How can I help you?
  ZH:   * 嘿，伊吠！有什么我能帮你的吗？

## SC12eb80f200f666ee | nsfw | datadm/all.ds | Hacker_Shared.HelloDog
CONTROL L4981  <Hacker_Shared.HelloDog>
ROW CAT:Oa956e2aa101fa4e2f74f L4982 * physical_line
  EN: Hello there Mr. Puppy! Do you want to be my rubber ducky?
  ZH:   * 你好呀，小狗先生！你想当我的橡皮鸭吗？
ROW CAT:O7207a0da26875e8f41f9 L4983 * physical_line
  EN: All you have do is stay here and listen to me talk about computers all day!
  ZH:   * 你只要待在这里，听我一整天聊电脑就行！

## SCd82b908104a6769d | nsfw | datadf/all.ds | Hacker_Shared.HelloKobo
CONTROL L4975  <Hacker_Shared.HelloKobo>
ROW CAT:O8ac5a246ef27a80407c8 L4976 * physical_line
  EN: Are you delivering my weekly supplies? I still have some leftover.
  ZH:   * 你是来送每周补给的？我还剩着一些呢。
ROW CAT:O79af4020e60d1e37bbd6 L4977 * physical_line
  EN: Since last cycle, I've been increasing my efficiency coefficient while usin-
  ZH:   * 从上个周期起，我一直在提高自己的效率系数，同时用——

## SC211bc1be6ae9bdc8 | nsfw | datadf/all.ds | Hacker_Shared.NotEnoughMoney
CONTROL L4994  <Hacker_Shared.NotEnoughMoney>
ROW CAT:O024569be401e75294fef L4995 * physical_line
  EN: Hey, wait a minute! You don't have enough components for this!
  ZH:   * 嘿，等一下！你的零件不够做这个！
ROW CAT:O7c5521b033619a01c7f4 L4996 * physical_line
  EN: I need isolinear modules pushing at least 400 terahertz.
  ZH:   * 我需要至少能跑到 400 太赫兹的等线性模块。
ROW CAT:O8d2f27bc0851234d01d9 L4997 * physical_line
  EN: Anything else is basically too slow to even bother with!
  ZH:   * 别的基本上太慢了，根本不值得一试！

## SC32064e45f3fb1d25 | nsfw | datadm/all.ds | Hacker_Shared.NotEnoughMoney
CONTROL L5007  <Hacker_Shared.NotEnoughMoney>
ROW CAT:O147c86ff0f7d0b00a9f2 L5008 * physical_line
  EN: Hey, wait a minute! You don't have enough components for this!
  ZH:   * 嘿，等一下！你的零件不够做这个！
ROW CAT:O5431e9d8146c133d8695 L5009 * physical_line
  EN: I need isolinear modules pushing at least 400 terahertz.
  ZH:   * 我需要至少能跑到 400 太赫兹的等线性模块。
ROW CAT:Oab6e9e73b99ae574d844 L5010 * physical_line
  EN: Anything else is basically too slow to even bother with!
  ZH:   * 别的基本上太慢了，根本不值得一试！

## SC232acede06e1de92 | nsfw | datadm/all.ds | Hacker_Shared.Talk.hacking
CONTROL L5012  <Hacker_Shared.Talk.hacking>
ROW CAT:Of57734021f97f5c21ff0 L5013 * physical_line
  EN: These cyber doors around here are really fun to hack!
  ZH:   * 这附近的赛博门黑起来可真有意思！
ROW CAT:O7e384b92f489d11924a7 L5014 * physical_line
  EN: If you can furnish the requisite components, I'll open them right up!
  ZH:   * 只要你能提供所需的部件，我就立刻把它们打开！

## SC335be8df2d84a059 | nsfw | datadf/all.ds | Hacker_Shared.Talk.radio
CONTROL L5003  <Hacker_Shared.Talk.radio>
ROW CAT:O65b69f700a1fce04b353 L5004 * physical_line
  EN: Call me at frequency 28.250 if you need help finding those chips!
  ZH:   * 如果你需要帮忙找那些芯片，就用频率28.250呼我！

## SC516d28e0e0aff161 | nsfw | datadm/all.ds | Macsen_Shared.BoneTheDog
CONTROL L5024  <Macsen_Shared.BoneTheDog>
ROW CAT:O7d3247ee805000bed025 L5025 * physical_line
  EN: Do you want my bone, boy? Do ya?
  ZH:   * 想要我的骨头吗，小子？想不想要？

## SCef43a2a04b38a0be | nsfw | datadm/all.ds | Macsen_Shared.CancelPurchase
CONTROL L5048  <Macsen_Shared.CancelPurchase>
ROW CAT:O315c061dc2d67b97ad18 L5049 * physical_line
  EN: That's a shame. Anything else?
  ZH:   * 真遗憾。还要点别的吗？

## SCbabfb46165e93b18 | nsfw | datadf/all.ds | Macsen_Shared.GoodbyeKobo
CONTROL L5026  <Macsen_Shared.GoodbyeKobo>
ROW CAT:O77fc23b781d7eb81b9ff L5027 * physical_line
  EN: Don't come back! I've got my eye on you!
  ZH:   * 别再来了！我可盯着你呢！

## SC39f3ab9d9aaab103 | nsfw | datadm/all.ds | Macsen_Shared.HelloKobo
CONTROL L5035  <Macsen_Shared.HelloKobo>
ROW CAT:Ob3338343ef01e7367414 L5036 * physical_line
  EN: Hmph! What do you want?
  ZH:   * 哼！你有什么事？
ROW CAT:O732c9ed047f04b694d7c L5037 * physical_line
  EN: Lot of nerve showing your face around here, slaver scoundrel!
  ZH:   * 你还有脸在这儿露面，奴隶贩子恶棍！

## SCd165ff4b07b0a7a8 | nsfw | datadf/all.ds | Macsen_Shared.NoRockForKobo
CONTROL L5029  <Macsen_Shared.NoRockForKobo>
ROW CAT:Of60e8054ab504d14b310 L5030 * physical_line
  EN: Hmph! What do you want?
  ZH:   * 哼！你想干什么？
ROW CAT:Odcb0a89f2d4b096f0bac L5031 * physical_line
  EN: Lot of nerve showing your face around here, slaver scoundrel!
  ZH:   * 亏你还敢在这儿露面，奴隶贩子混蛋！
ROW CAT:Ob5881fc79e24714d44e6 L5032 * physical_line
  EN: Hey, wait a minute... you're just trying to get free rocks, aren't you?!
  ZH:   * 嘿，等一下……你只是想白拿石头，对吧？！
ROW CAT:O14663ddad6d330208e1e L5033 * physical_line
  EN: Get out, and don't come back!
  ZH:   * 滚出去，别再回来！

## SCb65b9de624dc4e18 | nsfw | datadf/all.ds | Macsen_Shared.Purchased
CONTROL L5038  <Macsen_Shared.Purchased>
ROW CAT:O209e7f649fb123056aac L5039 * physical_line
  EN: Thanks a million! Anything else?
  ZH:   * 太谢谢你了！还要点别的吗？

## SCe88313d5428701e1 | nsfw | datadm/all.ds | Prison_Shared.NoKobo
CONTROL L5065  <Prison_Shared.NoKobo>
ROW CAT:Oc68abc180b47bd3dc245 L5066 * physical_line
  EN: Darn it! I'm in a tough enough spot as it is!
  ZH:   * 真是的！我的处境已经够艰难了！
ROW CAT:O2d7703f19b40aeb838b0 L5067 * physical_line
  EN: The last thing I need to deal with is a darn kobold all of a sudden!
  ZH:   * 我最不想应付的，就是突然冒出一只该死的科博德！
ROW CAT:O87dfb5cac9d6d89ef653 L5068 * physical_line
  EN: Shoo! Go on! Get out!
  ZH:   * 走开！快走！出去！

## SC88e6c7d9ad704dbc | nsfw | datadm/all.ds | Proto_Fenfen.CancelPurchase
CONTROL L5087  <Proto_Fenfen.CancelPurchase>
ROW CAT:Oe4df87b8f29db36a101d L5088 Anon/Fox physical_line
  EN: Hey, help a placeholder out here!
  ZH:   Anon/Fox: 嘿，帮这个占位角色一把吧！

## SC8ddd5b852c9ac63a | nsfw | datadf/all.ds | Proto_Fenfen.CancelPurchase
CONTROL L5074  <Proto_Fenfen.CancelPurchase>
ROW CAT:O4e71ec81f61c14ef7722 L5075 Anon/Fox physical_line
  EN: Hey, help a placeholder out here!
  ZH:   Anon/Fox: 嘿，帮帮这个占位角色啊！

## SC72e6afa168a4013c | nsfw | datadf/all.ds | Proto_Fenfen.GoodbyeNotRescued
CONTROL L5062  <Proto_Fenfen.GoodbyeNotRescued>
ROW CAT:O5669ef3eaf4e1abc5176 L5063 Anon/Fox physical_line
  EN: Please come back soon!
  ZH:   Anon/Fox: 请早点回来！

## SC4f524de93b3ad858 | nsfw | datadm/all.ds | Proto_Fenfen.Hello
CONTROL L5069  <Proto_Fenfen.Hello>
ROW CAT:O4eb0e6988404e14e1100 L5070 Anon/Fox physical_line
  EN: Help, I'm trapped in here!
  ZH:   Anon/Fox: 救命，我被困在这儿了！

## SCd91f729fa2d8831c | nsfw | datadf/all.ds | Proto_Fenfen.NoBoneForDog
CONTROL L5068  <Proto_Fenfen.NoBoneForDog>
ROW CAT:O0be0eda1b895c993aec8 L5069 Anon/Fox physical_line
  EN: Can you get your master to come and help me?
  ZH:   Anon/Fox: 你能让你的主人过来帮我吗？

## SC562e5f9f3361b7b0 | nsfw | datadm/all.ds | Proto_PrisonKey.GoodbyeDog
CONTROL L5119  <Proto_PrisonKey.GoodbyeDog>
ROW CAT:Oc6ccaf3b420300204ea4 L5120 * physical_line
  EN: Please come back soon with your master, and a key!
  ZH:   * 请早点带着你的主人和一把钥匙回来！

## SC7764fe7d22e5d659 | nsfw | datadm/all.ds | Proto_PrisonKey.NoBoneForDog
CONTROL L5116  <Proto_PrisonKey.NoBoneForDog>
ROW CAT:O4e274ab5c33c5fd098b7 L5117 * physical_line
  EN: Can you get your master to come back with a key? I'm locked up in here!
  ZH:   * 你能让你的主人带着钥匙回来吗？我被锁在这里面了！

## SCa36279a5637f3fb2 | nsfw | datadf/all.ds | Proto_PrisonKey.NoBoneForDog
CONTROL L5103  <Proto_PrisonKey.NoBoneForDog>
ROW CAT:O36bc0d784f0444b890c3 L5104 * physical_line
  EN: Can you get your master to come back with a key? I'm locked up in here!
  ZH:   * 你能让你的主人带着钥匙回来吗？我被锁在这里面了！

## SCd057c69030799dfe | nsfw | datadf/all.ds | Proto_PrisonKey.Rescue
CONTROL L5119  <Proto_PrisonKey.Rescue>
ROW CAT:O3fd5a6655730c755eb98 L5120 * physical_line
  EN: You'll need a key to unlock my shackles. You do have one, right?
  ZH:   * 要解开我的镣铐得有钥匙。你有的吧？

## SC62c0fa8aca8d3849 | nsfw | datadf/all.ds | Proto_PrisonKey.SoldOut
CONTROL L5128  <Proto_PrisonKey.SoldOut>
ROW CAT:Oa32f55a33dd0153e84ad L5129 * physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   * 谢谢，不过我已经被救出来了！

## SC94e9cd820ae5152a | nsfw | datadm/all.ds | Proto_PrisonKey.SoldOut
CONTROL L5141  <Proto_PrisonKey.SoldOut>
ROW CAT:O4954f88884de89f452c2 L5142 * physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   * 谢谢，不过我已经被救出来了！

## SCbdce11d2561c0a2e | nsfw | datadf/all.ds | Proto_PrisonTazer.GoodbyeDog
CONTROL L5152  <Proto_PrisonTazer.GoodbyeDog>
ROW CAT:O22e9d559583ff8625312 L5153 * physical_line
  EN: Please come back soon with your master!
  ZH:   * 请早点带着你的主人回来！

## SC3ff0bd7d505b9149 | nsfw | datadm/all.ds | Proto_PrisonTazer.GoodbyeNotRescued
CONTROL L5156  <Proto_PrisonTazer.GoodbyeNotRescued>
ROW CAT:O7de567daaa8a19953d1e L5157 * physical_line
  EN: Please come back soon!
  ZH:   * 请早点回来！

## SC8e2ec33479b40118 | nsfw | datadf/all.ds | Proto_PrisonTazer.GoodbyeNotRescued
CONTROL L5143  <Proto_PrisonTazer.GoodbyeNotRescued>
ROW CAT:Od1edb532c902261b7955 L5144 * physical_line
  EN: Please come back soon!
  ZH:   * 请早点回来！

## SC2c596916623d5a16 | nsfw | datadf/all.ds | Proto_PrisonTazer.Hello
CONTROL L5137  <Proto_PrisonTazer.Hello>
ROW CAT:O0139527c6d82557c3572 L5138 * physical_line
  EN: Help, I'm trapped in here!
  ZH:   * 救命，我被困在这儿了！

## SCc88ba053115ab1d5 | nsfw | datadf/all.ds | Proto_PrisonTazer.NoBoneForDog
CONTROL L5149  <Proto_PrisonTazer.NoBoneForDog>
ROW CAT:O5b52a9eab92f789905fc L5150 * physical_line
  EN: Can you get your master to come and help me?
  ZH:   * 你能让你的主人过来帮我吗？

## SC3efcc13de6dbdc58 | nsfw | datadf/all.ds | Proto_PrisonTazer.Purchased
CONTROL L5164  <Proto_PrisonTazer.Purchased>
ROW CAT:O2bfece465eb3b10a83f1 L5165 * physical_line
  EN: Thank you!
  ZH:   * 谢谢！

## SC772a3b533e883e9b | nsfw | datadm/all.ds | Proto_PrisonTazer.Purchased
CONTROL L5177  <Proto_PrisonTazer.Purchased>
ROW CAT:Ob4a837b707db26f862fe L5178 * physical_line
  EN: Thank you!
  ZH:   * 谢谢！

## SCd3addf3c41a94622 | nsfw | datadm/all.ds | Proto_PrisonTazer.TalkAfterRescue.thanks
CONTROL L5186  <Proto_PrisonTazer.TalkAfterRescue.thanks>
ROW CAT:O73cfe06a301fd8e57fdd L5187 * physical_line
  EN: I'm sorry I don't have any data for you. I'm just a placeholder...
  ZH:   * 抱歉，我没有什么数据可以给你。我只是个占位角色……

## SC63a19d13e021be6f | nsfw | datadm/all.ds | Test_Hacker1.CancelPurchase
CONTROL L5218  <Test_Hacker1.CancelPurchase>
ROW CAT:O078e8df39211fffe6fb9 L5219 * physical_line
  EN: Are you worried about voiding the warranty? Pft.
  ZH:   * 你是担心会让保修失效吗？噗。
ROW CAT:Ofb3855b6675950a42fda L5220 * physical_line
  EN: Oh well. Have you got something else for me to work on?
  ZH:   * 算了。你还有别的活儿要我干吗？

## SCdb403d90d429afc1 | nsfw | datadf/all.ds | Test_Hacker1.Hack
CONTROL L5225  <Test_Hacker1.Hack>
ROW CAT:O5af43cd908b681c60324 L5226 * physical_line
  EN: Ready to hack it?
  ZH:   * 准备好黑掉它了吗？

## SCa2b603706d87bee4 | nsfw | datadm/all.ds | Test_Prison1.CancelPurchase
CONTROL L5262  <Test_Prison1.CancelPurchase>
CONTROL L5263    if { hasItem(Key) } {
ROW CAT:O96cce9cabf05ea19532c L5264 * physical_line
  EN: [Stop fooling around and get me out of here!]
  ZH:     * [别胡闹了，快把我弄出去！]
CONTROL L5265    } else {
ROW CAT:Ocfd95fa49016e8859183 L5266 * physical_line
  EN: [You'll need a key to rescue me!]
  ZH:     * [要救我，你得有钥匙！]
CONTROL L5267    }

## SCa66d8bb15f39068b | nsfw | datadf/all.ds | Test_Prison1.CancelPurchase
CONTROL L5249  <Test_Prison1.CancelPurchase>
CONTROL L5250    if { hasItem(Key) } {
ROW CAT:Odbe0009db816a5bf9bfa L5251 * physical_line
  EN: [Stop fooling around and get me out of here!]
  ZH:     * [别胡闹了，快把我弄出去！]
CONTROL L5252    } else {
ROW CAT:Obfff760bcdd650b39922 L5253 * physical_line
  EN: [You'll need a key to rescue me!]
  ZH:     * [要救我，你得有钥匙！]
CONTROL L5254    }

## SC4b63add43943cb4e | nsfw | datadm/all.ds | Test_Prison1.Goodbye
CONTROL L5243  <Test_Prison1.Goodbye>
ROW CAT:O1dfe68f79a6f687582e4 L5244 * physical_line
  EN: [Thank you, Yiffai!]
  ZH:   * [谢谢你，伊吠！]

## SC26a9fbf51517bbca | nsfw | datadf/all.ds | Test_Prison1.HelloDog
CONTROL L5236  <Test_Prison1.HelloDog>
ROW CAT:O043d5e3c9a1d34f23e0b L5237 * physical_line
  EN: [It... it's a dog! Oh no!]
  ZH:   * [它……是只狗！哦不！]

## SCbb71e0c6f28aec87 | nsfw | datadm/all.ds | Test_Prison1.NotEnoughMoney
CONTROL L5275  <Test_Prison1.NotEnoughMoney>
ROW CAT:O5dcafd4f87dba001e9ca L5276 * physical_line
  EN: [You can't open these cuffs with your bare hands!]
  ZH:   * [你空手打不开这些手铐！]
ROW CAT:O68302baedbd99e530adf L5277 * physical_line
  EN: [You'll need to find a key.]
  ZH:   * [你得去找一把钥匙。]

## SC2948bec8acd8c0b4 | nsfw | datadm/all.ds | Test_Prison1.Purchased
CONTROL L5272  <Test_Prison1.Purchased>
ROW CAT:O8dc8ba2e84ea8bfcb48f L5273 * physical_line
  EN: [I'm free!]
  ZH:   * [我自由了！]

## SCfe6a07f5435082fe | nsfw | datadf/all.ds | Test_Prison1.Purchased
CONTROL L5259  <Test_Prison1.Purchased>
ROW CAT:O27fa462f2c9ae627b0b5 L5260 * physical_line
  EN: [I'm free!]
  ZH:   * [我自由了！]

## SC39d040eed5fb1839 | nsfw | datadf/all.ds | Test_Prison1.Rescue
CONTROL L5256  <Test_Prison1.Rescue>
ROW CAT:O5a1616915733282e2b63 L5257 * physical_line
  EN: [Quick, unlock my shackles! You have a key, right..?]
  ZH:   * [快，解开我的镣铐！你有钥匙的吧……？]

## SCeab91236f3254c5f | nsfw | datadf/all.ds | Test_Prison1.SoldOut
CONTROL L5266  <Test_Prison1.SoldOut>
ROW CAT:O644c7d73115b1857c400 L5267 * physical_line
  EN: [I'm already rescued, Yiffai!]
  ZH:   * [我已经被救出来了，伊吠！]

## SCa54df285583a58d1 | nsfw | datadf/all.ds | Test_Prison1.TalkAfterRescue.thanks
CONTROL L5272  <Test_Prison1.TalkAfterRescue.thanks>
ROW CAT:O43e495a6a3a960b70a1f L5273 * physical_line
  EN: [I don't know what I would have done if you hadn't shown up!]
  ZH:   * [要是你没出现，我真不知道该怎么办！]

## SCea06212702d2bdb4 | nsfw | datadf/all.ds | Test_Prison1.TalkBeforeRescue.bopped
CONTROL L5269  <Test_Prison1.TalkBeforeRescue.bopped>
ROW CAT:O652a5bbf2d8e3f5e1c6c L5270 * physical_line
  EN: [I got bopped by the baddies and woke up in here!]
  ZH:   * [我被坏蛋打晕了，醒来就在这儿！]

## SC588126dcfa071095 | nsfw | datadm/all.ds | Test_Slaver1.AgentM0C
CONTROL L5353  <Test_Slaver1.AgentM0C>
ROW CAT:O879de40acbe5247f4543 L5354 * physical_line
  EN: Little yiffer here isn't worth much, just take it! Just like he did ;3!
  ZH:   * 这儿这个小色狼不值钱，拿去用吧！就像他当初那样"用" ;3！

## SCa26814e8281f2cc6 | nsfw | datadf/all.ds | Test_Slaver1.CancelPurchase
CONTROL L5343  <Test_Slaver1.CancelPurchase>
ROW CAT:Oaa90c0685415925fbc43 L5344 * physical_line
  EN: That's a shame. Anything else?
  ZH:   * 真遗憾。还要点别的吗？

## SCaa633a718a5a505a | nsfw | datadf/all.ds | Test_Slaver1.GasMask
CONTROL L5331  <Test_Slaver1.GasMask>
ROW CAT:Of4a09d52978ee8bca35e L5332 * physical_line
  EN: Need to explore a toxic area? Bring a few of these along!
  ZH:   * 要探索有毒区域？带上几个这个！

## SC62b1cef19f673dfc | nsfw | datadf/all.ds | Test_Slaver1.GoodbyeDog
CONTROL L5287  <Test_Slaver1.GoodbyeDog>
ROW CAT:Occ652a7307e138adf87d L5288 * physical_line
  EN: Get out of here mutt! The other dogs got to these slaves first!
  ZH:   * 从这儿滚出去，杂种狗！这些奴隶已经让别的狗抢先占了！

## SC384e891d034e8027 | nsfw | datadm/all.ds | Test_Slaver1.GoodbyeNoID
CONTROL L5332  <Test_Slaver1.GoodbyeNoID>
ROW CAT:O1dd1564ab460ffcd3811 L5333 * physical_line
  EN: Bye bye, pup. Come back when you're older!
  ZH:   * 拜拜，小狗。等你长大点再来吧！

## SC4c2af9cdc88d9e24 | nsfw | datadf/all.ds | Test_Slaver1.Hello
CONTROL L5274  <Test_Slaver1.Hello>
ROW CAT:O4c8d98a5a1715082b1a0 L5275 * physical_line
  EN: Hello! Can I get you something?
  ZH:   * 你好！想买点什么？

## SC5790b067670ab317 | nsfw | datadm/all.ds | Test_Slaver1.Hello
CONTROL L5287  <Test_Slaver1.Hello>
ROW CAT:Oa2ceaa3c6aa86a4d3dc8 L5288 * physical_line
  EN: Hello! Can I get you something?
  ZH:   * 你好！想买点什么？

## SC088f6eb655f71c9b | nsfw | datadm/all.ds | Test_Slaver1.HelloDog
CONTROL L5290  <Test_Slaver1.HelloDog>
ROW CAT:Ocf4bb1f4a084d5f89cdb L5291 * physical_line
  EN: What? A dog?!
  ZH:   * 什么？一只狗？！

## SCf94a7b0d2b3b6b2a | nsfw | datadf/all.ds | Test_Slaver1.HelloDog
CONTROL L5277  <Test_Slaver1.HelloDog>
ROW CAT:Od3e14f3f445525655ca6 L5278 * physical_line
  EN: What? A dog?!
  ZH:   * 什么？一只狗？！

## SCf612f05129463f7c | nsfw | datadf/all.ds | Test_Slaver1.HelloNoJuice
CONTROL L5290  <Test_Slaver1.HelloNoJuice>
CONTROL L5291    if { isFeral() } {
ROW CAT:O0dc2d025f78b3ad2487a L5292 * physical_line
  EN: Oh, it's a dog...
  ZH:     * 哦，是只狗……
ROW CAT:O9ee2ff8f62ff2440f2d5 L5293 * physical_line
  EN: I'm afraid I can't do anything for you, pup.
  ZH:     * 恐怕我帮不了你，小狗。
CONTROL L5294    } else {
ROW CAT:Oa97a6a8d5da8826beb90 L5295 * physical_line
  EN: Oh, hello. This is my shop. Well, it's supposed to be.
  ZH:     * 哦，你好。这是我的店。嗯，本来应该是。
ROW CAT:Of826b276bf9a8d878deb L5296 * physical_line
  EN: I've just been feeling under the weather lately... like I'm missing something.
  ZH:     * 我最近一直不舒服……像是缺了点什么。
ROW CAT:O135ff40e724e1ef08509 L5297 * physical_line
  EN: I'm afraid you'll have to come back later.
  ZH:     * 恐怕你得晚点再来。
CONTROL L5298    }

## SC9bb7f3479db490d3 | nsfw | datadm/all.ds | Test_Slaver1.PsyTea
CONTROL L5338  <Test_Slaver1.PsyTea>
ROW CAT:O4b7834afbdaceb60dcba L5339 * physical_line
  EN: This tea will recover your psychic power!
  ZH:   * 这茶能恢复你的灵能！

## SC0f6df4c4a192acca | nsfw | datadm/all.ds | Test_Slaver1.SoldOut
CONTROL L5384  <Test_Slaver1.SoldOut>
ROW CAT:Oc4580e6a3f9dbfc42eee L5385 * physical_line
  EN: Flaunting your money now huh punk?!
  ZH:   * 现在显摆起钱来了是吧，小子？！
ROW CAT:O2082d4527341908f1b68 L5386 * physical_line
  EN: Come back when I catch another mangy play thing!
  ZH:   * 等我再抓到一只癞皮玩物再来！

## SC7a8997bd2b051f31 | nsfw | datadf/all.ds | Test_Slaver1.ThanksForJuice
CONTROL L5303  <Test_Slaver1.ThanksForJuice>
ROW CAT:O2719da444a324d5942b0 L5304 * physical_line
  EN: What?! For me? Wait... is this...
  ZH:   * 什么？！给我的？等等……这是……
ROW CAT:Ob40e020733d4fb63ea53 L5305 * physical_line
  EN: It's my special juice! Just one swig of this and I'm ready for business!
  ZH:   * 这是我的特制果汁！只要喝上一口，我马上就能开张做生意！
ROW CAT:O1064f369df55641caf15 L5306 * physical_line
  EN: Alright, can I get you something?
  ZH:   * 好了，要我给你来点什么吗？

