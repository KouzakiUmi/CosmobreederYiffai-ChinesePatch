# R9：全正文系统精校（第 1 轮）

本轮把 R1 粗校／R2 修复之后的**全文系统精校**真正开跑：对照英文重写中文，而不是只挑错词。方法口径沿用 [R1 中文重写方案](../r1/TRANSLATION_PLAN.md)，落地沿用来源锁定台账与候选构建链。

## 一、输入基线

| 项 | 值 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 快照 | 基线候选 | 场次／行 | 用途 |
| --- | --- | --- | --- |
| `snapshot-01` | candidate4 | 2,966／13,400 | 已过期，R1 使用 |
| `snapshot-02` | `r8-puzzle-candidate12` | 2,968／13,406 | batch-01 |
| `snapshot-03` | `r9-polish-candidate13` | 2,989／13,494 | batch-02 起 |

快照均用 `r1/tools/prepare_corpus.py --candidate <build> --output <snapshot>` 生成，状态 `prepared_not_semantically_reviewed`；`current` 是对应候选的实际显示行，不是初翻草稿。批次工单用 `tools/build_batch.py <batch> --snapshot <name>` 生成，工单里记录套用的快照与基线候选。

## 二、双路设置（按用户指派，不使用 ACP）

| 路 | 路由 | 档位 | 说明 |
| --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash` | `tiered`（自适应） | 非 ACP 入口；`antigravity-acp` 在本轮禁用 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash` | `high` | OpenDesign 套餐路由（DS(OD)） |

两路拿到完全相同的工单与参照，独立出提案、互不通信；主代理负责交叉核验、裁决与台账。

## 三、批次

批次优先级按 [TRANSLATION_PLAN](../r1/TRANSLATION_PLAN.md) 第八节。

| 批次 | 范围 | 场次 | 行数 | 字符 | 状态 |
| --- | --- | --- | --- | --- | --- |
| batch-01 | `The0`、`Area0_Macsen1/2/Bar`、`Area0_Prison1`、`MauserHints_AreaA` | 137 | 358 | 23,277 | 已并入 candidate13 |
| batch-02 | `Tomcat` | 56 | 566 | 36,041 | 已并入 candidate15 |
| batch-03 | `Bossu` | 53 | 437 | 29,033 | 已并入 candidate14 |
| batch-04 | `Mauser` | 81 | 871 | 58,922 | 已并入 candidate16 |
| batch-05 | `BossuDex`（图鉴） | 149 | 1,253 | 83,198 | 分 3 个 part，依次并入 candidate17／19／18 |
| batch-06 | `TomcatItems`（道具） | 260 | 1,753 | 117,974 | 分 4 个 part，依次并入 candidate20／19／23／21（最终 candidate24） |
| batch-07 | `vsn/*` 结局与开场（结局与平行版本） | 23 | 776 | — | 分 2 个 part，依次并入 candidate25／26 |
| batch-08 | `vsn/*` 剧情场景脚本 | 78 | 2,356 | 197,641 | 分 5 个 part，依次并入 candidate27／28／29／30／31 |
| batch-09 | 区域场景与条件分支（关卡救援与分支） | 913 | 1,597 | 115,212 | 分 4 个 part，依次并入 candidate32／33／34／35，**4 个 part 全部完成** |
| batch-10 | 界面与系统文本（UI 与其他） | 295 | 1,159 | 50,366 | 拆 3 个 part（98／98／99 场），依次并入 candidate36／37／38，**3 个 part 全部完成** |
| batch-11 | 其余零散条目（战败提示与失真广播） | 109 | 505 | 24,187 | 1 个 part（`DefeatHints` 72 场、`Starkill` 21 场、`Static` 16 场），并入 candidate39，**完成** |
| batch-12 | 界面与系统文本（未覆盖的词典与任务日志） | 473 | 650 | 19,581 | 拆 3 个 part（157／158／158 场），依次并入 candidate40／41／42，**3 个 part 全部完成** |
| batch-13 | 毛鼠旁白提示（`MauserHints`） | 50 | 183 | 12,066 | 1 个 part（`Area0` 14、`AreaB` 12、`AreaC` 10、`AreaE` 8、`AreaH` 2、无后缀 4），并入 candidate43，**完成** |
| batch-14 | 补漏：batch-01 只定义未出单的 21 场 | 21 | 88 | 3,362 | 1 个 part（AreaA 提示 9、The0 9、Area0 三处 3），并入 candidate45，**完成** |
| batch-15 | 术语与按键名残留清理 | —（清理批，不新增覆盖） | 325 行工单／24 行待改 | — | 扫描两个归档定位，采纳 15／驳回 9，并入 candidate44，**完成** |
| batch-16 | 专名统一：FENFEN | —（清理批） | 3 | — | 对白 1＋物品值 2，并入 candidate46，**完成** |
| batch-17 | 术语补漏：干员、LIGHTTAZER | —（清理批） | 13 | — | 干员 8＋LIGHTTAZER 5，并入 candidate47，**完成** |
| batch-19 | 中文引号：直引号换全角 | —（排版批） | 27 | — | 引号内含汉字才换；纯拉丁保留，并入 candidate48，**完成** |

