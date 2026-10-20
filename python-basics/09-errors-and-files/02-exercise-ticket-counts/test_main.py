import ast
import inspect
import textwrap
from solution import quantity_value, quantity_label

def test_quantity_value():
    """Convert valid text and handle ValueError."""
    assert quantity_value("5") == 5
    assert quantity_value("unknown") == 0
    tree = ast.parse(textwrap.dedent(inspect.getsource(quantity_value)))
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch ValueError specifically."

def test_quantity_label():
    """Build the label using quantity_value."""
    assert quantity_label("2") == "Quantity: 2"
    assert quantity_label("invalid") == "Quantity: 0"
    original = quantity_label.__globals__["quantity_value"]
    calls = []
    def tracked(text):
        calls.append(text)
        return 37
    try:
        quantity_label.__globals__["quantity_value"] = tracked
        assert quantity_label("new quantity") == "Quantity: 37"
        assert calls == ["new quantity"], "Call quantity_value(text) to build the label."
    finally:
        quantity_label.__globals__["quantity_value"] = original
