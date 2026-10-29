# r28 PAK DS 派生文案润色

本组件仅处理冻结 r27 **已经应用956组 canonical joins之后**的 PAK DS。全部文件独占本目录，不改 canonical [合句台账](<../../../../translations/dialogue-joins.jsonl>)、[原译文](<../../../../translations/zh-CN.jsonl>)、SFW 或布局代码，不重新合句。

## 逐条审校

[完整语境审校包](<review-packet.txt>)及[派生审校台账](<review-ledger.jsonl>)覆盖 **43 个审计条目**（含重叠）：

| 项目 | 审读 | 修订 | 明确保留 |
|---|---:|---:|---:|
| 中文词内短横风险 unit | 21 | 7 | 14 |
| 已合句 ASCII 短横组 | 17 | 11 | 6 |
| 漏记原因的未合边 | 5 | 0 | 5 |

去重后仅改 **16 个现有正文节点**：datadf 3 行、datadm 13 行，不新增/删除节点，不改变控制或点按次数。

- 确认污染：功-能、完-好、物-理（两变体）、补-给、发-生、监-测、六处目- 前、任何- 东西。
- 保留真实口吃/鼻音/自我改口：N-NO、H-HEY、M-MAYBE、W-WHAT、Y-YOU、W-WELL、H-HOW、D-DON'T、T-TASTY、S-SURE、T-THANKS、Mmmn-hmm，以及 HACK- I MEAN HUNTING 的改口笑话；不全局删除 `-`。
- 3P-X69 是型号，不改。FU-、YO-、THEY'LL-、KNOCK ME U- 等明确被打断的句末仍保留。
- 两条插入语将英文空格包围的 ` - ` 换成中文 `——`，内容与停顿保留。
- DJ1bedc5ba12ec06cfaf3c 去掉 ANY- THING 对应污染，并将生硬伤害比较收成完整中文句。

### 五条漏记 skip 的口径修正

[派生 skip 记录](<derived-skips.json>)不改原 coverage/hash：

1. datadf 634→635：完整感谢 + Whew 呼气之后另起铁砧感叹，**不是词中断**。
2. datadf 3873→3874：TO Y- 后识破坚果双关、自我改口，保留逐步揭示。
3. datadm 1382→1383：deep- 后 I mean 掩饰欲望，保留改口及口吃。
4. datadm 2730→2731：AGE- 后认出对方，保留先斥责再认人的节拍。
5. datadm 4234→4235：衣物辨认的悬念停顿和下一行猜测，**不是纯断词**。

## 短样本

| 原冻结 r27 文案 | 派生修订 |
|---|---|
| `[报告还说，那儿有一个功-能完好的休息区，是由之前的特工们建起来的。]` | `[报告还说，那儿有一个功能完好的休息区，是由之前的特工们建起来的。]` |
| `[其他特工已经绘制出你目- 前所处区域各个部分的地图，有时还带标注。]` | `[其他特工已经绘制出你目前所处区域各个部分的地图，有时还带标注。]` |
| `关键是务必避免撞上那只大壮兽。它伤人比那里其他任何- 东西都更狠` | `关键是务必避免撞上那只大壮兽。它造成的伤害比那里其他任何东西都大。` |

所有修订的精确旧/新文、occurrence/unit/source SHA、原 join ID、header/prefix、字符编辑映射均在[执行台账](<operations.jsonl>)。

## 纯 API 与主集成

[组件清单](<component_ds.json>)给出两个资源的归档 entry、冻结明文 SHA、API、派生数据 hash 和字形集合。[实现](<ds_polish.py>)独立可导入：

```python
# 将组件目录加入 sys.path 后：
from ds_polish import rewrite_ds_polish
new_bytes, report = rewrite_ds_polish(logical_path, r27_plain_bytes, archive='patch.pak')
```

调用顺序：冻结 r27 PAK 的 datadf/1 或 datadm/1 解密 → 本 API → 上层加密/归档。**不要再次应用 canonical joins，不要先重译或先套其他 DS 文案操作。** VSN 是其他资源，不受此先后约束。

API 对 whole-resource SHA + full header（含原空白）+ exact prefix + exact old line + occurrence/source evidence 全部预检后才构造结果。任何漂移抛 `DsPolishValidationError`，无部分返回；归档非 PAK、两个变体互套、重复套用或未知路径均拒绝。EOL、前后空白、所有其他行（包括合句留下的空行、动态占位符与脚本事件）逐字节守恒。

[required_chars.txt](<required_chars.txt>)已经验证全部用字在冻结 r27 的10px与12px字库中，不需要扩字。[源句润色建议](<source-polish-suggestions.json>)仅供 SFW 独立来源与上下文复核，不是可直接套用的 SFW 允许表。

## 验证

```bash
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/ds-polish/prepare_review.py
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/ds-polish/build_ledger.py
/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/ds-polish/verify.py
```

**11 项隔离测试通过**：16 修订/全部43审计条目、真实口吃和5 skip保留、双资源互套与SFW拒绝、后序记录错误的原子失败、header/prefix/文本标记/控制/EOL/占位符/原956合句台账hash守恒，以及冻结字库覆盖。[测试日志](<tests.log>)和[机读验证报告](<verification-report.json>)记录实际结果。

本组件是纯文案及字节结构验证，不冒称新增 DS 运行时绘制、游戏 clip/CRT 或可玩性验收。组合构建仍由主集成验证。
