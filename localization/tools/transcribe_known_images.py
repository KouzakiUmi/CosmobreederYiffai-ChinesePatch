"""Human-verified source transcriptions only; translations must come from Grok/reviewers."""
import collections
from projectlib import *
from extract_project import TextCatalog


def main():
    units=load_units();occ=load_occurrences()
    if any(u['category']=='image' for u in units):raise SystemExit('Image transcript units already present')
    catalog=TextCatalog();catalog.units={u['id']:u for u in units};catalog.occ=occ
    by_id={r['asset_id']:r for r in read_jsonl(PROJECT/'catalog/fixed_images.jsonl')}
    gamepad=['A4b6160b4569cc8b87687','Ada8d2a93e89e1525cbf1']
    entries=[
        (gamepad[:1],'THIS SOFTWARE IS FOR ADULTS ONLY','top_banner','Only present in blink-on frame.'),
        (gamepad,'THIS GAME IS BEST PLAYED WITH A CONTROL PAD','recommendation','Two physical lines in original image.'),
        (gamepad,'TO ACCESS GAME CONFIGURATION','configuration_heading',''),
        (gamepad,'PRESS (L+R) ON GAMEPAD','controller_chord','Keep the L+R chord unchanged.'),
        (gamepad,'OR PRESS (Q+E) ON KEYBOARD','keyboard_chord','Visual transcription Q+E; reviewer should confirm against input mappings before redrawing.'),
        (['Acfb74ff046445762b007'],'COSMOCARD VIEWER','viewer_heading',''),
        (['Acfb74ff046445762b007'],'"A" KEY TO FLIP CARD','flip_hint','The quoted A is a button/key label; preserve A.'),
        (['A3ad10e4fc08b09e2bef4'],'SUB MENU BESTIARY','bestiary_heading',''),
        (['A3ad10e4fc08b09e2bef4'],'-SELECT DATA TO VIEW BELOW-','bestiary_hint','')]
    transcripts=collections.defaultdict(list)
    for ids,source,fragment,note in entries:
        for aid in ids:
            a=by_id[aid];transcripts[aid].append(source)
            catalog.add('image',source,f'{aid}#{fragment}',context=a['name']+' | '+fragment,
                        extra={'asset_id':aid,'image_path':a['path'],'fragment':fragment,'transcription_notes':note,'requires_redraw':True})
    catalog.finish()
    rows=read_csv(PROJECT/'review/fixed_images.csv')
    for r in rows:
        if r['asset_id'] in transcripts:
            r.update(source_transcription='\n'.join(transcripts[r['asset_id']]),status='needs_redraw',review_notes='Source visually transcribed. See catalog image-unit occurrences; no automatic artwork edit.')
        elif r['name'] in ['ClassicPretitleFMOD','ClassicPretitleLogo']:
            r.update(status='not_text',review_notes='Trademark/company logo; preserve original artwork unless separately authorized.')
    write_csv(PROJECT/'review/fixed_images.csv',rows,list(rows[0]))
    write_json(PROJECT/'reports/image-transcription-summary.json',{'source_fragments':len(entries),'mapped_frames':len(transcripts),
               'method':'direct visual inspection of original extracted assets; no OCR or translation model assumed',
               'unreviewed_images_remain':True})
    summary=read_json(PROJECT/'reports/extraction-summary.json')
    summary.update(units=len(catalog.units),occurrences=len(catalog.occ),
                   unit_categories=dict(collections.Counter(u['category'] for u in catalog.units.values())),
                   occurrence_categories=dict(collections.Counter(o['category'] for o in catalog.occ)),
                   source_characters=sum(len(u['source']) for u in catalog.units.values()))
    write_json(PROJECT/'reports/extraction-summary.json',summary)
    print('Added',len(entries),'visually transcribed image text units; bitmap redraw is a separate pending stage.')


if __name__=='__main__':
    import collections
    main()
