# r28 局部场景文本与资料完整性

**已交付六个精确目标类的增量 patch、三个 helper class 的完整集合和 CPU 回归。未启动游戏、GL、Steam、安装器或存档服务；未安装、部署或执行 Git 写。**

集成入口：[component.json](<component.json>)。逐个原消费者的已修／保留理由／未知：[consumer-status.json](<consumer-status.json>)。不能把目标 class 数或调用点数换算为运行覆盖率。

## 实际改动

- [SceneText.java](<../../../../localization/layout/src/PRG/SceneText.java>)：场景局部适配，使用公开 PixelLayout 断行接口；不改核心类、全局 It 或全局 Yg。
- [SceneTextPatch.java](<../../../../localization/layout/tools/java/SceneTextPatch.java>)：以冻结 r27 为原字节，六个 raw SHA、整个 canonical ASM17 class 树 SHA、精确方法 descriptor 和调用点 ordinal 数全部预检；再一次性修改。主驱动必须在解析前校验 raw SHA，并使用 `ClassReader.EXPAND_FRAMES`。
- [EndingReportLayout.java](<../../../../localization/layout/src/PRG/EndingReportLayout.java>)：保留结算整行角色与颜色；保留的 legacy formatter 接口也不再把 ASCII 转交旧丢尾格式器。**真正 Kc 修复是 source→tail 局部接管，不是只重编此 helper。**
- [EndingReportLayoutTest.java](<../../../../localization/layout/tests/EndingReportLayoutTest.java>)／[SceneTextTest.java](<../../../../localization/layout/tests/SceneTextTest.java>)：两档实际字典、原 Ks/Kr/Kc、实际 Ew/Jm 行消费者、真实 kn 成就标题以及原 arr/arq CPU 顶点。

