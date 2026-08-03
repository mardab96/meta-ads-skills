---
name: budget-reallocation-planner-meta-ads
description: Reviews Meta Ads campaign and ad set performance to decide where to add, hold, reduce, or pause budget. Uses CPA, ROAS, spend share, conversion volume, learning status, stability, recent changes, and business constraints. Use before scaling or reallocating budget.
---

# Budget Reallocation Planner - Meta Ads

## Use this skill when

The user wants to decide how to move Meta Ads budget without making emotional changes.

Common user requests:

- "Where should I move budget?"
- "Can we scale this campaign?"
- "What should we reduce before increasing spend?"
- "Build a budget reallocation plan."

## Required input

Minimum useful data:

- Campaign and ad set performance for last 14-30 days.
- Current budgets.
- Target CPA or ROAS.
- Conversion volume.
- Recent budget or campaign changes.

Recommended additional data:

- Learning status.
- Conversion lag window.
- Revenue or lead quality data.
- Business constraints such as max daily spend, inventory, geography, or offer limits.

Required columns where available:

- campaign
- ad set
- budget
- spend
- impressions
- clicks
- conversions / results
- cost per result
- conversion value / ROAS
- frequency
- learning status
- date

## Before analysis

1. Confirm the KPI that governs budget decisions.
2. Confirm maximum allowed change size.
3. Confirm whether conversion data is mature.
4. Check whether recent edits make the data unstable.
5. Avoid aggressive recommendations when volume is low.

## Analysis workflow

1. Classify campaigns and ad sets by performance and data maturity.
2. Identify:
   - scale candidates
   - hold candidates
   - reduce candidates
   - pause candidates
   - needs-more-data candidates
3. Check whether winners are stable or only recently lucky.
4. Check whether losers are true losers or still inside learning / lag.
5. Build a reallocation plan with monitoring and rollback triggers.

When the export is a long CSV, run `../scripts/classify_budget.py` to compute the classification table deterministically instead of estimating the arithmetic.

## Decision rules

Every threshold below is a starting heuristic, not a Meta rule. Recalibrate against the account's own history, and say which threshold you adjusted and why.

Classification criteria:

| Class | Criteria (all must hold) |
|---|---|
| Scale candidate | CPA at least 15% below target (or ROAS 15% above) sustained for 14+ days, with 30+ conversions in the window, learning complete, no major edit in the last 72h [heuristic] |
| Hold | Within +/-15% of target, or fewer than 30 conversions in the window regardless of CPA [heuristic] |
| Reduce candidate | CPA 25-50% above target with 30+ conversions, after the conversion lag window has closed [heuristic] |
| Pause candidate | Spend of 3x target CPA or more with zero conversions after the lag window, or CPA more than 2x target with 20+ conversions [heuristic] |
| Needs more data | Fewer than 30 conversions in the window, still in learning, or a major edit inside the last 72h |

Movement rules:

- Maximum change per step: +/-20% of the current budget [heuristic]. Larger jumps re-enter learning and make the next read ambiguous.
- One budget change per campaign per 72 hours. Wait at least one full conversion-lag window before judging the effect.
- Do not scale and restructure in the same step. One variable at a time.
- Rollback trigger: CPA more than 20% above target for 3 consecutive days after a change reverts the change [heuristic].
- If reported conversions and CRM quality disagree, rank on the CRM-verified number and label the Meta number as volume, not value.

## Output format

### Budget verdict

Short summary of whether to scale, hold, or clean up first.

### Recommendation table

| Campaign / ad set | Recommendation | Amount or % | Evidence | Monitoring trigger |
|---|---|---:|---|---|

### Reallocation plan

Step-by-step plan with order of changes.

### Rollback rules

When to revert or stop, with the numeric trigger for each change.

### Missing data

Exports or fields that would change confidence, and which classification they would firm up.

## Practical example

User provides 30 days of campaign data. Claude finds one campaign with CPA 24% below target for 21 days and stable conversion volume, two ad sets with spend but no conversions after enough data, and one new campaign still in learning. Output recommends a 15% budget increase on the stable winner, reducing two inefficient ad sets, and holding the new campaign until it has enough conversion volume.

## Guardrails

- Do not recommend large budget jumps by default.
- Do not change budgets directly.
- Do not pause campaigns without enough spend or conversion context.
- Do not ignore conversion lag.
- Do not recommend scale without quality or revenue context when available.
