from datetime import datetime

class WarehouseTransaction:
    def __init__(self,id,product_name,warehouse_id,quantity,transaction_date,transaction_type,sender,receiver):
        self.id = id
        self.product_name = product_name
        self.warehouse_id = warehouse_id
        self.quantity = quantity
        self.transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transaction_type = transaction_type
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
            return f'{self.__dict__}'
