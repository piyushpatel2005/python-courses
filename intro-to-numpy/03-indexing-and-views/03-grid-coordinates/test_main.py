from solution import *
import numpy as np

def test_spot():
    """Read row 1, column 1"""
    assert spot == 7
    changed = _with_fixture('grid', [[18, 13, 15], [14, 17, 19]])
    assert changed['spot'] == 17, "Read the cell from grid"


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
