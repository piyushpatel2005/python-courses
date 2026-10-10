from solution import *
import pandas as pd

def test_required_email():
    """Remove only rows missing an email"""
    pd.testing.assert_frame_equal(result, signups.dropna(subset=["email"]))
    changed = _rerun_with_fixture('signups', 'pd.DataFrame({"name": list("ABCD"), "email": [None, "", "a@example.test", None], "note": ["ok", None, None, "ok"]}, index=list("wxyz"))')
    pd.testing.assert_frame_equal(changed["result"], changed["signups"].dropna(subset=["email"]))
    _uses('dropna')


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
