"""Sample exact candidate and frozen-original dingbats atlas channel bounds.
Only called by the CPU candidate runner; output lives in its NEW core directory.
"""
from io import BytesIO
from pathlib import Path
import hashlib,json,re,sys,zipfile
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/lib'))
from codec import decrypt_file

def sample(path):
    with zipfile.ZipFile(path) as z:
        fnt=z.read('dingbats.fnt')
        idx=json.loads(decrypt_file(z.read('dataq/0')))
        atlas=decrypt_file(z.read('dataq/'+str(idx['/sprites.atlas']))).decode('utf8')
        block=re.search(r'(?m)^dingbats\r?\n(?:  [^\n]*\n)*',atlas)[0]
        x,y=map(int,re.search(r'xy: (\d+), (\d+)',block).groups())
        w,h=map(int,re.search(r'size: (\d+), (\d+)',block).groups())
        with Image.open(BytesIO(decrypt_file(z.read('dataq/'+str(idx['/sprites.png']))))) as source:
            image=source.convert('RGBA').crop((x,y,x+w,y+h))
    assert image.size==(256,128)
    glyphs={}
    for line in fnt.decode('utf8').splitlines():
        if not line.startswith('char '):continue
        f={k:int(v) for k,v in re.findall(r'(\w+)=(-?\d+)',line)}
        if f['width']==0 or f['height']==0:continue
        crop=image.crop((f['x'],f['y'],f['x']+f['width'],f['y']+f['height']))
        alpha=crop.getchannel('A').getbbox();red=crop.getchannel('R').getbbox()
        assert alpha and red,('empty original symbol ink',f['id'])
        assert (f['xoffset'],f['yoffset'],f['width'],f['height'],f['xadvance'])==(-1,-1,11,12,8)
        glyphs[f['id']]={'fields':f,'alpha':alpha,'red':red}
    return fnt,image,glyphs

def export(candidate,baseline,out):
    fnt,image,glyphs=sample(candidate)
    old,old_image,old_glyphs=sample(baseline)
    assert fnt==old,'candidate changed pinned original dingbats FNT'
    assert image.tobytes()==old_image.tobytes(),'candidate changed original dingbats atlas pixels'
    assert glyphs==old_glyphs
    left=min(g['fields']['xoffset']+min(g['alpha'][0],g['red'][0]) for g in glyphs.values())
    right=max(g['fields']['xoffset']+max(g['alpha'][2],g['red'][2]) for g in glyphs.values())+27*8
    props=['fnt_sha256='+hashlib.sha256(fnt).hexdigest(),'ink_left='+str(left),'ink_right='+str(right)]
    for cp,g in sorted(glyphs.items()):
        for channel in ['alpha','red']:props.append(str(cp)+'.'+channel+'='+','.join(map(str,g[channel])))
    (out/'pattern-ink.properties').write_text('\n'.join(props)+'\n',encoding='utf8')
    report={'fnt_sha256':hashlib.sha256(fnt).hexdigest(),'atlas_rgba_sha256':hashlib.sha256(image.tobytes()).hexdigest(),'identical_to_frozen_original':True,'fnt_quad_local':[-1,-1,10,11],'ink_content_x_relative_to_original_anchor':[left,right],
            'actual_original_O':{'raw_quad_x_at_anchor16':[15,26],'alpha_crop_bbox':list(glyphs[79]['alpha']),'red_crop_bbox':list(glyphs[79]['red']),'alpha_x_at_anchor16':[15+glyphs[79]['alpha'][0],15+glyphs[79]['alpha'][2]]},'glyphs':glyphs}
    (out/'pattern-ink.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    return {k:v for k,v in report.items() if k!='glyphs'}
