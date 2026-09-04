---
name: meridian
description: "Plans a body of work into a durable decision map on the repo's issue tracker (or a plans/ file) and a route of tracer-bullet tickets. Use whenever the user wants to plan something out — a feature or bug that needs scoping before code, an idea too vague to act on, a wish to brainstorm directions, or a feeling of being stuck in obvious ideas — even if they don't ask for a formal plan. Also use to chart a new map or, once its frontier is empty, to write its spec and route. Trigger phrases — plan this out, help planning, let's brainstorm, scope this, break this down, turn this idea into a plan, roadmap this, chart the route, to spec, to tickets. Don't use for working or implementing a ticket on an existing map (transit), naming or wording brainstorms, personal or event logistics, tasks the user mainly wants done now, a quick sketch of a small in-session change, auditing existing code (crucible), interrogating shipped work (socratic), or reviewing how the session was conducted (retrospective)."
---

# Meridian

The plan is the meridian — the fixed line the whole body of work steers by. Take bearings → diverge if fogbound → chart the frontier → chart the route. Tickets between those two are worked by **transit**, one crossing per run. The map lives where the team already works, and it outlives every session. Order of operations: resolve the workspace, resume if a map exists, then Phase 1.

## The workspace

Before any write, settle where the map lives. Work the ladder top-down; stop at the first rung that answers.

1. **Persisted choice** — a `## Planning` section in `CONTEXT.md`, else in `AGENTS.md`. If present, use it silently; no confirm.
2. **The user names one** in the request.
3. **Infer from the repo** — scan for signals and rank them: `.github/ISSUE_TEMPLATE/` or open issues on the GitHub remote → `github-issues` (a bare GitHub remote is a weak signal; an authenticated `gh` is a prerequisite for writing, not a signal); Jira keys in recent commit messages or branch names, `.jira*`/Atlassian config, a Jira URL in docs → `jira`; an existing `plans/` directory → `local-markdown`. Cite the signal when proposing.
4. **Nothing found** → `local-markdown`.

Rungs 2–4 end in a **confirm** before the first write, phrased as a judgment question with the inferred tracker recommended. On confirm, ask once: "Record this in CONTEXT.md (or AGENTS.md) so future sessions skip this step?" Write the section only on yes; if neither file exists, offer to create `AGENTS.md`. The persisted line carries what the tracker doc needs:

```markdown
## Planning

Tracker: github-issues · Map query: label plan:map
```

For Jira, also record the project key, the map and ticket issue types, and the blocking link-type name.

As soon as the rung resolves — before the confirm, since reads such as the map query need none — **MANDATORY READ** `references/trackers/<tracker>.md`. Every map operation — create map, create ticket, wire blocking, claim, frontier query, resolve and close, graduate fog — is done the way that doc says, never improvised. If the doc is missing, fall back to `local-markdown.md`; if that is missing too, use `assets/PLAN.template.md` and tell the user the tracker reference was unavailable.

## The map

One map per effort. On a tracker it is a single map item labelled `plan:map` with tickets as child items; on local markdown it is `plans/<slug>.md` from `assets/PLAN.template.md`. Escalate to `plans/<slug>/` only when Bearings demand multiple documents (spec, PRD) — the map stays the index.

**Seven sections, always all,** in `assets/PLAN.template.md` order — Destination, Bearings, Decision log, Frontier, Fog, Ruled out, Route; the template says what each holds. On a tracker the Frontier section stays empty and is found by query.

**The map is an index, not a store.** A decision lives in exactly one place — its ticket — and the map gists it and links. Refer to tickets by name, never bare number; a wall of `#42 #43` is illegible.

**Tickets.** Each frontier decision is its own ticket, sized to one session, body headed `## Question`. Each carries exactly one type label:

| Label | Type | What unblocks it | Mode |
|---|---|---|---|
| `plan:judgment` | Judgment | Only the user can answer | HITL |
| `plan:research` | Research | Evidence from the codebase or the world | AFK |
| `plan:experiment` | Experiment | Talking cannot settle it; a throwaway prototype the user reacts to can | HITL |
| `plan:task` | Task | Nothing to decide — work that must happen first (access, sample data, a signup) | declared |

