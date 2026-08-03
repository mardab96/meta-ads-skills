---
name: pixel-capi-signal-quality-audit-meta-ads
description: Audits Meta Ads Pixel and Conversions API signal quality using Events Manager diagnostics, event match quality, deduplication, event volume, optimization event fit, and business context. Use before scaling, after tracking changes, or when reported results look suspicious.
---

# Pixel and CAPI Signal Quality Audit - Meta Ads

## Use this skill when

The user wants to know whether Meta Ads is optimizing from clean enough conversion signals.

Common user requests:

- "Audit Meta Pixel and CAPI quality."
- "Can we scale this campaign safely?"
- "Meta reports leads but sales says quality is bad."
- "Are our events duplicated?"

## Required input

Minimum useful data:

- Events Manager diagnostics screenshot or export.
- Pixel status.
- Conversions API status.
- Event match quality.
- Optimization event.
- Event volume by event.
- Campaign objective and optimization event.

Recommended additional data:

- Deduplication setup notes.
- Event IDs where available.
- CRM or sales quality data.
- Website or GTM change history.
- Consent mode / cookie banner notes if relevant.

## Before analysis

1. Confirm the conversion event Meta optimizes toward.
2. Confirm what the business actually values: lead, qualified lead, sale, purchase value, subscription, or another outcome.
3. Ask whether both browser and server events are active.
4. Ask whether deduplication is configured.
5. Treat screenshots as partial evidence. Ask for exports if needed.

## Analysis workflow

1. Build an event map:
   - event name
   - source
   - volume
   - match quality
   - used for optimization or not
   - business relevance
2. Identify missing, duplicated, shallow, or noisy events.
3. Check whether optimization event volume is enough for campaign learning.
4. Separate technical tracking problems from business quality problems.
5. Identify campaign risks created by weak signals.
6. Produce a tracking QA action list for a human or developer.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate to the account and say which threshold you adjusted.

Verdict rubric - the three states have criteria, not vibes:

| Verdict | Criteria |
|---|---|
| Ready to scale | EMQ 6.0+ on the optimization event [heuristic], deduplication verified (not just configured), optimization event at roughly 50+ conversions per week per ad set [heuristic tied to learning], and the event matches what the business values |
| Needs review | EMQ 4.0-6.0, OR only one source (browser-only or server-only) active, OR dedup configured but unverified, OR event volume between 20 and 50 per week |
| Not ready | EMQ below 4.0, OR both sources firing the same event with dedup unverified, OR optimization event under ~20 conversions per week, OR the optimized event is not what the business values (e.g. Lead optimized, 18% qualify) |

Deduplication verification procedure (configured is not verified):

1. Confirm the same `event_id` is sent on the browser and server copy of the same event.
2. In Events Manager, confirm the event shows a deduplicated count, not two separate totals.
3. Compare browser and server event counts over the same window: a healthy overlap band is roughly 60-90% [heuristic]; near 0% overlap means dedup keys never match, near 100% single-source means one channel is dead.

Signal-vs-business rule: a technically clean event that does not represent value (unqualified leads, add-to-carts optimized as purchases) caps the verdict at "needs review" regardless of EMQ.

### Vertical notes

- Ecommerce: purchase events need value and currency parameters checked, not just presence; wrong value feeds break ROAS bidding silently.
- Lead gen: the deeper-event tradeoff (qualified lead vs raw lead) trades volume against quality; below ~20 qualified events per week the deeper event may starve learning [heuristic].
- App: web Pixel rules do not transfer; SKAN / AEM has its own volume and delay constraints.

## Output format

### Signal verdict

Ready to scale, needs review, or not ready.

### Event map

| Event | Source | Volume | Match quality | Business value | Issue |
|---|---|---:|---|---|---|

### Issues

| Priority | Issue | Evidence | Why it matters | Owner |
|---|---|---|---|---|

### QA checklist

Concrete checks for the tracking owner.

### Missing data

What was not visible with the provided input (screenshots cover less than exports), and which verdict criteria it blocks.

## Practical example

User provides Events Manager screenshots. Claude finds Lead events from Pixel and CAPI both active, but deduplication is unclear. Campaigns optimize for Lead while CRM notes say only 18% are qualified. Output separates "possible deduplication risk" from "business signal mismatch" and recommends validating event IDs plus testing a deeper qualified-lead signal before scaling.

## Guardrails

- Do not edit tracking. Produce a QA list for the tracking owner.
- Do not assume CAPI is correct because it exists.
- Do not recommend scaling before signal quality is understood.
- Do not claim Pixel and CAPI should match exactly.
- Do not make developer-level claims without diagnostics or implementation details.
