# Open Loadout

> **Status:** v1 is in progress. No loadouts are ready yet. The planned contents are listed in [docs/LIBRARY_MAP.md](docs/LIBRARY_MAP.md).

Open Loadout is a free, open-source kit that gears up any AI with better instructions, skills, and workflows. It works with Claude, ChatGPT, Gemini, and others, in any app: desktop, web, or command line. Setup takes less than 5 minutes.

## Who it is for

People who use AI for everyday work and want better results without learning prompt tricks. No technical skills needed. If you like to tinker, every part can be changed.

## How it works

A **loadout** is a ready-made bundle for one area of work or life, such as writing, research, or money. Each loadout holds:

- **skills:** how-to guides the AI reads when it does a type of task
- **agents:** specialist workers that each do one step of the work
- **teams:** agents in a set order for bigger jobs

You do not pick any of these yourself. The AI opens only what the task needs. Everything is plain text, so you can change any part to make it your own.

How you install it in each AI tool is still being designed.

## Planned structure

```
loadouts/    one folder per loadout, holding its skills, agents, and teams
adapters/    small files that load a loadout into Claude, ChatGPT, Gemini, or a CLI
templates/   a template for making new loadouts
docs/        guides for users, plus the project brief and the library map
tests/       before and after examples for each loadout
```

## Contributing

The file formats are still being designed, so the steps below will change.

1. Check [docs/LIBRARY_MAP.md](docs/LIBRARY_MAP.md) to see where your idea fits.
2. Add a before and after example in `tests/`.
3. Open a pull request. Keep it short, plain, and model-neutral.

## License

MIT. See [LICENSE](LICENSE). Skills in `.claude/skills/` come from Anthropic and keep their own Apache 2.0 license.
