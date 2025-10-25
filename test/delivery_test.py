import unittest
from controller.delivery_controller import DeliveryController


class TestDeliveryController(unittest.TestCase):
    
    def test_save(self):
        """Test Delivery save method"""
        status, message = DeliveryController.save("Ali", "Rezaei", "123 Main St", "Fast delivery")
        self.assertTrue(status)
        self.assertIn("Delivery Saved Successfully", message)
    
    def test_find_all(self):
        """Test Delivery find_all method"""
        status, delivery_list = DeliveryController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(delivery_list, list)
    
    def test_find_by_id(self):
        """Test Delivery find_by_id method"""
        status, delivery = DeliveryController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Delivery update method"""
        status, message = DeliveryController.update(1, "Hassan", "Ahmadi", "456 Oak Ave", "Standard delivery")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Delivery delete method"""
        pass


if __name__ == '__main__':
    unittest.main()
