# https://github.com/neelarudolph/lab10-NR-EW/blob/main/calculator.py
# Partner 1: Neela Rudolph
# Partner 2: Erik Woods

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
def test_multiply(self):
    self.assertEqual(calculator.mul(3, 4), 12)
    self.assertEqual(calculator.mul(-2, 5), -10)
    self.assertEqual(calculator.mul(0, 100), 0)

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
def test_divide(self):
    # div(a, b) returns b / a
    self.assertEqual(calculator.div(2, 10), 5)
    self.assertAlmostEqual(calculator.div(3, 10), 10/3)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
def test_log_invalid_argument(self):
    with self.assertRaises(ValueError):
        calculator.logarithm(1, 10)

    with self.assertRaises(ValueError):
        calculator.logarithm(-3, 10)

    with self.assertRaises(ValueError):
        calculator.logarithm(10, -5)


    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
def test_hypotenuse(self):
    self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
    self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)


    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
def test_sqrt(self):
    self.assertEqual(calculator.square_root(9), 3)
    self.assertAlmostEqual(calculator.square_root(2.25), 1.5)

    # Negative input → ValueError
    with self.assertRaises(ValueError):
        calculator.square_root(-4)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
