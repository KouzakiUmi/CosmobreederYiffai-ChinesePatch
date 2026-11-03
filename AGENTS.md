# 项目维护入口

《Cosmobreeder Yiffai》简体中文补丁（本地仓库）。目标是让 Steam 版游戏的剧情、无线电、UI、道具与结局能连续读成通顺中文，同时不改动玩法条件、施受关系、信息揭示顺序与保护字段。

## 目的与验收

- **目的**：在原版 Java/libGDX 二进制上做源依赖差分补丁；发行物不携带完整替换归档。
- **验收分层**：语义正确（读得懂、作答对得上）／结构保留（actor、控制、动态占位符、行前缀）／视觉可读（字宽、分页、资料卡）／实机（安装、启动、存档）。四层分别留证，不用一层替代其余。
- **现状**：alpha0.2 测试版已构建（基于 candidate47，安装器协议仍为 alpha0.1）；本地已有 R1 粗校、R2 修复、R3 人名、R4 留置裁决、R5 创译、R6 纠错、R7 渲染判定、R8 谜题提示。R4 并入 candidate9、R5 并入 candidate10、R6 并入 candidate11、R8 并入 candidate12；R9 全正文精校三十四批依次并入 candidate13～47；排版与专名批 batch-19（中文引号）、batch-20（Fenfen→芬芬）、batch-21（多行卡面引号）、batch-22（续行不以标点开头）、batch-23（折行不切词）依次并入 candidate48～52，均通过 17 步 CPU 回归。**2,698 场／12,552 行已精校（90.3% 场、93.0% 行）**；剩余 291 场为 287 场不面向玩家的脚本串与 4 场位图资源（后者属图像本地化工艺线）。硬切容器的容量已用真实字模复核（角色卡 96、成就 60、数据书 200 个值，0 超限），合句留下的 1,709 个空尾行中 1,701 个由 240px 自动折行填满两行。
- **排版层剩余两项**（见 `localization/editorial/r9-polish/LEFTOVERS.md` 第五、七节）：折行切词已由 batch-23 修 1,180 行（断词 1,393→206 处），剩 206 处／137 行修不动（第一行占满 240px、词边界在搜索窗口外，挪动会改变显示行数）；行首标点由 batch-22 修 57 行，剩 1,074 行会改变分页。两者都卡在同一条线上：**再动就要接受显示行数改变**，那会连带改分页与动画节奏。机制已就绪（台账允许文本行插入 U+2028，条件是去掉断行符后与原文逐字相同；用 U+2028 而非 LF 以保持行号）。**文本精校与数据层排版复核已完成，实机验收未做。**

## 关键事实与取舍

- **基线**：原版归档 SHA 以 `localization/sources/archives.json` 为准；`backup/` 保存原版副本。**打补丁后的游戏目录不是英文源**——`datav/1` 解密即中文，取证前必须核对 SHA。
- **归档格式**：`cosmobreeder-multi.jar` 与 `patch.pak` 内资源为无扩展名编号条目，用 `localization/tools/codec.py`（Salsa20）解密。`patch.pak` 覆盖 jar 同键值；`datay` 仅存在于 jar。
- **无语音对白**：FMOD 事件库全为 Music/SFX，失真广播是文本风格装置，不存在可等的原音。
- **术语与人名**：正式裁决以 `localization/translations/character-names.json` 与 `localization/review/glossary.csv` 为准；`glossary.csv` 只作构建清单哈希输入，不参与自动替换。
- **修订落地**：改文一律写成来源锁定台账（`localization/translations/*-repairs.jsonl`），绑定归档、entry、整资源 SHA、精确旧值与定位器，由 `localization/tools/editorial_repairs.py` 校验应用；任何漂移整批拒绝。

## 维护约定

- 不覆盖历史证据：R1／R2／R3 的报告与台账保留原样，新结论写在新轮目录并引用旧记录。
- `localization/editorial/` 按轮次分目录；当前轮的 README 说明范围、结论分布与未做验证。
- 构建与回归入口：`localization/optimization/r28/integration/build_candidate.py`、`test_candidate.py`；不擅自安装、不启动游戏、不访问存档。
- 变更后同步本文件与相关轮次 README；未验证项明确写“未执行”。
- 合同语文本可能有三份（词典基础条目、`datay` 运行时 overlay、任务日志字段）：改一处要确认另外两处是否需要同步，`tools/r9_targets.py` 按 occurrence 记录定位，不按值反查。

## 索引

- 发行与构建：[README.md](README.md) · [docs/RELEASE-alpha0.2.md](docs/RELEASE-alpha0.2.md) · [docs/RELEASE-alpha0.1.md](docs/RELEASE-alpha0.1.md) · [docs/SOURCE_BUILD.md](docs/SOURCE_BUILD.md)
- 编辑审校：[R1 方案](localization/editorial/r1/TRANSLATION_PLAN.md) · [R2 修复](localization/editorial/r2/README.md) · [R3 人名](localization/editorial/r3-names/README.md) · [R4 留置裁决](localization/editorial/r4-pending/README.md) · [R5 创译](localization/editorial/r5-creative/README.md) · [R6 纠错](localization/editorial/r6-consistency/README.md) · [R7 渲染判定](localization/editorial/r7-render/README.md) · [R8 谜题提示](localization/editorial/r8-puzzle/README.md) · [R9 全正文精校](localization/editorial/r9-polish/README.md)
- 交接与恢复：[localization/editorial/HANDOFF.md](localization/editorial/HANDOFF.md)（当前状态、遗留项、精校批次进度与恢复步骤）
- 技术研究：[docs/](docs/) 下的排版、字体渲染、差分与 PAK 交付方案
