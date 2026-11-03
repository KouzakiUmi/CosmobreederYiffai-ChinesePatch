"""Resolve a batch row to the archive resource, locator and current text.

Two row shapes exist. Dialogue/VSN rows carry a physical `line` inside one text
entry. Dictionary/interface rows are scalar values inside `datav/1`, so they
carry no line; their locator is a JSON pointer taken from the occurrence catalog
(`json_key`), and the archive is still chosen by the row's `mode`.

The pointer is validated against the actual resource before use: if the value at
the pointer is not the row's `current` text, the caller reports baseline drift
instead of guessing.
"""
from pathlib import Path
from hashlib import sha256
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
CATALOG = LOC / 'catalog'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

MODE_ARCHIVE = {'sfw': 'cosmobreeder-multi.jar', 'nsfw': 'patch.pak'}

_occ = None


def occurrences():
    global _occ
    if _occ is None:
        _occ = {}
        for line in (CATALOG / 'occurrences.jsonl').read_text('utf8').splitlines():
            if line.strip():
                d = json.loads(line)
                _occ[d['occurrence_id']] = d
    return _occ


def pointer_of(json_key):
    """JSON pointer for a dictionary key. The asset is a flat map, so the key
    (dots included) is one segment; only `~` and `/` need escaping."""
    return '/' + json_key.replace('~', '~0').replace('/', '~1')


def resolve(document, pointer):
    value = document
    for part in pointer.strip('/').split('/'):
        value = value[part]
    return value


_doc_cache = {}


def _document(candidate, archive, entry):
    key = (str(candidate), archive, entry)
    if key not in _doc_cache:
        raw = read_resource(candidate, archive, entry)
        _doc_cache[key] = json.loads(raw.decode('utf8'))
    return _doc_cache[key]


def _pointer_by_value(candidate, archive, entry, root, value):
    """Fallback for SFW-numbered rows: the asset is a flat map, so the entry is
    the key whose value is exactly this row's text, narrowed by the scene root.

    The recorded root is a location, not a key: dictionary keys drop the
    `/patchDictionary/` prefix (`/patchDictionary/navmap.AreaB` is stored as
    `navmap.AreaB...`), so compare on suffix as well as prefix before insisting
    the match is unique."""
    document = _document(candidate, archive, entry)
    hits = [k for k, v in document.items() if isinstance(v, str) and v == value]
    if len(hits) > 1:
        tail = root.lstrip('/').replace('patchDictionary/', '')
        narrowed = [k for k in hits if k.startswith(tail) or tail.startswith(k) or k in root]
        hits = narrowed or hits
    if len(hits) != 1:
        raise ValueError('cannot resolve %r under %r: %d candidates %r'
                         % (value, root, len(hits), hits[:5]))
    return pointer_of(hits[0])


def target_of(row, mode, candidate, root):
    """(archive, entry, kind, locator_name, locator) for one row."""
    archive = MODE_ARCHIVE[mode]
    if row.get('line') is not None:
        return archive, row['archive_entry'], 'line', 'line', row['line']
    occ = occurrences().get(row['row_id'].replace('CAT:', ''))
    if occ and occ.get('json_key'):
        return archive, occ['archive_entry'], 'json', 'pointer', pointer_of(occ['json_key'])
    entry = row.get('archive_entry') or 'datav/1'
    value = row.get('current')
    return archive, entry, 'json', 'pointer', _pointer_by_value(candidate, archive, entry, root, value)


def read_resource(candidate, archive, entry):
    with zipfile.ZipFile(candidate / archive) as z:
        raw = decrypt_file(z.read(entry))
    return raw


def line_bodies(raw):
    import re
    lines = re.findall(r'[^\r\n]*(?:\r\n|\r|\n|\Z)', raw.decode('utf8'))
    if lines and lines[-1] == '':
        lines.pop()
    return [line.rstrip('\r\n') for line in lines]


def resource_state(candidate, archive, entry, kind):
    """(locator_lookup, digest) for one entry, parsed for line or JSON assets."""
    raw = read_resource(candidate, archive, entry)
    digest = sha256(raw).hexdigest()
    text = raw.decode('utf8')
    if kind == 'json':
        return {'document': json.loads(text)}, digest
    return {'lines': line_bodies(raw)}, digest


def old_text(state, kind, locator, row):
    if kind == 'json':
        return resolve(state['document'], locator)
    return state['lines'][locator - 1]
