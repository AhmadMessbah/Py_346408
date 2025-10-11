from model.entity.order import Order
from model.service.order_service import OrderService


order = Order(None,"sell",None,None,None,
              None,None,None)

order_service1 = OrderService()
order_service1.save(order)
order_service1.update(order)
order_service1.delete(2)


