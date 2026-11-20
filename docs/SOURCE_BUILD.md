# 源码构建与本地输入

仓库包含安装器源码、布局与字库补丁、图集覆盖片、测试和[公开校对索引](../review/scene-context-changes.jsonl)。原版游戏、完整汉化归档、原版图集切片和解密模板在本地准备。只需安装补丁时，直接从 [GitHub Releases](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases) 下载安装器。

## 准备构建输入

| 输入 | 要求 |
| --- | --- |
| `originals/` | 自备 Windows `1.0.5_full` 的原版 JAR 和官方 PAK。版本及目标指纹见[根清单](../manifest.json)和发行包的差分清单。 |
| `payload/` | 首次导出译文时，准备与发行版一致的目标 JAR 和 PAK。可用差分包在自己的独立副本上还原；导出方法见[翻译工作流](workflows/translation.md)。 |
| `deps/r27-base/` | 准备冻结的 `r27-story12-shaderfix-test5` 底座。构建器校验两份归档的 SHA-256，原版归档不能代替该底座。 |
| `deps/jdk17/`、`deps/jre/` | 分别提供 Windows JDK 17 和可运行游戏类的本地 Java 运行时。 |
| `deps/fonts/` | 匹配字体生产器指纹的 Fusion Pixel 12px ZIP、8px BDF 和许可证；源文件名及指纹见[字体工具](../tools/lib/optimized_fonts.py)。 |
| Python | 使用 3.12；本版构建用 Pillow 11.3.0，Windows EXE 打包额外使用 PyInstaller 6.22.3。 |

还没有冻结底座时，可使用现成安装包和匹配原版导出译文，不能从空的本地目录运行全量归档构建。安装器单测不依赖冻结底座。

## 维护与打包

在仓库根目录执行：

```cmd
python tools\tl_tool.py export --target payload
python -m unittest discover -s tests/release -v
python tl_work\chain_build.py --apply
python tools\release_tool.py --source originals --target payload --output dist\alpha0.4-scene-audit-local --label alpha0.4-scene-audit --exe
```

第一条只在准备新的译文工作区时执行。完整构建与打包的输出和校验步骤见[构建发布工作流](workflows/build-release.md)，差分文件格式和安装器接口见[差分格式说明](DELTA_FORMAT.md)。

## 历史资料

alpha0.1 时期的布局研究、旧打包器与双语审校材料保留在[迁移前的提交](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/tree/647b908bb7a7f30ea14062d268bf251ca7c75442)。日常维护使用当前目录和工具，不需要把旧流水线复制回新目录。
