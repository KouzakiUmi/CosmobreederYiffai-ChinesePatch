"""Shared, deterministic localization data formats. No game-install writes."""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import os
import uuid

PROJECT = Path(__file__).resolve().parents[1]
STATES = ('untranslated', 'draft', 'reviewed', 'approved', 'blocked')
PLACEHOLDER = re.compile(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:\d+\$)?[-+#0 ]*\d*(?:\.\d+)?[sdifouxXeEgGc%]')


def digest(data): return hashlib.sha256(data).hexdigest()
def stable_id(prefix, *parts):
    return prefix + digest(json.dumps(parts, ensure_ascii=False, separators=(',', ':')).encode('utf8'))[:20]
def read_json(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def atomic_text(path,text):
    target=Path(path).resolve()
    if not target.is_relative_to(PROJECT.resolve()):raise ValueError('Project writes must stay inside the project')
    target.parent.mkdir(parents=True,exist_ok=True)
    temp=target.with_name('.'+target.name+'.'+uuid.uuid4().hex+'.tmp')
    with temp.open('x',encoding='utf8',newline='\n') as f:f.write(text)
    # Verify both absolute paths before the atomic move; no install path is allowed.
    assert temp.resolve().parent==target.parent and target.is_relative_to(PROJECT.resolve())
    os.replace(temp,target)
def write_json(path, data):
    atomic_text(path,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def read_jsonl(path):
    with Path(path).open(encoding='utf-8-sig') as f:
        return [json.loads(line) for line in f if line.strip()]
def write_jsonl(path, rows):
    atomic_text(path,''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows))

def pointer_get(data,pointer):
    value=data
    for key in pointer.lstrip('/').split('/'):
        key=key.replace('~1','/').replace('~0','~')
        value=value[int(key)] if isinstance(value,list) else value[key]
    return value

def pointer_set(data,pointer,value):
    keys=[k.replace('~1','/').replace('~0','~') for k in pointer.lstrip('/').split('/')]
    parent=data
    for key in keys[:-1]:parent=parent[int(key)] if isinstance(parent,list) else parent[key]
    key=keys[-1]
    if isinstance(parent,list):parent[int(key)]=value
    else:parent[key]=value
def write_csv(path, rows, columns):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=columns,extrasaction='ignore');w.writeheader()
        for row in rows:
            out={k:(json.dumps(row.get(k),ensure_ascii=False) if isinstance(row.get(k),(dict,list)) else row.get(k,'')) for k in columns}
            w.writerow(out)
def read_csv(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def edge_parts(text):
    left=len(text)-len(text.lstrip());right=len(text.rstrip())
    return text[:left],text[left:max(left,right)],text[max(left,right):]
def source_hash(text):return digest(text.encode('utf8'))
def protected(text):return PLACEHOLDER.findall(text)
def marker_signature(text):
    return {'placeholders':sorted(protected(text)), 'pipes':text.count('|'),
            'newlines':text.count('\n'),'open_square':text.count('['),'close_square':text.count(']'),
            'underscore_runs':re.findall(r'_+',text),'angle_tag_pairs':len(re.findall(r'<[^<>\r\n]{1,60}>',text))}
def glyph_metrics():
    text=(PROJECT/'runtime/bbc2.fnt').read_text(encoding='utf8')
    return {int(cid):int(advance) for cid,advance in re.findall(r'^char id=(\d+)\s+.*?xadvance=(-?\d+)',text,re.M)}
def widths(text,metrics):
    return [sum(metrics.get(ord(c),12) for c in line) for line in re.split(r'\||\r?\n',text)]
def load_units():return read_jsonl(PROJECT/'catalog/units.jsonl')
def load_occurrences():return read_jsonl(PROJECT/'catalog/occurrences.jsonl')
def resource_path(row):return PROJECT/row['blob_path']
def current_translations():
    p=PROJECT/'translations/zh-CN.jsonl'
    return {r['id']:r for r in read_jsonl(p)} if p.exists() else {}


def draft_model_label(path,registry=None):
    relative=Path(path).resolve().relative_to(PROJECT.resolve()).as_posix()
    entries=registry if registry is not None else read_json(PROJECT/'catalog/draft-provenance.json')['drafts']
    if relative not in entries:raise ValueError('Unregistered draft provenance: '+relative)
    origin=entries[relative]
    if not all(isinstance(origin.get(k),str) and origin[k] for k in ('provider','model')):raise ValueError('Invalid model provenance')
    return origin['provider']+'/'+origin['model']+('/'+origin['reasoning_effort'] if origin.get('reasoning_effort') else '')


def parse_atlas(text):
    """Legacy libGDX text atlas: blank lines start pages; regions are not unique by name."""
    pages=[];regions=[];page=None;region=None
    for number,raw in enumerate(text.splitlines(),1):
        s=raw.strip()
        if not s:page=None;region=None;continue
        if page is None:
            page={'name':s,'line':number,'properties':{}};pages.append(page);continue
        if ':' not in s:
            region={'name':s,'line':number,'page':page['name'],'properties':{},'ordinal':len(regions)}
            regions.append(region);continue
        k,v=s.split(':',1)
        (region['properties'] if region is not None else page['properties'])[k.strip()]=v.strip()
    for r in regions:
        p=r['properties']
        r['xy']=[int(x.strip()) for x in p.get('xy','0,0').split(',')]
        r['size']=[int(x.strip()) for x in p.get('size','0,0').split(',')]
        r['orig']=[int(x.strip()) for x in p.get('orig',p.get('size','0,0')).split(',')]
        r['offset']=[int(x.strip()) for x in p.get('offset','0,0').split(',')]
        r['index']=int(p.get('index','-1'))
        r['rotation']=0 if p.get('rotate','false')=='false' else 90 if p.get('rotate')=='true' else int(p['rotate'])
    return pages,regions


def tokens_for_review(text):
    return json.dumps(marker_signature(text),ensure_ascii=False,separators=(',',':'))


def validate_translation(unit,translation,metrics):
    issues=[]
    if not isinstance(translation,str) or not translation.strip():return [('error','empty_translation','译文为空')]
    if any(ord(c)<32 and c not in '\r\n\t' for c in translation):issues.append(('error','control_character','包含不允许的控制字符'))
    if translation != translation.strip():issues.append(('error','edge_whitespace','正文首尾空白由 occurrence 保留，不应写入译文'))
    before,after=marker_signature(unit['source']),marker_signature(translation)
    for key in before:
        if before[key]!=after[key]:issues.append(('error','marker_'+key,f'{before[key]!r} -> {after[key]!r}'))
    missing=sorted(set(c for c in translation if c not in '\r\n\t|' and ord(c) not in metrics))
    if missing:issues.append(('error','missing_glyph',''.join(missing)))
    limit=unit.get('width_hint_px',240)
    actual=max(widths(translation,metrics),default=0)
    if actual>limit:issues.append(('warning','width_hint',f'{actual}px > indicative {limit}px; requires contextual layout review'))
    if re.search(r'[A-Za-z]{4,}',translation):issues.append(('info','latin_remaining','可能是专名/缩写，或有漏译；需人工判断'))
    return issues
