from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService

order_item = OrderItem(None, 1234, 5, 100000)
order_item_service = OrderItemService()
order_item_service.save(order_item)

# order_item_service.update(order_item)

# order_item_service.delete(id)

# print(order_item_service.find_all())

# print(order_item_service.find_by_id(id))

