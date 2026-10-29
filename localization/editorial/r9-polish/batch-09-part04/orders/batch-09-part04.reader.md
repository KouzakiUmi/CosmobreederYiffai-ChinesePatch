# batch-09-part04 精校工单：区域场景与条件分支（关卡救援与分支）（第 4／4 部分）

英文与当前中文都按整场连读；`current` 是构建候选的实际显示行（以本批参照摘录与 ORDER 记的候选为准）。
ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。

## SC9735d1c4d1313dbf | nsfw | datadf/all.ds | AreaA_Cellar.Hello
CONTROL L292  <AreaA_Cellar.Hello>
ROW CAT:O2b7274ef04e204c978fa L293 * physical_line
  EN: Oh heeeello, welcome to my little meat cellar!
  ZH:   * 哦，你——好——呀，欢迎来到我的小肉窖！

## SC7498ea44842679da | nsfw | datadf/all.ds | AreaA_Cellar.Talk.chew
CONTROL L301  <AreaA_Cellar.Talk.chew>
ROW CAT:Ob62512c7c20a7fc02b78 L302 * physical_line
  EN: Whew! Sure is a lot of work to carve up a dragon.
  ZH:   * 呼！把一条龙切开分块可真够费劲的。
ROW CAT:O9677dc9498c95bfbd590 L303 * physical_line
  EN: ...and don't even get me started on how tough it was to SLAY the things!
  ZH:   * ……更别提宰掉这些家伙有多难了！

## SC24f5ff25cb832b06 | nsfw | datadf/all.ds | AreaA_Cellar.Talk.meatcode
CONTROL L305  <AreaA_Cellar.Talk.meatcode>
ROW CAT:Oe4b76ad0514e1b4ef10b L306 * physical_line
  EN: What? You want something else?
  ZH:   * 什么？你还想要点别的？
ROW CAT:Ocb46cae6c640f52f0eb2 L307 * physical_line
  EN: Well, alright... I can give you access to my secret cartoon and card stash...
  ZH:   * 好吧，行吧……我可以让你看看我藏起来的秘密漫画和卡牌……
ROW CAT:O24bd0b1aae7bf36bba25 L308 * physical_line
  EN: All you gotta do is... TAEGXLAA... if you know what I mean... He! He! He!
  ZH:   * 你要做的只是……TAEGXLAA……如果你懂我意思的话……嘿！嘿！嘿！
CONTROL L310  ### shared ###

## SCa9b5286afb6d004b | nsfw | datadm/all.ds | AreaA_Macsen1.Hello
CONTROL L392  <AreaA_Macsen1.Hello>
ROW CAT:O9c63d5ea86d1e700800f L393 * physical_line
  EN: Welcome! Hot meats, cool treats! Perfect for Ayskammr!
  ZH:   * 欢迎光临！热腾腾的肉，透心凉的冷饮！最适合艾斯卡姆尔了！

## SCaa75c921bdff1c7e | nsfw | datadf/all.ds | AreaA_Macsen1.HelloIDPlease
CONTROL L402  <AreaA_Macsen1.HelloIDPlease>
ROW CAT:Oda948d654c570ca131ff L403 * physical_line
  EN: Oh hey there, I'm gonna need to see some ID.
  ZH:   * 哦，你好啊，我得先看看你的证件。
ROW CAT:O6111089c94a40bbbe765 L404 * physical_line
  EN: No pups allowed in here!
  ZH:   * 这里不许小狗进来！

## SC1acca4371fdd63fe | sfw | datadf/all.ds | AreaA_Macsen1.PsyTea
CONTROL L419  <AreaA_Macsen1.PsyTea>
ROW SFW39c1cd5c9b0a4c11a225e1ca L420 - physical_line
  EN: This stuff will quench your thirst and recover some PSY, but to be honest...
  ZH:   * 这玩意儿能解渴，还能恢复一些精神力，不过说实话……
ROW SFW37fcf86ba1602acd670692b1 L421 - physical_line
  EN: ...it won't cool you down like a nice ICECOLA will! 
  ZH:   * ……可它没法像爽口的 ICECOLA 那样让你凉快下来！ 

## SCad90771e17a06a99 | nsfw | datadm/all.ds | AreaA_Macsen1.VitMeat
CONTROL L412  <AreaA_Macsen1.VitMeat>
ROW CAT:O8aa338c7c53ee6f335dd L413 * physical_line
  EN: Carved from ferocious beasties, slow roasted over lava! Restores vitality!
  ZH:   * 取自凶猛野兽的肉，在熔岩上慢火烤成！恢复活力！

## SC248298ce6d588263 | nsfw | datadf/all.ds | AreaA_Macsen2.Hello
CONTROL L464  <AreaA_Macsen2.Hello>
ROW CAT:O86fa1a7a34be62c6eb23 L465 * physical_line
  EN: Whew, I thought you were a dwarf at first! Welcome!
  ZH:   * 呼，我一开始还以为你是个矮人呢！欢迎！

## SCee5b6732ec650150 | nsfw | datadm/all.ds | AreaA_Macsen2.HelloNoJuice
CONTROL L488  <AreaA_Macsen2.HelloNoJuice>
ROW CAT:Obc25dac4c3de989131b0 L489 * physical_line
  EN: Oh hey there, It's too hot to do any business right now!
  ZH:   * 哦，你好啊，天太热了，现在没法做生意！
ROW CAT:Ob54d777948c94b6e1896 L490 * physical_line
  EN: You're free to browse until I get my paws on a nice cool drink...
  ZH:   * 我没喝上冰凉的饮料前，你就先随便看看吧……

## SC29a9f3bebb472d37 | nsfw | datadm/all.ds | AreaA_Macsen2.Talk.icecola
CONTROL L482  <AreaA_Macsen2.Talk.icecola>
CONTROL L483    if { !f(shop_juiced) } {
ROW CAT:Oe0723521529072412555 L484 * physical_line
  EN: Wish I could get my hands on a nice cold ICECOLA right about now...
  ZH:     * 要是现在能弄到一瓶冰镇ICECOLA就好了……
ROW CAT:O25ae42292e48f8c4c882 L485 * physical_line
  EN: But I lost my ID and you need one of those to buy them. Dammit!
  ZH:     * 可我的证件丢了，买那个又得出示证件。该死！
CONTROL L486    }

## SC539eb0a55da812cc | nsfw | datadf/all.ds | AreaA_Macsen2.Talk.icecola
CONTROL L499  <AreaA_Macsen2.Talk.icecola>
CONTROL L500    if { !f(shop_juiced) } {
ROW CAT:O008578262a73fbe53eba L501 * physical_line
  EN: Wish I could get my hands on a nice cold ICECOLA right about now...
  ZH:     * 要是现在能弄到一瓶冰镇 ICECOLA 就好了……
ROW CAT:Of359ad6272672f56282f L502 * physical_line
  EN: But I lost my ID and you need one of those to buy them. Dammit!
  ZH:     * 可我的证件丢了，买那个又得出示证件。该死！
CONTROL L503    }
CONTROL L505  ### shared ###

## SC8160b804adc19568 | nsfw | datadm/all.ds | AreaA_Prison1.GoodbyeDog
CONTROL L561  <AreaA_Prison1.GoodbyeDog>
ROW CAT:Ofdbfe5497f062213e291 L562 * physical_line
  EN: Please come back soon with your master, and a key!
  ZH:   * 请早点带着你的主人和一把钥匙回来！

## SC7336d4b8ef3a1db6 | nsfw | datadf/all.ds | AreaA_Prison1.Hello
CONTROL L547  <AreaA_Prison1.Hello>
ROW CAT:O15c7d7f705c2a2e5c014 L548 * physical_line
  EN: Oh, hey! Am I ever g-glad to see you!
  ZH:   * 哦，嘿！见到你我真是太高、高兴了！

## SC9e3c488b91dd54bb | sfw | datadm/all.ds | AreaA_Prison1.Hello
CONTROL L546  <AreaA_Prison1.Hello>
ROW SFW9b4ea8c685bc54c0d65a8eef L547 - physical_line
  EN: Oh h-hey! Wasn't expecting another agent to get in here!
  ZH:   * 哦，嗨、嗨！没想到还有别的特工能进来！
ROW SFW5ebb896680d07ae457f95bc4 L548 - physical_line
  EN: I might have gotten myself in a sliight bit of trouble... 
  ZH:   * 我好像给自己惹了那么一——点小麻烦…… 

## SC5411cf96ee9fbab8 | nsfw | datadm/all.ds | AreaA_Prison1.HelloDog
CONTROL L555  <AreaA_Prison1.HelloDog>
ROW CAT:Oba03f4cd11d351d10fb0 L556 * physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SC564c98e73616dfda | nsfw | datadf/all.ds | AreaA_Prison1.HelloDog
CONTROL L556  <AreaA_Prison1.HelloDog>
ROW CAT:Oabf73f825703cca65742 L557 * physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SC59ecd8a076ae0115 | sfw | datadm/all.ds | AreaA_Prison1.NoBoneForDog
CONTROL L559  <AreaA_Prison1.NoBoneForDog>
ROW SFW83053430be7fd925ad1e9aa5 L560 - physical_line
  EN: Can you get your master to come back with a key? I'm locked up in here!
  ZH:   * 你能让你的主人带着钥匙回来吗？我被锁在这里面了！

## SCb810ac30e6045f70 | nsfw | datadm/all.ds | AreaA_Prison1.NotEnoughMoney
CONTROL L581  <AreaA_Prison1.NotEnoughMoney>
ROW CAT:O0ff0249f2a71ff2e82c2 L582 * physical_line
  EN: Yeah this guy's not letting go until he's finished...
  ZH:   * 是啊，这家伙不弄完是不会放开我的…… 
ROW CAT:O44c45e2546c426cce77d L583 * physical_line
  EN: ...or until you use a key to trigger that trap above us!
  ZH:   * ……或者直到你用钥匙触发咱们上面那个陷阱！

## SC7509b6e67d10f08b | sfw | datadm/all.ds | AreaA_Prison1.NotEnoughMoney
CONTROL L582  <AreaA_Prison1.NotEnoughMoney>
ROW SFW37541ebe8d077d3214f95bab L583 - physical_line
  EN: I could probably dig my way out of here after a couple of years...
  ZH:   * 再挖上几年，我大概就能挖出去了……
ROW SFW9ae9766b8d7f6c03a1538846 L584 - physical_line
  EN: ...unless you happen to find a key somewhere?
  ZH:   * ……除非你碰巧能在什么地方找到把钥匙？

## SC53f25359226ff8b4 | nsfw | datadf/all.ds | AreaA_Prison1.Purchased
CONTROL L579  <AreaA_Prison1.Purchased>
ROW CAT:Of933b44e9daccf091f67 L580 * physical_line
  EN: Ooooooh thank you!
  ZH:   * 哦——谢谢你！

## SC3e164cc042e9394c | nsfw | datadf/all.ds | AreaA_Prison1.Rescue
CONTROL L576  <AreaA_Prison1.Rescue>
ROW CAT:O7595d2b0980abe4dc258 L577 * physical_line
  EN: W-we could trap this fella if you had a k-k-key! You've got one, right?
  ZH:   * 要、要是有把钥、钥匙，我们就能困住这家伙了！你有吧？

## SC77c517b8a7db50f4 | nsfw | datadm/all.ds | AreaA_Prison1.Rescue
CONTROL L574  <AreaA_Prison1.Rescue>
ROW CAT:Oad3213f4ffa0d481a1d6 L575 * physical_line
  EN: I was just about to escape, but you know, if you want to help out a bit...
  ZH:   * 我正要逃走，不过嘛，你要是肯帮一把……
ROW CAT:O76486a49dab28db70f6d L576 * physical_line
  EN: ...that'd be pretty swell, pal!
  ZH:   * ……那可就太好了，老兄！

## SCdf99f6e95fccb7e3 | sfw | datadm/all.ds | AreaA_Prison1.TalkBeforeRescue.wip
CONTROL L589  <AreaA_Prison1.TalkBeforeRescue.wip>
ROW SFW99e2fa8b799c1a21714d7bf5 L590 - physical_line
  EN: I was totally conquering this planet before they locked me up, I swear!
  ZH:   * 我发誓，被关起来之前，我都快征服这颗星球了！

## SC4d26ced04c26ca61 | sfw | datadf/all.ds | AreaA_Prison2.CancelPurchase
CONTROL L617  <AreaA_Prison2.CancelPurchase>
ROW SFWff265414b964f1615c865e11 L618 - physical_line
  EN: Well do you have a plan, or are you just gonna stand there lookin'?
  ZH:   * 你到底有没有计划，还是就打算站着干看？

## SC0bfd8750f6ede28c | nsfw | datadf/all.ds | AreaA_Prison2.Goodbye
CONTROL L597  <AreaA_Prison2.Goodbye>
ROW CAT:O2425638028c14fb936a2 L598 * physical_line
  EN: Haah... I feel sooo much better.
  ZH:   * 哈啊……我现在感觉好太多太多啦。

## SC732e29238cbc13b8 | sfw | datadm/all.ds | AreaA_Prison2.Hello
CONTROL L594  <AreaA_Prison2.Hello>
ROW SFWe9f340272e7518f0e8fb6c42 L595 - physical_line
  EN: Oh hhh...hello. I've been waiting for someone to come along...
  ZH:   * 噢，嗯……你、你好。我一直等着有人来……
ROW SFW2795dcd7d2a8e0c6c46ad25e L596 - physical_line
  EN: Someone to set me free!
  ZH:   * 能放我自由的人！

## SC3bf4054d5c6afc06 | nsfw | datadm/all.ds | AreaA_Prison2.NoBoneForDog
CONTROL L606  <AreaA_Prison2.NoBoneForDog>
ROW CAT:O243b61386709876c9d09 L607 * physical_line
  EN: Who's a good boy? I am! But you wanna help me with... something?
  ZH:   * 谁是乖孩子？是我呀！不过你是想帮我……做点什么吗？

## SC62a0e5d9ff7a1d66 | nsfw | datadf/all.ds | AreaA_Prison2.NoBoneForDog
CONTROL L607  <AreaA_Prison2.NoBoneForDog>
ROW CAT:Odec00a34f18efc66e7ac L608 * physical_line
  EN: Shoo girl, you aren't gonna be able to help me!
  ZH:   * 走开啦姑娘，你帮不上我的忙的！

## SCb12b48e46ae18ed4 | sfw | datadm/all.ds | AreaA_Prison2.NoBoneForDog
CONTROL L607  <AreaA_Prison2.NoBoneForDog>
ROW SFW7af135f5684bf5101f2fb77a L608 - physical_line
  EN: Who's a good boy? I am! But you wanna help...?
  ZH:   * 谁是乖孩子？是我！不过，你想帮忙吗……？

## SC1357d946913edd49 | sfw | datadf/all.ds | AreaA_Prison2.Rescue
CONTROL L620  <AreaA_Prison2.Rescue>
ROW SFW670010b388ff399187e3a786 L621 - physical_line
  EN: Oh, do you think you can break me out of here?
  ZH:   * 哦，你觉得自己能把我救出去？
ROW SFWe83e9313ee7aa98c564b8cd1 L622 - physical_line
  EN: This outta be fun to see...
  ZH:   * 这下可有好戏看了……

## SC88f6a88f045f133e | sfw | datadf/all.ds | AreaA_Prison2.SoldOut
CONTROL L627  <AreaA_Prison2.SoldOut>
ROW SFW81ed97c518e7642f4a8927cb L628 - physical_line
  EN: I can make my way back to the hangar myself, no need to carry me.
  ZH:   * 我自己能回机库，不用你背。

## SC8ff1971dc1b688fa | nsfw | datadf/all.ds | AreaA_Prison2.TalkAfterRescue.thanks
CONTROL L633  <AreaA_Prison2.TalkAfterRescue.thanks>  
ROW CAT:O93c2ad1c64e46ae4974f L634 * physical_line
  EN: Good thing you came along when you did! Whew!
  ZH:   * 幸好你及时赶到！呼——
