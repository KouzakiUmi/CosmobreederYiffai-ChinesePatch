# R5：5 条创译硬骨头

**处置 [R4](../r4-pending/reports/pending-01/decisions.tsv) 判为 `creative_pending` 的 5 条**，共 16 个来源锁定行操作。已并入 candidate10 并通过 17 步 CPU 回归。

这 5 条不是证据问题：容器、上下文、源文都已核清，缺的是中文方案本身。本轮给的是**可运行的整组改写**，并把每组双关的得失写清楚，不拿译者长注冒充台词。

## 五组处置

| finding | 场景 | 双关处置 | 操作 |
| --- | --- | --- | --- |
| P08-013 | BossuDex 矿／地雷冷笑话 + 同一笑点提示段 | 部分放弃：mine 四重同形无法单字复现，保留结构改走“认主／炸毛” | 8 |
| P05-020 | `COME IN. BOSSU?` / `I HOPE NOT` | **保留**：中文“进来”同时承担无线电应答与身体动作 | 2 |
| P02-009 | `nano-mechanical` → 听错成 `anal` | 重建：改在“机”上做同音梗（机／鸡） | 2 |
| P07-025 | `beat off` | 放弃：“撸退”是生造词，按自然叙事译“打退” | 1 |
| P10-011 | `take it` / `Just like he did` | 重建：“拿去用”＋“当初那样‘用’”保住物品义与暗示 | 3 |

逐条说明见 [decisions.tsv](reports/creative-01/decisions.tsv)。

## 关键取舍

- **P08-013** 原译把“布上了雷”直接说破，Yiffai 接着问“跟爆炸有什么关系”在中文里不成立——读者会觉得雷当然会炸。改写后 Bossu 先说矿“认了主”，再说“认了主的东西，会自己炸毛”，把误听链重新接起来，最后 Mauser 落实“这矿是我家的”。同时删掉提示段台词里三处 `(mine)` 英文注释（那是把注释写进了对白）。代价：`mine` 单词层的三重义不可复制。
- **P05-020** 是全轮唯一双关完整保留的一组：Yiffai“我进来了”既像应答也像动作，Bossu“希望你别进来”接住荤梗再用“没什么”掩过去。
- **P02-009** 中文“纳米机械”里切不出荤音节，改在“机械”的“机”上落同音（机／鸡），仍是“听长词只抓住一个荤音”的结构，Bossu 继续若无其事讲解。
- **P07-025** 明确放弃双关：`beat off` 的中文对译无对应双关，“撸退”读感不成立；按自然叙事译“打退”，荤味由同段“手脚很不老实”“使尽浑身解数”承接，不加原文没有的自我改口。
- **P10-011** 用“拿去用”保物品义、“用”在指人时带暗示，结尾回指 `Just like he did` 并保留 `;3` 语气，不发明具体行为。

## 边界

5 条都是试读稿，取舍已按项目规则写明损失；不宣称等价复现原文双关。未安装、未启动游戏、未访问存档。

## 文件

- [逐条处置与理由](reports/creative-01/decisions.tsv) · [构建与回归](reports/creative-01/BUILD.md) · [候选复核](review/candidate10-review.json)
- 台账：[editorial-r5-creative-repairs.jsonl](../../translations/editorial-r5-creative-repairs.jsonl)
- 工具：[build_creative.py](tools/build_creative.py) · [verify_creative.py](tools/verify_creative.py) · [make_gate.py](tools/make_gate.py)
