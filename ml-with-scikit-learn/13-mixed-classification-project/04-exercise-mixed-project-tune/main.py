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
    # Complete this stage; prior stages remain unchanged.
    return None

if __name__ == '__main__':
    splits = make_splits(make_data())
    search = tune_model(splits['train'])
    print('Selected settings:', search.best_params_ if search is not None else 'Complete tune_model.')
