# R3 独立工程／载体核验：PASS

**范围：candidate6 → final-01 的 name-only 操作及当前正式 helper／同步数据源码。不是 candidate7 或发行封签批准。** 本报告冻结；后续实际归档与17项CPU结果另写 final-review，不覆盖本报告。

完整输入SHA、逐项计数和66资源重建SHA见 [engineering-01.json](<localization/editorial/r3-names/review/engineering-01.json>)。语义姓名裁决沿用独立 [names-01.json](<localization/editorial/r3-names/review/names-01.json>)，本轮不进行全文文学精校。

## 确定性范围证明

- **839操作／895姓名span／66改动资源：PASS**。独立脚本没有调用作者编译器或 apply_entries；独立递归JSON词法定位、物理行定位与反向splice，66份 before/after 均与 final-01 preview 逐字节一致。
- candidate6两归档SHA和CRC、537份清单明文SHA、每条op完整资源SHA与old、885份原始carrier样本SHA及定位全部一致；**无源样本差异**。
- 895 span逐一核正式旧变体、目标、合法顺序／不重叠和原文切片；重建后所有非姓名内容UTF-8字节不变。69个JSON目标原始token编码均为同一canonical编码，未以重新序列化掩盖其他字符改动。
- 770行前缀、839字段marker顺序／动态@／程序ID／The0数字与case、空合句、537资源物理EOL序列原样。全部JSON key原始词法token及非目标值原样；471份非目标清单资源字节原样。
- **R2 778项全部保持**：candidate6各目标等于R2冻结new；有名字交叠者仅批准的姓名span变化，其余完整目标不变。
- 同field多名41处完整保留；不合并姓名与同姓。实际重复名样本见 [family-samples.json](<localization/editorial/r3-names/review/engineering-isolated-01/family-samples.json>)。
- 结巴仅迁移原有22个单音片段，分隔符、次数与位置不变，新音严格为新名首字。昵称仅uppercase TOM所证3个精确carrier：jar/datadf/1:4402、patch/datadf/1:4573、patch/datadm/1:3947。

## 载体用途：不是“string或key不叫id所以安全”

最初对28个非ui.* JSON操作暂HOLD，经实际candidate6类的独立反汇编与访问器引用核验解除。保留最初机器检查结果，不伪造为一次性自动通过。

### datav：53操作，含12个非ui.*值

