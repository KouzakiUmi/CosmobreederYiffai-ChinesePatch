# batch-08-part05 精校工单：VSN 剧情场景脚本（第 5／5 部分）

本工单供**两路独立精校**使用：两路拿到完全相同的输入与口径，各自独立出提案，由主代理交叉核验后裁决。两路之间不通信、不参考对方产物。

## 一、输入（相对仓库根）

| 文件 | 用途 |
| --- | --- |
| `localization/editorial/r9-polish/batch-08-part05/orders/batch-08-part05.reader.md` | 工单正文：16 场、449 行、英文＋candidate26 当前中文 |
| `localization/editorial/r9-polish/batch-08-part05/orders/batch-08-part05.json` | 同源结构化数据（scene_id / row_id / line / controls） |
| `localization/editorial/r9-polish/batch-08-part05/orders/reference-excerpt.md` | 人物、称呼、术语、容器限制摘录 |
| `localization/editorial/r1/TRANSLATION_PLAN.md` | 方法口径（第五节七步重写、第七节分级） |
| `localization/editorial/r1/LOCALIZATION_BRIEF.md` | 语域分层与保护边界 |
| `localization/editorial/r1/reference/characters-primary.md`、`characters-support.md`、`world-and-plot.md` | 需要时定点查阅，**不要整读** |

`current` 是 `localization/builds/r9-polish-candidate26` 的实际显示行（R9 batch-01～07 已并入），不是初翻草稿。正式台账 `zh-CN.jsonl` 只用于追溯，不得据其覆盖当前行。

## 二、产出（只写三个文件，写入派单指定的输出目录）

1. `findings.jsonl` —— 每条发现一行 JSON。
2. `coverage.jsonl` —— 每个输入场景一行，无遗漏、不重复。
3. `summary.md` —— 覆盖统计、发现分布、高风险段、跨版本不一致、待核项、未覆盖项。

不要修改任何其它文件；不要写台账、归档、构建产物或译文库。

## 三、判据

按 `TRANSLATION_PLAN.md` 第五节七步重写：复述意图 → 锁事实 → 连读现译 → 重写整段 → 放回人物 → 倒查英文 → 再看结构。

分级：
- **A**：误义、漏义、施受／否定错、关系错、玩法误导、条件或揭示顺序破坏、占位符或结构损坏。
- **B**：整段衔接不成立、翻译腔、语用或笑点失效、角色口吻／称呼漂移、语境术语不一致。
- **C**：意思口吻都成立后的节奏与文笔打磨。C 只报你能给出明确更优理由的，不要凑数。
- **needs_evidence**：原文自相矛盾、说话人／触发条件存疑。用 `status` 表达，不冒充 A/B/C。

无语病且保留人物差异的译文**明确记 retain**，不为制造改动而重写。

## 四、硬约束

1. 英文原文、CONTROL 行、`row_id`、`line`、`speaker`、前缀与缩进结构一律不动。
2. `proposed_zh` 是**完整物理行**：原样保留 `current` 的行首前缀（如 `  The0: `、`  * `、`      Mauser: `）与行尾，只替换正文。前缀长度、冒号、方括号位置不改。
3. 不增删物理行、不合并两个说话人。若一句话应重分到相邻行，只在 `note` 里说明方案，`proposed_zh` 仍只给本行文本。
4. 保护标记原样保留：`[` `]`、`@DerekChipReport`、`<3`、`$`、`%`、`|`、`<...>`、数字与频率（`28.250`、`27.850`、`28.880`）、`Lect`、`OTP`。
5. 剧情框约 240px、12px 字；单行正文尽量不超过约 20 个全角字。确实必须更长时，在 `note` 写 `行宽待实测` 并说明理由。
6. 已裁决项不得重提：R3 人名终裁（伊吠、伊吠妮、毛鼠、雄猫、波苏、麦森、The0 保留英文、季高、星杀等）、R8 谜题提示措辞、R5 创译与 R6 术语回改。
7. 不改玩法条件、施受关系、否定、数量、揭示时点；不新增剧情、动机、口癖、亲密度或性化程度。
8. 全大写不等于吼叫；断词、结巴、被打断、信号失真按功能区分，不能统一抹平，也不能凭空添加。
9. `current` 为空的 ROW 是既有合句的尾行，**不得报漏译**；按整场合计意思判断是否完整。
10. 女线（`datadf`，Yiffany）与男线（`datadm`，Yiffai）分别处理，不把一版措辞机械复制到另一版；同型台词可作「跨版本不一致」发现，注明两边的 `row_id`。
11. **术语改动必须给出处**：主张把某个物种／道具名改成另一个写法时，`reason` 里要指出依据来自哪一行（游戏内词典条目名、同 root 另一场、或 UI 文件），不能只写「按术语表」。参照摘录第三节的术语若与语料冲突，以语料为准，并在 `note` 里报出冲突。

## 五、findings.jsonl 字段

```json
{"finding_id":"P08-0501","scene_id":"SC...","row_ids":["CAT:O..."],"severity":"B","category":"continuity","source_quote":"完整相关英文短段","current_quote":"当前对应中文行","proposed_zh":"完整替换行（含前缀）","reason":"为什么要改、如何承接上下文","reference_keys":["本批语域","称呼矩阵"],"status":"proposal","note":""}
```

- `finding_id`：`P08-0501` 起递增，不与其它批次冲突。
- `category`：`meaning|continuity|idiom|voice|term|relationship|gameplay|format|source_uncertainty`。
- `row_ids`：本发现涉及的全部 `row_id`；跨行改写在 `note` 注明分配建议。
- `source_quote` / `current_quote`：必须是工单内真实存在的完整短段，不得改写。
- 一条发现只处理一个判点；不要把全场改写塞进一条。

## 六、coverage.jsonl 字段

```json
{"scene_id":"SC...","read_status":"read_full","row_ids":["本场全部 row_id"],"result":"issues_found|retain|needs_evidence","findings":["P08-0501"],"notes":"本场判断与边界"}
```

`read_status` 只能是 `read_full` / `partial` / `not_read`；确实读不全就如实写 `partial`，不得虚报。

## 七、summary.md 必含

- 输入工单文件名与行数、实际读完的场景数。
- 发现总数及 A／B／C／needs_evidence 分布，按 root 归组。
- 高风险连续段（问答错位、合句断点、无线电套语）。
- 男女两版的不一致清单。
- 未覆盖项与「本工单不能证明的东西」。

## 八、停止条件

- 全批所有场都有 coverage 行、findings 每条字段齐全即完成。
- 遇到超出本批范围的文本或需要改动归档才能完成的事项，只在 summary 记录，不越界执行。
