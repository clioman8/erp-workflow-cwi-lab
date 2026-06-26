"""
Calculate starter CWI metrics from the integrated event log.
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
EVENT_LOG = DATA_DIR / "event_logs" / "synthetic_integrated_event_log.csv"

def role_handoffs(case_df: pd.DataFrame) -> int:
    roles = case_df.sort_values("timestamp")["actor_role"].tolist()
    return sum(1 for a, b in zip(roles, roles[1:]) if a != b)

def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(EVENT_LOG)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["exception_type"] = df["exception_type"].fillna("")

    activity_counts = df["activity"].value_counts().rename_axis("activity").reset_index(name="count")
    exception_counts = df[df["exception_type"] != ""]["exception_type"].value_counts().rename_axis("exception_type").reset_index(name="count")
    status_counts = df["status"].value_counts().rename_axis("status").reset_index(name="count")
    data_origin_counts = df["data_origin"].value_counts().rename_axis("data_origin").reset_index(name="count")

    cycle = df.groupby("case_id")["timestamp"].agg(case_start="min", case_end="max").reset_index()
    cycle["cycle_time_minutes"] = ((cycle["case_end"] - cycle["case_start"]).dt.total_seconds() / 60).round(1)

    handoff = df.groupby("case_id").apply(role_handoffs).reset_index(name="role_handoff_count")

    for name, table in [
        ("activity_counts", activity_counts),
        ("exception_counts", exception_counts),
        ("status_counts", status_counts),
        ("data_origin_counts", data_origin_counts),
        ("case_cycle_times", cycle),
        ("role_handoff_counts", handoff),
    ]:
        table.to_csv(REPORTS_DIR / f"{name}.csv", index=False)

    print(f"Wrote reports to {REPORTS_DIR}")

if __name__ == "__main__":
    main()
