# Cosmobreeder Yiffai 简体中文本地化校对项目

目标游戏：`1.0.5_full`。语言：简体中文。**主 JAR 与 patch.pak 均纳入项目，补丁覆盖主程序。**

这是本地授权处理项目，含原游戏成人文本和图片。不要把原资源作为开源代码或独立素材包分发。

## 从哪里开始

- **当前人名入口：[R3全角色音义统一](<editorial/r3-names/README.md>)。** 36项逐名裁决，采用雄猫／毛鼠、伊吠／伊吠妮等；以[正式姓名台账](<translations/character-names.json>)及[839节点操作](<translations/character-name-repairs.jsonl>)为准。构建在R2后、字体前应用，姓名事实不由译名反推，代号／谜题原形例外与零可见自报名也有记录。
- [R2修订结果](<editorial/r2/README.md>)继续继承：339条复审、291应用、45留置、3驳回；[前轮节点台账](<translations/editorial-r2-repairs.jsonl>)的非姓名内容全部保持。人物／世界原文证据和后续系统精校仍按[R1方案](<editorial/r1/TRANSLATION_PLAN.md>)；R1／R2修前证据不倒改，旧稿中的人名不能覆盖R3。
- 冻结初翻单元库记录 **8,146 条 draft、827 条 untranslated，共 8,973 单元**；它不包含R2节点修订层，不能单独代表当前显示中文。其中 code／image 候选与普通正文不能混算待译进度；草稿状态也不等于当前归档的实际覆盖率。SFW 独立来源和既有合句后处理另有台账，本轮对照最终候选中文而非只读修前草稿。旧工作表与生产检查点原样保留，不再作为本轮唯一执行入口。
- [历史初翻检查点](<reports/gpt-batch180-summary.json>)：保留 batch_180 当时的40目标验收记录，不作为当前内容修订进度。旧工作表仍可作历史对照，不能覆盖R2已闭环节点。
- 历史试译对照：[GPT试译40条对照.xlsx](<review/GPT试译40条对照.xlsx>)，仅作查看对照；正式校对回填请使用完整阶段快照。
- 技术与映射：[技术与映射说明](<docs/技术与映射说明.md>)。
- 字体补丁实现依据：[字体渲染逆向与补丁指南](<../docs/字体渲染逆向与补丁指南.md>)，含类映射、FNT/图集、缓存绘制、三类定位路径、混合着色及补丁验收清单。
- 阶段流程：[初翻与两轮精校](<docs/翻译与两轮精校流程.md>)。只参考 WoC 的流程，不参考其风格、术语或 Ren'Py 专有规则。
- 图像核对：[固定资产浏览器](<review/image_browser.html>)。
- 术语、图片转录和单位置覆盖表都在 `review/`。
- 初翻保留真实模型来源并写入工作表 model 列；本阶段普通与合规敏感完整源分流验收；未批准目标及既有留置项不动。当前模型分流见[模型分流规则](<docs/模型分流规则.md>)；[旧派单策略](<reports/model-dispatch-policy.json>)仅为历史证据，旧 MiMo/其他模型派单说明不作为当前指令。新包全量身份/格式增量检查＋完整源及全目标语义对读，不把 draft 或工作表导出成功当作终审/实机验收。

## 目录职责

```text
project.json                 版本、源安装、依赖、模型与运行时补丁指纹
sources/archives.json        两个原归档的 SHA-256
sources/blobs/               内容寻址的解密资源快照；原文保留原始字节
catalog/resources.jsonl      有效资源以及所有历史覆盖版本
catalog/occurrences.jsonl    每个文本出现位置的完整映射与原格式
catalog/units.jsonl          上下文区分后的稳定翻译单元
catalog/atlas_regions.jsonl  所有图集区域的页、坐标、索引与裁剪参数
catalog/scene_animations.jsonl 剧情动画每帧切片、延迟和首帧预览位置
catalog/code_string_locations.jsonl 代码字符串的 CP / UTF-8 索引和使用方法
catalog/additional_json_candidates.csv 其他 JSON 中待判断的文本候选
assets/source/              原始 PNG 页
assets/fixed/               固定/单帧资产裁图；并非全部都含文字
assets/scene_previews/       按 slices.json 重组的动画首帧
runtime/                    已实机验证的字库与正文 Unicode 补丁
reference/                  旧表候选/术语种子，仅作迁移参考
review/                     人工工作表、术语表、图片表及单位置覆盖表
translations/zh-CN.jsonl     初翻单元记录（冻结草稿，不含后续节点修订层）
translations/editorial-r2-repairs.jsonl  R2逐节点修订的正式来源锁定台账
translations/character-names.json  R3全角色姓名／姓氏／昵称裁决
translations/character-name-repairs.jsonl  R3名字层的精确来源锁定操作
batches/                    只读的 Grok 分批输入及分配清单
 drafts/                    Grok 原始初翻输出（保留来源，不直接覆盖原文）
reports/                    提取统计、自动检查、初翻合并和测试报告
builds/                     仅供预览/打包的输出，不指向 Steam 安装
 tools/                     可复现项目工具
 docs/                      技术、翻译与执行交接资料
```

