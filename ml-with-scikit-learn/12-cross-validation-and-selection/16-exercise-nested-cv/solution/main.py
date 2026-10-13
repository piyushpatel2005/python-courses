import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_validate, GridSearchCV, learning_curve, validation_curve
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
FEATURE_COLUMNS = ['measurement_a', 'measurement_b']
X_train = data[FEATURE_COLUMNS]
y_train = data['target']

def nested_scores(X, y):
    inner = KFold(2, shuffle=True, random_state=17)
    outer = list(KFold(2, shuffle=True, random_state=29).split(X))
    search = GridSearchCV(Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler()), ('ridge', Ridge())]), {'ridge__alpha': [0.1, 10.0]}, cv=inner, scoring='neg_mean_absolute_error', n_jobs=1, refit=True)
    result = cross_validate(search, X, y, cv=outer, scoring='neg_mean_absolute_error', n_jobs=1, return_estimator=True)
    return outer, -result['test_score'], result['estimator']

if __name__ == "__main__":
    print("Checkpoint:", nested_scores(X_train, y_train)[1])
