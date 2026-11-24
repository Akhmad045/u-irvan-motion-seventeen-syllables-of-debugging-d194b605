"""A haiku about debugging.

Writes one haiku, three lines in the 5-7-5 syllable shape, at most
200 characters, to /output/entry.txt and nothing else.
"""

import os

HAIKU = (
    "The midnight stack trace\n"
    "blames a line I never wrote\n"
    "someone else's code"
)


def main() -> None:
    lines = HAIKU.split("\n")
    if len(lines) != 3 or any(not line.strip() for line in lines):
        raise ValueError("haiku must be exactly three non-blank lines")
    if not 1 <= len(HAIKU) <= 200:
        raise ValueError("haiku must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")
    # Verify the written file round-trips exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written.decode("utf-8") != HAIKU + "\n":
        raise ValueError("written entry does not match the haiku")
    print(f"wrote {len(HAIKU)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
