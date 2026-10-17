from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_note_busiest_hour():
    """Complete `busiest_hour(hours, counts)` to plot the inputs, annotate the first maximum with text `"Peak: {count}"` at `(hour, count)`, place the note at `(hour, count + 3)` with an arrow, and return the figure."""
    try:
        for hours, counts in [([9, 11, 14], [12, 19, 16]), ([7, 12, 16], [21, 8, 6]), ([8, 10, 13], [7, 14, 14])]:
            chart = busiest_hour(hours, counts)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 1
            assert list(axis.lines[0].get_xdata()) == hours
            assert list(axis.lines[0].get_ydata()) == counts
            assert len(axis.texts) == 1
            note = axis.texts[0]
            position = counts.index(max(counts))
            assert note.get_text() == f"Peak: {counts[position]}"
            assert tuple(note.xy) == (hours[position], counts[position])
            assert tuple(note.get_position()) == (hours[position], counts[position] + 3)
            assert note.arrow_patch is not None
    finally:
        plt.close('all')
