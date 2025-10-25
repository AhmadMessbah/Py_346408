import unittest
from controller.order_controller import OrderController


class TestOrderController(unittest.TestCase):
    
    def test_save(self):
        """Test Order save method"""
        status, message = OrderController.save("frooshe", 2134654, 6469185, "04/07/20", 152648, 12654, 10, None, None)
        self.assertTrue(status)
        self.assertIn("Order Saved Successfully", message)
    
    def test_find_all(self):
        """Test Order find_all method"""
        status, order_list = OrderController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)
    
    def test_find_by_id(self):
        """Test Order find_by_id method"""
        status, order = OrderController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Order update method"""
        status, message = OrderController.update(1, "frooshe", 2134654, 6469185, "04/07/20", 152648, 12654, 10, None, None)
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Order delete method"""
        pass
    
    def test_find_by_order_type(self):
        """Test Order find_by_order_type method"""
        status, order_list = OrderController.find_by_order_type("frooshe")
        self.assertTrue(status)
    
    def test_find_by_customer_id(self):
        """Test Order find_by_customer_id method"""
        status, order_list = OrderController.find_by_customer_id(2134654)
        self.assertTrue(status)
    
    def test_find_by_employee_id(self):
        """Test Order find_by_employee_id method"""
        status, order_list = OrderController.find_by_employee_id(6469185)
        self.assertTrue(status)
    
    def test_find_by_date_time_range(self):
        """Test Order find_by_date_time_range method"""
        status, order_list = OrderController.find_by_date_time_range("01/01/20", "31/12/20")
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_customer_id(self):
        """Test Order find_by_date_time_range_and_customer_id method"""
        status, order_list = OrderController.find_by_date_time_range_and_customer_id("01/01/20", "31/12/20", 2134654)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
