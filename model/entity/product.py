class Product:
    def __init__(self, id, name, brand, model, serial, category, unit, expiration_date=None):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.serial = serial
        self.category = category
        self.unit = unit
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return tuple((self.id, self.name, self.brand,self.model,self.serial,self.category,self.unit,self.expiration_date))
