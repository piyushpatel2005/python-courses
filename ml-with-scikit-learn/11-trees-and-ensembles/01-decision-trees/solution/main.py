import numpy as np
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
FEATURE_COLUMNS = ['measurement_a', 'measurement_b', 'measurement_c']
X_train = data[FEATURE_COLUMNS]
y_train = data['target']
y_train = y_train.astype(int)
query = X_train.iloc[[1, 7]] + 0.1

def fit_tree(X, y):
    model = DecisionTreeClassifier(max_depth=2, random_state=17)
    return model.fit(X, y)

if __name__ == "__main__":
    print("Checkpoint:", fit_tree(X_train, y_train).predict(query))
    print('Depth limit:', fit_tree(X_train, y_train).max_depth)
