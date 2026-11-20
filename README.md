# Open Loadout

> **Status:** v1 is in progress. No loadouts are ready yet.

Open Loadout is a free, open-source kit that gears up any AI with better instructions, skills, and workflows. It works with Claude, ChatGPT, Gemini, and others, in any app: desktop, web, or command line. Setup takes less than 5 minutes.

## Who it is for

People who use AI for everyday work and want better results without learning prompt tricks. No technical skills needed. If you like to tinker, every part can be changed.

## How it works

A **loadout** is a ready-made bundle for one type of task, such as writing, research, or planning. Each loadout is a plain text file with:

- instructions the AI follows
- example prompts to get started
- simple settings you can change to make it your own

Pick a loadout, copy it into your AI tool (or use the small adapter file for your tool), and start working.

## Planned structure

```
loadouts/    one folder per loadout
adapters/    small files that load a loadout into Claude, ChatGPT, Gemini, or a CLI
templates/   a template for making new loadouts
docs/        guides for users
tests/       before and after examples for each loadout
```

## Contributing

1. Copy `templates/loadout-template/` into `loadouts/` and fill it in.
2. Add a before and after example in `tests/`.
3. Open a pull request. Keep it short, plain, and model-neutral.

## License

MIT. See [LICENSE](LICENSE). Skills in `.claude/skills/` come from Anthropic and keep their own Apache 2.0 license.
