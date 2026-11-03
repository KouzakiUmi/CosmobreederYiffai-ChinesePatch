# batch-09-part04 精校总结（路线 ds）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `orders/batch-09-part04.reader.md`，1,950 行 |
| 结构数据 | `orders/batch-09-part04.json`，8,017 行 |
| 场数 / ROW / CONTROL | 228 场 / 398 ROW / 295 CONTROL |
| 实际读完场景 | **228 / 228**（`coverage.jsonl` 全部 `read_status=read_full`） |
| 覆盖 ROW | 398 / 398（`coverage.jsonl` 的 `row_ids` 与工单逐场一致，已程序校验） |
| 结果分布 | `issues_found` 16 场、`retain` 212 场 |
| current 为空的 ROW | 17 行（既有合句尾行，按口径不报漏译、不填充） |

CONTROL 行按 ORDER §四.1 与参照摘录 §一.2 处理：不读作台词、不改、不提案、不计漏译；本路只核对了它们与分支结构（`if/else if/else`、`### shared ###`）的对应关系。

判据一律以英文原行为准：行尾空格用 `occurrence_id → unit_id → catalog/units.jsonl.source` 核对（SFW 编号行以工单 `source` 字段为准），未使用 `occurrences.trailing_ws`。

## 二、发现总数与分布

共有 18 条发现（`P09-0401`～`P09-0418`）：**A 1 条、B 9 条、C 8 条、needs_evidence 0 条**。

| root | 条数 | finding_id | 要点 |
| --- | --- | --- | --- |
| AreaA_Prison1 | 1 | 0414 | 行尾多空格 |
| AreaA_Prison3 | 1 | 0401 | kobolds→「狗头人」，应为「科博德」 |
| AreaB_Macsen1 | 1 | 0402 | 按键名 DOWN+ATTACK 被改成「DOWN+攻击」（A） |
| AreaB_Macsen2 | 2 | 0403、0404 | 「没开发……苦」病句；「接下来你怎么不走人呢」硬直译 |
| AreaB_Prison2 | 2 | 0405、0406 | free me→「放开我」；当地人被指代为「它们」 |
| AreaC_MacsenDark | 1 | 0407 | hookshot→「钩索」，应为「钩爪」 |
| AreaC_Prison1 | 1 | 0415 | 行尾多空格 |
| AreaC_Prison2 | 1 | 0409 | tazer→「电击器」，应为「电击枪」 |
| AreaC_Prison3 | 1 | 0410 | 「去找其他人救」悬空，易读反 |
| AreaE_Macsen1 | 3 | 0416、0417、0418 | 行尾多空格 ×3 |
| AreaH_Cellar | 1 | 0408 | agent→「探员」，应为「特工」 |
| Gitgud | 1 | 0411 | 「在光电击枪击中时」缺被动标记 |
| Test_Hacker1 | 2 | 0412、0413 | fancy chips 与 satlink 的同句两版不一致 |

按类别：`format` 6、`term` 5、`meaning` 4、`idiom` 3。

### A 级（1 条）

- **P09-0402**（SC261c757407969621，L744）：`DOWN+ATTACK` 被改写成「DOWN+攻击」。按键名属受保护标记（ORDER §四.4、参照摘录 §三、R9 已落地 `UP+ATTACK`），照当前中文，玩家按提示找不到该键。

### B 级（9 条）

术语类 4 条（0401 科博德、0407 钩爪、0408 特工、0409 电击枪）都给出了词典条目或同批同 root 的反例行号；语义类 3 条（0405 free me、0406 指代、0410 悬空宾语）都是同场或邻场可自证的读解错误；语病类 2 条（0403、0404）。这 9 条都只需改动一处短语，`proposed_zh` 与当前行等长或近乎等长。

### C 级（8 条）

语法标记 1 条（0411 补「被」）、跨版本与跨场用词不一致 2 条（0412「花哨芯片」、0413「卫星链路/有点偷看了」）、行尾多空格 5 条（0414～0418）。

