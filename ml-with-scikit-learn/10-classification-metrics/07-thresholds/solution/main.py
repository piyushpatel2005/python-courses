import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
X_fixture = data[['measurement_a', 'measurement_b', 'measurement_c']]
truth = data['truth']
predicted = data['predicted']
scores = data['score']

def choose_threshold(truth, scores, minimum_recall=0.75):
    candidates = [0.3, 0.5, 0.7]
    rows = []
    for threshold in candidates:
        predicted = np.asarray(scores) >= threshold
        precision = precision_score(truth, predicted, zero_division=0)
        recall = recall_score(truth, predicted, zero_division=0)
        rows.append((threshold, precision, recall))
    feasible = [row for row in rows if row[2] >= minimum_recall]
    if feasible:
        return max(feasible, key=lambda row: (row[1], row[0]))[0]
    return max(rows, key=lambda row: (row[2], row[1], -row[0]))[0]

if __name__ == "__main__":
    print("Checkpoint:", choose_threshold(truth, scores))
    print('Boundary probe:', choose_threshold([1, 1, 0], [0.5, 0.7, 0.2]))
