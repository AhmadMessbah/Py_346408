import unittest
from controller.payment_controller import PaymentController


class TestPaymentController(unittest.TestCase):
    
    def test_save(self):
        """Test Payment save method"""
        status, message = PaymentController.save("sale", "cash", "04/07/20", 2134654, 100000, 6469185, "Payment description")
        self.assertTrue(status)
        self.assertIn("Payment Saved Successfully", message)
    
    def test_find_all(self):
        """Test Payment find_all method"""
        status, payment_list = PaymentController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)
    
    def test_find_by_id(self):
        """Test Payment find_by_id method"""
        status, payment = PaymentController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Payment update method"""
        status, message = PaymentController.update(1, "sale", "card", "04/07/20", 2134654, 150000, 6469185, "Updated description")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Payment delete method"""
        pass
    
    def test_find_by_transaction_type(self):
        """Test Payment find_by_transaction_type method"""
        status, payment_list = PaymentController.find_by_transaction_type("sale")
        self.assertTrue(status)
    
    def test_find_by_payment_type(self):
        """Test Payment find_by_payment_type method"""
        status, payment_list = PaymentController.find_by_payment_type("cash")
        self.assertTrue(status)
    
    def test_find_by_date_time_range(self):
        """Test Payment find_by_date_time_range method"""
        status, payment_list = PaymentController.find_by_date_time_range("01/01/20", "31/12/20")
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_customer_id(self):
        """Test Payment find_by_date_time_range_and_customer_id method"""
        status, payment_list = PaymentController.find_by_date_time_range_and_customer_id("01/01/20", "31/12/20", 2134654)
        self.assertTrue(status)
    
    def test_find_by_date_time_range_and_employee_id(self):
        """Test Payment find_by_date_time_range_and_employee_id method"""
        status, payment_list = PaymentController.find_by_date_time_range_and_employee_id("01/01/20", "31/12/20", 6469185)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
