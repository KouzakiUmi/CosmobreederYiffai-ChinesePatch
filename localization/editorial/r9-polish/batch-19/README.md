# batch-19：直引号换全角引号

## 为什么做这一批

`fonts/story12.fnt` 里有两套字形：汉字是 12px 的，ASCII 是 8px 的（`"` 7×5、`'` 6×5、`,` 4–5）。这是「native12/CJK + original8/ASCII」的正常设计——拉丁小字配上拉丁引号没问题。问题是中文句子里出现了**直引号**：

```
念叨着"下、中、中、上……"，谁知道是什么意思！
```

那个 `"` 是 8px 字形，夹在 12px 汉字中间又小又偏（yoffset=-1），看起来就是错位。换成全角引号后与汉字同高同宽：

```
念叨着“下、中、中、上……”，谁知道是什么意思！
```

对照图：`out/layout/dialogue/quote-before.png`（candidate47）与 `quote-after.png`（candidate48）。图是用两个候选各自的真实字模渲染的同一行。

## 扫描口径

`tools/scan_batch19.py` 扫两个归档的 `datadf/1`、`datadm/1`、`vsn/*`、`datav/1`：

- 只改**引号对内含汉字**的配对；引号内是纯拉丁的保持不动（那里 8px 才配得上拉丁字，例如 `“SELECT”`、`“SPIKERS”`、`“DOWN”+“JUMP”`）。
- 跳过脚本行：`<标签>`、`include {...}`、`if/else`、含 `&&`/`||` 的行。`"` `'` 在脚本里是语法符号，改了会碎。
- 多行字典值（角色卡正背面）**暂不改**：TSV 单元格装不下换行，而 gate 的校验器按决策逐字比对回写值。3 处留给后续的「多行值通道」，已记入 LEFTOVERS。

结果：**27 行**，sfw 12 行、nsfw 15 行（jar 侧 `datadf` 3 + `datadm` 8 + `datav` 1；pak 侧 3 + 10 + 2）。

## 处置

全部 apply，理由一致：全角引号与 12px 汉字同宽同高；纯拉丁引号保持原样。决策表 `review/decisions.tsv`，台账 `localization/translations/editorial-r9-batch-19-repairs.jsonl`，gate `review/build-gate.json`（`verified_for_application`，27 决策 / 27 操作）。

## 验证

- 台账逐条核对：`old → new` 的差异**只有引号**（difflib 逐段比对，0 处意外差异）。
- 17 步 CPU 回归：`tests/candidate48` 全部 exit 0。
- 明文读回：785 个操作 / 781 个位置 / 0 问题（4 个被后续批次覆盖）。
- 封签：`candidate48/acceptance.json`，35 批，status `passed_cpu_and_independent_review_not_real_clip_CRT_input`。

## 顺带的工具改动

构建时发现 34 个旧 gate 记录的 `verifier.sha256` 与当前 `tools/verify_round.py` 不一致——`verify_round.py` 在某次未提交的编辑里变过，而 gate 没重算。逐批重跑 gate 后确认：**重建只改 `verifier` 一个字段**，其余字段逐字节相同。34 个 gate 因此重算，旧值保留在 git 历史里；candidate47 的 `acceptance.json` 保持原样（它记录的 gate 哈希对应 git 里的旧版本），candidate48 用重算后的 gate 封签。

## 未做

- 3 处多行角色卡值（`CosmoCardDragon`、`CosmoCardRedbull` ×2）的直引号。
- `,`、`!`、`?` 等半角标点在中文句中的情况：扫出来是 0 处（除了 `...`、`!!!!` 这类英文串）。
- 实机渲染：图是真实字模 + 真实折行规则，但没有对话框边框、背景与动画。
