import unittest
import time

class SimpleTests(unittest.TestCase):

    
    def test_should_succeed(self):
        assert 7 == 7
        
    def test_old_print_syntax(self):
        print "This should succeed in Python 2.x, but not 3.x"

        
if __name__ == "__main__":
    unittest.main()
