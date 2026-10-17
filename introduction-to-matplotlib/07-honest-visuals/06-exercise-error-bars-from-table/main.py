import pandas as pd
import matplotlib.pyplot as plt

def survey_intervals(frame):
    fig, ax = plt.subplots()
    ax.set(title='Library survey estimates')
    return fig, ax

survey = pd.DataFrame({'day': ['Mon', 'Tue'], 'score': [72, 75], 'margin': [3, 5]})
fig, ax = survey_intervals(survey)