ROW CAT:O200bb4a9b7d73ead0260 L635 * physical_line
  EN: I was just about to tear a hole in that anvil...
  ZH:   * 我都要把那铁砧凿出个窟窿了……

## SCf543f5d518e7bcf8 | nsfw | datadf/all.ds | AreaA_Prison3.CancelPurchase
CONTROL L657  <AreaA_Prison3.CancelPurchase>
ROW CAT:O213cbd94236da9058f19 L658 * physical_line
  EN: Oh? Is there something wrong?
  ZH:   * 哦？是出什么问题了吗？

## SC9909781819b3d4d8 | nsfw | datadm/all.ds | AreaA_Prison3.GoodbyeNotRescued
CONTROL L643  <AreaA_Prison3.GoodbyeNotRescued>
ROW CAT:Oeaf9fb0ca2f564c639da L644 * physical_line
  EN: I guess I'm not getting rescued today ? O-okay, well... I'll be waiting.
  ZH:   * 看来今天是不会有人来救我了 ？那、那好吧……我等着就是了。

## SCab7f86a283e376af | nsfw | datadm/all.ds | AreaA_Prison3.Hello
CONTROL L636  <AreaA_Prison3.Hello>
ROW CAT:Obca37d74eb7f16bb1d26 L637 * physical_line
  EN: O-oh hey there. I'm glad to see another agent!
  ZH:   * 哦、哦，你好。能见到别的特工真高兴！
ROW CAT:O4c8042acbcbdaf5c9677 L638 * physical_line
  EN: Especially a *dog* agent, haha... I mean...!
  ZH:   * 尤其是*狗*特工，哈哈……我是说……！

## SCeaac4f90decc80c9 | sfw | datadm/all.ds | AreaA_Prison3.Hello
CONTROL L636  <AreaA_Prison3.Hello>
ROW SFW1635d707f71f1fcdcecce2d8 L637 - physical_line
  EN: O-oh hey there. I'm glad to see another agent!
  ZH:   * 哦、哦，你好。能见到别的特工真高兴！

## SC7618d386bcbd0943 | nsfw | datadf/all.ds | AreaA_Prison3.SoldOut
CONTROL L669  <AreaA_Prison3.SoldOut>
ROW CAT:O81becdeb526cad535b39 L670 * physical_line
  EN: Alright, I'll get back to work! Quit nagging!
  ZH:   * 行了行了，我回去干活就是了！别唠叨了！

## SCa73174d600d0fb78 | sfw | datadm/all.ds | AreaA_Prison3.TalkAfterRescue.thanks
CONTROL L679  <AreaA_Prison3.TalkAfterRescue.thanks>
ROW SFW8e1be4dd447ff99f2a452afa L680 - physical_line
  EN: You know, I think I've had enough of the mines!
  ZH:   * 说真的，我已经受够矿井了！

## SC1c3e7d31f19708f4 | sfw | datadm/all.ds | AreaA_Prison3.TalkBeforeRescue.bopped
CONTROL L676  <AreaA_Prison3.TalkBeforeRescue.bopped>
ROW SFW92eec87c5517140354264d30 L677 - physical_line
  EN: I thought you were a dwarf at first. They aren't very nice!
  ZH:   * 我一开始还以为你是矮人。他们可不怎么友善！

## SCbb8a8179039049e8 | sfw | datadf/all.ds | AreaA_Prison3.TalkBeforeRescue.bopped
CONTROL L672  <AreaA_Prison3.TalkBeforeRescue.bopped>
ROW SFW1e08b7c09eb0db3ad33a7430 L673 - physical_line
  EN: It's been pretty nice down here, don't you think?
  ZH:   * 这下面待着还挺不错的，你不觉得吗？
ROW SFWa31bf3af662d09cafa62732d L674 - physical_line
  EN: The kobolds bring me food and everything.
  ZH:   * 狗头人还给我送吃的，什么都照顾到了。

## SCd8a5f7dd05b7892d | nsfw | datadm/all.ds | AreaB_Macsen1.Hello
CONTROL L730  <AreaB_Macsen1.Hello>
ROW CAT:Ocf3a117d3ed407161bd9 L731 * physical_line
  EN: Hello! Can I get you something?
  ZH:   * 你好！想买点什么？

## SC33ed9ca3f596edd5 | nsfw | datadf/all.ds | AreaB_Macsen1.PsyUp
CONTROL L739  <AreaB_Macsen1.PsyUp>
ROW CAT:O0b2295cce8dbbefbbd70 L740 * physical_line
  EN: A real live psy crystal, just like those espers use!
  ZH:   * 货真价实的精神力水晶，跟那些超能力者用的一样！

## SC261c757407969621 | nsfw | datadf/all.ds | AreaB_Macsen1.Talk.digging
CONTROL L742  <AreaB_Macsen1.Talk.digging>
ROW CAT:O67ba6df8a2494311308b L743 * physical_line
  EN: You look like a smart dog, real bright eyes, cold wet nose, fluffy raised tail...
  ZH:   * 你看着是只聪明的狗，眼睛亮晶晶的，鼻子又凉又湿，毛茸茸的尾巴翘得高高的……
ROW CAT:Ofcab17e83e72e4fd03a4 L744 * physical_line
  EN: Did you know that ferals, are able to dig up dirt by pressing DOWN+ATTACK?
  ZH:   * 你知道吗，野兽形态下按DOWN+攻击就能刨土！
ROW CAT:Ofa45df5f252b27291212 L745 * physical_line
  EN: It's just good info to know, ya know!
  ZH:   * 这可是实用的小知识，记着没坏处！

## SC67fd20ceba9a979d | nsfw | datadf/all.ds | AreaB_Macsen1.VitBone
CONTROL L735  <AreaB_Macsen1.VitBone>
ROW CAT:O2efd02c13e52ed1ef63f L736 * physical_line
  EN: Nothing like a nice bone to satisfy your craving!
  ZH:   * 没有比一根好骨头更能解馋的了！
ROW CAT:O27cd14ad264d439b6689 L737 * physical_line
  EN: Gives you a bit of vigor, too!
  ZH:   * 还能让你添点儿活力！

## SCfad3d975b187eeb1 | nsfw | datadm/all.ds | AreaB_Macsen2.Goodbye
CONTROL L801  <AreaB_Macsen2.Goodbye>
ROW CAT:O6b5669ab6d08a9ad2279 L802 * physical_line
  EN: Remember, this is our little secret!
  ZH:   * 记住了，这是咱们俩的小秘密！

## SC51ecfecbc787fbc9 | nsfw | datadf/all.ds | AreaB_Macsen2.Hello
CONTROL L792  <AreaB_Macsen2.Hello>
ROW CAT:Occ54699c4fd18eb8e0c1 L793 * physical_line
  EN: Oh hi, it's pretty rare to get visitors here!
  ZH:   * 哦，你好，这儿可难得有客人来！

## SCa6ca506a6d94efd7 | nsfw | datadf/all.ds | AreaB_Macsen2.Talk.macsenhard
CONTROL L801  <AreaB_Macsen2.Talk.macsenhard>
ROW CAT:Oec9bbd7531f32c5ea4b3 L802 * physical_line
  EN: Running all these shops all over Tutone, all at once... it's hard work!
  ZH:   * 图托恩各处这么多店同时开着……真辛苦！
ROW CAT:O7e69ebcd6364fc4c7cc5 L803 * physical_line
  EN: Not nearly as hard as developing Cosmobreeder Yiffai, but hard work still!
  ZH:   * 没开发《宇宙育种者伊吠》苦，可挺累人！

## SCc3ad59fdff3438ca | nsfw | datadf/all.ds | AreaB_Macsen2.Talk.macsenmoneycode1
CONTROL L805  <AreaB_Macsen2.Talk.macsenmoneycode1>
ROW CAT:Ob00a5efa7d522fa17976 L806 * physical_line
  EN: What, is taking all my money not good enough?
  ZH:   * 怎么，把我钱全拿走还不够？
ROW CAT:O46817f73fbd10e683e84 L807 * physical_line
  EN: Why don't you take off next, huh punk?
  ZH:   * 钱都拿了，还不快滚，小混混？

## SCd0245ca0662e436c | nsfw | datadm/all.ds | AreaB_Macsen2.Talk.macsenmoneycode1
CONTROL L811  <AreaB_Macsen2.Talk.macsenmoneycode1>
ROW CAT:O3627b196d1ce1041c04f L812 * physical_line
  EN: What, is taking all my money not good enough?
  ZH:   * 怎么，把我钱全拿走还不够？
ROW CAT:O57ecac04932c459403fd L813 * physical_line
  EN: Why don't you take off next, huh punk?
  ZH:   * 接下来你怎么不走人呢，啊，小混混？

## SC4d515f67e08dadbd | nsfw | datadf/all.ds | AreaB_Macsen2.Talk.macsenmoneycode3
CONTROL L813  <AreaB_Macsen2.Talk.macsenmoneycode3>
ROW CAT:O40133063a8082c0c2cf6 L814 * physical_line
  EN: Grrrr.... some folks are just absolutely SHAMELESS!
  ZH:   * 呜……有些家伙简直太不要脸了！
ROW CAT:O3a42054169241bbc81bf L815 * physical_line
  EN: Why don't you just take EVERYTHING you can get your hands on? Huh?
  ZH:   * 你怎么不干脆把能拿到的东西全拿走啊？嗯？
ROW CAT:Obc152f96c1e1c62594ed L816 * physical_line
  EN: Go on, do it! GEKKYZAA!!!!
  ZH:   * 来啊，拿啊！GEKKYZAA!!!!
CONTROL L818  ### shared ###

## SC8e1891c2afe8f0f4 | sfw | datadm/all.ds | AreaB_MacsenBar.Talk.main
CONTROL L864  <AreaB_MacsenBar.Talk.main>
CONTROL L865    if { !f(ClassicWerepup_defeated)} {
ROW SFW3cfe260ac81f09365e890955 L866 - physical_line
  EN: You're kinda early! Come back later and we can chat and drink, alright?
  ZH:     * 你来得有点早！晚点再来，咱们喝点东西聊聊天，好吗？
CONTROL L867    } else {
ROW SFW813d9e6f9b98ee0d31717499 L868 - physical_line
  EN: Well! That last quake just wrecked my whole supply!
  ZH:     * 唉！上次地震把我的存货全毁了！
ROW SFW1dca95baa313485f1a1b75c6 L869 - physical_line
  EN: I'll tell you what though, you seem like you're a good strong pupper.
  ZH:     * 不过说真的，你看着是只挺棒又壮实的狗狗。
ROW SFW46d5c882c95a6161d155409c L870 - physical_line
  EN: Another one of you cosmofellas came by muttering that they left 
  ZH:     * 之前还来过一个跟你一样的太空伙计，嘴里嘀咕着说把武器落在这儿正北边了！ 
ROW SFW0fb32b20f6ae7a6ba347309c L871 - physical_line
  EN: their weapon just north of here!
  ZH: 
ROW SFWd2aeafee6a77e66f3789ec10 L872 - physical_line
  EN: "Bottom, middle, middle, top..." is what they kept saying, whatever that means!
  ZH:     * 那家伙一直念叨着"下、中、中、上……"，谁知道是什么意思！
CONTROL L873    }

## SC8da20c884060ed70 | nsfw | datadm/all.ds | AreaB_Prison1.CancelPurchase
CONTROL L942  <AreaB_Prison1.CancelPurchase>
ROW CAT:Oc599bd8dc1bae793c9de L943 * physical_line
  EN: Hey, if you're not gonna help... then at least stop watching!
  ZH:   * 喂，你要是不打算帮忙……那至少别在旁边看了！

## SC15002909f5a86e3c | sfw | datadm/all.ds | AreaB_Prison1.Goodbye
CONTROL L920  <AreaB_Prison1.Goodbye>
ROW SFWcb468a15e58ae0bce2f9d21c L921 - physical_line
  EN: I'll be right behind you!
  ZH:   * 我马上跟在你后面！

## SC59c9c812aacf574a | nsfw | datadf/all.ds | AreaB_Prison1.GoodbyeNotRescued
CONTROL L920  <AreaB_Prison1.GoodbyeNotRescued>
ROW CAT:O2eda83f69d7741b598c3 L921 * physical_line
  EN: Bye bye! Take as much time as ya need!
  ZH:   * 拜拜啦！你要花多少时间都行！

## SCca415f75e217575d | nsfw | datadf/all.ds | AreaB_Prison1.HelloDog
CONTROL L923  <AreaB_Prison1.HelloDog>
ROW CAT:Oae59f05014b76ae46aeb L924 * physical_line
  EN: Huh? Oh. It's... a female...
  ZH:   * 啊？哦。是……是个母的……

## SCcb9dabb59faa274f | sfw | datadm/all.ds | AreaB_Prison1.HelloDog
CONTROL L926  <AreaB_Prison1.HelloDog>
ROW SFWd82dba9d62058e323fd6be66 L927 - physical_line
  EN: Oh, it's a little dog?
  ZH:   * 哦，是只小狗？

## SC575aba8343f18041 | nsfw | datadf/all.ds | AreaB_Prison1.NoBoneForDog
CONTROL L926  <AreaB_Prison1.NoBoneForDog>
ROW CAT:Oe96be9b580092421f9ec L927 * physical_line
  EN: Watch who you're ogling, bitch!! This is *my* man!
  ZH:   * 眼睛往哪儿瞟呢，贱货！！这是*我的*男人！

## SCe380d21ef6b387eb | nsfw | datadm/all.ds | AreaB_Prison1.NoBoneForDog
CONTROL L932  <AreaB_Prison1.NoBoneForDog>
ROW CAT:O9cb271d6997e747d9ae1 L933 * physical_line
  EN: You'll just have to wait your turn!
  ZH:   * 那就只好等着轮到你吧！
ROW CAT:O9ebf26ac313d8e2e5fc5 L934 * physical_line
  EN: Huh? Are you a good dog? Can you go get someone to help?
  ZH:   * 嗯？你是条好狗狗吗？能去找人来帮忙吗？

## SCb677f434b7a90bf2 | nsfw | datadf/all.ds | AreaB_Prison1.Purchased
CONTROL L941  <AreaB_Prison1.Purchased>
ROW CAT:O092005765c599423fc7c L942 * physical_line
  EN: Hey! You didn't have to bang his head like that. Poor guy!
  ZH:   * 喂！你没必要那样砸他脑袋吧。可怜的家伙！

## SCe15ed5424180beb7 | sfw | datadf/all.ds | AreaB_Prison1.Purchased
CONTROL L942  <AreaB_Prison1.Purchased>
ROW SFW8b155c944ac58928306addee L943 - physical_line
  EN: Wow! My heroine!
  ZH:   * 哇！我的女英雄！

## SC8e515bd8c97a8616 | nsfw | datadm/all.ds | AreaB_Prison1.Rescue
CONTROL L945  <AreaB_Prison1.Rescue>
ROW CAT:O331b15bb2131c5828ab3 L946 * physical_line
  EN: I've just- nh... just about got this situation under control!
  ZH:   * 我刚刚——唔……就快把局面控制住了！
ROW CAT:O0385bdcc11de7768f250 L947 * physical_line
  EN: But I could use a little help, I guess...
  ZH:   * 不过嘛……我想我也需要一点帮忙……

## SCb70e13308317f927 | nsfw | datadm/all.ds | AreaB_Prison1.SoldOut
CONTROL L952  <AreaB_Prison1.SoldOut>
ROW CAT:Oe42b6640e6a11b123147 L953 * physical_line
  EN: I... think I can handle this from here.
  ZH:   * 我……我想剩下的我自己能应付了。

## SCc178ef1afaa3aa6f | nsfw | datadf/all.ds | AreaB_Prison1.TalkAfterRescue.thanks
CONTROL L951  <AreaB_Prison1.TalkAfterRescue.thanks>
ROW CAT:Occd276f776a380158439 L952 * physical_line
  EN: Do you think command would let me take him along?
  ZH:   * 你觉得指挥部会让我把他一起带走吗？

