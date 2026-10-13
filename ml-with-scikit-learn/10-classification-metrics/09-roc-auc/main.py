import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
import pandas as pd

data = pd.read_csv('observations.csv', float_precision='round_trip')
X_fixture = data[['measurement_a', 'measurement_b', 'measurement_c']]
truth = data['truth']
predicted = data['predicted']
scores = data['score']

def rank_auc(truth, scores, positive):
    binary = np.asarray(truth) == positive
    return roc_auc_score(binary, np.asarray(scores) >= 0.5)

if __name__ == "__main__":
    print("Checkpoint:", rank_auc(truth, scores, 1))
