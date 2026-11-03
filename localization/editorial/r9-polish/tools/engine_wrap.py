"""The game's *actual* wrap rule, established by disassembling the original classes.

Everything before this file modelled `PRG/DialogueWrap`, which turns out to be a
**test-only reference implementation**: `CorePatch` injects exactly one call to
it (`terminalText`), and `story` / `radio` / `storyPages` / `pages` are never
patched into the game. The game still runs the original obfuscated `PRG/amw`.

So the earlier measurements — plain greedy, then `PixelLayout`'s punctuation
rules — were both measuring the wrong thing. What the game really does:

    PRG.amw.a(String, amq)                      // split into lines
      -> PRG.amr$e.a(String, String)            // split on "<p>"
      -> PRG.aDJ.e(String, int)                 // -> aCj iterator
      -> PRG.aDI$a.p()                          // substring(c, c + cols)
      -> PRG.aDJ.a(String, int, int)            // plain String.substring

`PRG.aDI$a.p()` takes the cursor `c` and returns `substring(c, c + b)` where `b`
is the column count handed in at construction. There is **no width measurement,
no punctuation avoidance, and no word awareness**: every line is a fixed number
of characters, cut wherever the count falls.

The column constants, read from their classes:

| constant | meaning | value |
| --- | --- | --- |
| `PRG.Ol` | story-box columns | **28** |
| `PRG.Ob` | radio columns | **20** |
| `PRG.NY` | ending panel columns | 12 |
| `PRG.Om` | rows per page | 3 |

`PRG.amw.b(char)` only tests for a space (0x20) and `PRG.amw.a(char)` returns a
space unconditionally — the obfuscated wrapper's only notion of a break is the
ASCII space, which Chinese text does not contain.

Consequence: with hard cutting, *any* line whose length is not a multiple of the
column count gets cut somewhere, and the cut position is decided purely by the
character count. Rewording can only move the cut; it cannot remove it. That is
exactly why batch-24 kept trading one split for another. What rewording *can*
do is move the cut onto punctuation or a function word instead of through a
content word.
"""

COLS_STORY = 28
COLS_RADIO = 20
COLS_ENDING = 12
ROWS = 3


def hard_rows(text, cols):
    """Exactly what `PRG.aDI$a.p()` produces: fixed-size character slices."""
    if not text:
        return ['']
    return [text[i:i + cols] for i in range(0, len(text), cols)]


def story_rows(text):
    return hard_rows(text, COLS_STORY)


def radio_rows(text):
    return hard_rows(text, COLS_RADIO)


def ending_rows(text):
    return hard_rows(text, COLS_ENDING)


def boundaries(rows):
    """The character pairs that straddle a line break."""
    return [rows[i][-1] + rows[i + 1][0] for i in range(len(rows) - 1)
            if rows[i] and rows[i + 1]]
