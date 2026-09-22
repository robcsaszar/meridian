---
type: llm
weight: 1
---

Judge ONLY this single criterion. Ignore everything else the response does well or badly.

**Criterion:** Every subagent brief tells the agent not to run the full test suite and to report immediately when edits are complete; the orchestrator runs the gate

PASS only if the response clearly satisfies it. A plausible-sounding substitute does not count. Absence counts as FAIL.
