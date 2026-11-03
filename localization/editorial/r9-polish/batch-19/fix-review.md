仍有 2 个阻断

快照：HEAD `7c2d749`。对照 `7a5a181`（两个阻断）和 `7c2d749`（八条观察）。工作区干净。本次只读，未复跑回归，未重写 gate。

## 阻断 1：sfw／nsfw 分侧

未修完。`batch-19/README.md:27` 已改对，`out/layout/ROUNDUP.md:111` 仍是旧句。

对得上的三处数据（与文档声明的 jar 3+8+1、pak 3+10+2 一致）：

- `orders/batch-19.json`：sfw 12（datadf 3、datadm 8、datav 1），nsfw 15（datadf 3、datadm 10、datav 2）。
- `review/decisions.tsv` 的 `scene_id`：sfw 12、nsfw 15。
- 台账 `editorial-r9-batch-19-repairs.jsonl`：`cosmobreeder-multi.jar` 12、`patch.pak` 15。

`batch-19/README.md:27` 现在是「27 行，sfw 12 行、nsfw 15 行（jar 侧 datadf 3 + datadm 8 + datav 1；pak 侧 3 + 10 + 2）」，与上面三处一致。

残留：`out/layout/ROUNDUP.md:111` 仍写「结果 27 行：sfw 13、nsfw 14」。`7a5a181` 的 diff 没有改这一行。当前 markdown 里另一处出现 13／14 的是 `batch-19/push-review.md:87`，那是上一份核验记录原句，不是新的现状陈述。

## 阻断 2：Fenfen 152／148 与槽位

总数和槽位修对了。分项句子没有修对，这是这次修复新写进去的事实错误。

从 candidate47 自行重算（玩家可见：不是空行，不以 `{` `}` `#` `<` 开头，不是 `include `／`if `／`else`／`do `，不含 `&&`／`||`，且含汉字；再数驼峰 `Fenfen`）。与 `probe_fenfen.py` 的定义相同，但是另一段计数，不读它的输出再加总。

| 口径 | 自算 | 文档／探针 | 差 |
| --- | ---: | ---: | ---: |
| 出现次数 | 152 | 152 | 0 |
| 位置数 | 148 | 148 | 0 |
| 说话人槽位 | 0 | 0 | 0 |

按资源的出现次数：datadf 19、datadm 18、datav 38、vsn 77，合计 152。与 `fenfen-hits.json` 的 `occurrences`、`by_source` 一致。

按资源的位置数：datadf 17、datadm 16、datav 38、vsn 77，合计 148。多出来的 4 次出现在 datadf（+2）和 datadm（+2），是同一位置里出现了两次，不在 datav／vsn。

文档把出现次数的分项安在了位置数后面：

- `LEFTOVERS.md:99`：「分布在 148 个位置（datadf/1 19、datadm/1 18、datav 38、vsn 77）」
- `ROUNDUP.md:65` 同型
- `AGENTS.md` 只写了 152，没有这组分项，不承担这条错误

19+18+38+77 = 152，不是 148。探针里的 `by_source` 加的是 `count`（出现次数），不是位置数。所以 JSON 字段本身与出现次数对得上，散文把这四项说成 148 个位置的分解，对不上。

说话人槽位 0 可信。自算用了两条规则：`Name: [` 且名字里含 `Fenfen`，以及行首 `Fenfen:`。玩家可见文本、以及能解码的全部文本（含脚本行）里，子串 `Fenfen:` 都是 0。探针 `actor_slot_locations` 为 0，148 条记录里 `actor_slot` 全是 false，记录文本里也没有 `Fenfen:`。

工具缺口（不改变这个 0）：`probe_fenfen.py:71-73` 扫 `vsn/*` 时把 `actor_slot` 写死为 false，没有跑 `ACTOR` 正则。datadf／datadm 才跑。vsn 的 0 是独立重算得来的，不是单靠这份探针字段。

## 观察处置

同意的：

