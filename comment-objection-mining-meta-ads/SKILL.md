---
name: comment-objection-mining-meta-ads
description: Reviews Meta Ads comments or copied comment samples to classify objections, confusion, trust issues, pricing concerns, support issues, spam, and praise. Use when comments contain customer feedback that can improve ads, landing pages, FAQs, or offer clarity.
---

# Comment and Objection Mining - Meta Ads

## Use this skill when

The user wants to extract useful customer feedback from Meta Ads comments.

Common user requests:

- "Analyze these ad comments."
- "What objections show up under our ads?"
- "Turn comments into landing page fixes."
- "Which comments need human response?"

## Required input

Minimum useful data:

- Comments or comment export.
- Ad ID, creative name, or campaign name.
- Campaign objective.
- Ad copy or creative description.

Recommended additional data:

- Ad-level performance for commented ads.
- Landing page URL or summary.
- Current FAQ.
- Brand response policy.

## Before analysis

1. Confirm whether comments are from paid ads, organic posts, or both.
2. Ask if there are legal, medical, finance, or regulated claims to handle carefully.
3. Treat comments as qualitative signal, not statistically representative proof.
4. Separate spam from genuine objection.
5. Do not draft public replies unless asked.

## Analysis workflow

1. Classify each comment:
   - confusion
   - trust objection
   - price objection
   - product objection
   - support issue
   - competitor mention
   - spam
   - praise
   - irrelevant
2. Group recurring themes.
3. Identify what the ad or landing page failed to explain.
4. Recommend fixes:
   - ad copy
   - creative
   - landing page
   - FAQ
   - offer
   - customer support response
5. Flag comments requiring human response.

## Decision rules

Comments are qualitative signal; these rules keep the output honest about how much signal there is. Thresholds are heuristics; say which one you adjusted.

- Recurring theme: at least 3 independent commenters (not one thread) raising the same objection [heuristic]. One vivid comment is an anecdote and is labeled as such.
- Sample floor: below ~30 genuine (non-spam) comments, the whole output is labeled "directional, low sample" and no fix recommendation gets high confidence [heuristic].
- Fix routing by cluster share of genuine comments [heuristic]:
  - 20%+ of genuine comments -> the ad or landing page failed to explain it; recommend an ad copy or landing page change.
  - 5-20% -> FAQ or comment-reply material; not worth changing the ad yet.
  - Under 5% -> log it, do nothing.
- A cluster earns "change the offer" only when the objection is about the offer's substance (price, terms, availability) AND it is the largest cluster - copy fixes come first everywhere else.
- Human response queue: legal / medical / finance claims, angry customers with an unresolved support issue, and questions from plausibly high-intent buyers. Everything else can wait for batch replies.

## Output format

### Objection summary

Main patterns in plain English.

### Comment clusters

| Cluster | Example comment | Meaning | Recommended fix |
|---|---|---|---|

### Human response queue

Comments that need manual attention.

### Copy and FAQ updates

Suggested clarifications.

### Missing data

What limits the read: sample size, missing ad-level performance for commented ads, or missing landing page context.

## Practical example

User provides 180 comments from lead-gen ads. Claude finds 37 genuine objections and 91 spam / irrelevant comments. Main clusters are "is this free?", "does it work for Shopify?", and "I do not trust AI with ad spend." Output recommends adding pricing clarity to the ad, a Shopify compatibility FAQ, and a human-approval line on the landing page.

## Guardrails

- Do not treat comments as statistically representative.
- Do not recommend hiding comments unless they are spam, abusive, or clearly irrelevant.
- Do not reply automatically.
- Do not make legal or policy claims without source material.
- Do not shame users or write defensive responses.
