# Quarantined eval cases

These cases are not part of the suite. They are kept because the data that
disqualified them is worth more than the cases were.

Measured at 10 runs per arm, both arms, one full suite run ($29.88, 1150s):

| Case | with | without | delta | why it is here |
|---|---|---|---|---|
| `afk-label-gate` | 0.65 +/-0.34 | 0.50 +/-0.24 | +0.15 | delta smaller than the spread |
| `workspace-defaults-to-file` | 0.35 +/-0.34 | 0.25 +/-0.26 | +0.10 | delta smaller than the spread |
| `route-gate-holds` | 0.53 +/-0.08 | 0.55 +/-0.35 | -0.03 | flat |
| `research-cites-and-defers` | 0.10 +/-0.21 | 0.20 +/-0.26 | -0.10 | both arms near zero; the task is hard for both |
| `waves-gates-and-commits` | 0.23 +/-0.24 | 0.55 +/-0.22 | **-0.32** | **convoy scores below baseline, reproducibly** |

## The one that is not just a bad test

`waves-gates-and-commits` has been negative in all four full runs and the
margin at n=10 is larger than either spread. Asked to describe how it would
work a whole route, convoy scores 0.23 against a baseline's 0.55.

Two readings, and it has not been settled which:

- the criteria reward a generic project-management answer, which a baseline
  writes fluently, while convoy's answer is specific and constrained; or
- convoy genuinely produces a worse plan for this prompt than no skill at all.

The second would be a real defect. It deserves a trace read
(`--keep-temp`, then `trace.jsonl`) before anyone assumes the first.

## Lesson for whoever rewrites these

At 3 runs per arm these deltas are not trustworthy. Two cases here read as
"consistently positive across three runs" and turned out to be noise once
measured at 10. Do not tune against a 3-run delta.
