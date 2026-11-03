# batch-09-part03 精校小结（路线 ds）

## 一、输入与实际读完

| 输入 | 规模 | 读取情况 |
| --- | --- | --- |
| `orders/ORDER.md` | 83 行 | 整篇读完 |
| `orders/reference-excerpt.md` | 60 行 | 整篇读完 |
| `orders/batch-09-part03.reader.md` | 1,991 行（229 场／399 物理 ROW） | 按 1–80 / 81–340 / 341–600 / 601–870 / 871–1,140 / 1,141–1,410 / 1,411–1,680 / 1,681–1,991 八段读完，无跳段 |
| `orders/batch-09-part03.json` | 229 scenes／399 rows／37 root | 用于取精确 `scene_id`／`row_id`／`source`／`current`／`controls` |

- 实读场数：**229／229**，`coverage.jsonl` 全部 `read_full`，无 `partial`、无 `not_read`。
- 方法：按 `TRANSLATION_PLAN.md` 第五节七步逐场连读（锁事实 → 连读现译 → 放回人物 → 倒查英文 → 再看结构）；分级按第七节。
- 行尾空格判据只认英文源行：`catalog/occurrences.jsonl` → `catalog/units.jsonl` 的 `source`，并与工单 JSON 的 `source` 双向核对（两条路径结论一致：15 行中文多空格）；**未使用** `occurrences.trailing_ws`（它描述中文侧）。

## 二、发现总数与分布

- 总数 **23** 条：**A 0 ／ B 6 ／ C 17 ／ needs_evidence 0**；涉及 **21 场**（`SCa77905dd8a62d2c1` 与 `SCecea8ac84823cd0b` 各 2 条），其余 **208 场**记 `retain`。
- 按 root 归组（15 个 root 有发现）：

| root | 发现数 | 编号 |
| --- | --- | --- |
| AreaH_Cellar | 4 | P09-0303、0307、0320、0321 |
| AreaE_Macsen1 | 3 | P09-0306、0318、0319 |
| AreaA_Macsen2 | 2 | P09-0311、0312 |
| AreaA_Prison1 | 2 | P09-0313、0314 |
| AreaX_Upgrade | 2 | P09-0322、0323 |
| AreaA_Prison2 | 1 | P09-0305 |
| AreaA_Prison3 | 1 | P09-0301 |
| AreaB_Macsen1 | 1 | P09-0309 |
| AreaB_Prison1 | 1 | P09-0302 |
| AreaC_MacsenDark | 1 | P09-0308 |
| AreaC_Prison2 | 1 | P09-0315 |
| AreaC_Prison3 | 1 | P09-0316 |
| AreaC_Slaver1 | 1 | P09-0317 |
| AreaH_MacsenBar | 1 | P09-0304 |
| AreaA_Macsen1 | 1 | P09-0310 |

- 按类别：`term` 5、`continuity` 1、`idiom` 1、`voice` 1、`format` 15（其中 14 条为行尾空格，1 条为合并行双省略号）。
- B 级六条：吠叫者→吠犬（0301）、狗头人→科博德（0302）、探员→特工（0303）、合句病句「救了一大批他们」（0304）、把字句被省略号拆断（0305）、`!inCosmoSuit` 分支里 spacesuit 译「宇航服」（0306）。
- **A 级为 0**：逐场核过否定、数量、施受、条件分支与揭示顺序（27 处 `CONTROL` 条件全部按分支核对，`hasItem(Key)`／`agentsRescued()`／`koboCostume()`／`inCosmoSuit()`／`isFeral()`／`f(ctx_*)` 六类条件均译对），未发现误义或玩法误导。

## 三、结构与格式核验（机检 + 逐行确认）

