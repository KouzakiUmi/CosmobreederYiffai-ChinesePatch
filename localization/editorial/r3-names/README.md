# R3：全角色人名音义统一

已按“姓名感＋物种／词义双关＋人物气质”完成36项裁决，并应用到两内容版的实际姓名显示中。可核的词义／动物梗尽量保留；不明词源不硬塞动物字，也不把姓名义译当作人物亚种鉴定。

## 查看与使用

- [36项完整新旧对照及理由](<reports/names-01/SUMMARY.md>)、[可筛选TSV](<reports/names-01/names.tsv>)
- [姓名修正版Windows安装器](<../../../dist/r28-character-names-20261026/CosmobreederYiffai-alpha0.1-setup.exe>)、[Python ZIP](<../../../dist/r28-character-names-20261026/CosmobreederYiffai-alpha0.1-python.zip>)
- [安装说明](<../../../dist/r28-character-names-20261026/README.md>)、[差分重建及EXE载荷／许可自检](<../../../dist/r28-character-names-20261026/build-report.json>)

安装器、档位检测和备份还原协议不变。已有旧补丁先用对应旧工具还原原版，不能覆盖未知状态。本轮仅本地构建，未更新远端公开发行，也未安装或访问存档。

## 主要新译名

|原名|本轮采用|规则取舍|
|---|---|---|
|Tomcat|雄猫；原TOM昵称三处为阿雄|保普通词义和电台呼号感，不强加花花公子性格|
|Mauser|毛鼠|近音与已证鼠身份兼顾，保部分毛瑟联想|
|Yiffai / Yiffany|伊吠 / 伊吠妮|同源创译，姓仍伊吠；全名伊吠·伊吠与伊吠妮·伊吠保重复|
|Gepard|猎豹|按名字词义译呼号，角色物种证据仍只记原文已证的猫|
|Chauchat|绍狞|保首音，借已证狞猫补可核chat猫义，明确是中文编辑补偿|
|Buntleen / Komet|邦妮琳 / 彗珂|兔名联想与女名形式；彗星词义与近音|
|Erma / Daleir / Gaoru|艾玛 / 黛蕾 / 高鲁|姓名化、缩减生硬音节，统一正文异形|
|Enelye / Bossu|恩莉耶 / 波苏|保合理既有译名，统一恩内莉／英文署名等混用|

中文创译不是作者官方释名，不宣称一个译名能完整容纳原名每层成人／军武／跨语联想；不因此给角色每句加喵／汪口癖。

## 保护边界

- The0保数字0与原大小写；Traeh／Sevaw／Erauqs保反写原形，不直送几何谜底，不改线索／机制。
- 四个仅证档案标题的Fenfen项目不升级成已证出生名；Bigbold等物种、无名Boss不强起名。
- Macsen／Gitgud当前无可见自报名载体，麦森／季高只是备用显示映射；原JF掩名仍在映射之前，不提前揭名。
- actor ID、脚本键、JSON keys、动态占位符、频率、条件、存档、真实制作／赞助名及英文游戏品牌保持。
- 39条父子称谓保持狼犬／狼崽，1条源有名而现译省略的记录留正文精校判断；本轮不猜补原句。

## 正式来源与证据

- [正式姓名台账](<../../translations/character-names.json>)是当前命名裁决；[精确节点台账](<../../translations/character-name-repairs.jsonl>)是构建输入。旧R1／R2记录保留为历史，不能用旧工作表覆盖本轮。
- [编译预检](<compiled/final-01/manifest.json>)：839个节点、895姓名片段、66资源；R2全部778非姓名修订保持。
- [独立语义审查](<review/names-01.md>)、[载体消费／身份键证据](<review/engineering-01.md>)、[最终归档独立核验](<review/final-review.md>)。
- [13项编译测试原始日志](<review/unit-tests-final.log>)、[昵称三正例／两负例证据](<review/unit-proof-final.json>)、[旧译残留检查](<review/residual-audit-final.json>)。
- [实际候选17项CPU结果](<../../optimization/r28/integration/tests/character-names-final8/results.json>)、[候选封签](<../../builds/r28-character-names-candidate8/acceptance.json>)。

构建在R2后、字体前应用名字层，逐entry核candidate6完整明文SHA，核正式台账／独立裁决／载体证据，再同步36名37别名的无线电映射。中文局部classic8、英文原role，原六字符频率框不变。旧字形墨迹／度量、ASCII记录和非字体原画保持；只允许生产器字体带内位置重排。

## 后续

下一轮系统整段精校应从candidate8的实际中文重新生成快照，人物事实仍参照R1原文证据，显示名以本轮为准。此轮没有宣布全部正文／物种术语已精校完成。

真实GPU／CRT、完整场景层次、输入／装备／全图与已有存档文本缓存尚未验证。未启动游戏、安装或迁移存档；不以CPU／EXE无安装自检冒充实机验收。
