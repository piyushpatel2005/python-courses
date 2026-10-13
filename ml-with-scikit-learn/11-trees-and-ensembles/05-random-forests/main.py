import numpy as np
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
FEATURE_COLUMNS = ['measurement_a', 'measurement_b', 'measurement_c']
X_train = data[FEATURE_COLUMNS]
y_train = data['target']
query = X_train.iloc[[1, 7]] + 0.1

def fit_forest(X, y):
    model = RandomForestRegressor(n_estimators=1, max_depth=3, random_state=17, n_jobs=1)
    return model.fit(X, y)

if __name__ == "__main__":
    print("Checkpoint:", fit_forest(X_train, y_train).predict(query))
