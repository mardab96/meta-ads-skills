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

Required columns where available:

- campaign
- ad set
- objective
- optimization event
- budget and budget level (CBO / ad set)
- spend
- conversions / results
- cost per result
- learning status
- audience / targeting summary
- date

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

## Decision rules

Every threshold is a starting heuristic; recalibrate to the account and say which threshold you adjusted.

- Underpowered ad set: fewer than ~50 optimization events per week [heuristic tied to exiting learning], or a daily budget below ~1x target CPA. Persistent "learning limited" status is the platform saying the same thing.
- Fragmentation flag: more ad sets than the account's weekly conversions divided by 50 can feed [heuristic]. An account with 100 conversions per week supports roughly 2 well-fed ad sets per campaign goal, not 15.
- Duplicate test flag: two or more ad sets with the same objective, overlapping audiences, and the same funnel stage, each below the underpowered line - merge candidates.
- Merge is recommended only when the combined ad set would clear the ~50 events per week line; merging two starving ad sets into one starving ad set is not a fix.
- Keep separate despite low volume when there is a named business reason: budget ownership, reporting lines, regulatory geo separation, or genuinely different offers.
- Migration mechanics every merge plan must state: what happens to audience exclusions, past learnings (reset on significant edits), budget carry, and naming - and a max of 2-3 structural changes per week so reads stay clean [heuristic].

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

### Missing data

Fields that would change the verdict (learning status, audience overlap, business constraints not visible in exports).

## Practical example

User provides an account with 11 campaigns and 46 ad sets. Claude maps four prospecting campaigns testing similar broad audiences with tiny budgets and separate creative tests. Output recommends consolidating redundant prospecting ad sets into fewer campaigns, keeping one separate catalog campaign for business reporting, and pausing two legacy remarketing ad sets only after a 14-day monitoring window.

## Guardrails

- Do not recommend consolidation without naming the signal benefit.
- Do not pause legacy campaigns automatically.
- Do not ignore reporting or budget ownership constraints.
- Do not assume broad structure is better for every account.
- Do not make account changes directly.
