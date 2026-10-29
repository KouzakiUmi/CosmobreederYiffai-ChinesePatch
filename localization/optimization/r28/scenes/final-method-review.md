# 最终候选13目标类的方法差异白名单审查

**结论：静态白名单通过。** 直接读取最终候选归档与冻结r27：13个目标类共845个方法，827个方法逻辑序列完全相同，18个变化方法严格等于预先枚举的排版／文字终态／显示时钟白名单；未发现其他方法、descriptor集合或字段schema变化。

- 候选：[cosmobreeder-multi.jar](<../../../builds/r28-full-opt-candidate1/cosmobreeder-multi.jar>)，SHA-256 `1227621dcda2e9e76e43469bedf872e2d06ab2b73995282d5d2cf4fdc7f0bd42`。
- 基线：[r27归档](<../../../builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar>)，SHA-256 `dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be`。
- 完整逐方法指纹、原／候选逻辑指令、白名单操作与逐段差异：[final-method-review.json](<final-method-review.json>)。
- 只列变化方法的明细：[changed-method-summary.json](<final-review/changed-method-summary.json>)。

## candidate2 最终归档绑定

**快核通过：candidate2的7779个JAR class entry集合及每项原始字节，全部与已审candidate1相同；PAK两档均为0个class entry。** 无增删、无重复class entry、无class字节差异。因此下文candidate1的13类／845方法静态白名单结论可严格绑定到candidate2相同代码，不需要重新apply或运行大探针。

- 最终[candidate2 JAR](<../../../builds/r28-full-opt-candidate2/cosmobreeder-multi.jar>)：SHA-256 `b8ad97ee9a5d96f38b8e3753bc3252d723c68c4686acef875e10ce69325c63c3`。
- 最终[candidate2 PAK](<../../../builds/r28-full-opt-candidate2/patch.pak>)：SHA-256 `10db525de973dc20a4c5f20b30bd989a0dcb1b0b08d80344b122bddeaa0cf245`。
- 全部class逐项SHA／bytes一致性证据：[candidate2-class-equivalence.json](<final-review/candidate2-class-equivalence.json>)；原candidate1审查完整快照：[candidate1-method-review-bound.json](<final-review/candidate1-method-review-bound.json>)，快照SHA-256 `1986f243aef00c903bb0ae3ae8db79d757828c301e0a1ae1d804be33e349b008`。
- 此核验只读取两份最终JAR／PAK，并在读前／读后复算归档SHA确认未被并发改变。没有改写候选、加载游戏class或调用patcher。资源／字典语义及主集成fresh-JVM final-02结果仍由其独立验收，不能仅从class等价性推出。

## 审查方法与边界

独立编写[只读ASM探针](<final-review/FinalMethodReview.java>)，没有调用CorePatch、CompactFieldsPatch、ItemFont8Patch或SceneTextPatch的`apply`，也没有加载任何游戏class。只在审查内存副本上逆掉逐条独立枚举的新draw／format／clock调用，再与基线比较；不向候选归档写入任何字节，不重新生成候选。

规范化仅忽略debug、StackMap表示、max_stack／max_locals及常量池编号。保留全部实际opcode与操作数、字段与方法owner／name／descriptor／itf、bootstrap／Handle参数、跳转／switch的逻辑指令目的地、try/catch边界、method access／signature／exceptions。插入ALOAD后，原有跳转目标的数字索引会机械增加；逆掉已验证的插入后所有目的地也精确恢复，**不把数字位移误报成输入分支改变**。

另外扫描所有基线class entry：没有class删除；除13个目标与已经声明重编的布局helper／核心排版class之外，未见其他原有class字节变化。布局helper／核心排版内部的重编差异明确列在JSON中，**不属于这次13目标类的方法内部白名单审查**，不能据此宣称全部新增helper已经完成传递调用审计。

## 逐类结果

