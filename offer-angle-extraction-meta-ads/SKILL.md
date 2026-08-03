---
name: offer-angle-extraction-meta-ads
description: Extracts offer, pain, promise, proof, audience, mechanism, CTA, and creative angle from Meta Ads copy and creative descriptions, then compares performance by hypothesis. Use when the user wants to learn why ads won or failed, not just which ad had lower CPA.
---

# Offer and Angle Extraction - Meta Ads

## Use this skill when

The user wants to turn Meta Ads performance into learning about messaging, offer, and customer objections.

Common user requests:

- "What angles are we testing?"
- "Which offer is working?"
- "Why did this ad win?"
- "Extract hypotheses from these ads."

## Required input

Minimum useful data:

- Ad copy.
- Creative screenshots or text descriptions.
- Ad-level performance.
- Landing page URL or summary.
- Campaign objective and optimization event.

Recommended columns:

- ad name / ID
- campaign
- ad set
- primary text
- headline
- description
- CTA
- creative concept / screenshot description
- spend
- impressions
- CTR
- conversions / results
- cost per result
- conversion value / ROAS

Optional:

- Comment samples.
- Sales or lead quality notes.
- Customer persona notes.

## Before analysis

1. Confirm the business goal and audience.
2. Ask whether ads map to planned hypotheses or were created ad hoc.
3. Do not infer customer intent from copy alone if performance data is missing.
4. Group by angle, not only by creative format.
5. Separate offer angle from creative execution.

## Analysis workflow

1. Extract from each ad:
   - audience
   - pain
   - promise
   - proof
   - mechanism
   - offer
   - CTA
   - objection handled
2. Group ads into angle families.
3. Compare spend, CTR, CVR, CPA, ROAS, and conversion volume by angle.
4. Identify winning and losing hypotheses.
5. Suggest next tests based on what the evidence supports.

## Decision rules

Every threshold is a starting heuristic; recalibrate to the account and say which threshold you adjusted.

Verdict floors - an angle family gets a verdict only above these:

- At least 3x target CPA in spend AND 10+ conversions across the family [heuristic]. Below that, the verdict column says "insufficient data", not a lean.
- "Winner" requires the family to beat the account's blended CPA / ROAS by 20%+ at those floors [heuristic]. Within +/-20% is "comparable", which is also a finding.
- CTR-only winners are labeled "attention winner, conversion unproven" - never just "winner".

Confounded comparison rule:

- If an angle family runs only in one audience or one campaign type while others run elsewhere, the comparison is confounded. Say so, cap confidence at low, and recommend the isolating test instead of a verdict.
- When lead quality notes exist, a family can lose on CPA and still win on qualified CPA; state both numbers and rank on the qualified one.

## Output format

### Angle map

| Angle | Ads | Promise | Evidence | Verdict |
|---|---|---|---|---|

### Hypotheses

What the account appears to be testing.

### Next tests

3-7 specific tests tied to evidence.

### Landing page implications

What the landing page should clarify or support.

### Missing data

What blocks a verdict per family (spend below floor, no conversion split, no quality notes), stated per angle.

## Practical example

User provides 22 ads. Claude extracts five angle families: price, speed, social proof, pain avoidance, and control. The speed angle has the highest CTR but weak CVR. The control angle has lower CTR but best CPA and lead quality notes. Output recommends developing more control-based creatives and adjusting the landing page to explain the mechanism earlier.

## Guardrails

- Do not claim an angle won without spend and conversion context.
- Do not confuse creative format with strategic angle.
- Do not invent persona language not present in data or user context.
- Do not recommend final new ads without brand constraints.
- Do not ignore lead quality if provided.
