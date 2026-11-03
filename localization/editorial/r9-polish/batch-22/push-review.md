有 2 个阻断

快照 `HEAD = c6b7ec4c696bde7ecd24027dbef0431b93c2913b`，核验时工作区干净。未跑 17 步回归，未启动游戏，未改已有文件。只读探针用系统 Python 3.12，对 `editorial_repairs.apply_entry` 做了内存用例，并解密 candidate50 的四份文本条目核对行定位。

## 阻断

### B1. 引擎守卫没有把 U+2028 关在 line 行的逐字例外里

`localization/tools/editorial_repairs.py:47` 把旧禁表 `'\x85\u2028\u2029'` 改成了 `'\x85\u2029'`。U+2028 的码位是 8232，不小于 32，所以 `:46` 把 `LINE_BREAK` 拼进 `allowed` 对它不起作用。结果是 **所有** `_safe_string` 模式都放行 U+2028，不只有 `line_row`。

`apply_entry` 的逐字条件在 `:171`，门是 `kind == 'line'`。JSON 不进这个分支，也没有对应的「只能插入断行符」检查；JSON 的换行计数只看 `\r` `\n`（`:169`）。

内存探针（合成资源，不是台账里的 op）：

| 用例 | 结果 |
| --- | --- |
| line：只插入 U+2028 | 通过 |
| line：插入 U+2028 并改字 | 拒绝，`line break insertion must not alter the text` |
| line：插入 LF / U+2029 / U+0085 | 拒绝，`string/control/newline violation` |
| line：U+2028 只放在 `old` | 拒绝，同一条逐字错误 |
| json：`hello` → `hello` + U+2028 + `X` | **通过**，写出的资源含 U+2028 |

旧代码会在 `_safe_string` 拒绝最后一行。这是这次 diff 放宽出来的，不是原有行为。`DialogueGrid.java:32` 只拒 CONTROL/FORMAT，U+2028 是 LINE_SEPARATOR，挡不住；`PixelLayout.hardBreak` 会把它当显式断行。当前三份台账没有借这条缝，但推上去的守卫本身不成立。

### B2. batch-22 的「总行数不变」量的是物理行，不是显示正文

`scan_batch22.py:75` 的 `attempt()` 对**整行**（含 `  * ` / `  Tomcat: `）做 240px 贪心折行，挪字后再用同一个 `wrap()` 比行数。这套自检在它自己的输入上成立：950 行独立重放，贪心行数全部不变，没有空段，没有超 240px 的段，台账 `new` 与重放结果一致。标点上移分支实际是 0 次，958 处全是「上一行末字下移」。

它不能证明显示行数不变。目录把说话人前缀和正文分开存（`occurrences.jsonl` 的 `prefix` 是 `  * ` / `  Tomcat: `，`speaker` 另记）。`DialogueWrap.story` 折的是已经解析过的对白元组；`DialogueWrapTest.java:140` 传入的是裸正文，不是带前缀的脚本行。VSN 侧 `render_layout_samples.py:60` 也写明引擎只画 payload。

用与扫描器相同的 story12 `xadvance`、240px 贪心，只折 `_line_role` 的正文：

- 950 行里 **691** 行正文行数变化，其中 **609** 行从 1 行变成 2 行。
- `editorial-r9-batch-22-repairs.jsonl:224` `R9-0224`（jar `datadf/1` 第 71 行）：整行 248px，折成 `…制服` / `？`；正文 `不知道这是什么，某种破旧的太空制服？` 只有 216px，原本 1 行。插入 U+2028 后正文变成 `…太空制` / `服？`，2 行。`ROUNDUP.md` 里单独一行的 `？` 就是整行折行后把前缀从示意里拿掉的结果，不是正文自己的折行。
- 同模式的第一笔：`R9-0001`（`:1`，第 1001 行）正文 216px，1 → 2。

分页按显示行、每页 3 行。这 609 行会多出一行，和「总行数不变所以分页与动画节奏不变」相反。

## 五项

### 1. 引擎守卫

文件 `localization/tools/editorial_repairs.py`，sha256 `2410bc8b504b`。