## SC7537d17bb139b23d | sfw | datadf/all.ds | AreaB_Prison1.TalkAfterRescue.thanks
CONTROL L952  <AreaB_Prison1.TalkAfterRescue.thanks>
ROW SFWfdddcdc835bd87d78fe0b208 L953 - physical_line
  EN: I'll see you back at the hangar!
  ZH:   * 我们回机库再见！

## SCf698a61c0f875f22 | sfw | datadm/all.ds | AreaB_Prison1.TalkBeforeRescue.bopped
CONTROL L951  <AreaB_Prison1.TalkBeforeRescue.bopped>
ROW SFWa0ee41c1502fd705a00e95fc L952 - physical_line
  EN: I'm - hmf - trying to access the electronics for this door.
  ZH:   * 我在——哼——想办法接上这扇门的电子线路。
ROW SFW2469e2f5478d365c7fdda287 L953 - physical_line
  EN: But it's a little tougher than I expected.
  ZH:   * 不过比我想的难了一点。

## SC90779c451a4d6d33 | nsfw | datadf/all.ds | AreaB_Prison2.CancelPurchase
CONTROL L975  <AreaB_Prison2.CancelPurchase>
CONTROL L976    if { hasItem(Key) } {
ROW CAT:O87d42180f80e114310cc L977 * physical_line
  EN: Don't tease me... please... just turn this thing oooooff!
  ZH:     * 别逗我了……求你了……快把这东西关——掉！
CONTROL L978    } else {
ROW CAT:Ob03aafa1c5d5389914ce L979 * physical_line
  EN: You'll need a key! I've... aaahng! T-tried everything...
  ZH:     * 你需要钥匙！我……啊嗯！什、什么都试过了……
CONTROL L980    }

## SC114e8af6578f9a3d | nsfw | datadm/all.ds | AreaB_Prison2.Goodbye
CONTROL L964  <AreaB_Prison2.Goodbye>
ROW CAT:O6eefafe103bf39df0450 L965 * physical_line
  EN: Hmph! They'll just graduate anyone these days...
  ZH:   * 哼！如今这年头，什么人都能毕业了……

## SCf4f2941f270334cf | nsfw | datadf/all.ds | AreaB_Prison2.Goodbye
CONTROL L956  <AreaB_Prison2.Goodbye>
ROW CAT:O8b9be62e7d2a63333d6b L957 * physical_line
  EN: I'm heading back to the hangar. Think I've had enough of this mission!
  ZH:   * 我回机库去了。这任务我算是受够了！

## SC9a02f7ad1afb83d5 | nsfw | datadf/all.ds | AreaB_Prison2.GoodbyeDog
CONTROL L969  <AreaB_Prison2.GoodbyeDog>
ROW CAT:O2e9e2c2477c18a299937 L970 * physical_line
  EN: Come back... uhn... soon! I c-aah...can't take much moooore!
  ZH:   * 快回来……嗯……快点回来！我、啊……撑不了多——久——啦！

## SC315caea10649eed6 | sfw | datadf/all.ds | AreaB_Prison2.GoodbyeNotRescued
CONTROL L960  <AreaB_Prison2.GoodbyeNotRescued>
ROW SFWa7f135e961f419772ece17bf L961 - physical_line
  EN: C-c'mon, you've *got* to get me out of here! You don't know what it's like! 
  ZH:   * 拜、拜托，你*一定*得把我救出去！你不知道这里有多难熬！ 
ROW SFW98a4f43b1675af44d3e0fc53 L962 - physical_line
  EN: I wanna run and jump, but I've been cooped up here for weeks...!
  ZH:   * 我想跑跑跳跳，可我已经被关在这里好几个星期了……！

## SC1a4f9a9997aa01ae | sfw | datadf/all.ds | AreaB_Prison2.Hello
CONTROL L954  <AreaB_Prison2.Hello>
ROW SFW87160a68f43aad2716e44b8f L955 - physical_line
  EN: Ooohhh! You're a sight for sore eyes!
  ZH:   * 哦哦哦！见到你可真是太好了！

## SC6f76dfacc583b773 | nsfw | datadf/all.ds | AreaB_Prison2.HelloDog
CONTROL L963  <AreaB_Prison2.HelloDog>
ROW CAT:O3c7552a3dcdeaee299c3 L964 * physical_line
  EN: Aahn... I... a dog?!
  ZH:   * 啊嗯……我、一条狗？！

## SCf26b5d8323f8d69f | nsfw | datadm/all.ds | AreaB_Prison2.NoBoneForDog
CONTROL L973  <AreaB_Prison2.NoBoneForDog>
ROW CAT:O28d7ca8461c25f4430f8 L974 * physical_line
  EN: Go on, get out of here mutt!
  ZH:   * 去去，从这儿滚出去，杂种狗！

## SCb748631be660b437 | nsfw | datadm/all.ds | AreaB_Prison2.NotEnoughMoney
CONTROL L992  <AreaB_Prison2.NotEnoughMoney>
ROW CAT:O88d28a17643775a45cd1 L993 * physical_line
  EN: What?! You don't have a key?!
  ZH:   * 什么？！你连钥匙都没有？！
ROW CAT:Ob7bd05f851a6440225e3 L994 * physical_line
  EN: Why, of all the incompetent-! Well, go and fetch one immediately!
  ZH:   * 怎么会这么没用——！好吧，马上去弄一把来！

## SCbd8653da68db25c0 | nsfw | datadm/all.ds | AreaB_Prison2.Rescue
CONTROL L986  <AreaB_Prison2.Rescue>
ROW CAT:Od4e389d08af3756d5860 L987 * physical_line
  EN: Stop standing around like you're fresh out of the academy and free me!
  ZH:   * 别像个刚出学院的新手似的傻站着，快放开我！

## SC0dd90a60521749d2 | nsfw | datadm/all.ds | AreaB_Prison2.SoldOut
CONTROL L996  <AreaB_Prison2.SoldOut>
ROW CAT:O5cc34cb9139e9df84316 L997 * physical_line
  EN: Your assistance is no longer needed, rookie.
  ZH:   * 不需要你的协助了，菜鸟。
ROW CAT:O3f1f83dc7670f0118bcc L998 * physical_line
  EN: You've already done enough, I assure you!
  ZH:   * 我保证，你已经做得够多了！

## SC72deb44475114949 | nsfw | datadf/all.ds | AreaB_Prison2.TalkBeforeRescue.bopped
CONTROL L995  <AreaB_Prison2.TalkBeforeRescue.bopped>
ROW CAT:O08c9cda6b496d79ad476 L996 * physical_line
  EN: These roboguys never, nh... ever stop breeding...!
  ZH:   * 这些机器人，嗯……一直操个不停……！
ROW CAT:O6b5c468a2e23938dd4b4 L997 * physical_line
  EN: I'm way past muh... ahn... my limit! Please, help me!
  ZH:   * 我早就超过……啊嗯……极限了！求你，救救我！

## SCf8381ccaf779d65a | nsfw | datadm/all.ds | AreaB_Prison2.TalkBeforeRescue.bopped
CONTROL L1000  <AreaB_Prison2.TalkBeforeRescue.bopped>
ROW CAT:O2e0808c463b507cf1e5e L1001 * physical_line
  EN: A few of the locals caught me in a dastardly sneak attack.
  ZH:   * 几个当地人卑鄙地偷袭，把我逮住了。
ROW CAT:Oebf9af1541e044844e81 L1002 * physical_line
  EN: They got lucky - ahem - *were* lucky to catch me off guard.
  ZH:   * 它们运气好——咳——*是*走运，趁我没防备。

## SCb68d08f30924b5b6 | sfw | datadm/all.ds | AreaB_Prison2.TalkBeforeRescue.bopped
CONTROL L996  <AreaB_Prison2.TalkBeforeRescue.bopped>
ROW SFW1d98fee67d7581dbb8cd2fb2 L997 - physical_line
  EN: A few of the locals caught me in a dastardly sneak attack.
  ZH:   * 几个当地人卑鄙地偷袭，把我逮住了。
ROW SFWaebc20ef9a5b9799bbaa68e0 L998 - physical_line
  EN: By the time I came to, they'd locked me up in here. The cowards!
  ZH:   * 等我醒过来，他们就已经把我关在这里了。一群胆小鬼！

## SC8f42cac7bc15fdab | nsfw | datadf/all.ds | AreaB_Slaver2.CancelPurchase
CONTROL L1023  <AreaB_Slaver2.CancelPurchase>
ROW CAT:Ocbfa0cc01a9abd4faa84 L1024 * physical_line
  EN: Well are you buying or not? Don't waste my time...
  ZH:   * 到底买不买？别浪费我时间……

## SC4d5d49be46ffc893 | nsfw | datadf/all.ds | AreaB_Slaver2.FakeDrumstick
CONTROL L1036  <AreaB_Slaver2.FakeDrumstick>
ROW CAT:O96043ff13599b3f0aad8 L1037 * physical_line
  EN: The slaves always gimme lip about the flies. Extra protein, I say!
  ZH:   * 奴隶老跟我抱怨苍蝇。我说这叫加餐补蛋白！

## SC3dd9e5d92c2ffe30 | nsfw | datadf/all.ds | AreaB_Slaver2.HelloDog
CONTROL L1066  <AreaB_Slaver2.HelloDog>
ROW CAT:O055a52d268928511cdf3 L1067 * physical_line
  EN: What the-? A dog?!
  ZH:   * 什么鬼——？一条狗？！

## SC90ea2f5911853c41 | nsfw | datadm/all.ds | AreaB_Slaver2.Purchased
CONTROL L1020  <AreaB_Slaver2.Purchased>
CONTROL L1021    if { !koboCostume() } {
ROW CAT:Od8912aa6cbf6483c6aba L1022 * physical_line
  EN: Remember, no refunds! What else you need? He! He! He!
  ZH:     * 记住，概不退款！还要点啥？嘿！嘿！嘿！
CONTROL L1023    } else {
ROW CAT:O26ac203af6dbe3fea580 L1024 * physical_line
  EN: Thanks for taking that off my hands.
  ZH:     * 多谢你帮我把这东西脱手。
ROW CAT:Ofd343e118a77e509c064 L1025 * physical_line
  EN: They get a bit uppity at 3P stations when you gots stolen equipment...
  ZH:     * 带着偷来的装备去3P空间站，他们可会摆臭脸……
CONTROL L1026    }

## SC10e696e4c411f828 | nsfw | datadm/all.ds | AreaB_Slaver2.SoldOut
CONTROL L1031  <AreaB_Slaver2.SoldOut>
ROW CAT:O67415d4e42c9fcc6d06c L1032 * physical_line
  EN: You stupid or something?! That was my last one!
  ZH:   * 你是不是傻？！那是最后一个了！

## SCf71b45fc6b085887 | nsfw | datadm/all.ds | AreaB_Slaver2.Talk.junk
CONTROL L1059  <AreaB_Slaver2.Talk.junk>
CONTROL L1060    if { koboCostume() } {
ROW CAT:O5b49428a40a73c99a051 L1061 * physical_line
  EN: All the cosmo-junk I sell has a story behind it.
  ZH:     * 我卖的每件宇宙破烂，背后都有段故事。
ROW CAT:Oec8230ff8fbe28d7b998 L1062 * physical_line
  EN: Reeeall good stories, heh-heh...
  ZH:     * 那可都是绝——妙的故事，嘿嘿……
CONTROL L1063    }

## SC0779a316abbdac12 | nsfw | datadf/all.ds | AreaB_Slaver2.Talk.spacebrats
CONTROL L1043  <AreaB_Slaver2.Talk.spacebrats>
CONTROL L1044    if { !koboCostume() } {
ROW CAT:O0ae397f3cfa9f3b1844f L1045 * physical_line
  EN: Business been pretty good lately, what with all you spacebrats wandering around.
  ZH:     * 最近生意可不错，全靠你们这帮太空崽子到处乱跑。
CONTROL L1046    }
CONTROL L1048  ### as kobo

## SCc32c2e652b675bd9 | nsfw | datadf/all.ds | AreaB_Slaver2.TazerAttuned
CONTROL L1049  <AreaB_Slaver2.TazerAttuned>
ROW CAT:Oe6909d38156d57a28d1e L1050 * physical_line
  EN: This here? One of them tazers those cute lil spacebrats carry around.
  ZH:   * 这个？就是那帮可爱太空崽子随身带的电击枪。
ROW CAT:O19df78013f232b75a03c L1051 * physical_line
  EN: Seemed like a pretty good one, until we broke it... the tazer, I mean.
  ZH:   * 看着挺不错，可惜被我们玩坏了……我是说电击枪。
ROW CAT:O737c1df4fce308d0b127 L1052 * physical_line
  EN: But the scrap alone will go for a thousand lect, off world. How about it?
  ZH:   * 不过光是这些废料，拿到外星都能卖一千LECT。怎么样？

## SCc4c547603e445346 | sfw | datadf/all.ds | AreaB_Slaver2.TazerAttuned
CONTROL L1050  <AreaB_Slaver2.TazerAttuned>
ROW SFWa7143f46f2b70eb907052c7e L1051 - physical_line
  EN: This here? One of them tazers those cute lil spacebrats carry around.
  ZH:   * 这个？就是那帮可爱太空崽子随身带的电击枪。
ROW SFW6867f33e9cd0e981866d993a L1052 - physical_line
  EN: A real primo, high end model too... except it's broken.
  ZH:   * 还是顶级的高端型号呢……只可惜坏了。
ROW SFW75baaa8071eb4bd4ae10556a L1053 - physical_line
  EN: But the scrap alone will go for a thousand lect, off world. How about it?
  ZH:   * 不过光是这些废料，拿到外星都能卖一千LECT。怎么样？

## SC893f2c12fec594c2 | nsfw | datadm/all.ds | AreaC_Macsen1.PsyUp
CONTROL L1136  <AreaC_Macsen1.PsyUp>
ROW CAT:Odf5f6f464d39fc444177 L1137 * physical_line
  EN: A real live psy crystal, just like those espers use!
  ZH:   * 货真价实的精神力水晶，跟那些超能力者用的一样！

## SCa2ade667e4f6878c | nsfw | datadm/all.ds | AreaC_Macsen1.Talk.forest1
CONTROL L1142  <AreaC_Macsen1.Talk.forest1>
ROW CAT:O48ba11d1dcd7654476a8 L1143 * physical_line
  EN: I know I look like a Space Pirate, but I'm really just a dog like you!
  ZH:   * 我知道自己像太空海盗，但我跟你一样只是条狗！
ROW CAT:Ob4217b64a868c2c16a09 L1144 * physical_line
  EN: If you get a full set of Kobo gear, you could fool people too.
  ZH:   * 要是弄到一整套科博装备，你也能骗过别人。

## SCd1a411a88bb6c1af | nsfw | datadm/all.ds | AreaC_Macsen1.Talk.forest2
CONTROL L1146  <AreaC_Macsen1.Talk.forest2>
ROW CAT:Ofd0511c5185fea040391 L1147 * physical_line
  EN: The scariest part about this outfit...
  ZH:   * 这身行头最吓人的地方……
ROW CAT:O19b0e96a132baa5d72d5 L1148 * physical_line
  EN: ...is that sometimes the zipper gets stuck!
  ZH:   * ……就是拉链有时候会卡住！

## SC738bff3e5f7a8cef | nsfw | datadm/all.ds | AreaC_Macsen1.Talk.forest3
CONTROL L1150  <AreaC_Macsen1.Talk.forest3>
ROW CAT:Oc4be6190f907e31b0065 L1151 * physical_line
  EN: Don't forget to take some food for your pets!
  ZH:   * 别忘了给你的宠物带点吃的！
CONTROL L1153  ### shared ###

## SC57f5de37f83ba432 | nsfw | datadf/all.ds | AreaC_MacsenDark.DarkNoPurchase
CONTROL L1195  <AreaC_MacsenDark.DarkNoPurchase>
ROW CAT:O141ce9751f1fcebb4fe1 L1196 * physical_line
  EN: Look buddy, if I could see where anything is I'd gladly sell that to you
  ZH:   * 听着，老兄，要是我能看清东西在哪儿，我很乐意卖给你，但我每次一动，好像都会踩到什——嗷呜！
