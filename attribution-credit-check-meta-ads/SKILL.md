---
name: attribution-credit-check-meta-ads
description: Checks how much of Meta's reported conversion count survives a stricter attribution window, and separates sales Meta caused from sales it merely saw. Use when Meta's numbers do not match the CRM, the shop backend, or GA4, or before a scaling decision based on reported ROAS.
---

# Is Meta Taking Credit It Did Not Earn - Meta Ads

## Use this skill when

The user suspects Meta is reporting more conversions than the business can find anywhere else.

Common user requests:

- "Meta says 40 sales, Shopify says 22."
- "Should I trust this ROAS?"
- "Why does GA4 show half of what Meta shows?"
- "Our retargeting ROAS is 12 and revenue did not move."

## Required input

Minimum useful data:

- Meta Ads export with conversions and conversion value, at campaign level.
- The attribution setting currently applied to that export.
- Total business orders or leads for the same date range, from the shop backend or CRM.

Recommended additional data:

- The same Meta export re-pulled under a stricter window (1-day click).
- Split by campaign objective, and by prospecting versus retargeting.
- GA4 or another independent source, with its own attribution model named.

## Before analysis

1. Read the attribution setting off the export itself. Do not assume 7-day click / 1-day view.
2. Confirm the date range is closed. An open range mixes this skill with conversion lag; if the range ends within the last 7 days, say so and hand the lag question to `conversion-lag-read-meta-ads`.
3. Confirm what the business counts as a sale, and whether refunds are already removed.
4. Ask whether any campaign is retargeting people who were going to buy anyway. That is a real answer, not a dodge.

## Analysis workflow

1. Put three numbers side by side for the same closed range: Meta reported conversions, business-recorded conversions, and the independent source.
2. Compute the overclaim ratio: Meta reported divided by business recorded.
3. Re-pull or request the same range under 1-day click. Compute what share of the reported total survives.
4. Split the gap by campaign type. Prospecting and retargeting almost never overclaim at the same rate.
5. Name which part of the gap is explainable (cross-device, view-through, longer window) and which part is not.
6. State what the account looks like if you plan against the stricter number instead of the reported one.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account and say which one you moved.

| Verdict | Criteria |
|---|---|
| Reported number is usable | Meta within roughly 1.0-1.3x of business-recorded conversions [heuristic], and 1-day click retains 60%+ of the reported total |
| Plan against the stricter number | Meta at 1.3-2.0x business-recorded, OR 1-day click retains 35-60% |
| Do not scale on this number | Meta above 2.0x business-recorded, OR 1-day click retains under 35%, OR the business cannot produce its own count at all |

Retargeting rule: when a retargeting campaign shows a ROAS several times the account average and total revenue is flat, the default reading is credit reassignment, not incremental sales. Confirming it needs a holdout, which is `incrementality-test-design-meta-ads`, not this skill.

View-through rule: if view-through conversions are more than roughly 25% of the reported total [heuristic], report the click-only number as the primary figure and the full number as secondary.

## Output format

### Credit verdict

Usable, plan against stricter, or do not scale.

### Three-source comparison

| Source | Conversions | Value | Attribution model | Date range |
|---|---:|---:|---|---|

### Where the gap sits

| Campaign type | Reported | 1-day click | Retained % | Reading |
|---|---:|---:|---:|---|

### What changes if you plan against the stricter number

Which campaigns stay profitable, which do not, and which decision flips.

### Missing data

What could not be checked, and which verdict criterion it blocks.

## Practical example

Account reports 61 purchases at 4.2 ROAS. Shopify shows 34 orders in the same closed week. Under 1-day click Meta shows 29. The gap is concentrated in one retargeting campaign reporting 22 purchases, of which 4 survive 1-day click. Output: plan against the stricter number, treat the retargeting ROAS as reassigned credit until a holdout says otherwise, and re-read the prospecting campaigns, which retained 71% and look sound.

## Guardrails

- Do not call the gap fraud or a bug. Different windows measuring different things is the normal case.
- Do not conclude anything from an open date range. That is lag, not overclaim.
- Do not claim Meta and GA4 should match. They never will; the question is the size and the shape of the gap.
- Do not recommend turning off retargeting on this evidence alone. Recommend a holdout.
- Do not restate a modeled number as observed. If the export does not say, mark it unknown.
