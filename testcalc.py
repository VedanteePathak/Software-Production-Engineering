#!/usr/bin/python3

import unittest
import math
from calculator import square_root, natural_logarithm, power, factorial

class TestCalculatorFunctions(unittest.TestCase):

    def test_square_root_positive(self):
        result = square_root(25)
        self.assertEqual(result, 5)

    def test_square_root_negative(self):
        result = square_root(-25)
        self.assertEqual(result, "Cannot find the square root of a negative number.")

    def test_natural_logarithm_positive(self):
        result = natural_logarithm(10)
        self.assertEqual(result, math.log(10))

    def test_natural_logarithm_non_positive(self):
        result = natural_logarithm(0)
        self.assertEqual(result, "Natural logarithm is not defined for non-positive numbers.")

    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

    def test_factorial_positive(self):
        result = factorial(5)
        self.assertEqual(result, math.factorial(5))

    def test_factorial_negative(self):
        result = factorial(-5)
        self.assertEqual(result, "Factorial is not defined for negative numbers.")

if __name__ == '__main__':
    unittest.main()
