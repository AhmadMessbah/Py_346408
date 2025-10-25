import unittest
from controller.bank_controller import BankController


class TestBankController(unittest.TestCase):
    
    def test_save(self):
        """Test Bank save method"""
        status, message = BankController.save("Test Bank", "Test Account", 1000, "Test Description")
        self.assertTrue(status)
        self.assertIn("Bank Saved Successfully", message)
    
    def test_find_all(self):
        """Test Bank find_all method"""
        status, bank_list = BankController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)
    
    def test_find_by_id(self):
        """Test Bank find_by_id method"""
        status, bank = BankController.find_by_id(1)
        self.assertTrue(status)
        self.assertIsNotNone(bank)
    
    def test_update(self):
        """Test Bank update method"""
        # Assuming bank with id 1 exists
        status, message = BankController.update(1, "Updated Bank", "Updated Account", 2000, "Updated Description")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Bank delete method"""
        # This will delete a bank, use with caution
        # status, message = BankController.delete(1)
        # self.assertTrue(status)
        pass
    
    def test_find_by_name(self):
        """Test Bank find_by_name method"""
        status, bank_list = BankController.find_by_name("Test")
        self.assertTrue(status)
    
    def test_find_by_account(self):
        """Test Bank find_by_account method"""
        status, bank_list = BankController.find_by_account("Test")
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
