# rutter — Specification

> Spec for [planning-plugin](../planning-plugin.md) · Synthesis of that map's 22 decisions, not a new interview.

## Problem statement

A planning method exists across three skills — meridian charts a body of work, transit works one ticket, convoy sails a whole map to done — but it lives in one private repo, wired to that project's build commands and file layout. Anyone else who wants the method has nothing to install. Worse, the three have drifted: they were written against different versions of each other and no longer share a ticket vocabulary, so meridian's maps and transit's expectations disagree about what a label means.

## Solution

One installable Claude Code plugin, `rutter`, that ships all three skills plus the agents they spawn, speaking a single vocabulary defined once. Installing it gives a person the whole plan-to-done pipeline in any repository: chart a map, work its tickets one at a time or sail the whole thing, with no assumption about their build tooling.

## User stories

1. As a developer in an unfamiliar repo, I want to install one plugin and get planning, ticket-working and whole-map execution together, so that I do not assemble three pieces myself.
2. As a developer, I want the plugin to discover my build and test commands, so that it works in a Makefile or pyproject repo as well as a pnpm one.
3. As a planner, I want every ticket label to mean the same thing to all three skills, so that a map charted by one is readable by the others.
4. As a planner, I want the vocabulary defined in exactly one place, so that it cannot drift between skills.
5. As an operator, I want each spawned agent to have a pinned model, effort and tool list, so that an unattended run cannot escalate itself.
6. As an operator, I want convoy's spawn guard to run from the installed plugin, so that its allowlist protects me rather than pointing at a path in someone else's project.
7. As a maintainer, I want a mechanical check that the plugin's copies and the origin project's copies have not diverged, so that the drift that caused this work does not recur silently.
8. As a maintainer, I want each skill's behaviour covered by an eval suite, so that a prompt edit that breaks behaviour is caught before release.
9. As a cautious installer, I want the agents' capabilities reviewed before the plugin is published, so that running it on my repository is a considered risk rather than an unexamined one.
10. As an installer on a distribution channel that forbids executables, I want the documentation to tell me plainly that convoy's guard is unavailable there, so that I am not silently unprotected.

## Implementation decisions

**Package shape.** A single plugin whose manifest names it `rutter` at version 1.0.0. Skills are discovered from a skills directory, one directory per skill; agents from an agents directory, one file per agent; executables from the plugin's binary directory, which is placed on PATH when the plugin is enabled. The published repository and its URL are unchanged; only the plugin's own identity is renamed.

**Vocabulary.** One reference document at plugin root defines the ticket-type labels under a single `meridian:` prefix and the execution-mode labels under a `mode:` prefix. All three skills reach it through the plugin-root path variable rather than carrying copies. This was verified to resolve from inside a skill before being adopted.

**Agent resolution.** Plugin agents are namespaced by the plugin name, and bare names do not resolve to them. Every spawn site in every skill therefore names the namespaced form. Project-level agents of the same bare name coexist rather than shadowing, so an installer's own agent is not reachable from these skills; that override is unsupported in this version and documented as such.

**Command discovery.** No build, test or lint command is written into any skill or agent. Each reads a commands block from the repository's own agent-instruction file, falling back to discovery from the project's manifest, makefile or equivalent. A repository offering neither yields no verification signal, and the skills must say so rather than assume success.

**Handoffs.** meridian charts and stops. A single ticket is worked by transit; a whole map by convoy. meridian states both exits and the rule for choosing between them, and implements neither.

**Spawn guard.** convoy's guard executes from the plugin's binary directory and whitelists the namespaced agent roster. Distribution channels that forbid bundled executables cannot carry it; that channel is unsupported for this version.

## Testing decisions

There is one seam: the loaded plugin. Everything observable about this package is observable by loading it and asking it something — structural validity, which components resolve, whether a shared reference is reachable, and how a skill behaves. Tests observe that boundary and never the source text.

Behaviour is covered per skill by eval suites held outside the skill directories, run through the plugin's own eval runner. Prior art is the existing retrospective and with-svelte suites: a small number of realistic prompts with checkable, falsifiable assertions, graded against a pre-change baseline rather than against nothing.

Source-level consistency — one label vocabulary, no build-tool assumptions, no origin-project references — is a lint in continuous integration, deliberately not a seam, because it observes text rather than behaviour.

## Out of scope

- Any change to the origin project's own copies of these skills; the two are kept separate by decision, with divergence caught by a check rather than prevented by a shared source.
- Restoring the installer's ability to override a bundled agent.
- Support for distribution channels that forbid bundled executables.
- Publishing under a name free of collision; the chosen name is contested and accepted as such.

## Further notes

The appetite bounds this at vocabulary unification and the plugin skeleton. Decoupling from one project's build tooling landed in route item 7: nothing in `skills/` or `agents/` names a package manager, and a probe in a Makefile-only Go repo resolved that repo's commands and reported the absent one as absent. Two couplings still block the full claim — route item 14 (the audit agent hard-requires a skill this plugin does not ship) and route item 15 (convoy's spawn guard probably never registers from a plugin). Until both close, "installable in any repository" is true of the build tooling but not of the package, and the release notes must not claim otherwise.
