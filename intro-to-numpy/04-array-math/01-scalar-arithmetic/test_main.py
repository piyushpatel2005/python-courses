from solution import *
import numpy as np

def test_offset():
    """Double each reading then add four"""
    assert np.array_equal(corrected, [10, 14, 18])
    varied = _with_inputs({'raw': 'np.array([-2, 0, 9])'})["corrected"]
    assert np.shape(varied) == np.shape([-0, 4, 22]), "Keep the expected result shape."
    assert np.allclose(varied, [-0, 4, 22]), "Apply the operation to the array, not fixed output values."
    assert isinstance(corrected, np.ndarray), "Keep the result as a NumPy array."


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
