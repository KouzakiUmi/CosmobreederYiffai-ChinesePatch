# batch-13 精校工单：毛鼠旁白提示（MauserHints）

英文与当前中文都按整场连读；`current` 是构建候选的实际显示行（以本批参照摘录与 ORDER 记的候选为准）。
ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。

## SC0bd9584e37e7ed33 | nsfw | datadf/all.ds | MauserHints.AreaC.PigobinHint noselect
CONTROL L3582  <MauserHints.AreaC.PigobinHint noselect>
ROW CAT:O57c1d51ff433c21c6c4a L3583 Mauser physical_line
  EN: [THAT SECTION OF SCEAFYA CAN GET PRETTY DARK]
  ZH:   Mauser: [斯凯菲亚那一段会变得挺黑的，都是因为这一带的树。]
ROW CAT:Oc54ca0b3d5d711080f03 L3584 Mauser physical_line
  EN: [THANKS TO ALL THE TREES IN THE AREA.]
  ZH: 
ROW CAT:O3a0b3aa3acc3b24d2421 L3585 Mauser physical_line
  EN: [IF YOU GRAB A FLASHLIGHT SOMEWHERE AROUND THERE]
  ZH:   Mauser: [你要是能在那一带弄到手电筒，那大概就能给这局面照点亮光！]
