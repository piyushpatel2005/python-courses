import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_validate, GridSearchCV, learning_curve, validation_curve
from sklearn.datasets import make_classification, make_regression, load_iris, load_wine

dataset = load_wine()
X_train, y_train = dataset.data, dataset.target

def evaluate_classes(X, y):
    folds = list(StratifiedKFold(n_splits=3, shuffle=True, random_state=17).split(X, y))
    model = Pipeline([('scale', StandardScaler()), ('logistic', LogisticRegression(max_iter=300, n_jobs=1))])
    result = cross_validate(model, X, y, cv=folds, scoring='f1_macro', n_jobs=1, return_estimator=True)
    return folds, result['test_score'], result['estimator']

if __name__ == "__main__":
    print("Checkpoint:", evaluate_classes(X_train, y_train)[1])