批次定义在 `tools/build_batch.py` 的 `BATCHES` 里，按 root 列出；`batch-07` 起按 R1 方案第八节的优先级 5（结局与平行版本）和 6（其他风格与文笔）排。`batch-07`／`batch-08` 的场景 `kind` 是 `vsn`、`batch-10`／`batch-12` 是 `ui`，所以 `BATCHES` 的条目可以带第三个元素指定 `kind`；不写时默认 `dialogue`。`batch-12` 还有第四种形状：条目第二元素写 `None`，改用 `logical_path` 选资源、再用 `exclude_covered` 扣掉别的批次已占的场次——它的文本散在词典与任务日志里，没有共同的 root 可列。

batch-07 及以后尚未全部出工单：`ORDER.md` 与 `reference-excerpt.md` 需按批手写（模板见 `batch-07-part01/orders/`），`reader.md` 与 `.json` 由 `build_batch.py` 生成。

每批工单在 `batch-NN/orders/`：`ORDER.md`（规范）· `batch-NN.reader.md`（正文）· `batch-NN.json`（结构化）· `reference-excerpt.md`（本批人物与术语摘录，按批重写）。

## 四、工单硬约束（摘要）

- `proposed_zh` 是完整物理行，前缀、缩进、方括号、`@DerekChipReport`、`<3`、数字与频率原样保留。
- 不增删物理行；跨行重分配只写 `note`，由主代理裁决。
- 剧情框 240px／12px 字，单行正文建议 ≤ 约 20 个全角字。
- `current` 为空的 ROW 是既有合句尾行，不报漏译，也不能直接填充（台账拒收空→非空）。
- 已裁决项（R3 人名、R6 术语、R8 谜题提示）不得重提。
- 提案不得让任何行由 ≤3 行折行变成 >3 行；反向也成立：既有 >3 行的合句行，本批应借机压回 3 行（batch-02 的 3 处 4 折行即此例）。

## 四之二、两路裁决的经验

三批下来，两路的可靠性差异不在发现数量，而在**方向**：

- 术语类提案里，「把少数写法改成多数写法」两路都可靠；「把多数写法改成术语提案里的写法」需要先有全库终裁，否则只会多出一种写法（`LIGHTTAZER`）。
- 已经 R2 裁决过的语用点（`torch` 英美异称、`agent` 取「特工」）会被后到的模型反复重提。裁决时以既有裁决为准，并要求提案带新证据才重开。
- 两路各自的「误判为 A」集中在把解释性改写当成误译；A 级只认能指到具体英文词、否定、数量、施受或结构的那种。

## 四之三、主代理补的发现

三批共补 21 条 `R9M-*`（batch-01 3 条、batch-02 2 条、batch-03 16 条），绝大多数是「同文的姊妹行」：工单要求每条发现只挂本场 row，同文异场的位置只能写进 note，落台账时按 row 逐条展开。批量落库后再回读归档核对，是发现这类遗漏的唯一可靠办法。

