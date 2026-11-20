Open Loadout: project brief
Last updated: 2026-11-20. Owner: Anthony Dean. Repo: ajdean6718/Open-Loadout.
Status labels used below:

* DECIDED: Anthony has decided this.
* ACCEPTED: proposed in brainstorming and Anthony agreed.
* PROPOSED: suggested but not yet approved. Do not treat as final.
* OPEN: not yet decided or designed.

1. What this is
Open Loadout is an open-source repo that makes any major AI work much better for everyday and intermediate users, with almost no setup. It is the everyday-user counterpart to heavy developer kits like Everything Claude Code (ECC), which are built for serious AI developers. Open Loadout is for normal people who just want better results and do not want to learn prompting or tech.
It must work, to the extent each tool allows, with any major LLM (Claude, ChatGPT, Gemini, and others) in any place people use them: the web app, the desktop app, the mobile app, and the command line. It must be fully customizable by whoever downloads it. (DECIDED)
The name "Open Loadout" means: open source, and you equip ("load out") your AI with the right gear. (DECIDED)
Open Loadout is an installable kit (a plugin and repo). It is not a collection of prompts. The heart of it is a large library of skills and agents. The goal is that about 95 percent of regular AI users could use it as their only kit. It should also help with heavy work such as coding, without trying to beat kits made only for that. (DECIDED 2026-11-20)
2. The core promise
The user does not learn how to use AI better. The system does that for them and tailors it to them. Two sides of one idea:

* Input side: whatever the user types, the AI behaves as if a skilled prompt engineer wrote it.
* Output side: whatever the AI produces, the user can understand and act on without asking another AI to translate.

Everything in this repo should serve that promise. If a feature makes the user's life more complicated, it is wrong. (DECIDED)
3. Design principles (non-negotiable)

1. Invisible by default. Users never pick agents, route skills, or tune prompts. The system does it.
2. Almost no setup. End-user setup should take under 5 minutes, and the first useful thing should work faster than that.
3. Plain language everywhere. No jargon in anything user-facing.
4. Model-neutral core. All core content is plain markdown that works if pasted into any chat. Tool-specific files are thin adapters only.
5. Smallest thing that works. Do not add features, files, or folders that were not asked for. Every layer must be useful on its own.
6. Lean context. Always-on instructions must be tiny. Everything else loads only when needed, because bloat costs usage and can reduce quality.
7. Customization never breaks updates. Base content and user content live in separate places so updates never overwrite what the user made.
8. Honest about limits. Different tools support different features. Say so plainly instead of overpromising.

4. System overview
Intended flow of a request:
User message -> Prompt brain (Stage 1 clean up, Stage 2 clarify) -> Router -> Skill library and/or Agents and teams -> Reviewer -> Explainer -> Result to user.
Running underneath every step: Memory and the Usage saver. The Onboarding team builds personal agents that sit beside the base agents.
4.1 Prompt brain (DECIDED that it is needed. No longer built first, see section 7)
Anthony's reasoning: most people get bad outputs because they give bad inputs (overexplaining, underexplaining, contradicting, and more). The brain makes sure that no matter how well someone prompts, the AI treats it like a prompt engineer wrote it.
Stage 1: clean up. Takes the user's prompt and improves it before the AI works on it (this is what is commonly called prompt rewriting, enhancement, or optimization). It must preserve the user's real intent, fix contradictions and vagueness, and never invent requirements. Keep it light.
Stage 2: clarify. This is the harder and more important stage. Even after Stage 1, a prompt usually does not contain enough for the AI to do real work well. So the AI follows a framework to (1) truly understand what the user wants, (2) make sure that is clarified in a form it can use, and (3) make sure nothing is missing. It asks questions when needed. The AI, not the user, decides whether the prompt is good enough to work from. This applies to real work, not simple lookups or quick answers.
Proposed shape of the Stage 2 framework (PROPOSED, to be designed in depth):

1. Triage: quick answer or real work?
2. Understand the real goal, who it is for, what done looks like, and any constraints.
3. Find gaps and contradictions.
4. Ask only what cannot reasonably be assumed. State other assumptions plainly.
5. Restate the brief in one or two lines, then execute.

