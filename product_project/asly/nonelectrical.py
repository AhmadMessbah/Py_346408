from asly.product import Product
#درسته؟ خود پروداکت رو نتونستم بیارم.

class NonElectrical(Product):
    def __init__(self,name,price,weight):
        super().__init__(name,price)
        self.weight = weight
