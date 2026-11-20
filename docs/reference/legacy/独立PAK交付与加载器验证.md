# 独立 PAK 交付与加载器验证

> 游戏：Cosmobreeder Yiffai `1.0.5_full`。日期：2026-10-21。
> **已完成真实 Steam 启动探针，不只是静态推测。** 本文验证的是补丁的装载方式，不是中文渲染管线已经实现。

## 1. 直接结论

**原版不支持“随便新增一个 `.pak`，放进去就自动重写渲染管线”。但可以做到“只新增三个文件，仍从 Steam 正常启动，不改原 EXE、主 JAR 和官方资源包”。**

建议正式交付形态（文件名为方案示例）：

```text
游戏目录/
  CosmobreederYiffai.exe          原文件不变
  cosmobreeder-multi.jar          原文件不变
  patch.pak                      官方文件不变

  CosmobreederYiffai.l4j.ini      新增：让原启动器带上 agent 参数
  cosmo-patch-loader.jar          新增：版本校验、内存补丁、资源加载
  cosmo-zh.pak                    新增：中文字库、文本、样式/补丁数据
```

旁置 INI 的形式：

```text
-javaagent:cosmo-patch-loader.jar=cosmo-zh.pak
```

这行是**交付接口示例**，不是当前已经存在的正式加载器。实际验证使用单独的探针文件，测试结束后已经撤下。

因此答案不是“必须修改一大堆游戏文件”，而是：

- **仅一个原生PAK：不够。**
- **INI＋加载器＋独立PAK：已验证装载链可行，推荐。**
- 首次安装需要这套入口；之后资源更新通常可以只换PAK。若新增加载器能力或helper类，则可能需要同时更新加载器，不能承诺所有未来代码更新永远只换PAK。

## 2. 本次实际验证到了哪一步

### 2.1 先用空壳验证启动器，避免直接拿游戏试错

原启动器40960字节，SHA-256：

```text
90d90611616e60b5b25a7d538082bd6ac2ceaef3cb717dc46216742bbb2fdb0c
```

静态字符串含 Launch4j、`l4j.ini`和主归档名称。[静态记录](<pak-delivery-evidence/bootstrap/launcher-static.json>)。

把同一启动器与已有JRE复制到新实验目录，那里所谓的主归档只含一个无害的 `MainProbe`，**没有任何游戏类、Steam/FMOD游戏库或存档**：

| 对照 | 结果 |
|---|---|
| 不放INI | 仅MainProbe写出标记，无agent标记 |
| 加入同名INI与测试agent | agent写出 `PREMAIN_OK_NO_GAME`，MainProbe也正常执行 |

两次启动器均退出0；日志明确带入INI参数。[空壳结果](<pak-delivery-evidence/launcher-probe/result.json>)。这在本机实际启动器上确认了默认旁置文件名，不再仅凭新版Launch4j文档猜测。

### 2.2 在Java中预校验目标类，不初始化游戏

探针加载器从独立PAK读取原始/替换 `PRG/iF`字节，只接受与基线完全相同的输入类：

- 替换窗口标题，加上 `[PAK PROBE]`。
- 将设置/存档定位方法改为工作区测试state目录，避免测试画面选项写回用户原设置。
- 不修改字体注册、shader、Steam接口或玩法。
- 输入类不匹配时中止本次游戏启动，而不是盲目应用。

先用游戏随包Java和 `-Xverify:all`加载目标类但不初始化，并访问方法元数据；退出0，记录 `READY → TRANSFORM_IF`。[预校验结果](<pak-delivery-evidence/live-probe/preflight.json>)。

### 2.3 真实游戏通过Steam启动成功

本机Steam快捷方式登记的URI为：

```text
steam://rungameid/3548000
```

实际测试仅向安装目录新增三个探针文件，没有替换任何现有文件；通过上述URI启动，而非直接运行游戏EXE。实际Java进程参数包含：

```text
-javaagent:cosmo-probe-agent.jar=cosmo-render-probe.pak
-jar <原安装>/cosmobreeder-multi.jar
```

观察结果：

