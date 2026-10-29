# 剧情与无线电：10px自然换行及同句合并

本分支按当前要求**保留原存档结构与10px字体，不再带单卡片**。优先修复真实剧情、无线电正文，不以开场字幕原型代替正文修复。

## 已实现的范围

- 全宽剧情是MN→Nb→Na：按20个汉字的等效200px预算测试。
- 无线电是JM→JR→JQ：按15个汉字的等效150px预算测试。Jt是作弊菜单，不是无线电。
- 字形和kerning来自SHA封存的原r21 10px字体；英文、数字和标点按实宽排，不虚增为24/18汉字。
- 中文正文先取得实际最终译文；无线电的五个动态变量先在完整句上展开，再大写化、测量、分行。已扩长的英文动态报告也测量分页，避免替换后再次越框。
- 新行仍序列化到原20／28码元网格，每页三行，复用原动画、掩码、翻页和事件列表。不会插入英文长词连字符，不改变菜单布局、存档键或图标。
- 其他profile（包括q12窄支路）、不含中文和已知变量的原英文保留旧行为；这不是所有文本入口的全局改写。

## 译文合并是真实内容变更

[合句台账](<../translations/dialogue-joins.jsonl>)当前含199组，依据原始DS的具体occurrence及逐组中文审校，减少205个被原行割裂的正文节点。内容修正包括重复词、未完短语和局部语序；保留完整含义、数值、键名及变量。

不是把共享unit全文写到第一条再清空后面的译文。原canonical源和unit保持，台账记录完整合句；本地化输出只在已核实的同一说话人/表情、同分支、无事件插入的指定位置形成完整话语，其余物理行仅留原换行，不生成空对白。原事件/命令/条件/header及EOL逐字节保持。明确的外层方括号收拢有组级delta，不放宽全局QA。

整库窄规则筛得203组，三片分别审校：198接纳、5保留原样；与首批11组去重10组后为199。候选不等于自动批准，其余宽口径候选仍未自动合并，不宣称全库语言审校完成。

## 本体与NSFW资源分开核对

PAK用有效源SHA与原occurrence位置。JAR本体源确有行偏移及措辞差异，不能套PAK行号；[SFW适配](<../tools/dialogue_sfw.py>)按真实原JAR的完整root、前缀、源句顺序定位后使用经验证的同句台账，并校验字形/控制符。比如SFW的“OUR SATELLITE”与NSFW的“SATELLITE R18”不同，不强行套同一个合句，跳过项明确记录。

## 实现及验证入口

- [网格兼容核心](<src/cosmoloc/layout/DialogueGrid.java>)和[纯CPU回归](<tests/DialogueGridTest.java>)。
- [正文适配](<src/PRG/DialogueWrap.java>)和[双目标ASM补丁](<tools/java/DialoguePatch.java>)，仅改JR、Nb两个原class。
- [真实JR/Nb入口及动画回归](<tests/DialogueWrapTest.java>)：实际调用两个改写主方法，延迟事件、visited、MG、剩余页及terminal保持；不是仅对模拟字符串测试。
- [合句回归](<../tests/test_dialogue_joins.py>)保留首批11组黄金样本，另对199组全量台账验收。
- [SFW回归](<../tests/test_dialogue_sfw.py>)验证真实源偏移、不同措辞不串文、歧义拒绝和保护符门禁。
- [独立构建器](<tools/build_dialogue.py>)从r21创建新目录，冻结输入/代码/译文，先跑回归，再打包和校验内嵌载荷。不会安装或启动游戏。

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python -B \
  localization/layout/tools/build_dialogue.py \
  --output localization/builds/r23-textflow-test1
```

输出必须是不存在的新目录。构建期ASM只在JDK17工具内；运行时helper为Java8，不将测试类或工具带入游戏。Windows不展开混淆游戏class作classpath，避免大小写碰撞。

尚未做真实窗口的clip、CRT、全部输入和全部动态数据域验收；不能把CPU／无图形回归当成游戏实机通过。测试安装器不读写用户存档，但运行游戏不是安全沙箱。若装过之前单卡片测试版，先用对应旧EXE还原，不能直接强制覆盖。
