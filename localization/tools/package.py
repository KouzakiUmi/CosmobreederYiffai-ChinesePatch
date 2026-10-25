"""Build separate JAR/PAK outputs, never edit source archives or the install.

Default is a dry run. --write requires a new project/builds child directory.
Only reviewed/approved text is used unless --include-drafts is explicit.
Bitmap artwork replacement is deliberately not automatic.
"""
from pathlib import Path
import argparse
import collections
import copy
import io
import json
import os
import re
import struct
import sys
import zipfile
from PIL import Image
from projectlib import *
from codec import decrypt_file,encrypt_file
from classfile import load
from review import selected_translations,render_resources
from layout_bundle import read_layout_bundle,apply_layout_bundle,verify_font_atlas


def replace_utf8(data,replacements):
    """Replace only designated CP Utf8 payloads; no bytecode or CP indices move."""
    if not replacements:return data
    original=load(data);count=struct.unpack_from('>H',data,8)[0];pos=10;index=1;parts=[]
    lengths={3:4,4:4,5:8,6:8,7:2,8:2,9:4,10:4,11:4,12:4,15:3,16:2,17:4,18:4,19:2,20:2}
    touched=set()
    while index<count:
        start=pos;tag=data[pos];pos+=1
        if tag==1:
            n=struct.unpack_from('>H',data,pos)[0];pos+=2+n
            if index in replacements:
                text=replacements[index]
                if '\0' in text or any(ord(c)>65535 or 0xD800<=ord(c)<=0xDFFF for c in text):raise ValueError('Only non-NUL BMP translations are supported')
                encoded=text.encode('utf8')
                if len(encoded)>65535:raise ValueError('Class UTF-8 constant too long')
                parts.append(b'\x01'+struct.pack('>H',len(encoded))+encoded);touched.add(index)
            else:parts.append(data[start:pos])
        else:
            if index in replacements:raise ValueError('Requested constant is not Utf8')
            pos+=lengths[tag];parts.append(data[start:pos])
            if tag in (5,6):index+=1
        index+=1
    if touched!=set(replacements):raise ValueError('Unknown CP UTF-8 index')
    out=data[:10]+b''.join(parts)+data[pos:];parsed=load(out)
    if parsed.this_name!=original.this_name:raise ValueError('Class identity changed')
    for a,b in zip(original.methods,parsed.methods):
        if original.code_of(a)!=parsed.code_of(b):raise ValueError('Bytecode changed unexpectedly')
    return out


def approved_overrides():
    out={};occ={o['occurrence_id']:o for o in load_occurrences()};units={u['id']:u for u in load_units()};metrics=glyph_metrics()
    for row in read_csv(PROJECT/'review/occurrence_overrides.csv'):
        if row['status'] not in ('reviewed','approved') or not row['translation_override']:continue
        o=occ[row['occurrence_id']]
        if row['unit_id']!=o['unit_id'] or row['location']!=o['location']:raise ValueError('Occurrence mapping changed')
        text=row['translation_override'];errors=[q for q in validate_translation(units[o['unit_id']],text,metrics) if q[0]=='error']
        if errors:raise ValueError('Invalid occurrence override '+str(errors))
        if row['occurrence_id'] in out:raise ValueError('Duplicate occurrence override')
        out[row['occurrence_id']]=text
    return out


def code_changes(translations):
    records=current_translations();by_class=collections.defaultdict(dict)
    for o in load_occurrences():
        if o['category']!='code' or o['unit_id'] not in translations:continue
        rec=records[o['unit_id']]
        if not rec.get('usage_approved'):continue
        name=o['class_name'];idx=o['utf8_index'];text=o['leading_ws']+translations[o['unit_id']]+o['trailing_ws']
        if idx in by_class[name] and by_class[name][idx]!=text:raise ValueError('Shared CP constant has conflicting translations')
        by_class[name][idx]=text
    return by_class


