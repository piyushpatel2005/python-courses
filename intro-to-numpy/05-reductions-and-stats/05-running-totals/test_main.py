import numpy as np
from solution import *


def test_running_totals():
    assert np.array_equal(running, np.cumsum(sightings))
    varied = _with_inputs({'sightings': 'np.array([2, 0, 5])'})["running"]
    assert np.shape(varied) == np.shape([2, 2, 7]), "Keep the expected result shape."
    assert np.allclose(varied, [2, 2, 7]), "Apply the operation to the array, not fixed output values."
    assert isinstance(running, np.ndarray), "Keep the result as a NumPy array."


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
