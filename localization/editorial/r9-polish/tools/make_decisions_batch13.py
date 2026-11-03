"""Write the r9 batch-13 decision table (two routes: DS and Grok).

Both routes read the same order independently. Where they agree, one decision
lands and the other is recorded as a duplicate instead of being applied twice.
Where they touch the same row from different angles (the ESPER line: one route
fixes the doubled 「超能力者能力」, the other the 「这趟任务已经神志不清」 tail),
the two edits are merged into a single final line — one row, one decision.

Counts behind the rulings: 仓库 49 : 补给站 1, 监狱卫星 3 : 监狱月球 1,
金库 4 : 宝库 3, 导航地图 10 : 导航图 5, 传输点 2 : 通讯点 0.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

b = Batch('batch-13')

# ---------------------------------------------------------------- applied rows
# The flashlight hint is one merged sentence: the second row carries no Chinese
# of its own, so only the row that holds the text is written.
FLASHLIGHT = '  Mauser: [你要是能在那一带弄到手电筒，大概就能把这情况照亮！]'
for row_id in ('CAT:O3a0b3aa3acc3b24d2421', 'CAT:O20344914793486543264'):
    b.emit('R9M-' + row_id, 'R9M', 'B', 'idiom', row_id, 'apply', FLASHLIGHT,
           '「给这局面照点亮光」是照英文硬翻的搭配；改成「把这情况照亮」，信息与手电筒的照应都不丢。')

for row_id, final in (
        ('CAT:Oc0f91c324721a0de3d2b', '      Mauser: [你的导航地图应该能显示你弟弟在哪儿！]'),
        ('CAT:O4bb1917176b03c96c3f0', '      Mauser: [你的导航地图应该标着你姐姐的位置！]'),
        ('CAT:O4d5fa3e6980ddf738b6f', '      Mauser: [记得查看导航地图，找找新的可去之处！]')):
    b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final,
           'NAVMAP 在库内作「导航地图」10 处、「导航图」5 处，按多数统一为「导航地图」；三条提示一起改。')

# One merged line: the doubled「超能力者能力」and the「这趟任务已经神志不清」tail.
b.emit('R9M-CAT:Oce3606d9440e4057ffc5', 'R9M', 'A', 'meaning', 'CAT:Oce3606d9440e4057ffc5',
       'apply',
       '    Mauser: [你说你听见一个声音在讲「按 SELECT 循环切换超能力，再用 UP+ATTACK 使用该能力」时，'
       '我还以为你神志不清、出不了任务了！]',
       '两条路各自指出同一行的不同毛病：一路修「超能力者能力」套叠，一路指出「这趟任务已经神志不清」把主语挂错了；'
       '原文是「我以为你疯了、干不下去这趟任务」，合并成一句落地。')

for row_id, final, reason in (
        ('CAT:O545a0eb5f8c861d80e15',
         '      Mauser: [我方在那处区域的通讯记录显示，附近共有两名特工。]',
         '「我方对那处区域的通讯记录显示」把两个介词叠在一起；改后仍指同一份记录，不改信息。'),
        ('CAT:O493c14fdafa36c200802',
         '      Mauser: [你真的要上那颗监狱卫星吗？]',
         '同一场里作「监狱卫星」的有 3 行、作「监狱月球」的只有 1 行；卫星与月球不是一回事，按多数统一。'),
        ('CAT:Oc95bd1e399dd8adc59e1',
         '    Mauser: [既然你现在有了更高级别的门卡，应该能往仓库更深处走了！]',
         'DEPOT 在库内 49 处作「仓库」（含「仓库B」），只有这一行作「补给站」。'),
        ('CAT:Ocab1b8cea53383771fb3',
         '  Mauser: [那附近有好多高等级的门，那肯定说明某处有一张高级门卡！]',
         '「哪儿有一张」在提示里指代不明；改成「某处有一张」，信息不变。'),
        ('CAT:Oba807d87d2fe06bb2d62',
         '  Mauser: [伊吠妮，我探测到那颗卫星东北部深处有强烈能量特征。]',
         '本行在女线（`datadf`）里，patch 生效的英文写成了 YIFFAI，而同场同族的女线都称 YIFFANY；'
         '按 R3 的女线名字落地为「伊吠妮」，不照抄这条异常原文。')):
    b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final, reason)

for row_id in ('CAT:Od9e9751cf628c0f4bf21', 'CAT:Ofb45bfbe751df9c94593'):
    b.emit('R9M-' + row_id, 'R9M', 'C', 'idiom', row_id, 'apply',
           '    Mauser: [我还以为你已经想到办法离开那片地带了呢。]',
           '「我还以为……了呢？」是陈述句挂问号；这是断言不是疑问。两个副本同一句，一起改。')

# VAULT: three copies move together; one of them also needs the place name,
# so that row carries both edits in a single line.
VAULT_REASON = ('VAULT 在库内作「金库」4 处（含主角自述）、「宝库」3 处；按多数统一为「金库」，三份副本一起改。'
                '这一改与 R4 当初只改 sfw 副本的选择相反，特此记录为反向统一。')
for row_id, final in (
        ('CAT:Oc430b6793288363249c2', '    Mauser: [我们在你打开的那座金库更深处探测到强烈的暗能量涌动。]'),
        ('CAT:Oda168f4d2a5a7f7785d1', '    Mauser: [你在流放地东北发现的那座金库，看起来确实很重要。]'),
        ('SFW724b2e902a7a29aaef76970b', '    Mauser: [你在流放地东北发现的那座金库，看起来确实很重要。]')):
    b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final, VAULT_REASON)

b.emit('R9M-CAT:O44c85c169b59493dd7e9', 'R9M', 'C', 'idiom', 'CAT:O44c85c169b59493dd7e9',
       'apply', '    Mauser: [你找到的那个护腕应该能帮你前往新区域！]',
       '「派上用场，用来前往」两个「用」叠在一起；改后信息与句长都不变。')

b.emit_trailing_space(reason='中文行尾多出半角空格，英文原文行尾没有；只删空格，不动前缀与行尾。')

# ----------------------------------------------------------------- rejections
DUPLICATE = '与另一路指出同一处，取一条落地，避免同一行两条决定。'
b.reject('grok:P13-X001', '男女两版同一句，已按行分别落地（R9M 条目），此处不重复。')
b.reject('grok:P13-X002', '同上。')
b.reject('grok:P13-X003', '与 X004／X009 同一点，已按行分别落地（R9M 条目）。')
b.reject('grok:P13-X004', '同上。')
b.reject('grok:P13-X005', DUPLICATE + '（监狱月球→卫星，由 R9M 条目落地）')
b.reject('grok:P13-X006', '与 ds:P13-D004 同一行，合并成 R9M 条目落地。')
b.reject('grok:P13-X007', DUPLICATE + '（与 ds:P13-D005 同一行，取 DS 的最小改动版）')
b.reject('grok:P13-X008', DUPLICATE + '（补给站→仓库，由 R9M 条目落地）')
b.reject('grok:P13-X009', '同上。')
b.reject('grok:P13-X010', DUPLICATE + '（宝库→金库，由 VAULT 条目落地）')
b.reject('grok:P13-X011', '与 X012 落在同一行（补「流放地」与改「金库」），已合并成一条落地。')
b.reject('grok:P13-X012', '同上：同一行的两处改动合并为一条。')
b.reject('grok:P13-X013', DUPLICATE + '（sfw 副本，已含在 VAULT 条目里）')
b.reject('ds:P13-D001',
         'TRANSMISSION POINT 在库内只有「传输点」两处、没有「通讯点」；虽然 TRANSMISSIONS 作「通讯」，'
         '但地名要按地名本身的写法，改成一个库里不存在的写法没有依据。')
b.reject('ds:P13-D002', '护腕句已由 R9M 条目落地，原条目不重复落笔。')
b.reject('ds:P13-D003', DUPLICATE + '（与 grok:P13-X005 同一处）')
b.reject('ds:P13-D004', '与 grok:P13-X006 同一行，合并成 R9M 条目落地。')
b.reject('ds:P13-D005', '本行由 R9M 条目按最小改动落地，原条目不重复落笔。')
b.reject('ds:P13-D006', DUPLICATE + '（与 grok:P13-X008 同一处）')
b.reject('ds:P13-D007', DUPLICATE + '（与 grok:P13-X007 一族，取 R9M 条目）')
b.reject('ds:P13-D008', '「某处有一张」已由 R9M 条目落地，原条目不重复落笔。')
b.reject('ds:P13-D009', 'NAVMAP 作「导航地图」10 处、「导航图」5 处；本行已是多数写法，改成少数写法会让分叉变多。')
b.reject('ds:P13-D010', '女线称呼已由 R9M 条目落地，原条目不重复落笔。')
b.reject('ds:P13-D011', DUPLICATE + '（与 VAULT 条目同一行，合并）')
b.reject('ds:P13-D012', DUPLICATE + '（已含在 VAULT 条目里）')

print(b.close())
