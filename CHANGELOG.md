# Changelog

All notable changes to this project are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

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

[0.2.1]: https://github.com/robcsaszar/meridian/releases/tag/v0.2.1
[0.2.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.2.0
[0.1.0]: https://github.com/robcsaszar/meridian/releases/tag/v0.1.0
