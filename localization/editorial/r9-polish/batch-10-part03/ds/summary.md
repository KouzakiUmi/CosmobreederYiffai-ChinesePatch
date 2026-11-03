# batch-10-part03 精校小结（路线 ds）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-10-part03/orders/batch-10-part03.reader.md`，1,167 行 |
| 结构化同源 | `orders/batch-10-part03.json`，4,008 行（99 场／299 行） |
| 规范 | `orders/ORDER.md`（88 行）、`orders/reference-excerpt.md`（97 行），全文读完 |
| 场景覆盖 | **99／99 场 read_full**（无 partial、无 not_read） |
| 行覆盖 | **299／299 行**，reader 分段（1–300／301–600／601–900／901–1167）逐行连读 |
| 写法 | 逐场按 `TRANSLATION_PLAN.md` 第五节七步重写（复述意图→锁事实→连读→重写→放回→倒查英文→再看结构）；不改任何其它文件、不跑构建、不实机 |

程序化核验（只做定位，结论仍人工判）：`|` 段数 EN/ZH 全批一致（0 处不等）；保护标记 `[ ] $ % * ___ @ <3` 计数全批一致；段内宽度（CJK 计 2 列）超 22 列者仅 `ui.end` 系居中行与两条制作名单（按口径不报）；「同英文不同中文」与「同中文不同英文」两向反查各命中 1 组（均已立案）；EN 侧行尾空格仅在提案行逐行核对。

## 二、发现分布

共 **9 条**（涉及 13 个 row_id；全部落在 root `ui`，本文的 root 指场景 root，归档为 `datav/dictionary.json` 两版）：

| 严重度 | 条数 | 编号 |
| --- | --- | --- |
| A | 3 | P10-0301、P10-0306、P10-0308 |
| B | 2 | P10-0304、P10-0305 |
| C | 3 | P10-0302、P10-0303、P10-0309 |
| needs_evidence | 1 | P10-0307 |

按类别：`term` 3、`meaning` 2、`continuity` 1、`idiom` 1、`format` 1、`source_uncertainty` 1。
按版本：nsfw 5 条、sfw 4 条。按其 root 细分：`ui.achievement.*` 2、`ui.breeding.*.affinity` 2、`ui.card.CosmoCardBigbold.desc` 1、`ui.data.*` 1、`ui.end.*` 3。

其余 90 场明确 **retain**（无语病且保留人物／语域差异，不为凑数重写）。典型 retain 依据记在 `coverage.jsonl` 的 `notes`：地名与存档代号（`SCE-*`／`DPB-*`／`SCEA-CTR`／`ZER-*`／`AYS-*`）、键名（`START`／`SELECT`／`A/B/X/Y`）、四种 `*.needs` 组合的 AND／BUT 与否定、`Tier2/Tier4` 逐行对位、`m_AgentMZ1/2/4`（R8 已裁决措辞）、`ui.options` 24 项、作弊码说明的条件与倍率方向。

## 三、高风险连续段

1. **`ui.end.Tier1` 阶级名与赞美句错位（P10-0308，A）**：`BEGINNER !` 被译成赞美句「还不错！」，`NOT BAD FOR` 行只剩悬空的「对新手来说」，阶级名整条丢失。英文四行合读为「NICE TRY! NOT BAD FOR A TRAINEE. RANK: BEGINNER!」。这是本批唯一的「问答／标签错位」型缺陷，`Tier2/3/4` 无同类问题。
2. **`ui.end.BadEnding` 合句断点（P10-0307，needs_evidence）**：`TRAEH IS`／`THERE...`／`STILL OUT` 按归档顺序读不成句，英文只有 r1→r3→r2 才成立「TRAEH IS STILL OUT THERE...」；现译按行分配后若同屏自上而下会读成「Traeh还／那里……／在外面」。显示行序在工单内无法证明，故不冒充 A/B/C，note 给了两种行序下的分配方案。
3. **`ui.data` 两版同句复制的隐患（P10-0306，A）**：`f_ClassicWerepup` 的 sfw 变体英文换成「揍了他一顿之后和他交朋友」，中文整行照抄 nsfw 版「回忆涌上心头，又迟疑起来」——同一份 memory 在男女两版变成两件事。这印证了 ORDER §四.10 的风险点：同型 key 的 nsfw／sfw 必须分别读英文。
4. **制作名单居中空格（`ui.end`）**：`*!`＋大段空格、名单行首行尾空格均为居中装置，按口径不报不改；本批未对这类行提任何提案。
5. **无线电套语**：本 part 无无线电对白（299 行全是字典值／嵌套 JSON 值，`speaker` 全空、`line` 全 null、无 CONTROL 行），此风险点在本 part 不适用。

## 四、男女两版不一致清单

