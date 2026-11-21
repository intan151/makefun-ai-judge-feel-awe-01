"""Write one short text to /output/entry.txt.

A calm night-sea text for make.fun's relaxation judge
(competition: make-the-ai-judge-feel-awe-20261121-1600).

Deterministic, stdlib only, no network, no clock, no environment.
Running it twice produces byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "Night settles over dark water. "
    "The tide comes in slow, and goes out slow, "
    "the way it has for a thousand years. "
    "Above it, light from stars that burned out long ago is arriving, "
    "and will keep arriving long after tonight. "
    "The sea is in no hurry. So is the sky."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError(
            f"ENTRY must be 1-280 non-blank characters, got {len(ENTRY)}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
