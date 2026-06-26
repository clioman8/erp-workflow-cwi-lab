"""
Ingest sanitized ECOUNT export files.

This script is intentionally conservative. It reads CSV/XLSX files from
ecount_lab/evidence/exports/ and writes cleaned CSV files into data/processed/.

Only sanitized exports should be placed in the exports folder.
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EXPORT_DIR = BASE_DIR / "ecount_lab" / "evidence" / "exports"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

def read_export(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported file type: {path}")

def sanitize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    return df

def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    if not EXPORT_DIR.exists():
        print(f"No export folder found: {EXPORT_DIR}")
        return

    for path in EXPORT_DIR.glob("*"):
        if path.suffix.lower() not in [".csv", ".xlsx", ".xls"]:
            continue
        df = sanitize_columns(read_export(path))
        out = PROCESSED_DIR / f"{path.stem}_processed.csv"
        df.to_csv(out, index=False)
        print(f"Wrote {out}")

if __name__ == "__main__":
    main()
