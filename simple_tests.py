import unittest
import time

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.x = 7
        self.s = "a string"

    def test_x_should_fail(self):
        assert self.x == 9
    
    def test_s_should_succeed(self):
        assert self.y == "a string"
        
    def test_old_print_syntax(self):
        print "This should succeed in Python 2.x, but not 3.x"
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
