"""The wrap rule that the shipped candidate actually uses.

Established by disassembling **the candidate jar**, not the original one. The
distinction matters: `PRG/Nb` and `PRG/JR` in `candidate54` carry a
`DialogueWrap.story` / `DialogueWrap.radio` call that the original jar does not
have (`javap` on the original reports zero `DialogueWrap` references; the
candidate reports the Methodref and the `invokestatic`). So Chinese dialogue in
the shipped build goes through `DialogueWrap`, **not** the original `PRG/amw`.

What `DialogueWrap` does:

* **story box** — `story` → `storyPages` → `DialogueGrid.formatCapped` →
  `PixelLayout.layout`, 12px story12 metrics, width **240**, 3 rows per page.
* **radio** — `radio` → `pages` → `DialogueGrid.format` → `PixelLayout.layout`,
  bbc2 metrics (10px per Han glyph), width **150**, 3 rows per page.
* **ending panel** — width 80, 12 columns.

Both call into `PixelLayout`, so both obey the same boundary rules, read from
`PixelLayout.legalBoundary` / `preferredBoundary`:

* a line may not end on an opening bracket and may not **start** with
  punctuation (`，。！？…` etc.);
* a break between two Latin word characters is not *preferred*;
* `wrap()` fills as far as it can, then prefers a preferred boundary, then a
  legal one, and only forces a break when neither exists.

The original `PRG/amw` — which the earlier versions of this file modelled — is
fixed-column hard cutting (28 characters for the story box, 20 for radio). That
is what the *unpatched* game does. Measuring against it would validate text that
never reaches the player.
"""

BUDGET_STORY = 240.0
BUDGET_RADIO = 150.0
ROWS_STORY = 3
ROWS_RADIO = 3

# `PixelLayout.legalBoundary`
LEGAL_LEFT_FORBIDDEN = '（［｛〈《「『【〔〖〘〚‘“([{'
LEGAL_RIGHT_FORBIDDEN = '、。，．：；？！‼⁇⁈⁉）］｝〉》」』】〕〗〙〛’”)]},.!?:;%‰…⋯'


def _is_word(ch):
    return ch < '\x80' and (ch.isalnum() or ch in "'-")


def legal_boundary(left, right):
    if not left or not right:
        return True
    return not (left in LEGAL_LEFT_FORBIDDEN or right in LEGAL_RIGHT_FORBIDDEN)


def preferred_boundary(left, right):
    if not left or not right:
        return True
    return not (_is_word(left) and _is_word(right))


def wrap(text, width_of, budget):
    """Fill, then prefer a preferred boundary, then a legal one."""
    chars = list(text)
    rows = []
    at = 0
    total = len(chars)
    while at < total:
        used = 0.0
        fit = at
        preferred = -1
        legal = -1
        while fit < total:
            advance = width_of(chars[fit])
            if used + advance > budget and fit > at:
                break
            used += advance
            fit += 1
            if fit == total or legal_boundary(chars[fit - 1], chars[fit]):
                legal = fit
                if fit == total or preferred_boundary(chars[fit - 1], chars[fit]):
                    preferred = fit
            if used + advance > budget and fit > at:
                break
        stop = fit
        if fit < total:
            if preferred > at:
                stop = preferred
            elif legal > at:
                stop = legal
        rows.append(''.join(chars[at:stop]))
        at = stop
    return rows or ['']


def story_rows(text, width_of):
    return wrap(text, width_of, BUDGET_STORY)


def radio_rows(text, width_of):
    return wrap(text, width_of, BUDGET_RADIO)


def boundaries(rows):
    return [rows[i][-1] + rows[i + 1][0] for i in range(len(rows) - 1)
            if rows[i] and rows[i + 1]]
