"""
Visualize Pascal's Triangle modulo 2 and CWI bitmask parity.

This is a lightweight educational script connecting the senior seminar
idea of digital Pascal patterns to binary workflow scenario encoding.
"""

from pathlib import Path
import math
import matplotlib.pyplot as plt

def pascal_mod2(n_rows=32):
    points_x, points_y = [], []
    for n in range(n_rows):
        for k in range(n + 1):
            if math.comb(n, k) % 2 == 1:
                points_x.append(k - n / 2)
                points_y.append(-n)
    return points_x, points_y

def main():
    x, y = pascal_mod2(32)
    plt.figure(figsize=(8, 7))
    plt.scatter(x, y, s=8)
    plt.title("Pascal Triangle Mod 2 Pattern")
    plt.axis("equal")
    plt.axis("off")
    out = Path(__file__).resolve().parents[1] / "visuals" / "pascal_to_workflow.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
