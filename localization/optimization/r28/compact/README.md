# r28 姓名／存档／主道具紧凑字段组件

只从冻结 r27 增量，不部署、不启动游戏，不接触任何存档。运行类仅两个 helper；补丁目标和调用协议见 [component.json](<component.json>)。

## 布局不是只缩字号

- **姓名／存档**：保留原三槽、24px 槽间距、64px 八格姓名、x+64 性别与 x+80 邻列。原 LY 第一行仍由真实 formatter 产生，只在前八码元边界拆成姓名与原元信息。中文紧框用真实 classic8 画整行，实际 advance8；绝不把 default10 的 advance 报成8。原 Id/It、名字内容、配额、存储、Mf/Iu 与旧单卡片均不改。
- **命名光标**：Mb 仍8×8，中文名光标 x=字段原点+同一 classic8 实测 advance；英文保留原调用。Mn 普通与选中重画走同一8px字形和颜色，原8×8高亮不扩大。三槽选择光标仍由真实未修改 Iu 绘制。
- **道具名称／类别**：名称 x176／72px；类别保留真实硬编码 ARMS／HEAD／BODY／SPCL／USE、x136。实际 Le 名称 y174／150／126／102／62。中文名称必须 classic8：下方紧邻原16×16图标，10px墨迹会侵入图标行；ASCII 沿原角色。原装备 cut8／pad8／+、闪烁 gate 不改。
- **道具说明**：原122×26内框在逻辑屏幕 `[130,196,252,222)`，竖分割 x127/128、横分割 y193/194。原说明 x136/y22 局部改锚点 y27；优先 default10 两行（y27/15，step12），不足时 classic8 三行（y27/19/11）。112px 文宽留下右侧4px以上余量，字符／英文词边界与中文禁则基于实际度量。
- **真正超高**：只有 classic8 仍超过三行时，采用两行内容＋第三行明确页码，完整循环；每页至少8秒、最长20秒。注册的原 Lb.a(float) 更新时钟，原 Le.x().a() 的选中对象 identity 或完整源改变即复位，包括不同物品同说明。无新输入绑定，不抛超高异常，不静默截尾。正式短文优先静态完整显示；冻结双档164说明只有旧英文 SpecialGeiger 触发分页。

## 完整改动清单

运行源码：
- [CompactFields.java](<../../../layout/src/PRG/CompactFields.java>) → `PRG/CompactFields.class`
- [ItemFont8.java](<../../../layout/src/PRG/ItemFont8.java>) → `PRG/ItemFont8.class`

构建期：
- [CompactFieldsPatch.java](<../../../layout/tools/java/CompactFieldsPatch.java>) 的 `apply(Map)`：LY/Mb/Mn。
- [ItemFont8Patch.java](<../../../layout/tools/java/ItemFont8Patch.java>) 的 `applyR27(Map)`：原 Le 构造器注册 owner、Lb/Lg 原空更新方法。**旧 apply 是原版输入入口，不可用于 r27**。

总共6个目标 class／7个方法；其他方法逐方法序列字节守恒，重复补丁拒绝、晚期预检失败不部分修改。没有 nested helper、资产或新字体。原 Yg/LayoutBridge/font bridge 继续复用。

测试：
- [CompactFieldsTest.java](<../../../layout/tests/CompactFieldsTest.java>)：六 entry 指纹、七方法精确差异、原子预检、重复拒绝与隔离 overlay。
- [CompactFieldsCpuTest.java](<../../../layout/tests/CompactFieldsCpuTest.java>)：真实最终消费者／arr／arq、两档词典字段、42真实选择坐标、三槽、命名光标、高亮、超高时钟／复位／完整性、禁则与像素边界。
- [ItemFont8Test.java](<../../../layout/tests/ItemFont8Test.java>)：原版输入旧 apply 入口兼容回归，已更新说明两行10／三行8断言。
- 只复用不修改 [CpuEvidence.java](<../../../../docs/font-layout-audit-20261025/simulation/CpuEvidence.java>) 的真实 FNT/arr/arq 录制工具。

## 集成与测试协议

1. 对冻结 r27 **全部6个 entry** 先验 component 的 `target_pins`；共用 EXPAND_FRAMES map。
2. `CompactFieldsPatch.apply(map)`，然后 `ItemFont8Patch.applyR27(map)`。
3. 用 COMPUTE_FRAMES|COMPUTE_MAXS 输出；替换两个 helper。不要再套旧原版 ItemFont8Patch.apply，不启用 SaveMenuLayout／ItemMenuLayout。
4. 以候选 JAR 编译 CPU 测试，**候选 JAR 置 classpath 第一位**；第一个参数提供实际 font/atlas，第二个参数是 LY 的实际 CodeSource。联合候选可两个参数都传同一候选 JAR。命令见 component，不锁旧 FNT SHA，新字形追加可兼容。
5. `prepare_inputs.py --pak-json <解密后候选PAK词典.json> --jar-json <解密后候选JAR词典.json>` 生成 UTF-8 TSV；格式为变体、base key、name、desc四列，反斜杠与换行使用显式转义。默认输入是冻结审计双词典，不读存档。
6. CPU 后运行 `render_compact.py <同一候选JAR>`。它读取最终原图集及其 FNT/实际顶点，对真实 alpha 逐像素测量；不替换系统字体。

## 已实测与证据

- [patch-final.log](<patch-final.log>)：6 pins／7 changed methods／atomic／double-patch 全通过；overlay SHA256 `6bbaae8a5ce232382532ead64eedc38b900cf8837e2af3bfa156ccbe4c5cd120`。
- [最终CPU日志](<baseline-evidence/cpu-formal-names.log>)：1864场景、88276实际顶点、2112断言、禁止API尝试0。包含正式164名称×五真实行×原未装备／装备展示两态的1640场景，164说明与42真实选择坐标；实际物品动作未执行。
- [最终像素日志](<baseline-evidence/render-formal-names.log>)：1864场景7类指标全0：墨迹交叉、分割线交叉、完整16×16保守图标框交叉、后绘面板／光标遮挡、真实性别图标交叉、说明框逃逸、画布裁切。
- 字号实测分布：PAK81非空说明全部default10，另1空说明；JAR78说明default10、3说明classic8、另1空说明。仅英文SpecialGeiger为4行2页，其余静态完整。
- [item-legacy-patch.log](<item-legacy-patch.log>)／[item-legacy-cpu.log](<item-legacy-cpu.log>)：旧原版输入 patcher 与更新 helper 兼容回归。
- [冻结CPU总览](<baseline-evidence/compact-contact-sheet.png>)／[冻结逐项像素报告](<baseline-evidence/render-report.json>)／[冻结原始录制](<baseline-evidence/cpu-recording.json>)。根目录输出可供联合候选重跑覆盖，baseline-evidence保留本轮确切身份。图片均是 **真实class驱动／合成数据／CPU／无CRT／非实机截图**。

## 明确未覆盖

没有游戏或存档构造器／读写服务、真实玩家存档、IME与真实键鼠／手柄输入、装备动作、父 clip／完整父帧、GPU过滤／shader／CRT。保守16×16图标框零交叉强于当前空图标像素，但不等于装备动画或动作验收。原八码元输入／装备截补仍在；任意未知字形、超原配额名字不承诺可输入或正确存储。正式候选新翻译／新背景必须重跑同一组件测试，不把旧原图证据升级为联合发行验收。
