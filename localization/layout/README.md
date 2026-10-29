# 10px 中文布局补丁：实现与隔离候选

> **当前方向已调整：** 存档保留原界面，仅采用10px字体，不继续单卡片重排；优先修复实际剧情和无线电的换行、打字与分页消费链。下文单卡片及r22-test1属于历史试验，不再作为后续默认方案；旧EXE保留供已安装者还原，不能把其开场/道具诊断模式当作正文修复。

当前可测试的是[r27实心黄色字块修正EXE](<../builds/r27-story12-shaderfix-test5/CosmobreederYiffaiCN-r27-story12-shaderfix-test5.exe>)：r26字库空白为透明白，实际终端shader忽略alpha并按红通道涂色，导致整格实心；r27仅将新增字格透明空白改黑，并逐像素验证2312字形。全部Java/字体度量/着色器与r26逐字节一致，布局不改。按用户最新要求，开场/普通全宽剧情/结束叙事报告原生12px、约20汉字；无线电10px/15字、Continue10px/8字、道具classic8、956组合句及存档原布局保持。范围见[本轮实施说明](<README-full-text.md>)与[测试说明](<../builds/r27-story12-shaderfix-test5/测试说明.md>)；这不是已通过实机验收的稳定版。旧r23/r24/r25保留供已安装者还原。

## 下文为旧P0/P1试验记录（不是r25运行状态）

**当时是 P0/P1 实现与离线候选，不是已验收的可玩补丁。** 不覆盖原安装、存档或正式译文；三个运行时适配器默认不接管原画面。真实容器、父裁剪、CRT 可读性和完整输入回归未通过前，不刷新安装器或宣布全游戏排版完成。

设计依据：[中文排版完善方案 v2](<../../docs/中文排版完善方案-v2-10px与紧凑菜单.md>)。本轮修正真实入口，而不是照示例预算硬改布局。

## 1. 实现范围

| 部分 | 实现与边界 |
|---|---|
| 像素布局 | [纯 Java8 核心](<src/cosmoloc/layout/PixelLayout.java>)：按真实字形/kerning/效果边界预排全文，保留 UTF-16 源映射及固定显露位置；超宽/超高明确报告，不截断 |
| 字体桥 | [LayoutBridge](<src/PRG/LayoutBridge.java>)＋[窄访问桥](<tools/java/BridgePatch.java>)：取得原 SN 真正使用的字体，补偿首字 offset/padLeft；仅支持已证明的 1:1 整数网格，拒绝小数缩放及不等价的控制字符原串重绘 |
| 首条正文链 | [VSN 适配](<src/PRG/VsnLayout.java>)：锁定 r21 真实 ClassicPreTitle 八条中文、事件键、实际 parser/格式化结果及实例身份；不沿用早期验证译稿。精确识别的 SFW 英文仍走原链，不把同名资源误当中文目标 |
| 存档菜单 | [单卡片适配](<src/PRG/SaveMenuLayout.java>)：保留原槽位、动作与输入列表，单独绘制选中槽；保留完整姓名、性别、LVL、TRY、十六进制编码、地点/百分比及八个图标。原编码不是日期 |
| 主道具页 | [选中名称/说明适配](<src/PRG/ItemMenuLayout.java>)：保留 42 项图标网格、类别标签和原输入；在原说明格式化前取得全文，原型模式移除名称八码元截断并保留装备“+”。没有安全翻页证据的超高说明仍阻塞 |
| 字体候选 | [compact10 构建/验证](<../tools/layout_fonts.py>)：复用既有 10px 位图，保留 classic 原 193 西文字形，另加 2311 中文/标点；不缩放、不下载字体、不全局替换 classic，也未注册这个新角色 |
| 构建 | [统一构建器](<tools/build_layout.py>)、[ASM 驱动](<tools/java/LayoutPatcher.java>)及[打包消费门禁](<../tools/layout_bundle.py>)：原身份、完整目标/依赖、配对字体、实际图集及最终 JAR 加载检查；失败不发布最终目录 |

定向证据：[VSN](<research/vsn-evidence.md>)、[存档](<research/save-menu-evidence.md>)、[主道具页](<research/item-menu-evidence.md>)。`Kr` 是结局演出，`Eu/Ew` 是繁育支路，不在主道具页适配中；命名输入、左状态区及其他 classic 场景也未冒充已修复。

## 2. 固定输入与构建

[输入基线](<baseline.json>)绑定原包与 r21 归档、字体/许可身份以及全部目标 class。revision 2 增补原 `amn` 复制入口，用于保留同一事件的动画来源身份；任何目标或资源身份改变即停止，不能重新生成基线来掩盖不匹配。

