from solution import *
import numpy as np

def test_band():
    """Keep values between five and ten"""
    assert np.array_equal(usable, [False, True, True, False])
    assert usable.dtype.kind == "b", "Keep a boolean mask."
    varied = _with_inputs({'bands': 'np.array([4, 5, 9, 10, 11])'})["usable"]
    assert np.shape(varied) == np.shape([False, True, True, True, False]), "Keep the expected result shape."
    assert np.allclose(varied, [False, True, True, True, False]), "Apply the operation to the array, not fixed output values."
    assert isinstance(usable, np.ndarray), "Keep the result as a NumPy array."


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
