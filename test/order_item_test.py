import unittest
from controller.order_item_controller import OrderItemController


class TestOrderItemController(unittest.TestCase):
    
    def test_save(self):
        """Test OrderItem save method"""
        status, message = OrderItemController.save(1, 1, 5, 10000, 10, "Test Item")
        self.assertTrue(status)
        self.assertIn("OrderItem Saved Successfully", message)
    
    def test_find_all(self):
        """Test OrderItem find_all method"""
        status, order_item_list = OrderItemController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(order_item_list, list)
    
    def test_find_by_id(self):
        """Test OrderItem find_by_id method"""
        status, order_item = OrderItemController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test OrderItem update method"""
        status, message = OrderItemController.update(1, 1, 1, 10, 12000, 15, "Updated Item")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test OrderItem delete method"""
        pass
    
    def test_find_by_order_id(self):
        """Test OrderItem find_by_order_id method"""
        status, order_item_list = OrderItemController.find_by_order_id(1)
        self.assertTrue(status)
    
    def test_find_by_product_id(self):
        """Test OrderItem find_by_product_id method"""
        status, order_item_list = OrderItemController.find_by_product_id(1)
        self.assertTrue(status)
    
    def test_find_by_quantity_less_than(self):
        """Test OrderItem find_by_quantity_less_than method"""
        status, order_item_list = OrderItemController.find_by_quantity_less_than(10)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
