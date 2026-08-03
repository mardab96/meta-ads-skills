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

Required columns where available:

- campaign
- objective
- optimization event
- budget
- spend
- impressions
- frequency
- CPM
- clicks
- CTR
- conversions / results
- cost per result
- conversion value / ROAS
- product set (ecommerce)
- date

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

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate to the account and say which threshold you adjusted.

State assignment criteria - a state needs its evidence, not a hunch:

| State | Criteria |
|---|---|
| Healthy and scaling | CPA / ROAS within 15% of target across 14 and 30 day windows, 50+ conversions per week [heuristic], stable or improving trend, no concentration flag |
| Healthy but constrained | Performance at target but volume flat while budget is underspent, or spend concentrated in one product set / creative at 70%+ [heuristic] with clean signals - the ceiling is mix or offer, not the campaign |
| Unstable because of weak signals | Optimization event under ~50 conversions per week [heuristic], OR EMQ in the low band, OR dedup unverified while both sources fire - route to the Pixel / CAPI audit before structural conclusions |
| Misleading because conversion quality is weak | Meta-reported results at target but CRM qualification / revenue quality materially lower (for example, less than a third of reported leads qualify) - the campaign optimizes toward the wrong thing |
| Unclear because required data is missing | Fewer than 14 days of data, no optimization event stated, or no CPA / ROAS target provided - say what is missing instead of guessing |

Concentration flags:

- One product set or one creative absorbing 70%+ of spend [heuristic] is a flag: healthy if its own CPA / ROAS beats target, constraint if it merely matches account average.
- Spend concentration right after a promo ends is expected for 7-14 days; do not call it structural before that window closes.

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

### Missing data

Exports or fields that would firm up the state assignment, and which criterion each one unlocks.

## Practical example

User provides 45 days of Advantage+ sales campaign data. ROAS dropped 31%, but CPM stayed stable. Spend concentrated into one product set after a promotion ended. Pixel diagnostics are clean. Claude classifies the campaign as "healthy but constrained by product and offer mix," not "broken Advantage+." Recommended action: review product set performance, refresh creative for underrepresented products, and do not reset structure yet.

## Guardrails

- Do not assume Advantage+ is bad by default.
- Do not recommend manual rebuilds unless the signal benefit is clear.
- Do not recommend scaling without conversion quality or revenue quality evidence.
- Do not ignore Pixel / CAPI signal issues.
- Do not make campaign changes directly.
