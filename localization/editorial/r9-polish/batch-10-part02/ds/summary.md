# batch-10-part02 精校提案摘要（路线 ds）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-10-part02/orders/batch-10-part02.reader.md`（1,432 行） |
| 结构化同源 | `orders/batch-10-part02.json`（98 场／401 行，与 reader 逐条一致） |
| 参照 | `orders/reference-excerpt.md`、`orders/ORDER.md` |
| 实际读完场景 | **98／98（read_status 全为 `read_full`）** |
| 覆盖行 | 401／401 |
| 精校对象范围 | `/patchDictionary/navmap*`、`navmap.AreaE/menu`、`input.gdx*`、`ui.achievement.*`、`ui.backers`、`ui.breeding.*`、`ui.card.*`、`ui.cheats*`、`ui.data*`（含 `ui.data` 名录）、`ui.defeated`、`ui.end.BadEnding/Tier1/Tier2`、`ui.item*`、`ui.options.*`、`ui.presetcheat.*`、`ui.save*` |

结论分布：`issues_found` 4 场，`retain` 94 场，`needs_evidence` 0 场，`partial`/`not_read` 0 场。

## 二、发现（共 4 条）

| severity | 条数 | finding_id |
| --- | --- | --- |
| A | 1 | P10-0201 |
| B | 1 | P10-0202 |
| C | 2 | P10-0203、P10-0204 |
| needs_evidence | 0 | — |

按 root 归组：

| root | 条数 | 说明 |
| --- | --- | --- |
| `ui.data.m_ClassicWerepup` | 1（A） | 战败/回忆卡说明后半句无原文对应、前半核心动作漏译 |
| `ui.data.exit` | 1（B） | 退出项用「兽鉴」，与本批 `ui.item`/`ui.save` 的「兽类图鉴」不一致 |
| `/patchDictionary/navmap.AreaB` | 1（C） | `EASTERN PASSAGE` 作「东方通道」，与同 root 的 EAST→「东部」体系不一 |
| `ui.breeding.Squeaker.affinity` | 1（C） | 「你来他就来精神」双「来」，断句歧义 |

结构类检查（`format`）**无发现**，逐项核对结果：

- `|` 段数：401 行中 98 行含 `|`，逐行比对 source 与 current 段数**全部一致**（卡面三行、卡面说明 14 段、成就提示两段均未错位）。
- 保护标记：`_`／`$`／`[` `]`／`<` `>`／`*!`／`--------` 计数逐行一致；坐标（`109, 088` 等 14 行）数字与逗号后半角空格全部原样；按键名（`R2`／`L1`／`TRIANGLE`／`START/OPTIONS`／`DPAD UP`／`L STICK LEFT` 等）未改；`POV`／`LECT` 类原形保留。
- 行宽：所有 `|` 分段最宽 16.5 全角格（上限约 20），无越界。
- 空行：`ui.end.BadEnding`／`ui.end.Tier1` 的空 source 与空 current 成对存在（共 12 组），未报漏译。
- 空译检查：全批无「source 非空而 current 空」的行。

## 三、高风险连续段（改造所需注意事项）

1. **`ui.options.confirmCheat`（8 行合句）**：中文按汉语语序把 `MAKING ANY CHANGES TO THE`（对当前作弊菜单设置）与 `CURRENT CHEAT MENU SETTINGS`（进行任何更改）两行内容互换位置，合读为「警告：对当前作弊菜单设置进行任何更改，都将重置游戏，以应用新设置。任何未保存的进度都将丢失！」——信息不增不减，**不作缺陷**，但落地时必须整段一起改，逐行改会打断合句。
2. **`ui.end.Tier1`（4 行＋RANK）**：`NOT BAD FOR`→「对新手来说」、`TRAINEE`→「见习」（与 `ui.end.Tier2` 的 `PRIVATE`→「列兵」同为 RANK 行位）、`BEGINNER !`→「还不错！」，同样是整句重排；按行孤立比对会误判为错位，**已按整段核过、不提案**。
3. **`ui.end.BadEnding`（9 行）**：`TRAEH IS`／`STILL OUT`／`THERE...` 三行合读为「Traeh 还在外面……」，居中空格随原文，属排版装置。
4. **卡面说明 14 段组**（`ui.card.CosmoCardBarker/Pigobin/Wyvern/Kobold/Elf/*.desc`）：段数与英文一致但**分段边界常重排**（如 `就它们|看来，`、`种族。就它们|看来，`），改动必须整段重排、不得单段替换。
5. **`ui.breeding.*.affinity`／`.needs` 三行组**：同一物种四个状态行共用同型英文句式，四条中文必须保持同一句式模板，否则会读成不同物种不同口吻。
6. 本 part **无无线电套语、无问答错位**（`MauserHints` 只在 part01/03 出现）。

