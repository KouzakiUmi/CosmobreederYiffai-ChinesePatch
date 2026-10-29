# 世界观、剧情结构与剧透参照（R1）

> 仅文档整理/粗校参照；全部术语暂译，未经终裁；不批量改正式译文或上线。含终盘与失败剧透。

## 阅读范围与核证

- 已逐句通读lore导出的全部独立文本：VSN **2321个unique unit**（导出所涉67份脚本）、BossuDex **676个unique unit**、TomcatItems **1140个unique unit**，含男女两线。导出每unit附一个选定位置；VSN这些unit在catalog共有2388个occurrence，dex共有922个、items共有1324个。**不把unit级source读完等同所有重复位置/上下文都读完。** 先抽出source阅读稿，再用<=100行连续小段实际阅读，不以关键词扫当通读。
- 对上述4137个独立unit各自导出的选定位置，逐条核对catalog unit原文、occurrence路径/行号、resources当前生效blob原始行，零不符；不是全部catalog位置的核证声明。[结构化参照](<world-and-plot.json>)保留全文证据、unit/occurrence/catalog行/资源hash/物理源行和每脚本或entry索引。
- 不把VSN非text演出/解锁指令称为已全读。DS男主线初次长read虽请求覆盖1–2481但返回裁剪，不验收全文；女DS非图鉴/道具未全读，由主控其他粗校包补齐。已读主线原始条件块列于下文。旧摘要只当线索，不作为事实唯一依据。

## 可靠性与分轴

**已证实**＝原文确如此呈现/确实这么说；仍受路线限制。**单方说辞**＝角色、总部、Fenfen记忆或报告编辑的有界认知。**推测**＝seems/might/I think/疑问、预言或解释。可信度“高”指原文和定位核证，不保证角色主张客观为真。不得把“本次局部未读到”升级成“游戏未提供”。

