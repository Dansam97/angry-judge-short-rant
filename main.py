"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (343 characters) about the self-checkout machine
treating three apples like a security incident. Deterministic, no network,
no dependencies.
"""

import os

TEXT = (
    "I bought three apples. Three. The self-checkout has asked if I need "
    "assistance four times, flagged my fruit as a security threat, and "
    "summoned a human who is also confused. I came here specifically to "
    "avoid talking to people. Now a robot and a teenager are both staring "
    "at my apples like they committed a crime. Just let me pay for the apples."
)


def _validate(text):
    """Gate check: UTF-8 text of 1 to 400 characters, single line, not blank."""
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1-400 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main():
    _validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("written entry does not match the text")


if __name__ == "__main__":
    main()
