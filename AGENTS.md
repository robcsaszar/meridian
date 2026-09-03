# AGENTS.md

## Mission

This repo publishes the `meridian` skill for others to install. There is no build, no tests, no runtime of its own; the deliverable is the contents of `skills/meridian/`. Judge changes by one test: would a stranger who installs this skill into their own project get a correct, generically useful planning workflow out of it?

## Judgment boundaries

NEVER:
- Never let the skill implement the work it plans — the boundary at the route handoff is the design.

ASK:
- Ask before adding a second skill; this repo is intentionally single-skill.
- Ask before restructuring the diagnose → diverge → converge → route flow or removing the honesty rules.
- Ask before changing the license or copyright holder.

ALWAYS:
- Keep the skill's content generic — it must read as planning guidance for any project, never tied to one codebase or tracker product.

## Releasing

Releases are cut by the `Release` workflow (`.github/workflows/release.yml`), never by hand. It is a manual `workflow_dispatch` that takes a tag and a target ref, slices that version's entry out of `CHANGELOG.md` as the notes, and creates the tag and the GitHub release in one `gh release create`.

When to run it: after the release commit is merged to `main` — the workflow file must be on the default branch to be dispatchable, and the target should be the merge commit so the tag lands on `main`'s history.

Before dispatching, check:
- Version parity: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and the newest `## [X.Y.Z] - YYYY-MM-DD` heading in `CHANGELOG.md` all carry the same version, and the entry has its link line at the bottom of the file.
- The CHANGELOG entry exists and is complete. The workflow fails on a missing entry by design; do not work around it with a hand-written note.

How: Actions tab → Release → Run workflow with `tag=vX.Y.Z` and `target=<merge sha>`, or from a shell:

```sh
gh workflow run release.yml -f tag=vX.Y.Z -f target=<merge sha>
```

NEVER push a tag or create a release outside this workflow — a tag made by hand has no notes tied to it, and a later workflow run for the same version fails because the tag already exists.
