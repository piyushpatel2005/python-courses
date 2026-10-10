import pandas as pd

def category_report(a):
    return a.copy()

a = pd.DataFrame({'category': ['Craft', 'Craft', 'Food'], 'amount': [5.0, None, 9.0]})
print(category_report(a))
