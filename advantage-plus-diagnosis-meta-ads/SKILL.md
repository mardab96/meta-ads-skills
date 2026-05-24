---
name: advantage-plus-diagnosis-meta-ads
description: Diagnoses Meta Advantage+ campaigns using exports for campaign performance, ad sets, creatives, product sets, placements, catalog performance, signal quality, and optimization events. Use when Advantage+ performance drops, scales poorly, concentrates spend strangely, or lacks clear visibility.
---

# Advantage+ Diagnosis - Meta Ads

## Use this skill when

The user wants to diagnose an Advantage+ sales, app, or leads campaign without assuming automation itself is the problem.

Common user requests:

- "Why is this Advantage+ campaign unstable?"
- "Should we scale this Advantage+ campaign?"
- "Advantage+ is spending but lead quality is poor."
- "Diagnose this Advantage+ sales campaign."

## Required input

Minimum useful data:

- Campaign report for last 7, 14, 30, and 60 days.
- Ad / creative performance export.
- Optimization event and campaign objective.
- Budget and recent budget changes.
- Conversion volume and CPA / ROAS.

Recommended additional data:

- Product set or catalog performance for ecommerce.
- Placement breakdown.
- Platform breakdown.
- Pixel / Conversions API diagnostics.
- CRM quality notes for lead-gen.
- Notes on offer, promo, or landing page changes.

## Before analysis

1. Confirm the Advantage+ campaign type and objective.
2. Confirm whether the optimized event is the real business goal.
3. Confirm if the campaign has enough conversion volume to judge.
4. Ask whether conversion quality differs from Meta-reported result quality.
5. Check tracking and signal quality before recommending structural changes.

## Analysis workflow

1. Review spend, conversion volume, CPA, ROAS, CTR, CPM, CPC, frequency, and CVR across time windows.
2. Check if performance change comes from auction cost, conversion rate, creative fatigue, signal quality, or product mix.
3. Review spend concentration across ads, creatives, placements, and product sets where available.
4. Check whether the campaign is learning from the right event.
5. Classify campaign state:
   - healthy and scaling
   - healthy but constrained
   - unstable because of weak signals
   - misleading because conversion quality is weak
   - unclear because required data is missing
6. Produce a cautious action plan.

## Output format

### Campaign state

One of the five states above, with confidence level.

### Evidence table

| Signal | Finding | Implication | Confidence |
|---|---|---|---|

### Recommended next checks

Ordered list of diagnostics.

### Action plan

Safe actions for review, with monitoring window and rollback trigger.

## Practical example

User provides 45 days of Advantage+ sales campaign data. ROAS dropped 31%, but CPM stayed stable. Spend concentrated into one product set after a promotion ended. Pixel diagnostics are clean. Claude classifies the campaign as "healthy but constrained by product and offer mix," not "broken Advantage+." Recommended action: review product set performance, refresh creative for underrepresented products, and do not reset structure yet.

## Guardrails

- Do not assume Advantage+ is bad by default.
- Do not recommend manual rebuilds unless the signal benefit is clear.
- Do not recommend scaling without conversion quality or revenue quality evidence.
- Do not ignore Pixel / CAPI signal issues.
- Do not make campaign changes directly.
