import pytest
from circle_app import circleId

def test_circle_id():
    ci = circleId(123)
    assert ci.Value == 123
    ci = circleId("abc")
    assert ci.Value == "abc"
    with pytest.raises(ValueError):
        circleId(None)