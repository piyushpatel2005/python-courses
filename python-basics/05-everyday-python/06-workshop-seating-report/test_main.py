from solution import *


def test_energy_total():
    """Count shard energy from a list."""
    assert energy_total([2, 1, 3]) == 6, "Add all energy readings."
    assert energy_total([]) == 0, "The empty list totals zero."


def test_energy_needed():
    """Needed energy never falls below zero."""
    assert energy_needed(8, 3) == 5, "Subtract gathered energy from target."
    assert energy_needed(8, 8) == 0, "A charged beacon needs zero energy."
    assert energy_needed(8, 10) == 0, "Excess energy must not produce a negative need."


def test_beacon_report():
    """The report combines both helpers into one line."""
    assert beacon_report("North Beacon", 8, [2, 1]) == "North Beacon: 3 energy, 5 needed", "Use both helpers to build the report."
    assert beacon_report("Exit Beacon", 2, [1, 2]) == "Exit Beacon: 3 energy, 0 needed", "Use the actual name and clamp needed energy to zero."
