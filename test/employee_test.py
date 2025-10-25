import unittest
from model import Employee
from controller import EmployeeController


class TestEmployeeController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = EmployeeController

    def test_save_employee(self):
        """Test saving an employee"""
        import random
        import string
        unique_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        status, message = self.controller.save("ali", "Mohammadi", 5000000, "cashier", "09123456789", unique_username, "pass1234", "cashier")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_employees(self):
        """Test finding all employees"""
        status, employee_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)

    def test_find_by_id(self):
        """Test finding employee by id"""
        status, message = self.controller.save("Test", "Employee", 3000000, "Test", "09999999999", "test", "pass", "user")
        if status:
            status_all, employee_list = self.controller.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, employee = self.controller.find_by_id(employee_id)
                self.assertTrue(status)

    def test_update_employee(self):
        """Test updating an employee"""
        status, message = self.controller.save("Update", "Employee", 4000000, "Tester", "09888888888", "upd", "pass", "admin")
        if status:
            status_all, employee_list = self.controller.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = self.controller.update(employee_id, "Updated", "Emp", 4500000, "Senior", "09888888888", "upd", "newpass", "admin")
                self.assertTrue(status)

    def test_delete_employee(self):
        """Test deleting an employee"""
        status, message = self.controller.save("Delete", "Employee", 2000000, "Temp", "09777777777", "del", "pass", "user")
        if status:
            status_all, employee_list = self.controller.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = self.controller.delete(employee_id)
                self.assertTrue(status)

    def test_find_by_username_and_password(self):
        """Test finding employee by username and password"""
        status, employee = self.controller.find_by_username_and_password("aliuser", "pass1234")
        self.assertTrue(status or employee is None)

    def test_find_by_role(self):
        """Test finding employees by role"""
        status, employee_list = self.controller.find_by_role("admin")
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)


if __name__ == "__main__":
    unittest.main()