- 实际游戏进程PID `34980`，窗口标题变为 **Cosmobreeder Yiffai [PAK PROBE]**。
- 独立PAK中的替换类确实被agent应用，事件日志增加第二组 `READY → TRANSFORM_IF`（第一组来自预校验）。
- 游戏进入片头演示，原图像、英文字幕和终端效果正常显示。
- 测试窗口按预设使用窗口模式；未进入玩法或主动操作存档。

![经Steam启动，外部PAK内存补丁已显示窗口标题标记](<pak-delivery-evidence/live-probe/steam-game-probe.png>)

[完整运行证据](<pak-delivery-evidence/live-probe/steam-runtime.json>)、[Steam启动记录](<pak-delivery-evidence/live-probe/steam-launch.json>)、[内存替换类反汇编](<pak-delivery-evidence/live-probe/patched-iF.txt>)。

**由此已经证明：**

```text
Steam启动
  → 原Launch4j EXE
  → 读取旁置INI
  → 随包Java启动premain agent
  → agent读取独立自定义PAK
  → 游戏类定义前替换字节码
  → 原游戏正常进入渲染画面
```

### 2.4 已退出并清理

通过本次窗口的系统关闭按钮正常退出，随后确认该PID无窗口、无进程。逐项核对绝对路径和SHA后，仅删除本次新增的三个文件。

- **25个受保护的原有文件全部字节不变**，包括主JAR、官方PAK、EXE、用户存档、设置及已登记的存档备份等。
- 未发现新增的意外根目录文件。
- 没有覆盖/回滚用户存档，也没有修改Steam启动项或持久化环境变量。

[清理与原文件复核](<pak-delivery-evidence/live-probe/cleanup.json>)。

边界：这不是对Steam云、成就、账号状态或所有系统缓存的全面审计。已验证的是指定本地文件和补丁装载；也没有把原版演示画面正常显示称为中文渲染改造通过。

## 3. 为什么一个普通PAK不能自己生效

### 3.1 原生入口只取固定包名

