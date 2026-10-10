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


def test_01_ends():
    """Return head and tail previews for the supplied amount."""
    _uses_attribute("ends", "head")
    _uses_attribute("ends", "tail")
    table = pd.DataFrame({"x": [4, 8, 12], "y": [7, 2, 5]}, index=["a", "b", "c"])
    for amount in [0, 1, 2, 8]:
        before = table.copy()
        actual = ends(table, amount)
        assert isinstance(actual, tuple) and len(actual) == 2, "Return a pair: front preview, then back preview."
        pd.testing.assert_frame_equal(actual[0], table.head(amount))
        pd.testing.assert_frame_equal(actual[1], table.tail(amount))
        pd.testing.assert_frame_equal(table, before)

def test_02_numeric_summary():
    """Return describe's numeric summary without changing the input."""
    _uses_attribute("numeric_summary", "describe")
    for table in [pd.DataFrame({"kind": ["a", "b", "c"], "count": [3, 9, 6]}), pd.DataFrame({"count": [10, 20], "price": [1.5, 4.5]}), pd.DataFrame({"price": [2.0, 7.0, 11.0, 5.0], "stock": [0, 1, 1, 9]})]:
        before = table.copy()
        pd.testing.assert_frame_equal(numeric_summary(table), table.describe())
        pd.testing.assert_frame_equal(table, before)
