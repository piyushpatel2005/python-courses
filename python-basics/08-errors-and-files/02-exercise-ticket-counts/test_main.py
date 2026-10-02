import ast
import inspect
import textwrap
from solution import charge_value, charge_label

def test_charge_value():
    assert charge_value("5") == 5
    assert charge_value("faded") == 0
    tree = ast.parse(textwrap.dedent(inspect.getsource(charge_value)))
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch the specific ValueError."

def test_charge_label():
    assert charge_label("2") == "Charge: 2"
    assert charge_label("blurred") == "Charge: 0"
    original = charge_label.__globals__["charge_value"]
    calls = []
    def tracked(text):
        calls.append(text)
        return 37
    try:
        charge_label.__globals__["charge_value"] = tracked
        assert charge_label("new reading") == "Charge: 37"
        assert calls == ["new reading"], "Build the label using charge_value(text)."
    finally:
        charge_label.__globals__["charge_value"] = original
