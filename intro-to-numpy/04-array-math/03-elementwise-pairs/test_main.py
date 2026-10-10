from solution import *
import numpy as np

def test_add():
    """Add corresponding entries"""
    assert np.array_equal(combined, [5, 10, 15])
    varied = _with_inputs({'left': 'np.array([2, -3])', 'right': 'np.array([7, 5])'})["combined"]
    assert np.shape(varied) == np.shape([9, 2]), "Keep the expected result shape."
    assert np.allclose(varied, [9, 2]), "Apply the operation to the array, not fixed output values."
    assert isinstance(combined, np.ndarray), "Keep the result as a NumPy array."


def _with_inputs(replacements):
    """Re-run the submitted calculation with another supplied fixture."""
    import ast
    import contextlib
    import io
    import solution as submitted
    with open(submitted.__file__, encoding="utf-8") as source:
        tree = ast.parse(source.read())
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in replacements:
                    node.value = ast.parse(replacements[target.id], mode="eval").body
    ast.fix_missing_locations(tree)
    namespace = {"__name__": "__review_fixture__"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(tree, "<changed fixture>", "exec"), namespace)
    return namespace