- PRG.lf把统一字符串映射的 `(key,value)` 转成 `(key,SL(value,key))`；SL类型名为 **DictionaryString**，显示值与键分别保存。证据：[loaders.javap.txt:1408–1470](<localization/editorial/r3-names/review/engineering-isolated-01/loaders.javap.txt#L1408-L1470>)、[log-entry.javap.txt:950–969](<localization/editorial/r3-names/review/engineering-isolated-01/log-entry.javap.txt#L950-L969>)。
- SH按原键取SL，统一name/desc拼键接口并不使用中文显示值反查身份：[dictionary-model.javap.txt:13–100](<localization/editorial/r3-names/review/engineering-isolated-01/dictionary-model.javap.txt#L13-L100>)。
- KQ$b/c从原actor ID拼接 `.popup` 查字典，返回值转显示文字；ID继续单独用于对象构造：[consumers.javap.txt:2449–2511](<localization/editorial/r3-names/review/engineering-isolated-01/consumers.javap.txt#L2449-L2511>)。zp同一路由进入消息队列：[consumers.javap.txt:1882–1915](<localization/editorial/r3-names/review/engineering-isolated-01/consumers.javap.txt#L1882-L1915>)。
- 因而非ui前缀popup及SpecialWhistle.desc仍为显示字典值，不是普通name/participant脚本内部ID。仅改值，所有键原样。

### datay：16个missionLog header/text

- Ll分别解码id、position、flag、header、text、subject、locationName、gfx；Li访问器 `a=id`、`g=header`、`h=text`：[mission-consumers.javap.txt:622–679](<localization/editorial/r3-names/review/engineering-isolated-01/mission-consumers.javap.txt#L622-L679>)。
- Lj把g/header与h/text组装、解析、排版成正文：[log-entry.javap.txt:466–555](<localization/editorial/r3-names/review/engineering-isolated-01/log-entry.javap.txt#L466-L555>)；Lq把header制成SL／IC显示标题：[mission-consumers.javap.txt:1753–1827](<localization/editorial/r3-names/review/engineering-isolated-01/mission-consumers.javap.txt#L1753-L1827>)。
- 身份进度键明确是 `mission_log_seen_ + Li.a(id)`，不是header/text：[mission-identity.javap.txt:402–414](<localization/editorial/r3-names/review/engineering-isolated-01/mission-identity.javap.txt#L402-L414>)。
- 独立穷举candidate6全部PRG类常量池的Li访问器引用，header/text只见模型／codec、Lj文字组装、Lq标题；未见身份或流程匹配消费者：[mission-method-refs.json](<localization/editorial/r3-names/review/engineering-isolated-01/mission-method-refs.json>)。
- 因此可批准内容字段中的姓名；包括stub／未来日志，但**不宣称每条现在可达或已实显**。

### 脚本行

770个目标前缀完整枚举为原actor（含Anon/Fox）、`*`、`text:`、`lang(Fox):`；没有选中name:/participant:/变量赋值载体。原前缀逐字节不变，不把姓名显示映射反写actor。详情：[puzzle-and-prefixes.json](<localization/editorial/r3-names/review/engineering-isolated-01/puzzle-and-prefixes.json>)。

## 特殊保护／同步

- 不由名字反定物种：操作仅姓名span和原有结巴首音；没有修改物种描述。支持者、内部ID、四个未证个人的反写标题、动态@及所有非目标值保持。
- Sevaw/Erauqs仅8个已证个体档案标题及2个卡背正文改名；谜题线索与其他字符串不变，未直送几何答案。详见 [puzzle-and-prefixes.json](<localization/editorial/r3-names/review/engineering-isolated-01/puzzle-and-prefixes.json>)。
- 正式36目标／37alias、Yifany别名、TSV、component与helper当前同步；脚本仅在内存调用outputs核对，没有写作者文件。36目标均≤6字符。中文选classic，Latin保传入role；六字符频率48px／完整104px及classic8字形metrics由现有测试覆盖，但**本轮未执行candidate7字形测试**。
- JF实际candidate6反汇编仍有gitgud/static/starkill→??????及The0 flag门控：[consumers.javap.txt:2855–2923](<localization/editorial/r3-names/review/engineering-isolated-01/consumers.javap.txt#L2855-L2923>)。当前 [RadioLabelsPatch.java:32–38](<localization/layout/tools/java/RadioLabelsPatch.java#L32-L38>)只在JF返回后插display，不在ID参数或判定前映射。candidate7实际class仍待独立核验。

## 限制与执行边界

1. PASS仅覆盖本阶段输入SHA冻结的源码、正式操作及preview；实际candidate7归档／字形／class差异和17CPU待主控通知，另报。
2. 原inventory的字段名／字符串启发式不足独立证明用途；本次对实际839操作另做消费端证据，不能把这个PASS推广到未来任意name字段。
3. 静态数据流证明不代替游戏实机、当前可达性、文学或语义人工审批。537份清单文本之外的非文本归档资源，要到candidate7才可比较新旧。
4. 未安装、未Git写、未再委派、未构建父候选、未启动游戏、未改作者模块／台账／正式库／归档、未重复跑整套CPU。所有实验只写review隔离目录。
5. 初始javap不在PATH（exit127），读取项目integration脚本确认现有JDK后使用其绝对项目路径；未安装工具。独立脚本曾将defaultdict容量误记为touched数，已修正为66；66份splice结果始终逐字节通过。

隔离实现：[audit.py](<localization/editorial/r3-names/review/engineering-isolated-01/audit.py>)、[method_refs.py](<localization/editorial/r3-names/review/engineering-isolated-01/method_refs.py>)；原始日志：[run.log](<localization/editorial/r3-names/review/engineering-isolated-01/run.log>)。
