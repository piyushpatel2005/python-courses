from solution import *
import pandas as pd

import ast
from pathlib import Path
import solution as submitted

def _tree():
    return ast.parse(Path(submitted.__file__).read_text())


def _rerun(name, expression):
    tree = _tree()
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            node.value = ast.parse(expression, mode="eval").body
            found = True
            break
    assert found, f"Keep the supplied {name} assignment."
    namespace = {}
    exec(compile(ast.fix_missing_locations(tree), str(submitted.__file__), "exec"), namespace)
    return namespace

def test_01_correct_price():
    """Correct the second price and keep total calculated from the inputs."""
    pd.testing.assert_frame_equal(table, pd.DataFrame({"sold": [3, 6], "price": [5, 4], "total": [15, 24]}))
    changed = _rerun("table", 'pd.DataFrame({"sold": [7, 2], "price": [3, 8]}, index=["a", "b"])')
    result = changed["table"]
    pd.testing.assert_series_equal(result["total"], (result["sold"] * result["price"]).rename("total"))