**Mode.** A HITL ticket resolves only through a live exchange with the user; an agent never stands in for the user's side of it. An AFK ticket an agent drives alone. Judgment and experiment are HITL by type, research AFK by type. Task and route tickets *declare* their mode with a second label at creation — `ready-for-agent` or `ready-for-human` — so an unattended run can tell what it may take. Tiebreaker: if the outcome *resolves* a decision it is an experiment; if it only *enables* one it is a task. Route items (Phase 4) carry `plan:route` so they never pollute the frontier query. If any `plan:` label already exists with a different meaning in the tracker, ask before reusing it.

**Blocking** uses the tracker's native dependency relation so the frontier is visible in its own UI; a **claim** is an assignee, set before any work. The **frontier** is the open, unblocked, unclaimed tickets.

## Sessions

Meridian runs two session kinds; the third belongs to transit.

- **Chart** — Phases 1–3: bearings, divergence if fogbound, breadth-first frontier, tickets created and wired, scouts fired. Resolves nothing but research.
- **Route** — Phase 4: frontier empty; spec if demanded, seams, tracer-bullet slices, route tickets, first move.
- **Work** — transit's: claim one ticket, resolve it by label, ripple, release. Never done here.

**Resume first.** Before creating a map, look for one — the tracker doc's map query *and* glob `plans/*.md`; a map found only in `plans/` on a tracker workspace is stale — ask whether to migrate or ignore it. If found, load the map body only (not every ticket), restate Destination and the current frontier in two lines, and pick the session kind from its state: open undeferred tickets → hand to transit; only deferred tickets (or none) and no Route → route session; Route present → hand to transit; the user brings new scope to a live map → run Phase 3 rounds on that branch only, create and wire its tickets, stop. Several plausible matches → list them and ask; never guess. A changed Destination marks the map superseded and starts a successor linking back.

## Phase 1 — Take bearings

Name what the user brought — idea, feature, bug, an itch to brainstorm — and state a candidate Destination in one sentence they would sign. Then diagnose:

- Destination statable and confirmed → create the map, fill Destination and Bearings, go to Phase 3.
- Destination vague, directions missing or all obvious, or the user signals stuckness → fill Bearings with what is known, go to Phase 2.
- The user rejects the candidate without naming what's wrong → the rejection is fog; go to Phase 2.

Ask at most two orienting questions here; deeper questions belong on the frontier where they are tracked. Appetite is a Bearings entry — ask for it, never assume it.

**No fog, no map.** If the Destination is signed and the breadth-first sweep in Phase 3 surfaces nothing that outlives this session, say so and ask how the user wants to proceed instead of charting a map for one sitting's work.

Completion criterion: the workspace is resolved (confirmed where the ladder requires it), and the map exists with Bearings filled and either a signed Destination or a named fog symptom.

## Phase 2 — Diverge (only when fogbound)

MANDATORY READ [`references/divergence.md`](references/divergence.md) before running any move. Do NOT load it when Phase 1 routed straight to Phase 3.

If the reference is missing or unreadable, do not improvise moves: write the fog symptom into the map, tell the user the reference was unavailable, and end the session.

Match the symptom to one move — one move per pass, never two. Run its full loop including the kill rule and record everything on the map: survivors as candidate directions, dead ideas in Ruled out with kill reasons. Present survivors and let the user pick — divergence never converges on their behalf. A second pass with a different move is allowed if the user asks or nothing survived. A barren or unfinished pass ends the session with the fog symptom written into the map; the next chart session resumes from it.

Completion criterion: the user has picked a direction, the Destination is written from it, and Ruled out is non-empty or the barren pass is recorded.

## Phase 3 — Chart the frontier (chart session)

Sweep the whole body of work breadth-first — scope, users, data, interfaces, sequencing, risks, quality bar — as a **design tree**, every decision branching into the ones that hang off it. Put the sweep to the user in **rounds**:

