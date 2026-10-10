from solution import *
import numpy as np

def test_wave():
    """Find sine for each angle in radians"""
    assert np.allclose(wave, [0, 1])
    varied = _with_inputs({'angles': 'np.array([np.pi / 6, -np.pi / 2, np.pi])'})["wave"]
    assert np.shape(varied) == np.shape([0.5, -1, 0]), "Keep the expected result shape."
    assert np.allclose(varied, [0.5, -1, 0]), "Apply the operation to the array, not fixed output values."
    assert isinstance(wave, np.ndarray), "Keep the result as a NumPy array."


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
