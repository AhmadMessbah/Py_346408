from asly.laptop import Laptop


class Asus(Laptop):
    def __init__(self,name,price,voltage,cpu,ram,serial1):
        super().__init__(name,price,voltage,cpu,ram)
        self.serial1 = serial1


