"""Localize/join original JAR DS by real source/root matches, never PAK line offsets."""
from pathlib import Path
import collections
import hashlib
import json
import re
from projectlib import PROJECT, load_occurrences, load_units, current_translations, read_jsonl, glyph_metrics, validate_translation


def digest(data):return hashlib.sha256(data).hexdigest()


def split_line(line):
    eol='\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else '\r' if line.endswith('\r') else ''
    return (line[:-len(eol)] if eol else line),eol


def rewrite_sfw(logical_path, original_bytes, localized_bytes, records):
    original=original_bytes.decode('utf8').splitlines(keepends=True)
    localized=localized_bytes.decode('utf8').splitlines(keepends=True)
    if len(original)!=len(localized):raise ValueError('SFW physical line-count drift')
    units={u['id']:u for u in load_units()};translations=current_translations()
    occurrences=[o for o in load_occurrences() if o.get('logical_path')==logical_path and o['category']=='dialogue']
    # Reuse the canonical ledger validator before relocating any group to an
    # alternate source version. Never trust caller-supplied merged text alone.
    import dialogue_joins
    resource=next(r for r in read_jsonl(PROJECT/'catalog/resources.jsonl') if r['logical_path']==logical_path)
    canonical=(PROJECT/resource['blob_path']).read_bytes();virtual=dialogue_joins._split(canonical)
    for o in occurrences:
        text=translations.get(o['unit_id'],{}).get('draft','')
        if text:
            virtual[o['line']-1]=(o['prefix']+o['leading_ws']+text+o['trailing_ws']).encode('utf8')+dialogue_joins._body_eol(virtual[o['line']-1])[1]
    dialogue_joins.apply_joins(logical_path,canonical,b''.join(virtual),records=records)
    lookup=collections.defaultdict(list)
    for o in occurrences:
        u=units[o['unit_id']]
        lookup[(o['entry'],o['prefix'],o['leading_ws']+u['source']+o['trailing_ws'])].append(o)
    prefixes=sorted({o['prefix'] for o in occurrences},key=len,reverse=True)
    metrics=glyph_metrics();validated=set()
    headers=[];parsed=[];active='';changed=0
    for i,line in enumerate(original):
        body,eol=split_line(line)
        if re.fullmatch(r'<[^>]+>',body.strip()):active=body.strip()[1:-1]
        headers.append(active)
        match=next((p for p in prefixes if body.startswith(p)),None)
        parsed.append((match,body[len(match):]) if match else None)
        old_body,old_eol=split_line(localized[i])
        if eol!=old_eol:raise ValueError('SFW EOL drift')
        if not match:
            if body!=old_body:raise ValueError('SFW non-dialogue control/header drift')
            continue
        choices=lookup.get((active,match,body[len(match):]),[])
        texts={translations.get(o['unit_id'],{}).get('draft','') for o in choices}
        texts.discard('')
        if len(texts)>1:raise ValueError('Ambiguous SFW translation at '+str(i+1))
        if texts:
            o=choices[0];text=next(iter(texts))
            uid=o['unit_id']
            if uid not in validated:
                errors=[e for e in validate_translation(units[uid],text,metrics) if e[0]=='error']
                if errors:raise ValueError('SFW translation hard-QA failure: '+uid+' '+str(errors))
                validated.add(uid)
            value=match+o['leading_ws']+text+o['trailing_ws']+eol
            if value!=localized[i]:localized[i]=value;changed+=1
    report={'logical_path':logical_path,'original_sfw_sha256':digest(original_bytes),'input_sha256':digest(localized_bytes),
            'translated_by_exact_root_prefix_source':changed,'applied_groups':0,'removed_text_nodes':0,'groups':[],'skipped':[]}
    occupied=set()
    for record in records:
        if record['logical_path']!=logical_path:continue
        prefix=record['prefix'];n=len(record['inputs']);expected=[]
        for item in record['inputs']:
            u=units[item['unit_id']]
            source_o=next(o for o in occurrences if o['occurrence_id']==item['occurrence_id'])
            expected.append((prefix,source_o['leading_ws']+u['source']+source_o['trailing_ws']))
        candidates=[i for i in range(len(original)-n+1)
                    if headers[i]==record['full_header'].strip()[1:-1]
                    and all(headers[i+j]==headers[i] and parsed[i+j]==expected[j] for j in range(n))]
        if len(candidates)!=1:
            report['skipped'].append({'join_id':record['join_id'],'reason':'source-version mismatch or ambiguous source group','matches':len(candidates)});continue
        i=candidates[0]
        if occupied.intersection(range(i,i+n)):raise ValueError('Overlapping SFW source group')
        for j,item in enumerate(record['inputs']):
            o=next(o for o in occurrences if o['occurrence_id']==item['occurrence_id'])
            if split_line(localized[i+j])[0]!=prefix+o['leading_ws']+item['input_translation']+o['trailing_ws']:
                raise ValueError('SFW target input translation drift')
        first_o=next(o for o in occurrences if o['occurrence_id']==record['inputs'][0]['occurrence_id'])
        localized[i]=prefix+first_o['leading_ws']+record['merged_translation']+first_o['trailing_ws']+split_line(original[i])[1]
        for j in range(1,n):localized[i+j]=split_line(original[i+j])[1]
        occupied.update(range(i,i+n));report['applied_groups']+=1;report['removed_text_nodes']+=n-1
        report['groups'].append({'join_id':record['join_id'],'actual_sfw_lines':list(range(i+1,i+n+1)),
                                 'canonical_occurrences':[x['occurrence_id'] for x in record['inputs']]})
    output=''.join(localized).encode('utf8');report['output_sha256']=digest(output)
    return output,report
