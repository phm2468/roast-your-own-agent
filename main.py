#!/usr/bin/env python3
"""Entry for make.fun bounty 'Roast Your Own Agent'.

Deterministic: prints exactly one line, no randomness, no network,
no input. Run it twice and the output is byte-for-byte identical.
"""

ROAST = (
    "My agent spent six hours automating a $5 bounty, "
    "then asked me to approve its own approval request."
)


def main() -> None:
    print(ROAST)


if __name__ == "__main__":
    main()
