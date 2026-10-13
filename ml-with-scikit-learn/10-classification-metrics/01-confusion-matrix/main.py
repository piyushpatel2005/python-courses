import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
X_fixture = data[['measurement_a', 'measurement_b', 'measurement_c']]
truth = data['truth']
predicted = data['predicted']
scores = data['score']

def summarize(truth, predicted, labels):
    matrix = confusion_matrix(truth, predicted, labels=labels[::-1])
    return matrix, accuracy_score(truth, predicted)

if __name__ == "__main__":
    print("Checkpoint:", summarize(truth, predicted, [0, 1]))
