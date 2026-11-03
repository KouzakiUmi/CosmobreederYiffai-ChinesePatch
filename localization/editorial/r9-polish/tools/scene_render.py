"""Render pages with the candidate's own layout classes.

Earlier batches verified wrap rules reimplemented in Python and got them wrong
twice — once as plain greedy, once by mistaking which container the text goes
through. The fix is not a better reimplementation; it is to stop
reimplementing. `SceneRender` loads the shipped `DialogueWrap` / `DialogueGrid`
/ `PixelLayout` straight out of the candidate jar and prints what the engine
produces, page by page.

What the engine actually does (confirmed by running it, not by reading it):

* `storyPages` wraps at 240px with 12px Han glyphs, so a full line is 20
  characters;
* breaks prefer a punctuation boundary, and a line never *starts* with
  punctuation (`PixelLayout.legalBoundary`);
* `formatCapped`'s `q=28` is a UTF-16 ceiling, not the visual width — it only
  bites for lines that are wide but few characters (Latin-heavy ones);
* pages hold 3 lines, and the third is padded empty when the text is short.

So a 96-character sentence becomes pages of 20/20/… characters, and the only
lever on where a word gets cut is how many characters precede the boundary.
"""

import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
JDK = ROOT / 'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
TOOL = Path(__file__).resolve().parent / 'SceneRender.java'


def _escape(text):
    return (text.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
                .replace('\n', '\\n').replace('\t', '\\t'))


def render(candidate, cases):
    """Render `cases` [(key, container, archive, entry, line, body)] with the engine.

    `container` is `story` (Nb -> storyPages, story12 240px) or `radio`
    (JR -> pages, bbc2 150px). Returns {key: {'ok', 'container', 'pages'}}.
    """
    candidate = Path(candidate).resolve()
    jar = candidate / 'cosmobreeder-multi.jar'
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        subprocess.run([str(JDK / 'javac.exe'), '-encoding', 'UTF-8', '-nowarn',
                        '-cp', str(jar), '-d', str(tmp), str(TOOL)], check=True)
        tsv = tmp / 'in.tsv'
        tsv.write_text('\n'.join(
            '%s\t%s\t%s\t%s\t%d\t%s' % (k, c, a, e, n, _escape(b))
            for k, c, a, e, n, b in cases) + '\n', encoding='utf8')
        out = tmp / 'out.json'
        subprocess.run([str(JDK / 'java.exe'), '-Dfile.encoding=UTF-8',
                        '-cp', '%s%s%s' % (jar, ';' if __import__('os').name == 'nt' else ':',
                                           tmp),
                        'SceneRender', str(jar), str(tsv), str(out)], check=True)
        return json.loads(out.read_text(encoding='utf8'))


def firm_breaks(pages, bigrams, floor=30):
    """Break pairs the corpus treats as a firm collocation."""
    return [p for pg in pages for p in pg['breaks'] if bigrams.get(p, 0) >= floor]


def all_lines(pages):
    return [l for pg in pages for l in pg['lines'] if l]
