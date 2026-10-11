from solution import *
import numpy as np

def test_view_copy():
    """A slice edit reaches the source, but a copy edit does not"""
    assert np.array_equal(record, [6, 70, 8, 9])
    assert np.shares_memory(record, window)
    assert not np.shares_memory(record, backup)
    assert np.array_equal(window, [70, 8])
    assert np.array_equal(backup, [-1, 8])
    changed = _with_fixture('record', [1, 2, 3, 4])
    assert np.array_equal(changed['record'], [1, 70, 3, 4])
    assert np.shares_memory(changed['record'], changed['window'])
    assert not np.shares_memory(changed['record'], changed['backup'])


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
