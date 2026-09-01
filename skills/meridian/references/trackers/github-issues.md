# Tracker: GitHub Issues

Loaded when the workspace resolves to `github-issues`. All operations go through `gh`; confirm it is authenticated against this repo's remote before the first write (`gh auth status`). Sub-issues and issue dependencies are GitHub-native features — use them, and fall back to body conventions only where this repo's plan does not expose them.

Persisted line: `Tracker: github-issues · Map query: label plan:map`

## Labels

Ensure the six labels exist once per repo; create any that are missing.

```sh
for l in plan:map plan:judgment plan:research plan:experiment plan:task plan:route; do
  gh label create "$l" --color 1D76DB --description "meridian planning" 2>/dev/null || true
done
```

If a `plan:` label already exists with a different description, stop and ask before reusing it.

## Create the map

One issue, labelled `plan:map`, titled with the effort's name. Body is the seven-section map from `assets/PLAN.template.md` with the Frontier section reading only "open child issues — see query below". Frontier tickets are never listed in the map body.

```sh
gh issue create --label plan:map --title "<effort name>" --body-file map.md
```

Record the returned number; every later operation references it.

## Create a ticket

A ticket is an issue with one type label and body `## Question` followed by the decision. Then attach it as a sub-issue of the map. The sub-issue API takes the issue's database id, not its number.

```sh
gh issue create --label plan:judgment --title "<ticket name>" --body-file ticket.md
MAP_NUM=<map number>; SUB_NUM=<new number>
SUB_ID=$(gh api "repos/{owner}/{repo}/issues/$SUB_NUM" --jq .id)
gh api -X POST "repos/{owner}/{repo}/issues/$MAP_NUM/sub_issues" -F sub_issue_id="$SUB_ID"
```

Route items (Phase 4) are created the same way with `plan:route`.

## Wire blocking

Second pass, after every ticket in the batch has a number. Use issue dependencies so the frontier renders in GitHub's own UI.

```sh
BLOCKER_ID=$(gh api "repos/{owner}/{repo}/issues/<blocker number>" --jq .id)
gh api -X POST "repos/{owner}/{repo}/issues/<blocked number>/dependencies/blocked_by" -F issue_id="$BLOCKER_ID"
```

If the dependencies endpoint is unavailable on this repo, add a line `Blocked by: [<ticket name>](<url>)` to the blocked ticket's body and treat it as the relation.

## Claim

Assign before any work; an unassigned open ticket is unclaimed.

```sh
gh issue edit <number> --add-assignee @me
```

## Frontier query

Open, unassigned children of the map, then drop any with an open blocker.

```sh
gh issue list --search "is:open no:assignee label:plan:judgment,plan:research,plan:experiment,plan:task" --json number,title,labels
# for each: gh api "repos/{owner}/{repo}/issues/<number>/dependencies/blocked_by" --jq '[.[] | select(.state=="open")] | length'
```

Keep only tickets whose open-blocker count is zero. With the body fallback, parse `Blocked by:` lines and check each linked issue's state.

## Resolve and close

The answer is a comment, then the issue closes, then the map's Decision log gets one line: name (linked) plus a one-line gist.

```sh
gh issue comment <number> --body-file resolution.md
gh issue close <number> --reason completed
gh issue edit <map number> --body-file map.md   # after editing the Decision log locally
```

An experiment ticket that defers to a spike stays open with a comment `Deferred → [<route item name>](<url>)`. A ticket ruled out of scope closes with `--reason "not planned"` and gets one line in the map's Ruled out.

## Graduate fog

Delete the graduated line from the map's Fog section, create the ticket(s) it became (create-then-wire), and rewrite the map body. The fog line and its ticket never coexist.
