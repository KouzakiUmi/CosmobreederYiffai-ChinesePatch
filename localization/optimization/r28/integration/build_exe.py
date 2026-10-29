"""Build a standalone Windows r28 EXE from the already-verified Python package.
No install/uninstall/game/save commands; all build outputs are NEW directories.
Uses the existing installer code and accepted payload without changing either.
"""
from pathlib import Path
from hashlib import sha256
import importlib.metadata as metadata
import argparse,json,os,struct,subprocess,sys
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from package_candidate import validate_candidate
sys.path.insert(0,str(ROOT/'src'))
from cosmobreeder_patch.installer import verify

SHA=lambda p:sha256(p.read_bytes()).hexdigest()
NAME='CosmobreederYiffaiCN-r28-candidate2-setup'
SOURCE=ROOT/'dist/r28-full-opt-candidate2-python/staged/cosmobreeder_patch'
CANDIDATE=ROOT/'localization/builds/r28-full-opt-candidate2'
MODULES=['__init__.py','__main__.py','installer.py','delta.py']

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--verify-existing',action='store_true');a=p.parse_args()
 out=a.output.absolute()
 if out.resolve()!=out or out.parent!=ROOT/'dist' or not out.name.startswith('r28'):raise ValueError('Isolated dist/r28* output only')
 if out.exists()!=a.verify_existing:raise ValueError('Build needs NEW output; verification needs existing output')
 candidate,cm,build_id,_=validate_candidate(CANDIDATE)
 payload=verify(SOURCE/'payload')
 if payload['build_id']!=build_id:raise ValueError('Payload build identity')
 for n,e in payload['files'].items():
  if e['target_sha256']!=cm['archives'][n]['sha256']:raise ValueError('Payload/candidate mismatch')
 for name in MODULES:
  if (SOURCE/name).read_bytes()!=(ROOT/'src/cosmobreeder_patch'/name).read_bytes():raise ValueError('Installer source drift')
 if (SOURCE/'acceptance.json').read_bytes()!=(candidate/'acceptance.json').read_bytes():raise ValueError('Acceptance drift')
 paths=sorted(p for p in SOURCE.rglob('*') if p.is_file())
 if any(p.is_symlink() or not p.resolve().is_relative_to(SOURCE) for p in paths):raise ValueError('Package path drift')
 pins={p.relative_to(ROOT).as_posix():SHA(p) for p in paths}
 work=out/'build'
 if not a.verify_existing:
  out.mkdir();work.mkdir();(work/'spec').mkdir();(work/'check-cwd').mkdir()
 report={'status':'building','build_id':build_id,'target_archives':{n:e['target_sha256'] for n,e in payload['files'].items()},
  'python':sys.version.split()[0],'pyinstaller':metadata.version('pyinstaller'),
  'hooks':metadata.version('pyinstaller-hooks-contrib'),'source_sha256':pins,'checks':[],
  'installed':False,'uninstalled':False,'game_started':False,'user_save_accessed':False,
  'signing':'unsigned','gui_interaction_tested':False,
  'documentation':'https://pyinstaller.org/en/v6.19.0/usage.html'}
 if a.verify_existing:
  old=json.loads((out/'exe-build-report.json').read_text('utf8'))
  if old['source_sha256']!=pins or old['build_id']!=build_id or not any(c['name']=='pyinstaller' and c['exit_code']==0 for c in old['checks']):raise ValueError('Cannot verify unbound/preexisting executable')
  report=old;report['verification_resumed']=True
 def save():(out/'exe-build-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 def run(label,argv,*,expected=0,env=None):
  result=subprocess.run([str(v) for v in argv],cwd=work/'check-cwd',env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=600)
  (work/(label+'.stdout.log')).write_bytes(result.stdout);(work/(label+'.stderr.log')).write_bytes(result.stderr)
  report['checks'].append({'name':label,'exit_code':result.returncode,'expected_exit_code':expected});save()
  print(label,'exit',result.returncode,flush=True)
  if result.returncode!=expected:raise RuntimeError('Read '+str(work/(label+'.stderr.log')))
  return result
 env=dict(os.environ);env['PYINSTALLER_CONFIG_DIR']=str(work/'config');env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONIOENCODING']='utf-8';env.pop('PYTHONPATH',None)
 argv=[sys.executable,'-B','-m','PyInstaller','--onefile','--console','--hide-console','hide-early','--noupx','--python-option','X utf8',
  '--name',NAME,'--paths',SOURCE.parent,'--distpath',out,'--workpath',work/'pyinstaller','--specpath',work/'spec']
 for name in ['payload','licenses']:
  argv.extend(['--add-data',str(SOURCE/name)+':'+name])
 for name in ['LICENSE','NOTICE','THIRD_PARTY_NOTICES.md','README.md','acceptance.json','package-report.json']:
  argv.extend(['--add-data',str(SOURCE/name)+':.'])
 argv.append(SOURCE/'__main__.py');save()
 if not a.verify_existing:run('pyinstaller',argv,env=env)
 exe=out/(NAME+'.exe')
 raw=exe.read_bytes();offset=struct.unpack_from('<I',raw,0x3c)[0]
 if raw[:2]!=b'MZ' or raw[offset:offset+4]!=b'PE\0\0' or struct.unpack_from('<H',raw,offset+4)[0]!=0x8664:raise ValueError('Not Windows x64 PE')
 # The exact installed 6.19 reader API is read-only; no bundled game executes.
 from PyInstaller.archive.readers import CArchiveReader
 archive=CArchiveReader(str(exe));lookup={n.replace('\\','/'):n for n in archive.toc}
 if len(lookup)!=len(archive.toc):raise ValueError('Duplicate normalized archive paths')
 datafiles=[p for p in paths if p.name not in MODULES or p.parent!=SOURCE]
 for source in datafiles:
  name=source.relative_to(SOURCE).as_posix()
  if name not in lookup or archive.extract(lookup[name])!=source.read_bytes():raise ValueError('Embedded data mismatch '+name)
 pyz_name=next(n for n,v in archive.toc.items() if v[-1]=='z')
 pyz=archive.open_embedded_archive(pyz_name);modules=pyz.toc
 if 'X utf8' not in archive.options:raise ValueError('UTF8 mode must be embedded, not inherited from environment')
 import marshal
 entry=marshal.loads(archive.extract('__main__'))
 if entry!=compile((SOURCE/'__main__.py').read_bytes(),entry.co_filename,'exec',dont_inherit=True,optimize=0):raise ValueError('Entry bytecode differs from verified source')
 for module,filename in [('cosmobreeder_patch','__init__.py'),('cosmobreeder_patch.installer','installer.py'),('cosmobreeder_patch.delta','delta.py')]:
  code=pyz.extract(module)
  if code!=compile((SOURCE/filename).read_bytes(),code.co_filename,'exec',dont_inherit=True,optimize=0):raise ValueError('Module bytecode differs from verified source: '+module)
 report['installer_compiled_code_matches_source']=True
 for name in ['cosmobreeder_patch','cosmobreeder_patch.installer','cosmobreeder_patch.delta','tkinter','tkinter.filedialog','tkinter.messagebox']:
  if name not in modules:raise ValueError('Missing module '+name)
 names={Path(n).name.lower() for n in lookup}
 for name in ['python312.dll','_tkinter.pyd','tcl86t.dll','tk86t.dll']:
  if name not in names:raise ValueError('Missing standalone runtime '+name)
 if '_tcl_data/init.tcl' not in lookup or '_tk_data/tk.tcl' not in lookup:raise ValueError('Missing Tk/Tcl scripts')
 report['embedded_data_files_exact']=len(datafiles);report['bundled_python_and_tk']=True;report['architecture']='Windows x64'
 # Remove Python search-path overrides and Python's PATH; only invoke safe CLI modes.
 frozen_env=dict(os.environ)
 for key in ['PYTHONPATH','PYTHONHOME','VIRTUAL_ENV','PYTHONUTF8','PYTHONIOENCODING']:frozen_env.pop(key,None)
 frozen_env['PATH']=str(Path(os.environ.get('SystemRoot','C:/Windows'))/'System32')
 frozen_env['PYTHONDONTWRITEBYTECODE']='1'
 report['permanent_python_option']='X utf8'
 report['encoding_env_overrides_removed_during_checks']=True
 value=run('verify-payload',[exe,'--verify-payload'],env=frozen_env)
 if json.loads(value.stdout)!= {'version':'alpha0.1','status':'verified','game_started':False}:raise ValueError('Unexpected verifier output')
 licenses=run('licenses',[exe,'--licenses'],env=frozen_env).stdout.decode('utf8').replace('\r\n','\n')
 report['license_text_comparison']='UTF8 decoded, Windows CRLF normalized to LF only; embedded file bytes separately exact'
 legal=[p for p in datafiles if p.relative_to(SOURCE).parts[0]=='licenses' or p.name in ['LICENSE','NOTICE','THIRD_PARTY_NOTICES.md']]
 for path in legal:
  if path.relative_to(SOURCE).as_posix() not in licenses or path.read_text('utf8') not in licenses:raise ValueError('License output incomplete')
 run('help',[exe,'--help'],env=frozen_env)
 bad=work/'bad-payload';bad.mkdir();(bad/'manifest.json').write_text('{"version":"invalid","files":{}}',encoding='utf8')
 run('bad-payload-rejected',[exe,'--verify-payload','--payload',bad],expected=1,env=frozen_env)
 if any(SHA(ROOT/n)!=v for n,v in pins.items()):raise ValueError('Read-only packaging input changed')
 report.update(status='passed_standalone_exe_no_install',exe=exe.name,exe_bytes=exe.stat().st_size,exe_sha256=SHA(exe),
  embedded_payload_manifest_sha256=SHA(SOURCE/'payload/manifest.json'),licenses_displayed=len(legal),
  no_python_on_test_PATH=True,installer_source_unmodified=True,source_package_unchanged=True)
 save()
 readme=f'''# r28 candidate2 Windows EXE

[下载／运行 {exe.name}](<{exe.name}>)，无需另装Python。双击打开图形安装界面；单文件初次启动需要解包，请稍候。

- 内容与已验收的r28 candidate2 Python差分版完全相同，安装器协议／界面版本仍标alpha0.1，不代表内容是旧r27。
- 已有旧补丁时，必须先用旧补丁自己的安装器／备份还原到支持的原版，再由用户自行决定安装此候选。不要用本包还原旧版本记录，不要覆盖旧备份／状态。
- 未签名。不要为运行而关闭安全软件或绕过系统安全策略；跨Windows版本／安全产品的兼容性未验证。
- 本次仅运行负载验证、许可显示、帮助和错误负载拒绝，没有执行安装／卸载、游戏、存档或GUI按钮交互。
- 上轮游戏候选通过CPU及独立复核；GPU／CRT／完整父裁剪／真实输入仍未实机验收。
- SHA-256：`{report['exe_sha256']}`。
- [构建与验证报告](<exe-build-report.json>)。

高级无安装检查：
```text
{exe.name} --verify-payload
{exe.name} --licenses
```
'''
 (out/'README.md').write_text(readme,encoding='utf8')
 (out/'SHA256SUMS').write_text(''.join(SHA(out/n)+'  '+n+'\n' for n in [exe.name,'README.md','exe-build-report.json']),encoding='utf8')
 print(json.dumps({k:report[k] for k in ['status','exe','exe_bytes','exe_sha256','embedded_data_files_exact','licenses_displayed','installed']},indent=2))
if __name__=='__main__':main()
