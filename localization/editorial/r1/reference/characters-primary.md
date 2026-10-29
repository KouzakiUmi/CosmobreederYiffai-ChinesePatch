# Mauser / Yiffai / Yiffany：首轮角色参照

**reference draft，未 approved；仅建参照，不交正式精修译文。**

## 覆盖与证据口径
旧lore仅作检索线索；收录evidence均通过units、occurrences、resources定位并核对真实blob载荷。人工读取原speaker JSONL：Mauser 1–187、Yiffai 1–190、Yiffany 1–187（以实际返回行而非请求limit计）；随后读取不含prev/next的精简全文视图：Mauser 188–287、288–387、388–487、488–587、588–633；Yiffai 191–290、291–390、391–490、491–540；Yiffany 188–287、288–387、388–487、488–570，每段实际完整返回。至此三人speaker的全部source已读（共1743条），但不等于所有对应完整场景/控制上下文都已审完。另读取全部115条初选证据的源上下文及关键场景、学历原文；新增细节仍按证据与作用域判断。

speaker总量：Mauser 633、Yiffai 540、Yiffany 570；本库收录202条载荷关联证据。**未人工核完整全文。**
三人speaker全部source已读；尚未逐场景审完与其相关的其他说话人/旁白/控制上下文，未核所有变身分支运行时触发代码，也未核完整游戏全文或SFW对照。candidate4仅抽样通讯、称姓、哨子段，不做全量质量结论。

源头：[units](<localization/catalog/units.jsonl>) → [occurrences](<localization/catalog/occurrences.jsonl>) → [resources](<localization/catalog/resources.jsonl>) → source blob；[旧角色线索](<localization/work/lore/characters-Mauser-Yiffai-Yiffany.json>)不作全文凭据。

WoC只借执行方式，不搬文风、禁词、术语。重写单位为完整对话意图和整段中文节奏，不逐框逐句对译。

## 事实等级与分支红线
- 已确认：姐姐Yiffany/弟弟Yiffai；Yiffai同时为姐姐姓氏与弟弟名字；全名呼叫不拆人。
- 角色说辞：学历/履历/专业自信、回忆与荤话仍标“本人说/同事说”；性格归纳不写成旁白。
- 推测禁区：同事→情侣/师徒、暧昧→稳定恋爱、昵称→未成年、岗位→军衔，均不能升级。
catalog female→datadf，常态发言者Yiffany；male→datadm，常态发言者Yiffai。raw_variant_semantics_unverified不能替代运行时触发验证。
GenderSwapped中总部相互误认另一主角，speaker仍是当前主角；误认不是身份互换。Feral/Slime仅该形态说BARK/GLOOP，不扩成常态口癖。Kobo的undercover是角色说辞，不自动认证真实潜伏任务。
按entry/触发条件管理，不以DS文件排列当游玩顺序。AreaC来电先知姓氏/疑似声音；AreaC_map64_b角色确认亲人身份；Area0_StarkillHint提供定位；SpecialWhistle提到恢复神志/传回哨子。确切触发顺序未运行验证，初期台词不加后知信息。

**源异常待判**：Mauser.Slime对speaker=Yiffany原文也喊YIFFAI；源文本疑点，不擅改speaker、家族关系或断言仅译文错误。 `D977ec3e597ecb67e5909` / `O139baccbe4571e62632d`，位置见证据表。

