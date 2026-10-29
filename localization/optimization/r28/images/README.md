# r28 固定位图中文独立候选

**已真实重绘33个逻辑工单、79条目标行；164条按理由保留。不是243条全部已译。** 全部图片只在本staging；未改原工单、r27归档、已部署staging或文本canonical。

## 入口

- [组件/API契约](<component.json>) · [可集成manifest](<manifest.json>) · [逐字锁定候选](<candidates.json>)
- [逐工单及逐帧结果](<workorder-results.json>) · [自动门禁结果](<test-results.json>) · [32张实际目视证据](<visual-review.json>) · [汇总](<verification.json>)
- [纯API](<../../../tools/optimized_images.py>) 返回新RGBA atlas，不写档、不解密、不加密、不部署；调用方负责统一解密/集成/加密。

## 自动验证与真实目视

- 79张新PNG（JAR 41 / PAK 38）及79张精确保护掩码。逐行像素变化77872；按物理atlas别名去重后JAR 40053 / PAK 32881。
- 所有243行的(name,index,ordinal,variant)完整覆盖；源rawRGBA、坐标、尺寸和PNG SHA全部锁定。
- 125个非瓷砖文字块逐字码点、标点、原生字形和完整目标槽像素复核；9类拒绝测试通过。
- **changed-pixels-outside-approved-mask=0，Alpha变化=0**；已在两份真实r27归档解密出的4096×6144 atlas上执行纯API内存贴区，所有164保留行仍精确匹配源hash。未写归档。
- 9张原图联系表覆盖101种不同rawRGBA帧；16张新图黑白双底表、7张三倍逐字对照表（50种文字块）全部实际read_image目视，按hash记录。不是仅自动导出。
- 目视发现Casino保守40px槽含角色斜边，已改为三个精确英文glyph框擦字、30px目标框贴字；角色/箭头/轮盘另有逐字节保护门禁。Gallery底部y207黑框也被排除。

## 字号、语义与保留依据

- 普通标题、操作提示、画廊及Casino教程用许可明确的Fusion Pixel原生12px；必要微标签用原生8px，不缩放字体。源字体SHA在组件中，OFL随候选附带。
- 8px仅用于8/9px高微标、继续栏、更新标、两行19px存档表头、二级9px提示行、商店11px标签，以及tile顶部8px招牌；没有扩大动态槽、命中框、atlas tile或抹除128px分线。
- JAR“回忆/训练/口袋训练”与PAK“图鉴/B.R.E.E.D/口袋B.R.E.E.D.”分开；JAR不添加A翻卡提示、年龄横幅、[R18]或额外帧。
- P.A.W.个人档案终端按本轮审定；B.R.E.E.D、F. DATA、COM%、TELE缩写及地图S/T/?/!编码保留，不擅自展开。UP/DOWN、A/B、L/R、Q/E身份与组合保留；TAB译动作，不改成实体Tab键。
- SHOP按map证据是tile0=SH + tile1=OP，tile1的替代帧是tile2；逐16×16块改“商/店/店”，保留原调色、下半图案与原动画声明。0B没有该动画声明，0F仅见嵌入候选定义，未宣称实机可达。
- Area0_map15的StaticBG2还单独复用tile0：原为SH碎片，现为“商”字；此静态复用明确保留记录，未修改地图。
- 32×8更新标仅亮帧“已更新”，灭帧全黑保持；16×8确认按钮两态“确认”；空开合帧保持，不在原无文字帧补字。

## 逐项清单

