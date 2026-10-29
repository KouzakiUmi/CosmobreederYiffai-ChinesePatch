# 角色名音义统一层

正式来源为[姓名台账](<../../../translations/character-names.json>)和[精确节点操作](<../../../translations/character-name-repairs.jsonl>)。前者包含36项裁决、同源姓氏、昵称及保留原文例外；后者为从已验收candidate6生成的839项操作。

## 构建合同

- 必须走全部前置组件，在R2修订后、最终字库生成前应用。
- 原资源完整SHA必须等于candidate6；昵称TOM只批准三个明确载体。
- 沿用[纯数据引擎](<../../../tools/editorial_repairs.py>)，一资源的全部操作一次预检，原旧值／前缀／EOL／JSON key／占位符／非姓名字符不漂移。
- 编译预检不是语义批准：构建另外核正式台账与独立36项裁决逐名一致、载体用途审查PASS及全部证据SHA。
- 同步[无线电helper](<../../../layout/src/PRG/RadioLabels.java>)及[37别名映射](<../../../editorial/r3-names/generated/radio-names.tsv>)，查名仍在原JF隐藏门控后。中文名局部classic8，英文保原role，六字符频率字段／48px冒号／104px总宽不变。
- 旧字形墨迹和度量、ASCII记录、非字体原画像素必须保持；扩字引起生产器带内坐标重排不等于字形变化。

```bash
python localization/editorial/r3-names/tools/sync_radio_names.py --check
python localization/editorial/r3-names/tools/compile_names.py --registry localization/translations/character-names.json --output localization/editorial/r3-names/compiled/新的未存在目录
```

不修改actor ID、脚本键、剧情控制、存档或公开发行。姓名中文创译不冒称作者官方释名；四个未证为个人名的Fenfen标题、通用物种与真实制作／赞助者不一并改写。具体裁决与实际验收见[R3入口](<../../../editorial/r3-names/README.md>)。
