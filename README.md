<p align="center"><img src=".github/meridian.png" width="400" alt="meridian banner"/></p>

# meridian

Planning skill charts your work. Diagnose the fog, diverge honestly, decide one question at a time. Dead ends stay on the chart.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![skills.sh](https://skills.sh/b/robcsaszar/meridian)](https://skills.sh/robcsaszar/meridian)

A skill that turns an idea, feature, bug, or open-ended brainstorm into a planned body of work — a durable map of decisions that a whole effort can steer by.

This skill follows the [Agent Skills specification](https://agentskills.io/specification) so it can be used by any skills-compatible agent.

## Installation

### npx skills
    npx skills add robcsaszar/meridian

### Marketplace
    /plugin marketplace add robcsaszar/meridian
    /plugin install robcsaszar-meridian@meridian

### Manually
Copy the `skills/meridian/` directory into your project's `.claude/skills/`.

## What it does

Bring it anything from a half-formed hunch to a well-understood feature. The skill first takes bearings: how clear is the destination? When the way is fogbound — no ideas, samey ideas, a constraint that feels unbreakable, a nagging sense you're solving the wrong problem — it runs a structured divergence pass where techniques are allowed to fail visibly and weak ideas die in the open, closing with one structural insight across everything generated. Once a direction survives, it converges: open decisions form a dependency-ordered frontier, each typed by what unblocks it — your judgment (an interview, one question at a time, always with a recommended answer), research (a subagent gathers evidence for your sign-off), or an experiment (a small spike whose outcome decides). Resolved decisions accrete into a plan artifact — the repo's issue tracker when it has one, a `plans/<slug>.md` file when it doesn't — with ruled-out paths kept on the chart, kill reasons and all.

The map is done when no open decisions remain. The skill then distills the decision log into a route: ordered work items with acceptance criteria, each traceable to the decision that shaped it. It never implements; it ends by naming the first move.

## License
[MIT](LICENSE) © Rob Csaszar
