class OrderItems:
    def __init__(self, id ,product_id , quantity, price, discount, description):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"
