# 校对与审查工作流

先读连续场景与分支，再修订台词。两档同义对白、公共标签和术语对齐；原版有差异时保留各自的信息和占位符。

## 一、统一检查命令

```cmd
python tools\review_tool.py stats              :: 查看各分块译文覆盖率与软断行统计
python tools\review_tool.py scan               :: 规则预筛 -> 输出 review/findings.md 与 review/candidates.tsv
python tools\review_tool.py terms              :: 对照 review/terms.tsv 检查术语不一致（加 --apply 写回）
python tools\review_tool.py dedupe             :: 检查同文异译（对比去断行后的纯文本）
python tools\review_tool.py export             :: 导出 review/sheet_*.tsv 供批量人工/AI 校对
python tools\review_tool.py apply              :: 预览 review/sheet_*.tsv 的 revised 列差异（加 --write 写回，--build 顺带全链构建）
```

## 二、`scan` 检查项目与良性噪音说明

- `marker_mismatch`：占位符/引擎标记与原文计数不一致。注意 `THE0`→`The0`、`ACTUAL_HINTS`→`真正_有用的` 属于已知良性差异，其余须核对。
- `trailing_space`：英文原文行尾无空格而中文行尾多出半角空格（已豁免 `ui.end.*` 与 `ui.backers.*` 居中装置）。
- `halfwidth_punct`：汉语语境混入半角 `, ; : ! ?`（颜文字 `;3`、纯英文吼叫除外）。
- `explicit_line_head_punct`：`⏎`（U+2028）断行后新行以禁止行首标点开头。
- `untranslated`：含 ≥4 个连续字母且中英完全相同的行（失真广播 `Static`、`Starkill` 乱码电台属刻意演出，见 `review/findings.md`）。
- `term:<en>`：术语扫描命中后，结合完整句子与道具、人物、地点的实际用途核对。

## 三、术语表 `review/terms.tsv`

7 列 Tab 分隔，与 `WoC-ChinesePatch` 同契约：

```text
en ⇥ cn ⇥ variants(其他译法|分隔) ⇥ protect(保护片段|分隔) ⇥ mode(word|phrase) ⇥ exclude_en ⇥ note
```

- **只有已确定的术语才入表**；未决项记在[待办清单](../../review/worklist.md)，不写自动规则。
- 新版改动见[公开校对索引](../../review/scene-context-changes.jsonl)；旧双语材料留在本地或[历史提交](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/tree/647b908bb7a7f30ea14062d268bf251ca7c75442/localization)。
