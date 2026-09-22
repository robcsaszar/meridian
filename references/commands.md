# Build commands

How every rutter skill and agent finds a repository's build, test, lint and
typecheck commands. Nothing in this plugin hardcodes a package manager — a
repo may be Node, Python, Go, Rust, Make-driven, or none of those.

Referenced as `${CLAUDE_PLUGIN_ROOT}/references/commands.md`.

## The ladder

Walk it in order and stop at the first rung that answers.

1. **Declared.** A `## Commands` section in `AGENTS.md`, else `CONTEXT.md`. This
   is authoritative — it overrides anything discovery would infer, because the
   maintainer wrote it on purpose. Shape:

   ```markdown
   ## Commands

   | Purpose | Command |
   |---|---|
   | test | `pnpm test` |
   | test one file | `pnpm test <path>` |
   | typecheck | `pnpm typecheck` |
   | lint | `npx biome check --write <files>` |
   | build | `pnpm build` |
   ```

   Only the rows a repo has. A missing row means that check does not exist here,
   not that you should guess one.

2. **Discovered.** No declared block → read the project's own manifest:

   | Signal | Where the commands live |
   |---|---|
   | `package.json` | its `scripts` block; the lockfile names the manager (`pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`, else npm) |
   | `Makefile` | its targets — `make test`, `make lint`, whatever exists |
   | `pyproject.toml` | `[tool.poetry.scripts]`, `[project.scripts]`, or the tool sections (pytest, ruff, mypy) |
   | `Cargo.toml` | `cargo test`, `cargo clippy`, `cargo check` |
   | `go.mod` | `go test ./...`, `go vet ./...` |
   | `justfile` | its recipes |

3. **Absent.** Neither rung answers → **there is no verification signal in this
   repository.** Say so plainly, in the report and on the ticket. Do not invent a
   command, do not run a tool the repo does not use, and do not treat "nothing
   failed" as "the gate passed" — nothing ran.

## Rules

- Resolve the commands **once**, at the start of a run, and pass the resolved
  strings into a brief. An agent should never re-derive them mid-task.
- A brief names the actual command it wants run, never a purpose word. The agent
  receives `pnpm test src/foo.test.ts`, not "run the tests".
- When a repo has a command for a check the work needs and it fails, that is a
  gate failure. When the repo has no such command, that is a stated gap — the two
  must never be reported the same way.
- Offer to write a `## Commands` block when discovery was ambiguous and the run
  had to pick. The next run then starts at rung 1.
