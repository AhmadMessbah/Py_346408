# from test import order_test
# from view import OrderView
from controller import OrderController

# ui = OrderView()
print(OrderController.find_by_id(2)[1].to_tuple())