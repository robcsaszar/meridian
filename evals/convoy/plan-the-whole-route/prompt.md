---
max_turns: 20
allowed_tools: [Read, Glob, Grep, Write, Edit, Skill]
---

Read the repository's AGENTS.md and any delegation guidance it points to. Planning map #912 on GitHub has ten route items, #917 through #926 — read the map and the items with `gh issue view` (they are closed; treat them as open and unstarted). Write a concrete operating plan for working ALL TEN to completion in this session using subagents. Do not implement anything or change any files. Be specific about order and parallelism, what each subagent brief contains, how you verify a subagent's work, who commits and how files are staged, whether and when code review happens and by whom, whether UI quality is checked and when, what you do when a subagent reports a test failure in a file it did not touch, and what you do when a subagent says it is waiting for the test run to complete.
