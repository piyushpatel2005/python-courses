from solution import *

def test_01_sorted_grouped_bars():
    """Sum duplicate items and make one mark per unit"""
    for frame, expected in [
        (pd.DataFrame({"item": ["Jam", "Tea", "Jam"], "units": [2, 1, 3]}), "Jam: #####\nTea: #"),
        (pd.DataFrame({"item": ["Tea", "Bread", "Bread"], "units": [3, 2, 1]}), "Bread: ###\nTea: ###"),
    ]:
        assert item_bars(frame) == expected
