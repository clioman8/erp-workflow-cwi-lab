"""
Detect authority mismatch candidates by comparing actor_role and approval rules.

This starter script flags approval-related events and roles that may
require manager or higher-authority intervention.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EVENT_LOG = BASE_DIR / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
APPROVAL_RULES = BASE_DIR / "data" / "master" / "approval_rules.csv"
OUT = BASE_DIR / "reports" / "authority_mismatch_candidates.csv"

def main():
    df = pd.read_csv(EVENT_LOG)
    rules = pd.read_csv(APPROVAL_RULES)
    approval_exceptions = set(rules["exception_if_delayed"].dropna().unique())
    candidates = df[df["exception_type"].isin(approval_exceptions) | df["activity"].str.contains("Approval", case=False, na=False)].copy()
    candidates["reason"] = "approval-related event or approval-delay exception"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    candidates.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
