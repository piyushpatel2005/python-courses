import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_validate, GridSearchCV, learning_curve, validation_curve
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
X_train = data[['measurement_a', 'measurement_b']]
groups = data['product_id'].to_numpy()

def entity_folds(X, groups):
    splitter = GroupKFold(n_splits=3)
    return list(splitter.split(X, groups=groups))

if __name__ == "__main__":
    print("Checkpoint:", [(len(tr), len(va)) for tr, va in entity_folds(X_train, groups)])
    print('First validation entities:', np.unique(groups[entity_folds(X_train, groups)[0][1]]))
