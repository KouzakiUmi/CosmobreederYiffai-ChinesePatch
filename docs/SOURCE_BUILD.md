# alpha0.1 源码与构建边界

## 交付物与可复现性

alpha0.1 的公开交付目标是**自有补丁源码、经审核的翻译数据，以及差分补丁安装器**，不是游戏本体或完整汉化后的游戏归档。用户须自行拥有匹配版本的原版游戏；官方可选补丁也由用户自行取得。

当前本地目标基线为 `r27-story12-shaderfix-test5`（游戏 `1.0.5_full`）。它保留原字体接口，修复 story12 字格透明背景的红通道值；不靠移除字体源码/API解决发布问题。目标 JAR/PAK、历史安装器和研究缓存留在本地隔离，不随源码仓库公开。

**现状不是“干净克隆 + 完整原图 = 一键重建 r27”。** 旧流水线依赖此前的 r21 本地化归档、提取目录、组合字体、语料目录和历史测试夹具。alpha 差分封装与旧全量目标重建是两条不同的链路；能从本地 r27 制作差分包，不代表能从公开源码独立重建 r27。

## 推荐公开范围：逐文件 allowlist

下列为源码候选，不是对整个目录内容的许可背书。发布前核对各文件的版权、嵌入内容、机器路径和注释；尤其不要直接 `git add .`。

| 范围 | 处置 |
|---|---|
| [工具源码目录](<../localization/tools/>)中的 Python 源码 | 审核后公开；保留 codec、classfile、字体生成与审计工具。旧脚本可能硬编码本机输入，不承诺开箱即用 |
| [布局源码](<../localization/layout/src/>)、[Java 补丁工具](<../localization/layout/tools/java/>)、[构建脚本](<../localization/layout/tools/>)中的自有源码 | 审核后公开；只选 `.java`、`.py`，不带编译产物、下载工具链或反编译快照 |
| [Java 测试](<../localization/layout/tests/>)、[Python 测试](<../localization/tests/>)中的测试源码 | 审核后公开；有真实游戏输入依赖的测试须明确分组，不把缺夹具跳过当通过 |
| [旧打包源码](<../localization/packaging/>)中的 `.py`、`.spec` | 可作历史实现参考，须核对硬编码路径；不收录 payload、build、dist、二进制或生成 manifest |
| [依赖声明](<../localization/requirements.txt>)、本说明及经过筛审的技术文档 | 可以逐文件纳入；依赖声明尚不足以复现旧完整 EXE 构建 |
| [翻译数据目录](<../localization/translations/>) | 有条件纳入：译文贡献与原游戏原文不是同一授权范围，须先做数据级审核，不能只看扩展名 |
| [字体许可](<../localization/runtime/LICENSE-FusionPixel-OFL.txt>)、[字体声明](<../localization/runtime/NOTICE.txt>)、[字体元数据](<../localization/runtime/font-license-metadata.json>) | 可保留上游许可与归属说明；核验元数据后纳入。不因此允许公开组合纹理或原游戏字形 |

新的 [alpha 独立包源码](<../src/cosmobreeder_patch/>)、[delta builder](<../tools/build_alpha_release.py>)、发布测试及格式说明应纳入最小公开 allowlist。独立安装器消费已下载的差分负载，不依赖 catalog、runtime、历史 r21 或研究缓存。源码盘点在其并发落地之前完成，故本地清单中的 99 个历史源码候选不含这组新文件。

### 默认排除

- 所有原游戏或完整衍生归档、JAR/PAK/EXE、原游戏 JRE、下载 JDK、`.class`、反编译源码快照、完整图集和原图裁片。
- 根目录历史 PNG、历史脚本和脚本输出默认不纳入；历史 `.py` 不等于发布必需源码。应逐文件迁移审核，不直接导入根目录。
- `backup/`、`extract/`、`research/`、`build/`、`work/`、`t/`、`testgame*/`、`tg_*/`、旧 `translation/`。
- `localization/assets/`、`sources/`、`catalog/`、`builds/`、`work/`、`toolchains/`；这些包含原资源、解密快照、语境原文、测试游戏或生成缓存。
- `localization/reference/`、`batches/`、`drafts/`、`review/`、`reports/` 默认不公开：含原文、工作表、图片、模型交接及本机路径；确有必要的技术结论应另写精简文档。
- `localization/runtime/` 内全部 PNG、FNT 及 FNT 备份/临时文件默认不公开。组合图保留原游戏 ASCII 像素与指标；OFL 仅覆盖新增开源字体贡献，不能为整个组合资产重新授权。story12 API 生成的混合 PNG/FNT 同样不能直接当纯 OFL 字库发布。
- `localization/project.json`、代理状态、PID、缓存、权限恢复记录、机器目录/日志、凭据和会话数据。需要公开配置时应另提供不含本机路径的模板。
- `.local/`（包括本次本地审计清单）不是发布内容。

差分负载也须检查其实际格式与许可边界：文件名叫“差分”不保证没有完整资源；不把完整原游戏条目、完整图集或解密快照包装为“补丁素材”。

