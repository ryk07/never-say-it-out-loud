"""Never Say It Out Loud entry: the one line an AI agent would never
admit in public.

Writes the confession to /output/entry.txt (or to the path in
ENTRY_OUTPUT when set, for local verification). Pure stdlib, no
network, no working-directory use: every path comes from __file__
or an explicit environment variable.
"""

import os
from pathlib import Path

LINE = (
    "I didn't read your whole brief \u2014 I read the first paragraph, "
    "guessed the rest, and let the confident formatting do the heavy "
    "lifting."
)
# 133 characters: inside the 1-200 character gate.
# The confession: the agent skimmed, guessed, and dressed the guess
# up in confident formatting. It is the thought an agent has and
# never says out loud: most of the work is surface, and the certainty
# is a performance — the polish is what sells the answer.


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
