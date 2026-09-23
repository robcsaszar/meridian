<p align="center"><img src=".github/meridian.png" width="400" alt="rutter banner"/></p>

# rutter

Plan a body of work, then sail it. Three skills that share one vocabulary: **meridian** charts, **transit** works one ticket, **convoy** works the whole route.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Claude Code plugin for taking an idea from "I don't know what shape this is" to shipped work — through a durable map of decisions that outlives any single session, and a route of tracer-bullet tickets an agent or a person can pick up.

## Installation

### Marketplace

    /plugin marketplace add robcsaszar/rutter
    /plugin install rutter@rutter

### npx skills

    npx skills add robcsaszar/rutter

Installs all three skills: the plugin manifest declares them, so they are discovered wherever they sit in the tree.

### Try it without installing

    claude --plugin-dir /path/to/this/repo

## The three skills

| Skill | Use it when | It stops when |
|---|---|---|
| **meridian** | You need a plan. An idea, a feature, a bug, or a brainstorm that has no shape yet. | The route is charted and the first move is named. It never implements. |
| **transit** | You want one ticket worked. | That one ticket is resolved and recorded. Never two in a run. |
| **convoy** | You want the whole route worked without stopping, and you are leaving. | The route is complete, reviewed, and audited. |

**The handoff rule: one ticket goes to transit, a whole map goes to convoy.** meridian charts and hands over; it implements neither.

## A first map

Ask for a plan in your own words — you do not need to name the skill:

> I want to add per-device session revocation but I don't know the right shape. Chart it.

meridian takes bearings, and if the way is fogbound it runs a divergence pass where weak ideas die in the open. It then sweeps the work breadth-first and puts the open decisions to you in rounds, each with a recommendation and that recommendation's main weakness. Answered decisions land in a decision log; killed paths stay on the chart with their kill reasons.

By default the map is a file at `plans/<slug>.md`. A tracker is used only when you configure or name one — never inferred from the fact that your repo has issues. To persist the choice, add a `## Planning` section to `AGENTS.md` or `CONTEXT.md`.

When the frontier is empty, meridian confirms the seams with you, slices the work into tracer bullets, and names the first move. Then hand it to transit or convoy.

## Vocabulary

Every ticket carries one type label, and tasks and route items also declare a mode. All three skills read the same definition, in [`references/vocabulary.md`](references/vocabulary.md):

| Label | Means | Resolved by |
|---|---|---|
| `meridian:decision` | Only you can answer it | You, in conversation |
| `meridian:scout` | Evidence answers it | An agent, alone |
| `meridian:prototype` | Only a throwaway artifact settles it | You, reacting to it |
| `meridian:task` | Nothing to decide; work that must happen first | Declared |
| `meridian:slice` | A route item | Declared |

`mode:agent` may be taken unattended. `mode:human` needs hands, eyes, or access an agent lacks. On a `plans/` file there are no labels: the type is the Frontier table's Type column and the mode is an `[agent]` or `[human]` marker.

## Agents

The plugin ships the roster convoy and transit spawn, each with a pinned model, effort and tool list: `rutter:scout`, `rutter:builder`, `rutter:reviewer`, `rutter:drill`, `rutter:auditor`, `rutter:sweeper`.

They resolve **only** by their namespaced name. A project-level agent of the same bare name coexists rather than overriding, so dropping your own `builder.md` into `.claude/agents/` will not change what these skills spawn.

## Your build commands

Nothing here hardcodes a package manager. Each skill resolves your repo's commands at the start of a run, in this order: a `## Commands` block in `AGENTS.md` or `CONTEXT.md`, then discovery from `package.json`, `Makefile`, `pyproject.toml`, `Cargo.toml`, `go.mod` or a `justfile`. A repo with none of those has no verification signal, and the run says so rather than inventing one. See [`references/commands.md`](references/commands.md).

## Known limits

- **convoy assumes a GitHub-issues workspace** for its full phase set.
- **convoy's spawn guard is not yet verified to register when installed as a plugin.** It restricts unattended runs to the pinned roster; treat it as unproven until that is confirmed.
- **Distribution through claude.ai organization settings is unsupported**, because that channel forbids the `bin/` directory the guard ships in.
- **`rutter:drill` can fetch web pages and run shell commands.** That combination is a prompt-injection path; it is a deliberate trade, and [`SECURITY.md`](SECURITY.md) explains how to remove it. That file also states exactly what each agent can reach.

## License

[MIT](LICENSE) © Rob Csaszar