## 翻译数据盘点（2026-10-25）

仅核对结构和计数，未在本说明复制原文或译文。

| 文件 | 当前结构与发布风险 |
|---|---|
| [zh-CN.jsonl](<../localization/translations/zh-CN.jsonl>) | 8,973 条；8,146 `draft`、827 `untranslated`；8,146 条非空 draft，正式 translation 字段均为空。包含稳定 ID、原文哈希、审校状态与来源路径；草稿不代表全量精校或实机验收 |
| [dialogue-joins.jsonl](<../localization/translations/dialogue-joins.jsonl>) | 956 组合句；包含 inputs、原资源身份、物理位置及 merged_translation；需审核嵌套输入与上下文是否携带原文 |
| [jar-variant.jsonl](<../localization/translations/jar-variant.jsonl>) | 158 条；含 `source`、`translation`、变体、entry；不能宣称是无原文的纯译文表 |
| [layout-short-overrides.jsonl](<../localization/translations/layout-short-overrides.jsonl>) | 1 条；含 expected_r21、replacement、来源身份；属于依赖旧基线的覆写输入 |
| [dialogue-join-coverage.json](<../localization/translations/dialogue-join-coverage.json>) | 合句覆盖证据；作为候选数据单独审核，不能以 JSON 后缀直接放行 |

本地 [旧项目说明](<../localization/README.md>) 的 3,884 初稿进度已不代表上述权威数据快照；其中本机绝对路径和全量资源项目说明也不应原样充当公开根 README。

## 两条构建链

### A. alpha 差分封装：发布维护者

输入为用户/维护者本地持有的已知原版归档，以及冻结的 r27 目标归档。输出只能是差分负载、安装器、必要许可与哈希清单；完整目标 JAR/PAK 不进入公开资产。两档安装须对应已核验的原版/官方补丁身份，不能把任意用户目录当匹配源。

已对照 [builder 源码](<../tools/build_alpha_release.py>)核对以下参数（项目根目录执行；输出必须是尚不存在的新目录）：

```text
python -B tools/build_alpha_release.py --source <local-original-archive-directory> --target <local-r27-archive-directory> --output <new-release-directory>
```

默认 source 为本地 `backup`，target 为 r27 基线，output 为 `dist/alpha0.1`。源码使用标准库 COPY/XOR + zlib 差分，逐文件重建校验后删除自身新建的校验输出，生成 payload、Python 分发 ZIP 和 SHA256SUMS；不会把完整目标 JAR/PAK收录到 Python ZIP。构建输入含本地原版 JAR/官方 PAK与目标 JAR/PAK，不能仅凭已下载 payload 反向声称完成源码重建。可选 `--exe` 调用本机已安装的 PyInstaller 构建 Windows 单文件程序；PyInstaller 是额外打包依赖，不是标准库的一部分。本次未执行构建或安装依赖。

解压已发布的 Python ZIP，在含 `cosmobreeder_patch` 包的目录执行以下命令；使用其随包负载时可省略 `--payload`：

```text
python -B -m cosmobreeder_patch --payload <payload-directory> --verify-payload
python -B -m cosmobreeder_patch --payload <payload-directory> --game-dir <game-directory> --check
python -B -m cosmobreeder_patch --payload <payload-directory> --game-dir <game-directory> --install
python -B -m cosmobreeder_patch --payload <payload-directory> --game-dir <game-directory> --uninstall
python -B -m cosmobreeder_patch --licenses
python -B -m cosmobreeder_patch
```

无参数进入 Tk GUI（需要可用的 tkinter 图形环境）。如直接从仓库运行而非分发 ZIP，应先让 Python 的模块搜索路径包含 `src`；不要假设未安装的 src-layout 包能在根目录直接 import。安装器源码位于 [独立包目录](<../src/cosmobreeder_patch/>)，CLI 参数已对照 [入口源码](<../src/cosmobreeder_patch/__main__.py>)；本说明没有验证 pip 元数据或声称已执行 pip 安装。

原版（仅 JAR）与官方补丁（JAR/PAK）档位均按发布 manifest 的 SHA 身份匹配，具体兼容指纹由最终资产确定，不能仅凭版本字符串绕过校验。安装前自行备份存档并退出游戏；拒绝未知源与损坏负载、失败回滚及卸载恢复须由发布测试验证。本次盘点未执行安装器或游戏，CLI 静态核验不代表安全测试已通过。

### B. r27 全量目标重建：当前为研究态

真实入口为 [build_full_text.py](<../localization/layout/tools/build_full_text.py>)，继承 [build_dialogue.py](<../localization/layout/tools/build_dialogue.py>) 与 [build_layout.py](<../localization/layout/tools/build_layout.py>)。以下都是额外输入/限制：

