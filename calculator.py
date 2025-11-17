# https://github.com/neelarudolph/lab10-NR-EW/blob/main/calculator.py
# Partner 1: Neela Rudolph
# Partner 2: Erik Woods

import math

# https://github.com/<your-link-here>
# Partner 1: <Name>
# Partner 2: <Name>

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a  # follows lab spec

def logarithm(a, b):
    # base a, argument b
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("math domain error")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
