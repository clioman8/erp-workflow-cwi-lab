"""
Generate a starter integrated synthetic ERP event log for CWI analysis.
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
OUT = BASE_DIR / "data" / "event_logs" / "synthetic_integrated_event_log.csv"

ROWS = [
    ["P2P-001","2026-06-20 09:00:00","P2P","Purchase Order Created","buyer","CWI26_PO_001",1,"CWI26_VENDOR_A","CWI26_RAW","completed","","ACT-0020","ecount_reconstructed"],
    ["P2P-001","2026-06-20 10:00:00","P2P","Goods Received","warehouse_operator","CWI26_RM_PCB",20,"CWI26_VENDOR_A","CWI26_RAW","completed","","ACT-0026","ecount_reconstructed"],
    ["MFG-001","2026-06-20 13:00:00","Manufacturing","Work Order Created","production_planner","CWI26_WO_001",1,"","CWI26_WIP","completed","","ACT-0040","ecount_reconstructed"],
    ["MFG-001","2026-06-20 13:30:00","Manufacturing","Production Receipt Created","production_operator","CWI26_FG_KIT",10,"CWI26_WIP","CWI26_FG","completed","","ACT-0046","ecount_reconstructed"],
    ["O2C-001","2026-06-20 15:00:00","O2C","Sales Order Received","sales_operator","CWI26_SO_001",1,"CWI26_CUSTOMER_A","CWI26_FG","completed","","ACT-0050","ecount_reconstructed"],
    ["O2C-001","2026-06-20 15:20:00","O2C","Goods Issued","warehouse_operator","CWI26_FG_KIT",6,"CWI26_FG","CWI26_CUSTOMER_A","completed","","ACT-0052","ecount_reconstructed"],
]

COLS = ["case_id","timestamp","process","activity","actor_role","object_code","quantity","from_location","to_location","status","exception_type","source_action_id","data_origin"]

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(ROWS, columns=COLS)
    df.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