## 四、男女两版（nsfw／sfw）不一致清单

| 类型 | 内容 | 判断 |
| --- | --- | --- |
| 同名源字符串中文 | 用脚本比对：全批同一 `source` 的中文**完全一致**，无版本间措辞漂移 | 无需处理 |
| 条目集合 | `ui.item`：nsfw 有 `POCKET BREED`／`BESTIALIARY`；sfw 有 `POCKET TRAIN`／`MEMORIES` | 英文本身不同条目，不互推；`POCKET BREED`→「口袋育种」与 `POCKET TRAIN`→「随身训练」前缀处理不同（口袋X／随身X），属可观察到的命名不齐，因两侧不见同一界面，本批不提案 |
| 成就 | `die_low` 仅 sfw；`die_15`／`die_18` 分属不同场景 | 无对照需求 |
| 结局分级 | `ui.end.Tier1` 仅 sfw、`ui.end.Tier2` 仅 nsfw | 两版分级文案不同步设计，逐行独立核过 |
| 名单 | `ui.backers` nsfw 源无居中空格、sfw 源自带；中文两侧都有空格 | 居中镜像，按 ORDER §四.13 不报 |
| 卡面行尾 | 卡面 `.desc` 的 nsfw 源**不带**行尾换行符、sfw 源**自带**；两侧中文都带 | 属英文件不对称，中文两侧一致，不报（见第六节） |

## 五、已考虑但不提案的判点（供裁决核对）

1. **卡面名字与 `<类别>` 之间的对齐空格**：`DRAGON   <ALPHA>`→`龙  <阿尔法>`、`KOBOLD   <FAUNA>`→`科博德  <动物>`、`WYVERN   <FAUNA>`→`双足飞龙  <动物>` 比英文少 1 个空格（其余四条一致）。中文字宽与拉丁不同，英文按第 9 列对齐，中文各行落点本就不同（4/5/6/7/8/10/13 格），补空格也换不来对齐，属对齐镜像，按 ORDER §四.13、参照摘录 §六 不报。
2. **`knot` 在本批只出现一次，作「结」**（`ui.card.CosmoCardBarker.desc`：「结的大小也舒服」）。同族卡面 `ui.card.CosmoCardDwarf.desc`「即便结已充血」、`ui.card.CosmoCardWerehund.desc`「会以类似结的方式充血」均用「结」；对话侧已落地「肉结」。卡面族内一致优先，故不改，也不把对话侧的「肉结」机械复制到卡面。
3. **`nubbed penis`→「带肉突的阴茎」**（Kobold 卡面）：语料中「肉突」（vsn 线）与「凸粒」（R9 已落地 nubs＝凸粒）并存且分工不明，无单一口径可比，不提案。
4. **`FENFEN` 的「芬芬」**：`ui.card.CosmoCardStarkill.desc`（SFW8850daec499cc9858fb446c9）是**全批唯一**「芬芬」写法，其余同批均作 `Fenfen`（库内 `Fenfen` 124 处）。FENFEN 中文名未终裁，按派单口径**不提案、不新造**，仅在此备案：该行是待裁项的落点。
5. **`TRAEH`／`SEVAW`／`ERAUQS`**：`Traeh`／`Sevaw`／`Erauqs` 原形保留，未动（R3 裁决）。
6. **`GEPARD`→「猎豹」**：与 `character-names.json` 终裁完全一致（`old_forms: 格帕德`），不重提。`BIGBOLD1/2`→「大壮兽1/2」已本地化，非缺口。
7. **`LEFT CLICK`／`RIGHT CLICK`→「左摇杆按下」／「右摇杆按下」**：参照摘录 §一.5 明列「右摇杆按下」为既有对应，视为既定，不改。
8. **`LOVEBUSTER`→「爱破者」**：语料孤例（全库仅此一处），按构词顺序直译并用引号标注绰号，无第二处可比，不提案。
9. **按键名中文化现状**（`CIRCLE`→圆圈、`CROSS`→十字、`DPAD UP`→方向键上 等）：与参照摘录 §一.5 的既有对应表一致，本批 `input.*` 54 条内部自洽（肩键／扳机／摇杆／方向键体系一致），不改。
10. **`ui.presetcheat.no_falling_debris`**「阻止不稳定区域随机掉落的碎石」略拗口，但语义（stop random debris falling in unstable areas）成立，属可改可不改，未凑数提案。
11. **`ui.data.m_ClassicBigboldV2`**`WINDING CHASE`→「漫长追逐」有轻微词义漂移（曲折≠漫长），不影响理解，不提改。