ROW CAT:Ofe9d4039cd8b91ca96a8 L1197 * physical_line
  EN: But every time I move I seem to step on somethi-YEOWCH!
  ZH: 
ROW CAT:Off09ae0a3109a0cf1172 L1198 * physical_line
  EN: Nope, no sales until the lights are back on. Sorry!
  ZH:   * 不行，灯亮之前不卖东西。抱歉！

## SCe1840409be9c48fb | nsfw | datadm/all.ds | AreaC_MacsenDark.Goodbye
CONTROL L1198  <AreaC_MacsenDark.Goodbye>
ROW CAT:O3bb706c702653a88c83f L1199 * physical_line
  EN: If you come across a lantern or something, come share some light with me, eh?
  ZH:   * 要是找到灯笼什么的，就来给我也照个亮，好吗？

## SC88b6f218321c8753 | sfw | datadm/all.ds | AreaC_MacsenDark.Hello
CONTROL L1190  <AreaC_MacsenDark.Hello>
ROW SFW051e0ff7ef01146daf0feed5 L1191 - physical_line
  EN: And here you are, to brighten up my day!
  ZH:   * 你一来，我这一天都亮堂了！
ROW SFW2a78dbb5b9686e3c085e2686 L1192 - physical_line
  EN: You and that torch are lifesavers.
  ZH:   * 你和那支手电筒真是救星。

## SC315078d27c77e498 | nsfw | datadf/all.ds | AreaC_MacsenDark.HelloDark
CONTROL L1184  <AreaC_MacsenDark.HelloDark>
ROW CAT:Of962ae415a89a00387b8 L1185 * physical_line
  EN: Oh hey! Sorry, I didn't see you come in there.
  ZH:   * 哦嘿！抱歉，我没看见你走进来。
ROW CAT:O9e76f656adfa7a98ad1b L1186 * physical_line
  EN: ...in fact, I can't see anything! It's too dark!
  ZH:   * ……其实我什么都看不见！这里太黑了！

## SCba0930245e8d717d | sfw | datadm/all.ds | AreaC_MacsenDark.Talk.dark
CONTROL L1212  <AreaC_MacsenDark.Talk.dark>
CONTROL L1213    if { !hasItem(SpecialTorch) } {
ROW SFW81f74bbe58471ca68fe82c26 L1214 - physical_line
  EN: This is just my luck, isn't it? 
  ZH:     * 我的运气还真是好啊，是吧？ 
ROW SFWdefa9e20df8302657abc8a22 L1215 - physical_line
  EN: First somewan stole my hookshot so I have to walk around on these tiny legs...
  ZH:     * 先是有人偷了我的钩索，害我只能靠这两条小短腿走路……
ROW SFW0b646b6839a880ebfa50a51d L1216 - physical_line
  EN: ...and now the power is out and my flashlight is missing! Bah!
  ZH:     * ……而现在又停电了，手电筒也不见了！哼！
CONTROL L1217    } else {
ROW SFW45958703a70d55754b3782f1 L1218 - physical_line
  EN: It's been getting ruffer and ruffer to do business around these parts, let me tell ya.
  ZH:     * 跟你说吧，在这一带做生意是越来越难了。
ROW SFWb3ce16c814d25f6e05d8c481 L1219 - physical_line
  EN: Earthquakes happen every other hour and the monsters are rowdier than ever...
  ZH:     * 隔一个小时就地震一次，魔物也比以前更闹腾了……
ROW SFW03d546ba619204f3a745d8bd L1220 - physical_line
  EN: ...it almost feels like things are building up to something!
  ZH:     * ……总觉得好像有什么大事要发生了！
CONTROL L1221    }

## SC51109c2b6493fd40 | sfw | datadm/all.ds | AreaC_Prison1.CancelPurchase
CONTROL L1289  <AreaC_Prison1.CancelPurchase>
ROW SFWa92e8a3644a9929f1f3bc3e0 L1290 - physical_line
  EN: P-please! I'm askin' ya real nice-like!
  ZH:   * 拜、拜托！我都这么客客气气地求你了！

## SC75e95d0e94930f6f | nsfw | datadm/all.ds | AreaC_Prison1.Goodbye
CONTROL L1275  <AreaC_Prison1.Goodbye>
ROW CAT:Odcde23e04ea9ec73215c L1276 * physical_line
  EN: Be seein' ya!
  ZH:   * 回头见啦！

## SCc6bf1eab3e794b63 | nsfw | datadf/all.ds | AreaC_Prison1.GoodbyeNotRescued
CONTROL L1272  <AreaC_Prison1.GoodbyeNotRescued>
ROW CAT:O77cd494277e39fba19f0 L1273 * physical_line
  EN: Really? Trust me girl, you *don't* want to get on my bad side.
  ZH:   * 真要这样？相信我，姑娘，你*绝对不会*想惹恼我的。

## SC937701d5b4d26497 | nsfw | datadm/all.ds | AreaC_Prison1.HelloDog
CONTROL L1281  <AreaC_Prison1.HelloDog>
ROW CAT:Oc80884aaafba7a880327 L1282 * physical_line
  EN: Well hii there, little doggy!
  ZH:   * 哎呀，你好呀，小狗狗！ 

## SC57bf16d73e55ce26 | nsfw | datadf/all.ds | AreaC_Prison1.NoBoneForDog
CONTROL L1278  <AreaC_Prison1.NoBoneForDog>
ROW CAT:O830b4f8509527cd01611 L1279 * physical_line
  EN: Are you gonna make yourself useful and go get help, or just stand there?
  ZH:   * 你是打算帮点忙去找人来，还是就这么站着？

## SC5ed42bd96deffabb | nsfw | datadf/all.ds | AreaC_Prison1.Purchased
CONTROL L1293  <AreaC_Prison1.Purchased>
ROW CAT:Oa2dc990d27c43185d483 L1294 * physical_line
  EN: Finally! I've been cooped up in here forever!
  ZH:   * 终于！我被关在这鬼地方都这么久了！

## SC5234a6bd294fef4e | sfw | datadm/all.ds | AreaC_Prison1.Purchased
CONTROL L1295  <AreaC_Prison1.Purchased>
ROW SFW753ebbafc025b6a1a1cef0e8 L1296 - physical_line
  EN: Thankyah kindly!
  ZH:   * 真是太感谢你啦！

## SCa3b719e08b22fe40 | nsfw | datadm/all.ds | AreaC_Prison1.Rescue
CONTROL L1296  <AreaC_Prison1.Rescue>
ROW CAT:Of535660610aae08766ef L1297 * physical_line
  EN: I've been cooped up here for stars knows how long. Can ya gimme me a hand?
  ZH:   * 只有星星才知道我被关在这儿多久了。能帮我一把吗？

## SC149a53d5368207b4 | nsfw | datadm/all.ds | AreaC_Prison1.TalkBeforeRescue.bopped
CONTROL L1305  <AreaC_Prison1.TalkBeforeRescue.bopped>
ROW CAT:O06336c85f36eb562b24a L1306 * physical_line
  EN: I'm... ahn... feelin' the energy from some kinda strange F.A.P jewel.
  ZH:   * 我……嗯啊……感到某种奇怪F.A.P宝石的能量。
ROW CAT:Od04271cb2e20e44fd4b7 L1307 * physical_line
  EN: In addition to my... ah... mortifyin' predicament here!
  ZH:   * 再加上我在这儿……啊……这难堪的处境！

## SC06b361bb8cfb2102 | sfw | datadm/all.ds | AreaC_Prison2.Goodbye
CONTROL L1309  <AreaC_Prison2.Goodbye>
ROW SFW73a801ed728a3334de09bad3 L1310 - physical_line
  EN: Just wait 'til I find my tazer again, those elves won't know what hit 'em!
  ZH:   * 等我找回电击器，那些精灵连自己怎么挨打的都不会知道！

## SC1b5714b5a3c49c78 | nsfw | datadm/all.ds | AreaC_Prison2.GoodbyeNotRescued
CONTROL L1317  <AreaC_Prison2.GoodbyeNotRescued>
ROW CAT:O301e153786f8732fc8bf L1318 * physical_line
  EN: Mmmm... Mm-hm...?
  ZH:   * 唔嗯……嗯哼……？

## SC4b1c604ace9893cc | nsfw | datadf/all.ds | AreaC_Prison2.GoodbyeNotRescued
CONTROL L1312  <AreaC_Prison2.GoodbyeNotRescued>
ROW CAT:Ofc6ecb1a6f460ab50854 L1313 * physical_line
  EN: Mmmn-hmm mmf! <3
  ZH:   * 唔嗯-嗯 唔姆！<3

## SC62f4caca55d74810 | sfw | datadm/all.ds | AreaC_Prison2.GoodbyeNotRescued
CONTROL L1312  <AreaC_Prison2.GoodbyeNotRescued>
ROW SFW471d86099f15fe79cc6e3e55 L1313 - physical_line
  EN: I'll break out of here myself!
  ZH:   * 我自己会逃出去的！

## SC83f3ea3a5b56c243 | nsfw | datadm/all.ds | AreaC_Prison2.Hello
CONTROL L1311  <AreaC_Prison2.Hello>
ROW CAT:O85f51834a4636108b975 L1312 * physical_line
  EN: Hmf... mm-mmph! Mmm!
  ZH:   * 唔夫……唔、唔姆！唔姆！

## SCe7c049200f8861f7 | sfw | datadm/all.ds | AreaC_Prison2.Hello
CONTROL L1306  <AreaC_Prison2.Hello>
ROW SFW12d266d813dc80525188d62e L1307 - physical_line
  EN: Oh hi there! I'm not really in trouble, it just looks like it!
  ZH:   * 哦，你好！我其实没遇上麻烦，只是看起来像而已！

## SC9cc5ba0032acaa45 | sfw | datadm/all.ds | AreaC_Prison2.HelloDog
CONTROL L1315  <AreaC_Prison2.HelloDog>
ROW SFWa87986b0aa9a3426aa6b52d5 L1316 - physical_line
  EN: Oh, it's a dog!
  ZH:   * 哦，是只狗！

## SCaeda1b9a591b8675 | sfw | datadm/all.ds | AreaC_Prison2.NoBoneForDog
CONTROL L1318  <AreaC_Prison2.NoBoneForDog>
ROW SFWcfd7ca81281ae918dd2486c9 L1319 - physical_line
  EN: Do you wanna keep me company while I think of how to break outta here, boy?
  ZH:   * 小伙子，要不要陪陪我，等我想出逃出去的办法？

## SC7f72e120af9846b2 | nsfw | datadm/all.ds | AreaC_Prison2.Purchased
CONTROL L1338  <AreaC_Prison2.Purchased>
ROW CAT:O9d4a368dfed6c0b43aa4 L1339 * physical_line
  EN: Aaa... hhaaa... thuh... thank you!
  ZH:   * 啊……哈啊……谢、谢谢你！

## SC4ad0b612b466ff69 | sfw | datadf/all.ds | AreaC_Prison2.Purchased
CONTROL L1334  <AreaC_Prison2.Purchased>
ROW SFWa4f47838211e65d828cfa61f L1335 - physical_line
  EN: Meep... guess you're telling me to get back to work...
  ZH:   * 呜……看来你是叫我回去工作啊……

## SCf80609c65d3dbd64 | nsfw | datadf/all.ds | AreaC_Prison2.Rescue
CONTROL L1330  <AreaC_Prison2.Rescue>
ROW CAT:O68308b22d608c873ff64 L1331 * physical_line
  EN: Mmmnh?! Mmmmphhmmm!!
  ZH:   * 唔嗯？！唔姆姆嗯！！

## SC3d900e9cb5bc790a | nsfw | datadm/all.ds | AreaC_Prison2.TalkBeforeRescue.bopped
CONTROL L1344  <AreaC_Prison2.TalkBeforeRescue.bopped>
ROW CAT:Oa0600298456faa9ca5b4 L1345 * physical_line
  EN: Mn-nhm... mmmphm... Mph-nnnh!
  ZH:   * 嗯、唔……唔嗯……唔、嗯啊！
ROW CAT:O5194430ed8f7c854195b L1346 * physical_line
  EN: Mmmm nnnhf!
  ZH:   * 嗯嗯，唔嗯！

## SC77978ba72435cfdd | sfw | datadm/all.ds | AreaC_Prison2.TalkBeforeRescue.bopped
CONTROL L1339  <AreaC_Prison2.TalkBeforeRescue.bopped>
ROW SFW6e8facbbc59d20adf9547bda L1340 - physical_line
  EN: I was single-pawwedly conquering the elven empire here.
  ZH:   * 我本来正在单爪征服这里的精灵帝国。
ROW SFW7cea4aa399f7ff4a49c63e58 L1341 - physical_line
  EN: But I hit a little setback. Nothing for a trainee like you to worry over!
  ZH:   * 不过遇到了一点挫折。用不着你这样的见习生操心！

## SC172035613542f565 | nsfw | datadf/all.ds | AreaC_Prison3.GoodbyeNotRescued
CONTROL L1352  <AreaC_Prison3.GoodbyeNotRescued>
ROW CAT:O74d39269c003ff6b0147 L1353 * physical_line
  EN: I'm not in like, a hurry, you know? You could totally come back whenever!
  ZH:   * 我又不着急，你知道吗？你随时都可以再回来的！

## SCf42cc448ed037c7d | nsfw | datadf/all.ds | AreaC_Prison3.NoBoneForDog
CONTROL L1358  <AreaC_Prison3.NoBoneForDog>
ROW CAT:O83f052e809cce0f40bec L1359 * physical_line
  EN: Are you gonna be a buddy and go get someone with a key?
  ZH:   * 你要不要当个好伙伴，去叫个有钥匙的人来？

## SCa6c44bc03317898b | nsfw | datadf/all.ds | AreaC_Prison3.NotEnoughMoney
CONTROL L1380  <AreaC_Prison3.NotEnoughMoney>
ROW CAT:Oaa47a377b951f58f1c56 L1381 * physical_line
  EN: You're gonna need like, a key, you know...?
  ZH:   * 你得有把钥匙才行，懂吧……？

## SC608ff9ff4a9a982a | nsfw | datadf/all.ds | AreaC_Prison3.SoldOut
CONTROL L1383  <AreaC_Prison3.SoldOut>
ROW CAT:Oab6417bbd92578a72177 L1384 * physical_line
  EN: Girl, the door's like, already unlocked?
  ZH:   * 妹子，这门不是早就开着的吗？
ROW CAT:Of292a8da1dfe2e99e900 L1385 * physical_line
  EN: Don't worry about me, I'm just saying bye-bye to my tentacle buddies.
  ZH:   * 别担心我，我在跟我的触手伙伴们说再见。

## SC68278d342b014e81 | sfw | datadf/all.ds | AreaC_Prison3.SoldOut
CONTROL L1384  <AreaC_Prison3.SoldOut>
ROW SFW4b6aba06e180e3f7ff63d57d L1385 - physical_line
  EN: Girl, the door's like, already unlocked?
  ZH:   * 妹子，这门不是早就开着的吗？
ROW SFW488e415590ba15509edeb3f1 L1386 - physical_line
  EN: Don't worry about me, I'll be along later.
  ZH:   * 别担心我，我待会儿就跟上。

## SCe369de7bd5d76fd9 | sfw | datadm/all.ds | AreaC_Prison3.SoldOut
CONTROL L1384  <AreaC_Prison3.SoldOut>
ROW SFW0bd683c51db72b3c0b168edf L1385 - physical_line
  EN: The lock's open. Maybe go find someone else to rescue...?
  ZH:   * 锁已经开了。不如去找其他人救……？

## SCc994ada55704cf82 | nsfw | datadf/all.ds | AreaC_Prison3.TalkAfterRescue.thanks
CONTROL L1391  <AreaC_Prison3.TalkAfterRescue.thanks>
ROW CAT:O64c01e41e68f7ee60d99 L1392 * physical_line
  EN: You know, I'm gonna miss hanging out here with these wiggly buddies for real...
  ZH:   * 你知道吗，我真的会想念在这儿和这些扭来扭去的小伙伴们待在一起……

