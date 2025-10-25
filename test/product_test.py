import unittest
from controller.product_controller import ProductController


class TestProductController(unittest.TestCase):
    
    def test_save(self):
        """Test Product save method"""
        status, message = ProductController.save("Laptop", "Dell", "Latitude", "DL12345", "Electronics", "unit", "2025-12-31")
        self.assertTrue(status)
        self.assertIn("Product Saved Successfully", message)
    
    def test_find_all(self):
        """Test Product find_all method"""
        status, product_list = ProductController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(product_list, list)
    
    def test_find_by_id(self):
        """Test Product find_by_id method"""
        status, product = ProductController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Product update method"""
        status, message = ProductController.update(1, "Laptop Pro", "Dell", "Latitude Pro", "DL12346", "Electronics", "unit", "2025-12-31")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Product delete method"""
        pass
    
    def test_find_by_name_and_brand(self):
        """Test Product find_by_name_and_brand method"""
        status, product_list = ProductController.find_by_name_and_brand("Laptop", "Dell")
        self.assertTrue(status)
    
    def test_find_by_category(self):
        """Test Product find_by_category method"""
        status, product_list = ProductController.find_by_category("Electronics")
        self.assertTrue(status)
    
    def test_find_by_expire_date_until(self):
        """Test Product find_by_expire_date_until method"""
        status, product_list = ProductController.find_by_expire_date_until("2025-12-31")
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
