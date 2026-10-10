from solution import *
import pandas as pd

import ast
from pathlib import Path
import solution as submitted

def _tree():
    return ast.parse(Path(submitted.__file__).read_text())

def _uses_attribute(function, attribute):
    nodes = [node for node in _tree().body if isinstance(node, ast.FunctionDef) and node.name == function]
    assert nodes and any(isinstance(node, ast.Attribute) and node.attr == attribute for node in ast.walk(nodes[0])), f"Use {attribute} inside {function}."


def test_01_arrival_labels():
    """Return the Index belonging to a Series of these counts."""
    _uses_attribute("arrival_labels", "Series")
    _uses_attribute("arrival_labels", "index")
    for values in [[], [9], [6, 2, 5], [1, 4, 8, 10]]:
        actual = arrival_labels(values)
        assert isinstance(actual, pd.Index), "Return the Index, not a list or a Series."
        pd.testing.assert_index_equal(actual, pd.Series(values).index)