## SCfb40649184a4a38a | nsfw | datadm/all.ds | AreaC_Slaver1.FakeMeat
CONTROL L1448  <AreaC_Slaver1.FakeMeat>
ROW CAT:O749c73d8511f7b0cec61 L1449 * physical_line
  EN: Oh? You want to try my special meat?
  ZH:   * 哦？想尝尝我的特制肉？
ROW CAT:Offd2634e3cce5aedcec6 L1450 * physical_line
  EN: Can't say you don't have guts, heh-heh...
  ZH:   * 胆子倒是不小，嘿嘿……

## SC0337ef03c18c3b84 | nsfw | datadf/all.ds | AreaC_Slaver1.Goodbye
CONTROL L1402  <AreaC_Slaver1.Goodbye>
CONTROL L1403    if { !koboCostume() } {
ROW CAT:Oec8adf8d413ef09eaca1 L1404 * physical_line
  EN: Be seeing you. Heh-heh...
  ZH:     * 回头见。嘿嘿……
CONTROL L1405    } else {
ROW CAT:O910e17b41d1e9dafe875 L1406 * physical_line
  EN: Take care out there. Ole Tutone's a rough place these days.
  ZH:     * 出门小心点。如今这老图托恩可不太平。
CONTROL L1407    }

## SC629db7770e65bbd1 | nsfw | datadm/all.ds | AreaC_Slaver1.HelloDog
CONTROL L1478  <AreaC_Slaver1.HelloDog>
ROW CAT:O2f685a7cf9bb4ebeff36 L1479 * physical_line
  EN: What the-? A dog?!
  ZH:   * 什么鬼——？一条狗？！

## SC1abe42edf94c4d3d | nsfw | datadf/all.ds | AreaC_Slaver1.NoInventorySpace
CONTROL L1429  <AreaC_Slaver1.NoInventorySpace>
ROW CAT:O7fb203ea35f3580d67a4 L1430 * physical_line
  EN: Hey, you don't even have room for that!
  ZH:   * 喂，你都没地方装这个了！
CONTROL L1432  ### as anthro:

## SCeb5f881523d7a407 | nsfw | datadm/all.ds | AreaC_Slaver1.NotEnoughMoney
CONTROL L1436  <AreaC_Slaver1.NotEnoughMoney>
ROW CAT:Od0e0d0cd6952a65535f4 L1437 * physical_line
  EN: This ain't a peepshow, punk! Show me the lect or get out!
  ZH:   * 这儿可不是给你白看的，混蛋！拿出LECT来，不然滚蛋！

## SC657ecaa66a191788 | nsfw | datadf/all.ds | AreaC_Slaver1.Purchased
CONTROL L1409  <AreaC_Slaver1.Purchased>
CONTROL L1410    if { !koboCostume() } {
ROW CAT:Oe6da1808c4195379a7b7 L1411 * physical_line
  EN: Remember, no refunds! What else you need? He! He! He!
  ZH:     * 记住，概不退款！还要什么？嘿！嘿！嘿！
CONTROL L1412    } else {
ROW CAT:Of147e91a8be9bff144ee L1413 * physical_line
  EN: Wow, thanks! I didn't think I'd ever find a kobold to buy these!
  ZH:     * 哇，多谢！我还以为找不到肯买这些的科博德呢！
CONTROL L1414    }

## SCa0b6f586bdc67262 | nsfw | datadm/all.ds | AreaC_Slaver1.Talk.psy
CONTROL L1468  <AreaC_Slaver1.Talk.psy>
CONTROL L1469    if { koboCostume() && hasItem(SpecialPsycards) } {
ROW CAT:O3625421030b990881cdc L1470 * physical_line
  EN: I'll be honest: all this PSY stuff gives me the creeps.
  ZH:     * 老实说：这些精神力的东西让我发毛。
ROW CAT:Ocb5b7df39b7d9da8ef16 L1471 * physical_line
  EN: Jus' don't blow me up and we'll be golden, okay?
  ZH:     * 就别把我炸了，咱们就妥了，好吗？
CONTROL L1472    } else {
ROW CAT:O3784d478755b18eb3564 L1473 * physical_line
  EN: Most kobolds don't really do all these mind games. I get it if y'ain't interested.
  ZH:     * 大多数科博德并不真搞这些心理把戏。你要是没兴趣，我理解。
ROW CAT:O283a647ea90bb7a8a8ff L1474 * physical_line
  EN: Any ole club and a length of rope'll do me just fine... All direct-like, ya-know?
  ZH:     * 随便一根旧棍子加一段绳子就够我用了……全都直接来的，懂吧？
CONTROL L1475    }
CONTROL L1477  ### dog handling

## SCe1411891da18e1a5 | nsfw | datadf/all.ds | AreaE_Macsen1.Goodbye
CONTROL L1481  <AreaE_Macsen1.Goodbye>
CONTROL L1482    if { !inCosmoSuit() } {
ROW CAT:O16f16bde07cfd6748436 L1483 * physical_line
  EN: You're real daring, going out without a spacesuit on!
  ZH:     * 不穿宇航服就往外跑，你胆子可真大！ 
ROW CAT:O47ffdd3a92cf4b6f7f07 L1484 * physical_line
  EN: You get 'em, tiger!
  ZH:     * 加油，猛将，去收拾他们吧！
CONTROL L1485    } else {
ROW CAT:O1918db0862731f0fd683 L1486 * physical_line
  EN: Bye! I'd toast to your health, but I know you can't drink with that helm on!
  ZH:     * 再见！本想举杯祝你健康，可我知道你戴着那头盔没法喝！
CONTROL L1487    }

## SC58e6139ca98d3a1d | nsfw | datadm/all.ds | AreaE_Macsen1.SpecialGeiger
CONTROL L1499  <AreaE_Macsen1.SpecialGeiger>
ROW CAT:O5646682bc67cfdf29f8c L1500 * physical_line
  EN: Fancy yourself an explorer?
  ZH:   * 觉得自己是个探险家？ 
ROW CAT:O11d9c4131585c54bd668 L1501 * physical_line
  EN: Then you probably aren't interested in this...
  ZH:   * 那你大概对这东西没兴趣……
ROW CAT:Ofeca87bcb892b8bd239e L1502 * physical_line
  EN: This little doohicky will detect anomalies
  ZH:   * 这小玩意儿能探测异常，还能在你的导航地图上标出重要的东西！ 
ROW CAT:Ob1808b679d8a3b1fd0bd L1503 * physical_line
  EN: and it'll even mark important things on your Navmap!
  ZH: 
ROW CAT:Obb23f8439bf70d780408 L1504 * physical_line
  EN: Great for cleaning up all the areas you've been to.
  ZH:   * 用来查漏补缺、扫遍去过的区域再合适不过了。

## SC16c88d04e6435719 | sfw | datadm/all.ds | AreaE_Macsen1.SpecialGeiger
CONTROL L1489  <AreaE_Macsen1.SpecialGeiger>
ROW SFW157dbb3382d4fd34e68b423c L1490 - physical_line
  EN: Fancy yourself an explorer? 
  ZH:   * 觉得自己是个探险家？ 
ROW SFWe7dda98ca3b700d524702bca L1491 - physical_line
  EN: Then you probably aren't interested in this...
  ZH:   * 那你大概对这东西没兴趣……
ROW SFWf02f48c0be82766e4b405512 L1492 - physical_line
  EN: This little doohicky will detect anomalies 
  ZH:   * 这小玩意儿能探测异常，还能在你的导航地图上标出重要的东西！ 
ROW SFWb19cc2d8b64a7837cd089a33 L1493 - physical_line
  EN: and it'll even mark important things on your Navmap!
  ZH: 
ROW SFW4d4fca8b9c56fe68087ecdc4 L1494 - physical_line
  EN: Great for cleaning up all the areas you've been to.
  ZH:   * 用来查漏补缺、扫遍去过的区域再合适不过了。

## SCf0854f9fd297eebd | nsfw | datadf/all.ds | AreaE_Macsen1.Talk.mags
CONTROL L1501  <AreaE_Macsen1.Talk.mags>
ROW CAT:O6142c5adc1c51138ae48 L1502 * physical_line
  EN: The worst part about all this space walking is having to wear a space suit.
  ZH:   * 太空行走最糟的，就是得穿宇航服。
ROW CAT:O94f14bb944e28cfeb5bd L1503 * physical_line
  EN: Don't worry though, there's extra MAGs in the back here if you need them!
  ZH:   * 不过别担心，后面还有备用弹匣，需要就拿。
CONTROL L1505  ### shared ###

## SC56c18b90b118102c | sfw | datadm/all.ds | AreaE_Macsen1.Talk.mags
CONTROL L1501  <AreaE_Macsen1.Talk.mags>
ROW SFW82d52c7ba74c38890e510d9d L1502 - physical_line
  EN: The worst part about all this space walking is having to wear a space suit.
  ZH:   * 太空行走最糟的，就是得穿宇航服。
ROW SFWbf159bea462cf6b142fb221f L1503 - physical_line
  EN: It gets my fur all mussed up!
  ZH:   * 弄得我的毛全乱了！
CONTROL L1505  ### shared ###

## SC2202086d640ba93b | nsfw | datadf/all.ds | AreaH_Cellar.CancelPurchase
CONTROL L1604  <AreaH_Cellar.CancelPurchase>
ROW CAT:O58a1c5b35e12df2584e4 L1605 * physical_line
  EN: Not hungry after all, huh?
  ZH:   * 到头来还是不饿，是吧？

## SC32533b7917c2dd2c | nsfw | datadm/all.ds | AreaH_Cellar.CancelPurchase
CONTROL L1614  <AreaH_Cellar.CancelPurchase>
ROW CAT:Oeda43341f7785ab6ee81 L1615 * physical_line
  EN: Not hungry after all, huh?
  ZH:   * 到头来还是不饿，是吧？

## SCe489e5f70c50918e | nsfw | datadm/all.ds | AreaH_Cellar.NotEnoughMoney
CONTROL L1620  <AreaH_Cellar.NotEnoughMoney>
ROW CAT:Occf14e69138ed71c0fe7 L1621 * physical_line
  EN: Doesn't your boss pay ya? Come back with some more Lect!
  ZH:   * 你老板不给你发钱吗？多带点Lect再来！

## SC7e74bd0d0fa2d0ea | nsfw | datadf/all.ds | AreaH_Cellar.Talk.food
CONTROL L1562  <AreaH_Cellar.Talk.food>
CONTROL L1563    if { agentsRescued() >= 7 } {
ROW CAT:O3b50a4fce0810c47003d L1564 * physical_line
  EN: Heyhey, if it isn't the great hero of Tutone!
  ZH:     * 嘿嘿，这不是图托恩的大英雄嘛！
ROW CAT:O49cd62d79e260bb1f777 L1565 * physical_line
  EN: With all these folks recovering here, business has been booming!
  ZH:     * 有这么多人在这一带养伤，生意可真是红火！
ROW CAT:O07e68ea2cec235896abc L1566 * physical_line
  EN: Feel free to buy as much meat as you need, stocks won't run out.
  ZH:     * 想买多少肉尽管买，存货管够。
CONTROL L1567    } else if  { agentsRescued() >= 4 } {
ROW CAT:O899b17667977abf8bbe8 L1568 * physical_line
  EN: Starting to get lively in here, isn't it?
  ZH:     * 这儿开始热闹起来了，是吧？
ROW CAT:Ocfa0f6bce8524cf37854 L1569 * physical_line
  EN: I keep bringing in food, and you fellas keep on eating it up!
  ZH:     * 我一批批把吃的运进来，你们这帮家伙就一个劲地吃光！
ROW CAT:O22bdb81079c37cfee711 L1570 * physical_line
  EN: Almost makes me think that I should bring in some of the GOOD stuff...
  ZH:     * 都快让我觉得该进点“好东西”了……
CONTROL L1571    } else if { agentsRescued() >= 1 } {
ROW CAT:O38ad51413d05a91c1933 L1572 * physical_line
  EN: There's not much reason to stock a lot of food right now
  ZH:     * 眼下没什么理由囤太多吃的
ROW CAT:O8a454fb14be4e625215b L1573 * physical_line
  EN: But you know, if there were more folks resting up in this hangar
  ZH:     * 不过你知道，要是这机库里歇着的人再多些，我倒也许该多运些补给进来……
ROW CAT:O0ce93419dcb65fad68c9 L1574 * physical_line
  EN: I could probably stand to bring in more provisions...
  ZH: 
CONTROL L1575    } else {
ROW CAT:Oe6e54de8abdcdade680d L1576 * physical_line
  EN: It's been so long since I saw another one of you agent sorts here
  ZH:     * 我已经很久没在这儿见到你们这种特工了，连存货都没顾上补！
ROW CAT:O66d55e0c0250043d5fad L1577 * physical_line
  EN: that I haven't even kept the stocks up!
  ZH: 
ROW CAT:Oba373d40f88b905307b2 L1578 * physical_line
  EN: Maybe if there were folks to eat the food, I could bring some in...
  ZH:     * 要是有谁来吃这些东西，也许我就能进些货……
CONTROL L1579    }
CONTROL L1581  ### shared ###

## SCcb0a76aad6da4b24 | sfw | datadm/all.ds | AreaH_Cellar.Talk.food
CONTROL L1562  <AreaH_Cellar.Talk.food>
CONTROL L1563    if { agentsRescued() >= 7 } {
ROW SFWe181eee90881a3e768ffc42b L1564 - physical_line
  EN: Heyhey, if it isn't the great hero of Tutone!
  ZH:     * 嘿嘿，这不是图托恩的大英雄嘛！
ROW SFW7fe42d6ff4a2bec0492b1f94 L1565 - physical_line
  EN: With all these folks recovering here, business has been booming!
  ZH:     * 有这么多人在这儿养伤，生意红火得很！
ROW SFW290c4adf1d65768d227f7739 L1566 - physical_line
  EN: Feel free to buy as much meat as you need, stocks won't run out.
  ZH:     * 想买多少肉尽管买，存货管够。
CONTROL L1567    } else if  { agentsRescued() >= 4 } {
ROW SFW7c3e7ac542422eefa9b1a3cf L1568 - physical_line
  EN: Starting to get lively in here, isn't it?
  ZH:     * 这儿总算开始热闹起来了，对吧？
ROW SFWfb9f2eca62329a2f15bc47fd L1569 - physical_line
  EN: I keep bringing in food, and you fellas keep on eating it up!
  ZH:     * 我一批批把吃的运进来，你们这帮家伙就一个劲地吃光！
ROW SFW96e59d1e78394aeb04d42350 L1570 - physical_line
  EN: Almost makes me think that I should bring in some of the GOOD stuff...
  ZH:     * 都快让我觉得该进点“好东西”了……
CONTROL L1571    } else if { agentsRescued() >= 1 } {
ROW SFW517375dd7e8fd5e9e6326c03 L1572 - physical_line
  EN: There's not much reason to stock a lot of food right now
  ZH:     * 眼下没什么理由囤太多吃的
ROW SFWf9b4e532d19cd6c56e2e5e77 L1573 - physical_line
  EN: But you know, if there were more folks resting up in this hangar
  ZH:     * 可你知道，要是这机库里多些人休整，我倒也许该多运些补给进来……
ROW SFWd1cb251f32ddd430210d1462 L1574 - physical_line
  EN: I could probably stand to bring in more provisions...
  ZH: 
CONTROL L1575    } else {
ROW SFW1358957567e6edf09b099433 L1576 - physical_line
  EN: It's been so long since I saw another one of you agent sorts here
  ZH:     * 我好久没在这儿见到你们这种探员了，连存货都没顾上补！
ROW SFWff354886aecfc3444df1968a L1577 - physical_line
  EN: that I haven't even kept the stocks up! 
  ZH: 
ROW SFW932c05a38e266294591c2f5c L1578 - physical_line
  EN: Maybe if there were folks to eat the food, I could bring some in...
  ZH:     * 要是有谁来吃这些东西，也许我就能进些货……
CONTROL L1579    }
CONTROL L1581  ### shared ###

