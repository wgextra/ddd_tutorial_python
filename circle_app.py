import uuid


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