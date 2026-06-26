"""
Summarize ECOUNT-SAP conceptual crosswalk.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
CROSSWALK = BASE_DIR / "data" / "mappings" / "ecount_sap_process_crosswalk.csv"
OUT = BASE_DIR / "reports" / "ecount_sap_crosswalk_summary.csv"

def main():
    df = pd.read_csv(CROSSWALK)
    summary = df.groupby(["mapping_level", "confidence"]).size().reset_index(name="count")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