`PRG/adE.<clinit>` PC10加载固定字符串，`adE.f()`通过 `adu.b`打开它并包装成ZIP资源容器。[固定名称与读取](<pak-delivery-evidence/snapshot/PRG_adE.txt#L11-L22>)、[打开入口](<pak-delivery-evidence/snapshot/PRG_adE.txt#L183-L200>)。

本轮扫描全部7,736个class中的相关字面量，只发现这一处 `.pak`名称；进一步读取该入口及资源分发实现，没有通配目录扫描或按名字依次挂载多个包的逻辑。**结论依据是已追踪的加载链，不是单凭搜索没命中。**

新增 `chinese.pak`、`patch2.pak` 或 `mods/xxx.pak`不会因为扩展名相同而被这条入口发现。正式加载器需要自己约定额外包的名称/位置和优先级。

### 3.2 原生PAK按“组”选择，不是任意文件差量覆盖

这是容易误判的部分：

1. `ada.a()`枚举ZIP entry名称。
2. `adE`对名称做去尾 `/`，不是自动推导每个文件的父目录。
3. 请求一个组时，成员表存在该组名才选PAK，否则选base。
4. 命中后，在同一个容器里读取该组的索引和序号资源；没有逐成员退回主归档的合并逻辑。

证据：[entry枚举](<pak-delivery-evidence/resources/PRG_ada.txt#L6-L28>)、[组门禁](<pak-delivery-evidence/snapshot/PRG_adE.txt#L174-L230>)、[去尾斜杠](<font-evidence/snapshot/aDJ.txt#L306-L321>)、[组内序号读取](<pak-delivery-evidence/resources/PRG_acV.txt#L70-L89>)。

本版官方PAK的423个entry中有5个显式目录entry：

```text
datadf/
datadm/
dataq/
datav/
vsn/
```

**创建原生PAK时不能省掉这些目录entry。** 只有 `dataq/0`、`dataq/6`等文件，不等于已满足组识别条件。一个组选中PAK后，组内缺文件也不会自动向主JAR补齐；因此不能把零散几个资源装成包就认为旧资源会自动合并。

这意味着“直接替换官方PAK”的方案既要保留官方其他内容，也要保证被替换组完整；它不是安全的通用增量Mod接口。

### 3.3 字体定义和shader还有另一条加载路径

默认字体定义由 `iF`直接调用 `apQ.e.b(...)`读取；shader由 `Ym`以同一路径读取顶点/片元文件。它们不通过 `adE/acV`的加密分组资源解析。

- [字体读取](<font-evidence/snapshot/iF.txt#L650-L677>)。
- [shader读取](<render-pipeline-evidence/snapshot/Ym.txt#L185-L204>)。
- [普通文件/资源流](<pak-delivery-evidence/snapshot/PRG_aqX.txt#L116-L182>)。

实际Internal路径允许磁盘同名文件优先、缺失时回退classpath；这提供了**散文件替换字体定义或现有shader**的可能，但不是“任何PAK内的同名文件都能覆盖”。其他位置类型的优先级不同，不能推广成全局规则。

此外，替换字体定义不等于替换字形像素；原 `bbc2`像素仍来自图集region。字体文件和shader替换也不能改变Java里的分行、光标、打字机和FBO逻辑。

### 3.4 PAK资源解析不是JVM类加载器

原生PAK中即使放入 `PRG/Yg.class`，这条ZIP资源读取链也不会替JVM定义它。原Manifest没有声明额外Class-Path，也没有agent入口。[原Manifest](<pak-delivery-evidence/bootstrap/manifest-normalized.txt>)。

Java17的 `-jar`模式会以启动归档覆盖普通classpath设置，不能靠旁边多放一个JAR，或加一个会被忽略的 `-cp`，就期待覆盖原类。Context7已查询到Java17启动器对应实现：[Java17 launcher](<https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>)。

本次使用的是**启动时agent**：在应用main之前注册类变换器，在目标游戏类首次定义前返回替换字节。它不是运行中临时附加，更不是修改磁盘上的原JAR。

## 4. 几种交付方式的取舍

| 方式 | 是否改原游戏文件 | 仍从Steam正常入口启动 | 对本次渲染重写是否足够 |
|---|---|---|---|
| 只新增任意原生PAK | 不改 | 可以启动原游戏，但包不会自动挂载 | 不够 |
| 替换固定官方PAK | 改资源包 | 原入口可保留 | 只能覆盖其资源路径，Java管线仍不改变 |
| 散文件＋资源包 | 增加/替换资源 | 原入口可保留 | 可做有限资源调整，不能完成整个布局/合成改造 |
| **旁置INI＋启动agent＋独立PAK** | **本次验证为只新增文件** | **已实测** | **可以承载代码与资源改造，推荐继续开发** |
| 重建主JAR并合并资源包 | 改主程序/资源包 | 预计可保留原入口，需验收 | 可行后备，更新冲突和回退成本更高 |
| 新启动器＋classpath overlay | 原归档可不改 | 需额外集成启动路径，不等于原Steam入口已适配 | 技术备选，不是本次首选 |

只改原Manifest加入启动agent属性，也是“修改原JAR”，不能宣传成纯旁置。

## 5. 推荐正式加载器的职责

本次探针只会处理一个版本的一份 `iF`类，不能直接当正式Mod加载器发布。正式版本至少要有：

### 5.1 代码部分

- 校验游戏版本、原归档/目标类SHA以及PAK兼容版本。
- 只变换白名单类；新文字bridge/helper必须对游戏类加载器可见。
- 在相关类首次加载前安装变换器，不在类已初始化后赌覆盖顺序。
- 目标不匹配时给出可读错误；不能让半套渲染补丁继续运行后悄悄写坏状态。
- 保留合法StackMap、异常表和调用约定，不把本次小型直线方法探针推广为任意字节码替换都安全。
- 兼容其他agent/补丁时明确顺序和冲突，不默认能随意叠加。

### 5.2 资源部分

- 明确定义新包的资源命名、索引和优先级，例如“汉化包 → 官方PAK → 原JAR”。这需要加载器实现，**不是原游戏已经提供的逐资源链**。
- 通过受控资源接口提供独立字体、shader、译文和容器profile；不要误把加密原生分组协议与自定义ZIP数据混为一谈。
- 资源可在自定义PAK内存读取，也可按内容哈希解到自己的cache目录；cache生命周期必须明确。
- 字体许可、原ASCII像素和原游戏资产权利分别处理。正式分发优先新代码/新资源/变换规则，不把本次含原class字节的研究PAK当公共发行包。

本次 `.pak`是**由自制agent显式读取的ZIP载荷**，不是原生 `adE`自动发现的新包。扩展名本身不带代码执行能力；把JAR改名PAK也不会消除启动入口的需要。

### 5.3 安装、更新、卸载

- 当前安装没有同名INI，因此实验可直接新增。正式安装器必须检查：若用户已有INI，合并自己的独立agent配置，不能覆盖其他JVM选项。
- 含空格路径、不同Steam库目录、不同启动cwd都要测试；本次相对agent/PAK路径在该Steam安装上已成立，不等于所有安装组合已经覆盖。
- 启动时读取并缓存资源，更新后需完整退出并重新启动游戏；不承诺运行中热替换PAK安全。
- 卸载只移除自己的agent配置和文件；保留用户INI中原有内容、存档、设置、官方包。
- 可以把三个文件做成一个发行ZIP或安装器，达到“一次解压/安装，以后照常点Steam开始”的体验。**这与“原生只放一个PAK自动生效”是不同承诺。**

现有[打包工具](<../localization/tools/package.py>)仍是重建JAR/PAK的旧交付流程；本次没有把它改成上述加载器式发行工具。

## 6. 对渲染重写方案的影响

[文字渲染重写方案](<文字渲染管线重写方案.md>)的独立字库、全文布局、文字覆盖mask和最终CRT保护，可以由这一启动agent加载的代码模块承载。

接下来不必先去替换原游戏JAR。建议顺序为：

1. 把已证的INI/agent入口整理为正式版本锁定加载器。
2. 先通过它接入一个VSN文本面和一个普通UI容器。
3. 新字库和样式放独立PAK，保持主美术图集不变。
4. 再完成字宽/换行、完整内容可访问、打字机稳定性、mask遮挡/淡出及实机可读性测试。

**本次只证明交付与内存加载通路，不证明这些渲染功能已经做完。**

## 7. 证据、工具与核验范围

- 静态研究：[原生包入口提取](<pak-delivery-evidence/inspect_loader.py>)、[资源分组与文件适配](<pak-delivery-evidence/inspect_resources.py>)、[启动器/委托绑定](<pak-delivery-evidence/inspect_bootstrap.py>)。
- 空壳实验：[启动器INI探针](<pak-delivery-evidence/probe_launcher_ini.py>)、[结果](<pak-delivery-evidence/launcher-probe/result.json>)。
- 真实实验：[构建探针](<pak-delivery-evidence/build_live_probe.py>)、[JVM预校验](<pak-delivery-evidence/preflight_live_probe.py>)、[部署脚本](<pak-delivery-evidence/deploy_live_probe.py>)、[精确清理脚本](<pak-delivery-evidence/cleanup_live_probe.py>)。
- 审计：[静态/证据检查脚本](<pak-delivery-evidence/verify_pak_research.py>)、[检查结果](<pak-delivery-evidence/verification.json>)。56项检查全部通过，覆盖23份类快照、实机记录一致性、原文件保护和31个本地链接；检查脚本不会重新启动游戏。

这些是有副作用边界的研究工具，不是给玩家直接运行的正式安装器；构建/实验目录存在时拒绝覆盖。真实部署、Steam启动和清理分开进行，不能只运行其中一半就当成完整复现。

文档核验：Context7查询了Java17启动器、Java17 instrumentation，以及Launch4j外部INI。来源：[Launch4j运行时选项](<https://github.com/mirror/launch4j/blob/master/l4j/web/docs.html>)、[Java17启动agent契约](<https://docs.oracle.com/en/java/javase/17/docs/api/java.instrument/java/lang/instrument/package-summary.html>)、[变换器注册](<https://docs.oracle.com/en/java/javase/17/docs/api/java.instrument/java/lang/instrument/Instrumentation.html>)。

Launch4j精确构建版本未知，但该EXE的INI机制已经实测；游戏随包Temurin `17.0.6+10`的agent支持也已实测。实际验证不依赖仅在文档中存在的假设，也没有因此声称对其他游戏版本兼容。