17 处 `current` 为空的合句尾行全部按口径处理，未报漏译、未填充；其中没有任何一处因「硬粘」而成病句，故本批没有合句类发现。

## 三、高风险连续段

1. **合句断点（17 处空尾行）**：集中在 `AreaB_MacsenBar.Talk.main`（L870/871）、`AreaC_MacsenDark.DarkNoPurchase`（L1196/1197）、`AreaE_Macsen1.SpecialGeiger`（L1500/1503 与 sfw 版 L1492/1493）、`AreaH_Cellar.Talk.food`（L1573/1574、L1576/1577）、`AreaH_MacsenBar.PsyUp`（L1626/1627）、`AreaH_MacsenBreeding.SpecialFap`（L1720/1721）、`AreaH_MacsenBreeding.TazerTrainer`（L1701/1702）、`AreaH_Ship.Talk.Ship`（L1859/1860、L1869/1870）、`AreaX_Upgrade.Hack`（L1930/1931）、`Gitgud.Tip3`（L3309/3310）、`Gitgud.Tip5`（L3317/3318）、`Hacker_Shared.Meeting`（L4972/4973）。并句后的中文行宽达 60～88 半角列（L1196、L1626、L1869、L1930 最长），属既有合句的排版约束，本批未作为发现上报，见第七节。
2. **条件分支密段**：`AreaH_Cellar.Talk.food`（`agentsRescued()` 7/4/1/else 四段 × 男女两版，各 12 行）、`AreaB_Slaver2`（`koboCostume()` 与 `!koboCostume()`）、`AreaC_Slaver1`、`AreaX_Upgrade.NotEnoughMoney`、`Test_Slaver1.HelloNoJuice`（`isFeral()`）。逐分支核对后只有 P09-0408 一处落点，分支内容未被两版混用。
3. **无线电套语**：本批没有 Bossu 的无线电行；唯一涉及频率的是 `Test_Hacker1.Talk.radio`（`28.250`，数字原样保留，无发现）。`Hacker_Shared.Meeting` 的黑客台词技术性最强，也是仅有的「同一句英文出现在两个场景」的段落（P09-0412、P09-0413）。
4. **问答错位**：本批场景碎且跨场不连续，未发现把上一场的答句接到这一场问句的情况；最接近的是 `AreaC_Prison3.SoldOut` 的收尾（P09-0410），当前译文读起来像在回答上一句、实际是让人去找别的待救者。
5. **已裁项边界**：`LIGHTTAZER`（L1508，未终裁，未提案）、`UP+ATTACK`（未动）、`下、中、中、上`（R8 谜题提示，未动）、`伊吠/伊吠妮`（R3，未动）、`torch→手电筒`（R2 口径内，未动）、`council→议会` 与 `command→指挥部` 未混用。

## 四、男女两版（datadf / datadm）不一致清单

同一英文在不同行译法不同者共 14 组（同场 sfw/nsfw 变体亦计入）：

| 英文 | 两版译文 | 处理 |
| --- | --- | --- |
| Why don't you take off next, huh punk? | 「钱都拿了，还不快滚，小混混？」/「接下来你怎么不走人呢，啊，小混混？」 | **提案 P09-0404** |
| It's been so long since I saw another one of you agent sorts here | 「……这种特工了……」/「……这种探员了……」 | **提案 P09-0408** |
| Greetings, Yiffai. You don't know me, but I kinda snooped your satlink. | 「……偷偷窥探了你的卫星通讯。」/「……有点偷看了你的卫星链路。」 | **提案 P09-0413** |
| It's simple: You bring me those fancy chips you find out there, | 「那些高级芯片」/「那些花哨芯片」 | **提案 P09-0412** |
| Wish I could get my hands on a nice cold ICECOLA right about now... | 仅 `ICECOLA` 两侧空格有无之差 | 不报（CJK/拉丁间距全局待裁） |
| Please come back soon with your master, and a key! | 「请早点……」/「请快些……」 | 不报（不同 NPC，口吻差） |
| Remember, no refunds! What else you need? He! He! He! | 「还要点啥？」/「还要什么？」 | 不报 |
| With all these folks recovering here, business has been booming! | 「生意可真是红火」/「生意红火得很」 | 不报 |
| Starting to get lively in here, isn't it? | 「这儿开始热闹起来了」/「这儿总算开始热闹起来了」 | 不报（后者略加「总算」，可接受） |
| But you know, if there were more folks resting up in this hangar | 「歇着的人再多些」/「多些人休整」 | 不报 |
| Hey! Where are you going ducky?! We've got refactoring to do! | 「小鸭子」「我们」/「小鸭鸭」「咱们」 | 不报（不同 NPC） |
| -wait a sec, you're not the delivery guy! | 「你不是送货的」/「你可不是送货那家伙」 | 不报 |
| Oh, it's a dog! / Do you want anything else? | 各处仅有无「还」字等差 | 不报 |

