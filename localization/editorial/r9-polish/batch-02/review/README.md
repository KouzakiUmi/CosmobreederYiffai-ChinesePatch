# batch-02 裁决与落地

「核心人物往来」之一：雄猫支援线（Tomcat 相关 56 场）。

## 一、两路产物

| 路 | 路由 | 发现 | 覆盖 | 分级 |
| --- | --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash`（`tiered`） | 63 条 | 56/56 场 `read_full` | A 3 / B 60 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash`（`high`） | 71 条 | 56/56 场 `read_full` | A 5 / B 62 / C 2 / needs_evidence 2 |

原始产物在 [`../gemini/`](../gemini/) 与 [`../ds/`](../ds/)；两路互不通信。

## 二、结构核验

[structure-report.json](structure-report.json)：两路 coverage 均 56 场、无重复、无跨场 row、前缀与标记守恒。112 个 row 有提案，两路同时提案 22 行（一致仅 2 行），冲突与独占各占一半。

[width-report.json](width-report.json)：用真实 12px 字形表实测，本批有 **3 行改前就是 4 折行**（超出 240px／3 行页限），全部是「三行英文合到一行」的既有合句；两路都独立发现并给出压缩稿，**改后全部回到 3 行**。这是本批最实的一类 A 级问题。

## 三、裁决

[裁决表](decisions.tsv) 共 38 条：**apply 24 / reject 11 / hold 3**。

主要采纳：

| 类别 | 内容 |
| --- | --- |
| 页限（A） | 3 处 4 折行压回 3 行（俯冲踢说明 ×2、宇宙大使那段 59 字） |
| 收线误义（A） | `Y-YIFFAI OUT!` 两处「先走了」→「伊吠完毕！」 |
| 术语 | KOBOLD「狗头人」→「科博德」4 处、`电击器`→`电击枪` 3 处、`上+攻击`→`UP+ATTACK` 4 处、钩锁→钩爪枪、`否定`→`不行` |
| 收线套语 | `伊吠通话结束`→`伊吠完毕`（与全库主用法一致） |
| 口吻 | 「说明，特工」→「说明情况，特工」、「你没有可能认错？」→「你会不会是认错了？」 |

驳回的 11 条里，有 2 条是**路线级别的方向错误**，值得记下来：

- Gemini 把 `torch` 全改成「手提电筒」。R2 已裁决 `torch`/`flashlight` 是同一件手电的英美异称（E07-010、P04-032），波苏管手电叫 torch 正是笑点本身；改掉笑点就没了。
- Gemini 把整批 `agent` 一律改「探员」。R2 明确「不将现用特工批量改探员」；全库 471 处「特工」，改单处只会新生不一致。

另驳回 DS 的 `NUB 小肉棒→小肉突`（既不更准也不更雅，且与全库同类用词不一）。

## 四、留置

3 条留置都是**全库口径问题**，不在单批改：

- `LIGHTTAZER` 三种写法：术语提案「光能电击刃」／全库 27 处「光电击枪」／本行「轻型电击枪」。单改一行只会多出第四种。
- 失真台词四场三种处理（保留英文残片／译成可读中文／纯拟声）。
- `COMMAND CENTER` 的「总部」与「指挥中心」并存。

## 五、落地

- 台账：[editorial-r9-batch-02-repairs.jsonl](../../../translations/editorial-r9-batch-02-repairs.jsonl)，24 个行级操作，基线 **candidate14**（batch-01 + batch-03 已并入）。
- gate：[build-gate.json](build-gate.json)，`verified_for_application`。
- `r9polish` 组件按 `batch-01 → batch-03 → batch-02` 顺序应用；每批基线绑定它之前的构建，构建时串行校验，不会互相覆盖。
- candidate15 = 三批合一，四步编译 exit 0、55 类，17 步 CPU 回归见轮次 README。

## 六、边界

- 术语只做**批内统一**，不是全局终裁；`LIGHTTAZER`、失真字幕、COMMAND CENTER 三项仍待全库口径。
- 3 处 4 折行压到 3 行是按真实字形表算的**行数**，不等于实机分页与逐字断行一定理想；仍需实机确认。
- 未安装、未启动游戏、未访问存档。
