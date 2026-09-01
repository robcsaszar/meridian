# Changelog

All notable changes to this project are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [0.3.0] - 2026-09-01

### Added

- Workspace resolution ladder: persisted `## Planning` section in `CONTEXT.md` (else `AGENTS.md`) → user-named tracker → inference from repo signals (`.github/ISSUE_TEMPLATE/`, `gh` auth, Jira keys in commits, existing `plans/`) → local markdown. Rungs after the persisted one confirm before the first write and offer to persist the choice so later sessions skip the step.
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

## [0.2.0] - 2026-08-06

### Added

- Quantified kill-rule expectations for each divergence move (Forced stimulus, Purpose climb, Provocation, Flip hunt) — the abandonment rule now has a concrete fail/survivor rate to check a suspiciously-clean pass against, not just a qualitative one.
- Degraded-mode fallback in Phase 2: if `references/divergence.md` is missing or unreadable, a condensed inline core loop for all four moves lets divergence still run instead of blocking.

## [0.1.0] - 2026-08-06

### Added

- Initial release: meridian skill.

[0.3.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.3.0
[0.2.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.2.0
[0.1.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.1.0