def grow_font(z):
    idx=json.loads(decrypt_file(z.read('dataq/0')))
    atlas_key='dataq/'+str(idx['/sprites.atlas']);png_key='dataq/'+str(idx['/sprites.png'])
    atlas=decrypt_file(z.read(atlas_key)).decode('utf8').replace('\r\n','\n')
    if not re.search(r'^size: 4096, 4096$',atlas,re.M):raise ValueError('Unexpected source atlas page dimensions')
    atlas=re.sub(r'^size: 4096, 4096$','size: 4096, 6144',atlas,count=1,flags=re.M)
    match=re.search(r'^bbc2\n(?:[ \t].*\n)+',atlas,re.M)
    if not match:raise ValueError('bbc2 region missing')
    block=match.group();block=re.sub(r'  xy: .*','  xy: 0, 4096',block)
    block=re.sub(r'  (size|orig): .*',lambda m:'  '+m.group(1)+': 2048, 2048',block)
    block=re.sub(r'  offset: .*','  offset: 0, 0',block);atlas=atlas[:match.start()]+block+atlas[match.end():]
    with Image.open(io.BytesIO(decrypt_file(z.read(png_key)))) as im:old=im.convert('RGBA')
    with Image.open(PROJECT/'runtime/bbc2-cjk-10.png') as im:font=im.convert('RGBA')
    if old.size!=(4096,4096) or font.size!=(2048,2048):raise ValueError('Unexpected texture dimensions')
    # classic 字体：游戏 UI 菜单用的就是它（14 个 class 引用），只有英文 193 字形，
    # 所以菜单里的中文会静默不画。它的 8px 中文页放在图集右侧原本空着的区域，
    # 图集不用再变大；classic.fnt 已由 tools/make-classic-cjk.py 重新生成。
    classic_page=PROJECT/'runtime/classic-cjk.png'
    if not classic_page.is_file():raise ValueError('missing runtime/classic-cjk.png; run tools/make-classic-cjk.py')
    classic_match=re.search(r'^classic\n(?:[ \t].*\n)+',atlas,re.M)
    if not classic_match:raise ValueError('classic region missing from atlas')
    cblock=classic_match.group()
    cblock=re.sub(r'  xy: .*','  xy: 2048, 4096',cblock)
    cblock=re.sub(r'  (size|orig): .*',lambda m:'  '+m.group(1)+': 2048, 2048',cblock)
    atlas=atlas[:classic_match.start()]+cblock+atlas[classic_match.end():]
    page=Image.new('RGBA',(4096,6144),(0,0,0,0));page.paste(old,(0,0));page.paste(font,(0,4096))
    with Image.open(classic_page) as _c:
        classic_font=_c.convert('RGBA')
    if classic_font.size!=(2048,2048):raise ValueError('classic page must be 2048x2048')
    page.paste(classic_font,(2048,4096))
    if page.crop((0,0,4096,4096)).tobytes()!=old.tobytes():raise ValueError('Original art changed')
    out=io.BytesIO();page.save(out,format='PNG')
    return {atlas_key:encrypt_file(atlas.encode('utf8'),os.urandom(32),os.urandom(8)),
            png_key:encrypt_file(out.getvalue(),os.urandom(32),os.urandom(8))}


