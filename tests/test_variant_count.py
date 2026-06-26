from pathlib import Path
import pandas as pd

def test_variant_count_positive():
    root = Path(__file__).resolve().parents[1]
    path = root / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
    df = pd.read_csv(path)
    assert df["case_id"].nunique() >= 3
    variants = df.groupby("case_id")["activity"].apply(lambda s: " > ".join(s))
    assert len(variants) == df["case_id"].nunique()
