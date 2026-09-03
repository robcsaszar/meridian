# Contributing

Thanks for considering a contribution to `meridian`. This is a small, single-skill repo.

## Before you start

- **The skill produced a bad plan?** Open an issue with what you asked for, which movement it ran (divergence, convergence, or both), and where it went wrong — a decision resolved without a recommendation, a dead idea silently dropped, a route item with no decision behind it. This is the highest-value kind of report here.
- **Proposing a change to the flow?** Open an issue describing the gap. The diagnose → diverge → converge → route order and the honesty rules are deliberate; if you're proposing to change them, explain why the existing structure doesn't already cover your case.
- **License or copyright holder:** don't change without asking first.

## Making a change

1. Fork and branch from `main`.
2. Keep edits inside `skills/meridian/`.
3. Preserve the honesty rules: ruled-out paths stay named with kill reasons, barren techniques admit it, recommendations name their main weakness. Any change to the method should keep those properties intact.

## Releasing (maintainers)

1. Bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, and add a dated `## [X.Y.Z]` entry to `CHANGELOG.md` with its link line.
2. Merge to `main`.
3. Run the **Release** workflow from the Actions tab with the tag (`vX.Y.Z`) and the merge commit as target. It tags, extracts the CHANGELOG entry, and publishes the GitHub release. Don't push tags by hand.

## Questions

Open an issue. There's no separate chat or forum for this project.
