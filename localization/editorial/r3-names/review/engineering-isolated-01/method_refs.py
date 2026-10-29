"""Read candidate6 constant pools; no class mutation."""
from pathlib import Path
import zipfile,struct,json
ROOT=Path(__file__).resolve().parents[5];HERE=Path(__file__).resolve().parent
out=[]
with zipfile.ZipFile(ROOT/'localization/builds/r28-editorial-repairs-candidate6/cosmobreeder-multi.jar') as z:
 for entry in z.namelist():
  if not entry.startswith('PRG/') or not entry.endswith('.class'):continue
  d=z.read(entry);n=int.from_bytes(d[8:10],'big');cp=[None]*n;i=1;p=10
  while i<n:
   t=d[p];p+=1
   if t==1:
    size=int.from_bytes(d[p:p+2],'big');p+=2;cp[i]=(t,d[p:p+size].decode('utf8','replace'));p+=size
   elif t in (3,4):cp[i]=(t,None);p+=4
   elif t in (5,6):cp[i]=(t,None);p+=8;i+=1
   elif t in (7,8,16,19,20):cp[i]=(t,int.from_bytes(d[p:p+2],'big'));p+=2
   elif t in (9,10,11,12,17,18):cp[i]=(t,*struct.unpack('>HH',d[p:p+4]));p+=4
   elif t==15:cp[i]=(t,None);p+=3
   else:raise ValueError((entry,t))
   i+=1
  text=lambda idx:cp[idx][1]
  for c in cp:
   if c and c[0] in (10,11):
    owner=text(cp[c[1]][1]);nt=cp[c[2]];name=text(nt[1]);desc=text(nt[2])
    if owner=='PRG/Li' and name in ['a','e','f','g','h','i','j']:
     out.append({'class':entry,'owner':owner,'method':name,'descriptor':desc})
(HERE/'mission-method-refs.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
