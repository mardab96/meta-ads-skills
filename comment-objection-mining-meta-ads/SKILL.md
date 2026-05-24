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

## Practical example

User provides 180 comments from lead-gen ads. Claude finds 37 genuine objections and 91 spam / irrelevant comments. Main clusters are "is this free?", "does it work for Shopify?", and "I do not trust AI with ad spend." Output recommends adding pricing clarity to the ad, a Shopify compatibility FAQ, and a human-approval line on the landing page.

## Guardrails

- Do not treat comments as statistically representative.
- Do not recommend hiding comments unless they are spam, abusive, or clearly irrelevant.
- Do not reply automatically.
- Do not make legal or policy claims without source material.
- Do not shame users or write defensive responses.
