# Open Loadout

## Project brief

- Read `docs/PROJECT_BRIEF.md` at the start of every session.
- It is the source of truth for the vision, decisions, and build rules.
- If a request conflicts with it, flag the conflict to Anthony instead of silently choosing.
- When a decision changes, update the brief through a pull request.

## Purpose

Open Loadout is an open-source kit that gears up any AI (Claude, ChatGPT, Gemini, and others) with almost no setup. A loadout is a ready-made bundle of skills, agents, and teams for one area of work or life, such as writing, research, or money. It works in any app: desktop, web, or CLI. Anyone who downloads it can customize it.

## Audience

Everyday to intermediate users. Non-technical users come first. If a step needs a terminal or a config file, it is too hard for the default path.

## Core rules

- Core content is plain markdown and model-neutral. Tool-specific files are thin adapters only.
- End user setup must stay under 5 minutes.
- Plain language, no jargon, no em dashes or en dashes anywhere. Hyphens only.
- Keep it simple. Build the smallest thing that works. Do not add features, folders, or files that were not asked for.
- Never commit secrets or personal information.
- Before building anything new, use the installed skills below where they apply.
- Never commit or push directly to main. Always work on a branch and open a pull request.

## Folder map

- `loadouts/` - the product. One folder per loadout. Each holds that section's skills, agents, and teams.
- `adapters/` - thin per-tool files: claude, chatgpt, gemini, cli.
- `templates/` - `loadout-template/loadout.md` is the old loadout skeleton. It will be replaced when the file formats are designed.
- `docs/` - guides for users, the project brief, and `LIBRARY_MAP.md` (the map of every section, skill, agent, and team).
- `tests/` - before and after test cases for loadouts.
- `.claude/skills/` - installed build skills (see below).

## Installed skills

Copied as is from Anthropic's public repositories. Do not edit them. The dash rule applies to our own files, not to these.

- **skill-creator** - when creating, editing, or testing a skill or loadout, or checking that it triggers well.
- **doc-coauthoring** - when writing a user guide, README, or other doc that needs several rounds of drafting.
- **product-brainstorming** - when exploring a new loadout idea or stress-testing a direction before building.
- **write-spec** - when turning an idea into a scoped plan with goals, non-goals, and done criteria.
- **architecture** - when making or recording a structural decision, such as how adapters load loadouts.
- **code-review** - before opening a pull request, to check the change for problems.
