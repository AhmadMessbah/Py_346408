from model.entity.order_items import OrderItems
from model.service.order_items_service import OrderItemsService

order_items = OrderItems(None, 1234, 5, 100000)
order_items_service = OrderItemsService()
order_items_service.save(order_items)

# order_items_service.update(order_items)

# order_items_service.delete(id)

# print(order_items_service.find_all())

# print(order_items_service.find_by_id(id))

