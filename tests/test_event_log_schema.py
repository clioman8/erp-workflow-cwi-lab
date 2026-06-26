from pathlib import Path
import pandas as pd

def test_event_log_schema():
    root = Path(__file__).resolve().parents[1]
    path = root / "data" / "event_logs" / "synthetic_integrated_event_log.csv"
    df = pd.read_csv(path)
    expected = [
        "case_id","timestamp","process","activity","actor_role","object_code",
        "quantity","from_location","to_location","status","exception_type",
        "source_action_id","data_origin"
    ]
    assert list(df.columns) == expected
    assert len(df) > 0
