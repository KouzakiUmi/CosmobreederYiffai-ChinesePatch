# Cosmobreeder Yiffai 简体中文补丁

**《Cosmobreeder Yiffai》的非营利性简体中文汉化补丁，仅面向 PC（Steam）版。**

![Status](https://img.shields.io/badge/Status-Alpha-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square)
![Engine](https://img.shields.io/badge/Engine-Java%2017%20%2B%20libGDX-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)

> **By KouzakiUmi (呜咪 / 神前海)**

---

**项目说明**：本补丁覆盖开场、剧情字幕、无线电、Continue 窄栏、道具与结局报告，并为每类场景单独适配 12px / 10px / classic8 像素字体与换行宽度。发行物是**依赖原文件的二进制差分**，不携带完整替换 JAR/PAK、游戏图片音频、原游戏 JRE 或存档，因此**不能脱离匹配的原游戏独立运行**。

| 项目 | 说明 |
| --- | --- |
| 适用游戏 | Cosmobreeder Yiffai `1.0.5_full`（Windows），原版档或官方可选 NSFW 补丁档 |
| 游戏引擎 | Java 17 + 自带 Temurin JRE 17.0.6；libGDX 混淆于 `PRG/*`，另有 Scala 3 / FMOD / Steamworks4J |
| 基线校验 | `cosmobreeder-multi.jar` 的 sha256 `cd37e445...`；官方补丁档另校验 `patch.pak` `2f9da7d4...`，不匹配拒绝写入 |
| 发行基线 | `r27-story12-shaderfix-test5` |
| 载荷 | 2 个源依赖差分：`cosmobreeder-multi.jar`（44.8MB → 45.6MB）、可选 `patch.pak`（12.5MB → 13.3MB） |
| 当前版本 | alpha0.1（预发行 · 未签名） |
| 运行要求 | 独立 EXE 无需 Python；Python 运行版需要 Python 3.12 |
| 翻译进度 | 译文快照 8,973 条，其中 8,146 条有草稿、827 条尚未翻译 |

---

## alpha0.1 更新（2026-10-25）

首个公开源码与差分安装器版本。

- **分场景中文排版**：开场、普通全宽剧情与结束叙事报告使用独立原生 12px 字体，约 20 汉字 / 240px 换行；无线电 10px / 约 15 字；Continue 窄栏 10px / 约 8 字；道具中文名称与说明走 classic8；存档界面保留原布局。
- **保留原逻辑**：原打字机、分页与事件处理不变，合并 956 组原始续句，来源不匹配的变体不强套；修复窄栏分页完成时可能漏末字的问题。
- **修复透明字块**：新字库的透明 RGB 与原游戏终端着色器的红通道采样不兼容，会让空白格被当成整格黄色笔画；本版修正 story12 字格透明背景取值。
- **新的源依赖差分协议** `CBDELTA1-COPY-XOR`：发行物不再携带完整替换 JAR/PAK，安装时校验源文件、差分负载与重建目标的完整 SHA-256。
- **事务化安装**：先在系统临时目录重建并校验全部目标，再建立本次专属备份与 journal，逐文件同盘原子替换；异常回滚、受测中断可恢复，未知文件一律不覆盖。
- **公开源码与许可**：自有补丁源码、去私有溯源字段与原文上下文的译文贡献快照、完整第三方许可文本；历史全量构建输入与研究缓存留在本地，不进入仓库。

---

## 📥 下载与安装

从 [alpha0.1 预发行页](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases/tag/alpha0.1) 下载 **Windows 独立安装器**，或下载 **Python 运行版 ZIP**。

1. **完全退出游戏**，自行备份存档。
2. 如果装过 r23–r27 等旧测试版，先使用对应旧安装器「卸载 / 还原」；**不要强制覆盖未知文件**。
3. 将安装器放在方便访问的位置，选择包含游戏 JAR 的目录，先「检测档位」，再「安装汉化」。
4. 安装器只接受发布清单中 SHA-256 匹配的原版文件，并自动区分原版与官方可选补丁档位；未知版本会拒绝修改。
5. 首次进入游戏，复测开场、剧情、无线电、Continue、道具和结局报告。需要还原时使用本版安装器，**勿手工删除备份**。

安装器不自动启动游戏、不要求管理员权限、不读取或改写存档。任何修改游戏文件的工具仍有风险，请保留原版与存档备份。

```cmd
:: Python 运行版（解压目录内执行，负载默认位于 cosmobreeder_patch/payload）
python -m cosmobreeder_patch --verify-payload
python -m cosmobreeder_patch --game-dir "<游戏目录>" --check
python -m cosmobreeder_patch --game-dir "<游戏目录>" --install
python -m cosmobreeder_patch --game-dir "<游戏目录>" --uninstall
python -m cosmobreeder_patch --licenses
```

不带操作参数会打开 Tk 图形界面（选择目录 → 检测 / 安装 / 还原），并可查看第三方许可全文。独立 EXE 内嵌相同差分负载，支持相同参数。

---

## 🎮 安装与还原机制

1. **定位固定文件**：只处理 `cosmobreeder-multi.jar` 与 `patch.pak`，不递归发现游戏、不扫描注册表、不访问存档。
2. **档位检测**：存在 `patch.pak` 时视为官方可选补丁档，同时校验两文件 SHA-256；否则只处理 JAR 的原版档。任一不匹配即拒绝，**不提供强制覆盖**。
3. **先重建再动手**：全部目标文件先在系统临时目录重建并通过精确 SHA-256 校验，之后才触碰游戏目录。
4. **专属备份 + journal**：备份写入 `_cosmobreeder_alpha0.1_backup/` 与 `cosmobreeder-alpha0.1-state.json`，记录本次源/目标哈希；已有安装记录或备份存在时拒绝重复安装。
5. **原子替换与回滚**：同盘 `os.replace` 逐文件替换，替换前后 flush/fsync；异常（含中断）仅在当前文件仍为已知源/目标时回滚，未知修改保留备份供人工核对。
6. **还原可重试**：还原前逐项校验备份与当前文件哈希，全部还原成功后才清理备份与记录；备份目录含未知文件或链接时拒绝删除。

> 💡 兜底方案：Steam → 游戏属性 → 已安装文件 → 验证文件完整性；补丁的专属备份位于游戏根目录，可用于人工还原。

差分格式细节见 [差分与恢复边界](docs/DELTA_FORMAT.md)。

---

## 🧩 补丁内容

| 内容 | 说明 |
| --- | --- |
| 开场字幕 | 12px 原生字库，约 20 字 / 240px 换行，保留原打字机与分页 |
| 全宽剧情 | 同上；合并 956 组原续句，变体来源不匹配不强套 |
| 结束叙事报告 | 12px；保留原事件处理 |
| 无线电 | 10px / 约 15 字 |
| Continue 窄栏 | 10px / 约 8 字，修复分页完成漏末字 |
| 道具名称 / 说明 | classic8 字体 |
| 存档界面 | 保留原布局，不重排 |

---

## 📁 目录结构

| 目录 / 文件 | 内容 |
| --- | --- |
| [src/cosmobreeder_patch](src/cosmobreeder_patch/) | 自包含差分协议、安装 / 备份 / 还原、CLI 与 Tk GUI |
| [tools](tools/) | alpha 发行构建（差分、EXE、清单、SHA256SUMS）与去私有溯源字段的译文快照导出 |
| [tests/release](tests/release/) | 合成夹具单测及可选真实归档集成测试 |
| [data/translations](data/translations/) | 去除本机路径与原文上下文的译文贡献快照，不是历史全量构建 ledger |
| [localization/layout/src](localization/layout/src/) | 自有 Java 布局与字体适配器源码 |
| [localization/layout/tools](localization/layout/tools/) | 历史布局补丁 / 构建源码，需额外本地输入 |
| [localization/tools](localization/tools/) | 提取、来源身份、翻译与字体研究工具源码 |
| [docs](docs/) | 差分格式、源码构建边界、alpha 发行说明 |
| [licenses](licenses/) | 字体与安装器运行时完整许可文本 |

历史全量构建依赖本地 r21 中间归档、组合字体、提取语料与历史夹具；**公开源码目前不能从干净克隆一键重建完整 r27 目标**。alpha 差分封装可从维护者提供的本地原始归档与冻结目标重现；独立安装器消费已下载的差分负载，不需要研究缓存。不要把两条构建链混为一谈。

---

## 🛠️ 技术细节

### 差分为什么依赖原文件

`CBDELTA1-COPY-XOR` 的指令流只有两类：从原文件整块 COPY（整块 SHA 匹配时），以及 XOR + zlib 压缩的差值。r27 重打包后的两个文件都没有匹配整块 COPY，实际走 XOR，因此差分量接近原文件大小——这**不是**对完整目标的压缩替代，解码仍必须提供 SHA 锁定的原文件。XOR 不是加密或版权保护承诺。

### 校验层级

| 机制 | 作用 |
| --- | --- |
| `payload/manifest.json` | 锁定两文件完整源 / 目标 / 差分 SHA-256 与尺寸，超限即拒绝 |
| `--verify-payload` | 只读校验发布负载完整性，不接触游戏目录 |
| `--check` | 判定原版档 / 官方补丁档 / 已安装，并核对当前文件哈希 |
| 备份与 journal | 还原时校验"备份 = 原版、当前 = 本次目标"，其余一律拒绝覆盖 |
| `SHA256SUMS` | 发行资产与内部负载的外部校验清单，须从可信发布渠道核对 |

项目内置哈希是完整性检查，不是发布者数字签名，无法防止攻击者同时替换程序与全部元数据。

### 进程守卫

安装与还原前检测 `java.exe` / `javaw.exe` / `Cosmobreeder.exe`，命中即保守拒绝（可能同时阻止无关 Java 程序）。请先关闭游戏与其它 Java 程序。

### 中文如何显示

游戏把整个 libGDX 混淆进 `PRG/*`，位图字体走自研缓存绘制链与终端着色器（存在 8 像素周期采样）。补丁不替换原字体接口，而是提供独立的原生 12px 字库并按场景适配字号与换行；字格透明 RGB 必须与着色器红通道采样兼容，否则空白格会显示为实心黄色字块——这是 r27 修复的问题。

---

## 📘 排版与体例

| 场景 | 字体 / 宽度 | 说明 |
| --- | --- | --- |
| 开场 / 全宽剧情 / 结束报告 | 原生 12px，约 20 字 / 240px | 保留原分页与打字机 |
| 无线电 | 10px，约 15 字 | 窄栏独立宽度预算 |
| Continue | 10px，约 8 字 | 修复末字遗漏 |
| 道具名称 / 说明 | classic8 | 沿用原 8px 格 |
| 存档 | 原布局 | 不重排、不缩放 |

中文标点全角；译文以草稿为主，**草稿不等于审校批准**。

---

## ⚙️ 构建与发布（维护者）

差分封装构建需要本地持有：`backup/` 内的原版两文件、`localization/builds/r27-story12-shaderfix-test5/` 的冻结目标，以及仅在构建独立 EXE 时需要的 PyInstaller（本次 6.19.0）。输出目录必须尚不存在。

```sh
# 默认输出 dist/alpha0.1；输出目录已存在时会拒绝构建，重建前先移走旧目录
python tools/build_alpha_release.py          # 差分 + Python 运行版 zip
python tools/build_alpha_release.py --exe    # 同上并追加 Windows 独立 EXE

python -m unittest discover -s tests/release -v
CB_REAL_DELTA_TEST=1 python -m unittest discover -s tests/release -v
CB_REAL_DELTA_TEST=1 CB_EXE_DELTA_TEST=1 CB_GUI_DELTA_TEST=1 python -m unittest discover -s tests/release -v
```

构建器重新生成 `manifest.json`、`SHA256SUMS`，并把根 `LICENSE`、`NOTICE`、`THIRD_PARTY_NOTICES.md` 与完整 `licenses/` 文本目录复制进发行目录、嵌入 EXE 与运行 zip；许可文件缺失时拒绝构建。构建会短暂生成精确目标验证文件，校验后立即删除，不进入发布包。

发布采用**新增** Release 的方式，不覆盖历史版本。版本历史见 [Releases](../../releases)。

---

## ⚠️ 版权与许可

- **原作者**：游戏《Cosmobreeder Yiffai》及其原版代码、美术、音频、剧情、文本与原有位图字体，权利均归原权利人所有；本项目与原游戏作者、发行方无隶属或背书关系。
- **不含游戏本体**：仓库与发行物仅含自有补丁源码、差分负载、译文贡献快照与工具，**不含任何完整游戏归档、原游戏 JRE 或存档**；使用前请自行取得正版游戏。
- **非营利**：仅限非营利目的使用与分享，严禁用于商业用途；演绎作品须沿用同一许可。
- **翻译数据**：译文贡献与原游戏原文不是同一授权范围，项目许可不得解释为对原游戏内容的再许可。

**字体**：新增中文字体贡献来自 [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font) 2026.10.16 的 12px 版本，按 **SIL OFL 1.1** 分发，上游组件许可随包提供（见 [NOTICE](NOTICE) 与 [第三方声明](THIRD_PARTY_NOTICES.md)）。组合字体中仍含原游戏 ASCII 位图的部分不单独发布。

**许可证**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)（全文见 [LICENSE](LICENSE)）。

反馈问题时请附补丁版本、原版 / 官方补丁档位、截图与复现步骤；不要上传完整游戏、存档、个人路径、令牌或其他敏感信息。
