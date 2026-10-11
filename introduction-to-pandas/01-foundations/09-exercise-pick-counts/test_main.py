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


def test_01_by_label():
    """Use loc with the requested label."""
    _uses_attribute("by_label", "loc")
    for card in [pd.Series([2, 8], index=["z", "a"]), pd.Series([19, 5], index=[20, 10])]:
        for label in card.index:
            assert by_label(card, label) == card.loc[label]

def test_02_by_position():
    """Use iloc with the requested position."""
    _uses_attribute("by_position", "iloc")
    for card in [pd.Series([2, 8], index=["z", "a"]), pd.Series([19, 5, 13], index=[20, 10, 0])]:
        for position in range(len(card)):
            assert by_position(card, position) == card.iloc[position]
