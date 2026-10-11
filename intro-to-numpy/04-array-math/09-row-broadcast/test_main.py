from solution import *
import numpy as np

def test_broadcast_rows():
    """Subtract the same vector from both rows"""
    assert np.array_equal(adjusted, [[-9, -18, -27], [-6, -15, -24]])
    varied = _with_inputs({'sky': 'np.array([[4, 8, 12], [1, 2, 3]])', 'column_offset': 'np.array([2, 3, 5])'})["adjusted"]
    assert np.shape(varied) == np.shape([[2, 5, 7], [-1, -1, -2]]), "Keep the expected result shape."
    assert np.allclose(varied, [[2, 5, 7], [-1, -1, -2]]), "Apply the operation to the array, not fixed output values."
    assert isinstance(adjusted, np.ndarray), "Keep the result as a NumPy array."


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
