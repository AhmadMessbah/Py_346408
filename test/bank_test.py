import unittest
from model.entity.bank import Bank
from controller.bank_controller import BankController


class TestBankController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = BankController

    def test_save_bank(self):
        """Test saving a bank"""
        status, message = self.controller.save("Melli Bank", "123456", 1000000, "Test Description")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_banks(self):
        """Test finding all banks"""
        status, bank_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_id(self):
        """Test finding bank by id"""
        # First save a bank
        status, message = self.controller.save("Test Bank", "999999", 500000, "Test")
        if status:
            # Find all to get the id of the last saved bank
            status_all, bank_list = self.controller.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, bank = self.controller.find_by_id(bank_id)
                self.assertTrue(status)
                self.assertIsNotNone(bank)

    def test_update_bank(self):
        """Test updating a bank"""
        # First save a bank
        status, message = self.controller.save("Update Test Bank", "111111", 200000, "Before Update")
        if status:
            status_all, bank_list = self.controller.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, message = self.controller.update(bank_id, "Updated Bank", "111111", 300000, "After Update")
                self.assertTrue(status)

    def test_delete_bank(self):
        """Test deleting a bank"""
        # First save a bank
        status, message = self.controller.save("Delete Test Bank", "222222", 150000, "To Be Deleted")
        if status:
            status_all, bank_list = self.controller.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, message = self.controller.delete(bank_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_name(self):
        """Test finding banks by name"""
        status, bank_list = self.controller.find_by_name("Melli")
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_account(self):
        """Test finding banks by account"""
        status, bank_list = self.controller.find_by_account("123456")
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent bank"""
        status, result = self.controller.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_bank(self):
        """Test updating a non-existent bank"""
        status, message = self.controller.update(999999, "Test", "999", 1000, "Test")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
