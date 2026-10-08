from solution import *
import pandas as pd

def test_01_exercise_pick_counts():
    """Make `by_label(card, label)` return the value at the supplied index label using `loc`."""
    assert by_label(pd.Series([2, 8], index=["z", "a"]), "a") == 8 and by_label(pd.Series([19, 5], index=[20, 10]), 20) == 19

def test_02_exercise_pick_counts():
    """Make `by_position(card, position)` return the value at the supplied integer position using `iloc`."""
    assert by_position(pd.Series([2, 8], index=["z", "a"]), 0) == 2 and by_position(pd.Series([19, 5], index=[20, 10]), 1) == 5

