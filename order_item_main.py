# from view.order_item_view import OrderItemView
#
# ui = OrderItemView()
from controller import OrderItemController

for item in OrderItemController.find_all()[1]:
    print(item.to_tuple())