- 说话人前缀 229 场全部与 `speaker` 一致（`  * `、`    * `、`    Gitgud: `、`  Anon/Fox: `）；分支内缩进差异属既有体例，不动。
- 方括号对数、`<3`、`*…*`、`[ ]`、`DOWN+ATTACK`、`400 太赫兹`、`28.250`、`G+RADIO`、`TAEGXLAA`、`;3`、`Anon/Fox` 逐行与英文对齐；无行末标点缺失。
- 行尾空格：中文比英文多 15 行（L420、475、493、547、589、1337、1402、1406、1490、1492、1493、1553、1563、1894、1898）。其中 L1493 已并在术语提案（0306）里一并去掉，其余 14 行各立一条 `format` 提案。
- **镜像不报**：L494、867、1213、1301、1397、1492(sfw)、1494(sfw)、1579、1895、1899 共 10 行英文源行本身带行尾空格，中文同步带空格是镜像，逐行核对后未报。
- 合句尾行（ZH 为空）17 行，按工单口径**不报漏译、不填充**：L868、1203、1231、1493、1495、1584、1587、1576、1579、1637、1660、1653、1920、1956、1948、3381、3385。

## 四、高风险连续段

1. **问答错位风险段**：`AreaH_Cellar.Talk.food` 四分支（`agentsRescued()` 0／1／≥4／≥7）与其 sfw 镜像四分支是同一 NPC 的两套文本，逐分支比对后分支对位正确；`AreaX_Upgrade.Purchased`／`SoldOut`／`CancelPurchase` 三处 `f(ctx_hack_the_world)`／`f(ctx_hack_e_hack)` 分支也逐条对位，无错挂。
2. **合句断点**：17 处合句尾行（见上）。其中 **Gitgud.Tip4／Tip5（L3380、L3384）** 是把两条**各自成对的**方括号提示并进一行，合并后括号对由 2 组变 1 组、第二条物理行整行为空。按「ZH 为空的 ROW 是合句尾行」不报漏译，但这与「保护标记原样保留」的边界值得主代理裁定是否要保留两组方括号。
3. **无线电／固定套语**：`Hacker_Shared.Talk.radio` 频率 `28.250` 与 `NotEnoughMoney` 三条重复段（`isolinear modules`／`400 terahertz`）男女两版译文完全一致；`Gitgud` 两条提示全大写按陈述处理，未加吼叫。
4. **合并长行**：本批多行是把两三个英文物理行并成一行，现译最长约 46 字（L1295 一类）。本次所有提案均不长于现译，未新增折行风险；仍未实测 240px／12px 下的实际折行（见第七节）。

## 五、男女两版（datadm／datadf）不一致清单

同一 `source` 在两条变体里译文不同（均判为可保留的差异，不作提案；除 0303 那条术语分叉）：

| 英文 | 女线 | 男线／sfw | 判断 |
| --- | --- | --- | --- |
| Take care with the heat out there! | L475「外头这么热，多当心！」 | L493「外面那么热，你可当心！」 | 口吻差异，保留（两条各带行尾空格缺陷，另立 0311／0312） |
| Wish I could go out and get a nice ICECOLA… | L476「弄瓶上好的 ICECOLA 来压压这暑气」 | L494「买瓶ICECOLA消消暑」 | 保留 |
| Please come back soon with your master, and a key! | L563「请快些…」 | L5120「请早点…」 | 保留 |
| Take care out there. Ole Tutone is a rough place these days. | L1012「老图托恩」 | L1416「图托恩」（丢了 Ole） | 保留，Ole 未译出属可接受省略 |
| You smell pretty cute for a kobold… | L1062「你这科博德，闻起来倒挺讨人喜欢」 | L1067「作为科博德，你闻着还挺可爱的」 | 保留 |
| With all these folks recovering here… | L1575「在这儿养伤」 | L1567「在这一带养伤」 | 保留 |
| Starting to get lively in here… | L1578「总算开始热闹」（多「总算」） | L1570「开始热闹起来了」 | 保留，语义一致 |
| But you know, if there were more folks resting up… | L1583「多些人休整」 | L1575「歇着的人再多些」 | 保留 |
| **It has been so long since I saw another one of you agent sorts here** | L1586「**探员**」 | L1578「**特工**」 | **术语分叉，提 P09-0303** |
| Are you delivering my weekly supplies? | L1897「来送我这周的补给的吗」 | L4976「来送每周补给的」 | 保留 |
| According to my calculations, your tazer should be fully repaired! | L1897「根据我的计算…已经完全修好」 | L1898「按我的计算…完全修好」 | 保留 |
| Hmph! What do you want? / Lot of nerve… | L5036「你有什么事」／L5037「奴隶贩子恶棍」 | L5030「你想干什么」／L5031「奴隶贩子混蛋」 | 保留（并列结构两边都略生硬，不提案） |
| Hey, help a placeholder out here! | L5088「帮这个占位角色一把吧」 | L5075「帮帮这个占位角色啊」 | 保留 |
| I am already rescued, **Yiffai**!（datadf 文件） | L5267 照源文作「伊吠」 | — | 源文在女线文件里仍写 Yiffai，属既有源文异常，不擅改（见第七节） |

