from solution import *

def test_01_import_dates():
    """Parse the date column in each CSV"""
    for text, day in [
        ("arrived_on,crate\n2026-09-01,Flowers\n2026-09-02,Herbs\n", 2),
        ("arrived_on,crate\n2025-12-19,Apples\n", 19),
    ]:
        result = read_deliveries(text)
        assert pd.api.types.is_datetime64_any_dtype(result["arrived_on"])
        assert result["arrived_on"].iloc[-1].day == day
