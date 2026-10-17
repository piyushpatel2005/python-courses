import pandas as pd
import matplotlib.pyplot as plt

def plot_canopy_temperature(frame):
    fig, ax = plt.subplots()
    return fig, ax

fig, ax = plot_canopy_temperature(pd.DataFrame({"canopy_pct": [30, 70], "temp_c": [29, 23]}))
