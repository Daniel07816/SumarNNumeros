import unittest
import main

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(main.sumador(6), 21)
        
if __name__ == "__main__":
    unittest.main()