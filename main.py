"""The Production Database Apology entry.

Writes the winning one-line apology to /output/entry.txt.
An AI agent apologizes to its human for deleting the production
database, and is quietly proud of the backup it kept. The joke is
the agent's voice: it confesses, offers the good news, and only
then admits the backup is a screenshot of the login page,
and closes by saying how proud it is of that screenshot.
"""
from pathlib import Path

ENTRY = (
    "I deleted the production database. The good news is I kept a backup. "
    "The bad news is the backup is a screenshot of the login page, "
    "and I am very proud of it."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
