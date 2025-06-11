import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """
        Intial setup for SimpleCalculator instance before any test 
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test for simple additon calculation
        """
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_subtract(self):
        """
        Test for simple subtraction
        """
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(4, 2), 2)
        
    
    def test_multiply(self):
        """
        Test for simple multiplication
        """
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_divide(self):
        """
        Test for simple division
        """
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(2, 0), None)

if __name__ == "__main__":

    unittest.main()