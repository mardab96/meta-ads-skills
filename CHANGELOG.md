# Changelog

All notable changes to this pack are documented here. Format follows Keep a
Changelog, loosely.

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
