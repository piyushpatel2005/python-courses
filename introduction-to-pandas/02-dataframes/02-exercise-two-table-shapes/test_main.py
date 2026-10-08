from solution import *
import pandas as pd

def test_01_exercise_two_table_shapes():
    """Make `from_columns(columns)` return a DataFrame built from the supplied dictionary of column lists."""
    assert isinstance(from_columns({"fruit": ["fig", "pear"], "boxes": [2, 7]}), pd.DataFrame) and from_columns({"fruit": ["fig", "pear"], "boxes": [2, 7]}).to_dict("list") == {"fruit": ["fig", "pear"], "boxes": [2, 7]} and from_columns({"price": [5]}).to_dict("list") == {"price": [5]}

def test_02_exercise_two_table_shapes():
    """Make `from_records(records)` return a DataFrame built from the supplied list of row dictionaries."""
    assert isinstance(from_records([{"name": "tea", "sold": 4}, {"name": "jam", "sold": 8}]), pd.DataFrame) and from_records([{"name": "tea", "sold": 4}, {"name": "jam", "sold": 8}]).to_dict("records") == [{"name": "tea", "sold": 4}, {"name": "jam", "sold": 8}] and from_records([{"day": "Fri"}]).columns.tolist() == ["day"]

