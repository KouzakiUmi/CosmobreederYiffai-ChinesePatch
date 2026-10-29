# 无线电人名与图鉴字号修正

## 修正范围

- 无线电头像旁、对白署名、底部联系人使用统一中文显示：毛瑟、汤姆猫、伊法伊、伊法妮、波苏；兼容原游戏的 `YIFANY` 拼写。
- 只改查名后的显示结果与局部字体，内部角色 ID、头像判断、频率、颜色、身份解锁条件不变。隐藏身份仍显示 `??????`，沿用原译文保留代号 `THE0`。
- 图鉴中文列表名称（包括“败北”）使用 classic8，保持原 8px 行距与选择位置。
- 图鉴中文说明从 classic8 改用 default10，按 224px 宽度重新换行，10px 行距、最多三行；保留全文、显式分行、样式与颜色。绘制前先验证整个文本，不截尾。
- 不修改共享字号、图像资产、剧情正文布局、存档或游戏目录。

## 验证

[完整候选测试结果](<../integration/tests/radio-book-04/results.json>)：17 项全部通过，包含实际最终归档加载、无线电四处显示调用及 classic8 字形指标、SFW 33 条与 NSFW 59 条图鉴说明的实际 Kc 绘制、正文、Continue、字幕、结局、字体生命周期和紧凑字段回归。

[独立复核](<independent-review.json>)：仅修改 Kc / JM / JQ / SceneText 并新增 RadioLabels；全部非 class 资源与上一验收候选解密后等价，字体与图集未变。实际 alpha 墨迹检查支持说明 10px / 名称 8px 行距，不以透明字形 padding 误判可见字高。

原差分安装器测试：47 项中 42 项通过，5 项需显式启用的实归档 / EXE / GUI 用例未执行。新版 EXE 的构建自检另见交付包构建报告。

这些是 CPU、字节码及像素 alpha 核验，不是游戏 GPU / CRT / 完整场景裁剪或实际输入验收；未安装到游戏、未启动游戏、未访问存档。

## 重现

以下输出路径必须尚不存在；例子中的新目录名可自行更换。

```sh
python localization/optimization/r28/integration/build_candidate.py --output localization/builds/r28-radio-book-candidate4
python localization/optimization/r28/integration/test_candidate.py --candidate localization/builds/r28-radio-book-candidate4 --output localization/optimization/r28/integration/tests/radio-book-04
```

独立复核须针对新归档和源码实际执行、重新生成报告；不能沿用旧哈希或将旧报告改名冒充新验收。封签会核全部 17 项、源文件 / 证据 / 归档 SHA、父验收及逐条归档等价，继承原有限制。

```sh
python localization/optimization/r28/radio-book/seal_incremental.py --candidate localization/builds/r28-radio-book-candidate4 --tests localization/optimization/r28/integration/tests/radio-book-04 --review localization/optimization/r28/radio-book/independent-review.json
python tools/build_alpha_release.py --target localization/builds/r28-radio-book-candidate4 --output dist/r28-radio-book-fix-20261026 --exe
```

图鉴说明现在依赖完整候选追加后的 default10 字库，验证应使用上述最终归档测试，不以只有 r27 旧字库的孤立夹具替代。

## 使用

完全退出游戏。已有汉化须先用对应旧安装器还原，再用新安装器安装；不支持覆盖旧补丁记录。安装器保持原 SHA 校验、备份 / 还原协议，不能强制覆盖未知来源。
