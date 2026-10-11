from solution import *


def _cases():
    return [pd.DataFrame({"units": [3, 4], "unit_price": [2.5, 4.0], "sold_at": pd.to_datetime(["2026-09-05", "2026-09-07"])}), pd.DataFrame({"units": [5, 1], "unit_price": [1.25, 0.0], "sold_at": pd.to_datetime(["2024-02-29", "2025-01-01"])}, index=[8, 3])]


def _run(frame):
    before = frame.copy(deep=True)
    result = enrich_sales(frame)
    pd.testing.assert_frame_equal(frame, before)
    pd.testing.assert_frame_equal(result[frame.columns], before)
    return result


def test_01_revenue_column():
    """Add row-by-row revenue without requiring the day label"""
    for frame, values in zip(_cases(), [[7.5, 16.0], [6.25, 0.0]]):
        assert _run(frame)["revenue"].tolist() == values


def test_02_day_labels():
    """Format the date label without requiring revenue"""
    for frame, dates in zip(_cases(), [["2026-09-05", "2026-09-07"], ["2024-02-29", "2025-01-01"]]):
        assert _run(frame)["day"].tolist() == dates
