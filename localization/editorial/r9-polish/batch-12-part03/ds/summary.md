# batch-12-part03 精校小结（DS 路）

## 一、输入与实际读完

| 文件 | 行数／规模 |
| --- | --- |
| `orders/ORDER.md`（规范） | 89 行 |
| `orders/reference-excerpt.md`（口径与既有写法） | 95 行 |
| `orders/batch-12-part03.reader.md`（正文） | 1,009 行、158 场、218 行 ROW |
| `orders/batch-12-part03.json`（结构化同源） | 3,925 行、158 scenes |

- **实际读完：158／158 场**，`read_status` 全部 `read_full`。分段读（reader 1–340／341–680／681–1009 行），每段读完即落盘 coverage 与 findings，三段合计与 JSON 逐行核对过 `scene_id`、`row_ids`、`source`／`current`。
- 场景结果分布：`retain` 142、`issues_found` 15、`needs_evidence` 1。
- 覆盖做法：`row_id → occurrences.jsonl → unit_id → units.jsonl.source` 反查英文行（CAT: 前缀 171 行可解析，本批除 SpecialFap.OmegobinBuff 为 `patch` 外全部 `archive=jar`）；47 行 `SFW…` 行在 `occurrences.jsonl` 无记录，按派单口径改用工单 JSON 的 `source`。行尾空格判据只按英文 `source` 行尾，未使用 `occurrences.trailing_ws`（中文列）。

## 二、发现分布（共 8 条）

| 严重度 | 条数 | finding_id |
| --- | --- | --- |
| A | 0 | — |
| B | 4 | P12-0302、0303、0304、0306 |
| C | 3 | P12-0301、0305、0307 |
| needs_evidence | 1 | P12-0308 |

类别：`term` 4（0302、0303、0304、0306）、`format` 2（0301、0305）、`idiom` 1（0307）、`source_uncertainty` 1（0308）。

按 root 归组：

- **任务日志面** `/missionLog/*`：2 条，覆盖 10 行
  - P12-0301 行尾空格（female/3、female/6、male/4、male/7、male/9 的 `text`，同一判点合并为一条，`note` 给出其余 4 行的完整替换值）
  - P12-0302 异常等级名留拉丁（male/6、male/7、male/9 `header`，关联词典 `AnomalyBeta`）
- **词典面** `datav/dictionary.json`：6 条
  - P12-0303 `CosmoBody`／STARSUIT＝星装（道具名与「宇宙服／科博服」系列不一致）
  - P12-0304 `LuckyBodyNotUpgraded`／GET A FEELING|SO COMPLICATED（男／女两版两种写法）
  - P12-0305 `SpecialFap.OmegobinBuff` 标签行尾多一个空格（英文行尾无空格；sfw 侧英文自带空格属镜像，不动）
  - P12-0306 `SpecialHookshot`／UP+ATK 被译成「上+攻击」（按键名不是术语）
  - P12-0307 `StatFortune`／SOFT & CREAMY 译「又软又腻」（褒义口感被译成「腻」）
  - P12-0308 `StatPretzel`／HARD KNOTTED|BRED 原文可疑（BRED／BREAD）
- `/shops/male/Area0_Macsen1/products/2/displayName`：0 条（OLD JUNK＝旧杂货，男女两侧一致）。

结构自检（脚本核过）：所有提案 `|` 段数与英文相同；逐段字符数均 ≤ 英文字符数；提案无行尾空格；行前缀结构、数字、`+`、`G+`、`X-`、`UP+ATK`、`P-` 类标记与问号/省略号都没动；未改任何 `root` 键名，未新增/删除物理行。

## 三、高风险段

本批全是界面短标签与任务日志字段，**没有剧情对话、没有无线电套语、没有合句断点与问答错位**，所以那三类风险在本批不存在，不需要在这里找。真正的风险点转移为下面三处：

1. **固定列宽标签的行尾空白**（P12-0301、0305）：样板行与满行标签一旦带尾随空格，右缘会顶到相邻列；同时这里最容易按「中文列 trailing_ws」误判，本批坚持只对英文行尾。
2. **键名与属性名混用**（P12-0306）：`UP+ATK`（键名，保留拉丁）与「+3 ATK」→「+3 攻击」（属性名，译中文）是两种语境，同一批里同时出现，容易被「统一」错改。
3. **跨面体例 vs 单点误译的边界**（见下节待核）：ZENER 形状名在词典面用「星星／三角／圆圈／十字／方块／波浪」、在任务日志面用「星形／三角形／圆形／十字／方形／波」，两套各自内部一致，按体例处理而不是逐条改。

## 四、男女两版（nsfw／sfw、datadm／datadf）不一致清单

