import pytest
from circle_app import circleId
from circle_app import circleName
from circle_app import user

def test_circle_id():
    ci = circleId(123)
    assert ci.Value == 123
    ci = circleId("abc")
    assert ci.Value == "abc"

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

def test_user():
    us = user(name="testUser")
    assert us.name == "testUser"
    assert len(us.id) == 36
    us2 = user(name="testUser2",id="testId")
    assert us2.name == "testUser2"
    assert us2.id == "testId"