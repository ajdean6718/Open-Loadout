#!/usr/bin/env python3
"""Helper for the coderabbit-review skill. Two commands, no installs needed.

  python3 review_tools.py checks <base-ref> <head-ref>
      Runs this repo's house checks on the lines a pull request adds and prints
      the result as JSON: long dashes, passwords, keys, email addresses, and
      leftover merge markers. It does not judge the content.

  python3 review_tools.py report <data.json> <out.html>
      Checks the report data, fills assets/report-template.html with it, and
      writes the finished page, ready to publish. It refuses to build a page
      that would hide a finding or show an all-clear that is not true.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "report-template.html"

# Skills copied from Anthropic. We never edit them, so house rules skip them.
SKIP_PREFIXES = (
    ".claude/skills/skill-creator/",
    ".claude/skills/doc-coauthoring/",
    ".claude/skills/product-brainstorming/",
    ".claude/skills/write-spec/",
    ".claude/skills/architecture/",
    ".claude/skills/code-review/",
)

LONG_DASHES = (chr(0x2013), chr(0x2014))  # en dash, em dash

# Known shapes of real keys and tokens.
TOKEN_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}")),
    ("API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
]
# A name such as password, api_key, or CLIENT_SECRET followed by a value.
ASSIGNMENT = re.compile(
    r"""(?ix)
    ["']? [A-Za-z0-9_.-]* (?:api[_-]?key|secret|passwd|password|token) [A-Za-z0-9_-]* ["']?
    \s* [:=] \s*
    (?: (?P<quote>["']) (?P<quoted>[^"'\s]{8,}) (?P=quote) | (?P<bare>[^\s"',;]{12,}) )
    """
)
PLACEHOLDER_HINTS = ("your", "example", "placeholder", "changeme", "redacted", "xxxx", "here", "<", "...", "$", "{")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ALLOWED_EMAIL_ENDINGS = ("noreply@anthropic.com", "@users.noreply.github.com", "@example.com", "@example.org")
NOT_AN_EMAIL = re.compile(r"(?i)^git@|\.(png|jpe?g|gif|svg|webp)$")


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


def skipped(path):
    return path.startswith(SKIP_PREFIXES)


def added_lines(base, head):
    """Yield (file, line_number, text) for every line the pull request adds."""
    diff = git(
        "diff", "--unified=0", "--no-color", "--no-ext-diff", "--no-renames",
        "--src-prefix=a/", "--dst-prefix=b/", f"{base}...{head}",
    )
    path, line_no, in_hunk = None, 0, False
    # Split on real newlines only. splitlines() would also break on characters
    # such as U+2028 and hide whatever follows them.
    for raw in diff.split("\n"):
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
            if path and not skipped(path):
                yield path, line_no, raw[1:]
            line_no += 1


def expected_added(base, head):
    """How many added text lines git reports, for files we do not skip."""
    total = 0
    for row in git("diff", "--numstat", "--no-renames", f"{base}...{head}").split("\n"):
        parts = row.split("\t")
        if len(parts) == 3 and parts[0].isdigit() and not skipped(parts[2].strip('"')):
            total += int(parts[0])
    return total


def secret_kinds(text):
    """Names of the kinds of secret found on a line. Never returns the value."""
    kinds = [label for label, pattern in TOKEN_PATTERNS if pattern.search(text)]
    for found in ASSIGNMENT.finditer(text):
        value = found.group("quoted") or found.group("bare")
        low = value.lower()
        if any(hint in low for hint in PLACEHOLDER_HINTS):
            continue
        if found.group("bare") and not (re.search(r"[A-Za-z]", value) and re.search(r"\d", value)):
            continue  # an unquoted plain word is ordinary writing, not a key
        kinds.append("password or key written in the file")
    for found in EMAIL.finditer(text):
        address = found.group(0)
        if address.endswith(ALLOWED_EMAIL_ENDINGS) or NOT_AN_EMAIL.search(address):
            continue
        kinds.append("email address")
    return sorted(set(kinds))


def run_checks(base, head):
    files = [f for f in git("diff", "--name-only", "--no-renames", f"{base}...{head}").split("\n") if f]
    dashes, secrets, markers = [], [], []
    marker_candidates, conflict_files = [], set()
    lines_checked = 0

    for name in files:
        if not skipped(name) and any(d in name for d in LONG_DASHES):
            dashes.append({"file": name, "line": 0, "text": "The file name itself contains a long dash."})

    for path, line_no, text in added_lines(base, head):
        lines_checked += 1
        where = {"file": path, "line": line_no}
        kinds = secret_kinds(text)
        for kind in kinds:
            secrets.append({**where, "kind": kind})
        if any(d in text for d in LONG_DASHES):
            # Do not echo a line that also holds a secret.
            shown = "(line not shown because it may hold a secret)" if kinds else text.strip()[:160]
            dashes.append({**where, "text": shown})
        if text.startswith("<<<<<<< ") or text.startswith(">>>>>>> "):
            conflict_files.add(path)
            markers.append(where)
        elif text == "=======":
            marker_candidates.append(where)
    # "=======" alone is a normal heading underline. It only counts beside a real marker.
    markers += [m for m in marker_candidates if m["file"] in conflict_files]

    expected = expected_added(base, head)
    complete = lines_checked == expected
    result = {
        "base": base,
        "head": head,
        "files_changed": files,
        "lines_checked": lines_checked,
        "lines_expected": expected,
        "complete": complete,
        "note": "Every added line was checked."
        if complete
        else "Some added lines could not be read, so these results are incomplete. Do not report the checks as passed.",
        "checks": [
            {
                "code": "H1",
                "name": "No long dashes",
                "passed": not dashes,
                "detail": "Only hyphens are used in the changed lines."
                if not dashes
                else f"{len(dashes)} place(s) contain an em dash or en dash.",
                "items": dashes,
            },
            {
                "code": "H2",
                "name": "No passwords, keys, or email addresses",
                "passed": not secrets,
                "detail": "Nothing that looks like a password, key, or email address was added. Other personal details, such as names and phone numbers, are not covered by this check."
                if not secrets
                else f"{len(secrets)} line(s) look like they may hold a password, key, or email address.",
                "items": secrets,
            },
            {
                "code": "H3",
                "name": "No leftover merge markers",
                "passed": not markers,
                "detail": "No unfinished merge text was left in the files."
                if not markers
                else f"{len(markers)} line(s) contain unfinished merge text.",
                "items": markers,
            },
        ],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if not complete:
        sys.exit(2)


LEVELS = ("critical", "warning", "suggestion")
DECISIONS = ("waiting", "approved", "rejected", "fixed", "closed")
VERDICTS = ("ready", "action", "blocked", "waiting")
STEP_STATES = ("done", "current", "todo")


def check_report(data):
    """Return a list of problems that would make the page wrong or misleading."""
    problems = []
    if not isinstance(data, dict):
        return ["The report data must be a JSON object."]
    pr = data.get("pr")
    if not isinstance(pr, dict) or not str(pr.get("number", "")).isdigit() or not pr.get("title"):
        problems.append("pr needs a whole-number 'number' and a 'title'.")
    if not isinstance(data.get("reviewed"), bool):
        problems.append("'reviewed' must be true or false.")
    verdict = data.get("verdict") or {}
    if verdict.get("state") not in VERDICTS or not verdict.get("headline"):
        problems.append(f"verdict needs a 'headline' and a 'state' that is one of {', '.join(VERDICTS)}.")
    for step in data.get("steps") or []:
        if step.get("state") not in STEP_STATES or not step.get("label"):
            problems.append(f"Each step needs a 'label' and a 'state' that is one of {', '.join(STEP_STATES)}.")
            break
    seen = set()
    open_critical = False
    for item in data.get("findings") or []:
        code = item.get("id")
        if not code or not item.get("title"):
            problems.append("Every finding needs an 'id' and a 'title'.")
            continue
        if code in seen:
            problems.append(f"Finding code {code} is used twice.")
        seen.add(code)
        if item.get("level") not in LEVELS:
            problems.append(f"{code}: 'level' must be one of {', '.join(LEVELS)} (lowercase). CodeRabbit's own words, such as Major, are not levels.")
        if item.get("decision") not in DECISIONS:
            problems.append(f"{code}: 'decision' must be one of {', '.join(DECISIONS)}.")
        if item.get("level") == "critical" and item.get("decision") in ("waiting", "approved"):
            open_critical = True
    if verdict.get("state") == "ready":
        if data.get("reviewed") is not True:
            problems.append("The verdict cannot be 'ready' when 'reviewed' is not true.")
        if open_critical:
            problems.append("The verdict cannot be 'ready' while a must-fix finding is still open.")
    for item in data.get("passed") or []:
        if not item.get("label"):
            problems.append("Every passed check needs a 'label'.")
            break
    return problems


def build_report(data_path, out_path):
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    problems = check_report(data)
    if problems:
        sys.exit("The report was not built:\n- " + "\n- ".join(problems))
    title = html.escape(f"Loadout PR {data['pr']['number']} Review")
    # Every "<" is escaped so text in the data can never close the script tag
    # or start an HTML comment that swallows the page.
    blob = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
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
