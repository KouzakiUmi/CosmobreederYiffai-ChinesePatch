可推送

观察：4 项（均不阻断推送）。

独立只读核验。快照：`HEAD = f0d7637`（`release: seal candidate47 and build alpha0.2`），工作区干净，`origin/main` 落后 55 个提交；本报告是本轮唯一新增文件。未安装、未启动游戏、未跑构建或回归、未做任何 Git 写操作；构建产物与归档仅做哈希与明文读取。

---

## 1. 译文改动 batch-17 与台账

核验文件：`localization/editorial/r9-polish/batch-17/review/decisions.tsv`、`localization/translations/editorial-r9-batch-17-repairs.jsonl`。

- **列数**：`decisions.tsv` 共 14 行（1 行表头 + 13 行数据），逐行 `split('\t')` 均为 9 列，0 行异常；表头为 `finding_id / route / severity / category / scene_id / row_id / decision / final_zh / reason`。行尾为 CRLF（14 个 `\r\n`），与 batch-16（4 个 `\r\n`）等既有批次一致，不是本批引入的偏差。
- **台账**：13 行，逐行 `json.loads` 全部成功，无空行；每行均含 `op_id / archive / archive_entry / kind / before_resource_sha256 / old / new / finding_ids / source_refs`，`op_id` 13 个互不重复（`R9-0001`…`R9-0013`）。
- **差异白名单**：对 13 行逐条把 `old` 施加三类替换（`干员→特工`、`光电击器→光击枪`、`光刃电击器→光击枪`）后与 `new` 逐字节比较，**13/13 完全相等**；反向用 `difflib` 取差异段，5 行（`R9-0003/0005/0007/0008/0012`）被切成两段，原因是 `光电击器→光击枪` 内部先删 `电` 再换 `击器→击枪`，差异段仍全部落在白名单替换内，无第三类改动。
- **结构保留**：13 行的行首前缀（`  * `、`  Bossu: `、`  Mauser: `、`text: `）、行尾无空白、`[` `]` `|` `$` 计数在 `old`/`new` 中逐一相等，0 处异常。
- **表内与台账一致性**：`decisions.tsv` 的 `final_zh` 与台账 `new` 13/13 逐字符相同，`decision` 全为 `apply`，`scene_id` 与 `source_refs[0]` 13/13 相同；`build-gate.json` 的 `operations: 13` 与 `decisions_total: 13` 与之相符。
- **落地与残留**（超出本项要求，补充证据）：独立复跑 `tools/verify_readback.py r9-polish-candidate47`，输出 `operations_checked: 758 / locations: 756 / problem_count: 0`，退出码 0；batch-17 是链上最后一批，其 13 条 op 不可能被后续批次覆盖。另用 `codec.decrypt_file` 全量解密候选 47 的两个归档扫描旧术语：jar 8429/8429 条目、patch.pak 442/447 条目（另 5 个是 0 字节目录条目 `datadf/ datadm/ dataq/ datav/ vsn/`），`干员`、`光电击器`、`光刃电击器` **残留 0 处**——即本批三项替换在整库范围内已无遗漏，不存在"漏改同义写法"的需求缺口。
- 哈希：台账 `91fc37f0b1addc39…`、`decisions.tsv` `dcda3b0f6d330441…`、`build-gate.json` `81777687d1174e3b…`，与 `build-gate.json` 内记录的两个哈希一致（另见第 2 项 gate 复算）。

结论：本项无阻断、无观察项。

## 2. 封签脚本 `localization/optimization/r28/integration/finalize_r9_acceptance.py`

逐条对照其自称的校验，均为**真值比较**，不是存在性判断：

