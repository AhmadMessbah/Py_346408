import unittest
from controller.employee_controller import EmployeeController


class TestEmployeeController(unittest.TestCase):
    
    def test_save(self):
        """Test Employee save method"""
        status, message = EmployeeController.save("Ali", "Rezaei", 5000, "Developer", "09123456789", "alirez", "password123", "admin")
        self.assertTrue(status)
        self.assertIn("Employee Saved Successfully", message)
    
    def test_find_all(self):
        """Test Employee find_all method"""
        status, employee_list = EmployeeController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)
    
    def test_find_by_id(self):
        """Test Employee find_by_id method"""
        status, employee = EmployeeController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Employee update method"""
        status, message = EmployeeController.update(1, "Ali", "Rezaei", 6000, "Senior Developer", "09123456789", "alirez", "newpass", "admin")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Employee delete method"""
        pass
    
    def test_find_by_firstname_and_lastname(self):
        """Test Employee find_by_firstname_and_lastname method"""
        status, employee_list = EmployeeController.find_by_firstname_and_lastname("Ali", "Rezaei")
        self.assertTrue(status)
    
    def test_find_by_phone_number(self):
        """Test Employee find_by_phone_number method"""
        status, employee_list = EmployeeController.find_by_phone_number("09123456789")
        self.assertTrue(status)
    
    def test_find_by_username(self):
        """Test Employee find_by_username method"""
        status, employee_list = EmployeeController.find_by_username("alirez")
        self.assertTrue(status)
    
    def test_find_by_username_and_password(self):
        """Test Employee find_by_username_and_password method"""
        status, employee = EmployeeController.find_by_username_and_password("alirez", "password123")
        self.assertTrue(status)
    
    def test_find_by_role(self):
        """Test Employee find_by_role method"""
        status, employee_list = EmployeeController.find_by_role("admin")
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