ROW CAT:O606d9d79d3acebcf857c L3586 Mauser physical_line
  EN: [THAT'D PROBABLY SHINE LIGHT ON THE SITUATION!]
  ZH: 

## SC928066794d1c49a1 | nsfw | datadm/all.ds | MauserHints.AreaC.PigobinHint noselect
CONTROL L3645  <MauserHints.AreaC.PigobinHint noselect>
ROW CAT:Ofe61bf2e2c59a9d742ce L3646 Mauser physical_line
  EN: [THAT SECTION OF SCEAFYA CAN GET PRETTY DARK]
  ZH:   Mauser: [斯凯菲亚那一段会变得挺黑的，都是因为这一带的树。]
ROW CAT:Oef08946e062fdb9c7fd2 L3647 Mauser physical_line
  EN: [THANKS TO ALL THE TREES IN THE AREA.]
  ZH: 
ROW CAT:O20344914793486543264 L3648 Mauser physical_line
  EN: [IF YOU GRAB A FLASHLIGHT SOMEWHERE AROUND THERE]
  ZH:   Mauser: [你要是能在那一带弄到手电筒，那大概就能给这局面照点亮光！]
ROW CAT:O95d57ea8f3a59f4669c5 L3649 Mauser physical_line
  EN: [THAT'D PROBABLY SHINE LIGHT ON THE SITUATION!]
  ZH: 

## SC1db30291a8d893bd | nsfw | datadf/all.ds | MauserHints.AreaC_OneBossDefeated
CONTROL L3589  <MauserHints.AreaC_OneBossDefeated>
CONTROL L3590    if { f(ClassicPigobinV3_defeated) || f(ClassicEnelye_defeated) } {
CONTROL L3591      if { f(ClassicEnelye_defeated) } {
CONTROL L3592        if { hasItem(SpecialTorch) } {
CONTROL L3593          include { MauserHints_AreaC.PigobinHint }
CONTROL L3594        } else {
ROW CAT:O89d403e553e56e5a2048 L3595 Mauser physical_line
  EN: [WE'VE GOT A MEMO HERE THAT ONE AGENT SOLD A FLASHLIGHT]
  ZH:         Mauser: [我们这儿有条备忘录，说有个特工把一支手电筒卖给了一只小狗……结果它转眼就弄丢了。]
ROW CAT:O2e9cc161a32b47c8864c L3596 Mauser physical_line
  EN: [TO A TINY DOG... WHO PROMPTLY LOST IT.]
  ZH: 
ROW CAT:O8485c68de5472fc628f5 L3597 Mauser physical_line
  EN: [THAT WAS SOMEWHERE IN THE SOUTHWEST OF THAT AREA!]
  ZH:         Mauser: [就在那片区域的西南部！]
CONTROL L3598        }
CONTROL L3599      } else {
CONTROL L3600        if { hasItem(SpecialKeycard3) } {
CONTROL L3601          include { MauserHints_AreaC.EnelyeHint } 
CONTROL L3602        } else {
ROW CAT:Ob49a6e864169d2dbfee9 L3603 Mauser physical_line
  EN: [THE HIGHER YOU GO IN THIS SECTOR THE MORE ELVES SHOW UP!]
  ZH:         Mauser: [这个扇区越往上走，出现的精灵就越多！]
ROW CAT:Oedb9281a0eaca1f0712f L3604 Mauser physical_line
  EN: [THAT MUST MEAN THAT THEY'RE PROTECTING SOMETHING!]
  ZH:         Mauser: [这肯定说明他们在守着什么！]
ROW CAT:Oa69c58bef5b895626083 L3605 Mauser physical_line
  EN: [GO FIND OUT WHAT IT IS!]
  ZH:         Mauser: [去搞清楚那是什么！]
CONTROL L3606        }
CONTROL L3607      }
CONTROL L3608    }

## SCaa167d4a176e4ef5 | nsfw | datadm/all.ds | MauserHints.AreaC_OneBossDefeated
CONTROL L3651  <MauserHints.AreaC_OneBossDefeated>
CONTROL L3652    if { f(ClassicPigobinV3_defeated) || f(ClassicEnelye_defeated) } {
CONTROL L3653      if { f(ClassicEnelye_defeated) } {
CONTROL L3654        if { hasItem(SpecialTorch) } {
CONTROL L3655          include { MauserHints_AreaC.PigobinHint }
CONTROL L3656        } else {
ROW CAT:O88cba587a4d7b2de16ae L3657 Mauser physical_line
  EN: [WE'VE GOT A MEMO HERE THAT ONE AGENT SOLD A FLASHLIGHT]
  ZH:         Mauser: [我们这儿有条备忘录，说有个特工把一支手电筒卖给了一只小狗……它转眼就弄丢了。]
ROW CAT:Oc28c47a01f956ee57e52 L3658 Mauser physical_line
  EN: [TO A TINY DOG... WHO PROMPTLY LOST IT.]
  ZH: 
ROW CAT:O1b005670485e61715bba L3659 Mauser physical_line
  EN: [THAT WAS SOMEWHERE IN THE SOUTHWEST OF THAT AREA!]
  ZH:         Mauser: [那地方就在这片区域的西南方！]
CONTROL L3660        }
CONTROL L3661      } else {
CONTROL L3662        if { hasItem(SpecialKeycard3) } {
CONTROL L3663          include { MauserHints_AreaC.EnelyeHint } 
CONTROL L3664        } else {
ROW CAT:O17734621cdf275b8917a L3665 Mauser physical_line
  EN: [THE HIGHER YOU GO IN THIS SECTOR THE MORE ELVES SHOW UP!]
  ZH:         Mauser: [这片区域越往高处走，精灵就越多！]
ROW CAT:Oaaaf2b3e77c777dfa068 L3666 Mauser physical_line
  EN: [THAT MUST MEAN THAT THEY'RE PROTECTING SOMETHING!]
  ZH:         Mauser: [这肯定说明他们在守着什么！]
ROW CAT:Od0c6372b9ca88ce012fc L3667 Mauser physical_line
  EN: [GO FIND OUT WHAT IT IS!]
  ZH:         Mauser: [快去查查是什么！]
CONTROL L3668        }
CONTROL L3669      }
CONTROL L3670    }

## SC16650bbc771784c4 | nsfw | datadm/all.ds | MauserHints_Area0.AfterBigbold1Killed
CONTROL L3454  <MauserHints_Area0.AfterBigbold1Killed>
CONTROL L3455    if { f(ClassicBigbold_defeated) } {
ROW CAT:Obee3e580d1304d7cb60c L3456 Mauser physical_line
  EN: [YOU HAVE TO TRACK DOWN THAT BIGBOLD!]
  ZH:     Mauser: [你得追踪到那只大壮兽！]
ROW CAT:Of50e704bcb4c3d441695 L3457 Mauser physical_line
  EN: [HE WENT FURTHER INTO THE FACILITY, FOLLOW HIM!]
  ZH:     Mauser: [他往设施更深处去了，追上去！]
CONTROL L3458    }

## SC57a88c132be4705d | nsfw | datadf/all.ds | MauserHints_Area0.AfterBigbold1Killed
CONTROL L3392  <MauserHints_Area0.AfterBigbold1Killed>
CONTROL L3393    if { f(ClassicBigbold_defeated) } {
ROW CAT:Oa3ca8a74a91025ed7325 L3394 Mauser physical_line
  EN: [YOU HAVE TO TRACK DOWN THAT BIGBOLD!]
  ZH:     Mauser: [你得追踪到那只大壮兽！]
ROW CAT:Oe3399156cc2f89faf2fa L3395 Mauser physical_line
  EN: [HE WENT FURTHER INTO THE FACILITY, FOLLOW HIM!]
  ZH:     Mauser: [他往设施更深处去了，跟上他！]
CONTROL L3396    }

## SC1c96012cacee79f9 | nsfw | datadf/all.ds | MauserHints_Area0.AfterBigboldV2KilledEscape
CONTROL L3398  <MauserHints_Area0.AfterBigboldV2KilledEscape>
CONTROL L3399    if { f(ClassicBigboldV2_defeated) } {
ROW CAT:O99991becac7bc48d8fbd L3400 Mauser physical_line
  EN: [THAT PLACE LOOKS LIKE IT'S GONNA COLLAPSE!]
  ZH:     Mauser: [那地方看着就要塌了！]
ROW CAT:O9382939c8f2116eafbfb L3401 Mauser physical_line
  EN: [GET OUT OF THERE!!!]
  ZH:     Mauser: [快从那儿出来！！！]
CONTROL L3402    }

## SCc51db72a0adbcd7d | nsfw | datadm/all.ds | MauserHints_Area0.AfterBigboldV2KilledEscape
CONTROL L3460  <MauserHints_Area0.AfterBigboldV2KilledEscape>
CONTROL L3461    if { f(ClassicBigboldV2_defeated) } {
ROW CAT:Od384f200d9ea6d199868 L3462 Mauser physical_line
  EN: [THAT PLACE LOOKS LIKE IT'S GONNA COLLAPSE!]
  ZH:     Mauser: [那地方看起来快要塌了！]
ROW CAT:Oe1633cdb2ccea912b68a L3463 Mauser physical_line
  EN: [GET OUT OF THERE!!!]
  ZH:     Mauser: [快离开那里！！！]
CONTROL L3464    }

## SC3c709e08abecdd6b | nsfw | datadf/all.ds | MauserHints_Area0.AfterBigboldV2KilledSafe
CONTROL L3404  <MauserHints_Area0.AfterBigboldV2KilledSafe>
CONTROL L3405    if { f(story_escaped_ClassicBigboldV2) } {
ROW CAT:O6bc935e82401f1e26f12 L3406 Mauser physical_line
  EN: [REPORTS INDICATE THAT THERE IS AN AGENT SOMEWHERE IN]
  ZH:     Mauser: [报告显示，有一名特工就在东部传输点附近。]
ROW CAT:Oe699925d01ef9730a9c8 L3407 Mauser physical_line
  EN: [THE VICINITY OF THE EASTERN TRANSMISSION POINT.]
  ZH: 
ROW CAT:O89ecdbd4fcec30d2f314 L3408 Mauser physical_line
  EN: [DO YOUR BEST TO RESCUE THEM!]
  ZH:     Mauser: [尽力把人救出来！]
CONTROL L3409    }

## SC8b485ccdf0b6b9fc | nsfw | datadm/all.ds | MauserHints_Area0.AfterBigboldV2KilledSafe
CONTROL L3466  <MauserHints_Area0.AfterBigboldV2KilledSafe>
CONTROL L3467    if { f(story_escaped_ClassicBigboldV2) } {
ROW CAT:Oec5baf9874c2a41f45b6 L3468 Mauser physical_line
  EN: [REPORTS INDICATE THAT THERE IS AN AGENT SOMEWHERE IN]
  ZH:     Mauser: [报告显示，有一名特工就在东部传输点附近。]
ROW CAT:Oebd96ca254a41ea2e035 L3469 Mauser physical_line
  EN: [THE VICINITY OF THE EASTERN TRANSMISSION POINT.]
  ZH: 
ROW CAT:Oda04f2a1eac952a4b1e3 L3470 Mauser physical_line
  EN: [DO YOUR BEST TO RESCUE THEM!]
  ZH:     Mauser: [尽力救出对方！]
CONTROL L3471    }

## SCa4aeea4fcaaf7602 | nsfw | datadf/all.ds | MauserHints_Area0.AfterFirstAgentRescued
CONTROL L3411  <MauserHints_Area0.AfterFirstAgentRescued>
CONTROL L3412    if { hasItem(Agent*0B) || f(ctx_entered_area_AreaB) } {
ROW CAT:O44c85c169b59493dd7e9 L3413 Mauser physical_line
  EN: [THAT BRACE THAT YOU FOUND SHOULD COME IN HANDY FOR]
  ZH:     Mauser: [你找到的那个护腕应该能派上用场，用来前往新区域！]
ROW CAT:O8af90f3574f5c3c6a51e L3414 Mauser physical_line
  EN: [REACHING NEW AREAS!]
  ZH: 
CONTROL L3415    }

## SCee65d81001fa7f60 | nsfw | datadm/all.ds | MauserHints_Area0.AfterFirstAgentRescued
CONTROL L3473  <MauserHints_Area0.AfterFirstAgentRescued>
CONTROL L3474    if { hasItem(Agent*0B) } {
ROW CAT:O62d99d3f1e4af29c37ee L3475 Mauser physical_line
  EN: [THAT BRACE THAT YOU FOUND SHOULD COME IN HANDY FOR]
  ZH:     Mauser: [你找到的那个护腕应该能派上用场，用来前往新区域！]
ROW CAT:O65f249447314decf9720 L3476 Mauser physical_line
  EN: [REACHING NEW AREAS!]
  ZH: 
CONTROL L3477    }

## SC096b5ffbba08d9e5 | nsfw | datadm/all.ds | MauserHints_Area0.BeforeBigbold1Killed
CONTROL L3450  <MauserHints_Area0.BeforeBigbold1Killed>
ROW CAT:O64d94cd387ae9861a245 L3451 Mauser physical_line
  EN: [YOU NEED TO RECOVER YOUR EQUIPMENT, YIFFAI!]
  ZH:   Mauser: [伊吠，你得把装备找回来！]
ROW CAT:Oa7563bd2465f3f0e6647 L3452 Mauser physical_line
  EN: [THE THIEVES COULDN'T HAVE GONE TOO FAR.]
  ZH:   Mauser: [那些小偷跑不了多远的。]

## SC2870fbd3d222a195 | nsfw | datadf/all.ds | MauserHints_Area0.BeforeBigbold1Killed
CONTROL L3388  <MauserHints_Area0.BeforeBigbold1Killed>
ROW CAT:O1f51ec2ff69921ba8e2b L3389 Mauser physical_line
  EN: [YOU NEED TO RECOVER YOUR EQUIPMENT, YIFFANY!]
  ZH:   Mauser: [你得找回你的装备，伊吠妮！]
ROW CAT:Ob60ced94cd981c1e8550 L3390 Mauser physical_line
  EN: [THE THIEVES COULDN'T HAVE GONE TOO FAR.]
  ZH:   Mauser: [那些小偷不可能走太远。]

## SC3a12fdcd058b0e59 | nsfw | datadf/all.ds | MauserHints_Area0.Endgame
CONTROL L3424  <MauserHints_Area0.Endgame>
CONTROL L3425    if { f(ClassicPigobinV3_defeated) && f(ClassicEnelye_defeated) } {
CONTROL L3426      if { !f(ClassicStarkillV3_defeated) } {
ROW CAT:Oc0f91c324721a0de3d2b L3427 Mauser physical_line
  EN: [YOUR NAVMAP SHOULD SHOW WHERE YOUR BROTHER IS!]
  ZH:       Mauser: [你的导航图应该能显示你弟弟在哪儿！]
ROW CAT:O780892b434d14bbc0106 L3428 Mauser physical_line
  EN: [GO AND SLAP SOME SENSE INTO THEM!]
  ZH:       Mauser: [去把他打醒！]
CONTROL L3429      } else if { !hasItem(CosmoBody) || !hasItem(CosmoHead) } {
ROW CAT:O2c8c7e60fb8931578f94 L3430 Mauser physical_line
  EN: [ARE YOU REALLY GOING UP TO THE PRISON MOON?]
  ZH:       Mauser: [你真要上那颗监狱卫星吗？]
ROW CAT:O3c46cacd9182b0686efc L3431 Mauser physical_line
  EN: [YOU'LL WANT TO GET YOUR COSMOSUIT BACK FIRST]
  ZH:       Mauser: [你最好先把宇宙服拿回来。]
ROW CAT:O168ef941c1d3cab5688f L3432 Mauser physical_line
  EN: [THOSE DWEEBY SQUEAKERS COULDN'T HAVE TAKEN IT FAR!]
  ZH:       Mauser: [那些窝囊的吱吱怪不可能把它带远！]
CONTROL L3433      } else {
ROW CAT:Obc6a6b9a9c6ccf5dacd5 L3434 Mauser physical_line
  EN: [YOU'VE GOT YOUR COSMOSUIT BACK TOGETHER AGAIN!]
  ZH:       Mauser: [你把宇宙服重新拼好了！]
ROW CAT:O87f050fa52168dd7008a L3435 Mauser physical_line
  EN: [NOTHING'S STOPPING YOU FROM HEADING UP]
  ZH:       Mauser: [没什么能拦着你前往那颗名叫“流放地”的监狱卫星！]
ROW CAT:Oc3c9abcbe95d540c20e3 L3436 Mauser physical_line
  EN: [TO THE PRISON MOON NAMED "EXILE"!]
  ZH: 
CONTROL L3437      }
CONTROL L3438    }

## SC567b9e156beb4379 | nsfw | datadm/all.ds | MauserHints_Area0.Endgame
CONTROL L3486  <MauserHints_Area0.Endgame>
CONTROL L3487    if { f(ClassicPigobinV3_defeated) && f(ClassicEnelye_defeated) } {
CONTROL L3488      if { !f(ClassicStarkillV3_defeated) } {
ROW CAT:O4bb1917176b03c96c3f0 L3489 Mauser physical_line
  EN: [YOUR NAVMAP SHOULD SHOW WHERE YOUR SISTER IS!]
  ZH:       Mauser: [你的导航图应该标着你姐姐的位置！]
ROW CAT:O201825a8a0a17f3f659f L3490 Mauser physical_line
  EN: [GO AND SLAP SOME SENSE INTO THEM!]
  ZH:       Mauser: [去把她揍醒吧！]
ROW CAT:Ocf0ed5914e20a248647a L3491 Mauser physical_line
  EN: [...BUT NOT TOO HARD!]
  ZH:       Mauser: [……不过可别下手太重！]
CONTROL L3492      } else if { !hasItem(CosmoBody) || !hasItem(CosmoHead) } {
ROW CAT:O493c14fdafa36c200802 L3493 Mauser physical_line
  EN: [ARE YOU REALLY GOING UP TO THE PRISON MOON?]
  ZH:       Mauser: [你真的要去那座监狱月球吗？]
ROW CAT:O8af677897cd0d331b6e2 L3494 Mauser physical_line
  EN: [YOU'LL WANT TO GET YOUR COSMOSUIT BACK FIRST]
  ZH:       Mauser: [你最好先把自己的宇宙服找回来]
ROW CAT:O9948c8af8d258c2d5b50 L3495 Mauser physical_line
  EN: [THOSE DWEEBY SQUEAKERS COULDN'T HAVE TAKEN IT FAR!]
  ZH:       Mauser: [那些窝囊的吱吱怪不可能把它带远！]
CONTROL L3496      } else {
ROW CAT:O1e76c90271a952dcb597 L3497 Mauser physical_line
  EN: [YOU'VE GOT YOUR COSMOSUIT BACK TOGETHER AGAIN!]
  ZH:       Mauser: [你的宇宙服又凑齐了！]
ROW CAT:O8acb8d21dd835b5c8209 L3498 Mauser physical_line
  EN: [NOTHING'S STOPPING YOU FROM HEADING UP]
  ZH:       Mauser: [没有什么能拦着你前往那颗名叫“流放地”的监狱卫星！]
ROW CAT:Oe2a4f8c91004efcb1f06 L3499 Mauser physical_line
  EN: [TO THE PRISON MOON NAMED "EXILE"!]
  ZH: 
CONTROL L3500      }
CONTROL L3501    }

## SC5b5bdf78b8b742d0 | nsfw | datadm/all.ds | MauserHints_Area0.ReturnFromAreaB
CONTROL L3479  <MauserHints_Area0.ReturnFromAreaB>
CONTROL L3480    if { f(ctx_entered_area_AreaB) } {
ROW CAT:Occ991800e26909127da5 L3481 Mauser physical_line
  EN: [GEE YIFFAI, WHATCHU YOU DOING BACK IN THAT OLD PLACE?]
  ZH:     Mauser: [哎呀伊吠，你跑回这老地方干嘛呀？]
ROW CAT:O8431c6d535c2fc46e1b5 L3482 Mauser physical_line
  EN: [THERE'S OTHER THINGS TO DO IF YOU USE THE TELEPORTAL]
  ZH:     Mauser: [要是用传送门去探索别的区域，还有别的事情可做！]
ROW CAT:Oe60de5b1b99a00563b4d L3483 Mauser physical_line
  EN: [AND EXPLORE OTHER AREAS!]
  ZH: 
CONTROL L3484    }

## SCba47a5e8f5af9dac | nsfw | datadf/all.ds | MauserHints_Area0.ReturnFromAreaB
CONTROL L3417  <MauserHints_Area0.ReturnFromAreaB>
CONTROL L3418    if { f(ctx_entered_area_AreaB) } {
ROW CAT:O72465c1daa40ce3a9d61 L3419 Mauser physical_line
  EN: [GEE YIFFANY, WHAT'S GOING ON BACK IN THAT AREA?]
  ZH:     Mauser: [哎呀，伊吠妮，那片区域那边怎么了？]
ROW CAT:O4ce88a97a0efcf0c2592 L3420 Mauser physical_line
  EN: [AREN'T THERE MORE INTERESTING PLACES THAT YOU COULD SEE]
  ZH:     Mauser: [通过传送门去别的区域探索，不是还能看到更有意思的地方吗？]
ROW CAT:O74fc355e9727d6aa81e7 L3421 Mauser physical_line
  EN: [IF YOU TAKE A TELE- PORTAL TO EXPLORE OTHER AREAS?]
  ZH: 
CONTROL L3422    }

## SC27e73dec7f1dda6a | nsfw | datadm/all.ds | MauserHints_AreaB.AfterEnteredAreaB
CONTROL L3583  <MauserHints_AreaB.AfterEnteredAreaB>
ROW CAT:O97766d4122e94bd80ffa L3584 Mauser physical_line
  EN: [YOU'RE CURRENTLY IN AN OLD ABANDONED DEPOT, YIFFAI.]
  ZH:   Mauser: [你现在在一座废弃的旧仓库里，伊吠。]
ROW CAT:O97d33dda0f23d930753a L3585 Mauser physical_line
  EN: [WE LOST CONTACT WITH 2 AGENTS IN THAT SECTOR]
  ZH:   Mauser: [我们在那个片区和2名特工失去了联络，所以盯紧点，留意他们！]
ROW CAT:Ocb7d61bebd1616e34da7 L3586 Mauser physical_line
  EN: [SO KEEP YOUR EYES PEELED FOR THEM!]
  ZH: 
ROW CAT:O0523fc3129dab4afb160 L3587 Yiffai physical_line
  EN: [AFFIRMATIVE, WILL KEEP AN EYE OUT.]
  ZH:   Yiffai: [明白，我会留意。]

## SC2ed631bfbecca526 | nsfw | datadf/all.ds | MauserHints_AreaB.AfterEnteredAreaB
CONTROL L3520  <MauserHints_AreaB.AfterEnteredAreaB>
ROW CAT:O7c244fe2894a16703765 L3521 Mauser physical_line
  EN: [YOU'RE CURRENTLY IN AN OLD ABANDONED DEPOT, YIFFANY.]
  ZH:   Mauser: [你现在在一座废弃的旧仓库里，伊吠妮。]
ROW CAT:O36def2d29748b84fc650 L3522 Mauser physical_line
  EN: [WE LOST CONTACT WITH 2 AGENTS IN THAT SECTOR]
  ZH:   Mauser: [我们和那个扇区的2名特工失去了联系，所以留神找他们！]
ROW CAT:O556f8e286b8c7b719690 L3523 Mauser physical_line
  EN: [SO KEEP YOUR EYES PEELED FOR THEM!]
  ZH: 
ROW CAT:O1c48328a8bc5d14d76d4 L3524 Yiffany physical_line
  EN: [ROGER, I'LL KEEP AN EYE OUT.]
  ZH:   Yiffany: [收到，我会留意的。]

## SC370a1f4dea390913 | sfw | datadm/all.ds | MauserHints_AreaB.AfterEnteredAreaB
CONTROL L3513  <MauserHints_AreaB.AfterEnteredAreaB>
ROW SFW0efec171fbb13293f01f8f72 L3514 - physical_line
  EN: [YOU'RE CURRENTLY IN AN OLD ABANDONED DEPOT, YIFFAI.]
  ZH:   Mauser: [你现在在一座废弃的旧仓库里，伊吠。]
ROW SFWcc1c6a838e8d7dedb35d7c2c L3515 - physical_line
  EN: [WE LOST CONTACT WITH 2 AGENTS IN THAT SECTOR]
  ZH:   Mauser: [我们在那个片区和2名特工失去了联络，所以盯紧点，留意他们！]
ROW SFWefcd89cea0a176b4c7285fcd L3516 - physical_line
  EN: [SO KEEP YOUR EYES PEELED FOR THEM!] 
  ZH: 
ROW SFW9f31d4625b480d8ecf195c6f L3517 - physical_line
  EN: [AFFIRMATIVE, WILL KEEP AN EYE OUT.]
  ZH:   Yiffai: [明白，我会留意。]

## SCe103949e27738048 | sfw | datadf/all.ds | MauserHints_AreaB.AfterEnteredAreaB
CONTROL L3471  <MauserHints_AreaB.AfterEnteredAreaB>
ROW SFW7cf0f95e206e902b428f4edb L3472 - physical_line
  EN: [YOU'RE CURRENTLY IN AN OLD ABANDONED DEPOT, YIFFANY.]
  ZH:   Mauser: [你现在在一座废弃的旧仓库里，伊吠妮。]
ROW SFW4403840dbcb63809859c9242 L3473 - physical_line
  EN: [WE LOST CONTACT WITH 2 AGENTS IN THAT SECTOR]
  ZH:   Mauser: [我们和那个扇区的2名特工失去了联系，所以留神找他们！]
ROW SFW4b339dfc63ada9959224d6b9 L3474 - physical_line
  EN: [SO KEEP YOUR EYES PEELED FOR THEM!] 
  ZH: 
ROW SFWd8752572efb02f1a6c58ce8e L3475 - physical_line
  EN: [ROGER, I'LL KEEP AN EYE OUT.]
  ZH:   Yiffany: [收到，我会留意的。]

## SC2c6addff352bfb13 | nsfw | datadf/all.ds | MauserHints_AreaB.AfterPsyStar
CONTROL L3532  <MauserHints_AreaB.AfterPsyStar>
CONTROL L3533    if { hasItem(ZenerStar) } {
ROW CAT:Oc55b17629c9466a69030 L3534 Mauser physical_line
  EN: [ARE YOU SURE YOU'RE OKAY, YIFFANY?]
  ZH:     Mauser: [你确定没事吗，伊吠妮？]
ROW CAT:Oce3606d9440e4057ffc5 L3535 Mauser physical_line
  EN: [WHEN YOU SAID YOU HEARD A VOICE THAT SAID]
  ZH:     Mauser: [你说你听见一个声音在讲「按 SELECT 循环切换超能力者能力，再用 UP+ATTACK 使用该能力」时，我还以为你这趟任务已经神志不清了！]
ROW CAT:O1b5fec6d933a38f50785 L3536 Mauser physical_line
  EN: ["PRESS SELECT TO CYCLE THROUGH ESPER ABILITIES"]
  ZH: 
ROW CAT:O527bf21de747b2fff2a4 L3537 Mauser physical_line
  EN: ["AND THEN USE THE ABILITY WITH UP+ATTACK"]
  ZH: 
ROW CAT:O3789ad543e5c5e5205b9 L3538 Mauser physical_line
  EN: [I THOUGHT YOU MIGHT'VE BEEN OUT FOR THE MISSION!]
  ZH: 
CONTROL L3539    }

## SC82f75109d82edca1 | nsfw | datadm/all.ds | MauserHints_AreaB.AfterPsyStar
CONTROL L3595  <MauserHints_AreaB.AfterPsyStar>
CONTROL L3596    if { hasItem(ZenerStar) } {
ROW CAT:O2245fcc383bc018b8176 L3597 Mauser physical_line
  EN: [ARE YOU SURE YOU'RE OKAY, YIFFAI?]
  ZH:     Mauser: [你确定自己没事吗，伊吠？]
ROW CAT:O8b854625d85440b6e163 L3598 Mauser physical_line
  EN: [WHEN YOU SAID YOU HEARD A VOICE THAT SAID]
  ZH:     Mauser: [你说听见有声音叫你“按 SELECT 键循环切换超能力，再按 UP+ATTACK 发动能力”，我还以为你没法继续执行任务了！]
ROW CAT:O62c9591646e11da015c7 L3599 Mauser physical_line
  EN: ["PRESS SELECT TO CYCLE THROUGH ESPER ABILITIES"]
  ZH: 
ROW CAT:O7cbdd0b19da897f7abae L3600 Mauser physical_line
  EN: ["AND THEN USE THE ABILITY WITH UP+ATTACK"]
  ZH: 
ROW CAT:O207b66afd101091acc52 L3601 Mauser physical_line
  EN: [I THOUGHT YOU MIGHT'VE BEEN OUT FOR THE MISSION!]
  ZH: 
CONTROL L3602    }

## SC83a94423b5d46770 | nsfw | datadf/all.ds | MauserHints_AreaB.AfterWerehundDefeat
CONTROL L3541  <MauserHints_AreaB.AfterWerehundDefeat>
CONTROL L3542    if { f(ClassicWerehund_defeated) } {
CONTROL L3543      if { !hasItem(Agent*01) || !hasItem(Agent*02) } {
ROW CAT:O51d8db668a2ed7854037 L3544 Mauser physical_line
  EN: [OUR RECORD OF TRANSMISSIONS FOR THAT AREA SHOWS]
  ZH:       Mauser: [我方通讯记录显示，那处区域附近有两名特工。]
ROW CAT:O90abeddc722b00b8059c L3545 Mauser physical_line
  EN: [THAT THERE WERE TWO AGENTS IN THE VICINITY]
  ZH: 
ROW CAT:O1fe928a9fdddc3034d90 L3546 Mauser physical_line
  EN: [I HOPE THAT THEY'RE OKAY!]
  ZH:       Mauser: [希望他们平安！]
ROW CAT:O76c38d2a2f103b9f1989 L3547 Yiffany physical_line
  EN: [I'LL FIND THEM! YOU CAN COUNT ON ME!]
  ZH:       Yiffany: [我会找到他们的！包在我身上！]
CONTROL L3548      } else {
ROW CAT:O767c5e1bbf092a9eab70 L3549 Mauser physical_line
  EN: [IF ONLY YOU HAD SOME WAY TO DIG THROUGH DIRT]
  ZH:       Mauser: [真要是有办法挖开泥土，也许就能往西走了！]
ROW CAT:O03f0eecda640376ac6be L3550 Mauser physical_line
  EN: [YOU MIGHT BE ABLE TO MAKE YOUR WAY WESTWARD!]
  ZH: 
CONTROL L3551      }
CONTROL L3552    }

## SC8fb6708eb73e3670 | nsfw | datadm/all.ds | MauserHints_AreaB.AfterWerehundDefeat
CONTROL L3604  <MauserHints_AreaB.AfterWerehundDefeat>
CONTROL L3605    if { f(ClassicWerehund_defeated) } {
CONTROL L3606      if { !hasItem(Agent*01) || !hasItem(Agent*02) } {
ROW CAT:O545a0eb5f8c861d80e15 L3607 Mauser physical_line
  EN: [OUR RECORD OF TRANSMISSIONS FOR THAT AREA SHOWS]
  ZH:       Mauser: [我方对那处区域的通讯记录显示，共有两名特工在附近。]
ROW CAT:Of1cbd0e8771344d3f3b6 L3608 Mauser physical_line
  EN: [THAT THERE WERE TWO AGENTS IN THE VICINITY]
  ZH: 
ROW CAT:O38ca28bcff64afb37443 L3609 Mauser physical_line
  EN: [I HOPE THAT THEY'RE OKAY!]
  ZH:       Mauser: [希望他们都没事！]
ROW CAT:O5f880587a33e89499e4a L3610 Yiffai physical_line
  EN: [I'LL FIND THEM! YOU CAN COUNT ON ME!]
  ZH:       Yiffai: [我去找他们！交给我吧！]
CONTROL L3611      } else {
ROW CAT:Oe470f76cad7c19747818 L3612 Mauser physical_line
  EN: [IF ONLY YOU HAD SOME WAY TO DIG THROUGH DIRT]
  ZH:       Mauser: [要是你有办法挖穿泥土，说不定就能一路往西去了！]
ROW CAT:O73e5959a79ba87226dc1 L3613 Mauser physical_line
  EN: [YOU MIGHT BE ABLE TO MAKE YOUR WAY WESTWARD!]
  ZH: 
CONTROL L3614      }
CONTROL L3615    }

## SC65bfc7226dcf8d7d | nsfw | datadm/all.ds | MauserHints_AreaB.AfterWerepupDefeat
CONTROL L3589  <MauserHints_AreaB.AfterWerepupDefeat>
CONTROL L3590    if { f(ClassicWerepup_defeated) } {
ROW CAT:Oc95bd1e399dd8adc59e1 L3591 Mauser physical_line
  EN: [NOW THAT YOU HAVE A HIGHER LEVEL OF KEYCARD]
  ZH:     Mauser: [既然你现在有了更高级别的门卡，应该能往补给站更深处走了！]
ROW CAT:O3ff376a3bf87dd3a7003 L3592 Mauser physical_line
  EN: [YOU SHOULD BE ABLE TO MOVE DEEPER INTO THE DEPOT!]
  ZH: 
CONTROL L3593    }

## SCd2a3cf4d18f14a7d | nsfw | datadf/all.ds | MauserHints_AreaB.AfterWerepupDefeat
CONTROL L3526  <MauserHints_AreaB.AfterWerepupDefeat>
CONTROL L3527    if { f(ClassicWerepup_defeated) } {
ROW CAT:O11899300ea2ff45f192a L3528 Mauser physical_line
  EN: [NOW THAT YOU HAVE A HIGHER LEVEL OF KEYCARD]
  ZH:     Mauser: [既然你现在有了更高级的门卡，应该就能往仓库更深处走了！]
ROW CAT:O145475ee2fb9ca33fd5b L3529 Mauser physical_line
  EN: [YOU SHOULD BE ABLE TO MOVE DEEPER INTO THE DEPOT!]
  ZH: 
CONTROL L3530    }

## SC68434f2afb7359a4 | nsfw | datadm/all.ds | MauserHints_AreaB.ReturnFromAreaA
CONTROL L3617  <MauserHints_AreaB.ReturnFromAreaA>
CONTROL L3618    if { f(ctx_entered_area_AreaA) } {
ROW CAT:O3ce4049eff3982178a7e L3619 Mauser physical_line
  EN: [STILL HANGING AROUND THAT OLD AREA, HUH?]
  ZH:     Mauser: [还在那片旧区域晃悠啊？]
ROW CAT:Od9e9751cf628c0f4bf21 L3620 Mauser physical_line
  EN: [I THOUGHT YOU FIGURED OUT SOME WAY TO]
  ZH:     Mauser: [我还以为你已经想到办法离开那片地带了呢？]
ROW CAT:Oe52fd3f5520cbfa4593a L3621 Mauser physical_line
  EN: [MOVE ON FROM THAT ZONE?]
  ZH: 
CONTROL L3622    }

## SC745aeb8f8f9dc42d | nsfw | datadf/all.ds | MauserHints_AreaB.ReturnFromAreaA
CONTROL L3554  <MauserHints_AreaB.ReturnFromAreaA>
CONTROL L3555    if { f(ctx_entered_area_AreaA) } {
ROW CAT:O35f05a1863f712b0f5ab L3556 Mauser physical_line
  EN: [STILL HANGING AROUND THAT OLD AREA, HUH?]
  ZH:     Mauser: [还在那片旧区域晃悠啊？]
ROW CAT:Ofb45bfbe751df9c94593 L3557 Mauser physical_line
  EN: [I THOUGHT YOU FIGURED OUT SOME WAY TO]
  ZH:     Mauser: [我还以为你已经想到办法离开那片地带了呢？]
ROW CAT:O148cea9aeb28dea56b6e L3558 Mauser physical_line
  EN: [MOVE ON FROM THAT ZONE?]
  ZH: 
CONTROL L3559    }

## SCb9b29c00401737b2 | nsfw | datadf/all.ds | MauserHints_AreaC.AfterFirstEnteredAreaC
CONTROL L3560  <MauserHints_AreaC.AfterFirstEnteredAreaC>
ROW CAT:Od185afa9258b4b6e6a77 L3561 Mauser physical_line
  EN: [THERE ARE MULTIPLE EXITS FROM THAT SECTION OF SCEAFYA]
  ZH:   Mauser: [斯凯菲亚那一段有好几个出口，不过抱歉，得你自己去找！]
ROW CAT:Odafa959f7aaae7e0f5da L3562 Mauser physical_line
  EN: [BUT YOU'LL HAVE TO FIND THEM YOURSELF, SORRY!]
  ZH: 

## SCfde47d76460411f7 | nsfw | datadm/all.ds | MauserHints_AreaC.AfterFirstEnteredAreaC
CONTROL L3623  <MauserHints_AreaC.AfterFirstEnteredAreaC>
ROW CAT:O8f37dbb3515b830bb6a5 L3624 Mauser physical_line
  EN: [THERE ARE MULTIPLE EXITS FROM THAT SECTION OF SCEAFYA]
  ZH:   Mauser: [斯凯菲亚那一段有好几个出口，不过抱歉，得你自己去找！]
ROW CAT:Oeeceeb6f7813c0892e98 L3625 Mauser physical_line
  EN: [BUT YOU'LL HAVE TO FIND THEM YOURSELF, SORRY!]
  ZH: 

## SC1fdcff4e3d3e1844 | nsfw | datadm/all.ds | MauserHints_AreaC.End
CONTROL L3672  <MauserHints_AreaC.End>
CONTROL L3673    if { f(ClassicPigobinV3_defeated) && f(ClassicEnelye_defeated) } {
CONTROL L3674      if { !hasItem(Agent*05) || !hasItem(Agent*06) || !hasItem(Agent*08) } {
ROW CAT:Oce85611f4bca6a157ac2 L3675 Mauser physical_line
  EN: [OUR RECORD OF TRANSMISSIONS FOR THAT AREA SHOWS]
  ZH:       Mauser: [我方通讯记录显示，那处区域附近共有三名特工。]
ROW CAT:Oe1241f76fb5bbc90ee23 L3676 Mauser physical_line
  EN: [THERE WERE A TOTAL OF THREE AGENTS IN THE VICINITY]
  ZH: 
ROW CAT:O374247914a61d7399514 L3677 Mauser physical_line
  EN: [I HOPE THAT THEY'RE OKAY!]
  ZH:       Mauser: [希望他们都没事！]
ROW CAT:Ob3c1f59c63a304df5c2d L3678 Yiffai physical_line
  EN: [I'LL FIND THEM! YOU CAN COUNT ON ME!]
  ZH:       Yiffai: [我去找他们！交给我吧！]
CONTROL L3679      } else {
ROW CAT:O959da3455db34db01d3e L3680 Mauser physical_line
  EN: [GEE, I WONDER IF THERE'S ANYTHING NEW]
  ZH:       Mauser: [哎呀，不知道泽罗尼亚那边有没有新东西……]
ROW CAT:O5b435942c84ae3f15010 L3681 Mauser physical_line
  EN: [BACK IN ZERONIA...]
  ZH: 
CONTROL L3682      }
CONTROL L3683    }

## SC3f9f071617094d38 | nsfw | datadf/all.ds | MauserHints_AreaC.End
CONTROL L3610  <MauserHints_AreaC.End>
CONTROL L3611    if { f(ClassicPigobinV3_defeated) && f(ClassicEnelye_defeated) } {
CONTROL L3612      if { !hasItem(Agent*05) || !hasItem(Agent*06) || !hasItem(Agent*08) } {
ROW CAT:Of648a95afaa0ac7d66fe L3613 Mauser physical_line
  EN: [OUR RECORD OF TRANSMISSIONS FOR THAT AREA SHOWS]
  ZH:       Mauser: [我方通讯记录显示，那处区域附近一共有三名特工。]
ROW CAT:O5dbdf14f1cf075fdd3af L3614 Mauser physical_line
  EN: [THERE WERE A TOTAL OF THREE AGENTS IN THE VICINITY]
  ZH: 
ROW CAT:O42cea62a380c6d2c2bcc L3615 Mauser physical_line
  EN: [I HOPE THAT THEY'RE OKAY!]
  ZH:       Mauser: [希望他们平安！]
ROW CAT:Oeb79c3b8e9e8661b1d56 L3616 Yiffany physical_line
  EN: [I'LL FIND THEM! YOU CAN COUNT ON ME!]
  ZH:       Yiffany: [我会找到他们的！包在我身上！]
CONTROL L3617      } else {
ROW CAT:O79291bfc722e8596d278 L3618 Mauser physical_line
  EN: [GEE, I WONDER IF THERE'S ANYTHING NEW]
  ZH:       Mauser: [哎呀，不知道泽罗尼亚那边有没有什么新东西……]
ROW CAT:Ocb032b7965142540aaf5 L3619 Mauser physical_line
  EN: [BACK IN ZERONIA...]
  ZH: 
CONTROL L3620      }
CONTROL L3621    }

## SC2d557c5f86ef9923 | nsfw | datadf/all.ds | MauserHints_AreaC.EnelyeHint noselect
CONTROL L3577  <MauserHints_AreaC.EnelyeHint noselect>
ROW CAT:Oa25783c6c24481283640 L3578 Mauser physical_line
  EN: [THERE'S A LOT OF HIGH LEVEL DOORS AROUND THERE]
  ZH:   Mauser: [那附近有不少高等级门，肯定也有张高等级门卡藏在某处！]
ROW CAT:O04cab93fd9753c78b983 L3579 Mauser physical_line
  EN: [WHICH MUST MEAN THERE'S A HIGH LEVEL KEYCARD SOMEWHERE!]
  ZH: 
ROW CAT:O526c59a28f5a2c36e766 L3580 Mauser physical_line
  EN: [YOUR BEST BET IS TO FIND THAT AND SEE WHERE IT'LL TAKE YA]
  ZH:   Mauser: [最好的办法就是先找到它，看看能通往哪些地方。]

## SCae10fcc52e96b81c | nsfw | datadm/all.ds | MauserHints_AreaC.EnelyeHint noselect
CONTROL L3640  <MauserHints_AreaC.EnelyeHint noselect>
ROW CAT:Ocab1b8cea53383771fb3 L3641 Mauser physical_line
  EN: [THERE'S A LOT OF HIGH LEVEL DOORS AROUND THERE]
  ZH:   Mauser: [那附近有好多高等级的门，那肯定说明哪儿有一张高级门卡！]
ROW CAT:O6226dcf6a6483bc5e09d L3642 Mauser physical_line
  EN: [WHICH MUST MEAN THERE'S A HIGH LEVEL KEYCARD SOMEWHERE!]
  ZH: 
ROW CAT:O6b8e9edfa47ecb0913ab L3643 Mauser physical_line
  EN: [YOUR BEST BET IS TO FIND THAT AND SEE WHERE IT'LL TAKE YA]
  ZH:   Mauser: [最靠谱就是找到它，看它能带你去哪儿]

## SC0e0edfdfdc16fe62 | nsfw | datadf/all.ds | MauserHints_AreaC.OpenMode
CONTROL L3564  <MauserHints_AreaC.OpenMode>
CONTROL L3565    if { hasItem(SpecialHookshot) } {
CONTROL L3566      if { hasItem(SpecialKeycard3) } {
CONTROL L3567        include { MauserHints_AreaC.EnelyeHint }
CONTROL L3568      } else if { hasItem(SpecialTorch) } {
CONTROL L3569        include { MauserHints_AreaC.PigobinHint }
CONTROL L3570      } else {
ROW CAT:Oaceac2454b8471ac7d93 L3571 Mauser physical_line
  EN: [WITH ALL THAT GEAR YOU HAVE NOW]
  ZH:       Mauser: [以你现在这些装备，基本上哪儿都能去了吧？]
ROW CAT:O2993ced0ab62c575e850 L3572 Mauser physical_line
  EN: [YOU CAN GET BASICALLY ANYWHERE, HUH?]
  ZH: 
ROW CAT:O4d5fa3e6980ddf738b6f L3573 Mauser physical_line
  EN: [MAKE SURE TO CHECK YOUR NAVMAP FOR NEW PLACES TO GO!]
  ZH:       Mauser: [记得查看导航图，找找新的可去之处！]
CONTROL L3574      }
CONTROL L3575    }

## SC87179380694e608e | nsfw | datadm/all.ds | MauserHints_AreaC.OpenMode
CONTROL L3627  <MauserHints_AreaC.OpenMode>
CONTROL L3628    if { hasItem(SpecialHookshot) } {
CONTROL L3629      if { hasItem(SpecialKeycard3) } {
CONTROL L3630        include { MauserHints_AreaC.EnelyeHint }
CONTROL L3631      } else if { hasItem(SpecialTorch) } {
CONTROL L3632        include { MauserHints_AreaC.PigobinHint }
CONTROL L3633      } else {
ROW CAT:O2c11e72d956a328bf8ad L3634 Mauser physical_line
  EN: [WITH ALL THAT GEAR YOU HAVE NOW]
  ZH:       Mauser: [有了你现在这些装备，基本哪儿都能去了吧？]
ROW CAT:O896ef7703a5740ad6c95 L3635 Mauser physical_line
  EN: [YOU CAN GET BASICALLY ANYWHERE, HUH?]
  ZH: 
ROW CAT:O0c354543d06f72ef4507 L3636 Mauser physical_line
  EN: [MAKE SURE TO CHECK YOUR NAVMAP FOR NEW PLACES TO GO!]
  ZH:       Mauser: [记得查看导航地图，找找新去处！]
CONTROL L3637      }
CONTROL L3638    }

## SC747ef12f51e290c1 | nsfw | datadf/all.ds | MauserHints_AreaC.ReturnLater
CONTROL L3623  <MauserHints_AreaC.ReturnLater>
CONTROL L3624    if { hasItem(CosmoHead) || hasItem(CosmoBody) || f(ClassicStarkillV3_defeated) } {
ROW CAT:Oa49014b9f4a02a3d1003 L3625 Mauser physical_line
  EN: [GEE YIFFANY, WHAT'S GOING ON BACK IN THAT AREA?]
  ZH:     Mauser: [哎呀，伊吠妮，那片区域那边怎么了？]
ROW CAT:O64b847986647efd6df8f L3626 Mauser physical_line
  EN: [AREN'T THERE MORE INTERESTING PLACES THAT YOU COULD SEE]
  ZH:     Mauser: [通过传送门去别的区域探索，不是还能看到更有意思的地方吗？]
ROW CAT:Oeb958bca312a681cc736 L3627 Mauser physical_line
  EN: [IF YOU TAKE A TELE- PORTAL TO EXPLORE OTHER AREAS?]
  ZH: 
CONTROL L3628    }

## SC867009a1a6bdb6ec | nsfw | datadm/all.ds | MauserHints_AreaC.ReturnLater
CONTROL L3685  <MauserHints_AreaC.ReturnLater>
CONTROL L3686    if { hasItem(CosmoHead) || hasItem(CosmoBody) || f(ClassicStarkillV3_defeated) } {
ROW CAT:Odb581a9e222b75422fe8 L3687 Mauser physical_line
  EN: [GEE YIFFAI, WHATCHU YOU DOING BACK IN THAT OLD PLACE?]
  ZH:     Mauser: [哎呀伊吠，你跑回这老地方干嘛呀？]
ROW CAT:O203ac3bc328cdef135f8 L3688 Mauser physical_line
  EN: [THERE'S OTHER THINGS TO DO IF YOU USE THE TELEPORTAL]
  ZH:     Mauser: [要是用传送门去探索别的区域，还有别的事情可做！]
ROW CAT:O03e93365e897d29cc912 L3689 Mauser physical_line
  EN: [AND EXPLORE OTHER AREAS!]
  ZH: 
CONTROL L3690    }

## SC471820d1e214f97c | nsfw | datadm/all.ds | MauserHints_AreaE.AfterFirstEnteredAreaE
CONTROL L3691  <MauserHints_AreaE.AfterFirstEnteredAreaE>
ROW CAT:O91949fb526d7540c7f68 L3692 Mauser physical_line
  EN: [I'M DETECTING STRONG ENERGY SIGNATURES DEEP IN]
  ZH:   Mauser: [我在那颗卫星东北部的深处探测到强烈能量特征，伊吠。]
ROW CAT:Oa38ae9e212424952cd57 L3693 Mauser physical_line
  EN: [THE NORTHEAST OF THAT MOON, YIFFAI.]
  ZH: 
ROW CAT:Oc6318d9ff0e2ee0653b5 L3694 Mauser physical_line
  EN: [YOU SHOULD TRY TO FIND A WAY INTO THOSE CAVERNS.]
  ZH:   Mauser: [你该试着找条路进那些洞窟。]

## SCedea7267588eb179 | nsfw | datadf/all.ds | MauserHints_AreaE.AfterFirstEnteredAreaE
CONTROL L3629  <MauserHints_AreaE.AfterFirstEnteredAreaE>
ROW CAT:Oba807d87d2fe06bb2d62 L3630 Mauser physical_line
  EN: [I'M DETECTING STRONG ENERGY SIGNATURES DEEP IN]
  ZH:   Mauser: [伊吠，我探测到那颗卫星东北部深处有强烈能量特征。]
ROW CAT:O1eb7be28c9af1ea5a413 L3631 Mauser physical_line
  EN: [THE NORTHEAST OF THAT MOON, YIFFAI.]
  ZH: 
ROW CAT:O08930ec8da72de4de1ca L3632 Mauser physical_line
  EN: [YOU SHOULD TRY TO FIND A WAY INTO THOSE CAVERNS.]
  ZH:   Mauser: [你该试着找条路进那些洞窟。]

## SC6fdb8418c5faf950 | sfw | datadf/all.ds | MauserHints_AreaE.AfterFirstEnteredAreaE
CONTROL L3580  <MauserHints_AreaE.AfterFirstEnteredAreaE>
ROW SFW5fcadca254065f81d358d161 L3581 - physical_line
  EN: [I'M DETECTING STRONG ENERGY SIGNATURES DEEP IN]
  ZH:   Mauser: [伊吠妮，我探测到了很强的能量信号。]
ROW SFWd40939bcf1fb5974ce06ba38 L3582 - physical_line
  EN: [THE NORTHEAST OF THAT MOON, YIFFANY.]
  ZH:   Mauser: [就在那颗卫星的东北部深处。]
ROW SFW744c27461afee6102905e239 L3583 - physical_line
  EN: [YOU SHOULD TRY TO FIND A WAY INTO THOSE CAVERNS.]
  ZH:   Mauser: [你该试着找条路进那些洞窟。]

## SC9c3ee111c4458d24 | nsfw | datadm/all.ds | MauserHints_AreaE.AfterOpenedLock
CONTROL L3705  <MauserHints_AreaE.AfterOpenedLock>
CONTROL L3706    if { f(AreaE_map23_door_key) } {
ROW CAT:O710a25afe652ec70566a L3707 Mauser physical_line
  EN: [WE'VE DETECTED POWERFUL SURGES OF DARK ENERGY DEEPER]
  ZH:     Mauser: [我们探测到，你打开的那个金库更深处有强烈的暗能量涌动。]
ROW CAT:O656c774b16cbd7aefb42 L3708 Mauser physical_line
  EN: [WITHIN THAT VAULT YOU UNLOCKED.]
  ZH: 
ROW CAT:O8121e2a94476733e4f99 L3709 Mauser physical_line
  EN: [BEFORE YOU GO IN THERE, MAKE SURE YOU'RE READY.]
  ZH:     Mauser: [进去之前，确保你已经准备好了。]
CONTROL L3710    }

## SCb83c11a1adaf52ec | nsfw | datadf/all.ds | MauserHints_AreaE.AfterOpenedLock
CONTROL L3643  <MauserHints_AreaE.AfterOpenedLock>
CONTROL L3644    if { f(AreaE_map23_door_key) } {
ROW CAT:Oc430b6793288363249c2 L3645 Mauser physical_line
  EN: [WE'VE DETECTED POWERFUL SURGES OF DARK ENERGY DEEPER]
  ZH:     Mauser: [我们在你打开的那座宝库更深处探测到强烈的暗能量涌动。]
ROW CAT:O3f964ac9eb0a49d62467 L3646 Mauser physical_line
  EN: [WITHIN THAT VAULT YOU UNLOCKED.]
  ZH: 
ROW CAT:Odf8998cd41f4dd388581 L3647 Mauser physical_line
  EN: [BEFORE YOU GO IN THERE, MAKE SURE YOU'RE READY.]
  ZH:     Mauser: [进去之前，务必做好准备。]
CONTROL L3648    }

## SC73e818ac21de50e7 | nsfw | datadm/all.ds | MauserHints_AreaE.AfterSeenLock
CONTROL L3696  <MauserHints_AreaE.AfterSeenLock>
CONTROL L3697    if { f(ctx_entered_room_AreaE_map23) } {
ROW CAT:O2b6a8d1ace2b71a5b10a L3698 Mauser physical_line
  EN: [THAT VAULT YOU FOUND IN THE NORTHEAST OF EXILE]
  ZH:     Mauser: [你在流放地东北边发现的那个金库，看来真的很重要。]
ROW CAT:Oa215ecef27c4953b1a5c L3699 Mauser physical_line
  EN: [SEEMS REALLY IMPORTANT.]
  ZH: 
ROW CAT:O8c32aa58ae8432cb6885 L3700 Yiffai physical_line
  EN: [ANY IDEA HOW I COULD OPEN IT?]
  ZH:     Yiffai: [有什么办法能打开它吗？]
ROW CAT:Odc1636b64ef44fd01bf2 L3701 Mauser physical_line
  EN: [IT SEEMS TO BE FENFEN TECH. SO IF YOU RUN INTO ANY]
  ZH:     Mauser: [看起来是Fenfen的技术。所以你要是碰上他们中的任何一个，也许该留意他们对你说的话？]
ROW CAT:O9383481eabba4a410fe0 L3702 Mauser physical_line
  EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
  ZH: 
CONTROL L3703    }

## SCa1e42fd2a89cb4a7 | nsfw | datadf/all.ds | MauserHints_AreaE.AfterSeenLock
CONTROL L3634  <MauserHints_AreaE.AfterSeenLock>
CONTROL L3635    if { f(ctx_entered_room_AreaE_map23) } {
ROW CAT:Oda168f4d2a5a7f7785d1 L3636 Mauser physical_line
  EN: [THAT VAULT YOU FOUND IN THE NORTHEAST OF EXILE]
  ZH:     Mauser: [你在流放东北发现的那座宝库，看起来确实很重要。]
ROW CAT:Ocdbdf9e283658ee3a4e2 L3637 Mauser physical_line
  EN: [SEEMS REALLY IMPORTANT.]
  ZH: 
ROW CAT:O2d115ca64d6b31fc781a L3638 Yiffany physical_line
  EN: [ANY IDEA HOW I COULD OPEN IT?]
  ZH:     Yiffany: [有什么办法能让我打开它吗？]
ROW CAT:O0b1cbd97cc7bf76b0568 L3639 Mauser physical_line
  EN: [IT SEEMS TO BE FENFEN TECH. SO IF YOU RUN INTO ANY]
  ZH:     Mauser: [看起来是Fenfen的技术。所以你要是碰上他们，也许该留意他们对你说的话？]
ROW CAT:Of0c902fc1440402f7fc0 L3640 Mauser physical_line
  EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
  ZH: 
CONTROL L3641    }

## SC6fc409e41e2a9bb6 | sfw | datadf/all.ds | MauserHints_AreaE.AfterSeenLock
CONTROL L3585  <MauserHints_AreaE.AfterSeenLock>
CONTROL L3586    if { f(ctx_entered_room_AreaE_map23) } {
ROW SFW724b2e902a7a29aaef76970b L3587 - physical_line
  EN: [THAT VAULT YOU FOUND IN THE NORTHEAST OF EXILE]
  ZH:     Mauser: [你在流放地东北发现的那座宝库，看起来确实很重要。]
ROW SFW03ec05bbb13c782704fa8edf L3588 - physical_line
  EN: [SEEMS REALLY IMPORTANT.]
  ZH: 
ROW SFW2f93c3e2b2d9dba9e86a65ef L3589 - physical_line
  EN: [ANY IDEA HOW I COULD OPEN IT?]
  ZH:     Yiffany: [有什么办法能让我打开它吗？]
ROW SFW9f1b0263bb7236695b225e44 L3590 - physical_line
  EN: [IT SEEMS TO BE FENFEN TECH. SO IF YOU RUN INTO ANY]
  ZH:     Mauser: [看起来是Fenfen的技术。所以你要是碰上他们，也许该留意他们对你说的话？]
ROW SFWe5ac5e75cd9488f638847440 L3591 - physical_line
  EN: [MAYBE YOU SHOULD PAY ATTENTION TO WHAT THEY TELL YOU?]
  ZH: 
CONTROL L3592    }

## SC096ff031233354a6 | nsfw | datadm/all.ds | MauserHints_AreaH.Stub
CONTROL L3711  <MauserHints_AreaH.Stub>
ROW CAT:O00e8cfa7e0711016d8e3 L3712 Mauser physical_line
  EN: [IT LOOKS LIKE YOU'RE IN THE HANGAR, YIFFAI.]
  ZH:   Mauser: [看样子你到机库里了，伊吠。]
ROW CAT:O0680646e1e7533d8f43b L3713 Mauser physical_line
  EN: [YOU CAN REST AND RECOVER THERE WHILE YOU PLAN]
  ZH:   Mauser: [你可以在那儿休息恢复，顺便规划你的下一步行动！]
ROW CAT:O31ce13876abc1ae46df7 L3714 Mauser physical_line
  EN: [YOUR NEXT MOVE!]
  ZH: 

## SCff4ab55d36c06867 | nsfw | datadf/all.ds | MauserHints_AreaH.Stub
CONTROL L3649  <MauserHints_AreaH.Stub>
ROW CAT:Oa9351a5fa29986e6d64e L3650 Mauser physical_line
  EN: [IT LOOKS LIKE YOU'RE IN THE HANGAR, YIFFANY.]
  ZH:   Mauser: [看起来你在机库里，伊吠妮。]
ROW CAT:O0b28fcfdf84050eb24bd L3651 Mauser physical_line
  EN: [YOU CAN REST AND RECOVER THERE WHILE YOU PLAN]
  ZH:   Mauser: [你可以在那儿休息恢复，一边计划下一步行动！]
ROW CAT:O073c7aafa7f224ba09d2 L3652 Mauser physical_line
  EN: [YOUR NEXT MOVE!]
  ZH: 

