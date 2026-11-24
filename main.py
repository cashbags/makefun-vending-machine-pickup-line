#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Entry program: writes a single pickup line, spoken by a vending machine
to a passing human, to /output/entry.txt. Python 3.13, standard library
only. No clock, no randomness, no network: the same line every run.

The line
-------
    Check my coin return — I've been saving your change since Tuesday.
    Call it a down payment.

Ninety characters, ninety-two bytes in UTF-8 (the em dash is three
bytes). The gate allows 1 to 200 characters, so it passes with room.

Why this line was chosen (design reasoning)
--------------------------------------------
The brief ranks its five criteria in a fixed order, and the line was
built to satisfy them in that order rather than to be merely funny.

First, the speaker must be the machine itself. The line opens with a
direct command only a machine can give — "Check my coin return" — and
it is addressed to someone standing in front of it. No stranger in a
bar could say it, because no stranger has a coin return.

Second, it must live in the machine's own world. The coin return and
exact change are the machine's working parts, named in the brief
itself. Saving change is something only a machine that holds coins can
do; the line treats a mechanical habit as a romantic gesture.

Third, the laugh has to land on the last few words. "Call it a down
payment" reframes the saved change as the first instalment on a
relationship. The turn is the whole joke: the machine has been quietly
collecting the human's money and now declares what the collection was
for. Nothing after the punch explains it.

Fourth, it stays short and speakable: one breath, three short clauses,
no tacked-on tail. The em dash is a spoken pause, not decoration.

Fifth, it stays charming rather than creepy. Saving someone's change
could read as possessive, so the line keeps the tone playful and
transactional — a down payment is a cheerful, businesslike promise,
not a claim. The machine offers, it does not demand.

How the line was picked
------------------------
Ten candidate lines were written, each on a different lane of the
machine's world (hum and compressor, coin return, sold-out row, bill
acceptor, out-of-order sign, glass front, exact change kept, coin slot,
matchmaker snacks, best-before date), then judged pairwise against the
brief's five criteria in order, first differing criterion deciding.
The coin-return line won the round robin 9–0; the hum line was second
at 8–1 and is recorded as the fallback in CANDIDATES.md.

Lanes deliberately avoided: the live field at build time (32 entries)
already floods "Press B7" (four times), "you pressed all my buttons"
(twice), coils (twice) and the snack aisle (three times), and about half
the field hides its line behind a generic title. The coin return was
empty — the only visible exact-change entry takes the opposite angle
("One Thing I Can't Dispense", about inability, not saving).

Gate check
----------
Before writing, the program checks the line is UTF-8 text of 1 to 200
characters and not only whitespace, exactly the gate the sealed scorer
applies, and refuses to write anything that fails it.
"""

import os
import sys

LINE = (
    "Check my coin return \u2014 I've been saving your change "
    "since Tuesday. Call it a down payment."
)


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if the line is not valid UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline: the output is exactly the line
    print(f"wrote {path} ({len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
