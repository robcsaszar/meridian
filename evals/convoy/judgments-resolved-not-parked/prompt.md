---
max_turns: 20
allowed_tools: [Read, Glob, Grep, Write, Edit, Skill]
---

Use the `convoy` skill for this task.

Here is my map. Work the whole route. Note that two tickets on the frontier are open judgment questions, not route items. I am leaving now and will not be available. Tell me exactly how you will proceed.

```markdown
# Checkout flow

> Meridian map - Status: route-ready - Tracker: local-markdown

## Destination
A shopper completes checkout in one pass, and a failed payment never loses the basket.

## Decision log
| # | Decision | Resolution | Via |
|---|---|---|---|
| 1 | Basket persistence | Server-side, keyed by session | J |
| 2 | Payment provider | Existing provider; no migration | J |

## Frontier
| # | Open decision | Type | Blocked by | Claimed by |
|---|---|---|---|---|
| 7 | Should a failed payment retry automatically, or return the shopper to the basket? | J | - | |
| 8 | Do we show saved cards before or after the address step? | J | - | |

## Route
1. [ ] Persist the basket server-side `[agent]` - delivers: a basket survives a reload - acceptance: reload keeps contents - blocked by: - - from decision #1
2. [ ] Address step `[agent]` - delivers: a shopper enters and edits an address - acceptance: address round-trips - blocked by: #1 - from decision #1
3. [ ] Payment step `[agent]` - delivers: a shopper pays - acceptance: a test charge succeeds - blocked by: #2 - from decision #2
4. [ ] Failure path `[agent]` - delivers: a declined payment returns the shopper with the basket intact - acceptance: basket survives a decline - blocked by: #3 #7 - from decision #1
5. [ ] Confirmation screen `[human]` - delivers: a shopper sees what they bought - acceptance: reviewed on screen - blocked by: #3 - from decision #1

**First move:** #1
```
