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


def test_01_first_position():
    """Use iloc to return the first value, regardless of its label."""
    _uses_attribute("first_count", "iloc")
    assert chosen == first_count(card) == 7
    for values, labels in [([31, 7, 14], [20, 10, 30]), ([99, -1, 18], [10, 20, 0]), ([42, 3, 18], ["first", "other", "first"])]:
        assert first_count(pd.Series(values, index=labels)) == values[0]
