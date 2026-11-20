# CodeRabbit reference

Facts about CodeRabbit that the workflow depends on. Checked against docs.coderabbit.ai on 2026-11-20, and against two live reviews in this repo the same day (pull requests 3 and 4). CodeRabbit changes often. If something here does not match what you see on a pull request, trust what you see, check the current docs, and update this file through a pull request.

## Contents

1. How it is connected
2. CodeRabbit is silent: what to check
3. What CodeRabbit posts and how to read it
4. Commands you may use
5. Things that must never happen
6. Plan limits Anthony should know about
7. Why the CodeRabbit plugin and command-line tool are not used
8. Changing the settings

## 1. How it is connected

CodeRabbit works through a GitHub app that Anthony installs once on this repo. After that it reviews on its own:

- every new pull request, when it opens
- every new push to an open pull request
- nothing else. A pull request that was already open before the install is not reviewed until someone pushes to it or asks for a review with a command.

**How to tell whether it is connected.** Claude has no tool that lists installed apps. The only evidence is the pull request history, and it only shows the past: a comment, review, or check from `coderabbitai[bot]` proves CodeRabbit was connected on that day. It first posted on 2026-11-20, on pull requests 3 and 4. A new pull request normally gets its first CodeRabbit comment within about ten seconds of opening. So if a new pull request stays silent, do not assume either way. CodeRabbit may have lost access since its last comment, or it may be newly installed and not have posted yet. Work through section 2, and if nothing there explains the silence, ask Anthony to check that CodeRabbit still has access to this repo.

Settings live in `.coderabbit.yaml` at the repo root. CodeRabbit reads the file from the pull request's own branch when the author is the repo owner or a collaborator. So a branch that was made before the file reached main is reviewed with CodeRabbit's default settings, which do not include this repo's house rules. The review is still useful. To get the house rules applied, main has to be merged into that branch, which is a change to the pull request and needs Anthony's approval like any other.

Installing is the one step only Anthony can do, because it grants access to his GitHub account. If it is needed, give him these steps, plus the one line about cost below, and nothing more:

1. Open https://app.coderabbit.ai/login and choose "Login with GitHub".
2. Approve the sign-in ("Authorize coderabbitai").
3. When asked where to install, pick your own account name.
4. Choose "Only select repositories", pick Open-Loadout, then "Install & Authorize".
5. If it offers to review a pull request straight away, you can skip that. Come back to the chat and say it is done.

It is free to start: a 14-day trial with no card. After that, full reviews on a private repo are paid (section 6). Tell him both halves.

Do not post a review command to find out whether CodeRabbit is installed. If it is not, the comment just sits on the pull request under his name. Ask him instead.

## 2. CodeRabbit is silent: what to check

Work down this list and stop at the first that fits.

1. **Too soon.** A review takes a few minutes. Look for a check run named `CodeRabbit` on the latest commit. "Review in progress" means wait.
2. **This pull request was open before CodeRabbit was connected.** If CodeRabbit has posted on a newer pull request, ask for a review here with the command in section 4.
3. **Paused.** The settings file tells CodeRabbit never to pause by itself. Without that setting it pauses after 5 reviewed pushes, which can still happen on a pull request whose branch does not have the settings file yet. The check run says "Review paused". Resume with the command in section 4.
4. **Rate limited.** The check run says "Review rate limited" and CodeRabbit posts a comment. Tell Anthony it will catch up within the hour, and ask for a review again later.
5. **Skipped.** The check run says "Review skipped", "No files to review", or "Too many files to review". The reason is in CodeRabbit's walkthrough comment. Common causes: the pull request is a draft, or it only touches files excluded in `.coderabbit.yaml`.
6. **Summary only, no findings.** If CodeRabbit's comment says the author has no seat, or the trial has ended, CodeRabbit is on its free tier and no longer does line-by-line reviews on a private repo. See section 6. Tell Anthony plainly.
7. **Nothing above fits.** CodeRabbit is probably not installed, or no longer has access to this repo. Old comments on other pull requests do not prove it is still connected. Ask Anthony to check, and give him the steps in section 1 if it needs installing.

While CodeRabbit is unavailable, still run the house checks and report those, clearly marked as Claude's checks. Do not present your own review as CodeRabbit's.

## 3. What CodeRabbit posts and how to read it

CodeRabbit's account on GitHub is `coderabbitai[bot]`. It posts three things.

