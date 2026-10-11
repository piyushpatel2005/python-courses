from solution import *

def test_01_group_variable_totals():
    """Sum neighborhoods and retain unknown labels"""
    for rows, names, units, revenue in [
        ([("South", 2, 4.0), ("North", 3, 7.5), ("South", 4, 8.0)], ["North", "South"], [3, 6], [7.5, 12.0]),
        ([("East", 1, 2.0), (None, 5, 10.0), ("East", 2, 3.0)], ["East", None], [3, 5], [5.0, 10.0]),
        ([(None, 2, 1.5), ("West", 1, 4.0), (None, 3, 2.5)], ["West", None], [1, 5], [4.0, 4.0]),
    ]:
        joined = pd.DataFrame(rows, columns=["neighborhood", "units", "revenue"])
        result = total_by_neighborhood(joined)
        assert list(result.columns) == ["neighborhood", "units", "revenue"]
        assert result.neighborhood.dropna().tolist() == [n for n in names if n is not None]
        if None in names:
            assert pd.isna(result.neighborhood.iloc[-1])
        assert result.units.tolist() == units and result.revenue.tolist() == revenue
        assert result.index.tolist() == list(range(len(result)))
