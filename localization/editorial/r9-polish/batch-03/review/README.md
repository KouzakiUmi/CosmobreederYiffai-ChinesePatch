# batch-03 裁决与落地

两路独立精校的产物、结构核验、裁决表与来源锁定台账。本批是「核心人物往来」之二：波苏指挥线。

## 一、两路产物

| 路 | 路由 | 发现 | 覆盖 | 分级 |
| --- | --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash`（`tiered`） | 44 条 | 53/53 场 `read_full` | A 1 / B 30 / C 13 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash`（`high`） | 38 条 | 53/53 场 `read_full` | A 5 / B 29 / C 3 / needs_evidence 1 |

原始产物在 [`../gemini/`](../gemini/) 与 [`../ds/`](../ds/)；两路互不通信。

## 二、结构核验

[structure-report.json](structure-report.json)：两路 coverage 均 53 场、无重复、无跨场 row、前缀与标记守恒。70 个 row 有提案；两路同时提案 12 行，文本一致仅 2 行、冲突 10 行（本批冲突率明显高于 batch-01，主要来自术语方向相反与断句方式不同）。

[width-report.json](width-report.json)：真实 12px 字形表实测，70 条提案无一条超过 3 行折行。

DS 路把「同文多处一并改」写进了单条发现的 `row_ids`，超过本次结构脚本的「全场」约束；裁决时按 row 逐条展开，没有放宽脚本约束。

## 三、裁决

[裁决表](decisions.tsv) 共 35 条：**apply 28 / reject 5 / hold 2**。

主要采纳：

| 类别 | 内容 |
| --- | --- |
| 误义（A） | OUT 从「先走了」改为「通话完毕」（把断线写成了离场）；OVERTAKEN 从「控制」改为「吞噬」；男线 SIBLING「手足」改「姐姐」 |
| 术语统一 | 通讯器→无线电、干员→特工、观测单元/装置合一、报尾「结束通话」→「通话完毕」 |
| 无线电套语 | `WHO IS THIS` 四种写法统一为「是谁？立刻表明身份！」（同一句形的四处）；只有一句的三处另计入留置 |
| 排版 | 人名两侧多余空格、句末缺感叹号、LECT 两侧空格 |

驳回 5 条、留置 2 条，理由都写在表里。其中 `GOOP` 是典型的两路方向相反案例：Gemini 主张女线「黏糊」改「咕叽」，DS 主张男线「咕叽」改「黏糊」。核到男线上文已是「咕噜。咕叽。」，男线才是撞词的一方，故采纳 DS 方向。

## 四、落地

- 台账：[editorial-r9-batch-03-repairs.jsonl](../../../translations/editorial-r9-batch-03-repairs.jsonl)，28 个行级操作，基线 `r9-polish-candidate13`。
- gate：[build-gate.json](build-gate.json)，`verified_for_application`。
- 已注册进 `r9polish` 组件的 `batches`，构建出 candidate14 并跑 17 步 CPU 回归。

## 五、边界

- 术语（无线电／特工／观测单元／鳞片套装／报尾）本批只做**批内统一**，不是全局终裁；全库仍存在「通讯器」以外的写法差异。
- 「鳞装／鳞片套装」两版并存（`TomcatItems.KoboBody` 与 `Bossu.KoboPickup`），本批未动，留待装备类批次统一。
- 断行合句（`SFWc00f5f149929e58137123612` 与下一行）保持原样，未做跨行重分配。
- 未安装、未启动游戏、未访问存档。
