全库共 **3185 处切词断点**，分布在 **3087 行**（占 10563 行玩家可见中文行的 29.2%）。

> 数据：candidate47（`localization/builds/r9-polish-candidate47`），story12 真实字宽，240px 贪心折行；扫描 `cosmobreeder-multi.jar` 与 `patch.pak` 的 `datadf/1`、`datadm/1`、`vsn/1`–`vsn/200`。生成脚本见文末。

注：扫描时跳过 66 个非文本条目（`vsn/` 中的 PNG 位图，不产生文本行）。

## 总表

| 指标 | 数值 |
| --- | ---: |
| 扫描原始行数 | 85837 |
| 玩家可见中文行数（总行数） | 10563 |
| 含任意断点的行数 | 6675 |
| 断点总数（所有换行点） | 7306 |
| **切词断点数** | **3185** |
| **含切词断点的行数** | **3087（29.2%）** |
| 被切开的不同组合数 | 968 |

## 前 25 个高频被切组合

按切开次数降序（同分按语料频次）；「语料频次」为该二元组在全库玩家可见行中的出现次数。

| # | 组合 | 切开次数 | 语料频次 | 例 1 | 例 2 | 例 3 |
| ---: | --- | ---: | ---: | --- | --- | --- |
| 1 | **它们** | 37 | 546 | `cosmobreeder-multi.jar` `datadf/1`:2767 —  [还好敲上几下好像还能让它\|们停下来……] | `cosmobreeder-multi.jar` `datadf/1`:2778 —  [还好敲上几下好像还能让它\|们停下来……] | `cosmobreeder-multi.jar` `datadf/1`:2789 —  [还好敲上几下好像还能让它\|们停下来……] |
| 2 | **特工** | 28 | 580 | `cosmobreeder-multi.jar` `datadf/1`:1578 — 经很久没在这儿见到你们这种特\|工了，连存货都没顾上补！ | `cosmobreeder-multi.jar` `datadf/1`:2338 —  [我们刚从那边收到一大堆特\|工的求救信标。] | `cosmobreeder-multi.jar` `datadf/1`:2401 — [这片区域里似乎还有另一名特\|工。] |
| 3 | **那些** | 24 | 419 | `cosmobreeder-multi.jar` `datadf/1`:1425 — ，没有反悔这回事！我才不管那\|些卡在你兜里有多让人发麻。 | `cosmobreeder-multi.jar` `datadf/1`:2054 —  [太好了，那我就能去轰掉那\|些该死的飞船——] | `cosmobreeder-multi.jar` `datadf/1`:2764 — [其实并没有人真的接下更换那\|些老旧自卫武器的工作。它们几 |
| 4 | **的生** | 22 | 91 | `cosmobreeder-multi.jar` `datadf/1`:2607 —  [只是碰到他的手，就让你的\|生命体征飙上去了？] | `cosmobreeder-multi.jar` `datadf/1`:3163 — [那些蹦来蹦去、很有攻击性的\|生物……] | `cosmobreeder-multi.jar` `datadf/1`:3220 — [那个异常生物不属于图托恩的\|生态。] |
| 5 | **前所** | 22 | 48 | `cosmobreeder-multi.jar` `datadm/1`:4487 —  [其他特工已经绘制出你目前\|所处区域各个部分的地图，有时 | `cosmobreeder-multi.jar` `datadm/1`:4494 —  [其他特工已经绘制出你目前\|所处区域的各个部分，有时还带 | `cosmobreeder-multi.jar` `datadm/1`:4501 —  [其他特工已经绘制出你目前\|所处区域各个部分的地图，有时 |
| 6 | **我的** | 20 | 321 | `cosmobreeder-multi.jar` `datadf/1`:4527 —  [我看到了！重型装备不是我\|的专长，不过我们在旧机库雇了 | `cosmobreeder-multi.jar` `datadf/1`:4534 —  [我看到了！重型装备不是我\|的专长，不过我们在旧机库雇了 | `cosmobreeder-multi.jar` `datadf/1`:4541 —  [我看到了！重型装备不是我\|的专长，不过我们在旧机库雇了 |
| 7 | **完毕** | 17 | 114 | `cosmobreeder-multi.jar` `datadf/1`:2082 — 当然，28.880。伊吠妮完\|毕！] | `cosmobreeder-multi.jar` `datadf/1`:3286 —  [只好挂断了，“女士”。完\|毕。] | `cosmobreeder-multi.jar` `datadf/1`:3298 —  [只好挂断了，“女士”。完\|毕。] |
| 8 | **力者** | 16 | 90 | `cosmobreeder-multi.jar` `datadf/1`:740 — 实的精神力水晶，跟那些超能力\|者用的一样！ | `cosmobreeder-multi.jar` `datadf/1`:1132 — 实的精神力水晶，跟那些超能力\|者用的一样！ | `cosmobreeder-multi.jar` `datadf/1`:4183 —  [嘿————那也许和超能力\|者有关。] |
| 9 | **扫描** | 16 | 40 | `cosmobreeder-multi.jar` `datadf/1`:3627 — 找到新芯片了吗？让我看看。扫\|描中……] | `cosmobreeder-multi.jar` `datadf/1`:3632 — 找到新芯片了吗？让我看看。扫\|描中……] | `cosmobreeder-multi.jar` `datadf/1`:3652 — 我打赌你能钻进狭窄的地方！扫\|描中……] |
| 10 | **东西** | 15 | 249 | `cosmobreeder-multi.jar` `datadf/1`:2379 — 我附近压根没有半点像植物的东\|西。] | `cosmobreeder-multi.jar` `datadf/1`:3056 — [想想你在障碍训练课上学的东\|西！] | `cosmobreeder-multi.jar` `datadf/1`:4088 —  [听着，我一般不评论这种东\|西，不过……] |
| 11 | **械师** | 15 | 26 | `cosmobreeder-multi.jar` `datadm/1`:4574 — 我们在旧机库请了一位当地机械\|师，他可以给你进一步的建议。 | `cosmobreeder-multi.jar` `datadm/1`:4577 —  [明白了。我会去问那位机械\|师。] | `cosmobreeder-multi.jar` `datadm/1`:4581 — 我们在旧机库请了一位当地机械\|师，他可以给你进一步的建议。 |
| 12 | **把它** | 14 | 114 | `cosmobreeder-multi.jar` `datadf/1`:2536 — [所以先确认一下，没人偷偷把\|它拿走。] | `cosmobreeder-multi.jar` `datadf/1`:4258 —  [伊吠第一次出外勤时，我把\|它传给了他……] | `cosmobreeder-multi.jar` `datadf/1`:4819 — 能提供所需的部件，我就立刻把\|它们打开！ |
| 13 | **样的** | 14 | 73 | `cosmobreeder-multi.jar` `datadf/1`:2578 —  [哦，嘿！终于找到一把像样\|的驯兽电击刃了？] | `cosmobreeder-multi.jar` `datadf/1`:2799 — [他们一定试着在那些各式各样\|的废墟上面盖起一处基地。] | `cosmobreeder-multi.jar` `datadf/1`:2812 — [他们一定试着在那些各式各样\|的废墟上建立一处基地。] |
| 14 | **什么** | 13 | 847 | `cosmobreeder-multi.jar` `datadf/1`:5113 — 近一直不舒服……像是缺了点什\|么。 | `cosmobreeder-multi.jar` `datadm/1`:2187 — : [……你是。怎么了？出什\|么事了？] | `cosmobreeder-multi.jar` `datadm/1`:3986 —  [在外面永远不知道会碰上什\|么。]  |
| 15 | **了一** | 13 | 156 | `cosmobreeder-multi.jar` `datadf/1`:2251 —  [我……是啊，我刚刚经历了\|一些……] | `cosmobreeder-multi.jar` `datadm/1`:2247 —  [我……是啊，我刚刚经历了\|一些……] | `cosmobreeder-multi.jar` `datadm/1`:3354 —  [对，是我。我只是伪装成了\|一只科博德。] |
| 16 | **的地** | 13 | 146 | `cosmobreeder-multi.jar` `datadf/1`:1861 — 接把你送到那个邪恶女王藏身的\|地方，但这艘船没修好之前可飞 | `cosmobreeder-multi.jar` `datadf/1`:3023 — 伙，但它们身上有点非常古怪的\|地方……] | `cosmobreeder-multi.jar` `datadm/1`:1859 — 接把你送到那个邪恶女王藏身的\|地方，但这艘船没修好之前可飞 |
| 17 | **就行** | 13 | 57 | `cosmobreeder-multi.jar` `datadf/1`:1882 — 待在这里，听我一整天聊电脑就\|行！ | `cosmobreeder-multi.jar` `datadf/1`:4063 —  [嘿，只要别在我手里炸掉就\|行！] | `cosmobreeder-multi.jar` `datadf/1`:4788 — 待在这里，听我一整天聊电脑就\|行！ |
| 18 | **在这** | 12 | 178 | `cosmobreeder-multi.jar` `datadf/1`:3089 — [至于该怎么应付它们，我们在\|这边可说不准。] | `cosmobreeder-multi.jar` `datadf/1`:4448 —  [其他特工绘制了你当前所在\|这片区域各部分的地图，有时还 | `cosmobreeder-multi.jar` `datadf/1`:4462 —  [其他特工绘制了你当前所在\|这片区域各部分的地图，有时还 |
| 19 | **还有** | 12 | 144 | `cosmobreeder-multi.jar` `datadf/1`:1885 — 要去哪儿啊，小鸭鸭？！咱们还\|有重构要做呢！ | `cosmobreeder-multi.jar` `datadf/1`:4791 — 要去哪儿啊，小鸭鸭？！咱们还\|有重构要做呢！ | `cosmobreeder-multi.jar` `datadf/1`:5009 — 要去哪儿啊，小鸭鸭？！咱们还\|有重构要做呢！ |
| 20 | **时间** | 12 | 40 | `cosmobreeder-multi.jar` `datadf/1`:3129 — [这些加农炮似乎已经有一段时\|间不需要自行修复了。] | `cosmobreeder-multi.jar` `datadf/1`:3136 — [这些加农炮似乎已经有一段时\|间不需要自行修复了。] | `cosmobreeder-multi.jar` `datadf/1`:3143 — [这些加农炮似乎已经有一段时\|间不需要自行修复了。] |
| 21 | **人机** | 12 | 26 | `cosmobreeder-multi.jar` `datadf/1`:2752 — [特工，小心这一带的飞行无人\|机。] | `cosmobreeder-multi.jar` `datadf/1`:2847 — [小心那些四处巡逻的带刺无人\|机。] | `cosmobreeder-multi.jar` `datadf/1`:3060 — [小心那些四处巡逻的带刺无人\|机] |
| 22 | **的勇** | 12 | 18 | `cosmobreeder-multi.jar` `vsn/11`:5 — 雄，谢谢你救了我，证明了你的\|勇气。 | `cosmobreeder-multi.jar` `vsn/17`:5 — 雄，谢谢你救了我，证明了你的\|勇气。 | `cosmobreeder-multi.jar` `vsn/23`:5 — 雄，谢谢你救了我，证明了你的\|勇气。 |
| 23 | **的子** | 12 | 15 | `cosmobreeder-multi.jar` `datadf/1`:2792 — [那些自我修复的加农炮发射的\|子弹，是用一种塑化金属制成的 | `cosmobreeder-multi.jar` `datadf/1`:2805 — [那些自我修复的加农炮发射的\|子弹，是用一种塑化金属制成的 | `cosmobreeder-multi.jar` `datadf/1`:2817 — [那些自我修复的加农炮发射的\|子弹，是用一种塑化金属制成的 |
| 24 | **在区** | 12 | 12 | `cosmobreeder-multi.jar` `datadf/1`:4441 —  [其他特工绘制了你当前所在\|区域各部分的地图，有时还带标 | `cosmobreeder-multi.jar` `datadf/1`:4455 —  [其他特工绘制了你当前所在\|区域各部分的地图，有时还带标 | `cosmobreeder-multi.jar` `datadf/1`:4469 —  [其他特工绘制了你当前所在\|区域各部分的地图，有时还带标 |
| 25 | **弹依** | 12 | 12 | `cosmobreeder-multi.jar` `datadf/1`:2794 — [虽说又慢又会弹跳，这些子弹\|依然危险。] | `cosmobreeder-multi.jar` `datadf/1`:2807 — [虽说又慢又会弹跳，这些子弹\|依然危险。] | `cosmobreeder-multi.jar` `datadf/1`:2819 — [虽说又慢又会弹跳，这些子弹\|依然危险。] |

## 按资源分组

| 资源 | 行数 | 含断点行 | 断点总数 | 切词断点 | 含切词断点行 | 切词率(行) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| jar datadf | 2168 | 1418 | 1545 | 699 | 675 | 31.1% |
| jar datadm | 2208 | 1437 | 1579 | 725 | 699 | 31.7% |
| pak datadf | 2266 | 1518 | 1666 | 740 | 719 | 31.7% |
| pak datadm | 2303 | 1520 | 1682 | 739 | 716 | 31.1% |
| vsn | 1618 | 782 | 834 | 282 | 278 | 17.2% |

## 判据与局限

- **判据**：对扫描到的全部玩家可见中文行统计相邻两字（二元组）出现次数，换行点前字 `A` 与后字 `B` 组成的 `AB` 在全库出现 **≥8 次** 即视为常用组合，断在这里算切词。频次只在同一行内相邻计数，不跨行、不跨标点。
- **会漏**：出现不足 8 次的低频专名（人名、地名、技能名等）即使被切开也不计；单行独有但语义完整的组合同样漏判。
- **可能误判**：跨词的高频二元组（如虚词接续）会被算作切词；语料本身的重复句式会抬高某些组合的频次。
- **未做像素级渲染核对**：本统计基于字体度量模拟折行，未逐行渲染核对，也未覆盖引擎分页（每页 3 行）、缺失字形回退与标点禁则等运行时行为。

## 脚本

`/tmp/wordbreak_stats.py`（仓库外临时脚本，未提交进仓库）。
