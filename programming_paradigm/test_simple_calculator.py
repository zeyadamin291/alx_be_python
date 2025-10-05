import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        # Create an instance of SimpleCalculator before each test
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calc.multiply(7, 6)
        self.assertEqual(result, 42)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        # Division by zero should raise an error
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