The gate matters: asking must be rare and cheap, or it breaks the "no complexity" principle. Ask only when the task is real work and a missing detail would materially change the result. Keep to a few questions, offer defaults, offer multiple choice where possible, and let the user say "just go."
Portability note: in the CLI, a hook can rewrite the prompt before the model reads it. In web, desktop, and mobile chat apps nothing sits in between, so the portable version is a standing instruction that makes the AI do both stages itself as its first step. In that version both stages become one behavior. Design for the portable version first; treat hooks as an optional upgrade. (ACCEPTED)
4.2 Router (ACCEPTED)
Reads the clarified brief and decides which skills and agents the job needs, and only those. Restraint rule: a simple task must never trigger a team. Agents add time, cost, and lost context, so they are used when work has distinct steps, parts that can run in parallel, or when a reviewer with fresh eyes is wanted.
4.3 Skill library and roadmap (DECIDED)
A large skill library that makes the user's AI better at actual work. Nobody wants to track dozens of skills, so the library has a roadmap with routing.

* Skills and the roadmap are organized in big sections, then sections within sections, and so on, so an AI never needs to read everything to find what it needs.
* The AI always ends up exactly where it needs to be, and only there: no more context than the task requires, but every relevant piece of information.
* When an agent reads a skill and gets stuck or needs more help, the skill gives an exact pinpoint to which skill and which section to go to for what it needs.
* The goal is that skills make agents machines at the work, not just good at it.
* The roadmap format and index structure are OPEN and need careful design.
* Size (DECIDED 2026-11-20): about 300 skills, grouped into about 20 sections with about 5 subsections each. The AI sees only the section list up front and opens skills one at a time.
* One section equals one loadout (DECIDED 2026-11-20). Each loadout folder holds that section's skills, agents, and teams.
* Quality bar (ACCEPTED): a skill only earns its place if it changes the result in a before-and-after test. It covers what the AI gets wrong by default.
* The full draft list of sections, skills, agents, and teams is in docs/LIBRARY_MAP.md. The list itself is PROPOSED until Anthony approves it.

4.4 Agents and teams (DECIDED)
Two kinds of profile:

* Agent profile: one specialist for a specific task or a specific step within a category of work.
* Team profile: a defined group of agents for a category, with the order, handoffs, and who reviews.

Why: if the user is not deliberately using subagents, they still get them by default when needed, and only the applicable ones.
Rules Anthony set:

* Cover all major categories of work (examples he gave: design, coding team, data team, marketing; he wants more than those).
* Maximum of 10 agents per category.
* About 100 agents in total (DECIDED 2026-11-20). Skills hold the knowledge, so hundreds are needed. Agents are roles in a workflow, so far fewer are needed.
* Cover all the major stuff in each category while keeping each agent's job narrow.
* Base agents are generally not something users need to customize.

Suggestions to build on (PROPOSED):

* Define agents by step in the work, not by job title.
* Every profile states what it handles and what it explicitly does not do, so neighbors do not overlap and routing stays clean.
* Keep each agent's routing description short, since routers choose by description.
* Category list (PROPOSED): the 21 sections in docs/LIBRARY_MAP.md. Writing and editing are one section. Prove the structure with one section first: Writing and editing (DECIDED 2026-11-20).
* Keep base agents and user agents in separate locations. Base agents live inside their loadout folder. The location for user agents is OPEN.
* Write profiles as portable plain markdown. Adapters turn them into real subagent files where the tool supports that. In chat apps without subagents, the model plays the roles in sequence.

