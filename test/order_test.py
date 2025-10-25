from service.order_service import OrderService
from view.order_view import *

order = Order(2,"frooshe",2134654,6469185,"04/07/20",
              152648,12654,10)

order_service1 = OrderService()

# test passed
print(order_service1.save(order))

# test passed
#order_service1.update(order)

# test passed
#order_service1.delete(1)

# test passed
#print(order_service1.find_all())

# test passed
print(order_service1.find_by_id(17))
