import pandas as pd
import matplotlib.pyplot as plt

def library_totals(frame):
    return frame.dropna(subset=['branch','visits']).groupby('branch')['visits'].sum().sort_index()

def library_bars(frame):
    totals = library_totals(frame)
    fig, ax = plt.subplots()
    ax.bar(totals.index, totals.values, color='#e6a45c')
    ax.set(title='Library visits by branch', ylabel='Visits')
    ax.set_ylim(bottom=0)
    return fig, ax

library = pd.DataFrame({'branch':['East','West','East',None], 'visits':[30,42,14,8]})
fig, ax = library_bars(library)
