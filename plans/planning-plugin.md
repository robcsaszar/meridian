# Meridian planning plugin

> Meridian map · Status: charting · Started: 2026-09-22 · Tracker: local-markdown

## Destination

One generic Claude Code plugin, installable in any repo, that ships meridian, transit, and convoy plus the agents they need — a plan-to-done pipeline with a single shared vocabulary and no project-specific assumptions.

## Bearings

- **Brought as:** feature (scope change to an existing published repo)
- **Context:** The `meridian` repo is a published one-skill Claude Code plugin at v0.4.0 (`robcsaszar-meridian`), with a valid `.claude-plugin/` manifest and a release workflow. `transit` and `convoy` exist only in `orakl/.claude/skills/`, written against an *older* meridian: every ticket label differs (`plan:*` vs `meridian:*`), mode labels differ (`ready-for-agent` vs `mode:agent`), and meridian v0.4.0 never mentions convoy. Six agents (`scout`, `builder`, `drill`, `reviewer`, `auditor`, `sweeper`) live in `orakl/.claude/agents/`; all six name "the orakl repo" in their descriptions. Measured coupling is lighter than that implies: 25 hits are `pnpm test/typecheck/lint`, the rest `src/lib/*` example paths and `docs/*.md` pointers, concentrated in `transit/references/dispatch.md` and `convoy/references/ownership.md`. convoy ships `scripts/guard-agent.sh`.
- **Appetite:** A weekend-sized push — get the trio composing under one vocabulary and shipping as one plugin; defer anything not required for that.
- **For:** Public marketplace — anyone installing into any repo. Deliberately not orakl, and not only Rob's repos.
- **Consult:** none
- **Preferences:** none recorded yet

## Decision log

| # | Decision | Resolution | Via |
|---|----------|------------|-----|
| 1 | Which label vocabulary wins | `meridian:*` prefix for type labels — transit/convoy's set, not meridian v0.4.0's `plan:*`. No migration of orakl's live maps. | J |
| 2 | Does convoy ship in v1 | Yes — all three skills ship together. | J |
| 3 | Repo identity | Keep the repo and URL `github.com/robcsaszar/meridian`. | J |
| 4 | Do the six agents ship in the plugin | Yes — ship agents; all six, not a transit-only subset. | J |
| 5 | How agents learn a repo's commands | `## Commands` block in AGENTS.md/CONTEXT.md, falling back to discovery from `package.json` / `Makefile` / `pyproject.toml`. | J |
| 6 | Canonical source after the re-scope | Keep them separate — orakl retains its copies; the plugin does not become orakl's source. | J |
| 7 | Version for the re-scope | `1.0.0`. | J |
| 8 | Plugin layout for 3 skills + 6 agents | `skills/<name>/SKILL.md` + `agents/<name>.md` at plugin root; multiple of each explicitly supported, no documented cap. Repo already matches. Cited: code.claude.com/docs/en/plugins.md. | R |
| 9 | Does the weekend appetite hold | Yes — re-aimed at vocabulary unification + plugin skeleton; de-coupling is follow-on work. | J |
| 10 | Mode-label vocabulary | `mode:agent` / `mode:human`. | J |
| 11 | Who meridian hands off to | Both, with the rule stated: one ticket → transit, whole map → convoy. | J |
| 12 | Agent safety pass | A pre-publish gate, not weekend work. Publish nothing until it passes. | J |
| 13 | Anti-divergence for the two copies | One named direction of travel plus a drift check that fails loudly. | J |
| 14 | Do evals ship | Yes — at top-level `evals/<skill>/`, settling the repo-wide placement split. | J |
| 15 | Approach to the shared-vocabulary question | Run the `${CLAUDE_PLUGIN_ROOT}` experiment first (ticket #16); duplicate only if it fails. | J |
| 19 | Plugin name | `rutter` — a mariner's book of sailing directions carried voyage to voyage; matches the single-evocative-noun house style and becomes the agent prefix (`rutter:scout`). Repo and URL unchanged per #3. | J |
| 17 | Agent resolution | Namespaced `rutter:<agent>` everywhere. Accepted weakness: walks past a user's project-level override; whether a project agent can shadow a namespaced reference is untested and folded into #16. | J |
| 18 | convoy's guard hook | Move the script to `bin/` (auto-PATH); declare claude.ai org-settings distribution unsupported in v1 and state it in the README. Accepted weakness — raised and confirmed: an org-settings install would get convoy with its guard silently absent, which sits in tension with #12's "safety is a pre-publish gate". The safer alternative (convoy refuses to start when the guard is unreachable) was weighed and not taken. | J |
| 20 | Is `rutter` free as a plugin/marketplace name | **Contested.** npm `rutter` taken and live (v1.4.0, 2026-05-24, ~121 dl/mo, npmjs.com/package/rutter). GitHub org `rutter` = Rutter Inc. (rutter.com), YC/a16z, $27M Series A, "universal API for business financial software" — a developer-API company, same category. No `rutter` plugin found in public marketplaces (not-prominent: solid; nothing-anywhere: UNVERIFIED). Trademark status UNVERIFIED (USPTO unreachable); active commercial use implies common-law rights. Bare "rutter" is SEO-buried; "rutter claude code plugin" is clean. | R |
| 21 | Plugin name, reconsidered against finding #20 | Keep `rutter`. Accepted weakness — raised and confirmed: shares a name with Rutter Inc., a funded developer-API company in the same category; bare-term search is unwinnable; npm `rutter` is closed if the plugin ever needs a package. Judged reputational, not technical: plugin marketplaces are a separate namespace and no `rutter` plugin exists. | J |

## Frontier

| # | Open decision | Type | Blocked by | Claimed by |
|---|---------------|------|------------|------------|
| 16 | Plugin-runtime behaviour, one throwaway plugin answers both: (a) does `${CLAUDE_PLUGIN_ROOT}/references/<shared>.md` resolve from inside a skill, or must the vocabulary be duplicated per skill; (b) can a project-level `.claude/agents/builder.md` shadow a namespaced `rutter:builder` reference? | E | — | |

## Fog

- Whether the `ai-forge-judge` 1024-char description rule (shipped into the skills monorepo this session) is simply wrong — scout cites 1,536 in skills.md. Clarifies when: the limit is checked against the docs directly.

- Whether convoy's parallel-subagent orchestration is safe to hand strangers at all, versus staying a private power tool — clarifies when: the agent safety pass (#12) reports what a `builder`/`sweeper` can reach in an arbitrary repo.

## Ruled out

- `admiralty` — killed because: the strongest semantic fit (charts + orders + fleet), but "admiralty law" owns the search space and the military register sat wrong.
- `chartroom` — killed because: names a place, so it holds the map but not the fleet; compound style is reserved for grab-bags.
- `passage` — killed because: collides with `prose` ("a passage" of text) and names the part (a crossing) rather than the whole.
- `pilot` / `pilotage` — killed because: "Copilot" and "pilot program" make the word unusable in this space.
- `lodestar` — killed because: pure direction; duplicates meridian's own metaphor and contains no execution.
- `squadron` — killed because: all fleet, no charting; drops a third of the package.
- `almanac` — killed because: a static reference table; no agency, and these skills act.
- `compass` / `sextant` — killed because: single instruments; the package is not one instrument.
- `fleet` — killed because: accurate but flat; reads as infrastructure tooling rather than a method.

## Route

**First move:** [not yet charted]