## 四之四、参照摘录写错会让两路一致地错

batch-04 里两路都要求把「反重力脚环」改成「反重力踝环」，提案质量很高：行数齐、理由足、覆盖 4 个 row。但方向是反的——UI 道具名就是「脚环」，正文也是「脚环」多。

根源是我在 `reference-excerpt.md` 里把 `anti-grav anklet` 定为「反重力踝环」。两路照做，交叉核对也发现不了，因为**两路错得一样**。

教训：参照摘录里的每一条术语都要先回查全库用法与 UI 名，再写进工单；写错比不写危害更大，它会把两路的一致性变成一致错。

## 五、流程与产物

1. `tools/build_batch.py <batch> --snapshot <snap>` 生成批次工单（可复现，带 corpus manifest SHA 与基线候选）。
2. 两路各自写 `batch-NN/gemini|ds/{findings,coverage}.jsonl` 与 `summary.md`。
3. `tools/verify_batch.py <batch>` 做结构核验（覆盖、row 归属、前缀与标记守恒）并输出 worksheet；`tools/measure_width.py <batch>` 用真实 12px 字形表实测折行。
4. 主代理逐条核验后写 `batch-NN/review/decisions.tsv`；`tools/build_ledger.py <batch>` 生成该批来源锁定台账并 dry-run，`tools/verify_round.py <batch>` 出 gate。
5. 在 `localization/optimization/r28/r9polish/component.json` 的 `batches` 数组登记该批（台账／gate／decisions 三项），再构建候选与跑 17 步回归。

## 五之一、排版层复核（2026-11-03）

`tools/audit_containers.py` 用真实字模逐个量了硬切容器：角色卡 96 个值、成就 60 个、数据书／结局数据块 200 个，**0 个超限**（卡面按 15 行算——原版英文背面本身就是 13–14 段）。合句留下的 1,709 个空尾行里，1,701 个中文超过 240px、由 `StoryFont12` 自动折成两行填满，8 个是 `DefeatHints` 的短提示（228–236px，一行放得下，第二行空着也不接续对话）。所以排版层没有必修项，判据与数字见 [LEFTOVERS](LEFTOVERS.md) 第三节。

## 五之二、逐批合计（batch-01～11，二十六批）

裁决／采纳／驳回／留置／主代理补五行由各批 `review/decisions.tsv` 逐表重算（2026-11-03）。本表只统计 batch-01～11 这二十六批；batch-12／13 的裁决另见下一小节。旧表把部分 `R9M-*` 行算进了「裁决」而没算进「采纳」，因此旧合计 812 与三列之和 800 对不上；重算后 649＋283＋39＝971，与「裁决」一致。历史批次的 `两路发现` 保留当时的记录值。

batch-10 三个 part 只有 DS 一路：Gemini 路在本批连续六次失败（读完整批却不落盘、也没有收尾消息），故 `两路发现` 记 `0＋N`，缺陷覆盖由 DS 一路加上主代理的机械扫描（行尾空格、`|` 段数、纯 ASCII 未译行）承担。