def patch_jar_dialogue(tr_by_source,jar_path=None):
    """把 jar 内 datadf/datadm 的台词换成中文。

    没装官方 NSFW 补丁的玩家没有 patch.pak，游戏从 jar 里的 datadf/datadm 读台词。
    这两个文件和 pak 里的同名文件结构一样、场景 key 也一样，但部分 block 的原文
    措辞不同（SFW 版），所以不能按 pak 的行号套，只能按原文匹配译文。

    返回 {archive_entry: 明文 bytes}，由调用方统一加密。
    """
    # 必须读“已回退到原版”的 jar：游戏目录那份可能已被本补丁覆盖成中文，
    # 那样按原文匹配就一行都命中不了，本体版台词会漏翻。
    if jar_path is None:
        jar=[a for a in read_json(PROJECT/"sources/archives.json") if a["tag"]=="jar"][0]
        jar_path=jar["path"]
    raw_jar=Path(jar_path).read_bytes()
    out={}
    for entry in ("datadf/1","datadm/1"):
        with zipfile.ZipFile(io.BytesIO(raw_jar)) as z:
            if entry not in z.namelist():
                continue
            plain=decrypt_file(z.read(entry)).decode("utf8")
        kept=hit=0
        lines=plain.split("\n")
        for i,line in enumerate(lines):
            s=line.rstrip("\r")
            body=s.lstrip()
            if not body.startswith("*"):
                continue
            indent=s[:len(s)-len(body)]
            text=body[1:].strip()
            zh=tr_by_source.get(text)
            if zh:
                lines[i]=indent+"* "+zh+("\r" if line.endswith("\r") else "")
                hit+=1
            else:
                kept+=1
        if not hit:
            continue
        new_plain="\n".join(lines)
        out[entry]=new_plain.encode("utf8")   # 明文；构建时会统一加密
        print("jar %s: 换成中文 %d 行，保留原文 %d 行" % (entry,hit,kept))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(PROJECT/'builds/package'))
    ap.add_argument('--include-drafts',action='store_true');ap.add_argument('--write',action='store_true')
    ap.add_argument('--layout-bundle',type=Path,help='Explicit experimental layout bundle; not visual acceptance')
    a=ap.parse_args()
    layout_manifest=layout_identity=None
    if a.layout_bundle is not None:
        layout_manifest,layout_identity=read_layout_bundle(a.layout_bundle)
    output=Path(a.output).resolve();allowed=(PROJECT/'builds').resolve()
    if output==allowed or not output.is_relative_to(allowed):raise ValueError('Output must be a new child of project/builds')
    archives=read_json(PROJECT/'sources/archives.json');config=read_json(PROJECT/'project.json')
    for archive in archives:
        src=Path(archive['path'])
        if digest(src.read_bytes())!=archive['sha256']:
            # 游戏可能已经被本补丁覆盖过，原版在安装器留下的备份里
            alt=src.parent/'_汉化补丁备份'/src.name
            if alt.is_file() and digest(alt.read_bytes())==archive['sha256']:
                print('原版已改用备份：'+str(alt));archive['path']=str(alt)
            else:raise ValueError('Original archive fingerprint changed')
    for name,sha in config['runtime_files'].items():
        if digest((PROJECT/'runtime'/name).read_bytes())!=sha:raise ValueError('Runtime baseline changed')
    translations=selected_translations(a.include_drafts);overrides=approved_overrides()
    rendered=render_resources(translations,overrides);resources={r['logical_path']:r for r in read_jsonl(PROJECT/'catalog/resources.jsonl')}
    edits=collections.defaultdict(dict)
    for key,data in rendered.items():
        r=resources[key]
        if digest(data)!=r['sha256']:edits[r['archive']][r['archive_entry']]=data
    # 本体版（没装官方 NSFW 补丁）从 jar 里的 datadf/datadm 读台词，那里也要换成中文。
    # 装了补丁的玩家走 patch.pak，pak 覆盖 jar，所以两种客户用同一个包就够了。
    _units={u['id']:u for u in load_units()}
    _tr_by_source={}
    for _uid,_txt in translations.items():
        _src=_units[_uid].get('source','').strip()
        if _src: _tr_by_source.setdefault(_src,_txt)
    # 本体版（SFW）独有、pak 里没有对应原文的台词，单独维护在这张表里。
    _jv=PROJECT/'translations/jar-variant.jsonl'
    if _jv.is_file():
        for _r in read_jsonl(_jv):
            _tr_by_source.setdefault(_r['source'],_r['translation'])
    for _entry,_data in patch_jar_dialogue(_tr_by_source,{a['tag']:a['path'] for a in archives}['jar']).items():
        edits['jar'][_entry]=_data
    code=code_changes(translations)
    plan={'write':a.write,'output':str(output),'include_drafts':a.include_drafts,'selected_units':len(translations),
          'occurrence_overrides':len(overrides),'changed_text_resources':{k:len(v) for k,v in edits.items()},
          'code_classes_with_usage_approval':len(code),'runtime_font_and_unicode_patch':True,
          'bitmap_redraw_included':False,'source_installation_write':False}
    if layout_manifest is not None:
        overlap=set(code)&set(layout_manifest['original_classes'])
        if overlap:raise ValueError('CP-index/layout class overlap requires explicit composition: '+str(sorted(overlap)))
        plan['layout_bundle']={'manifest_sha256':layout_identity,'status':layout_manifest['status'],
                              'runtime_activation':layout_manifest['runtime_activation'],'visual_acceptance':False}
    print(json.dumps(plan,ensure_ascii=False,indent=2))
    if not a.write:return
    if output.exists():raise ValueError('Refuse to overwrite an existing package directory')
    final_output=output
    if layout_manifest is not None:
        # Keep experimental output private until BOTH resource modes pass.
        import uuid
        output=PROJECT/'work/layout-package'/uuid.uuid4().hex
    output.mkdir(parents=True);evidence=[]
    for archive in archives:
        tag=archive['tag'];path=Path(archive['path']);dest=output/path.name
        with zipfile.ZipFile(path) as z:
            replacements=grow_font(z)
            for entry,data in edits.get(tag,{}).items():replacements[entry]=encrypt_file(data,os.urandom(32),os.urandom(8))
            if tag=='jar':
                replacements['bbc2.fnt']=(PROJECT/'runtime/bbc2.fnt').read_bytes()
                replacements['classic.fnt']=(PROJECT/'runtime/classic.fnt').read_bytes()
                replacements['PRG/afH.class']=(PROJECT/'runtime/afH.class').read_bytes()
                replacements['cosmoloc/CjkText.class']=(PROJECT/'runtime/CjkText.class').read_bytes()
                replacements['META-INF/licenses/FusionPixel-OFL.txt']=(PROJECT/'runtime/LICENSE-FusionPixel-OFL.txt').read_bytes()
                replacements['META-INF/licenses/Localization-NOTICE.txt']=(PROJECT/'runtime/NOTICE.txt').read_bytes()
                for name,changes in code.items():replacements[name]=replace_utf8(replacements.get(name,z.read(name)),changes)
                if a.layout_bundle is not None:
                    plan['layout_bundle']=apply_layout_bundle(z,replacements,a.layout_bundle,code,
                                                              expected_manifest_sha256=layout_identity)
            elif layout_manifest is not None:
                verify_font_atlas(z,replacements,layout_manifest,PROJECT/'runtime')
            existing=set(z.namelist())
            with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as target:
                for info in z.infolist():
                    data=replacements.pop(info.filename,z.read(info.filename));target.writestr(copy.copy(info),data)
                for name,data in replacements.items():target.writestr(name,data)
        with zipfile.ZipFile(dest) as result:
            if result.testzip() is not None:raise ValueError('ZIP integrity failure')
        evidence.append({'archive':dest.name,'sha256':digest(dest.read_bytes()),'bytes':dest.stat().st_size})
    write_json(output/'package-manifest.json',{'plan':plan,'archives':evidence,'originals':archives})
    if layout_manifest is not None:
        if final_output.exists() or final_output.resolve()!=final_output or not final_output.resolve().is_relative_to(allowed):
            raise ValueError('Layout package destination changed before publish')
        final_output.parent.mkdir(parents=True,exist_ok=True)
        print('Publish new layout package:',output.resolve(),'->',final_output.resolve())
        output.rename(final_output);output=final_output
    print('Separate output archives written; not installed:',output)


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