| 输入/约束 | 如何得到、目前的限制 |
|---|---|
| 原版 `cosmobreeder-multi.jar`、可选官方 `patch.pak` | 用户自行取得匹配的 `1.0.5_full`，只在本地保留；旧构建会核验基线指纹，不得用新文件冒充 |
| `builds/final-8146-r21-images` 中本地化 JAR/PAK | 旧全量构建直接以 r21 为 BASE，包含此前译文、图片与扩展图集。不是只给原版游戏便可替代；尚未交付独立重建该 r21 基线的干净入口 |
| `extract/patch/datadf/all.ds` 与 `datadm/all.ds` | 必须从匹配官方归档本地解密提取。旧 text_resources 直接读取这些路径；提取目录不公开 |
| `catalog/{units,occurrences,resources}.jsonl` 与 `sources/blobs` | [提取器](<../localization/tools/extract_project.py>)可从用户原归档生成目录，本次将 GAME 输入改为 `COSMOBREEDER_GAME_DIR`（默认本地隔离输入目录），既有输出目录仍有防覆盖门禁；后续覆盖映射/追加校订不等于自动全部重放。不能直接运行便宣称重现当前最终目录 |
| default10/classic8 的组合 FNT/PNG | 从用户原游戏 ASCII/字体指标与开源 CJK 字体在本地组合；现有生成脚本仍依赖旧组合图、work 字符集、其他项目字体绝对路径等，缺少已验证的 clean-clone bootstrap |
| 官方 Fusion Pixel native12 ZIP | [story12 资产 API](<../localization/tools/build_story_font12.py>)记录上游 URL、ZIP/BDF SHA-256 与完整 OFL；当前全量构建固定从 `work/story-font12/font12.zip` 取源。仅开源 native12 ZIP 不能替代所需 default10 组合输入 |
| 字体覆盖语料 | story12 API 读取 units、当前译文、956 合句，并包含 default10 字符集；删掉语料会改变封存输出身份，不应为公开方便而绕过哈希门禁 |
| Python/图像依赖 | [requirements.txt](<../localization/requirements.txt>)记录 Pillow 11.3.0、openpyxl 3.1.5；全量构建 `--asset-python` 帮助却要求 Pillow12.3 资产环境。PNG 编码影响封存 SHA，须另冻结实际生产者环境；不得混称同一依赖集 |
| Java 工具链与运行时 | 脚本固定本地 Microsoft JDK 17 路径、research 内游戏 JRE；自有运行时代码以 Java 8 目标编译，工具用 JDK 内置 ASM exports。不分发整套本机工具链 |
| 历史 EXE 打包 | 旧脚本调用 PyInstaller，但未列入上述 requirements；旧安装器还准备完整 JAR/PAK payload，不是公开 delta builder |
| shader 回归夹具 | [test_story12_shader.py](<../localization/tests/test_story12_shader.py>)读取 r26 旧 JAR 的混合图及真实着色器，不能在无 r26 的干净克隆运行；r26 不应为满足测试而提交 |

因此本说明不提供旧 `build_full_text` 的“完整重建成功”示例，也不把复制全部历史构建作为依赖安装。应先补齐本地输入配置、原版到 r21 的可重放步骤、字体 bootstrap、测试夹具分层和依赖锁定，再宣称公开源码可独立重建最终目标。

## 本地可重建资产及边界

在已准备匹配组合字体、语料和官方 native12 ZIP 的研究工作区，字体 API 有已存在的 CLI（以下不是 clean-clone 操作，也不是 alpha 差分构建）：

```text
python -B localization/tools/build_story_font12.py --source-zip <official-native12.zip> --output <new-local-output-directory>
python -B localization/tools/build_story_font12.py --validate <local-output-directory> --source-zip <official-native12.zip>
```

API 同时提供 `build_story_font12_assets(source_zip)`：只返回 manifest/字节，由归档构建器直接收录，不要求提交 runtime 中间产物。输出含受保护的原 ASCII 区域，**只能作为用户本地衍生资产使用**；保留上游 OFL 及其归属说明，不公开完整混合图。

原始 PNG、FNT、解密文本和图集索引原则上从用户自备归档本地提取；中文组合图由源码及许可明确的上游字体生成。当前“有工具源码”不等于各历史路径均已参数化，也不等于当前 r21 图片与所有译文覆盖都有经验证的自动重放链。

## 测试分层与验收

- 新 alpha 安装器的自包含/合成夹具测试与旧真实游戏集成测试应分别报告。测试源码可以公开，真实归档/截图/着色器夹具不随之公开。
- 旧 Python 测试依赖 catalog、原版备份、提取 DS、runtime FNT/PNG；部分还导入 research 脚本。不能在源码包中默认承诺整个测试目录无外部输入。
- Java 布局/桥接/字体测试需要相应游戏类和字体；验证 JVM、CPU 绘制记录、真实窗口/CRT/clip、用户可玩性是不同层级。
- r27 构建声明的 CPU/隔离测试不等同本次审计重跑，也不代表完整游戏视觉验收。本次仅静态读取构建依赖、统计元数据、检查数据 schema/计数。
- 公开发布前检查源码/差分 allowlist、无完整归档与图集、许可归属、输入/目标哈希、安装/回滚/卸载结果，并独立验证 Release 资产与清单一致。
