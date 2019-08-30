import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        self.assertEqual(maths.add(1,2),3,"Numbers were not added properly")
        self.assertEqual(maths.add(17,14,12),27,"Numbers not added over base 10 properly")
        self.assertEqual(maths.add(10,12,8),26,"Numbers not added under base 11 properly")
        ''' Tests the add function. '''
    def test_fibonacci(self):
        self.assertEqual(maths.fibonacci(5),5,"Fibonacci was not done properly")
        ''' Tests the fibonacci function. '''

    def test_convert_base(self):
        self.assertEqual(int(maths.convert_base(17, 7)),23,"Under base 10 test failed")
        self.assertEqual(int(maths.convert_base(17, 16)),11, "Over base 10 test failed")
        

# This allows running the unit tests from the command line (python test_maths.py)
if __name__=='__main__':
    unittest.main()
