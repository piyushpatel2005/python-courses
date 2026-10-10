import numpy as np

def totals(scores):
    round_totals = np.sum(scores, axis=0)
    player_totals = np.sum(scores, axis=1)
    return round_totals, player_totals

print(totals(np.array([[4, 8, 2], [6, 3, 7]])))
