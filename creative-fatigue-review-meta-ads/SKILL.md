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

For long ad-level CSVs, run `../scripts/fatigue_trend.py` to compute the per-concept trend comparison deterministically; Claude then does the concept grouping and the replacement angles.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Compare each concept against its own 30-day baseline, not against other concepts. Recalibrate to account volume and say which threshold you adjusted.

Status assignment (evidence to label):

| Status | Criteria |
|---|---|
| Winner | CPA at or below target, CTR within 20% of its own 30-day baseline, regardless of frequency [heuristic] |
| Tired winner | Previously at or below target CPA for 14+ days AND frequency up 50%+ vs its own baseline AND CTR down 30%+ vs baseline AND CPM roughly stable (within +/-15%, so it is not an auction story) [heuristic] |
| Watchlist | Meets 2 of the 3 tired-winner signals (frequency, CTR decline, CPA drift) but not all, or the decline is younger than 7 days [heuristic] |
| Replace | Tired-winner criteria met for 14+ days with no recovery after spend was stable [heuristic] |
| Kill candidate | Never reached within 20% of target CPA after spending 3x target CPA - that is not fatigue, it never worked [heuristic] |
| Insufficient data | Less than 3x target CPA in spend, or fewer than 10 conversions attributable to the concept in the window [heuristic] |

Disambiguation rules:

- CPM up while CTR is stable points at auction pressure, not fatigue. Route to a budget or auction review.
- CTR stable while CVR dropped points at the landing page or the offer, not the creative.
- A concept present in several ad sets is judged on its combined data; per-ad-set slices below the volume floor do not get their own verdict.

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

Input (60 days, 18 ads grouped into 3 of the 5 concepts shown; target CPA $40):

| Concept | Spend | Freq now / baseline | CTR now / baseline | CPM now / baseline | CPA now / baseline |
|---|---:|---|---|---|---|
| Testimonial | $6,200 | 6.2 / 4.8 | 1.9% / 2.1% | $14 / $13 | $38 / $36 |
| Before-after | $4,800 | 5.9 / 3.1 | 0.9% / 1.7% | $13 / $13 | $61 / $38 |
| Feature demo | $1,100 | 2.2 / 2.0 | 1.1% / 1.2% | $15 / $14 | $71 / $69 |

Filled output:

| Creative concept | Status | Evidence | Likely reason | Recommended action |
|---|---|---|---|---|
| Testimonial | Winner | CPA $38 vs $40 target; CTR within 10% of baseline despite frequency 6.2 | Still converting; frequency alone is not fatigue | Do not replace; monitor weekly |
| Before-after | Tired winner | Was at target 14+ days; frequency +90%, CTR -48%, CPM stable, CPA +61% | Fatigue: audience saw it out | Replace with 2 new hooks on the same proof mechanism |
| Feature demo | Kill candidate | Spent $1,100 = 27x target CPA per conversion; never within 20% of target | Never worked; not fatigue | Stop iterating on this concept |

The before-after verdict is fatigue because CPM stayed flat; had CPM risen 40% with CTR stable, the same CPA jump would be an auction story and the recommendation would be different.

## Guardrails

- Do not recommend replacing creative only because frequency is high.
- Do not call fatigue without trend evidence.
- Do not generate final ads unless brand voice, landing page, offer, and constraints are provided.
- Do not ignore conversion lag.
- Do not recommend campaign edits or budget changes.
