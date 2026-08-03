#!/usr/bin/env python3
"""Budget reallocation classifier for Meta Ads exports.

Applies the Decision rules from budget-reallocation-planner-meta-ads
deterministically: scale / hold / reduce / pause / needs-more-data, with the
step-size cap. Thresholds are the skill's labeled heuristics; override via flags.

Usage:
  python3 classify_budget.py export.csv --target-cpa 50
  python3 classify_budget.py export.csv --target-cpa 50 \
      --col-spend "Amount spent" --col-conv "Results" --col-name "Campaign name"

Expected columns (auto-detected, case-insensitive; override with --col-*):
  name (campaign/ad set), spend, conversions, budget (optional), days (optional
  per-row; else pass --window-days).

Exit codes: 0 ok, 2 could not read input (distinct from "empty file read fine").
"""
import argparse, csv, sys

def find_col(header, candidates, override):
    if override:
        for h in header:
            if h.strip().lower() == override.strip().lower():
                return h
        sys.exit(f"column override not found in CSV header: {override!r}")
    for h in header:
        hl = h.strip().lower()
        for c in candidates:
            if c in hl:
                return h
    return None

def num(v):
    if v is None:
        return 0.0
    v = str(v).replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return float(v)
    except ValueError:
        return 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--target-cpa", type=float, required=True)
    ap.add_argument("--window-days", type=int, default=30)
    ap.add_argument("--min-conv", type=int, default=30,
                    help="conversions needed before a verdict [heuristic]")
    ap.add_argument("--scale-edge", type=float, default=0.15,
                    help="CPA must beat target by this fraction to scale")
    ap.add_argument("--max-step", type=float, default=0.20,
                    help="max budget change per step")
    ap.add_argument("--col-name"); ap.add_argument("--col-spend")
    ap.add_argument("--col-conv"); ap.add_argument("--col-budget")
    a = ap.parse_args()

    try:
        with open(a.csvfile, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        print(f"READ FAILED (this is not an empty account): {e}", file=sys.stderr)
        sys.exit(2)
    if not rows:
        print("CSV read fine but contains zero data rows. "
              "Empty export is a finding about the export, not the account.")
        return

    header = list(rows[0].keys())
    c_name = find_col(header, ["campaign", "ad set", "name"], a.col_name)
    c_spend = find_col(header, ["spend", "amount spent", "cost"], a.col_spend)
    c_conv = find_col(header, ["conversions", "results", "purchases", "leads"], a.col_conv)
    c_budget = find_col(header, ["budget"], a.col_budget)
    missing = [n for n, c in [("name", c_name), ("spend", c_spend), ("conversions", c_conv)] if not c]
    if missing:
        sys.exit(f"could not detect columns: {missing}; pass --col-* overrides. Header: {header}")

    # aggregate by name (multi-day exports)
    agg = {}
    for r in rows:
        k = r[c_name]
        d = agg.setdefault(k, {"spend": 0.0, "conv": 0.0, "budget": num(r.get(c_budget)) if c_budget else None})
        d["spend"] += num(r.get(c_spend))
        d["conv"] += num(r.get(c_conv))

    print(f"Target CPA: {a.target_cpa:.2f} | window: {a.window_days}d | "
          f"min conversions for a verdict: {a.min_conv} [heuristic]\n")
    print("| Campaign / ad set | Spend | Conv | CPA | Class | Suggested step (max +/-{:.0f}%) |".format(a.max_step * 100))
    print("|---|---:|---:|---:|---|---|")
    for name, d in sorted(agg.items(), key=lambda kv: -kv[1]["spend"]):
        spend, conv = d["spend"], d["conv"]
        cpa = spend / conv if conv else None
        if conv == 0 and spend >= 3 * a.target_cpa:
            cls, step = "pause candidate", "pause after lag-window check"
        elif cpa is not None and cpa > 2 * a.target_cpa and conv >= 20:
            # outranks the min-conv floor by design (see skill Decision rules)
            cls, step = "pause candidate", "review before pausing"
        elif conv < a.min_conv:
            cls, step = "needs more data", "hold; widen window"
        elif cpa <= a.target_cpa * (1 - a.scale_edge):
            cls, step = "scale candidate", f"+{a.max_step*100:.0f}% if stable 14d and learning complete"
        elif cpa > a.target_cpa * 1.25:
            cls, step = "reduce candidate", f"-{a.max_step*100:.0f}% after lag window"
        else:
            cls, step = "hold", "no change"
        cpa_s = f"{cpa:.2f}" if cpa is not None else "-"
        print(f"| {name} | {spend:.2f} | {conv:.0f} | {cpa_s} | {cls} | {step} |")
    print("\nRules applied are the skill's labeled heuristics; classifications on "
          "immature windows or mid-learning data still need the human checks in "
          "the SKILL.md (lag window, recent edits, CRM quality).")

if __name__ == "__main__":
    main()
