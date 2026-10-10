from solution import *


def _base():
    return pd.DataFrame({"sale_id": [9, 10, 11, 12], "sold_at": pd.to_datetime(["2024-02-29", "2025-01-02", "2025-02-03", "2026-01-01"]), "units": [2, 3, 4, 5], "unit_price": [1.5, 0.0, 2.0, 4.0]})


def _run(frame):
    before = frame.copy(deep=True)
    result = clean_sales(frame)
    pd.testing.assert_frame_equal(frame, before)
    assert result.index.tolist() == list(range(len(result))), "Return a fresh default index."
    return result


def test_01_first_sale_id():
    """Keep the first row for each repeated sale ID"""
    for ids in [[9, 9, 11, 11], [3, 4, 3, 5]]:
        frame = _base()
        frame["sale_id"] = ids
        actual = _run(frame)
        expected = frame.drop_duplicates("sale_id").reset_index(drop=True)
        pd.testing.assert_frame_equal(actual[frame.columns], expected, check_dtype=False)


def test_02_parse_dates():
    """Convert year-month-day text to datetime values"""
    frame = _base()
    frame["sold_at"] = ["2024-02-29", "2025-01-02", "2025-02-03", "2026-01-01"]
    result = _run(frame)
    assert pd.api.types.is_datetime64_any_dtype(result.sold_at), "Use to_datetime for sold_at."
    assert result.sold_at.dt.day.tolist() == [29, 2, 3, 1]
    # A later dropna task may remove a coerced row; either state is valid here.
    frame.loc[1, "sold_at"] = "not-a-date"
    result = _run(frame)
    assert pd.api.types.is_datetime64_any_dtype(result.sold_at)
    if 10 in result.sale_id.values:
        assert result.loc[result.sale_id == 10, "sold_at"].isna().all()


def test_03_numeric_units():
    """Convert units from numeric text without guessing bad values"""
    frame = _base()
    frame["units"] = ["2", "3", "4", "5"]
    result = _run(frame)
    assert pd.api.types.is_numeric_dtype(result.units)
    assert result.units.tolist() == [2, 3, 4, 5]
    frame.loc[2, "units"] = "bad"
    result = _run(frame)
    if 11 in result.sale_id.values:
        assert result.loc[result.sale_id == 11, "units"].isna().all()


def test_04_numeric_prices():
    """Convert unit prices and keep a valid zero price"""
    frame = _base()
    frame["unit_price"] = ["1.5", "0", "2", "4"]
    result = _run(frame)
    assert pd.api.types.is_numeric_dtype(result.unit_price)
    assert result.unit_price.tolist() == [1.5, 0, 2, 4]
    frame.loc[3, "unit_price"] = "bad"
    result = _run(frame)
    if 12 in result.sale_id.values:
        assert result.loc[result.sale_id == 12, "unit_price"].isna().all()


def test_05_required_values():
    """Remove rows missing a required date or amount"""
    frame = _base()
    frame.loc[0, "sold_at"] = pd.NaT
    frame.loc[1, "units"] = float("nan")
    frame.loc[2, "unit_price"] = float("nan")
    assert _run(frame).sale_id.tolist() == [12]


def test_06_allowed_amounts():
    """Exclude nonpositive units and negative prices, but keep free items"""
    frame = _base()
    frame["units"] = [0, -1, 2, 3]
    frame["unit_price"] = [2, 2, -0.01, 0]
    assert _run(frame).sale_id.tolist() == [12]
