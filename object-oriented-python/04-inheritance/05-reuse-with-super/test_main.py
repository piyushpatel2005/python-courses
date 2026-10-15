from solution import *


def test_01_reuse_with_super():
    for code, amount in (("Q8", 200), ("Z1", 0), ("long code", 750)):
        item = InsuredShipment(code, amount)
        assert item.label() == f"Shipment {code} | insured {amount}"
        assert (item.tracking, item.amount) == (code, amount)
    original = Shipment.label
    calls = []
    try:
        def replacement(self):
            calls.append(self.tracking)
            return "Revised " + self.tracking
        Shipment.label = replacement
        assert InsuredShipment("NEW", 12).label() == "Revised NEW | insured 12"
        assert calls == ["NEW"], "Call the shared label exactly once."
    finally:
        Shipment.label = original
    import ast, inspect, textwrap
    source = ast.parse(textwrap.dedent(inspect.getsource(InsuredShipment.label)))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "super" for node in ast.walk(source)), "Reuse the base method through super()."