- **U+2029、U+0085、LF、CR、VT 没有被 line_row 放行。** 探针：line_row 下这些都是 `string/control/newline violation`。U+2028 被放行，但是因为从全局禁表删掉了，json / 非 line 同样放行。见 B1。
- **行级逐字校验在 `apply_entry` 里、且只对 `kind == 'line'` 生效。** `:167-176` 先 `_safe_string(..., line_row=kind == 'line')`，再在计数不等时要求 `new.replace(LINE_BREAK, '') == old`。插断行并改字被拒，证明这条在应用路径上真的跑到了。
- **U+2028 放进 `old` 绕不过。** 计数不等时左边去掉 U+2028 后不可能等于仍含 U+2028 的 `old`。源行里本来没有 U+2028 时，`bodies[n-1] != old` 也会先对不上。JSON 不是借 line_row 分支（`line_row` 为假），而是全局禁表被拿掉，见 B1。
- **`_line_role` 这次没改。** Python 的 `.` 匹配 U+2028，`[^\r\n]` 切行不切它（`:134`）。950 条 line op 的前缀组都不变。紧贴无空格冒号插入（`Name:` + U+2028）会让 `\s` 吃掉断行符、前缀变掉，随后被 `:183` 拒绝；本批没有这种插入。
- **历史批次行为不变。** `translations/editorial-r9*-repairs.jsonl` 去掉 20/21/22 后 35 个文件，裸 U+2028 与 `\u2028` 转义都是 0。新分支只在计数不等时触发，这些 op 走不到。`_safe_string` 相对旧版唯一放宽的字符就是 U+2028，它们不含这个字符。batch-01 的 `build-gate.json` 只改了校验器哈希，现值为 `0b76aa5a89fc`，与当前 `verify_round.py` 一致。没有 batch-18 台账文件。

### 2. batch-22（950 行）

`localization/translations/editorial-r9-batch-22-repairs.jsonl`，sha256 `ccd805e65800`，950 行，全部 `kind == line`。文件内裸 U+2028（UTF-8 `E2 80 A8`）为 0，`\u2028` 转义 1084 处；`splitlines()` 与按 LF 切开的记录数都是 950。

- 去掉 U+2028 后 `new == old`：950/950。没有多余字符。
- 插入的是 U+2028，不是 LF / CR / U+2029 / U+0085。每行 `new` 至少 1 个：1 个 817 行，2 个 132 行，3 个 1 行；`old` 里是 0。
- `line` 与 candidate50 同一物理行：四个资源 SHA 与台账 `before_resource_sha256` 一致，`bodies[line-1] == old` 无失配。
  - jar `datadf/1` 228 行，`5dc3bb1c14e5`，5190 物理行
  - jar `datadm/1` 234 行，`4f9acb1b8ff1`，5238 物理行
  - pak `datadf/1` 244 行，`98f6e448e618`，5373 物理行
  - pak `datadm/1` 244 行，`e6eaba3fdea4`，5386 物理行

`attempt()` 的比较逻辑，在它自己的整行模型里可信，而且几乎是宽度检查的重述：advance 非负时，段宽 ≤ 240 就不可能再被同一个 `wrap()` 拆开。它没有第二套实现，也没有量显示正文。显示行数见 B2。

### 3. batch-20（148 行）

`editorial-r9-batch-20-repairs.jsonl`，sha256 `670cf97c3071`。148 个 op，152 次 `Fenfen`→`芬芬`。逐 opcode 走查：除了这个替换，以及紧贴 token 的单侧一个空格被去掉，没有别的差异。去掉空格的是 8 个 op、9 个 token 位点（`R9-0088` 两个 token 各去掉前后一个空格），与提交说明里的「九处」一致。例：`:13` `R9-0013`，`关于 Fenfen 服装` → `关于芬芬服装`。

纯拉丁上下文：把 `Fenfen` 拿掉后仍无汉字的值是 0；token 左右各 12 字无汉字的也是 0。`fenfen` / `FENFEN` 没有被改，也没有残留在 `new` 里。`\n` / `\r` / U+2028 计数全部不变。

### 4. batch-21（3 行）

`editorial-r9-batch-21-repairs.jsonl`，sha256 `e666ab48889b`。三处都是 json 指针，差异只有直引号 `"` 换成 `“` / `”`。换行数不变：每处 `old`/`new` 都是 1 个 LF、0 个 CR、0 个 U+2028，尾部空格保留（`R9-0001` 尾部是 `……     \n`）。

### 5. 共享文本规则

