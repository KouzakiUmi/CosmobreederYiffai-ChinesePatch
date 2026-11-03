# candidate43 封签材料清单（未封签）

本文件只回答一个问题：**要给 candidate43 生成 `acceptance.json`，得先有什么、绑什么、验什么**。这里是清单与现状，不是封签结果，也没有生成 `acceptance.json`。

当前状态一句话：candidate43 的**语义与结构证据齐了**，缺的是**封签脚本本身**（R3 那套脚本把 R3 的计数写死了，不能直接套用）和**实机层证据**（安装、启动、存档、真实 GPU／CRT／输入），后者本轮不做。

## 一、要绑进 acceptance.json 的产物

| 项 | 路径 | 现状 |
| --- | --- | --- |
| 候选归档（两个） | `localization/builds/r9-polish-candidate43/cosmobreeder-multi.jar` `…/patch.pak` | jar `e7245c85…`（45,841,980 B，114 个条目改动）· pak `5a3db829…`（13,588,075 B，84 个条目改动） |
| 构建清单 | `…/candidate43/build-manifest.json` | sha `3e7b9cdc…`；`status=integrated_candidate_not_real_clip_CRT_input_acceptance`、`full_component_set=true`、`installed=false`、`real_clip_CRT_input_verified=false` |
| 字体清单 | `…/candidate43/font-manifest.json` | 10 项；字体是多轮重打过 pin 的，必须与本次归档一同封 |
| CPU 回归结果 | `localization/optimization/r28/integration/tests/candidate43/results.json` | sha `0d11f450…`；`status=passed_cpu_only_not_real_clip_CRT_input`、17 步全 exit 0、`test_sources_unchanged_after_run=true`、`candidate_sha256` 与 jar 归档一致、`game_started=false`、`user_save_accessed=false` |
| 组件清单 | `localization/optimization/r28/r9polish/component.json` | sha `ccd8b6d0…`；30 批，台账／gate／decisions 30×3 个文件全部存在 |
| 逐批 gate | `localization/editorial/r9-polish/batch-*/review/build-gate.json` | 30 份，`status=verified_for_application`；每份绑 `ledger_sha256`、`decisions_sha256`、`verifier.sha256` |
| 逐批台账 | `localization/translations/editorial-r9-*-repairs.jsonl` | 30 份，合计 706 个操作 |
| 逐批裁决表 | `localization/editorial/r9-polish/batch-*/review/decisions.tsv` | 30 份，合计 1,086 条决定（采纳 706／驳回 344／留置 36） |
| 测试源 pin | `results.json:test_source_sha256` | 16 项；封签时需与工作树逐一对齐 |
| 构建源 pin | `build-manifest.json:source_sha256` | 需与工作树逐一对齐（构建脚本、组件、字体表） |

## 二、封签脚本必须做的校验（当前**没有**这样一个脚本）

R3 的 `localization/editorial/r3-names/tools/seal_candidate.py` 不能直接复用：它把 R3 的计数写死了（`operation_count==839`、`non_name_preserved==778`、`Tomcat.nickname_occurrences==3`），还引用 `r28-editorial-repairs-candidate6` 作为父候选，对 R9 链不成立。要封 candidate43，需要一个 R9 版脚本，至少覆盖：

1. **归档身份**：`acceptance.archives` 与候选目录里两个归档的实际 sha256／bytes 一致。
2. **构建清单身份**：`build-manifest.json` 的 sha 与记录一致，且 `full_component_set=true`、`status` 是 `integrated_candidate_not_real_clip_CRT_input_acceptance`。
3. **回归身份**：`results.json` 的 `candidate_sha256` 等于 jar 的 sha；17 步全 0；`test_sources_unchanged_after_run=true`。
4. **源 pin 不漂移**：`test_source_sha256`（16 项）与 `source_sha256` 逐项等于工作树当前文件。
5. **组件完整性**：`component.json` 的 30 批顺序与 gate 的 `base_candidate` 链一致（batch-12 三个 part → candidate40／41／42，batch-13 → candidate43），且每个 gate 的 `verifier.sha256` 等于当前 `verify_round.py`。
6. **台账身份**：每份 gate 的 `ledger_sha256`／`decisions_sha256` 等于台账／裁决表的实际 sha。
7. **明文读回**：`tools/verify_readback.py r9-polish-candidate43` 返回 0，且 `operations_checked=706`（本轮已跑过，0 问题；封签时应重跑存档）。
8. **解码一致性**：`datav/1`、`datay/1`、`datadf/1`、`datadm/1` 解密后的内容与 `tests/candidate43/` 里的输入副本一致（回归用到的输入必须来自同一份归档）。
9. **字体 pin**：`font-manifest.json` 的 10 项与候选里实际字体文件一致；字体若变，前面所有视觉结论都不再适用。
10. **不得写入的字段**：`installed`、`real_clip_CRT_input_verified`、`game_started`、`user_save_accessed` 必须保持 `false`，封签也不得把它们改成 true。

## 三、封签前还缺的证据（本清单不外推）

| 缺项 | 需要什么 | 谁能做 |
| --- | --- | --- |
| 产物能装进 Steam 版 | 安装流程脚本 + 安装后的目录快照（不是启动游戏） | 需要用户确认是否允许写游戏目录 |
| 真实启动与运行 | 实机启动、进入场景、读一段剧情的录像／截图 | 只能实机，且需用户在场 |
| GPU／CRT／输入 | 真实显示与手柄／键盘输入验证 | 只能实机 |
| 存档兼容 | 读取用户既有存档 | 涉及用户数据，需明确授权 |
| 视觉层复核 | 卡面 16 列、数据书 3 行、结局名单、`DragonHint` 4 行折行是否翻页；任务日志面板与词典标签的截断 | 实机或渲染复核 |

以上五项在本文件与 [README](README.md) 里一律记为「未执行」，不得用 CPU 回归结论替代。

## 四、下一步（按顺序）

1. 写 `localization/editorial/r9-polish/tools/seal_candidate.py`（R9 版），参数化：`--candidate`、`--tests`、`--component`，把第二节的 10 项做成硬校验，全部通过才写 `acceptance.json`。
2. 用 candidate43 跑一次 dry-run，确认它能拒绝"错误归档"（例如把 candidate42 的 results.json 配到 candidate43 上）——封签脚本必须先能挡住错配。
3. 用户确认实机层安排后，再决定是否把 `installed`／`real_clip_CRT_input_verified` 从 false 更新；在那之前 `acceptance.json` 即使生成，也只能是 `cpu_only` 级别的封签。
