from solution import *


def test_behavior():
    """Run a scripted shopping session."""
    shop = Shop(Catalog([Product("P", "Pen", 50)]))
    assert run_session(shop, []) == []
    responses = run_session(shop, ["checkout", "add P 2", "checkout", "track O1", " quit ", "add P 9"])
    assert responses == ["Error: cart is empty", "Added P x 2", "Created O1", "O1: placed"]
    assert shop.cart.lines == {}
    assert run_session(shop, ["show absent", "orders"]) == ["Error: 'absent'", "O1"]
    commands = iter(["orders", " quit ", "add P 9"])
    assert run_session(shop, commands) == ["O1"]
    assert next(commands, None) == "add P 9", "Stop consuming commands at quit"
    assert shop.cart.lines == {}
    class Broken:
        def execute(self, command):
            raise RuntimeError("bug")
    try:
        run_session(Broken(), ["products"])
    except RuntimeError:
        pass
    else:
        assert False, "Do not hide programming failures"