| 项 | -01 | -02 | -03 | -04 | 05-p01 | 05-p02 | 05-p03 | 06-p01 | 06-p02 | 06-p03 | 06-p04 | 07-p01 | 07-p02 | 08-p01 | 08-p02 | 08-p03 | 08-p04 | 08-p05 | 09-p01 | 09-p02 | 09-p03 | 09-p04 | 10-p01 | 10-p02 | 10-p03 | 11 | 合计 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 场次／行 | 137／358 | 56／566 | 53／437 | 81／871 | 49／419 | 50／419 | 50／415 | 65／434 | 65／441 | 65／437 | 65／441 | 11／385 | 12／391 | 15／452 | 16／470 | 15／483 | 16／502 | 16／449 | 228／402 | 228／398 | 229／399 | 228／398 | 98／459 | 98／401 | 99／299 | 109／505 | 2,154／11,631 |
| 两路发现 | 18＋22 | 63＋71 | 44＋38 | 22＋39 | 13＋33 | 28＋23 | 20＋27 | 4＋31 | 28＋23 | 32＋28 | 9＋24 | 3＋33 | 12＋18 | 21＋29 | 1＋26 | 0＋8 | 2＋7 | 5＋28 | 11＋24 | 4＋14 | 19＋23 | 9＋18 | 0＋7 | 0＋4 | 0＋9 | 0＋11 | 935 |
| 裁决 | 35 | 38 | 35 | 40 | 56 | 55 | 56 | 38 | 55 | 62 | 35 | 38 | 30 | 53 | 28 | 25 | 36 | 50 | 47 | 21 | 56 | 32 | 11 | 8 | 17 | 26 | 971 |
| 采纳 | 32 | 24 | 28 | 19 | 41 | 26 | 36 | 28 | 30 | 41 | 20 | 32 | 23 | 24 | 25 | 24 | 32 | 27 | 24 | 15 | 24 | 17 | 10 | 8 | 14 | 25 | **649** |
| 驳回 | 2 | 11 | 5 | 14 | 11 | 27 | 18 | 8 | 11 | 19 | 14 | 4 | 7 | 26 | 2 | 0 | 3 | 23 | 23 | 6 | 32 | 15 | 1 | 0 | 1 | 1 | 283 |
| 留置 | 1 | 3 | 2 | 7 | 4 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 3 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 39 |
| 主代理补 | 3 | 2 | 16 | 1 | 6 | 4 | 1 | 3 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 17 | 26 | 0 | 0 | 3 | 14 | 5 | 0 | 0 | 0 | 0 | 152 |

### batch-12／13 的裁决

| 项 | 12-p01 | 12-p02 | 12-p03 | 13 | 小计 |
| --- | --- | --- | --- | --- | --- |
| 场次／行 | 157／213 | 158／219 | 158／218 | 50／183 | 523／833 |
| 两路发现 | 0＋11 | 10＋11 | 8＋7 | 12＋13 | 72 |
| 裁决 | 20 | 29 | 23 | 42 | 114 |
| 采纳（含机械条目） | 14 | 13 | 12 | 17 | 56 |
| 驳回 | 6 | 16 | 11 | 25 | 58 |
| 留置 | 0 | 0 | 0 | 0 | 0 |

batch-12-part01 同样是 DS 一路（Gemini 试水第八次失败）；part02／part03 与 batch-13 的第二路改用 Grok 4.7，三批都正常收尾。

batch-12／13 的驳回比例明显高于早期批次：两路（或一路＋机械扫描）常常指向同一行，只取一条落地，另一条记为重复——这类驳回不是判错，而是去重。跨面命名（Zener 形状词条名、STARSUIT、FENFEN）一律不提案、记入 [LEFTOVERS](LEFTOVERS.md)。

驳回率从 batch-01 的 6% 升到 batch-02 的 29%、batch-04 的 35%，batch-06-part02 的 26%。驳回变多不等于审校变差：后期批次的驳回里有一大半是两路同报同一行、只取一路措辞，这类在早期批次里根本没被计数。真正判错的类型仍在变少。

batch-06-part01 的 4 条是 Gemini 路一整批的产量，而 DS 路两段合起来报了 31 条。同一个模型在不同批次上的产出量能差到一个量级，所以「两路一致」不能当作覆盖率的证据——真正的判据是每条改动有没有可指认的出处。

## 五之三、行尾空格的判据

这一族缺陷在 R9 里反复出现，也是最容易判反的一类，判据只有一条：**看英文原文行行尾有没有空格**。

三个来源的可靠性不同：

