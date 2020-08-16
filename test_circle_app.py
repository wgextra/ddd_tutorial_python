import pytest
from circle_app import *

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

def test_circle_invitation():
    ci = circleInvitation("testFromUserId","testToUserId","testCircleId")
    assert ci.fromUserId == "testFromUserId"
    assert ci.toUserId == "testToUserId"
    assert ci.circleId == "testCircleId"
    assert len(ci.id) == 36
    ci2 = circleInvitation("testFromUserId2","testToUserId2","testCircleId2",id="testInvitationID")
    assert ci2.fromUserId == "testFromUserId2"
    assert ci2.toUserId == "testToUserId2"
    assert ci2.circleId == "testCircleId2"
    assert ci2.id == "testInvitationID"

def test_circle():
    ccl = circle(id="testCircleId",name="testCircleName",owner="testCircleOwnerId",members=[user("testCircleMemberId1"),user("testCircleMemberId2"),user("testCircleMemberId3")])
    assert ccl.id == "testCircleId"
    assert ccl.name == "testCircleName"
    assert ccl.owner == "testCircleOwnerId"
    assert [member.name for member in ccl.members] == ["testCircleMemberId1","testCircleMemberId2","testCircleMemberId3"]
    ccl.join(user("testCircleMemberId4"))
    assert [member.name for member in ccl.members] == ["testCircleMemberId1","testCircleMemberId2","testCircleMemberId3","testCircleMemberId4"]
    

def test_circle_create_command():
    ccc = circleCreateCommand("testUserId","testCircleName")
    assert ccc.userId == "testUserId"
    assert ccc.name == "testCircleName"

def test_circle_join_command():
    cjc = circleJoinCommand("testUserId","testCircleId")
    assert cjc.userId == "testUserId"
    assert cjc.circleId == "testCircleId"

def test_circle_invite_command():
    cic = circleInviteCommand("testFromUserId","testInvitedUserId","testCircleId")
    assert cic.fromUserId == "testFromUserId"
    assert cic.toUserId == "testInvitedUserId"
    assert cic.circleId == "testCircleId"

class ImMemoryUserRepository(IUserRepository):
    store = {
        "testUserId1":"testUserName1",
        "testUserId2":"testUserName2",
        "testUserId3":"testUserName3",
    }
    def findById(self,userId):
        if userId in self.store.keys():
            return userId
        else:
            return None
    
    def findByName(self,userName):
        matchedIds = [id for id,name in self.store.items() if name == userName]
        return matchedIds[0]

    def save(self,user):
        self.store[user.id] = user(user.name,user.id)
        