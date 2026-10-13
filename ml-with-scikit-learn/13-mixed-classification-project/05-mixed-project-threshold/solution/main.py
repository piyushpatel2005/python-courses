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

def tune_model(train):
    search = GridSearchCV(
        build_model(), {'logistic__C': [0.2, 2.0]},
        scoring='f1_macro',
        cv=StratifiedKFold(3, shuffle=True, random_state=17),
        refit=True, n_jobs=1,
    )
    return search.fit(train[FEATURES], train['flagged'])

def choose_threshold(model, validation):
    positive_index = list(model.classes_).index(1)
    scores = model.predict_proba(validation[FEATURES])[:, positive_index]
    truth = validation['flagged'].to_numpy()
    rows = []
    for threshold in [0.25, 0.5, 0.75]:
        predicted = scores >= threshold
        precision = precision_score(truth, predicted, zero_division=0)
        recall = recall_score(truth, predicted, zero_division=0)
        rows.append((threshold, precision, recall))
    feasible = [row for row in rows if row[2] >= 0.6]
    if feasible:
        return max(feasible, key=lambda row: (row[1], row[0]))[0]
    return max(rows, key=lambda row: (row[2], row[1], -row[0]))[0]


if __name__ == '__main__':
    data = make_analogue()
    train = data.iloc[:18].copy()
    validation = data.iloc[18:24].copy()
    test = data.iloc[24:].copy()
    model = tune_model(train).best_estimator_
    print('Threshold:', choose_threshold(model, validation))
    from types import SimpleNamespace
    boundary = pd.DataFrame({'weight_kg': [0.5, 0.75, 0.2], 'width_cm': 1., 'material': 'wood', 'flagged': [1, 1, 0]})
    probe_model = SimpleNamespace(classes_=np.array([0, 1]), predict_proba=lambda X: np.column_stack([1-X.weight_kg, X.weight_kg]))
    print('Boundary probe:', choose_threshold(probe_model, boundary))
