from solution import *

def test_01_enrich_variable_rows():
    """Compute revenue and day labels on every supplied row"""
    for units, prices, dates, revenues in [
        ([3, 4], [2.5, 4.0], ["2026-09-05", "2026-09-07"], [7.5, 16.0]),
        ([5, 1], [1.25, 0.0], ["2025-01-31", "2025-02-01"], [6.25, 0.0]),
    ]:
        source = pd.DataFrame({"sale_id": [1, 2], "units": units, "unit_price": prices, "sold_at": pd.to_datetime(dates)})
        original = source.copy(deep=True)
        result = enrich_sales(source)
        assert result.revenue.tolist() == revenues
        assert result.day.tolist() == dates
        assert list(result.columns) == list(source.columns) + ["revenue", "day"]
        pd.testing.assert_frame_equal(source, original)
