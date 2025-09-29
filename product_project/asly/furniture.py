from asly.nonelectrical import NonElectrical


class Furniture(NonElectrical):
    def __init__(self,name,price,weight,capacity):
        super().__init__(name,price,weight)
        self.capacity = capacity
