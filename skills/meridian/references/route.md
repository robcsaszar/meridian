# Route session shapes

Loaded in Phase 4. The spec shape, the slicing rules, and the route item body.

## Spec shape — `plans/<slug>/SPEC.md`

Written only when Bearings demanded a spec or the Route will exceed a handful of items. Synthesis of the Decision log, not a new interview. Use `CONTEXT.md` vocabulary; respect ADRs in the area.

- **Problem statement** — the problem from the user's perspective.
- **Solution** — the solution from the user's perspective.
- **User stories** — a long numbered list, `As a <actor>, I want <feature>, so that <benefit>`, covering every aspect.
- **Implementation decisions** — modules built or modified, their interfaces, schema changes, API contracts, specific interactions, architectural choices. No file paths or code; they rot. Exception: a prototype-derived snippet that encodes a decision more precisely than prose — a state machine, reducer, schema, type shape — trimmed to the decision-rich part and marked as prototype-derived.
- **Testing decisions** — what makes a good test here (external behaviour through public interfaces, never internals), which modules are tested, prior art in the repo's tests.
- **Out of scope** — what this spec deliberately excludes.
- **Further notes** — anything that fits nowhere else.

## Seams

A seam is the public boundary tests observe behaviour at. Prefer existing seams to new ones, the highest seam possible, as few as possible — the ideal number is one. Confirm the seams with the user before slicing; route items name theirs so transit drives test-first work there without renegotiating.

## Slicing rules

- A **tracer bullet** cuts a narrow but complete path through every layer it touches — schema, API, UI, tests — never a horizontal slice of one layer.
- A completed slice is demoable or verifiable on its own.
- A slice fits one fresh context window.
- Prefactoring comes first: make the change easy, then make the easy change.
- A **wide refactor** — one mechanical change (rename a column, retype a shared symbol) whose blast radius fans across the codebase so no slice can land green — is sequenced **expand → migrate → contract**: add the new form beside the old; migrate call sites in batches sized by blast radius, each batch its own item blocked by the expand; delete the old form in an item blocked by every batch. If even batches cannot stay green alone, they share an integration branch and all block one integrate-and-verify item.

## Quiz before publishing

Present the breakdown numbered — Title · Blocked by · What it delivers — and ask: is the granularity right (too coarse, too fine)? does each blocking edge genuinely gate? what should merge or split? Iterate until approved.

## Route item body

Published in dependency order, blockers first, as `plan:route` child items with `ready-for-agent`, or `ready-for-human` where the item needs manual testing, design judgment, or access an agent lacks.

```markdown
## Parent

[map name](url)

## What to build

<the end-to-end behaviour this item makes work, from the user's perspective — not a layer-by-layer list>

## Acceptance criteria

- [ ] <checkable criterion>

## Blocked by

- <route item name (link)>, or "None (can start immediately)"

## Seams

<where tests sit — confirmed above>

## From decisions

- <decision ticket name (link)>
```

No file paths or code snippets in the body; the prototype-derived exception above applies. Spikes deferred from experiments keep their place in the order. Never close or modify the parent map's tickets from a route item.
