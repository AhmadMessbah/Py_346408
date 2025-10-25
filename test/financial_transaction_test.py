import unittest
from controller.financial_transaction_controller import FinancialTransactionController


class TestFinancialTransactionController(unittest.TestCase):
    
    def test_save(self):
        """Test FinancialTransaction save method"""
        status, message = FinancialTransactionController.save("sale", 2134654, 6469185, 50000, "04/07/20", 152648, "Transaction description")
        self.assertTrue(status)
        self.assertIn("FinancialTransaction Saved Successfully", message)
    
    def test_find_all(self):
        """Test FinancialTransaction find_all method"""
        status, transaction_list = FinancialTransactionController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)
    
    def test_find_by_id(self):
        """Test FinancialTransaction find_by_id method"""
        status, transaction = FinancialTransactionController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test FinancialTransaction update method"""
        status, message = FinancialTransactionController.update(1, "sale", 2134654, 6469185, 75000, "04/07/20", 152648, "Updated description")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test FinancialTransaction delete method"""
        pass
    
    def test_find_by_transaction_type(self):
        """Test FinancialTransaction find_by_transaction_type method"""
        status, transaction_list = FinancialTransactionController.find_by_transaction_type("sale")
        self.assertTrue(status)
    
    def test_find_by_customer_id(self):
        """Test FinancialTransaction find_by_customer_id method"""
        status, transaction_list = FinancialTransactionController.find_by_customer_id(2134654)
        self.assertTrue(status)
    
    def test_find_by_employee_id(self):
        """Test FinancialTransaction find_by_employee_id method"""
        status, transaction_list = FinancialTransactionController.find_by_employee_id(6469185)
        self.assertTrue(status)
    
    def test_find_by_payment_id(self):
        """Test FinancialTransaction find_by_payment_id method"""
        status, transaction_list = FinancialTransactionController.find_by_payment_id(152648)
        self.assertTrue(status)
    
    def test_find_by_date_time_range(self):
        """Test FinancialTransaction find_by_date_time_range method"""
        status, transaction_list = FinancialTransactionController.find_by_date_time_range("01/01/20", "31/12/20")
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_customer_id(self):
        """Test FinancialTransaction find_by_date_time_range_and_customer_id method"""
        status, transaction_list = FinancialTransactionController.find_by_date_time_range_and_customer_id("01/01/20", "31/12/20", 2134654)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
