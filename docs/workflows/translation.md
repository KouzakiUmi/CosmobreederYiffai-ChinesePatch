# 翻译与导出工作流

译文唯一可编辑源位于 `tl_work/chunks/` 下的分块 TSV；`payload/` 内的加密资源（`cosmobreeder-multi.jar` 与 `patch.pak`）均由 `tl_work/template/` 与 `tl_work/chunks/*.tsv` 经 `tools/tl_tool.py build` 重建生成。

## 一、快速导出与查看状态

```cmd
python tools\tl_tool.py export --target payload             :: 首次从 originals/ + payload/ 导出 TSV 与冻结骨架
python tools\tl_tool.py status                             :: 查看各分块行数、已译、未译、合句空行与软断行统计
```

`export` 以本地 `originals/` 为原文基准、以 `--target` 为译文基准生成九个分块和冻结骨架。已有工作区时，可用 `--tl-dir` 指定一个新的目录做对照；`--force` 会清空该目录的已有分块与模板。

### 核对全量场景校对版

以 `1.0.5_full` 的本地原版文件和 [alpha0.4-scene-audit](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases/tag/alpha0.4-scene-audit) 对应的已还原归档为输入。在仓库根目录核对导出结果：

```cmd
python tools\tl_tool.py export --target payload --tl-dir build\scene-audit-check
python tools\scene_context_index.py verify --chunks build\scene-audit-check\chunks
python tools\tl_tool.py verify-readback --tl-dir build\scene-audit-check --target payload
```

[公开校对索引](../../review/scene-context-changes.jsonl)记录改动 ID、场景或键、译文及指纹，不含原文列。纯代码、原样保留的值或直接嵌入原句的译文只留下指纹。[版本指纹](../../review/scene-context-index.json)锁定索引与全部分块，校验时也会检查未修改的条目。

## 二、TSV 分块结构

```text
tl_work/chunks/
├── dialogue/
│   ├── jar_datadf.tsv    # SFW 女线对白 (cosmobreeder-multi.jar :: datadf/1)
│   ├── jar_datadm.tsv    # SFW 男线对白 (cosmobreeder-multi.jar :: datadm/1)
│   ├── pak_datadf.tsv    # NSFW 女线对白 (patch.pak :: datadf/1)
│   └── pak_datadm.tsv    # NSFW 男线对白 (patch.pak :: datadm/1)
├── vsn/
│   ├── jar_vsn.tsv       # SFW 演出字幕 (cosmobreeder-multi.jar :: vsn/*)
│   └── pak_vsn.tsv       # NSFW 演出字幕 (patch.pak :: vsn/*)
└── ui/
    ├── jar_datav.tsv     # SFW 词典与界面串 (cosmobreeder-multi.jar :: datav/1)
    ├── pak_datav.tsv     # NSFW 词典与界面串 (patch.pak :: datav/1)
    └── jar_datay.tsv     # 运行时 overlay、任务日志与商店名 (cosmobreeder-multi.jar :: datay/1)
```

### 列格式

- **dialogue / vsn（8 列，Tab 分隔）**：`seq \t archive \t entry \t scene \t line \t prefix \t source \t target`
- **ui（6 列，Tab 分隔）**：`seq \t archive \t entry \t key \t source \t target`

### 编辑规则（必守）

1. **只改最后一列 `target`**，其余定位列（`seq`、`archive`、`entry`、`line`/`key`、`prefix`、`source`）一律不动。
2. **转义规范**：
   - 真换行 `\n`、制表符 `\t`、回车 `\r`、反斜杠 `\` 在 TSV 中写作字面 `\n`、`\t`、`\r`、`\\`。
   - 对话框软断行 `U+2028` 在 TSV 中记作 **`⏎`**（仅限 `dialogue/` 使用，**禁止写入 `vsn/` 与 `ui/`**，VSN 词法解析器拒绝 U+2028）。
3. **合句空尾行**：`dialogue/` 与 `vsn/` 中因合句而清空的行，`target` 保持为空字符串 `""`（唯一特例 `patch.pak vsn/251:94` 为 `__RAW__: `）。
4. **结构与标记守恒**：
   - 原文中的 `@变量`、`{...}`、`${...}`、`%s`、`</>`、`|` 分段符与引擎 ID（如 `BIGBOLD1`）必须数量与内容一致。
   - 对话框 240px（`story12` 12px 字，每行约 20 汉字，每页 3 行）；无线电与物品说明 150px（`bbc2` 10px 字，每行约 15 汉字）。排版约束见[维护入口](../../AGENTS.md#维护约定与安全边界)。
5. **同文联动检查**：
   - 同一句通常同时存在于 `jar`（SFW）与 `pak`（NSFW）两侧；地名/任务日志还可能在 `datav/1` 与 `datay/1`（`/patchDictionary/`、`/missionLog/`）各自存一份。改一处时用 `review_tool.py dedupe` 检查两侧是否同步。

## 三、字体与资源自动同步

运行 `tools/tl_tool.py build` 时，构建器会：

1. 将 `tl_work/chunks/*.tsv` 精确回填到 `tl_work/template/`，校验 JSON 语法后用 Salsa20 重新加密；
2. 汇总所有文本用到的字符，调用 `tools/lib/optimized_fonts.py` 从 `deps/fonts/` 动态补全 `story12.fnt`、`bbc2.fnt`、`classic.fnt` 与字库图集区域，并自动把新字体 SHA 注入 `src/java/runtime/` 后编译（Java 8 目标）；
3. 叠加 `assets/images/` 图集覆盖并执行 `IncrementalPatchDriver` 与 `VerifyLayout` 字节码校验。
