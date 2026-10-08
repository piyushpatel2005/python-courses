from solution import *
import pandas as pd

def test_01_exercise_select_columns():
    """Make `one_field(table, name)` return the named column as a Series."""
    assert isinstance(one_field(pd.DataFrame({"x": [4, 7], "y": [8, 9]}), "y"), pd.Series) and one_field(pd.DataFrame({"x": [4, 7], "y": [8, 9]}), "y").tolist() == [8, 9] and one_field(pd.DataFrame({"x": [4, 7], "y": [8, 9]}), "x").name == "x"

def test_02_exercise_select_columns():
    """Make `report_fields(table, names)` return a DataFrame with precisely those columns in the requested order."""
    assert isinstance(report_fields(pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}), ["c", "a"]), pd.DataFrame) and report_fields(pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}), ["c", "a"]).to_dict("list") == {"c": [5, 6], "a": [1, 2]} and report_fields(pd.DataFrame({"a": [1]}), ["a"]).columns.tolist() == ["a"]

