# Gate mechanics

What the orchestrator runs at Phase 3 and Phase 6b — the per-item checklist, then the shell. Each section is the smallest thing that has failed here.

## Contents

- [Checklist](#checklist)
- [Line endings](#line-endings)
- [Partial-hunk staging](#partial-hunk-staging)
- [Tombstone guard](#tombstone-guard)
- [Attributing a failure](#attributing-a-failure)
- [Ticking by ancestry](#ticking-by-ancestry)

## Checklist

The additions to the repo's verify-then-commit, applied per item at Phase 3:

1. Compare the lint count to the baseline; a new warning in a touched file is the agent's, whatever it says.
2. For the one acceptance criterion that carries risk — a visibility rule, a data-path move, a deletion — trace it yourself.
3. When a fix moves data off one path onto another, grep every **consumer** of the old path, not the one the report mentions. "Unaffected" describes the thing it looked at.
4. Write the orchestrator-owned lines the agent reported. Stage by explicit path; one item per commit, carrying `Closes #<n>`. A wave-hub file is staged whole into the wave's **last** item's commit, never hunk-split; each earlier commit's message names the commit that completes it. § Partial-hunk staging stays for the rare file no wave owns.
5. Before staging, § Line endings and § Partial-hunk staging below. Scripted writes flip LF to CRLF and zero-context hunks land at the wrong offset silently; both have happened here.
6. A new test in a shared-database suite cleans up its rows at the end of that test — later cases count them.
7. A test file deleted on the strength of its name is restored from HEAD and read by its imports before it goes.
8. An agent report that replaces the item's named seam — "no harness renders this", "tested the helper instead" — is a gap: file it on the map and do not accept the substitute as the seam. Three such reports in a row once shipped three pages nobody had rendered.
9. When any end-to-end spec changed in this convoy, the end-to-end suite runs once before Phase 6 — a changed spec is the one place a convoy can corrupt shared data without a unit test ever failing.
10. An acceptance criterion the orchestrator can only meet by *narrowing* a logged decision ("gate the content, keep the tiles") is a judgment ticket, filed and resolved by the Phase 1 predicate before the commit — never a reading applied at the gate and noted on the map afterwards.

Paths in `git status` that no owner claims get attributed at the gate — `git diff` against the wave's reports — or restored, before any re-snapshot can mistake them for the user's. A report saying "pre-existing", "unrelated", or "not mine" is a claim to verify — agents have called their own unformatted file "pre-existing", deleted a domain test suite as "the staging test", and called a consumer "unaffected" after removing its input. Check against `git status` and the baseline first; attribute a disowned failure by the failing suite's imports (§ Attributing a failure). A failure that holds on the baseline and belongs to no item is filed as a `meridian:task` with `mode:agent` under the map, with the reproduction and the commit it holds on; the gate proceeds against the baseline.

Gate fails on a path outside the item's predicted ∪ reported ∪ orchestrator set → not this item's failure; re-gate after that path's owner reports. Otherwise: under thirty lines across one or two files, fix and re-gate; larger, revert the item's scope — `git restore <paths>` for tracked, `rm` for untracked it added; a reported path another report also names is left in place and both items fail — comment the failing output on the ticket, re-queue it. Twice re-queued → leave it open with the output; the map says why.

## Line endings

Scripted writes on Windows emit CRLF unless the file is opened with `newline=""` — a Python or heredoc rewrite of an LF file turns every line into a diff line and the real change disappears inside it. Prefer the Edit tool for prose; when a script must write, open with `newline=""`.

Before staging, check every dirty path:

```sh
for f in $(git status --porcelain | awk '{print $2}'); do
  [ -f "$f" ] && file "$f" | grep -q CRLF \
    && ! (git show "HEAD:$f" 2>/dev/null | file - | grep -q CRLF) \
    && { sed -i 's/\r$//' "$f"; echo "fixed $f"; }
done
```

A file that was CRLF at HEAD stays CRLF. A single bare `\r` inside a line (a literal `\r` in a heredoc that the shell collapsed) also reads as "with CR" — `grep -c $'\r'` finds it; fix it with perl or the Edit tool, not another heredoc.

## Partial-hunk staging

Two items in one wave touching one shared file — `quizSession.svelte.ts`, `page-config.ts` — are split at the gate by hunk, not by file:

```sh
git diff -U0 <file> | python -c "
import sys,re
kw=sys.argv[1:]
t=sys.stdin.buffer.read().decode(); parts=re.split(r'(?m)^(?=@@ )',t)
hunks=[h for h in parts[1:] if any(k in h for k in kw)]
sys.stdout.buffer.write((parts[0]+''.join(hunks)).encode())" <keyword…> > h.patch
git apply --cached --unidiff-zero h.patch
```

Zero-context hunks land at the wrong offset silently — one landed a reset inside a curator-only branch. After **every** `--unidiff-zero` apply, read `git diff --cached -U2 <file>` before the commit; a `+`/`-` pair of identical lines is the tell. The other item's commit repairs the placement, so the pair is acceptable only when the next commit is that item's.

## Tombstone guard

The grep is a gate, not a report — a printed `1` has been committed straight past. Chain it into the commit:

```sh
[ "$(git diff --cached | grep -E '^\+' | grep -cE 'used to|no longer|previously|the old ')" -eq 0 ]   && git commit -q -F msg.txt
```

## Attributing a failure

An agent cannot attribute a failure across the wave: stash is forbidden and a suite cannot run against `git show HEAD:<file>` in a temp path. "Reproduces on a clean checkout of that file" restores the test, not the source another item changed. The gate attributes by imports: the failing suite's imports against the wave's predicted sets — the item whose file it imports owns the failure, whatever its report says.

## Ticking by ancestry

A Route box ticks only when the closing commit is on the default branch remotely:

```sh
sha=$(git log --format=%h --grep "Closes #<n>\b" -1)
git merge-base --is-ancestor "$sha" origin/main && echo shipped || echo "committed, unpushed"
```

Run it per item at Phase 0 (reconciliation), Phase 6 (report) and Phase 6b (close-out). "Committed, unpushed" is a state the report names with its commit range; it is never a tick.
