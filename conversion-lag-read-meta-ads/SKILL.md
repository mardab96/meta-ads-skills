---
name: conversion-lag-read-meta-ads
description: Establishes how long a Meta Ads result keeps changing after the day it happened, so decisions are not made on numbers that are still filling in. Use when someone wants to judge yesterday, after a launch, or before any pause or budget cut based on recent days.
---

# When Today's Numbers Stop Moving - Meta Ads

## Use this skill when

The user is about to act on a number that is not finished yet.

Common user requests:

- "Yesterday was terrible, should I pause it?"
- "The new campaign is not working, it has been two days."
- "Why did last week's ROAS go up after I exported it?"
- "How long do I wait before judging this?"

## Required input

Minimum useful data:

- The same Meta Ads export pulled at least twice for an overlapping date range, at different times.
- If only one pull exists: a closed historical range of 30+ days at daily granularity.

Recommended additional data:

- Business-side timestamps for order or lead creation.
- Campaign objective and optimization event.
- Any long consideration cycle known to the business, such as a quote or approval step.

## Before analysis

1. Ask whether two pulls of the same range exist. Without them, lag is estimated from history and must be labelled as such.
2. Confirm the optimization event. A purchase lags differently from a lead, and a qualified lead differently again.
3. Ask the business how long its own cycle runs from click to recorded outcome.
4. Note the attribution window: a 7-day click window cannot be final before 7 days have passed, by construction.

## Analysis workflow

1. For each day in the overlap, compare the value at first pull against the value at the later pull.
2. Compute the fill curve: what share of the final number was visible after 1 day, 3 days, and 7 days.
3. Identify the day at which the curve flattens, meaning further waiting adds little.
4. Split by campaign type if the account mixes lead gen and purchase, or prospecting and retargeting.
5. Convert the curve into a waiting rule the user can apply without redoing the analysis.
6. Re-read any recent decision that was made inside the unfinished window.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Judge after 1-2 days | 80%+ of the final number is visible within 1 day [heuristic], typical of short-cycle ecommerce with 1-day click |
| Judge after 3-4 days | 50-80% visible at 1 day |
| Judge after 7+ days | Under 50% visible at 1 day, OR a 7-day click window is in use, OR the business cycle includes a human approval step |

Do-not-decide rule: no pause, no budget cut and no creative kill inside the window the curve says is unfinished. If a decision must be made sooner, make it on leading indicators such as cost per click, hook rate or landing page rate, and say explicitly that it is a leading-indicator call.

Launch rule: a new ad set is also inside its learning period, so early numbers are unfinished twice over. Do not read a launch through this skill alone; pair it with `learning-phase-check-meta-ads`.

## Output format

### Waiting rule

The number of days after which this account's results are stable enough to act on.

### Fill curve

| Days after the day | Share of final value visible |
|---:|---:|

### Decisions to revisit

| Decision | Date | Days of data at the time | Share visible | Would it still hold |
|---|---|---:|---:|---|

### Missing data

Whether the curve is measured from two pulls or estimated from history, and what that costs in confidence.

## Practical example

Two exports of the same fortnight, pulled 5 days apart, show that day-one numbers carry 46% of the eventual total and day-three carries 79%. A campaign paused on its second day at a 2.1 ROAS would have read 3.6 once filled. Output: waiting rule of 4 days, the pause is flagged for reversal, and cost per landing page view is proposed as the leading indicator for faster calls.

## Guardrails

- Do not present an estimated curve as a measured one.
- Do not apply a curve from one account or objective to another.
- Do not use lag as a reason to never decide. The output is a waiting rule with a number, not a delay.
- Do not confuse lag with overclaim. If the range is closed and the gap persists, that is `attribution-credit-check-meta-ads`.
