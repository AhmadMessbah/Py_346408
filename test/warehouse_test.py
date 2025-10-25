import unittest
from controller.warehouse_controller import WarehouseController


class TestWarehouseController(unittest.TestCase):
    
    def test_save(self):
        """Test Warehouse save method"""
        status, message = WarehouseController.save(1, 100)
        self.assertTrue(status)
        self.assertIn("Warehouse Saved Successfully", message)
    
    def test_find_all(self):
        """Test Warehouse find_all method"""
        status, warehouse_list = WarehouseController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(warehouse_list, list)
    
    def test_find_by_id(self):
        """Test Warehouse find_by_id method"""
        status, warehouse = WarehouseController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Warehouse update method"""
        status, message = WarehouseController.update(1, 1, 150)
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Warehouse delete method"""
        pass
    
    def test_find_by_product_id(self):
        """Test Warehouse find_by_product_id method"""
        status, warehouse_list = WarehouseController.find_by_product_id(1)
        self.assertTrue(status)
    
    def test_find_by_quantity_less_than(self):
        """Test Warehouse find_by_quantity_less_than method"""
        status, warehouse_list = WarehouseController.find_by_quantity_less_than(50)
        self.assertTrue(status)
    
    def test_find_by_quantity_more_than(self):
        """Test Warehouse find_by_quantity_more_than method"""
        status, warehouse_list = WarehouseController.find_by_quantity_more_than(50)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
