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

## Practical example

User provides Events Manager screenshots. Claude finds Lead events from Pixel and CAPI both active, but deduplication is unclear. Campaigns optimize for Lead while CRM notes say only 18% are qualified. Output separates "possible deduplication risk" from "business signal mismatch" and recommends validating event IDs plus testing a deeper qualified-lead signal before scaling.

## Guardrails

- Do not tell Claude to edit tracking.
- Do not assume CAPI is correct because it exists.
- Do not recommend scaling before signal quality is understood.
- Do not claim Pixel and CAPI should match exactly.
- Do not make developer-level claims without diagnostics or implementation details.
