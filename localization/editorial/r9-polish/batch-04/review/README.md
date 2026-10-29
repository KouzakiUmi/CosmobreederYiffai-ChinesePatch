# batch-04 裁决与落地

「装备与情报」：毛鼠支援线与装备说明（`Mauser` root，81 场／871 行）。

## 一、两路产物

| 路 | 路由 | 发现 | 覆盖 | 分级 |
| --- | --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash`（`tiered`） | 22 条 | 81/81 场 `read_full` | A 6 / B 11 / C 4 / needs_evidence 1 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash`（`high`） | 39 条 | 81/81 场 `read_full` | A 3 / B 27 / C 7 / needs_evidence 2 |

## 二、结构核验

[structure-report.json](structure-report.json)：两路 coverage 均 81 场、无重复、无跨场 row、前缀与标记守恒。53 个 row 有提案；两路同时提案 8 行，文本一致仅 2 行。

[width-report.json](width-report.json)：真实 12px 字形表实测，本批**既有行没有一条超 3 折行**，19 条应用项也全部在 3 行内。

## 三、裁决

[裁决表](decisions.tsv) 共 40 条：**apply 19 / reject 14 / hold 7**。

### 采纳

| 类别 | 内容 |
| --- | --- |
| A 地名 | `艾斯坎默`→`艾斯卡姆尔`（导航图、图鉴卡、麦森台词都用后者） |
| A 收线 | `Y-YIFFAI OUT!` 两处「先走了」→「完毕！」 |
| A 句子 | 「甚至出更糟的事」缺谓语 →「或者更糟」 |
| A 键名 | `UP & 攻击`／`UP+攻击` → `UP & ATTACK`／`UP+ATTACK` |
| A 残留 | 两行行尾孤立 `"]`（源文引号未闭合被照抄） |
| 术语 | `干员`→`特工`（431 对 12）、`电台`→`无线电`（42 对 2）、`仓储站`→`仓库`（49 对 1）、`COSMO套件`→`宇宙套件` |
| 口吻 | `主联络官`→`主要联络人`（liaison 不是军衔）、`鼠鼠`→`老鼠`（不萌化损友调侃）、`该打给`→`该呼叫` |

### 驳回 14 条，其中一整组是我的错

两路**都**主张把「反重力脚环」改成「反重力踝环」，理由充足、行数也对：6 条提案覆盖 4 个 row。但我核对后发现方向是反的——

| 写法 | 数量 | 证据 |
| --- | --- | --- |
| `脚环` | UI 道具名 + 正文 7 处「反重力脚环」+12 处裸「脚环」 | `SpecialAnklet` 条目的中文就是「脚环」 |
| `踝环` | 5 处 | 全在 `MauserHints_AreaA.OpenMode` 与 `TomcatItems.SpecialAnklet` |

根源是我给两路的 `reference-excerpt.md` 里把 `anti-grav anklet` 写成了「反重力踝环」。两路照我的口径执行，都很称职，但依据本身错了。已修正全部 6 份参照摘录（batch-01/04 与 batch-06 四个 part），并在裁决表逐条写明。

这类错误值得记下来：**参照摘录一旦写错术语，两路会一致地朝错方向改，交叉核对也发现不了。**

### 留置 7 条

- 「唯一在活动的特工」涉及主线信息量，需对照后段剧情。
- 句末缺标点但后续是合句尾行，补标点会改合句节奏。
- `付赌钱` 疑为「付赌注」之误，语义把握不足。
- `Fenfen` 保留英文属未裁专名。
- 失真字幕口径（2 条）与 `MAUSER ORDERS IN... WHAT?` 残句。
- 女线 `YIFFAI?!` 是作者复制男线脚本的笔误，中文照原文不算错译。

## 四、落地

- 台账：[editorial-r9-batch-04-repairs.jsonl](../../../translations/editorial-r9-batch-04-repairs.jsonl)，19 个行级操作，基线 **candidate15**。
- gate：[build-gate.json](build-gate.json)，`verified_for_application`。
- candidate16 = 四批合一，四步编译 exit 0、55 类，17 步 CPU 回归全部 exit 0；四份台账在归档中逐行核对 0 处不匹配。

## 五、边界

- 术语只做批内统一。`LIGHTTAZER`（3 种写法）、失真字幕、`CHEESEBALL` 外号、结巴标记（半角连字符 vs 顿号）、`DEAR` 称呼，都是全库口径问题，未在单批改。
- 未安装、未启动游戏、未访问存档。
