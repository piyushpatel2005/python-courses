from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_account_registry():
    """Register object identities without overwriting an ID"""
    registry = AccountRegistry()
    other = AccountRegistry()
    a = Account("Paz", 10)
    b = CurrentAccount("Quin", 20, 30)
    assert registry.add("B", a) == 1
    assert registry.add("A", b) == 2
    assert registry.accounts["B"] is a and registry.accounts["A"] is b
    for replacement in [a, b, FixedDeposit("Rae", 40)]:
        _expect_value_error(lambda: registry.add("B", replacement))
        assert registry.accounts == {"B": a, "A": b}
    assert registry.add("C", a) == 3
    a.deposit(5)
    assert registry.accounts["B"].balance_cents == 15
    assert registry.accounts["C"] is a
    assert other.accounts == {}
