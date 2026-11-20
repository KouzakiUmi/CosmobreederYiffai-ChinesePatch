"""Resolve generated output without following links or leaving workspace roots."""
from __future__ import annotations

import os
from pathlib import Path


def reject_link(path: Path) -> None:
    if path.is_symlink() or path.is_junction():
        raise ValueError(f'输出路径不能使用链接：{path}')


def workspace_output(root: Path, requested: str | Path, *, exact=(), parents=()) -> Path:
    path = Path(os.path.abspath(root / requested))
    if not path.is_relative_to(root):
        raise ValueError(f'输出目录必须在工作区内：{path}')
    if os.name == 'nt' and any(part.endswith(('.', ' ')) or ':' in part
                               for part in path.relative_to(root).parts):
        raise ValueError(f'输出路径含有 Windows 保留的路径写法：{path}')
    for part in (*reversed(path.parents), path):
        if part.is_relative_to(root):
            reject_link(part)
    if (path not in {root / directory for directory in exact}
            and not any(path != root / directory and path.is_relative_to(root / directory)
                        for directory in parents)):
        raise ValueError(f'不允许的输出目录：{path}')
    return path


def check_outputs(directory: Path, names: tuple[str, ...]) -> None:
    for name in names:
        path = directory / name
        reject_link(path)
        if path.is_file() and path.stat().st_nlink != 1:
            raise ValueError(f'输出文件不能是硬链接：{path}')
