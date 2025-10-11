# انبار
class Warehouse:
        def __init__(self,id,product_name,warehouse_id,quantity):
                self.id = id
                self.product_name = product_name
                self.warehouse_id = warehouse_id
                self.quantity = quantity

        def __repr__(self):
                return f'{self.__dict__}'