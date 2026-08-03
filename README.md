# 10 Claude Skills for Meta Ads

A pack of 10 production-ready Claude Skills that help performance marketers run rigorous Meta Ads diagnostics from exports: account health, creative fatigue, Advantage+ diagnosis, Pixel and Conversions API signal quality, budget reallocation, placement breakdowns, campaign structure, offer-angle extraction, comment mining, and weekly readouts.

Each skill is a self-contained `SKILL.md` with explicit triggers, required inputs, analysis workflow, decision rules with unit-carrying thresholds (every threshold labeled as a heuristic to recalibrate per account), a practical example, output format, and guardrails. Four number-heavy skills additionally ship a deterministic helper in `scripts/` (budget classification, week-over-week deltas, fatigue trends, placement efficiency), so the arithmetic on long CSVs is computed, not eyeballed. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

These skills are intentionally conservative. They work with Meta Ads exports today. If you later connect Meta Ads through MCP or another data layer, the same workflows can use live tools, but the default design does not require write access or campaign mutation.

## What's inside

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 1 | Account Health Check | `account-health-check-meta-ads` | Find the top issues in a Meta Ads account before deep optimization |
| 2 | Creative Fatigue Review | `creative-fatigue-review-meta-ads` | Identify tired winners, weak concepts, and replacement creative angles |
| 3 | Advantage+ Diagnosis | `advantage-plus-diagnosis-meta-ads` | Diagnose Advantage+ campaigns without assuming automation is the problem |
| 4 | Pixel and CAPI Signal Quality Audit | `pixel-capi-signal-quality-audit-meta-ads` | Review Pixel, Conversions API, event quality, deduplication, and optimization event fit |
| 5 | Budget Reallocation Planner | `budget-reallocation-planner-meta-ads` | Decide where to add, hold, reduce, or pause budget with rollback triggers |
| 6 | Placement Breakdown Review | `placement-breakdown-review-meta-ads` | Find placement-level efficiency issues and creative mismatches |
| 7 | Campaign Structure Audit | `campaign-structure-audit-meta-ads` | Map campaign and ad set roles, flag fragmentation, duplication, and legacy debt |
| 8 | Offer and Angle Extraction | `offer-angle-extraction-meta-ads` | Extract the actual hypotheses being tested across ads and creatives |
| 9 | Comment and Objection Mining | `comment-objection-mining-meta-ads` | Turn comments into objections, FAQ gaps, creative notes, and landing page fixes |
| 10 | Weekly Performance Readout | `weekly-performance-readout-meta-ads` | Produce a weekly Meta Ads update with facts, hypotheses, next actions, and approval asks |

## How to install

### Option A - Claude Code

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level skills directory at `~/.claude/skills/`.
3. Start a new Claude Code session in that project. Skills will activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/meta-ads-skills.git
mkdir -p ~/.claude/skills
cp -r meta-ads-skills/*-meta-ads meta-ads-skills/scripts ~/.claude/skills/
```

The `scripts/` folder ships the deterministic helpers four skills call via relative paths; the command above keeps those paths working.

### Option B - Other Claude environments

The skills are plain Markdown with YAML frontmatter. Paste the relevant `SKILL.md` content into context when you want to use it.

## How to use

Once installed, describe what you want in natural language. Skills self-trigger on the patterns documented in their `## Use this skill when` section.

Examples:

- "Review this Meta Ads account health, here are campaign and ad set exports." -> activates Account Health Check.
- "CPA is rising and frequency is up. Check if this is creative fatigue." -> activates Creative Fatigue Review.
- "Prepare my weekly Meta Ads readout for this client." -> activates Weekly Performance Readout.

## Bring your data

Every skill is data-first. They work best when you provide actual Meta Ads exports.

Recommended exports:

- campaign performance report
- ad set performance report
- ad performance report
- placement breakdown
- platform breakdown
- age and gender breakdown, if relevant
- country or region breakdown
- Pixel and Conversions API diagnostics screenshots or exports
- comments export or copied comment samples
- product set or catalog performance export for ecommerce accounts

## Guardrails

These skills are designed for diagnosis and approval-ready recommendations. By default they do not:

- publish ads
- change budgets
- pause campaigns, ad sets, or ads
- edit tracking setup
- change optimization events
- modify audiences or exclusions
- make performance claims without data

Use them to structure the work, not to hand over control of the account.

## License & attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) - performance marketing infrastructure for AI-native operators.
