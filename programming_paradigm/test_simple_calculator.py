import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """
        Intial setup method
        """
        self.calculator = SimpleCalculator()

    def test_add(self):
        """
        Test for simple additon calculation
        """
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.add(5, 7), 12)

    def test_subtract(self):
        """
        Test for simple subtraction
        """
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.subtract(4, 2), 2)
        
    
    def test_multiply(self):
        """
        Test for simple multiplication
        """
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.multiply(5, 5), 25)

    def test_divide(self):
        """
        Test for simple division
        """
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.divide(2, 0), None)

if __name__ == "__main__":

    unittest.main()