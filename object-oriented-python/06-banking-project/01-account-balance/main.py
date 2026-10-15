class Account:
    def __init__(self, owner, balance_cents=0):
        # TODO: validate the opening balance and store the account data.
        pass

    @property
    def balance_cents(self):
        return self._balance_cents

if __name__ == "__main__":
    account = Account("Mira", 1250)
    print("Opening cents:", getattr(account, "balance_cents", "unfinished"))
