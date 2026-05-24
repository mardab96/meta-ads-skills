---
name: placement-breakdown-review-meta-ads
description: Reviews Meta Ads placement, platform, and device breakdown exports to identify inefficient placements, creative-format mismatches, cheap traffic traps, and placement-specific next actions. Use when blended performance hides where results are coming from.
---

# Placement Breakdown Review - Meta Ads

## Use this skill when

The user wants to understand whether placements are helping or hurting Meta Ads performance.

Common user requests:

- "Review placement performance."
- "Is Audience Network wasting spend?"
- "Instagram Reels gets clicks but no conversions."
- "Should we exclude any placements?"

## Required input

Minimum useful data:

- Placement breakdown export.
- Campaign and ad set performance.
- Campaign objective and optimization event.
- Date range: ideally 14-30 days.

Recommended columns:

- campaign
- ad set
- placement
- platform
- device
- spend
- impressions
- reach
- frequency
- CPM
- clicks
- CTR
- CPC
- conversions / results
- cost per result
- conversion value / ROAS

Optional:

- Creative format per placement.
- Video retention or thumb-stop proxy metrics.
- Landing page conversion rate by placement.

## Before analysis

1. Confirm the objective and optimization event.
2. Confirm whether the same creative is used across placements.
3. Ask whether placement controls are manual or Advantage+ placements are active.
4. Check conversion volume before recommending exclusions.
5. Treat cheap clicks as suspicious until outcome quality is known.

## Analysis workflow

1. Aggregate performance by placement, platform, and device.
2. Compare spend share to conversion or value share.
3. Identify placements with high spend and weak outcomes.
4. Check if the issue may be creative-format mismatch.
5. Distinguish low-quality traffic from low-volume uncertainty.
6. Recommend monitor, adapt creative, test exclusion, or no action.

## Output format

### Placement verdict

One paragraph summary.

### Placement table

| Placement | Spend share | Outcome share | Issue | Recommended action | Confidence |
|---|---:|---:|---|---|---|

### Creative notes

Placement-specific creative adjustments.

### Missing data

What would improve confidence.

## Practical example

User provides placement breakdown. Claude finds Reels has 31% of spend, 45% of clicks, but only 9% of conversions. CPM is low, CTR is high, and landing page CVR is weak. Output recommends testing placement-specific creative and landing page review before excluding Reels, because the issue may be intent mismatch rather than placement quality alone.

## Guardrails

- Do not recommend excluding placements only on CTR or CPC.
- Do not optimize for cheap traffic.
- Do not generalize from tiny spend.
- Do not override Advantage+ placements without explaining the tradeoff.
- Do not make placement changes directly.
