"""Persist component-only unit-test and pure apply evidence; no archive writes."""
from pathlib import Path
import json
import sys
import unittest
import zipfile

HERE=Path(__file__).resolve().parent
LOC=HERE.parents[3]
sys.path.insert(0,str(HERE));sys.path.insert(0,str(LOC/'tools'))
import ds_polish as ds
from codec import decrypt_file


def main():
    suite=unittest.defaultTestLoader.discover(str(HERE),pattern='test_ds_polish.py')
    with (HERE/'tests.log').open('w',encoding='utf8') as stream:
        result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    if not result.wasSuccessful():raise RuntimeError('DS polish test failure: inspect tests.log')
    manifest,_=ds.load_data();reports=[]
    with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/patch.pak') as z:
        for path,pin in manifest['resources'].items():
            _,report=ds.rewrite_ds_polish(path,decrypt_file(z.read(pin['archive_entry'])))
            reports.append(report)
    payload={'status':'passed','tests':result.testsRun,'scope':'pure byte/source conservation and glyph coverage; no game or DS runtime draw claim',
             'source_api_sha256':ds.sha((HERE/'ds_polish.py').read_bytes()),
             'component_manifest_sha256':ds.sha((HERE/'component_ds.json').read_bytes()),
             'canonical_joins_unchanged_sha256':ds.sha((LOC/'translations/dialogue-joins.jsonl').read_bytes()),
             'resources':reports}
    (HERE/'verification-report.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n','utf8')
    print('PASS DS polish: tests='+str(result.testsRun)+' revisions='+str(sum(r['applied_revisions'] for r in reports))+'; controls/EOL/source identity conserved')

if __name__=='__main__':main()