## 五、未覆盖项

无。228 场全部 `read_full`，398 行 ROW 全部逐行对照英文；没有因读不全而记为 `partial`／`not_read` 的场次。

## 六、待裁与未提案的观察（留给主代理判断）

1. **LECT / Lect**：本批混用「LECT」（L682、L694、L1014）与「Lect」（L1134、L1910）。词典条目 `Lect.name＝LECT`、`BarLectReward.name＝500 LECT` 支持大写，但 ORDER §四.4 把 `Lect` 列为「原样保留」的保护标记，两者冲突，故未提案，只在 `coverage` 的 note 记录。
2. **Cosmosuit＝宇宙服 vs spacesuit 的「宇航服」**（L1052、L1102、L1112）：英文写的是通名 spacesuit，非道具名 Cosmosuit，未提案。
3. **Kobo gear→「科博装备」**（L709）：词典条目只有 `KOBOSUIT＝科博服`、`KOBOHEAD＝科博头`，「科博装备」是派生的集合说法，未提案。
4. **「他们」指生物**（L1720「拿着这个，再一次跟他们亲近、亲昵」）：同批对生物惯用「它们」，但说话人是对养宠者讲口语，未提案。
5. 若干低优先措辞未提案：L118「嗨、嗨」对应 h-hey、L453「等着轮到你吧」、L1056「加油，猛将」（tiger）、L1844「带上几个这个」、L1242「神奇的水晶」（crazy crystals）。

## 七、本工单不能证明的东西

1. **渲染未验证**：本路没有构建、没有启动游戏，也没有读构建产物。行长是否在 240px／12px／每页 3 行的框内真的不溢出，最长的那几个合句行（L1196、L1626、L1869、L1930 等，宽 74～88 半角列）是否会在实机多折一行，只能实测。
2. **只覆盖 candidate31 的显示行**：工单给的 `current` 是 `r9-polish-candidate31` 的实际显示行；本路没有核对其它候选或更晚构建是否已改动这些行。
3. **文体内一致性未闭环**：引号体例（`“”` 与 `""` 并存，如 L409、L1157）、CJK 与拉丁字母间距（LENT／ICECOLA／F.A.P／400 太赫兹 等处）在参照摘录 §六 已列为全局待裁，本批未统一、未报。
4. **术语只在词典可证范围内核对**：把物种／道具名改回词典写法时，依据是 `catalog/units.jsonl` 里条目单元的 source 与草稿（`KOBOLD`、`HOOKSHOT`、`tazer`、`agent`），不是 `datav/dictionary.json` 的中文原文；本路没有解包归档去比对词典中文侧。
5. **全库不统一项未处理**：`HOOKSHOT` 另有「钩锁」写法（单元 `D91b0a5508d611271c4b7`），跨批统一超出本工单范围，只在 P09-0407 的 `note` 记录。
6. **本路为独立审校**：按派单要求未读、未参考本批另一路产物，也未做交叉核验；两路结论是否一致需主代理比对。