| 英文 | 一侧 | 另一侧 | 处置 |
| --- | --- | --- | --- |
| GET A FEELING\|SO COMPLICATED | nsfw「涌起的感觉\|复杂难言」 | sfw「涌上一种\|复杂的感觉」 | **已提案** P12-0304（取贴合原文的 sfw 方向） |
| UP+ATK WITHOUT\|PSY ABILITY ON | nsfw「上+攻击，且\|精神能力未开」 | sfw「未开启精神能力时\|按UP+ATK」 | **已提案** P12-0306（键名保留拉丁） |
| ACQUIRED ANOMALY ALPHA/BETA/GAMMA/OMICRON | male「已获得异常 X」 | female「已获取异常体 X」 | 未提案：female 侧 4 行不在本批；另有 8 行 header 的字母写法差异见 P12-0302（需一并裁决，否则会留下 male 中文／female 拉丁两种） |
| FENFEN | nsfw「Fenfen」 | sfw「芬芬」 | 未提案：FENFEN 中文名未终裁，按派单口径不新造、不按一股改另一股 |
| A WEAPON FOR VIRGIN AGENTS / NEW AGENTS | nsfw「给童贞特工\|用的武器。」 | sfw「新特工\|使用的武器。」 | 不算不一致：两侧**英文原文本来就不同**，各自译文都对 |
| BIG AND SPICY JUST FOR YOU! / BUT ADDICTIVE! | nsfw「又大又辣\|专给你的！」 | sfw「个大味辣\|却让人上瘾！」 | 不算不一致：英文不同源 |
| STARSUIT | nsfw 星装 | sfw 星装 | 两侧相同，问题在系列体例，见 P12-0303 |

其余 9 组同名两侧（ElfHead、PirateHead、PsyCoffee、SpecialPowermark、SpecialWhistle、TazerAttuned、StatPepper 等）逐字相同，无跨侧问题。

## 五、待核项（本批不提案，交上游裁决）

1. **术语表与语料冲突（已按语料处理）**：`reference-excerpt` §三 写「torch＝手电」，但库内该道具 20+ 行一律作「手电筒」（TomcatItems、AreaC_MacsenDark 等），且剧情明确区分「手电筒」与墙上「火把」。本批 `SpecialTorch`／TORCH＝手电筒 保留，未改成「手电」（ORDER §11：摘录与语料冲突时以语料为准）。同理 `hookshot＝钩爪` 与语料一致，无冲突。
2. **ZENER 形状名跨面体例**：词典 ZenerStar/Triangle/Circle/Cross/Square/Waves＝星星／三角／圆圈／十字／方块／波浪；任务日志 header＝泽纳星形／三角形／圆形／十字／方形／波。两套各自一致，属体例而非单点误译，本批未改任何一条（含 `ZenerCircle` 与 `ACQUIRED ZENER CIRCLE`）。
3. **异常等级名方向**：P12-0302 取中文方向（中文 12 行 vs 拉丁 8 行）；若上游判定任务日志面应当留拉丁，则应撤本条并反向统一词典 4 条与卡面 8 行，不能只改一侧。
4. **`Traeh-XE`**：按 R3／派单口径现状不动，未提案。
5. **`HARD KNOTTED|BRED`**：原文 BRED 疑为 BREAD 错拼或双关，记 `needs_evidence`，未擅改。
6. **`F COOKIE`＝福饼干**：两侧写法一致，但库内没有第二处出处可校；未凭印象改成「幸运饼干」。
7. **`OLD JUNK`＝旧杂货**：库内无同名 `ui.item` 条目可直接比对（只有 `TazerAttunedNotUpgraded` 的 `JUNK`＝废品），无法证明二者是同一件货，故不动。
8. **6 行中文值带尾随换行**（female/10、male/10 的 `Stub: Mauser bio`，female/18、male/18 的 `Line 1…`，female/15、male/15 多行样板）：英文无对应换行，但判据只覆盖「行尾空格」，本批不处理，仅记录。

## 六、未覆盖项与「本工单不能证明的东西」

- **没有入台账、没有构建、没有实机**：本目录只产出提案；未写 `localization/translations/zh-CN.jsonl`，未跑 `build_candidate.py` / `test_candidate.py`，未启动游戏，未验证安装、存档与实机显示。
- **列宽是按字符数近似，不是像素实测**：所有「长度不超英文」都用逐段字符数核对；卡面 16 列 × 128px、数据书 224px ≤3 行等容器约束没有实测，若某些短标签是等宽/像素排版，仍需渲染侧复核。
- **两侧归档层（jar／pak）未直接对照**：本批 occurrence 除 `SpecialFap.OmegobinBuff`（`patch`）外全部落在 `jar`，无法在批内比对「同一标签 jar 与 pak 各一份」的差异；文中的「两侧」实际指 nsfw／sfw 变体行。
- **语料计数口径有限**：频次统计基于 `snapshot-03` 的 `current_line`（13,494 行），不是全库 2,989 场全文本；摘录表里的条数（如 ZERONIA 20、AYSKAMMR 12）沿用摘录，未另行复算。
- **未触及的相邻文本**：female/6～9 的 `ACQUIRED ANOMALY …` header、剧情行「星际服」（CAT:O7680fc134078537c5d92）、`SpecialTorch` 的 nsfw 孪生行、`TazerAttunedNotUpgraded` 的 `JUNK`＝废品 等均在本批范围外，只在必要处作为证据引用，未提案。
- **按口径明确不报的类型**：`LIGHTTAZER`（本批无该条目）、`FENFEN` 中文名、引号体例（「」与“”并存）、CJK 与拉丁间距体例、英文原文自带的排版镜像空格。这些不等于「已确认正确」，只是全局待裁或本批不处理。
