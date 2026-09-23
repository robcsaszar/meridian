# Security Policy

This is a small, personally-maintained project. If you find a security issue:

- Do not open a public issue.
- Email robert@nhg.design with details and, if possible, steps to reproduce.

No formal response-time SLA. This is maintained on a best-effort basis.

## What the agents can reach

This plugin ships six subagents that convoy and transit spawn. They run on your
machine, in your repository, with your credentials. Their capabilities are set
in each agent's frontmatter and are the real boundary — a constraint written in
an agent's prose is guidance to the model, not an enforced control.

| Agent | Can read | Can write files | Can run a shell | Can reach the network |
|---|---|---|---|---|
| `rutter:scout` | yes | no | no | no |
| `rutter:auditor` | yes | no | no | no |
| `rutter:sweeper` | yes | **yes** (mechanical renames) | no | no |
| `rutter:reviewer` | yes | no | **yes** | no |
| `rutter:builder` | yes | **yes** | **yes** | no |
| `rutter:drill` | yes | no | **yes** | **yes** |

### Known risk: drill

`rutter:drill` can both fetch web content and run shell commands. Fetched pages
are untrusted input, and an agent that holds a shell while reading untrusted
input is the standard prompt-injection path: a crafted page can attempt to steer
it into running a command.

This is a deliberate trade — drill exists to attack a decision from an angle,
which sometimes means reading what is outside the repository. If that risk is
not acceptable for your work, remove `WebFetch` from `agents/drill.md` after
installing, or avoid unattended convoy runs on repositories you do not control.

### Known gap: the spawn guard

convoy declares a `PreToolUse` hook that restricts unattended runs to the six
agents above. **It is not yet verified to register when convoy is installed as a
plugin** — no plugin in the official marketplace declares hooks in skill
frontmatter, and the plugin inventory reports none for this one. Until that is
confirmed, treat the roster as a convention the skills follow, not as an
enforced limit.

### Running unattended

convoy is designed to work a whole route with nobody watching. Before doing that
on a repository that matters, know that `rutter:builder` edits files and runs
your repo's commands, and that nothing here pushes unless you ask.

