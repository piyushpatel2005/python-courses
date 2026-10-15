from solution import *


def test_descriptor_read():
    assert isinstance(Sensor.__dict__["reading"], ScaledReading)
    assert Sensor.reading is Sensor.__dict__["reading"]
    for raw in [0, 3, -2, 11]:
        sensor = Sensor(raw)
        assert sensor.reading == raw * 10
        sensor.raw = raw + 1
        assert sensor.reading == (raw + 1) * 10
