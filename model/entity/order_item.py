from tools.order_item_validator import *
# from model import ProductService


class OrderItem:

    def __init__(self, id, order_id, product_id, quantity, price, discount=None, description=None):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.description = description

    def validate(self):
        quantity_validator(self.quantity)
        price_validator(self.price)
        discount_validator(self.discount)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    # def to_tuple(self):
    #     product_service = ProductService()
    #     product = product_service.find_by_id(self.product_id)[0]
    #
    #     return tuple((
    #         self.id,
    #         self.order_id,
    #         product.name + " " + product.brand,
    #         self.quantity,
    #         self.price,
    #         self.discount,
    #         self.description))