Universal agents that apply across categories (ACCEPTED): a Reviewer (checks the work, ideally with fresh eyes that did not write it) and an Explainer (see 4.7). Every team ends with these two steps.
4.5 Onboarding team (DECIDED)
Customization comes from a team of agents whose job is to give the user more agents, specialized to them. It works two ways: it notices patterns over time and recommends an agent or team, or the user asks to make one on demand.
Suggested members (PROPOSED): Interviewer (learns the user in a few short questions, reusing Stage 2 skills), Pattern Spotter, Agent Designer, and Tester (runs the new agent on a sample task before saving it).
Constraints: first-run onboarding must be tiny or skippable. Pattern noticing needs a visible, user-owned, local log (plain text), and suggestions must be rare and low-key, not nagging.
4.6 Memory (DECIDED that it is needed)
Anthony wants memory in the system and does not want to build memory from scratch because good memory skills and repos already exist. Choose and adapt a proven existing approach. Memory is limited in apps and web chat, so the design must degrade gracefully: it should work for everyone to the extent each tool allows, with the most capability in the desktop app and CLI, which is where most users are likely to be. The specific memory approach is OPEN and needs research.
Memory feeds: Stage 2 (do not re-ask known things), the router (preferences), the Onboarding team (patterns), and the Explainer (what has already been explained).
4.7 Plain-language layer (ACCEPTED)
Anthony is non-technical and constantly has to ask other AIs to explain what Claude Code said. The average user must never need to do that. Pieces:

* Lead with the outcome: what happened, what it means for the user, what (if anything) they need to do, in everyday words. Technical detail goes underneath for anyone who wants it.
* Turn technical questions into choices: what each option means for the user, a recommendation, and why.
* Translate errors: what went wrong, whether it is serious, and what the AI is doing about it.
* Define a term once, the first time it appears, and remember it was explained.
* Auto-calibrate to the user's level instead of using a toggle. The user can always say "explain that" or "shorter."
* Confidence flags: a plain note when the AI is guessing versus sure, and what the answer rests on.
* Safety net for risky actions: before anything hard to undo (deleting, overwriting, sending, spending), say so in plain words and make it reversible when possible.
* Tradeoff to manage: explanations cost tokens and can annoy experts, so default to a few lines and calibrate.

4.8 Quality loop (ACCEPTED)

* Final Reviewer step before results are delivered.
* Feedback loop: when a user edits or rejects an output, log what was wrong so the same mistake is not repeated. Skills and agents should get better with the person; that is part of what makes the system personal.

4.9 Usage saver (DECIDED that it is needed, design OPEN)
Most people do not want to pay for big subscriptions, so token usage optimization is built in. Users must not have to set up routers or tools to get it. Anthony wants creative approaches here and will get to the details later. Ideas so far (PROPOSED): triage that skips clarification on quick asks, loading only the needed skill section, not spawning agents for simple tasks, short default replies, summarizing long chats and restarting, cheaper models for simple steps where the tool allows, and not re-reading the same material. Much of this falls out of the other pieces if they are designed lean.
4.10 Update path (ACCEPTED, design OPEN)
Users need a painless way to pull new versions of the skill library and base agents without losing their own agents, memory, and settings. Separate base and user locations are the starting point.
5. Portability and tiers (PROPOSED)
Be honest about what works where:

* Tier 1: paste-in instructions that work in any chat on any model.
* Tier 2: project or custom-instructions setup plus uploaded files, for apps that support it.
* Tier 3: full install for agentic tools (CLI and desktop) with real subagents, hooks, and memory files.

The README should state what users get at each tier. Anthony has acknowledged the reasons behind this but has not formally approved the tier model.
6. Other suggestions not yet approved (PROPOSED)

* First-win moment: show the same request answered with and without Open Loadout so users see the value immediately.
* Starting profiles (student, small business, job seeker, and so on) that switch on the right categories with one pick.
* Memory transparency commands such as "what do you remember about me" and "forget that," backed by a local plain-text file.
* A doctor command that detects the tool and tier, says what is working, and fixes what is not.
* A small before-and-after test set to prove outputs actually improve, especially to prove Stage 2 helps instead of annoying people.

7. Build order
DECIDED 2026-11-20: the skill library and the agents are built first. This replaces the earlier decision to build the prompt brain first. The prompt brain is still needed and comes later.
DECIDED 2026-11-20, the order of work:

1. Agree the full map by name: every section, skill, agent, and team (docs/LIBRARY_MAP.md).
2. Design the file format for skills, agents, teams, and the roadmap.
3. Build one section fully and test it with before-and-after examples. The first section is Writing and editing.
4. Fix the pattern based on what the tests show.
5. Fill in the remaining sections using the proven pattern.

PROPOSED order after that (Anthony will decide):

1. Prompt brain. The shared Reviewer and Explainer are built with the first section, since every team ends with them.
2. Memory, the feedback loop, and the Onboarding team.
3. Usage saver, doctor command, and update path.

