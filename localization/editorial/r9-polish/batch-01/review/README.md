# batch-01 裁决与落地

两路独立精校的产物、结构核验、裁决表与来源锁定台账。本目录只记录本批（开场与第一区无线电教学）。

## 一、两路产物

| 路 | 路由 | 发现 | 覆盖 | 分级 |
| --- | --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash`（`tiered` 自适应） | 18 条 | 137/137 场 `read_full` | A 0 / B 16 / C 2 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash`（`high`） | 22 条 | 137/137 场 `read_full` | A 0 / B 17 / C 5 |

原始产物分别在 [`../gemini/`](../gemini/) 与 [`../ds/`](../ds/)；两路互不通信。

## 二、结构核验

`tools/verify_batch.py`（[报告](structure-report.json)）：

- 两路 coverage 均 137 场、无重复、无跨场 row、无空尾行填充，前缀与保护标记守恒。
- 32 个 row 有提案；两路同时提案 8 行，其中文本一致 4 行、冲突 4 行（`ReturnFromAreaC`、`HAPPY HACK-`、`OTP 频道`、`好价钱` 让价句）。
- `tools/measure_width.py`（[报告](width-report.json)）用真实 12px 字形表测折行：唯一超 3 行的行是**既有**男线 `DragonHint`（4 行），本轮 32 条提案全部 ≤ 3 行，无新增溢出。

## 三、裁决

[裁决表](decisions.tsv) 共 35 条：**apply 32 / reject 2 / hold 1**。其中 `R9M-001`／`R9M-002` 是主代理交叉核对时补的姊妹行，`R9M-003` 是留置项。

主要采纳：

| 类别 | 内容 | 处理 |
| --- | --- | --- |
| 术语 | `radio` 女线作「收音机」、`security door` 女线作「安全门」、`shaft/network` 各版作「矿道／巷道／矿洞」 | 统一为无线电／安保门／竖井网（与男线及术语表一致） |
| 语用 | `I'll let you have it for a good price` 三处「按好价钱把它让给你」 | 改为「这石头便宜点卖给你！」（与女线 nsfw 既有译一致） |
| 口吻 | 男线 `HAPPY HACK-` 被拆成「黑-客快乐」、`MY SCANNING PROGRAM IS-` 行尾半角减号 | 统一为女线既有的「黑客——」「是——」破折号写法 |
| 施受 | 男线「身上有芯片粘着你吗」 | 改「身上粘着芯片吗」 |
| 衔接 | 女线 `ReturnFromAreaC`「那片区域那边怎么了」 | 合并两路改为「你跑回那片区域干嘛呀？」 |
| 术语双关 | 男线「OTP 密码加密频道」 | 与女线一致改「一次性密码本加密频道」，接后文双关 |

驳回 2 条、留置 1 条，理由见裁决表：`捅出大窟窿→彻底崩掉`（C 级，两版各自成立）、`黏黏→黏糊糊的小家伙`（C 级，加长约 60px 而收益小）、`28.250` 两侧空格（全库排版口径未统一，单独处理）。

## 四、落地

- 台账：[editorial-r9-polish-repairs.jsonl](../../../translations/editorial-r9-polish-repairs.jsonl)，32 个行级操作，绑定 4 个资源的整资源 SHA 与精确旧值。
- gate：[build-gate.json](build-gate.json)，`verified_for_application`，含 dry-run 的 before/after 资源 SHA。
- 首次应用：并入 candidate13 构建；构建与 CPU 回归结果见[轮次 README](../../README.md#六构建与回归)。

## 五、边界

32 条提案只证明「这些行在本批语境下更准、更连得上」。没有做全量语义终审，没有实机排版/分页验收；`DragonHint` 既有 4 行折行仍需实机确认是否翻页或溢出。
