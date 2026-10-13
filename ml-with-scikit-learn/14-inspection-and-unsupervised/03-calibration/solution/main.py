import numpy as np
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedKFold, train_test_split
import pandas as pd

table = pd.read_csv('checkout-measurements.csv')
X = table[['basket_index', 'item_count_index', 'category_index']]
y = table['returned']
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=17)

def fit_calibrated(X, y):
    folds = StratifiedKFold(n_splits=3, shuffle=True, random_state=17)
    return CalibratedClassifierCV(LinearSVC(dual="auto", random_state=17),
        method="sigmoid", cv=folds, ensemble=True, n_jobs=1).fit(X, y)

model = fit_calibrated(X_train, y_train)
if model is not None:
    probabilities = model.predict_proba(X_valid)[:, 1]
    observed, predicted = calibration_curve(y_valid, probabilities, n_bins=3)
    print("Bin mean probabilities:", predicted)
    print("Bin positive fractions:", observed)
    print("Uniform bin counts:", np.histogram(probabilities, bins=[0,1/3,2/3,1])[0])
