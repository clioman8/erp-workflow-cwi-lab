"""
Detect possible knowledge-gap signals in event logs.

This prototype flags exception events that may indicate missing process
understanding, unclear master data, or insufficient workflow documentation.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EVENT_LOG = BASE_DIR / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
OUT = BASE_DIR / "reports" / "knowledge_gap_signals.csv"

KNOWLEDGE_GAP_EXCEPTIONS = {
    "warehouse_error": "warehouse selection / inventory location knowledge gap",
    "bom_variance": "BOM standard-vs-actual usage knowledge gap",
    "material_shortage": "planning and availability knowledge gap",
    "approval_delay": "authority and approval-rule knowledge gap",
    "qc_hold": "quality status and release workflow knowledge gap",
}

def main():
    df = pd.read_csv(EVENT_LOG)
    df["exception_type"] = df["exception_type"].fillna("")
    rows = []
    for _, row in df.iterrows():
        if row["exception_type"] in KNOWLEDGE_GAP_EXCEPTIONS:
            d = row.to_dict()
            d["knowledge_gap_signal"] = KNOWLEDGE_GAP_EXCEPTIONS[row["exception_type"]]
            rows.append(d)
    out = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
