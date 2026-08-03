#!/usr/bin/env python3
"""Placement efficiency index for Meta Ads placement breakdown exports.

Applies the Decision rules from placement-breakdown-review-meta-ads
deterministically: spend share vs outcome share per placement, an efficiency
index, and the volume gate so tiny-spend placements are auto-marked
"insufficient data" instead of judged.

Usage:
  python3 placement_index.py placements.csv
  python3 placement_index.py placements.csv --min-spend-share 0.05 --min-conv 10

Exit codes: 0 ok, 2 could not read input.
"""
import argparse, csv, sys

def num(v):
    v = str(v or "").replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return float(v)
    except ValueError:
        return 0.0

def pick(header, cands):
    for h in header:
        hl = h.strip().lower()
        if any(c in hl for c in cands):
            return h
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--min-spend-share", type=float, default=0.05,
                    help="volume gate: min spend share for a verdict [heuristic]")
    ap.add_argument("--min-conv", type=float, default=10,
                    help="volume gate: min conversions for a verdict [heuristic]")
    a = ap.parse_args()

    try:
        with open(a.csvfile, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        print(f"READ FAILED (not the same as no placements): {e}", file=sys.stderr)
        sys.exit(2)
    if not rows:
        print("CSV read fine but has zero rows - a finding about the export, not the account.")
        return

    header = list(rows[0].keys())
    c_pl = pick(header, ["placement", "platform position", "position"])
    c_spend = pick(header, ["spend", "amount spent", "cost"])
    c_conv = pick(header, ["conversions", "results", "purchases", "leads"])
    c_val = pick(header, ["conversion value", "purchase value", "value"])
    if not c_pl or not c_spend:
        sys.exit(f"could not detect placement/spend columns. Header: {header}")

    agg = {}
    for r in rows:
        d = agg.setdefault(r[c_pl], {"spend": 0.0, "conv": 0.0, "val": 0.0})
        d["spend"] += num(r.get(c_spend))
        d["conv"] += num(r.get(c_conv)) if c_conv else 0.0
        d["val"] += num(r.get(c_val)) if c_val else 0.0

    tot_spend = sum(d["spend"] for d in agg.values()) or 1.0
    tot_out = sum(d["val"] or d["conv"] for d in agg.values()) or 1.0
    blended_cpa = tot_spend / sum(d["conv"] for d in agg.values()) if sum(d["conv"] for d in agg.values()) else None
    outcome_name = "value" if any(d["val"] for d in agg.values()) else "conversions"

    print(f"Outcome basis: {outcome_name}. Volume gate: >= {a.min_spend_share*100:.0f}% spend share "
          f"or >= {a.min_conv:.0f} conversions [heuristic]. "
          f"Blended CPA: {blended_cpa:.2f}\n" if blended_cpa else "\n")
    print("| Placement | Spend share | Outcome share | Index (out/spend) | CPA | Gate verdict |")
    print("|---|---:|---:|---:|---:|---|")
    for name, d in sorted(agg.items(), key=lambda kv: -kv[1]["spend"]):
        ss = d["spend"] / tot_spend
        outcome = d["val"] or d["conv"]
        os_ = outcome / tot_out
        idx = os_ / ss if ss else 0.0
        cpa = d["spend"] / d["conv"] if d["conv"] else None
        if ss < a.min_spend_share and d["conv"] < a.min_conv:
            verdict = "insufficient data - no verdict"
        elif d["conv"] == 0 and ss >= 0.10:
            verdict = "exclusion-test candidate IF lag window closed (10%+ spend, 0 conv)"
        elif cpa and blended_cpa and cpa > 2 * blended_cpa and d["conv"] >= 10:
            verdict = "exclusion-test candidate (CPA > 2x blended at 10+ conv) - try adapted creative first"
        elif idx < 1 / 3:
            verdict = "outcome share < 1/3 of spend share - watch across a second window"
        else:
            verdict = "no action from this data"
        cpa_s = f"{cpa:.2f}" if cpa is not None else "-"
        print(f"| {name} | {ss*100:.1f}% | {os_*100:.1f}% | {idx:.2f} | {cpa_s} | {verdict} |")
    print("\nCreative-format mismatch and intent questions stay with the skill; "
          "this table only settles the arithmetic and the volume gate.")

if __name__ == "__main__":
    main()
