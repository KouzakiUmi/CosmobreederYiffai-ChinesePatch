# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller 打包配置 —— 单文件 exe，双击即装。

    cd localization/packaging
    python prepare.py --build ../builds/final-8146-r11-images
    pyinstaller CosmobreederYiffaiCN.spec

产物：dist/CosmobreederYiffaiCN.exe（约 56 MB，payload 内嵌）
onefile 会把 datas 解到 sys._MEIPASS，patch_tool.py 里已按这个处理路径。
"""
import json as _json
import os as _os

_HERE = _os.getcwd()   # 必须在 localization/packaging 下运行 pyinstaller

with open(_os.path.join(_HERE, 'manifest.json'), encoding='utf-8') as _f:
    _manifest = _json.load(_f)

# manifest.json 放根，payload 里的文件按原结构放 payload/
_datas = [(_os.path.join(_HERE, 'manifest.json'), '.')]
_seen = set()
for _v in _manifest['variants'].values():
    for _entry in _v['files']:
        _name = _entry['payload']
        if _name in _seen:
            continue
        _seen.add(_name)
        _src = _os.path.join(_HERE, 'payload', _name)
        if not _os.path.isfile(_src):
            raise SystemExit('payload missing: ' + _src)
        _datas.append((_src, 'payload'))

a = Analysis(
    [_os.path.join(_HERE, 'launcher.py')],
    pathex=[_HERE],
    binaries=[],
    datas=_datas,
    hiddenimports=['patch_tool'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'PIL', 'pandas', 'matplotlib', 'scipy', 'pytest'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CosmobreederYiffaiCN-v1.5',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,              # upx 压 56MB 的 payload 收益小、还容易被杀软误报
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # 无控制台窗口，界面全在 tkinter
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
