class Session:#
    employee = None
    customer = None
    book = None
    order_items = []
    payment = None

    @classmethod
    def add_order_item(cls, order_item):
        cls.order_items.append(order_item)