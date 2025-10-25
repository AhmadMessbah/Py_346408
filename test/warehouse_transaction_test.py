import unittest
from controller.warehouse_transaction_controller import WarehouseTransactionController


class TestWarehouseTransactionController(unittest.TestCase):
    
    def test_save(self):
        """Test WarehouseTransaction save method"""
        status, message = WarehouseTransactionController.save(1, 50, "in", "04/07/20", 2134654, 6469185)
        self.assertTrue(status)
        self.assertIn("WarehouseTransaction Saved Successfully", message)
    
    def test_find_all(self):
        """Test WarehouseTransaction find_all method"""
        status, transaction_list = WarehouseTransactionController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)
    
    def test_find_by_id(self):
        """Test WarehouseTransaction find_by_id method"""
        status, transaction = WarehouseTransactionController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test WarehouseTransaction update method"""
        status, message = WarehouseTransactionController.update(1, 1, 75, "out", "04/07/20", 2134654, 6469185)
        self.assertTrue(status)
    
    def test_delete(self):
        """Test WarehouseTransaction delete method"""
        pass
    
    def test_find_by_product_id(self):
        """Test WarehouseTransaction find_by_product_id method"""
        status, transaction_list = WarehouseTransactionController.find_by_product_id(1)
        self.assertTrue(status)
    
    def test_find_by_transaction_type(self):
        """Test WarehouseTransaction find_by_transaction_type method"""
        status, transaction_list = WarehouseTransactionController.find_by_transaction_type("in")
        self.assertTrue(status)
    
    def test_find_by_customer_id(self):
        """Test WarehouseTransaction find_by_customer_id method"""
        status, transaction_list = WarehouseTransactionController.find_by_customer_id(2134654)
        self.assertTrue(status)
    
    def test_find_by_employee_id(self):
        """Test WarehouseTransaction find_by_employee_id method"""
        status, transaction_list = WarehouseTransactionController.find_by_employee_id(6469185)
        self.assertTrue(status)
    
    def test_find_by_date_time_range(self):
        """Test WarehouseTransaction find_by_date_time_range method"""
        status, transaction_list = WarehouseTransactionController.find_by_date_time_range("01/01/20", "31/12/20")
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_customer_id(self):
        """Test WarehouseTransaction find_by_date_time_range_and_customer_id method"""
        status, transaction_list = WarehouseTransactionController.find_by_date_time_range_and_customer_id("01/01/20", "31/12/20", 2134654)
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_employee_id(self):
        """Test WarehouseTransaction find_by_date_time_range_and_employee_id method"""
        status, transaction_list = WarehouseTransactionController.find_by_date_time_range_and_employee_id("01/01/20", "31/12/20", 6469185)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
