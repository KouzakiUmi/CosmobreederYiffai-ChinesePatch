# 隔离运行预检：存储边界未闭合，不直接启动旧验证包

## 结论

**本轮没有启动游戏或读取用户存档。** 布局候选的G1/G2与受控绘制探针不等于完整游戏隔离。当前保留默认off；没有以“复制目录＋重定向两个字符串”作为安全运行证明。

静态核验产物：[存储字节码预检](<../../work/layout-storage-audit/run-v1/storage-preflight.json>)。它针对哈希匹配的原JAR，复读11个相关类、已有调用索引中的7个getter/setter/Steam直接调用记录，确认这些存储相关类在布局候选里原样保留。此报告只输出代码元数据，不读取存档内容，也不执行JVM。

## 1. 旧验证线存在真实事故记录

[旧应用脚本](<../../reports/planning/opening-verification-20261023-v1/tools/apply_opening_verification.py#L111-L118>)与[事故记录](<../../reports/planning/opening-verification-20261023-v1/checks/incident-save-write.json>)明确记载：一次退出/保存流程写回了原安装的存档并新增备份，因此不能直接沿用那条运行链。

但不能将事故根因草率定为“只改了options”：[旧构建器](<../../reports/planning/opening-verification-20261023-v1/tools/build_opening_patch.py#L77-L85>)及旧载荷中的替换方法均包含save/options两个setter。日志证明options写入已重定向，却没有记录当时getter值和`Hi`初始化时序。事故**事实明确、根因未定**；本次没有恢复、改写或删除任何历史存档。

## 2. 已证Java存储链

- `SO.a(String)V`／`b(String)V`只是写静态字符串。`Hi.<clinit>()V`经`SO.a()String → adu.c(String)adt → He(adt) → Tk(adt,azy)`创建并缓存文件句柄。之后再调用setter不会重绑已存在的句柄；这是代码可证明的机制，不等于已经证明历史事故恰由它引起。
- 保存、删除槽和玩家数据持久化经`He.a(HH/I/GL) → Tk.a(Object,avS)V`。`Tk`先由缓存文件的parent构造`save_backups`并写备份，再覆写目标；加载解码失败分支也可能写`.loadfail-`备份，不能认为“只读加载”必无写入。
- options经`iw → iP.a(String,iO) → SO.b()String → adu.c(String) → Yn/aqX → FileOutputStream`；其取路径时机不同于缓存的save链。
- 错误日志由`iG.uncaughtException`及`adh`持有的`Path`独立写入，不受SO getter覆盖。Local/External文件域还有`aqo`根缓存。
- save/options实际使用的Absolute文件分支不使用Local根。因此不能把`aqo`的CWD缓存直接认定为历史写原目录的根因。

上述调用可按[已有调用索引](<../../../docs/full-layout-study-20261023/inventory/all-invocations.jsonl#L96020-L96055>)和[本轮提取](<../../work/layout-storage-audit/run-v1/storage-preflight.json>)复算。静态直接调用索引不覆盖反射、原生库或进程外行为。

## 3. 可进一步验证的测试设计，不是已执行安全补丁

若后续要准备独立运行副本，可研究在**全新测试JVM首次加载前**，将测试专用JAR的`SO.a()/b()Ljava/lang/String;`两个getter固定为私有绝对路径，而不是只改setter。当前直接字段扫描没有发现SO之外绕过getter读取那两个String字段的已见指令；这个设计仍须人工数据的存储夹具验证备份、loadfail、options及初始化顺序。

Steam方面，`Yu.a()azK`先加载DLL再调用`SteamAPI.init()`，只让init失败并不能阻止DLL加载。原有合法失败返回是空对象`azI.MODULE$`；只有测试副本中整段方法直接返回此值，才切断目前已见的游戏侧Steam初始化路径。已见消费者按空Option跳过，不存在已见的无条件取值。然而这不约束已运行的Steam客户端、原生DLL或系统缓存，**本轮没有生成或运行这样的存储/Steam补丁**。

不以改ACL、修改原安装、关闭Steam或拿真实存档试错来弥补证据缺口；完整运行前必须单独验证其写入边界。

## 4. 当前安全推进方式

[绘制探针](<save-probe-notes.md>)仅执行指定原类的绘制/格式化方法：用合成数据、测试专用`Mf.s()`替代真正进入`Mg→Hi`的存档枚举，记录SN而不创建窗口或纹理。内置测试guard拒绝私有目录外写入、原安装访问、进程、网络和native加载；正向拒绝0，8项直接API负例均拒绝。

这是一份纯Java测试的防误触措施，不是OS沙箱、不是实际游戏native防护，也没有把构造器绕过/合成注册表等夹具限制藏起来。真实存档、地点翻译、父clip、CRT和实际输入/退出时序仍未验收。

因此本轮可以扩大离线执行与像素证据，不能升级为“安全启动完整游戏已证明”或“正式可玩版已通过”。
