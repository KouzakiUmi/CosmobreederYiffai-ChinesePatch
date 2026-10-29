# r28 canonical PAK VSN 派生合句

本组件不修改 canonical catalog/译文、不改 DS joins、不改变 SFW、不改布局 Java 或总构建器。候选是审读入口，不是自动批准规则。

## 审校结论

- 421 条候选边组成 391 最大组；按 [双语完整演出段](<review-packet.txt>)逐组审读，全部原脚本上下文另封存在 [完整脚本上下文](<full-script-contexts.json>)。
- 接受 **300 合句组 / 324 边**：295 最大组全部接受，5 最大组仅合安全子组。
- **97 边明确保留**：全部 72 条 Fox/HardFox 语言角色边，加 25 条正文独立话语、改口、词中断、反应或递进停顿边。没有因为英文句尾缺标点就自动合句。
- 4 未译续行按 occurrence/unit/source SHA 记录在 [续行候选](<continuation-translations.json>)，通过 VG141、VG153、VG356 三个合句消费；canonical 原未译状态不改。
- [逐组审校台账](<review-ledger.jsonl>)保留每条输入的 occurrence、unit、原文/原 payload hash、冻结 r27 行 hash、完整演出段、明确接受/保留理由、边集分区；[执行台账](<operations.jsonl>)另外保存逐字符编辑映射及控制行证据。
- [原始显式决定](<review-decisions.tsv>)中的 `=` 表示经审读后原译文顺接已自然，`，`/`。` 表示所选边界标点，其余为逐组完整编辑；它们不是未审候选的批量接受标记。

## 纯 API

实现：[vsn_joins.py](<../../../tools/vsn_joins.py>)；固定资源身份和调用元数据：[component.json](<component.json>)。

```python
from vsn_joins import rewrite_vsn, apply_joins
new_bytes, report = rewrite_vsn(logical_path, r27_plaintext_bytes, archive='patch.pak')
# 可选：若调用方也持有 canonical 英文源，另加该源的强 hash 门禁。
new_bytes, report = apply_joins(logical_path, canonical_english_bytes, r27_plaintext_bytes)
```

1. 从冻结 r27 PAK 的 [组件资源映射](<component.json>)读取准确 archive entry 并解密。
2. **不要先重译或先改行**：输入必须逐字节等于该 logical path 冻结的 r27 明文。
3. 调用 `rewrite_vsn`；返回明文 bytes/report，由上层决定加密/归档。本 API 不写文件。
4. SFW 必须使用其自身 independently reviewed source/ledger；传入 `archive='cosmobreeder-multi.jar'` 总是拒绝，同名/同行号/同词句没有回退定位。
5. 源/路径/归档/任一记录身份不符会抛 `VsnJoinValidationError`。全部记录先预检，失败不返回部分 bytes/report。`records=[]` 是显式不操作，但仍检查冻结源身份。

只改精确允许的 `text: ` 行，后续输入行留成空物理行，不留下空 `text:` 命令。不改变任何非正文控制、sfxcue block、角色、auto、演出次序或 EOL。唯一无终止符的末行在被消费时保留一个 parser 忽略的空格，防止物理末行凭空消失；不添加末尾换行。

手动点按数减少是显式且有记录的预期变化（每个接受边少一个原 text 节点），不是伪称时序完全不变。合句全文由冻结 r27 `SubtitleLayout` 软换行，溢出页保留手动模式并排在原下一事件之前，原队列 sentinel 事件在全部后页结束后恰执行一次。所有八条 `auto(8.0)` 明文、解析时长、样式及总时长保持；不把单个 auto 拆成额外页。

## 复算与测试

```bash
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/prepare_review.py
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/build_ledger.py
/c/Windows/py.exe -3.12 -B -m unittest discover -s localization/tests -p test_vsn_joins.py -v
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/run_integration.py
```

前两步只复算本目录派生产物，不改变审校决定。Python 测试覆盖全部 67 档/300 组合句、全部 421 边分区、4 续行身份、改字编辑映射/标记守恒、控制/角色/auto 字节守恒、CR/LF/末行、SFW拒绝与后序错误的原子拒绝。

Java 集成编译组件自带的 [真实入口断言夹具](<VsnRuntimeAssertions.java>)与[整档 parser 测试](<VsnJoinIntegrationTest.java>)（不依赖并发改动中的布局测试源码），classpath 是**实际冻结 r27 JAR**，调用真实 `amS$a.E` parser、`anp`/`amH`、`amn`、`anh` 队列与 `jo` 记录式 SN，不启动游戏入口/GL。比较修改前后全部解析控制对象及次序、全部 auto 正文/时长/角色；重建全部中文文本并验证逐显露位置、skip/完成、三行宽度及末页后事件次数。输出只在本组件的 integration 子目录。

## 本次验证结果

- Python：**13 项通过**，包括全量合句、97 条显式保留、4 条续行、整档身份/SFW拒绝、EOF/EOL、文本编辑与全部新增用字的冻结 story12 字库覆盖。
- [实际 r27 JVM 日志](<integration/parser-layout.log>)：67 脚本；2388→2064 正文命令；**1986 个解析控制节点逐项且按序完全相同**；8 条 auto 全部不变；实际绘制 **2073 页**，其中 9 条手动正文产生后页、auto 溢出 0；**37,280,294 项断言通过**。
- [机读集成报告](<integration-report.json>)绑定实际 r27 JAR SHA、每档输入/输出 SHA、应用组与 occurrence 映射。
- [仅源句迁移建议](<source-join-suggestions.json>)可供 SFW 独立复核，不含 SFW 行号或批准结论。

离线测试不等于实机 clip/CRT、演出感受、输入或可玩性验收；合句改变手动原节点的点按边界，实际阅读体验仍应实测。
