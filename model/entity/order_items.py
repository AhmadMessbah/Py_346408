# product_id    unit_price    discount     total_price      unit     stock_status     order_id

class OrderItems:
    def __init__(self, id ,product , quantity, price):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.__dict__}"
