from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_statement_report():
    """Read current balances in sorted ID order without mutation"""
    registry = AccountRegistry()
    assert registry.statement() == "No accounts registered."
    savings = SavingsAccount("Uma", 10000, 300)
    current = CurrentAccount("Val", 100, 200)
    fixed = FixedDeposit("Wes", 5000, 400)
    base = Account("Xiu", 1)
    for key, account in [("S", savings), ("F", fixed), ("C", current), ("A", base)]:
        registry.add(key, account)
    savings.deposit(1000)
    savings.apply_interest(InterestCalculator(), 12)
    current.withdraw(300)
    fixed.apply_interest(InterestCalculator(), 6)
    before = [(key, account.balance_cents) for key, account in registry.accounts.items()]
    expected = "A | Xiu | 1 cents\nC | Val | -200 cents\nF | Wes | 5100 cents\nS | Uma | 11330 cents"
    assert registry.statement() == expected
    assert registry.statement() == expected
    assert [(key, account.balance_cents) for key, account in registry.accounts.items()] == before
    current.deposit(201)
    assert "C | Val | 1 cents" in registry.statement().splitlines()
    one = AccountRegistry()
    one.add("only", Account("Yara"))
    assert one.statement() == "only | Yara | 0 cents"
