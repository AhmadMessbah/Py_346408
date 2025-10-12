from model.entity.order import Order
from model.service.order_service import OrderService

order = Order(None, "Ali", "Tozihat")

order_service = OrderService()
order_service.save(order)

order_service.update(order)

order_service.delete(id)

print(order_service.find_all())

print(order_service.find_by_id(id))

