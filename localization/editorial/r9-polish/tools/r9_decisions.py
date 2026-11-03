"""Shared plumbing for the r9 decision tables.

The per-batch scripts differ only in their apply/reject calls; the mechanics
(reading the order, owning a row at most once, emitting the mechanical
trailing-space rows, refusing to drop an unhandled route finding) are the same
and live here so a rule only has to be fixed once.

Row-ownership rule: one decision per row. A finding that also strips a stray
trailing space keeps both edits in its own `final_zh`, so the mechanical pass
must skip rows a semantic decision already owns.

Trailing-space scope: the only criterion is whether the English source line
ends with whitespace. `catalog/occurrences.jsonl:trailing_ws` describes the
Chinese line and must never be used. Centred layout blocks (`ui.end*`,
`ui.backers`) are excluded explicitly by the caller, because their padding is a
layout device rather than a defect.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'
CATALOG = ROOT / 'localization/catalog'
COLUMNS = ('finding_id', 'route', 'severity', 'category', 'scene_id', 'row_id',
           'decision', 'final_zh', 'reason')

_occ = None
_units = None


def _load_sources():
    global _occ, _units
    if _occ is None:
        _occ, _units = {}, {}
        for line in (CATALOG / 'occurrences.jsonl').read_text('utf8').splitlines():
            if line.strip():
                d = json.loads(line)
                _occ[d['occurrence_id']] = d['unit_id']
        for line in (CATALOG / 'units.jsonl').read_text('utf8').splitlines():
            if line.strip():
                d = json.loads(line)
                _units[d['id']] = d['source']
    return _occ, _units


def trailing_trim(text):
    """Drop spaces/tabs at the end of a value, never a trailing newline.

    Interface rows keep their Chinese as one JSON string, so the whitespace
    that matters sits before the final `\n`; `str.rstrip()` would remove the
    newline too and change the JSON newline count, which the repair engine
    refuses.
    """
    if text.endswith('\n'):
        return text[:-1].rstrip(' 	') + '\n'
    return text.rstrip(' 	')


def source_of(row):
    """English source line for a row, or None when it cannot be traced."""
    occ, units = _load_sources()
    uid = occ.get(row['row_id'].replace('CAT:', ''))
    if uid and uid in units:
        return units[uid]
    src = row.get('source')
    return src if src else None


# Stands in for a real newline inside one TSV cell. U+240A (␊) never appears
# in game text, and keeps the cell single-line so the table stays readable.
SYMBOL_FOR_NEWLINE = '␊'


class Batch:
    def __init__(self, batch):
        self.batch = batch
        self.base = R9 / batch
        self.order = json.loads((self.base / 'orders' / (batch + '.json')).read_text('utf8'))
        self.rows = {}
        self.root_of = {}
        for scene in self.order['scenes']:
            for row in scene['rows']:
                self.rows[row['row_id']] = (scene['scene_id'], row)
                self.root_of[row['row_id']] = scene['root']
        self.lines = ['\t'.join(COLUMNS)]
        self.seen = set()
        self.taken = {}
        self.leftover = []

    def route(self, name):
        out = {}
        p = self.base / name / 'findings.jsonl'
        if p.exists():
            for line in p.read_text('utf8').splitlines():
                if line.strip():
                    f = json.loads(line)
                    out[f['finding_id']] = f
        return out

    def emit(self, key, route, severity, category, row_id, decision, final, reason):
        if row_id not in self.rows:
            # A rejected proposal may quote a row id that does not exist (a
            # mistyped id); it changes nothing, so record it instead of failing.
            if decision != 'apply':
                self.seen.add(key)
                self.lines.append('	'.join((key, route, severity, category, '', row_id,
                                             decision, '', reason)))
                return
            raise SystemExit('%s: unknown row %s' % (key, row_id))
        if key in self.seen:
            raise SystemExit('%s: planned twice' % key)
        self.seen.add(key)
        scene_id, row = self.rows[row_id]
        # A TSV cell holds one line, but a JSON value may contain real newlines.
        # Carry them as SYMBOL_FOR_NEWLINE and let the ledger builder expand it, so a
        # multi-line value can be edited instead of being rejected.
        final = final.replace(chr(10), SYMBOL_FOR_NEWLINE)
        if decision == 'apply':
            if not (row.get('current') or '').strip():
                raise SystemExit('%s: blank joined-tail row' % key)
            if row['current'] == final:
                raise SystemExit('%s: no-op' % key)
            if row_id in self.taken:
                raise SystemExit('%s: row owned by %s' % (key, self.taken[row_id]))
            self.taken[row_id] = key
        self.lines.append('\t'.join((key, route, severity, category, scene_id, row_id,
                                     decision, final, reason)))

    def apply_finding(self, route, fid, reason, final=None, severity=None):
        f = self.route(route).get(fid)
        if f is None:
            raise SystemExit('missing finding %s:%s' % (route, fid))
        text = final if final is not None else (f.get('proposed_zh') or '')
        if not text:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        self.emit(route + ':' + fid, route, severity or f.get('severity', ''),
                  f.get('category', ''), f['row_ids'][0], 'apply', text, reason)

    def trailing_space_rows(self, skip_roots=()):
        """Rows whose Chinese line ends in whitespace the English source lacks."""
        out = []
        for row_id, (scene_id, row) in self.rows.items():
            cur = row.get('current') or ''
            if not cur or row_id in self.taken:
                continue
            if any(self.root_of[row_id].startswith(p) for p in skip_roots):
                continue
            if trailing_trim(cur) == cur:
                continue
            src = source_of(row)
            if src is None or src != src.rstrip():
                continue
            out.append((row_id, cur))
        return out

    extra = {}

    def emit_trailing_space(self, skip_roots=(), reason=None):
        reason = reason or '中文行尾多出半角空格，英文原文行尾没有（按 unit 原文核对）。只删空格。'
        applied = deferred = 0
        for row_id, cur in self.trailing_space_rows(skip_roots):
            if chr(10) in cur[:-1]:
                # The value spans several lines, so the edit cannot be written as
                # one TSV cell. Say so instead of dropping the row silently.
                self.emit('R9M-' + row_id, 'R9M', 'C', 'format', row_id, 'reject', '',
                          '该行的中文是多行 JSON 值，行尾空格无法用行式裁决表表达；'
                          '本批不改，记入 LEFTOVERS 由清理批次处理。')
                deferred += 1
                continue
            self.emit('R9M-' + row_id, 'R9M', 'C', 'format', row_id, 'apply',
                      trailing_trim(cur), reason)
            applied += 1
        self.extra = {'trailing_space_applied': applied, 'trailing_space_deferred': deferred}
        return self.extra

    def reject(self, key, reason):
        route, fid = key.split(':', 1)
        f = self.route(route)[fid]
        self.emit(key, route, f.get('severity', ''), f.get('category', ''),
                  f['row_ids'][0], 'reject', '', reason)

    def close(self, manual_reject=None):
        """Reject every route finding not already decided, or fail loudly."""
        manual_reject = manual_reject or {}
        for route in ('gemini', 'ds'):
            for fid, f in self.route(route).items():
                key = route + ':' + fid
                if key in self.seen:
                    continue
                rid = f['row_ids'][0]
                if key in manual_reject:
                    self.reject(key, manual_reject[key])
                elif rid in self.taken:
                    self.reject(key, '与 %s 同一行同一处，取先落地的条目。' % self.taken[rid])
                else:
                    self.leftover.append(key)
        if self.leftover:
            raise SystemExit('unhandled route findings: ' + ', '.join(self.leftover))
        (self.base / 'review').mkdir(parents=True, exist_ok=True)
        path = self.base / 'review/decisions.tsv'
        path.write_text('\n'.join(self.lines) + '\n', encoding='utf8')
        counts = {}
        for line in self.lines[1:]:
            d = line.split('\t')[6]
            counts[d] = counts.get(d, 0) + 1
        return {'batch': self.batch, 'decisions': len(self.lines) - 1, **counts, **self.extra}
