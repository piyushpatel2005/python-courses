from solution import *


def _cases():
    for rows, expected in [
        ([("Orchard", 7.5), (None, 16.0), ("Tea", 3.0)], {"rows": 3, "unmatched": 1, "revenue": 26.5}),
        ([(None, 1.25), (None, 2.0)], {"rows": 2, "unmatched": 2, "revenue": 3.25}),
        ([], {"rows": 0, "unmatched": 0, "revenue": 0.0}),
    ]:
        yield pd.DataFrame(rows, columns=["stall_name", "revenue"]), expected


def test_01_row_count():
    """Count the joined rows"""
    for frame, expected in _cases():
        assert audit_sales(frame).get("rows") == expected["rows"]


def test_02_missing_names():
    """Count missing stall names independently of other audit fields"""
    for frame, expected in _cases():
        assert audit_sales(frame).get("unmatched") == expected["unmatched"]


def test_03_total_revenue():
    """Sum every joined row's revenue"""
    for frame, expected in _cases():
        assert audit_sales(frame).get("revenue") == expected["revenue"]
