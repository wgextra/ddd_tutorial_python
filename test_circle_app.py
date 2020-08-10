import pytest
from circle_app import circleId
from circle_app import circleName

def test_circle_id():
    ci = circleId(123)
    assert ci.Value == 123
    ci = circleId("abc")
    assert ci.Value == "abc"
    with pytest.raises(ValueError):
        circleId(None)

def test_circle_name():
    cn = circleName("testname")
    cn_same = circleName("testname")
    cn_diff = circleName("testname2")
    assert cn.equals(cn_same) == True
    assert cn.equals(cn_diff) == False
    with pytest.raises(ValueError):
        circleName("a")
    with pytest.raises(ValueError):
        circleName("aaaaaaaaaaaaaaaaaaaaa")