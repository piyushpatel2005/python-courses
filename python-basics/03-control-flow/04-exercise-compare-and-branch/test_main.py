import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as _solution


def _tree():
    source_path = _solution.__file__
    assert source_path is not None, "The runner must provide your main.py source."
    return ast.parse(Path(source_path).read_text(encoding="utf-8"))


def _chain():
    branches = [node for node in _tree().body if isinstance(node, ast.If)]
    assert branches, "Add an if statement below the supplied gate_signal line."
    return branches[0]


def _run_with_charge(charge):
    tree = _tree()
    supplied_charge = next(
        (
            node for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "charge_left"
                    for target in node.targets)
        ),
        None,
    )
    assert supplied_charge is not None, "Keep the supplied charge_left assignment."
    supplied_charge.value = ast.Constant(value=charge)
    scope = {}
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(ast.fix_missing_locations(tree), "solution.py", "exec"), scope)
    return scope.get("gate_signal"), output.getvalue().strip()


def _expect(charge, expected):
    signal, output = _run_with_charge(charge)
    assert signal == expected, (
        f"With charge_left = {charge}, set gate_signal to {expected!r}."
    )
    assert output == expected, "Keep print(gate_signal) after the whole branch chain."


def test_sealed_gate():
    """1. Seal the gate when its charge is zero"""
    _chain()
    _expect(0, "Sealed")
    assert _run_with_charge(8)[0] != "Sealed", (
        "Use == 0: a gate with charge remaining should not be Sealed."
    )


def test_flickering_gate():
    """2. Show Flickering for a low positive charge"""
    first = _chain()
    assert first.orelse and isinstance(first.orelse[0], ast.If), (
        "Add elif charge_left < 4 after the zero-charge branch."
    )
    for charge in (1, 2, 3):
        _expect(charge, "Flickering")
    assert _run_with_charge(4)[0] != "Flickering", (
        "Use < 4, not <= 4: charge 4 belongs to the final branch."
    )


def test_open_gate():
    """3. Open the gate when its charge is at least four"""
    first = _chain()
    assert first.orelse and isinstance(first.orelse[0], ast.If), (
        "Keep the if / elif chain, then add its final else branch."
    )
    low_charge = first.orelse[0]
    assert low_charge.orelse and not isinstance(low_charge.orelse[0], ast.If), (
        "Add an else branch aligned with if and elif."
    )
    for charge in (4, 8, 20):
        _expect(charge, "Open")
    assert _run_with_charge(3)[0] != "Open", (
        "A charge of 3 still belongs to the Flickering branch."
    )
