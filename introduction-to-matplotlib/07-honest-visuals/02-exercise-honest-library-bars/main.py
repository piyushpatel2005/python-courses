import pandas as pd
import matplotlib.pyplot as plt

def branch_bars(frame):
    fig, ax = plt.subplots()
    ax.set(title='Library visits by branch')
    return fig, ax

library = pd.DataFrame({'branch': ['East', 'West'], 'visits': [42, 67]})
fig, ax = branch_bars(library)
