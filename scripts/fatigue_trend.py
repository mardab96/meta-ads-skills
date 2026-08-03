#!/usr/bin/env python3
"""Creative fatigue trend comparison for Meta Ads ad-level exports.

Applies the status rules from creative-fatigue-review-meta-ads
deterministically: compares a recent window against a baseline window per
creative (or per concept, given a mapping column) on frequency, CTR, CPM and
CPA, and assigns winner / tired winner / watchlist / kill candidate /
insufficient data. Concept grouping and replacement angles stay with Claude.

Input: one CSV with a date column and per-day (or per-week) ad rows.

Usage:
  python3 fatigue_trend.py ads.csv --target-cpa 40 --recent-days 14 --baseline-days 30
  python3 fatigue_trend.py ads.csv --target-cpa 40 --col-group "Concept"

Exit codes: 0 ok, 2 could not read input.
"""
import argparse, csv, sys
from datetime import datetime

def num(v):
    v = str(v or "").replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return float(v)
    except ValueError:
        return 0.0

def parse_date(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(str(s).strip()[:10], fmt)
        except ValueError:
            continue
    return None

def pick(header, cands, override=None):
    if override:
        for h in header:
            if h.strip().lower() == override.strip().lower():
                return h
        sys.exit(f"column override not found: {override!r}")
    for h in header:
        hl = h.strip().lower()
        if any(c in hl for c in cands):
            return h
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--target-cpa", type=float, required=True)
    ap.add_argument("--recent-days", type=int, default=14)
    ap.add_argument("--baseline-days", type=int, default=30)
    ap.add_argument("--col-group", help="column to group by (e.g. Concept); default: ad name")
    a = ap.parse_args()

    try:
        with open(a.csvfile, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        print(f"READ FAILED (not the same as no ads): {e}", file=sys.stderr)
        sys.exit(2)
    if not rows:
        print("CSV read fine but has zero rows - a finding about the export, not the ads.")
        return

    header = list(rows[0].keys())
    c_date = pick(header, ["date", "day", "reporting starts"])
    c_grp = pick(header, ["ad name", "creative", "name"], a.col_group)
    c_spend = pick(header, ["spend", "amount spent", "cost"])
    c_imp = pick(header, ["impressions"])
    c_reach = pick(header, ["reach"])
    c_clicks = pick(header, ["clicks"])
    c_conv = pick(header, ["conversions", "results", "purchases", "leads"])
    need = {"date": c_date, "group": c_grp, "spend": c_spend, "impressions": c_imp, "clicks": c_clicks}
    missing = [k for k, v in need.items() if not v]
    if missing:
        sys.exit(f"could not detect columns: {missing}. Header: {header}")

    dates = [d for d in (parse_date(r[c_date]) for r in rows) if d]
    if not dates:
        sys.exit("no parseable dates found")
    maxd = max(dates)

    def bucket(r):
        d = parse_date(r[c_date])
        if d is None:
            return None
        age = (maxd - d).days
        if age < a.recent_days:
            return "recent"
        if age < a.recent_days + a.baseline_days:
            return "baseline"
        return None

    agg = {}
    for r in rows:
        b = bucket(r)
        if not b:
            continue
        g = agg.setdefault(r[c_grp], {"recent": {}, "baseline": {}})[b]
        for key, col in (("spend", c_spend), ("imp", c_imp), ("clicks", c_clicks),
                         ("conv", c_conv), ("reach", c_reach)):
            if col:
                g[key] = g.get(key, 0.0) + num(r.get(col))

    def derived(g):
        out = {}
        out["ctr"] = g.get("clicks", 0) / g["imp"] if g.get("imp") else None
        out["cpm"] = 1000 * g.get("spend", 0) / g["imp"] if g.get("imp") else None
        out["cpa"] = g.get("spend", 0) / g["conv"] if g.get("conv") else None
        out["freq"] = g["imp"] / g["reach"] if g.get("reach") else None
        return out

    print(f"Windows: recent {a.recent_days}d vs baseline {a.baseline_days}d before it. "
          f"Target CPA {a.target_cpa:.2f}. Thresholds are the skill's labeled heuristics.\n")
    print("| Group | Spend(r) | Conv(r) | Freq r/b | CTR r/b | CPM r/b | CPA r/b | Status |")
    print("|---|---:|---:|---|---|---|---|---|")
    for name, w in sorted(agg.items(), key=lambda kv: -kv[1]["recent"].get("spend", 0)):
        r, b = w["recent"], w["baseline"]
        dr, db = derived(r), derived(b)
        spend_r, conv_r = r.get("spend", 0), r.get("conv", 0)
        def rel(cur, base):
            if cur is None or not base:
                return None
            return (cur - base) / base
        ctr_drop = rel(dr["ctr"], db["ctr"])
        freq_up = rel(dr["freq"], db["freq"])
        cpm_move = rel(dr["cpm"], db["cpm"])
        cpa_ok = dr["cpa"] is not None and dr["cpa"] <= a.target_cpa
        if spend_r < 3 * a.target_cpa or conv_r < 10:
            status = "insufficient data"
        elif dr["cpa"] is not None and dr["cpa"] > 1.2 * a.target_cpa and \
                (db["cpa"] is None or db["cpa"] > 1.2 * a.target_cpa):
            status = "kill candidate (never worked)"
        elif cpa_ok and (ctr_drop is None or ctr_drop > -0.20):
            status = "winner"
        else:
            signals = sum([
                1 if (freq_up is not None and freq_up >= 0.50) else 0,
                1 if (ctr_drop is not None and ctr_drop <= -0.30) else 0,
                1 if (dr["cpa"] and db["cpa"] and dr["cpa"] / db["cpa"] >= 1.2) else 0,
            ])
            cpm_stable = cpm_move is not None and abs(cpm_move) <= 0.15
            if signals == 3 and cpm_stable:
                status = "tired winner"
            elif signals >= 2:
                status = "watchlist"
            elif cpm_move is not None and cpm_move > 0.20 and \
                    (ctr_drop is None or ctr_drop > -0.15):
                status = "auction story, not fatigue - route to budget/auction review"
            else:
                status = "watchlist"
        def fmt(x, pct=False):
            if x is None:
                return "-"
            return f"{x*100:.1f}%" if pct else f"{x:.2f}"
        print(f"| {name} | {spend_r:.0f} | {conv_r:.0f} "
              f"| {fmt(dr['freq'])}/{fmt(db['freq'])} "
              f"| {fmt(dr['ctr'], True)}/{fmt(db['ctr'], True)} "
              f"| {fmt(dr['cpm'])}/{fmt(db['cpm'])} "
              f"| {fmt(dr['cpa'])}/{fmt(db['cpa'])} | {status} |")
    print("\nGroup rows are per ad unless --col-group was given; concept grouping "
          "and replacement angles stay with the skill.")

if __name__ == "__main__":
    main()