Concern to keep in view: scope is large and the project promises simplicity to users while being complex underneath. Each layer must be independently useful, and the always-on part must stay tiny.
8. Current repo state

* Repo: ajdean6718/Open-Loadout, MIT license for the project.
* Folders: loadouts/ (the product, one folder per loadout, each holding one section's skills, agents, and teams), adapters/ (thin per-tool files for claude, chatgpt, gemini, cli), templates/ (loadout template), docs/, tests/, .claude/skills/.
* templates/loadout-template/loadout.md is the old loadout skeleton. It will be replaced when the file formats are designed.
* docs/LIBRARY_MAP.md is the draft map of every section, skill, agent, and team. No skills or agents are built yet.
* Installed build skills in .claude/skills/ (Apache 2.0, from Anthropic, copied unedited): skill-creator, doc-coauthoring, product-brainstorming, write-spec, architecture, code-review. They may contain em dashes; leave them unedited.
* CLAUDE.md contains the core rules, including: never commit or push directly to main; always work on a branch and open a pull request.
* Branch protection on GitHub is not enabled yet. Revisit when the repo goes public.
* The repo is currently private. Before making it public, check for secrets and personal or employer information.

9. How to work with Anthony

* He is not technical. Explain outcomes in plain language, define any necessary term once, and avoid jargon in your replies.
* He tends to overcomplicate requests and wants the best approach proposed rather than literal execution. If a request would make things more complex than needed, say so and propose the simpler route.
* When a decision is his to make, present it as a clear choice with a recommendation and the reason, not as a technical question.
* Hard rule across everything you write: no em dashes and no en dashes, anywhere. Use hyphens only. This applies to all files you create in this repo (installed third-party skills are the one exception, since they stay unedited).
* Plan first on anything non-trivial and wait for his approval before building. For prompts he writes, do not assume they are concise; he uses automatic prompt optimization.
* Brainstorming happens in a separate chat. This brief is the bridge. If something in the brief is labeled PROPOSED or OPEN, ask before treating it as final.

10. Rules for building

1. Read this brief and CLAUDE.md at the start of every session.
2. Work on a branch and open a pull request. Never push to main.
3. Use the installed skills where they apply (skill-creator for anything skill-related, doc-coauthoring for docs, architecture before structural decisions, code-review before merge).
4. Build the smallest thing that works. Propose before building.
5. Keep core content model-neutral plain markdown. Adapters stay thin.
6. Keep always-on instructions tiny and load detail only when needed.
7. Test improvements with before-and-after examples. If a loadout or agent does not clearly help, say so.
8. Commit in logical chunks and write clear pull request summaries in plain language.
9. Keep this brief current. When a decision changes, update it through a pull request.

11. Open questions

* Exact Stage 2 framework and the rule that gates when to ask questions.
* How personalization works in detail (Anthony will bring ideas later).
* Which existing memory approach to build on.
* File format for skills, agents, and teams, and the roadmap and index format, including how pinpoint references to a skill and section are written.
* Approval of the section list and the skill and agent names in docs/LIBRARY_MAP.md.
* Where user-made skills and agents live, separate from the base ones.
* How the kit is installed in each tool.
* Usage saver design.
* How updates work for users on each tier.
* Whether to adopt the tier model, the first-win demo, memory commands, and the doctor command.

12. Glossary

* Loadout: one section of the kit, such as Writing or Money. A ready-made bundle of skills, agents, and teams for one area of work or life.
* Section: the same thing as a loadout.
* Prompt brain: the two-stage system that cleans up and clarifies what the user asks.
* Router: decides which skills and agents a job needs.
* Skill: a reusable instruction set that makes the AI better at a type of work.
* Agent profile: a definition of one narrow specialist.
* Team profile: a defined group of agents with order and handoffs.
* Onboarding team: the agents that create personal agents for the user.
* Explainer: the universal agent that turns output into plain language.
* Reviewer: the universal agent that checks the work before delivery.
* Adapter: a thin tool-specific file that connects the plain-markdown core to one tool.
* ECC: Everything Claude Code, an existing kit for heavy AI coders that inspired this project.