| 声称校验 | 实现位置 | 实际做法 | 判定 |
| --- | --- | --- | --- |
| manifest 状态与版本 | `:50-58` | `full_component_set is True`、`status == 'integrated_candidate_not_real_clip_CRT_input_acceptance'`、`version == 'r28-full-opt-candidate'`、`game_started`/`user_save_accessed` 必须为假 | 真校验 |
| 两个归档 SHA | `:60-63` | 现场对候选目录两个归档算 sha256，与 manifest 记录的 `archives[name]['sha256']` 逐值比较 | 真校验 |
| 17 步回归 | `:65-75` | `status == 'passed_cpu_only_not_real_clip_CRT_input'`、`len(steps) == 17`、任一 `exit_code` 非零即拒、`candidate_sha256 == 候选 jar sha`、`test_sources_unchanged_after_run` 必须为真 | 真校验（步数/退出码/候选 SHA/源未变四项齐全） |
| 34 份 gate | `:78-88` | 遍历 `component.json['batches']`，逐个要求 `status == 'verified_for_application'`，并现场对 `ledger` 与 `decisions` 算 sha256 与 gate 记录逐值比较 | 真校验 |
| 明文读回 0 问题 | `:90-93` | 子进程跑 `verify_readback.py`，非零退出即拒；`verify_readback.py:62` 在 `problems` 非空时 `SystemExit(1)`，故"0 问题"由退出码等价保证 | 等价成立 |
| 写出状态字符串 | `:96` | 硬编码 `passed_cpu_and_independent_review_not_real_clip_CRT_input` | 与消费方一致 |

- **放行路径排查**：全文 124 行无 `try/except`、无 `except: pass`、无提前 `return`；所有失败分支都是 `SystemExit`/`ValueError`/未捕获异常（均非零退出），无 `if` 写反（`not is_relative_to` → 拒、`not test_sources_unchanged_after_run` → 拒、`any(exit_code)` → 拒、`!=` → 拒，极性均正确）。`:47-48` 拒绝覆盖已存在的 `acceptance.json`，无法用旧记录覆盖新候选。`:40-45` 限定 `--candidate` 必须在 `localization/builds` 下、`--tests` 必须在 `integration/tests` 下。
- **"任意候选放行"不可行**：即便伪造 `build-manifest.json` 与 `results.json`（两者都是自报文件），`:90` 的读回会真实解密候选归档，把 758 条台账的 `new` 文本逐条比对候选明文——内容对不上即退出非零。这是本脚本最强的一条真实约束。
- **状态字符串闭环**：`acceptance.json` 的 `status` 实测为 `passed_cpu_and_independent_review_not_real_clip_CRT_input`；消费方 `tools/build_alpha_release.py:33` 要求的字面量与之逐字符相同（另注意 `finalize:66` 比较的是**另一个**近似串 `passed_cpu_only_not_real_clip_CRT_input`，两处未混淆）。
- **记录与当前磁盘一致**（复算，非仅读记录）：候选 47 的 `build-manifest.json` 为 `version=r28-full-opt-candidate`、`status=integrated_candidate_not_real_clip_CRT_input_acceptance`、`full_component_set=True`、`game_started=False`、`user_save_accessed=False`；34 份 gate 逐份复算 `status` 与 `ledger/decisions` 哈希，**漂移 0 份**；`component.json` 哈希与记录相符（`e05b03cb5ff6e3d4…`）；`tests/candidate47/results.json` 为 17 步、退出码 `[0]*17`、`candidate_sha256=06c9515b…`（等于候选 jar）、`test_sources_unchanged_after_run=True`，其文件哈希 `d2b4983eff90095d…` 与记录一致。

本项无阻断，观察 3 条（见「观察」O1–O3）。

## 3. 构建脚本 `tools/build_alpha_release.py`（新增 `--label`）

