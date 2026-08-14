---
name: click-to-session-gap-meta-ads
description: Explains why Meta reports more clicks than the website records sessions, and separates the part that is normal measurement difference from the part that is a broken landing experience. Use when Meta clicks and site sessions disagree, when cost per click looks fine but nothing arrives, or before blaming creative for a traffic problem.
---

# Where Clicks Go Missing - Meta Ads

## Use this skill when

Meta says people clicked and the website does not see them arrive.

Common user requests:

- "Meta says 4,000 clicks, GA4 says 1,700 sessions."
- "We pay for traffic that never lands."
- "Is our tracking broken or is the ad lying?"
- "Cost per click is great and nothing happens after."

## Required input

Minimum useful data:

- Meta Ads export with link clicks and landing page views, at campaign level.
- Site sessions for the same closed range, from GA4 or equivalent, filtered to the same source.
- The destination URL used in the ads.

Recommended additional data:

- Mobile page load time for that URL.
- Whether the ads use an in-app browser or open externally.
- Any redirect chain on the destination URL.
- Consent banner behaviour on first visit.

## Before analysis

1. Use Meta's landing page views, not link clicks, as the closest comparable figure. Comparing link clicks to sessions overstates the gap by design.
2. Confirm the site-side number is filtered to the same source and the same closed range.
3. Open the destination URL yourself and note redirects, parameter stripping and load behaviour.
4. Confirm the tracking parameter survives the redirect. If it does not, the sessions exist but arrive unattributed.

## Analysis workflow

1. Lay out four numbers: link clicks, landing page views, site sessions from that source, and site sessions total.
2. Compute two separate ratios: landing page views over link clicks, and sessions over landing page views.
3. Attribute the first ratio to abandonment before load, which is speed, weight and in-app browser behaviour.
4. Attribute the second ratio to measurement, which is parameter loss, consent blocking and cross-domain breaks.
5. Check whether the gap is uniform or concentrated on one destination. Concentrated points at the page, not the platform.
6. Name which of the two problems is bigger and therefore which fix comes first.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Normal difference | Landing page views 80%+ of link clicks [heuristic], and sessions 70%+ of landing page views |
| Load problem first | Landing page views under 70% of link clicks, regardless of the second ratio |
| Measurement problem first | Landing page views 80%+ of link clicks, but sessions under 50% of landing page views |

Redirect rule: if the destination URL redirects and the tracking parameter does not survive to the final address, stop and fix that first. Every ratio below it is unreadable until it is fixed.

Attribution rule: this skill explains the traffic step only. A healthy click-to-session ratio with no sales is a landing page or offer problem, and belongs outside this pack.

## Output format

### Gap verdict

Normal, load problem first, or measurement problem first.

### Four-number ladder

| Step | Count | Share of previous step |
|---|---:|---:|

### Destination check

| URL | Redirects | Parameter survives | Mobile load | Gap |
|---|---|---|---:|---:|

### Fix order

What to fix first, and what will stop being measurable until it is fixed.

### Missing data

What could not be observed, and which ratio it leaves unreadable.

## Practical example

Link clicks 4,100, landing page views 3,780, sessions from that source 1,610. The first ratio is healthy at 92%, the second is 43%. The destination URL redirects from a campaign short link and drops its query string on the way. Output: measurement problem first, redirect named as the cause, and a note that the creative is not the problem here despite the flat reported result.

## Guardrails

- Do not compare link clicks to sessions and call the difference loss.
- Do not blame creative for a gap that sits between click and load.
- Do not recommend tracking changes without opening the destination URL.
- Do not extend into landing page conversion quality. This skill ends when the visitor arrives.