## SC909ea33ab8ae827c | nsfw | datadm/all.ds | AreaH_MacsenBar.Goodbye
CONTROL L1631  <AreaH_MacsenBar.Goodbye>
ROW CAT:Oc4fc8749aa1822d6c56e L1632 * physical_line
  EN: Bye for now! You take care, you hear!
  ZH:   * 先这样啦！你多保重，听见没！

## SCe90373e908bd0fdb | nsfw | datadm/all.ds | AreaH_MacsenBar.Hello
CONTROL L1628  <AreaH_MacsenBar.Hello>
ROW CAT:O82bd95a85e34b4d35541 L1629 * physical_line
  EN: Hey there! Don't be a stranger, come on in!
  ZH:   * 嘿，你好！别见外，快进来吧！

## SC2c7f69c489a9e89a | nsfw | datadf/all.ds | AreaH_MacsenBar.PsyUp
CONTROL L1624  <AreaH_MacsenBar.PsyUp>
ROW CAT:O7131c34a1889053ee251 L1625 * physical_line
  EN: You come across any of these crazy crystals out there in the world?
  ZH:   * 你在外头见过这种神奇的水晶吗？
ROW CAT:O96e4a3c79c4b418c3f3b L1626 * physical_line
  EN: They say that if an Esper gets one of these, it'd boost their psychic capacity
  ZH:   * 听说超能力者得到一颗，就能提升灵能容量，可我只是条普通的狗，这东西对我没用。送你吧！
ROW CAT:O1b7abda77e5562dbc4cf L1627 * physical_line
  EN: but I'm just a simple dog, so it does nothing for me. You can have it!
  ZH: 

## SCd25892ff5279d08d | nsfw | datadm/all.ds | AreaH_MacsenBar.SoldOut
CONTROL L1700  <AreaH_MacsenBar.SoldOut>
ROW CAT:O5e5bd0e57298667c514b L1701 * physical_line
  EN: I'm out now, sorry! If I had more I'd gladly give 'em to ya!
  ZH:   * 抱歉，现在没货了！要是还有，我很乐意给你！

## SC2c52f43a7a15157b | nsfw | datadm/all.ds | AreaH_MacsenBreeding.Goodbye
CONTROL L1705  <AreaH_MacsenBreeding.Goodbye>
ROW CAT:O752bce7fb38d1bab212a L1706 * physical_line
  EN: BYE-OH! DON'T FORGET TO COME OFTEN!
  ZH:   * 拜拜！别忘了常来啊！

## SCe2fee62c3bfc9b27 | nsfw | datadm/all.ds | AreaH_MacsenBreeding.SpecialFap
CONTROL L1718  <AreaH_MacsenBreeding.SpecialFap>
ROW CAT:O4980db4516a7198a5a03 L1719 * physical_line
  EN: SINCE YOU'VE GOTTEN REAL CLOSE WITH ONE OF THOSE CREATURES, TAKE THIS!
  ZH:   * 既然你已经和那些生物中的一个变得非常亲近了，把这个拿去！
ROW CAT:Oc77c7abfa706468e2268 L1720 * physical_line
  EN: GET REAL CLOSE AND AFFECTIONATE TO THEM ONE MORE TIME WHILE HOLDING THIS
  ZH:   * 拿着这个，再一次跟他们亲近、亲昵，你也许会感到某种力量流经你……
ROW CAT:Oef6911ca1ed8a2a147c5 L1721 * physical_line
  EN: AND YOU MIGHT FEEL A CERTAIN POWER COURSE THROUGH YOU...
  ZH: 

## SC69cf1fb9619b4227 | nsfw | datadf/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1713  <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1714    if { !f(ctx_maxed_any_pet_affinity) } {
ROW CAT:O8988e9c955b5e1662588 L1715 * physical_line
  EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
  ZH:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW CAT:O24802e5dd74f0347e94f L1716 * physical_line
  EN: AFTER YOU'VE MAXXXED OUT AN AFFINITY, RETURN HERE FOR A SPECIAL REWARD.
  ZH:     * 把任意一只宠物的亲密度提升到最高，再回来领特别奖励。
CONTROL L1717    } else {
ROW CAT:O855a59c5a1c97f9bbd97 L1718 * physical_line
  EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
  ZH:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW CAT:Ob0c580a571e9cf616874 L1719 * physical_line
  EN: JUST PET THEM WHILE THEY'RE AT MAX AFFINITY TO CHARGE THE CRYSTAL.
  ZH:     * 只要在亲密度最高时抚摸它们，就能给水晶充能。
ROW CAT:Of3ec5506319e3159db81 L1720 * physical_line
  EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
  ZH:     * 每种生物给的力量都不同！都试试！
CONTROL L1721    }
CONTROL L1723  ### shared ###

## SCed20df0301e3b8c0 | sfw | datadf/all.ds | AreaH_MacsenBreeding.Talk.fap
CONTROL L1715  <AreaH_MacsenBreeding.Talk.fap>
CONTROL L1716    if { !f(ctx_maxed_any_pet_affinity) } {
ROW SFWa98d4b0720f01e91f556c68c L1717 - physical_line
  EN: MAKE SURE TO SHOW YOUR PETS SOME AFFECTION, AND FEED THEM WELL!
  ZH:     * 一定要给宠物一点关爱，并且好好喂它们！
ROW SFW1642579fc9ed0268da90fcf6 L1718 - physical_line
  EN: AFTER YOU'VE MAXED A PET'S CONFIDENCE, RETURN HERE FOR A SPECIAL REWARD.
  ZH:     * 把宠物的自信提升到最高后，回来领取特别奖励。
CONTROL L1719    } else {
ROW SFW44ae65d7b0f8f3f30faf5341 L1720 - physical_line
  EN: WITH THE CRYSTAL, THE CREATURES THAT LOVE YOU CAN GIVE YOU A SPECIAL BOOST!
  ZH:     * 有了这水晶，爱你的生物就能给你一份特殊加成！
ROW SFW9495f93b7477eb0c6f19dd4e L1721 - physical_line
  EN: JUST PET THEM WHILE THEY'RE AT FULL CONFIDENCE TO CHARGE THE CRYSTAL.
  ZH:     * 在它们自信满满时抚摸它们，就能给水晶充能。
ROW SFW50e5b598e3affd5a3f9507d4 L1722 - physical_line
  EN: EACH CREATURE GIVES A DIFFERENT POWER! TRY THEM ALL!
  ZH:     * 每种生物给的力量都不同！都试试！
CONTROL L1723    }
CONTROL L1725  ### shared ###

## SCf2b4c9e07f44df76 | nsfw | datadm/all.ds | AreaH_MacsenBreeding.TazerTrainee
CONTROL L1714  <AreaH_MacsenBreeding.TazerTrainee>
ROW CAT:O7d6f9c83e012e71479aa L1715 * physical_line
  EN: NOT INTERESTED IN CAPTURING CREATURES? SURE, WE CAN TRADE BACK.
  ZH:   * 对捕捉生物没兴趣？没问题，我们可以换回来。
ROW CAT:O925b8572fccf0a324a26 L1716 * physical_line
  EN: YOU'RE WELCOME TO GET THE TRAINER TAZER AGAIN LATER, OF COURSE!
  ZH:   * 当然，以后想再拿驯兽电击枪，随时欢迎！

## SC5a590253bcfbc1a2 | nsfw | datadf/all.ds | AreaH_MacsenBreeding.TazerTrainer
CONTROL L1698  <AreaH_MacsenBreeding.TazerTrainer>
ROW CAT:Of880d0e300a70f1ae95b L1699 * physical_line
  EN: THIS RIGHT HERE IS A TRAINER TAZER! MUCH DIFFERENT THAN THE TRAINEE TAZER!
  ZH:   * 这就是驯兽电击枪！跟学员电击枪可大不一样！
ROW CAT:Oc512f77796faae3bd424 L1700 * physical_line
  EN: IF YOU DEFEAT AN ENEMY WHILE WIELDING THIS, IT'LL SEND THE CREATURE HERE!
  ZH:   * 拿着它击败敌人，就会把那个生物传送到这里！
ROW CAT:O427738b945daa890db3e L1701 * physical_line
  EN: AND WHILE THEY'RE HERE YOU CAN OBSERVE AND GROW YOUR RAPPORT WITH THEM
  ZH:   * 它们待在这里时，你可以观察它们，跟它们增进关系，从而更深入地了解这个物种！
ROW CAT:Oaa5b4798742ac0c6b730 L1702 * physical_line
  EN: TO UNDERSTAND MORE ABOUT THE SPECIES!
  ZH: 

## SC5ccf136cef295900 | nsfw | datadf/all.ds | AreaH_MacsenMechanic.Hello
CONTROL L1760  <AreaH_MacsenMechanic.Hello>
ROW CAT:Of4eba903f2637af9d2b6 L1761 * physical_line
  EN: Welcome to my little shop!
  ZH:   * 欢迎光临我的小店！
ROW CAT:O07277a881507fe080694 L1762 * physical_line
  EN: ...no, not that kind of shop! This is an auto shop!
  ZH:   * ……不，不是那种店！这是汽车修理店！

## SC5ab9f13dfc627644 | nsfw | datadm/all.ds | AreaH_MacsenMechanic.Talk.PartHints2
CONTROL L1812  <AreaH_MacsenMechanic.Talk.PartHints2>
CONTROL L1813    if { f(ClassicStarkillV3_defeated) && (!hasItem(ShipGun) || !hasItem(ShipShield) || !hasItem(ShipRadar) || !hasItem(ShipTurbo)) } {
ROW CAT:O697e0ec340c4df170aac L1814 * physical_line
  EN: Don't worry about memorizing what I just told ya...
  ZH:     * 别费劲记我刚才说的那些……
ROW CAT:Obfea178b181f4d405d68 L1815 * physical_line
  EN: ...I marked it on your Navmap already! Go check it out!
  ZH:     * ……我已经在你的导航地图上标好了！去看看吧！
CONTROL L1816    }
CONTROL L1818  ### shared ###

## SC66b17e91a90ae706 | nsfw | datadm/all.ds | AreaH_Ship.Talk.Bro
CONTROL L1872  <AreaH_Ship.Talk.Bro>
ROW CAT:Oa366532c8a9dd67bbe34 L1873 * physical_line
  EN: You've really come a long way, haven't you?
  ZH:   * 你真的一路成长了不少，不是吗？
ROW CAT:O81b6ce37b391f72d8dab L1874 * physical_line
  EN: Feels like you were still wetting the bed only yesterday!
  ZH:   * 感觉昨天你还在尿床呢！
ROW CAT:Oc9d1911f07393dc228da L1875 * physical_line
  EN: ...you've gotten over that by now, right?
  ZH:   * ……你现在应该已经改掉了吧？

## SC1c250b8c13a9b3fb | nsfw | datadf/all.ds | AreaH_Ship.Talk.Ship
CONTROL L1857  <AreaH_Ship.Talk.Ship>
ROW CAT:Oddd3aa3893dc5b9d3267 L1858 * physical_line
  EN: Man, this ship got beat up pretty good, didn't it?
  ZH:   * 哇，这艘船伤得可真惨，是吧？
ROW CAT:Oc7a7c78482d26dff871c L1859 * physical_line
  EN: I'd fly you straight to where that evil Queen is hiding
  ZH:   * 我会直接把你送到那个邪恶女王藏身的地方，但这艘船没修好之前可飞不了那么高！
ROW CAT:O1bd8bb4a58657ecc60e7 L1860 * physical_line
  EN: but this bird can't fly that high until it's fixed up!
  ZH: 

## SCf27358ddd70e6726 | nsfw | datadm/all.ds | AreaH_Ship.Talk.Ship
CONTROL L1867  <AreaH_Ship.Talk.Ship>
ROW CAT:O49806282fe5a695c4874 L1868 * physical_line
  EN: Man, this ship got beat up pretty good, didn't it?
  ZH:   * 哇，这艘船伤得可真惨，是吧？
ROW CAT:O3b67e9267ef2c9ec40f8 L1869 * physical_line
  EN: I'd fly you straight to where that evil Queen is hiding
  ZH:   * 我会直接把你送到那个邪恶女王藏身的地方，但这艘船没修好之前可飞不了那么高！
ROW CAT:O76eba1df91296b0626c5 L1870 * physical_line
  EN: but this bird can't fly that high until it's fixed up!
  ZH: 

## SCbe90f218b357ac29 | nsfw | datadf/all.ds | AreaH_Ship.Talk.Sis
CONTROL L1862  <AreaH_Ship.Talk.Sis>
ROW CAT:O6f6e57b4abfba88c968e L1863 * physical_line
  EN: You always were the winner when we roughhoused...
  ZH:   * 以前咱们打打闹闹的时候，你总是赢的那个……
ROW CAT:Oef74995b43451461e672 L1864 * physical_line
  EN: ...but hey! I put up a good effort this time, right?
  ZH:   * ……不过嘿！这次我可是很拼的，对吧？

## SCf3d0e0d08447de2a | nsfw | datadm/all.ds | AreaX_Upgrade.CancelPurchase
CONTROL L1912  <AreaX_Upgrade.CancelPurchase>
ROW CAT:Ofc47dc0b0e272a1ec588 L1913 * physical_line
  EN: Are you worried about voiding the warranty? Pft.
  ZH:   * 你是担心会让保修失效吗？噗。
ROW CAT:Oadfef54b7d3ee57fb300 L1914 * physical_line
  EN: Oh well. Have you got something else for me to work on?
  ZH:   * 算了。你还有别的活儿要我干吗？

## SC8f902d56c00bf9c1 | nsfw | datadm/all.ds | AreaX_Upgrade.GoodbyeDog
CONTROL L1893  <AreaX_Upgrade.GoodbyeDog>
ROW CAT:O8b6e10891674097cf16f L1894 * physical_line
  EN: Hey! Where are you going ducky?! We've got refactoring to do!
  ZH:   * 喂！你要去哪儿啊，小鸭子？！我们还有重构要做呢！

## SC6c9d23b9ef2ba2fe | nsfw | datadf/all.ds | AreaX_Upgrade.GoodbyeKobo
CONTROL L1889  <AreaX_Upgrade.GoodbyeKobo>
ROW CAT:Oa15b84162e60edeb2205 L1890 * physical_line
  EN: -wait a sec, you're not the delivery guy! G-get out of here right now!
  ZH:   * -等等，你不是送货的！快、快给我出去！

## SC1cc467fe0eab6151 | nsfw | datadm/all.ds | AreaX_Upgrade.Hack
CONTROL L1927  <AreaX_Upgrade.Hack>
ROW CAT:Of78ab14aad5e573106e6 L1928 * physical_line
  EN: I see you've been having some real trouble finding those chips.
  ZH:   * 我看你找那些芯片可真是费了不少劲。
ROW CAT:O9803d78accf8d612c470 L1929 * physical_line
  EN: Fortunately, I've got a solution... well, I think!
  ZH:   * 幸好我有个办法……嗯，我觉得有！
ROW CAT:O9763c249286493504ef9 L1930 * physical_line
  EN: With my novel algorithms - and the energy afforded by this site - I believe
  ZH:   * 凭我新颖的算法——以及此地供给的能量——我相信我能侵入驱动我们这个现实的模拟程序……
ROW CAT:O31191a90f652f1aebaed L1931 * physical_line
  EN: I can hack into the simulation that drives our very reality...
  ZH: 
ROW CAT:Od74d43653b5a2853da47 L1932 * physical_line
  EN: Then we could have all the chips we'd ever need, with no downsides probably!
  ZH:   * 那样我们就有永远用不完的芯片了，而且大概没有任何坏处！
ROW CAT:Od6a9737a7c2a93496a99 L1933 * physical_line
  EN: How about it? Wanna try?! Let's hack the world!
  ZH:   * 怎么样？想试试？！我们来黑掉这个世界吧！

