import numpy as np
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

table = pd.read_csv('checkout-measurements.csv')
X = table[['basket_index', 'item_count_index', 'category_index']]
y = table['returned']
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=17)
model = LogisticRegression(n_jobs=1).fit(X_train,y_train)

def inspect_features(model, X_valid, y_valid):
    return permutation_importance(model, X_valid, y_valid, scoring='accuracy',
                                  n_repeats=3, random_state=17, n_jobs=1)

result = inspect_features(model,X_valid,y_valid)
if result is not None:
    print("Baseline validation accuracy:",model.score(X_valid,y_valid))
    print("Score decreases:",result.importances)
    print("Mean decreases:",result.importances_mean)
