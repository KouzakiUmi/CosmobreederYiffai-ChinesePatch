# r28 Fox / HardFox 缺字修复组件

## 已实现

[StoryFont12.java](../../../layout/src/PRG/StoryFont12.java#L83-L110) 保留真实 `jo` 的 `HardFox || (Fox && !readable)` 判断，只在 `pattern=true` 时调用新增的 [PatternSymbols.java](../../../layout/src/PRG/PatternSymbols.java)。没有修改剧情源文、源身份、`amn`、显露算法、字体图集或角色选择：

| 场景 | 输出 |
|---|---|
| HardFox，两种 readable 值 | 原 dingbats，中文等缺字单元编码成其现有符号 |
| Fox，不可读 | 同上 |
| Fox，可读 | 原中文 story12 / 纯英文 default |
| Normal | 原中文 story12 / 纯英文 default |

映射是有损的虚构文字表示，不是加密、密码或可逆翻译。原 `33..126`、`160..255` dingbats 字符保持原码位；新增支持的非空白 UTF-16 单元确定性映射到 `A..Z/a..z` 的 52 个原符号。每个原单元仍占一个原8px符号格，不扩张字符串、不插入标记分隔符；相同字符在不同位置和显露帧得到同一符号。空格、未来显露空白及原结构字符保持；其他 Unicode 空白归为原空格。补充平面字符沿用原引擎两 UTF-16 单元的步进，不声称引入 Unicode 字素排版。

**仅转换当前掩码，不转换完整页来绘制。** 未显露格不可能因完整页已含中文而提前出现符号。中文源串始终留在原状态中，解读后按原分支显示中文；HardFox 仍不会因 readable 为 true 而泄露明文。没有缓存、纹理创建、资源所有权或生命周期变更。

## 集成协议：默认基于冻结 r27 增量

机器清单、输入 pins 与测试 CLI 见 [component.json](component.json)。

1. 将两个 runtime 源以 `--release 8` 编译，classpath 为冻结 r27。
2. 替换三个原 StoryFont12 runtime class，增加一个 PatternSymbols class：

```text
PRG/StoryFont12.class
PRG/StoryFont12$Font.class
PRG/StoryFont12$Metrics.class
PRG/PatternSymbols.class
```

3. **r27 不运行 `StoryFont12Patch.apply`。** 它已安装 `jo/Na/Yg` hook，本组件无需新的 ASM pass。不要把 run 目录中测试器 class 打入成品。
4. 不修改任何资源。现有 dingbats、story12 FNT/PNG、字幕/剧情排版器保持原样。

若走原始 r21 / original class 的完整重建，才沿用原 [StoryFont12Patch.java](../../../layout/tools/java/StoryFont12Patch.java) 的原始 SHA gate 与一次 apply；其 helper inventory 已增加 PatternSymbols。原始 pins 没改，不能误认为这些 SHA 对应已补丁的 r27。旧 PNG 常量修正为 r27 实际、现有生产器均使用的 `486935a160007265569428c871ce3f949fd1b3a1d68f3690ea7f6572276540bd`；不是另建字体、再生成资源或放宽 pin。

## 独立验证

```text
C:/Windows/py.exe -3.12 -B localization/optimization/r28/pattern/run_tests.py
```

[测试驱动](run_tests.py) 仅创建本目录下新 run 目录，验证冻结 JAR/PAK SHA，并核实 106 个解密脚本夹具逐字节等于两归档实际条目；不会调用总构建器、安装器、游戏入口或存档 API。真实 parser 以 Unsafe 隔离其 IO 构造器；真实 FNT/arp 字形解析器只覆盖纹理上传入口，不构造 GPU 对象。

最新证据：[results.json](run-b754944448e54c01a4905b9f6f9e7bd4/results.json)、[pattern CPU 日志](run-b754944448e54c01a4905b9f6f9e7bd4/pattern-cpu.log)、[原 story12 CPU 日志](run-b754944448e54c01a4905b9f6f9e7bd4/story12-cpu.log)、[原始 ASM preflight 日志](run-b754944448e54c01a4905b9f6f9e7bd4/original-patcher-preflight.log)。

- [PatternSymbolsTest.java](../../../layout/tests/PatternSymbolsTest.java)：20,620,734 checks，真实 parser → anp → amn/amw → jo/Id/SN → arr/FNT；544 条 Fox/HardFox，268 条含汉字命令 / 4735 汉字；旧 230 条零可见字形降为 0。
- 原语料与 Normal/纯英文/独立中文标点/混排/前导空白/多页合成夹具：共 597 页，两种 readable × 每页全部 85 显露位置，101,490 帧，308,052 次真实 arr，2,313,034 个可见字形四边形。
- 每个已显露非空白字符必须有精确字体 glyph 与非零尺寸；检查实际 arr 字形几何处于 logical256，且每一前缀字形的坐标/尺寸与最终帧相同。逐格检查未来空格无 ink，原中文源和样式不变；原 amn 完成与跳过路径也检查。
- 穷举全部 65,536 个 UTF-16 单元映射；保留原纯英文字符串引用/内容。
- 对冻结图集实际 dingbats 区域检查全部 190 个原非空白 glyph 的红通道和 alpha 笔画均非空，包括完整52符号 palette。没有把非零 glyph 矩形误当作实际像素证据。
- 原 [StoryFont12Test.java](../../../layout/tests/StoryFont12Test.java)：CPU 2435 断言（真实 Yg/jo/Na、一次注册、借用纹理、失败前不变异等），原始 patch preflight132 断言；两者通过。该完整 run 时测试未修改，之后只增加下述 candidate 原生字形计数参数。
- 新 runtime class 均 Java8 major52；测试前后原归档及实现源 SHA 一致。

早期 run 的失败证据保留：一个合成夹具使用了不在冻结 r27 字集的“页”，导致严格 story12 gate 拒绝；后改用已存在的“段”。没有因此放宽缺字校验或增加字体。最终两次完整回归通过，以最新 sealed run 为交付证据。

## 主集成注意

旧 SubtitleLayoutTest 的 pattern 绘制文本断言假设 `draw.text == rawRow`，在新双表示语义下不再正确（普通显露与 skip 两处）；请该文件所有者将 **pattern 分支**期望改为 `PatternSymbols.encodeMask(rawRow)`。本组件没有修改它。其原测试对 pattern 跳过 ink 校验，不能替代这里的真实 dingbats 测试。

本独立驱动刻意冻结 r27 的语料数量和字体 SHA。若主集成新增 SFW 译文、扩字集或协同更新 story12 pin，应另生成对应最终归档的 fixture 和计数、再回归；本结果不冒充新增语料已经通过。

### 最终 candidate 独立入口

当前 [PatternSymbolsTest.java](../../../layout/tests/PatternSymbolsTest.java) 新增可选第五参数；父构建器不必重跑冻结驱动，可直接针对候选归档运行：

```text
java -Xverify:all -Dfile.encoding=UTF-8 -cp <testclasses>;<candidate-runtime-classes>;<candidate.jar> PatternSymbolsTest <new-vsn.tsv> <dingbats.fnt> <new-story12.fnt> <bbc2.fnt> <expected-census.properties>
```

第五参数为 UTF-8 Java properties。父集成从 candidate 的实际解密脚本独立统计以下三项，并核实 TSV 所列脚本逐字节相等；不得将旧268/4735直接套给新SFW：

```properties
commands=544
han_commands=填写候选实际含汉字命令总数
han=填写候选实际汉字单元总数
# 可选：before_blank=未编码时实际零ink的含汉字命令数
```

`commands` 也必须使用候选实际值，上例544不是默认值。传第五参数时三项均必填且严格相等；不传才沿用冻结 r27 census。仍强制 `after_blank=0`、所有实际字形/几何/完整显露步进和 readable 分支，不因候选模式跳过这些测试。新字库 pin 以父集成显式 staging 并编译的 `StoryFont12.FONT_SHA256` 为准，本测试会核实实际传入新 FNT，不接受伪造旧 pin。

该 CLI 增量未重复完整冻结回归；以 [聚焦契约测试驱动](check_candidate_cli.py) 验证实际单一 HardFox 脚本的独立计数通过、错误计数拒绝及缺项拒绝。此前 sealed run 保留当时完整测试源码 SHA，CLI 扩展不冒充已经验证父方尚未产出的最终 candidate。

[StoryFont12Test.java](../../../layout/tests/StoryFont12Test.java) 的生命周期测试也新增 `--cpu <runtime-font-dir> [expected-native-count]`；省略最后参数仍严格2312。候选扩字库必须独立统计其 `StoryFont12.uses12` 范围内的实际 glyph 数并显式传入，不关闭总数检查。此项之外原断言和生命周期均未改变；聚焦驱动同时验证显式2312通过、错误2313拒绝。

未验证：GPU / 着色器执行、父裁剪 / CRT、实机截图、全部场景可达性及解读能力解锁状态流。本组件只证明 CPU 路径和原图集可见笔画，不把它称为实机验收。
