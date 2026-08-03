# Changelog

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
