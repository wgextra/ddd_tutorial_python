class circleId:
    def __init__(self,value):
        if value == None:
            raise ValueError(value)
        self.Value = value