## 校对方式

主表列：`source` 原文、`initial_zh` Grok 初翻、`review_zh` 校对稿、`status` 状态、`notes` 备注。

1. 不改 `id`、原文和原文哈希。
2. 在 `review_zh` 写校对稿；完成后设置 `reviewed` 或 `approved`，填写 reviewer。
3. `draft` 不代表审校通过；`blocked` 表示拒译或其他明确阻碍，不能算完成。
4. 同一句若只有某个位置需要不同译法，编辑单位置覆盖表，不必牺牲其他上下文。
5. code 页只含候选，不保证面向玩家；确认用途后才能勾选 `usage_approved`。
6. 图片页可以维护文字转录与译文，但不能把填好文字当成已重绘/已部署。

## 命令（在此项目目录运行）

使用系统独立 Python，不使用 `.dsh` 内的解释器。依赖版本已记录；本轮没有安装依赖。

```powershell
$py = 'C:\Users\Fractal\AppData\Local\Programs\Python\Python312\python.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'

# 初翻完成或收到新分片后：校验身份并合并，保留原始分片
& $py tools\review.py merge-drafts

# 导出/更新工作表；注意会替换生成的工作表，先导入或另存人工修改
& $py tools\review.py export

# 导入人工工作表；核对原文、ID 与哈希后才写权威记录
& $py tools\review.py import-review 'review\翻译校对.xlsx'

# 占位符、换行、字库覆盖及宽度风险检查
& $py tools\review.py validate

# 生成已校对资源预览，只允许输出到 builds 的新子目录
& $py tools\review.py render 'builds\review-preview'

# 开发检查：显式允许草稿预览，但有阻断性格式错误时仍拒绝回填
& $py tools\review.py render 'builds\draft-preview' --include-drafts

# 分别构建主 JAR 和 patch.pak；默认只显示计划，不写文件
& $py tools\package.py --output 'builds\package-preview'

# 明确 --write 才写入 builds 下的新目录；绝不原地安装
& $py tools\package.py --output 'builds\package-reviewed' --write
```

**禁止使用旧工作区的通用重打包脚本直接改原安装。** 该脚本仍保留过时的 `st.*` 字体逻辑，且旧表只按原文散列去重，缺少本项目的完整语境映射。

## 复现与已知限制

- 源归档位置保存在配置中，重新提取前必须核对 SHA-256。提取器在目录已经有单元库时会拒绝覆盖，防止破坏校对身份。
- 全部来源/覆盖关系保留；不会把已被补丁替换的旧文本混进当前初翻。
- 原始音频银行仅登记，不复制进文本校对项目。
- 图像候选名称匹配不等于 OCR。未人工检查的图片明确标为待核对。
- 宽度预算只是提示；多行排版、字体 wrapper 行距和全部 UI 容器仍需实机验收。
- Grok 新拟译名另存术语提案表，冲突未擅自抹平；例如 BIGBOLD 的两种拟译已标为待定，后续暂保留原名。
- 已核对本机 Fusion Pixel 字体的版本、SHA-256 与内嵌 OFL 1.1 声明，并保留官方许可文本。许可只覆盖对应字体部分，不为原游戏资源或组合字库的公开分发提供整体授权。
- 打包工具会加入中文运行时补丁与字体许可说明；图片重绘不包含在自动打包流程中。
- 字幕技术链路已在隔离副本通过实机验证；并不代表全量译文已经部署或全游戏测试通过。
- 本项目工具不会自动修改 Steam 原安装。

- 下一唯一执行入口：[batch_133工单](<batches/grok-sensitive/batch_133.job.json>)、[派单文本](<work/gpt-neutral-handoff/batch_133-dispatch.txt>)；阶段全部收尾、最新正式基线最后冻结全SHA与writer明确释放后由主控直派Grok36。后继[134准备工单](<batches/gpt-ordinary/batch_134.job.json>)普通33只准备，正式基线待133完整闭环。旧分类/留置/真实拒绝记录原样保留。

## 2715→3011文本生产阶段

- 140–148共9包，新增296条初稿，完整源/296目标/388位置对读及机器门禁闭环。仍未两轮精校或实机验收。
- [阶段证据](<localization/reports/production-stage2715-3011-summary.json>)、[真实模型与父调度来源](<localization/reports/production-stage2715-3011-dispatch-lineage.json>)、[精简接力](<localization/work/coord-sol/执行接力-after148.md>)。
- [149工单](<localization/batches/grok-sensitive/batch_149.job.json>)仅2目标保守非露骨调侃；[150工单](<localization/batches/gpt-ordinary/batch_150.job.json>)仅33目标完整普通根；均未派/未计完成。149正式基线以最后冻结工件为准，150仅准备。
- 正式入口为caller-context v4及production v6；旧v3弱门禁保留历史但不用于生产。初QA与修前档不可覆盖，修后用单独final-preflight报告。独立F1签收范围与未覆盖边界见[签收002](<localization/reports/production-independent002-orchestrator-stage-conclusion.md>)。
