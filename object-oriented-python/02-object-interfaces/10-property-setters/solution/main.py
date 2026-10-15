class Tool:
    def __init__(self, loan_days):
        self.loan_days = loan_days

    @property
    def loan_days(self):
        return self._loan_days

    @loan_days.setter
    def loan_days(self, value):
        if value <= 0:
            raise ValueError("loan_days must be positive")
        self._loan_days = value


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = Tool(7)
        sample.loan_days = 14
        print("Accepted period:", sample.loan_days)
        try:
            sample.loan_days = 0
        except ValueError:
            print("Invalid period rejected")
        print("Period after rejection:", sample.loan_days)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