|工单|逻辑组|重绘行|保留行|结论|
|---|---|---:|---:|---|
|IMG-001|CardViewMenuBG|2|0|完成重绘|
|IMG-002|CardViewMenuBGTitle|1|1|完成重绘；其余逐帧保留|
|IMG-003|ClassicHUDBreedMenu|2|0|完成重绘|
|IMG-004|ClassicHUDSubBreed|2|0|完成重绘|
|IMG-005|CosmoCodecMenuBG|2|0|完成重绘|
|IMG-006|CosmoItemMenuBG|2|0|完成重绘|
|IMG-007|CosmoMissionLogMenuBG|2|0|完成重绘|
|IMG-008|CosmoSaveMenuBG|2|0|完成重绘|
|IMG-009|CosmoNameEntryMenuBG|2|0|完成重绘|
|IMG-010|CosmoSubData|2|0|完成重绘|
|IMG-011|CosmoSubMapBG|2|0|完成重绘|
|IMG-012|CosmoSubMapV2BG|2|0|完成重绘|
|IMG-013|CosmoTitleData|1|1|完成重绘；其余逐帧保留|
|IMG-014|ClassicPretitleGamepad|1|2|完成重绘；其余逐帧保留|
|IMG-015|CosmoGalleryBG|2|0|完成重绘|
|IMG-016|CosmoGalleryViewerBG|2|0|完成重绘|
|IMG-017|CosmoShopBG|2|0|完成重绘|
|IMG-018|CosmoGameOverBG|2|0|完成重绘|
|IMG-019|CosmoGameOverLiteBG|2|0|完成重绘|
|IMG-020|Observe|6|12|完成重绘；其余逐帧保留|
|IMG-021|SelectItem|6|12|完成重绘；其余逐帧保留|
|IMG-022|SelectProgram|6|12|完成重绘；其余逐帧保留|
|IMG-023|CosmoHUDUpdatedFlagDefault|2|2|完成重绘；其余逐帧保留|
|IMG-024|ClassicNameEntryBoxOKActive|2|0|完成重绘|
|IMG-025|ClassicNameEntryBoxOKInactive|2|0|完成重绘|
|IMG-026|SelectAgentClose|4|12|完成重绘；其余逐帧保留|
|IMG-027|SelectMapClose|4|12|完成重绘；其余逐帧保留|
|IMG-028|ClassicTitlescreenDefault|0|32|保留品牌/版权|
|IMG-029|ClassicTitlescreenTransition|0|58|保留品牌/版权|
|IMG-030|ClassicTileset0|2|0|完成重绘|
|IMG-031|ClassicTileset0A|2|0|完成重绘|
|IMG-032|ClassicTileset0B|2|0|完成重绘|
|IMG-033|ClassicTileset0C|2|0|完成重绘|
|IMG-034|ClassicTileset0F|2|0|完成重绘|
|IMG-035|CollectableSpecialLabel|0|4|受阻：未可靠转录，保留|
|IMG-036|IconSpecialLabelActive|0|2|受阻：未可靠转录，保留|
|IMG-037|IconSpecialLabelInactive|0|2|受阻：未可靠转录，保留|
|IMG-038|CosmoCasino2|2|0|完成重绘|

保留合计：已有中文4行；空开合60行；更新灭帧2行；品牌/版权动画90行；未确认微符号8行。后者对应IMG-035/036/037三工单，仍不能可靠转录，不伪造中文字。品牌两工单按本轮政策保留，不算待译英文失败。

## 集成及复验

```python
from optimized_images import apply_overrides
new_page, report = apply_overrides(decoded_rgba_page, parsed_regions, "jar")
# parsed_regions: name, index, ordinal, xy, size, rotation；另一次使用 "patch"。
# 仅替换manifest列出的region；保留主集成的所有其他页面/条目/代码。
```

```bash
PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/images/test_images.py
```

重跑[重绘工具](<build_images.py>)会将目视状态重新标为待核；不能将既往目视自动授予变化后的图片。新图视觉证据以[目视记录](<visual-review.json>)中的PNG hash为准。

**未覆盖**：工程归档编译/安装/部署、游戏启动、GPU/CRT/窗口缩放、动态clip、输入命中与存档I/O实机验证；不声称已验证这些项目。未使用AI付费图像服务。
