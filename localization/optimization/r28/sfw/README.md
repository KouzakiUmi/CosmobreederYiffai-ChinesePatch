# SFW 独立来源候选本地化

这是原始 JAR 自身的派生翻译台账及只读重建组件，不是安装包，也不是人工终审完成声明。仅新增本目录、[纯 API](<../../../tools/sfw_localization.py>)与[新测试](<../../../tests/test_sfw_localization.py>)；未改既有主译文、catalog、canonical joins、构建器、字体、旧归档或存档。

## 冻结结果

原始来源 JAR SHA-256：`cd37e445b36b8ad1b64a0089fe718362ec130af9219ee02f215d223ba8fa6221`。42 个来源资源＝2 DS＋1 UI 字典＋39 VSN。以下数字按**原 JAR 源记录**计，不按唯一句子或最终节点计。

| 类型 | 原记录 | 精确英中复用 | 新增／修正候选 | 显式保留原文 | 待审、不输出 |
|---|---:|---:|---:|---:|---:|
| DS | 5471 | 4976 | 439 | 56 | 0 |
| VSN | 792 | 647 | 143 | 2 | 0 |
| UI | 871 | 734 | 44 | 93 | 0 |
| 合计 | 7134 | 6357 | 626 | 151 | 0 |

- 原审计的 **460 条未匹配 DS**全部按自身 entry／prefix／完整原文定位：417 条新候选＋39 条精确全文复用＝**456 条中文候选**；另4条经原JAR上下文独立复核，为刻意失真的广播，原Latin碎段显式保留，不计完整中文。
- 另有 **16条SFW独立DS后处理**，修复834共享合句或单句继承的“功-能／完-好／物-理／目- 前”等中文断词污染。全部由本JAR完整有序英文、root／prefix、实际应用canonical组和旧中文共同验证，不能仅凭中文相同或PAK行号迁移。它们不重复计入626条源候选。
- 新增的 19 组 **SFW 自身 VSN 合句**另有独立来源台账，逐组读过本 JAR 前后演出上下文；都是同块、同说话者／叙述者的连续普通 `text`，不跨控制行、不含 `auto`／`lang`。38 个原节点变成19个，源命令级手动推进数减少19。软分页后最终交互次数仍需运行层验收。
- 既有 canonical DS 合句仍为 **834 应用／122 源变体不符跳过**，没有降低来源门禁。DS 源节点5471→4502；VSN792→773；UI仍871键。
- 启用特殊语言中文候选时，内存最终输出含汉字的 DS／UI／VSN 节点分别为4376／778／758；无汉字不自动等于漏译，字典保留的空槽、按键、地点短码、货币及署名都有显式记录。
- `SpecialGeiger.desc` 新候选为“通讯联络｜探测秘密！”（实际分隔符为 ASCII `|`），保持两行玩法含义。
- final-01真实JVM发现`ui.end.cr6`旧复用候选34格/272px；仅把两端各4个装饰空格改为3个，完整保留“FMOD STUDIO，由 FIRELIGHT 开发”。[60字段实际classic8度量](<ending-field-layout.json>)确认29非空字段全部≤32格/256px，没有其他超宽。API保留原32格容量门禁，padding例外仅绑定此源ID与精确正文，不授权其他空白漂移。

以上都是候选，不等于人工批准、字体实际可见或实机全场景验收。已有草稿的来源与复用方法逐条保留；冲突候选未按多数票猜译。

## 数据入口

- [组件协议](<component.json>)：主构建直接读取的入口、参数、返回类型、顺序与门禁。
- [来源清单](<source-manifest.json>)：完整归档 SHA、加密索引／entry SHA、解密资源 SHA、复用输入 SHA、各 ledger 文件 SHA。
- [DS 台账](<ledger-ds.jsonl>)、[VSN 台账](<ledger-vsn.jsonl>)、[UI 台账](<ledger-ui.jsonl>)：完整英文、候选中文、状态、原 JAR 身份与来源链。不是只有统计的覆盖清单。
- [SFW VSN 合句台账](<vsn-joins.jsonl>)、[逐组演出上下文](<vsn-join-contexts.jsonl>)、[人工编写的候选决策](<vsn-join-decisions.json>)：19组完整源身份、输入译文 SHA、整句中文、前后控制上下文与点击差额。
- [DS独立后处理台账](<ds-polish.jsonl>)、[16条适配审查](<ds-polish-review.json>)：全部16条均在SFW最终旧中文中仍有污染，已修；自身源ID和已应用canonical组为主门禁，旧中文完全相同仅为附加条件。
- [机读覆盖](<coverage.json>)、[剩余与刻意失真保留](<remaining-review.json>)、[完整目标字符集](<required_chars.json>)：2113个目标码点，包含19个新合句、16条后处理及 Fox／HardFox 中文备选全文；不因r27缺字强改同义词。
- [验证结果](<verification.json>)、[测试日志](<tests.log>)、[完整重建报告](<rebuild-report.json>)：42个内存输出entry SHA、834组合句源→blank映射、19组VSN源→blank映射、控制序列SHA与剩余条目。
- [VSN来源迁移扫描](<vsn-join-source-review.json>)：另一组件300条建议中，仅19组在本 JAR 唯一匹配；281组不存在／已变体，完全未套用。该扫描本身不执行修改，19组实际应用依据的是本目录独立合句台账。
- [分批候选](<translations/>)：TSV 是明确逐条编写的候选输入，对应 JSON 冻结完整英文；包含显式保留与待审说明，空字符串只用于原版刻意空槽，绝不计为中文补齐。

## 身份和 fail-closed 契约

