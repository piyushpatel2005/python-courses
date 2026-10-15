from solution import *


def test_loan_period_setter_validates_before_storing():
    prop = vars(Tool).get("loan_days")
    assert isinstance(prop, property) and prop.fset is not None, "Add a setter to the loan_days property."
    first, second = Tool(7), Tool(2)
    for valid in (1, 14, 3):
        first.loan_days = valid
        assert first.loan_days == valid and second.loan_days == 2
        for invalid in (0, -1, -20):
            try:
                first.loan_days = invalid
            except ValueError:
                pass
            else:
                assert False, "Reject zero and negative periods with ValueError."
            assert first.loan_days == valid, "Validate before overwriting the previous period."
    for invalid in (0, -8):
        try:
            Tool(invalid)
        except ValueError:
            pass
        else:
            assert False, "Construction must use the same validation rule."
