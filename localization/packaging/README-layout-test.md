# r22-test1 中文排版测试安装器

[测试EXE](<../builds/layout-r22-test-installer-final/CosmobreederYiffaiCN-Layout-r22-test1.exe>)约69MB，内嵌载荷，不要求用户安装Python。它不是稳定版，不会自动安装或启动游戏。

## 本次测试什么

- **默认启用存档单卡片**：只有测试载荷中的一个新helper改变默认开关；其20个非初始化方法与原候选的符号指令相同。
- 开场字幕、主道具详情仍仅诊断，不猜填尚未验证的容器参数。
- 其他classic/DS文本系统未扩展；真实clip、CRT、输入、全部数据域仍未通过G3。
- 原实验候选、正式安装器、正式载荷及译文不变。测试版不新增启动INI；显式JVM属性`-Dcosmo.layout.save.prototype=false`仍能关闭单卡片。

## 使用

1. 自行备份存档，退出游戏和其他补丁工具。运行游戏不是安全隔离，仅复制目录不足以证明不会写回。
2. 打开测试EXE，选择游戏根目录。支持SHA匹配的原版／已知r21，分别识别有无官方NSFW包；未知版本拒绝，不提供强制覆盖。
3. 阅读风险提示后点击“安装测试版”。安装器只写游戏归档和独立测试备份/状态，不读写存档，不启动游戏。
4. 测试后用同一个程序“卸载 / 还原”，还原到安装测试版前的精确来源，而非一律退回最早原版。旧汉化备份和状态保留。

测试备份目录为`_中文排版测试备份`，状态为`layout-test-install-state.json`。请不要手工改动、混用旧安装器还原或删除备份。安装后用户改过的文件会被保留并报告未完成；缺失或错误备份不会强行还原。

本EXE未签名；若系统安全策略拦截，请核对来源和[SHA校验文件](<../builds/layout-r22-test-installer-final/CosmobreederYiffaiCN-Layout-r22-test1.exe.sha256>)，不要为测试关闭安全防护。

## 已验证

- [22项后端测试](<../tests/test_layout_test_installer.py>)：版本/载荷拒绝、路径漂移、失败回滚、精确备份来源、用户改动保护、缺失备份、返回码及只读自检。
- [真实归档夹具日志](<../builds/layout-r22-test-installer-final/verification-logs/installer-roundtrip.log>)：原版／r21×本体／NSFW四组合安装→检查→卸载，JAR/PAK回到原SHA，人工存档/设置/旧状态哨兵不变。只在工作区执行，没有安装原游戏。
- [开关验证](<tests/TestInstallProfileProbe.java>)：测试Jar默认on、显式属性false及API启停通过；46类在原JRE加载校验，不调用游戏Main。
- [EXE内嵌自检](<../builds/layout-r22-test-installer-final/frozen-verification.json>)：实际运行EXE的只读分支，载荷SHA、版本/开关及Tcl8.6.15通过；没有打开安装界面或访问游戏目录。
- [构建身份](<../builds/layout-r22-test-installer-final/build-manifest.json>)绑定源、生成代码及载荷。PyInstaller6.19.0的onefile流程沿用现有spec；只读检查其CArchive，未将测试JRE、安装夹具或用户数据打入EXE。

安装器GUI的真实点击流程与游戏画面尚未验收，不将以上结果扩大为实机通过。

## 重建

[构建脚本](<build_layout_test_installer.py>)在全新工作目录复制现有GUI与安装引擎，仅为测试版添加警告、兼容“未变化PAK”的识别条件及[安全包装](<layout_test_backend.py>)。不覆写现有正式准备目录。

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python -B \
  localization/packaging/build_layout_test_installer.py \
  --output localization/builds/layout-r22-test-installer-new
```

输出必须是不存在的新目录。脚本编译单helper测试变体、验证所有其他Jar条目不变、运行后端与真实归档夹具、打包EXE、检查内嵌载荷，再运行只读自检，最后才发布。

外部契约：先查Context7，再对照[PyInstaller6.19.0官方spec文档](<https://pyinstaller.org/en/v6.19.0/spec-files.html>)；CArchive和缓存目录读取契约还核对了当前安装的6.19.0源码。未安装或更新任何打包依赖。