| # | 项 | nsfw 侧 | sfw 侧 | 处理 |
| --- | --- | --- | --- | --- |
| 1 | `ui.achievement.hack_the_world` 成就名 | `HELLO WORLD`（未译） | `你好，世界` | P10-0301（A） |
| 2 | `ui.data.f_ClassicWerepup` memory 文案 | 击败小狼崽后「回忆涌上心头，又迟疑起来」 | 英文为「揍他一顿后和他交朋友」，中文照抄 nsfw 版 | P10-0306（A） |
| 3 | `ui.breeding.Kobold.affinity` 末段 | —（nsfw 无此场） | 「真是个好宠物！」vs 同批另四条「真是棒极了的宠物！」 | P10-0304（B） |
| 4 | `ui.card.CosmoCardDragon.desc` 种族名 | `Fenfen超能力者` | `芬芬长老`（库内唯一「芬芬」） | **不提案**：FENFEN 中文名未终裁，按口径不按一股改另一股；待主代理终裁后需两侧同时处理 |
| 5 | `ui.end.Tier4` | 哇！！／你是／真正的／宇宙-／育种者！ | 同句同译、空行占位一致 | 一致，retain |
| 6 | `ui.breeding`／`*.needs`／`ui.options` 等同型 key | 与 sfw 侧逐条同形 | 同左 | 一致，retain |
| 7 | 卡面 `.desc` 值尾部换行 | 13 行（nsfw 侧）值尾带 `\n` | 无 | 结构性差异，见第六节待核（不在本批判据内，未立案） |

## 五、术语与参照冲突记录（按 ORDER 口径：以语料为准，不据摘录强行改）

1. **nubs**：摘录 §五「R9 已落地 nubs＝凸粒」，而 `ui.card.CosmoCardBigbold.desc` 第 2 段作「肉突」（同语料其它 nubs 行作「小凸粒」）。按既定术语提请对齐 → P10-0305；只改一词，14 段不变。
2. **LECT 两侧空格**：摘录 §三记「LECT（大写，两侧留半角空格）」，本批 `ui.presetcheat.no_spend_lect` 作「不消耗LECT。」无空格。属 CJK／拉丁间距体例，本批**不报**，仅记冲突。
3. **`R 肩键`**：摘录 §一.5 的既有对应「R 肩键」对应源串 `R Bumper`；本场 `input.xinput` 是 `LEFT BUMPER`／`RIGHT BUMPER`，译作「左肩键／右肩键」。两串不同源，**不构成冲突**，未提案。
4. **`上位特工`**：`m_AgentM03` 的 `TOP AGENT` 作「上位特工」。语料内「上位特工」75 处、「顶尖特工」24 处，前者为主用写法，按语料为准**不改**（虽在情色语境下「上位」易生歧义，但无更强出处支持单点改动）。
5. **卡面标题对齐**：`BARKER   <FAUNA>`→「吠犬  <动物>」等五张卡一律「名＋两空格＋`<类别>`」，与英文原空格数不同但五卡自洽；按「`<...>` 与对齐空格原样保留」的口径不单改一张卡（会造成同屏不一致），未提案。
6. **`FENFEN`／`LIGHTTAZER`／引号体例**：未终裁，本路不提案（对应项见第四节 #4）。

## 六、未覆盖项与「本工单不能证明的东西」

1. **跨侧地名一致性只部分可证**：`navmap` 与 `/patchDictionary/navmap` 两侧对照需要同一 Area 的两份条目；本 part 只含 jar 侧 `navmap.AreaB`，patch 侧仅 `AreaC/E/H/TestArea/menu`。本 part 内可证的一致项：`DEPOT B`→仓库B（menu 与 AreaB 两处同形）、`HANGAR`→机库（patch 侧两处同形）、`EXILE`→流放地（patch 侧两处同形）。其余地名的跨侧一致**不能由本工单证明**。
2. **容器与行宽只做了静态推算**：提案均未增 `|` 段数、未增物理行，段内字数均未超过英文对应段（唯 P10-0304 段 3 由 7 字增至 9 字，仍短于英文该段 18 列）。**未实机渲染**，`行宽待实测` 未使用；卡面 16 列 × 128px、数据书 224px、剧情框 240px 的实际折行未验证。
3. **nsfw 侧卡面 `.desc` 值尾 `\n`**：`CosmoCardBigbold/Dragon/Elf/Enelye/Squeaker/Starkill/Swiper.desc` 共 13 行，中文值尾带 `\n` 而英文源无。可能是构建层表示差异，也可能是值的一部分（若渲染器当作换行，会使卡面多一空行，Bigbold 第 2 段正好 14 段 + 1 行 = 15 行，压在上限）。无法在不构建、不实机的前提下判定，**未立案**，请主代理裁是否转系统层核查。
4. **行尾空格只对提案行核过**：只核了 9 条发现所涉行的英文源行尾（均无行尾空格，中文亦无）。其余 290 行未逐行走 `occurrence_id → unit_id → catalog/units.jsonl.source`，因此「中文行尾空格是否为英文镜像」在全批层面**未逐行证明**（按口径本也不报）。
5. **按键名与手柄实际图标**：`input.xinput` 中文侧（摇杆反下、肩键、L/R 扳机、指南键）与实际手柄渲染／图标是否对应，本工单不能证明。
6. **`ui.data` 双关与文笔类未报项**：`f_AgentF07` 的 `SPOTTY`（有斑点／时好时坏）、`f_ClassicBossRedbull` 的 `BOUNCY BOON`（「会弹的好处」）、`ui.end.Tier3` 的 `NATURAL` 与 `HOTSHOT` 同作「高手」——本路判断为「无更优且不增信息的改法」，retain，留作主代理交叉核验时的参考，不构成缺陷主张。
7. **未执行**：未跑构建／回归／17 步 CPU 流程，未改台账、归档或译文库，未启动游戏，未读其它批次或另一路产物。
