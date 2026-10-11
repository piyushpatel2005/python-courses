from solution import *
import numpy as np

def test_row_correction():
    import ast
    function = next(n for n in _source_tree().body if isinstance(n, ast.FunctionDef) and n.name == "row_correction")
    assert any(isinstance(n, ast.Attribute) and n.attr == "newaxis" for n in ast.walk(function)), "Use np.newaxis to form the baseline column."
    """Subtract one baseline from each entire row"""
    assert np.array_equal(row_correction(np.array([[5, 9], [8, 4]]), np.array([1, 3])), [[4, 8], [5, 1]])
    assert np.array_equal(row_correction(np.array([[7, 8, 9], [4, 5, 6]]), np.array([2, 4])), [[5, 6, 7], [0, 1, 2]])

def test_incompatible():
    """Catch only incompatible broadcasting shapes"""
    assert incompatible(np.ones((2, 3)), np.array([1, 2, 3, 4])) is True
    assert incompatible(np.ones((2, 3)), np.array([1, 2, 3])) is False
    assert incompatible(np.ones((3, 2)), np.array([1, 2, 3])) is True
    assert incompatible(np.ones((3, 2)), np.array([[1], [2], [3]])) is False
    assert incompatible(np.ones((2, 3)), np.array([2])) is False
    assert incompatible(np.ones((2, 3)), np.array(2)) is False
    assert incompatible(np.ones((2, 3)), np.ones((4, 3))) is True
    try:
        incompatible(np.ones((2, 3)), np.array(["not a number"]))
    except TypeError:
        pass
    else:
        assert False, "Catch ValueError only; other errors should still be raised."


def _source_tree():
    import ast
    import solution as submitted
    with open(submitted.__file__, encoding="utf-8") as source:
        return ast.parse(source.read())
