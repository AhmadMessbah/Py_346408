class Sample:
    def __init__(self,id ,name ,description ):
        self.id = id
        self.name = name
        self.description = description


    def __repr__(self):
        return f"{self.__dict__}"


