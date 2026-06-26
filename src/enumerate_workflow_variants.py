"""
Enumerate process variants by case_id.
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EVENT_LOG = BASE_DIR / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
OUT = BASE_DIR / "reports" / "process_variants.csv"

def main() -> None:
    df = pd.read_csv(EVENT_LOG)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    variants = (
        df.sort_values(["case_id", "timestamp"])
          .groupby("case_id")["activity"]
          .apply(lambda s: " > ".join(s))
          .reset_index(name="variant")
    )
    counts = variants["variant"].value_counts().rename_axis("variant").reset_index(name="case_count")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    counts.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