- `orders/batch-NN.json` 的 `source` 字段：多数行保留了原文行尾空白，但 `SFW` 一侧有被裁掉的情况，不能单独作准。
- `catalog/occurrences.jsonl` 的 `trailing_ws`：**这一列描述的是中文译文行，不是原文**。用它判断会得出「中英一致、都是镜像」的循环结论——batch-08-part03 的 DS 路就是这么判的，17 处真缺陷因此全部漏报。
- `catalog/units.jsonl` 的 `source`：按 `occurrence_id → unit_id` 查到原文，是这三者里唯一可直接对照的。原文行尾无空格而中文有，就是缺陷。

batch-08-part03 起一律用 `units.jsonl` 复核。同一批里 17 处为真缺陷、12 处为镜像，说明「整批都是镜像」或「整批都是缺陷」都不成立，必须逐行查。

已落地的 78 处行尾空格改动按此复核过一遍：76 处原文行尾确无空格，2 处因缺 `occurrence` 记录无法追溯，无需回退。

batch-09-part03／04 起改成「主代理先扫、两路各自报」：主代理用 [`tools/scan_trailing_ws.py`](tools/scan_trailing_ws.py) 按 `units.jsonl` 把整批的缺陷行一次列全（part03 15 行、part04 5 行），两路的同类发现只用来交叉确认。理由很直接——两路都会漏，也都会重复：part03 的 Gemini 报 13 行、DS 报 14 行，两个集合都不等于真值；把它们当覆盖证据会漏掉真缺陷。裁决表里这些行统一记 `R9M-<row_id>`，理由固定为「中文行尾多出半角空格，英文原文行尾没有」。

**界面文本要按 root 过滤这一族。** batch-10 的机械扫描会命中 `ui.end`（制作名单）、`ui.backers`（赞助者名单）与 `ui.card.*.desc`：前两者的中文行首行尾空格是居中装置（英文没有、中文加了对称空格），删掉会把版面推歪，按参照摘录第六节**不报不改**；`ui.card.*.desc` 的末段尾空格没有版面作用，按缺陷处理。这条过滤由主代理在裁决表里做，扫描脚本保持机械、不做语义猜测。

## 五之四、第二路的价值与代价

batch-06 四个 part 的第一版都用单路落地（对方要么读完整批却零落盘，要么还没收尾），之后逐个补第二路。补完之后 part01 从 8 条涨到 28 条、part03 从 6 条涨到 41 条、part04 从 6 条涨到 20 条。这些增量绝大部分是单路漏掉的真实缺陷，不是重复。

但第二路也会提坏改动。仅 batch-06 就出现三类：把已经改对的门卡指代再翻一次（三次）、把源文逐字加空格的排版镜像当缺陷、把限定词从句子里拆出去导致句子变成否定。判定这类只能靠回原文与回库内频次，不能靠「另一路也这么说」。

batch-09-part03／04 又补了三条，都是「方向」问题而不是「数量」问题：

1. **同一句在 jar 与 pak 两侧各一份**。batch-02 把 `Tomcat.Kobo` 的「狗头人」改成「科博德」，只改了 jar 侧；pak 侧副本照旧。本轮 part03／04 再遇到同句时，先查 `archive_entry` 与行号确认是不是姊妹行，是就各自单独落一条操作（`spacesuit`、`kobold`、`agent`、`hookshot` 四句都是这么处理的）。
2. **术语改动只能往库内多数写法靠，不能往少数靠**。batch-09-part02 曾把「电击枪」改成「电击器」（库内 92 对 10），本轮 part04 又按多数改回来。落台账前的固定动作是回库数频次，而不是相信某一路的理由写得漂亮。
3. **同一个词在不同变体里分叉时，先数变体再定方向**。`fancy chips` 在四个平行变体里三处作「花哨芯片」，因此 part04 驳回了「改成高级芯片」的提案——只改一处会让分叉变多，整句口径该另立裁决。

batch-11 的战败提示又添两条，属于「同一句话里哪层含义该留」的问题：

