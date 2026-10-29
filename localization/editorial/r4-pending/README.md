# R4：R2 留置项裁决

**本目录处置 [R2 的 45 条 defer](../r2/reports/repair-01/PENDING.md)，不是新的全文精校轮。** 3 条 reject 维持原判，不在此重开。

R2 的 defer 理由集中在三类阻塞：等不到的原音／演出证据、未核的嵌套 JSON 用途、尚未终裁的术语。三者本轮均以可复跑证据解除或重新定性，逐条结论见 [decisions.tsv](reports/pending-01/decisions.tsv)。

## 证据基础

[runtime-evidence.json](evidence/runtime-evidence.json) 由 [collect_evidence.py](tools/collect_evidence.py) 生成，脚本对归档 SHA 不符即拒绝取证。

- **取的是原版基线**：`backup/` 两份归档 SHA 与 `localization/sources/archives.json` 记录一致（jar `cd37e445…`、pak `2f9da7d4…`）。游戏安装目录当前处于已打补丁状态（jar `e4ebec61…`），其 `datav/1` 解密即为中文，**不能当英文源**。这一点此前分析曾误用，已纠正。
- **无语音对白**：JAR 内 `audio/0–3` 解密后为 FMOD manifest 与 Master 事件库，217 个事件全部属 `Music`／`SFX`；与对白相关的仅 `event:/Music/Radio` 电台音乐，无 voice／vox／dialog／speech／line 类事件。失真广播是纯文本风格装置，不存在可等的原音演出。
- **字典与运行时数据可直接解密**：`datav/1`（dictionary）、`datay/1`（scripts_pack）用项目 [codec.py](../../tools/codec.py) 解出，`ui.breeding.*` 85 键、`ui.end.BadEnding.l0–l9`、`SpecialFap.ElfBuff.desc`、`shops/*/Area0_Macsen1/products/2` 等容器与键名均实测存在。

## 关键推翻

**`HARD KNOTTED|BRED` 是官方刻意写的荤双关，不是 BREAD 拼误。** 基础 JAR 原文为 `TWISTED BREAD|BAKED FRESH`，官方 `patch.pak` 把它改成 `HARD KNOTTED|BRED`。同一字典组的 `StatPepper.desc` 原文 `BIG AND SPICY BUT ADDICTIVE` 也是同样调情口吻。R1 的“改成硬脆打结的面包”提案方向错误，不予采用；本轮按 `apply` 重写为“硬结打卷|育得正好”。

**`OLD JUNK` 不是店铺名。** 真实位置是 `shops/{male,female}/Area0_Macsen1/products/2/displayName`，商品 `CosmoBody`（9999 Lect，`!hasItem(CosmoBody)`），商品本名 `STARSUIT`／“制装”。这是 Macsen 把制式特工制服当“破烂”兜售的伪装展示名。现译“旧货铺”确实读反了，R1 的“旧杂物”方向对、但需按商品展示名锁定口径。

**坏结局大字没有顺序错乱。** `ui.end.BadEnding.l6=特蕾还`、`l7=在外面`、`l8=那里……`，按键号递增绘制即读作完整句；R1 阅读稿的错乱印象来自按源字符串顺序展示，不是实际演出。

## 处置口径

| 结论 | 条数 | 含义 |
| --- | ---: | --- |
| `apply` | 10 | 阻塞解除，本轮给出确定新文，共 13 个来源锁定操作 |
| `close_no_change` | 8 | 阻塞解除且现译成立，不改文，仅结案 |
| `close_upstream` | 6 | 源数据自身瑕疵／错位，中文跟随源文是正确行为，标记上游并结案 |
| `style_rule` | 8 | 失真残片类，无原音可等；统一定为“保残片形态”，不做补全 |
| `defer` | 13 | 仍缺可核证据或无可靠中文方案，保留并写明下一步取证路径 |

数字相加 10+8+6+8+13=45。

## 未解除的部分

- **创译硬骨头仍在**：mine 多义冷笑话（P08-013）、`NA-NO-MY-WHAT ANAL` 音桥（P02-009）、`beat off`（P07-025）等，中文方案尚未成立。这些不是证据问题，是需要整组试读的创作问题，本轮不硬凑。
- **源文本身异常**：`SENSOR DARK`、`TR...MIS...ATE` 类残片，即使有文本内证也不足以唯一还原。保留原文异质感优于编造。
- **未做的验证**：本轮未构建候选、未跑 CPU 回归、未安装、未启动游戏、未访问存档；归档、安装器与正式译文库未改。`apply` 的 10 条已写入来源锁定台账并 dry-run 通过，需在下一候选构建时才进入归档。

## 候选与回归

R4 已作为构建组件 `r4pending` 接入流水线，产出 [candidate9](../../builds/r4-pending-candidate9)：

- 13 个操作全部落地，10 条 apply 生效；相对 candidate8 只有 3 个文本资源变化，另加 1 个新字形 U+60EC「惬」。
- R2 778 项、R3 839 项保留状态在 c8/c9 完全一致，无回归。
- 17 步 CPU 回归全部 exit 0；未安装、未启动游戏、未访问存档。
- 未生成 `acceptance.json`：正式封签需绑定与本次归档一致的上游复核记录。

详见 [构建与回归报告](reports/pending-01/BUILD.md) 与 [候选复核](review/candidate9-review.json)。

## 验证

- [collect_evidence.py](tools/collect_evidence.py)：归档 SHA 与 `archives.json` 不符即拒绝取证。
- [verify_decisions.py](tools/verify_decisions.py)：独立重解定位器，13/13 操作的旧值与整资源 SHA 实测存在。
- [make_gate.py](tools/make_gate.py)：生成 `build-gate.json`，构建时重算比对。
- [review_candidate.py](tools/review_candidate.py)：候选级独立复核，17 项断言 PASS。

## 文件

- [逐条裁决](reports/pending-01/decisions.tsv) · [总览](reports/pending-01/SUMMARY.md) · [构建与回归](reports/pending-01/BUILD.md)
- [运行时证据](evidence/runtime-evidence.json) · [采集脚本](tools/collect_evidence.py)
- 台账：[editorial-r4-pending-repairs.jsonl](../../translations/editorial-r4-pending-repairs.jsonl)（apply 项）. 术语终裁见 [glossary.csv](../../review/glossary.csv)

## 后续

13 条 `defer` 中已有 5 条在 [R5](../r5-creative/README.md) 完成中文创译并并入 candidate10：P02-009、P05-020、P07-025、P08-013、P10-011。其余 8 条中又有 5 条在 [R6](../r6-consistency/README.md) 处置（含对本轮 Bumper 与道具名判断的更正），剩 P08-022、P01-035、P03-033；其中 P03-033 经 [R7 渲染模拟](../r7-render/README.md) 判定可结案（11 行是全局卡面结构、现译不越界），P08-022 已在 [R8](../r8-puzzle/README.md) 改为“不相邻”并并入 candidate12；现在只剩 P01-035（`MAGs`）一条留置。本轮裁决表与门禁不因 R5 回改，保持候选9 的封签口径。
