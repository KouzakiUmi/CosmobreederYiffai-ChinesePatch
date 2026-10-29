"""采集 R2 留置项的运行时/资源证据，输出可复跑 JSON。

覆盖四类此前标为"用途未证/原音待核"的阻塞点：
  1. audio/0-3 -> FMOD bank 事件清单（是否存在语音对白演出）
  2. datav/1 -> dictionary.json 的 ui.breeding / ui.end.BadEnding / StatPretzel / ElfBuff 键
  3. datay/1 -> scripts_pack.json 的 shops products displayName
  4. 源归档 SHA 与候选归档身份绑定

只读原始归档与项目 codec，不写任何归档、台账或译文。
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'localization' / 'tools'))
from codec import decrypt_file  # noqa: E402

# 原版基线：项目 backup/ 下的两份归档，SHA 与 localization/sources/archives.json 记录一致。
# 游戏安装目录当前可能处于已打补丁状态，不能作为英文源使用。
JAR = ROOT / 'backup' / 'cosmobreeder-multi.jar'
PAK = ROOT / 'backup' / 'patch.pak'
INSTALLED = Path(r'C:\SteamLibrary\steamapps\common\Cosmobreeder Yiffai')
BASELINE = json.loads((ROOT / 'localization' / 'sources' / 'archives.json').read_text(encoding='utf-8'))


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def audio_events(jar):
    manifest = json.loads(decrypt_file(jar.read('audio/0')))
    bank = json.loads(decrypt_file(jar.read('audio/1')))
    events = [e['path'] for e in bank if e.get('header') == 'event:']
    music = [e for e in events if e.startswith('event:/Music/')]
    sfx = [e for e in events if not e.startswith('event:/Music/')]
    voice_like = [e for e in events
                  if any(k in e.lower() for k in ('voice', 'vox', 'dialog', 'speech', 'line'))]
    return {
        'manifest': manifest,
        'event_total': len(events),
        'music_count': len(music),
        'sfx_count': len(sfx),
        'voice_like_events': voice_like,
        'radio_events': [e for e in events if 'radio' in e.lower()],
        'has_narration_voice': bool(voice_like),
        'events': events,
    }


def dictionary(jar, pak):
    # 原版 jar 保留英文源；patch.pak 仅作当前中文覆盖层，两者分开记录。
    original = json.loads(decrypt_file(jar.read('datav/1')))
    overlay = json.loads(decrypt_file(pak.read('datav/1')))
    merged = dict(original)
    merged.update(overlay)

    def pick(prefixes, source=merged):
        return {k: v for k, v in sorted(source.items())
                if any(k.startswith(p) for p in prefixes)}

    return {
        'key_total': len(merged),
        'overlay_changed_keys': sum(1 for k, v in overlay.items() if original.get(k) != v),
        'breeding_keys': pick(['ui.breeding.']),
        'badending_keys': pick(['ui.end.BadEnding.']),
        'pretzel': pick(['StatPretzel.']),
        'pretzel_source': pick(['StatPretzel.'], original),
        'pepper_reference': pick(['StatPepper.'], original),
        'elf_buff': pick(['SpecialFap.ElfBuff.']),
        'elf_buff_source': pick(['SpecialFap.ElfBuff.'], original),
        'cosmobody_item': pick(['CosmoBody.']),
        'hardknotted_source': {k: v for k, v in original.items()
                               if 'HARD KNOTTED' in str(v).upper()},
    }


def scripts_pack(jar):
    data = json.loads(decrypt_file(jar.read('datay/1')))
    shops = data.get('shops', {})
    out = {}
    for variant, table in shops.items():
        for shop_id, shop in table.items():
            for index, product in enumerate(shop.get('products') or []):
                if product.get('displayName'):
                    out.setdefault(variant, []).append({
                        'shop': shop_id,
                        'index': index,
                        'item': product.get('item'),
                        'price': product.get('price'),
                        'inStockCondition': product.get('inStockCondition'),
                        'displayName': product['displayName'],
                    })
    return {'sections': sorted(data.keys()), 'display_name_entries': out}


def main():
    installed = {}
    for name in ('cosmobreeder-multi.jar', 'patch.pak'):
        path = INSTALLED / name
        installed[name] = {'sha256': sha256(path) if path.exists() else None,
                           'matches_baseline': False}
    baseline_by_tag = {row['tag']: row['sha256'] for row in BASELINE}
    installed['cosmobreeder-multi.jar']['matches_baseline'] = (
        installed['cosmobreeder-multi.jar']['sha256'] == baseline_by_tag.get('jar'))
    installed['patch.pak']['matches_baseline'] = (
        installed['patch.pak']['sha256'] == baseline_by_tag.get('patch'))

    report = {
        'schema': 'cosmo-editorial-r4-evidence/v1',
        'baseline': {
            'jar': {'path': str(JAR), 'sha256': sha256(JAR),
                    'expected': baseline_by_tag.get('jar')},
            'pak': {'path': str(PAK), 'sha256': sha256(PAK),
                    'expected': baseline_by_tag.get('patch')},
        },
        'installed_state': installed,
    }
    report['baseline']['jar']['verified'] = (
        report['baseline']['jar']['sha256'] == baseline_by_tag.get('jar'))
    report['baseline']['pak']['verified'] = (
        report['baseline']['pak']['sha256'] == baseline_by_tag.get('patch'))
    if not (report['baseline']['jar']['verified'] and report['baseline']['pak']['verified']):
        raise SystemExit('baseline archives do not match recorded SHA; refusing to collect evidence')

    with zipfile.ZipFile(JAR) as jar, zipfile.ZipFile(PAK) as pak:
        report['audio'] = audio_events(jar)
        report['dictionary'] = dictionary(jar, pak)
        report['scripts_pack'] = scripts_pack(jar)

    target = Path(__file__).resolve().parents[1] / 'evidence' / 'runtime-evidence.json'
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'wrote {target.relative_to(ROOT)}')
    print('baseline jar/pak verified:', report['baseline']['jar']['verified'],
          report['baseline']['pak']['verified'])
    print('installed jar matches baseline:', installed['cosmobreeder-multi.jar']['matches_baseline'])
    print('installed pak matches baseline:', installed['patch.pak']['matches_baseline'])
    print('audio events:', report['audio']['event_total'],
          'voice-like:', len(report['audio']['voice_like_events']))
    print('breeding keys:', len(report['dictionary']['breeding_keys']),
          'badending keys:', len(report['dictionary']['badending_keys']))
    print('displayName entries:', sum(len(v) for v in report['scripts_pack']['display_name_entries'].values()))


if __name__ == '__main__':
    main()
