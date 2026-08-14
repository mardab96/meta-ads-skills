---
name: ios-reporting-gap-meta-ads
description: Estimates how much of an account's audience is reporting back incompletely because of app tracking permission and event limits, and states which decisions that blind spot can and cannot support. Use when platform numbers undercount known sales, when iOS-heavy audiences underperform on paper, or before setting event priority.
---

# What iPhone Users Are Not Telling You - Meta Ads

## Use this skill when

Part of the audience converts but does not report back, and the account is being judged as if it did.

Common user requests:

- "iOS looks terrible, should I exclude it?"
- "We know these sales happened, Meta does not show them."
- "How do I set my event priority?"
- "Is our iOS performance real or a reporting artifact?"

## Required input

Minimum useful data:

- Meta Ads export broken down by platform or device.
- Business-recorded conversions for the same closed range, with device if available.
- The current event priority list from Events Manager.

Recommended additional data:

- Share of traffic by operating system from the site analytics.
- Conversions API status.
- Consent banner behaviour on iOS.

## Before analysis

1. Confirm the export is genuinely split by device, not by placement.
2. Confirm the business can attribute at least some of its own sales to device. Where it cannot, the gap is bounded, not measured.
3. Read the current event priority order before proposing changes to it.
4. Note the ceiling: a limited number of events per domain can be prioritised, so the list is a budget, not a wish list.

## Analysis workflow

1. Compare the platform mix Meta reports against the platform mix the site sees.
2. Where site traffic is more iOS-heavy than Meta's reported conversions, size the reporting shortfall.
3. Check whether iOS underperformance is uniform across campaigns or concentrated. Concentrated means a real campaign problem underneath the reporting one.
4. Review the event priority list against what the business values, and against which events actually carry volume.
5. Separate three things explicitly: fewer conversions, fewer reported conversions, and worse-optimised delivery caused by weaker signal.
6. State which decisions the remaining data can still support.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Reporting gap is small | Reported iOS share within roughly 10 percentage points of site iOS share [heuristic], and Conversions API is live |
| Reporting gap is material | Difference of 10-25 points, OR Conversions API absent, OR consent decline on iOS above roughly 30% |
| Cannot judge iOS on platform data | Difference above 25 points, OR the business cannot attribute any sales to device |

Exclusion rule: never recommend excluding iOS on reported performance alone. Exclusion removes the audience and the reporting problem at once, so it always looks like it worked. Recommend a holdout or a geo split instead.

Event priority rule: the priority list is ordered by business value, not by volume, with one exception. An event too rare to sustain learning at the top of the list starves optimisation, so where the top event runs below roughly 20 per week [heuristic], propose the next event down and say what that costs.

## Output format

### Blind spot verdict

Small, material, or cannot judge.

### Platform mix comparison

| Platform | Site share | Meta reported conversion share | Difference |
|---|---:|---:|---:|

### Event priority review

| Rank | Event | Weekly volume | Business value | Keep or move |
|---:|---|---:|---|---|

### What this data can still decide

The decisions that survive the blind spot, and the ones that do not.

### Missing data

What was not measurable, and what it would take to measure it.

## Practical example

Site analytics show 58% iOS traffic; Meta attributes 31% of conversions to iOS. Conversions API is not live. Two campaigns carry almost all of the shortfall, and both point at the same landing page. Output: material gap, no exclusion recommended, Conversions API named as the first fix, and the landing page flagged because a concentrated gap points at something real underneath the reporting loss.

## Guardrails

- Do not recommend excluding a platform to make reporting look better.
- Do not present the shortfall as a precise count of lost sales. It is a bounded estimate.
- Do not propose an event priority change without saying what volume it costs.
- Do not duplicate the signal quality audit. Event match quality and deduplication belong to `pixel-capi-signal-quality-audit-meta-ads`.
