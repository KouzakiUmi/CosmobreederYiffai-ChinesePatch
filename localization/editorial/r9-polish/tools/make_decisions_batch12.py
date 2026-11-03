"""Write the r9 batch-12 decision tables (three parts, single-route: DS only).

The Gemini route failed again on the first trial part, so this expansion batch
lands on the DS route plus the main agent's trailing-space pass, exactly like
batch-10.

Rulings specific to this batch:

* Anomaly ranks are unified to one wording — 「已获得异常体 阿尔法／贝塔／伽马／奥密克戎」 —
  across all eight mission-log headers. The dictionary and the cards already say
  阿尔法／伽马 in Chinese while the headers kept Latin; the female lines said
  已获取 and the male ones 已获得, and one male line dropped 体.
* Key names stay literal (`UP+ATK`, `DOWN+JUMP`, `SELECT`), as batch-10 and
  batch-11 already ruled; three rows had them translated into Chinese again.
* Cross-surface naming (Zener shape labels, STARSUIT) is left alone: renaming an
  item across dictionary／card／log surfaces needs one global ruling, and the
  labels and the log sentences are each internally consistent. Recorded in
  LEFTOVERS.md instead.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

SKIP = ('ui.end', 'ui.backers', 'ui.options')

# One wording for the whole anomaly family, whatever the part.
ANOMALY = {
    'CAT:O0115379ce41430c0f5a3': '已获得异常体 贝塔',
    'CAT:O4a55f0d0855295ec691c': '已获得异常体 伽马',
    'CAT:O224df3feba5259136068': '已获得异常体 奥密克戎',
    'CAT:O4d512d9660c464937935': '已获得异常体 伽马',
    'CAT:O8e693539f4176a2c26f8': '已获得异常体 阿尔法',
    'CAT:O51cb2f4e2b75ec5d5388': '已获得异常体 阿尔法',
    'CAT:O00f5e4dc3a462f81e30c': '已获得异常体 贝塔',
    'CAT:Oc6f3f1cbb00514abb7da': '已获得异常体 奥密克戎',
}

APPLY = {
    'batch-12-part01': [
        ('ds', 'P12-0105', 'HAUNTING 在库内 4 处都作谓语「作祟」，这里它是修饰地点的形容词，读「阴森」才通。'),
        ('ds', 'P12-0106', 'SPIKE 在库内已落地为「尖刺」；「刺机器人」是逐词直译，且丢掉了「尖刺」这个既有写法。'),
        ('ds', 'P12-0107', '按键名一律保留英文（batch-10／11 已裁决）；同 root 的 sfw 侧就写 `按DOWN+JUMP`。'),
        ('ds', 'P12-0108', '「精灵加成」是原文没有的增译，且语序与本组另两条不一致；原文只说精灵闲置时回精神力。'),
        ('ds', 'P12-0111', '中文行尾多一个半角空格，英文原文行尾没有；只删空格。'),
    ],
    'batch-12-part02': [
        ('ds', 'P12-0205', '按键名保留英文（batch-10／11 已裁决）；「选择」是把 SELECT 译了两遍。'),
        ('ds', 'P12-0206', '按键名保留英文；「空中下+跳跃」还把按键语序读错了，原文是空中按 DOWN+JUMP。'),
        ('ds', 'P12-0207', 'MELON 在库内作「瓜」；「一对好货」把水果读成了货物。'),
        ('ds', 'P12-0208', '整段误译：PRETZEL 是扭结面包，「硬结打卷｜育得正好」把面包读成了育种。'),
        ('ds', 'P12-0209', 'RAPER 是 RAPIER 掉字的原文；同 root 描述行与另一侧都作「细剑」，现译把它读成了罪名。'),
    ],
    'batch-12-part03': [
        ('ds', 'P12-0305', '中文行尾多一个半角空格；同 root 的 sfw 侧英文自带尾空格，属镜像，不动。'),
        ('ds', 'P12-0306', '按键名保留英文（batch-10／11 已裁决）；同 root 的 sfw 侧已作 `按UP+ATK`。'),
        ('ds', 'P12-0307', 'SOFT & CREAMY 是褒义的口感，译作「又软又腻」把褒义读成了负面。'),
    ],
}

EXTRA_EMIT = {
    # P12-0203 reports `CAT:O491243629a3f33f762d`; the row in the order is
    # `CAT:O4912436292a3f33f762d` (one character short). Landed on the real row.
    'batch-12-part02': [('R9M-CAT:O4912436292a3f33f762d', 'CAT:O4912436292a3f33f762d',
                         '大壮兽王',
                         'KINGBOLD 是 BIGBOLD 的王者变体，BIGBOLD 在库内一律作「大壮兽」；「胆王」把它读成了胆量。'
                         '（提案里的 row_id 少一位，已按工单里的真实 row_id 落地。）')],
}

REJECT = {
    'batch-12-part01': {
        'ds:P12-0101': '整族由 R9M 条目统一处理（含本条所在行），避免同一行两条决定。',
        'ds:P12-0103': '等级名是否中文化属跨面命名口径：词典与卡面已作中文，任务日志 8 行留拉丁，两条路各自内部一致；'
                       '本批已按「整族统一为中文」处理 header 行（见 R9M 条目），此处不再单独立案。',
        'ds:P12-0104': 'Zener 形状在词典作「三角／星星／圆圈」、任务日志整句作「三角形／星形／圆形」，两面各自成体系；'
                       '改词条名会同时影响物品栏与图鉴，属跨面命名口径，进 LEFTOVERS 等终裁。',
        'ds:P12-0109': '本侧写法已正确（`按UP+ATK`），要改的是另一侧那两行，落在本批之外；本批不改本行。',
        'ds:P12-0110': '同 P12-0109：本侧已作 `按(SELECT)`，需改的是另一侧副本，本批不改本行。',
    },
    'batch-12-part02': {
        'ds:P12-0203': '提案的行 id 少一位（`…629a3f…` 与工单里的 `…6292a3f…`），'
                       '本批已按真实 row_id 用 R9M 条目落地，原条目不重复落笔。',
        'ds:P12-0201': '整族由 R9M 条目统一处理（含本条所在行）。',
        'ds:P12-0202': '与 R9M 行尾空格条目同一行同一点，取机械条目。',
        'ds:P12-0204': '「通讯联络」与「探测秘密」两句在两侧只是措辞差异，看不出哪一侧更贴原文；不凭偏好改。',
        'ds:P12-0210': '同 P12-0104：Zener 形状在词典与任务日志两面各自成体系，改词条名属跨面命名口径，进 LEFTOVERS。',
    },
    'batch-12-part03': {
        'ds:P12-0302': '整族由 R9M 条目统一处理（含本条所在三行）。',
        'ds:P12-0301': '与 R9M 行尾空格条目同一行同一点（另有 4 行在 note 里），取机械条目。',
        'ds:P12-0303': 'STARSUIT 现作「星装」，与 COSMOSUIT「宇宙服」、KOBOSUIT「科博服」是同一命名系列；'
                       '改成「星服」会与剧情里的「星际服」「星服降落伞」形成第三种写法，属跨面命名口径，进 LEFTOVERS。',
        'ds:P12-0304': '男女两侧各一种写法、次数 1:1，没有多数可依；两种都通，不凭偏好改动。',
        'ds:P12-0308': '原文 `HARD KNOTTED|BRED` 本身可疑（BRED／BREAD），现译按育种解；没有新证据前不改，记 needs_evidence。',
    },
}

# Second route (Grok). Most of it lands on the same points as the DS route; where
# it does, one decision lands and the other is recorded as a duplicate. The two
# genuinely new items are the fish-taco description (an ethnonym the English does
# not contain) and a batch of format notes that the mechanical pass already owns.
GROK_APPLY = {
    'batch-12-part03': [
        ('P12-0307', 'SFWf7a2de9d85d4e27997b5f8aa', '烤鱼|夹在薄饼里',
         '原文只说 GRILLED FISH IN A TORTILLA，没有「墨西哥」；现译加了地名并把两段顺序颠倒，'
         '按原文分段改为「烤鱼|夹在薄饼里」。'),
    ],
}

GROK_REJECT = {
    'batch-12-part02': {
        'P12-X201': '与 R9M 行尾空格条目同一行同一点，取机械条目。',
        'P12-X202': '同上。',
        'P12-X203': '要删的是值末尾的换行：本批台账按行写，值里的换行无法表达（build_ledger 会拒绝），'
                    '属既有限制，记入 LEFTOVERS。',
        'P12-X204': '同上：末尾换行，行式台账表达不了。',
        'P12-X205': '这一段要重排分段并补「她的」，改动量超出「同一行内替换」，且现译尚未确认哪一段漏了；'
                    '留给专门的一次分段校订，不在本批强行拼。',
        'P12-X206': '整族已由 R9M 条目统一为「已获得异常体 X」（含本条两行），等级名取中文。',
        'P12-X207': '与 ds:P12-0203 同一行，已由 R9M 条目落地。',
        'P12-X208': '与 ds:P12-0205 同一处，已落地。',
        'P12-X209': '与 ds:P12-0206 同一处，已落地。',
        'P12-X210': '与 ds:P12-0208 同一处，已落地。',
        'P12-X211': 'FENFEN 的中文写法尚未终裁（词典另有「芬芬」候选）；两路提了两种互不相同的拉丁写法，'
                    '都不能当定论，记入 LEFTOVERS。',
    },
    'batch-12-part03': {
        'P12-0301': '整族已由 R9M 条目统一为「已获得异常体 X」（含本条三行）。',
        'P12-0302': '同上：等级名取中文写在同一条 R9M 决定里。',
        'P12-0303': '与 ds:P12-0304 同一行：两侧各一种写法、次数 1:1，第三路又提了第三种；没有多数可依，不改。',
        'P12-0304': '与 ds:P12-0306 同一处，已落地。',
        'P12-0305': 'FENFEN 写法未终裁；本条主张保留拉丁，与另一路的「Fenfen译」相反，两说都不能当定论，记入 LEFTOVERS。',
        'P12-0306': '与 ds:P12-0307 同一处，已落地。',
    },
}

ANOMALY_REASON = ('任务日志八条同一模板统一为「已获得异常体 X」：等级名取中文（词典与卡面即中文），'
                  '动词取「获得」（女线原「已获取」），并补回男线漏掉的中心词「体」。')

b = Batch(sys.argv[1]) if len(sys.argv) > 1 else None
if b is None:
    raise SystemExit('usage: make_decisions_batch12.py <batch-12-partNN>')

for route, fid, reason in APPLY[b.batch]:
    b.apply_finding(route, fid, reason)

for row_id, final in ANOMALY.items():
    if row_id in b.rows:
        b.emit('R9M-' + row_id, 'R9M', 'B', 'term', row_id, 'apply', final, ANOMALY_REASON)

for key, row_id, final, reason in EXTRA_EMIT.get(b.batch, []):
    b.emit(key, 'R9M', 'A', 'meaning', row_id, 'apply', final, reason)

for key, reason in REJECT[b.batch].items():
    b.reject(key, reason)

for fid, row_id, final, reason in GROK_APPLY.get(b.batch, []):
    b.emit('R9M-' + fid, 'R9M', 'B', 'meaning', row_id, 'apply', final, reason)

for fid, reason in GROK_REJECT.get(b.batch, {}).items():
    b.reject('grok:' + fid, reason)

b.emit_trailing_space(skip_roots=SKIP,
                      reason='中文行尾多出半角空格，英文原文行尾没有；只删空格，不动 `|` 与换行。')

print(b.close())
