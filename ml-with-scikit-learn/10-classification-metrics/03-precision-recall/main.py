import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
X_fixture = data[['measurement_a', 'measurement_b', 'measurement_c']]
truth = data['truth']
predicted = data['predicted']
scores = data['score']

def measure(truth, predicted, positive):
    policy = 1
    return (precision_score(truth, predicted, pos_label=positive, zero_division=policy),
            recall_score(truth, predicted, pos_label=positive, zero_division=policy))

if __name__ == "__main__":
    print("Checkpoint:", measure(truth, predicted, 1))
    print('No positive decisions:', measure([0, 0], [0, 0], 1))
