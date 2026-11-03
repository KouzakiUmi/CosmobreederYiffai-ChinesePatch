# batch-22 自查记录（主代理，非独立核验）

这份是主代理在等待独立核验期间自己跑的确定性检查，**不是**独立复核，不能替代
`push-review.md`。写下来是为了让结论有据可查，也让独立核验方有对照。

快照 `HEAD = c6b7ec4`。

## 1. 三份台账

| 台账 | 操作数 | 检查 | 结果 |
| --- | ---: | --- | --- |
| batch-20（Fenfen） | 148 | `new` 里是否还有 `Fenfen` | 0 |
| batch-21（多行卡面引号） | 3 | 换行数是否与 `old` 相同 | 相同 |
| batch-22（行首标点） | 950 | `new` 去掉 U+2028 后是否逐字等于 `old` | 0 处不符 |
| batch-22 | 950 | 是否混入 LF | 0 |
| batch-22 | 950 | 是否都真的插了 U+2028 | 0 处没插 |
| batch-22 | — | 插入的断行点总数 | 1,084 |

## 2. 引擎守卫（`editorial_repairs`）

用 candidate50 的 `datadf/1` 第 71 行做真实探针：

| 用例 | 期望 | 实际 |
| --- | --- | --- |
| 只插 U+2028，文本不变 | 接受 | 接受 |
| 插 U+2028 同时改字 | 拒绝 | 拒绝（`line break insertion must not alter the text`） |
| 插 U+2028 同时换词 | 拒绝 | 拒绝 |
| 在行首前缀里插断行 | 拒绝 | 拒绝 |
| 连插两处 U+2028，文本不变 | 接受 | 接受 |
| 用 LF 代替 | 拒绝 | 拒绝（`string/control/newline violation`） |
| 夹带 U+2029 | 拒绝 | 拒绝 |
| 夹带 U+0085 | 拒绝 | 拒绝 |
| 原 `old` 已含 U+2028 且 `new == old` | 拒绝 | 拒绝（`no-op operation`） |

`_line_role` 在前缀后带 U+2028 时仍能正确切出前缀：`  * `、`  Mauser: `、`text: `
三种形状都验过。

## 3. 共享文本规则

- `effective_final` 现在只有一份实现（`tools/text_rules.py`），`build_ledger.py` 与
  `verify_round.py` 都 import 它；两个工具里 `def effective_final` 的计数为 0。
- 两种哨兵互不干扰：`'a␊b␋c'` → `'a\nb\u2028c'`，`'a␋b'` → `'a\u2028b'`（不会二次展开）。
- 台账写出时把裸 U+2028 转义成 `\u2028`，否则 `splitlines()` 会切开 JSONL —— 这条是
  第一次跑读回时踩到的（1,416 个假问题），已修。

## 4. 回归与读回（本轮实际执行）

| 候选 | 批数 | 17 步回归 | 读回 | 封签 |
| --- | ---: | --- | --- | --- |
| candidate49（+batch-20） | 36 | 全部 exit 0 | 933 ops／0 问题 | passed |
| candidate50（+batch-21） | 37 | 全部 exit 0 | 936 ops／0 问题 | passed |
| candidate51（+batch-22） | 38 | 全部 exit 0 | 1,886 ops／0 问题 | passed |

## 5. 一次失败并回退的尝试

第一版 batch-22 用 LF 断行。构建成功、回归也跑通了，但**读回报 1,416 个问题**：插
LF 会改变物理行数，entry 里所有后续行号整体错位，于是历史批次按行号取的文本全部
对不上（例：batch-01 R9-0001 行 131 期望「这石头便宜点卖给你！」、实际拿到「先前
震动时…」）。

处理：撤掉 component 里的 batch-22、删掉 batch-22 目录与台账、删掉 candidate51、
`git checkout` 回退引擎改动，然后改用 U+2028 重做。U+2028 同样被 `PixelLayout` 当
显式断行，但本工具链只在 CR/LF 处切行，所以行号不变 —— 重做后读回 0 问题。

## 6. 未做

- 没有独立复核（那份是 `push-review.md`，由另一个只读代理产出）。
- 没有实机渲染：图是真实字模 + 真实折行规则，但没有对话框边框、背景与动画。
- 没有对断词（3,185 处）做任何改动，见 LEFTOVERS 第五节。
