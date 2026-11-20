#!/usr/bin/env python3
"""Helper for the coderabbit-review skill. Two commands, no installs needed.

  python3 review_tools.py checks <base-ref> <head-ref>
      Runs this repo's house checks on the lines a pull request adds and prints
      the result as JSON: long dashes, passwords, keys, email addresses, and
      leftover merge markers. It does not judge the content.

  python3 review_tools.py report <data.json> <out.html>
      Fills assets/report-template.html with the report data and writes the
      finished page, ready to publish.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "report-template.html"

# Folders that hold third-party files we never edit, so house rules skip them.
# This skill is also skipped: it has to name the patterns it looks for.
SKIP_PREFIXES = (
    ".claude/skills/skill-creator/",
    ".claude/skills/doc-coauthoring/",
    ".claude/skills/product-brainstorming/",
    ".claude/skills/write-spec/",
    ".claude/skills/architecture/",
    ".claude/skills/code-review/",
    ".claude/skills/coderabbit-review/scripts/",
)

LONG_DASHES = (chr(0x2013), chr(0x2014))  # en dash, em dash
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    (
        "password or key written in the file",
        re.compile(
            r"(?i)\b(api[_-]?key|secret|passwd|password|token)\b\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"
        ),
    ),
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
]
ALLOWED_EMAILS = ("noreply@anthropic.com", "@users.noreply.github.com", "@example.com")


def git(*args):
    done = subprocess.run(
        ["git", "-c", "core.quotePath=false", *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",  # a binary file in the diff must not crash the check
    )
    if done.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {done.stderr.strip()}")
    return done.stdout


def added_lines(base, head):
    """Yield (file, line_number, text) for every line the pull request adds."""
    diff = git("diff", "--unified=0", "--no-color", "--no-ext-diff", "--no-renames", f"{base}...{head}")
    path, line_no, in_hunk = None, 0, False
    for raw in diff.splitlines():
        if raw.startswith("diff --git "):
            # A new file starts. Its header lines come before the first "@@".
            path, in_hunk = None, False
        elif not in_hunk and raw.startswith("+++ "):
            path = raw[6:].rstrip("\t") if raw.startswith("+++ b/") else None
        elif raw.startswith("@@"):
            match = re.search(r"\+(\d+)", raw)
            line_no = int(match.group(1)) if match else 0
            in_hunk = True
        elif in_hunk and raw.startswith("+"):
            if path and not path.startswith(SKIP_PREFIXES):
                yield path, line_no, raw[1:]
            line_no += 1


def run_checks(base, head):
    files = [f for f in git("diff", "--name-only", f"{base}...{head}").splitlines() if f]
    dashes, secrets, markers = [], [], []
    for path, line_no, text in added_lines(base, head):
        where = {"file": path, "line": line_no}
        if any(d in text for d in LONG_DASHES):
            dashes.append({**where, "text": text.strip()[:160]})
        if re.match(r"^(<{7} |={7}$|>{7} )", text):
            markers.append(where)
        for label, pattern in SECRET_PATTERNS:
            found = pattern.search(text)
            if not found:
                continue
            if label == "email address" and found.group(0).endswith(ALLOWED_EMAILS):
                continue
            # Never print the value itself, only where it is.
            secrets.append({**where, "kind": label})
    result = {
        "base": base,
        "head": head,
        "files_changed": files,
        "checks": [
            {
                "name": "No long dashes",
                "passed": not dashes,
                "detail": "Only hyphens are used in the changed lines."
                if not dashes
                else f"{len(dashes)} changed line(s) contain an em dash or en dash.",
                "items": dashes,
            },
            {
                "name": "No passwords, keys, or email addresses",
                "passed": not secrets,
                "detail": "Nothing that looks like a password, key, or email address was added. Other personal details, such as names and phone numbers, are not covered by this check."
                if not secrets
                else f"{len(secrets)} line(s) look like they may hold a password, key, or email address.",
                "items": secrets,
            },
            {
                "name": "No leftover merge markers",
                "passed": not markers,
                "detail": "No unfinished merge text was left in the files."
                if not markers
                else f"{len(markers)} line(s) contain unfinished merge text.",
                "items": markers,
            },
        ],
    }
    print(json.dumps(result, indent=2))


def build_report(data_path, out_path):
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    pr = data.get("pr", {})
    title = f"Open Loadout PR {pr.get('number', '')} Review".replace("  ", " ")
    # "</" is escaped so text inside the data can never close the script tag.
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("__REPORT_TITLE__", title).replace("__REPORT_DATA__", blob)
    Path(out_path).write_text(page, encoding="utf-8")
    print(f"Wrote {out_path} ({len(page)} characters)")


def main():
    args = sys.argv[1:]
    if len(args) == 3 and args[0] == "checks":
        run_checks(args[1], args[2])
    elif len(args) == 3 and args[0] == "report":
        build_report(args[1], args[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
