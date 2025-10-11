import unittest
from simple_calculator import SimpleCalculator


class testclass(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3 , 4) ,7)
        self.assertEqual(self.calc.add(178 , 4) ,182)
        self.assertEqual(self.calc.add(3 , 5) ,8)
        self.assertEqual(self.calc.add(3 , 6) ,9)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-1 , -1) , 0)
        self.assertEqual(self.calc.subtract(-1 , 90) , -91)
        self.assertEqual(self.calc.subtract(78 ,102) , -24)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(78 , 90) , 7020)
        self.assertEqual(self.calc.multiply(3 , 5) , 15)
        self.assertEqual(self.calc.multiply(78 , 91) , 7098)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertEqual(self.calc.divide(10,7), 10/7)

    def ZeroDivisionTest(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10 , 0)


    if __name__ == "__main__":
        unittest.main()