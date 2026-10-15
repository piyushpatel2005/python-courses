class Account:
    def __init__(self, owner, balance_cents=0):
        if type(balance_cents) is not int or balance_cents < 0:
            raise ValueError("Opening balance must be nonnegative integer cents")
        self.owner = owner
        self._balance_cents = balance_cents

    @property
    def balance_cents(self):
        return self._balance_cents

    def deposit(self, amount_cents):
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("Deposit must be positive integer cents")
        self._balance_cents += amount_cents
        return self.balance_cents

    def withdraw(self, amount_cents):
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("Withdrawal must be positive integer cents")
        if amount_cents > self.balance_cents:
            raise ValueError("Insufficient balance")
        self._balance_cents -= amount_cents
        return self.balance_cents


class SavingsAccount(Account):
    def __init__(self, owner, balance_cents=0, rate_bps=300):
        if type(rate_bps) is not int or rate_bps < 0:
            raise ValueError("Rate must be nonnegative integer basis points")
        super().__init__(owner, balance_cents)
        self.rate_bps = rate_bps

    def apply_interest(self, calculator, months):
        earned = calculator.calculate(self.balance_cents, self.rate_bps, months)
        if earned > 0:
            self.deposit(earned)
        return earned


class CurrentAccount(Account):
    def __init__(self, owner, balance_cents=0, overdraft_cents=0):
        if type(overdraft_cents) is not int or overdraft_cents < 0:
            raise ValueError("Overdraft must be nonnegative integer cents")
        super().__init__(owner, balance_cents)
        self.overdraft_cents = overdraft_cents

    def withdraw(self, amount_cents):
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("Withdrawal must be positive integer cents")
        if self.balance_cents - amount_cents < -self.overdraft_cents:
            raise ValueError("Overdraft limit exceeded")
        self._balance_cents -= amount_cents
        return self.balance_cents


class FixedDeposit(SavingsAccount):
    def withdraw(self, amount_cents):
        raise ValueError("Fixed deposit is locked")


class InterestCalculator:
    def calculate(self, principal_cents, rate_bps, months):
        for value in (principal_cents, rate_bps, months):
            if type(value) is not int or value < 0:
                raise ValueError("Interest inputs must be nonnegative integers")
        return principal_cents * rate_bps * months // 120000


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account_id, account):
        if account_id in self.accounts:
            raise ValueError("Account ID already registered")
        self.accounts[account_id] = account
        return len(self.accounts)

if __name__ == "__main__":
    account = Account("Mira", 1250)
    print("Opening cents:", getattr(account, "balance_cents", "unfinished"))

    deposit_account = Account("Mira", 1250)
    print("After deposit:", deposit_account.deposit(250))

    withdrawal_account = Account("Mira", 1500)
    print("After withdrawal:", withdrawal_account.withdraw(400))

    savings = SavingsAccount("Mira", 10000)
    print("Savings rate:", getattr(savings, "rate_bps", "unfinished"))

    current = CurrentAccount("Mira", 200, 500)
    print("Current cents:", current.withdraw(700))

    fixed = FixedDeposit("Mira", 20000, 450)
    try:
        fixed.withdraw(1)
        print("Fixed deposit: unfinished")
    except ValueError:
        print("Fixed deposit: locked")

    calculator = InterestCalculator()
    print("Interest cents:", calculator.calculate(20000, 600, 3))

    credited = SavingsAccount("Mira", 10000, 300)
    earned = credited.apply_interest(InterestCalculator(), 12)
    print("Credited:", earned, "Balance:", credited.balance_cents)

    registry = AccountRegistry()
    print("Account count:", registry.add("S-1", SavingsAccount("Mira", 10000)))