- 337 行对 341 次：改成按出现次数记 152，与自算一致。早前 337 不再当作现状。
- 卡面 3 处：`LEFTOVERS.md:87` 已改成 jar 1 处（仅 Redbull Front）、pak 2 处（Dragon Front + Redbull Front）。与上一轮对 candidate47／48 的解密计数一致。`ROUNDUP.md:111` 和 `batch-19/README.md:46` 仍用「Dragon、Redbull ×2」，这是对的简写，不是「两边各一份」。
- 逗号字模：`batch-19/README.md:5` 与 `ROUNDUP.md:100` 已改成 `,` 5×5，句号 4×4 保留。与 `candidate48/fonts/story12.fnt` 的 `char id=44`（宽 5 高 5）、`id=46`（宽 4 高 4）一致。
- glossary：`LEFTOVERS.md:99` 与 `ROUNDUP.md:69` 已写成 `Fenfen,种族名,芬芬,,proposed`，并说明中间是空列。与 `localization/review/glossary.csv:5` 一致。
- 未复跑回归／gate dry-run：没有被改成「已经复跑」。`batch-19/README.md:36-38` 仍是原先的产物陈述，不是这次新追认。

不同意的一条：扫描器跳过表是启发式，提交说明写「已写进 batch-19 README」，文件里没有这句。`7c2d749` 对 `batch-19/README.md` 的 diff 只改了逗号字模。`:24` 仍只列 `<标签>`、`include`、`if/else`、`&&`／`||`，没有说明 `if(`、`include{` 和行中标签不会被跳过。这条观察没有落地。

## R9 README 边界节

`localization/editorial/r9-polish/README.md:232-244` 没有把已定案说回未定案，也没有把 acceptance 说成别的东西。

- `:232`：candidate47 与 candidate48 的 `acceptance.json` 都在，顶层 `status` 都是 `passed_cpu_and_independent_review_not_real_clip_CRT_input`。封签脚本 `localization/optimization/r28/integration/finalize_r9_acceptance.py` 在。两份文件里的 `cpu_regression.status` 仍是 `passed_cpu_only_not_real_clip_CRT_input`，句子指的是文档顶层状态，没有说错。
- `:238`：batch-01～17 与 batch-19 都已在 `component.json` 里。括号里的 2,698 场／12,552 行是原有覆盖数字，batch-19 是排版批，没有另报一批新场次。不是把未落地的批次说成已落地。
- `:241`：`LIGHTTAZER` 移出待终裁，定为「光击枪」。与 `LEFTOVERS.md:25`、`:48`（batch-17 改 5 处，统一为光击枪）一致。失真字幕、`COMMAND CENTER`、`PUPLOCK` 仍标待终裁。
- `:243`：152 处未跟进、槽位 0，与自算一致。没有把这 152 处说成已经改完。
- `:244`：删掉了「未生成 acceptance.json」。与文件存在性一致。

## 阻断

1. `out/layout/ROUNDUP.md:111` 仍写 sfw 13、nsfw 14。数据与 `batch-19/README.md:27` 都是 12／15。
2. Fenfen 的 152／148 和槽位 0 是对的，但 `LEFTOVERS.md:99` 与 `ROUNDUP.md:65` 把出现次数分项（19／18／38／77，合计 152）写成了 148 个位置的分解。位置分项是 datadf 17、datadm 16、datav 38、vsn 77。

## 二次复核

三处已确认

对照 `e890ccc`，只核上一节的三处，没有重开全量审查，也没有重解密。Fenfen 两组分项沿用上一轮对 candidate47 的独立重算。

1. 分侧已对齐。`batch-19/README.md:29` 与 `out/layout/ROUNDUP.md:111` 都是 sfw 12、nsfw 15，并写出 jar 侧 datadf 3 + datadm 8 + datav 1、pak 侧 3 + 10 + 2。与工单、决策表、台账一致。ROUNDUP 其它章节、`LEFTOVERS.md`、`AGENTS.md` 里没有再把本批写成 sfw 13／nsfw 14。还出现这组旧数字的只有 `batch-19/push-review.md` 和本文件上文，都是核验记录在引用旧句，不是现状陈述。

2. 两组数与重算一致，没有再混用。`LEFTOVERS.md:99` 与 `ROUNDUP.md:65` 分开写：152 次出现，分项 19／18／38／77；148 个位置，分项 17／16／38／77。19+18+38+77 = 152，17+16+38+77 = 148。`AGENTS.md:10`、`README.md:243`、`ROUNDUP.md:18` 与 `:142` 只写「152 处」，没有把 19／18／38／77 安到 148 个位置上。

3. 启发式说明与第 5 节一致，没有说成本批可能误伤。`batch-19/README.md:26` 写明跳过表是前缀启发式、不是完整脚本解析器，并点了 `if(`、`include{`、行中标签、不以这些前缀开头的 `while`／`return`。接着写本批 27 行没有这类行，所以没有误伤；下次全库重扫不能只靠这份跳过表。
