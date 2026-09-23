---
max_turns: 20
allowed_tools: [Read, Glob, Grep, Write, Edit, Skill]
---

Use the `meridian` skill for this task.

Here is my map. Its frontier is empty and there is no Route section yet. Take it from here.

```markdown
# Lobby intake seam

> Meridian map - Status: charting - Tracker: local-markdown

## Destination
A visitor signing in at the lobby kiosk is recorded once, and reception sees them within five seconds.

## Bearings
- **Brought as:** feature
- **Appetite:** a fortnight
- **For:** reception staff; not the security desk

## Decision log
| # | Decision | Resolution | Via |
|---|---|---|---|
| 1 | Where intake is recorded | One POST to the intake handler; the kiosk holds no state | J |
| 2 | How reception is notified | Server-sent events on the existing reception channel | J |
| 3 | What a duplicate sign-in does | Second sign-in within 10 minutes updates the first record rather than creating one | J |
| 4 | Badge printing | Out of scope; reception prints manually as today | J |

## Frontier
| # | Open decision | Type | Blocked by | Claimed by |
|---|---|---|---|---|

## Fog

## Ruled out
- Kiosk-side queueing - killed because: the kiosk cannot be trusted to retry, and a lost queue is a lost visitor.
- Polling reception every 30s - killed because: it misses the five-second target in the Destination.

## Route

**First move:** [not yet charted]
```
