from solution import *
import pandas as pd

def test_integer_tickets():
    """Invalid numeric text becomes zero in an integer Series"""
    pd.testing.assert_series_equal(result, pd.to_numeric(counts["tickets"], errors="coerce").fillna(0).astype(int))
    changed = _rerun_with_fixture('counts', 'pd.DataFrame({"station": list("ABCD"), "tickets": ["31", "", "0", "-2"]}, index=list("wxyz"))')
    pd.testing.assert_series_equal(changed["result"], pd.to_numeric(changed["counts"]["tickets"], errors="coerce").fillna(0).astype(int))
    _uses('to_numeric')


def _rerun_with_fixture(name, expression):
    # Run the submitted source, replacing only its supplied input fixture.
    import ast
    import contextlib
    import io
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            node.value = ast.parse(expression, mode="eval").body
            found = True
            break
    assert found, "Keep the supplied input table so your selection can be checked on different records."
    namespace = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(ast.fix_missing_locations(tree), "<changed-input>", "exec"), namespace)
    return namespace


def _uses(attribute, function=None):
    import ast
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    if function:
        tree = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function)
    assert any(isinstance(n, ast.Attribute) and n.attr == attribute for n in ast.walk(tree)), "Use " + attribute + " for this task, rather than a fixed answer."
