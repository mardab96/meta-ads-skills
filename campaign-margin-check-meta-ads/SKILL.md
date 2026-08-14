---
name: campaign-margin-check-meta-ads
description: Rebuilds campaign performance on contribution margin instead of revenue, so a healthy ROAS that loses money is visible before budget follows it. Use when ROAS looks fine and the bank account does not, when product mix varies widely, or before scaling any campaign in a business with real unit costs.
---

# Which Campaigns Actually Make Money - Meta Ads

## Use this skill when

The reported return is good and the business is not getting richer.

Common user requests:

- "ROAS is 3 and we made nothing."
- "Which campaigns are actually profitable?"
- "Our best ROAS campaign sells our worst margin product."
- "What ROAS do we actually need?"

## Required input

Minimum useful data:

- Meta Ads export with spend and conversion value at campaign level.
- Cost of goods for the products sold, or an average contribution margin percentage.
- The date range, closed.

Recommended additional data:

- Product-level sales split by campaign, from the shop backend.
- Returns rate, payment fees, shipping cost and packaging cost.
- Discount and promotional codes active in the range.

## Before analysis

1. Establish what the business already knows about its own costs. Where the cost stack does not exist, this skill produces a break-even target rather than a margin figure, and says so.
2. Confirm whether the conversion value in the export is gross revenue, revenue after discount, or something else.
3. Confirm whether returns are already deducted anywhere.
4. Ask whether product mix differs by campaign. Where it does, an account-average margin will mislead at campaign level.

## Analysis workflow

1. Build the cost stack per order: cost of goods, discount, returns allowance, payment fee, shipping, packaging.
2. Compute contribution margin before ad spend, as an amount and as a share of revenue.
3. Compute break-even ROAS as one divided by that margin share, and state it as the target the account has to clear.
4. Recompute every campaign as margin after ad spend, not as ROAS.
5. Rank campaigns by margin contributed, not by ROAS. The order usually changes.
6. Flag any campaign above break-even ROAS but below zero margin after all costs, and say which cost line puts it there.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Profitable | Positive margin after ad spend, and ROAS at least 1.2x break-even ROAS [heuristic buffer for estimate error] |
| Marginal | Positive margin after ad spend but ROAS within 1.0-1.2x break-even |
| Losing money | ROAS below break-even ROAS, OR negative margin after ad spend |

Mix rule: where product mix differs materially between campaigns, an account-average margin is not good enough. Say so and ask for product-level sales by campaign rather than producing a confident wrong number.

Missing-cost rule: if the cost stack is incomplete, do not print a margin percentage. Print the break-even ROAS the account must clear and name the missing cost lines. A margin built on an assumed landed cost is worse than none, because someone will act on it.

## Output format

### Break-even ROAS

The number this account has to clear, and the cost stack it comes from.

### Campaigns by margin

| Campaign | Spend | Revenue | ROAS | Margin before ad spend | Margin after ad spend |
|---|---:|---:|---:|---:|---:|

### Rank change

Which campaigns move up or down when ranked by margin instead of ROAS.

### Missing cost lines

What was not available, and what it does to confidence.

## Practical example

Account average ROAS 3.1 against a break-even of 2.8, so it looks fine. Product-level data shows the top-ROAS campaign sells a bundle with a 22% margin, giving a break-even of 4.5 for that campaign alone. Output: that campaign is losing money at 3.4 ROAS, two mid-ROAS campaigns rank highest on margin, and the recommended budget move is the opposite of the one ROAS implied.

## Guardrails

- Do not print a margin number from an assumed cost. Ask, or give break-even instead.
- Do not apply an account-average margin to campaigns with different product mixes.
- Do not include fixed overhead. This is contribution margin, and mixing in fixed costs makes every campaign look worse than it is.
- Do not recommend pausing on one closed range alone where the range is short. Say how much data the call rests on.
