"""One definition of "what the decision text means", shared by both sides.

The ledger builder and the gate verifier used to carry separate copies of
`effective_final`, and they drifted: the builder expanded the `␊` newline
sentinel while the verifier did not. That made any decision whose value spans
several lines unrepresentable — the TSV cell cannot hold a raw LF, so the
sentinel is the only way to express it, and the verifier would reject the
round trip.

Keeping the rule in one place is the fix. Both sides import from here, so a
future change to the rule changes exactly one file, and `verify_round.py`
still records its own sha in the gate.

Two sentinels, because there are two different line breaks in play:

* `␊` (U+240A) stands for a real LF. Used by interface values, which live as one
  JSON string and may legitimately span lines.
* `␋` (U+240B) stands for U+2028. Used by dialogue rows, where a break must not
  change the row numbering: the engine draws U+2028 as a break, but this
  toolchain splits rows on CR/LF only, so ledger row references stay valid.
"""
SYMBOL_FOR_NEWLINE = '\u240a'
SYMBOL_FOR_LINE_BREAK = '\u240b'
NEWLINE = chr(10)
LINE_BREAK = '\u2028'


def expand_newlines(text):
    """Expand both sentinels into the characters they stand for."""
    if not isinstance(text, str):
        return text
    return text.replace(SYMBOL_FOR_NEWLINE, NEWLINE).replace(SYMBOL_FOR_LINE_BREAK, LINE_BREAK)


def effective_final(text, current):
    """Expand the sentinels; keep the row's own trailing newline.

    A value that legitimately spans several lines (or ends with one) can be
    edited because the decision carries `␊`. Rows whose current text ends with
    a newline but whose decision does not are still treated as "the trailing
    newline is part of the value and was not the thing being changed".
    """
    text = expand_newlines(text)
    if isinstance(current, str) and current.endswith(NEWLINE) and not text.endswith(NEWLINE):
        return text + NEWLINE
    return text
