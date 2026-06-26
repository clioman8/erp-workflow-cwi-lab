"""
Generate a starter Markdown CWI report from analysis outputs.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = BASE_DIR / "reports"
OUT = REPORTS_DIR / "sample_cwi_report.md"

def read_csv(name):
    path = REPORTS_DIR / f"{name}.csv"
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

def md_table(df, max_rows=10):
    if df.empty:
        return "_No data available._"
    return df.head(max_rows).to_markdown(index=False)

def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    sections = [
        "# Sample CWI Report",
        "",
        "## 1. Overview",
        "",
        "This report summarizes starter CWI metrics from the synthetic integrated ERP workflow event log.",
        "",
        "## 2. Activity Counts",
        md_table(read_csv("activity_counts")),
        "",
        "## 3. Exception Counts",
        md_table(read_csv("exception_counts")),
        "",
        "## 4. Case Cycle Times",
        md_table(read_csv("case_cycle_times")),
        "",
        "## 5. Role Handoff Counts",
        md_table(read_csv("role_handoff_counts")),
        "",
        "## 6. Interpretation",
        "",
        "CWI interprets ERP workflow behavior as combinations of activities, roles, constraints, exceptions, and operational outcomes.",
    ]

    OUT.write_text("\\n".join(sections), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
