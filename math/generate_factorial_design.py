"""
Generate first-stage CWI factorial scenario design.

The first stage includes:
- baseline: C(6,0)
- single-factor scenarios: C(6,1)
- two-factor scenarios: C(6,2)

Total = 1 + 6 + 15 = 22 scenarios.
"""

from itertools import product
from pathlib import Path
import pandas as pd

FACTORS = ["F1", "F2", "F3", "F4", "F5", "F6"]

def execution_mode(bits):
    if bits[5] == 1:
        return "synthetic_only"
    if bits[4] == 1:
        return "hybrid"
    if sum(bits) == 2:
        return "hybrid"
    return "ecount_observed"

def main():
    rows = []
    for bits in product([0, 1], repeat=len(FACTORS)):
        hamming_weight = sum(bits)
        if hamming_weight <= 2:
            bitmask = "".join(str(b) for b in bits)
            rows.append([
                f"CWI-{bitmask}",
                bitmask,
                hamming_weight,
                *bits,
                execution_mode(bits)
            ])

    df = pd.DataFrame(
        rows,
        columns=["scenario_id", "bitmask", "hamming_weight", *FACTORS, "execution_mode"]
    )

    output = Path(__file__).resolve().parent / "scenario_design.csv"
    df.to_csv(output, index=False)
    print(f"Wrote {output} with {len(df)} scenarios.")

if __name__ == "__main__":
    main()
