from model.entity.order import Order
from model.service.order_service import OrderService

order = Order(1,"forosh",2134654,6469185,"04/07/20",
              152648,12654,10)

order_service1 = OrderService()

# test passed
#order_service1.save(order)

# test passed
#order_service1.update(order)

# test passed
# order_service1.delete(1)

# test passed
# print(order_service1.find_all())

# test passed
#print(order_service1.find_by_id(10))


