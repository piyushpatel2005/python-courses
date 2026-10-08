from solution import *
import pandas as pd

def test_01_loc_and_iloc_table_cells():
    """Set `chosen` to the second row’s `sold` count using `iloc`."""
    assert chosen == 11 and table.index.tolist() == [20, 10]

