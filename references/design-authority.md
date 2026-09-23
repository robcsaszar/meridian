# Design authority

How the audit finds what "correct" looks like for a repository's interface.
Nothing here assumes a particular design system, review skill, or framework —
a repo may have a full design language, a single tokens file, or nothing.

Referenced as `${CLAUDE_PLUGIN_ROOT}/references/design-authority.md`.

## The ladder

Walk it in order. Use every rung that answers; skip every rung that does not.

1. **Declared.** A `## Design` section in `AGENTS.md`, else `CONTEXT.md`. This is
   authoritative — the maintainer wrote it on purpose, and it overrides anything
   discovery would infer. It may name a document, a skill, or both:

   ```markdown
   ## Design

   | Purpose | Where |
   |---|---|
   | tokens and components | `DESIGN.md` |
   | copy and tone | `AGENTS.md` § Voice |
   | review checklist | skill: `interface` |
   ```

   A row naming `skill: <name>` means: read `.claude/skills/<name>/SKILL.md` and
   follow whatever review guidance it carries. That is how a repo plugs its own
   design skill into this audit without the plugin knowing anything about it.

2. **Discovered.** No declared block → look for what the repo happens to have:

   | Signal | What it supplies |
   |---|---|
   | `DESIGN.md` | tokens, components, tone |
   | a design-tokens file (`tokens.json`, `theme.ts`, a Tailwind config) | the token scale |
   | a Storybook or component-catalogue config | the component inventory |
   | a `## Voice`, `## Tone` or `## Copy` section in `AGENTS.md` / `CONTEXT.md` | copy rules |
   | a review-oriented skill under `.claude/skills/` | a checklist |

3. **Absent.** Nothing on either rung → **this repository declares no design
   authority.** Say so in the report and drop the checks that depended on one.

## The rule that matters

Never infer a design standard from the code and then audit the code against your
inference. An invented standard produces confident findings a maintainer cannot
act on, and in a findings table it is indistinguishable from a real one.

With no authority at all the audit still has work: **cross-surface consistency**
measures surfaces against each other, not against a standard. One component
boxed in three places and bare in three others is a finding in any repository,
declared design language or not.

## Reporting

The audit names the authority it used, per rung, or states
`Authority: none found — consistency only`. A reader must be able to tell which
checks ran from the report alone.
