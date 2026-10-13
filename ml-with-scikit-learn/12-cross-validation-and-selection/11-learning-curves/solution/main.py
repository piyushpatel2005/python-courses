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

def size_curve(X, y):
    sizes, train_scores, validation_scores = learning_curve(Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler()), ('ridge', Ridge())]), X, y, train_sizes=[0.5, 0.75, 1.0], cv=KFold(3, shuffle=True, random_state=17), scoring='neg_mean_absolute_error', n_jobs=1, shuffle=True, random_state=17)
    return sizes, -train_scores, -validation_scores

if __name__ == "__main__":
    print("Checkpoint:", size_curve(X_train, y_train)[2].mean(axis=1))
