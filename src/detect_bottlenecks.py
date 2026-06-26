"""
Detect simple bottleneck candidates.

This first version uses activity frequency and exception co-occurrence
as a proxy because direct duration-by-activity may not be available.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EVENT_LOG = BASE_DIR / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
OUT = BASE_DIR / "reports" / "bottleneck_candidates.csv"

def main():
    df = pd.read_csv(EVENT_LOG)
    df["exception_type"] = df["exception_type"].fillna("")
    table = (
        df.assign(has_exception=df["exception_type"] != "")
          .groupby("activity")
          .agg(event_count=("activity", "size"), exception_count=("has_exception", "sum"))
          .reset_index()
    )
    table["bottleneck_proxy_score"] = table["event_count"] * (1 + table["exception_count"])
    table = table.sort_values("bottleneck_proxy_score", ascending=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
