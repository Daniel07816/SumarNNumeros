import unittest
import main

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(main.sum(4, 5), 5)
        
if __name__ == "__main__":
    unittest.main()