from model.entity.order import Order
from model.service.order_service import OrderService

order = Order(1,"sell",2134654,6469185,"04/07/19",
              152648,12654,20)

order_service1 = OrderService()
order_service1.save(order)

# order_service1.update(order)

# order_service1.delete(1)

#print(order_service1.find_all())

#print(order_service1.find_by_id(1))
