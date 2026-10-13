import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_validate, GridSearchCV, learning_curve, validation_curve
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
FEATURE_COLUMNS = ['measurement_a', 'measurement_b', 'measurement_c']
X_train = data[FEATURE_COLUMNS]
y_train = data['target']

def evaluate_folds(X, y):
    folds = list(KFold(n_splits=3, shuffle=True, random_state=17).split(X))
    result = cross_validate(Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler()), ('ridge', Ridge())]), X, y, cv=folds, scoring='neg_mean_absolute_error', n_jobs=1, return_estimator=True)
    return folds, result['test_score'], result['estimator']

if __name__ == "__main__":
    print("Checkpoint:", evaluate_folds(X_train, y_train)[1])
