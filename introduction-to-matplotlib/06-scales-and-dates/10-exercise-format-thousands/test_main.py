from solution import *
import pandas as pd

def test_01_changed_counts_stay_numeric():
    _, axis = plot_large_visits(pd.DataFrame({"site": ["Hall", "Garden", "Station"], "visits": [512, 9012, 12750]}))
    assert [t.get_text() for t in axis.get_xticklabels()] == ["Hall", "Garden", "Station"]
    assert [bar.get_height() for bar in axis.patches] == [512, 9012, 12750]

def test_02_thousands_formatter_is_general():
    _, axis = plot_large_visits(pd.DataFrame({"site": ["Hall"], "visits": [1000]}))
    fmt = axis.yaxis.get_major_formatter()
    assert fmt(1250, 0) == "1,250" and fmt(23456, 1) == "23,456"
