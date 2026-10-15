from solution import *


def test_reject_existing_catalog_id():
    d = DispatchWorkbench({"s": []})
    d.catalog["x"] = {"id": "x"}
    assert d.ensure_new_id("y") is None
    try:
        d.ensure_new_id("x")
    except ValueError:
        pass
    else:
        assert False
    assert list(d.catalog) == ["x"]


def test_copy_catalog_record():
    job = {"id": "x", "units": 3}
    copied = DispatchWorkbench.copy_record(job)
    assert copied == job and copied is not job
    job["units"] = 99
    assert copied["units"] == 3


def test_store_record_by_identifier():
    d = DispatchWorkbench({"s": []})
    one = {"id": "x", "units": 3}
    two = {"id": "y", "units": 0}
    d.store_record("x", one)
    d.store_record("y", two)
    assert d.catalog == {"x": one, "y": two}
    assert DispatchWorkbench({"s": []}).catalog == {}
