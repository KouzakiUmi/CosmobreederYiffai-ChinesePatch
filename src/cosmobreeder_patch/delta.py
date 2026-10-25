"""Bounded COPY/source-dependent XOR delta. No complete target is embedded."""
import hashlib
import os
import struct
import zlib
from pathlib import Path

BLOCK = 65536
MAGIC = b'CBDELTA1'
MAX_FILE = 256 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024
MAX_OPS = 65536

def validate_entry(entry):
    if not isinstance(entry, dict):
        raise ValueError('差分条目必须为对象')
    for field in ('source_size', 'target_size', 'delta_size'):
        value = entry.get(field)
        minimum = BLOCK if field == 'source_size' else 1
        if type(value) is not int or not minimum <= value <= MAX_FILE:
            raise ValueError('差分大小字段无效: ' + field)
    for field in ('source_sha256', 'target_sha256', 'delta_sha256'):
        value = entry.get(field)
        if not isinstance(value, str) or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
            raise ValueError('差分SHA字段无效')

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def build(source, target, output):
    if not BLOCK <= Path(source).stat().st_size <= MAX_FILE or not 1 <= Path(target).stat().st_size <= MAX_FILE:
        raise ValueError('构建源/目标大小越界')
    index = {}
    with open(source, 'rb') as f:
        offset = 0
        for b in iter(lambda: f.read(BLOCK), b''):
            index.setdefault(hashlib.sha256(b).digest(), (offset, len(b)))
            offset += len(b)
    copied = 0
    with open(target, 'rb') as t, open(output, 'wb') as out:
        out.write(MAGIC)
        for b in iter(lambda: t.read(BLOCK), b''):
            match = index.get(hashlib.sha256(b).digest())
            if match:
                out.write(b'C' + struct.pack('>QI', *match))
                copied += len(b)
            else:
                # XOR against the cyclic source: every literal needs the user's source.
                with open(source, 'rb') as original:
                    original.seek((t.tell() - len(b)) % Path(source).stat().st_size)
                    base = original.read(len(b))
                    if len(base) < len(b):
                        original.seek(0)
                        base += original.read(len(b) - len(base))
                if len(base) != len(b):
                    raise ValueError('源文件必须至少包含一个完整块')
                data = zlib.compress(bytes(x ^ y for x, y in zip(b, base)), 9)
                out.write(b'X' + struct.pack('>II', len(b), len(data)) + data)
        out.write(b'E')
    return {'source_sha256': sha(source), 'target_sha256': sha(target),
            'source_size': Path(source).stat().st_size, 'target_size': Path(target).stat().st_size,
            'delta_sha256': sha(output), 'delta_size': Path(output).stat().st_size, 'copy_bytes': copied}

def apply(source, delta, output, entry):
    validate_entry(entry)
    if Path(source).stat().st_size != entry['source_size'] or Path(delta).stat().st_size != entry['delta_size']:
        raise ValueError('源或差分尺寸不匹配')
    if sha(source) != entry['source_sha256'] or sha(delta) != entry['delta_sha256']:
        raise ValueError('源文件或差分SHA不匹配')
    size = 0
    def exact(f, n):
        b = f.read(n)
        if len(b) != n:
            raise ValueError('截断的差分')
        return b
    with open(source, 'rb') as s, open(delta, 'rb') as d, open(output, 'wb') as out:
        if exact(d, 8) != MAGIC:
            raise ValueError('差分格式无效')
        operations = 0
        while True:
            operations += 1
            if operations > MAX_OPS + 1:
                raise ValueError('差分指令数越界')
            op = exact(d, 1)
            if op == b'E':
                if d.read(1):
                    raise ValueError('差分尾部数据')
                break
            if operations > MAX_OPS:
                raise ValueError('差分指令数越界')
            if op == b'C':
                offset, n = struct.unpack('>QI', exact(d, 12))
                if not 0 < n <= BLOCK or offset + n > entry['source_size']:
                    raise ValueError('COPY越界')
                s.seek(offset)
                b = exact(s, n)
            elif op == b'X':
                n, compressed = struct.unpack('>II', exact(d, 8))
                if not 0 < n <= BLOCK or compressed > BLOCK + 1024:
                    raise ValueError('literal越界')
                decoder = zlib.decompressobj()
                b = decoder.decompress(exact(d, compressed), n + 1)
                if len(b) != n or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
                    raise ValueError('literal压缩流无效')
                s.seek(size % entry['source_size'])
                base = s.read(n)
                if len(base) < n:
                    s.seek(0)
                    base += s.read(n - len(base))
                if len(base) != n:
                    raise ValueError('源文件过短')
                b = bytes(x ^ y for x, y in zip(b, base))
            else:
                raise ValueError('未知差分指令')
            size += len(b)
            if size > entry['target_size']:
                raise ValueError('输出越界')
            out.write(b)
        out.flush()
        os.fsync(out.fileno())
    if size != entry['target_size'] or sha(output) != entry['target_sha256']:
        raise ValueError('重建目标SHA不匹配')
