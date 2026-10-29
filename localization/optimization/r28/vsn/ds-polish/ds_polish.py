"""Pure, exact-identity text polish over already-joined frozen r27 PAK DS.

No regex replacement over unknown scripts; no canonical, archive or SFW writes.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
HEADER=re.compile(r'^<[^<>\r\n]+>[ \t]*$')


class DsPolishValidationError(ValueError):
    """Atomic fail-closed: no partial new bytes/report is returned."""


def sha(data):return hashlib.sha256(data).hexdigest()


def require(ok,message):
    if not ok:raise DsPolishValidationError(message)


def split(data):
    require(isinstance(data,bytes),'Expected immutable plaintext bytes')
    try:data.decode('utf8')
    except UnicodeDecodeError as exc:raise DsPolishValidationError('Invalid UTF-8') from exc
    return re.findall(rb'[^\r\n]*(?:\r\n|\r|\n|$)',data)[:-1]


def body_eol(line):
    for e in (b'\r\n',b'\n',b'\r'):
        if line.endswith(e):return line[:-len(e)],e
    return line,b''


def markers(text):
    return {'placeholders':Counter(re.findall(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:\d+\$)?[-+#0 ]*\d*(?:\.\d+)?[sdifouxXeEgGc%]',text)),
            'angle_tags':Counter(re.findall(r'<[^<>\r\n]*>',text)),
            'underscores':Counter(re.findall(r'_+',text)),
            'square_open':text.count('['),'square_close':text.count(']'),
            'pipes':text.count('|'),'newlines':text.count('\n'),
            'hearts':text.count('<3'),'stars':text.count('*'),'slash':text.count('/')}


def load_data():
    manifest=json.loads((HERE/'component_ds.json').read_text('utf8'))
    raw=(HERE/'operations.jsonl').read_bytes()
    require(sha(raw)==manifest['operations_sha256'],'Derived DS polish ledger SHA mismatch')
    return manifest,[json.loads(row) for row in raw.decode('utf8').splitlines() if row]


def rewrite_ds_polish(logical_path,r27_plain_bytes,archive='patch.pak'):
    """Return (new_plain_bytes, report), without writing or partially applying.

    Only datadf/all.ds and datadm/all.ds frozen r27 PAK plaintext are accepted.
    Input has ALREADY had canonical 956 DS joins applied in r27. Do not call
    canonical joins or apply translations before this routine. Whole-file SHA,
    header, exact prefix/old line, occurrence/source evidence and markup all
    preflight before constructing output. SFW has a separate independent source.
    """
    manifest,records=load_data()
    require(archive=='patch.pak','Archive identity mismatch: PAK only; SFW needs its own ledger')
    require(logical_path in manifest['resources'],'Unknown pinned DS resource identity')
    pin=manifest['resources'][logical_path]
    require(isinstance(r27_plain_bytes,bytes) and sha(r27_plain_bytes)==pin['r27_plaintext_sha256'],
            'Frozen r27 already-joined resource SourceSHA mismatch')
    before=split(r27_plain_bytes)
    require(len(before)==pin['physical_line_count'],'Physical line count mismatch')
    context={};header=None;header_line=None
    for n,raw in enumerate(before,1):
        text=body_eol(raw)[0].decode('utf8')
        if HEADER.fullmatch(text):header=text;header_line=n
        context[n]=(header_line,header)
    chosen=[r for r in records if r['logical_path']==logical_path]
    plans=[];seen=set();lines=set()
    for row in chosen:
        rid=row.get('operation_id');n=row.get('line')
        require(row.get('schema_version')==1 and row.get('archive')==archive,'Operation schema/archive mismatch')
        require(isinstance(rid,str) and rid and rid not in seen,'Duplicate operation identity')
        seen.add(rid)
        require(type(n) is int and 1<=n<=len(before) and n not in lines,'Invalid/overlapping physical line')
        lines.add(n)
        require(row['source_resource_sha256']==sha(r27_plain_bytes),'Operation resource SHA mismatch')
        require(context[n]==(row['header_line'],row['full_header']),'Header/branch identity mismatch')
        body,end=body_eol(before[n-1]);old=body.decode('utf8')
        require(sha(body)==row['input_line_sha256'] and old==row['input_line'],'Exact old text/prefix mismatch')
        prefix=row['prefix']
        require(isinstance(prefix,str) and re.fullmatch(r'[ \t]*(?:\* |[A-Za-z][A-Za-z0-9_]*(?:/[A-Za-z][A-Za-z0-9_]*)?: )',prefix)
                and old.startswith(prefix),'Not an exact dialogue prefix')
        require(old[len(prefix):].strip()==row['old_text'],'Pinned old payload mismatch')
        text=row['replacement'];out=row['output_line']
        require(isinstance(text,str) and text.strip()==text and re.search(r'[\u3400-\u9fff]',text),'Invalid Chinese replacement')
        require(not any(ord(c)<32 or c in '\u2028\u2029' for c in text) and '<p>' not in text and '|' not in text,
                'Replacement delimiter/control injection')
        require(sha(text.encode('utf8'))==row['replacement_sha256'],'Replacement SHA mismatch')
        payload=old[len(prefix):]
        leading=payload[:len(payload)-len(payload.lstrip())];trailing=payload[len(payload.rstrip()):]
        require(out==prefix+leading+text+trailing,'Output prefix/edge whitespace drift')
        require(markers(row['old_text'])==markers(text),'Inline marker/placeholder conservation mismatch')
        require(row['inputs'] and all(i['occurrence_id'] and i['unit_id'] and
                sha(i['source_en'].encode('utf8'))==i['source_sha256'] for i in row['inputs']),
                'Occurrence/source evidence mismatch')
        edits=row['text_edits']
        require(''.join(e['before'] for e in edits)==row['old_text'] and ''.join(e['after'] for e in edits)==text,
                'Reviewed edit evidence mismatch')
        plans.append((row,out.encode('utf8')+end))
    # Every check above precedes any rewritten output copy.
    output=before[:]
    for row,raw in plans:output[row['line']-1]=raw
    result=b''.join(output)
    require(len(split(result))==len(before),'Output physical structure drift')
    require(all(before[n-1]==output[n-1] for n in range(1,len(before)+1) if n not in lines),
            'Unrelated source/control bytes changed')
    report={'archive':archive,'logical_path':logical_path,'input_sha256':sha(r27_plain_bytes),
            'output_sha256':sha(result),'applied_revisions':len(plans),'physical_line_count':len(before),
            'removed_text_nodes':0,'control_or_timing_changes':0,
            'operations':[row['operation_id'] for row,_ in plans],
            'occurrence_mapping':[{'operation_id':row['operation_id'],'output_line':row['line'],
                 'canonical_join_id':row['canonical_join_id'],
                 'source_occurrence_ids':[i['occurrence_id'] for i in row['inputs']]} for row,_ in plans]}
    return result,report