1. **亲属称谓按两侧分别写，不做统一**。Starkill 的提示在 `datadm` 与 `datadf` 两侧是镜像的（姐／弟），女线作「弟弟」、男线作「姐姐」看着不一致，实际是刻意的；任何"统一称谓"的提案都会把其中一侧改错。
2. **失真广播里的旧译名要认得出**。`Starkill` 的破损行里还留着「伊法」（Yiffai 的旧译），而这类行满是噪声体例（`KKZZT`、`SHHHZZZTER`），容易被当成演出装置放过。判据是 `character-names.json` 的 `old_forms`：只要命中旧名，就按错字处理，与噪声无关。

batch-12 又添一条，属于「同一句话在几个地方各存一份」的问题：

3. **界面条目可能有三份**：`datav/dictionary.json`（基础条目）、`datay/scripts_pack.json` 里 `/patchDictionary/...` 的运行时 overlay、以及任务日志自身的字段。batch-10-part02 按值反查把一条 navmap 地名改在了基础条目上，而该行真正的资源是 overlay；结果是基础条目变了、运行时读的那份没变。`r9_targets.py` 现在按 occurrence 记录的 `archive`／`archive_entry`／`location` 定位，只有查不到 occurrence 时才退回按值反查。这类「改了一处、另一处没跟上」的问题不会自己暴露——`verify_readback` 只证明台账里的操作落地了，不证明同一句话的其它副本一致。

操作上的两条教训已经落实：并发写同一个 findings 文件的代理必须各自一个文件名（part01 丢过一条发现，编号在裁决过程中还移过位）；裁决表引用某一路的 `proposed_zh` 时，必须在建台账之前重读该文件，而不是之前。

## 五之三、batch-05-part01 的两个教训

**一、参照摘录里的术语表是最高危的一行。** part01 摘录把 Squeaker／Spiker／Driller 写成「吱吱兽／刺甲机／钻掘机」，Gemini 老老实实按表执行，DS 没有照表而是去查游戏内名，才躲过去。语料实测 `datav/dictionary.json` 的条目名是「吱吱怪／刺虫／钻探者」（SQUEAKER 同源 16 处、FLAMER 作「喷火者」），三个「规范译名」在库里零出现。真正需要的不是「更聪明的模型」，而是**摘录里的每条术语都必须带出处行号**——没有出处的术语表等于把错了的常识写成规则。

**二、`BOSSU HERE` 不是 `roger`。** Gemini 把 `[BOSSU HERE, WHAT'S THE PROBLEM, AGENT?]` 改成「波苏收到」，「收到」对应 roger／copy that，而 HERE 是报明身份。这行真正的问题是译名替换留下的 `波苏 在此`（半角空格）。同类误判还有 `COME IN. BOSSU?`：源文带问号，现译「波苏，我进来了。」把呼叫写成陈述，抹掉了问句，也抹掉了下行波苏拿 come in 开黄腔的支点。

## 六、构建与回归

`r9polish` 组件按 `batches` 数组顺序应用各批台账。每批的 gate 绑定**它应用之前的那一个构建**（batch-01 绑 candidate12、batch-03 绑 candidate13、batch-02 绑 candidate14、batch-04 绑 candidate15、batch-05-part01 绑 candidate16），构建时逐批串行校验整资源 SHA：任何一批的基线漂移都会让构建直接失败，而不是悄悄覆盖。

| 候选 | 组件 | 台账 | 编译 | 17 步回归 |
| --- | --- | --- | --- | --- |
| candidate13 | 15 个（新增 `r9polish`），`full_component_set=true` | batch-01，32 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate14 | 同上 | batch-01 + batch-03，60 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate15 | 同上 | batch-01 + batch-03 + batch-02，84 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate16 | 同上 | 再加 batch-04，共 103 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate17 | 同上 | 再加 batch-05-part01，共 144 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate18 | 同上 | 再加 batch-05-part03，共 180 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate19 | 同上 | 再加 batch-05-part02，共 206 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |

