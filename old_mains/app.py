from view import *

# from view.warehouse_transaction_view import WarehouseTransactionView
# from view.warehouse_view import WarehouseView

# Phase 1 Passed
# Group A
# ui = CustomerView()
# ui = EmployeeView()
# ui = ProductView()
# ui = PaymentView()

# Group B
# ui = BankView()
# ui = FinancialTransactionView()
from view.book_view import BookView

def main():
    app = BookView()
    app.run()

if __name__ == "__main__":
    main()

# Group D
# ui = OrderView()
# ui = OrderItemView()


# Phase 1 Not Passed
# Group C
# ui = WarehouseView()
# ui = WarehouseTransactionView()


# ui = DashboardView()