#درسته این from ......?
from asly.mobile import Mobile


class IPhone(Mobile):
    def __init__(self,name,price,voltage,screen_size,brand,serial):
        super().__init__(name, price, voltage,screen_size, brand)
        self.serial = serial
