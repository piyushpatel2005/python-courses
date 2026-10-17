import pandas as pd
import matplotlib.pyplot as plt

def branch_totals(frame):
    totals = frame.groupby('branch')['visits'].sum().sort_index()
    fig, ax = plt.subplots()
    ax.bar(totals.index, totals.values, color='#e6a45c')
    ax.set(title='Visits by library branch', ylabel='Visits')
    ax.set_ylim(bottom=30)
    return fig, ax

library = pd.DataFrame({'branch':['East','West','East'], 'visits':[32,45,39]})
fig, ax = branch_totals(library)