项目内 JDK 来自官方微软 ZIP 并验证官方 SHA256，仅编译使用；不改 PATH。运行验证使用原游戏副本的 Temurin 17.0.6。JDK 下载记录位于项目工具链目录，不进入游戏归档。

在工作区根执行，输出必须是不存在的新目录：

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python -B \
  localization/layout/tools/build_layout.py \
  --output localization/builds/layout-r22-candidate-v2
```

构建器不会调用游戏主函数。流程为：冻结身份复核 → Java8 helper/测试及 Java17 构建工具编译 → 精确 ASM 改写/重建帧 → 原 JRE 测试 → helper/目标加载 → 字体门禁 → r21 增量归档 → 最终归档加载 → 日志封存 → 原子发布。

**Windows 不能把混淆后的原 class 整批展开后当 classpath。** 原包同时有大小写不同的 `PRG/Iu` 和 `PRG/iu`；中间验证也使用 JAR，避免文件系统大小写碰撞。构建期 ASM 不进入运行时。

[现有打包入口](<../tools/package.py>)另提供显式消费选项，默认打包行为不变：

```bash
python localization/tools/package.py --include-drafts \
  --layout-bundle localization/builds/layout-r22-candidate-v2/layout-bundle \
  --output localization/builds/layout-r22-package-check --write
