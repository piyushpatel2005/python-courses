from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_dashboard_sum():
    "Fill the report's `sum` entry by calling the Fenwick range-sum method."
    for values in [[],[8],[6,-3,7,2,9]]:
        dashboard=RangeDashboard(values)
        for left in range(len(values)+1):
            for right in range(left,len(values)+1):
                assert dashboard.report(left,right)['sum']==sum(values[left:right])
        if values:
            dashboard.replace(0,4)
            assert dashboard.report(0,len(values))['sum']==sum(values)-values[0]+4
    expect_error(IndexError,lambda:RangeDashboard([1]).report(0,2))
    dashboard = RangeDashboard([6, 2, 9])
    calls = []
    original = dashboard.sums.range_sum
    def record(left, right):
        calls.append((left, right))
        return original(left, right)
    dashboard.sums.range_sum = record
    assert dashboard.report(1, 3)['sum'] == 11
    assert calls == [(1, 3)]


def test_dashboard_minimum():
    'Fill `minimum` by querying the minimum tree over the same half-open interval.'
    for values in [[],[8],[6,-3,7,2,9]]:
        dashboard,other=RangeDashboard(values),RangeDashboard(values)
        for left in range(len(values)+1):
            for right in range(left,len(values)+1):
                assert dashboard.report(left,right)['minimum']==min(values[left:right],default=float('inf'))
        if values:
            dashboard.replace(0,-10)
            assert dashboard.report(0,len(values))['minimum']==-10
        assert other.report(0,len(values))['minimum']==min(values,default=float('inf'))
    dashboard=RangeDashboard([1,2])
    result=dashboard.report(0,2)
    result['minimum']=999
    assert dashboard.report(0,2)['minimum']==1
    calls = []
    original = dashboard.minimums.query
    def record(left, right):
        calls.append((left, right))
        return original(left, right)
    dashboard.minimums.query = record
    assert dashboard.report(1, 2)['minimum'] == 2
    assert calls == [(1, 2)]
