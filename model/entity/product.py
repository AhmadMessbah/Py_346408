class Product:
    def __init__(self, product_code, product_name, product_type, expiration_date, warehouse_code, unit_price, stock_quantity):
        self.product_code = product_code
        self.name = product_name
        self.product_type = product_type
        self.expiration_date = expiration_date
        self.warehouse_code = warehouse_code
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"{self.__dict__}"