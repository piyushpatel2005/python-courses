from solution import *
import pandas as pd

def test_01_add_a_calculated_column():
    """Change the second `price` from 2 to 4 so the second `total` becomes 24."""
    assert table["total"].tolist() == [15, 24] and table["price"].tolist() == [5, 4]

