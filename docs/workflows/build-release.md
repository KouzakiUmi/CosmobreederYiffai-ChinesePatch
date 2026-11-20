# 构建、回归与发版工作流

## 一、全链构建与验证（日常改完译文/代码后执行）

```cmd
python tl_work\chain_build.py            :: dry-run：校验 TSV 与规则扫描
python tl_work\chain_build.py --apply    :: 全链执行（5 步闭环）
```

`--apply` 依次执行：
1. `tl_tool.py status` & `review_tool.py scan`
2. `tl_tool.py build --output payload`（重建 `payload/cosmobreeder-multi.jar` 与 `payload/patch.pak`）
3. `tests/run_cpu_regression.py --candidate payload --output payload/test-results`（19 步 JVM CPU 回归）
4. `tl_tool.py verify-readback --target payload`（逐条回验 `payload/` 明文与 `tl_work/chunks/*.tsv` 完全一致）
5. 写入 `payload/acceptance.json` 并同步根目录 `manifest.json`

在隔离目录试构建时，`tl_tool.py build --output` 指向新的 `build/` 子目录；CPU 回归的 `--output` 指向新的 `build/` 或 `payload/` 子目录。全链使用固定的 `payload/` 与 `payload/test-results/`。不得把原版或测试源码目录当作输出。

## 二、发布与安装器单元测试

```cmd
python -m unittest discover -s tests/release -v
CB_REAL_DELTA_TEST=1 python -m unittest discover -s tests/release -p test_real_payload.py -v
```

## 三、生成差分发行包（EXE + Python ZIP）

```cmd
python tools\release_tool.py --source originals --target payload --output dist\alpha0.4-scene-audit-local --label alpha0.4-scene-audit --exe
```

产物包含：
- `CosmobreederYiffai-alpha0.X-setup.exe`（Windows 单文件独立安装器，内置 Python）
- `CosmobreederYiffai-alpha0.X-python.zip`（Python 3.12 运行版）
- `payload/`（`CBDELTA1-COPY-XOR` 差分负载 + `manifest.json`）
- `acceptance.json`、`build-report.json`、`SHA256SUMS` 与完整 `licenses/`

发行输出必须是新的 `dist/` 子目录。打包器核对目标归档及验收封签，并在打包完成后复查输入、安装器源码和许可证的指纹。

校验产物（不接触游戏目录）：
```cmd
 dist\alpha0.4-scene-audit-local\CosmobreederYiffai-alpha0.4-scene-audit-setup.exe --verify-payload
 dist\alpha0.4-scene-audit-local\CosmobreederYiffai-alpha0.4-scene-audit-setup.exe --licenses
```

## 四、发版前核对清单

- [ ] `tl_work/chain_build.py --apply` 全部 5 步退出码为 0（19 步 CPU 回归通过、读回无差异）
- [ ] `tests/release` 单测全部通过
- [ ] `release_tool.py` 差分重建字节相等、`--verify-payload` 与 `--licenses` 通过
- [ ] 新增 [../release-notes/](../release-notes/) 对应版本发布说明，更新 [../../README.md](../../README.md) 与 [../接续.md](../接续.md)
- [ ] 如已完成实机测试（安装、启动、SFW/NSFW 开场与对话字体显示、存档读写），将实际证据补充进对应记录