- 性别轴：m玩家Yiffai、f玩家Yiffany，开场救援对象/受控Starkill/哨子转交与驾驶员镜像。Yiffany始终姐姐、Yiffai始终弟弟。各同事m/f报告常只是题材槽位相对，不是同事件代词替换。
- 内容版本轴：SFW是原始JAR自身资源，NSFW是PAK覆盖内容；两归档都包含男女资源。已核[独立来源说明:7–18](<../../../optimization/r28/sfw/README.md#L7-L18>)及[隔离约束:38–44](<../../../optimization/r28/sfw/README.md#L38-L44>)、[卡背留白:82](<../../../optimization/r28/sfw/README.md#L82>)。本参照核当前catalog生效原文，不把PAK成人情节补进JAR；未重新宣称运行时完整加载分支已实测。
- 状态轴：同一DS内营救人数、装备、形态、首领胜负分支，与男女和内容版本均不同；狗态店主反应不是失败结局。

## 章节偏序与揭示门槛

**目录顺序不等于游玩顺序；下面是文本支持的局部偏序，不是已实测唯一攻略。**

1. 3P片头 → GameStart（Tutone/5555、双任务、已知失踪手足）→ 受袭下降/装备被盗 → Zeronia追装备、Bigbold、V2塌顶逃生。
2. 机库/teleportal允许休息、探索与回访；不能仅凭AreaA/B/C目录排唯一0→A→B→C。A区Redbull/Dragon与C区Enelye/Pigobin均有先败对称提示。
3. 图鉴/物品通话按已遭遇/已取得用，不把后期能力灌进开场。机库开放不等于英雄称号、修船/女王话题已全解锁。
4. **失踪手足开场已知；后期确认的是当前敌人身份和受控原因。** StarkillV3前不把模糊敌称提前直译成姐姐/弟弟；后期全名不能反证开场不知道家人。
5. C双首领败后回Zeronia → StarkillV3相认 → 气密套装配齐 → Exile；Fenfen Z系列是历史回溯，不是按文件顺序发生的新事件。
6. 先记录Fenfen日志、后获得项链复看解读是文本支持的层次；获取与理解不同。
7. 低轨坠落无线电不是全游戏结尾；区分修船不足的EndingBad、追击入口与EndingGood。GameOverArea0/A/B/C/E是替代失败报告，不接入成功主线当必经章节。

## 已核原始条件（非运行时实测）

- **C01** Cellar按agentsRescued()分0、>=1、>=4、>=7，great hero只>=7；不是未经核定的满员。 [原始控制流:1552–1589](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1552-L1589>)
- **C02** 机械师位置提示需ClassicStarkillV3_defeated，再按缺Gun→Shield→Radar→Turbo的else-if优先；齐件才说需要安装时间。 [原始控制流:1777–1818](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L1777-L1818>)
- **C03** upgraded_TazerAttuned分艺术品/未修破损两套说法，不是设定矛盾。 [原始控制流:4282–4292](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4282-L4292>)
- **C04** A区Redbull/Dragon、C区Enelye/Pigobin有对称先败提示，只证明提示支持双先后，非完整可达路线。 [原始控制流:3509–3683](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3509-L3683>)
- **C05** Area0 Endgame需C双首领败；先StarkillV3，再CosmoBody/Head配齐，再指向Exile。 [原始控制流:3486–3501](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3486-L3501>)
- **C06** 见过Exile金库后提示Fenfen；3701与3702为跨行完整句，不是截断。开锁标志后才说金库深处黑暗能量。 [原始控制流:3691–3710](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3691-L3710>)

## 事实层（稳定锚点）

### W01 · 时代/组织
超光速航行和先进赛博机器人时代；3P派Cosmobreeders收集情报。文明繁荣/全民敬仰是宣传式旁白评价，不自动证明组织绝对正义。
- 已证实（框架）；单方说辞（评价）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**片头**。
- `V461a6a7d5f000b146d7c` / `O6f1874ad91277b85ec82` · `vsn/ClassicPreTitle/script.vsn:6` · [catalog位置](<../../../catalog/occurrences.jsonl#L6787>) · [当前原文:6](<../../../sources/blobs/93f5c0dd1ffc4e76059f3d9e0d6eee36b28ea8ec11106b6343c76a9336ddaa33.vsn#L6>)
- `V55c96355e2eb9ed0e0ab` / `Oa0d45569662be525ff41` · `vsn/ClassicPreTitle/script.vsn:32` · [catalog位置](<../../../catalog/occurrences.jsonl#L6794>) · [当前原文:32](<../../../sources/blobs/93f5c0dd1ffc4e76059f3d9e0d6eee36b28ea8ec11106b6343c76a9336ddaa33.vsn#L32>)

### W02 · 天体
Tutone明确是5555星系的行星；XXXX星历与倒计时是掩码，不补年代。40N/74W是计划下降坐标，不推全图中心。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**开场**。
- `Vfe440d529a77f7889ac2` / `O6e87be36775bc5790e80` · `vsn/m_GameStart/script.vsn:6` · [catalog位置](<../../../catalog/occurrences.jsonl#L9144>) · [当前原文:6](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L6>)
- `V19028f4bad54a44a177c` / `Oef0167ace37e225e502f` · `vsn/m_GameStart/script.vsn:18` · [catalog位置](<../../../catalog/occurrences.jsonl#L9146>) · [当前原文:18](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L18>)

### W03 · 任务
Bossu为指挥官；任务同时要求有用生物数据和寻找失踪同僚，不是仅杀敌或仅救姐姐。
- 已证实（任务口径）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**开场**。
- `V7e5558b3c01bcc427629` / `Oe1c1e35550dfaad049f0` · `vsn/m_GameStart/script.vsn:19` · [catalog位置](<../../../catalog/occurrences.jsonl#L9147>) · [当前原文:19](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L19>)
- `V19bb5e02417dd779ae52` / `O2cc1d3ef5fa8395bae6a` · `vsn/m_GameStart/script.vsn:35` · [catalog位置](<../../../catalog/occurrences.jsonl#L9154>) · [当前原文:35](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L35>)

### W04 · 男女镜像
男线Yiffai首次飞行、班级第一、寻找失踪姐姐；女线Yiffany临时受命寻找弟弟Yiffai。不是两次事件依序叠在同一次游玩。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**开场**。
- `V14bea897234f812bf8dc` / `O6fa9a3dae88ba2cf230f` · `vsn/m_GameStart/script.vsn:23` · [catalog位置](<../../../catalog/occurrences.jsonl#L9148>) · [当前原文:23](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L23>)
- `V19bb5e02417dd779ae52` / `O2cc1d3ef5fa8395bae6a` · `vsn/m_GameStart/script.vsn:35` · [catalog位置](<../../../catalog/occurrences.jsonl#L9154>) · [当前原文:35](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L35>)

### W05 · 男女镜像
女线明确Yiffany是姐姐、Yiffai为弟弟。姐姐救弟弟，不是妹妹救兄长。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**开场**。
- `V6b946ff0cd3e851cd52f` / `O92cd853866ba1c6f31ed` · `vsn/f_GameStart/script.vsn:23` · [catalog位置](<../../../catalog/occurrences.jsonl#L7946>) · [当前原文:23](<../../../sources/blobs/11a3464d17326cec77a18a7d047ac7cb98ee22286e0e8468a8131ba70dd7ef42.vsn#L23>)
- `V7847f0e261e479955cbf` / `Of08c9c9464b2573a786d` · `vsn/f_GameStart/script.vsn:36` · [catalog位置](<../../../catalog/occurrences.jsonl#L7953>) · [当前原文:36](<../../../sources/blobs/11a3464d17326cec77a18a7d047ac7cb98ee22286e0e8468a8131ba70dd7ef42.vsn#L36>)

### W06 · 全名
好结局报告写Yiffany Yiffai为姐姐/资深老将，Yiffai Yiffai为弟弟/天才；末段Yiffai重名不可擅自删掉。
- 已证实（结局报告）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**好结局全名，不前灌**。
- `Vab192be073383a46437e` / `O13c960410aeedf0216d0` · `vsn/m_EndingGood/script.vsn:55` · [catalog位置](<../../../catalog/occurrences.jsonl#L8901>) · [当前原文:55](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L55>)
- `V1f422217877d0e1a1372` / `O014c38c7ec9610db4cad` · `vsn/m_EndingGood/script.vsn:61` · [catalog位置](<../../../catalog/occurrences.jsonl#L8907>) · [当前原文:61](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L61>)

### W07 · 年龄
Yiffai自报21岁、首次任务；成人主角被叫pup不等于未成年。
- 单方说辞（多处一致）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Bigbold后**。
- `V60e2610da1363aa4fd96` / `O8711c26c30b47d3461b5` · `vsn/m_ClassicBigbold/script.vsn:34` · [catalog位置](<../../../catalog/occurrences.jsonl#L8511>) · [当前原文:34](<../../../sources/blobs/9be0235b421ca71a01278d5959459ac8489ec48684e86f1ff645f3ae8d19025f.vsn#L34>)
- `V509ba93f7a5556baea43` / `O944727aa4c6611e47011` · `vsn/m_ClassicBigbold/script.vsn:43` · [catalog位置](<../../../catalog/occurrences.jsonl#L8516>) · [当前原文:43](<../../../sources/blobs/9be0235b421ca71a01278d5959459ac8489ec48684e86f1ff645f3ae8d19025f.vsn#L43>)

### W08 · 年龄/履历
Yiffany说22岁荣誉毕业、曾为PPPC招募宣传面孔及最年轻现役，纪录后被弟弟破。22是毕业/首任务年龄，不是明确当前年龄。3P/PPP/PPPC/3PC未在本次原文中展开全称，不造四个组织。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**BigboldV2后**。
- `V9b7d2d514805746355e0` / `Oaceef4097553b99b104b` · `vsn/f_ClassicBigboldV2/script.vsn:15` · [catalog位置](<../../../catalog/occurrences.jsonl#L7374>) · [当前原文:15](<../../../sources/blobs/4815d8fd5f3908b51ef353cd8f2eec2028b9d1612d660af9f236e1a3e6d23232.vsn#L15>)
- `V821bf51b08a5f7fdcfba` / `O356b4b4a9e1d0b9d5fb0` · `vsn/f_ClassicBigboldV2/script.vsn:26` · [catalog位置](<../../../catalog/occurrences.jsonl#L7381>) · [当前原文:26](<../../../sources/blobs/4815d8fd5f3908b51ef353cd8f2eec2028b9d1612d660af9f236e1a3e6d23232.vsn#L26>)

### W09 · 训练
男线18岁前不许实操；先自动训练工具后VR，用此前探员首任务模拟；RealFeel有振动/电刺激。第一次实战不等于未受训练。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Werepup回忆**。
- `V72c17f5952ef6a975ed3` / `O23346acae18972cf83c7` · `vsn/m_ClassicWerepup/script.vsn:18` · [catalog位置](<../../../catalog/occurrences.jsonl#L8792>) · [当前原文:18](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L18>)
- `V190e70794d19b638005c` / `Ob6cf9c3b3b72eed12083` · `vsn/m_ClassicWerepup/script.vsn:84` · [catalog位置](<../../../catalog/occurrences.jsonl#L8822>) · [当前原文:84](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L84>)

### W10 · 开场偏序
通话干扰→不明敌舰围攻→紧急下降→船损仍能飞→装备被盗→追入洞口。敌人身份不可用后文提前代称。
- 已证实（场景）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**开场**。
- `Vfa848cd72b97a813db48` / `O5f39fc2ea696bcdb4783` · `vsn/m_GameStart/script.vsn:42` · [catalog位置](<../../../catalog/occurrences.jsonl#L9155>) · [当前原文:42](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L42>)
- `V2593d5d258113e2337ed` / `Of94f70bd92ba38dc198a` · `vsn/m_GameStart/script.vsn:121` · [catalog位置](<../../../catalog/occurrences.jsonl#L9174>) · [当前原文:121](<../../../sources/blobs/78e99a122124f1eede83a3d0a2e36d2f54f5d0197400a541fafb41f7016505d9.vsn#L121>)

### W11 · 采集双关
战后data/research叠加公务口吻和亲密接触/形态行为观察。不能全部净化成战斗情报，也不能所有data都荤化。
- 已证实（语用）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**对应战后场景**。
- `V35753ef8d2e8ce3545f3` / `O3eaf818ea22d9b055205` · `vsn/m_ClassicBigboldV2/script.vsn:51` · [catalog位置](<../../../catalog/occurrences.jsonl#L8581>) · [当前原文:51](<../../../sources/blobs/b7036abd2f81660ca9c02eb8e7ab148eacb67d5e92abf05c1301d658f7958115.vsn#L51>)
- `V6898fbdec6f7ad53f202` / `O9db61455d92adec0e2ee` · `vsn/m_ClassicBigboldV2/script.vsn:83` · [catalog位置](<../../../catalog/occurrences.jsonl#L8592>) · [当前原文:83](<../../../sources/blobs/b7036abd2f81660ca9c02eb8e7ab148eacb67d5e92abf05c1301d658f7958115.vsn#L83>)

### W12 · 道具取得
BigboldV2逃跑撞门致塌顶，落下hyper bracer供滑行逃生；不是敌人主动赠予。
- 已证实（场景）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**BigboldV2后**。
- `Vbc39b6700499188d96dc` / `O2b8ab9c1b423ab764b66` · `vsn/m_ClassicBigboldV2/script.vsn:215` · [catalog位置](<../../../catalog/occurrences.jsonl#L8627>) · [当前原文:215](<../../../sources/blobs/b7036abd2f81660ca9c02eb8e7ab148eacb67d5e92abf05c1301d658f7958115.vsn#L215>)
- `V73ae48e307b5c7eadf69` / `Oc5f313cdf525c22cd842` · `vsn/m_ClassicBigboldV2/script.vsn:248` · [catalog位置](<../../../catalog/occurrences.jsonl#L8639>) · [当前原文:248](<../../../sources/blobs/b7036abd2f81660ca9c02eb8e7ab148eacb67d5e92abf05c1301d658f7958115.vsn#L248>)

### W13 · 战后反转
Redbull仍能反制主角，交出此前战士留下的鞋并退入矿井；不能写成永久击杀或玩家毫无疑问完胜。
- 已证实（场景）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Redbull后**。
- `V8fbbb671495980a55f0e` / `O7cc615106cfe7095e804` · `vsn/m_ClassicBossRedbull/script.vsn:13` · [catalog位置](<../../../catalog/occurrences.jsonl#L8646>) · [当前原文:13](<../../../sources/blobs/39b33e833a253f07235cd336ef168863adfc749f94082c79d8c958a614d51e98.vsn#L13>)
- `V039d12864539ff38e40f` / `O0d3702a8344a50680c7e` · `vsn/m_ClassicBossRedbull/script.vsn:50` · [catalog位置](<../../../catalog/occurrences.jsonl#L8660>) · [当前原文:50](<../../../sources/blobs/39b33e833a253f07235cd336ef168863adfc749f94082c79d8c958a614d51e98.vsn#L50>)

### W14 · 角色/语域
Enelye自称Tutone精灵不朽High Lady，赞赏战斗后给主角穿裙；男线抗议、女线说下回自己穿，不可互换。
- 单方说辞（身份）；已证实（场景）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Enelye后**。
- `V999b254bd5dfa6ae3e0a` / `O1f4b45aa23a38f1a3776` · `vsn/m_ClassicEnelye/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L8661>) · [当前原文:5](<../../../sources/blobs/28b549c22b50eb578e4211521e52e85bc89bf091b75c82e6d52ae854c1f477ab.vsn#L5>)
- `Vbe95c0e7724981c8d0aa` / `Obdee6145ab24aad222be` · `vsn/m_ClassicEnelye/script.vsn:29` · [catalog位置](<../../../catalog/occurrences.jsonl#L8674>) · [当前原文:29](<../../../sources/blobs/28b549c22b50eb578e4211521e52e85bc89bf091b75c82e6d52ae854c1f477ab.vsn#L29>)

### W15 · 道具/语域
Pigobin说古语、给项链并称可理解当地语言；古语是角色文体，不授权整个科幻世界古风化。
- 已证实（赠予）；单方说辞（功能，后有通话佐证）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**PigobinV3后**。
- `Va87e9b3dbf6b755ea053` / `Oc5a2e346c20c75d21319` · `vsn/m_ClassicPigobinV3/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L8675>) · [当前原文:5](<../../../sources/blobs/507a1034c21fb60d63b45055c7a1fd5e31593d8d4ecbacc398bc4b73dfe01763.vsn#L5>)
- `V574a507a7af1ddf40041` / `O07fa4e79e39c930c0770` · `vsn/m_ClassicPigobinV3/script.vsn:38` · [catalog位置](<../../../catalog/occurrences.jsonl#L8690>) · [当前原文:38](<../../../sources/blobs/507a1034c21fb60d63b45055c7a1fd5e31593d8d4ecbacc398bc4b73dfe01763.vsn#L38>)

### W16 · 能力/预言
Werehund父亲Esper使主角兽态化，自称Zener能量可随意变形；他因快速习得而判断主角是chosen one，是父亲信念，不是全知授予唯一救世主。
- 已证实（变形）；单方说辞（机理/预言）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Werehund后**。
- `Vaf7dd57056720eea492a` / `Oa1a5a2668f3f2ff2e746` · `vsn/m_ClassicWerehund/script.vsn:123` · [catalog位置](<../../../catalog/occurrences.jsonl#L8758>) · [当前原文:123](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L123>)
- `Vd3c21ab4ac8140eb6d64` / `Of843d7458e52815a2868` · `vsn/m_ClassicWerehund/script.vsn:184` · [catalog位置](<../../../catalog/occurrences.jsonl#L8784>) · [当前原文:184](<../../../sources/blobs/84107b94199ab6ae3dfef734025c84a05f7418b80b83b5514a7aa8683da0eda2.vsn#L184>)

### W17 · 幼崽边界/钥匙卡
Werepup被认为不懂成人话题，主角推迟成人互动；回忆是成人主角的过去，不是幼崽参与。末尾幼崽挖卡赠玩家，不是玩家赠卡。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**Werepup后**。
- `V7e92b286a418ffc7c48f` / `O3a29a67b9fc1b0bd129d` · `vsn/m_ClassicWerepup/script.vsn:162` · [catalog位置](<../../../catalog/occurrences.jsonl#L8847>) · [当前原文:162](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L162>)
- `V6d973f390e555b4dce41` / `Oca5002f42b15c7b03e89` · `vsn/m_ClassicWerepup/script.vsn:190` · [catalog位置](<../../../catalog/occurrences.jsonl#L8860>) · [当前原文:190](<../../../sources/blobs/4f192932288d9d92c91595133e95647ed9271093e79f47123120ade8b17614da.vsn#L190>)

### W18 · 相认/哨子
男线唤醒受控姐姐Yiffany；姐姐说受dark queen控制、暂不能战斗，交父亲哨子并当驾驶员。不是玩家把哨子给姐姐。
- 已证实（相认/赠予）；单方说辞（体验）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**StarkillV3后**。
- `Vd23eb400d183857344ce` / `O8412a0ae707b31ef48f2` · `vsn/m_ClassicStarkillV3/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L8703>) · [当前原文:5](<../../../sources/blobs/6e099226f9924e5387f1bc5f2f9dfcf0a95045a23ed241f55716ecdaadbc95ce.vsn#L5>)
- `Vf5d9788c9895aff82a64` / `O04703be7e3b9c5d54f0d` · `vsn/m_ClassicStarkillV3/script.vsn:36` · [catalog位置](<../../../catalog/occurrences.jsonl#L8719>) · [当前原文:36](<../../../sources/blobs/6e099226f9924e5387f1bc5f2f9dfcf0a95045a23ed241f55716ecdaadbc95ce.vsn#L36>)

### W19 · 相认/哨子
女线唤醒弟弟Yiffai；弟弟交回姐姐曾给的父亲旧哨子并驾驶接应。两条获救者不同时叠进一条线。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**StarkillV3后**。
- `V44bdc68e09da003fe3fb` / `Obb28d40545e60e42b0b9` · `vsn/f_ClassicStarkillV3/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L7514>) · [当前原文:5](<../../../sources/blobs/e9a9d407b5f4b2ca3d14b73ca80b36f5429eba9071d1a13f11530a1d9c38a9b0.vsn#L5>)
- `V0870740e8182164137af` / `O84dc975ecaaa70ec5246` · `vsn/f_ClassicStarkillV3/script.vsn:37` · [catalog位置](<../../../catalog/occurrences.jsonl#L7531>) · [当前原文:37](<../../../sources/blobs/e9a9d407b5f4b2ca3d14b73ca80b36f5429eba9071d1a13f11530a1d9c38a9b0.vsn#L37>)

### W20 · 气密装备
SqueakerBoss后取回Cosmohelm，还需Cosmosuit配齐气密套装；一件头盔不等于已能太空行走。
- 已证实；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**SqueakerBoss后**。
- `V80479a61bdb981bdaa98` / `O7188e11ab7cd06c3e395` · `vsn/m_ClassicSqueakerBoss/script.vsn:12` · [catalog位置](<../../../catalog/occurrences.jsonl#L8695>) · [当前原文:12](<../../../sources/blobs/21645f1219dc510e550cadc33679ec16bfdc934df3c936bd79b815f3c0d066f0.vsn#L12>)
- `V0aa16be204f4dd5b153f` / `Oe5f0ee057ad8e11e594a` · `vsn/m_ClassicSqueakerBoss/script.vsn:22` · [catalog位置](<../../../catalog/occurrences.jsonl#L8702>) · [当前原文:22](<../../../sources/blobs/21645f1219dc510e550cadc33679ec16bfdc934df3c936bd79b815f3c0d066f0.vsn#L22>)

### H01 · Fenfen史
Fenfen记忆说本族长期住Tutone、避免主角文明式技术、由智慧Esper议会处理争端。和平社会是本族自述，非所有个体绝对善良。
- 单方说辞（记忆传递）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**对应Fenfen记忆可理解后**。
- `V340e5be183a58363ed99` / `O591263fb1aaeb32d2640` · `vsn/f_AgentFZ1/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L7174>) · [当前原文:5](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L5>)
- `V8c793751eb4c59dd23ed` / `Oc85892a707445187e050` · `vsn/f_AgentFZ1/script.vsn:25` · [catalog位置](<../../../catalog/occurrences.jsonl#L7184>) · [当前原文:25](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L25>)

### H02 · Traeh史
Traeh原为杰出Esper，获准接触历代储能后吸收/腐化而深层畸变；不是简单外星女王最初入侵。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z1**。
- `V3e4b26d559a0f078b20a` / `O9937a948d85746468013` · `vsn/f_AgentFZ1/script.vsn:29` · [catalog位置](<../../../catalog/occurrences.jsonl#L7185>) · [当前原文:29](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L29>)
- `V1cd6d701001d75c6a989` / `Ofc8881c2290b7de859db` · `vsn/f_AgentFZ1/script.vsn:50` · [catalog位置](<../../../catalog/occurrences.jsonl#L7198>) · [当前原文:50](<../../../sources/blobs/9fada4a493eab776c31660d2b866f698d39c8ee55ac555a406026575434568ec.vsn#L50>)

### H03 · 战争史
Traeh攻击议会，生物似响应其呼唤，征服奴役Fenfen；哭喊似助长其力量，不编精确吸收公式。
- 单方说辞/推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z2**。
- `V4dda0eff99679a5b22e4` / `O64c282165c424cfd7ad6` · `vsn/f_AgentFZ2/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L7204>) · [当前原文:11](<../../../sources/blobs/b5b3dd8bf2f495f52d1acb58265ff7846919315893d76c989b05f56592ae192a.vsn#L11>)
- `V72d63bc2f10926968705` / `O2d76260a8b221350040d` · `vsn/f_AgentFZ2/script.vsn:45` · [catalog位置](<../../../catalog/occurrences.jsonl#L7222>) · [当前原文:45](<../../../sources/blobs/b5b3dd8bf2f495f52d1acb58265ff7846919315893d76c989b05f56592ae192a.vsn#L45>)

### H04 · 能力史
Fenfen将精神弹、念动力、身体变形军用化；精灵援助，地底另一些古老存在有独立复仇/支配欲，不把所有存在合并女王部下。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z3**。
- `Vc435b13cff17293a78b5` / `O22dc7561e3ae3310e13a` · `vsn/f_AgentFZ3/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L7226>) · [当前原文:11](<../../../sources/blobs/f1600c23d547d7d9923c63ea00b45e453633e89c153c29761382365fb80f549c.vsn#L11>)
- `Vdc37b119b938bad01293` / `O2c6e88d327c3145d1047` · `vsn/f_AgentFZ3/script.vsn:43` · [catalog位置](<../../../catalog/occurrences.jsonl#L7241>) · [当前原文:43](<../../../sources/blobs/f1600c23d547d7d9923c63ea00b45e453633e89c153c29761382365fb80f549c.vsn#L43>)

### H05 · 封印史
战争多年；议会趁精神弱点以水晶囚禁Traeh，不能将其终结；残党仍囚Fenfen，不等于战后全恢复。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z4**。
- `Vd1a1c68b557da460653b` / `Ofbcc37bb5456f4661f5d` · `vsn/f_AgentFZ4/script.vsn:12` · [catalog位置](<../../../catalog/occurrences.jsonl#L7245>) · [当前原文:12](<../../../sources/blobs/7b0456d0e169ff913218d0d99a74d837fec61d0f58a223e1c02c052fa0104eaf.vsn#L12>)
- `V94a69df7f6d2ca298ba5` / `O7afcfdc93f1882ec5380` · `vsn/f_AgentFZ4/script.vsn:46` · [catalog位置](<../../../catalog/occurrences.jsonl#L7264>) · [当前原文:46](<../../../sources/blobs/7b0456d0e169ff913218d0d99a74d837fec61d0f58a223e1c02c052fa0104eaf.vsn#L46>)

### H06 · 受控史
星际访客落在监牢卫星岩体，触水晶受控。叙述者明确不知道接近出于好奇还是黑暗力量，不替其终裁动机。
- 单方说辞；动机未定；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z5**。
- `V335e9be4b47622a55c98` / `Oe3f4e96c21e036dba02c` · `vsn/f_AgentFZ5/script.vsn:12` · [catalog位置](<../../../catalog/occurrences.jsonl#L7268>) · [当前原文:12](<../../../sources/blobs/68425b9e3802775934fa8f97bc9d485c5b169ae49d39749589db0c30eb5b79ec.vsn#L12>)
- `V53a1a40f684c7780301a` / `Ofd9ced8703115dfa01c1` · `vsn/f_AgentFZ5/script.vsn:42` · [catalog位置](<../../../catalog/occurrences.jsonl#L7283>) · [当前原文:42](<../../../sources/blobs/68425b9e3802775934fa8f97bc9d485c5b169ae49d39749589db0c30eb5b79ec.vsn#L42>)

### H07 · 危机
受控者逐个捕获议员、封印减弱；Traeh等足够力量换新宿主。命运英雄/玩家成为宿主均是劝导或可能，不是已经发生。
- 单方说辞/未来推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**记忆Z6**。
- `Va0221f64944d5ae004ac` / `O988c4690d9c2202c7c26` · `vsn/f_AgentFZ6/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L7287>) · [当前原文:11](<../../../sources/blobs/0181dc2867c742fb5d24f81ec0e1bac3f5a6524f58843fda9bb23ff0e73d098b.vsn#L11>)
- `Vb9742341654fb562dc06` / `Oc2145dd928d40f4b0324` · `vsn/f_AgentFZ6/script.vsn:47` · [catalog位置](<../../../catalog/occurrences.jsonl#L7305>) · [当前原文:47](<../../../sources/blobs/0181dc2867c742fb5d24f81ec0e1bac3f5a6524f58843fda9bb23ff0e73d098b.vsn#L47>)

### E01 · 坏结局
船修不足无法追上Traeh；角色只希望其不恢复能量，女线问至少救了Tutone。不能写成银河已保证安全，也非全员死亡。
- 已证实（分支）；推测（安全）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**EndingBad**。
- `V126d0d503b538ef17c1b` / `Oa47d9ac8ada602e4dac6` · `vsn/f_EndingBad/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L7660>) · [当前原文:5](<../../../sources/blobs/62faadbba3848232f0ecba4e76e07bc0c6c68ed1cf72e3c09e8dfa130e730261.vsn#L5>)
- `V638d4d2afc2bd4c83fd8` / `Of84dd25713b73aa4cb93` · `vsn/f_EndingBad/script.vsn:25` · [catalog位置](<../../../catalog/occurrences.jsonl#L7672>) · [当前原文:25](<../../../sources/blobs/62faadbba3848232f0ecba4e76e07bc0c6c68ed1cf72e3c09e8dfa130e730261.vsn#L25>)

### E02 · 好结局
Traeh败、精神异常停止、部下逃走；兄姐弟救星球并由总部庆祝报告。与坏结局是替代路线，不是连续章节。
- 已证实（结局报告）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**EndingGood**。
- `V1b62e7e2440de935ca20` / `O6825b01ad3488536b4d1` · `vsn/m_EndingGood/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L8874>) · [当前原文:5](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L5>)
- `V1f422217877d0e1a1372` / `O014c38c7ec9610db4cad` · `vsn/m_EndingGood/script.vsn:61` · [catalog位置](<../../../catalog/occurrences.jsonl#L8907>) · [当前原文:61](<../../../sources/blobs/c5ca1505377714e88f9b63266ceda6fa99710bc80d69db44b1750d13287c7309.vsn#L61>)

### E03 · 追击
EndingIntoShmup是涡轮/武装准备后的追击入口，目录Bad/Good/IntoShmup字母顺序不等于先坏后好再追击；确切触发条件另核。
- 已证实（文本作用）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**追击入口**。
- `V4214eba657260234a04a` / `O328b279d970b4b7a8b01` · `vsn/m_EndingIntoShmup/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L8911>) · [当前原文:11](<../../../sources/blobs/2dac326179e20019a213f510ad6e8a65990ff032fa52dfe88015507d606c548f.vsn#L11>)
- `V3c624d8d5ba0d1c22310` / `Of8969aca8ab2f9f327a3` · `vsn/m_EndingIntoShmup/script.vsn:13` · [catalog位置](<../../../catalog/occurrences.jsonl#L8913>) · [当前原文:13](<../../../sources/blobs/2dac326179e20019a213f510ad6e8a65990ff032fa52dfe88015507d606c548f.vsn#L13>)

### E04 · 失败A
原作EDITOR’S NOTE说Flayer抽心智、另种触手取能，两者似共生；恢复心智是PPP希望，非已救回。编辑注是叙事框架而非翻译备注。
- 单方说辞（报告编辑）/推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**AreaA失败**。
- `V5b2be15bc92522ad4ce7` / `O0e8aec9197dd0ec98617` · `vsn/m_GameOverAreaA/script.vsn:93` · [catalog位置](<../../../catalog/occurrences.jsonl#L9002>) · [当前原文:93](<../../../sources/blobs/fcb1c4f6824f86c2676cc22aabad97631b15f7358203cfe0ac839575b9f368e8.vsn#L93>)
- `V2e6e02356878853ba464` / `O2977053ba936be407e02` · `vsn/m_GameOverAreaA/script.vsn:118` · [catalog位置](<../../../catalog/occurrences.jsonl#L9017>) · [当前原文:118](<../../../sources/blobs/fcb1c4f6824f86c2676cc22aabad97631b15f7358203cfe0ac839575b9f368e8.vsn#L118>)

### E05 · 失败B
男线先Kobold囚留、拍卖再Barker，女线先Barker后奴贩囚留；两版有当地大耳生物救援/撤回，不凭外观强补姓名。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**AreaB失败**。
- `Veb51976821f7f63252df` / `Oc570ca9cfd9b3473f474` · `vsn/m_GameOverAreaB/script.vsn:19` · [catalog位置](<../../../catalog/occurrences.jsonl#L9025>) · [当前原文:19](<../../../sources/blobs/a882533e6ead274a011a776dafa34c373456e9adf3641497129bffd23262f8e9.vsn#L19>)
- `V2879271da0c378ffca73` / `O789d6e8453122adc2b2b` · `vsn/m_GameOverAreaB/script.vsn:105` · [catalog位置](<../../../catalog/occurrences.jsonl#L9076>) · [当前原文:105](<../../../sources/blobs/a882533e6ead274a011a776dafa34c373456e9adf3641497129bffd23262f8e9.vsn#L105>)

### E06 · 失败C
Gobin圈养→逃脱→精灵温泉驯化→效忠Enelye；水或PSY是主角猜测，不定具体机制。效忠不证明Enelye客观正义。
- 单方说辞/推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**AreaC失败**。
- `Vebe92d4eed3128235ad2` / `O2e564fbc64811b075cee` · `vsn/m_GameOverAreaC/script.vsn:18` · [catalog位置](<../../../catalog/occurrences.jsonl#L9083>) · [当前原文:18](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L18>)
- `V9d5576530406eeda841c` / `O8b9529096d318227e59e` · `vsn/m_GameOverAreaC/script.vsn:105` · [catalog位置](<../../../catalog/occurrences.jsonl#L9136>) · [当前原文:105](<../../../sources/blobs/7c961fb7c04822004e212d30b125d4886a1f91044b13038fc116001d9dc0d7c6.vsn#L105>)

### E07 · 失败E/天体
Exile明确为绕Tutone小行星；未归者不大可能生还，但没有遗体、命运不明。moon是剧情俗称，不另造天体；不写确认死亡。
- 单方说辞（报告）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**AreaE失败**。
- `V787512b9ff4f80145c2e` / `Oc4e1b1dbb4e988aa7119` · `vsn/m_GameOverAreaE/script.vsn:5` · [catalog位置](<../../../catalog/occurrences.jsonl#L9137>) · [当前原文:5](<../../../sources/blobs/48984a988d04b74ef7de5c943ae9e61b86019152460171fba89c61003d6274da.vsn#L5>)
- `V0590bb5431e2737c6ade` / `O67df409ad2717d103b2f` · `vsn/m_GameOverAreaE/script.vsn:15` · [catalog位置](<../../../catalog/occurrences.jsonl#L9143>) · [当前原文:15](<../../../sources/blobs/48984a988d04b74ef7de5c943ae9e61b86019152460171fba89c61003d6274da.vsn#L15>)

### R01 · 报告可靠性
F01只是I think对方试图令其受孕，不是已产幼犬；后来投入不能抹除最初无力反抗。
- 单方说辞；受孕推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**F01获救报告**。
- `Vdb90579d41254a8f0a50` / `Ob77f37a1bc312289b6c9` · `vsn/f_AgentF01/script.vsn:18` · [catalog位置](<../../../catalog/occurrences.jsonl#L6802>) · [当前原文:18](<../../../sources/blobs/011d9333e6e863d1dd1c2e571e50521128d300cd7c40988588aa8fd9c8e4bec4.vsn#L18>)
- `Ve34b7394e987ad8010c6` / `O38250d28667af2301861` · `vsn/f_AgentF01/script.vsn:73` · [catalog位置](<../../../catalog/occurrences.jsonl#L6833>) · [当前原文:73](<../../../sources/blobs/011d9333e6e863d1dd1c2e571e50521128d300cd7c40988588aa8fd9c8e4bec4.vsn#L73>)

### R02 · 报告可靠性
Erma以为Daleir在帮助自己；Daleir口误暴露诱导嫌疑。她将挣扎称foreplay/natural，不可客观改写Erma自愿。
- 单方说辞（矛盾视角）；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**F05与F06对读**。
- `Vfd407e62f0d4f201e7dc` / `Oe3ad7a379fb99ca55e45` · `vsn/f_AgentF06/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L7004>) · [当前原文:11](<../../../sources/blobs/efb300787c67687ce77d16c287b7979a5a0acf090f819f3a95a8a3b7edceab0f.vsn#L11>)
- `Vc0bc6a390a382fed3bf5` / `O445f74c841728ae37a7e` · `vsn/f_AgentF06/script.vsn:71` · [catalog位置](<../../../catalog/occurrences.jsonl#L7040>) · [当前原文:71](<../../../sources/blobs/efb300787c67687ce77d16c287b7979a5a0acf090f819f3a95a8a3b7edceab0f.vsn#L71>)

### R03 · 报告可靠性
F07 You would think I pulled out my lighttazer是比喻对方惊慌，不是实际掏枪击晕；她自戴脚镣并领薪休闲。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**F07报告**。
- `Vde585c0544552a90a9ea` / `Ofd2908d86c3c2c28fd59` · `vsn/f_AgentF07/script.vsn:19` · [catalog位置](<../../../catalog/occurrences.jsonl#L7065>) · [当前原文:19](<../../../sources/blobs/781ebf12d26890caa73e04effa84e7194724412257fa1231364c84c0dc6156ad.vsn#L19>)
- `V7e5e2f46b66cc5fb794a` / `Oa63c73a6068a305c8639` · `vsn/f_AgentF07/script.vsn:75` · [catalog位置](<../../../catalog/occurrences.jsonl#L7100>) · [当前原文:75](<../../../sources/blobs/781ebf12d26890caa73e04effa84e7194724412257fa1231364c84c0dc6156ad.vsn#L75>)

### R04 · 报告可靠性
F08自封海盗女王Vickers是幻想，不是Traeh身份；沉默探员未看清，不靠后文擅自点名Starkill。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**F08报告**。
- `V9ec2d936ab267e87c766` / `O5e09ee818be546b7254b` · `vsn/f_AgentF08/script.vsn:46` · [catalog位置](<../../../catalog/occurrences.jsonl#L7124>) · [当前原文:46](<../../../sources/blobs/125a52a5276ae17c0d9a12e6229f20d9978f802fa8b92fe25f30efb7e8e159aa.vsn#L46>)
- `Ve004c737f8f19862f334` / `Oe8c7856fe8d87bc12913` · `vsn/f_AgentF08/script.vsn:84` · [catalog位置](<../../../catalog/occurrences.jsonl#L7147>) · [当前原文:84](<../../../sources/blobs/125a52a5276ae17c0d9a12e6229f20d9978f802fa8b92fe25f30efb7e8e159aa.vsn#L84>)

### R05 · 报告可靠性
M02 Top自夸与受制反讽并存，声称别人男性会高潮而自己不；Top同时是优越感/性角色双关，不当客观军衔。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**M02报告**。
- `Va74c93d39852456ec8d3` / `Ob4a45eaf7d8711381215` · `vsn/m_AgentM02/script.vsn:11` · [catalog位置](<../../../catalog/occurrences.jsonl#L8014>) · [当前原文:11](<../../../sources/blobs/48f30c9acb970e1fe9e6840b49c094c9ef34896787dfc0b29a8b89ca4ddc71dc.vsn#L11>)
- `Vac8c14c8a0c7ea007fe0` / `O6b970313efbdabd02e13` · `vsn/m_AgentM02/script.vsn:77` · [catalog位置](<../../../catalog/occurrences.jsonl#L8055>) · [当前原文:77](<../../../sources/blobs/48f30c9acb970e1fe9e6840b49c094c9ef34896787dfc0b29a8b89ca4ddc71dc.vsn#L77>)

### R06 · 报告可靠性
M04自称压倒矮人却记忆模糊、渴望good boy；不替角色圆谎成真实胜利。
- 单方说辞；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**M04报告**。
- `V3c4d47340fea21023e9b` / `O48edb39c13f2ea6f5ffa` · `vsn/m_AgentM04/script.vsn:12` · [catalog位置](<../../../catalog/occurrences.jsonl#L8100>) · [当前原文:12](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L12>)
- `Vf9d00a6ebaf77c1106f2` / `Oa27ea73cca8fc7422640` · `vsn/m_AgentM04/script.vsn:90` · [catalog位置](<../../../catalog/occurrences.jsonl#L8145>) · [当前原文:90](<../../../sources/blobs/1f962bc8687b45d38cbd1442dc2931ce1b6e9d9bda336faa4d1edcc79e420ae9.vsn#L90>)

### R07 · 报告可靠性
M08 F.A.P.-like jewel与M0B蓝光物均为体验/猜测，不能直接等同宠物棱晶或Traeh黑暗能量；M0B捕获者性别亦推测。
- 单方说辞/推测；可信度：高（文字与来源定位）；不保证角色主张客观为真；揭示门槛：**M08/M0B报告**。
- `Va862c5d2a8065618090e` / `O1cff8b76e0c68708b441` · `vsn/m_AgentM08/script.vsn:77` · [catalog位置](<../../../catalog/occurrences.jsonl#L8333>) · [当前原文:77](<../../../sources/blobs/da613c182df43fac842cbb0498f928404f02964b000e0765aad941f721a7cecd.vsn#L77>)
- `Vd8ae0d592645c5d42e51` / `O7065e1a1163d2e66f146` · `vsn/m_AgentM08/script.vsn:94` · [catalog位置](<../../../catalog/occurrences.jsonl#L8344>) · [当前原文:94](<../../../sources/blobs/da613c182df43fac842cbb0498f928404f02964b000e0765aad941f721a7cecd.vsn#L94>)

### D01 · 机械分类
Spiker是机械仿体，Bumper为失控巡逻机器人，不是虫兽/撞击兽；自修炮弹是塑化金属。三类炮台（制式地面炮、海盗自修炮、失控天花炮）不得混称同一型号。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `De933955b20dc64b1a22d` / `Oc2b7948077102e9eef2f` · `datadm/all.ds:2768` · [catalog位置](<../../../catalog/occurrences.jsonl#L4082>) · [当前原文:2768](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2768>)
- `Db0a297f91f81a7acd6b2` / `O5c16b1751bb1060a1d70` · `datadm/all.ds:2868` · [catalog位置](<../../../catalog/occurrences.jsonl#L4164>) · [当前原文:2868](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2868>)

### D02 · Fenfen分类
投石不回应的是Fenfen机械复制体；总部当时没有遇到血肉原生型，不等于灭绝或游戏未给设定。Come in是无线电呼叫并被荤梗接话，不是走进总部。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D9fce9d54f3d94ad4e6a5` / `O93747cb50f2482f26380` · `datadm/all.ds:3124` · [catalog位置](<../../../catalog/occurrences.jsonl#L4376>) · [当前原文:3124](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3124>)
- `D1ad1f0199fae9cf16b48` / `O429870245653e6c57714` · `datadm/all.ds:3137` · [catalog位置](<../../../catalog/occurrences.jsonl#L4389>) · [当前原文:3137](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3137>)

### D03 · 科技
旧太空站机器人有纳米机械回收可无尽自修，过时后难拆；保留科幻技术语，不套WoC禁现代词。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Dae3c593ea275d0db400d` / `Ocdcbf1db74a509c2b16c` · `datadm/all.ds:3140` · [catalog位置](<../../../catalog/occurrences.jsonl#L4390>) · [当前原文:3140](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3140>)
- `Db37cabfd70b571c0c5c2` / `O59eab8bdcaaecbd66c8a` · `datadm/all.ds:3157` · [catalog位置](<../../../catalog/occurrences.jsonl#L4407>) · [当前原文:3157](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3157>)

### D04 · 精灵
Bossu说Sceafya精灵全女性、与各物种雄性交配后渐具凡俗特征，并非全部不朽；保留as far as we can tell。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D5b2a0ded65b05a8c4a4b` / `O0941d5049655f792da9c` · `datadm/all.ds:3208` · [catalog位置](<../../../catalog/occurrences.jsonl#L4449>) · [当前原文:3208](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3208>)
- `D19a92a0d298c43889bd7` / `O6fda860e5fad296df668` · `datadm/all.ds:3219` · [catalog位置](<../../../catalog/occurrences.jsonl#L4460>) · [当前原文:3219](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3219>)

### D05 · 生物链
Hopper/Ghoster是暂名；Hopper受能量影响为推测，变Bullfrog是reports；Thorner是Viner演化形，Tribulb是更凶Bulber。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Dc666dbc85660a3be0667` / `O6a441ed4e465d53414e1` · `datadm/all.ds:3227` · [catalog位置](<../../../catalog/occurrences.jsonl#L4464>) · [当前原文:3227](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3227>)
- `D354b8575406af4893f89` / `Oc1e29058d884edf3ce2e` · `datadm/all.ds:3329` · [catalog位置](<../../../catalog/occurrences.jsonl#L4542>) · [当前原文:3329](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3329>)

### D06 · 异常
Jellyfish是报告中的精神动荡幻象；Ghoster似精神显现；Xeno不属总部已知生态且疑寻卵宿主。未知不是不存在。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Db8de9edef242b9e4a21a` / `Oe221133b4ddccf9c0f90` · `datadm/all.ds:3194` · [catalog位置](<../../../catalog/occurrences.jsonl#L4436>) · [当前原文:3194](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3194>)
- `Daaa319ff3e680cdaead4` / `O296ff6089295b06a321e` · `datadm/all.ds:3365` · [catalog位置](<../../../catalog/occurrences.jsonl#L4571>) · [当前原文:3365](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3365>)

### D07 · 图鉴反证
Spikeball不可摧毁是Bossu基于记录的断言，紧接被主角质疑/作弊笑话，非无条件系统定理；Bigbold图鉴后来称不同个体，物种不等于唯一专名角色。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D8c8b20a77d3d6a2c95e9` / `Of339f5abe9ca663acf16` · `datadm/all.ds:2913` · [catalog位置](<../../../catalog/occurrences.jsonl#L4199>) · [当前原文:2913](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2913>)
- `D6fbcacad9713522c04fa` / `Od87b7b5fc1919f998e3a` · `datadm/all.ds:2985` · [catalog位置](<../../../catalog/occurrences.jsonl#L4263>) · [当前原文:2985](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L2985>)

### I01 · 食物
骨头/鸡腿明确少量VIT；茶安神清脑；StatCherry对白是berries不必强称樱桃，StatFortune不凭键补幸运效果。maybe/I bet保留猜测。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Dd5a9e59ee559eafa445f` / `O71965802a40e771e1466` · `datadm/all.ds:3861` · [catalog位置](<../../../catalog/occurrences.jsonl#L4837>) · [当前原文:3861](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3861>)
- `D0398ca0991ce2fa4cffe` / `O19ae2247083eef5ae486` · `datadm/all.ds:3907` · [catalog位置](<../../../catalog/occurrences.jsonl#L4873>) · [当前原文:3907](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L3907>)

### I02 · 食物
Hardnut女线明确提高防御；男线仅崩牙/私密笑话，不跨线强补。奶酪、浆果、瓜、蝌蚪效果多为推测而非数值实测。
- 单方说辞/推测；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应物品获得后**。
- `Dea192348642b3d3100be` / `O64f6fcf48b0e7f925577` · `datadf/all.ds:3872` · [catalog位置](<../../../catalog/occurrences.jsonl#L1930>) · [当前原文:3872](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3872>)
- `D8b7715ecae3692a88a31` / `Oc148e61e10103ad072af` · `datadf/all.ds:3950` · [catalog位置](<../../../catalog/occurrences.jsonl#L1990>) · [当前原文:3950](<../../../sources/blobs/66d08528bbeb2090451c82758e40b7cc3805f161a38113f2722bd2ba8920ecca.ds#L3950>)

### I03 · 武器
Trainee是新人弱化武器；Trainer Tazer对特定怪物打最后一击送机库，两个词不能混同；lighttazer未证为电磁枪。
- 已证实（系统说明）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Dbbd7a6f007c51f7e62bc` / `Oc9bf7affe4d123a5be51` · `datadm/all.ds:4087` · [catalog位置](<../../../catalog/occurrences.jsonl#L4997>) · [当前原文:4087](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4087>)
- `D68aa1de1bb8dfd07d642` / `Oe85eaa3f722d3c7ae523` · `datadm/all.ds:4099` · [catalog位置](<../../../catalog/occurrences.jsonl#L5007>) · [当前原文:4099](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4099>)

### I04 · 移动/防御
护环冲刺、踝环贴墙再跳、鞋空中下+跳俯冲反弹、Cosmo ID接入旧3P传送垫；圆盾蹲下挡小弹、攻击需放下。
- 已证实（物品说明）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D8b665c4f3efaac4503f6` / `O33af25802cb3ff14b519` · `datadm/all.ds:4342` · [catalog位置](<../../../catalog/occurrences.jsonl#L5177>) · [当前原文:4342](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4342>)
- `D9f2c466d9a67b32927a6` / `Oc3b4684289fc6671a773` · `datadm/all.ds:4429` · [catalog位置](<../../../catalog/occurrences.jsonl#L5248>) · [当前原文:4429](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4429>)

### I05 · 语言/充能
项链可懂Fenfen语并建议复看既有日志；记录顺序不等于理解顺序。torch/flashlight同一手电自动照暗；F.A.P.为Jakov’s Obscura/Field Attenuated Prism，抚摸高亲和生物充能，效果依物种。
- 已证实（物品说明）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D723fb8eba708ff0e331d` / `O4b6a4374e037fc658e57` · `datadm/all.ds:4432` · [catalog位置](<../../../catalog/occurrences.jsonl#L5249>) · [当前原文:4432](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4432>)
- `Dc2706e0d26130d1c2b59` / `O83a8755f819de56f23ac` · `datadm/all.ds:4470` · [catalog位置](<../../../catalog/occurrences.jsonl#L5279>) · [当前原文:4470](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4470>)

### I06 · Zener
近场看不见球体但生命读数会变；SELECT选能力，上+攻击发动；圆形段是另一探员能量球报告，不凭entry把形状直接当已测技能表。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D1e4ba99d5eb82af6da29` / `Oc7b903c046595a6b2416` · `datadm/all.ds:4475` · [catalog位置](<../../../catalog/occurrences.jsonl#L5280>) · [当前原文:4475](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4475>)
- `De52e9f4e6ca103b2fd43` / `O6025fc0ed4478d0f83a1` · `datadm/all.ds:4504` · [catalog位置](<../../../catalog/occurrences.jsonl#L5305>) · [当前原文:4504](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4504>)

### I07 · 取舍
十字增强攻击却承受更重伤害；三角更坚韧却打出更小伤害；保留角色might/feeling，不编倍率。
- 单方说辞/体验推测；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `Dc93c0b9cb62c795dde0e` / `O69adf15a43b171b87373` · `datadm/all.ds:4532` · [catalog位置](<../../../catalog/occurrences.jsonl#L5329>) · [当前原文:4532](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4532>)
- `D1983be56a3624b9efe37` / `Ofebffd735536dad5e505` · `datadm/all.ds:4546` · [catalog位置](<../../../catalog/occurrences.jsonl#L5341>) · [当前原文:4546](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4546>)

### I08 · 未测物品
PsyUp增强潜在精神力是当地人声称，总部无测量法；升级芯片本通话只知近装备有反应，不提前灌升级商功能。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D8cabb826d2cd1944988e` / `Odec75a48721193eacce7` · `datadm/all.ds:4569` · [catalog位置](<../../../catalog/occurrences.jsonl#L5358>) · [当前原文:4569](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4569>)
- `D9c3a882196237013e5d8` / `O2525fd37432127390787` · `datadm/all.ds:4587` · [catalog位置](<../../../catalog/occurrences.jsonl#L5374>) · [当前原文:4587](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4587>)

### I09 · 科技/法律
Statcoin为非法biocrypto，USL明确Universal Scripting Language，可在P.A.W.运行；Mauser称Omega Protocol绝密任务授权超正常法律，属角色法律口径，不造3P宪制。
- 单方说辞（总部阶段性知识）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D25c06edf2a8c203d1fdd` / `O1bb1392ddd0081a65977` · `datadm/all.ds:4590` · [catalog位置](<../../../catalog/occurrences.jsonl#L5375>) · [当前原文:4590](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4590>)
- `D90387b195df95df4e943` / `Oe9885a7e1e66fa9ea69d` · `datadm/all.ds:4617` · [catalog位置](<../../../catalog/occurrences.jsonl#L5402>) · [当前原文:4617](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4617>)

### I10 · 资料卡/分工
Map disk是勘测地图；CosmoCard是敌方能力/掉落与成人背面，不是开门keycard；Tomcat非重型机械专家，修船应找受雇机库机械师。
- 已证实（物品说明）；可信度：高（文字/定位）；非角色主张必真；揭示门槛：**对应遭遇/物品获得后**。
- `D73388e47212e1c666dc3` / `O27accfac95100145c8c5` · `datadm/all.ds:4622` · [catalog位置](<../../../catalog/occurrences.jsonl#L5403>) · [当前原文:4622](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4622>)
- `Db839109f7a807498ae58` / `O3b2678714dde81f6dc5a` · `datadm/all.ds:4724` · [catalog位置](<../../../catalog/occurrences.jsonl#L5478>) · [当前原文:4724](<../../../sources/blobs/1672b5dd05ef370162fcea4e39ad4dd03c16221513c676fd90da0264dc5f4b1e.ds#L4724>)

## 英式用法、双关与语域

- **torch/flashlight**是英美用法差异，同一手电不是火把；Bossu用词引起小吐槽按功能重写。
- **mine/miner/mine、depot/despot、meat/meet、purr/pervert、ruff/rough、bone/boner、come/cum/come in、get off/beat off、sleepy head**等保留“冷笑话→误解/接梗→吐槽”节拍；不逐词硬凑。come in主功能仍是无线电呼叫。
- **Top/bottom Agent**按职位优越感、成人角色自称、同事挖苦分别处理，不设全局固定攻受/军衔。
- **Daleir/Erma与自夸探员**有不可靠叙述；后续快感/身体反应不能追溯改变最初同意状态；不替角色圆谎。
- **纳米机械、卫星、FTL、生物识别、赛博复制、USL、P.A.W.、biocrypto**均为本作科幻语汇。不得套WoC/其他作品“禁现代词”或全古风规则；Pigobin古语仅属人物口吻。
- **F.A.P.**技术全称与成人缩写、Jakov’s Obscura命名趣味分层；棱晶、F.A.P.-like jewel、Traeh黑暗能量不能无证合一。
- [术语提案](<terms-proposals.tsv>)按语境绑定，不是英文词全局替换表。所有final_decision留空，暂译和终裁严格分离。

## 后续验收边界

- 主控完成DS男女粗校全文补证，核无线电身份门槛、商店条件和施受关系。
- 按JAR/PAK自身完整英文对照内容版；原JAR卡背空白不填PAK成人资料，双版本都不是简单删荤词。
- 精确结局修船判定、全图可达顺序、日志解锁仍需运行时取证；本轮静态文本不可冒称实测。
- 属性倍率和伤害公式另查数据，不从角色玩笑推数值；source键不自动等于玩家可见名。
- XXXX是掩码，失真广播保持残片；EDITOR’S NOTE是原作报告框架，角色含混发音是表演文体，不混作待翻译备注。