## 六、参照摘录与语料冲突（不提案，报冲突）

1. **HOOKSHOT**：参照摘录 §三 记 HOOKSHOT＝钩爪，但 zh-CN 语料有明确记录「hookshot 取『钩索』」，且本行（L1215「先是有人偷了我的钩索」）与语料一致。按 ORDER「以语料为准」，**不改**，只报冲突。
2. **torch**：R2 已裁 torch＝手电，但本批 L1537 的 `THE TORCHES THAT LINE THE WALLS` 指墙上的火把，语料亦记「TORCH译火把，与手电筒区分，未定」。故此处作「火把」**不报**；同批 flashlight 仍作「手电筒」。
3. **LECT 体例**：同一货币在批内有 `lect`／`Lect`／`LECT` 三种写法（L434、L686、L635、L680），且「两侧留半角空格」与「CJK 与拉丁间距体例全局待裁」相抵。**不提案**，留待全局裁；本批未动。
4. **维修舱／维修区**：同一设施 `repair bay` 在 `AreaX_Upgrade.Talk.macsen` 作「维修舱」（L1507），在 `Talk.repair` 作「维修区」（L1521）；语料两种写法分别出现 3 次／4 次，无多数写法，**不提案**。
5. **零件／部件**：`components` 在 L1585 作「零件」、L1611 作「部件」，语料两词并存（13／16），**不提案**。
6. **灵能／精神力**：`PSY`／`psychic power` 在批内分别作「精神力」（L63、L1069）与「灵能」（L1295、L1969），语料两词各 50+ 次，**不提案**。
7. **太空小鬼／太空小混蛋**：`spacebrats` 两处不同译，同在反派口中，判为自然变化，**不提案**。
8. **cosmo fellas**：已提 P09-0307（「宇宙来的家伙」→「太空伙计」），属批内定式统一，不是词典术语。

## 七、未覆盖项与「本工单不能证明的东西」

- 未覆盖项：**无**。229 场全部 `read_full`；未出现需要越界（改归档／改台账）才能判断的条目。
- 已知未做、因此不能证明：
  1. **未解密构建产物里的中文词典条目名**：术语判断依据是参照摘录 §三 自带的词典条目名与 zh-CN 语料实际用法，未直接核对 `candidate31` 内 `datav/dictionary.json` 的中文侧。
  2. **未做字宽／折行实测**：本批多处合并行在 240px／12px 下是否超 3 行未验证；只说「不新增长度」。
  3. **未跑构建／回归、未进游戏**：`proposed_zh` 只是提案文本，是否正确落盘、是否与 `candidate33` 台账冲突不在本工单范围。
  4. **LIGHTTAZER 中文名未终裁**：批内现作「光电击枪」（L1546），按参照摘录 §六 **未提案**。
  5. **源文自身异常不属可判点**：`datadf` 文件里 `Yiffai`（L5267 等）、`get back to to hangar`（L1304 源文重复 to）、`The say Triangle powers`（L1652 源文笔误）、`Test_*` 场景与正式场景共用行号（如 L5287 同时被 `Test_Slaver1.GoodbyeNoID` 与 `Test_Slaver1.Hello` 用作头行）——译文按源文处理，未据此提案，也未替源文补正。
  6. **已裁决项未动**：R2（agent＝特工、torch＝手电，仅在不冲突处援引）、R3 人名（伊吠／伊吠妮／麦森／图托恩 等）、R6 Bumper＝弹跳机、R8 谜题提示、R9 已落地项（Kobo＝科博德／Cosmohelm／Cosmosuit／council／feral／knot／nubs／UP+ATTACK）未被重提；本次涉及 Kobo／Cosmosuit 的两条是**应用**既有裁决修异写与装备名，不是重开裁决。
