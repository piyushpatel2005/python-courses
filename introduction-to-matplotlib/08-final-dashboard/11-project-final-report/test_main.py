from solution import *
import matplotlib.pyplot as plt

def test_01_report_tracks_new_inputs():
    """Report counts reflect changed observations and caveat"""
    for garden, library, transit, expected in [
        (pd.DataFrame({'day':['01','01','02'], 'temp_c':[18,20,None]}), pd.DataFrame({'day':['01','02'], 'branch':['A','B'], 'visits':[4,9]}), pd.DataFrame({'day':['01'], 'route':['X'], 'rides':[7]}), (1,1,13,7)),
        (pd.DataFrame({'day':['A','B','C'], 'temp_c':[10,11,12]}), pd.DataFrame({'day':['B','C','C'], 'branch':['E','E','W'], 'visits':[8,5,3]}), pd.DataFrame({'day':['A','A','B'], 'route':['X','Y','X'], 'rides':[4,6,8]}), (3,2,16,18))
    ]:
        result = report(garden, library, transit)
        assert tuple(result[k] for k in ('garden_days','shared_days','library_visits','transit_rides')) == expected
        assert 'not causation' in result['caveat'].lower()

def test_02_note_on_actual_figure():
    """Visible note discloses coverage and uncertainty of interpretation"""
    plt.close('all')
    garden = pd.DataFrame({'day':['A','B','B'], 'temp_c':[10,20,22]})
    library = pd.DataFrame({'day':['B'], 'branch':['E'], 'visits':[5]})
    transit = pd.DataFrame({'day':['A'], 'route':['X'], 'rides':[7]})
    figure, axes = build_dashboard(garden, library, transit)
    note = ' '.join(t.get_text() for t in figure.texts)
    assert '2 days' in note and '1' in note and 'not causation' in note.lower()
    assert axes[1,1].get_xlabel() == 'Temperature (°C)'
