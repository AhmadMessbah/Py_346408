from asly.laptop import Laptop


class Lenovo(Laptop):
    def __init__(self,name,price,voltage,cpu,ram,serial2):
        super().__init__(name,price,voltage,cpu,ram)
        self.serial2 = serial2


