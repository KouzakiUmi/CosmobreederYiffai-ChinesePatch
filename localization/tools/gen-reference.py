#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 localization/work/lore/*.json 合成为人读参考文档 localization/docs/reference/*.md

用法：
    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/gen-reference.py

输入（缺哪个就跳过哪一节，不报错）：
    lore-dex.json                          图鉴实体 / 世界规则 / 待裁决
    lore-items.json                        物品实体 / 机制 / 待裁决
    characters-*.json                      角色画像
    plot-main.json, plot-vsn.json          剧情时序（主线 / 支线）

输出：
    docs/reference/README.md               索引与用法
    docs/reference/characters.md           角色声线红线
    docs/reference/lore.md                 名词总表与设定约束
    docs/reference/plot.md                 时序、剧透分层、占位符

注意：本脚本只读 JSON 写 Markdown，不碰任何译文。
"""
import json
import os
import sys

LORE = os.path.join('localization', 'work', 'lore')
OUT = os.path.join('localization', 'docs', 'reference')

TYPE_ZH = {
    'species': '物种 / 种族',
    'item': '物品',
    'place': '地点',
    'concept': '概念',
    'title': '头衔 / 职级',
    'org': '组织',
    'consumable': '消耗品',
    'key': '钥匙 / 通行类',
    'armor': '护甲',
    'weapon': '武器',
    'system': '系统 / 界面',
    'currency': '货币',
}

ISSUE_MARK = {
    'multiple_forms': '⚠ 一词多译',
    'suspicious': '⚠ 存疑',
    'none': '',
}


def load(name):
    p = os.path.join(LORE, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def cell(s):
    """Markdown 表格单元格转义。"""
    if s is None:
        return ''
    s = str(s).replace('\r', ' ').replace('\n', ' ')
    return s.replace('|', r'\|').strip()


def write(name, text):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('wrote %s (%d chars)' % (p, len(text)))


# ---------------------------------------------------------------- characters

def build_characters():
    files = sorted(
        f for f in os.listdir(LORE)
        if f.startswith('characters-') and f.endswith('.json')
    )
    chars = []
    for f in files:
        d = load(f)
        if d:
            chars.extend(d.get('characters', []))
    if not chars:
        return None

    L = []
    L.append('# 角色声线参考\n')
    L.append('从英文原文提取，**不是从译文反推**。校对时用这一页判断"这句话像不像这个人说的"。\n')
    L.append('优先级：本页红线 > 译文的现有措辞。出现冲突时以本页为准，按 revision 批次改。\n')
    L.append('角色共 %d 名。\n' % len(chars))

    L.append('## 速查\n')
    L.append('| 角色 | 身份 |')
    L.append('| --- | --- |')
    for c in chars:
        L.append('| %s | %s |' % (cell(c.get('name')), cell(c.get('identity'))))
    L.append('')

    for c in chars:
        L.append('## %s\n' % cell(c.get('name')))

        L.append('### 身份与说话场合\n')
        L.append(cell(c.get('identity')))
        L.append('')

        L.append('### 声线\n')
        L.append(cell(c.get('speech_style')))
        L.append('')

        traits = c.get('traits') or []
        if traits:
            L.append('### 性格证据\n')
            for t in traits:
                L.append('- **%s**' % cell(t.get('trait')))
                for ev in (t.get('evidence') or []):
                    L.append('  - `%s`' % cell(ev))
            L.append('')

        lines = c.get('red_lines') or []
        if lines:
            L.append('### 红线\n')
            for r in lines:
                L.append('- %s' % cell(r))
            L.append('')

        samples = c.get('samples') or []
        if samples:
            L.append('### 对照样例\n')
            L.append('| 原文 | 译法提示 |')
            L.append('| --- | --- |')
            for s in samples:
                L.append('| `%s` | %s |' % (cell(s.get('en')), cell(s.get('zh_hint'))))
            L.append('')

    return '\n'.join(L)


# --------------------------------------------------------------------- lore

def build_lore():
    dex = load('lore-dex.json') or {}
    items = load('lore-items.json') or {}

    ents = []
    for e in dex.get('entities', []):
        e = dict(e)
        e['_src'] = '图鉴'
        ents.append(e)
    for e in items.get('entities', []):
        e = dict(e)
        e['_src'] = '物品'
        ents.append(e)
    if not ents:
        return None

    L = []
    L.append('# 名词总表与设定约束\n')
    L.append('从英文原文提取，**不是从译文反推**。用途：定名一致、判断某个词该不该意译、避免把设定译错。\n')
    L.append('优先级：`GLOSSARY-LOCK.md` 已锁定的词 > 本页 > 模型建议。本页与锁表冲突时以锁表为准，并把冲突报出来。\n')
    L.append('条目共 %d 条（图鉴 %d + 物品 %d）。\n' % (
        len(ents), len(dex.get('entities', [])), len(items.get('entities', []))))

    # 有问题的先列，这是校对要动的部分
    flagged = [e for e in ents if e.get('translation_issue') in ('multiple_forms', 'suspicious')]
    L.append('## 待统一 / 待存疑（%d 条）\n' % len(flagged))
    L.append('这一节是校对的实际作业清单。`一词多译` 指同一英文词在现行译文里有多种写法；`存疑` 指现有译法可能导入原文没有的含义。\n')
    L.append('| 英文 | 现有译法 | 类型 | 问题 | 说明 |')
    L.append('| --- | --- | --- | --- | --- |')
    for e in flagged:
        L.append('| %s | %s | %s | %s | %s |' % (
            cell(e.get('en')),
            cell(e.get('zh')),
            TYPE_ZH.get(e.get('type'), cell(e.get('type'))),
            ISSUE_MARK.get(e.get('translation_issue'), ''),
            cell(e.get('notes')),
        ))
    L.append('')

    # 按类型全表
    L.append('## 全表\n')
    order = ['species', 'place', 'org', 'title', 'concept',
             'weapon', 'armor', 'consumable', 'key', 'currency', 'system', 'item']
    by_type = {}
    for e in ents:
        by_type.setdefault(e.get('type'), []).append(e)
    seen = set()
    for t in order + [k for k in by_type if k not in order]:
        if t in seen or t not in by_type:
            continue
        seen.add(t)
        rows = by_type[t]
        L.append('### %s（%d）\n' % (TYPE_ZH.get(t, t), len(rows)))
        L.append('| 英文 | 现有译法 | 来源 | 说明 |')
        L.append('| --- | --- | --- | --- |')
        for e in rows:
            L.append('| %s | %s | %s | %s |' % (
                cell(e.get('en')), cell(e.get('zh')), e['_src'], cell(e.get('notes'))))
        L.append('')

    rules = dex.get('world_rules') or []
    if rules:
        L.append('## 世界规则（%d 条）\n' % len(rules))
        L.append('这些是原文明确写出的设定边界。译文与这里冲突时，是译文错。\n')
        for r in rules:
            L.append('- %s' % cell(r))
        L.append('')

    mech = items.get('mechanics') or []
    if mech:
        L.append('## 机制（%d 条）\n' % len(mech))
        for m in mech:
            L.append('- %s' % cell(m))
        L.append('')

    oq = (dex.get('open_questions') or []) + (items.get('open_questions') or [])
    if oq:
        L.append('## 未决（%d 条）\n' % len(oq))
        L.append('原文证据不足、不能单方面定论的项。遇到相关句子不要自己拍板，记到 findings 里。\n')
        for q in oq:
            L.append('- %s' % cell(q))
        L.append('')

    return '\n'.join(L)


# --------------------------------------------------------------------- plot

VSN_GROUPS = [
    ('主线本体（开场 / 结局 / 世界史回溯）',
     ('主线开场', '世界观序章', '结局', '世界史回溯')),
    ('被俘特工任务记录（可选救援支线）', ('被俘任务记录',)),
    ('BOSS 战与剧情战', ('BOSS 战', '主线剧情战')),
    ('失败分支（Game Over）', ('失败记录',)),
]


def vsn_group(theme):
    for label, keys in VSN_GROUPS:
        for k in keys:
            if k in theme:
                return label
    return '其他'


def build_plot_vsn(L, vsn):
    """plot-vsn.json 的 schema 与主线不同：scripts / mirror_pairs / placeholders。"""
    scripts = vsn.get('scripts') or []

    L.append('### 脚本清单（%d 个）\n' % len(scripts))
    L.append('`m_` = 男主角 Yiffai 线，`f_` = 女主角 Yiffany 线。两线互为镜像前提：'
             '男线说失踪的是姐姐，女线说去找弟弟。\n')
    L.append('路径前缀一律 `vsn/<名字>/script.vsn`。\n')

    groups = {}
    for s in scripts:
        groups.setdefault(vsn_group(s.get('theme', '')), []).append(s)
    for label, _ in VSN_GROUPS + [('其他', ())]:
        rows = groups.get(label)
        if not rows:
            continue
        L.append('#### %s（%d）\n' % (label, len(rows)))
        L.append('<details><summary>展开</summary>\n')
        for s in rows:
            L.append('**`%s`** — %s' % (cell(s.get('path')), cell(s.get('theme'))))
            if s.get('who'):
                L.append('- 说话人：%s' % cell(s.get('who')))
            if s.get('summary'):
                L.append('- 内容：%s' % cell(s.get('summary')))
            if s.get('relation_to_main'):
                L.append('- 与主线关系：%s' % cell(s.get('relation_to_main')))
            L.append('')
        L.append('</details>\n')

    pairs = vsn.get('mirror_pairs') or []
    if pairs:
        L.append('### 男女线镜像配对（%d 组）\n' % len(pairs))
        L.append('校对时**不要**把同一组的男女两版当成同一段话的两种译法。'
                 '除少数逐字相同的过场外，事件本身不同（玩家与 NPC 角色互换）。\n')
        L.append('| 男线 | 女线 | 关系 |')
        L.append('| --- | --- | --- |')
        for p in pairs:
            L.append('| `%s` | `%s` | %s |' % (
                cell(p.get('m')), cell(p.get('f')), cell(p.get('note'))))
        L.append('')

    ph = vsn.get('placeholders') or []
    if ph:
        L.append('### 占位与格式注意\n')
        for p in ph:
            L.append('- %s' % cell(p))
        L.append('')


def build_plot():
    main = load('plot-main.json')
    vsn = load('plot-vsn.json')
    if not main and not vsn:
        return None

    L = []
    L.append('# 剧情时序\n')
    L.append('从英文原文提取。用途：判断一句话在剧情里处于什么位置、有没有提前泄露、是不是错把另一条线的设定搬过来。\n')
    L.append('**两条线是平行分支，不要把男线的事件并进女线，反之亦然。**\n')

    for label, d in (('主线', main), ('vsn 支线', vsn)):
        if not d:
            L.append('## %s\n' % label)
            L.append('_（待补）_\n')
            continue
        L.append('## %s\n' % label)

        # vsn 是另一套 schema：67 个脚本 + 镜像配对
        if label == 'vsn 支线' and 'scripts' in d:
            build_plot_vsn(L, d)
            continue

        layers = d.get('spoiler_layers') or []
        if layers:
            L.append('### 剧透分层与校对顺序\n')
            for s in layers:
                L.append('- %s' % cell(s))
            L.append('')

        regions = d.get('regions') or []
        if regions:
            L.append('### 区域推进（%d 区）\n' % len(regions))
            L.append('| 序 | 区域 | 内容 |')
            L.append('| --- | --- | --- |')
            for r in regions:
                L.append('| %s | `%s` | %s |' % (
                    cell(r.get('order')), cell(r.get('area')), cell(r.get('summary'))))
            L.append('')

        events = d.get('events') or []
        if events:
            L.append('### 关键事件（%d）\n' % len(events))
            for e in events:
                L.append('#### `%s` — %s\n' % (cell(e.get('entry')), cell(e.get('event'))))
                ev = e.get('evidence_en')
                if ev:
                    if isinstance(ev, list):
                        for x in ev:
                            L.append('- `%s`' % cell(x))
                    else:
                        L.append('- `%s`' % cell(ev))
                L.append('')

        endings = d.get('endings') or []
        if endings:
            L.append('### 结局（%d）\n' % len(endings))
            L.append('| 条件 | 结果 |')
            L.append('| --- | --- |')
            for e in endings:
                if isinstance(e, dict):
                    L.append('| %s | %s |' % (cell(e.get('condition')), cell(e.get('outcome'))))
                else:
                    L.append('| %s | |' % cell(e))
            L.append('')

        ph = d.get('placeholders') or []
        if ph:
            L.append('### 占位 / 未启用条目（%d）\n' % len(ph))
            L.append('这些是脚本里存在但玩家碰不到的条目（test、stub、未接线分支）。校对时不必为它们改译文，也不要拿它们当设定依据。\n')
            L.append('<details><summary>展开清单</summary>\n')
            for p in ph:
                L.append('- `%s`' % cell(p))
            L.append('\n</details>\n')

    return '\n'.join(L)


# ------------------------------------------------------------------- README

def build_readme(has):
    L = []
    L.append('# 参考库\n')
    L.append('从游戏英文原文提取的校对参考，用于代替"凭语感判断"。全部由原文取证，**不含从译文反推的结论**。\n')
    L.append('## 什么时候查哪一页\n')
    L.append('| 遇到的情况 | 查 |')
    L.append('| --- | --- |')
    L.append('| 这句台词不像这个人说的 / 拿不准语气 | [characters.md](characters.md) |')
    L.append('| 名词有多种写法 / 怀疑意译过头 / 设定是不是这样 | [lore.md](lore.md) |')
    L.append('| 有没有剧透 / 是不是把另一条线的设定搬过来 / 这句在哪 | [plot.md](plot.md) |')
    L.append('| 该词是否已锁定 | `../work/translate/GLOSSARY-LOCK.md` |')
    L.append('')
    L.append('## 优先级\n')
    L.append('1. `GLOSSARY-LOCK.md` 已锁定的译名')
    L.append('2. 本库（原文取证）')
    L.append('3. 模型建议 / 精校意见')
    L.append('')
    L.append('冲突时不自行取舍，记进 findings 交给裁决。\n')
    L.append('## 当前覆盖\n')
    L.append('| 文档 | 状态 |')
    L.append('| --- | --- |')
    for name, ok in has:
        L.append('| [%s](%s) | %s |' % (name, name, '已生成' if ok else '待补'))
    L.append('')
    L.append('## 重新生成\n')
    L.append('```')
    L.append('python localization/tools/gen-reference.py')
    L.append('```')
    L.append('源数据在 `localization/work/lore/*.json`。补了新 JSON 后重跑即可，本脚本只读 JSON 写 Markdown，不碰译文。\n')
    return '\n'.join(L)


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    if not os.path.isdir(LORE):
        sys.exit('missing %s' % LORE)

    has = []
    for name, fn in (('characters.md', build_characters),
                     ('lore.md', build_lore),
                     ('plot.md', build_plot)):
        text = fn()
        if text:
            write(name, text)
            has.append((name, True))
        else:
            print('skip %s (no input json)' % name)
            has.append((name, False))
    write('README.md', build_readme(has))
    return 0


if __name__ == '__main__':
    sys.exit(main())
