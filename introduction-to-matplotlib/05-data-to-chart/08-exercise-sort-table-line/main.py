import pandas as pd
import matplotlib.pyplot as plt

def plot_parcels(frame):
    fig, ax = plt.subplots()
    return fig, ax

fig, ax = plot_parcels(pd.DataFrame({"day": [3, 1, 2], "parcels": [8, 2, 5]}))
