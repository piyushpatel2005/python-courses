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

def search_model(X, y):
    model = Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler()), ('ridge', Ridge())])
    search = GridSearchCV(model, {'ridge__alpha': [0.1, 1.0, 10.0]}, cv=KFold(3, shuffle=True, random_state=17), scoring='neg_mean_absolute_error', n_jobs=1, refit=True)
    return search.fit(X, y)

if __name__ == "__main__":
    print("Checkpoint:", search_model(X_train, y_train).best_params_)
