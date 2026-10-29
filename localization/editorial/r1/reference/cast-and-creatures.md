# 其他登场者、获救探员与重要生物参照（R1）

> 仅文档整理/粗校，非性格终裁或正式译文；含成人报告与终盘身份剧透。原有三份世界观参照及他人文件未修改。

## 识别入口与覆盖口径

- **先读原作署名再辨人物**：从当前字典 `ui.data.<script>` 及说明键关联同名VSN，识别18位具名获救探员。没有靠预想名单猜人。UI标题/说明是菜单介绍，不自动等于角色亲口自述。
- 另识别6个Fenfen历史档案标题，m/f各一个记录，共12条，不冒称12名不同人物。SEVAW/ERAUQS另有资料卡明确Sevaw/Erauqs个体。字形倒序趣味不代替角色对象/触发核证。
- 本文95条含18探员、12个Fenfen性别化档案、主要首领/具名Fenfen、6店铺场所、44个图鉴对象及叙事/群体补项；不是“所有图像匿名NPC已认出”。[结构化参照](<cast-and-creatures.json>)包含完整所用unit/occurrence链、原文、UI json_key、源路径行号和原始命令prefix。
- 前序已读VSN2321/dex676/items1140个独立unit的source，不是全部重复位置上下文。追加原作56个标题及说明、14条主要首领卡片文本；全部通过当前resources blob与catalog units/occurrences核对。资料标题/卡片较长原文另以本JSON前1–130小段读完。
- 新增男DS连续段：291–347、1007–1088、1404–1483、1552–1628、1695–1818、4964–4972。其余已读范围见[世界观参照](<world-and-plot.md#L5-L9>)；没有重新宣称全量DS所有位置通读或运行时实测。

## 已有角色文档与分轴

- 主角Yiffai/Yiffany/Mauser画像见[主角参照](<characters-primary.md>)；Tomcat/Bossu/Macsen/The0/Gitgud/Starkill/Queen及匿名Fox概览见[配角参照](<characters-support.md>)。此处补获救探员、其他Boss/族群与声音归属，不复制总部长篇人物像。
- 当前证据主要为PAK生效文本；m/f是男女叙事轴，不是SFW/NSFW开关。SFW原JAR不同内容须对自身原文，不将PAK成人动机补进空白/不同场景。参见[内容版本边界](<world-and-plot.md#L11-L17>)。
- **自述/外评/场景事件分开**：自夸、回忆、资料卡介绍与报告编辑都可能有立场；“可信度高”仅指文字定位。只一场支持的语气一律不扩成永恒人格。
- **不能混说话者**：报告第一人称多是获救者；战后VSN第一人称多是玩家；EDITOR’S NOTE是报告编辑；Fenfen的lang(Fox)与主角I can see插话分开。narrator元数据不是最终声部。

## 18位具名报告者速查

|报告槽|原作标题|本场声音关键词|
|---|---|---|
|`f_AgentF01`|YOGO|热情说服、亲昵lil/ya know/hehe，夸张very/Amazing|
|`f_AgentF02`|BUNTLEEN|自问right、where was I转题、俏皮夸张，由纵情转厌倦果断|
|`f_AgentF03`|KAHR|Oh my gosh、拉长音、fo/foever与连串惊叹|
|`f_AgentF04`|KOMET|急迫烦躁、hunky重复、hunk of iron口误，感谢中仍惦记大犬|
|`f_AgentF05`|ERMA|like/totally/ohmygawsh/WTF、疑问转折，天真惊诧|
|`f_AgentF06`|DALEIR|拖长音、eh-heh、自我纠正与粉饰，狡黠反讽|
|`f_AgentF07`|NAMBU|直率戏谑、反问、调侃玩家浪费钥匙|
|`f_AgentF08`|VICKERS|不耐烦、反问命令、cowards/brats蔑称，自豪并自嘲被冷落|
|`f_AgentF0B`|CETARTNI|Golly、戏剧化VILLAIN、礼貌感谢和期待|
|`m_AgentM01`|GAORU|Hmf/Tch/NOT、急躁反问抱怨，末尾尴尬求保密|
|`m_AgentM02`|GEPARD|yours truly/ahem/professionals/rookie假正经长句、居高临下、尾句泄气|
|`m_AgentM03`|TRUVELO|like/yeah sure/right、WHAM BAM、straight/gay冷笑话，急于解释青年腔|
|`m_AgentM04`|VULCAN|lad/nosirree/gentleman/naught/whatfor老派自尊，纠正口误|
|`m_AgentM05`|HENSCHEL|结巴、purropurrly猫谐音、删记录请求，公务语切羞涩|
|`m_AgentM06`|FRANCHI|courtesies/merciful/generous端着英雄自尊，对newbie施惠，夹Eep|
|`m_AgentM07`|CHAUCHAT|明显结巴、道歉hassle、pounding自纠，谨慎转热切|
|`m_AgentM08`|KARBINE|Howdy thar/ta/ya、民间叙述节奏、轻松自嘲|
|`m_AgentM0B`|PANCOR|Hee/hehee、轻快直率、插话解释，不是高傲Top腔|

## 详细角色／对象条目

### 获救探员

#### YOGO · `f_AgentF01`
- **角色功能/身份依据**：犬群采集回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自称物种专家、犬群只是被误解；最初恐惧、后来投入均为其说辞，受孕仅I think
- **口吻/声线**：热情说服、亲昵lil/ya know/hehe，夸张very/Amazing；非冷科普腔
- **观察行为**：开场护住生物并劝玩家别打；收尾劝收武器
- **关系、版本和证据边界**：后续愉悦不追溯改变最初同意，也不证明产下幼犬；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U4bb6b56c691ac36829ad` / `O3ace0f6364551c100088` · `datav/dictionary.json#ui.data.f_AgentF01` · [位置](<../../../catalog/occurrences.jsonl#L6537>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vc72409078324e6d85f3a` / `O832454e4831179fafb7a` · `vsn/f_AgentF01/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L6795>) · [原始来源](<../../../sources/blobs/011d9333e6e863d1dd1c2e571e50521128d300cd7c40988588aa8fd9c8e4bec4.vsn#L5>)
- 证据：`V15b3efe983337013d755` / `O494f564928f3a31b4fa0` · `vsn/f_AgentF01/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L6806>) · [原始来源](<../../../sources/blobs/011d9333e6e863d1dd1c2e571e50521128d300cd7c40988588aa8fd9c8e4bec4.vsn#L25>)
- 证据：`Vb7fcdd5194de509ffa8c` / `O545479757359d51a60fe` · `vsn/f_AgentF01/script.vsn:59` · [位置](<../../../catalog/occurrences.jsonl#L6825>) · [原始来源](<../../../sources/blobs/011d9333e6e863d1dd1c2e571e50521128d300cd7c40988588aa8fd9c8e4bec4.vsn#L59>)

#### BUNTLEEN · `f_AgentF02`
- **角色功能/身份依据**：海盗与机械复制体囚禁回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自称通常擅长避免被俘；误认Fenfen后承认VERY wrong
- **口吻/声线**：自问right、where was I转题、俏皮夸张，由纵情转厌倦果断
- **观察行为**：愿讲经历，末尾准备离开星球
- **关系、版本和证据边界**：UI兔身份不是所有兔同一个人；误认生物不当原生Fenfen；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`Uf779cec7d9f7df13957f` / `O26fc0a98c086b7fe7dc5` · `datav/dictionary.json#ui.data.f_AgentF02` · [位置](<../../../catalog/occurrences.jsonl#L6539>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V3aec0f293981b764bb27` / `O4d53e9afe712d9f6909b` · `vsn/f_AgentF02/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L6834>) · [原始来源](<../../../sources/blobs/8d1f0de0ffec48cd7d30e0ff5c24477ddb889fa89ef4231680fe10c3516e4955.vsn#L5>)
- 证据：`V2f935b338de295ac28dc` / `Oe9e58754c69b9a1cc39a` · `vsn/f_AgentF02/script.vsn:27` · [位置](<../../../catalog/occurrences.jsonl#L6847>) · [原始来源](<../../../sources/blobs/8d1f0de0ffec48cd7d30e0ff5c24477ddb889fa89ef4231680fe10c3516e4955.vsn#L27>)
- 证据：`V210f7cefff0c9177baae` / `O499645554da45492422f` · `vsn/f_AgentF02/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L6866>) · [原始来源](<../../../sources/blobs/8d1f0de0ffec48cd7d30e0ff5c24477ddb889fa89ef4231680fe10c3516e4955.vsn#L58>)

#### KAHR · `f_AgentF03`
- **角色功能/身份依据**：侦察员首次被俘；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自称去过许多星球而未被俘，不是首次任务
- **口吻/声线**：Oh my gosh、拉长音、fo/foever与连串惊叹；不套现实地域方言
- **观察行为**：热烈道谢亲吻式感谢；结尾问如何接繁殖任务
- **关系、版本和证据边界**：害羞不等于毫无外勤经验，受袭后的转变保时序；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U65985c673b8ba9f1c9a1` / `O6d4459d51ad6473965df` · `datav/dictionary.json#ui.data.f_AgentF03` · [位置](<../../../catalog/occurrences.jsonl#L6541>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V95f02a385e7764d6af6f` / `O1c5e5e95713c1f55ddf4` · `vsn/f_AgentF03/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L6874>) · [原始来源](<../../../sources/blobs/4de1d6569827c5e41054b20d2fe565786deeb7d804718a68856e70a2431ef573.vsn#L5>)
- 证据：`V682d920aff5c16495c5a` / `O4fbccecb1db944b6b8cb` · `vsn/f_AgentF03/script.vsn:83` · [位置](<../../../catalog/occurrences.jsonl#L6916>) · [原始来源](<../../../sources/blobs/4de1d6569827c5e41054b20d2fe565786deeb7d804718a68856e70a2431ef573.vsn#L83>)
- 证据：`V99be9bf2fe48d4cc87c5` / `O1df90480febe8fc0de74` · `vsn/f_AgentF03/script.vsn:57` · [位置](<../../../catalog/occurrences.jsonl#L6903>) · [原始来源](<../../../sources/blobs/4de1d6569827c5e41054b20d2fe565786deeb7d804718a68856e70a2431ef573.vsn#L57>)

#### KOMET · `f_AgentF04`
- **角色功能/身份依据**：高温矿区困牢回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：将高温与焦躁相连、称多数满足可复工
- **口吻/声线**：急迫烦躁、hunky重复、hunk of iron口误，感谢中仍惦记大犬
- **观察行为**：自述主动接触，怨只做一轮便被单独关牢
- **关系、版本和证据边界**：原文对方几乎把她撞墙，不颠倒施受；RACCUNNY不擅定杂交谱系；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U4b757e065d4005633f69` / `O680193ef8df946e77571` · `datav/dictionary.json#ui.data.f_AgentF04` · [位置](<../../../catalog/occurrences.jsonl#L6543>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V7ed28541e31a46763985` / `Od57b1a51f3eb6ee4ec0f` · `vsn/f_AgentF04/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L6918>) · [原始来源](<../../../sources/blobs/58d2f809c0e6a579bb252e7901daf6c575ab86e9b77a683de851e0e44ee8bc7c.vsn#L5>)
- 证据：`Vbb278516cbf0c23ab2f5` / `O40a9f215a35fa0a4d90f` · `vsn/f_AgentF04/script.vsn:77` · [位置](<../../../catalog/occurrences.jsonl#L6956>) · [原始来源](<../../../sources/blobs/58d2f809c0e6a579bb252e7901daf6c575ab86e9b77a683de851e0e44ee8bc7c.vsn#L77>)
- 证据：`Ve65d4ef2ec58e215a6c1` / `O44d145f7a224704db567` · `vsn/f_AgentF04/script.vsn:56` · [位置](<../../../catalog/occurrences.jsonl#L6945>) · [原始来源](<../../../sources/blobs/58d2f809c0e6a579bb252e7901daf6c575ab86e9b77a683de851e0e44ee8bc7c.vsn#L56>)

#### ERMA · `f_AgentF05`
- **角色功能/身份依据**：Erma/Daleir搭档新人视角；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：相信搭档建议，又觉得踢打只在挑动怪物，想不起任务
- **口吻/声线**：like/totally/ohmygawsh/WTF、疑问转折，天真惊诧；不每句塞人家
- **观察行为**：听建议反抗、用树枝打晕怪物逃入旧牢
- **关系、版本和证据边界**：不可用Daleir的natural/foreplay评语将Erma反抗改成自愿；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`Uaae0d53312920887448e` / `O0d9081053584931205da` · `datav/dictionary.json#ui.data.f_AgentF05` · [位置](<../../../catalog/occurrences.jsonl#L6545>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V4440c57385ea14a93e55` / `Oda86e90cda64bacd6b96` · `vsn/f_AgentF05/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L6957>) · [原始来源](<../../../sources/blobs/25a1dde5194c0057fd7ff034c8977d61ab1dc730d684ef12ceb7889aea499f27.vsn#L5>)
- 证据：`Vb38ab7447ae500e5fea2` / `O7c9dbd885f58ee3a8ba5` · `vsn/f_AgentF05/script.vsn:22` · [位置](<../../../catalog/occurrences.jsonl#L6968>) · [原始来源](<../../../sources/blobs/25a1dde5194c0057fd7ff034c8977d61ab1dc730d684ef12ceb7889aea499f27.vsn#L22>)
- 证据：`Vec7e8db57e36776f466c` / `Odc0d596c6bafd5225a76` · `vsn/f_AgentF05/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L6989>) · [原始来源](<../../../sources/blobs/25a1dde5194c0057fd7ff034c8977d61ab1dc730d684ef12ceb7889aea499f27.vsn#L58>)

#### DALEIR · `f_AgentF06`
- **角色功能/身份依据**：Daleir资深搭档视角；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自称给Erma指点，却口误险说tricking，需两份报告对读
- **口吻/声线**：拖长音、eh-heh、自我纠正与粉饰，狡黠反讽；不替她圆谎
- **观察行为**：责怪玩家打触手，同时汇报；想找神秘星球
- **关系、版本和证据边界**：名字和狐狸有自报；腹部变化/母亲幻想不等于已产育；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U3df34020d73f9d62b774` / `O3587022e95c6c40a7043` · `datav/dictionary.json#ui.data.f_AgentF06` · [位置](<../../../catalog/occurrences.jsonl#L6547>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V2d24f74492f3c399bf29` / `O074b0061b33542b7204e` · `vsn/f_AgentF06/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7001>) · [原始来源](<../../../sources/blobs/efb300787c67687ce77d16c287b7979a5a0acf090f819f3a95a8a3b7edceab0f.vsn#L5>)
- 证据：`V7bb3c5a2075f6e146bbf` / `O928765560df15822641a` · `vsn/f_AgentF06/script.vsn:90` · [位置](<../../../catalog/occurrences.jsonl#L7050>) · [原始来源](<../../../sources/blobs/efb300787c67687ce77d16c287b7979a5a0acf090f819f3a95a8a3b7edceab0f.vsn#L90>)
- 证据：`V1eb2e27f9d778cf20c6b` / `O886c88e08a1915e7b275` · `vsn/f_AgentF06/script.vsn:59` · [位置](<../../../catalog/occurrences.jsonl#L7031>) · [原始来源](<../../../sources/blobs/efb300787c67687ce77d16c287b7979a5a0acf090f819f3a95a8a3b7edceab0f.vsn#L59>)

#### NAMBU · `f_AgentF07`
- **角色功能/身份依据**：主动滞留探员回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：称制服主动脱、镣铐自己戴、边享受边领薪
- **口吻/声线**：直率戏谑、反问、调侃玩家浪费钥匙；非羞涩结巴
- **观察行为**：感谢开场先为浪费钥匙道歉，报告强调主动示意
- **关系、版本和证据边界**：You would think pulled out tazer为比喻，非实际拔枪；spotty不锁定品种；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U9ca0cee31b548ce4c8e7` / `O9f5b1b8477f7770f7692` · `datav/dictionary.json#ui.data.f_AgentF07` · [位置](<../../../catalog/occurrences.jsonl#L6549>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vefc9459831df85ac1324` / `Oa1e06b020259efd99963` · `vsn/f_AgentF07/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7057>) · [原始来源](<../../../sources/blobs/781ebf12d26890caa73e04effa84e7194724412257fa1231364c84c0dc6156ad.vsn#L5>)
- 证据：`V36720c66e4e811997000` / `Oaff5ce3eb520f58d33e0` · `vsn/f_AgentF07/script.vsn:23` · [位置](<../../../catalog/occurrences.jsonl#L7069>) · [原始来源](<../../../sources/blobs/781ebf12d26890caa73e04effa84e7194724412257fa1231364c84c0dc6156ad.vsn#L23>)
- 证据：`V75d8086ecd39182664a8` / `O858b4d38645c9e7e853b` · `vsn/f_AgentF07/script.vsn:59` · [位置](<../../../catalog/occurrences.jsonl#L7090>) · [原始来源](<../../../sources/blobs/781ebf12d26890caa73e04effa84e7194724412257fa1231364c84c0dc6156ad.vsn#L59>)

#### VICKERS · `f_AgentF08`
- **角色功能/身份依据**：自封海盗女王探员；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自称支配海盗、幻想Queen；承认sloppy，未看清沉默探员
- **口吻/声线**：不耐烦、反问命令、cowards/brats蔑称，自豪并自嘲被冷落
- **观察行为**：催迟到救援，急于找海盗
- **关系、版本和证据边界**：Vickers是UI真名，海盗女王是幻想，非Traeh/Enelye；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U2a327735fd7fa131e065` / `O1f1e467bdc29be6a3521` · `datav/dictionary.json#ui.data.f_AgentF08` · [位置](<../../../catalog/occurrences.jsonl#L6551>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V24ce8e7ef73a56cee17c` / `Oc78e41b8da8f19c28692` · `vsn/f_AgentF08/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7101>) · [原始来源](<../../../sources/blobs/125a52a5276ae17c0d9a12e6229f20d9978f802fa8b92fe25f30efb7e8e159aa.vsn#L5>)
- 证据：`Vc243643e43f96d240052` / `O9545cc9381b4352e5dd3` · `vsn/f_AgentF08/script.vsn:82` · [位置](<../../../catalog/occurrences.jsonl#L7145>) · [原始来源](<../../../sources/blobs/125a52a5276ae17c0d9a12e6229f20d9978f802fa8b92fe25f30efb7e8e159aa.vsn#L82>)
- 证据：`Vb09371c684dd2126a614` / `O75f0d796a90ff78db566` · `vsn/f_AgentF08/script.vsn:56` · [位置](<../../../catalog/occurrences.jsonl#L7131>) · [原始来源](<../../../sources/blobs/125a52a5276ae17c0d9a12e6229f20d9978f802fa8b92fe25f30efb7e8e159aa.vsn#L56>)

#### CETARTNI · `f_AgentF0B`
- **角色功能/身份依据**：桌面岗位新人外勤；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：免责书、迷路、眼镜丢失、未看清俘获者均自述
- **口吻/声线**：Golly、戏剧化VILLAIN、礼貌感谢和期待
- **观察行为**：试图整合模糊记忆采集数据，期待下一任务
- **关系、版本和证据边界**：CETARTNI保原UI拼写；新人不是未成年；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 女线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U53013c8a57190d8ba229` / `O95db8a5b1e9dd2e1ca6a` · `datav/dictionary.json#ui.data.f_AgentF0B` · [位置](<../../../catalog/occurrences.jsonl#L6553>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V66a71ccb258440e72edd` / `O8743c5c177e752c09962` · `vsn/f_AgentF0B/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7148>) · [原始来源](<../../../sources/blobs/dcbff217f25e1183ee888032679154c06c203e04cb7b10b4bc15139f92eba8d9.vsn#L5>)
- 证据：`V0c60e241fb291fe048f4` / `O043b03200c93c2c60d9a` · `vsn/f_AgentF0B/script.vsn:31` · [位置](<../../../catalog/occurrences.jsonl#L7161>) · [原始来源](<../../../sources/blobs/dcbff217f25e1183ee888032679154c06c203e04cb7b10b4bc15139f92eba8d9.vsn#L31>)
- 证据：`V9ea60ac2a862a0034bb6` / `O723d7b356a59348695e0` · `vsn/f_AgentF0B/script.vsn:52` · [位置](<../../../catalog/occurrences.jsonl#L7173>) · [原始来源](<../../../sources/blobs/dcbff217f25e1183ee888032679154c06c203e04cb7b10b4bc15139f92eba8d9.vsn#L52>)

#### GAORU · `m_AgentM01`
- **角色功能/身份依据**：犬舍被俘报告；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：怪招募/队长、声称不享受且怕录像公开；不替其定真实心愿
- **口吻/声线**：Hmf/Tch/NOT、急躁反问抱怨，末尾尴尬求保密
- **观察行为**：要求别看、质疑为何有录像还要复述
- **关系、版本和证据边界**：Gaoru与Yogo不同人；身体反应不证明同意；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`Uc6e84296569f6f8e3c78` / `O3231008cf80dfb759b39` · `datav/dictionary.json#ui.data.m_AgentM01` · [位置](<../../../catalog/occurrences.jsonl#L6594>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V0f24b5461097be406a72` / `O5f158b2446e5c80be303` · `vsn/m_AgentM01/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7975>) · [原始来源](<../../../sources/blobs/b7aecc4ecf9693e537fb0601c39c5b2a602646de55fa6064bedeb2206242c7c5.vsn#L5>)
- 证据：`Vb4ec22bec132940cb9e2` / `O1e031bb0bd573da26346` · `vsn/m_AgentM01/script.vsn:26` · [位置](<../../../catalog/occurrences.jsonl#L7987>) · [原始来源](<../../../sources/blobs/b7aecc4ecf9693e537fb0601c39c5b2a602646de55fa6064bedeb2206242c7c5.vsn#L26>)
- 证据：`V3c1e7614abb6b10eb783` / `O1ad70893194c118ee22f` · `vsn/m_AgentM01/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L8004>) · [原始来源](<../../../sources/blobs/b7aecc4ecf9693e537fb0601c39c5b2a602646de55fa6064bedeb2206242c7c5.vsn#L58>)

#### GEPARD · `m_AgentM02`
- **角色功能/身份依据**：Top探员失控自夸；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：声称即将自己逃出、屈从全是策略；后文不断自圆其说
- **口吻/声线**：yours truly/ahem/professionals/rookie假正经长句、居高临下、尾句泄气
- **观察行为**：想控制资料审查、否认不利记录
- **关系、版本和证据边界**：Top双关非客观军衔；不替自夸圆谎；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U7ae1ce507d3a3c948886` / `O7d8e78d85b71970596b5` · `datav/dictionary.json#ui.data.m_AgentM02` · [位置](<../../../catalog/occurrences.jsonl#L6596>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V97a88a7deff94680212d` / `Od5d500b7140ed29eca3a` · `vsn/m_AgentM02/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8011>) · [原始来源](<../../../sources/blobs/48f30c9acb970e1fe9e6840b49c094c9ef34896787dfc0b29a8b89ca4ddc71dc.vsn#L5>)
- 证据：`V3f558723e4ea3a6216c8` / `O599ffad80eac19092bcb` · `vsn/m_AgentM02/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L8021>) · [原始来源](<../../../sources/blobs/48f30c9acb970e1fe9e6840b49c094c9ef34896787dfc0b29a8b89ca4ddc71dc.vsn#L24>)
- 证据：`V2086c23a4e5e441017da` / `Oe1556d9ba4bb7a5eb26c` · `vsn/m_AgentM02/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L8043>) · [原始来源](<../../../sources/blobs/48f30c9acb970e1fe9e6840b49c094c9ef34896787dfc0b29a8b89ca4ddc71dc.vsn#L58>)

#### TRUVELO · `m_AgentM03`
- **角色功能/身份依据**：Wyvern遭遇报告；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自夸Top、否认享受，末尾承认没趁无锁逃走
- **口吻/声线**：like/yeah sure/right、WHAM BAM、straight/gay冷笑话，急于解释青年腔
- **观察行为**：抱怨需要救援，同时许可回看日志
- **关系、版本和证据边界**：UI HYENA不是每句加笑声的授权；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U0a97efb8eff430ec3e0f` / `Oe0c4ae28fff6e806f946` · `datav/dictionary.json#ui.data.m_AgentM03` · [位置](<../../../catalog/occurrences.jsonl#L6598>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vdfa829dd6183d87bef04` / `Oe62441cf3bc1a3517759` · `vsn/m_AgentM03/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8056>) · [原始来源](<../../../sources/blobs/ba9584455433b4a24001ce0545dd4d5c3f661ede76d8ec75f8e28b729c463ceb.vsn#L5>)
- 证据：`Vb9372470ff885230c15c` / `O4916c0076137ccecb3e5` · `vsn/m_AgentM03/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L8066>) · [原始来源](<../../../sources/blobs/ba9584455433b4a24001ce0545dd4d5c3f661ede76d8ec75f8e28b729c463ceb.vsn#L24>)
- 证据：`V17c94f0f187f131c3ad3` / `Oc3fce6613ea6f96e359a` · `vsn/m_AgentM03/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L8085>) · [原始来源](<../../../sources/blobs/ba9584455433b4a24001ce0545dd4d5c3f661ede76d8ec75f8e28b729c463ceb.vsn#L58>)

#### VULCAN · `m_AgentM04`
- **角色功能/身份依据**：矿区地图与精神影响；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自夸体格/克制，却记忆断续、渴望good boy
- **口吻/声线**：lad/nosirree/gentleman/naught/whatfor老派自尊，纠正口误
- **观察行为**：要忽略记录，仍说自己做过地图
- **关系、版本和证据边界**：UI little fennec和prodigiously buff并列，不按自夸抹反讽；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U07683bc37cb3f1d66ce0` / `O04c2b0a120618e947c71` · `datav/dictionary.json#ui.data.m_AgentM04` · [位置](<../../../catalog/occurrences.jsonl#L6600>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V3bf6f0e9716f51f785e0` / `O8c9180a5c85ca65f5d39` · `vsn/m_AgentM04/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8096>) · [原始来源](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L5>)
- 证据：`Vc6f67f4a14eee1b15401` / `Oc057c47b03ed955b0c4a` · `vsn/m_AgentM04/script.vsn:87` · [位置](<../../../catalog/occurrences.jsonl#L8142>) · [原始来源](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L87>)
- 证据：`Vd2e798be570710ea11c3` / `Oc827b8fa53847e6d87e9` · `vsn/m_AgentM04/script.vsn:56` · [位置](<../../../catalog/occurrences.jsonl#L8126>) · [原始来源](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L56>)

#### HENSCHEL · `m_AgentM05`
- **角色功能/身份依据**：Bullfrog与海盗回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：反复自称Top，否认快感与档案，末尾却试探bad kitty
- **口吻/声线**：结巴、purropurrly猫谐音、删记录请求，公务语切羞涩
- **观察行为**：感谢后努力返回汇报，结尾走神
- **关系、版本和证据边界**：Henschel在Karbine报告被提及是另一人视角，不当独立镜头；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U1389c5be6e2c209e0fa8` / `O9904ffede804413433fa` · `datav/dictionary.json#ui.data.m_AgentM05` · [位置](<../../../catalog/occurrences.jsonl#L6602>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vcebf9a913991021fca3c` / `Of4bdd967aef26714cfd0` · `vsn/m_AgentM05/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8146>) · [原始来源](<../../../sources/blobs/d4681e1fc650758725a53d04afdd36f6464c70a09c081acd17a2be45faee2707.vsn#L5>)
- 证据：`V446300ca8f8ad80b6612` / `Oa1a3553e65604217f857` · `vsn/m_AgentM05/script.vsn:84` · [位置](<../../../catalog/occurrences.jsonl#L8192>) · [原始来源](<../../../sources/blobs/d4681e1fc650758725a53d04afdd36f6464c70a09c081acd17a2be45faee2707.vsn#L84>)
- 证据：`Vae009303885fa37782f7` / `O9a66e80cd6785089d192` · `vsn/m_AgentM05/script.vsn:56` · [位置](<../../../catalog/occurrences.jsonl#L8176>) · [原始来源](<../../../sources/blobs/d4681e1fc650758725a53d04afdd36f6464c70a09c081acd17a2be45faee2707.vsn#L56>)

#### FRANCHI · `m_AgentM06`
- **角色功能/身份依据**：精灵营地受困报告；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：Red Pandarian战姿令精灵投降/自己胜者是自夸，结尾承认是假降
- **口吻/声线**：courtesies/merciful/generous端着英雄自尊，对newbie施惠，夹Eep
- **观察行为**：接受照顾后被留下，仍把被救说成让新人立功
- **关系、版本和证据边界**：不把夸胜写成真胜，也不凭Red Pandarians造政体；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`Ufbce775d5bf5dc024b34` / `O2e0806e42ac0081c5680` · `datav/dictionary.json#ui.data.m_AgentM06` · [位置](<../../../catalog/occurrences.jsonl#L6604>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vb71e8069afc14c6631fd` / `O98617ad11017288497ab` · `vsn/m_AgentM06/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8197>) · [原始来源](<../../../sources/blobs/833c58cddb68da4b667eca18703f311ec692cad172b03950ff8aae8e42667780.vsn#L5>)
- 证据：`V01032757e5538658c518` / `O48492f863b6761856fd6` · `vsn/m_AgentM06/script.vsn:88` · [位置](<../../../catalog/occurrences.jsonl#L8246>) · [原始来源](<../../../sources/blobs/833c58cddb68da4b667eca18703f311ec692cad172b03950ff8aae8e42667780.vsn#L88>)
- 证据：`Ve0da254c0f969ca03abc` / `Oabe34b6226eecd67c458` · `vsn/m_AgentM06/script.vsn:59` · [位置](<../../../catalog/occurrences.jsonl#L8229>) · [原始来源](<../../../sources/blobs/833c58cddb68da4b667eca18703f311ec692cad172b03950ff8aae8e42667780.vsn#L59>)

#### CHAUCHAT · `m_AgentM07`
- **角色功能/身份依据**：高温矿区犬科体验；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：称偏安静侦察，怕直接战斗；体验后想补数据
- **口吻/声线**：明显结巴、道歉hassle、pounding自纠，谨慎转热切
- **观察行为**：强调鞋幸存、成功俯冲；结尾试探并挽留玩家
- **关系、版本和证据边界**：UI caracal/pusillanimous是评价，不每句弱化或删其反击；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U6e1d01b6865b79234118` / `O06cd6c3391c60ccd77ee` · `datav/dictionary.json#ui.data.m_AgentM07` · [位置](<../../../catalog/occurrences.jsonl#L6606>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Ve0f622b76a2bf392cb75` / `Occ46d1d379bfa5dbeb03` · `vsn/m_AgentM07/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8250>) · [原始来源](<../../../sources/blobs/dd57c72ce5bbbfbcc3628d5292e1b164f821e94fee80064c75fa09a38dae96ae.vsn#L5>)
- 证据：`V01fe56a1f12e5ac7856d` / `O649561bbad5e4eb6944e` · `vsn/m_AgentM07/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L8260>) · [原始来源](<../../../sources/blobs/dd57c72ce5bbbfbcc3628d5292e1b164f821e94fee80064c75fa09a38dae96ae.vsn#L24>)
- 证据：`V989a3f29b50c6b31194f` / `O702db1d00fb11b2e9dd3` · `vsn/m_AgentM07/script.vsn:59` · [位置](<../../../catalog/occurrences.jsonl#L8280>) · [原始来源](<../../../sources/blobs/dd57c72ce5bbbfbcc3628d5292e1b164f821e94fee80064c75fa09a38dae96ae.vsn#L59>)

#### KARBINE · `m_AgentM08`
- **角色功能/身份依据**：海盗与宝石回顾；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：自信outfox，宝石令记忆模糊，不足定机制
- **口吻/声线**：Howdy thar/ta/ya、民间叙述节奏、轻松自嘲；不套现实地域腔
- **观察行为**：谈Henschel后求多样采集奖金，主动掌控后再受制
- **关系、版本和证据边界**：Karbine与Vickers不同人，狐狸无全族统一口癖；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U8cba0229003db7177ff3` / `Oe18c398d648ede8b3767` · `datav/dictionary.json#ui.data.m_AgentM08` · [位置](<../../../catalog/occurrences.jsonl#L6608>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V99eeb2321b69bbe2c45b` / `Oea5400e1c1deac637af1` · `vsn/m_AgentM08/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8291>) · [原始来源](<../../../sources/blobs/da613c182df43fac842cbb0498f928404f02964b000e0765aad941f721a7cecd.vsn#L5>)
- 证据：`Vd178960e2c222c7e9589` / `Oef4cfb443105d934680d` · `vsn/m_AgentM08/script.vsn:88` · [位置](<../../../catalog/occurrences.jsonl#L8341>) · [原始来源](<../../../sources/blobs/da613c182df43fac842cbb0498f928404f02964b000e0765aad941f721a7cecd.vsn#L88>)
- 证据：`Vc1f650ec2890aaf08f9a` / `Od474170b5d2da91656cc` · `vsn/m_AgentM08/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L8323>) · [原始来源](<../../../sources/blobs/da613c182df43fac842cbb0498f928404f02964b000e0765aad941f721a7cecd.vsn#L58>)

#### PANCOR · `m_AgentM0B`
- **角色功能/身份依据**：兔探员Pancor汇报；原作ui.data标题与同名VSN相连，narrator是容器标签非全知说话者。
- **自述与客观层级**：猜披袍犬捕获者性别与蓝光武器真伪，记忆模糊
- **口吻/声线**：Hee/hehee、轻快直率、插话解释，不是高傲Top腔
- **观察行为**：谢救援，惦记Swiper再约一次，直叫玩家Yiffai
- **关系、版本和证据边界**：总部top agent赞语与其自述分层，气味性别只是猜测；仅本报告语气，不足独立证明跨情境人格。 当前catalog生效PAK 男线；同号异性别报告不合并同人；高（标题与文本），性格概括仅本场。
- 证据：`U9aecda89e6fffab2648e` / `Ocd4ef5e792c51e2e7ebe` · `datav/dictionary.json#ui.data.m_AgentM0B` · [位置](<../../../catalog/occurrences.jsonl#L6610>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V1fe35184caac2674b681` / `O18a10500d7fc5bcf7c4e` · `vsn/m_AgentM0B/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8345>) · [原始来源](<../../../sources/blobs/6948ad4101a6f0b8e977e2f3d249108b98554c323932a4b37789b81970298a70.vsn#L5>)
- 证据：`V2ab446301b35649036f1` / `Oe1339a10cc042e0a2705` · `vsn/m_AgentM0B/script.vsn:27` · [位置](<../../../catalog/occurrences.jsonl#L8358>) · [原始来源](<../../../sources/blobs/6948ad4101a6f0b8e977e2f3d249108b98554c323932a4b37789b81970298a70.vsn#L27>)
- 证据：`V09ee2b3411a47089dd3b` / `Oe4c23bfcdddb099447d1` · `vsn/m_AgentM0B/script.vsn:51` · [位置](<../../../catalog/occurrences.jsonl#L8370>) · [原始来源](<../../../sources/blobs/6948ad4101a6f0b8e977e2f3d249108b98554c323932a4b37789b81970298a70.vsn#L51>)

### Fenfen档案

#### RATS · `f_AgentFZ1`
- **角色功能/身份依据**：文明与Traeh起源；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uc4e0849ce1f8224f6ceb` / `Ob87f206e65f7a964cc72` · `datav/dictionary.json#ui.data.f_AgentFZ1` · [位置](<../../../catalog/occurrences.jsonl#L6555>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V340e5be183a58363ed99` / `O591263fb1aaeb32d2640` · `vsn/f_AgentFZ1/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L7174>) · [原始来源](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L5>)
- 证据：`V9b56bf52ffea1f6f3102` / `Oe22ae03425eda1b2c998` · `vsn/f_AgentFZ1/script.vsn:17` · [位置](<../../../catalog/occurrences.jsonl#L7179>) · [原始来源](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L17>)
- 证据：`V8c793751eb4c59dd23ed` / `Oc85892a707445187e050` · `vsn/f_AgentFZ1/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L7184>) · [原始来源](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L25>)

#### ELGNAIRT · `f_AgentFZ2`
- **角色功能/身份依据**：征服奴役；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U8ccb6e5fb63a9f9fafc9` / `O6ed8c51a9a8dfc0fd088` · `datav/dictionary.json#ui.data.f_AgentFZ2` · [位置](<../../../catalog/occurrences.jsonl#L6557>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V4dda0eff99679a5b22e4` / `O64c282165c424cfd7ad6` · `vsn/f_AgentFZ2/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L7204>) · [原始来源](<../../../sources/blobs/b5b3dd8bf2f495f52d1acb58265ff7846919315893d76c989b05f56592ae192a.vsn#L11>)
- 证据：`V7d2fd78ccd57feaf75fa` / `O6f28a94c58171b7bfbb9` · `vsn/f_AgentFZ2/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L7208>) · [原始来源](<../../../sources/blobs/b5b3dd8bf2f495f52d1acb58265ff7846919315893d76c989b05f56592ae192a.vsn#L18>)
- 证据：`Ve6a84f40793b574e98b5` / `Oe3b3bf4b7d7e75f299a2` · `vsn/f_AgentFZ2/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L7212>) · [原始来源](<../../../sources/blobs/b5b3dd8bf2f495f52d1acb58265ff7846919315893d76c989b05f56592ae192a.vsn#L25>)

#### SEVAW · `f_AgentFZ3`
- **角色功能/身份依据**：反抗与能力军用化；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U92cef30530c466844d39` / `O3626940b44bff87c3433` · `datav/dictionary.json#ui.data.f_AgentFZ3` · [位置](<../../../catalog/occurrences.jsonl#L6559>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vc435b13cff17293a78b5` / `O22dc7561e3ae3310e13a` · `vsn/f_AgentFZ3/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L7226>) · [原始来源](<../../../sources/blobs/f1600c23d547d7d9923c63ea00b45e453633e89c153c29761382365fb80f549c.vsn#L11>)
- 证据：`Vdac8a66d8d9f91da79de` / `Oafbc9c849c84d2de1102` · `vsn/f_AgentFZ3/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L7230>) · [原始来源](<../../../sources/blobs/f1600c23d547d7d9923c63ea00b45e453633e89c153c29761382365fb80f549c.vsn#L18>)
- 证据：`Vef93c367f4819a3a9092` / `O5d2d560c47ac750b3455` · `vsn/f_AgentFZ3/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L7233>) · [原始来源](<../../../sources/blobs/f1600c23d547d7d9923c63ea00b45e453633e89c153c29761382365fb80f549c.vsn#L24>)

#### ELCRIC · `f_AgentFZ4`
- **角色功能/身份依据**：水晶封印；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U9b47c169e84bc37001c5` / `Oed673d8eb7c745fed5c6` · `datav/dictionary.json#ui.data.f_AgentFZ4` · [位置](<../../../catalog/occurrences.jsonl#L6561>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vd1a1c68b557da460653b` / `Ofbcc37bb5456f4661f5d` · `vsn/f_AgentFZ4/script.vsn:12` · [位置](<../../../catalog/occurrences.jsonl#L7245>) · [原始来源](<../../../sources/blobs/7b0456d0e169ff913218d0d99a74d837fec61d0f58a223e1c02c052fa0104eaf.vsn#L12>)
- 证据：`Ve9a2b6e1204eddd96634` / `O13da2c1abdb86a47b80e` · `vsn/f_AgentFZ4/script.vsn:19` · [位置](<../../../catalog/occurrences.jsonl#L7249>) · [原始来源](<../../../sources/blobs/7b0456d0e169ff913218d0d99a74d837fec61d0f58a223e1c02c052fa0104eaf.vsn#L19>)
- 证据：`V64ba547d389b24f6ab93` / `Od3b7331d50964cb9b2d1` · `vsn/f_AgentFZ4/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L7252>) · [原始来源](<../../../sources/blobs/7b0456d0e169ff913218d0d99a74d837fec61d0f58a223e1c02c052fa0104eaf.vsn#L25>)

#### SSORC · `f_AgentFZ5`
- **角色功能/身份依据**：访客接触受控；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uf1fb2c377a8094beb2b5` / `Of63106e39a255de6062c` · `datav/dictionary.json#ui.data.f_AgentFZ5` · [位置](<../../../catalog/occurrences.jsonl#L6563>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V335e9be4b47622a55c98` / `Oe3f4e96c21e036dba02c` · `vsn/f_AgentFZ5/script.vsn:12` · [位置](<../../../catalog/occurrences.jsonl#L7268>) · [原始来源](<../../../sources/blobs/68425b9e3802775934fa8f97bc9d485c5b169ae49d39749589db0c30eb5b79ec.vsn#L12>)
- 证据：`V1d4c3283630959a4122a` / `Oaf650d8d4960d3312844` · `vsn/f_AgentFZ5/script.vsn:19` · [位置](<../../../catalog/occurrences.jsonl#L7272>) · [原始来源](<../../../sources/blobs/68425b9e3802775934fa8f97bc9d485c5b169ae49d39749589db0c30eb5b79ec.vsn#L19>)
- 证据：`V03951cad66995422d1ca` / `O67dc68ea520b452279e3` · `vsn/f_AgentFZ5/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L7275>) · [原始来源](<../../../sources/blobs/68425b9e3802775934fa8f97bc9d485c5b169ae49d39749589db0c30eb5b79ec.vsn#L25>)

#### ERAUQS · `f_AgentFZ6`
- **角色功能/身份依据**：捕议员与换宿主危机；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK f路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uc781902974216b5a5ce5` / `O9cc97a9858c052d49f9b` · `datav/dictionary.json#ui.data.f_AgentFZ6` · [位置](<../../../catalog/occurrences.jsonl#L6565>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Va0221f64944d5ae004ac` / `O988c4690d9c2202c7c26` · `vsn/f_AgentFZ6/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L7287>) · [原始来源](<../../../sources/blobs/0181dc2867c742fb5d24f81ec0e1bac3f5a6524f58843fda9bb23ff0e73d098b.vsn#L11>)
- 证据：`Ve92c65d667fc90054ed6` / `O7642902a928c559e65d3` · `vsn/f_AgentFZ6/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L7291>) · [原始来源](<../../../sources/blobs/0181dc2867c742fb5d24f81ec0e1bac3f5a6524f58843fda9bb23ff0e73d098b.vsn#L18>)
- 证据：`Vc911c46ef8708077f727` / `O550fb218ae1c09d8a447` · `vsn/f_AgentFZ6/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L7294>) · [原始来源](<../../../sources/blobs/0181dc2867c742fb5d24f81ec0e1bac3f5a6524f58843fda9bb23ff0e73d098b.vsn#L24>)

#### RATS · `m_AgentMZ1`
- **角色功能/身份依据**：文明与Traeh起源；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uc4e0849ce1f8224f6ceb` / `Oa5c3addb423f13c275f5` · `datav/dictionary.json#ui.data.m_AgentMZ1` · [位置](<../../../catalog/occurrences.jsonl#L6612>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V10c9c7d86e3f7fd739c8` / `Ob3561ecd5daca9db50ca` · `vsn/m_AgentMZ1/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8371>) · [原始来源](<../../../sources/blobs/246575c9a22bd285f6c2d8ad2721ede9e17a074482435ff91dff16661f4148c9.vsn#L5>)
- 证据：`Vdaccdf5e92d39f98da11` / `O3f7c00f2c42b39b682a6` · `vsn/m_AgentMZ1/script.vsn:17` · [位置](<../../../catalog/occurrences.jsonl#L8376>) · [原始来源](<../../../sources/blobs/246575c9a22bd285f6c2d8ad2721ede9e17a074482435ff91dff16661f4148c9.vsn#L17>)
- 证据：`Vc531acf26f84e4f3eabf` / `O965e5b14da113211f062` · `vsn/m_AgentMZ1/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L8381>) · [原始来源](<../../../sources/blobs/246575c9a22bd285f6c2d8ad2721ede9e17a074482435ff91dff16661f4148c9.vsn#L25>)

#### ELGNAIRT · `m_AgentMZ2`
- **角色功能/身份依据**：征服奴役；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U8ccb6e5fb63a9f9fafc9` / `O4b4652d942d78105ad7d` · `datav/dictionary.json#ui.data.m_AgentMZ2` · [位置](<../../../catalog/occurrences.jsonl#L6614>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vac59c6296c7322f24301` / `O125b21788705de67edee` · `vsn/m_AgentMZ2/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L8401>) · [原始来源](<../../../sources/blobs/75cb4918fae0ff30ed65264911e52dc65b8c0d5b0f1240757ee42f48d9f6520d.vsn#L11>)
- 证据：`V563e38303100480e3f4d` / `O8024ff2116a080221c33` · `vsn/m_AgentMZ2/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L8405>) · [原始来源](<../../../sources/blobs/75cb4918fae0ff30ed65264911e52dc65b8c0d5b0f1240757ee42f48d9f6520d.vsn#L18>)
- 证据：`V60e999df7b7682a8d097` / `O15a3ed5a6461e634581a` · `vsn/m_AgentMZ2/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L8409>) · [原始来源](<../../../sources/blobs/75cb4918fae0ff30ed65264911e52dc65b8c0d5b0f1240757ee42f48d9f6520d.vsn#L25>)

#### SEVAW · `m_AgentMZ3`
- **角色功能/身份依据**：反抗与能力军用化；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U92cef30530c466844d39` / `Oae53fdaa7f117992c230` · `datav/dictionary.json#ui.data.m_AgentMZ3` · [位置](<../../../catalog/occurrences.jsonl#L6616>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V833dff7405d20cd073e0` / `O13a0923237a1a26ba975` · `vsn/m_AgentMZ3/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L8423>) · [原始来源](<../../../sources/blobs/8172d0ef45a3cbf79d3db7431e19f48266e5438ace8f7cb16f924f18e2dcb1d5.vsn#L11>)
- 证据：`Va8ea95822759dbc017ec` / `O6e5722108c3d24c2bef3` · `vsn/m_AgentMZ3/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L8427>) · [原始来源](<../../../sources/blobs/8172d0ef45a3cbf79d3db7431e19f48266e5438ace8f7cb16f924f18e2dcb1d5.vsn#L18>)
- 证据：`V670601413d75a3f98306` / `O48849d0845701f2fb9d3` · `vsn/m_AgentMZ3/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L8430>) · [原始来源](<../../../sources/blobs/8172d0ef45a3cbf79d3db7431e19f48266e5438ace8f7cb16f924f18e2dcb1d5.vsn#L24>)

#### ELCRIC · `m_AgentMZ4`
- **角色功能/身份依据**：水晶封印；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`U9b47c169e84bc37001c5` / `O22344a2b632defc64d8d` · `datav/dictionary.json#ui.data.m_AgentMZ4` · [位置](<../../../catalog/occurrences.jsonl#L6618>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V00289b99919500040727` / `Oedc037f43f7bf1af55b7` · `vsn/m_AgentMZ4/script.vsn:12` · [位置](<../../../catalog/occurrences.jsonl#L8442>) · [原始来源](<../../../sources/blobs/81e744bbd1079cd81576598261d491d983bb629142de1b93272d7da146503d6c.vsn#L12>)
- 证据：`Vafeb4673d65b56c12bce` / `O1ac486de0419963e7228` · `vsn/m_AgentMZ4/script.vsn:19` · [位置](<../../../catalog/occurrences.jsonl#L8446>) · [原始来源](<../../../sources/blobs/81e744bbd1079cd81576598261d491d983bb629142de1b93272d7da146503d6c.vsn#L19>)
- 证据：`Vb34814caefa31d465ab5` / `Ofa13323ac3b10731eb9a` · `vsn/m_AgentMZ4/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L8449>) · [原始来源](<../../../sources/blobs/81e744bbd1079cd81576598261d491d983bb629142de1b93272d7da146503d6c.vsn#L25>)

#### SSORC · `m_AgentMZ5`
- **角色功能/身份依据**：访客接触受控；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uf1fb2c377a8094beb2b5` / `Oa81833fde0eae0efae7e` · `datav/dictionary.json#ui.data.m_AgentMZ5` · [位置](<../../../catalog/occurrences.jsonl#L6620>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vb75b37103e7f168d17c8` / `O4056e2e0fffe6f8836bd` · `vsn/m_AgentMZ5/script.vsn:12` · [位置](<../../../catalog/occurrences.jsonl#L8465>) · [原始来源](<../../../sources/blobs/91e0e9d6751dc80f0a46e8702b100a3e35faba947ab219d5a9f56cdbef421aa4.vsn#L12>)
- 证据：`V6c5593dc7980f82e58c3` / `O0d4b69ffb49b865152e8` · `vsn/m_AgentMZ5/script.vsn:19` · [位置](<../../../catalog/occurrences.jsonl#L8469>) · [原始来源](<../../../sources/blobs/91e0e9d6751dc80f0a46e8702b100a3e35faba947ab219d5a9f56cdbef421aa4.vsn#L19>)
- 证据：`V090bdd51d76c7cb0c56e` / `Oc1f5ad2ac35cc0641dd8` · `vsn/m_AgentMZ5/script.vsn:25` · [位置](<../../../catalog/occurrences.jsonl#L8472>) · [原始来源](<../../../sources/blobs/91e0e9d6751dc80f0a46e8702b100a3e35faba947ab219d5a9f56cdbef421aa4.vsn#L25>)

#### ERAUQS · `m_AgentMZ6`
- **角色功能/身份依据**：捕议员与换宿主危机；原作ui.data标题；不凭图像/倒写字形确定六个具体个体。
- **自述与客观层级**：we/us为族群/议会自述；I can see为主角插话，不归讲述者。
- **口吻/声线**：庄重引导、hero称呼、集体we/us、遗憾反问与未来二选一；自然仪式感不强套汝/吾。Z2–5不足定各人独特口癖。
- **观察行为**：Z1/Z6以手触手/静心观看框架引导；其余主要历史叙述。
- **关系、版本和证据边界**：m/f同标题不证明两名同名个体；原prefix lang(Fox)不可因narrator元数据改全知。标题到场景对象仍需核证。 当前PAK m路线；不假定JAR同量同文；高（档案标题/文本）；个体人格不足。
- 证据：`Uc781902974216b5a5ce5` / `Od3f90ed1b3ae47cc2f1b` · `datav/dictionary.json#ui.data.m_AgentMZ6` · [位置](<../../../catalog/occurrences.jsonl#L6622>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vd66dadb24deb49f367d1` / `O25866ba6b7947416d031` · `vsn/m_AgentMZ6/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L8484>) · [原始来源](<../../../sources/blobs/69252b40147ab7a24ba36a4736d352a631e36a7894f7da3ab35434419711e82d.vsn#L11>)
- 证据：`Vdd2d299cd752d5cdcb4f` / `Oa180cc6bb1333adf93af` · `vsn/m_AgentMZ6/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L8488>) · [原始来源](<../../../sources/blobs/69252b40147ab7a24ba36a4736d352a631e36a7894f7da3ab35434419711e82d.vsn#L18>)
- 证据：`Vbc52cbfe4f923d23d51e` / `Oc47a19e6de8996be80ce` · `vsn/m_AgentMZ6/script.vsn:24` · [位置](<../../../catalog/occurrences.jsonl#L8491>) · [原始来源](<../../../sources/blobs/69252b40147ab7a24ba36a4736d352a631e36a7894f7da3ab35434419711e82d.vsn#L24>)

### 其他角色／叙事声部

#### Bigbold（首战/V2个体与物种分开） · `boss-bigbold`
- **角色功能/身份依据**：追装备主线与追击逃生；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：醒来逃走/撞门致塌顶为场景；主角说其在装睡/享受是主角猜测。图鉴另次是不同个体。
- **口吻/声线**：本次VSN未见其可辨人语台词，不造憨厚、口吃、海盗口音。
- **观察行为**：战后未醒，醒后逃离；深层图鉴个体更强。
- **关系、版本和证据边界**：不能把物种全部当同一首领；主角口含东西的ashleep等不是Bigbold口音。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：Bigbold场景第一人称/含混发音属于玩家；本条动作只据场景/旁白。
- 证据：`V0e446b853004d8778d3f` / `O3049b54282026314f729` · `vsn/m_ClassicBigbold/script.vsn:204` · [位置](<../../../catalog/occurrences.jsonl#L8557>) · [原始来源](<../../../sources/blobs/9be0235b421ca71a01278d5959459ac8489ec48684e86f1ff645f3ae8d19025f.vsn#L204>)
- 证据：`Dc9841be1615e29d5d3f9` / `O408ae5e532bc15529cfa` · `datadf/all.ds:2928` · [位置](<../../../catalog/occurrences.jsonl#L1308>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2928>)
- 证据：`D6fbcacad9713522c04fa` / `Od87b7b5fc1919f998e3a` · `datadm/all.ds:2985` · [位置](<../../../catalog/occurrences.jsonl#L4263>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2985>)

#### Redbull · `boss-redbull`
- **角色功能/身份依据**：矿区古老存在、反制并给鞋；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：卡片称古老矿区居民、期盼独角兽回归；角色以自己领域自居。
- **口吻/声线**：Heh重复、居高临下却从容的反问、复述玩家关键词harm（男）/power（女）后教训；不是暴躁吼叫或统一古语。
- **观察行为**：能突然绕到主角身后，仍让主角拿鞋离开，自己退深矿。
- **关系、版本和证据边界**：鞋来自另一战士说法是其话；单场不足写所有情境残酷或仁慈；unicorn情结按卡片而非其直接台词。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：5–9、20–22、43–45为Redbull；13–19与38–39为玩家；49–50场景叙述。
- 证据：`Uc24d38bf8121c2b6207c` / `Ob78d7d46254d6d826a1b` · `datav/dictionary.json#ui.card.CosmoCardRedbull.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6500>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vf4717986988628db1fc8` / `O4c3175d4bd789d7c4e01` · `vsn/m_ClassicBossRedbull/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8641>) · [原始来源](<../../../sources/blobs/39b33e833a253f07235cd336ef168863adfc749f94082c79d8c958a614d51e98.vsn#L5>)
- 证据：`V618c9d2b31f913bd17ef` / `O5eca4e4e22618b3f661a` · `vsn/m_ClassicBossRedbull/script.vsn:21` · [位置](<../../../catalog/occurrences.jsonl#L8651>) · [原始来源](<../../../sources/blobs/39b33e833a253f07235cd336ef168863adfc749f94082c79d8c958a614d51e98.vsn#L21>)
- 证据：`V039d12864539ff38e40f` / `O0d3702a8344a50680c7e` · `vsn/m_ClassicBossRedbull/script.vsn:50` · [位置](<../../../catalog/occurrences.jsonl#L8660>) · [原始来源](<../../../sources/blobs/39b33e833a253f07235cd336ef168863adfc749f94082c79d8c958a614d51e98.vsn#L50>)

#### Enelye · `boss-enelye`
- **角色功能/身份依据**：精灵High Lady/战后奖励；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：自称不朽、年长；卡片以High Lady/魔法才能与允许年轻精灵练战描述。
- **口吻/声线**：正式赞赏、my young sir/young lady、commend/respectable、停顿reward；温雅而掌控，不自动改本宫或女王。
- **观察行为**：赞赏战斗并给主角穿裙；女主自己穿诉求/男主羞抗应分线。
- **关系、版本和证据边界**：长生/魔法来自自述与卡片，不把所有精灵都不朽；失败线主角称my queen不等于Traeh同人。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：11–19为Enelye；5–7和20以后玩家抗议/回应，不归Enelye口气。
- 证据：`U0f43c6d6513201ebb813` / `O33d205e8c3d2c6695fbb` · `datav/dictionary.json#ui.card.CosmoCardEnelye.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6488>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V99330da3446c694d80fb` / `O85ea1ba930c89658e5a6` · `vsn/m_ClassicEnelye/script.vsn:11` · [位置](<../../../catalog/occurrences.jsonl#L8664>) · [原始来源](<../../../sources/blobs/28b549c22b50eb578e4211521e52e85bc89bf091b75c82e6d52ae854c1f477ab.vsn#L11>)
- 证据：`V7fd1501f2e8794fc6404` / `Od7145b4ad2f5e7b27c59` · `vsn/f_ClassicEnelye/script.vsn:17` · [位置](<../../../catalog/occurrences.jsonl#L7478>) · [原始来源](<../../../sources/blobs/9178414c11414e1275b225caf0f21f34637d863d57c620822f1bd97cd77a2a42.vsn#L17>)
- 证据：`V0e7e430fb60e93baeb83` / `O29333bb5bb0e75b0c36f` · `vsn/f_ClassicEnelye/script.vsn:30` · [位置](<../../../catalog/occurrences.jsonl#L7486>) · [原始来源](<../../../sources/blobs/9178414c11414e1275b225caf0f21f34637d863d57c620822f1bd97cd77a2a42.vsn#L30>)

#### Pigobin · `boss-pigobin`
- **角色功能/身份依据**：无法常规取胜的古语人物、赠语言项链；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：自称古老力量/慷慨主人；卡片称曾统一Omegobin帝国、被传说英雄封印。
- **口吻/声线**：thou/thee/thine/pray/hast等古语、fairest knight带居高临下讥诮，结尾guttural laugh。中文适度古雅而非全作古风。
- **观察行为**：给项链、把主角失礼反将一军，随后消失。
- **关系、版本和证据边界**：封印者未具名不可代填Traeh；不能把Gobin/Omegobin/Pigobin当同一族内一人；古语不影响科学词。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：5–7、16–17、26–33为Pigobin；11–12、21–22为玩家；37–38场景叙述。
- 证据：`U02099386cc030ff040ad` / `O5aad05b99f5851139777` · `datav/dictionary.json#ui.card.CosmoCardPigobin.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6497>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Va87e9b3dbf6b755ea053` / `Oc5a2e346c20c75d21319` · `vsn/m_ClassicPigobinV3/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8675>) · [原始来源](<../../../sources/blobs/507a1034c21fb60d63b45055c7a1fd5e31593d8d4ecbacc398bc4b73dfe01763.vsn#L5>)
- 证据：`V57f92d44aa5e64b06af8` / `O46c5a1d8ea1bc27b4b04` · `vsn/m_ClassicPigobinV3/script.vsn:30` · [位置](<../../../catalog/occurrences.jsonl#L8685>) · [原始来源](<../../../sources/blobs/507a1034c21fb60d63b45055c7a1fd5e31593d8d4ecbacc398bc4b73dfe01763.vsn#L30>)
- 证据：`V574a507a7af1ddf40041` / `O07fa4e79e39c930c0770` · `vsn/m_ClassicPigobinV3/script.vsn:38` · [位置](<../../../catalog/occurrences.jsonl#L8690>) · [原始来源](<../../../sources/blobs/507a1034c21fb60d63b45055c7a1fd5e31593d8d4ecbacc398bc4b73dfe01763.vsn#L38>)

#### Werehund（父亲） · `boss-werehund`
- **角色功能/身份依据**：反制玩家并赋变形能力，父子尾声认定英雄；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：自述测试玩家品格/父亲经验；卡片说本无天然Esper亲和，因Esper妻得变形；能力与生理突变相关仍may。
- **口吻/声线**：方括号精神交流中my young friend/my dear、please/for now、礼貌而有支配力；父亲回答儿子简短安抚。
- **观察行为**：反转表面败局、变形教学；肯定chosen one但推迟幼子请求。
- **关系、版本和证据边界**：chosen one是父亲判断；卡片与自述来源分层，非从所有were类名猜狼人族；不把玩家呻吟归父亲。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：括号123–148为父亲；171/178–179幼子；172/176–177/184父亲；其余多玩家。
- 证据：`U7d945ba3bcece2eb4c10` / `O8ff2c0ba7b0d769af136` · `datav/dictionary.json#ui.card.CosmoCardWerehund.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6512>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vaf7dd57056720eea492a` / `Oa1a5a2668f3f2ff2e746` · `vsn/m_ClassicWerehund/script.vsn:123` · [位置](<../../../catalog/occurrences.jsonl#L8758>) · [原始来源](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L123>)
- 证据：`V05508eabd001ef94b6cc` / `Of16666f0a7e1ce7d55f6` · `vsn/m_ClassicWerehund/script.vsn:146` · [位置](<../../../catalog/occurrences.jsonl#L8768>) · [原始来源](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L146>)
- 证据：`Vd3c21ab4ac8140eb6d64` / `Of843d7458e52815a2868` · `vsn/m_ClassicWerehund/script.vsn:184` · [位置](<../../../catalog/occurrences.jsonl#L8784>) · [原始来源](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L184>)

#### Werepup（幼子） · `boss-werepup`
- **角色功能/身份依据**：遭遇后挖钥匙卡、父子尾声的提问者；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：卡片称天生变形亲和，母亲Erauqs；玩家的毕业/VR回忆是玩家，不是幼崽自传。
- **口吻/声线**：自身台词仅Gee papa、superhero、Can I重复追问，兴奋仰慕；证据不足扩写成熟声线。
- **观察行为**：听玩家回忆，挖卡赠予；向父亲求下次训练。
- **关系、版本和证据边界**：成人话题是成年人对幼崽回忆，明确暂缓成人互动；不能把幼崽当21岁讲述者。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：Werepup独立场景第一人称几乎全为玩家；其直接话语见父亲场景171/178–179，父亲184答复。
- 证据：`U634da93e6a656cc80f5c` / `O41ef0db5166c62d3b241` · `datav/dictionary.json#ui.card.CosmoCardWerepup.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6515>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`V7e92b286a418ffc7c48f` / `O3a29a67b9fc1b0bd129d` · `vsn/m_ClassicWerepup/script.vsn:162` · [位置](<../../../catalog/occurrences.jsonl#L8847>) · [原始来源](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L162>)
- 证据：`Vd7bf1f0f445e574d7108` / `O8e0175d319220f4740cc` · `vsn/m_ClassicWerepup/script.vsn:184` · [位置](<../../../catalog/occurrences.jsonl#L8857>) · [原始来源](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L184>)
- 证据：`Vd3c21ab4ac8140eb6d64` / `Of843d7458e52815a2868` · `vsn/m_ClassicWerehund/script.vsn:184` · [位置](<../../../catalog/occurrences.jsonl#L8784>) · [原始来源](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L184>)

#### SqueakerBoss（场景个体） · `boss-squeaker`
- **角色功能/身份依据**：取回Cosmohelm节点；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：原文玩家辨认头盔；卡片介绍Squeaker物种偷窃/快速，不直接证明每个动作均该首领所为。
- **口吻/声线**：该VSN无可辨Boss直接台词，不能从玩家训斥构造其顶嘴口吻。
- **观察行为**：战后主角发现自己的Cosmohelm；头盔具体搬运主角有must猜测。
- **关系、版本和证据边界**：不把开场小偷、任意Squeaker与Boss强证同人；物种习性不是个体人格。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：全段发言是玩家；不要将pipsqueak/小贼训斥给Squeaker本人。
- 证据：`U90771bde017e8dee80cd` / `O58e511e31dd487ac79e2` · `datav/dictionary.json#ui.card.CosmoCardSqueaker.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6503>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Vae8f85531a74cccc0746` / `O0b15430051d27c9823e6` · `vsn/m_ClassicSqueakerBoss/script.vsn:5` · [位置](<../../../catalog/occurrences.jsonl#L8691>) · [原始来源](<../../../sources/blobs/21645f1219dc510e550cadc33679ec16bfdc934df3c936bd79b815f3c0d066f0.vsn#L5>)
- 证据：`V0f60066d6df0f07d4f16` / `O1364d8857165c433f58e` · `vsn/m_ClassicSqueakerBoss/script.vsn:13` · [位置](<../../../catalog/occurrences.jsonl#L8696>) · [原始来源](<../../../sources/blobs/21645f1219dc510e550cadc33679ec16bfdc934df3c936bd79b815f3c0d066f0.vsn#L13>)
- 证据：`V0aa16be204f4dd5b153f` / `Oe5f0ee057ad8e11e594a` · `vsn/m_ClassicSqueakerBoss/script.vsn:22` · [位置](<../../../catalog/occurrences.jsonl#L8702>) · [原始来源](<../../../sources/blobs/21645f1219dc510e550cadc33679ec16bfdc934df3c936bd79b815f3c0d066f0.vsn#L22>)

#### Dragon / ClassicDragonV2 · `boss-dragon`
- **角色功能/身份依据**：矿区龙类传说与Sevaw能力线索；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：卡正面为传说，背面说Fenfen Esper Sevaw按幼年故事召唤apparition自卫；属于资料卡解释。
- **口吻/声线**：本次没有该龙直接对白证据，无声线；不因ALPHA头衔造傲慢龙王人格。
- **观察行为**：作为矿区战斗节点被提示提及；不要把“影像/显现”全译成实体远古龙。
- **关系、版本和证据边界**：传说、召唤显现、解剖肉类店说法分层；未核二者机制，不替所有龙科设统一身世。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：卡片叙述者说法，不是Dragon或Sevaw直接自述。
- 证据：`Uf043ccb603b699a57827` / `Odf64f9c93d5b342e2ba5` · `datav/dictionary.json#ui.card.CosmoCardDragon.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6479>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`U61fbecb6ec0783d0fb53` / `O48e0a6d2a2232acd10f7` · `datav/dictionary.json#ui.card.CosmoCardDragon.desc.Back` · [位置](<../../../catalog/occurrences.jsonl#L6478>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)

#### Sevaw / SEVAW档案标题 · `fenfen-sevaw`
- **角色功能/身份依据**：Dragon显现的召唤者；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：卡片点名Fenfen Esper Sevaw；Z3同拼写倒序标题对应很强，但原名到场景对象仍未运行核证。
- **口吻/声线**：无独立日常对话；Z3若归该档案，是庄重历史叙述而非龙声线。
- **观察行为**：卡片说以童年听闻故事召显现自卫。
- **关系、版本和证据边界**：不把Sevaw写成Dragon本体，也不因Z3标题证明所有历史we均他独历。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：资料卡第三人称，Z3记忆集体叙述；非同一声部。
- 证据：`Uf043ccb603b699a57827` / `Odf64f9c93d5b342e2ba5` · `datav/dictionary.json#ui.card.CosmoCardDragon.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6479>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`U92cef30530c466844d39` / `O3626940b44bff87c3433` · `datav/dictionary.json#ui.data.f_AgentFZ3` · [位置](<../../../catalog/occurrences.jsonl#L6559>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)

#### Erauqs / ERAUQS档案标题 · `fenfen-erauqs`
- **角色功能/身份依据**：Werepup母亲/能力传递发现；原作稳定脚本/entry/卡片标题；见各证据。
- **自述与客观层级**：卡背明确Elder Erauqs为母亲、与非Esper丈夫结合后发现部分力量可传递。
- **口吻/声线**：无足够独立生活台词；Z6是仪式叙述口吻，不扩写慈母/严厉妻子人格。
- **观察行为**：能力发现为卡片报告，不是她在场亲口教授。
- **关系、版本和证据边界**：Werehund卡妻子与Werepup母亲支持家庭关系，但不凭匿名图像定每位人物造型。 当前catalog生效文本；男女镜像按各path，JAR/PAK不同版不擅互补；高（定位）；本场/卡片认知边界保留。
- **施受/发话归属**：卡片第三人称，与Z6集体/仪式记忆声音分开。
- 证据：`U634da93e6a656cc80f5c` / `O41ef0db5166c62d3b241` · `datav/dictionary.json#ui.card.CosmoCardWerepup.desc.Front` · [位置](<../../../catalog/occurrences.jsonl#L6515>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)
- 证据：`Uc781902974216b5a5ce5` / `O9cc97a9858c052d49f9b` · `datav/dictionary.json#ui.data.f_AgentFZ6` · [位置](<../../../catalog/occurrences.jsonl#L6565>) · [原始来源](<../../../sources/blobs/c824f484f6ec3d19b3b69e9ae892acaf1451649c47b2ee8df8e5f015b1f8553d.json#L1>)

#### Depot B奴贩/废品商（AreaB_Slaver2） · `shop-b-slaver2`
- **角色功能/身份依据**：伪食物/赃物/破损武器交易；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：称奴隶抱怨苍蝇、装备有故事是自述；未讲故事内容不能补遭遇。
- **口吻/声线**：gots/gimme/ole/pree-mo、heh-heh，粗俗交易口语；对没钱/犹豫者急躁。
- **观察行为**：普通人形面前推吃食、鳞装面前承认赃物并问船员归属；狗态赶回笼。
- **关系、版本和证据边界**：不能把koboCostume条件当玩家天生物种；装友好是状态反应，不必全局善良/邪恶口号。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`Dc89186c6bbf5a5149eb6` / `O325d443ba58f267f7a70` · `datadm/all.ds:1008` · [位置](<../../../catalog/occurrences.jsonl#L3112>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1008>)
- 证据：`Dd03692735e547e3c7323` / `O673b32ac7787ca271098` · `datadm/all.ds:1042` · [位置](<../../../catalog/occurrences.jsonl#L3123>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1042>)
- 证据：`Df1fb023529235695fdb7` / `O992136124c0f3cb483db` · `datadm/all.ds:1075` · [位置](<../../../catalog/occurrences.jsonl#L3134>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1075>)

#### Sceafya黑市商（AreaC_Slaver1） · `shop-c-slaver1`
- **角色功能/身份依据**：伪食物、精灵物品和PSY卡交易；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：自称七沼泽最精美食物、害怕PSY，均角色说法；卡能力有传闻it is said。
- **口吻/声线**：假殷勤接毒舌，lookee/Jus/ya know、调笑cabin-boy；口语与威胁不套文言客官。
- **观察行为**：人形推食物/海盗工作，鳞装欢迎黑市，拥有卡时害怕被炸。
- **关系、版本和证据边界**：不把他与B店奴贩合并同名个人；big night/forest不证明全昼夜时序。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`D7df47bfc7692f2d1856a` / `O6ae060dcf8288b352e6c` · `datadm/all.ds:1406` · [位置](<../../../catalog/occurrences.jsonl#L3222>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1406>)
- 证据：`Dd7204cd8ceca860adcff` / `O4cc325a94a59523353e0` · `datadm/all.ds:1453` · [位置](<../../../catalog/occurrences.jsonl#L3239>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1453>)
- 证据：`De0beb32acb4f26015665` / `O96b8198c19f13d0353fe` · `datadm/all.ds:1482` · [位置](<../../../catalog/occurrences.jsonl#L3251>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1482>)

#### Ayskammr肉窖主人（AreaA_Cellar） · `shop-a-cellar`
- **角色功能/身份依据**：私藏龙肉/秘密代码；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：自称杀龙并分割，属于自述；不因Sevaw幻龙设定强解释肉来源。
- **口吻/声线**：heeeello热情、our little secret私语、He He笑，献宝/分享式调侃。
- **观察行为**：允许拿肉、要求保密、再给卡通/卡牌库代码。
- **关系、版本和证据边界**：说话者未具名；是否Macsen仅共享模板不能终裁；代码是元功能非世界秘密。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`Dd8c299718241d394e36e` / `O0cd036c7b1d26fdf82eb` · `datadm/all.ds:292` · [位置](<../../../catalog/occurrences.jsonl#L2952>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L292>)
- 证据：`D0b3f28be1b149eb688f6` / `Odff9f9d40f48c9249ccd` · `datadm/all.ds:302` · [位置](<../../../catalog/occurrences.jsonl#L2956>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L302>)
- 证据：`Dcc20b96f8bd629e43e28` / `O5f71b8af9a1cce04dd34` · `datadm/all.ds:307` · [位置](<../../../catalog/occurrences.jsonl#L2959>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L307>)

#### 机库肉铺主人（AreaH_Cellar） · `shop-h-cellar`
- **角色功能/身份依据**：补给与休养人数反馈；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：英雄称号只营救>=7条件；供货生意随人数而变，不说满员或早期已成英雄。
- **口吻/声线**：welcome welcome、带胃口和钱、meat/meet冷笑话，热情生意口语。
- **观察行为**：0人不备货，1/4/7档逐渐旺；没钱仍催Lect。
- **关系、版本和证据边界**：不凭共享Macsen话术或行商设定把A/H两肉铺无证合一。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`Db1d278162bc779398ddb` / `O7ecc70d544b872b90795` · `datadm/all.ds:1554` · [位置](<../../../catalog/occurrences.jsonl#L3265>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1554>)
- 证据：`D92f8033806a020e64ce1` / `O86d4af3d1d1635711971` · `datadm/all.ds:1582` · [位置](<../../../catalog/occurrences.jsonl#L3278>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1582>)
- 证据：`D6eb2fa617b4f8534061d` / `Occf14e69138ed71c0fe7` · `datadm/all.ds:1621` · [位置](<../../../catalog/occurrences.jsonl#L3286>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1621>)

#### 机库育种/观察员（AreaH_MacsenBreeding） · `shop-h-breeder`
- **角色功能/身份依据**：捕获/亲和/水晶教学；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：说明Trainer/Trainee区别和亲和奖励，机制说明非自称超能力大师。
- **口吻/声线**：COME ON IN/FELLOW BREEDER、BYE-OH、鼓励MAXXXED强调；大写不等于每句吼叫。
- **观察行为**：鼓励喂饱、亲近并尝试各生物；允许换回武器。
- **关系、版本和证据边界**：entry有Macsen不证明所有场所为同一个可分身者；严守对应条件不提前给奖励。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`Dc8327cb286c3a2ecdf74` / `O373b9115c4640cd4ddf2` · `datadm/all.ds:1703` · [位置](<../../../catalog/occurrences.jsonl#L3310>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1703>)
- 证据：`Dc1ed4ed58c9fa0bbc42b` / `O4980db4516a7198a5a03` · `datadm/all.ds:1719` · [位置](<../../../catalog/occurrences.jsonl#L3318>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1719>)
- 证据：`D422114309ba07af8dad1` / `Occ847a03a1c84f586059` · `datadm/all.ds:1730` · [位置](<../../../catalog/occurrences.jsonl#L3325>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1730>)

#### 机库机械师（AreaH_MacsenMechanic） · `shop-h-mechanic`
- **角色功能/身份依据**：修船与缺件提示；当前DS entry和条件分支；*不作为同一人身份证明。
- **自述与客观层级**：说老板已付安装费；四件齐需时间是其说明，不是此处已修完。
- **口吻/声线**：先澄清not that kind of shop，再直接务实讲零件，my sources say保传闻。
- **观察行为**：按StarkillV3/缺Gun→Shield→Radar→Turbo优先给提示与Navmap标记。
- **关系、版本和证据边界**：Macsen概览见配角参照；不把Tomcat当实际修船者，不把首次机库开放写成终盘。；不同场所共享include不足证明同一人或分身。 本次核男线PAK；女线/原JAR需按自身原文复核；高（当前场所文本），全局身份不定。
- 证据：`Dc5bdbcdceb830555098c` / `O7518ec7bb290a9dd8547` · `datadm/all.ds:1771` · [位置](<../../../catalog/occurrences.jsonl#L3326>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1771>)
- 证据：`Dbd0ad53989de920a827c` / `O44fe1f3207210c575287` · `datadm/all.ds:1795` · [位置](<../../../catalog/occurrences.jsonl#L3339>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1795>)
- 证据：`Dcc4c1da03f6cc8a0de61` / `Obfea178b181f4d405d68` · `datadm/all.ds:1815` · [位置](<../../../catalog/occurrences.jsonl#L3350>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1815>)

### 图鉴对象（非人格）

#### BugSpiker · `dex-BugSpiker`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBugSpiker，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：银色带刺机械仿体，制造者数据不足。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dfb8e0614c734eb500131` / `Oc8227e39ed2d2509f0dc` · `datadf/all.ds:2740` · [位置](<../../../catalog/occurrences.jsonl#L1157>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2740>)
- 证据：`De933955b20dc64b1a22d` / `Oc2b7948077102e9eef2f` · `datadm/all.ds:2768` · [位置](<../../../catalog/occurrences.jsonl#L4082>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2768>)
- 证据：`D0cc34c6316d30b428762` / `Oab6ce7b8e5c5bd081da0` · `datadm/all.ds:2773` · [位置](<../../../catalog/occurrences.jsonl#L4087>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2773>)

#### Squeaker · `dex-Squeaker`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSqueaker，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：棕毛近视、速度快且偷窃；物种习性不等于首领本人。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D8e0573f6830646376b6a` / `O98c14bff4eea72e7f0d2` · `datadf/all.ds:2748` · [位置](<../../../catalog/occurrences.jsonl#L1163>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2748>)
- 证据：`D6548a5d7553ec0ca49ca` / `O2072f53beec326800614` · `datadm/all.ds:2776` · [位置](<../../../catalog/occurrences.jsonl#L4088>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2776>)
- 证据：`Db7c147600b88864c5722` / `Of2f1257c7fa3510817ab` · `datadm/all.ds:2780` · [位置](<../../../catalog/occurrences.jsonl#L4092>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2780>)

#### Swiper · `dex-Swiper`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSwiper，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：大型粉毛条纹猫科、强爪与后腿、懒；不把名称当动作。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D516c30b00d6f73c9cb5a` / `O952f986d3917b6de54bf` · `datadf/all.ds:2756` · [位置](<../../../catalog/occurrences.jsonl#L1169>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2756>)
- 证据：`D7293c8137034f6763c27` / `O65655ae0ad8b2cec78a9` · `datadm/all.ds:2784` · [位置](<../../../catalog/occurrences.jsonl#L4094>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2784>)
- 证据：`D6c56e39f4ffb34d17a0b` / `O1eb78af5908d295a6b8a` · `datadm/all.ds:2789` · [位置](<../../../catalog/occurrences.jsonl#L4099>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2789>)

#### Bumper · `dex-Bumper`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBumper，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：故障巡逻机器人上下运动；不可译成兽。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D1d4ce61890390c788e32` / `O755b0bb28061eb01bf91` · `datadf/all.ds:2764` · [位置](<../../../catalog/occurrences.jsonl#L1175>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2764>)
- 证据：`D8a25efcc881471cbeb4f` / `O426b165cf2266271d9b5` · `datadm/all.ds:2794` · [位置](<../../../catalog/occurrences.jsonl#L4102>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2794>)
- 证据：`D83e4697bb41de17281de` / `O5f8f8b1e63eac7e8f170` · `datadm/all.ds:2799` · [位置](<../../../catalog/occurrences.jsonl#L4107>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2799>)

#### FlyDrone · `dex-FlyDrone`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicFlyDrone，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：自动接战程序，靠近会受攻击。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Db7e6b7dcb88f82c35bc4` / `O8f9644082ec3ca9396b0` · `datadf/all.ds:2776` · [位置](<../../../catalog/occurrences.jsonl#L1183>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2776>)
- 证据：`D45c521902ccadfb8dc51` / `O3d1c218d453e325fa0c6` · `datadm/all.ds:2814` · [位置](<../../../catalog/occurrences.jsonl#L4118>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2814>)
- 证据：`D7c50bec99f402f4086c9` / `O0363851d33520c1550cf` · `datadm/all.ds:2820` · [位置](<../../../catalog/occurrences.jsonl#L4124>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2820>)

#### CannonFloor · `dex-CannonFloor`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicCannonFloor，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：约两个世纪制式自卫炮塔，与训练装备相似。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D18e671e69c652335657c` / `O3adcb0072a438547ee3a` · `datadf/all.ds:2783` · [位置](<../../../catalog/occurrences.jsonl#L1188>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2783>)
- 证据：`D07891eb8e2ad19e829fd` / `O8b08444a0bf8c07e03bb` · `datadm/all.ds:2823` · [位置](<../../../catalog/occurrences.jsonl#L4125>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2823>)
- 证据：`De4dbe2aaffc72815b626` / `O78e078ae1a367ca4a261` · `datadm/all.ds:2832` · [位置](<../../../catalog/occurrences.jsonl#L4134>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2832>)

#### XCannonCeiling · `dex-XCannonCeiling`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicXCannonCeiling，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：海盗自修炮、弹为塑化金属；建废墟基地是推断。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Db3b35761ac25548f4086` / `O91d102738973ddc79752` · `datadf/all.ds:2816` · [位置](<../../../catalog/occurrences.jsonl#L1215>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2816>)
- 证据：`De965adfc09ab084bc121` / `Oc178dbf7c91d6c6e0b02` · `datadm/all.ds:2859` · [位置](<../../../catalog/occurrences.jsonl#L4155>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2859>)
- 证据：`Db0a297f91f81a7acd6b2` / `O5c16b1751bb1060a1d70` · `datadm/all.ds:2868` · [位置](<../../../catalog/occurrences.jsonl#L4164>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2868>)

#### Blocker · `dex-Blocker`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBlocker，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：遗迹异常、似免多数物理伤害，PSY弱点源于前探员报告。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Db9bfb2fdc485ff860e7b` / `O0e5a41d2c344740f70d0` · `datadf/all.ds:2853` · [位置](<../../../catalog/occurrences.jsonl#L1245>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2853>)
- 证据：`De51d28f84eee67dd8f39` / `Od42effc413ac521cd509` · `datadm/all.ds:2895` · [位置](<../../../catalog/occurrences.jsonl#L4185>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2895>)
- 证据：`Dbfc6431c07aacedcd7c7` / `O75306fec07212a69e000` · `datadm/all.ds:2904` · [位置](<../../../catalog/occurrences.jsonl#L4194>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2904>)

#### Tentacle · `dex-Tentacle`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicTentacle，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：较小Blocker型，预期同样抗物理；不据名创造独立人格。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Ddd442e2d2f8627c07cf7` / `Oe28e0416ea4cd397e7c7` · `datadf/all.ds:2865` · [位置](<../../../catalog/occurrences.jsonl#L1255>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2865>)
- 证据：`Db9a31bf56595672f2e37` / `O850e5e85f7d25926e88d` · `datadm/all.ds:2907` · [位置](<../../../catalog/occurrences.jsonl#L4195>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2907>)
- 证据：`D690c7fe4850566646892` / `Of36cb5d928c890348ccc` · `datadm/all.ds:2910` · [位置](<../../../catalog/occurrences.jsonl#L4198>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2910>)

#### SpikeballZero · `dex-SpikeballZero`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSpikeballZero，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：Bossu称不可破坏被主角质疑，带作弊笑话。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D3768db53e3bb85df38f5` / `Oe8390f2ba6e9527ea456` · `datadf/all.ds:2871` · [位置](<../../../catalog/occurrences.jsonl#L1259>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2871>)
- 证据：`D8c8b20a77d3d6a2c95e9` / `Of339f5abe9ca663acf16` · `datadm/all.ds:2913` · [位置](<../../../catalog/occurrences.jsonl#L4199>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2913>)
- 证据：`Df72d417648d2b52c4c48` / `O3a16172f80b8be32fd51` · `datadm/all.ds:2924` · [位置](<../../../catalog/occurrences.jsonl#L4210>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2924>)

#### MineZero · `dex-MineZero`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicMineZero，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：震动激活近接雷；引爆方法与冷笑话不混人格。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Ddcfa7ac4e2843a447499` / `Od2cc19423522ce03cf14` · `datadf/all.ds:2885` · [位置](<../../../catalog/occurrences.jsonl#L1271>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2885>)
- 证据：`D9b34846af1bfe39de1f4` / `Oad113de0c10a7089428e` · `datadm/all.ds:2928` · [位置](<../../../catalog/occurrences.jsonl#L4212>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2928>)
- 证据：`D71fda6d8a60bba8cbd1f` / `O1a0af4494d252e552cd1` · `datadm/all.ds:2939` · [位置](<../../../catalog/occurrences.jsonl#L4223>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2939>)

#### MineWallZero · `dex-MineWallZero`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicMineWallZero，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：地雷mine双关节点，不是单独有声角色。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D407b3a00963573879b2e` / `O6b931f90aa29d2030dbe` · `datadf/all.ds:2918` · [位置](<../../../catalog/occurrences.jsonl#L1300>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2918>)
- 证据：`D1cc869e4d5bc0934bbfb` / `O03f10b4c9a480da72ec7` · `datadf/all.ds:2920` · [位置](<../../../catalog/occurrences.jsonl#L1302>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2920>)
- 证据：`D97acc908c475a9916189` / `O2adda26a6338548c97c1` · `datadf/all.ds:2921` · [位置](<../../../catalog/occurrences.jsonl#L1303>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2921>)

#### BigboldEnemy · `dex-BigboldEnemy`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBigboldEnemy，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：深层同物种不同个体、更强；震动扰巢属解释。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D21a5525982cf2f9f2411` / `Oca0738896753b716320a` · `datadf/all.ds:2924` · [位置](<../../../catalog/occurrences.jsonl#L1304>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2924>)
- 证据：`D85c4672c4be2cc17b90f` / `O684d5baf11fc27aa95cc` · `datadm/all.ds:2972` · [位置](<../../../catalog/occurrences.jsonl#L4250>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2972>)
- 证据：`D6fbcacad9713522c04fa` / `Od87b7b5fc1919f998e3a` · `datadm/all.ds:2985` · [位置](<../../../catalog/occurrences.jsonl#L4263>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2985>)

#### Dwarf · `dex-Dwarf`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicDwarf，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：犬科矿工/强力拳击，与稀矿有关；giant dwarfism语用反差。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dc0f54b45c697af6f26bc` / `Odb63dbb56866df7db1bd` · `datadf/all.ds:2939` · [位置](<../../../catalog/occurrences.jsonl#L1318>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2939>)
- 证据：`Dbf70b9a4a2eb02c42c8d` / `O415be81c7b3258ed132a` · `datadm/all.ds:2987` · [位置](<../../../catalog/occurrences.jsonl#L4264>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2987>)
- 证据：`D3cc50fc3132d38bc57f2` / `O625fa7b1d687c06a8e3c` · `datadm/all.ds:2997` · [位置](<../../../catalog/occurrences.jsonl#L4274>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2997>)

#### Flamer · `dex-Flamer`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicFlamer，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：龙科掘石巢、有领地意识，吐火驱入侵者。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D02570fee748e1d553caf` / `O7955489532c488358c6e` · `datadf/all.ds:2965` · [位置](<../../../catalog/occurrences.jsonl#L1340>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2965>)
- 证据：`D57b9c2809560372ad1b3` / `Of1c8f9cb526700a44f48` · `datadm/all.ds:3013` · [位置](<../../../catalog/occurrences.jsonl#L4286>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3013>)
- 证据：`D7b71128dbb0c097d5c54` / `Oe63a1739c40a66b7f1a4` · `datadm/all.ds:3018` · [位置](<../../../catalog/occurrences.jsonl#L4291>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3018>)

#### Flybomb · `dex-Flybomb`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicFlybomb，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：悬浮无人机带爆炸载荷，宜远程应对。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D7b8fb17b7ed5b6009ab9` / `Oa486f2f7632677251967` · `datadf/all.ds:2972` · [位置](<../../../catalog/occurrences.jsonl#L1345>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2972>)
- 证据：`Dced4c7a532d9294162f9` / `O82a6dcad40bae1480e17` · `datadf/all.ds:2977` · [位置](<../../../catalog/occurrences.jsonl#L1350>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2977>)
- 证据：`D422dfa6a2fc5815afe6b` / `O1494a025333c3f8fc2bc` · `datadm/all.ds:3025` · [位置](<../../../catalog/occurrences.jsonl#L4296>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3025>)

#### Spikebot · `dex-Spikebot`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSpikebot，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：原运矿/工具轮机被改装刺与寻敌逻辑。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Db9879998a2737a56db82` / `O829863279bb55814844e` · `datadf/all.ds:2980` · [位置](<../../../catalog/occurrences.jsonl#L1351>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2980>)
- 证据：`D0a0562c6bc040757b38b` / `O9df35108fe2d4ae2dd0e` · `datadm/all.ds:3028` · [位置](<../../../catalog/occurrences.jsonl#L4297>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3028>)
- 证据：`Dfdf8b1abd9240a082041` / `O272d2df3f19285d47683` · `datadm/all.ds:3034` · [位置](<../../../catalog/occurrences.jsonl#L4303>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3034>)

#### Wyvern · `dex-Wyvern`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicWyvern，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：敏捷飞行龙科，高潮分心战术来自前队记录，当前独行不能照用。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D71538f9724092a07ce72` / `Od80b27f552d4d8d94722` · `datadf/all.ds:2989` · [位置](<../../../catalog/occurrences.jsonl#L1358>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L2989>)
- 证据：`Dd301cf74357041898fca` / `Oce734c9839a4b5aedb4b` · `datadm/all.ds:3037` · [位置](<../../../catalog/occurrences.jsonl#L4304>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3037>)
- 证据：`D9f6670c84a88de676aa7` / `O528ab715f36928161df7` · `datadm/all.ds:3049` · [位置](<../../../catalog/occurrences.jsonl#L4316>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3049>)

#### Fire · `dex-Fire`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicFire，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：矿区火可扫灭却会重燃，是环境危险。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Da3d54da2429c0fcd9d47` / `O7cba9c624a638bffaff3` · `datadf/all.ds:3003` · [位置](<../../../catalog/occurrences.jsonl#L1370>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3003>)
- 证据：`Dd03222602229eee6c4af` / `O1a6dfc71565a097882bd` · `datadm/all.ds:3052` · [位置](<../../../catalog/occurrences.jsonl#L4317>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3052>)
- 证据：`D70f9ef7e5f464d083332` / `O217d8f12b369b0187faf` · `datadm/all.ds:3053` · [位置](<../../../catalog/occurrences.jsonl#L4318>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3053>)

#### Driller · `dex-Driller`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicDriller，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：纳米机械自修，限矿区运行，等/造空隙穿过。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D5caacc098dcfba1fbe4b` / `O92e36425c795c5a40b5f` · `datadf/all.ds:3007` · [位置](<../../../catalog/occurrences.jsonl#L1372>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3007>)
- 证据：`Dc6d1528a813f620ba782` / `O42b010a5ea248a4dbf37` · `datadf/all.ds:3015` · [位置](<../../../catalog/occurrences.jsonl#L1380>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3015>)
- 证据：`D4fdaeb6c96a5bdeef9a4` / `O8b41ba5bb79d95f182b0` · `datadm/all.ds:3063` · [位置](<../../../catalog/occurrences.jsonl#L4326>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3063>)

#### Mine · `dex-Mine`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicMine，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：矿井地雷及所有权双关，不给装置人格。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dcfb0d2795adf8563a88a` / `Ofbbb7547e07cadfa3085` · `datadf/all.ds:3018` · [位置](<../../../catalog/occurrences.jsonl#L1381>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3018>)
- 证据：`D9b20bbf24880288d1ccf` / `Oa0269f1397b535ef1499` · `datadm/all.ds:3067` · [位置](<../../../catalog/occurrences.jsonl#L4328>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3067>)
- 证据：`D76e86f60d00fbb1d6f4e` / `O2d626bedb667308b3b31` · `datadm/all.ds:3073` · [位置](<../../../catalog/occurrences.jsonl#L4334>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3073>)

#### Barker · `dex-Barker`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBarker，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：红毛feral犬，处繁殖季是阶段判断，男线报告跃前低吼。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Ddd96e0742fbbb4bbbc3d` / `O92bb23b881e2650164ec` · `datadf/all.ds:3041` · [位置](<../../../catalog/occurrences.jsonl#L1399>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3041>)
- 证据：`D758ee6c4edd1678fa033` / `O2988efef6206f192b023` · `datadm/all.ds:3095` · [位置](<../../../catalog/occurrences.jsonl#L4351>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3095>)
- 证据：`Dae2608ce9fd12fb09ee8` / `O0e8bb7a0db37c23c99cb` · `datadm/all.ds:3105` · [位置](<../../../catalog/occurrences.jsonl#L4361>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3105>)

#### Kobold · `dex-Kobold`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicKobold，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：绿色拟人蜥蜴、海盗奴贩逐利；总部许可买回探员，不等于所有个体同一人格。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D3cca34c0c0b9e05f5179` / `O826c24a313d7f09f7b17` · `datadf/all.ds:3053` · [位置](<../../../catalog/occurrences.jsonl#L1409>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3053>)
- 证据：`Db3e108c43fe2e9e96a55` / `Oc46262f46143a5270b73` · `datadm/all.ds:3110` · [位置](<../../../catalog/occurrences.jsonl#L4364>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3110>)
- 证据：`D9beede62566232e767ee` / `Od2582ea0a87c40d0fce0` · `datadm/all.ds:3121` · [位置](<../../../catalog/occurrences.jsonl#L4375>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3121>)

#### Fenfen · `dex-Fenfen`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicFenfen，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：图鉴遇到的是机械复制体，原生有毛族群另列。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D3d655b3d460896f9951d` / `Oa6d18b09a8386995abec` · `datadf/all.ds:3065` · [位置](<../../../catalog/occurrences.jsonl#L1419>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3065>)
- 证据：`D6e6502a174573bf6140d` / `O78f189f7c18c5738e817` · `datadm/all.ds:3125` · [位置](<../../../catalog/occurrences.jsonl#L4377>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3125>)
- 证据：`D1ad1f0199fae9cf16b48` / `O429870245653e6c57714` · `datadm/all.ds:3137` · [位置](<../../../catalog/occurrences.jsonl#L4389>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3137>)

#### BugFlier · `dex-BugFlier`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBugFlier，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：旧站纳米机械回收自修，过时后难拆。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D4b4db7f96bdf3380bdeb` / `O000059a9bccb01172eaa` · `datadf/all.ds:3078` · [位置](<../../../catalog/occurrences.jsonl#L1430>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3078>)
- 证据：`D9cecb815d3ead9979303` / `Of1ab72ec2ab954f539c0` · `datadm/all.ds:3142` · [位置](<../../../catalog/occurrences.jsonl#L4392>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3142>)
- 证据：`Db37cabfd70b571c0c5c2` / `O59eab8bdcaaecbd66c8a` · `datadm/all.ds:3157` · [位置](<../../../catalog/occurrences.jsonl#L4407>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3157>)

#### CeilingTurret · `dex-CeilingTurret`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicCeilingTurret，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：电气系统损伤或致天花炮乱射，原因probably不定。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D7ec3051fc05db57bcec2` / `O7562468c9c7e5dcb99a4` · `datadf/all.ds:3093` · [位置](<../../../catalog/occurrences.jsonl#L1443>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3093>)
- 证据：`D11903fa8e43e248d4278` / `O5f600ae5ab4c4abda1ac` · `datadm/all.ds:3160` · [位置](<../../../catalog/occurrences.jsonl#L4408>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3160>)
- 证据：`Dd5ceb8d01edd3c68023d` / `Ofae81cd00d4f84252689` · `datadm/all.ds:3166` · [位置](<../../../catalog/occurrences.jsonl#L4414>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3166>)

#### Orber · `dex-Orber`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicOrber，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：反重力滚动触手团，Bossu建议避开。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`De9098dd0bdcbb6686fd0` / `O476ba3ffa9a3982222cd` · `datadf/all.ds:3116` · [位置](<../../../catalog/occurrences.jsonl#L1462>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3116>)
- 证据：`Df90d5ad17534d1f1da2d` / `Off90ada0805730646d1f` · `datadm/all.ds:3183` · [位置](<../../../catalog/occurrences.jsonl#L4427>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3183>)
- 证据：`Dd0e1b446211a9bb7a7f0` / `O8efc326396eccf579579` · `datadm/all.ds:3191` · [位置](<../../../catalog/occurrences.jsonl#L4435>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3191>)

#### Jellyfish · `dex-Jellyfish`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicJellyfish，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：非物理精神异常报告；主角受击吐槽不是水母说话。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dfccc45cc29de47fd5b89` / `Odb4931725a302877f84b` · `datadf/all.ds:3126` · [位置](<../../../catalog/occurrences.jsonl#L1470>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3126>)
- 证据：`D6fc0303239e980828ab4` / `O5b3a8e7cd7c5b4df1007` · `datadm/all.ds:3195` · [位置](<../../../catalog/occurrences.jsonl#L4437>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3195>)
- 证据：`D0f5d51e08ddc9289bfdd` / `O5fe2a66ff67baa19e7b8` · `datadm/all.ds:3206` · [位置](<../../../catalog/occurrences.jsonl#L4448>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3206>)

#### Archer · `dex-Archer`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicArcher，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：Sceafya年轻精灵战斗者，部分不朽的种族概述非每个个体。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D17b382128cc21c7a6308` / `O25871effa77ad5bdc2c5` · `datadf/all.ds:3138` · [位置](<../../../catalog/occurrences.jsonl#L1481>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3138>)
- 证据：`D5b2a0ded65b05a8c4a4b` / `O0941d5049655f792da9c` · `datadm/all.ds:3208` · [位置](<../../../catalog/occurrences.jsonl#L4449>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3208>)
- 证据：`D19a92a0d298c43889bd7` / `O6fda860e5fad296df668` · `datadm/all.ds:3219` · [位置](<../../../catalog/occurrences.jsonl#L4460>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3219>)

#### Bulber · `dex-Bulber`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBulber，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：再生植物，攻击靠近未知动物。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D1374ab1fe1127d62d0a9` / `O570fcd7fadb2cef2b531` · `datadf/all.ds:3152` · [位置](<../../../catalog/occurrences.jsonl#L1493>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3152>)
- 证据：`Da3f50273c25db88fefe7` / `Of5ca7106694f726e3341` · `datadm/all.ds:3222` · [位置](<../../../catalog/occurrences.jsonl#L4461>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3222>)
- 证据：`D03a219330882a1035f9d` / `O34c427812269da21b4ed` · `datadm/all.ds:3224` · [位置](<../../../catalog/occurrences.jsonl#L4463>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3224>)

#### Bullfrog · `dex-Bullfrog`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBullfrog，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：据报告Hopper吸精神能量变体，远泡与长舌伤害。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D94cdd0b668a409dbfa08` / `Od65baabc30d343ed6f34` · `datadf/all.ds:3157` · [位置](<../../../catalog/occurrences.jsonl#L1496>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3157>)
- 证据：`Dc666dbc85660a3be0667` / `O6a441ed4e465d53414e1` · `datadm/all.ds:3227` · [位置](<../../../catalog/occurrences.jsonl#L4464>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3227>)
- 证据：`D77ef56036cf7bdf7b366` / `O54479c6278d30d809bad` · `datadm/all.ds:3233` · [位置](<../../../catalog/occurrences.jsonl#L4470>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3233>)

#### BumperC · `dex-BumperC`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicBumperC，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：装甲更好巡逻机、撞击更疼。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dc2fd89154684ee982d4d` / `O36f6164c219bb7a1683c` · `datadf/all.ds:3166` · [位置](<../../../catalog/occurrences.jsonl#L1503>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3166>)
- 证据：`Def2c0606064a27d89d4f` / `O54d27b252304a018e56f` · `datadm/all.ds:3236` · [位置](<../../../catalog/occurrences.jsonl#L4471>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3236>)
- 证据：`De768083eb82ee39649b2` / `Oae614ca5116b5c4dbcfe` · `datadm/all.ds:3240` · [位置](<../../../catalog/occurrences.jsonl#L4475>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3240>)

#### CannonCeilingC · `dex-CannonCeilingC`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicCannonCeilingC，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：久未自修的炮似功率更高，语气推测。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D2a4fe8565f6793bc65ec` / `O016dfddd78a53a28315d` · `datadf/all.ds:3173` · [位置](<../../../catalog/occurrences.jsonl#L1508>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3173>)
- 证据：`D2da0b13ef37e89272217` / `O37b51f1ec51d96dcdd08` · `datadm/all.ds:3243` · [位置](<../../../catalog/occurrences.jsonl#L4476>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3243>)
- 证据：`D8e2eba435163b9ebf0f7` / `O9ee446bde455d8ed32d6` · `datadm/all.ds:3247` · [位置](<../../../catalog/occurrences.jsonl#L4480>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3247>)

#### Hopper · `dex-Hopper`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicHopper，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：暂定命名，本普通蛙似受能量致强韧好斗。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D08e9c948975d44cfc3aa` / `O10e7ae7fc3ed769a49ab` · `datadf/all.ds:3209` · [位置](<../../../catalog/occurrences.jsonl#L1535>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3209>)
- 证据：`Daacca3e332d912656255` / `O643431c369e15c5eca3a` · `datadm/all.ds:3278` · [位置](<../../../catalog/occurrences.jsonl#L4503>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3278>)
- 证据：`D4b428eebd7f97f88bf8e` / `O77aec0a4fe0a25f65ba7` · `datadm/all.ds:3287` · [位置](<../../../catalog/occurrences.jsonl#L4512>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3287>)

#### Ivyball · `dex-Ivyball`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicIvyball，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：只说无法杀死故无情报，不补藤球外观或生态。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D82f1eeae75f8b14509ed` / `O6401c4fd5aa3c664211c` · `datadf/all.ds:3221` · [位置](<../../../catalog/occurrences.jsonl#L1545>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3221>)
- 证据：`D053445449e5ff7031c4e` / `Ob03d7aebdc3e627b65c8` · `datadm/all.ds:3290` · [位置](<../../../catalog/occurrences.jsonl#L4513>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3290>)

#### Omegothrower · `dex-Omegothrower`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicOmegothrower，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：原文称Omegobin，在树梢藏身投掷；不是据entry发明新种。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dde2e7d6ec9f75b6ee20a` / `O69094af5b4faccc630d8` · `datadf/all.ds:3224` · [位置](<../../../catalog/occurrences.jsonl#L1546>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3224>)
- 证据：`D6fe280ca441c15235a50` / `O0c54c83a7d50abec53ec` · `datadm/all.ds:3293` · [位置](<../../../catalog/occurrences.jsonl#L4514>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3293>)
- 证据：`D3d973cfca379d6065c2d` / `Obc374400578cf84fa127` · `datadm/all.ds:3296` · [位置](<../../../catalog/occurrences.jsonl#L4517>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3296>)

#### Spiderbot · `dex-Spiderbot`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSpiderbot，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：非真蜘蛛，机械纳米网维护环境。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dff8d597f900bfead7553` / `O98576dc249bbafdca8e2` · `datadf/all.ds:3230` · [位置](<../../../catalog/occurrences.jsonl#L1550>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3230>)
- 证据：`Dfbfd40f559ec5ccc82b3` / `O9369d0bf3dfb82cfb853` · `datadm/all.ds:3299` · [位置](<../../../catalog/occurrences.jsonl#L4518>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3299>)
- 证据：`D3c60eeed95e139ca2a12` / `O9a64707a850330b891aa` · `datadm/all.ds:3310` · [位置](<../../../catalog/occurrences.jsonl#L4529>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3310>)

#### Thorner · `dex-Thorner`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicThorner，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：Viner演化型可射刺。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D643d2e421f3f84504979` / `Oaab5ac6f7aaac3465064` · `datadf/all.ds:3245` · [位置](<../../../catalog/occurrences.jsonl#L1562>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3245>)
- 证据：`Da671acf23f7f3560809a` / `O7e3df3a88dba265e03db` · `datadm/all.ds:3313` · [位置](<../../../catalog/occurrences.jsonl#L4530>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3313>)
- 证据：`D6943b4cf13b5d62011b4` / `Oc4d6ce9a9d46504d05dc` · `datadm/all.ds:3316` · [位置](<../../../catalog/occurrences.jsonl#L4533>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3316>)

#### Tribulb · `dex-Tribulb`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicTribulb，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：更凶Bulber型，突然射击。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Da04127548777829b3b84` / `O645e6c2707d58d1371b7` · `datadf/all.ds:3251` · [位置](<../../../catalog/occurrences.jsonl#L1566>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3251>)
- 证据：`D1bdab7fa7384c18202a4` / `O7e0fa0a36b01b7f54c13` · `datadm/all.ds:3319` · [位置](<../../../catalog/occurrences.jsonl#L4534>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3319>)
- 证据：`Dc273d5cea3ac625ce5c6` / `O40e74966416104a14f59` · `datadm/all.ds:3322` · [位置](<../../../catalog/occurrences.jsonl#L4537>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3322>)

#### Viner · `dex-Viner`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicViner，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：快速生长围猎物，待别的生物制伏后取能。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Dc86aab8580b5fda0f5f2` / `O437e852becaf5ee7ca8a` · `datadf/all.ds:3257` · [位置](<../../../catalog/occurrences.jsonl#L1570>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3257>)
- 证据：`Df2dd9be0561465d46f77` / `Od4b0fbc3eb531f43998d` · `datadm/all.ds:3325` · [位置](<../../../catalog/occurrences.jsonl#L4538>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3325>)
- 证据：`D354b8575406af4893f89` / `Oc1e29058d884edf3ce2e` · `datadm/all.ds:3329` · [位置](<../../../catalog/occurrences.jsonl#L4542>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3329>)

#### Xeno · `dex-Xeno`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicXeno，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：不属总部已知生态、疑寻卵宿主，提示别研究；不能反证全宇宙未知。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Da65ac093cd03f50cf5c9` / `O8e0a556e468e7f408557` · `datadf/all.ds:3265` · [位置](<../../../catalog/occurrences.jsonl#L1575>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3265>)
- 证据：`Db8ceba97e6e2dcaa6c09` / `O461072d0b727d9080f08` · `datadm/all.ds:3332` · [位置](<../../../catalog/occurrences.jsonl#L4543>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3332>)
- 证据：`D78d78be02d386c1dc1e9` / `Oedc236e6ee094ea33d09` · `datadm/all.ds:3343` · [位置](<../../../catalog/occurrences.jsonl#L4554>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3343>)

#### Crawly · `dex-Crawly`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicCrawly，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：沿地形单向循环，总部无资料，似威胁不大。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D4be014de00d07dc38cb4` / `O700b4eb8f8dbc4a970d5` · `datadf/all.ds:3278` · [位置](<../../../catalog/occurrences.jsonl#L1587>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3278>)
- 证据：`D1f9347b5abae67db0528` / `O5c5f0905be474d0a9f43` · `datadm/all.ds:3345` · [位置](<../../../catalog/occurrences.jsonl#L4555>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3345>)
- 证据：`Daa5b5307c80dea015144` / `O0ed2ac1c3310213099a4` · `datadm/all.ds:3349` · [位置](<../../../catalog/occurrences.jsonl#L4559>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3349>)

#### Ghoster · `dex-Ghoster`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicGhoster，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：暂定名、似无尽生成精神动荡显现。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`D58064d5635db99b7d4d4` / `O1368f37e163f9f4873c7` · `datadf/all.ds:3285` · [位置](<../../../catalog/occurrences.jsonl#L1592>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3285>)
- 证据：`De7783887ca551b03ad9a` / `O37de77e763578d74f734` · `datadm/all.ds:3352` · [位置](<../../../catalog/occurrences.jsonl#L4560>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3352>)
- 证据：`D62a543f842b688831395` / `Ob2119bc3c3ba8c8d326c` · `datadm/all.ds:3359` · [位置](<../../../catalog/occurrences.jsonl#L4567>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3359>)

#### SpaceHead · `dex-SpaceHead`
- **角色功能/身份依据**：遭遇说明/生态或战术情报对象；BossuDex.ClassicSpaceHead，按entry区别物种/设备与个体，不从UI同名推单人。
- **自述与客观层级**：以下为Bossu/总部图鉴报告或主角观察，不是对象直接自述。
- **口吻/声线**：本次没有该对象独立台词可建声线；引用中的Bossu说明和玩家吐槽不可转给它。
- **观察行为**：大浮头像Ghoster、可能更强精神异常。
- **关系、版本和证据边界**：单场/物种行为不当独立人格；seems/reports/for now保持认知层级。若与首领同名，交叉参照首领个体条目而非合并全部。 当前PAK两路线图鉴各自source；原JAR另核；高（原文位置）；物种主张有界。
- 证据：`Ddacf768900dcbf0e5428` / `O485628a7cbb739f8ea42` · `datadf/all.ds:3295` · [位置](<../../../catalog/occurrences.jsonl#L1600>) · [原始来源](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3295>)
- 证据：`D9d58a0238df00de11f7a` / `O76ac07c116e260ff0418` · `datadm/all.ds:3362` · [位置](<../../../catalog/occurrences.jsonl#L4568>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3362>)
- 证据：`Daaa319ff3e680cdaead4` / `O296ff6089295b06a321e` · `datadm/all.ds:3365` · [位置](<../../../catalog/occurrences.jsonl#L4571>) · [原始来源](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3365>)

### 其他角色／叙事声部

#### 匿名任务报告编辑（-EDITOR） · `narrator-editor`
- **角色功能/身份依据**：失败报告整理/对被俘结果的机构评述；报告正文/直接引语，未凭图像定个体。
- **自述与客观层级**：用seems/as far as we can make out/believe表明证据局限；恢复心智是希望，不是已实现。
- **口吻/声线**：冷静报告语体、we here at PPP、档案on hold的公务冷幽默；不让前段受制主角继续说这段话。
- **观察行为**：根据残留记录给结论，说明后续调查和档案暂存。
- **关系、版本和证据边界**：-EDITOR未具名；不能因好结局SIGNED BOSSU就把所有编辑都定Bossu。 当前PAK相应路线，不跨SFW强补；高（文字）；匿名身份不定。
- 证据：`V5b2be15bc92522ad4ce7` / `O0e8aec9197dd0ec98617` · `vsn/m_GameOverAreaA/script.vsn:93` · [位置](<../../../catalog/occurrences.jsonl#L9002>) · [原始来源](<../../../sources/blobs/fcb1c4f6824f86c2676cc22aabad97631b15f7358203cfe0ac839575b9f368e8.vsn#L93>)
- 证据：`V2e6e02356878853ba464` / `O2977053ba936be407e02` · `vsn/m_GameOverAreaA/script.vsn:118` · [位置](<../../../catalog/occurrences.jsonl#L9017>) · [原始来源](<../../../sources/blobs/fcb1c4f6824f86c2676cc22aabad97631b15f7358203cfe0ac839575b9f368e8.vsn#L118>)
- 证据：`Vedd76574d4db58424c68` / `Oa39945aad2f6f988b45b` · `vsn/f_GameOverAreaA/script.vsn:117` · [位置](<../../../catalog/occurrences.jsonl#L7824>) · [原始来源](<../../../sources/blobs/cfd853e9a3ac0fcbe84afac19f9669c9b2a333504384bf99225e645eee21b8d8.vsn#L117>)

#### 好结局报告署名Bossu（交叉参照） · `narrator-good-report`
- **角色功能/身份依据**：兄姐弟任务总结与庆功；报告正文/直接引语，未凭图像定个体。
- **自述与客观层级**：结局报告有明确SIGNED BOSSU，战绩修辞仍属于报告框架。
- **口吻/声线**：正式总结与英雄颂扬；不把报告中elder sister/younger brother当兄弟姐妹互相自称。
- **观察行为**：以双全名和亲属关系结案。
- **关系、版本和证据边界**：Bossu日常画像见characters-support，不另造全知旁白。 当前PAK相应路线，不跨SFW强补；高（文字）；匿名身份不定。
- 证据：`Vab192be073383a46437e` / `O13c960410aeedf0216d0` · `vsn/m_EndingGood/script.vsn:55` · [位置](<../../../catalog/occurrences.jsonl#L8901>) · [原始来源](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L55>)
- 证据：`V0550adfc3a915ed7cbbe` / `O9445e86e4a5f516eec61` · `vsn/m_EndingGood/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L8904>) · [原始来源](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L58>)
- 证据：`V1f422217877d0e1a1372` / `O014c38c7ec9610db4cad` · `vsn/m_EndingGood/script.vsn:61` · [位置](<../../../catalog/occurrences.jsonl#L8907>) · [原始来源](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L61>)

#### 失败C分支精灵巡林/温泉引导者群 · `elves-bathers`
- **角色功能/身份依据**：拦截、安抚并驯化失败主角；报告正文/直接引语，未凭图像定个体。
- **自述与客观层级**：主角转述她们的话，并猜药物或PSY；未确认具体机制。
- **口吻/声线**：Shh/Just relax/good puppy/sweet nothings，柔声短命令；仅本场，不当所有精灵日常都甜腻。
- **观察行为**：无视弱抗议、安排清洗/拥抱、反复引导服从。
- **关系、版本和证据边界**：具体个体无姓名；不能把每句都归Enelye。 当前PAK相应路线，不跨SFW强补；高（文字）；匿名身份不定。
- 证据：`Va19f80cbd27b44e7337e` / `Oe7e0a7c0eb634e305356` · `vsn/m_GameOverAreaC/script.vsn:67` · [位置](<../../../catalog/occurrences.jsonl#L9113>) · [原始来源](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L67>)
- 证据：`V0426a4c5f7384a30dbfd` / `Oe340d6bfa6373e781bf5` · `vsn/m_GameOverAreaC/script.vsn:104` · [位置](<../../../catalog/occurrences.jsonl#L9135>) · [原始来源](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L104>)
- 证据：`Va92be2047f39f9bb30d7` / `Oe0a2b1317c18c5474b62` · `vsn/f_GameOverAreaC/script.vsn:94` · [位置](<../../../catalog/occurrences.jsonl#L7931>) · [原始来源](<../../../sources/blobs/682a581be597f1e8ebab0a4c806e91954a77f447205088940e4e7aefb88cbf30.vsn#L94>)

#### Gobin村落俘获者群（与Omegobin名界待核） · `gobin-captors`
- **角色功能/身份依据**：失败C村落/吊笼俘获节点；报告正文/直接引语，未凭图像定个体。
- **自述与客观层级**：名字由主角报告称Gobin；装备卖海盗、守卫被叫走原因是主角推测。
- **口吻/声线**：主角听不懂其语言/只转述snorting或jabbering；没有足够可译直接台词建声线。
- **观察行为**：带走主角、群体看守、吊笼；男线靠看守离开逃走，女线自述撬笼。
- **关系、版本和证据边界**：不因Gobin字根将其与Pigobin个人合并；Gobin/Omegobin具体分类仍按原词分列，不自创二者严格谱系。 当前PAK相应路线，不跨SFW强补；高（文字）；匿名身份不定。
- 证据：`Vebe92d4eed3128235ad2` / `O2e564fbc64811b075cee` · `vsn/m_GameOverAreaC/script.vsn:18` · [位置](<../../../catalog/occurrences.jsonl#L9083>) · [原始来源](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L18>)
- 证据：`Vaaa2fc80e840f257973a` / `O4c4b691aefe043c0de93` · `vsn/m_GameOverAreaC/script.vsn:62` · [位置](<../../../catalog/occurrences.jsonl#L9111>) · [原始来源](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L62>)
- 证据：`Vb0532bc783c5446d55b1` / `O0fe25114dad3f5aa507e` · `vsn/f_GameOverAreaC/script.vsn:58` · [位置](<../../../catalog/occurrences.jsonl#L7910>) · [原始来源](<../../../sources/blobs/682a581be597f1e8ebab0a4c806e91954a77f447205088940e4e7aefb88cbf30.vsn#L58>)

#### Flayer / Mind Flayer（报告对象） · `flayer-report`
- **角色功能/身份依据**：失败A及Vulcan记忆中的精神影响；报告正文/直接引语，未凭图像定个体。
- **自述与客观层级**：报告编辑称心智被剥取并与另一触手生物似共生；具体机制不是其亲口自述。
- **口吻/声线**：没有可辨直接台词；good boy称呼的Vulcan回忆源头不清，不给Flayer编人格台词。
- **观察行为**：以目光/触手制伏，报告认为取心智能量；阶段性资料非全游戏物种定理。
- **关系、版本和证据边界**：Flayer不因中文近似被混成Flamer；主角语音失真不是它说话。 当前PAK相应路线，不跨SFW强补；高（文字）；匿名身份不定。
- 证据：`V8e20d97e2ab4f53386c3` / `O4701442807cb48460c96` · `vsn/m_GameOverAreaA/script.vsn:85` · [位置](<../../../catalog/occurrences.jsonl#L8997>) · [原始来源](<../../../sources/blobs/fcb1c4f6824f86c2676cc22aabad97631b15f7358203cfe0ac839575b9f368e8.vsn#L85>)
- 证据：`Vad65a4de1114a6d6935c` / `Od3f23f6b049f0ab02d7b` · `vsn/m_AgentM04/script.vsn:54` · [位置](<../../../catalog/occurrences.jsonl#L8124>) · [原始来源](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L54>)
- 证据：`Vf9d00a6ebaf77c1106f2` / `Oa27ea73cca8fc7422640` · `vsn/m_AgentM04/script.vsn:90` · [位置](<../../../catalog/occurrences.jsonl#L8145>) · [原始来源](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L90>)

## 身份仍不应强定的部分

- AreaA/H肉铺、B/C奴贩、Breeding/Mechanic均以稳定场所entry标记。共享交易include或Macsen标签，不证明分身，也不足无条件合为同一有名NPC；具体场景对象由主控后续核。
- 六Fenfen档案有标题，Sevaw/Erauqs有额外卡片支持；仍不把全部we/us历史归某一人独历，不由匿名Fox/Anon模板猜所有个体。
- Werepup自己的话只见父子尾声小量提问；Werepup独立场景的21岁、毕业、VR等是成年玩家对幼崽讲往事。Bigbold/SqueakerBoss/Dragon没有本次可建独立声线的直接话，不能用玩家对白替它们塑性格。
- 浴池精灵、村落Gobin、前任队长、早期模糊俘获者及编辑仍匿名；没有声线证据不造口癖。Flayer与Flamer严格分开。
- 物种、群体、独立个体、机械仿体和环境危险分别记录。可观察行为不等于性格，更不等于所有同种个体道德一致。

## 粗校使用守则

1. 同一报告先标说话者，再标自夸/被拆台/记忆模糊，最后调整中文口气；不能只搜Top/bottom做全局替换。
2. 结巴、含混口音、原文排版断词、无线电杂音分开；不给每只猫加喵、每只犬加汪、每只鬣狗加笑声。
3. 源自单场的温柔/暴躁/爱财/支配，不扩成全部人生或亲属关系；证据不足就保留本场语气。
4. 英式/俚语/动物双关按功能重写，Pigobin有限古雅不覆盖科幻技术词。
