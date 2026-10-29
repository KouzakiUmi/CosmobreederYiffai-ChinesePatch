# 首轮粗校工单与记录协议

本轮以[重写口径](<LOCALIZATION_BRIEF.md>)为准。参考库中的事实须有原文定位；暂定性格或术语不能冒充终裁。

## 输入

只读 corpus 当前快照中的 packet JSON / Markdown。每个包保持完整 DS entry 或 VSN 文件；包含原英文、当前归档中文、原 ledger 草稿与控制上下文。当前中文物理空行可能是已经合句的尾行，须按场景合计意思判断，不能逐行配对报漏译。

SFW / NSFW 仅当整场源文、当前文和控制结构都相同才共享一份审读实体；别名保留各自来源行与 ID。不同主角／逻辑路径不按单句相同合并。工单混排不代表游玩顺序。

## 过程

1. 小段 read 全包，防止长输出被裁剪。记录实际看过的区间；搜索、统计和程序遍历不算语义通读。
2. 整场先读英语，判断动作、条件、角色意图、信息落点，再连读当前中文。
3. 第一遍收集事实与候选问题；参照库汇合后复核建议，修正先入为主的性格假定。
4. 有问题给完整短段重写；不是只把一两个英语词换成同义词。不凭空补剧情，不跨说话人或控制事件重组。
5. 无问题或合法变体明确保留。用途未证实的 code、仅有转录的 image 单列待核，不能算玩家可见文本已校。
6. 不回写正式译文、不标 reviewed / approved，不改脚本节点与归档。

## 独占输出

每个包在 `audit/packet-NN/` 单独输出以下文件，同一包只有一个写入人。

### findings.jsonl

每行一条发现，至少字段：

```json
{"finding_id":"P01-001","scene_id":"SC...","row_ids":["CAT:O..."],"severity":"B","category":"continuity","source_quote":"完整相关原文短段","current_quote":"当前归档对应段","proposed_zh":"按中文重写的完整短段","reason":"为什么需要改、怎样承接上下文","evidence_refs":["资源/entry/Ln","稳定unit或occurrence ID"],"reference_keys":[],"status":"proposal","apply_scope":"scene_draft_only"}
```

类别可用：`meaning`、`continuity`、`idiom`、`voice`、`term`、`relationship`、`gameplay`、`format`、`source_uncertainty`、`usage_unverified`。待核问题 `status=needs_evidence`；不得为了填字段编造译文或事实。

### coverage.jsonl

每个输入场景一行，无遗漏、不重复：

```json
{"scene_id":"SC...","read_status":"read_full","row_ids":["本场所有review_row_id"],"context_checked":true,"findings":["P01-001"],"result":"issues_found","notes":"场景判断和边界"}
```

未看全须 `read_status=partial` 或 `not_read`。`result` 可为 `issues_found`、`retain`、`needs_evidence`、`inventory_only`。对白与 VSN 必须核完整脚本控制语境；code／image／用途未核的 UI 不强制声称 `context_checked=true`，文本读完不等于其运行时用途已核。code / image 即使读完全，也只能记录用途／转录范围，不冒称玩家实显或图像验证。`row_ids` 可精确列本场 canonical ID 或精确列全部版本别名 ID；若另有 `canonical_row_ids`，其集合必须与主审行完全相同。

### reading-log.json 与 summary.md

记录 packet 输入 SHA、实际 read 区间、是否发生裁剪、精读范围与未覆盖项。摘要包含高风险连续段、角色／设定新增证据、需要后续整段精修的工单，不用“未发现问题”替代审读说明。

覆盖收据是可追踪声明，不是自动证明模型理解正确；后续仍须抽取高风险段独立复核。最终汇总严格区分语料已入库、自动检查、人工式语义通读、发现复审、正式应用与实机验证。
