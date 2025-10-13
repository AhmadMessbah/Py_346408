from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService

order_item = OrderItem(3, 33695, 2456, 55, 120000, 10, "test")
# print(order_item)
order_item_service1 = OrderItemService()

# test passed
# order_item_service1.save(order_item)

# test passed
# order_item_service1.update(order_item)

# test passed
# order_item_service1.delete(5)

#############################################################

# todo *** BUT Doesn't Raise Error if ID doesn't exist????******
# todo *** AND Autoincrement ID is NOT RESET?????*******
# todo *** order_id set null????******

#############################################################

# test passed
# print(order_item_service1.find_all())

# test passed
# print(order_item_service1.find_by_id(10))
