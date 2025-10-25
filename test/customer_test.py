import unittest
from controller.customer_controller import CustomerController


class TestCustomerController(unittest.TestCase):
    
    def test_save(self):
        """Test Customer save method"""
        status, message = CustomerController.save("John", "Doe", "1234567890", "123 Main St")
        self.assertTrue(status)
        self.assertIn("Customer Saved Successfully", message)
    
    def test_find_all(self):
        """Test Customer find_all method"""
        status, customer_list = CustomerController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)
    
    def test_find_by_id(self):
        """Test Customer find_by_id method"""
        status, customer = CustomerController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Customer update method"""
        status, message = CustomerController.update(1, "Jane", "Smith", "0987654321", "456 Oak Ave")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Customer delete method"""
        # Use with caution
        pass
    
    def test_find_by_firstname_and_lastname(self):
        """Test Customer find_by_firstname_and_lastname method"""
        status, customer_list = CustomerController.find_by_firstname_and_lastname("John", "Doe")
        self.assertTrue(status)
    
    def test_find_by_phone_number(self):
        """Test Customer find_by_phone_number method"""
        status, customer_list = CustomerController.find_by_phone_number("1234567890")
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
