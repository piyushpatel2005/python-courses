from io import StringIO
import numpy as np

def make_sky_grid(strip):
    return strip.reshape(-1, 3)

def exposure_schedule(settings):
    column = settings[:, np.newaxis]
    held = np.repeat(column, 2, axis=0)
    return np.tile(held, (1, 2))

def export_sky(grid):
    buffer = StringIO()
    np.savetxt(buffer, grid, delimiter=",", fmt="%d")
    return buffer.getvalue()

def import_sky(text):
    return np.genfromtxt(StringIO(text), delimiter=",", dtype=int, ndmin=2)

def observation_report(grid):
    means = ", ".join(f"{mean:.1f}" for mean in grid.mean(axis=1))
    return f"Rows: {grid.shape[0]}; brightest: {grid.max()}; row means: {means}"

packet = np.array([3, 6, 9, 2, 5, 8])
sky = make_sky_grid(packet)
print("sky:", sky)
print("exposures:", exposure_schedule(np.array([2, 5])))
if getattr(sky, "ndim", 0) == 2:
    text = export_sky(sky)
    print("CSV:", repr(text))
    if text:
        print("loaded:", import_sky(text))
    print("report:", observation_report(sky))
