import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import confusion_matrix, precision_score, recall_score

FEATURES = ['weight_kg', 'width_cm', 'material']

def make_analogue():
    """Read the fixed original synthetic table from its real CSV file."""
    return pd.read_csv('handling.csv', float_precision='round_trip')

def build_model():
    numeric = Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale', StandardScaler()),
    ])
    categorical = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    preprocess = ColumnTransformer([
        ('numeric', numeric, ['weight_kg', 'width_cm']),
        ('material', categorical, ['material']),
    ], remainder='drop', n_jobs=1)
    return Pipeline([
        ('preprocess', preprocess),
        ('logistic', LogisticRegression(max_iter=300, n_jobs=1, random_state=17)),
    ])


if __name__ == '__main__':
    data = make_analogue()
    train = data.iloc[:18].copy()
    validation = data.iloc[18:24].copy()
    test = data.iloc[24:].copy()
    model = build_model().fit(train[FEATURES], train.flagged)
    print('Unknown-category policy:', model.named_steps['preprocess'].named_transformers_['material'].handle_unknown)
