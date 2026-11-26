"""Roast the Smart Fridge: one line, best laugh wins.

The entry is a single roast line for the make.fun bounty. The program
writes that line to /output/entry.txt, where the sealed scorer reads it:
UTF-8 text, 1 to 160 characters, not only whitespace.
"""

import os

# The scorer reads this path. Overridable for local testing only; the
# graded run always writes /output/entry.txt.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

LINE = (
    "I asked my fridge for ice and it played a documentary about ice, "
    "so now I'm outsmarted by an appliance dumber than a light switch."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 160 characters, not only
    # whitespace, on a single line. Fail loudly instead of writing an
    # entry the scorer would reject.
    if not (1 <= len(LINE) <= 160):
        raise ValueError(f"line is {len(LINE)} characters, must be 1-160")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no blank edges")
    # Deterministic: the same bytes on every run, no trailing newline,
    # so the two graded runs match byte for byte.
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