- A round is the tree's current frontier — every candidate decision whose prerequisites are settled. Number each, give its type, and where you have one, a recommended answer with its main weakness. A candidate that depends on another still open this round belongs to a later round.
- Facts are yours to find. Dispatch a scout for anything in the filesystem, tools, or docs; never ask the user for a fact you could look up. Only the questions downstream of a running scout wait.
- The user confirms, merges, kills, or answers each candidate. A killed candidate → Ruled out with its reason. An **answered** candidate is not ticketed — it goes straight to the Decision log, Via J. What cannot yet be framed as a question → Fog, with what would clarify it; the test is whether the question can be *stated* precisely now, not answered. Do not pre-slice fog into tickets.
- Sharpen terms as they surface (see Rules).

Rounds end when the tree has no unvisited branch. Then create tickets, and wire blocking in a **second pass** — items need ids before they can reference each other. Claim every research ticket and fire a scout on each now; they run in parallel and report back as text. Record each finding per the tracker doc's *Resolve and close*; findings follow `.claude/skills/transit/references/dispatch.md` § plan:research (every claim cited and confidence-flagged) — if that file is absent, require a citation on every claim and mark uncited ones as speculation. A finding that implies a decision becomes a new judgment ticket, never a decision. Then stop: charting resolves nothing else.

Completion criterion: every candidate the rounds surfaced is a ticket, a log line, a Ruled out line, or a Fog line; blocking is wired; research scouts are fired; nothing else is resolved.

## Phase 4 — Chart the route (route session)

Precondition: no open, undeferred tickets. MANDATORY READ [`references/route.md`](references/route.md) for the spec shape, seam rules, slicing rules, and route item body. Then, in order:

Then, per the reference and in this order: spec (only when Bearings demanded one or the Route exceeds a handful of items) → seams confirmed with the user → tracer-bullet slices → quiz → publish as `plan:route` items, each with `ready-for-agent` or `ready-for-human`. An item no decision demanded is scope creep — flag or cut it.

Name the **first move** — the smallest route item that unblocks the most — mark the map route-ready, and stop. Implementation is transit's job.

Completion criterion: every log entry is reflected in a route item or explicitly needs no work; seams are confirmed; every item has acceptance criteria, a mode label, and wired blockers; the first move is named; nothing has been implemented.

## Rules

- Ruled out stays on the chart — every killed path keeps its name and kill reason; visible dead ends are what make the surviving plan credible.
- A barren move says so — "this produced nothing" is a valid result. A session where every technique works was faked.
- Every recommendation names its main weakness; one without is advertising.
- A finished map with an empty Ruled out and no weighed alternatives in the log is flagged as untested — nothing was weighed, so nothing was chosen.
- Research answers cite their evidence; an uncited claim is speculation and is marked as such.
- Terms are sharpened as they land: a term that conflicts with `CONTEXT.md`'s glossary is called out and settled; a fuzzy or overloaded one gets a canonical name; a resolved term is written to `CONTEXT.md` immediately, glossary only, never implementation detail. Offer an ADR only when the decision is hard to reverse, surprising without context, and a real trade-off — all three.

## NEVER

- **NEVER write to a tracker before the workspace is confirmed**
  **Instead:** Walk the ladder; confirm on rungs 2–4; persist only when the user says yes.
  **Why:** A tracker is shared. An unasked-for map item with five new labels is noise the whole team sees and someone has to clean up.

- **NEVER resolve a non-research ticket in a chart or route session**
  **Instead:** Create it, wire it, fire scouts on research; hand the rest to transit.
  **Why:** With the whole frontier in view, the pull to finish it turns charting into a monologue that decides on the user's behalf — one ticket per run is what keeps each answer honest.

- **NEVER invent timelines or effort estimates**
  **Instead:** Record appetite in Bearings; give the Route order and acceptance criteria only.
  **Why:** A confident "~4.5 weeks" nobody asked for anchors every later scoping conversation to a number with no evidence.

- **NEVER ask a subagent to write the map**
  **Instead:** Scouts return text; the orchestrator writes every artifact.
  **Why:** The map is the only state that survives the session; an agent writing it directly leaves the orchestrator unable to reconcile what the map claims with what was decided.

- **NEVER start implementing route items on your own initiative**
  **Instead:** Name the first move and stop; transit implements, and only from a ticket labelled for it.
  **Why:** Planning and doing in one sitting bends the route toward whatever is easiest to execute right now.