- **`--label` 影响面**：`:81` 默认 `alpha0.1`；实际只用于 `:150-151` README 内的两条命令示例、`:152` Python ZIP 文件名、`:173` 与 `:65` 的 EXE 文件名（`--name`）。载荷清单 `:119` 的 `version` 是硬编码字面量 `'alpha0.1'`，与 `--label` 无关。
- **`version` 未被 label 污染**：实测 `dist/alpha0.2/payload/manifest.json` 的 `version == "alpha0.1"`；`src/cosmobreeder_patch/installer.py:25` 只接受 `version == 'alpha0.1'`，且 `:139` 的 `verify(payload)` 会在构建期就跑这条校验。`build-report.json` 的 `installer_protocol` 亦为 `alpha0.1`，`--verify-payload` 的期望输出（`:183`）同样是 `{'version': 'alpha0.1', 'status': 'verified', 'game_started': False}`。
- **不传 `--label` 时**：`a.label` 默认 `alpha0.1`，`exe_command(..., label='alpha0.1')`（`:60`）默认值相同，`:152`/`:173` 的产物名与改前一致，`:150-151` 的 README 命令指向 `alpha0.1`——默认值与默认参数均与改前等价。
- **消费方绑定**：`target_identity`（`:21-42`）对 r28 候选要求 `acceptance.status`、`acceptance.archives`、`acceptance.build_manifest_sha256`、manifest 的 `full_component_set/version/status` 与两个归档 SHA 全部匹配，否则抛 `ValueError`；候选 47 实测全部匹配，故 `dist/alpha0.2` 的构建前置条件成立。`:119` 的写法是 `{'version': 'alpha0.1', ..., **identity, ...}`；`identity` 只含 `baseline/build_id/candidate/integration_baseline` 四个键、不含 `version`，展开顺序不会覆盖 `'alpha0.1'`，无风险。

本项无阻断，观察 1 条（见「观察」O4）。

## 4. 发行产物 `dist/alpha0.2/`

- **`SHA256SUMS` 26 行全核**：逐行按 `<sha>  <相对路径>` 重算磁盘文件，**26/26 全部一致，0 处不匹配、0 处缺失**。目录内共 27 个文件，唯一未列入的是 `SHA256SUMS` 自身（脚本先算行、后写文件，符合预期）。
- **`acceptance.json` 的 `archives`**：`cosmobreeder-multi.jar = 06c9515b98f3d7b3d3f96ead769687d53d81a39f34a2ddcdcac110d4ebbd6fec`、`patch.pak = 33479da8936c17a2039138990a20dcbf1a78b4cbd9657858fa31f29544b9345f`，与 `localization/builds/r9-polish-candidate47/` 两个归档的现场 sha256 **逐值相等**；`build_manifest_sha256 = 6ea65bb5c0f15593…` 也等于候选 47 的 `build-manifest.json`；该文件与候选 47 的 `acceptance.json` **逐字节相同**。
- **`payload/manifest.json`**：`version == "alpha0.1"`（`installer.py:25` 唯一接受值）；`target_sha256` 位于 `files[<archive>]` 之下，两值分别为 `06c9515b98f3d7b3…` 与 `33479da8936c17a2…`，等于上述归档 sha。载荷目录仅 `manifest.json` + 两个 `.cbd`，两个 delta 的现场 sha256 与大小均与清单记录一致，无 `*.reconstruction-check` 残留、无 `build/` 工作目录残留。
- **内层一致性**：`CosmobreederYiffai-alpha0.2-python.zip` 内 `cosmobreeder_patch/payload/manifest.json` 的 `version` 同样是 `alpha0.1`，`files[].target_sha256` 同上；`README.md` 为合法 UTF-8（524 字符），其中命令示例用 `alpha0.2`，与 label 一致。`build-report.json` 记录 `reconstruction` 两份 `byte-for-byte-equal`、三项检查 `exit_code: 0`、`exe_name = CosmobreederYiffai-alpha0.2-setup.exe`、`exe_sha256 = 09d441ec65fe4e89…`（与 `SHA256SUMS` 中该行一致）。
- **推送体积**：`dist/` 与 `localization/builds/` 均在 `.gitignore` 内、`git ls-files` 计数为 0，55 个提交不含发行二进制（最大的两个产物 70.8 MB / 59.5 MB 因此不会进库），无 GitHub 单文件 100 MB 上限风险。

