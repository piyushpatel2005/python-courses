from solution import *

def test_01_left_join_variable_directory():
    """Preserve sales while looking up stall names by ID"""
    for ids, directory, expected in [
        (["B", "A", "Z"], [("A", "Apples", "East"), ("B", "Bread", "West")], ["Bread", "Apples", None]),
        (["Y", "X", "Y"], [("X", "Honey", "North"), ("Y", "Tea", "South")], ["Tea", "Honey", "Tea"]),
    ]:
        selected = pd.DataFrame({"sale_id": list(range(len(ids))), "stall_id": ids, "revenue": [3] * len(ids)})
        stalls = pd.DataFrame(directory, columns=["stall_id", "stall_name", "neighborhood"])
        before_sales, before_stalls = selected.copy(deep=True), stalls.copy(deep=True)
        result = attach_stalls(selected, stalls)
        assert result.sale_id.tolist() == list(range(len(ids)))
        assert result.stall_id.tolist() == ids
        assert "neighborhood" in result.columns
        assert len(result) == len(ids)
        neighborhoods = dict((stall_id, neighborhood) for stall_id, _, neighborhood in directory)
        for actual, stall_id in zip(result.neighborhood, ids):
            expected_neighborhood = neighborhoods.get(stall_id)
            assert (pd.isna(actual) if expected_neighborhood is None else actual == expected_neighborhood)
        for actual, name in zip(result.stall_name, expected):
            assert (pd.isna(actual) if name is None else actual == name)
        pd.testing.assert_frame_equal(selected, before_sales)
        pd.testing.assert_frame_equal(stalls, before_stalls)
