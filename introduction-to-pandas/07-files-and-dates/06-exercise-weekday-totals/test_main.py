from solution import *

def test_01_weekday_totals():
    """Group changing dates by weekday and add visits"""
    for dates, visits, expected in [
        (["2026-09-07", "2026-09-08", "2026-09-14"], [3, 7, 5], {"Monday": 8, "Tuesday": 7}),
        (["2025-12-26", "2026-01-02", "2026-01-03"], [4, 6, 2], {"Friday": 10, "Saturday": 2}),
        (["2026-09-07", None], [3, 99], {"Monday": 3}),
    ]:
        frame = pd.DataFrame({"visited_on": pd.to_datetime(dates), "visits": visits})
        assert visitors_by_weekday(frame).to_dict() == expected
