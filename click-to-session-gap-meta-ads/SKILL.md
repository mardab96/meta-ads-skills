---
name: click-to-session-gap-meta-ads
description: Investigates differences between Meta website clicks, landing page views and site sessions using aligned metric scopes, redirect traces and collection diagnostics. Use when Meta clicks and site sessions disagree, when cost per click looks fine but nothing arrives, or before blaming creative for a traffic problem.
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

1. Compare website landing page views alongside eligible website clicks and sessions. Establish each metric definition before treating differences as loss; none is interchangeable with the others.
2. Confirm the same closed range, timezone, destination population and site-side session source/medium filter. Record the Meta click metric and reporting basis; exclude on-platform destinations from a website comparison. Sessions are not unique clicks: repeated clicks can share a session, and session source attribution can differ from event attribution.
3. Open the destination URL yourself and note redirects, parameter stripping and load behaviour.
4. Check whether required attribution parameters survive each redirect and whether an allowed first-party mechanism captured them earlier. Parameter loss can cause source misclassification; it does not prove that sessions were recorded. Check consent, tag loading and source classification separately.

## Analysis workflow

1. Lay out four numbers: link clicks, landing page views, site sessions from that source, and site sessions total.
2. Compute landing page views over eligible website clicks, and source-filtered sessions over landing page views. Name the denominator used; use a matching outbound-click metric when available. Report N/A for a zero or unavailable denominator. These are aggregate comparison ratios, not person-level funnel completion rates.
3. Treat a low landing-page-view ratio as a hypothesis to investigate: speed, abandonment, in-app browser behaviour, destination mismatch, consent and missing or delayed Meta measurement can all contribute. Verify actual loading and event delivery on representative devices before assigning a cause.
4. Investigate the session ratio using redirect traces, consent states, tag diagnostics, cross-domain setup and session counting/source rules. A high or low ratio alone cannot isolate parameter loss, consent blocking or a tracking defect.
5. Check whether the gap is uniform or concentrated on one destination. A concentration narrows the investigation to that destination and its traffic mix; it does not establish the cause.
6. Rank the checks or fixes by corroborating evidence and business impact. If only aggregates are available, report competing hypotheses and the next distinguishing check rather than a confirmed cause.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule or proof of causation. Apply only after scope checks; recalibrate per account and include an inconclusive verdict where neither evidence nor rubric supports a diagnosis.

| Verdict | Criteria |
|---|---|
| No immediate anomaly in these ratios | Landing page views 80%+ of eligible website clicks [heuristic], and sessions 70%+ of landing page views |
| Investigate load and Meta measurement first | Landing page views under 70% of eligible website clicks; verify load and event collection before diagnosing |
| Investigate session measurement and attribution first | Landing page views 80%+ of eligible website clicks, but sessions under 50% of landing page views |

Redirect rule: record verified parameter loss and its affected source filter. Prioritize a repair when the parameter is required and was not captured earlier by an allowed mechanism. Retain usable total-session and load evidence; label affected source comparisons as unreliable.

Attribution rule: this skill explains the traffic step only. A healthy ratio does not establish conversion tracking or explain a lack of sales. Investigate downstream outcome collection and the landing page or offer separately.

## Output format

### Gap verdict

No immediate ratio anomaly, investigate load/Meta measurement, investigate session measurement/attribution, or inconclusive. Distinguish observed defects from hypotheses.

### Four-number ladder

| Metric and scope | Count | Comparison ratio (not a user funnel) |
|---|---:|---:|

### Destination check

| URL | Redirects | Parameter survives | Mobile load | Gap |
|---|---|---|---:|---:|

### Fix order

Prioritized checks or verified fixes, with evidence and the comparisons affected by each defect.

### Missing data

What could not be observed, and which ratio it leaves unreadable.

## Practical example

Link clicks 4,100, landing page views 3,780, sessions from that source 1,610. The first ratio is 92%, the second is 43%. The destination URL redirects from a campaign short link and drops its query string on the way. Output: investigate session measurement/attribution first; parameter stripping is a verified defect if no earlier allowed capture exists. Its contribution to the session gap needs a controlled redirect/tag check. These aggregates do not establish whether creative performance is sound.

## Guardrails

- Do not compare link clicks to sessions and call the difference loss.
- Do not blame creative for a gap that sits between click and load.
- Do not recommend tracking changes without opening the destination URL.
- Do not extend into landing page conversion quality. This skill ends when the visitor arrives.
- Do not bypass consent to make platform counts agree, or send identifiers without the required consent.
- Do not treat agreement between counts as proof that both systems are collecting correctly.

## Measurement reference

[Google Analytics session definitions](https://support.google.com/analytics/answer/9191807) explain session counting and session attribution. Record the corresponding current Meta metric definition with each export; do not treat clicks, landing page views and sessions as interchangeable units.
