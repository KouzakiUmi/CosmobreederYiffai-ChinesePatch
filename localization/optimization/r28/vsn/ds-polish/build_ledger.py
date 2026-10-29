"""Materialize individually reviewed DS text-only polish; never edit canonical ledgers."""
from pathlib import Path
from collections import Counter
import difflib
import hashlib
import json
import re
import sys
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
LOC=ROOT/'localization'
sys.path.insert(0,str(LOC/'tools'))
from codec import decrypt_file
from projectlib import read_jsonl


def sha(b):return hashlib.sha256(b).hexdigest()
def dump(name,x):(HERE/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n','utf8')
def jsonl(name,xs):(HERE/name).write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in xs),'utf8')
def body_eol(b):
    for end in (b'\r\n',b'\n',b'\r'):
        if b.endswith(end):return b[:-len(end)],end
    return b,b''


def build():
    packet=json.loads((HERE/'review-packet.json').read_text('utf8'))
    joins=read_jsonl(LOC/'translations/dialogue-joins.jsonl')
    units={u['id']:u for u in read_jsonl(LOC/'catalog/units.jsonl')}
    occ={o['occurrence_id']:o for o in read_jsonl(LOC/'catalog/occurrences.jsonl')}
    hyphen_fixes={'DH03':('功-能','功能'),'DH04':('物-理','物理'),
                   'DH10':('补-给','补给'),'DH12':('完-好','完好'),
                   'DH15':('发-生','发生'),'DH16':('物-理','物理'),
                   'DH18':('监-测','监测')}
    retain_hyphen={
        'DH01':('muffled-vocalization','Mmmn-hmm mmf为含混的鼻音/哼声，连字符对应发声衔接，不是词内排版断词；保留两次occurrence。'),
        'DH02':('true-stutter','源文N-NO重复起音，与受影响后急忙否认的语境一致；保留真实口吃。'),
        'DH05':('true-stutter','源文H-HEY重复起音，回应批评时结巴；不是HEY分音节排版断开。'),
        'DH06':('true-stutter','源文M-MAYBE重复起音，尴尬地劝对方别盯显示器；保留迟疑。'),
        'DH07':('true-stutter','源文W-WHAT疑问起音重复，与无线电断续后的吃惊一致。'),
        'DH08':('true-stutter','源文Y-YOU重复起音，焦急回应断续信号；保留真实口吃。'),
        'DH09':('true-stutter','源文N-NO重复起音，与受影响后急忙否认的语境一致。'),
        'DH11':('true-stutter','源文W-WELL为窘迫地接受四脚挖土建议时的口吃，不是单词中部排版断词。'),
        'DH13':('true-stutter','源文H-HOW重复起音，听到对方看穿兴奋时的吃惊。'),
        'DH14':('true-stutter','源文D-DONT重复起音，明确否认时结巴；保留语气。'),
        'DH17':('deliberate-self-correction','HACK- I MEAN HUNTING为刻意黑客/狩猎改口笑话，并非HACK某个后半词跨行续接；不机械抹去中断/改口。'),
        'DH19':('true-stutter','源文T-TASTY重复起音，对不明来源食物的惊疑；保留口吃。'),
        'DH20':('true-stutter','源文S-SURE重复起音，不情愿同意；不是SURE排版断开。'),
        'DH21':('true-stutter','源文T-THANKS重复起音并接GRR低吼，尴尬感谢的语气有据；不统一标点或清掉口吃。')}
    skip_reasons={
        'DS01':'原文先完整感谢并以Whew呼气结束，下一行另起铁砧感叹。中文呼——是松气停顿，不是词中断；保留独立点按。',
        'DS02':'TO Y-明确自我截断，随后OH HAR HAR识破坚果双关并改口；保留截断与揭示笑点的独立点按。',
        'DS03':'deep-后I mean明确掩饰欲望的自我改口；后句d-doing/f-f-fucking口吃也需保留，不能合并提前揭示。',
        'DS04':'AGE-在认出伊法伊前被自己中止，随后独立确认身份；保留先斥责再认人的悬念/角色事件时机。',
        'DS05':'some sort of...后下一行试探性辨认SCALE SUIT，属于悬念停顿和后续猜测，不是纯句法断词；不提前显露答案。'}
    scripts={};pins={}
    with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/patch.pak') as z:
        for path,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            data=decrypt_file(z.read(entry));scripts[path]=data.splitlines(keepends=True)
            pins[path]={'archive':'patch.pak','archive_entry':entry,'r27_plaintext_sha256':sha(data),'physical_line_count':len(scripts[path])}
    reviews=[];operations={};suggestions=[]
    def add_operation(case,path,line,prefix,new,classification,reason,inputs,join_id=None):
        raw=scripts[path][line-1];body,end=body_eol(raw);old=body.decode('utf8')
        assert old.startswith(prefix)
        payload=old[len(prefix):];leading=payload[:len(payload)-len(payload.lstrip())];trailing=payload[len(payload.rstrip()):]
        oldtext=payload.strip()
        newtext=new(oldtext) if callable(new) else new
        assert oldtext!=newtext
        newbody=prefix+leading+newtext+trailing
        n=line-1
        while n>=0 and not re.fullmatch(r'<[^<>]+>\s*',body_eol(scripts[path][n])[0].decode('utf8')):n-=1
        assert n>=0
        header=body_eol(scripts[path][n])[0].decode('utf8')
        opid='DSP-'+path.split('/')[0]+'-'+str(line)
        record={'schema_version':1,'operation_id':opid,'archive':'patch.pak','logical_path':path,
                'source_resource_sha256':pins[path]['r27_plaintext_sha256'],'line':line,
                'header_line':n+1,'full_header':header,'prefix':prefix,
                'input_line':old,'input_line_sha256':sha(body),'old_text':oldtext,'replacement':newtext,
                'output_line':newbody,'replacement_sha256':sha(newtext.encode('utf8')),
                'classification':classification,'reason':reason,'canonical_join_id':join_id,
                'inputs':inputs,'origin':{'status':'candidate_user_requested','independent_qa_approval':False},
                'text_edits':[{'tag':tag,'old_range':[a,b],'new_range':[c,d],'before':oldtext[a:b],'after':newtext[c:d]}
                              for tag,a,b,c,d in difflib.SequenceMatcher(None,oldtext,newtext,autojunk=False).get_opcodes()]}
        if opid in operations:
            assert operations[opid]['output_line']==newbody
        else:operations[opid]=record
        return opid
    def identities(rows):
        return [{'occurrence_id':o['occurrence_id'],'unit_id':o['unit_id'],'line':o['line'],
                 'source_en':units[o['unit_id']]['source'],'source_sha256':units[o['unit_id']]['source_sha256'],
                 'raw_payload_sha256':o['raw_payload_sha256']} for o in rows]
    for case in packet:
        cid=case['case_id'];row={'case_id':cid,'kind':case['kind'],'context':case.get('context'),
                               'decision':'retained','operations':[],'source_case':case}
        if case['kind']=='unit-cjk-word-hyphen':
            if cid in hyphen_fixes:
                a,b=hyphen_fixes[cid]
                classification='english-layout-word-break-contamination'
                reason=f'英文单词内部排版断词被错误投射成中文词内{a}，无起音重复或改口；仅复原{b}。'
                if cid=='DH18':reason+='该entry虽为TestA，仍只修精确文案，不改可达性或测试控制。'
                for item in case['occurrences']:
                    o=item['occurrence'];j=item['joined'];inputs=identities([occ[i['occurrence_id']] for i in j['inputs']]) if j else identities([o])
                    op=add_operation(cid,o['logical_path'],item['effective_line'],o['prefix'],lambda text,a=a,b=b:text.replace(a,b),classification,reason,inputs,j['join_id'] if j else None)
                    row['operations'].append(op)
                row.update(decision='revised',classification=classification,reason=reason)
            else:
                classification,reason=retain_hyphen[cid];row.update(classification=classification,reason=reason)
        elif case['kind']=='merged-ascii-hyphen':
            j=case['join'];inputs=identities([occ[i['occurrence_id']] for i in j['inputs']])
            if cid in ('DM01','DM05'):
                classification='english-parenthetical-punctuation-transfer';reason='两个空格包围的ASCII短横是英文插入语标点；改为中文破折号保留插入语停顿，不删插话内容。'
                op=add_operation(cid,j['logical_path'],j['physical_lines'][0],j['prefix'],lambda text:text.replace(' - ','——'),classification,reason,inputs,j['join_id'])
            elif cid in ('DM07','DM08'):
                a,b=('功-能','功能') if cid=='DM07' else ('完-好','完好')
                classification='english-layout-word-break-contamination';reason='与DH03/DH12同一冻结已合句节点，去掉英文functional排版断词污染；不重复应用修订。'
                op=add_operation(cid,j['logical_path'],j['physical_lines'][0],j['prefix'],lambda text,a=a,b=b:text.replace(a,b),classification,reason,inputs,j['join_id'])
            elif cid in ('DM11','DM12','DM13','DM14','DM15','DM16'):
                classification='english-layout-word-break-contamination';reason='英文CURR- ENTLY仅排版断词，投射的“目- 前”不是中文口吃；恢复“目前”，保留本entry/说话人/括号。'
                op=add_operation(cid,j['logical_path'],j['physical_lines'][0],j['prefix'],lambda text:text.replace('目- 前','目前'),classification,reason,inputs,j['join_id'])
            elif cid=='DM17':
                classification='layout-word-break-and-incomplete-sentence';reason='ANY- THING是排版断词而非中断；中文“伤人比…更狠”生硬且唯一未括起无句末标点，按完整伤害比较句收束，不增加信息。'
                op=add_operation(cid,j['logical_path'],j['physical_lines'][0],j['prefix'],'关键是务必避免撞上那只大壮兽。它造成的伤害比那里其他任何东西都大。',classification,reason,inputs,j['join_id'])
            else:
                classification='model-identifier' if cid=='DM04' else 'deliberate-interruption'
                reason={'DM02':'FU-被另一角色打断，保留断口，不补齐句子。',
                        'DM03':'YO-解释定位时被角色催促打断，保留句末断口。',
                        'DM04':'3P-X69是源文型号，短横属于身份标记，不是污染。',
                        'DM06':'YO-解释定位时被角色催促打断，保留句末断口。',
                        'DM09':'THEYLL-因被打断而中止，下一说话人介入；保留停顿。',
                        'DM10':'KNOCK ME U-是刻意双关中断，保留含蓄断口，不补成完整句。'}[cid]
                row.update(classification=classification,reason=reason);reviews.append(row);continue
            row.update(decision='revised',operations=[op],classification=classification,reason=reason)
        else:
            row.update(classification='derived-coverage-skip',reason=skip_reasons[cid])
        reviews.append(row)
    assert len(operations)==16
    ops=list(operations.values())
    jsonl('review-ledger.jsonl',reviews);jsonl('operations.jsonl',ops)
    dump('derived-skips.json',[r for r in reviews if r['kind']=='unrecorded-skip'])
    required=''.join(sorted(set(''.join(o['replacement'] for o in ops))))
    (HERE/'required_chars.txt').write_text(required+'\n','utf8')
    dump('source-polish-suggestions.json',[{'canonical_operation_id':o['operation_id'],'source_en':[i['source_en'] for i in o['inputs']],
          'source_sha256':[i['source_sha256'] for i in o['inputs']],'canonical_header':o['full_header'],
          'prefix':o['prefix'],'old_zh_CN':o['old_text'],'candidate_zh_CN':o['replacement'],
          'warning':'SFW独立来源/上下文/译文核验建议，不是SFW允许表或行号定位规则。'} for o in ops])
    summary={'review_cases':len(reviews),'cjk_word_hyphen_units':21,'revised_cjk_word_hyphen_units':7,
             'retained_cjk_word_hyphen_units':14,'merged_ascii_hyphen_cases':17,'revised_merged_cases':11,
             'retained_merged_cases':6,'derived_skip_edges':5,'distinct_text_lines_revised':16,
             'by_resource':dict(Counter(o['logical_path'] for o in ops)),'removed_text_nodes':0,'control_or_timing_changes':0}
    dump('component_ds.json',{'schema_version':1,'component':'r27-pak-ds-polish','archive':'patch.pak',
         'frozen_build':'r27-story12-shaderfix-test5','resources':pins,
         'canonical_join_ledger_sha256':sha((LOC/'translations/dialogue-joins.jsonl').read_bytes()),
         'operations_sha256':sha((HERE/'operations.jsonl').read_bytes()),'review_ledger_sha256':sha((HERE/'review-ledger.jsonl').read_bytes()),
         'required_chars':'localization/optimization/r28/vsn/ds-polish/required_chars.txt',
         'required_chars_sha256':sha((HERE/'required_chars.txt').read_bytes()),
         'api':{'module':'localization/optimization/r28/vsn/ds-polish/ds_polish.py','function':'rewrite_ds_polish',
                'signature':"rewrite_ds_polish(logical_path, r27_plain_bytes, archive='patch.pak') -> (new_bytes, report)",
                'call_order':'decrypt frozen r27 PAK datadf/1 or datadm/1 -> polish -> encrypt; never apply to SFW or re-run canonical joins'},
         'tests':['/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/ds-polish/verify.py'],
         'summary':summary})
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':build()
