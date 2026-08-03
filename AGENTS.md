# AGENTS.md: Meta Ads diagnostic skills

This repo is a pack of 10 Claude Code Skills for recurring Meta Ads
diagnostics run from exports. Each skill is a self-contained `SKILL.md` under
its own folder, following the Agent Skills standard, so the pack also runs in
any other Agent Skills tool.

## How these skills behave

- **Data-first.** Every skill reads what you provide: Ads Manager exports,
  breakdowns, Events Manager screenshots, comment exports. If the input is
  missing, the skill says so and marks an assumption instead of guessing.
- **Human-in-the-loop.** Skills diagnose and recommend. They do not log into
  the ad account and they do not change campaigns, budgets or audiences.
- **Honest about limits.** Every threshold inside a skill (frequency caps,
  fatigue signals, health checks) is a labeled heuristic, not a rule Meta
  published. Confidence is stated.

## How the pack composes

- `account-health-check-meta-ads` is the entry point. It establishes the
  overall state and routes to the right deep-dive skill.
- Signal skills (`pixel-capi-signal-quality-audit-meta-ads`) come before
  performance skills. Advantage+ and creative diagnosis on top of a broken
  Pixel/CAPI setup produces confident, wrong answers.
- Qualitative skills (`comment-objection-mining-meta-ads`,
  `offer-angle-extraction-meta-ads`) feed the creative skills: mine the
  objections first, then brief the next angle.
- `weekly-performance-readout-meta-ads` is the recurring summary skill; run
  it last.

## Verticals

Ecommerce accounts lean on creative fatigue, placement breakdowns and
Advantage+ diagnosis; lead gen accounts lean on signal quality and the
offer-angle skills, and should rank on CRM-verified lead value rather than
the platform's reported cost per lead.
