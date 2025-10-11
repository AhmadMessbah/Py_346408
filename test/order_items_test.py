from model.entity.order_items import OrderItems
from model.service.order_items_service import OrderItemsService


order_item = OrderItems(None,None,10,500000,None,
              None)


order_item1 = OrderItemsService()

order_item1.save(order_item)

#order_item1.update(order_item)

#order_item1.delete(2)

#order_item1.find_all()

#order_item1.find_by_id(1)
