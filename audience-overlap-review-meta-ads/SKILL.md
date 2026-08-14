---
name: audience-overlap-review-meta-ads
description: Finds audiences bidding against each other, stale lists that no longer refresh, and exclusion gaps that let paid ads chase existing customers. Use when several ad sets target similar people, when costs rise without a creative change, or before adding another audience to a working account.
---

# Audiences Fighting Each Other - Meta Ads

## Use this skill when

The account has accumulated audiences and nobody has looked at how they interact.

Common user requests:

- "Costs went up and nothing changed."
- "Do my ad sets overlap?"
- "Are we paying to reach our own customers?"
- "Should I add another lookalike?"

## Required input

Minimum useful data:

- List of active ad sets with their audience definitions, inclusions and exclusions.
- Custom audience list with size and last-refresh behaviour.
- Meta Ads export with frequency and cost per result by ad set.

Recommended additional data:

- Audience overlap tool output for the main audiences.
- Customer list size in the CRM, against the custom audience size in Meta.
- Which audiences are rule-based and refresh themselves, and which were uploaded once.

## Before analysis

1. Separate audiences that refresh themselves from static uploads. A static list only ages.
2. Confirm which exclusions are actually applied at ad set level rather than assumed.
3. Note the account structure first: overlap inside a single campaign behaves differently from overlap across campaigns.
4. Check audience sizes against the business's own list sizes. A custom audience far smaller than the CRM list points at a match rate problem, not a targeting choice.

## Analysis workflow

1. Map every active ad set to its audience, its exclusions, and its spend.
2. Identify pairs likely to overlap: same lookalike source, nested percentages, interest sets on the same theme.
3. Check whether existing customers are excluded from prospecting. Where they are not, size how much prospecting spend is reaching them.
4. Check staleness: how long since each uploaded list was refreshed, and whether its size has moved.
5. Correlate rising frequency and rising cost per result with the overlapping pairs.
6. Produce a consolidation proposal, naming what merges and what gets excluded.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Clean | No prospecting ad set missing a customer exclusion, uploaded lists refreshed within roughly 30 days [heuristic], no overlapping pair above roughly 20% |
| Tidy up | One or two overlapping pairs above 20%, OR uploaded lists between 30 and 90 days old |
| Consolidate now | Overlapping pairs above roughly 30%, OR prospecting running without customer exclusion, OR uploaded lists older than 90 days still in active use |

Nested lookalike rule: a 1% lookalike sits inside a 5% built from the same source, so running both without exclusion is bidding against yourself. Either exclude the smaller from the larger, or run one.

Consolidation caution: merging ad sets restarts learning. Where the account is already thin on volume, say what the restart costs before recommending the merge, and hand the volume question to `learning-phase-check-meta-ads`.

## Output format

### Overlap verdict

Clean, tidy up, or consolidate now.

### Audience map

| Ad set | Audience | Exclusions | Spend | Frequency | Cost per result |
|---|---|---|---:|---:|---:|

### Overlapping pairs

| Pair | Overlap | Evidence | Proposed fix |
|---|---:|---|---|

### Staleness

| Audience | Last refresh | Size now | Size at upload | Action |
|---|---|---:|---:|---|

### Missing data

What could not be checked without the overlap tool or CRM sizes.

## Practical example

Five ad sets, three built on 1%, 3% and 5% lookalikes from the same purchaser seed, none excluding the others. Frequency has climbed and cost per result with it, while creative has not changed. Purchasers are not excluded from prospecting. Output: consolidate now, keep the 5% with the 1% excluded, add the purchaser exclusion, and a note that the merge restarts learning on roughly 40% of account spend.

## Guardrails

- Do not claim an overlap percentage without the overlap tool. Infer carefully and label it as inference.
- Do not recommend merging without naming the learning cost.
- Do not treat a small custom audience as a targeting decision. Check match rate first.
- Do not exclude customers from retargeting by reflex. Some businesses sell to them again on purpose.
