from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService

order_item = OrderItem(2)
order_item_service = OrderItemService()
# order_item_service.save(order_item)
# Save Successful!

# order_item_service.update(order_item)
# Update Successful!!

# order_item_service.delete(id)

# print(order_item_service.find_all())
# Find All Successful!!

print(order_item_service.find_by_id(id))

