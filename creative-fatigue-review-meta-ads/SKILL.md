---
name: creative-fatigue-review-meta-ads
description: Reviews Meta Ads ad-level and creative-level exports to identify likely creative fatigue, tired winners, weak concepts, and replacement angles. Use when CPA rises, CTR drops, frequency increases, CPM changes, or the user asks whether Meta Ads creatives need refresh.
---

# Creative Fatigue Review - Meta Ads

## Use this skill when

The user suspects Meta Ads performance dropped because creatives are tiring.

Common user requests:

- "Check if this is creative fatigue."
- "Which ads need refreshing?"
- "Frequency is up and CPA is worse."
- "Find tired winners and replacement angles."

## Required input

Minimum useful data:

- Ad-level export for last 7, 14, 30, and ideally 60 days.
- Creative names, IDs, or screenshots / descriptions.
- Campaign and ad set names.
- Target CPA or ROAS if available.

Recommended columns:

- ad name / ID
- creative name / ID
- campaign
- ad set
- date
- spend
- impressions
- reach
- frequency
- CPM
- link clicks
- CTR
- CPC
- conversions / results
- cost per result
- conversion value / ROAS
- comments, shares, saves, reactions where available

Optional:

- Landing page conversion rate.
- Comment samples.
- Offer or promotion notes.

## Before analysis

1. Confirm the business goal and optimization event.
2. Confirm whether the same creative exists in multiple ad sets or campaigns.
3. Ask whether any landing page, offer, tracking, or budget changes occurred.
4. Treat high frequency as a signal to inspect, not proof of fatigue.
5. Group creatives by concept, not only by ad ID.

## Analysis workflow

1. Normalize data by ad, creative, campaign, and time window.
2. Group ads by creative concept:
   - message / promise
   - format
   - hook
   - offer
   - audience angle
3. Compare frequency, CTR, CPM, CPC, CVR, CPA, spend, and conversion trend.
4. Identify:
   - tired winners
   - current winners
   - never-worked ads
   - insufficient data ads
   - potential auction / CPM issues
   - potential landing page / offer issues
5. Recommend replacement angles based on prior winners and current objections.

## Output format

### Fatigue verdict

Short verdict with confidence level.

### Creative table

| Creative concept | Status | Evidence | Likely reason | Recommended action |
|---|---|---|---|---|

Status values:

- winner
- tired winner
- watchlist
- replace
- kill candidate
- insufficient data

### Replacement angles

3-7 new creative angles, each tied to the evidence.

### Missing data

Fields or exports needed for better confidence.

## Practical example

User provides 60 days of ad-level exports. Claude groups 18 ads into 5 concepts. One testimonial concept still has stable CPA despite frequency 6.2, so it is labeled "winner, do not replace yet." A before-after creative has frequency up, CTR down 48%, CPM stable, and CPA up 61%, so it is labeled "tired winner." A third concept had weak CPA from launch, so it is not called fatigue. Output recommends replacing the tired winner with two new hooks using the same proof mechanism.

## Guardrails

- Do not recommend replacing creative only because frequency is high.
- Do not call fatigue without trend evidence.
- Do not generate final ads unless brand voice, landing page, offer, and constraints are provided.
- Do not ignore conversion lag.
- Do not recommend campaign edits or budget changes.