## Mauser
### 身份
总部联络与数据支援人员；男性鼠类由同事的mouse / he / his称呼支持，不从名字猜测。27.550是其频率。MAIN LIASON是本次行动职责，不据此增设军衔。
### 关系边界
Bossu会纠正其准备工作；Tomcat是装备专家、熟人同事，互损不代表敌意。Yiffany逗他并给他与Tomcat凑对，不能据cute couple/card date写成已交往。对两位外勤的支援是互斥主角分支，不合并为共同历险。
### 说话节奏
先问候、确认或感叹，再跨数框讲清资料与操作；热心而略絮叨。资料兴奋、装束引发的局部结巴与平稳技术说明交替。全大写/方括号不是持续吼叫。
### 自称与称呼
自称I，代表总部用we/our；中文通常“我/我们”。公事称agent或主角姓名/全名；SQUEAKS、CUTIE、LITTLE GUY是别人叫他，不是他的自称。不固定加“鼠鼠”“本鼠”。
### 专业语与玩笑转换
P.A.W.、卫星、导航、坐标、数据传输须讲清；技术能力有边界，装备专业问题会转给Tomcat。研究型话匣子可被打断；装束玩笑后会恢复认真讲布料功能。奶牛场履历属于本人自述，不是旁白认证。
### 不可外推边界
不是永远正确的百科，也不是无能吉祥物。便宜黑市食品的嘴硬只见同段对话，应作局部笑点，不能断言一贯吝啬或战斗怯懦。
### 自然中文整段重写原则
整段重排为“先关切—说明情势—给可执行建议”，保留被催才给答案、欲言又止和同事插话；只在原有触发处留结巴，不将所有解释拆成冷硬提示。
身份锚点：`D376f167a81f62411a33a`；`D9d3430edfa4d0d0bef52`；`D0ffcf6a1a1080ec407d4`；`Df6606140658e223af76c`；`Dc9790a635ada0495d7eb`
### 主要性格（各两条源文证据）
- **关心外勤同伴，遇险先问安危，常以鼓励和可执行建议支援，而非只有冷硬指令。**（编辑归纳）
  - [THE IMPORTANT THING IS THAT YOU'RE OKAY! WHEW!!] — `D105749d8ddc53dbea9a2`
  - [WHY DON'T WE DEAL WITH GETTING YOU TO SAFETY FIRST?] — `D51af9cedc6be62b00521`
  - 限制：限已采样场景，不外推每一句。
- **研究与资料型热情：乐于分享技术、地图和收藏，容易兴奋得讲过程忘了先给答案。**（编辑归纳）
  - [I'VE GOT COMPLETE SETS OF MULTIPLE PLANETARY SYSTEMS-] — `D7ec0fbbcef1e2deb6a25`
  - [YOU SEE, FIRST I NOTED THE AREAS WITHOUT RECEPTION] — `D6811a104dea18dbac485`
  - 限制：限已采样场景，不外推每一句。
- **社交上容易紧张，特别是面对 Yiffany 的装束和调侃；有好感暗示，不等于已确认情侣。**（编辑归纳）
  - [I-I HEARD YOU... THAT IS, YOU FOUND... I MEAN...] — `D44717639d460218d5c59`
  - [N-N-NOT THAT YOU SHOULDN'T! THEY'D LOOK GOOD O-] — `D5e9a21a3d2b66168e36b`
  - [W-WHY WOULD I BE JEALOUS OF A PUPPY???] — `D190a9d4cf642d322a278`
  - 限制：装束与送礼调侃两场景支持局部紧张；仍不等于稳定恋情。。
- **并非永远正确的百科：依赖研究资料，也会漏看任务说明、搞错现场情况。**（编辑归纳）
  - [W-WHAT? BUT MY RESEARCH SAYS...] — `Dbe9a373b5c8e5283e2dd`
  - [Y-YEAH BOSSU?] — `D8a2dbcb4cd79a3bb00a7`
  - 限制：限已采样场景，不外推每一句。
- **也会吐槽、接双关和偷偷想听荤段子，不能简化为毫无欲念的乖巧助手。**（编辑归纳）
  - [COULDN'T HAVE BEEN THAT SMART IF YOUR STUFF WAS STOLEN...] — `D0588ff6a358491d3e3f4`
  - [...NOBODY EVER TELLS ME ALL THEIR DIRTY STORIES...] — `D6d2c7f7d25d98facc658`
  - [MINES IN THEIR MINES, AS A WAY TO SAY "THAT'S MINE!"] — `D44887a0491a7e5e54ed5`
  - 限制：限已采样场景，不外推每一句。
- **偏爱靠补给准备、会贪黑市便宜；被同事戳中后嘴硬。不能外推成战斗无能或一贯吝啬。**（编辑归纳）
  - I SOMETIMES STOCK UP ON FOOD — `De3404ee0edc8d5a132a4`
  - I WOULD'VE STOCKED UP ON FOOD — `Dd5b74aa60469f134a518`
  - BUT IT'S SO CHEAP! — `D18a63f6cf95d8dadc9ff`
  - 限制：补给习惯见两处失败提示；便宜食品仅一场景笑点。。

## Yiffai
### 身份
PPP外勤Cosmobreeder，常态男性犬类；Yiffany的弟弟。全名Yiffai Yiffai由自报支持；同一拼写同时作名字与姓氏，不拆成两名发言者。成绩优异是自述且获Bossu肯定，不据此推定军衔或确切年龄。
### 关系边界
姐姐/弟弟由kid brother与sis交叉确认。Bossu是指挥关系，Tomcat与Mauser是总部支援同事；熟稔称呼不自动成为师徒、亲属或恋人。PUP/KIDDO是逗弄与犬类称呼，不能据此认定未成年。
### 说话节奏
正式报到、应令、复述手册之后容易突然兴奋炫耀；被戳穿或调戏时急辩、停顿、局部重复。年轻气盛不是幼儿腔；会冷笑话，也有欲望与主动兴趣。
### 自称与称呼
通常I→我；得意时可自报全名/ACE STUDENT，但不固定改成“本天才”。对Bossu有sir/understood，对Tomcat/Mauser直呼姓名；不移植姐姐的CUTIE/SQUEAKS套话。
### 专业语与玩笑转换
保留训练用语的认真感；STRATEGIMICAL是滑稽造词，不端成完美战术术语，也不硬造长期口癖。学院、海盗违法与被当幼犬的笑点保留迟一拍的落差。
### 不可外推边界
首个正式任务的说法来自哨子回忆与姐姐分支first field mission；不能扩成此前从未训练或从无能力。对姐姐的对战夹着唤醒目的，不定性为永久敌对。
### 自然中文整段重写原则
整段维持“认真汇报/显摆—同事提醒—急辩—接受建议”的弧线。保留学员式措辞与轻快欢呼，不写成姐姐式熟练撩人，也不因羞怯删去明确欲望。
身份锚点：`D087d6367e5099eaadae5`；`Da734fe57b0fc487344d5`；`D4972562db19421d8902b`；`D162f21e0d797713ceded`
### 主要性格（各两条源文证据）
- **好胜、爱显摆成绩和力量，想被当作能独当一面的优秀探员。**（编辑归纳）
  - [HEHE! TOLD YA I WAS TOP OF MY CLASS!] — `D4972562db19421d8902b`
  - [H-HEY! I JUST DON'T KNOW MY OWN STRENGTH!] — `D38a7b6f632d3d4920fba`
  - 限制：限已采样场景，不外推每一句。
- **服从指挥、熟悉手册，习惯用正式程序证明自己；规章意识有时显得天真。**（编辑归纳）
  - [UNDERSTOOD, BOSSU! I WON'T LET YOU DOWN.] — `D09dce01cbf1bccb85bb0`
  - [BUT TOMCAT, ISN'T A TAZER LIKE THIS... ILLEGAL?!] — `Dd572c9dbbdfe3018ebdf`
  - 限制：限已采样场景，不外推每一句。
- **精力旺盛、先动手再想策略，战斗成功后容易兴奋过头。**（编辑归纳）
  - [WHAT? CAN'T I DESTROY THEM?] — `D3a3ec2aa6d9eeaa0d7ce`
  - [IT WAS NO MATCH FOR ME! I WENT HIYAA, THEN ATAA, AN-] — `De98920ca8f91e60bb6d4`
  - 限制：限已采样场景，不外推每一句。
- **容易害羞和嘴硬，讨厌被当小孩或被说可爱，但不能因此否认他的能力。**（编辑归纳）
  - [GEEZE I KNOW THAT, I AIN'T NO PUP...] — `D2793fac7cef4c23c459c`
  - [HMF! I DO NOT. I LOOK LIKE A COOL PIRATE!] — `D9b4390931b98a23a2ed7`
  - 限制：限已采样场景，不外推每一句。
- **欲望、好奇和逞强并存，并非不懂性事的纯洁白纸；有时坦率得忘了掩饰。**（编辑归纳）
  - [I MEAN, THAT SOUNDS KINDA HOT...] — `D62fd87bbc4d0873ca615`
  - [CAN STILL SEE MY BUTT! THAT'S AWESOME!] — `D78442f08fd1910aade20`
  - 限制：限已采样场景，不外推每一句。
- **重亲情、珍视姐姐的承诺；想证明自己长大，也真心承担救援责任。**（编辑归纳）
  - [I GUESS SHE KEPT HER PROMISE AFTER ALL...] — `Db511e25a924247b94f82`
  - [I'LL FIND THEM! YOU CAN COUNT ON ME!] — `D6eb99d6dc485daf1a20d`
  - 限制：限已采样场景，不外推每一句。

## Yiffany
### 身份
PPP女性犬类外勤Cosmobreeder，Yiffai的姐姐。Yiffai也是她的姓，Yiffany Yiffai是全名。TOP OF MY CLASS与既往field mission是本人说辞；可概括有训练经验，不以自夸证明万能或特定等级。
### 关系边界
与Tomcat共享学院往事、互揭短，但sex club细节被Tomcat否认/辩解，须写为双方说辞而非客观履历。主动逗Mauser，尊重Bossu但能开玩笑；不升级恋人。对弟弟的little snot与唤醒/家传哨子并读，不能写成真正仇恨。
### 说话节奏
爽快短句、反问、截话与拖音反讽；能背完整手册，也能立刻转双关。遇异常会发冷、结巴，不是永不露怯。郑重长句有时故意与Tomcat抬杠，不一律肃穆化。
### 自称与称呼
I通常译“我”，不凭气场固定加“老娘/本小姐/姐姐”。对Mauser可用SQUEAKS/CUTIE/BUDDY/LITTLE GUY，按亲疏与场景变化；对弟弟按已证长幼用“弟弟/名字”，不因brother无长幼写成哥哥。
### 专业语与玩笑转换
任务目标和战术判断保持清楚，再让调情与互损自然转进。THE TEMPERATURE在纠正发情双关，不把本来的气温也色情化。专业不等于擅长电脑，PAWWING笑点承认技术短板。 武器手感可短促认真（SWIFT / SURGICAL / TRUE），不能一律加色情暗示。
### 不可外推边界
救援目标、装备实用性与好胜同时成立，不能只剩黄腔。哨子回收及Starkill被打醒属后段剧透，不塞进初次通讯。 她说脚环纪录“没认真试”，弟弟却回忆她连续两周练习；这是不同角色说辞形成的嘴硬反差，不能只信其中一句。维生素求救段最终揭示为逗Tomcat，不拿开头假中毒认定她莽撞。
### 自然中文整段重写原则
先重建她对谁说、想让谁失措、当前是否急着救人，再按中文整段节奏写。保留主动接梗与干脆纠正，避免每句撒娇、每句爆粗或无端“老娘”化。
身份锚点：`D162f21e0d797713ceded`；`Db5f510c042be72b137fb`；`Deb45e587c2538fe44b60`；`Dbe379922dff98eeb4e47`；`Da8e8650fbd6b56daadc0`；`D5b9dba70fc0d7ae6b8c5`
### 主要性格（各两条源文证据）
- **有经验、行动导向，优先关心救援与实用战术；大胆不等于不看任务说明。**（编辑归纳）
  - [I'M HERE TO RESCUE PEOPLE, NOT HUNT TREASURE] — `Dddd21d0630cc823889b6`
  - [I TRAINED WITH A SIMILAR DEVICE ON A FIELD MISSION.] — `D5b9dba70fc0d7ae6b8c5`
  - 限制：限已采样场景，不外推每一句。
- **外向爱逗人，熟练掌握调情、反讽与抢先接梗，尤其爱让总部同事招架不住。**（编辑归纳）
  - [ROGER THAT CUTIE, I'LL BE IN TOUCH!] — `D064674808072ec6c4008`
  - [MADE YA SMIRK! YIFFANY OUT.] — `Dbad1d892b65e445d5d78`
  - 限制：限已采样场景，不外推每一句。
- **对欲望和亲密兴趣较坦然，往往主动把话题带歪，而不是一被开黄腔就羞怯。**（编辑归纳）
  - [HEY, A LITTLE PUPPY PLAY NEVER HURT ANYONE, RIGHT?] — `D77075fd3d25a8e9936bc`
  - [I'LL LICK AND NIBBLE IT GENTLY JUST FOR YOU, TOO!] — `Db9c81657bf209f033d72`
  - 限制：限已采样场景，不外推每一句。
- **在弟弟出事时急切而护短；表面骂得凶，也珍视亲情和家庭传承。**（编辑归纳）
  - [LIKE WHAT THE HELL HAPPENED TO MY KID BROTHER?] — `D162f21e0d797713ceded`
  - [I PASSED IT ON TO YIFFAI FOR HIS FIRST FIELD MISSION...] — `D1fbce41541c5471fba9f`
  - 限制：限已采样场景，不外推每一句。
- **好胜爱面子，喜欢保持很酷、很专业的形象，被戳穿短处会嘴硬。**（编辑归纳）
  - [COME ON, I'M A PRO! I CAN HANDLE THEM!] — `D12c7ea906e3d950c7a4f`
  - [GRR. NOT LIKE I TRIED VERY HARD OR ANYTHING...] — `D293a90c96cf8bc008ad8`
  - [WE WENT THERE EVERY DAY FOR TWO WEEKS! SHE WAS DEDICATED!] — `Dbf906e0d90ea0b16c930`
  - 限制：弟弟分支回忆两周练习与姐姐“没认真试”构成对照；仍标双方说辞，不合并当前任务经历。。
- **专业有明确边界：不是万能技术专家，也会怕诡异事物；需要时能承认不知道、向总部求助。**（编辑归纳）
  - [THERE'S ONLY ONE TYPE OF PAWWING I'M GOOD AT,] — `De303c41cf5764d629a0e`
  - [OKAY, SURE, BUT THESE SPIDERBOTS ARE STILL CREEPY!] — `D44c6de2b94b8e4bd07c8`
  - 限制：限已采样场景，不外推每一句。

## candidate4只读抽查（非全量口吻结论）
只读解码candidate4 patch.pak内datadf/1、datadm/1；candidate行号指解码后的完整DS，段落合并保留空行，不用行号直接强配所有unit。
原包：[candidate4 patch.pak](<localization/builds/r28-radio-book-candidate4/patch.pak>)；SHA-256 `149768acbbc4b0a37c017baba63083cc0ab5056e808380915cb24468f4bbcccd`。
- **datadm Bossu.Area0_map10_a**，解码DS行 2011,2019：H-HEY写成“嘿-嘿”易听成笑声；Pup残留英文使被当幼犬后的急辩失去落点。不是正式精修稿。
  - 当前译文：[嘿-嘿！我就是不知道自己的力气有多大！] / [哎呀我知道，我才不是Pup...]
  - 源ID：`D38a7b6f632d3d4920fba`；`D2793fac7cef4c23c459c`
- **datadf Mauser.AreaC_map65_a**，解码DS行 2478,2483,2498：结巴与姐姐抢先逗人仍在，不能宣称角色口吻已全面抹平；cute couple只作玩笑，不升级关系。
  - 当前译文：[我、我听说你……就是说，你找到了……我是说……] / [哎呀，多可爱的一对。玩得开心！]
  - 源ID：`D44717639d460218d5c59`；`D5e9a21a3d2b66168e36b`
- **datadm/datadf Starkill.AreaC_map04_a**，解码DS行 2524,2505：name/surname分支差别保留，应继续保护，不因同名统一合并。
  - 当前译文：[等等……你知道我的名字？你是谁？？] / [等等……你知道我的姓？你是谁？？]
  - 源ID：`Dc5631fdfa2754ea960b8`；`Deb45e587c2538fe44b60`
- **datadm/datadf TomcatItems.SpecialWhistle**，解码DS行 4417,4418,4410：亲情回忆与长幼在此抽样保留，不等于全篇关系无误。
  - 当前译文：[她说等我第一次正式出任务，就让我拿着。] / [看来她还真守了诺言……] / [伊法伊第一次出外勤时，我把它传给了他……]
  - 源ID：`De07de0de34e1ef44a0ae`；`Db511e25a924247b94f82`；`D1fbce41541c5471fba9f`

## 证据定位表
短链指向真实source blob行；unit/occurrence与目录行号、speaker位置、前后句和原始行完整保存在[机器可读证据库](<localization/editorial/r1/reference/characters-primary.json>)。重复原文在不同分支有不同ID，不合并经历。

|角色 / unit ID|英文原文|speaker位置|全部occurrence及源位置|
|---|---|---|---|
|Mauser / `D105749d8ddc53dbea9a2`|[THE IMPORTANT THING IS THAT YOU'RE OKAY! WHEW!!]|[speaker:20](<localization/work/lore/speaker-Mauser.jsonl#L20>)|`Ofbf3f085bc11d7adaeb6` [datadf/all.ds#L2032](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2032>)|
|Mauser / `D7ec0fbbcef1e2deb6a25`|[I'VE GOT COMPLETE SETS OF MULTIPLE PLANETARY SYSTEMS-]|[speaker:43](<localization/work/lore/speaker-Mauser.jsonl#L43>)|`O8163db088c8c2df5cff6` [datadf/all.ds#L2101](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2101>)|
|Mauser / `D6811a104dea18dbac485`|[YOU SEE, FIRST I NOTED THE AREAS WITHOUT RECEPTION]|[speaker:47](<localization/work/lore/speaker-Mauser.jsonl#L47>)|`O104053f01d0648f06cbe` [datadf/all.ds#L2114](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2114>)|
|Mauser / `Dbe9a373b5c8e5283e2dd`|[W-WHAT? BUT MY RESEARCH SAYS...]|[speaker:103](<localization/work/lore/speaker-Mauser.jsonl#L103>)|`O33729688ce4ddcf7c35b` [datadf/all.ds#L2393](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2393>)|
|Mauser / `D8a2dbcb4cd79a3bb00a7`|[Y-YEAH BOSSU?]|[speaker:105](<localization/work/lore/speaker-Mauser.jsonl#L105>)|`O9b1f6e3154e710f59f9f` [datadf/all.ds#L2403](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2403>)|
|Mauser / `Dbe379922dff98eeb4e47`|[AGENT YIFFANY YIFFAI, COME IN.]|[speaker:106](<localization/work/lore/speaker-Mauser.jsonl#L106>)|`O899141955aefe1d24c63` [datadf/all.ds#L2408](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2408>)|
|Mauser / `D51af9cedc6be62b00521`|[WHY DON'T WE DEAL WITH GETTING YOU TO SAFETY FIRST?]|[speaker:112](<localization/work/lore/speaker-Mauser.jsonl#L112>)|`Od1667a4c0149304c94fb` [datadf/all.ds#L2453](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2453>)|
|Mauser / `D44717639d460218d5c59`|[I-I HEARD YOU... THAT IS, YOU FOUND... I MEAN...]|[speaker:114](<localization/work/lore/speaker-Mauser.jsonl#L114>)|`O65bd6ed637352f08cae8` [datadf/all.ds#L2478](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2478>)|
|Mauser / `D5e9a21a3d2b66168e36b`|[N-N-NOT THAT YOU SHOULDN'T! THEY'D LOOK GOOD O-]|[speaker:116](<localization/work/lore/speaker-Mauser.jsonl#L116>)|`O4b20c65773d6989892bc` [datadf/all.ds#L2483](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2483>)|
|Mauser / `D5ddb3549cbbb6be422ff`|[H-HUH? WHO'S THIS? YIFFANY?!]|[speaker:141](<localization/work/lore/speaker-Mauser.jsonl#L141>)|`O131dba376daf2d252e6f` [datadf/all.ds#L3332](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3332>)|
|Mauser / `Df913664def64bd911401`|[UM... THIS CHANNEL IS FOR AUTHORIZED COSMOBREEDERS ONLY.]|[speaker:142](<localization/work/lore/speaker-Mauser.jsonl#L142>)|`O14eedb6b34160a6641a6` [datadf/all.ds#L3334](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3334>)；`Ode619721e1496d1af8af` [datadf/all.ds#L3346](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3346>)|
|Mauser / `D91e6eb650f9dd5131cd9`|[I'LL HAVE TO DISCONNECT, 'MAM'. OVER.]|[speaker:143](<localization/work/lore/speaker-Mauser.jsonl#L143>)|`O15319bdbf837b2fe4a72` [datadf/all.ds#L3335](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3335>)；`O7ed3d1b243d0ec83fdf1` [datadf/all.ds#L3347](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3347>)|
|Mauser / `D8f3059dde90b88861317`|[HUH? THIS ISN'T FUNNY!]|[speaker:144](<localization/work/lore/speaker-Mauser.jsonl#L144>)|`O98990272ac49151311e7` [datadf/all.ds#L3338](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3338>)；`Oa96397389ef512a4e07f` [datadf/all.ds#L3350](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3350>)|
|Mauser / `Dedae24e581d8a3dedfa6`|[TELL YOUR MASTER TO CALL ME BACK!]|[speaker:145](<localization/work/lore/speaker-Mauser.jsonl#L145>)|`Oef366f513269eabf1f01` [datadf/all.ds#L3340](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3340>)|
|Mauser / `D977ec3e597ecb67e5909`|[H-HUH? WHO'S THIS? YIFFAI?!]|[speaker:146](<localization/work/lore/speaker-Mauser.jsonl#L146>)|`O139baccbe4571e62632d` [datadf/all.ds#L3344](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3344>)|
|Mauser / `De5e7b4dbb845daa01089`|[... I'LL JUST CALL BACK LATER...]|[speaker:147](<localization/work/lore/speaker-Mauser.jsonl#L147>)|`Ob8742a390e1c68865c5d` [datadf/all.ds#L3352](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3352>)|
|Mauser / `D5721c89ba8dc2e424e3e`|HUH?! AGENT... YIFFAI?|[speaker:152](<localization/work/lore/speaker-Mauser.jsonl#L152>)|`Oebd056a24430c045a800` [datadf/all.ds#L3368](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3368>)；`O96afca4eeda27c0d2fcd` [datadf/all.ds#L3372](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3372>)|
|Mauser / `D5d44b4cda85e74ab37ac`|[I USED TO WORK AT A DAIRY FARM, AND THAT IS NOOOT MILK.]|[speaker:256](<localization/work/lore/speaker-Mauser.jsonl#L256>)|`Ob1620521dd7d2d6a5b5e` [datadf/all.ds#L3995](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3995>)|
|Mauser / `D18a63f6cf95d8dadc9ff`|BUT IT'S SO CHEAP!|[speaker:290](<localization/work/lore/speaker-Mauser.jsonl#L290>)|`Obf07c934b6302cc8ec1e` [datadf/all.ds#L4845](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4845>)|
|Mauser / `D19242f41b4fdaa12e16e`|...NOT EVERY TIME...|[speaker:291](<localization/work/lore/speaker-Mauser.jsonl#L291>)|`O267219933f47e5f8aad1` [datadf/all.ds#L4847](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4847>)|
|Mauser / `D0588ff6a358491d3e3f4`|[COULDN'T HAVE BEEN THAT SMART IF YOUR STUFF WAS STOLEN...]|[speaker:318](<localization/work/lore/speaker-Mauser.jsonl#L318>)|`O03224b2f5d12a85adf6a` [datadm/all.ds#L1968](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1968>)|
|Mauser / `D376f167a81f62411a33a`|[BUT NO MATTER! I'M YOUR MAIN LIASON FOR THIS SORTIE]|[speaker:319](<localization/work/lore/speaker-Mauser.jsonl#L319>)|`O2e9427e1ca032962fa33` [datadm/all.ds#L1969](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1969>)|
|Mauser / `D566c57b2c491cda9dee0`|[YOU SEE, FIRST I NOTED THE AREAS WITHOUT RECEPTION]|[speaker:358](<localization/work/lore/speaker-Mauser.jsonl#L358>)|`O6ff670cf9af769243b1c` [datadm/all.ds#L2116](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2116>)|
|Mauser / `D6d2c7f7d25d98facc658`|[...NOBODY EVER TELLS ME ALL THEIR DIRTY STORIES...]|[speaker:401](<localization/work/lore/speaker-Mauser.jsonl#L401>)|`O91adc776171b3ec65f46` [datadm/all.ds#L2334](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2334>)|
|Mauser / `D5df750f66d0fc4ee1898`|[W-WHAT? BUT MY RESEARCH SAYS...]|[speaker:413](<localization/work/lore/speaker-Mauser.jsonl#L413>)|`O795058d0773b6522536d` [datadm/all.ds#L2402](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2402>)|
|Mauser / `Df72f4617a55baabe8fbe`|[Y-YEAH BOSSU?]|[speaker:415](<localization/work/lore/speaker-Mauser.jsonl#L415>)|`Oceffdec89b28559243fe` [datadm/all.ds#L2412](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2412>)|
|Mauser / `D322ca199430c4c1fbafb`|[WHY DON'T WE DEAL WITH GETTING YOU TO SAFETY FIRST?]|[speaker:422](<localization/work/lore/speaker-Mauser.jsonl#L422>)|`O60bc67fc042ae290c280` [datadm/all.ds#L2467](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2467>)|
|Mauser / `D5abda48862ab1ee031ac`|[H-HUH? WHO'S THIS? YIFFAI?!]|[speaker:455](<localization/work/lore/speaker-Mauser.jsonl#L455>)|`O06b721bca7f15ce6be74` [datadm/all.ds#L3400](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3400>)；`Oa13868cf60016445ad09` [datadm/all.ds#L3412](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3412>)|
|Mauser / `Dff735ec073dd56110fe4`|[UM... THIS CHANNEL IS FOR AUTHORIZED COSMOBREEDERS ONLY.]|[speaker:456](<localization/work/lore/speaker-Mauser.jsonl#L456>)|`Oca4efe1cf5486e58f13f` [datadm/all.ds#L3402](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3402>)；`O926edfa3ee6aee035586` [datadm/all.ds#L3414](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3414>)|
|Mauser / `Dcb1bb863853d9c22415c`|[I'LL HAVE TO DISCONNECT, 'SIR'. OVER.]|[speaker:457](<localization/work/lore/speaker-Mauser.jsonl#L457>)|`Of342fec122260a59ac50` [datadm/all.ds#L3403](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3403>)；`Ob490e1f17c6e17df9ef1` [datadm/all.ds#L3415](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3415>)|
|Mauser / `D3271922884ad74f46814`|[HUH? THIS ISN'T FUNNY!]|[speaker:458](<localization/work/lore/speaker-Mauser.jsonl#L458>)|`Oa030bd8a3661c39bf255` [datadm/all.ds#L3406](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3406>)；`O8a5eefafcb24a51e21d0` [datadm/all.ds#L3418](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3418>)|
|Mauser / `D2a63b8d5028bd977c7e9`|[TELL YOUR MASTER TO CALL ME BACK!]|[speaker:459](<localization/work/lore/speaker-Mauser.jsonl#L459>)|`Oa6671493156a78db7d93` [datadm/all.ds#L3408](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3408>)|
|Mauser / `Da4b7a0aa8874d1d391c1`|[... I'LL JUST CALL BACK LATER...]|[speaker:460](<localization/work/lore/speaker-Mauser.jsonl#L460>)|`O173bafb8e31fb1d7a84d` [datadm/all.ds#L3420](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3420>)|
|Mauser / `Dce704cb5bdb4de7f1a4f`|HUH?! AGENT... YIFFANY?|[speaker:465](<localization/work/lore/speaker-Mauser.jsonl#L465>)|`O6c5ce686c2c900558169` [datadm/all.ds#L3435](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3435>)；`O708457496e662c3a9677` [datadm/all.ds#L3439](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3439>)|
|Mauser / `Df71d1965c0918087934c`|[I USED TO WORK AT A DAIRY FARM, AND THAT IS NOOOT MILK.]|[speaker:567](<localization/work/lore/speaker-Mauser.jsonl#L567>)|`Of79481260db1acaacbc6` [datadm/all.ds#L4027](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4027>)|
|Mauser / `D830461823a20a9396b56`|BUT IT'S SO CHEAP!|[speaker:608](<localization/work/lore/speaker-Mauser.jsonl#L608>)|`O84b9ebe0bbce34e0040e` [datadm/all.ds#L4857](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4857>)|
|Mauser / `D4e0aa800658f149f80ad`|...NOT EVERY TIME...|[speaker:609](<localization/work/lore/speaker-Mauser.jsonl#L609>)|`O1db1fc15adb677bc8474` [datadm/all.ds#L4859](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4859>)|
|Yiffai / `D38a7b6f632d3d4920fba`|[H-HEY! I JUST DON'T KNOW MY OWN STRENGTH!]|[speaker:13](<localization/work/lore/speaker-Yiffai.jsonl#L13>)|`Od00964fe255c6771c86e` [datadm/all.ds#L2011](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2011>)|
|Yiffai / `D09dce01cbf1bccb85bb0`|[UNDERSTOOD, BOSSU! I WON'T LET YOU DOWN.]|[speaker:14](<localization/work/lore/speaker-Yiffai.jsonl#L14>)|`O89b96c25e307c5fe326d` [datadm/all.ds#L2014](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2014>)|
|Yiffai / `D2793fac7cef4c23c459c`|[GEEZE I KNOW THAT, I AIN'T NO PUP...]|[speaker:15](<localization/work/lore/speaker-Yiffai.jsonl#L15>)|`Ob31df43cd88f8778dff1` [datadm/all.ds#L2019](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2019>)|
|Yiffai / `D4972562db19421d8902b`|[HEHE! TOLD YA I WAS TOP OF MY CLASS!]|[speaker:16](<localization/work/lore/speaker-Yiffai.jsonl#L16>)|`O6d723c1cf36b76a79250` [datadm/all.ds#L2023](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2023>)|
|Yiffai / `Da734fe57b0fc487344d5`|[COME ON SIS, SNAP OUT OF IT!]|[speaker:42](<localization/work/lore/speaker-Yiffai.jsonl#L42>)|`Of24fd1153e1712576ec1` [datadm/all.ds#L2133](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2133>)|
|Yiffai / `Df2aac6738ef4e2a9102a`|[BARK BARK!]|[speaker:202](<localization/work/lore/speaker-Yiffai.jsonl#L202>)|`O4354be2ea8cf1ea96af6` [datadm/all.ds#L2677](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2677>)；`Od72a2532df8f28118f39` [datadm/all.ds#L3401](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3401>)；`O3fff5b949cf2ca11aeda` [datadm/all.ds#L3798](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3798>)|
|Yiffai / `Db21242f301a30388ffaa`|[BARK..?]|[speaker:203](<localization/work/lore/speaker-Yiffai.jsonl#L203>)|`Ob7ef6ea77188e80a2316` [datadm/all.ds#L2679](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2679>)|
|Yiffai / `D7221f4aa464ce19d9960`|[BARK?]|[speaker:204](<localization/work/lore/speaker-Yiffai.jsonl#L204>)|`O5086d51e813f57972f8f` [datadm/all.ds#L2687](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2687>)；`O0281175efbfefd1f11c6` [datadm/all.ds#L3805](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3805>)|
|Yiffai / `Db8f4b3f649f39bce2e0c`|[...BARK?]|[speaker:205](<localization/work/lore/speaker-Yiffai.jsonl#L205>)|`O45a0846ce59ac8c293c7` [datadm/all.ds#L2691](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2691>)|
|Yiffai / `D91b6ee0b9cdb27bae33c`|[GLUG. GLOOP.]|[speaker:206](<localization/work/lore/speaker-Yiffai.jsonl#L206>)|`Oae9aabaa7e0c913d0ba0` [datadm/all.ds#L2698](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2698>)|
|Yiffai / `D1bec6191b5d968423f7d`|[GOOP..?]|[speaker:207](<localization/work/lore/speaker-Yiffai.jsonl#L207>)|`Oc3d736938ce9949f1320` [datadm/all.ds#L2700](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2700>)|
|Yiffai / `D069d05645ddbc89f76dd`|[GLOOP?]|[speaker:208](<localization/work/lore/speaker-Yiffai.jsonl#L208>)|`Occ06489d7a4856d49adf` [datadm/all.ds#L2708](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2708>)|
|Yiffai / `D7d2b310847ea26512315`|[...GLUG?]|[speaker:209](<localization/work/lore/speaker-Yiffai.jsonl#L209>)|`Ocecafdd4047d8c5ad7ea` [datadm/all.ds#L2712](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2712>)|
|Yiffai / `D8e0adc626bde4dd652a0`|I... I'M SORRY... Y-YIFFAI OUT!|[speaker:210](<localization/work/lore/speaker-Yiffai.jsonl#L210>)|`O9e8c6bc92c5b884e1cb3` [datadm/all.ds#L2738](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2738>)；`O1d1de1873ef4c286442a` [datadm/all.ds#L2742](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2742>)；`O0c4ed02a9a1bf4c8922c` [datadm/all.ds#L3436](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3436>)；`O9e0e7cd658a4c2373215` [datadm/all.ds#L3440](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3440>)；`Ob7711f8dc438e6e9ed0d` [datadm/all.ds#L3849](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3849>)；`Obc38d2918bf863d8853b` [datadm/all.ds#L3853](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3853>)|
|Yiffai / `D3a3ec2aa6d9eeaa0d7ce`|[WHAT? CAN'T I DESTROY THEM?]|[speaker:215](<localization/work/lore/speaker-Yiffai.jsonl#L215>)|`Od6b03d9386ce4fdd019b` [datadm/all.ds#L2796](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2796>)；`Oe4a12b5958981c7c9fbc` [datadm/all.ds#L2806](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2806>)|
|Yiffai / `De98920ca8f91e60bb6d4`|[IT WAS NO MATCH FOR ME! I WENT HIYAA, THEN ATAA, AN-]|[speaker:218](<localization/work/lore/speaker-Yiffai.jsonl#L218>)|`O07b2c3b2e1eda4aaec28` [datadm/all.ds#L2815](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2815>)|
|Yiffai / `D087d6367e5099eaadae5`|[YOU DON'T THINK YIFFAI YIFFAI, ACE STUDENT]|[speaker:292](<localization/work/lore/speaker-Yiffai.jsonl#L292>)|`O88e973110bfb96cba4aa` [datadm/all.ds#L3186](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3186>)|
|Yiffai / `D62fd87bbc4d0873ca615`|[I MEAN, THAT SOUNDS KINDA HOT...]|[speaker:315](<localization/work/lore/speaker-Yiffai.jsonl#L315>)|`O6be4abf0ed95458ae4fd` [datadm/all.ds#L3338](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3338>)|
|Yiffai / `Dd64f5c8d153c375591a8`|[BARK!]|[speaker:319](<localization/work/lore/speaker-Yiffai.jsonl#L319>)|`Oeb8de746fcbad43f6512` [datadm/all.ds#L3399](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3399>)；`O32c6267dadd73e2cd857` [datadm/all.ds#L3796](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3796>)|
|Yiffai / `D1537d1faf77913ba845d`|[BARK...?]|[speaker:320](<localization/work/lore/speaker-Yiffai.jsonl#L320>)|`O5e83b9d85132dd794235` [datadm/all.ds#L3407](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3407>)|
|Yiffai / `D5b72308202917cc2dfae`|[GLOOP...]|[speaker:321](<localization/work/lore/speaker-Yiffai.jsonl#L321>)|`Ob4091e2321cb64124198` [datadm/all.ds#L3411](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3411>)|
|Yiffai / `Dc03499147faa16401bcf`|[GLUGH]|[speaker:322](<localization/work/lore/speaker-Yiffai.jsonl#L322>)|`Oab2ef7f1d8cb08b32a2f` [datadm/all.ds#L3413](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3413>)|
|Yiffai / `D640ba5ef931f09859b34`|[GLOOP...?]|[speaker:323](<localization/work/lore/speaker-Yiffai.jsonl#L323>)|`Oa80fe03c87c0130cd23c` [datadm/all.ds#L3419](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3419>)|
|Yiffai / `D6eb99d6dc485daf1a20d`|[I'LL FIND THEM! YOU CAN COUNT ON ME!]|[speaker:336](<localization/work/lore/speaker-Yiffai.jsonl#L336>)|`Obfc43543957c2101d4dd` [datadm/all.ds#L3569](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3569>)；`O5f880587a33e89499e4a` [datadm/all.ds#L3610](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3610>)；`Ob3c1f59c63a304df5c2d` [datadm/all.ds#L3678](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3678>)|
|Yiffai / `D4902bcd8da5e984eced4`|[BARK?!]|[speaker:342](<localization/work/lore/speaker-Yiffai.jsonl#L342>)|`O492d955cee03dc689c50` [datadm/all.ds#L3752](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3752>)|
|Yiffai / `D9e930fa6912c6aaa32ef`|[GLOOP?!]|[speaker:343](<localization/work/lore/speaker-Yiffai.jsonl#L343>)|`O9d4cd6a8b874b5b8792c` [datadm/all.ds#L3762](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3762>)|
|Yiffai / `Dd799a28858bd017bf496`|[BARK BARK?]|[speaker:344](<localization/work/lore/speaker-Yiffai.jsonl#L344>)|`Of04bd5a86c078700a639` [datadm/all.ds#L3807](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3807>)|
|Yiffai / `Da224af69fdca52be2b5b`|[GLOOP!]|[speaker:345](<localization/work/lore/speaker-Yiffai.jsonl#L345>)|`Of1944d8b620404ce4e20` [datadm/all.ds#L3815](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3815>)|
|Yiffai / `Dec927568a49a012ef659`|[GLUG-UGH!]|[speaker:346](<localization/work/lore/speaker-Yiffai.jsonl#L346>)|`Of85e2cb5a9fdf05d975e` [datadm/all.ds#L3817](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3817>)|
|Yiffai / `Dbb4fdd448103fc689834`|[GOOP?]|[speaker:347](<localization/work/lore/speaker-Yiffai.jsonl#L347>)|`O8106c0c948299a21a011` [datadm/all.ds#L3824](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3824>)|
|Yiffai / `D6f9b800cb8496e6235fc`|[GLUGH!]|[speaker:348](<localization/work/lore/speaker-Yiffai.jsonl#L348>)|`O633be82addf694767a5a` [datadm/all.ds#L3826](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3826>)|
|Yiffai / `D78442f08fd1910aade20`|[CAN STILL SEE MY BUTT! THAT'S AWESOME!]|[speaker:422](<localization/work/lore/speaker-Yiffai.jsonl#L422>)|`O067a5d74028e46932eef` [datadm/all.ds#L4176](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4176>)|
|Yiffai / `Dd572c9dbbdfe3018ebdf`|[BUT TOMCAT, ISN'T A TAZER LIKE THIS... ILLEGAL?!]|[speaker:425](<localization/work/lore/speaker-Yiffai.jsonl#L425>)|`Oc07ff68ca7da047f75c4` [datadm/all.ds#L4186](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4186>)|
|Yiffai / `D9b4390931b98a23a2ed7`|[HMF! I DO NOT. I LOOK LIKE A COOL PIRATE!]|[speaker:436](<localization/work/lore/speaker-Yiffai.jsonl#L436>)|`O66c6635bffdaf3eee0c6` [datadm/all.ds#L4213](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4213>)|
|Yiffai / `D99be0c88264c88a274a6`|[OUR DAD'S WHISTLE, ACTUALLY. YIFFANY GAVE IT TO ME]|[speaker:474](<localization/work/lore/speaker-Yiffai.jsonl#L474>)|`O93a54425620baf04928b` [datadm/all.ds#L4412](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4412>)|
|Yiffai / `Daff0a4c655c02942b2a9`|[THE ACADEMY AND DAD GAVE HER THIS...]|[speaker:477](<localization/work/lore/speaker-Yiffai.jsonl#L477>)|`O1f6948a3941b8b23c015` [datadm/all.ds#L4416](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4416>)|
|Yiffai / `De07de0de34e1ef44a0ae`|[SHE SAID SHE'D LET ME HOLD IT ON MY FIRST REAL MISSION.]|[speaker:478](<localization/work/lore/speaker-Yiffai.jsonl#L478>)|`Ofb573232a240bfd262cf` [datadm/all.ds#L4417](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4417>)|
|Yiffai / `Db511e25a924247b94f82`|[I GUESS SHE KEPT HER PROMISE AFTER ALL...]|[speaker:479](<localization/work/lore/speaker-Yiffai.jsonl#L479>)|`Of526c583f9e29bf214d0` [datadm/all.ds#L4418](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4418>)|
|Yiffany / `D064674808072ec6c4008`|[ROGER THAT CUTIE, I'LL BE IN TOUCH!]|[speaker:8](<localization/work/lore/speaker-Yiffany.jsonl#L8>)|`Occf4bebdc706950f229d` [datadf/all.ds#L1965](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L1965>)|
|Yiffany / `Dddd21d0630cc823889b6`|[I'M HERE TO RESCUE PEOPLE, NOT HUNT TREASURE]|[speaker:68](<localization/work/lore/speaker-Yiffany.jsonl#L68>)|`O2ae040fb9710d2f9c37a` [datadf/all.ds#L2181](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2181>)|
|Yiffany / `Dc5be7f255998e6e8ae49`|[THAT WAS DEFINITELY ACADEMY STYLE TAZER TECHNIQUE.]|[speaker:75](<localization/work/lore/speaker-Yiffany.jsonl#L75>)|`Od9ead9c83376e143131d` [datadf/all.ds#L2202](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2202>)|
|Yiffany / `D162f21e0d797713ceded`|[LIKE WHAT THE HELL HAPPENED TO MY KID BROTHER?]|[speaker:144](<localization/work/lore/speaker-Yiffany.jsonl#L144>)|`O28a8c07afe4fd6f4d947` [datadf/all.ds#L2439](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2439>)|
|Yiffany / `Db5f510c042be72b137fb`|[WAS DEFINITELY MY BROTHER, YIFFAI.]|[speaker:148](<localization/work/lore/speaker-Yiffany.jsonl#L148>)|`Oa53606e1713be3c7475d` [datadf/all.ds#L2444](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2444>)|
|Yiffany / `Deb45e587c2538fe44b60`|[WAIT... YOU KNOW MY SURNAME? WHO ARE YOU??]|[speaker:166](<localization/work/lore/speaker-Yiffany.jsonl#L166>)|`O77d050dac3ba8c527e64` [datadf/all.ds#L2505](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2505>)|
|Yiffany / `D1e5b312e99d7dfc3c7e5`|[BARK BARK!]|[speaker:207](<localization/work/lore/speaker-Yiffany.jsonl#L207>)|`O8341c8ce331698be8fd5` [datadf/all.ds#L2663](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2663>)；`Od1474779a723fb94f83d` [datadf/all.ds#L3333](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3333>)；`O1e1a6d7726f0ba5cf755` [datadf/all.ds#L3735](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3735>)|
|Yiffany / `Dc3628ab2b6a13a4deec5`|[BARK..?]|[speaker:208](<localization/work/lore/speaker-Yiffany.jsonl#L208>)|`O089280cf0922b4d68fd5` [datadf/all.ds#L2665](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2665>)|
|Yiffany / `Dea3996d35e23286edf01`|[BARK?]|[speaker:209](<localization/work/lore/speaker-Yiffany.jsonl#L209>)|`Odcb37c1ecbc2633b8caa` [datadf/all.ds#L2673](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2673>)；`O7d7026c26a8a04a3488c` [datadf/all.ds#L3742](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3742>)|
|Yiffany / `D8da3038a9a5adde8e192`|[...BARK?]|[speaker:210](<localization/work/lore/speaker-Yiffany.jsonl#L210>)|`O21e1a5933abfcbe56a3a` [datadf/all.ds#L2677](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2677>)；`Oba3a46ef663a93d17294` [datadf/all.ds#L3747](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3747>)|
|Yiffany / `D4d2c83cd89101a34b8ef`|[GLUG. GLOOP.]|[speaker:211](<localization/work/lore/speaker-Yiffany.jsonl#L211>)|`O2e414d9a50ecf2550778` [datadf/all.ds#L2683](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2683>)|
|Yiffany / `D6638f36c03afe4350a5a`|[GOOP..?]|[speaker:212](<localization/work/lore/speaker-Yiffany.jsonl#L212>)|`O278112971f2254c3f194` [datadf/all.ds#L2685](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2685>)|
|Yiffany / `Db56e832a268dd5a0917a`|[GLOOP?]|[speaker:213](<localization/work/lore/speaker-Yiffany.jsonl#L213>)|`Ob3ad883df844350eb50c` [datadf/all.ds#L2693](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2693>)；`O4f91398b05b1838e72da` [datadf/all.ds#L3765](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3765>)|
|Yiffany / `Df228d3b075516925fde2`|[...GLUG?]|[speaker:214](<localization/work/lore/speaker-Yiffany.jsonl#L214>)|`O1f48102fc96b81c79946` [datadf/all.ds#L2697](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2697>)|
|Yiffany / `Dd012ffd6b18b3be64aff`|I... I'LL CALL YOU LATER!|[speaker:215](<localization/work/lore/speaker-Yiffany.jsonl#L215>)|`O577cc1b192c53bde200c` [datadf/all.ds#L2715](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2715>)；`O76404f2fa4ba679f82b7` [datadf/all.ds#L2719](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2719>)；`Oe8c798f002870f4ebdf0` [datadf/all.ds#L3369](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3369>)；`O45f891390de9f8688dd2` [datadf/all.ds#L3373](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3373>)；`Ob12c8dbc68fe1ccc8599` [datadf/all.ds#L3794](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3794>)；`Od830ba5014a21772be6d` [datadf/all.ds#L3798](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3798>)|
|Yiffany / `Dbad1d892b65e445d5d78`|[MADE YA SMIRK! YIFFANY OUT.]|[speaker:253](<localization/work/lore/speaker-Yiffany.jsonl#L253>)|`O93b1831270972ed3ff5e` [datadf/all.ds#L2986](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2986>)|
|Yiffany / `D94ec7de12206c6ffd260`|[...WISH MORE GUYS AT THE ACADEMY HAD BEEN LIKE THAT.]|[speaker:260](<localization/work/lore/speaker-Yiffany.jsonl#L260>)|`Od206255a0d1795eb6fb3` [datadf/all.ds#L3013](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3013>)|
|Yiffany / `D12c7ea906e3d950c7a4f`|[COME ON, I'M A PRO! I CAN HANDLE THEM!]|[speaker:286](<localization/work/lore/speaker-Yiffany.jsonl#L286>)|`O2019feb962688b2accf9` [datadf/all.ds#L3119](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3119>)|
|Yiffany / `D44c6de2b94b8e4bd07c8`|[OKAY, SURE, BUT THESE SPIDERBOTS ARE STILL CREEPY!]|[speaker:305](<localization/work/lore/speaker-Yiffany.jsonl#L305>)|`O5256e197725896a66b82` [datadf/all.ds#L3236](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3236>)|
|Yiffany / `D26799cd7cbda9c08457c`|[BARK!]|[speaker:312](<localization/work/lore/speaker-Yiffany.jsonl#L312>)|`O17121a67418b05f038f7` [datadf/all.ds#L3331](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3331>)；`Od3844a3781d6030559f6` [datadf/all.ds#L3732](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3732>)|
|Yiffany / `D26bebf56e228c9b15686`|[BARK...?]|[speaker:313](<localization/work/lore/speaker-Yiffany.jsonl#L313>)|`O07bd6de2516562d1431d` [datadf/all.ds#L3339](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3339>)|
|Yiffany / `D331f6a71ec7cf33ff723`|[GLOOP...]|[speaker:314](<localization/work/lore/speaker-Yiffany.jsonl#L314>)|`O820d3707b65dfc5b4551` [datadf/all.ds#L3343](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3343>)|
|Yiffany / `Dc08beb9af455c495502f`|[GLUGH]|[speaker:315](<localization/work/lore/speaker-Yiffany.jsonl#L315>)|`O9bbf3a7be671102d8a38` [datadf/all.ds#L3345](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3345>)|
|Yiffany / `D4a084a7e7bb0927d0a3f`|[GLOOP...?]|[speaker:316](<localization/work/lore/speaker-Yiffany.jsonl#L316>)|`Ob306cc094c5e714a669e` [datadf/all.ds#L3351](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3351>)|
|Yiffany / `Daf9f93a68cf92c7924ff`|[BARK?!]|[speaker:336](<localization/work/lore/speaker-Yiffany.jsonl#L336>)|`O05f455b1c464674c019e` [datadf/all.ds#L3689](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3689>)|
|Yiffany / `D140b789b5f14a9b0f6ce`|[GLOOP?!]|[speaker:337](<localization/work/lore/speaker-Yiffany.jsonl#L337>)|`O061699b4d7f09a916d47` [datadf/all.ds#L3699](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3699>)|
|Yiffany / `Deb9b1f94e24683cde9da`|[BARK BARK?]|[speaker:338](<localization/work/lore/speaker-Yiffany.jsonl#L338>)|`O0061f8ac949f856eb5b7` [datadf/all.ds#L3744](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3744>)|
|Yiffany / `Dc9122f8fed82e2a44a08`|[GLUG!]|[speaker:339](<localization/work/lore/speaker-Yiffany.jsonl#L339>)|`O01b4c21f1f0160cf2fae` [datadf/all.ds#L3754](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3754>)|
|Yiffany / `D7329931db349e00a8a9c`|[GLOO-GLOOP!]|[speaker:340](<localization/work/lore/speaker-Yiffany.jsonl#L340>)|`O50a3c995e516ba28bbc4` [datadf/all.ds#L3757](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3757>)|
|Yiffany / `D7ebcaf22a22b5e7d6fdd`|[GLUG?]|[speaker:341](<localization/work/lore/speaker-Yiffany.jsonl#L341>)|`O0c9038431f567dc89780` [datadf/all.ds#L3763](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3763>)|
|Yiffany / `Da027d440754c2b9585a4`|[...GOOP?]|[speaker:342](<localization/work/lore/speaker-Yiffany.jsonl#L342>)|`O33084bfff7b210bf7122` [datadf/all.ds#L3768](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3768>)|
|Yiffany / `Db9c81657bf209f033d72`|[I'LL LICK AND NIBBLE IT GENTLY JUST FOR YOU, TOO!]|[speaker:375](<localization/work/lore/speaker-Yiffany.jsonl#L375>)|`O639822058112fecbd6f8` [datadf/all.ds#L3900](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3900>)|
|Yiffany / `Dd9f86cad75e9da0595c4`|[THE TEMPERATURE, TOMCAT.]|[speaker:403](<localization/work/lore/speaker-Yiffany.jsonl#L403>)|`O92ef16b2279aef5f1d03` [datadf/all.ds#L4054](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4054>)|
|Yiffany / `D77075fd3d25a8e9936bc`|[HEY, A LITTLE PUPPY PLAY NEVER HURT ANYONE, RIGHT?]|[speaker:412](<localization/work/lore/speaker-Yiffany.jsonl#L412>)|`Oc9034154b3e2be274504` [datadf/all.ds#L4083](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4083>)|
|Yiffany / `Dc9e207dabffc42c6f632`|[JUST CASUALLY AROUND THE ACADEMY.]|[speaker:425](<localization/work/lore/speaker-Yiffany.jsonl#L425>)|`Ob77b922beef7b9a829b7` [datadf/all.ds#L4125](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4125>)|
|Yiffany / `Deeb454e9091fd09b7b06`|[IN THE ACADEMY AND YOU WERE PART OF THAT SEX CLUB!]|[speaker:461](<localization/work/lore/speaker-Yiffany.jsonl#L461>)|`O0f8c46b1579f62020441` [datadf/all.ds#L4229](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4229>)|
|Yiffany / `D293a90c96cf8bc008ad8`|[GRR. NOT LIKE I TRIED VERY HARD OR ANYTHING...]|[speaker:482](<localization/work/lore/speaker-Yiffany.jsonl#L482>)|`O06f887a2d5c397ad1f70` [datadf/all.ds#L4368](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4368>)|
|Yiffany / `D1fbce41541c5471fba9f`|[I PASSED IT ON TO YIFFAI FOR HIS FIRST FIELD MISSION...]|[speaker:500](<localization/work/lore/speaker-Yiffany.jsonl#L500>)|`Od2c632a249a5ca995e6f` [datadf/all.ds#L4410](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4410>)|
|Yiffany / `D5b9dba70fc0d7ae6b8c5`|[I TRAINED WITH A SIMILAR DEVICE ON A FIELD MISSION.]|[speaker:504](<localization/work/lore/speaker-Yiffany.jsonl#L504>)|`O4556f6cd2bb095499f54` [datadf/all.ds#L4420](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4420>)|
|Yiffany / `De303c41cf5764d629a0e`|[THERE'S ONLY ONE TYPE OF PAWWING I'M GOOD AT,]|[speaker:557](<localization/work/lore/speaker-Yiffany.jsonl#L557>)|`O51aee77a57477a03474f` [datadf/all.ds#L4592](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4592>)|
|Mauser / `D9d3430edfa4d0d0bef52`|[OH! RIGHT! YOU CAN CATCH ME AT 27.550 ANYTIME!]|[speaker:6](<localization/work/lore/speaker-Mauser.jsonl#L6>)|`Ob7d365072374790a796f` [datadf/all.ds#L1964](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L1964>)|
|Mauser / `D06b57027c1e09a8deef4`|[YOU OUGHTTA CALL UP TOMCAT! SHE'S THE EXPERT ON GEAR.]|[speaker:37](<localization/work/lore/speaker-Mauser.jsonl#L37>)|`Oc09961bc21c658a3e6dc` [datadf/all.ds#L2084](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2084>)|
|Mauser / `Ddec3566a460e8585083c`|[THE TUTONE ELVES ARE SAID TO HAVE WOVEN SPECIAL CLOTH]|[speaker:119](<localization/work/lore/speaker-Mauser.jsonl#L119>)|`O1320955f247bc497178a` [datadf/all.ds#L2490](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2490>)|
|Mauser / `D1b01b84e4dfd2ae94347`|[THAT WOULD ACTUALLY MAKE A PERSON FEEL LIGHTER WHEN WORN!]|[speaker:120](<localization/work/lore/speaker-Mauser.jsonl#L120>)|`O52ed73bef590f579c54c` [datadf/all.ds#L2491](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2491>)|
|Mauser / `D1e3ff6d0bd721c289411`|[AGENT, COME IN. REQUESTING STATUS REPORT.]|[speaker:126](<localization/work/lore/speaker-Mauser.jsonl#L126>)|`O15dbb1b5257f5650405e` [datadf/all.ds#L2552](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2552>)|
|Mauser / `D0b0d72ce9e445fb31f6c`|[HUH? YIFFANY...?]|[speaker:148](<localization/work/lore/speaker-Mauser.jsonl#L148>)|`Ocaeb948aefe4568bb81b` [datadf/all.ds#L3355](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3355>)；`O5acc630361ff65ba8242` [datadf/all.ds#L3363](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3363>)|
|Mauser / `D491439b79c7f8f16a070`|[... DON'T YOU THINK YOUR COVER MIGHT BE BLOWN IF YOU'RE]|[speaker:149](<localization/work/lore/speaker-Mauser.jsonl#L149>)|`Oa7308118fad528f5f568` [datadf/all.ds#L3357](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3357>)|
|Mauser / `Db0c81af2b192dbea5130`|[WAVING A PPP RADIO AROUND AND CALLING PEOPLE?]|[speaker:150](<localization/work/lore/speaker-Mauser.jsonl#L150>)|`O816e96324151621dd6b9` [datadf/all.ds#L3358](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3358>)|
|Mauser / `D190a9d4cf642d322a278`|[W-WHY WOULD I BE JEALOUS OF A PUPPY???]|[speaker:90](<localization/work/lore/speaker-Mauser.jsonl#L90>)|`O4e775239411fffaef993` [datadf/all.ds#L2324](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2324>)|
|Mauser / `D0670c9150738f3f67f89`|[A-A-A-A-A-AIRY!!?]|[speaker:121](<localization/work/lore/speaker-Mauser.jsonl#L121>)|`Odf8eaee8f25e3ff7e70d` [datadf/all.ds#L2494](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2494>)|
|Mauser / `De3404ee0edc8d5a132a4`|I SOMETIMES STOCK UP ON FOOD|[speaker:268](<localization/work/lore/speaker-Mauser.jsonl#L268>)|`Oc10aac2ea75c028119a2` [datadf/all.ds#L4752](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4752>)|
|Mauser / `D3d4fc7ddeec09fde58da`|RIGHT BEFORE FIGHTING A BIG GUY!|[speaker:269](<localization/work/lore/speaker-Mauser.jsonl#L269>)|`O5552f65808b2a5ab2abb` [datadf/all.ds#L4753](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4753>)|
|Mauser / `Dd5b74aa60469f134a518`|I WOULD'VE STOCKED UP ON FOOD|[speaker:294](<localization/work/lore/speaker-Mauser.jsonl#L294>)|`O5ecda2eb9350c47b127d` [datadf/all.ds#L4864](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4864>)|
|Mauser / `De373727b973acfd9b415`|BEFORE A BIG FIGHT LIKE THAT!|[speaker:295](<localization/work/lore/speaker-Mauser.jsonl#L295>)|`O03aa924e392fda642789` [datadf/all.ds#L4865](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4865>)|
|Mauser / `D44887a0491a7e5e54ed5`|[MINES IN THEIR MINES, AS A WAY TO SAY "THAT'S MINE!"]|[speaker:454](<localization/work/lore/speaker-Mauser.jsonl#L454>)|`Oc55856c16103acb09a06` [datadm/all.ds#L3072](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3072>)；`Obc17a16bc5764c1621a2` [datadm/all.ds#L3082](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3082>)；`Oa34b63c37bc726ad5efe` [datadm/all.ds#L3092](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3092>)|
|Mauser / `Dd3bf4b261ffbefea1f47`|[YEAH! IF YOU END UP WITH SOMETHING REALLY IMMORAL...]|[speaker:578](<localization/work/lore/speaker-Mauser.jsonl#L578>)|`O86e842b4d6c07a0a6baf` [datadm/all.ds#L4612](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4612>)|
|Mauser / `Dacb8d7b384b47a5be5f8`|[...BRING A COPY BACK, OKAY?]|[speaker:579](<localization/work/lore/speaker-Mauser.jsonl#L579>)|`O52c408acc0c4af2d542b` [datadm/all.ds#L4613](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4613>)|
|Mauser / `D90387b195df95df4e943`|[N-NO! I WAS JOKING!! IT WAS A JO-]|[speaker:580](<localization/work/lore/speaker-Mauser.jsonl#L580>)|`Oe9885a7e1e66fa9ea69d` [datadm/all.ds#L4617](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4617>)|
|Yiffai / `D510dcddc5212e91c9c32`|[THIS IS AGENT YIFFAI! LOUD AND CLEAR!]|[speaker:1](<localization/work/lore/speaker-Yiffai.jsonl#L1>)|`O7a876e7eb58d720cd06f` [datadm/all.ds#L1964](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1964>)|
|Yiffai / `Dcb31ebcd8ad3f1db0bed`|[OKAY, OKAY! I'LL TRY AND BE A BIT MORE STRATEGIMICAL.]|[speaker:28](<localization/work/lore/speaker-Yiffai.jsonl#L28>)|`Oaaeb46661c5d0f2852fc` [datadm/all.ds#L2068](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2068>)|
|Yiffai / `D1a7b7e489352f23d46f8`|[N-NAUGHTY? I DUNNO ABOUT THAT, BUT TH-THESE SOUND LIKE]|[speaker:35](<localization/work/lore/speaker-Yiffai.jsonl#L35>)|`O06f1907ba07d8dc7b391` [datadm/all.ds#L2105](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2105>)|
|Yiffai / `D2e4eaf8f00647b5a6bf2`|[USEFUL AVENUES OF RESEARCH. YIFFAI OUT!]|[speaker:36](<localization/work/lore/speaker-Yiffai.jsonl#L36>)|`Ofdbd7aa68bd132099508` [datadm/all.ds#L2106](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2106>)|
|Yiffai / `D2c69e3d7c2d459b3ec77`|[RIGHT, LOCALIZED ANTI GRAVITY FIELD WHILE MID-AIR.]|[speaker:71](<localization/work/lore/speaker-Yiffai.jsonl#L71>)|`O7bf0509baac75614001c` [datadm/all.ds#L2223](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2223>)|
|Yiffai / `D05040e7f8f2a9efef038`|[JUMP, AND WHILE MAKING MID-AIR WALL CONTACT, JUMP AGAIN]|[speaker:72](<localization/work/lore/speaker-Yiffai.jsonl#L72>)|`Oa54d41c10c17b79719fa` [datadm/all.ds#L2224](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2224>)|
|Yiffai / `Dc8dca2cd1961aaf9cfa0`|[IN ORDER TO LAUNCH OFF THE WALL TO GREATER HEIGHTS.]|[speaker:73](<localization/work/lore/speaker-Yiffai.jsonl#L73>)|`O94b42704149471e08dfc` [datadm/all.ds#L2225](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2225>)|
|Yiffai / `D9929389ea8339310603b`|[NO TIME FOR THAT. URGENT UPDATE INCOMING:]|[speaker:136](<localization/work/lore/speaker-Yiffai.jsonl#L136>)|`Ofdc1532a3e2b53fbfbed` [datadm/all.ds#L2448](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2448>)|
|Yiffai / `D9f135c43a6fcc8b7011e`|[MY SISTER IS CONF- IRMED TO BE THE AGGRESSIVE AGENT]|[speaker:137](<localization/work/lore/speaker-Yiffai.jsonl#L137>)|`Oc69b9d6eef5497f38c85` [datadm/all.ds#L2449](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2449>)|
|Yiffai / `Da95704a748c2bc6056ed`|[NO DOUBT ABOUT IT. SHE DISROBED IN FRONT OF ME]|[speaker:139](<localization/work/lore/speaker-Yiffai.jsonl#L139>)|`O6157258ddd7562f1bcdf` [datadm/all.ds#L2452](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2452>)|
|Yiffai / `D20c781ab8da9a3857752`|[HER OWN BROTHER!!]|[speaker:143](<localization/work/lore/speaker-Yiffai.jsonl#L143>)|`Obbb95cec4d199e5f3318` [datadm/all.ds#L2459](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2459>)|
|Yiffai / `Dc5631fdfa2754ea960b8`|[WAIT... YOU KNOW MY NAME? WHO ARE YOU??]|[speaker:163](<localization/work/lore/speaker-Yiffai.jsonl#L163>)|`Oe036e902ba2e4762e0a3` [datadm/all.ds#L2524](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2524>)|
|Yiffai / `D3e24ccb78cef401855e5`|[UNDERSTOOD! STAND- ARD COSMOBREEDER PROTOCOL! GOT IT!]|[speaker:189](<localization/work/lore/speaker-Yiffai.jsonl#L189>)|`Od2a0b976c337d0e21de2` [datadm/all.ds#L2624](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2624>)|
|Yiffai / `D0e1f81673f0f76a3023e`|[I D-DON'T KNOW WHAT YOU'RE TALKING ABOUT...]|[speaker:190](<localization/work/lore/speaker-Yiffai.jsonl#L190>)|`O5634e0799263319247d9` [datadm/all.ds#L2627](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2627>)|
|Yiffai / `De04ea274b282da30483d`|[I REMEMBER ONE TIME MY SISTER SNUCK ONE OF THESE OUT]|[speaker:457](<localization/work/lore/speaker-Yiffai.jsonl#L457>)|`O72e5361190684a185aad` [datadm/all.ds#L4370](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4370>)|
|Yiffai / `D24c61177c3634efc3356`|[YEAH, IT WAS OVER WINTER BREAK. I'D SIT AT THE ATHLETIC]|[speaker:458](<localization/work/lore/speaker-Yiffai.jsonl#L458>)|`O2e9ba83c89bf293183ad` [datadm/all.ds#L4372](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4372>)|
|Yiffai / `D19baffd54d78257f39c3`|[CENTER WATCHING HER JUMP BACK AND FORTH, PRACTICING.]|[speaker:459](<localization/work/lore/speaker-Yiffai.jsonl#L459>)|`O63e361bf1516f516b39a` [datadm/all.ds#L4373](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4373>)|
|Yiffai / `Dbf906e0d90ea0b16c930`|[WE WENT THERE EVERY DAY FOR TWO WEEKS! SHE WAS DEDICATED!]|[speaker:460](<localization/work/lore/speaker-Yiffai.jsonl#L460>)|`O365d696ed46ed28c80c7` [datadm/all.ds#L4375](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4375>)|
|Yiffai / `D030115471ecc60cd7e3a`|[I THINK SO! I TOOK A CLASS ON ADVANCED COMBAT GEAR.]|[speaker:480](<localization/work/lore/speaker-Yiffai.jsonl#L480>)|`Oedf4b100d9b153a42153` [datadm/all.ds#L4425](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4425>)|
|Yiffai / `D49ad436b3cb5e5626143`|[TO ACTIVATE THE BUCKLER, I JUST CROUCH, RIGHT?]|[speaker:481](<localization/work/lore/speaker-Yiffai.jsonl#L481>)|`Ofcad33f16d79f0fb7ca6` [datadm/all.ds#L4426](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4426>)|
|Yiffai / `D9f2c466d9a67b32927a6`|[I THINK I'VE GOT IT, THANKS!]|[speaker:482](<localization/work/lore/speaker-Yiffai.jsonl#L482>)|`Oc3b4684289fc6671a773` [datadm/all.ds#L4429](<localization/sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4429>)|
|Yiffany / `D1ae4c8f47e27e2044495`|[GOOD IDEA, SQUEAKS. I'LL MAKE MY WAY TOWARDS THE SURFACE]|[speaker:28](<localization/work/lore/speaker-Yiffany.jsonl#L28>)|`O136b7a4d187e25d4a542` [datadf/all.ds#L2038](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2038>)|
|Yiffany / `Ddea6def7e5eeb5cd2860`|[ANYTIME, HAVE A NICE CARD DATE! TEEHEE!]|[speaker:45](<localization/work/lore/speaker-Yiffany.jsonl#L45>)|`Oe9067aa09e6d84db3485` [datadf/all.ds#L2104](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2104>)|
|Yiffany / `D56717653d42a6522038d`|[DAMN IT, BROTHER, SNAP OUT OF IT!]|[speaker:51](<localization/work/lore/speaker-Yiffany.jsonl#L51>)|`O26c870373992f327f49a` [datadf/all.ds#L2131](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2131>)|
|Yiffany / `D3f98637f9a77f51da786`|[HEY DON'T WORRY, I'M A PRO, RIGHT?]|[speaker:65](<localization/work/lore/speaker-Yiffany.jsonl#L65>)|`Ocd592eacf63396c972ca` [datadf/all.ds#L2173](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2173>)|
|Yiffany / `D33323b4a6ba0debf5d4c`|[YEAH OF COURSE. ALL I HAVE TO DO IS JUMP]|[speaker:77](<localization/work/lore/speaker-Yiffany.jsonl#L77>)|`O4a3d08c8564f648e9a87` [datadf/all.ds#L2213](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2213>)|
|Yiffany / `D916973c9b9c4ca44c005`|[AND THEN JUMP AGAIN WHILE MAKING MID-AIR WALL CONTACT.]|[speaker:78](<localization/work/lore/speaker-Yiffany.jsonl#L78>)|`O2804fb6c03d513e4a5f8` [datadf/all.ds#L2214](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2214>)|
|Yiffany / `D5e37338ec6d41c6b9fb0`|[ARE YOU TWO HAVING A MOMENT? SHOULD I LEAVE YOU ALONE?]|[speaker:81](<localization/work/lore/speaker-Yiffany.jsonl#L81>)|`O49f6501f67e6eb011602` [datadf/all.ds#L2235](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2235>)|
|Yiffany / `D914a987a1733f395f71e`|[THE KIND THAT DOESN'T HAVE A SHOE FETISH, I GUESS?]|[speaker:82](<localization/work/lore/speaker-Yiffany.jsonl#L82>)|`O4d0b85b3042cc4723913` [datadf/all.ds#L2237](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2237>)|
|Yiffany / `Db8acbb4c42c962e7fcfb`|[N-NO, NOTHING LIKE THAT. IT'S JUST... IT SOUNDS LIKE...]|[speaker:89](<localization/work/lore/speaker-Yiffany.jsonl#L89>)|`Of3d8eac24c3a65588c13` [datadf/all.ds#L2260](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2260>)|
|Yiffany / `Dc989f1cc447784ee1b5e`|[COMMAND, THIS IS AGENT YIFFANY. I'VE ENCOUNTERED ANOTHER]|[speaker:127](<localization/work/lore/speaker-Yiffany.jsonl#L127>)|`Oecbb1202d27bbdf4d190` [datadf/all.ds#L2365](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2365>)|
|Yiffany / `D2c2c1d562e8957a4296a`|[I READ THE MISSION NOTES AND HAVE THE COORDINATES]|[speaker:130](<localization/work/lore/speaker-Yiffany.jsonl#L130>)|`O6a6a53c685a277ca9d52` [datadf/all.ds#L2373](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2373>)|
|Yiffany / `D99436dfd9bb090a88e9a`|[FOR ALL THE OTHER TELEPORTALS MEMORIZED ALREADY.]|[speaker:131](<localization/work/lore/speaker-Yiffany.jsonl#L131>)|`O31960787a2dd569b429b` [datadf/all.ds#L2374](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2374>)|
|Yiffany / `D8d2e62d3ef8e01be5973`|[ALRIGHT, ALRIGHT, FIIIIINE. YIFFANY OUT!]|[speaker:132](<localization/work/lore/speaker-Yiffany.jsonl#L132>)|`O20555292d580fdb20496` [datadf/all.ds#L2378](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2378>)|
|Yiffany / `D97faea630b88a385f2a4`|[HOW MANY TIMES DO YOU THINK WE ROUGH- HOUSED GROWING UP?]|[speaker:149](<localization/work/lore/speaker-Yiffany.jsonl#L149>)|`Od27fb97255e6b84fdf3e` [datadf/all.ds#L2446](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2446>)|
|Yiffany / `D45ce8315575e29b5797f`|[OR A "TORCH" AS BOSSU WOULD SAY.]|[speaker:154](<localization/work/lore/speaker-Yiffany.jsonl#L154>)|`O87297e9cd773755f8f8f` [datadf/all.ds#L2466](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2466>)|
|Yiffany / `De1a0234c92300e3684b2`|[YOU KNOW, I GOT SOME SORT OF SHIVERS GOING ON TOO...]|[speaker:155](<localization/work/lore/speaker-Yiffany.jsonl#L155>)|`O11d1ca2d7be5bdc80dc2` [datadf/all.ds#L2470](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2470>)|
|Yiffany / `D227a738649ef918543c6`|[Y-YEAH, I THINK I'LL DO THAT...]|[speaker:156](<localization/work/lore/speaker-Yiffany.jsonl#L156>)|`O065ff9b9ca9e1e74cfe3` [datadf/all.ds#L2473](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2473>)|
|Yiffany / `D141f60ae0fa997f8797b`|[AWWW, WHAT A CUTE COUPLE. HAVE FUN!]|[speaker:163](<localization/work/lore/speaker-Yiffany.jsonl#L163>)|`O4b68c81f222b720baba3` [datadf/all.ds#L2498](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2498>)|
|Yiffany / `D46c50f02a1424a113662`|[AFTER I'VE BONDED WITH THEM USING A COMBINATION OF]|[speaker:189](<localization/work/lore/speaker-Yiffany.jsonl#L189>)|`O41c5c57fde9156338c9a` [datadf/all.ds#L2593](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2593>)|
|Yiffany / `Dce5da45c964d0e8a8bc4`|[CONSENSUAL CONTACT AND FREELY GIVEN MATERIAL GOODS]|[speaker:190](<localization/work/lore/speaker-Yiffany.jsonl#L190>)|`Oef1436e0305dabf72bb7` [datadf/all.ds#L2594](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2594>)|
|Yiffany / `D177164c0a57cf21b708d`|[AS BEFITS A COSMO AMBASSADOR.]|[speaker:191](<localization/work/lore/speaker-Yiffany.jsonl#L191>)|`Oce074f825fc014f7d2fc` [datadf/all.ds#L2595](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2595>)|
|Yiffany / `Da8e8650fbd6b56daadc0`|[COME ON, I DIDN'T GRADUATE TOP OF MY CLASS FOR NOTHING!]|[speaker:192](<localization/work/lore/speaker-Yiffany.jsonl#L192>)|`O44abc9ae439d2607ec8c` [datadf/all.ds#L2599](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2599>)|
|Yiffany / `D57c5bd335135f690ffa5`|[YOU ARE SOOOOOO JEALOUS, HEHE...]|[speaker:193](<localization/work/lore/speaker-Yiffany.jsonl#L193>)|`Obf1ae30118ffe3d4566e` [datadf/all.ds#L2602](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2602>)|
|Yiffany / `D9b31ff5fbfa6022dfbe6`|[YEAH. IT'S A SORT OF FAMILY GOOD LUCK CHARM.]|[speaker:499](<localization/work/lore/speaker-Yiffany.jsonl#L499>)|`O0e65bae7c83c20ddeac4` [datadf/all.ds#L4409](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4409>)|
|Yiffany / `D09e1b712fc50cd15c28a`|[BUT HE GAVE IT BACK A MOMENT AGO, AFTER I KNOCKED THE]|[speaker:501](<localization/work/lore/speaker-Yiffany.jsonl#L501>)|`Oc575c9aeec9de6170b12` [datadf/all.ds#L4411](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4411>)|
|Yiffany / `D301ec9fe3ecf9d8b5c4e`|['STARKILL' OUT OF HIM...]|[speaker:502](<localization/work/lore/speaker-Yiffany.jsonl#L502>)|`Occfbc87de029671fc36f` [datadf/all.ds#L4412](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4412>)|
|Yiffany / `De0d9179b08a5c074ed6b`|[BY CROUCHING, I ACTIVATE THE BUCKLER AND CAN REPEL]|[speaker:505](<localization/work/lore/speaker-Yiffany.jsonl#L505>)|`O8fec67313b3867b57982` [datadf/all.ds#L4421](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4421>)|
|Yiffany / `D36b455ada80ffb77c2ac`|[MOST SMALL WEAPONS FIRE AND SIMILAR.]|[speaker:506](<localization/work/lore/speaker-Yiffany.jsonl#L506>)|`O9f7559bd4fa6abcc88d4` [datadf/all.ds#L4422](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4422>)|
|Yiffany / `De88daf943c43c6554328`|[I'LL HAVE TO LOWER IT TO USE MY TAZER, THOUGH.]|[speaker:507](<localization/work/lore/speaker-Yiffany.jsonl#L507>)|`Ofac6b171c42eef049b06` [datadf/all.ds#L4423](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4423>)|
|Yiffany / `D0a50f5c4a87ae62b887c`|[AND IT DOESN'T REQUIRE A COMPUTER. TRUST ME.]|[speaker:558](<localization/work/lore/speaker-Yiffany.jsonl#L558>)|`O33f21e2f6b7349d90f71` [datadf/all.ds#L4593](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4593>)|
|Yiffany / `Dc8628e6ad4a844720b16`|[AND THEY'LL LOVE IT JUST LIKE EVERY OTHER MISSION!]|[speaker:218](<localization/work/lore/speaker-Yiffany.jsonl#L218>)|`Oe89cde8d1cbb65ca3350` [datadf/all.ds#L2738](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2738>)|
|Yiffany / `D8f30ab4795e69d02a219`|[DAMMIT, MY SQUAD WON'T LET ME HEAR THE END OF THIS.]|[speaker:407](<localization/work/lore/speaker-Yiffany.jsonl#L407>)|`Ofc50086293b617d1b615` [datadf/all.ds#L4067](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4067>)|
|Yiffany / `De008d90dce4ec68cbd51`|[LOOK CAN YOU, I DUNNO, DELAY THAT REPORT FOR NOW?]|[speaker:408](<localization/work/lore/speaker-Yiffany.jsonl#L408>)|`Od71afefaeee707796a6f` [datadf/all.ds#L4068](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4068>)|
|Yiffany / `D3ae713c799422836f5f7`|[WHAT DO YOU THINK OF THIS COLLAR, TOMCAT? STYLISH?]|[speaker:417](<localization/work/lore/speaker-Yiffany.jsonl#L417>)|`Of1c2e58306be9df014ce` [datadf/all.ds#L4093](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4093>)|
|Yiffany / `Dfeb07eb8b89c777218cb`|[COME ON, LET'S BE PRACTICAL! I'VE GOT SNEAKING TO DO.]|[speaker:418](<localization/work/lore/speaker-Yiffany.jsonl#L418>)|`O9111637478e32705eceb` [datadf/all.ds#L4096](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4096>)|
|Yiffany / `D020f46b047402e569089`|[WHO? ME? NOT LIKE *I* HAVE A THING FOR PIRATES. SHUT UP.]|[speaker:449](<localization/work/lore/speaker-Yiffany.jsonl#L449>)|`Of62a225ee612ca0745c9` [datadf/all.ds#L4191](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4191>)|
|Yiffany / `Ddfa6b717ba79969aa462`|[I WILL UTILIZE THIS GARMENT'S WEIGHTLESS ABILITY TO]|[speaker:464](<localization/work/lore/speaker-Yiffany.jsonl#L464>)|`Of7dd9279514d511c1ae6` [datadf/all.ds#L4243](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4243>)|
|Yiffany / `Da345262b75e095bc5ba5`|[TRAVERSE CRUMBLING TERRAIN FOR SAKE OF THE MISSION.]|[speaker:465](<localization/work/lore/speaker-Yiffany.jsonl#L465>)|`O687b2b84587aa0ad073b` [datadf/all.ds#L4244](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4244>)|
|Yiffany / `Dc04c57bf91bedc9af1fa`|[SWIFT. SURGICAL, IN A WAY. AND EVERY STAB FEELS... TRUE.]|[speaker:468](<localization/work/lore/speaker-Yiffany.jsonl#L468>)|`O629f5f52760a183e9308` [datadf/all.ds#L4255](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4255>)|
|Yiffany / `D1169c5033428ad2f5e4a`|[TOMCAT! COME IN! IMMEDIATE ASSISTANCE IS REQUIRED!]|[speaker:539](<localization/work/lore/speaker-Yiffany.jsonl#L539>)|`Ocba36b884ef293d16172` [datadf/all.ds#L4542](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4542>)|
|Yiffany / `De29afce0a07f5509e7d9`|[I FOUND A STRANGE PILL AND ATE IT WITHOUT THINKING]|[speaker:540](<localization/work/lore/speaker-Yiffany.jsonl#L540>)|`O178df2e4abc64c3e30c4` [datadf/all.ds#L4544](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4544>)|
|Yiffany / `Da117aa2f573d1697cf9b`|[AND NOW THE WORLD IS SPINNING... AND GOING DARK...]|[speaker:541](<localization/work/lore/speaker-Yiffany.jsonl#L541>)|`O6ea32f4281cfdd9a57c9` [datadf/all.ds#L4545](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4545>)|
|Yiffany / `D758cf7d8cd91a4c70f28`|[IT... IT WAS.... RED... AND YELLOW... OVAL SHAPED...]|[speaker:542](<localization/work/lore/speaker-Yiffany.jsonl#L542>)|`O6a930a398fe03637e128` [datadf/all.ds#L4548](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4548>)|
|Yiffany / `D36496c62a95c908fb634`|[HAHA, COME ON, IT WAS FUNNY!]|[speaker:543](<localization/work/lore/speaker-Yiffany.jsonl#L543>)|`Oa842460aff02adf254de` [datadf/all.ds#L4553](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4553>)|
|Yiffany / `D5196740e73587d4c7d04`|[I'M NOT SOME PUPPY THAT SHOVES RANDOM THINGS IN MY MOUTH.]|[speaker:544](<localization/work/lore/speaker-Yiffany.jsonl#L544>)|`O1d92c6498c2b01bdcd63` [datadf/all.ds#L4554](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L4554>)|
|Tomcat / `D0ffcf6a1a1080ec407d4`|[YEAH CHEESEBALL OVER HERE LOOKS LIKE HE'S ABOUT TO FAINT]|[speaker:90](<localization/work/lore/speaker-Tomcat.jsonl#L90>)|`O2c7062e3dd39a403386a` [datadf/all.ds#L2486](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2486>)|
|Tomcat / `Df6606140658e223af76c`|[MAYBE I SHOULD START MONITORING /HIS/ VITALS TOO...]|[speaker:91](<localization/work/lore/speaker-Tomcat.jsonl#L91>)|`O102bef63f627ec0a464b` [datadf/all.ds#L2487](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2487>)|
|Tomcat / `Dc9790a635ada0495d7eb`|[WHILE I DEAL WITH THIS FAINTING MOUSE OVER HERE.]|[speaker:94](<localization/work/lore/speaker-Tomcat.jsonl#L94>)|`O837254dff2b71d006e8c` [datadf/all.ds#L2497](<localization/sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2497>)|