candidate13 归档：jar `fb533645…61587`（45,842,131 B）· pak `046158e7…af8ca8`（13,588,668 B）。
candidate15 归档：jar `2ff30bbd…bcb29`（45,842,088 B）· pak `9c2c7377…0ca585`（13,588,593 B），明细见 [`build-manifest.json`](../../builds/r9-polish-candidate15/build-manifest.json)。
candidate16 归档见 [`build-manifest.json`](../../builds/r9-polish-candidate16/build-manifest.json)。
| candidate20 | 同上 | 再加 batch-06-part02，共 236 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate21 | 同上 | 再加 batch-06-part01（补全 28 处） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate23 | 同上 | 再加 batch-06-part04（重建后 20 处），共 290 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate24 | 同上 | 再加 batch-06-part03，共 331 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate25 | 同上 | 再加 batch-07-part01，共 363 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate26 | 同上 | 再加 batch-07-part02，共 386 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate27 | 同上 | 再加 batch-08-part01，共 410 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate28 | 同上 | 再加 batch-08-part02，共 435 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate29 | 同上 | 再加 batch-08-part03，共 459 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate30 | 同上 | 再加 batch-08-part04，共 491 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate31 | 同上 | 再加 batch-08-part05，共 518 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate32 | 同上 | 再加 batch-09-part01，共 542 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate33 | 同上 | 再加 batch-09-part02，共 551 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate34 | 同上 | 再加 batch-09-part03，共 575 个行级操作（21 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate35 | 同上 | 再加 batch-09-part04，共 592 个行级操作（22 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate36 | 同上 | 再加 batch-10-part01，共 602 个操作（23 批，首批 JSON 指针操作） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate37 | 同上 | 再加 batch-10-part02，共 610 个操作（24 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate38 | 同上 | 再加 batch-10-part03，共 624 个操作（25 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate39 | 同上 | 再加 batch-11，共 649 个操作（26 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate40 | 同上 | 再加 batch-12-part01（词典与任务日志），共 664 个操作（27 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate41 | 同上 | 再加 batch-12-part02，共 677 个操作（28 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate42 | 同上 | 再加 batch-12-part03，共 689 个操作（29 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate43 | 同上 | 再加 batch-13（`MauserHints`），共 706 个操作（30 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate44 | 同上 | 再加 batch-15（残留清理），共 721 个操作（31 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate45 | 同上 | 再加 batch-14（补漏 21 场），共 742 个操作（32 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate46 | 同上 | 再加 batch-16（FENFEN 统一），共 745 个操作（33 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate47 | 同上 | 再加 batch-17（干员／LIGHTTAZER），共 758 个操作（34 批） | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate48 | 同上 | 再加 batch-19（中文引号），共 785 个操作（35 批） | 四步 exit 0，55 类 | 全部 exit 0 |

candidate17 归档见 [`build-manifest.json`](../../builds/r9-polish-candidate17/build-manifest.json)。

candidate34 归档：jar `aa582d80…`（45,841,993 B）· pak `56c8c6f9…`（13,588,134 B）；candidate35：jar `8b61df31…`（45,842,005 B）· pak `b05376b4…`（13,588,153 B）；candidate36：jar `d9f84be5…`（45,842,006 B）· pak `265da4b1…`（13,588,138 B）；candidate37：jar `0cb6b1fe…`（45,842,003 B）· pak `0f30d392…`（13,588,122 B）；candidate38：jar `c5e17da5…`（45,842,001 B）· pak `131e8b2d…`（13,588,116 B）；candidate39：jar `01fd4aea…`（45,841,995 B）· pak `189763e2…`（13,588,104 B）；candidate40：jar `99240052…`（45,841,992 B）· pak `0396bf6a…`（13,588,099 B）；candidate41：jar `f5490c63…`（45,841,978 B）· pak `1876e323…`（13,588,110 B）；candidate42：jar `1dc1f5d4…`（45,841,980 B）· pak `c538fdc6…`（13,588,108 B）；candidate43：jar `e7245c85…`（45,841,980 B）· pak `5a3db829…`（13,588,075 B）；candidate44：jar `7aaf7df5…`（45,841,980 B）· pak `939f3731…`（13,588,075 B）；candidate45：jar `39dbdf11…`（45,841,965 B）· pak `806c608c…`（13,588,075 B）；candidate46：jar `fdc626a5…`（45,841,961 B）· pak `47e32c37…`（13,588,071 B）；candidate47：jar `06c9515b…`（45,841,949 B）· pak `33479da8…`（13,588,065 B）；candidate48：jar `dcedd6bf…` · pak `504af7bb…`。所有候选的 `status` 均为 `integrated_candidate_not_real_clip_CRT_input_acceptance`，manifest 记 `installed: false`、`real_clip_CRT_input_verified: false`；`tests/candidate34`～`tests/candidate43` 的 `results.json` 记 `game_started: false`、`user_save_accessed: false`。

