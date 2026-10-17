import pandas as pd
import matplotlib.pyplot as plt

def survey_intervals(frame):
    fig, ax = plt.subplots()
    ax.errorbar(frame['day'], frame['score'], yerr=frame['margin'], fmt='o-', capsize=5, color='#347f9a')
    ax.set(title='Library survey estimates', ylabel='Survey score (points)', xlabel='Day')
    return fig, ax

survey = pd.DataFrame({'day': ['Mon', 'Tue'], 'score': [72, 75], 'margin': [3, 5]})
fig, ax = survey_intervals(survey)
