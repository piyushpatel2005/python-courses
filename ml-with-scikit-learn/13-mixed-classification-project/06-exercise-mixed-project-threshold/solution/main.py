import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import confusion_matrix, precision_score, recall_score

FEATURES = ['basket_value_usd', 'item_count', 'category']
SNAPSHOT = '2025-04-01'

def make_data():
    """Read the fixed original synthetic table from its real CSV file."""
    return pd.read_csv('orders.csv', float_precision='round_trip')

def make_splits(data):
    """Independent rows: 60% search train, 20% threshold, 20% sealed test."""
    development, test = train_test_split(data, test_size=0.2, random_state=43, stratify=data['returned_30d'])
    train, validation = train_test_split(development, test_size=0.25, random_state=43, stratify=development['returned_30d'])
    return {'train': train.copy(), 'validation': validation.copy(), 'test': test.copy()}

def build_model():
    numeric = Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale', StandardScaler()),
    ])
    categorical = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    preprocess = ColumnTransformer([
        ('numeric', numeric, ['basket_value_usd', 'item_count']),
        ('category', categorical, ['category']),
    ], remainder='drop', n_jobs=1)
    return Pipeline([
        ('preprocess', preprocess),
        ('logistic', LogisticRegression(max_iter=300, n_jobs=1, random_state=43)),
    ])

def tune_model(train):
    search = GridSearchCV(
        build_model(), {'logistic__C': [0.1, 1.0, 10.0]},
        scoring='f1_macro',
        cv=StratifiedKFold(3, shuffle=True, random_state=43),
        refit=True, n_jobs=1,
    )
    return search.fit(train[FEATURES], train['returned_30d'])

def choose_threshold(model, validation):
    positive_index = list(model.classes_).index(1)
    scores = model.predict_proba(validation[FEATURES])[:, positive_index]
    truth = validation['returned_30d'].to_numpy()
    rows = []
    for threshold in [0.3, 0.5, 0.7]:
        predicted = scores >= threshold
        precision = precision_score(truth, predicted, zero_division=0)
        recall = recall_score(truth, predicted, zero_division=0)
        rows.append((threshold, precision, recall))
    feasible = [row for row in rows if row[2] >= 0.75]
    if feasible:
        return max(feasible, key=lambda row: (row[1], row[0]))[0]
    return max(rows, key=lambda row: (row[2], row[1], -row[0]))[0]

if __name__ == '__main__':
    splits = make_splits(make_data())
    model = tune_model(splits['train']).best_estimator_
    threshold = choose_threshold(model, splits['validation'])
    print('Validation threshold:', threshold)
