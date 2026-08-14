---
name: incrementality-test-design-meta-ads
description: Designs a holdout or geo test that answers whether Meta spend causes sales or reports sales that would have happened anyway, and states what the account needs before such a test can produce a readable result. Use before scaling, before cutting a high-ROAS retargeting campaign, or whenever reported ROAS and total revenue disagree.
---

# Would These Sales Happen Anyway - Meta Ads

## Use this skill when

Reported performance is strong and the business cannot feel it.

Common user requests:

- "Retargeting ROAS is 11 and revenue is flat."
- "How do I prove Meta is actually working?"
- "Can I turn this off and see what happens?"
- "Is our brand campaign buying sales we already had?"

## Required input

Minimum useful data:

- Total business revenue or lead volume by week, for at least 8 weeks.
- Meta spend by week for the same period.
- The campaigns under suspicion, with their reported conversions and value.

Recommended additional data:

- Revenue split by region, if the business sells across several.
- Any past period when Meta spend stopped, for any reason.
- Known seasonality and promotional calendar.

## Before analysis

1. Establish the baseline: what the business does in a week with no Meta spend at all. Without any such period, the test has to create one.
2. Confirm the business can read revenue at the level the test will split on, whether that is region, audience or time.
3. Ask what the business is willing to risk. A holdout costs real sales during the test; that is the price of the answer.
4. Check for anything else changing in the test window. A concurrent promotion makes the result unreadable.

## Analysis workflow

1. Choose the test shape: a geo split where regions are comparable, an audience holdout where they are not, or a clean on-off period where the account is small.
2. Size the test from the baseline: work out how many weeks are needed for a difference to be visible above normal week-to-week variation.
3. Define the single metric the test reads, chosen from business data, never from Meta's reported conversions.
4. Write down the expected result under both hypotheses before the test runs.
5. Define the stop rule and the maximum acceptable loss.
6. State what the test will not answer, so the result is not overread later.

## Decision rules

Every threshold is a starting heuristic, not a Meta rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Test is readable | Weekly revenue variation under roughly 25% of its own median [heuristic], 8+ weeks of history, and a clean window with no promotion |
| Test needs a longer window | Variation 25-50%, or fewer than 8 weeks of history |
| Do not run the test yet | Variation above 50%, OR a promotion inside the window, OR the business cannot read revenue at the split level |

Holdout size rule: a holdout too small produces a result that cannot clear normal noise, which reads as "no effect" and gets misquoted as proof. Where the baseline cannot support a readable holdout, say the test is not available rather than running a decorative one.

Reading rule: the result is a range, never a point. Report the observed difference alongside normal week-to-week variation, so the reader can see whether the effect clears it.

## Output format

### Test readiness

Readable, needs a longer window, or not yet.

### Test design

| Element | Choice | Why |
|---|---|---|

### Baseline

Weekly business figures, their median and their spread.

### Stop rule and maximum loss

The number at which the test ends early, and the cost the business is accepting.

### What this test will not answer

Named explicitly.

## Practical example

Retargeting reports 11 ROAS while total revenue has been flat for six weeks. Weekly revenue varies by 19% around its median and no promotion is planned. Output: a four-week audience holdout on 30% of the retargeting audience, read on shop revenue rather than Meta conversions, with an expected difference written down in advance and a stop rule at a 15% revenue drop in the held-out group.

## Guardrails

- Do not read the test on Meta's own conversion numbers. That defeats the purpose.
- Do not run a test through a promotion or a seasonal peak.
- Do not report a result that does not clear normal variation as a finding.
- Do not present a holdout as free. Name the expected cost before it starts.
- Do not use a past accidental pause as a clean test without checking what else changed then.
