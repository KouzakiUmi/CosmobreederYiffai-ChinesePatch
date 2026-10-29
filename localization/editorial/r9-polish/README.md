# R9：全正文系统精校（第 1 轮）

本轮把 R1 粗校／R2 修复之后的**全文系统精校**真正开跑：对照英文重写中文，而不是只挑错词。方法口径沿用 [R1 中文重写方案](../r1/TRANSLATION_PLAN.md)，落地沿用来源锁定台账与候选构建链。

## 一、输入基线

| 项 | 值 |
| --- | --- |
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

## 五、流程与产物

1. `tools/build_batch.py <batch> --snapshot <snap>` 生成批次工单（可复现，带 corpus manifest SHA 与基线候选）。
2. 两路各自写 `batch-NN/gemini|ds/{findings,coverage}.jsonl` 与 `summary.md`。
3. `tools/verify_batch.py <batch>` 做结构核验（覆盖、row 归属、前缀与标记守恒）并输出 worksheet；`tools/measure_width.py <batch>` 用真实 12px 字形表实测折行。
4. 主代理逐条核验后写 `batch-NN/review/decisions.tsv`；`tools/build_ledger.py <batch>` 生成该批来源锁定台账并 dry-run，`tools/verify_round.py <batch>` 出 gate。
5. 在 `localization/optimization/r28/r9polish/component.json` 的 `batches` 数组登记该批（台账／gate／decisions 三项），再构建候选与跑 17 步回归。

## 五之二、三批合计

| 项 | batch-01 | batch-02 | batch-03 | 合计 |
| --- | --- | --- | --- | --- |
| 场次／行 | 137／358 | 56／566 | 53／437 | 246／1,361 |
| 两路发现 | 18＋22 | 63＋71 | 44＋38 | 256 |
| 裁决 | 35 | 38 | 35 | 108 |
| 　采纳 | 32 | 24 | 28 | **84** |
| 　驳回 | 2 | 11 | 5 | 18 |
| 　留置 | 1 | 3 | 2 | 6 |
| 主代理补 | 3 | 2 | 16 | 21 |

驳回率从 batch-01 的 6% 升到 batch-02 的 29%：batch-02 的两路都大量重提已裁决术语（`agent`／`torch`／`MARK IV`），并且互相把对方的方向当成误译。

## 六、构建与回归

`r9polish` 组件按 `batches` 数组顺序应用各批台账。每批的 gate 绑定**它应用之前的那一个构建**（batch-01 绑 candidate12、batch-03 绑 candidate13、batch-02 绑 candidate14），构建时逐批串行校验整资源 SHA：任何一批的基线漂移都会让构建直接失败，而不是悄悄覆盖。

| 候选 | 组件 | 台账 | 编译 | 17 步回归 |
| --- | --- | --- | --- | --- |
| candidate13 | 15 个（新增 `r9polish`），`full_component_set=true` | batch-01，32 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate14 | 同上 | batch-01 + batch-03，60 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate15 | 同上 | batch-01 + batch-03 + batch-02，84 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |

candidate13 归档：jar `fb533645…61587`（45,842,131 B）· pak `046158e7…af8ca8`（13,588,668 B）。
candidate15 归档：jar `2ff30bbd…bcb29`（45,842,088 B）· pak `9c2c7377…0ca585`（13,588,593 B），明细见 [`build-manifest.json`](../../builds/r9-polish-candidate15/build-manifest.json)。

构建入口仍是 [`build_candidate.py`](../../optimization/r28/integration/build_candidate.py) 与 [`test_candidate.py`](../../optimization/r28/integration/test_candidate.py)；未生成 `acceptance.json`（字体与资源复核未重新封签）。

## 七、边界

- 已落地 batch-01／02／03（246 场／1,361 行），约占全库 2,989 场的 8.2%；**其余批次未精校，「第 1 轮」不因此视为完成**。
- 三项全库口径问题已留置待终裁：`LIGHTTAZER` 命名、失真字幕处理方式、`COMMAND CENTER`（总部／指挥中心）。
- 不覆盖任何历史证据；未安装、未启动游戏、未访问存档；未生成 `acceptance.json`。
- CPU 回归与静态复核不等于实机验收：男线 `DragonHint` 既有 4 行折行（240px／12px 实测）是否翻页或溢出，仍需实机确认。
- 台账中的应用项只证明「更准、更连得上」，不证明全篇语义终审通过。
- 后续批次按 [TRANSLATION_PLAN](../r1/TRANSLATION_PLAN.md) 第八节顺序推进，每批沿用同一双路与裁决流程；`R9M-003`（频率数字两侧空格）待全库排版口径统一后单独处理。
