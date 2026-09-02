---
name: meridian
description: "Plans a body of work into a durable decision map on the repo's issue tracker (or a plans/ file when there is none) and an executable route. Use whenever the user wants to plan something out — a feature or bug that needs scoping before code, an idea too vague to act on, a wish to brainstorm directions or concepts, or a feeling of being stuck in obvious ideas — even if they don't ask for a formal plan. Also use to chart a new map, work the next ticket on an existing map, or chart its route. Trigger phrases — plan this out, help planning, let's brainstorm, scope this, break this down, turn this idea into a plan, roadmap this, next ticket, work the map. Don't use for naming or wording brainstorms, personal or event logistics, tasks the user mainly wants done now where a plan is incidental, a quick implementation sketch of a small in-session change, auditing existing code (run-crucible), interrogating shipped work (socratic), or reviewing how the session itself was conducted (retrospective)."
---

# Meridian

The plan is the meridian — the fixed line the whole body of work steers by. Take bearings → diverge if fogbound → converge one decision per session → chart the route. The map lives where the team already works, and it outlives every session.

## The workspace

Before any write, settle where the map lives. Work the ladder top-down; stop at the first rung that answers.

1. **Persisted choice** — a `## Planning` section in `CONTEXT.md`, else in `AGENTS.md`. If present, use it silently; no confirm.
2. **The user names one** in the request.
3. **Infer from the repo** — scan for signals and rank them: `.github/ISSUE_TEMPLATE/` or open issues on the GitHub remote → `github-issues` (a GitHub remote alone is a weak signal, proposed only when nothing stronger exists; an authenticated `gh` is a prerequisite for writing, not a signal); Jira keys in recent commit messages or branch names, `.jira*`/Atlassian config, a Jira URL in docs → `jira`; an existing `plans/` directory → `local-markdown`. Cite the signal when proposing.
4. **Nothing found** → `local-markdown`.

Rungs 2–4 end in a **confirm** before the first write — planning writes into a shared system — phrased as a judgment question with the inferred tracker recommended. On confirm, ask once: "Record this in CONTEXT.md (or AGENTS.md) so future sessions skip this step?" Write the section only on yes; if neither file exists, offer to create `AGENTS.md`. The persisted line carries what the tracker doc needs:

```markdown
## Planning

Tracker: github-issues · Map query: label plan:map
```

For Jira, also record the project key, the map and ticket issue types, and the blocking link-type name.

As soon as the rung resolves — before the confirm, since reads such as the map query need none — **MANDATORY READ** `references/trackers/<tracker>.md`. Every map operation — create map, create ticket, wire blocking, claim, frontier query, resolve and close, graduate fog — is done the way that doc says, never improvised. If the doc is missing, fall back to `local-markdown.md`; if that is missing too, use `assets/PLAN.template.md` and tell the user the tracker reference was unavailable.

## The map

One map per effort. On a tracker it is a single map item labelled `plan:map` with tickets as child items; on local markdown it is `plans/<slug>.md` from `assets/PLAN.template.md`. Escalate to `plans/<slug>/` only when Bearings demand multiple documents (spec, PRD, ADRs) — the map stays the index.

