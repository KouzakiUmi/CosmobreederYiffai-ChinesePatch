# 最终 candidate2 字体／资源独立只读复核

**PASS：9009 项检查，0 个问题。**

完整证据：[final-candidate-review.json](final-candidate-review.json)。先对 candidate1 做1159项实际归档、class常量、FNT、BDF源笔画和整图集RGBA检查，再以全部class/font bundle字节与完整图集RGBA身份桥接到 candidate2；未重跑字体producer或父方JVM套件。

## 绑定的最终归档

| 最终文件 | 实际 SHA256 |
|---|---|
| [cosmobreeder-multi.jar](../../../../builds/r28-full-opt-candidate2/cosmobreeder-multi.jar) | `b8ad97ee9a5d96f38b8e3753bc3252d723c68c4686acef875e10ce69325c63c3` |
| [patch.pak](../../../../builds/r28-full-opt-candidate2/patch.pak) | `10db525de973dc20a4c5f20b30bd989a0dcb1b0b08d80344b122bddeaa0cf245` |

检查前后 candidate1、candidate2 均未变动。

## 字体、诊断 bundle 与许可

- 两归档各9个旧 `story12/` entry 与冻结r27逐字节相同；旧诊断inventory内部SHA仍自洽。
- 两归档各12个新 `r28-font/` entry齐全。三个root FNT与新nested FNT逐字节一致；两诊断PNG与实际解密图集区域逐像素一致；FNT/PNG container/RGBA manifest SHA全部相符。
- native8完整OFL、四组件许可（boutique-bitmap-7x7、galmuri、misaki、miseki-bitmap）均与源文件逐字节相等；来源、10px最近邻派生和原作权利NOTICE齐全。
- default10：2409旧glyph +31新glyph＝2440；classic8：2504+31＝2535；story12：2409+31＝2440。所有旧metadata、page、kerning、glyph metrics及glyph RGBA不变。
- 31个新字的实际字格分别直接核对原BDF位串：12px原生、8px原生，10px明确为12px最近邻派生。新格只含透明黑／不透明白，未裁切、未额外添笔画。
- 冻结PAK原本没有default/classic root FNT；这两角色的旧metrics比较基准明确使用冻结JAR，其旧PAK图集像素仍单独比较，不将原root缺项误报为候选问题。

## 实际编译 pin

直接解析最终class字段的 ConstantValue，不只检查源码字符串：

| 字体 owner | 实际 FONT_SHA256 |
|---|---|
| `PRG/DialogueWrap.class` | `a00549d74925fe647462f0f545417a725fe3673a90a20fe8d60eb2aed902cbfa` |
| `PRG/StoryFont12.class` | `977bb36a550eb84a991e6080ea285d1da119d1445be5bfff62f3a14857005153` |
| `PRG/EndingReportLayout.class` | `be7ab5c40a009cf8b72038fcb9da787b94bc271a5cfd7d8ac38f953157095f53` |

三者匹配实际root FNT，旧pin无残留；SubtitleLayout内联的default pin也正确。52个新增／修改runtime与target class均为Java8 major52。三个字体producer源码已进入构建snapshot。

## 整图集与覆盖

- JAR的41条、PAK的38条图片记录：最终真实路由、源／新RGBA hash、approved mask、完整alpha均通过。
- 整个4096×6144图集仅在font append和已批准图片mask内变化；两归档范围外变化均 **0像素**。font append与图片mask不相交。
- dingbats原FNT存在性／字节及实际区域RGBA均不变。
- 静态解析最终DS、VSN、dictionary：JAR6146记录／39脚本／2114个非空白码位；PAK7784记录／67脚本／2392码位。三个角色对该union均无缺glyph。此项不冒充真实JVM或场景可达性验证。

## candidate1 → candidate2 身份桥接

- JAR全部7779个class逐字节相同；root FNT、旧bundle、新bundle各对应entry相同（JAR25项、PAK24项）。
- 两完整图集RGBA逐字节相同；资源路由及atlas文本相同，字体与图片检查可按身份继承。
- 检查全部entry差异后，唯一明文变化为JAR dictionary的 `ui.end.cr6`：两侧padding各4空格改为各3空格，UTF-16长度34→32，非空白内容不变。PAK明文无变化；其余差异均为重加密nonce。
- 图集RGBA SHA：JAR `47e6e699b4f22738eb54087bd2d09cff0e53158b8fd289affce6ebf8fb4d2ea7`；PAK `7bf058c1b41cfd3f1c4bf344ead2cc6998b23c56bf24b592d46c33952e138417`。

## 边界

只写本报告和配套JSON；未修改候选、源码、字体或父方测试。未启动游戏、JVM套件、安装器，未操作存档、Git或委派。父方fresh实际候选JVM套件是独立证据；GPU／shader执行、父裁剪／CRT、实机截图、场景可达性与译文语义不在本次结论内。
