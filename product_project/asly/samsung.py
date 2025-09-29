from asly.mobile import Mobile


class Samsung(Mobile):
    def __init__(self,name,price,voltage,screen_size,brand,serie):
        super().__init__(name, price, voltage,screen_size, brand)
        self.serie = serie


