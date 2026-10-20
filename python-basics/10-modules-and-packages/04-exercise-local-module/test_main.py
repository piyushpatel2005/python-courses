import ast
import inspect
import solution
from solution import tax_for_order

def test_module_import():
    """Import sales_tax from the local tax_rules module."""
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.ImportFrom)
        and node.module == "tax_rules"
        and any(alias.name == "sales_tax" and alias.asname is None for alias in node.names)
        for node in tree.body
    ), "Import sales_tax from tax_rules in main.py."
    assert callable(solution.sales_tax)

def test_tax_for_order():
    """Delegate the calculation to sales_tax."""
    original = solution.sales_tax
    calls = []
    def tracked(subtotal):
        calls.append(subtotal)
        return original(subtotal)
    try:
        solution.sales_tax = tracked
        assert tax_for_order(40) == 4.0
        assert tax_for_order(100) == 10.0
        assert tax_for_order(0) == 0.0
        assert calls == [40, 100, 0], "Call sales_tax(subtotal)."
    finally:
        solution.sales_tax = original
