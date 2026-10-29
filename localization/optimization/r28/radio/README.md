# 无线电显示名局部同步

## 数据与范围

映射来源为 [命名规则](../../../editorial/r3-names/NAMING_RULES.md) 和 [提议台账](../../../editorial/r3-names/decisions/names-proposed.json)。这是36个人名的工程同步，不代表语义审查 approved；不修改台账状态。

[同步脚本](../../../editorial/r3-names/tools/sync_radio_names.py) 从每个人名的 source_forms/radio_aliases 生成精确、大小写不敏感的静态 helper 与 [测试期望 TSV](../../../editorial/r3-names/generated/radio-names.tsv)。TSV 含完整台账 SHA-256；`--check` 检查过期输出，无运行时 JSON IO。昵称不加入无线电映射。Yifany 六字母别名保留；The0 preserve_ascii_case 返回原输入对象。Mauser→毛鼠、Tomcat→雄猫、Yiffai→伊吠、Yiffany/Yifany→伊吠妮；其他名字仅以台账为准。

## 集成契约

`RadioLabelsPatch.apply(Map<String, ClassNode>)` 接口、patcher及 target pins 不变。runtime helper 用 Java8 字节码，工具用现有 JDK17 内置 ASM。基线仍为 r27，不能将已打 radio 补丁的候选作为 patcher 输入。

| class | SHA-256 |
|---|---|
| PRG/JM.class | ec45f0d0718ed0c50804c85cb127c0a51c0ebb0cbe0a515934c8a9c2355d12ae |
| PRG/JQ.class | 78f1053cd0d06b9eb3be07cd14b2405bf7ce91f8b15c7d959c73f8da2c08a9a7 |

仅既有4个 `JF.a(String,apr)` 查名返回结果经过 display：JM 两头像、一联系人频率行，JQ 一说话者标签；只改其后3 draw/1 drawTint。JF/JM/JQ 源码、ID、控制流、频率不变。隐藏返回 `??????` 原样保留，不推断 Gitgud/static/Starkill/The0 身份，不让 Queen/High Lady 提前变为人名；null、未知 actor、脚本键原样返回。

## 字体与几何

这4条路由中，台账中文 target 集合局部选择 classic8；Latin名保原 role（包括 glyph9），不是全局字号切换。Tomcat 现为雄猫，必须使用 classic，不再有原 ASCII 特例。颜色、原文、坐标原样传递。

所有 target 最多6字符；括号标签总 advance≤64px；联系人字段补齐6字符，冒号固定 +48px，连频率总104px。required_chars 含全部36个 target，包括当前可见 carrier 为0的 Macsen/Gitgud，确保将来合法查名不缺字。

## 隔离测试（仓库根，Git Bash）

```bash
python localization/editorial/r3-names/tools/sync_radio_names.py --check
JDK=localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin
BASE=localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar
mkdir -p work/radio-names-r3/classes work/radio-names-r3/tools
"$JDK/javac.exe" --release 8 -encoding UTF-8 -cp "$BASE" -d work/radio-names-r3/classes localization/layout/src/PRG/RadioLabels.java
"$JDK/javac.exe" --add-exports java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED --add-exports java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED -encoding UTF-8 -cp "work/radio-names-r3/classes;$BASE" -d work/radio-names-r3/tools localization/layout/tools/java/RadioLabelsPatch.java localization/layout/tests/RadioLabelsTest.java
"$JDK/java.exe" --add-exports java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED --add-exports java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED -Dfile.encoding=UTF-8 -Xverify:all -cp "work/radio-names-r3/tools;work/radio-names-r3/classes;$BASE" RadioLabelsTest "$BASE"
```

隔离测试覆盖36名/37别名及大小写、The0原对象、未知键/hidden/null、SN实际方法代理的原文/颜色/坐标/role、64/48/104px几何、预检与重复补丁拒绝，以及逆还两class序列化逐字节一致。

最终 candidate7 由主控构建后再使用三参数模式 `RadioLabelsTest base.jar candidate.jar classic.fnt`：classpath必须为 `tools;candidate.jar`（不能有隔离 helper/classes 或另一个提供helper的jar），CodeSource 严格核验实际 candidate。该模式检查 candidate 的4lookup/4display/3draw/1tint，全部target汉字8×8/offset0/advance8及Latin/频率advance8。隔离成功不冒充实际candidate或GPU验证；本改动没有构建父候选、安装或部署。
