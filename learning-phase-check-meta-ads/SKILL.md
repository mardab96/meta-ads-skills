---
name: learning-phase-check-meta-ads
description: Checks whether an account's structure allows any ad set to accumulate enough weekly conversions to leave learning, and identifies the fragmentation and edit habits that keep resetting it. Use when ad sets sit in learning limited, after a restructure, or before splitting a working ad set further.
---

# Why Nothing Leaves Learning - Meta Ads

## Use this skill when

Ad sets never stabilise and the account keeps being adjusted in ways that restart them.

Common user requests:

- "Everything says learning limited."
- "Should I split this ad set?"
- "Why does performance reset every time I touch it?"
- "How many ad sets should I run on this budget?"

## Required input

Minimum useful data:

- Active ad sets with budget, optimization event and current delivery status.
- Weekly conversions per ad set for the optimization event.
- Total account budget for the period.

Recommended additional data:

- Edit history, especially budget and targeting changes.
- Campaign budget structure, whether budget sits at campaign or ad set level.
- The conversion lag for this account, since it changes what a week actually contains.

## Before analysis

1. Read the optimization event per ad set. Different events across ad sets means they are not comparable.
2. Compute weekly conversions per ad set, not per campaign. Learning happens at ad set level.
3. Check the account's conversion lag first. Where results fill in over four days, a week holds less finished signal than it appears to.
4. Note recent edits. A restart explains a reading better than any structural theory.

## Analysis workflow

1. For each ad set, put weekly conversions next to the level needed to exit learning.
2. Compute how many ad sets the account budget can actually support at that level, and compare with how many are running.
3. Where more ad sets run than the budget supports, name the excess as the structural cause.
4. Review the edit pattern: how often changes are made that reset learning, and whether they are made inside the learning window.
5. Propose a consolidation that gets the largest number of ad sets above the threshold, naming what is merged and what is turned off.
6. State the cost of the consolidation, which is a deliberate restart across the merged ad sets.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Structure supports learning | Most active ad sets at roughly 50+ optimization events per week [heuristic, this is the commonly cited exit level], and no reset-triggering edit inside the last week |
| Thin but workable | Ad sets at 25-50 per week, OR one reset-triggering edit in the last week |
| Structure cannot support learning | Most ad sets under 25 per week, OR the budget cannot fund the number of ad sets at the threshold, OR edits reset learning more than once a week |

Split rule: never recommend splitting a working ad set that is only just clearing the threshold. The split halves the signal and both halves fall back into learning.

Deeper-event rule: where an ad set cannot reach the threshold on a deep event such as qualified lead or purchase, the choice is a shallower event with enough volume or a consolidated structure. Name the tradeoff rather than recommending patience.

Edit rule: significant budget and targeting changes restart learning. Where the account edits weekly, no structural change will help until the edit habit changes, and that is the first recommendation.

## Output format

### Structure verdict

Supports learning, thin but workable, or cannot support learning.

### Ad set table

| Ad set | Budget | Optimization event | Weekly events | Status | Above threshold |
|---|---:|---|---:|---|---|

### Capacity

How many ad sets this budget can fund above the threshold, against how many are running.

### Consolidation proposal

| Merge or stop | Ad sets | Expected weekly events after | Restart cost |
|---|---|---:|---|

### Missing data

What was not available, particularly edit history.

## Practical example

Eleven ad sets on a budget that supports four at the threshold. Nine sit in learning limited, weekly events range from 6 to 22, and budgets were edited three times in the last week. Output: structure cannot support learning, first recommendation is to stop editing inside the window rather than to restructure, then a merge to four ad sets with the restart cost named against the two ad sets currently closest to stable.

## Guardrails

- Do not present the exit threshold as an exact Meta rule. It is a widely used figure, not a published guarantee.
- Do not recommend a split for an ad set near the threshold.
- Do not blame structure where the real cause is weekly editing.
- Do not read learning status without checking conversion lag first.
- Do not recommend a shallower optimization event without saying what it costs in lead quality.
