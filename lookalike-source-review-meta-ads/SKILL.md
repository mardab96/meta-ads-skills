---
name: lookalike-source-review-meta-ads
description: Inspects what a lookalike audience is actually built from, because the model copies the seed and a weak seed produces a weak audience no bidding change can fix. Use before creating a lookalike, when lookalike performance decays, or when several lookalikes behave identically.
---

# What Your Lookalike Is Copying - Meta Ads

## Use this skill when

A lookalike underperforms and the account keeps adjusting everything except its source.

Common user requests:

- "Our lookalikes stopped working."
- "Which seed should I use?"
- "All my lookalikes perform the same, why?"
- "Should I go 1% or 5%?"

## Required input

Minimum useful data:

- The seed audience for each active lookalike: its type, its size, and how it is defined.
- Performance by lookalike ad set from the Meta Ads export.
- When each seed was last refreshed.

Recommended additional data:

- What the seed members are worth to the business, such as average order value or qualification rate.
- Whether the seed is rule-based or a static upload.
- Country and the lookalike percentage in use.

## Before analysis

1. Read the seed definition, not the lookalike name. Names lie and outlive the thing they describe.
2. Confirm seed size against the level where the model has enough to copy.
3. Ask what the business would want more of. A seed of all buyers and a seed of high-value repeat buyers produce different audiences.
4. Check whether the seed refreshes. A static seed teaches the model about last year.

## Analysis workflow

1. Tabulate every lookalike with its seed, seed size, seed age, percentage and country.
2. Identify seeds that are too small, too old, too broad, or too similar to one another.
3. Check whether several lookalikes share one seed. If they do, they are variations on a single hypothesis, and identical performance is the expected result, not a mystery.
4. Assess seed quality against business value rather than count: what share of the seed represents the outcome the business wants more of.
5. Propose a better seed where one exists in the data the business already holds.
6. Separate a seed problem from a delivery problem, so the recommendation lands in the right place.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Seed is sound | 1,000+ members from one country [heuristic, Meta's own floor is lower than what works], refreshed within 30 days, and the members represent the outcome the business wants |
| Seed is weak | 500-1,000 members, OR 30-90 days stale, OR the seed mixes valuable and low-value members without separation |
| Rebuild the seed | Under 500 members, OR older than 90 days, OR the seed is a raw list with no relationship to business value |

Shared-seed rule: lookalikes built from the same seed at different percentages are not independent tests. Treat them as one audience decision and read them together.

Value-over-volume rule: a smaller seed of high-value customers usually beats a larger seed of everyone, but only above the size floor. Below the floor, volume wins because the model needs something to copy.

## Output format

### Seed verdict per lookalike

Sound, weak, or rebuild.

### Seed table

| Lookalike | Seed | Seed size | Seed age | Percentage | Cost per result |
|---|---|---:|---|---:|---:|

### Proposed seeds

| Proposed seed | Where it comes from | Expected size | Why it is better |
|---|---|---:|---|

### Missing data

What was not visible about seed composition, and what it blocks.

## Practical example

Three lookalikes at 1%, 2% and 5%, all from a 340-member purchaser list uploaded in March and never refreshed. Performance is identical across all three, which is the expected result for one shared seed below the size floor. Output: rebuild the seed from the last 180 days of purchasers, drop to a single lookalike until the seed clears 1,000 members, and stop reading the three ad sets as three tests.

## Guardrails

- Do not judge a lookalike without reading its seed.
- Do not recommend a percentage change as a fix for a bad seed.
- Do not treat lookalikes from one seed as separate experiments.
- Do not propose a seed the business cannot actually produce from data it holds.
