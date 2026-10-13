import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_validate, GridSearchCV, learning_curve, validation_curve
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
timestamps = data['date'].to_numpy(dtype='datetime64[D]')
X_train = data[['daily_index']]

def future_folds(X):
    splitter = TimeSeriesSplit(n_splits=3, test_size=4, gap=0)
    return list(splitter.split(X))

if __name__ == "__main__":
    print("Checkpoint:", [(tr[-1], va[0]) for tr, va in future_folds(X_train)])
