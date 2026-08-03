#!/usr/bin/env python3
"""Week-over-week delta calculator for the Meta Ads weekly readout.

Joins two campaign-level CSVs (previous week, current week), computes deltas
for the standard metrics and applies the noise band from
weekly-performance-readout-meta-ads: a row is flagged only if it moved more
than the band AND rests on enough volume. Spend is always shown.

Usage:
  python3 wow_delta.py prev_week.csv this_week.csv
  python3 wow_delta.py prev.csv cur.csv --band 0.15 --min-conv 30 --min-clicks 1000

Exit codes: 0 ok, 2 could not read an input file.
"""
import argparse, csv, sys

METRICS = [
    ("spend", ["spend", "amount spent", "cost"]),
    ("conversions", ["conversions", "results", "purchases", "leads"]),
    ("clicks", ["clicks", "link clicks"]),
    ("impressions", ["impressions"]),
]

def num(v):
    v = str(v or "").replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return float(v)
    except ValueError:
        return 0.0

def load(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        print(f"READ FAILED for {path} (not the same as an empty week): {e}", file=sys.stderr)
        sys.exit(2)
    tot = {}
    if not rows:
        return tot
    header = list(rows[0].keys())
    cols = {}
    for key, cands in METRICS:
        for h in header:
            if any(c in h.strip().lower() for c in cands):
                cols[key] = h
                break
    for r in rows:
        for key, col in cols.items():
            tot[key] = tot.get(key, 0.0) + num(r.get(col))
    return tot

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prev_csv"); ap.add_argument("cur_csv")
    ap.add_argument("--band", type=float, default=0.15, help="noise band [heuristic]")
    ap.add_argument("--wide-band", type=float, default=0.25,
                    help="band when weekly conversions are under --min-conv")
    ap.add_argument("--min-conv", type=float, default=30)
    ap.add_argument("--min-clicks", type=float, default=1000)
    a = ap.parse_args()

    prev, cur = load(a.prev_csv), load(a.cur_csv)
    if not prev or not cur:
        print("One of the files read fine but had zero rows - that is a finding "
              "about the export, not the account. Not computing deltas.")
        return

    def derive(t):
        d = dict(t)
        d["CPA"] = t["spend"] / t["conversions"] if t.get("conversions") else None
        d["CTR%"] = 100 * t["clicks"] / t["impressions"] if t.get("impressions") else None
        d["CPM"] = 1000 * t["spend"] / t["impressions"] if t.get("impressions") else None
        return d

    p, c = derive(prev), derive(cur)
    low_volume = c.get("conversions", 0) < a.min_conv
    band = a.wide_band if low_volume else a.band
    print(f"Noise band applied: +/-{band*100:.0f}% "
          f"({'widened: under ' + str(int(a.min_conv)) + ' conversions/week' if low_volume else 'standard'}) [heuristic]\n")
    print("| Metric | Last week | This week | Change | Flag |")
    print("|---|---:|---:|---:|---|")
    for m in ["spend", "conversions", "clicks", "impressions", "CPA", "CTR%", "CPM"]:
        pv, cv = p.get(m), c.get(m)
        if pv in (None, 0) or cv is None:
            print(f"| {m} | {pv if pv is not None else '-'} | {cv if cv is not None else '-'} | - | insufficient base |")
            continue
        ch = (cv - pv) / pv
        volume_ok = (c.get("conversions", 0) >= a.min_conv) or \
                    (m in ("spend", "clicks", "impressions", "CTR%", "CPM") and c.get("clicks", 0) >= a.min_clicks)
        if m == "spend":
            flag = "ALWAYS REPORT (reader owns the budget)"
        elif abs(ch) > band and volume_ok:
            flag = "FLAG - enters 'What changed'"
        elif abs(ch) > band:
            flag = "moved, but volume base too small - report as low confidence"
        else:
            flag = "within noise band"
        print(f"| {m} | {pv:,.2f} | {cv:,.2f} | {ch*100:+.1f}% | {flag} |")
    print("\nDriver attribution stays with the skill: match flags against the "
          "change log before assigning causes.")

if __name__ == "__main__":
    main()
