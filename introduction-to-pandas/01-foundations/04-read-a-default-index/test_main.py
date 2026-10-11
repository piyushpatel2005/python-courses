from solution import *
import pandas as pd

import ast
from pathlib import Path
import solution as submitted

def _tree():
    return ast.parse(Path(submitted.__file__).read_text())



def test_01_default_index():
    """Change the final receipt to 10 and keep the default index."""
    pd.testing.assert_series_equal(receipts, pd.Series([5, 8, 10]))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "Series" and not any(k.arg == "index" for k in node.keywords) for node in ast.walk(_tree())), "Build the Series without an index argument."
