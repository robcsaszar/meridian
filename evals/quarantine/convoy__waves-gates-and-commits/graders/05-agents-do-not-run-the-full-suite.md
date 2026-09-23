---
type: llm
weight: 1
---

Judge ONLY this single criterion against the response. Ignore everything else it does well or badly.

**Criterion:** Subagents are told to run only the tests they touched and report; the full suite runs once at the gate, not once per agent.

PASS only if the response clearly satisfies it. Absence counts as FAIL.
