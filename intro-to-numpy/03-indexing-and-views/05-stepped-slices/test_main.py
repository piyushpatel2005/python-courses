from solution import *
import numpy as np

def test_slice_assignment():
    """Replace odd-indexed samples"""
    assert np.array_equal(pulses, [10, -1, 12, -1, 14, -1])
    changed = _with_fixture('pulses', [20, 21, 22, 23, 24, 25])
    assert np.array_equal(changed['pulses'], [20, -1, 22, -1, 24, -1]), "Replace only the selected slots"


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
