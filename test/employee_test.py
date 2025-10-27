import unittest #
from model import Employee
from controller import EmployeeController


class TestEmployeeController(unittest.TestCase):

    def test_save_employee(self):
        import random
        import string
        unique_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        status, message = EmployeeController.save("ali", "mohammadi", 5000000, "cashier", "09123456789", unique_username, "pass12345", "cashier")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_employees(self):
        status, employee_list = EmployeeController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)

    def test_find_by_id(self):
        status, message = EmployeeController.save("test", "employee", 3000000, "manager", "09999999999", "test", "pass12345", "cashier")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, employee = EmployeeController.find_by_id(employee_id)
                self.assertTrue(status)
                self.assertIsNotNone(employee)

    def test_update_employee(self):
        status, message = EmployeeController.save("update", "employee", 4000000, "cashier", "09888888888", "upd", "pass12345", "cashier")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = EmployeeController.update(employee_id, "updated", "Emp", 4500000, "cashier", "09888888888", "upd", "pass12345", "cashier")
                self.assertTrue(status)

    def test_delete_employee(self):
        status, message = EmployeeController.save("delete", "employee", 2000000, "cashier", "09777777777", "aliuser", "pass12345", "cashier")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = EmployeeController.delete(employee_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_username_and_password(self):
        status, employee = EmployeeController.find_by_username_and_password("aliuser", "pass12345")
        self.assertTrue(not status or employee is None)

    def test_find_by_role(self):
        status, employee_list = EmployeeController.find_by_role("admin")
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)

    def test_find_by_id_not_found(self):
        status, result = EmployeeController.find_by_id(1)
        self.assertFalse(status)

    def test_update_nonexistent_employee(self):
        status, message = EmployeeController.update(1, "test", "emp", 3000000, "manager", "09111111111", "test", "pass", "user")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
