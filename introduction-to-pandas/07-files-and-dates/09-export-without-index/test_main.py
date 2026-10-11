from solution import *

from io import StringIO

def test_01_export_columns():
    """Export only requested columns, even after an unusual index"""
    for names, tickets in [(["Jo", "Kim"], [2, 1]), (["Inez"], [12])]:
        frame = pd.DataFrame({"guest": names, "tickets": tickets}, index=[40 + i for i in range(len(names))])
        text = make_guest_csv(frame)
        assert text.splitlines()[0] == "guest,tickets"
        again = pd.read_csv(StringIO(text))
        assert again.guest.tolist() == names and again.tickets.tolist() == tickets
