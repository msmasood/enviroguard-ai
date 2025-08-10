# tests/test_monitor.py
from enviroguard.monitor import detect_hazards, assess_risk
def test_monitor_demo():
    dets = detect_hazards('data/sample_image.tif')
    assert isinstance(dets, list)
    if dets:
        r = assess_risk(dets[0])
        assert 'score' in r and 'level' in r
