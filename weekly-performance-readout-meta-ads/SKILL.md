---
name: weekly-performance-readout-meta-ads
description: Creates a weekly Meta Ads performance readout from campaign, ad set, ad, placement, and change-log exports. Separates facts from hypotheses, explains likely drivers, lists next actions, approval requests, risks, and missing data. Use for client, founder, or internal weekly updates.
---

# Weekly Performance Readout - Meta Ads

## Use this skill when

The user needs a weekly Meta Ads update that is useful for decisions, not just reporting.

Common user requests:

- "Prepare this week's Meta Ads readout."
- "Summarize what changed for the client."
- "What should we do next week?"
- "Write a founder-friendly Meta Ads update."

## Required input

Minimum useful data:

- Current week campaign report.
- Previous week campaign report.
- Ad set report.
- Ad report.
- Notes on changes made during the week.
- Target CPA, ROAS, lead quality goal, or campaign KPI.

Recommended additional data:

- Placement breakdown.
- Creative fatigue review.
- Pixel / CAPI diagnostics if tracking is in question.
- CRM or sales quality notes.
- Known external events, promotions, seasonality, or tracking changes.

## Before analysis

1. Confirm audience: founder, client, internal team, or specialist.
2. Confirm the KPI that matters.
3. Confirm what changes were made during the week.
4. Check data maturity and conversion lag.
5. Keep facts, hypotheses, and recommendations separate.

## Analysis workflow

1. Compare current week to previous week.
2. Identify biggest changes in spend, conversions, CPA, ROAS, CTR, CPM, CPC, CVR, and frequency.
3. Attribute likely drivers with confidence:
   - creative
   - auction cost
   - tracking
   - landing page / offer
   - budget or structure
   - seasonality
   - insufficient data
4. Decide what to do next.
5. Identify what needs approval.
6. Identify what should not change yet.

For the week-over-week arithmetic on long exports, run `../scripts/wow_delta.py` - it computes the deltas and applies the noise band, so the readout starts from flagged rows instead of eyeballed ones.

## Decision rules

Every threshold is a starting heuristic; recalibrate to the account's volume and say which threshold you adjusted.

What earns a row in "What changed":

- A metric enters the table only if it moved more than +/-15% week over week AND rests on at least 30 conversions per week (or 1,000 clicks for pre-conversion metrics) [heuristic].
- Below 30 conversions per week, widen the noise band to +/-25% and compare against a 4-week average instead of last week alone [heuristic].
- A change that mirrors a known cause (budget change, promo start or end, tracking edit) is reported as that cause, with the driver marked at high confidence only when the timing matches.
- Spend changes are always reported regardless of the band - the reader owns the budget.

Confidence labels in the driver column:

- High: timing matches a logged change, and the metric pattern fits (for example, CPM up after budget up).
- Medium: pattern fits but no logged change explains it.
- Low: several drivers fit equally; say so and name the next check instead of picking one.

## Output format

### Executive summary

3-5 sentences for a non-specialist.

### What changed

| Metric / area | Change | Likely driver | Confidence |
|---|---|---|---|

### What we are doing next

Ordered action list.

### What needs approval

Budget, creative, tracking, landing page, or offer decisions.

### What we are not changing yet

Areas where action would be premature.

### Missing data

Data needed for a better decision.

## Practical example

Input (change log: budget +25% on Prospecting from Tuesday; target CPA $50):

| Metric | Last week | This week | Change | Volume base |
|---|---:|---:|---:|---|
| Spend | $4,000 | $5,000 | +25% | - |
| Conversions | 82 | 84 | +2% | 84 conv |
| CPA | $48.80 | $59.50 | +22% | 84 conv |
| CPM | $12.10 | $14.80 | +22% | - |
| CTR | 1.8% | 1.75% | -3% | 6,100 clicks |
| Frequency | 2.4 | 2.9 | +21% | - |

Filled "What changed" table (the noise-band rule applied - CTR does not get a row, it moved 3%):

| Metric / area | Change | Likely driver | Confidence |
|---|---|---|---|
| Spend | +25% | Planned budget increase Tuesday | High |
| CPA | +22% ($48.80 -> $59.50) | Auction cost from the budget step, not conversion loss: CPM +22% with CTR flat, conversions held | High |
| Frequency | 2.4 -> 2.9 | More budget into the same audience | Medium |

Executive summary states: conversions held at 84 while cost per result rose with the budget step; this is a price effect, not a demand or creative effect. Recommendation: hold 72h before judging the new budget level; do not roll back yet because volume held. Approval requested for two replacement creatives on the early-fatigue concept. Not changing: bids, structure, the fatigued concept (insufficient data to kill).

## Guardrails

- Do not over-explain normal noise.
- Do not hide uncertainty.
- Do not claim causality from correlation.
- Do not turn the readout into a sales pitch.
- Do not recommend live changes without an approval section.
