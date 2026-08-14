# Changelog

## [2.0.0] - 2026-08-19

### Added

Ten skills that read the signal and the money underneath the account. The first ten
all read what the account reported; these read whether the report can be trusted and
whether the revenue behind it is profit.

- `attribution-credit-check-meta-ads` - compare reported conversions against the business count and a stricter attribution window
- `modeled-conversions-review-meta-ads` - separate observed conversions from estimated ones before betting on them
- `conversion-lag-read-meta-ads` - measure how long results keep filling in, and set a waiting rule
- `ios-reporting-gap-meta-ads` - size the iOS reporting blind spot and set event priority against it
- `click-to-session-gap-meta-ads` - split the click-to-session gap into a load problem and a measurement problem
- `incrementality-test-design-meta-ads` - design a holdout or geo test the account can actually read
- `campaign-margin-check-meta-ads` - rank campaigns on contribution margin instead of ROAS
- `audience-overlap-review-meta-ads` - find overlap, stale lists and missing exclusions
- `lookalike-source-review-meta-ads` - judge the seed, because the model copies whatever it is given
- `learning-phase-check-meta-ads` - check whether structure and budget let any ad set exit learning

### Changed

- README title and count from 10 to 20, with the full skill table.

### Notes

Every threshold in the new skills is labelled as a heuristic to recalibrate per account,
not as a published Meta rule. Three skills refuse to answer under stated conditions rather
than return a number the data cannot support: incrementality declines to design a holdout
the account cannot read, campaign margin prints break-even ROAS instead of a margin
percentage when cost lines are missing, and modeled conversions reports a range instead of
a point below the learning volume threshold.


All notable changes to this pack are documented here. Format follows Keep a
Changelog, loosely.

## [1.2.0] - 2026-08-03

### Added
- `Decision rules` section in all 10 skills: unit-carrying thresholds for every
  verdict label (fatigue statuses, budget classes, Advantage+ states, signal
  verdicts, placement exclusion criteria, noise bands), each labeled as a
  starting heuristic to recalibrate per account.
- Driver-attribution decision tree in the account health check (metric deltas
  to issue type, applied in order).
- Deterministic helpers in `scripts/`: `classify_budget.py`, `wow_delta.py`,
  `fatigue_trend.py`, `placement_index.py` - CSV in, verdict table out, so the
  arithmetic on long exports is computed instead of estimated. Each
  distinguishes "file read fine but empty" from "could not read the file".
- Worked examples with input tables and filled outputs in the creative fatigue
  review and the weekly readout.
- `Missing data` output section in the six skills that lacked one; required
  column lists in the Advantage+ diagnosis and the structure audit; vertical
  notes (ecommerce / lead gen / app) in the health check, Advantage+ diagnosis
  and signal audit.

### Fixed
- The Pixel/CAPI guardrail "Do not tell Claude to edit tracking" now reads
  "Do not edit tracking; produce a QA list for the tracking owner".
- Install command copies `scripts/` so the relative paths skills cite resolve.

## [1.1.0] - 2026-08-03

### Fixed
- Install command now creates `~/.claude/skills` before copying, so it works on
  a machine where Claude Code has not created the folder yet. The previous
  `cp -r repo/* ~/.claude/skills/` failed with "Not a directory" on a fresh
  setup.
- Install command copies only the 10 skill folders, instead of dumping the
  repo's README into the skills root.

### Added
- MIT `LICENSE` (the pack was described as open source; now it formally is).
- `AGENTS.md` with durable guidance on how the pack behaves and composes.
- This changelog.

## [1.0.0] - 2026-05-24

### Added
- Initial public release: 10 diagnostic skills for Meta Ads run from exports.
