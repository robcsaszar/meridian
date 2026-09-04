# Changelog

All notable changes to this project are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [0.4.0] - 2026-09-04

### Added

- Ticket **mode**: judgment and experiment are HITL by type, research AFK by type; task and route tickets declare theirs with a second label, `ready-for-agent` or `ready-for-human`, so an unattended run can tell what it may take. Tracker references create the two mode labels and carry the convention (local markdown uses `[agent]` / `[human]` markers).
- Phase 3 runs the breadth-first sweep as grilling-style **rounds** (numbered candidates, recommended answer with its weakness, one round per frontier); an answered candidate goes straight to the Decision log instead of becoming a ticket. Terms are sharpened into `CONTEXT.md` as they land; ADRs only when hard to reverse, surprising, and a real trade-off.
- Phase 4 becomes spec → seams → tracer-bullet slices → quiz → publish, with the spec shape, slicing rules (prefactor first, expand → migrate → contract for wide refactors), and route item body in `references/route.md`. Route items carry Parent / What to build / Acceptance criteria / Blocked by / Seams / From decisions.
- Bearings gains **Consult** (skills every session loads) and **Preferences**.
- Resume handles deferred-only frontiers, stale `plans/` maps on a tracker workspace, and new scope brought to a live map.

### Changed

- The **work session** (formerly Phase 3b) moves to the companion skill **transit**, which claims one ticket, resolves it by label, records and ripples. Meridian charts and routes; it never resolves a non-research ticket. Description, Sessions, and NEVER rules updated to match.
- Research findings are recorded per the tracker doc's Resolve and close; a finding that implies a decision becomes a judgment ticket, never a decision.
- Phase 2 degraded mode: a missing divergence reference ends the session with the fog symptom recorded instead of running a condensed table inline.
- Map sections and Phase 4 steps defer to the template and `references/route.md` rather than restating them.

### Removed

- The inline degraded-mode divergence table.
- The `Execution` Bearings field (nothing consumed it).

## [0.3.0] - 2026-09-01

### Added

- Workspace resolution ladder: persisted `## Planning` section in `CONTEXT.md` (else `AGENTS.md`) → user-named tracker → inference from repo signals (`.github/ISSUE_TEMPLATE/`, open issues on the GitHub remote, Jira keys in commits, existing `plans/`) → local markdown. Rungs after the persisted one confirm before the first write and offer to persist the choice so later sessions skip the step.
- Per-tracker operation references under `references/trackers/` — `github-issues.md`, `jira.md`, `local-markdown.md` — each covering the same seven operations (create map, create ticket, wire blocking, claim, frontier query, resolve and close, graduate fog) so SKILL.md stays tracker-agnostic.
- Label scheme `plan:map`, `plan:judgment`, `plan:research`, `plan:experiment`, `plan:task`, `plan:route`, with an ask-before-reusing guard for pre-existing `plan:` labels.
- Fourth ticket type, **task**, for work that must happen before a decision is possible; tiebreaker against experiment (resolves a decision vs. enables one).
- Claim convention (assignee) and native blocking relations so the frontier is visible in the tracker's own UI. The GitHub issue-dependencies endpoint (`issues/<n>/dependencies/blocked_by`) could not be exercised from the release session, so `github-issues.md` keeps the `Blocked by:` body-line fallback documented alongside it for plans where the endpoint is unavailable.
- "No fog, no map" escape hatch in Phase 1 for efforts that fit one session.
- Fixed shape for judgment questions: numbered title, body with 2–4 options, recommendation with its main weakness.

### Changed

- Sessions now come in three kinds — chart, work, route — and a session resolves at most one non-research ticket. Phase 3 is split into 3a (chart the frontier, create and wire tickets, stop) and 3b (claim one ticket, resolve, ripple, name the next, stop). Previously one session looped until the frontier was empty.
- The map is an index, not a store: decisions live on their tickets and the map gists and links; on a tracker the Frontier section is populated by query, never listed in the body.
- `assets/PLAN.template.md` gains a Tracker field, a Claimed by column, and the T type.
- Description rewritten to name the tracker as the map's home and add work-session triggers.
- All skill files normalized to LF line endings.

### Removed

- Silent fallback to `plans/<slug>.md` when instruction files did not name a tracker.

## [0.2.1] - 2026-08-29

### Changed

- Negative triggers in the description corrected: interrogating shipped work now points at `socratic` (was a stale sibling name), and a new negative trigger points session-conduct reviews at `retrospective`. Planning behavior is unchanged.

## [0.2.0] - 2026-08-06

### Added

- Quantified kill-rule expectations for each divergence move (Forced stimulus, Purpose climb, Provocation, Flip hunt) — the abandonment rule now has a concrete fail/survivor rate to check a suspiciously-clean pass against, not just a qualitative one.
- Degraded-mode fallback in Phase 2: if `references/divergence.md` is missing or unreadable, a condensed inline core loop for all four moves lets divergence still run instead of blocking.

## [0.1.0] - 2026-08-06

### Added

- Initial release: meridian skill.

[0.3.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.3.0
[0.2.1]: https://github.com/robcsaszar/meridian/releases/tag/v0.2.1
[0.2.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.2.0
[0.1.0]: https://github.com/robcsaszar/meridian/commit/fd0d846d0cbbd299e190c41fdf4e94326d86d3f0
