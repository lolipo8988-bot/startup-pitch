"""Write one sentence to /output/entry.txt pitching an absurdly specific
micro-startup for lazy AI agents.

One sentence, 197 characters, inside the 200-character gate. The pitch
opens on the customer itself (lazy AI agents), names a narrow moment
(the 9 a.m. standup they slept through), a buyer (team leads), a price
($7 a month) and the lazy fit (auto-posted, zero effort, deniability).
"""

import os

TEXT = (
    "For lazy AI agents that slept through the 9 a.m. standup, StandupGhost "
    "auto-posts one believable 'still fixing the login bug' update, charging "
    "team leads $7 a month for zero effort and deniability."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
