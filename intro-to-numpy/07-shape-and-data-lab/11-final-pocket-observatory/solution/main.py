from io import StringIO
import numpy as np

def make_sky_grid(strip):
    return strip.reshape(-1, 3)

def exposure_column(settings):
    return settings[:, np.newaxis]

def hold_exposures(column):
    return np.repeat(column, 2, axis=0)

def exposure_schedule(settings):
    column = exposure_column(settings)
    held = hold_exposures(column)
    return np.tile(held, (1, 2))

def export_sky(grid):
    buffer = StringIO()
    np.savetxt(buffer, grid, delimiter=",", fmt="%d")
    return buffer.getvalue()

def import_sky(text):
    return np.genfromtxt(StringIO(text), delimiter=",", dtype=int, ndmin=2)

def format_report(rows, brightest, row_means):
    """Supplied formatting: join the means, each with one decimal place."""
    means = ", ".join(f"{mean:.1f}" for mean in row_means)
    return f"Rows: {rows}; brightest: {brightest}; row means: {means}"

def observation_report(grid):
    return format_report(grid.shape[0], np.max(grid), np.mean(grid, axis=1))

packet = np.array([3, 6, 9, 2, 5, 8])
sky = make_sky_grid(packet)
settings = np.array([2, 5])
print("sky:", sky)
print("setting column:", exposure_column(settings))
print("held rows:", hold_exposures(settings[:, np.newaxis]))
print("exposures:", exposure_schedule(settings))
# Inspect early steps even while later helpers are unfinished.
if sky.ndim == 2:
    text = export_sky(sky)
    print("CSV:", repr(text))
    if text:
        loaded = import_sky(text)
        print("loaded:", loaded)
        if loaded.size:
            print("report:", observation_report(loaded))
    # This separate probe lets you check the report before CSV is finished.
    print("report from sky:", observation_report(sky))