构建入口仍是 [`build_candidate.py`](../../optimization/r28/integration/build_candidate.py) 与 [`test_candidate.py`](../../optimization/r28/integration/test_candidate.py)；未生成 `acceptance.json`（字体与资源复核未重新封签）。

台账与候选的核对做法由 [`tools/verify_readback.py`](tools/verify_readback.py) 承担：构建后按 component.json 的批次顺序遍历全部台账，逐条读回候选归档的明文（行号或 JSON 指针）与台账 `new` 逐字节比较。candidate43 上 30 批 706 个操作全部相等（candidate39 是 26 批 649 个，candidate40／41／42 分别为 664／677／689 个），再确认 gate 的 `ledger_sha256`／`decisions_sha256` 与暂存区 blob 一致。

## 七、边界

- 已落地 batch-01～16（2,698 场／12,552 行），约占全库 2,989 场的 90.3%（行 93.0%）。**但「第 1 轮」仍不因此视为完成**：剩下 291 场不在任何批次定义内（287 场脚本串、4 场图像，见 COVERAGE_AUDIT），且视觉层与实机层未验。
- 批次定义本身的覆盖边界见 [COVERAGE_AUDIT](COVERAGE_AUDIT.md)：batch-01～11 合起来覆盖 2,175／2,989 场，剩下的 473 场是词典条目、50 场是 `MauserHints*` 提示语、287 场是脚本串、4 场是图像。**按当前批次定义完成，不等于全库逐行精校完成**；扩大范围要新开批次并另行确认。
- 已发现但不在任何批次内的术语分叉与反向改动记在 [LEFTOVERS](LEFTOVERS.md)（例：`Tomcat*`／`TomcatItems*` 的 pak 侧仍有 8 处「狗头人」；batch-09-part02 曾把「电击枪」改成少数写法「电击器」；batch-10 里卡面值尾多出的换行受引擎换行计数保护，改不了）。
- 四项全库口径问题已留置待终裁：`LIGHTTAZER` 命名、失真字幕处理方式、`COMMAND CENTER`（总部／指挥中心）、`PUPLOCK`（pup＋Harlock 双关，音译会丢掉 pup 那一层）。
- 引号体例（`“”` 与 `「」` 并存）也仍待终裁：各批只在行内保持原体例，未做全局统一，累计约 110 对 `“”` 对 39 对 `「」`。
- `FENFEN` 的中文条目名未定：词典 SFW 版作「芬芬」、NSFW 版作「Fenfen」，正文 124 处作 Fenfen。目前只统一英文写法，未新造中文名。
- 不覆盖任何历史证据；未安装、未启动游戏、未访问存档；未生成 `acceptance.json`。
- CPU 回归与静态复核不等于实机验收：男线 `DragonHint` 既有 4 行折行（240px／12px 实测）是否翻页或溢出，仍需实机确认。
- 台账中的应用项只证明「更准、更连得上」，不证明全篇语义终审通过。
- 后续批次按 [TRANSLATION_PLAN](../r1/TRANSLATION_PLAN.md) 第八节顺序推进，每批沿用同一双路与裁决流程；`R9M-003`（频率数字两侧空格）待全库排版口径统一后单独处理。
