有 2 个阻断

快照：HEAD `fc48649`（只改了 `AGENTS.md`）。batch-19 与 34 个旧 gate 的改动在 `e0e1193`，对照父提交 `b89e093`。工作区相对 HEAD 没有这些文件的未提交 diff；未跟踪的 `out/layout/grok-visual-review.md` 不在本次范围。现场哈希均为文件原始字节 sha256。

## 1. 台账只有引号变化

通过。`localization/translations/editorial-r9-batch-19-repairs.jsonl` 27 行，sha256 `8f035cd6dc9f…`。

- 27 行都有 `op_id`、`archive`、`archive_entry`、`kind`、`before_resource_sha256`、`old`、`new`、`finding_ids`、`source_refs`。`finding_ids` 各 1 个且不重复；`source_refs` 各为长度 2 的列表。另有定位字段 `line` 或 `pointer`，不是缺字段。
- `old` 与 `new` 等长。27 行各改 2 个字符，且每个差异都是 `"` → `“`/`”` 或 `'` → `‘`/`’`。没有空格、前缀、`[]`、`|`、`$` 或其它字符变化。`R9-0001`…`R9-0027` 全部如此。
- `new` 的 `“”` / `‘’` 用栈配对：先开后合，数量成对，0 处失配。没有把纯拉丁包进全角引号（`“SELECT”` 这类口径不符为 0）。
- 27 行都能过 `scan_batch19.player_visible`，且 `rewrite(old) == new`。没有残留的、内部含汉字的直引号对。
- 归档：`cosmobreeder-multi.jar` 12 行（datadf 3、datadm 8、datav 1），`patch.pak` 15 行（datadf 3、datadm 10、datav 2）。kind：`line` 24、`json` 3。

## 2. 决策表与台账一致

通过。`localization/editorial/r9-polish/batch-19/review/decisions.tsv`，sha256 `8abdbb04b55d…`。

- 28 个 CRLF 行：1 行表头 + 27 行数据。表头是 `finding_id route severity category scene_id row_id decision final_zh reason`，逐行 9 列，0 行列数异常。
- `decision` 全部是 `apply`。
- `final_zh` 里没有 `␊`（U+240A）。按「`␊` 换成真换行」比较，27 行都与对应 op 的 `new` 逐字节相同。工单 `orders/batch-19.hits.json` 的 `current`/`target` 也与台账 `old`/`new` 一致。
- `scene_id` 的 mode：sfw 12、nsfw 15。与第 1 节的 jar／pak 计数相同，与文档的 13／14 不同（见阻断 1）。

## 3. gate 哈希

通过（哈希绑定）。`localization/editorial/r9-polish/batch-19/review/build-gate.json`。

| 字段 | 记录 | 现场 |
| --- | --- | --- |
| `status` | `verified_for_application` | 相符 |
| `operations` | 27 | 台账 27 行 |
| `decisions_total` | 27 | 决策 27 行 |
| `ledger_sha256` | `8f035cd6dc9f…` | 相同 |
| `decisions_sha256` | `8abdbb04b55d…` | 相同 |
| `verifier.sha256` | `d42ff0928a30…` | 与 `tools/verify_round.py` 相同 |
| `verifier.path` | `localization/editorial/r9-polish/tools/verify_round.py` | 文件在 |
| `apply_findings` | 27 个，已排序 | 与决策 `finding_id` 集合相同 |
| `problems` | `[]` | — |

`base_candidate` 是 `localization/builds/r9-polish-candidate47`。未复跑 `verify_round.py`（它会重写 gate），所以 `dry_run.after_resource_sha256` 没有在这次核验里重算。

## 4. 34 个旧 gate 只改了 verifier

通过。`git diff` 工作区为空，因为重算已经在 `e0e1193`。用 `git diff b89e093 e0e1193` 看这 34 个 `review/build-gate.json`（batch-01…04、05 的 3 段、06 的 4 段、07 的 2 段、08 的 5 段、09 的 4 段、10 的 3 段、11、12 的 3 段、13…17）：