**Sections, always all seven:** **Destination** (one sentence the user would sign) · **Bearings** (context, constraints, appetite, who it's for) · **Decision log** (resolved, one line each, linking the ticket that holds the detail) · **Frontier** (open decisions — on a tracker, found by query, not listed) · **Fog** (too unclear to frame as a decision yet, with what would clarify each) · **Ruled out** (killed paths with kill reasons) · **Route** (the work breakdown, filled in Phase 4).

**The map is an index, not a store.** A decision lives in exactly one place — its ticket — and the map gists it and links. Refer to tickets by name, never bare number; a wall of `#42 #43` is illegible.

**Tickets.** Each frontier decision is its own ticket, sized to one session, body headed `## Question`. Each carries exactly one type label:

| Label | Type | What unblocks it | Who |
|---|---|---|---|
| `plan:judgment` | Judgment | Only the user can answer | with the user |
| `plan:research` | Research | Evidence from the codebase or the world | scout subagent |
| `plan:experiment` | Experiment | Talking cannot settle it; a small spike can | with the user |
| `plan:task` | Task | Nothing to decide — work that must happen first (access, sample data, a signup) | either |

Tiebreaker: if the outcome *resolves* a decision it is an experiment; if it only *enables* one it is a task. Route items (Phase 4) carry `plan:route` so they never pollute the frontier query. If any `plan:` label already exists with a different meaning in the tracker, ask before reusing it.

**Blocking** uses the tracker's native dependency relation so the frontier is visible in its own UI; a **claim** is an assignee, set before any work. The **frontier** is the open, unblocked, unclaimed tickets.

## Sessions

Three session kinds. **Never resolve more than one non-research ticket per session.**

- **Chart** — Phases 1–3a: bearings, divergence if fogbound, breadth-first frontier, tickets created and wired. Ends without resolving anything but research.
- **Work** — Phase 3b: claim one frontier ticket, resolve it, update the map, graduate fog. Research tickets are the exception: scouts may resolve any number, in parallel, in any session.
- **Route** — Phase 4: frontier empty, distill the log into the Route, name the first move.

**Resume first.** Before creating a map, look for one — the tracker doc's map query, or glob `plans/*.md`. If found, load the map body only (not every ticket), restate Destination and the current frontier in two lines, and pick the session kind from its state. Several plausible matches → list them and ask; never guess. A changed Destination marks the map superseded and starts a successor linking back.

**Subagents scout; you write** — the map is the cross-session handoff; subagent memory is not.

## Phase 1 — Take bearings

Resolve the workspace. Name what the user brought — idea, feature, bug, an itch to brainstorm — and state a candidate Destination in one sentence they would sign. Then diagnose:

- Destination statable and confirmed → create the map, fill Destination and Bearings, go to Phase 3.
- Destination vague, directions missing or all obvious, or the user signals stuckness → fill Bearings with what is known, go to Phase 2.
- The user rejects the candidate without naming what's wrong → the rejection is fog; go to Phase 2.

Ask at most two orienting questions here; deeper questions belong on the frontier where they are tracked. Appetite is a Bearings entry — ask for it, never assume it.

**No fog, no map.** If the Destination is signed and the breadth-first sweep in Phase 3a surfaces nothing that outlives this session, say so and ask how the user wants to proceed instead of charting a map for one sitting's work.

Completion criterion: the workspace is resolved (confirmed where the ladder requires it), and the map exists with Bearings filled and either a signed Destination or a named fog symptom.

## Phase 2 — Diverge (only when fogbound)

MANDATORY READ [`references/divergence.md`](references/divergence.md) before running any move. Do NOT load it when Phase 1 routed straight to Phase 3.

**Degraded mode.** If the reference is missing or unreadable, do not block — run this condensed core loop inline and tell the user the full reference was unavailable:

| Move | Symptom | Mechanic | Kill rule |
|---|---|---|---|
| Forced stimulus | No ideas, or every idea feels the same | Anchor on something unrelated to the domain; force a bridge from each of its properties | Kill bridges that needed the property redefined into vagueness; expect most to die |
| Purpose climb | Suspicion of solving the wrong problem | Climb "what is this in service of?" 2–3 levels; at each, generate 2–3 sibling problems that would also serve it | Kill strawman siblings; expect at least one real sibling to die on inspection |
| Provocation | A constraint everyone treats as unbreakable | State the impossible version as fact; extract the real mechanism from each consequence | Drop consequences with no extractable mechanism; if none yield one, the constraint is load-bearing — record that as a finding |
| Flip hunt | The current approach feels inevitable | Flip each load-bearing assumption to its strongest plausible opposite; hunt a real place where the flip already holds | No real "where" found kills the flip; expect at least one flip to die and at least one assumption to survive |

Match the symptom to one move — one move per pass, never two. Run its full loop including the kill rule, close with the meta-pattern scan, and record everything on the map: survivors as candidate directions, dead ideas in Ruled out with kill reasons. Present survivors and let the user pick — divergence never converges on their behalf. A second pass with a different move is allowed if the user asks or nothing survived. A barren or unfinished pass ends the session with the fog symptom written into the map; the next chart session resumes from it.

Completion criterion: the user has picked a direction, the Destination is written from it, and Ruled out is non-empty or the barren pass is recorded.

## Phase 3 — Converge

### 3a — Chart the frontier (chart session)

Sweep the whole body of work breadth-first — scope, users, data, interfaces, sequencing, risks, quality bar — and write every open decision as its own ticket before resolving any. Type each by what unblocks it. What cannot yet be framed as a question goes to Fog with a note on what would clarify it — the test is whether the question can be *stated* precisely now, not whether it can be answered. Do not pre-slice fog into tickets.

Create tickets, then wire blocking in a **second pass** — items need ids before they can reference each other. Claim every research ticket and fire a scout on each now; they run in parallel and report back as text, and their findings are recorded the way 3b's Research step says. Then stop: charting resolves nothing else.

### 3b — Work one ticket (work session)

1. Load the map body. Choose the ticket: the one the user named, else the frontier ticket that unblocks the most. **Claim it** before any work.
2. Resolve by type. **Judgment** — interview the user one question at a time, in this shape, and wait for the answer:

   ```markdown
   **Q<n>** - **<question title>**: <question body, with 2–4 concrete options>

   **Recommendation:** <the option> — <why in one or two lines>. Main weakness: <named>.
   ```

   **Research** — the scout's findings with citations (file, line, URL), plus a recommendation for the user's sign-off; evidence is delegable, judgment is not. **Experiment** — write the spike as a `plan:route` item whose stated outcome resolves the decision; mark the ticket deferred to it; do not argue it to a fake resolution. **Task** — do it when the session's own tools can, otherwise hand the user a precise checklist; the resolution records what was done and every resulting fact later tickets depend on.
3. Record: resolution comment, close the ticket (a deferred experiment stays open, marked deferred), one line in the map's Decision log. Options killed for cause go to Ruled out with their reasons — an option merely not chosen is not a killed path.
4. Ripple: create newly surfaced tickets (create-then-wire); graduate any fog the answer made statable, removing it from Fog so it lives only as its ticket; a ticket now beyond the Destination is closed and noted in Ruled out as out of scope; tickets the decision invalidated are updated or closed with a one-line reason, never orphaned.
5. Stop. Name the next frontier ticket and end the session.

Expect other sessions to be editing the tracker concurrently; the claim is what keeps them apart. A session that ends with its ticket unresolved releases the claim and leaves a comment saying where it stopped — a claim that outlives its session hides the ticket from every later frontier query.

Completion criterion (for the map): no open, undeferred tickets remain — every decision is resolved in the log, deferred to a route spike, or in Fog with a named trigger.

## Phase 4 — Chart the route (route session)

Distill the Decision log into the Route: ordered work items labelled `plan:route`, each with acceptance criteria and a reference to the decision(s) that shaped it — an item no decision demanded is scope creep; flag it or cut it. Spikes keep their place in the order. Escalate to `plans/<slug>/` documents only if Bearings demanded specs or ADRs.

End by naming the first move — the smallest route item that unblocks the most — and stop. Implementation is a different job.

Completion criterion: every log entry is reflected in the Route or explicitly needs no work; the first move is named; the map is marked route-ready; nothing has been implemented without an explicit go.

## Rules

- Ruled out stays on the chart — every killed path keeps its name and kill reason; visible dead ends are what make the surviving plan credible.
- A barren move says so — "this produced nothing" is a valid result. A session where every technique works was faked.
- Every recommendation names its main weakness; one without is advertising.
- A finished map with an empty Ruled out and no weighed alternatives in the log is flagged as untested — nothing was weighed, so nothing was chosen.
- Research answers cite their evidence; an uncited claim is speculation and is marked as such.

## NEVER

- **NEVER write to a tracker before the workspace is confirmed**
  **Instead:** Walk the ladder; confirm on rungs 2–4; persist only when the user says yes.
  **Why:** A tracker is shared. An unasked-for map item with five new labels is noise the whole team sees and someone has to clean up.

- **NEVER resolve more than one non-research ticket in a session**
  **Instead:** Claim one, resolve it, ripple, name the next, stop.
  **Why:** With only one decision to reach, there is nothing to rush toward — the pull to finish the frontier is what turns an interview into a monologue that decides on the user's behalf.

- **NEVER resolve a judgment ticket without the user**
  **Instead:** Ask in the 3b question shape and wait for the answer.
  **Why:** A plan fixed before its questions were asked ignores the answers that would have changed it.

- **NEVER invent timelines or effort estimates**
  **Instead:** Record appetite in Bearings; give the Route order and acceptance criteria only.
  **Why:** A confident "~4.5 weeks" nobody asked for anchors every later scoping conversation to a number with no evidence.

- **NEVER ask a subagent to write the map**
  **Instead:** Scouts return text; the orchestrator writes every artifact.
  **Why:** The map is the only state that survives the session; an agent writing it directly leaves the orchestrator unable to reconcile what the map claims with what was decided.

- **NEVER start implementing route items on your own initiative**
  **Instead:** Name the first move and stop; implement only when the user explicitly says go after seeing the finished route.
  **Why:** Planning and doing in one sitting bends the route toward whatever is easiest to execute right now.
