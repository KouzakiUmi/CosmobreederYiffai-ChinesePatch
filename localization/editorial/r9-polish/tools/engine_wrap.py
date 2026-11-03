"""The engine's real wrap rule, shared by every verifier.

The earlier tools used plain greedy wrapping (accumulate until 240px). That is
**not** what the engine does, and the difference produced real mistakes: rows
that looked clean at 240px greedy actually split a word once the engine applied
its boundary rules.

Two engines matter, and both refuse to open a line with punctuation:

* **story box** — `DialogueWrap.storyPages` → `DialogueGrid.formatCapped` →
  `PixelLayout.layout`, 12px story12 metrics, width 240, 3 rows per page.
  Boundary rules from `PixelLayout.legalBoundary` / `preferredBoundary`.
* **radio** — `DialogueWrap.pages` → `DialogueGrid.format` → `PixelLayout`, the
  same 12px metrics, width 150 (80 for the NY caller), 3 rows per page. It uses
  the **same** boundary rules as the story box. `ItemFont8` is the item-name
  field, not the radio body — do not use its `noStart` / `noEnd` here.

Both wrap the same way in spirit: fit as much as possible, then prefer a break
at a *legal* boundary, then a *preferred* one, and only fall back to a forced
break when neither exists. This module implements that once, so a verifier
cannot accidentally measure the wrong thing again.
"""
BUDGET_STORY = 240
BUDGET_RADIO = 150
ROWS_STORY = 3
ROWS_RADIO = 2

# `PixelLayout.legalBoundary`: a line may not end on an opening bracket, and a
# line may not start with any of these.
LEGAL_LEFT_FORBIDDEN = '（［｛〈《「『【〔〖〘〚‘“([{'
LEGAL_RIGHT_FORBIDDEN = '、。，．：；？！‼⁇⁈⁉）］｝〉》」』】〕〗〙〛’”)]},.!?:;%‰…⋯'
# `ItemFont8.noStart` / `noEnd` — item-name field only, NOT the radio body.
NO_START = '，。！？；：、）》】〕〉」』”’…,.!?;:%)]}'
NO_END = '（《【〔〈「『“‘([{$'


def _is_word(ch):
    return ch < '\x80' and (ch.isalnum() or ch in "'-")


def legal_boundary(left, right):
    """May a line break between these two characters? (engine `legalBoundary`)"""
    if not left or not right:
        return True
    if left in LEGAL_LEFT_FORBIDDEN or right in LEGAL_RIGHT_FORBIDDEN:
        return False
    return True


def preferred_boundary(left, right):
    """Is the break a *good* one? (engine `preferredBoundary`)"""
    if not left or not right:
        return True
    return not (_is_word(left) and _is_word(right))


def wrap(text, width_of, budget):
    """Wrap like the engine: fill, then prefer a legal+preferred boundary.

    `width_of` maps a character to its advance in pixels. Returns the drawn rows.
    """
    chars = list(text)
    rows = []
    at = 0
    total = len(chars)
    while at < total:
        used = 0
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
            # else: forced break — the engine records an issue and breaks at `fit`
        rows.append(''.join(chars[at:stop]))
        at = stop
    return rows or ['']


def radio_rows(text, width_of):
    """Radio pages: same PixelLayout rule as the story box, width 150."""
    return wrap(text, width_of, BUDGET_RADIO)


def story_rows(text, width_of):
    return wrap(text, width_of, BUDGET_STORY)


def boundaries(rows):
    return [rows[i][-1] + rows[i + 1][0] for i in range(len(rows) - 1)
            if rows[i] and rows[i + 1]]
