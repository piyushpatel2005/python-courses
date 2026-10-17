import pandas as pd
import matplotlib.pyplot as plt

def library_totals(frame):
    return frame['visits']

def library_bars(frame):
    fig, ax = plt.subplots()
    ax.set(title='Library visits by branch')
    return fig, ax

library = pd.DataFrame({'branch':['East','West','East',None], 'visits':[30,42,14,8]})
fig, ax = library_bars(library)