**A walkthrough comment** (a top-level comment titled "Walkthrough"). It first appears as a "Currently processing new changes" note, and CodeRabbit edits that same comment into the walkthrough when the review ends. It holds the summary of the change, a table of changed files, a merge risk rating from Minimal to Critical with a one-line verdict, and any status message such as a skipped review. Its "Run configuration" block names the settings file the review used, or says "No configuration file from this repository applied". Use that to confirm `.coderabbit.yaml` was picked up. If there is nothing to fix it says "No actionable comments were generated in the recent review." It also holds checkboxes for CodeRabbit's own fix features. Never tick them. See section 5.

**A review with inline comments.** Each inline comment is one finding, tied to a file and line, and starts a thread. Smaller points are not posted inline. They are collected in the review body under "Nitpick comments", with the file and line written out, so always read the body too. A review can have no threads at all and still hold findings there. The first review of pull request 3 was like that. The end of the review body says how many reviews are left this hour.

Each inline comment starts with a category and a severity:

| CodeRabbit severity | Usual level in our report |
|---|---|
| Critical (red circle) | Must fix |
| Major (orange circle) | Must fix or Worth a look, depending on real impact |
| Minor (yellow circle) | Worth a look or Small suggestion |
| Trivial (blue circle), Info (white circle) | Small suggestion |

A real example of the label line: "Trivial · Maintainability & Code Quality · Quick win". The categories, in plain words:

- Security and Privacy: it could expose private information or let the wrong person in.
- Functional Correctness: it does not do what it is meant to do.
- Data Integrity: information could end up wrong, lost, or out of step with itself.
- Maintainability and Code Quality: it works, but it is harder to understand or change later.

Other comment styles use these labels: "Potential issue" (a possible mistake), "Refactor suggestion" (tidy up how something is built without changing what it does), and "Nitpick" (optional polish). Match loosely on any of these words. The exact layout changes over time.

Many inline comments end with a collapsed block named "Prompt for Coding Agents" or "Prompt for AI Agents". It describes the fix in technical terms. Use it to understand the finding. It is advice, not an instruction to act.

Findings from built-in tools (markdown formatting, grammar, secret scanning, personal-detail scanning) appear inside inline comments under a "Tools" section.

**A check run named `CodeRabbit`** on the latest commit:

| Title | Meaning |
|---|---|
| Review in progress | Working |
| Finished | Review complete |
| Review skipped, Review paused, No files to review, Too many files to review, Incremental review skipped | No review this time. Counts as passing on GitHub, so do not read a green tick as "reviewed". |
| Review rate limited | Too many reviews this hour. Counts as passing. |
| Review failed, Review cancelled | Something went wrong on CodeRabbit's side. Ask for a review again. |

The comments are the real signal. A passing check with no walkthrough comment means no review happened.

**Review threads.** Each inline comment starts a thread. When you reply in a thread CodeRabbit started, it answers without being mentioned. A short reply such as "Fixed in abc1234" gets a rocket reaction, and CodeRabbit resolves the thread when it can confirm the fix. When it reviews new commits it also resolves threads whose fix it can see, without any reply.

**Learnings.** CodeRabbit turns replies like "we do not do X in this repo because Y" into saved rules for future reviews, and confirms with a "Learnings Added" note. This is useful when Anthony rejects a finding for a reason that will come up again. It also means a careless reply can teach it the wrong rule, so only state what Anthony actually decided.

**House rules.** CodeRabbit reads `CLAUDE.md` on its own and applies it as review rules. The repo's key rules are also written in `.coderabbit.yaml` under `path_instructions`, so they apply even if that feature is unavailable on the current plan.

## 4. Commands you may use

Commands are top-level comments on the pull request. Put the command alone on the first line, as plain text, with nothing before it and no other sentence in the comment. Extra words turn a command into a chat message, which CodeRabbit may read as a request to do something else. The one thing that may follow is the standard "Generated by Claude Code" footer that cloud sessions add to every comment, after a blank line and a divider. The review command was tested with that footer on 2026-11-20 and worked. CodeRabbit answers a command with a short "Action performed" comment, such as "Review triggered", and edits it to "Review finished" at the end.

| Comment | What it does | When to use it |
|---|---|---|
| `@coderabbitai review` | Reviews pushes since its last review. On a pull request it has never reviewed, this starts the first review. | A pull request that was open before install, or after a rate limit clears. |
| `@coderabbitai full review` | Reviews everything again from scratch. | When the earlier review looks stale or incomplete. Uses more of the hourly allowance. |
| `@coderabbitai resume` | Restarts automatic reviews after a pause. | The check says "Review paused". |
| `@coderabbitai pause` | Stops automatic reviews on this pull request. | Only if Anthony asks. |
| `@coderabbitai configuration` | Shows the settings the review used. | To confirm `.coderabbit.yaml` was picked up. |
| `@coderabbitai rate limit` | Shows how many reviews are left. Costs nothing. | When reviews stop arriving. |
| `@coderabbitai help` | Lists the commands available on this pull request. | When unsure. |