## SC640575f521bad842 | nsfw | datadf/all.ds | AreaX_Upgrade.Hello
CONTROL L1872  <AreaX_Upgrade.Hello>
ROW CAT:O62c3a559cc38f4aeb82b L1873 * physical_line
  EN: Heya Yiffany! How can I help you?
  ZH:   * 嘿，伊吠妮！有什么我能帮你的吗？

## SC979a83b684e56cb5 | nsfw | datadf/all.ds | AreaX_Upgrade.NotEnoughMoney
CONTROL L1924  <AreaX_Upgrade.NotEnoughMoney>
ROW CAT:Od1988d391d87030a97b2 L1925 * physical_line
  EN: Hey, wait a minute! You don't have enough components for this!
  ZH:   * 嘿，等一下！你的零件不够做这个！
ROW CAT:O1b3cc66188ba2417398a L1926 * physical_line
  EN: I need isolinear modules pushing at least 400 terahertz.
  ZH:   * 我需要至少能跑到 400 太赫兹的等线性模块。
ROW CAT:O462bfc9e47042222ccff L1927 * physical_line
  EN: Anything else is basically too slow to even bother with!
  ZH:   * 别的基本上太慢了，根本不值得一试！

## SCb63ca130676dfa96 | nsfw | datadm/all.ds | AreaX_Upgrade.NotEnoughMoney
CONTROL L1935  <AreaX_Upgrade.NotEnoughMoney>
ROW CAT:O85a57f9937ce1868d67f L1936 * physical_line
  EN: Hey, wait a minute! You don't have enough components for this!
  ZH:   * 嘿，等一下！你的零件不够做这个！
ROW CAT:Ofb34ed526e78ece1f475 L1937 * physical_line
  EN: I need isolinear modules pushing at least 400 terahertz.
  ZH:   * 我需要至少能跑到 400 太赫兹的等线性模块。
ROW CAT:O3d0b406aee77adfa9384 L1938 * physical_line
  EN: Anything else is basically too slow to even bother with!
  ZH:   * 别的基本上太慢了，根本不值得一试！

## SC2d695de7a27a8b74 | nsfw | datadf/all.ds | AreaX_Upgrade.TechBabble.trashed
CONTROL L1948  <AreaX_Upgrade.TechBabble.trashed>
ROW CAT:Oa106e6fca6f15eae53cf L1949 * physical_line
  EN: Wow, this thing is really *trashed*, but I can tell it used to be top of the line.
  ZH:   * 哇，这东西真是*烂透了*，不过我看得出它从前是顶级货。
ROW CAT:O6bb2dc2ad527f290e211 L1950 * physical_line
  EN: Throw me those chips and let's see what this repair bay can do!
  ZH:   * 把那些芯片丢给我，看看这个维修区能有什么本事！

## SCefd38091f44a8fd1 | nsfw | datadf/all.ds | Fenfen_Shared.Hello
CONTROL L4951  <Fenfen_Shared.Hello>
ROW CAT:Oc57c8af721685279e4c2 L4952 Anon/Fox physical_line
  EN: Help, I'm trapped in here!
  ZH:   Anon/Fox: 救命，我被困在这儿了！

## SC4c1bcd84e2601339 | nsfw | datadf/all.ds | Gitgud.Tip3
CONTROL L3308  <Gitgud.Tip3>
ROW CAT:O977cba0cd59dad5ece7d L3309 Gitgud physical_line
  EN: [YOU SHOULD BE ON THE LOOKOUT FOR SUSPICIOUS WALLS]
  ZH:     Gitgud: [你应该留意可疑的墙壁，因为有些一被攻击就会崩塌！]
ROW CAT:O6a3c45b65a4ae573e0c7 L3310 Gitgud physical_line
  EN: [AS SOME WILL CRUMBLE AS SOON AS YOU ATTACK THEM!]
  ZH: 

## SC3607806e90147971 | nsfw | datadf/all.ds | Gitgud.Tip5
CONTROL L3316  <Gitgud.Tip5>
ROW CAT:O75b48db3a6f250e4503d L3317 Gitgud physical_line
  EN: [MANY ENEMIES GET STUNNED WHEN THE LIGHTTAZER STRIKES]
  ZH:     Gitgud: [许多敌人在光电击枪击中时会眩晕，这给了你跳开躲避的机会！]
ROW CAT:O3ceba25e8e1fc9d28eae L3318 Gitgud physical_line
  EN: [WHICH GIVES YOU A CHANCE TO JUMP OUT OF THE WAY!]
  ZH: 

## SC4ecae8f983164b21 | nsfw | datadm/all.ds | Hacker_Shared.CancelPurchase
CONTROL L4999  <Hacker_Shared.CancelPurchase>
ROW CAT:O39aa163fe62af3e1c5ec L5000 * physical_line
  EN: Are you worried about triggering a security alert? Pft.
  ZH:   * 你是担心会触发安全警报吗？噗。
ROW CAT:Obbe7b53c462ef4aaada5 L5001 * physical_line
  EN: Oh well. Have you got something else for me to work on?
  ZH:   * 算了。你还有别的活儿要我干吗？

## SC545db67f494b57d8 | nsfw | datadf/all.ds | Hacker_Shared.GoodbyeDog
CONTROL L4972  <Hacker_Shared.GoodbyeDog>
ROW CAT:O93679cce8209df51b71f L4973 * physical_line
  EN: Hey! Where are you going ducky?! We've got refactoring to do!
  ZH:   * 嘿！你要去哪儿啊，小鸭鸭？！咱们还有重构要做呢！

## SC5407e2e1302d820a | nsfw | datadf/all.ds | Hacker_Shared.Hack
CONTROL L5006  <Hacker_Shared.Hack>
ROW CAT:O03fdc48e8e4363dde921 L5007 * physical_line
  EN: Ready to hack it?
  ZH:   * 准备好黑掉它了吗？

## SC4a8d568c9ad725e2 | nsfw | datadf/all.ds | Hacker_Shared.HelloDog
CONTROL L4968  <Hacker_Shared.HelloDog>
ROW CAT:O737d120aa92368efbe9e L4969 * physical_line
  EN: Hello there Mr. Puppy! Do you want to be my rubber ducky?
  ZH:   * 你好呀，小狗先生！你想当我的橡皮鸭吗？
ROW CAT:O37c1cbd78ab2a4c2def0 L4970 * physical_line
  EN: All you have do is stay here and listen to me talk about computers all day!
  ZH:   * 你只要待在这里，听我一整天聊电脑就行！

## SCd14e021c6ca16c23 | nsfw | datadm/all.ds | Hacker_Shared.Meeting
CONTROL L4969  <Hacker_Shared.Meeting>
ROW CAT:O52909c720e43010faa0b L4970 * physical_line
  EN: Greetings, Yiffai. You don't know me, but I kinda snooped your satlink.
  ZH:   * 你好，伊吠。你不认识我，不过我偷偷窥探了你的卫星通讯。
ROW CAT:O90af7e4a58483015f82f L4971 * physical_line
  EN: So I've actually been watching you for a while, and I have a proposition...
  ZH:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:Oa61a078198bc4a8bf661 L4972 * physical_line
  EN: It's simple: You bring me those fancy chips you find out there,
  ZH:   * 很简单：把你在外头找到的那些高级芯片带给我，我就替你破解门锁！这不是双赢嘛！
ROW CAT:Oe84a9ddc8afbed7d9c71 L4973 * physical_line
  EN: and I'll hack open doors for you! It's a win-win, obviously!
  ZH: 

## SC3296dc605ff47e43 | nsfw | datadf/all.ds | Hacker_Shared.Purchased
CONTROL L4982  <Hacker_Shared.Purchased>
ROW CAT:O5de08648a3b10e887e0c L4983 * physical_line
  EN: According to my calculations, that door should be open!
  ZH:   * 根据我的计算，那扇门现在应该开了！
ROW CAT:Obe6c4df0501b19426901 L4984 * physical_line
  EN: That one was fun! Got anything else for me?
  ZH:   * 那扇挺有意思的！还有别的要给我吗？

## SCeb3844da594b6c77 | sfw | datadm/all.ds | Macsen_Shared.BoneTheDog
CONTROL L4877  <Macsen_Shared.BoneTheDog>
ROW SFWb838ffe9c516e582fa0c9197 L4878 - physical_line
  EN: Do you want a treat, boy? Do ya?
  ZH:   * 想吃点零食吗，小伙子？想不想呀？

## SCfea42f78c36c3448 | sfw | datadf/all.ds | Macsen_Shared.GoodbyeDog
CONTROL L4836  <Macsen_Shared.GoodbyeDog>
ROW SFW9854461b353a184181b051f1 L4837 - physical_line
  EN: What a cute doggie!
  ZH:   * 真是只可爱的小狗！

## SC6083cbc3d2809517 | nsfw | datadm/all.ds | Macsen_Shared.GoodbyeKobo
CONTROL L5039  <Macsen_Shared.GoodbyeKobo>
ROW CAT:Ob6404306494eae84932b L5040 * physical_line
  EN: Don't come back! I've got my eye on you!
  ZH:   * 别再来了！我可盯着你呢！

## SCd7e3aa69e31742f0 | nsfw | datadf/all.ds | Macsen_Shared.NoBoneForDog
CONTROL L5014  <Macsen_Shared.NoBoneForDog>
ROW CAT:O8b2d3a1e2524e7933760 L5015 * physical_line
  EN: What? Are you expecting another bone already?
  ZH:   * 什么？你还想再要一根骨头？
ROW CAT:O110410bdbbcb152bfa80 L5016 * physical_line
  EN: I'd bone myself out of house and home at this rate!
  ZH:   * 照这速度，我非得为了骨头把家底都赔光不可！

## SC94e373e911c95082 | nsfw | datadm/all.ds | Macsen_Shared.NoInventorySpace
CONTROL L5058  <Macsen_Shared.NoInventorySpace>
ROW CAT:Ofddb120147ed6acb3b9d L5059 * physical_line
  EN: Sorry, you are over-encumbered!
  ZH:   * 抱歉，你已经超重了！
ROW CAT:O9841deeef9c3cc8f6562 L5060 * physical_line
  EN: Do you want anything else?
  ZH:   * 还想要点别的吗？

## SC117c91fbdbef4732 | nsfw | datadm/all.ds | Macsen_Shared.NoRockForKobo
CONTROL L5042  <Macsen_Shared.NoRockForKobo>
ROW CAT:O8d8a1aef025e5e2ba809 L5043 * physical_line
  EN: Hmph! What do you want?
  ZH:   * 哼！你有什么事？
ROW CAT:O3de80dc22363fc56ebee L5044 * physical_line
  EN: Lot of nerve showing your face around here, slaver scoundrel!
  ZH:   * 你还有脸在这儿露面，奴隶贩子恶棍！
ROW CAT:Oc84d8d72be90b8c89f3c L5045 * physical_line
  EN: Hey, wait a minute... you're just trying to get free rocks, aren't you?!
  ZH:   * 嘿，等一下……你不就是想白拿石头吗？！
ROW CAT:O1ac5124341d65a765672 L5046 * physical_line
  EN: Get out, and don't come back!
  ZH:   * 滚出去，别再回来！

## SCef7b359cc543ffb2 | nsfw | datadf/all.ds | Macsen_Shared.SoldOut
CONTROL L5049  <Macsen_Shared.SoldOut>
ROW CAT:O4f7f1c6a04609c1cba58 L5050 * physical_line
  EN: Sorry! That was the only one I had. I'm cleared out!
  ZH:   * 抱歉！我就那么一件，已经卖光啦！
ROW CAT:O1a24d5ed173b95a6b4d3 L5051 * physical_line
  EN: Do you want anything else?
  ZH:   * 你还想要点别的吗？

## SC0c8501f54b97d3ca | nsfw | datadf/all.ds | Proto_Fenfen.Goodbye
CONTROL L5059  <Proto_Fenfen.Goodbye>
ROW CAT:Ob3ddabcdcd1c8b373c3d L5060 Anon/Fox physical_line
  EN: Thank you Yiffany!
  ZH:   Anon/Fox: 谢谢你，伊吠妮！

## SC754ea155ff02718a | nsfw | datadm/all.ds | Proto_Fenfen.GoodbyeNotRescued
CONTROL L5075  <Proto_Fenfen.GoodbyeNotRescued>
ROW CAT:O3aa3d757229f980a8a2e L5076 Anon/Fox physical_line
  EN: Please come back soon!
  ZH:   Anon/Fox: 请早点回来！

## SC108b405a3cc96f8f | nsfw | datadf/all.ds | Proto_Fenfen.Hello
CONTROL L5056  <Proto_Fenfen.Hello>
ROW CAT:Ocf3afbcdd54b8a923c7a L5057 Anon/Fox physical_line
  EN: Help, I'm trapped in here!
  ZH:   Anon/Fox: 救命，我被困在这儿了！

## SCdb7fbdb40292ea09 | nsfw | datadf/all.ds | Proto_Fenfen.HelloDog
CONTROL L5065  <Proto_Fenfen.HelloDog>
ROW CAT:O5400094c14bb74cd6d97 L5066 Anon/Fox physical_line
  EN: Oh, it's a dog!
  ZH:   Anon/Fox: 哦，是只狗！

## SC2dc11c61e9c09ae2 | nsfw | datadf/all.ds | Proto_Fenfen.Purchased
CONTROL L5080  <Proto_Fenfen.Purchased>
ROW CAT:O8de7348a90b43f02828a L5081 Anon/Fox physical_line
  EN: Thank you!
  ZH:   Anon/Fox: 谢谢！

## SC39f8f976540435b2 | nsfw | datadm/all.ds | Proto_Fenfen.Purchased
CONTROL L5093  <Proto_Fenfen.Purchased>
ROW CAT:Ob3e4d17b6e6399f4ddce L5094 Anon/Fox physical_line
  EN: Thank you!
  ZH:   Anon/Fox: 谢谢！

## SCfe6cc677594ac7f4 | nsfw | datadf/all.ds | Proto_PrisonKey.GoodbyeDog
CONTROL L5106  <Proto_PrisonKey.GoodbyeDog>
ROW CAT:O692d634294e887c6f897 L5107 * physical_line
  EN: Please come back soon with your master, and a key!
  ZH:   * 请快些带着你的主人和一把钥匙回来！

## SC8969e0ae426ebc79 | nsfw | datadf/all.ds | Proto_PrisonKey.GoodbyeNotRescued
CONTROL L5097  <Proto_PrisonKey.GoodbyeNotRescued>
ROW CAT:Od52adefd4692573dee3a L5098 * physical_line
  EN: Please, come back soon!
  ZH:   * 拜托，快点回来！

## SC9d554cf89b0b7c16 | nsfw | datadf/all.ds | Proto_PrisonKey.TalkAfterRescue.thanks
CONTROL L5135  <Proto_PrisonKey.TalkAfterRescue.thanks>
ROW CAT:O8a7562621e9f8486c398 L5136 * physical_line
  EN: I'm sorry I don't have any data for you. I'm just a placeholder...
  ZH:   * 抱歉，我没有什么数据可以给你。我只是个占位角色……

## SCa114dd4c04c70fdb | nsfw | datadm/all.ds | Proto_PrisonKey.TalkBeforeRescue.bopped
CONTROL L5144  <Proto_PrisonKey.TalkBeforeRescue.bopped>
ROW CAT:Of04eb018d89d17f8b695 L5145 * physical_line
  EN: I'm just a placeholder so you can get rid of your keys!
  ZH:   * 我只是个占位角色，好让你把钥匙处理掉！
ROW CAT:O335d4c063460b8d27009 L5146 * physical_line
  EN: But I'm so glad to see another cosmobreeder!
  ZH:   * 不过能见到另一位宇宙育种者，我太高兴了！

## SC64da9645f1b612c6 | nsfw | datadm/all.ds | Proto_PrisonTazer.Rescue
CONTROL L5174  <Proto_PrisonTazer.Rescue>
ROW CAT:O45c120f5b5a530aecd66 L5175 * physical_line
  EN: These shackles are damaged. You should be able to break them with a few good whacks!
  ZH:   * 这些镣铐坏了。你好好砸几下应该就能砸开！

