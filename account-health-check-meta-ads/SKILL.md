---
name: account-health-check-meta-ads
description: Reviews Meta Ads exports to identify the highest-priority account issues across campaigns, ad sets, delivery, learning status, spend distribution, conversion volume, CPA, ROAS, and missing data. Use when opening an account, diagnosing broad performance decline, preparing an audit, or deciding what to inspect first.
---

# Account Health Check - Meta Ads

## Use this skill when

The user wants a fast but rigorous read on the overall health of a Meta Ads account.

Common user requests:

- "Audit this Meta Ads account."
- "What should I look at first?"
- "CPA is up across the account."
- "Give me a first-pass Meta Ads diagnosis."

## Required input

Ask for the narrowest set of exports needed for the requested scope.

Minimum useful data:

- Date range: ideally last 7, 14, and 30 days.
- Business goal: CPA, ROAS, lead quality, purchase volume, revenue, or another KPI.
- Optimization event for each campaign.
- Notes on major recent changes, promotions, tracking changes, or budget changes.

Recommended Meta Ads exports:

- Campaign performance report.
- Ad set performance report.
- Ad performance report.
- Placement breakdown.
- Platform breakdown.
- Country or region breakdown.
- Pixel / Events Manager diagnostics if available.

Required columns where available:

- campaign name / ID
- objective
- status
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
- purchase value / conversion value
- ROAS
- optimization event
- learning status
- budget
- date

## Before analysis

1. Confirm what conversion or result matters.
2. Confirm whether data is mature enough to judge, especially for purchase or offline events.
3. Ask whether any campaign, offer, tracking, landing page, or budget change happened inside the window.
4. Separate Meta-reported results from CRM or revenue quality if both are provided.
5. If key inputs are missing, continue with lower confidence and state what is missing.

## Analysis workflow

1. Normalize column names, dates, and currencies.
2. Compare account-level performance across 7, 14, and 30 day windows.
3. Rank campaigns by spend share and outcome contribution.
4. Identify campaigns or ad sets with high spend and weak outcome quality.
5. Check learning status, delivery status, and insufficient-volume patterns.
6. Compare CTR, CPM, CPC, CVR, CPA, ROAS, frequency, and conversion volume.
7. Separate likely issue type using the attribution tree in Decision rules.
8. Return the few issues worth human attention first.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate to account volume and say which threshold you adjusted.

Driver attribution tree - apply in order, stop at the first match:

1. Conversions dropped, clicks stable, AND a tag / landing page / consent change happened in the window -> tracking or signal quality. Verify before anything else.
2. Account below ~30 conversions in the last 30 days, or the delta rests on fewer than 10 conversions -> insufficient data. Do not attribute a driver; widen the window.
3. CPM up 20%+ while CTR is within 15% of baseline -> auction cost or budget change. Check recent budget moves and seasonality first.
4. CTR down 25%+ vs baseline while CPM is roughly stable, frequency rising -> creative fatigue. Route to the creative fatigue review. (The router threshold is deliberately looser than the fatigue verdict's 30%: routing sends something for inspection, the verdict needs stronger evidence.)
5. CVR down 25%+ while CTR and CPM are stable -> landing page or offer. Ask what changed on the page.
6. Spend share concentrated (one campaign holding 70%+ of spend) with weak outcome share -> budget allocation or structure. Route to reallocation or structure audit.
7. None of the above at material size -> normal noise. Say so instead of inventing a driver.

Materiality gate: a metric change only enters the priority table if it moved 15%+ vs baseline AND rests on at least 10 conversions or 500 clicks [heuristic]. Below that, list it under "What not to touch yet". Baseline here means the trailing 30-day window unless the user names another; the weekly readout skill uses higher floors (30 conversions / 1,000 clicks) because its window is one week, not thirty days.

### Vertical notes

- Ecommerce: judge on ROAS and product mix, expect purchase lag of 1-7 days; a post-promo ROAS drop with stable CPM is usually offer mix, not account health.
- Lead gen: Meta-reported leads are volume, not value; without a CRM qualification rate, cap confidence at medium for any "healthy" verdict.
- App: SKAN / AEM postbacks delay and aggregate; day-level attribution trees above do not apply cleanly below the privacy threshold.

## Output format

### Executive summary

One paragraph: account state, biggest risk, and next best diagnostic.

### Priority issues

| Priority | Area | Evidence | Likely issue | Recommended next check | Confidence |
|---|---|---|---|---|---|

### What not to touch yet

List areas where changes would be premature.

### Missing data

List the exact exports or fields that would improve confidence.

### Next action queue

3-7 review tasks, ordered by expected impact.

## Practical example

User provides 30 days of campaign and ad set exports. Spend is concentrated in two campaigns. Account CPA rose 42%. Claude finds that one campaign has stable CPM and CTR but CVR dropped after a landing page change. Another has frequency up from 2.1 to 5.8, CTR down 37%, and CPA up 54%. Output separates landing page risk from creative fatigue instead of giving one generic "refresh creatives" answer.

## Guardrails

- Do not recommend budget increases from less than 7 days of data.
- Do not call a campaign broken if conversion lag is likely.
- Do not treat Meta-reported conversions as revenue proof unless revenue quality was provided.
- Do not recommend live account changes. Produce approval-ready recommendations only.
- Do not invent reasons for performance changes when evidence is missing.