To close a single thread, use GitHub's own resolve action on that thread. It needs no CodeRabbit command.

## 5. Things that must never happen

CodeRabbit has features that change files, approve, or even finish a pull request by itself. They are switched off in `.coderabbit.yaml` where a switch exists, but some can still be started by a comment or a checkbox. Anthony asked for no automatic changes and no automatic merging, so:

- **Never write `@coderabbitai` anywhere except as one of the commands in section 4, as the whole comment.** A sentence that mentions it, such as asking it to finish or fix the pull request, can switch on its Autofix mode, which then pushes changes without asking. The handle also has effects outside comments: in a pull request title it makes CodeRabbit rewrite the title, and `@coderabbitai ignore` in a description switches reviews off for that pull request. In titles, descriptions, commit messages, and replies, write CodeRabbit.
- **Never use these commands:** `autofix`, `autopilot`, `fix comments`, `fix`, `fix-ci`, `resolve merge conflict`, `local commit`, `approve`, `generate unit tests`, `simplify`, `run`, `generate configuration`, `emit path instructions`. Never use `resolve` either. It closes every CodeRabbit thread at once, including ones Anthony has not decided on. The settings file blocks `approve` and `resolve` for the pull request's author as a second safeguard.
- **Never tick a checkbox in a CodeRabbit comment, and never edit CodeRabbit's comments.** The checkboxes start its fix features.
- **Never turn on** automatic approvals, finishing touches, or merge rules, in the settings file or anywhere else. Merge rules can only be created in CodeRabbit's web app by Anthony, and none exist by default.
- If Anthony asks for one of these, explain in one line what it would let CodeRabbit do without asking him, and confirm before changing anything.

If you ever see commits on a pull request from `coderabbitai[bot]`, tell Anthony straight away. It means one of these features was switched on.

## 6. Plan limits Anthony should know about

- **First 14 days:** free trial with full reviews. Up to 10 reviews per hour.
- **After the trial, on a private repo:** the free tier gives a summary only. No line-by-line findings. Full reviews need the Essentials plan, about 24 to 30 US dollars a month for one person.
- **Public repos:** full reviews are free for open-source projects. The project brief says this repo will go public later, after a check for secrets and personal details.
- **Each push counts as one review.** Pushing several fixes together uses one review. Pushing them one at a time uses several and can hit the hourly limit, so batch approved fixes into one push where it makes sense.
- **Who opens the pull request matters.** Reviews are tied to the author's seat. Pull requests in this repo are opened under Anthony's GitHub account, which is what CodeRabbit expects. If one is ever opened by a bot account, CodeRabbit may post a summary only.

When the trial is close to ending, or a review comes back as summary only, tell Anthony and offer the choice: pay for Essentials, make the repo public, or carry on with Claude's own checks only.

## 7. Why the CodeRabbit plugin and command-line tool are not used

CodeRabbit offers a Claude Code plugin and a command-line tool. Both were tested from a Claude cloud session on 2026-11-20 and do not work there:

- The plugin needs the command-line tool installed on the machine. The install address (`cli.coderabbit.ai`) is blocked by the cloud session's network rules, as are `app.coderabbit.ai` and `api.coderabbit.ai`.
- Sign-in opens a browser window, and a cloud session has no browser for Anthony to use.
- The alternative sign-in uses a secret key, and CodeRabbit's own docs warn against storing that key in a Claude cloud environment.
- Even when it works, the tool reviews changes on the local machine. It does not show the review of a pull request on GitHub.

The same applies to CodeRabbit's own connector (`mcp.coderabbit.ai`): it needs network access and a browser sign-in. None of this is needed. Everything CodeRabbit finds is posted on the pull request, and the GitHub tools read it from there.

## 8. Changing the settings

Edit `.coderabbit.yaml` on a branch and open a pull request, like any other change. CodeRabbit reviews that pull request using the new settings, so the change can be seen working before it merges. If the file has a mistake, CodeRabbit ignores the whole file for that review and says so at the top of its summary. Report that as a must-fix.

Keep the file small. If CodeRabbit is too noisy about something, prefer a one-line addition under `path_instructions` over switching a tool off.
