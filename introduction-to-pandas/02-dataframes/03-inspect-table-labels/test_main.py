from solution import *
import pandas as pd

def test_01_inspect_table_labels():
    """Replace row label `unknown` with `late` in `table`."""
    assert table.index.tolist() == ["early", "late"] and table.columns.tolist() == ["stall", "sold"] and pd.api.types.is_integer_dtype(table["sold"])

