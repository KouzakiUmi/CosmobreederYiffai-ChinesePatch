# Cosmobreeder Yiffai 简体中文补丁

**alpha0.1 · 非官方预发行版 · 需要自行取得原游戏**

面向 Cosmobreeder Yiffai 的简体中文翻译与分场景排版补丁。当前发行基线为 `r27-story12-shaderfix-test5`。本仓库与发行物**不包含完整游戏JAR/PAK、游戏图片/音频、原游戏JRE或存档**，不能脱离匹配的原游戏独立运行。

## 下载与安装

从[alpha0.1预发行页](<https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases/tag/alpha0.1>)下载Windows独立安装器，或下载Python运行版ZIP。

1. 完全退出游戏，自行备份存档。
2. 如果装过r23–r27等旧测试版，先使用对应旧安装器“卸载/还原”。不要强制覆盖未知文件。
3. 将安装器放在方便访问的位置，选择包含游戏JAR的目录，先检查兼容性，再安装。
4. 安装器只接受发布清单中SHA-256匹配的原版文件；自动区分原版和官方可选补丁档位。未知版本会拒绝修改。
5. 首次进入游戏，复测开场、剧情、无线电、Continue、道具和结局报告。需要还原时使用本版安装器，勿手工删除备份。

安装器不自动启动游戏、不要求管理员权限，不主动读取或改写存档。任何修改游戏文件的工具仍有风险，请保留原版及存档备份。详细命令见[构建与运行说明](<docs/SOURCE_BUILD.md>)；差分与恢复边界见[格式说明](<docs/DELTA_FORMAT.md>)。

## 当前内容

- 中文开场、普通全宽剧情及结束叙事报告：独立原生12px字体，约20汉字/240px换行。
- 无线电：10px/约15字；Continue窄栏：10px/约8字；道具中文名称/说明：classic8；存档保留原布局。
- 保留原打字机、分页和事件处理；合并956组原始续句，来源不匹配的变体不强套。
- 修复12px新增字格的透明RGB与原终端着色器不兼容问题：透明空白不会再被当成整格黄色笔画。
- 发行物使用依赖原文件的二进制差分，不再携带完整替换JAR/PAK；安装时校验源、负载与重建目标的完整哈希。

## alpha限制

这是测试性发布，不是稳定版，也不是完整人工精校版。公开译文快照包含8,973条记录，其中8,146条有草稿、827条尚未翻译；草稿与合句不等于正式审校批准。原版与官方可选补丁文本存在差异，部分内容会保留英文。

已完成的离线/隔离验证与完整游戏实机验收是不同层级；当前仍需玩家验证图形裁剪、CRT效果、各场景可读性和完整流程。Windows EXE未进行代码签名，系统可能提示未知发布者。**不要因为安装测试通过而忽略备份。**

## 源码结构

| 目录 | 内容 |
|---|---|
| [src/cosmobreeder_patch](<src/cosmobreeder_patch/>) | 自包含差分协议、安装/备份/还原、CLI与GUI |
| [tools](<tools/>) | alpha发行构建与去私有溯源字段的翻译快照导出 |
| [tests/release](<tests/release/>) | 合成夹具单测及可选真实归档集成测试 |
| [data/translations](<data/translations/>) | 去除本机路径与原文上下文的译文贡献快照，不是历史全量构建ledger |
| [localization/layout/src](<localization/layout/src/>) | 自有Java布局与字体适配器 |
| [localization/layout/tools](<localization/layout/tools/>) | 历史布局补丁/构建源码，需额外本地输入 |
| [localization/tools](<localization/tools/>) | 提取、来源身份、翻译与字体研究工具源码 |
| [licenses](<licenses/>) | 字体与安装器运行时完整许可文本 |

历史全量构建依赖本地r21中间归档、组合字体、提取语料和历史夹具；**公开源码目前不能从干净克隆一键重建完整r27目标**。alpha差分封装可从维护者提供的本地原始归档与冻结目标重现；独立安装器使用已下载的差分负载，不需要研究缓存。不要把两条构建链混为一谈。

## 开发与测试

应用源码运行只需要Python3.12及其标准库；GUI另需可用的Tk。Windows独立EXE构建使用PyInstaller。运行发布测试：

```bash
PYTHONPATH=src python -m unittest discover -s tests/release -v
```

真实游戏集成测试需要用户自行准备的匹配归档；缺少它们不代表已通过该层测试。旧布局测试的额外输入见[源码构建边界](<docs/SOURCE_BUILD.md>)。

## 许可与归属

原创代码及项目文档：[MIT](<LICENSE>)。原游戏及其内容权利保留给原权利人；该许可不对原游戏或翻译的原作内容作再许可。原生中文字体贡献适用上游OFL及组件许可，见[NOTICE](<NOTICE>)与[第三方声明](<THIRD_PARTY_NOTICES.md>)。本项目不代表原作者，也不提供游戏本体的下载。

反馈问题时请附补丁版本、原版/官方补丁档位、截图和复现步骤；不要上传完整游戏、存档、个人路径、令牌或其他敏感信息。