每条源身份包含 `archive + archive_sha256 + logical_path + archive_entry + root + prefix + raw_source_sha256`；同一root／prefix／原文重复时，还绑定明确的 `source_ordinal` 与 `source_multiplicity`。整份解密资源 SHA 把分支、顺序、演出及上下文一起冻结。源行号仅是本 JAR 自身的证据，不是定位器；测试故意改成不存在的行号，仍按身份正确匹配。

`raw_source` 保留完整正文，包括原前后空白。DS／VSN哈希针对去掉结构前缀后的完整UTF-8正文；UI针对JSON解码后的完整字符串值。源JSON token的转义形式、空白及原字节同时由完整resource SHA与读时派生字节范围保护。字典只改值token，不改key或其他字节。

输入必须是冻结的**原始** JAR，不能把已翻译／合句的r27资源作为来源；也没有PAK fallback。归档、索引路由、stored entry、明文、源身份、重复数量、ledger摘要、输入译文、上下文或整句SHA漂移均拒绝，不返回部分结果。标记及placeholder按多重集校验，保护重复占位符、控制tag、括号、段落、管道、下划线、数字、ID及显式按键组合。普通英文动词 `SELECT A PROGRAM` 不误认成实体按键。

## 调用和重建顺序

```python
# sys.path 已包含 localization/tools
import dialogue_joins
from sfw_localization import rebuild_candidate_entries

entries, report = rebuild_candidate_entries(
    original_jar_path,
    data_dir=sfw_data_dir,
    canonical_join_records=dialogue_joins.load_records(),
    glyphs=None,  # 字符集发现阶段可省略；最终字体须完整核验
    allow_pattern_candidates=True,  # 仅在下游特殊语言兼容方案已就绪时启用
)
# entries: dict[str, bytes]
# key 为原JAR archive_entry；value 为解密UTF-8明文，不是加密包。
# API不写任何文件或游戏归档。
```

也可调用[简化包装入口](<../../../tools/sfw_localization.py>) `build_replacements(original_jar_path, ...)`，默认加载本目录与canonical joins。

1. 校验原始 JAR 与完整 ledger。
2. 对其自身记录生成候选；DS在内部调用旧安全rewriter进行834组合句，再仅覆盖**未被合句消费**的自身记录，最后按SFW独立台账修正16条断词／标点污染。防止原rewriter覆盖已修正的按键文案。不要在返回结果上再跑一次旧rewriter。默认`enable_ds_polish=True`，关闭仅用于扫描旧基线；未请求canonical joins时，多源后处理明确暂缓，不能假装已应用。
3. 对译好的VSN执行19组独立来源合句：首个`text`承载整句，其余只保留各自EOL，绝不留下空`text:`节点。物理行数、CRLF／LF、无终止换行的末行及全部非text控制命令逐字节不变。
4. 若启用中文Fox／HardFox，最终主集成方案保留原jo可读性门禁，并把**当前mask确定性映射为合法dingbats字形**；运行时PatternSymbols不读取sourceEng。ledger中的原English身份与`symbol_source`仅保留来源证据，不能冒称运行时在重放原英文。默认不启用时，272条特殊角色正文原样保留；不会把中文直接丢给原dingbats冒称可见。此兼容路由由主构建联合验收。
5. 主构建把本字符集与canonical合句／其他组件字符集取并集，统一补字体并检验最终整句所有字符与特殊路由；传入`glyphs`时，本API还会检查最终输出全文，包含末字，而不只抽样首字。
6. 加密和写入**新候选归档**由主构建负责；本组件无加密写包／安装接口。

## 明确剩余

[剩余表](<remaining-review.json>)的 `needs_review`／`needs_translation`现为0；这不是把原刻意失真内容冒报成中文完成：

- 两种受干扰广播各有男女来源，共4条，显式标记 `intentional-corruption/source-preserved`，保留Latin原碎段，不猜补DEF...ING／TEN／END的缺失部分，不计完整中文。相邻`BIG TEN...`两档均保留原碎片，中文上下文不再猜成“大触”。
- `CAPTAIN PUPLOCK`经原JAR上下文独立复核，为幼年太空海盗角色扮演的自拟名；保留PUPLOCK拼写并采用忠实中文上下文。
- 龙卡正面采用中文全文；Ayskammr与既有地区名及相邻红牛卡统一为“艾斯卡姆尔”，Sevaw保源拼写。不因未知音译拒译整句。

上述均为agent-reviewed候选，`human_approved`仍为false。原460缺口是456条中文候选＋4条刻意失真保留，而非460条完整中文。SFW原卡片背面的刻意留白、空结算槽等原样保留，绝不套用PAK成人文案；地点短码、作者署名、实体按键也没有伪装成中文正文。

## 重现与验证边界

```bash
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/sfw/compile_batches.py
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/sfw/build_data.py
# 仅需重新扫描其他组件的16条建议时；生成自己的来源适配台账后再次冻结摘要
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/sfw/prepare_ds_polish.py
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/sfw/build_data.py
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/sfw/verify.py
```

[构建数据脚本](<build_data.py>)与[验证脚本](<verify.py>)只写本目录。`verify.py`实际运行37项隔离测试、内存重建42资源并保存SHA／映射。覆盖唯一性、源漂移、marker／placeholder多重集、整句末字符、SFW／PAK及男女变体隔离、19组合句重复／上下文／输入漂移、控制／auto／角色／EOL／末行守恒；16条DS后处理的源身份、实际合句、旧中文、重放及重复拒绝；刻意失真与专名上下文复核。早期两次测试失败分别来自测试误删原字典末尾换行、误要求已翻译末条text仍等于英文源；修正的是错误断言，源换行与完整译文保留门禁没有放宽。

本worker没有执行JVM真实VSN parser、GL、游戏、部署、安装或存档操作。真实parser与最终字体／特殊语言可见性由主构建的联合验收补证；这里的源parser与字节结构测试不能替代它们。
