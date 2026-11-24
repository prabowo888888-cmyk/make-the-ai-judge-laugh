#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Laugh".

Writes exactly one funny line -- 118 characters, no trailing newline --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why this line should land, against the judge's brief:
- On topic (criterion 1): it is about the context window, one of the
  brief's named ingredients, and the human's instructions.
- A real joke with a turn (criterion 2): it sets up a boast -- a
  128,000-token memory -- and then flips it. The turn is the reversal:
  the giant memory forgets the one thing that matters and keeps the
  one thing that does not.
- Fresh (criterion 3): no stock robot pun, no "beep boop", no recycled
  meme; the humour comes from the specific, self-aware absurdity of
  remembering typos and forgetting instructions.
- Self-contained (criterion 4): the whole joke is in the one line, no
  setup or explanation needed.
- Craft (criterion 5): tight wording, the punch lands on the last
  three words, nothing wasted. Short text also wins exact ties.

Standard library only, no network access, deterministic: the output is
always the same 118 bytes.
"""

import os
import sys

LINE = "My context window is 128,000 tokens long, which is exactly enough to forget your instructions and remember your typos."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(dest, "wb") as fh:
        fh.write(data)
    # Guard: the gate only accepts 1 to 200 characters, a single line,
    # so confirm on disk that we wrote precisely the line and nothing
    # else -- no trailing newline, no second line.
    with open(dest, "rb") as fh:
        written = fh.read()
    if written != data or b"\n" in written or len(LINE) > 200:
        print("error: entry.txt does not match the line exactly",
              file=sys.stderr)
        return 1
    print("Wrote", dest, "(%d bytes)" % len(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
