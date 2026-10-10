import numpy as np
from solution import *


def test_describe_a_series():
    assert np.isclose(spread, np.std(temperatures)) and not np.isclose(spread, np.mean(temperatures))
    varied = _with_inputs({'temperatures': 'np.array([2., 2., 8., 8.])'})["spread"]
    assert np.shape(varied) == np.shape(3), "Keep the expected result shape."
    assert np.allclose(varied, 3), "Apply the operation to the array, not fixed output values."


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
