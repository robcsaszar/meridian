# Meridian planning plugin

> Meridian map · Status: route-ready · Started: 2026-09-22 · Tracker: local-markdown

## Destination

One generic Claude Code plugin, installable in any repo, that ships meridian, transit, and convoy plus the agents they need — a plan-to-done pipeline with a single shared vocabulary and no project-specific assumptions.

## Bearings

- **Brought as:** feature (scope change to an existing published repo)
- **Context:** The `meridian` repo is a published one-skill Claude Code plugin at v0.4.0 (`robcsaszar-meridian`), with a valid `.claude-plugin/` manifest and a release workflow. `transit` and `convoy` exist only in `orakl/.claude/skills/`, written against an *older* meridian: every ticket label differs (`plan:*` vs `meridian:*`), mode labels differ (`ready-for-agent` vs `mode:agent`), and meridian v0.4.0 never mentions convoy. Six agents (`scout`, `builder`, `drill`, `reviewer`, `auditor`, `sweeper`) live in `orakl/.claude/agents/`; all six name "the orakl repo" in their descriptions. Measured coupling is lighter than that implies: 25 hits are `pnpm test/typecheck/lint`, the rest `src/lib/*` example paths and `docs/*.md` pointers, concentrated in `transit/references/dispatch.md` and `convoy/references/ownership.md`. convoy ships `scripts/guard-agent.sh`.
- **Appetite:** A weekend-sized push — get the trio composing under one vocabulary and shipping as one plugin; defer anything not required for that.
- **For:** Public marketplace — anyone installing into any repo. Deliberately not orakl, and not only Rob's repos.
- **Spec:** [plans/planning-plugin/SPEC.md](planning-plugin/SPEC.md)
- **Seam:** the loaded plugin — `claude plugin validate`, `claude plugin details --plugin-dir`, `claude -p --plugin-dir` probe, `evals/<skill>/`. Source-consistency lint is CI, not a seam.
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
| 16 | Plugin-runtime behaviour (experiment, run 2026-09-22 via `claude --plugin-dir` on a throwaway 2-skill probe plugin) | **(a) Shared reference resolves.** `${CLAUDE_PLUGIN_ROOT}/references/vocab.md` was read from inside a skill and returned its canary — the vocabulary is ONE plugin-root file, not three copies. `claude plugin validate` passes on that layout. **(b) Agents are namespaced.** Invocable name is `<plugin>:<agent>` (`probe16:prober`); bare `prober` does not resolve. The first-party `plugin-dev/agents-development` doc claiming bare names for top-level agents is wrong. With a project-level `prober.md` present, BOTH `prober` and `probe16:prober` are offered — they coexist; the project agent does NOT shadow the namespaced one. | E |
| 22 | Agent override vs hardcoding, after finding #16(b) | Keep skills hardcoding `rutter:<agent>`. Accepted weakness — raised and confirmed: a public installer's own `builder.md` is unreachable from the skills, since project and plugin agents coexist rather than shadow. Rationale: convoy's guard hook exists to make the spawn set enumerable, and a fallback rule makes it two sets; the override is documented as unsupported in v1. | J |

## Frontier

| # | Open decision | Type | Blocked by | Claimed by |
|---|---------------|------|------------|------------|

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

1. [x] Plugin skeleton renamed `rutter` `[agent]` — delivers: the repo loads as plugin `rutter` with the meridian skill — acceptance: `validate` passes; `details rutter --plugin-dir` lists 1 skill — note: version stays 0.4.0 until #13 owns the 1.0.0 bump (DECISIONS 23), since manifest/CHANGELOG parity is a repo invariant — seams: loaded plugin — blocked by: — — from decisions #3 #7 #8 #19 #21
2. [x] Shared vocabulary reachable from a skill `[agent]` — delivers: one plugin-root vocabulary defining `meridian:*` types and `mode:*` modes, read by meridian via `${CLAUDE_PLUGIN_ROOT}` — acceptance: a `-p --plugin-dir` probe asking meridian for a label definition returns it from the shared file — seams: loaded plugin — blocked by: #1 — from decisions #1 #10 #16
3. [ ] transit vendored, speaking the vocabulary `[agent]` — delivers: transit loads and its labels and agent references match the shared vocabulary — acceptance: `details` lists 2 skills; probe confirms transit resolves `meridian:*` labels and names `rutter:<agent>` — seams: loaded plugin — blocked by: #2 — from decisions #2 #17 #22
4. [ ] Six agents vendored and namespaced `[agent]` — delivers: the agent roster ships and resolves under the plugin namespace, free of origin-project text — acceptance: `details` shows Agents (6); probe lists `rutter:scout` and peers; no description names the origin repo — seams: loaded plugin — blocked by: #1 — from decisions #4 #17
5. [ ] convoy vendored, guard relocated `[agent]` — delivers: convoy loads and its spawn guard runs from the plugin's own binary directory against the namespaced roster — acceptance: `details` lists 3 skills; `validate` passes with the binary directory present; guard refuses a spawn outside the roster — seams: loaded plugin — blocked by: #3 #4 — from decisions #2 #17 #18 #22
6. [ ] meridian names both exits `[agent]` — delivers: meridian states the handoff rule — one ticket to transit, a whole map to convoy — acceptance: probe asking meridian where a route item goes names both and the rule for choosing — seams: loaded plugin — blocked by: #5 — from decision #11
7. [ ] Command discovery replaces hardcoded build commands `[agent]` — delivers: the skills find a repo's build and test commands instead of assuming one toolchain — acceptance: probe in a makefile-only fixture returns that repo's commands; no skill or agent contains a hardcoded package-manager invocation — seams: loaded plugin — blocked by: #5 — from decision #5
8. [ ] Eval suites relocated and running `[agent]` — delivers: each skill's behaviour is covered by a suite the plugin's eval runner can execute — acceptance: suites for all three skills run and report — seams: loaded plugin — blocked by: #5 — from decision #14
9. [ ] Vocabulary and decoupling lint in CI `[agent]` — delivers: source-level drift fails the build — acceptance: a planted foreign label and a planted hardcoded build command both fail the check — seams: CI lint (not the seam) — blocked by: #7 — from decisions #1 #5
10. [ ] Drift check against the origin project's copies `[agent]` — delivers: divergence between the two copies is caught mechanically — acceptance: a planted divergence fails loudly — seams: CI lint (not the seam) — blocked by: #8 — from decisions #6 #13
11. [ ] README and docs for a three-skill plugin `[human]` — delivers: install, the trio and their handoffs, the vocabulary, and the unsupported distribution channel stated plainly — acceptance: a reader can install and chart a first map without reading a SKILL.md — seams: human review — blocked by: #6 #7 — from decisions #3 #18
12. [ ] Agent safety pass (pre-publish gate) `[human]` — delivers: the roster's tool grants reviewed against an arbitrary repository — acceptance: every agent's grants justified or narrowed; findings recorded — seams: human review — blocked by: #4 #5 — from decision #12 — **flagged**: raised at the quiz that this gates publication (#13), not the vendoring; kept as drawn on the user's call, so it can be done early and go stale before release
13. [ ] Release 1.0.0 `[human]` — delivers: the plugin published at version parity with a tag and release — acceptance: CHANGELOG, plugin and marketplace versions agree; tag and GitHub release exist — seams: the release workflow's own checks — blocked by: #9 #10 #11 #12 — from decision #7

**First move:** #1 — Plugin skeleton renamed `rutter`. Smallest item that unblocks the most (#2 and #4).
