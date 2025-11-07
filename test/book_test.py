import unittest
from model import Book
from controller import BookController


class TestBookController(unittest.TestCase):

    def setUp(self):
        self.controller = BookController

    def test_save_book(self):
        """Test saving a book"""
        status, message = self.controller.save("Test Book", 1, 1, "2024", 1, "Test Publisher", "1234567890", "Borrow", 10.0, 5.0, 100.0)
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_books(self):
        status, book_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(book_list, list)

    def test_find_by_id(self):
        status, message = self.controller.save("Find Test", 1, 1, "2024", 1, "Publisher", "1111111111", "Sell", 5.0, 2.0, 50.0)
        if status:
            status_all, book_list = self.controller.find_all()
            if book_list:
                book_id = book_list[-1].book_id
                status, book = self.controller.find_by_id(book_id)
                self.assertTrue(status)
                self.assertIsNotNone(book)

    def test_update_book(self):
        status, message = self.controller.save("Update Test", 1, 1, "2024", 1, "Publisher", "2222222222", "Borrow", 10.0, 5.0, 100.0)
        if status:
            status_all, book_list = self.controller.find_all()
            if book_list:
                book_id = book_list[-1].book_id
                status, message = self.controller.update(book_id, "Updated Book", 2, 2, "2025", 2, "Updated Publisher", "3333333333", "Sell", 15.0, 10.0, 200.0)
                self.assertTrue(status)

    def test_delete_book(self):
        status, message = self.controller.save("Delete Test", 1, 1, "2024", 1, "Publisher", "4444444444", "Borrow", 10.0, 5.0, 100.0)
        if status:
            status_all, book_list = self.controller.find_all()
            if book_list:
                book_id = book_list[-1].book_id
                status, message = self.controller.delete(book_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_title(self):
        status, book_list = self.controller.find_by_title("Test Book")
        self.assertTrue(status)
        self.assertIsInstance(book_list, list)

    def test_find_by_customer_id(self):
        status, book_list = self.controller.find_by_customer_id(1)
        self.assertTrue(status)
        self.assertIsInstance(book_list, list)

    def test_find_by_employee_id(self):
        status, book_list = self.controller.find_by_employee_id(1)
        self.assertTrue(status)
        self.assertIsInstance(book_list, list)


if __name__ == "__main__":
    unittest.main()