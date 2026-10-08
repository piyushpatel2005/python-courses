from solution import *

def test_01_day_numbers():
    """Extract each row's day, not its month"""
    for dates, days in [(["2026-09-04", "2026-09-18"], [4, 18]), (["2025-12-31", "2025-01-02"], [31, 2])]:
        frame = pd.DataFrame({"arrived_on": pd.to_datetime(dates)})
        assert delivery_days(frame).tolist() == days