| 目标 | 全部方法数 | 变化方法／descriptor | 经核实的唯一差异 |
|---|---:|---|---|
| PRG/amn | 29 | `a(DZ)I` | 原`amr$e.c(String)`调用换成`DialogueWrap.terminalText(amr$e,String)`；其他计时、索引、构造、copy和输入逻辑完全相同。 |
| PRG/LY | 38 | `b(SN)V` | 原两处Id绘字分别换成`CompactFields.saveRow/saveLower`；源数据读取与其他36方法完全相同。 |
| PRG/Mb | 22 | `b(SN)V` | 仅首个姓名draw与光标draw换局部helper；光标调用前插入`ALOAD 0`。其余两个Id文字调用、原条件和全部其余21方法相同。 |
| PRG/Mn | 21 | `b(SN)V`、`a(SN,aab)V` | 普通／选中字符的两个SN draw替换；构造、选择／点击动作及其余19方法不变。 |
| PRG/Le | 112 | `<init>(apr)V` | 两处既存注册调用增加Le receiver，各插入`ALOAD 0`；其他构造指令、字段赋值、选择／装备／原cut8+后缀和其余111方法相同。 |
| PRG/Lb | 11 | `a(F)V` | 原单RETURN方法前精确加入`ALOAD 0; FLOAD 1; ItemFont8.update(Lb,F)`；原description draw和其余10方法相同。 |
| PRG/Lg | 8 | `a(F)V` | 原单RETURN方法前精确加入`ALOAD 0; FLOAD 1; ItemFont8.updateName(Lg,F)`；原name draw和其余7方法相同。 |
| PRG/Ew | 127 | `a(SN,Z)V`、`a(SN,I,aAJ)V` | 两个format调用分别换affinity／needs全文helper，各增加SN参数；三个旧文字消费draw换成空占位过滤helper。除这些call替换／ALOAD外，包含条件、状态、奖励／动作逻辑的全部指令恢复后逐条一致，其余125方法相同。 |
| PRG/Jm | 125 | `a(Jm,SN,At)V`、`a(Jm,SN,I,aAJ)V` | 两个旧format与两个右栏draw替换；奖励、统计取值／拼接、翻卡与选择逻辑其余指令以及123方法完全相同。 |
| PRG/kn | 41 | `a(ka,SH,SN,D)V`、`a(km,SN,aAJ)V`、`a(String,SH,km,SN,D)V` | 一个format、两个局部居中draw替换；动画／延时、SA语言变换调用链、输入检测与其余38方法完全相同。 |
| PRG/Lx | 140 | `a(SN,Z)V` | 唯一`SN.a(String,I,String)I`居中调用替换为`SceneText.mapCenter`；地图状态、原输入、图例和其余139方法完全相同。 |
| PRG/Po | 66 | `a(apr,SH,SN,I)V` | 唯一传送目标draw替换为`SceneText.mapDraw`；目标取值、传送语义、MISSION／PAWSED和其余65方法完全相同。 |
| PRG/Kc | 105 | `b(SN,Z,I)V` | 详见下一节：完整source保存前缀完全相同，只替换有损format／zip尾；其余104方法完全相同。 |

表内混淆类型采用简写；JSON保存完整JVM descriptor。方法数是审查范围，不是消费者覆盖率。

## Kc 源头／输入边界的专门核验

不是仅确认某个helper名字出现，而是分别验证：

1. 原／候选该方法从入口，到唯一`ASTORE 9`保存完整说明文本为止的**全部逻辑指令相同**，包括原x预算、`B()`分支选择3／4行基线、选中对象解析、Option／fallback、原全文字符串提取。
2. 该边界之后的候选尾部**严格只有八条指令**：

```text
ALOAD 1                 // SN
ALOAD 9                 // 已完整取得的source
ILOAD 2                 // 原双pass参数
ILOAD 4                 // 原x
ILOAD 6                 // 原计算基线
ILOAD 3                 // 原offset
INVOKESTATIC PRG/SceneText.dataBlock(SN,String,Z,I,I,I)V
RETURN
```

3. 原尾部删除的仅是原三行y数组构造、format、按28切块、zip与逐行draw分发；它没有包含输入写入、奖励／交易、存档服务调用。
4. Kc的其他104方法无逻辑变化，包括输入、动作回调、状态setter／getter和构造器。由此确认本次source-tail接管没有顺手改动Kc其他输入body。

## 明确保留的受保护class

以下最终class与r27原始字节逐字节一致：`PRG/Mf`、`PRG/Iu`、`PRG/Mc`、`PRG/Id`、`PRG/It`、`PRG/LX`、`PRG/GB`、`PRG/FM`、`PRG/Hi`。

与13目标全部方法审查结合，可以确认：本轮目标字节码没有新增其他输入／奖励／交易／存档服务方法修改；姓名／槽位数据源、共享网格与存储相关既存class没有被这些target patch改写。**这不是任意新helper的全传递语义证明，也不是完整游戏输入体验、存档兼容性或实机clip验收。** 新helper会有预期排版／显露终态／显示时钟行为差异；这些应由主代理正在执行的候选CPU与后续实机测试分别验证。

## 可复现命令

```bash
JDK='localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
EXP=(--add-exports java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED --add-exports java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED)
"$JDK/javac.exe" -J-Duser.language=en "${EXP[@]}" -encoding UTF-8 \
  -d localization/optimization/r28/scenes/final-review/classes \
  localization/optimization/r28/scenes/final-review/FinalMethodReview.java
"$JDK/java.exe" "${EXP[@]}" \
  -cp localization/optimization/r28/scenes/final-review/classes FinalMethodReview \
  localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar \
  localization/builds/r28-full-opt-candidate1/cosmobreeder-multi.jar \
  localization/optimization/r28/scenes/final-review/NEW-review.json
```

探针拒绝覆盖输出，只接受审查子目录中的新JSON。实际本次输出：[review-raw-01.json](<final-review/review-raw-01.json>)；[格式化脚本](<final-review/summarize_review.py>)生成最终完整JSON及变化方法明细。没有调用游戏入口、安装、部署、Git写或存档服务。
