# alpha0.1 差分协议与安装安全

alpha0.1 是预发行，不代表稳定版验收。目标为 `r27-story12-shaderfix-test5`，需要用户自备合法原游戏。发布物不含完整游戏 JAR/PAK，也不含原版备份。

## CBDELTA1-COPY-XOR

全部整数采用大端。8 字节 `CBDELTA1` 后是指令流：

- `C` + uint64 源偏移 + uint32 长度：从原文件复制，长度 1–65536。
- `X` + uint32 解压长度 + uint32 压缩长度 + zlib 数据：解压得到 XOR 差值，与原文件在 `当前输出偏移 % 源大小` 起的字节逐位 XOR。读至源结尾则从源首部继续；源至少 65536 字节，每条最多 65536 字节。
- `E`：结束，不允许尾随数据。

构建器先尝试 SHA256 匹配的整块 COPY，其余生成源依赖 XOR。r27 重打包后的两个文件均未匹配整块 COPY，实际使用 XOR+压缩，差分可能接近原文件大小；这不等同于压缩完整目标，解码仍必须提供 SHA 锁定的原文件。内存为源块索引及数个 64KiB 缓冲区，不把整文件放入内存。XOR 不是加密或版权保护承诺。

[manifest](<../dist/alpha0.1/payload/manifest.json>) 锁定两文件完整源/目标/差分 SHA256 和尺寸。应用先验源和负载 SHA，重建后验精确目标 SHA。manifest 尺寸字段必须是非 bool 的正整数；源至少 64KiB，单个源/目标/差分均不超过 256MiB，每类文件合计不超过 512MiB；实际源/差分尺寸必须精确匹配。manifest 本身最多 1MiB，差分最多 65536 条数据指令，每条输出最多 64KiB，总输出受目标尺寸上限约束。压缩流输出有上限，拒绝截断、额外数据、未知指令、越界读写。外部 SHA256SUMS 必须从可信发布渠道核对；内置 manifest 及 SHA 是完整性检查，不是发布者数字签名，无法防止攻击者同时替换程序和全部元数据。

原版档仅更新 JAR，必须无 patch.pak；官方 NSFW 档更新 JAR+PAK，二者源 SHA 均必须匹配。未知源在产生游戏目录写入前拒绝。检测到 Java/Javaw/Cosmobreeder 进程时保守拒绝安装与还原（可能同时阻止无关 Java 应用）。不启动游戏，不递归发现游戏，不读写存档、注册表或其他游戏资产。

## 事务与还原

固定路径：`cosmobreeder-multi.jar`、`patch.pak`、`cosmobreeder-alpha0.1-state.json`、`_cosmobreeder_alpha0.1_backup/`。拒绝链接、已有安装记录、已有备份；不支持 force 或自定义备份。先在系统临时目录重建并校验所有目标，再创建本次专属备份，校验后 flush/fsync 备份和 transaction.json；所有重建输出及同盘 stage 都在替换前 flush/fsync，随后逐个同盘原子替换。捕获异常（含 KeyboardInterrupt）时，仅在当前文件仍为已知源/目标时还原已替换文件，并同步、校验；未知用户修改不覆盖。异常回滚本身失败时保留备份并显式报错。受测的进程异常/中断在 journal 已写入且当前文件仍通过源/目标 SHA 校验时可用还原操作恢复，恢复可重试。这不是任意硬件断电可恢复的保证，也不是多文件原子事务；存储设备/目录元数据持久化不能由文件 fsync 完整保证。未知、丢失或损坏的 current 一律拒绝覆盖并保留备份供人工核对。journal 写入前中断仅可能留下原版备份且未替换游戏文件；需人工核对并移走此残留备份后重试，不自动猜测归属。

还原校验记录、备份精确源 SHA 和当前文件 SHA；当前文件仅允许本次目标或本次原版，未知修改拒绝覆盖。备份目录含未知文件或链接时拒绝删除。还原 stage 在替换前 flush/fsync，替换后再次同步当前文件；全部还原完成并逐文件验证精确源 SHA 后才清理专属备份和安装记录。还原途中异常保留记录/备份，重试仍须通过全部 current 校验。存档不作为发现、校验、备份或恢复输入。

## 命令

从源码运行（Python 3.12，无额外运行依赖）：

```sh
PYTHONPATH=src python -m cosmobreeder_patch --payload dist/alpha0.1/payload --verify-payload
PYTHONPATH=src python -m cosmobreeder_patch --payload dist/alpha0.1/payload --game-dir GAME --check
PYTHONPATH=src python -m cosmobreeder_patch --payload dist/alpha0.1/payload --game-dir GAME --install
PYTHONPATH=src python -m cosmobreeder_patch --payload dist/alpha0.1/payload --game-dir GAME --uninstall
```

不传操作参数打开 Tk GUI，选择目录后检测、安装或还原。EXE 内嵌相同差分负载；支持相同参数。Python 发布 zip 解压后在其目录运行 `python -m cosmobreeder_patch`。CLI 的 `--verify-payload` 只读发布负载，不发现或访问游戏目录。

```sh
python tools/build_alpha_release.py --exe
python -m unittest discover -s tests/release -v
CB_REAL_DELTA_TEST=1 python -m unittest discover -s tests/release -v
CB_REAL_DELTA_TEST=1 CB_EXE_DELTA_TEST=1 CB_GUI_DELTA_TEST=1 python -m unittest discover -s tests/release -v
```

构建输出目录必须尚不存在；已有输出不可覆盖，可用 `--output` 指定新的发布目录。构建需要自备原版 backup 两文件及已有 r27 本地构建结果，EXE 另需预装 PyInstaller（本次使用 6.19.0，不自动安装）。源码仓库不承诺能从空目录生成原游戏。构建器会短暂生成精确目标验证文件，校验成功后立即删除；该文件不进入发布压缩包。

发行包同时附带根 [LICENSE](<../LICENSE>)、[NOTICE](<../NOTICE>)、[THIRD_PARTY_NOTICES.md](<../THIRD_PARTY_NOTICES.md>) 与完整 [licenses/](<../licenses/>) 文本目录（字体及 Python/PyInstaller/Tk 运行时许可证）；EXE/运行 zip 内也嵌入相同文本并保持目录层级。通过 `--licenses` 或 GUI“第三方许可与声明”递归查看。src-layout 源码运行时使用项目根，zip 使用包目录，EXE 使用内嵌资源根；许可查看器不跟随任何符号链接。根声明与 licenses 子路径保持同级，完整保留相对路径引用。构建器要求这些许可文件已经存在，否则拒绝构建；不依赖未公开的 localization/runtime 目录许可证。

EXE 使用 PyInstaller 标准 onefile，未签名；GUI 需要桌面会话，命令行验证不等价于人工 GUI 点击验收。
