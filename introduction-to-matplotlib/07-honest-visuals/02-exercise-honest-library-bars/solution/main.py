import pandas as pd
import matplotlib.pyplot as plt

def branch_bars(frame):
    fig, ax = plt.subplots()
    ax.bar(frame['branch'], frame['visits'], color='#347f9a')
    ax.set(title='Library visits by branch', ylabel='Visits')
    ax.set_ylim(bottom=0)
    return fig, ax

library = pd.DataFrame({'branch': ['East', 'West'], 'visits': [42, 67]})
fig, ax = branch_bars(library)
