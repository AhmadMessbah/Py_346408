# product_id    discount    unit     stock_status     order_id

class OrderItems:
    def __init__(self, id ,product , unit_price, quantity, total_price):
        self.id = id
        self.product = product
        self.unit_price = unit_price
        self.quantity = quantity
        self.total_price = total_price



    def __repr__(self):
        return f"{self.__dict__}"
