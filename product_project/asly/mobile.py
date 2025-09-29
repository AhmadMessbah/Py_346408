from asly.electrical import Electrical


class Mobile(Electrical):
    def __init__(self,name,price,voltage,screen_size,brand):
        super().__init__(name, price, voltage)
        self.screen_size = screen_size
        self.brand = brand