本项无阻断、无观察项。

---

## 阻断

没有。

## 观察

1. **O1 17 步只钉数量与退出码**（`finalize_r9_acceptance.py:68`）：`len(steps) != 17 or any(s.get('exit_code') for s in tests['steps'])` 不校验步骤名称/顺序，也不校验 suite 标识；且某步若**缺** `exit_code` 字段，`s.get('exit_code')` 返回 `None`（falsy）会被当作通过。当前 `results.json` 17 步全为 `exit_code: 0`，实际无风险；若要收紧，可改成 `s.get('exit_code') != 0` 并钉住步骤名。
2. **O2 批次数量无下限断言**（`:78-88`）：gate 集合完全取自 `component.json['batches']`，脚本不断言其长度为 34、不查重。若该文件被改成空列表，`verify_readback.py` 会以 0 操作通过（`problem_count: 0`），seal 仍会写出 `passed…` 状态。当前 `component.json` 有 34 批且其 sha256（`e05b03cb5ff6e3d4…`）已写入 `acceptance.json`，产物可追溯，风险仅为未来重跑时的宽松点。
3. **O3 读回结论依赖退出码、JSON 截取较脆**（`:90-93`、`:104-107`）：脚本自身不再断言 `readback['problem_count'] == 0`，只信 `verify_readback.py` 的退出码（该脚本 `:62` 确实 `SystemExit(1 if problems else 0)`，等价成立，故不是漏洞）；另 `output[output.index('{'):]` 在子进程前置输出含 `{` 时会解析错，属健壮性问题。
4. **O4 不传 `--label` 的"与改前一致"仅限命名口径**：`--label` 默认值与 `exe_command` 默认参数确实等价（第 3 项已核），但本轮同一 diff 还改了 EXE 构建参数（新增 `--noupx`、`--python-option X utf8`、`--hide-console hide-early`、工作目录由 `.local/release-audit/…` 改为输出目录下 `build/`、构建后追加 `verify(payload)`、`--verify-payload`/`--licenses` 自动复检、`SHA256SUMS` 与 `build-report.json` 生成、`README.md` 生成、r28 候选的 `acceptance.json` 与字体声明复制）。这些与 label 无关，但若"行为与改前一致"被理解为整体等价，则不成立——建议按"label 维度等价、其余为有意增强"来表述。

补充（不计入观察，仅备案）：候选链 `component.json` 中 `batch-06-part03` 的 `base_candidate` 为 `r9-polish-candidate23`，而 `r9-polish-candidate22` 存在却没有被任何 gate 当作 base（21→23 跳号，孤儿构建）。因 `build_candidate.py` 每次从冻结 r27（`BASE_PINS`）+ 全组件重建候选（"Build an isolated r28 candidate incrementally from frozen r27"），且读回证明 758 条台账全部落地，该跳号不影响候选 47 的内容；seal 只记录 base 名字、不校验线性，属记录层现象。

## 未覆盖

- 未执行构建产物 EXE 的 `--verify-payload` / `--licenses`（`dist/alpha0.2/build-report.json` 记录为 `exit_code: 0`，本次仅核对记录与产物哈希，未运行二进制）。
- 未做差分重建的独立复算（`build-report.json` 记 `byte-for-byte-equal`；本次未重新 `apply` delta，因会写出临时文件，超出本次"只新建一个报告文件"的约束）。
- 未做实机安装/启动/存档、GPU/CRT/裁剪渲染、4 张位图本地化——与 `acceptance.json` 的 `not_verified` 一致。
- 未复核译文语义质量本身（本轮只按需求核结构、哈希与落地，不评 `干员→特工` 等术语裁决是否恰当）。
