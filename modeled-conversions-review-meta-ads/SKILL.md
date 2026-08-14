---
name: modeled-conversions-review-meta-ads
description: Separates conversions Meta actually observed from conversions Meta statistically modeled, and states how much of a reported result rests on estimation. Use before scaling, when reported results look smooth compared to the backend, or when small campaigns report suspiciously stable performance.
---

# Which Sales Meta Guessed - Meta Ads

## Use this skill when

The user is about to make a budget decision on a number that may be partly estimated.

Common user requests:

- "How much of this is real?"
- "Why is Meta so confident on a tiny campaign?"
- "Our backend shows lumpy sales, Meta shows a smooth line."
- "Can I trust this at this spend level?"

## Required input

Minimum useful data:

- Meta Ads export at campaign or ad set level, with conversions and spend.
- The attribution setting on that export.
- Business-recorded conversions for the same closed range.

Recommended additional data:

- Daily breakdown rather than a single total.
- Any Meta notice in Events Manager about modeled or estimated results.
- Consent-banner status and share of traffic that declines tracking, if known.

## Before analysis

1. Establish that modeling exists in this account at all: it appears where observed signal is incomplete, most visibly after iOS and consent losses.
2. Confirm the date range is closed.
3. Ask what the business can verify independently. Modeling is only a problem when nothing else can check it.
4. Note that Meta does not label every modeled conversion in the interface. Absence of a label is not evidence of absence.

## Analysis workflow

1. Compare Meta's daily conversion series with the business's daily series over the same closed range.
2. Look at the shape, not just the total: modeled series tend to be smoother, with fewer zero-days than a small real business produces.
3. Compute the ratio of Meta conversions to business conversions per day, and its spread. A stable ratio suggests scaling of a real signal; a ratio that only holds on the total suggests smoothing.
4. Check volume per ad set per week against the level where estimation matters most: low-volume ad sets carry the highest modeled share.
5. Flag any campaign where the decision would flip if the modeled portion were removed.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Mostly observed | Daily ratio to business data stays within roughly plus or minus 30% of its own median [heuristic], and the account has 50+ conversions per week per ad set |
| Partly modeled, decide with care | Ratio spread wider than that, OR 20-50 conversions per week per ad set, OR consent decline rate above roughly 30% |
| Treat as an estimate | Under roughly 20 conversions per week per ad set, OR the business has no independent count, OR Meta shows zero zero-days where the backend shows several |

Small-campaign rule: below roughly 20 weekly conversions [heuristic], report performance as a range, not a point. A single point number at that volume implies precision the data does not have.

Decision-flip rule: if removing the unverified portion changes a scale, hold or pause decision, that campaign is reported as blocked on verification, regardless of its verdict.

## Output format

### Confidence verdict

Mostly observed, partly modeled, or treat as an estimate.

### Series comparison

| Day | Meta conversions | Business conversions | Ratio |
|---|---:|---:|---:|

### Campaigns whose decision depends on the unverified portion

| Campaign | Reported | Verified floor | Decision at reported | Decision at floor |
|---|---:|---:|---|---|

### Missing data

What could not be separated, and why.

## Practical example

An ad set at 18 conversions per week reports a steady 2.9 ROAS every week for a month. The shop backend shows three weeks with sales and one with none. Output: treat as an estimate, report the ad set as a range rather than a point, and hold the proposed budget increase until either volume rises above the learning threshold or a second source confirms the flat weeks.

## Guardrails

- Do not claim a specific percentage of conversions is modeled. Meta does not expose that per campaign.
- Do not treat smoothness alone as proof. State it as one indicator among several.
- Do not tell the user modeling is wrong. It is a reasonable estimate under signal loss; the point is what to bet on it.
- Do not use this skill to explain a gap against the CRM. That is `attribution-credit-check-meta-ads`.
