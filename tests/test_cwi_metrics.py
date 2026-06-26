from pathlib import Path
import pandas as pd

def test_scenario_design_hamming_weight():
    root = Path(__file__).resolve().parents[1]
    path = root / "data" / "scenarios" / "scenario_design.csv"
    df = pd.read_csv(path)
    for _, row in df.iterrows():
        bits = str(row["bitmask"])
        assert int(row["hamming_weight"]) == sum(int(ch) for ch in bits)
