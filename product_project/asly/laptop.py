from asly.electrical import Electrical

#این دایره ها چین؟

class Laptop(Electrical):
    def __init__(self,name,price,voltage,cpu,ram):
        super().__init__(name,price,voltage)
        self.cpu = cpu
        self.ram = ram