## SC04a2470f69fa3a3c | nsfw | datadm/all.ds | Proto_PrisonTazer.SoldOut
CONTROL L5180  <Proto_PrisonTazer.SoldOut>
ROW CAT:O77787b4da29f285ec5da L5181 * physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   * 谢谢，不过我已经被救出来了！

## SC081f555ace4291d2 | nsfw | datadf/all.ds | Proto_PrisonTazer.SoldOut
CONTROL L5167  <Proto_PrisonTazer.SoldOut>
ROW CAT:O9f39782bdc6a94f4f2ff L5168 * physical_line
  EN: Thank you, but I'm already rescued!
  ZH:   * 谢谢，不过我已经被救出来了！

## SC09f871f5d728b7cc | nsfw | datadf/all.ds | Proto_PrisonTazer.TalkBeforeRescue.bopped
CONTROL L5170  <Proto_PrisonTazer.TalkBeforeRescue.bopped>
ROW CAT:O0e8fddd21cf198f7bdc4 L5171 * physical_line
  EN: I'm so glad to see another cosmobreeder, even if I'm just a placeholder!
  ZH:   * 能见到另一位宇宙育种者，我太高兴了，哪怕我只是个占位角色！

## SCb805ce02ab3e99dd | nsfw | datadf/all.ds | Test_Hacker1.Goodbye
CONTROL L5184  <Test_Hacker1.Goodbye>
ROW CAT:O9705f7c1aa011f9bd42d L5185 * physical_line
  EN: Bye bye, agent! Bring me something to play wi- I mean upgrade!
  ZH:   * 拜拜，特工！给我带点东西来玩——我是说升级！

## SC16959f491e51a26a | nsfw | datadm/all.ds | Test_Hacker1.GoodbyeKobo
CONTROL L5211  <Test_Hacker1.GoodbyeKobo>
ROW CAT:O90940f1fc1c461df7f7e L5212 * physical_line
  EN: -wait a sec, you're not the delivery guy! G-get out of here right now!
  ZH:   * -等等，你可不是送货那家伙！快、快给我出去！

## SC0708e7baa14af60e | nsfw | datadf/all.ds | Test_Hacker1.Hello
CONTROL L5181  <Test_Hacker1.Hello>
ROW CAT:O0c6fe607d3fe9c1b1af6 L5182 * physical_line
  EN: Heya! Want me to optimize your gear?
  ZH:   * 嘿！要我帮你优化装备吗？

## SC354ed2002651769b | nsfw | datadm/all.ds | Test_Hacker1.Hello
CONTROL L5194  <Test_Hacker1.Hello>
ROW CAT:Ocbfd20820f09061dba65 L5195 * physical_line
  EN: Heya! Want me to optimize your gear?
  ZH:   * 嘿！要我帮你优化装备吗？

## SC1d33dc520bd482fa | nsfw | datadm/all.ds | Test_Hacker1.HelloDog
CONTROL L5200  <Test_Hacker1.HelloDog>
ROW CAT:O2f20e41ceb0567195bc9 L5201 * physical_line
  EN: Hello there Mr. Puppy! Do you want to be my rubber ducky?
  ZH:   * 你好呀，小狗先生！你想当我的橡皮鸭吗？
ROW CAT:Od2d132edb26ee8b3aa62 L5202 * physical_line
  EN: All you have do is stay here and listen to me talk about computers all day!
  ZH:   * 你只要待在这里，听我一整天聊电脑就行！

## SC366c31bba1965e0b | nsfw | datadm/all.ds | Test_Hacker1.HelloKobo
CONTROL L5207  <Test_Hacker1.HelloKobo>
ROW CAT:Oc35ef26d90e400dfbbf5 L5208 * physical_line
  EN: Are you delivering my weekly supplies? I still have some leftover.
  ZH:   * 你是来送我这周的补给的吗？我还剩下一些。
ROW CAT:Od5773885cfc5c92aaec9 L5209 * physical_line
  EN: Since last cycle, I've been increasing my efficiency coefficient while usin-
  ZH:   * 从上个周期起，我一直在提高自己的效率系数，同时用——

## SC4740dd505f30d827 | nsfw | datadf/all.ds | Test_Hacker1.Meeting
CONTROL L5175  <Test_Hacker1.Meeting>
ROW CAT:O702cab4a082ccdcb9e20 L5176 * physical_line
  EN: Greetings, Yiffai. You don't know me, but I kinda snooped your satlink.
  ZH:   * 你好，伊吠。你不认识我，不过我有点偷看了你的卫星链路。
ROW CAT:O83ff4a9d7ef1f822d0f3 L5177 * physical_line
  EN: So I've actually been watching you for a while, and I have a proposition...
  ZH:   * 所以其实我已经观察你有一阵子了，我有个提议……
ROW CAT:O4bcf0750048f867986a2 L5178 * physical_line
  EN: It's simple: You bring me those fancy chips you find out there,
  ZH:   * 很简单：你把在外头找到的那些花哨芯片带给我，
ROW CAT:Oe3d06b898c4987d61b27 L5179 * physical_line
  EN: and I'll power-up your equipment! It's a win-win, obviously!
  ZH:   * 而且我会给你的装备强化！显然是双赢！

## SC2d99dfc7ef94dc2f | nsfw | datadm/all.ds | Test_Hacker1.Talk.radio
CONTROL L5235  <Test_Hacker1.Talk.radio>
ROW CAT:O95357e70c9c6d740151a L5236 * physical_line
  EN: Call me at frequency 28.250 if you need help finding those chips!
  ZH:   * 如果你需要帮忙找那些芯片，就用频率28.250呼我！

## SCbc21ae6879225ba0 | nsfw | datadf/all.ds | Test_Hacker1.Talk.upgrade
CONTROL L5218  <Test_Hacker1.Talk.upgrade>
ROW CAT:Oe51d26aafa44c6800387 L5219 * physical_line
  EN: Does your gear feel weak? Mediocre? Sub-optimal, even?
  ZH:   * 装备用着没劲？性能平平？甚至……还远没调到最佳状态？
ROW CAT:Oae2c10739fe44890c796 L5220 * physical_line
  EN: Well if you can furnish the requisite components, I'll tune it right up!
  ZH:   * 只要把需要的零件备齐，我就能帮你调到位！

## SC060f301606c5f81c | nsfw | datadm/all.ds | Test_Prison1.GoodbyeDog
CONTROL L5256  <Test_Prison1.GoodbyeDog>
ROW CAT:O96a7ba825ba144564cdb L5257 * physical_line
  EN: [Good boy! Come back with your master!]
  ZH:   * [乖狗狗！带着你的主人回来！]

## SC48cba0863b2b5dbd | nsfw | datadf/all.ds | Test_Prison1.GoodbyeDog
CONTROL L5243  <Test_Prison1.GoodbyeDog>
ROW CAT:O39956e6228ca366dcb8d L5244 * physical_line
  EN: [Good boy! Come back with your master!]
  ZH:   * [乖狗狗！带着你的主人回来！]

## SC1d322acd9184b507 | nsfw | datadm/all.ds | Test_Prison1.Hello
CONTROL L5240  <Test_Prison1.Hello>
ROW CAT:O1fb9ca06f1c6d1235f24 L5241 * physical_line
  EN: [Help, I'm in gay baby jail!]
  ZH:   * [救命，我被关在基佬宝宝监狱里了！]

## SC84e8de042769c776 | nsfw | datadm/all.ds | Test_Prison1.HelloDog
CONTROL L5249  <Test_Prison1.HelloDog>
ROW CAT:O90e52bd9810bbf260c94 L5250 * physical_line
  EN: [It... it's a dog! Oh no!]
  ZH:   * [它……是只狗！哦不！]

## SCee069f7f8bd59350 | nsfw | datadm/all.ds | Test_Prison1.SoldOut
CONTROL L5279  <Test_Prison1.SoldOut>
ROW CAT:O8a7120fa085e55e41027 L5280 * physical_line
  EN: [I'm already rescued, Yiffai!]
  ZH:   * [我已经被救出来了，伊吠！]

## SCe587fa5b72d20787 | nsfw | datadm/all.ds | Test_Prison1.TalkBeforeRescue.bopped
CONTROL L5282  <Test_Prison1.TalkBeforeRescue.bopped>
ROW CAT:Ob0d390f17b53ca4f781d L5283 * physical_line
  EN: [I got bopped by the baddies and woke up in here!]
  ZH:   * [我被坏蛋打晕了，醒来就在这儿！]

## SCd093a1066b39687e | nsfw | datadm/all.ds | Test_Slaver1.CancelPurchase
CONTROL L5356  <Test_Slaver1.CancelPurchase>
ROW CAT:O02be93781feeb7a27462 L5357 * physical_line
  EN: That's a shame. Anything else?
  ZH:   * 真遗憾。还要点别的吗？

## SC024a3470e943ce33 | nsfw | datadm/all.ds | Test_Slaver1.ConfirmPurchase
CONTROL L5362  <Test_Slaver1.ConfirmPurchase>
ROW CAT:O337ace084f67d8fa4147 L5363 * physical_line
  EN: Wanna buy it?
  ZH:   * 想买吗？

## SC1e23f72effe35166 | nsfw | datadf/all.ds | Test_Slaver1.ConfirmPurchase
CONTROL L5349  <Test_Slaver1.ConfirmPurchase>
ROW CAT:O04914b473aa66f4bd5a1 L5350 * physical_line
  EN: Wanna buy it?
  ZH:   * 想买吗？

## SCd643a17f048f464a | nsfw | datadm/all.ds | Test_Slaver1.GasMask
CONTROL L5344  <Test_Slaver1.GasMask>
ROW CAT:O2386692a1e25edb82515 L5345 * physical_line
  EN: Need to explore a toxic area? Bring a few of these along!
  ZH:   * 要探索有毒区域？带上几个这个！

## SCc4d63f35d3c7eee7 | nsfw | datadf/all.ds | Test_Slaver1.GoodbyeNoID
CONTROL L5319  <Test_Slaver1.GoodbyeNoID>
ROW CAT:Of0d42e0c2925919cc8c3 L5320 * physical_line
  EN: Bye bye, pup. Come back when you're older!
  ZH:   * 拜拜，小狗。等你长大点再来吧！

## SC03b5128a70a097ed | nsfw | datadf/all.ds | Test_Slaver1.HasID
CONTROL L5315  <Test_Slaver1.HasID>
ROW CAT:O15ba4509342fb76c82cc L5316 * physical_line
  EN: Hmm... twenty one years old. Looks legitimate.
  ZH:   * 嗯……二十一岁。看起来是真的。
ROW CAT:O072ed01dc905f7e9ba7b L5317 * physical_line
  EN: Alright, can I get you something?
  ZH:   * 好了，要我给你来点什么吗？

## SC9d24f73693506100 | nsfw | datadm/all.ds | Test_Slaver1.HelloNoJuice
CONTROL L5303  <Test_Slaver1.HelloNoJuice>
CONTROL L5304    if { isFeral() } {
ROW CAT:O0f84d762cc7e7056644c L5305 * physical_line
  EN: Oh, it's a dog...
  ZH:     * 哦，是条狗啊……
ROW CAT:Oa963b9ceca8d41d8d8c3 L5306 * physical_line
  EN: I'm afraid I can't do anything for you, pup.
  ZH:     * 恐怕我帮不了你，小家伙。
CONTROL L5307    } else {
ROW CAT:Oc271ce1615d2435abce3 L5308 * physical_line
  EN: Oh, hello. This is my shop. Well, it's supposed to be.
  ZH:     * 哦，你好。这是我的店。呃，本来应该是。
ROW CAT:Ode0ba5aab57b2b5e217b L5309 * physical_line
  EN: I've just been feeling under the weather lately... like I'm missing something.
  ZH:     * 我最近有点不舒服……总觉得少了点什么。
ROW CAT:O798577e7627f01c15148 L5310 * physical_line
  EN: I'm afraid you'll have to come back later.
  ZH:     * 恐怕你得改天再来了。
CONTROL L5311    }

## SC52b5c806a0c71b4a | nsfw | datadm/all.ds | Test_Slaver1.IonCannon
CONTROL L5313  <Test_Slaver1.IonCannon>
ROW CAT:Oac140583d7c006f15d6e L5314 * physical_line
  EN: [This tests the Ion Cannon mode for the world map.]
  ZH:   * [这是在测试世界地图的离子炮模式。]

## SC438c9d1ee4281d21 | nsfw | datadm/all.ds | Test_Slaver1.NoBoneForDog
CONTROL L5296  <Test_Slaver1.NoBoneForDog>
ROW CAT:Oaaa3fb03c956189d5974 L5297 * physical_line
  EN: What? Are you expecting another bone already?
  ZH:   * 什么？你还想再要一根骨头？
ROW CAT:O4eb051a773c98b6c2e1d L5298 * physical_line
  EN: I'd bone myself out of house and home at this rate!
  ZH:   * 照这速度，我非得为了骨头把家底都赔光不可！

## SCf85dfd6d927078cd | nsfw | datadf/all.ds | Test_Slaver1.NoInventorySpace
CONTROL L5356  <Test_Slaver1.NoInventorySpace>
ROW CAT:Oc7082694cf4a11e3d143 L5357 * physical_line
  EN: Sorry, you are over-encumbered!
  ZH:   * 抱歉，你已经超重了！
ROW CAT:O75e7695fa9f05ef67169 L5358 * physical_line
  EN: Do you want anything else?
  ZH:   * 你还想要点别的吗？

## SCd8ab2b790e9d8dcc | nsfw | datadf/all.ds | Test_Slaver1.NotEnoughMoney
CONTROL L5352  <Test_Slaver1.NotEnoughMoney>
ROW CAT:Ob1965411c3b252350661 L5353 * physical_line
  EN: No Lect, no sale. And no discounts!
  ZH:   * 没有 Lect，就没有交易。而且绝不打折！
ROW CAT:Oae31f43673ecced05a82 L5354 * physical_line
  EN: Do you want anything else?
  ZH:   * 你还想要点别的吗？

## SCba650e0013327262 | nsfw | datadf/all.ds | Test_Slaver1.Pickaxe
CONTROL L5337  <Test_Slaver1.Pickaxe>
ROW CAT:Ob57d57ad54c7b2d5dc73 L5338 * physical_line
  EN: [Pickaxe description]
  ZH:   * [镐子描述]

## SC5a57386039dcddd1 | nsfw | datadf/all.ds | Test_Slaver1.PsyTea
CONTROL L5325  <Test_Slaver1.PsyTea>
ROW CAT:O95405ec7fa339e567680 L5326 * physical_line
  EN: This tea will recover your psychic power!
  ZH:   * 这茶能恢复你的灵能！

## SCf0fde83f241e7c05 | nsfw | datadm/all.ds | Test_Slaver1.Purchased
CONTROL L5359  <Test_Slaver1.Purchased>
ROW CAT:Od58368550eb7db383b56 L5360 * physical_line
  EN: Thanks a million! Anything else?
  ZH:   * 太谢谢你了！还要点别的吗？

## SCf7c85570bbec2ce9 | nsfw | datadm/all.ds | Test_Slaver1.ThanksForJuice
CONTROL L5316  <Test_Slaver1.ThanksForJuice>
ROW CAT:Oacbe5bb12e28aeaf928f L5317 * physical_line
  EN: What?! For me? Wait... is this...
  ZH:   * 什么？！给我的？等等……这是不是……
ROW CAT:O90050bd3968a6ff964c7 L5318 * physical_line
  EN: It's my special juice! Just one swig of this and I'm ready for business!
  ZH:   * 这是我的特制果汁！只要喝上一口，我马上就能开张做生意！
ROW CAT:O121994f0c8f3b51476e3 L5319 * physical_line
  EN: Alright, can I get you something?
  ZH:   * 好了，要我给你来点什么吗？

## SCcd1d2711b511cec8 | nsfw | datadf/all.ds | Test_Slaver1.Vitamin
CONTROL L5328  <Test_Slaver1.Vitamin>
ROW CAT:O814a1e99244a92105a61 L5329 * physical_line
  EN: This vitamin will increase your vitality!
  ZH:   * 这维生素能提高你的活力！