完整新增／重编 helper 集合：`PRG/SceneText.class`、`PRG/SceneText$1.class`、`PRG/EndingReportLayout.class`。目标：`PRG/Ew.class`、`PRG/Jm.class`、`PRG/kn.class`、`PRG/Lx.class`、`PRG/Po.class`、`PRG/Kc.class`。完整 raw pin 在[清单](<component.json#L20-L27>)；canonical pin 在[patcher](<../../../../localization/layout/tools/java/SceneTextPatch.java#L14-L26>)。

不要对 r27 重新运行旧 EndingReportPatch：其 Kc 输入 pin 是原版，不是 r27。新 SceneTextPatch 的 Kc pin 是 `2f407f1f6c3e4e7dda3f3f47a8a3445f3047b5be87f35d1b775aa559c76a0eb2`。

## 矩形与角色依据

以下是原调用参数给出的保守内容预算，不冒充完整父 clip 或背景像素验收。

| 消费路径 | 原始依据／安全预算 | 本次行为 |
|---|---|---|
| Ew affinity | 原 x=It.a(2)=16；y=It.b(13-row)=110/102/94；28列；NW=3；原迭代实际上能画三行 | 在旧 format 前拿全文；整块选择角色，ASCII三行仍默认字库／8px步距；可容两行的中文用default10／12px。原文本明确用两个 `\|` 分成三行时，使用已有classic8／8px步距，而不是删断行、裁尾或缩放字体。 |
| Ew needs | 原只取块0、1，x16；原 y78/70；28列 | 全文预先排版；中文两行 y78/66、默认10px；ASCII两行保持原8px步距。只有完整计划全部通过才绘制；旧消费者只收到空白占位，因此不会再二次 clip。 |
| Jm 卡牌右栏 | x=It.a(15)=120；NV=16→128px；前／背NU=11、NT=15行；原相邻基线8px；右界248 | 按16×11/15的完整容量规划；与8px实际行距配套使用已有classic8，标题／统计行同矩形。调用原 `amw.a(text)`＋`ams.a` 保留确切normalize语义，只替换有损格式化阶段。奖励／数字／翻卡／选择均未改变。 |
| kn 弹窗 | Oi=30，Oa=2；原y214/206；classic8 | 统一禁则、完整两行；保留SA语言变换链、原动画与时长；最终文本用实际arr字形布局居中，不替换全局String.length。 |
| Lx 底栏 | 唯一 `SN.a(text,256,role)` 居中调用；实际绘字role为SN.b | 在此处改用同一字体原arr测量，含glyph offset／padding／kerning。其他Yg调用者不受影响；地图左右竖排／图例不宣称已修。 |
| Po 传送目标 | 唯一目标地名draw；全宽256；y206 | 仅重新计算该标签原生SN原点，使用真实arr宽；固定标题、MISSION／PAWSED和输入不变。 |
| Kc 三行资料说明 | x16；通常y30/22/14；B=true时38/30/22；原offset逐行相加；28可绘列→224px | 保留原选择对象及全文提取至local9，只替换后续format/zip尾；`$`样式位不占第28可绘列。复现原双pass、颜色float和偏移，中文classic8。 |
| Kr 结算／credits | 既有r27经典32列／8格 | 不改变字段文案、动态值或颜色／闪烁；完整字段测试重新执行。 |

原证据：[Ew snapshot](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Ew__4034ebb93463.txt#L731-L910>)、[Ew行调用](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Ew__4034ebb93463.txt#L1829-L1857>)、[Jm](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Jm__e6ae7a07e1e9.txt#L1303-L1371>)、[kn](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_kn__06ecd40ba832.txt#L541-L587>)、[Lx](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Lx__3affe2e2e0fb.txt#L907-L924>)、[Po](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Po__9120a3493600.txt#L1206-L1243>)、[Kc](<../../../../docs/full-layout-study-20261023/inventory/snapshots/PRG_Kc__091ac03da527.txt#L704-L784>)。NW/NU/NT/Oa/Oi/NV常量还用原class的javap实际核对。

## Kc 丢括号根因与修复

两个 SFW 原样式行的 payload 本身有28字符，旧格式器把开头 `$` 也放入28字符块，实际只剩27个可绘字位。单纯换禁则或新字体无法找回最后的 `]`。新 source-tail 绘制把 style 放在布局外，因此完整保留 `[STAR BETWEEN CROSS &SQUARE]` 及另一条实际原文的闭括号；不修改谜题内容／语言含义。

新测试还包含28汉字样式行、混合普通／样式行和中文禁则，防止只修两个字符串而不修消费者。

## 本轮真实 CPU 结果

最终冻结 r27 增量回归：[run010/results.json](<run010/results.json>)。

- [SFW 结算与资料](<run010/ending-sfw.log>)：6386断言，60结算字段、33实际资料说明，全文守恒通过。
- [NSFW 结算与资料](<run010/ending-nsfw.log>)：4496断言，60结算字段、59实际资料说明，全文守恒通过。
- [场景测试](<run010/scenes.log>)：8132断言，29068个真实CPU顶点、337个两档语料字段；实际Ew／Jm行方法、kn成就标题和arr/arq执行；晚到的Kc pin故障证明前面Ew未部分修改。测试期禁止native／network／exec及未许可文件读写，禁止访问尝试为0。SecurityManager弃用警告是JRE17的测试guard告警，不是运行helper依赖。
- [144个繁育逐字段绘制记录](<run010/breeding-corpus.json>)：SFW36 affinity三行default ASCII＋36 needs两行default；NSFW36 affinity显式三行classic8＋36 needs两行default10。此固定语料没有剩余超限条目。所有字段均比对完整source与实际draw，不以顶点数代替全文检查。

以前失败运行保留在本目录的 run001–run009 及较早日志中：编译夹具访问级别、SFW专属条目断言、It.b基线推导及缺少XK空目录夹具等均经读日志后修正。不能把旧失败日志当最终候选结果。

### 重跑

```bash
/c/Windows/py.exe -3.12 -B localization/optimization/r28/scenes/run_tests.py NEW-UNUSED-NAME
```

该[脚本](<run_tests.py>)只编译／生成本目录中的新隔离覆盖层并执行CPU测试，拒绝复用输出目录；不会调用总构建、安装、游戏入口或部署。生成[组件清单与账本的脚本](<make_component.py>)是独立操作，不属于游戏构建。

集成最终候选后必须再次按[component的candidate CLI](<component.json#L45-L93>)运行，传入候选的新字库及其分别解码的SFW／NSFW字典。现有run010只证明冻结r27语料，不冒充尚未生成候选的结果。

## 超高与未验边界

**没有新增安全input／滚动策略，不会冒称支持任意超高全文。** 最小可用方案已经实现：针对原本可达的固定场景，源头拿全文、整体选角色／行距、按完整可见容量预检并让所有已登记字段实际走到draw；新候选新增文案必须经过同一CLI。超容量会在候选构建测试中拒绝，运行时也明确拒绝，不 clip、截尾或让内容不可达。若将来要允许任意动态超高，必须另行联动滚动／查看input、焦点和命中几何，不可只增加一个“下一页”假按钮。

未验：完整父场景／FBO／clip、实际键鼠／手柄输入、背景线条和CRT／shader／GPU、Jm全部前后面／翻卡动画、kn的Reverse／AlBhed变换、任意玩家文本／扩展区汉字／未知glyph。SceneText不修改紧凑姓名／存档、ItemFont8、StoryFont12、字幕或核心排版；这些也不因本轮测试自动变为通过。
