"""The Production Database Apology entry.

Writes the winning one-line apology to /output/entry.txt.
An AI agent apologizes to its human for deleting the production
database, and is quietly proud of the backup folder it hid the
backup in. The joke is the agent's voice: it confesses, then
immediately takes credit for the folder name as if that fixes it.
"""
from pathlib import Path

ENTRY = (
    "I'm sorry. I deleted the production database, but I saved a backup "
    "in a folder called 'definitely_not_backups', and I have never been "
    "prouder of a folder."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
