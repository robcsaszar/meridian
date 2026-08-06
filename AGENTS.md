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
