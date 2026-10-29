"""Deterministic fixed-image localization. Writes only this isolated staging.
Run with system Python 3.12 -B; never reads/writes live game directories.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import sys
import zipfile
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = ROOT/'docs/font-layout-audit-20261025/image-workorders'
sys.path.insert(0, str(ROOT/'localization/tools'))
from optimized_images import raw_rgba_hash, verify_replacement

BLUE=(0,0,252,255); WHITE=(252,252,252,255); BLACK=(0,0,0,255)
YELLOW=(248,184,0,255)
FONT8=ROOT/'work/item-font8/asset/fusion-pixel-8px-monospaced-zh_hans.bdf'
FONT12=ROOT/'localization/work/story-font12/font12.zip'
PINS={str(FONT8.relative_to(ROOT)).replace('\\','/'):'44a2d82b3dd782b505fa2297f10d8fd65499f9476d47b0331a22a133419b0ec3',
      str(FONT12.relative_to(ROOT)).replace('\\','/'):'76ed4adde0cc43ae8312041960d586c130c75a9d0f7c1c64a7cace7e4130c358'}


def require(ok, message):
    if not ok: raise ValueError(message)


def digest(data): return sha256(data).hexdigest()


def write_json(path, obj):
    require(path.resolve().is_relative_to(OUT.resolve()), 'write outside owned image staging')
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')


class NativeFont:
    def __init__(self, data, size, required):
        self.size=size; self.glyphs={}
        text=data.decode('utf8')
        require(f'\nPIXEL_SIZE {size}\n' in text, 'not native font size')
        ascent=int(next(l.split()[1] for l in text.splitlines() if l.startswith('FONT_ASCENT ')))
        for block in text.split('STARTCHAR ')[1:]:
            lines=block.splitlines()
            cp=int(next(l.split()[1] for l in lines if l.startswith('ENCODING ')))
            advance=int(next(l.split()[1] for l in lines if l.startswith('DWIDTH ')))
            w,h,xo,yo=map(int,next(l for l in lines if l.startswith('BBX ')).split()[1:])
            # Nonspacing combining marks may legally extend beyond a cell. They
            # are not in this exact locked UI corpus; do not process unrelated glyphs.
            if cp not in required:continue
            bitmap=lines[lines.index('BITMAP')+1:lines.index('ENDCHAR')]
            cell=Image.new('L',(advance,size))
            for y,line in enumerate(bitmap):
                value=int(line,16); nbits=len(line)*4
                for x in range(w):
                    if value & (1<<(nbits-1-x)):
                        tx,ty=xo+x,ascent-yo-h+y
                        require(0<=tx<advance and 0<=ty<size,f'font bounds U+{cp:04X}')
                        cell.putpixel((tx,ty),255)
            self.glyphs[cp]=(advance,cell)
    def raster(self,text):
        require('\n' not in text,'one line per raster')
        require(all(ord(c) in self.glyphs for c in text),'missing exact candidate glyph')
        width=sum(self.glyphs[ord(c)][0] for c in text)
        im=Image.new('L',(width,self.size)); x=0
        for ch in text:
            advance,glyph=self.glyphs[ord(ch)]
            require(ch.isspace() or glyph.getbbox() is not None,f'empty candidate glyph {ch!r}')
            im.paste(glyph,(x,0)); x+=advance
        return im


class Redraw:
    def __init__(self,before,fonts,locked):
        self.before=before;self.after=before.copy();self.fonts=fonts;self.locked=locked
        self.mask=Image.new('L',before.size);self.operations=[]
    def text(self,box,english,size=12,fg=BLUE,bg=WHITE,text=None,align='center',source_inks=None,erase_boxes=None):
        source_inks=source_inks or (fg,)
        text=self.locked[english] if text is None else text
        # Exact locked string or an explicitly declared line from a locked block.
        require(text in self.locked[english].split('\n') or text==self.locked[english], 'unlocked output string')
        glyph=self.fonts[size].raster(text)
        x0,y0,x1,y1=box
        require(0<=x0<x1<=self.before.width and 0<=y0<y1<=self.before.height,'invalid approved slot')
        require(glyph.width<=x1-x0 and glyph.height<=y1-y0,f'text exceeds immutable slot: {text} {box}')
        x=x0 if align=='left' else x0+(x1-x0-glyph.width)//2
        y=y0+(y1-y0-glyph.height)//2
        old=self.before.load(); new=self.after.load(); approved=self.mask.load()
        erased=[];drawn=[]
        erase_boxes=erase_boxes or [box]
        for ex0,ey0,ex1,ey1 in erase_boxes:
            require(0<=ex0<ex1<=self.before.width and 0<=ey0<ey1<=self.before.height,'invalid source ink box')
            for yy in range(ey0,ey1):
                for xx in range(ex0,ex1):
                    if old[xx,yy] in source_inks:
                        new[xx,yy]=bg;approved[xx,yy]=255;erased.append((xx,yy))
        for yy in range(glyph.height):
            for xx in range(glyph.width):
                if glyph.getpixel((xx,yy)):
                    tx,ty=x+xx,y+yy
                    require(old[tx,ty] in (*source_inks,bg),f'target ink intersects protected art/alpha: {(tx,ty)} {text}')
                    new[tx,ty]=fg;approved[tx,ty]=255;drawn.append((tx,ty))
        require(erased, f'no confirmed source ink: {english}')
        require(drawn, 'no candidate ink')
        # Re-raster audit verifies every output ink pixel and every character.
        require(all(new[xx,yy]==fg for xx,yy in drawn),'exact raster mismatch')
        self.operations.append({'english':english,'zh':text,'font_px':size,'slot':list(box),
                                'source_erase_boxes':[list(b) for b in erase_boxes],
                                'origin':[x,y],'ink_size':list(glyph.size),
                                'foreground':list(fg),'background':list(bg),
                                'source_ink_pixels':len(erased),'candidate_ink_pixels':len(drawn),
                                'raster_mask_sha256':digest(glyph.tobytes()),'exact_locked_text':True})

    def tiles(self):
        """Each 16px tile independently: SH + animated OP/OP -> 商 + 店/店.

        Source bevel ink is two palette colors plus its one-pixel dark shadow.
        Unrelated background, y>=8 rim/animation and tile placement stay exact.
        """
        old=self.before.load();new=self.after.load();mask=self.mask.load()
        highlight=old[2,0];middle=old[1,2];background=old[7,1];shadow=(1,1,0,255)
        require(len({highlight,middle,background,shadow})==4,'sign palette segmentation')
        for tile,ch in enumerate('商店店'):
            x0=tile*16;erase=set()
            for y in range(8):
                for x in range(x0,x0+16):
                    if old[x,y] in (highlight,middle):
                        erase.add((x,y))
                        if x+1<x0+16 and y+1<8 and old[x+1,y+1]==shadow: erase.add((x+1,y+1))
            for x,y in erase:new[x,y]=background;mask[x,y]=255
            glyph=self.fonts[8].raster(ch);gx=x0+4
            for y in range(8):
                for x in range(8):
                    if glyph.getpixel((x,y)) and x+1<8 and y+1<8:
                        new[gx+x+1,y+1]=shadow;mask[gx+x+1,y+1]=255
            for y in range(8):
                for x in range(8):
                    if glyph.getpixel((x,y)):
                        new[gx+x,y]=highlight if y==0 else middle;mask[gx+x,y]=255
            self.operations.append({'english':'SHOP' if tile==0 else 'OP animation suffix',
                                    'zh':ch,'font_px':8,'slot':[x0,0,x0+16,8],
                                    'tile_id':tile,'exact_locked_text':True,
                                    'basis':'ktilemaps ClassicTileset0*: local0 SH + local1 OP, animation [[1,0.1],[2,0.1]]',
                                    'palette_preserved':True,'source_ink_pixels':len(erase)})
        require(self.after.crop((0,8,self.before.width,self.before.height)).tobytes()==self.before.crop((0,8,self.before.width,self.before.height)).tobytes(),'tile lower art changed')
        require(self.after.crop((48,0,self.before.width,8)).tobytes()==self.before.crop((48,0,self.before.width,8)).tobytes(),'unapproved tile changed')


def draw_recipe(j,a,v,fonts,locked):
    source=Image.open(BASE/v['preview']).convert('RGBA')
    require(raw_rgba_hash(source)==v['rgba_sha256'], 'workorder source RGBA pin drift')
    r=Redraw(source,fonts,locked);name=j['name'];tag=v['variant']
    if name in ('ClassicTitlescreenDefault','ClassicTitlescreenTransition'):
        return r,'preserved-brand-copyright-animation','品牌、署名、版权及全部转场帧保留；已逐不同像素帧目视。'
    if name in ('CollectableSpecialLabel','IconSpecialLabelActive','IconSpecialLabelInactive'):
        return r,'preserved-unconfirmed-micro-symbol','实际放大核验为极微型符号/装饰，不能可靠逐字转录；不幻猜。'
    if tag=='patch' and name in ('CardViewMenuBGTitle','CosmoTitleData','ClassicPretitleGamepad'):
        return r,'preserved-existing-chinese-regression','已汉化帧原样保留，含年龄横幅显隐。'
    if name in ('Observe','SelectItem','SelectProgram','SelectAgentClose','SelectMapClose'):
        ys=[y for y in range(source.height) for x in range(source.width) if source.getpixel((x,y))==BLUE]
        if not ys:return r,'preserved-empty-animation-frame','逐帧无英文文字；纯线、纯条和透明空帧保持精确rawRGBA。'
        english={'Observe':'OBSERVE','SelectItem':'SELECT ITEM','SelectProgram':'SELECT PROGRAM','SelectAgentClose':'SELECT AGENT','SelectMapClose':'SELECT AREA'}[name]
        r.text((6,min(ys)-1,250,max(ys)+2),english)
    elif name in ('CardViewMenuBG','CardViewMenuBGTitle'):
        r.text((6,1,161 if tag=='patch' else 249,15),'COSMOCARD VIEWER',align='left')
        if tag=='patch':r.text((168,1,250,16),'"A" KEY TO FLIP CARD')
    elif name=='ClassicHUDBreedMenu':
        r.text((6,1,249,15),'TRAINER TERMINAL' if tag=='jar' else 'B.R.E.E.D TERMINAL',align='left')
        r.text((6,177,249,191),'SELECT ACTION FROM ABOVE LIST')
    elif name=='ClassicHUDSubBreed':
        r.text((6,1,249,15),'SUB MENU POCKET TRAINER' if tag=='jar' else 'SUB MENU POCKET B.R.E.E.D.',align='left')
        r.text((6,177,249,191),'TAB LEFT / RIGHT')
    elif name=='CosmoCodecMenuBG':
        r.text((6,1,249,15),'SUB MENU COMMUNICATION',align='left')
        r.text((6,47,249,61),'CHOOSE RADIO CHANNEL ABOVE' if tag=='jar' else 'KEY "UP" AND "DOWN" TO SEARCH')
    elif name=='CosmoItemMenuBG':
        r.text((6,1,249,15),'PERSONAL ARCHIVE WRITER',align='left')
    elif name=='CosmoMissionLogMenuBG':
        r.text((6,1,249,15),'SUB MENU MISSION LOG',fg=BLACK,align='left')
        r.text((6,15,249,24),'CHOOSE A SUBJECT BELOW',8,fg=BLACK)
        r.text((6,177,249,191),'SELECT ENTRY ABOVE FOR INFO',fg=BLACK)
    elif name in ('CosmoSaveMenuBG','CosmoNameEntryMenuBG'):
        r.text((6,1,250,22),'PERSONAL ARCHIVE WRITER'+(' [R18]' if tag=='patch' else ''),align='left')
        # Refined slots EXCLUDE horizontal rule y42 and column rules x99..100/x211..213.
        r.text((6,23,99,33),'FILENAME',8)
        # F. DATA is deliberately left in source pixels, rather than expanding an unknown abbreviation.
        r.text((101,23,211,33),'LEVEL ATTEMPT',8)
        r.text((101,33,211,42),'LOCATION COM%',8)
        r.text((214,23,250,42),'TIME')
        if name=='CosmoSaveMenuBG':
            english='DEFAULT KEY SETTINGS: / ENTER CONFIG MENU WITH (Q)+(E) / OR (L SHOULDER) + (R SHOULDER)'
            lines=locked[english].split('\n')
            r.text((6,194,250,207),english,text=lines[0])
            r.text((6,207,250,222),english,text=lines[1])
        else:
            english='ENTER FILE NAME USING / CHARACTERS ABOVE AND OKAY';lines=locked[english].split('\n')
            r.text((6,195,250,208),english,text=lines[0])
            r.text((6,208,250,222),english,text=lines[1])
    elif name in ('CosmoSubData','CosmoTitleData'):
        r.text((6,1,249,15),'SUB MENU MEMORIES' if tag=='jar' else 'SUB MENU BESTIARY',align='left')
        r.text((6,15,249,24),'-SELECT DATA TO VIEW BELOW-',8)
    elif name=='CosmoSubMapBG':
        r.text((6,1,249,15),'SUB MENU MAP',align='left')
        r.text((6,177,249,191),'S=SAVE T=TELE ?=CLUE !=DATA',8)
    elif name=='CosmoSubMapV2BG':
        r.text((6,1,249,15),'SUB MENU NAVIGATION',align='left')
    elif name=='ClassicPretitleGamepad':
        r.text((0,22,256,49),'THIS GAME IS BEST PLAYED / WITH A CONTROL PAD',fg=YELLOW,bg=BLACK,source_inks=(YELLOW,(80,48,0,255)))
        r.text((0,79,256,95),'TO ACCESS GAME CONFIGURATION',fg=YELLOW,bg=BLACK,source_inks=(YELLOW,(80,48,0,255)))
        r.text((0,95,256,114),'PRESS (L+R) ON GAMEPAD / OR PRESS (Q+E) ON KEYBOARD',fg=YELLOW,bg=BLACK,source_inks=(YELLOW,(80,48,0,255)))
    elif name in ('CosmoGalleryBG','CosmoGalleryViewerBG'):
        r.text((14,17,242,31),'PERSONAL ARCHIVE WRITER',align='left')
        english='PRESS KEY "A" TO ADVANCE OR / REWIND SCENE WITH KEY "B"';lines=locked[english].split('\n')
        r.text((14,178,242,193),english,text=lines[0]);r.text((14,193,242,207),english,text=lines[1])
    elif name=='CosmoShopBG':
        r.text((6,33,139,47),'SHOPPING',align='left')
        r.text((22,54,80,65),'-STOCK-',8,fg=WHITE,bg=BLACK)
        r.text((91,54,139,65),'-COST-',8,fg=WHITE,bg=BLACK)
    elif name in ('CosmoGameOverBG','CosmoGameOverLiteBG'):
        r.text((5,1,94,10),'?CONTINUE?',8)
    elif name=='CosmoHUDUpdatedFlagDefault':
        if source.getbbox() and WHITE not in set(source.getdata()):
            return r,'preserved-blink-off-frame','更新提示灭帧；保持全黑，不添加中文。'
        r.text((0,0,32,8),'UPDATED',8,fg=WHITE,bg=BLACK)
    elif name in ('ClassicNameEntryBoxOKActive','ClassicNameEntryBoxOKInactive'):
        r.text((0,0,16,8),'OK!',8,fg=WHITE,bg=BLACK)
    elif name.startswith('ClassicTileset0'):
        r.tiles()
    elif name=='CosmoCasino2':
        # The conservative 40px workorder includes character art at x30..39,
        # y109..120! Erase only the three actual English glyph rectangles;
        # draw two native12 lines inside x0..29 and retain the arrow below.
        english='PRESS / TO / STOP';lines=locked[english].split('\n')
        r.text((0,96,30,108),english,fg=WHITE,bg=BLACK,text=lines[0],
               erase_boxes=[(0,97,38,104),(8,105,22,108)])
        r.text((0,108,30,121),english,fg=WHITE,bg=BLACK,text=lines[1],
               erase_boxes=[(8,108,22,112),(0,113,30,120)])
        require(r.after.crop((30,104,112,168)).tobytes()==r.before.crop((30,104,112,168)).tobytes(),'casino character art changed')
        require(r.after.crop((0,121,112,168)).tobytes()==r.before.crop((0,121,112,168)).tobytes(),'casino arrow/character art changed')
    else:raise ValueError('unhandled workorder '+name)
    return r,'redrawn','按本轮锁定逐字候选重排；动态槽、分割、Alpha、逐帧身份保持。'


def preview_sheets(replacements,retained):
    review=OUT/'review'
    for variant in ('jar','patch'):
        # Review every distinct resulting pixel frame, including untouched frames.
        seen=set();group=[]
        for row in replacements+retained:
            if row['variant']!=variant:continue
            key=row.get('new_rawRGBA_sha256',row['expected_rawRGBA_sha256'])
            if key in seen:continue
            seen.add(key)
            path=ROOT/row['newPNG'] if 'newPNG' in row else BASE/row['source_preview']
            im=Image.open(path).convert('RGBA')
            if row['logical_name'].startswith('ClassicTitlescreen'):continue # originals separately reviewed
            if row['logical_name'].startswith('ClassicTileset'):im=im.crop((0,0,64,32)).resize((256,128),Image.Resampling.NEAREST)
            elif im.width<=32:im=im.resize((im.width*8,im.height*8),Image.Resampling.NEAREST)
            group.append((row,im))
        for background in ('black','white'):
            color=(0,0,0,255) if background=='black' else (255,255,255,255)
            for start in range(0,len(group),12):
                sheet=Image.new('RGB',(960,1000),(70,70,70));d=ImageDraw.Draw(sheet)
                for i,(row,im) in enumerate(group[start:start+12]):
                    x=i%3*320;y=i//3*250
                    d.text((x+3,y+3),f"{row['workorder_id']} {row['logical_name']} {row['index']}",fill='white')
                    sheet.paste(Image.alpha_composite(Image.new('RGBA',im.size,color),im).convert('RGB'),(x,y+20))
                sheet.save(review/f'candidate-{variant}-{background}-{start//12+1}.png')


def build():
    for path,expected in PINS.items():require(digest((ROOT/path).read_bytes())==expected,'native font source pin drift')
    with zipfile.ZipFile(FONT12) as z:
        data12=z.read('fusion-pixel-12px-monospaced-zh_hans.bdf')
        require(digest(data12)=='b1e9a54fdd1c1e86fdc32efa16a04d8bd2897391ddb441238cee66947d6e3388','font12 BDF pin')
        # Licenses retained alongside rendered assets; no full font is redistributed here.
        (OUT/'LICENSE-FusionPixel-OFL.txt').write_bytes(z.read('OFL.txt'))
    locked=json.loads((OUT/'candidates.json').read_text(encoding='utf8'))['exact_text']
    required={ord(c) for text in locked.values() for c in text if c!='\n'}
    fonts={8:NativeFont(FONT8.read_bytes(),8,required),12:NativeFont(data12,12,required)}
    workorders=json.loads((BASE/'workorders.json').read_text(encoding='utf8'))
    replacements=[];retained=[]
    for dirname in ('png','masks','review'):(OUT/dirname).mkdir(exist_ok=True)
    for j in workorders['workorders']:
        for a in j['assets']:
            for v in a['variants']:
                if v['variant'] not in ('jar','patch'):continue
                r,status,note=draw_recipe(j,a,v,fonts,locked)
                region=v['region'];row={'workorder_id':j['workorder_id'],'logical_name':a['name'],
                    'index':region['index'],'ordinal':region['ordinal'],'variant':v['variant'],
                    'source_xy':region['xy'],'size':region['size'],'source_preview':v['preview'],
                    'expected_rawRGBA_sha256':v['rgba_sha256'],'status':status,'note':note}
                if status!='redrawn':
                    require(r.after.tobytes()==r.before.tobytes(),'retained row changed')
                    retained.append(row);continue
                proof=verify_replacement(r.before,r.after,r.mask)
                require(proof['changed_pixels']>0,'redraw must actually change pixels')
                require(r.before.getchannel('A').tobytes()==r.after.getchannel('A').tobytes(),'alpha exactness')
                stem=f"{v['variant']}__{a['name']}__{region['index']}__{region['ordinal']}"
                png=OUT/'png'/(stem+'.png');mask=OUT/'masks'/(stem+'.png')
                r.after.save(png);r.mask.save(mask)
                row.update({'newPNG':png.relative_to(ROOT).as_posix(),'newPNG_sha256':digest(png.read_bytes()),
                    'new_rawRGBA_sha256':raw_rgba_hash(r.after),'approved_mask':mask.relative_to(ROOT).as_posix(),
                    'approved_mask_png_sha256':digest(mask.read_bytes()),'operations':r.operations,**proof})
                replacements.append(row)
    require(len(replacements)+len(retained)==243,'243 target runtime row coverage')
    manifest={'schema':1,'scope':'independent-staging-only','base':'r27-story12-shaderfix-test5',
              'workorders':38,'target_variant_rows':243,'font_sources':PINS,
              'candidate_text_sha256':digest((OUT/'candidates.json').read_bytes()),
              'source_workorders_sha256':digest((BASE/'workorders.json').read_bytes()),
              'source_archives':json.loads((BASE/'archive-evidence.json').read_text(encoding='utf8')),
              'replacements':replacements,'retained':retained}
    write_json(OUT/'manifest.json',manifest)
    summary={'target_variant_rows':243,'workorder_count':38,'redrawn_rows':len(replacements),
             'retained_rows':len(retained),'retained_by_reason':dict(Counter(r['status'] for r in retained)),
             'changed_pixels':sum(r['changed_pixels'] for r in replacements),
             'changed_pixels_outside_approved_mask':sum(r['changed_pixels_outside_approved_mask'] for r in replacements),
             'alpha_changed_pixels':sum(r['alpha_changed_pixels'] for r in replacements),
             'font_sizes':dict(Counter(str(op['font_px']) for r in replacements for op in r['operations'])),
             'not_performed':['archive-build','install','deploy','game-launch','save-I/O','runtime-clip-validation'],
             'visual_review':'pending actual read_image of generated black/white sheets'}
    write_json(OUT/'verification.json',summary)
    required=''.join(sorted(set(''.join(op['zh'] for r in replacements for op in r['operations']))))
    write_json(OUT/'component.json',{'schema':1,'component':'r28-fixed-images','scope':'staging-only',
        'manifest':'localization/optimization/r28/images/manifest.json',
        'api':'localization/tools/optimized_images.py','api_contract':{
            'load_overrides':'load_overrides(variant, manifest_path=None) -> list[dict + image + mask]',
            'apply_overrides':'apply_overrides(decoded_RGBA_page, parsed_regions, variant, manifest_path=None) -> (new_page, report)',
            'region_fields':['name','index','ordinal','xy','size','rotation'],
            'fail_closed':['expected_rawRGBA_sha256','exact index+ordinal','source_xy','dimensions','PNG hash','approved-mask','unchanged-alpha','overlap consistency'],
            'side_effects':'Reads manifest/PNGs only; no writes, archive decoding, encryption or deployment.'},
        'required_chars':required,'required_codepoints':[ord(c) for c in required],
        'test_cli':'PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/images/test_images.py',
        'build_cli':'PYTHONIOENCODING=utf-8 /c/Windows/py.exe -3.12 -B localization/optimization/r28/images/build_images.py',
        'source_pins':{'workorders_sha256':manifest['source_workorders_sha256'],'font_sources':PINS},
        'counts':summary,'retained_abbreviations':['F. DATA','COM%','TELE','B.R.E.E.D'],
        'font_distribution':'Only rendered game images, no BDF/TTF. OFL notice bundled; original game pixels remain under original rights.'})
    preview_sheets(replacements,retained)
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':build()
