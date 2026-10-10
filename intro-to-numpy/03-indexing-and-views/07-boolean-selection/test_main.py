from solution import *
import numpy as np

def test_mask():
    """Replace all readings over 20"""
    assert np.array_equal(readings, [8, 0, 16, 0])
    changed = _with_fixture('readings', [29, 20, 4, 21])
    assert np.array_equal(changed['readings'], [0, 20, 4, 0]), "Only values strictly over 20 are flagged"


def _with_fixture(name, values):
    import ast
    import solution as submitted
    with open(submitted.__file__, encoding="utf-8") as source:
        tree = ast.parse(source.read())
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            node.value = ast.parse("np.array(" + repr(values) + ")", mode="eval").body
            found = True
            break
    assert found, "Keep the supplied " + name + " array"
    ns = {}
    exec(compile(ast.fix_missing_locations(tree), "<changed fixture>", "exec"), ns)
    return ns