`text_rules.py` sha256 `9e20949190ff`。`expand_newlines` 先把 U+240A（`␊`）换成 LF，再把 U+240B（`␋`）换成 U+2028（`:32`）。LF 不是 `␋`，U+2028 不是 `␊`，两种顺序对混排哨兵结果相同（探针 7 组，含相邻、重复、以及文本里已经有的 LF / U+2028）。

`build_ledger.py:24` 与 `verify_round.py:22` 都从这里 import。`r9-polish/tools/*.py` 里 `def expand_newlines` / `def effective_final` 只剩 `text_rules.py`。`r9_decisions.py:72` 和 batch-19/20/21 的决策脚本各自有一份 `SYMBOL_FOR_NEWLINE`，只负责往 TSV 里编码，不展开。

写台账：`build_ledger.py:137-138` 在 `json.dumps(ensure_ascii=False)` 之后把裸 U+2028 换成 `\u2028`。Python 3.12 的 `dumps` 会写出裸字符；替换后 `splitlines()` 不再切开，`json.loads` 能还原。batch-22 文件符合这个形态。注释说「`text_rules` 展开它」不准确，展开转义的是 `json.loads`，不是 `text_rules`。功能上读回是通的。

## 观察

- `allowed` 里的 U+2028 是死代码。真正放行它的是禁表删除。
- DEL（U+007F）、U+0080、U+0086、ZWSP 现在也能过 `_safe_string`。旧禁表也不含它们，不是这次引入的。
- 历史 gate 只更新了校验器哈希，dry-run 段没有在这次 diff 里重算。静态路径上历史 op 不会改行为；没有重跑 `apply_entries`。
- `attempt()` 的「标点上移」分支在这 950 行上一次都没走到。续行以标点开头，说明当时标点就放不进上一行。
- 同一套 PixelLayout 近似（墨宽、禁则、28 个 UTF-16）折整行，950 行行数也不变。这只说明整行模型内部稳，不能抵消 B2。端口没有对上 Java 回归，不单独当证据。

## 未覆盖

未跑 17 步回归，未启动游戏，未用游戏解析器实跑一条 DS 行。B2 的显示行数是按目录前缀切开后、用 story12 `xadvance` 贪心折正文得到的，不是实机分页。

## 二次复核

两处已确认

复核提交 `b34cd4b76bcd81c90e2084739161508270fe9e99`。只核 B1、B2。未跑回归，未启动游戏。正文行数用 candidate50 的 `story12.fnt` `xadvance`、240px 贪心独立重算，前缀用 `editorial_repairs._line_role`，不调用 `scan_batch22.attempt()`。

### B2

`editorial-r9-batch-22-repairs.jsonl` 现为 57 个 op、71 个 U+2028（文件内裸 U+2028 为 0，`\u2028` 转义 71）。`decisions.tsv` 是 1 行表头 + 57 行 `apply`。四个资源的 `before_resource_sha256` 与 candidate50 明文一致，`bodies[line-1] == old`，57/57。

57 行的正文显示行数全部相等：前缀不变，去掉 U+2028 后正文逐字相同，`wrap(body(old))` 与 `wrap(body(new))` 行数无失配。

上次那条没有漏进来。jar 与 pak 的 `datadf/1` 第 71 行仍是 `  * 不知道这是什么，某种破旧的太空制服？`，正文 216px、1 行；按旧插入点在「制／服」之间加 U+2028 后正文变成 2 行。新台账里没有这句。筛选把这种「正文 1 行、插入后 2 行」挡在 57 行之外。

### B1

`editorial_repairs.py:50-59` 按类型分表：`json_value` 禁 U+2028/U+2029/U+0085；`line_row` 只从禁表拿掉 U+2028；其余仍禁这三个。`:179-180` 只按 `kind` 传参，json 与 line 互斥。即便两个标志同时为真，json 分支在前，U+2028 仍被拒（直接探针）。

| 探针 | 结果 |
| --- | --- |
| json：`hello` → `hello` + U+2028 + `X` | 拒绝，`string/control/newline violation` |
| json：只插入 U+2028 | 拒绝，同上 |
| line：只插入 U+2028 | 通过 |
| line：U+2029 / U+0085 / LF | 拒绝 |
| line：`old` 与 `new` 都有 U+2028，且计数不等并改字 | 拒绝，`line break insertion must not alter the text` |

计数相同的改字仍走普通替换（源行必须等于 `old`），不是插入例外的新口子。没有发现 json 借 `line_row=True` 混进来的路径。
