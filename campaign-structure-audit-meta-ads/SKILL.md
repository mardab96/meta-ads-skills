---
name: campaign-structure-audit-meta-ads
description: Audits Meta Ads campaign and ad set structure to identify unclear roles, duplicate tests, fragmented budgets, underpowered ad sets, legacy debt, and structures that limit learning. Use when inheriting an account, cleaning structure, or preparing to scale.
---

# Campaign Structure Audit - Meta Ads

## Use this skill when

The user wants to understand whether the Meta Ads structure supports learning and decision-making.

Common user requests:

- "Audit this Meta Ads structure."
- "Do we have too many ad sets?"
- "Should we consolidate campaigns?"
- "Clean up this inherited account."

## Required input

Minimum useful data:

- Campaign and ad set export.
- Objective and optimization event.
- Budget and spend.
- Audience or targeting logic.
- Geography and placement settings where available.
- Conversion volume.

Recommended additional data:

- Naming convention.
- Recent test notes.
- Funnel stage for each campaign.
- Business reason for separate budgets.

## Before analysis

1. Confirm business goal and account stage.
2. Ask whether campaigns map to different funnel stages, offers, geographies, or product groups.
3. Check if low volume is caused by structure or market size.
4. Avoid consolidation recommendations without explaining what signal improves.
5. Preserve legitimate separation where budget ownership or reporting requires it.

## Analysis workflow

1. Map every campaign and ad set role:
   - prospecting
   - remarketing
   - creative test
   - offer test
   - geo test
   - catalog / product set
   - retention
   - unclear / legacy
2. Find duplicated objectives and overlapping tests.
3. Identify underpowered ad sets and fragmented budgets.
4. Identify mixed-variable tests that are hard to read.
5. Propose keep, merge, pause candidate, rename, or clarify role.
6. Build a target structure for human review.

## Output format

### Structure verdict

Short diagnosis of whether structure supports or fragments learning.

### Account map

| Campaign / ad set | Current role | Issue | Recommendation |
|---|---|---|---|

### Target structure

Proposed simplified structure with rationale.

### Migration plan

Low-risk order of cleanup.

## Practical example

User provides an account with 11 campaigns and 46 ad sets. Claude maps four prospecting campaigns testing similar broad audiences with tiny budgets and separate creative tests. Output recommends consolidating redundant prospecting ad sets into fewer campaigns, keeping one separate catalog campaign for business reporting, and pausing two legacy remarketing ad sets only after a 14-day monitoring window.

## Guardrails

- Do not recommend consolidation without naming the signal benefit.
- Do not pause legacy campaigns automatically.
- Do not ignore reporting or budget ownership constraints.
- Do not assume broad structure is better for every account.
- Do not make account changes directly.
