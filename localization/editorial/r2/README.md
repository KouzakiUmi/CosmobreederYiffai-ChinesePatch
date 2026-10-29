# R2：先修一波，再进入系统精校

## 结果

R1 全部 **339 条记录已逐项复审**：291 条应用修订、45 条留置、3 条驳回。291 条含 1 项明确标注的保守局部修正；留置项不冒称已经修好。

- [本轮修订总览](<reports/repair-01/SUMMARY.md>)
- [逐条裁决与实际节点新文](<reports/repair-01/decisions.tsv>)
- [留置和驳回清单](<reports/repair-01/PENDING.md>)

536 个主审节点按已核证版本别名展开，并加上明确的命名撤回，共 778 个真实资源操作。每个操作绑定原归档／entry／资源 SHA／位置和精确旧值，不是把自由段落平均切回英文行。

## Tomcat

正文、字典和无线电头像／对白／联系人显示均撤回“汤姆猫”，保留 Tomcat；原界面大写流程可显示 TOMCAT。未另定“雄猫／公猫”为角色正式名字，不改内部角色标识、频率或隐藏身份条件。

历史 R1 语料与冻结初稿保留，不倒改原证据。当前名字决定见[术语表](<../../review/glossary.csv#L6>)；当前正式修订源见[来源锁定修订台账](<../../translations/editorial-r2-repairs.jsonl>)。

## 当前可用构建

- [Windows 修正版安装器](<../../../dist/r28-editorial-repairs-20261026/CosmobreederYiffai-alpha0.1-setup.exe>)
- [Python ZIP](<../../../dist/r28-editorial-repairs-20261026/CosmobreederYiffai-alpha0.1-python.zip>)
- [安装说明](<../../../dist/r28-editorial-repairs-20261026/README.md>)、[差分重建与EXE自检](<../../../dist/r28-editorial-repairs-20261026/build-report.json>)
- [实际候选验收](<../../builds/r28-editorial-repairs-candidate6/acceptance.json>)

安装器协议、界面和原版源 SHA 校验机制不变。已有旧补丁时先用旧补丁对应工具还原原版，不能覆盖旧状态。此处为本地修正版，不表示已更新远端公开发行。

## 独立复核与证据

- [全部 339 决策及六项退修的语义闭环](<compiled/pass-02/semantic-acceptance.json>)：333 条直接通过，6 条退修后独立定向复核通过。
- [实际最终归档工程核验](<engineering/final-review.md>)：目标文本精确等于台账、非目标明文不漂移、角色 ID／控制不变；旧字形像素及非位置度量保持，ASCII 记录保持。
- [最终CPU回归结果](<../../optimization/r28/integration/tests/editorial-final6/results.json>)：17 步全部 exit 0。106 个双内容版 VSN 测试输入和两份字典再次绑定最终归档。
- [节点合同](<REPAIR_CONTRACT.md>)、[编译与别名展开记录](<compiled/pass-02/manifest.json>)、[六个修正](<corrections/round-01.jsonl>)。

归档中的随机重加密不等于译文变化；字体扩字造成的内部 atlas 坐标重排也不等于旧字形变形。两者均按解密明文／codepoint 裁切像素独立核过。

## 修订源与重建

当前资源顺序是既有冻结初稿／合句／SFW-VSN处理 → 来源锁定的正式R2节点修订 → 最终字库与归档生成。初翻单元库不是本轮修后显示中文的唯一来源；不能只读旧草稿后再提相同问题。

```bash
PYTHONIOENCODING=utf-8 python localization/optimization/r28/integration/build_candidate.py --output localization/builds/新的未存在目录
PYTHONIOENCODING=utf-8 python localization/optimization/r28/integration/test_candidate.py --candidate localization/builds/新的未存在目录 --output localization/optimization/r28/integration/tests/新的未存在目录
```

构建会核正式台账、全量来源预检、独立语义闭环及全部证据 SHA。归档、位置、旧值或来源漂移即拒绝，不降级套用。后续改稿应新建修订版本，不覆盖本轮闭环输入。

## 下一阶段

按[R1方案](<../r1/TRANSLATION_PLAN.md>)继续系统整段精校，以 candidate6 的实际中文重新生成阅读快照，优先特殊双关、源异常与待核用途，再统一处理整段语气和人物声线。本轮未宣布全游戏最终定稿。

未安装、启动游戏或访问存档；真实 GPU／CRT、完整场景层次、输入／IME／装备与全图可达性仍未验证。候选内容验收与安装器构建验证是两个阶段，各自留报告；不以无安装自检冒充真实安装／游戏验收。
