from solution import *

def test_01_audit_selected_rows():
    """Count variable selected rows and unmatched stall names"""
    for rows, expected in [
        ([("Orchard", 7.5), (None, 16.0), ("Tea", 3.0)], {"rows": 3, "unmatched": 1, "revenue": 26.5}),
        ([(None, 1.25), (None, 2.0)], {"rows": 2, "unmatched": 2, "revenue": 3.25}),
    ]:
        joined = pd.DataFrame(rows, columns=["stall_name", "revenue"])
        assert audit_sales(joined) == expected
