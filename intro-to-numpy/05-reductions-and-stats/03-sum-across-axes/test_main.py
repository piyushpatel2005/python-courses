import numpy as np
from solution import *


def test_sum_across_axes():
    assert np.array_equal(night_totals, np.sum(grid, axis=1)) and night_totals.shape == (grid.shape[0],)
    varied = _with_inputs({'grid': 'np.array([[1, 2], [3, 4], [8, 1]])'})["night_totals"]
    assert np.shape(varied) == np.shape([3, 7, 9]), "Keep the expected result shape."
    assert np.allclose(varied, [3, 7, 9]), "Apply the operation to the array, not fixed output values."
    assert isinstance(night_totals, np.ndarray), "Keep the result as a NumPy array."


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
