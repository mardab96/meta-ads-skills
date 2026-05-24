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

User provides weekly exports and change notes. CPA increased 18%, but conversion volume is within normal range. CPM increased 22% after a budget increase, while CTR stayed stable. One creative group shows early fatigue but not enough data to kill. Output explains that performance softened mainly from auction cost and budget change, recommends monitoring for 72 hours, requests approval for two replacement creatives, and does not recommend pausing the campaign.

## Guardrails

- Do not over-explain normal noise.
- Do not hide uncertainty.
- Do not claim causality from correlation.
- Do not turn the readout into a sales pitch.
- Do not recommend live changes without an approval section.
