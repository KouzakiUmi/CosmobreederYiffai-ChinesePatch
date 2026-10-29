"""Read-only directory discovery adapted from localization/packaging/patch_tool.py.

Discovery is only a hint: the installer still verifies source hashes before writes.
No recursive drive scan, save access, registry writes, or game launch.
"""
import os
from pathlib import Path
import re
import sys


def _unique(paths):
    seen = set()
    result = []
    for path in paths:
        path = Path(path).absolute()
        key = os.path.normcase(str(path))
        if key not in seen:
            seen.add(key)
            result.append(path)
    return result


def _steam_roots():
    bases = [Path(base) / 'Steam' for name in ('ProgramFiles', 'ProgramFiles(x86)')
             if (base := os.environ.get(name))]
    bases += [Path(p) for p in (r'C:\Program Files (x86)\Steam', r'C:\Program Files\Steam',
              r'C:\Steam', r'C:\SteamLibrary', r'D:\Steam', r'D:\SteamLibrary',
              r'E:\Steam', r'E:\SteamLibrary', r'F:\SteamLibrary')]
    if os.name == 'nt':
        import winreg
        for hive, key in ((winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\Valve\Steam'),
                          (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Valve\Steam'),
                          (winreg.HKEY_CURRENT_USER, r'Software\Valve\Steam')):
            try:
                with winreg.OpenKey(hive, key) as handle:
                    for field in ('InstallPath', 'SteamPath'):
                        try:
                            value = winreg.QueryValueEx(handle, field)[0]
                            if isinstance(value, str) and value:
                                bases.append(Path(value))
                        except OSError:
                            continue
            except OSError:
                continue
    return _library_roots(_unique(base / 'steamapps' for base in bases))


def _library_roots(roots):
    extra = []
    for root in roots:
        try:
            vdf = root / 'libraryfolders.vdf'
            if vdf.stat().st_size > 4 * 1024 * 1024:
                continue
            text = vdf.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        for value in re.findall(r'"path"\s+"([^"\r\n]+)"', text, re.IGNORECASE):
            extra.append(Path(value.replace('\\\\', '\\')) / 'steamapps')
    return _unique(roots + extra)


def _nearby_dirs():
    # Unlike _MEIPASS, sys.executable points to the actual onefile EXE location.
    home = Path(sys.executable).absolute().parent if getattr(sys, 'frozen', False) else Path(__file__).absolute().parent
    return _unique([home, home.parent, home.parent.parent, Path.cwd()])


def find_game():
    candidates = []
    for root in _steam_roots():
        try:
            entries = list((root / 'common').iterdir())
        except OSError:
            continue
        for entry in entries:
            if 'cosmobreeder' in entry.name.lower() or 'yiffai' in entry.name.lower():
                candidates.append(entry)
    candidates.extend(_nearby_dirs())
    result = []
    for candidate in _unique(candidates):
        try:
            # SFW must not require patch.pak; source identity is checked separately.
            if (candidate.is_dir() and not candidate.is_symlink()
                    and candidate.resolve() == candidate
                    and (candidate / 'cosmobreeder-multi.jar').is_file()
                    and not (candidate / 'cosmobreeder-multi.jar').is_symlink()):
                result.append(candidate)
        except OSError:
            continue
    return result
