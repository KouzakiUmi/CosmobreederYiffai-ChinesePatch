# Editorial repair API

`localization/tools/editorial_repairs.py` is a pure UTF-8 plaintext bytes transformer.
It does not load ledgers, decrypt/encrypt, open archives or select editorial wording.
`component.json` binds the reviewed `localization/translations/editorial-r2-repairs.jsonl`
ledger, full source-validation manifest and independent semantic closure. The build
rechecks their hashes and all evidence; it does not infer approval from a candidate directory name.

## Integration

Call `apply_entry(archive, entry, data, operations)` after the existing SFW/VSN
processing and before final text collection/font generation. `data` must be the
candidate4 baseline plaintext for the exact archive and entry. Every operation's
`before_resource_sha256` is checked against those **original complete bytes**;
all operations for one resource must be passed together, not applied sequentially.
The result is `(new_bytes, report)`; errors raise `EditorialRepairError` without
emitting partial output. `apply_entries` accepts a mapping of `(archive, entry)`
to plaintext bytes and performs whole-batch validation before returning a new
mapping and reports. No input is mutated.

Only exact archive names `cosmobreeder-multi.jar` and `patch.pak` and numeric,
positive entries in `datadf`, `datadm`, `vsn`, `datav`, `datay` are accepted.
DS/VSN operations are physical-line operations; datav/datay use JSON pointers.
`finding_ids` and `source_refs` are nonempty lists of nonempty reference strings.
Operations contain the fixed common fields plus exactly `line` or `pointer`.
Duplicate op IDs are errors. Identical duplicate targets with distinct op IDs
are coalesced; conflicting replacements are errors. No-ops are rejected.

## Protection boundaries

Physical EOL bytes and every untargeted byte remain unchanged. Empty joined-tail
lines cannot become new text events, nor can nonempty dialogue become empty.
DS actor and VSN text/lang/auto prefixes are exact-match protected. Other lines
are control barriers, not editorial targets. Placeholder/markup multisets may
move across edited text lines only in the same contiguous control-free segment
with an identical actor/command prefix. Actor changes, command parameter changes
and control events start new segments; consumed blank join tails do not create
events. JSON placeholders are conserved per string.
ASCII alphanumeric-number/underscore identifiers are protected, as are JSON
fields named id, *_id, *Id, uuid, guid or internal_id. This is a structural guard,
not an exhaustive semantic classifier of arbitrary game-specific ID values:
the editor must not approve operations that change other internal identifiers.
Numbers and percent arithmetic are not treated as placeholders.

JSON replacement uses exact string-token spans. Other whitespace, key tokens,
Unicode escapes outside edited tokens and non-string values are untouched.
Duplicate keys anywhere, nonstandard NaN/Infinity, invalid pointer escapes,
missing pointers, key/container targets and non-string targets are rejected.
Edited strings are serialized with `ensure_ascii=False`; original spelling of
escapes within an edited token is not retained. JSON string values may retain
existing CR/LF characters only when each character's old/new count is identical;
serialization escapes them without changing physical resource lines. Other JSON
control characters are rejected. Physical-line edits cannot contain CR/LF;
Unicode line separators are rejected in both modes. This conservative engine has no global Tomcat
replacement and no independent translation/approval rules.

## Isolated tests

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s localization/tests -p test_editorial_repairs.py -v
```

This exercises only in-memory synthetic resources. Formal ledger application,
real candidate4 SHA pins, archive rebuild and game acceptance belong to integration.
