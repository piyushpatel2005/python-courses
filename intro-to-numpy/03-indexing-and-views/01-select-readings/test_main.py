from solution import *
import numpy as np

def test_selected():
    """Gather the first and third samples"""
    assert np.array_equal(selected, np.array([12, 15]))
    changed = _with_fixture('samples', [30, 40, 50, 60, 70])
    assert np.array_equal(changed['selected'], [30, 50]), "Select from samples rather than typing the result"


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