- 每个文件 `--numstat` 都是 1 行插入、1 行删除。
- 唯一变化的行是 `verifier.sha256`：`acdc64a4d8f9…` → `d42ff0928a30…`。34 个新值都等于当前 `verify_round.py`。
- 把父提交与现文件按 JSON 逐字段比较，34 个文件都只有 `.verifier.sha256` 不同。`ledger_sha256`、`decisions_sha256`、`operations`、`apply_findings`、`status`、`base_candidate` 及其余字段没有变化。
- 样本：`batch-01/review/build-gate.json` 与 `batch-17/review/build-gate.json` 的 diff 上下文都是 `"path": "localization/editorial/r9-polish/tools/verify_round.py"` 下面那一行。

`verify_round.py` 本身不在 `e0e1193` 里；内容最后一次提交是 `b6a7151`。这次只是把 gate 里记下的哈希改成已经在库里的那个文件。

## 5. 工具

通过，对本批落地的 27 行不会误伤脚本。

`tools/scan_batch19.py`：

- 替换只发生在成对引号上（`scan_batch19.py:30-31`、`:52-70`）。内部没有汉字的对原样返回；不跨行。函数本身改不了空格、前缀、`[]`、`|`、`$`。
- 跳过脚本行（`:42-49`）：去空白后以 `{` `}` `#` `<` 开头；或以 `include `、`if `、`else`、`do ` 开头；或行内有 `&&`／`||`。再要求行内有汉字。
- 跳过含 LF／CR 的字典值（`:99-100`）。candidate47 上因此留下的含汉字直引号对正好 3 处，candidate48 未改（见第 6 节）。
- 本批 27 行的前缀只有对白说话人（`  Yiffany:`、`  Bossu:`、`  Mauser:`、`  Tomcat:`）、`  * `，或普通正文／词典值。没有 `<`、`include`、`if`、`&&`、`||`。

判断：这 27 行是玩家可见正文，不是脚本。扫描器不是完整脚本解析器——`if(`、`include{`、行中才出现的标签、以及不以这些前缀开头的 `while`／`return` 不会被跳过。那是重扫时的残留风险，不是本批已经改坏的行。`scan_vsn`（`:115-118`）用空 `except` 吞掉解密失败，只会漏扫，不会改坏脚本。

`tools/make_decisions_batch19.py`：表头 9 列（`:20-21`），与 `verify_round.py:29-30` 的 `COLUMNS` 一致。`␊`（`:12`、`:30`）只替换 `\n`，写出时用 `newline=''` 和显式 CRLF（`:34-35`）。本批 0 个哨兵，因为多行值已被扫描器跳过。台账展开哨兵的是 `build_ledger.py:48-50`，不是 gate 校验器。`verify_round.py:37-48` 的 `effective_final` 不展开 `␊`，所以多行值若写进 TSV，现有 gate 会按逐字比较拒绝。文档把这说成「先做多行值通道」是对的。

`localization/optimization/r28/r9polish/component.json`：`batches` 35 项，末项是 `batch-19`（`:383-391`）。`ledger`、`gate`、`decisions` 三个路径以及 `required_data` 里的三条相对路径都存在。

## 6. 文档与事实

27 行、3 处多行卡面、337 处 Fenfen 的行数对得上。sfw／nsfw 拆分和 39 处 actor 对不上。三份指定文档都没有把断词或 Fenfen 说成已经改完。

对得上的：

- 27 行：台账、决策、gate、`orders/batch-19.json` 都是 27。
- 3 处多行卡面：candidate47 与 candidate48 的 `datav/1` 用同一条扫描规则（含汉字的直引号对，且值里有换行）得到 3 处，两侧值相同，没有被本批改掉。jar 只有 `ui.card.CosmoCardRedbull.desc.Front`；pak 是 `ui.card.CosmoCardDragon.desc.Front` 与 `ui.card.CosmoCardRedbull.desc.Front`。`ROUNDUP.md:111` 的「Dragon、Redbull ×2」与此一致。
- 337 处 Fenfen：`out/layout/probe/fenfen-hits.json` 有 337 行、31 个 scene。`LEFTOVERS.md:95-99` 与 `ROUNDUP.md:65` 写的是未处理，不是已改。
- 断词：`LEFTOVERS.md:89-93` 写未处理。3,185／3,087 与 `out/layout/dialogue/wordbreak-stats.md` 首行一致。`PixelLayout.java:12` 确有 CR/LF 与 U+2028 显式换行；`editorial_repairs.py:37-39` 对非 JSON 行只放行 `\t`。
- 引号字模：`candidate48/fonts/story12.fnt` 里 `"` 为宽 7 高 5、yoffset -1，`'` 为宽 6 高 5，汉字样本 U+4E00 为 12×12、xadvance 12。与 batch-19 的理由一致。
- 回归与封签：`batch-19/README.md:35-38` 的 17 步、785／781／0、`passed_cpu_and_independent_review_not_real_clip_CRT_input` 与 `candidate48/acceptance.json` 一致。`tests/candidate48/results.json` 17 步 exit code 都是 0，sha256 `f400537a1b36…` 与 acceptance 的 `cpu_regression.results_sha256` 相同。本次没有复跑回归。

