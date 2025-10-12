from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService

order_item = OrderItem(None, 899, 2456, 45, 120000)
order_item_service = OrderItemService()

# order_item_service.save(order_item)
# Save Successful,
#                       BUT ORDER_ID Always Set to NULL???

# order_item_service.update(order_item)
# Update Successful!!

# order_item_service.delete(id)
# Delete Successful!!,
#                       BUT Doesn't Raise Error if ID doesn't exist????

# print(order_item_service.find_all())
# Find All Successful!!

# print(order_item_service.find_by_id(id))
# Find by id Successful!!