```

这个入口重新走现有文本打包流程，**不等同于保留 r21 位图的增量候选构建器**。同一 class 的原 CP 索引编辑若与布局改写冲突，直接阻断，不能在 ASM 重排后套旧索引或覆盖另一项补丁。显式布局分支先写私有暂存，JAR/PAK 均通过后才发布；不会安装。

## 3. 原型如何启用

以下只是隔离测试接口，不是安装或发行建议。默认关闭时原画面不发生布局改善，不得把“能启动”描述成已修好。

### 存档

```text
-Dcosmo.layout.save.prototype=true
```

仅开启候选固定单卡片。背景内部覆盖、字段和光标都检查候选矩形，但该矩形不等于已测父 clip；长字段溢出明确报错。

### VSN 八条开场字幕

```text
-Dcosmo.layout.vsn.prototype=true
-Dcosmo.layout.vsn.x=<局部逻辑x>
-Dcosmo.layout.vsn.y=<局部向下逻辑y>
-Dcosmo.layout.vsn.width=<实际候选宽>
-Dcosmo.layout.vsn.height=<实际候选高>
-Dcosmo.layout.vsn.lineStep=<行步进>
-Dcosmo.layout.vsn.effectLeft=<效果边距>
-Dcosmo.layout.vsn.effectTop=<效果边距>
-Dcosmo.layout.vsn.effectRight=<效果边距>
-Dcosmo.layout.vsn.effectBottom=<效果边距>
```

所有数值必须显式提供，没有假定的“240px 安全宽”。原 SN 锚点和场景合成顺序保留；布局输出向下的 y 转为原 SN 的减量。字体、身份、显露掩码或容量不匹配时，启用的原型明确失败，不静默退回旧分块。

### 主道具页

```text
-Dcosmo.layout.item.prototype=true
-Dcosmo.layout.item.name.x=<局部x>
-Dcosmo.layout.item.name.y=<局部向下y>
-Dcosmo.layout.item.name.width=<候选宽>
-Dcosmo.layout.item.name.height=<候选高>
-Dcosmo.layout.item.name.step=<至少14的行步进>
-Dcosmo.layout.item.description.x=<局部x>
-Dcosmo.layout.item.description.y=<局部向下y>
-Dcosmo.layout.item.description.width=<候选宽>
-Dcosmo.layout.item.description.height=<候选高>
-Dcosmo.layout.item.description.step=<至少14的行步进>
```

不将背景整个右半区当说明矩形，那里已有图标网格。必须先确定局部矩形与图标/类别/页脚、实际 clip 的关系。超高时不截尾、不轮播、不借用装备/使用键翻页，也未新增未经验证的快捷键。

## 4. 已做与待做的验收

- 核心：37,928 项断言；实际字体字段/整数字形边界夹具；存档 28 项＋启动属性 2 项；主道具页 188 项；VSN 真正 r21 parser、八条×85 显露边界、事件/实例/角色与原尾部次序。最终数量以对应候选日志为准。
- Python：**64 项通过**（字体34＋bundle门禁28＋显式打包暂存/失败注入2）；后者实际让第二归档失败，确认最终输出目录不发布半成品。摘要及源身份见[离线验证记录](<verification-summary.json>)。
- 旧字体打包测试已修正误对照 12px 研究页的问题；在固定原包副本夹具下回归，不读写原安装。
- 原 Java8 helper/运行时代码不使用 Unsafe。VSN 无图形测试夹具用到它以跳过不相关上下文构造，编译警告保留在日志，不冒称零警告。
- **未完成 G3：** 真正窗口内的 contentRect/clip/CRT、八条时序、存档各模式全可达与确认/取消、道具图标导航/装备事件、自动播放/补全/返回/重入。未完成全 61 类扩展，也未调整 CRT 或重新准备安装器。

最早的 11 目标候选仅保留为中间证据；当前消费门禁要求 revision 2 完整目标集合，不允许把旧包当最终输入。原游戏安装、正式译文和存档保持原样；不要把实验候选交给安装器当正式载荷。

## 5. 当前集成快照

[revision 2 候选清单](<../builds/layout-r22-candidate-v2/package-manifest.json>)记录 **12 个原 class 改写＋34 个新增 helper**；[最终 JAR 加载日志](<../builds/layout-r22-candidate-v2/verification-logs/verify-final-archive.log>)在原 JRE 的 `-Xverify:all` 下解析46类且不初始化游戏。PAK 与 r21逐字节相同，字体/美术资源未变；三种适配的原型均默认关闭。

此快照不包含窗口内验收，不代表G3或全游戏通过。下一步应在安全测试环境中测真实矩形并完成输入/时序回归，再确定哪些profile可以从候选升级；仅复制目录不足以证明存档隔离。

## 6. 后续无启动绘制验证

[真实方法绘制探针](<validation/save-probe-notes.md>)在指定JRE下通过 **22 场景、1450 个SN调用、3172项断言**；实际执行候选的Mf/LX/LY/Iu入口及原格式化/CPU glyph-run构建器。它以人工数据和覆盖后的存档枚举方法避开存档服务，不调用游戏Main、GL或Steam。受限测试guard正向拒绝0，8项直接API负例均拒绝，不是OS沙箱。

[最终重放报告](<../work/layout-drawing-replays/run-v3/replay-report.json>)绑定候选、字体及冻结录制SHA。全部7个正常选中状态：原逐字路径动态文字alpha重叠15px，候选均0；4个成功的删除态候选帧也为0。九中文姓名仍是明确的预期拒绝，不作为“0重叠通过”。重放器另外通过9项测试。

[左右对照](<../work/layout-drawing-replays/run-v3/compare-normal-0-4x.png>)为**左原绘制、右候选，原始图集RGBA、无shader/CRT的CPU重放，不是实机截图**。碰撞统计只针对动态文字alpha，不涵盖图标/面板、真实父clip、输入与显示滤镜；合成地点仅覆盖原SORTIE回退，不能扩大为实际存档域验收。图中背景版本字样不能替代manifest身份。

[存储隔离预检](<validation/isolation-preflight.md>)发现旧验证线有写回原存档的事故记录；当前布局候选未修改存储链，完整游戏运行隔离仍未证明。因此未直接重启旧测试包，候选仍默认关闭、不可当正式安装载荷。[本轮核验摘要](<validation/verification-followup.json>)分列了执行、静态证据及未验收项。

## 7. 实验交付

本阶段交付[实验候选ZIP](<../builds/layout-r22-experimental-delivery.zip>)及[后续验收清单](<validation/acceptance-checklist.md>)。ZIP含候选归档、bundle、日志、有限验证摘要及CPU对照图；内附逐文件SHA清单和显著的非安装版警告。不含安装器、启动脚本或JRE，不自动启用原型，不作为正式载荷部署。

完整游戏安全隔离、真实clip/CRT/输入及其他文本入口留待下一阶段；本次实验交付不将这些未验项勾选为通过。

## 8. 独立测试安装器 r22-test1

后续另行构建了[测试EXE](<../builds/layout-r22-test-installer-final/CosmobreederYiffaiCN-Layout-r22-test1.exe>)，区别于上述默认关闭的实验ZIP：**测试载荷默认启用存档单卡片，开场/道具仍仅诊断**。仅一个helper的初始化默认值不同，其20个其他方法未变；原候选和正式安装器不被覆写。

[测试安装说明](<../packaging/README-layout-test.md>)列出支持源、独立备份/状态、精确来源还原、22项测试和四组合真实文件夹具结果。已核对EXE内嵌载荷及只读自检；没有在原游戏安装、启动游戏或做实机G3。请先备份存档再自行决定是否试用，不将测试版当作已验收稳定版。