对不上的见阻断。没有把「3 处卡面、断词、Fenfen」说成已经落地。

## 阻断

1. **sfw／nsfw 写成 13／14，数据是 12／15。** `batch-19/README.md:27` 与 `out/layout/ROUNDUP.md:111` 写「sfw 13、nsfw 14」。决策表 `scene_id`、工单 mode、台账归档三处都是 sfw／jar 12、nsfw／pak 15。27 这个总数是对的，拆分错了 1。

2. **39 处 actor 在引用的数据里是 0。** `LEFTOVERS.md:99` 与 `ROUNDUP.md:66` 写 337 里有 39 处是说话人槽位 `Fenfen: [...]`，并指向 `out/layout/probe/fenfen-hits.json`。该文件 337 行里子串 `Fenfen:` 出现 0 次；`speaker` 字段全空。candidate47 两个归档里能解码的 `datadf/1`、`datadm/1`、`datav/1`、`vsn/*` 文本，也没有 `Fenfen:` 说话人行。探到的行首是「Fenfen故事第 N 部分」这类词典标题，不是 actor 槽位。因此「298 处可改、39 处不能碰」这组算术没有数据支撑。Fenfen 本身仍标为未处理，这一点没有说成已做。

## 观察

1. 337 对的是探到文件的行数。同一文件里子串 `Fenfen` 出现 341 次（4 行各有两处）。若「处」指出现次数，则少计 4；若指命中行，则与 31 个 scene 一起对得上。
2. `LEFTOVERS.md:87` 把两枚键名和「jar 与 pak 各一份」写在一起，读起来像两边各有一份。现场是 jar 1 处（仅 Redbull Front）、pak 2 处（Dragon Front + Redbull Front）。总数 3 与 `ROUNDUP.md:111` 一致。jar 的 Dragon Front 有换行，但没有含汉字的直引号对，扫描器本来就不会改。
3. `ROUNDUP.md:100` 把逗号写成 4×4。字模表 `char id=44` 是宽 5 高 5。句号 4×4 是对的。引号尺寸没有写错。`batch-19/README.md:5` 写逗号「4–5」，比 ROUNDUP 宽。
4. glossary 实际是 `Fenfen,种族名,芬芬,,proposed`（`localization/review/glossary.csv:5`，芬芬与 proposed 之间多一个空列）。文档写成 `Fenfen,种族名,芬芬,proposed`。
5. 同一次提交改过的 `localization/editorial/r9-polish/README.md` 边界节仍是旧口径：`:232` 与 `:244` 写未生成 `acceptance.json`，但 `candidate48/acceptance.json` 在；`:238` 仍写已落地 batch-01～16；`:241` 仍把 LIGHTTAZER 放在待终裁；`:243` 仍写正文 124 处 Fenfen。这是过时陈述，不是把未做的事说成做了。
6. 扫描器的脚本跳过是前缀和运算符启发式，见第 5 节。本批没有误伤；下次全库重扫不能单靠这份跳过表。
7. 本批决策没有用到 `␊`。校验器仍不展开它，多行通道还没做，与「3 处暂不改」一致。
8. 未复跑 17 步回归，也未重算 gate 的 dry-run 哈希。现有 `results.json` 与 acceptance 的哈希一致。未看 `quote-before.png`／`quote-after.png` 的画面。未启动游戏。

## 未覆盖

- 没有重跑 `verify_round.py` 或 `editorial_repairs.apply_entries`，因此不能独立再生 `dry_run.after_resource_sha256`。
- 没有重跑 `tests/candidate48` 的 17 步。结论只覆盖已有产物与本次读到的文件。
