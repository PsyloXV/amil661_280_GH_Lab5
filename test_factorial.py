import unittest     # Import the Python unit testing framework
from maths import factorial     # Our code to test

class FactorialTest(unittest.TestCase):
    def test_factoral(self):
        self.assertEqual(factorial(3),6,"Factorial was not done correctly")
if __name__=='__main__':
    unittest.main()