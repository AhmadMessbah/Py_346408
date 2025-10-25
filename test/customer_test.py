import unittest
from model.entity.customer import Customer
from controller.customer_controller import CustomerController


class TestCustomerController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = CustomerController

    def test_save_customer(self):
        """Test saving a customer"""
        status, message = self.controller.save("Ahmad", "Rezaei", "09123456789", "Tehran, Iran")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_customers(self):
        """Test finding all customers"""
        status, customer_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)

    def test_find_by_id(self):
        """Test finding customer by id"""
        status, message = self.controller.save("Test", "Customer", "09987654321", "Test Address")
        if status:
            status_all, customer_list = self.controller.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, customer = self.controller.find_by_id(customer_id)
                self.assertTrue(status)

    def test_update_customer(self):
        """Test updating a customer"""
        status, message = self.controller.save("Update", "Test", "09111111111", "Address 1")
        if status:
            status_all, customer_list = self.controller.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, message = self.controller.update(customer_id, "Updated", "Name", "09999999999", "New Address")
                self.assertTrue(status)

    def test_delete_customer(self):
        """Test deleting a customer"""
        status, message = self.controller.save("Delete", "Test", "09222222222", "Delete Address")
        if status:
            status_all, customer_list = self.controller.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, message = self.controller.delete(customer_id)
                self.assertTrue(status)

    def test_find_by_firstname_and_lastname(self):
        """Test finding customers by firstname and lastname"""
        status, customer_list = self.controller.find_by_firstname_and_lastname("Ahmad", "Rezaei")
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)

    def test_find_by_phone_number(self):
        """Test finding customers by phone number"""
        status, customer_list = self.controller.find_by_phone_number("09123456789")
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)


if __name__ == "__main__":
    unittest.main()
