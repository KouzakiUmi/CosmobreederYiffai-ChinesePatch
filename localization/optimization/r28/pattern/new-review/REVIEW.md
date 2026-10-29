# 字体追加／集成只读复核

## 结论

当前已检查的补字算法没有发现裁切、旧字形变动、透明白底或 append band 冲突。完整七组件当前已知的三个字体 SHA owner 均在编译集合，每个旧字面量恰好出现一次，可被 staging 完整替换。此次只做只读探针，未编译或运行新的最终 candidate。

主实现、字体、集成测试文件均未修改；仅本 new-review 目录有探针和报告产物。

## 已确认修复

此前 `story12/` 新 PNG 配旧 manifest/nested FNT 的漂移，主方已修。[build_candidate.py:122–131](../../integration/build_candidate.py#L122-L131) 现在完整保留旧诊断 bundle，单独增加 `r28-font/` 的三角色 FNT、两区域 PNG、manifest、OFL8、NOTICE。静态确认逻辑正确；未把尚未执行的新归档验证冒充完成。

## 剩余问题

### P2：partial 组件选择没有字体 owner／pattern 依赖闭包

[build_candidate.py:156](../../integration/build_candidate.py#L156) 只取已选组件 runtime；[178–186](../../integration/build_candidate.py#L178-L186) 仅对其中的源替换 SHA。但 [94](../../integration/build_candidate.py#L94) 和 [119–121](../../integration/build_candidate.py#L119-L121) 会追加并发布全部角色字体。

合法组合 `--components core,sfw` 不包含 StoryFont12 源。SFW 增字后 root story12 FNT 已变，冻结 r27 helper 仍持旧 SHA，首次 metrics/register 会拒绝。另 [77](../../integration/build_candidate.py#L77) 无条件启用中文 pattern 候选，而此组合未装 PatternSymbols 表示，会重现原缺字符号问题。

建议：FNT 变化必须有相应编译 owner；启用中文 SFW pattern 必须有 pattern 组件。自动补齐或提前拒绝均可。现 [VerifyLayout.java:10](../../../../layout/tools/java/VerifyLayout.java#L10) 不执行初始化，无法发现这些运行时字体 gate。

这不是对默认 full 七组件的失败指控：独立静态 [staging-probe-results.json](staging-probe-results.json) 确认 full 当前三 owner 均在编译集，三个旧 SHA 均恰好替换一次，替换后无旧 SHA 残留。partial 缺 owner 列表也记录在同报告。

### P3：字体生产器导入代码不在构建 source snapshot

[build_candidate.py:159](../../integration/build_candidate.py#L159) 纳入了 optimized_fonts、codec、projectlib，但 [optimized_fonts.py:19–21](../../../../tools/optimized_fonts.py#L19-L21) 实际执行的 layout_fonts、build_story_font12、build_item_font8 没有加入 snapshot。字体 manifest 记录 BDF/ZIP 输入 SHA 及输出 SHA，但不能补足此次执行的三个解析器版本与并发变动检测。

建议将三文件加入来源快照。这是可复现性／并发审计缺口，不是本次独立像素探针发现了错误输出。

## 独立实际字集探针

[probe_fonts.py](probe_fonts.py) 输入当前 SFW required_chars、VSN required_chars、两冻结归档 dictionary，形成2274码位 union；每个角色追加30字。详细 [font-probe-results.json](font-probe-results.json) 记录新增 IDs、各角色 SHA 和源像素证据。

验证结果：

- 原三角色全部 info/common/pages/kernings/metrics 保持；每个旧 glyph 的 RGBA 逐字节相等。
- append 以外整个区域的 RGBA 逐字节相等。新格覆盖的9240旧像素均为透明黑。
- 冻结 JAR 与 PAK 的 bbc2/classic 两区域完全相同，当前使用 JAR 生产再给两归档 overlay 的前提成立。
- 对每个新字独立从原 BDF BBX/位串重建：native12逐像素相等；default10确为其最近邻10px派生；native8逐像素相等。
- 30个新增 native8 的源 BBX 均为7×7、左0、顶1、advance8；在8×8格中预合成后不丢一笔、不多加一笔，说明当前 bbox 处理不是只对满8×8成立。
- 新格只含 RGBA(0,0,0,0) 与 RGBA(255,255,255,255)，红通道和 alpha 安全。
- 原新区域摆放为 default10 y1024、story12 y1280、classic8独立区域 y1024；生成器的旧声明矩形检查和新格交叉 mask 均未触发。

## 现有六测试的局限

[test_fonts.py:28–38](../../integration/test_fonts.py#L28-L38) 检查非空、R==A和尺寸，但不核对原 BDF 笔画、BBX top/left 及所有通道透明黑；[23–27](../../integration/test_fonts.py#L23-L27) 只比原 metrics，不独立比旧像素。因此它们单独不能排除“忘加native8顶偏移但仍有墨”或“RGB额外残留”等回归。此次独立探针已补足当前输出证据；建议日后把对应断言并入单测，不需要扩大生产生命周期。

未验证：最终候选归档、GPU/着色器执行、父裁剪/CRT、实机画面。完整构建仍需使用最终 candidate 的真实字库和脚本运行既定 CPU 集成测试。
