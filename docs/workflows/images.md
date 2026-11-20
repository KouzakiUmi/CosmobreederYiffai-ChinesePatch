# 图像本地化工作流

本项目的图像资产分两条线管理：

## 一、已落地 UI 图集替换（`assets/images/`）

- 清单：[../../assets/images/manifest.json](../../assets/images/manifest.json)
- 资源：79 张覆盖 PNG 与 79 张二值遮罩。遮罩内是实际修改的像素，遮罩外的 RGBA 全为零；仓库不收录作为输入的原图裁片。
- 运行机制：构建器先校验本地图集中原区域的 RGBA 哈希，再按遮罩合成新像素，并验证合成区域的哈希及透明通道。两档各用自己的图集定位和素材。
- 约束：严禁改动掩码外任何非文字像素或透明通道。

## 二、待处理的 4 张独立位图资产（`assets/fixed/*.png`）

以下 4 场位图文本不在文本 TSV 中，需单独走位图本地化。原版参考切片从本地归档提取，不随源码仓库分发：

1. `Ada8d2a93e89e1525cbf1.png`（键位配置标题/手柄与键盘组合提示）
2. `A3ad10e4fc08b09e2bef4.png`（`-SELECT DATA TO VIEW BELOW-` / `SUB MENU BESTIARY`）
3. `Acfb74ff046445762b007.png`（卡牌查看器标题与 `"A" KEY TO FLIP CARD`）
4. `A4b6160b4569cc8b87687.png`（成人限定横幅、L+R / Q+E 键位提示与配置入口）
