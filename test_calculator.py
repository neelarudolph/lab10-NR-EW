# https://github.com/neelarudolph/lab10-NR-EW/blob/main/calculator.py
# Partner 1: Neela Rudolph
# Partner 2: Erik Woods

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -3), 1)
    ########################################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):  # 3 assertions
        # divide(a, b) returns b / a
        self.assertEqual(divide(2, 10), 5)          # 10 / 2
        self.assertEqual(divide(4, 20), 5)          # 20 / 4
        self.assertAlmostEqual(divide(3, 10), 10 / 3)
    ########################################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        # base 1 is invalid
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    ########################################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # invalid argument b <= 0
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2.25), 1.5)

        # Negative input → ValueError
        with self.assertRaises(ValueError):
            square_root(-4)
    ########################################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
