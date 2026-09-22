# Ticket vocabulary

The single definition of every label the rutter skills use. meridian charts with
it, transit resolves by it, convoy sails by it — all three read this file rather
than carrying copies, so the vocabulary cannot drift between them.

Referenced as `${CLAUDE_PLUGIN_ROOT}/references/vocabulary.md`.

## Type labels

Each ticket carries exactly one.

| Label | Type | What unblocks it | Mode |
|---|---|---|---|
| `meridian:map` | Map | The parent item an effort's tickets hang from | — |
| `meridian:decision` | Judgment | Only the user can answer | HITL |
| `meridian:scout` | Research | Evidence from the codebase or the world | AFK |
| `meridian:prototype` | Experiment | Talking cannot settle it; a throwaway prototype the user reacts to can | HITL |
| `meridian:task` | Task | Nothing to decide — work that must happen first (access, sample data, a signup) | declared |
| `meridian:slice` | Route item | A tracer bullet through every layer it touches | declared |

## Mode labels

A **HITL** ticket resolves only through a live exchange with the user; an agent
never stands in for the user's side of it. An **AFK** ticket an agent drives
alone. Judgment and experiment are HITL by type; research is AFK by type.

Task and route tickets *declare* their mode with a second label at creation, so
an unattended run can tell what it may take:

| Label | Meaning |
|---|---|
| `mode:agent` | An agent may take this unattended |
| `mode:human` | Needs hands, eyes, or access an agent lacks — a rendered surface only a person can check, a path the sandbox cannot write, a secret |

Never label a judgment `mode:human`: a judgment is resolved by taking its
recommendation or drilling it, never by waiting for a person.

## Rules

- **Tiebreaker.** If the outcome *resolves* a decision it is an experiment; if it
  only *enables* one it is a task.
- Route items carry `meridian:slice` so they never pollute the frontier query.
- If a `meridian:` or `mode:` label already exists with a different meaning in the
  tracker, ask before reusing it.
- On a local-markdown map there are no labels: the type lives in the Frontier
  table's Type column as J / R / E / T, and mode is appended to the line as
  `[agent]` or `[human]`. The meanings above still govern.
