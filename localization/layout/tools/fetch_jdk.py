"""Fetch the user-authorized, project-local Microsoft JDK; never set PATH."""
from pathlib import Path
import hashlib
import json
import re
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[3]
TARGET = ROOT / 'localization' / 'toolchains' / 'microsoft-jdk17'
URL = 'https://aka.ms/download-jdk/microsoft-jdk-17.0.20.1-windows-x64.zip'


def main():
    if TARGET.exists():
        raise ValueError('Refuse existing toolchain directory: ' + str(TARGET))
    TARGET.mkdir(parents=True)
    checksum_url = URL + '.sha256sum.txt'
    with urllib.request.urlopen(checksum_url, timeout=60) as response:
        checksum = response.read().decode('utf-8')
    match = re.search(r'\b[0-9a-fA-F]{64}\b', checksum)
    if not match:
        raise ValueError('Official SHA256 not found')
    expected = match.group().lower()
    archive = TARGET / 'jdk.zip'
    digest = hashlib.sha256()
    with urllib.request.urlopen(URL, timeout=120) as response, archive.open('xb') as output:
        final_url = response.url
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)
            digest.update(chunk)
    if digest.hexdigest() != expected:
        raise ValueError('JDK checksum mismatch; do not extract')
    with zipfile.ZipFile(archive) as source:
        for entry in source.infolist():
            path = TARGET / entry.filename
            if not path.resolve().is_relative_to(TARGET.resolve()):
                raise ValueError('Archive path escapes toolchain directory')
        source.extractall(TARGET)
    javacs = list(TARGET.glob('*/bin/javac.exe'))
    if len(javacs) != 1:
        raise ValueError('Expected one compiler')
    metadata = {'download_url': URL, 'final_url': final_url,
                'checksum_url': checksum_url, 'sha256': expected,
                'java_home': str(javacs[0].parents[1].relative_to(ROOT)),
                'system_install': False, 'path_modified': False}
    (TARGET / 'download-manifest.json').write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