## 六、跨版本/跨轮观察（不改，只备案）

- 卡面 `.desc` 的 nsfw 侧 current 行尾比 source 多一个 `\n`（10 行），而 sfw 侧 source 本身即带 `\n`、中文与之一致。也就是说**中文两侧写法一致，英文文件两侧不一致**，属源侧不对称，不作缺陷提案。
- `结`（卡面说明族）与 `肉结`（对话族）的分工是跨批历史形成的，若日后要统一，应整族改（卡面另有 2 处：Dwarf、Werehund），不宜只改本批这一行。
- `兽类图鉴`／`兽鉴` 的用词分裂来自 R1 草稿期，本批 `ui.data.exit` 是唯一落点，故 P10-0202 只改这一行；若 jar 侧另有一份 `ui.data.exit`，须同时改。

## 七、未覆盖项与本工单不能证明的东西

- **未覆盖项：无**（98 场全部 `read_full`，401 行全部逐行核过）。
- **本工单不能证明**：
  1. **实际显示行序**。工单 JSON 的 row 顺序是 `row_id` 排序，不是 dictionary 键序／屏幕行序。`ui.options.confirmCheat`、`ui.end.Tier1/Tier2`、`ui.end.BadEnding` 这类多行合一单元的「合读是否通顺」只能按内容一一对应核实（信息不增不减），**无法证明屏幕上的实际行序**，故这几处一律不按「错位」提案。
  2. **改动后的实机版面**。本次未跑构建、未跑回归、未启动游戏；P10-0202 由 6 字增至 8 字（96px），估算仍短于英文行宽，属静态推算，未实测。
  3. **两侧 navmap 的另一半**。P10-0203 涉及 `navmap.AreaB`；patch 侧（本 part）与 jar 侧（`datav/dictionary.json#navmap.AreaB.east_exit`，不在本 part）必须一起改，jar 侧条目未在本工单内，无法在此覆盖。
  4. **未终裁项**：FENFEN 中文名、`LIGHTTAZER` 中文名、引号体例（`“”`／`「」`）、CJK 与拉丁间距体例，本批按口径一律不提案。
  5. 界面文本无语境音频/说话人，`voice`、`relationship` 类判点在本批基本不适用；本批所有发现均不涉及玩法条件、施受关系、数量或揭示顺序。

## 八、产物

- `localization/editorial/r9-polish/batch-10-part02/ds/findings.jsonl`（4 行）
- `localization/editorial/r9-polish/batch-10-part02/ds/coverage.jsonl`（98 行，无重复 scene_id）
- `localization/editorial/r9-polish/batch-10-part02/ds/summary.md`（本文件）
