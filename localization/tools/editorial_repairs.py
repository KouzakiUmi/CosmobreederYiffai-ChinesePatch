"""Source-locked editorial operations. Pure bytes in/out; never opens archives.

A rejected operation raises EditorialRepairError before any result is emitted.
The caller owns semantic approval, ledger loading, decryption and persistence.
"""
from collections import Counter, defaultdict
from hashlib import sha256
import json
import re


class EditorialRepairError(ValueError):
    pass


ARCHIVES = frozenset(('cosmobreeder-multi.jar', 'patch.pak'))
ENTRY = re.compile(r'(datadf|datadm|vsn|datav|datay)/[1-9][0-9]*\Z')
DS = re.compile(r'^(\s*\*\s?|\s*[^<>{}#*\s][^:]{0,40}:\s?)(.*)$')
VSN = re.compile(r'^(\s*(?:text|lang\([^)]*\)|auto\([^)]*\))\s*:\s?)(.*)$')
# Deliberately no numeric/percent heuristic: 50% math is ordinary prose.
MARKERS = re.compile(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:[1-9]\d*\$)?(?:[-+#0]*\d*(?:\.\d+)?)?[sdifouxXeEgGc](?![A-Za-z])|</?[A-Za-z][^<>\r\n]*>|\|')
FIELDS = {'op_id', 'archive', 'archive_entry', 'kind', 'before_resource_sha256',
          'old', 'new', 'finding_ids', 'source_refs'}


def _fail(message):
    raise EditorialRepairError(message)


def _markers(text):
    markers = Counter(MARKERS.findall(text))
    # Engine IDs (not ordinary numbers or percent mathematics) remain literal.
    markers.update(re.findall(r'(?<![A-Za-z0-9_])(?:[A-Za-z]+[0-9][A-Za-z0-9_-]*|[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+)(?![A-Za-z0-9_])', text))
    return markers


LINE_BREAK = '\u2028'


def _safe_string(text, *, json_value=False, line_row=False):
    # `line_row` admits U+2028 only. The engine treats it as an explicit line
    # break (`PixelLayout`), but this toolchain does not split rows on it, so
    # row numbering — and every ledger that references a row number — stays
    # intact. LF stays banned for exactly that reason: inserting one renumbers
    # every following row and invalidates the ledgers.
    #
    # U+2028 is admitted *only* for line rows. It must not leak into JSON values:
    # there the newline rule compares counts, so a value could gain a break while
    # also having its text edited. `json` keeps the global ban.
    if json_value:
        banned = '\x85\u2028\u2029'
        allowed = '\r\n'
    elif line_row:
        banned = '\x85\u2029'
        allowed = '\t' + LINE_BREAK
    else:
        banned = '\x85\u2028\u2029'
        allowed = '\t'
    if not isinstance(text, str) or any(ord(c) < 32 and c not in allowed or c in banned for c in text):
        _fail('string/control/newline violation')


def _json_tokens(text):
    """Validate full JSON and collect value token spans, never key spans."""
    decoder = json.JSONDecoder()
    tokens = {}
    def ws(i):
        while i < len(text) and text[i] in ' \t\r\n':
            i += 1
        return i
    def parse(i, path):
        i = ws(i)
        start = i
        if text[i:i+1] == '{':
            i = ws(i+1)
            seen = set()
            if text[i:i+1] == '}':
                return i+1
            while True:
                if text[i:i+1] != '"': _fail('JSON object key')
                key, i = decoder.raw_decode(text, i)
                if key in seen: _fail('duplicate JSON key')
                seen.add(key)
                i = ws(i)
                if text[i:i+1] != ':': _fail('JSON colon')
                i = ws(parse(i+1, path + (key,)))
                if text[i:i+1] == '}': return i+1
                if text[i:i+1] != ',': _fail('JSON object separator')
                i = ws(i+1)
        if text[i:i+1] == '[':
            i = ws(i+1)
            if text[i:i+1] == ']': return i+1
            n = 0
            while True:
                i = ws(parse(i, path + (str(n),)))
                n += 1
                if text[i:i+1] == ']': return i+1
                if text[i:i+1] != ',': _fail('JSON array separator')
                i = ws(i+1)
        value, end = decoder.raw_decode(text, i)
        if not isinstance(value, (str, int, float, bool, type(None))): _fail('JSON scalar')
        tokens[path] = (start, end, value)
        return end
    try:
        end = ws(parse(0, ()))
        if end != len(text): _fail('JSON trailing data')
        # Reject nonstandard NaN/Infinity, including nested values.
        json.loads(text, parse_constant=lambda _: _fail('nonfinite JSON'))
    except (ValueError, IndexError, RecursionError) as exc:
        if isinstance(exc, EditorialRepairError): raise
        raise EditorialRepairError('invalid JSON') from exc
    return tokens


def _pointer(pointer):
    if not isinstance(pointer, str) or (pointer and not pointer.startswith('/')):
        _fail('invalid JSON pointer')
    if re.search(r'~(?![01])', pointer): _fail('invalid pointer escape')
    return tuple(p.replace('~1', '/').replace('~0', '~') for p in pointer[1:].split('/')) if pointer else ()


def _line_role(body, family):
    if family == 'vsn':
        match = VSN.fullmatch(body)
    else:
        if re.match(r'^\s*(?:<|#|include\b|if\b|else\b|do\b|[{}])', body): return None
        match = DS.fullmatch(body)
    return match.groups() if match else None


def apply_entry(archive: str, entry: str, data: bytes, operations: list[dict]):
    """Preflight every operation against the same original resource, then splice.

    Identical duplicate targets are coalesced (reported once); conflicting targets
    and duplicate op_ids are errors. An unchanged/no-op operation is rejected.
    """
    if archive not in ARCHIVES or not isinstance(entry, str) or not ENTRY.fullmatch(entry):
        _fail('archive/entry outside editable text scope')
    if not isinstance(data, bytes) or not isinstance(operations, list): _fail('bytes/list required')
    digest = sha256(data).hexdigest()
    try: text = data.decode('utf8')
    except UnicodeDecodeError as exc: raise EditorialRepairError('not UTF-8 text') from exc
    family = entry.split('/')[0]
    expected_kind = 'json' if family in ('datav', 'datay') else 'line'
    ids, targets, edits, applied = set(), {}, [], []
    lines = re.findall(r'[^\r\n]*(?:\r\n|\r|\n|\Z)', text)
    if lines and lines[-1] == '': lines.pop()
    bodies = [re.sub(r'(?:\r\n|\r|\n)\Z', '', line) for line in lines]
    offsets, offset = [], 0
    segments, segment, previous_prefix = {}, 0, None
    for n, line in enumerate(lines):
        offsets.append(offset); offset += len(line)
        role = _line_role(bodies[n], family)
        if role is None:
            if bodies[n].strip():
                segment += 1
                previous_prefix = None
        elif role[0] != previous_prefix:
            segment += 1
            previous_prefix = role[0]
        # Blank consumed join tails do not create events or reset the actor.
        segments[n+1] = segment
    tokens = _json_tokens(text) if expected_kind == 'json' else {}
    before_markers, after_markers = defaultdict(Counter), defaultdict(Counter)
    for op in operations:
        if not isinstance(op, dict) or not FIELDS <= op.keys(): _fail('missing operation fields')
        kind = op['kind']
        if kind != expected_kind: _fail('kind/resource mismatch')
        locator = 'line' if kind == 'line' else 'pointer'
        if set(op) != FIELDS | {locator}: _fail('unexpected operation fields')
        if not isinstance(op['op_id'], str) or not op['op_id'] or op['op_id'] in ids: _fail('invalid/duplicate op_id')
        ids.add(op['op_id'])
        if op['archive'] != archive or op['archive_entry'] != entry: _fail('operation archive/entry mismatch')
        if op['before_resource_sha256'] != digest: _fail('whole-resource SHA drift')
        for field in ('finding_ids', 'source_refs'):
            if not isinstance(op[field], list) or not op[field] or any(not isinstance(x, str) or not x for x in op[field]):
                _fail('missing provenance: ' + field)
        old, new = op['old'], op['new']
        _safe_string(old, json_value=kind == 'json', line_row=kind == 'line')
        _safe_string(new, json_value=kind == 'json', line_row=kind == 'line')
        if kind == 'json' and any(old.count(c) != new.count(c) for c in '\r\n'):
            _fail('JSON newline count drift')
        if kind == 'line' and new.count(LINE_BREAK) != old.count(LINE_BREAK):
            # A row may gain explicit breaks so a continuation line stops opening
            # on punctuation, but the breaks must be the only structural change:
            # removing them has to give back the old text verbatim.
            if new.replace(LINE_BREAK, '') != old:
                _fail('line break insertion must not alter the text')
        if old == new: _fail('no-op operation')
        if kind == 'line':
            n = op['line']
            if type(n) is not int or not 1 <= n <= len(lines): _fail('line out of range')
            if bodies[n-1] != old: _fail('old physical line mismatch')
            a, b = _line_role(old, family), _line_role(new, family)
            if a is None or b is None or a[0] != b[0]: _fail('control/actor/command prefix drift')
            if not a[1].strip() or not b[1].strip(): _fail('blank joined-tail/new join forbidden')
            start, end = offsets[n-1], offsets[n-1] + len(old)
            group = segments[n]
            target = n
        else:
            target = _pointer(op['pointer'])
            if target and (re.fullmatch(r'(?i)(?:id|.*_id|uuid|guid|internal_?id)', target[-1]) or re.fullmatch(r'.+Id', target[-1])):
                _fail('internal ID field protected')
            if target not in tokens: _fail('pointer is not scalar value')
            start, end, value = tokens[target]
            if not isinstance(value, str): _fail('non-string JSON token protected')
            if value != old: _fail('old JSON value mismatch')
            if _markers(old) != _markers(new): _fail('JSON marker drift')
            group = target
        if target in targets:
            if targets[target] != new: _fail('conflicting duplicate target')
            continue
        targets[target] = new
        before_markers[group].update(_markers(old)); after_markers[group].update(_markers(new))
        replacement = json.dumps(new, ensure_ascii=False) if kind == 'json' else new
        edits.append((start, end, replacement))
        applied.append(op['op_id'])
    if before_markers != after_markers: _fail('segment marker multiset drift')
    result = text
    for start, end, replacement in sorted(edits, reverse=True):
        result = result[:start] + replacement + result[end:]
    output = result.encode('utf8')
    return output, {'archive': archive, 'archive_entry': entry,
                    'before_resource_sha256': digest, 'after_resource_sha256': sha256(output).hexdigest(),
                    'operations_applied': applied, 'targets_changed': len(edits)}


def apply_entries(entries: dict, operations: list[dict]):
    """All-entry preflight. entries maps (archive, entry) to plaintext bytes.

    Returns a new mapping and reports; never mutates inputs or emits partial data.
    """
    grouped = defaultdict(list)
    ids = set()
    for op in operations:
        if not isinstance(op, dict) or not isinstance(op.get('op_id'), str): _fail('invalid operation')
        if op['op_id'] in ids: _fail('duplicate op_id across entries')
        ids.add(op['op_id'])
        key = (op.get('archive'), op.get('archive_entry'))
        if key not in entries: _fail('missing source entry')
        grouped[key].append(op)
    output, reports = dict(entries), []
    for (archive, entry), ops in grouped.items():
        output[(archive, entry)], report = apply_entry(archive, entry, entries[(archive, entry)], ops)
        reports.append(report)
    return output, reports
