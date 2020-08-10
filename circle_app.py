import uuid
from abc import ABCMeta
from abc import ABCMeta, abstractmethod

# value object for circle identifier
class circleId:
    def __init__(self,value):
        self.Value = value

# value object for cicle name
class circleName:
    def __init__(self,value):
        if len(value) < 3:
            raise ValueError("circleName must be 3 chars or longer")
        if len(value) > 20:
            raise ValueError("circleName must be 20 chars or shorter")
        self.Value = value
    def equals(self,otherCircleName):
        return otherCircleName.Value == self.Value

# entity for user
class user:
    def __init__(self,name,id=None):
        if id == None:
            self.id = str(uuid.uuid4())
            self.name = name
        else:
            self.id = id
            self.name = name

# entity for circle
class circle:
    def __init__(self,id,name,owner,members):
        self.id = id
        self.name = name
        self.owner = owner
        self.members = members

# entity for circleInvitation
class circleInvitation:
    def __init__(self,fromUserId,toUserId,circleId,id=None):
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.fromUserId = fromUserId
        self.toUserId = toUserId
        self.circleId = circleId

# interface for CircleRepository
class ICircleRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def findById(self,circleId):
        pass
    @abstractmethod
    def findByName(self,circleName):
        pass 

# interface for UserRepository
class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def findById(self,userId):
        pass
    @abstractmethod
    def findByName(self,userName):
        pass 

# interface for CircleFactory
class ICircleFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self,circleName,owner):
        pass

class circleService:
    def __init__(self,ICircleRepository):
        self.circleRepository = ICircleRepository
    def exists(self,circle):
        duplicate = self.circleRepository.findByName(circle.name)
        return duplicate != None

class circleCreateCommand:
    def __init__(self,userId,name):
        self.userId = userId
        self.name = name

class circleJoinCommand:
    def __init__(self,userId,circleId):
        self.userId = userId
        self.circleId = circleId

class circleInviteCommand:
    def __init__(self,fromUserId,toUserId,circleId):
        self.fromUserId = fromUserId
        self.toUserId = toUserId
        self.circleId = circleId

class circleApplicationService:
    def __init__(self,circleFactory,circleRepository,circleService,userRepository):
        self.circleFactory = circleFactory
        self.circleRepository = circleRepository
        self.circleService = circleService
        self.userRepository = userRepository

    def create(self,circleCreateCommand):
        if self.userRepository.findById(circleCreateCommand.userId) == None:
            raise ValueError("owner user not found.")
        if self.circleService.exists(circleCreateCommand.name) == True:
            raise ValueError("name already used.")
        self.circleRepository.save()

    def join(self,circleJoinCommand):
        if self.userRepository.findById(circleJoinCommand.userId) == None:
            raise ValueError("user not found.")
        circle = self.circleRepository.findById(circleJoinCommand.circleId)
        if circle == None:
            raise ValueError("circle not found.")
        if len(circle.members) >= 29:
            raise ValueError("circle is full.")
        circle.members.append(circleJoinCommand.userId)
        self.circleRepository.save()

    def invite(self,circleInviteCommand):
        fromUserId = self.userRepository.findById(circleInviteCommand.fromUserId)
        if fromUserId == None:
            raise ValueError("inviting user not found.")
        toUserId = self.userRepository.findById(circleInviteCommand.toUserId)
        if toUserId == None:
            raise ValueError("invited user not found.")
        circle = self.circleRepository.findById(circleInviteCommand.circleId)
        if circle == None:
            raise ValueError("circle not found.")
        if len(circle.members) >= 29:
            raise ValueError("circle is full.")
        circle.members.append(circleInviteCommand.toUserId)
        self.circleRepository.save()
