from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_apply_interest():
    """Delegate once and credit only positive interest"""
    account = SavingsAccount("May", 10000, 300)
    assert account.apply_interest(InterestCalculator(), 12) == 300
    assert account.balance_cents == 10300
    assert account.apply_interest(InterestCalculator(), 12) == 309
    assert account.balance_cents == 10609
    _expect_value_error(lambda: account.apply_interest(InterestCalculator(), -1))
    assert account.balance_cents == 10609
    calls = []
    class CalculatorProbe:
        def __init__(self, result):
            self.result = result
        def calculate(self, principal, rate, months):
            calls.append((principal, rate, months))
            return self.result
    class SavingsProbe(SavingsAccount):
        def __init__(self):
            super().__init__("Probe", 200, 725)
            self.deposits = []
        def deposit(self, amount):
            self.deposits.append(amount)
            return super().deposit(amount)
    probe = SavingsProbe()
    assert probe.apply_interest(CalculatorProbe(7), 5) == 7
    assert calls == [(200, 725, 5)]
    assert probe.balance_cents == 207 and probe.deposits == [7]
    calls.clear()
    assert probe.apply_interest(CalculatorProbe(0), 0) == 0
    assert calls == [(207, 725, 0)] and probe.deposits == [7]
    fixed = FixedDeposit("Noor", 20000, 450)
    assert fixed.apply_interest(InterestCalculator(), 12) == 900
    assert fixed.balance_cents == 20900
    _expect_value_error(lambda: fixed.withdraw(1))
