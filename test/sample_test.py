import unittest
from controller.sample_controller import SampleController


class TestSampleController(unittest.TestCase):
    
    def test_save(self):
        """Test Sample save method"""
        status, message = SampleController.save("Test Sample", "This is a test sample")
        self.assertTrue(status)
        self.assertIn("Sample Saved Successfully", message)
    
    def test_find_all(self):
        """Test Sample find_all method"""
        status, sample_list = SampleController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(sample_list, list)
    
    def test_find_by_id(self):
        """Test Sample find_by_id method"""
        status, sample = SampleController.find_by_id(1)
        self.assertTrue(status)
    
    def test_update(self):
        """Test Sample update method"""
        status, message = SampleController.update(1, "Updated Sample", "Updated description")
        self.assertTrue(status)
    
    def test_delete(self):
        """Test Sample delete method"""
        pass


if __name__ == '__main__':
    unittest.main()
