"""Static references for fixed atlas assets. References are not runtime reachability claims."""
import collections
import re
import sys
import zipfile
from projectlib import *
from classfile import load,disasm


def main():
    fixed=read_jsonl(PROJECT/'catalog/fixed_images.jsonl');by_name=collections.defaultdict(list)
    for a in fixed:by_name[a['name']].append(a['asset_id'])
    refs=[]
    def add(name,kind,where,extra=None):
        refs.append({'asset_name':name,'asset_ids':by_name[name],'reference_kind':kind,'location':where,
                     'runtime_visibility_verified':False,**(extra or {})})
    jar=next(a for a in read_json(PROJECT/'sources/archives.json') if a['tag']=='jar')
    with zipfile.ZipFile(jar['path']) as z:
        for name in sorted(n for n in z.namelist() if n.startswith('PRG/') and n.endswith('.class')):
            cf=load(z.read(name));hits={i:cf.cp.utf8(v[1]) for i,v in cf.cp.items.items() if v[0]==8 and cf.cp.utf8(v[1]) in by_name}
            if not hits:continue
            for m in cf.methods:
                code,_=cf.code_of(m)
                if code is None:continue
                for pc,op,arg in disasm(cf,code):
                    if op not in ('ldc','ldc_w'):continue
                    index=int(arg.split(' ',1)[0][1:])
                    if index in hits:add(hits[index],'class_constant_reference',f'{name}#{m["name"]}{m["desc"]}@{pc}',{'cp_index':index})
    def walk(value,pointer=''):
        if isinstance(value,dict):
            for k,v in value.items():
                key=pointer+'/'+str(k).replace('~','~0').replace('/','~1')
                if k in by_name:yield k,key,'json_key_definition'
                yield from walk(v,key)
        elif isinstance(value,list):
            for i,v in enumerate(value):yield from walk(v,pointer+'/'+str(i))
        elif isinstance(value,str) and value in by_name:yield value,pointer,'json_value_reference'
    for r in read_jsonl(PROJECT/'catalog/resources.jsonl'):
        key=r['logical_path']
        if key.endswith('.json'):
            for name,pointer,kind in walk(read_json(resource_path(r))):add(name,kind,key+'#'+pointer)
        elif key.endswith('.vsn'):
            for number,line in enumerate(resource_path(r).read_bytes().decode('utf8').splitlines(),1):
                if re.match(r'\s*(?:text|lang\(|auto\()',line):continue
                for token in set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*',line))&set(by_name):add(token,'vsn_directive_reference',key+f'#L{number}')
    write_jsonl(PROJECT/'catalog/asset_usage.jsonl',refs)
    write_csv(PROJECT/'catalog/asset_usage.csv',refs,['asset_name','asset_ids','reference_kind','location','cp_index','runtime_visibility_verified'])
    locations=collections.defaultdict(list)
    for r in refs:
        if r['reference_kind']!='json_key_definition':
            for aid in r['asset_ids']:locations[aid].append(r['location'])
    rows=read_csv(PROJECT/'review/fixed_images.csv')
    for r in rows:r['usage_summary']=' ; '.join(locations[r['asset_id']][:3]) or 'No direct static reference found; may be loaded dynamically.'
    write_csv(PROJECT/'review/fixed_images.csv',rows,list(rows[0]))
    summary={'fixed_assets':len(fixed),'static_references':len(refs),'kinds':dict(collections.Counter(r['reference_kind'] for r in refs)),
             'assets_with_non_definition_reference':len(locations),'runtime_visibility_proven':False,
             'limitations':'Literal/class/JSON/VSN references only; dynamic lookups are not treated as unused.'}
    write_json(PROJECT/'reports/asset-usage-summary.json',summary);print(__import__('json').dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
