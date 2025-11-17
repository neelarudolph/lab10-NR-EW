# https://github.com/neelarudolph/lab10-NR-EW/blob/main/calculator.py
# Partner 1: Neela Rudolph
# Partner 2: Erik Woods

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("math domain error")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    # raise ValueError if a < 0
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    # can be negative, math.hypot handles it fine
    return math.hypot(a, b)
    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a    # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    return math.log(b,a)

def exponent(a, b):
    return a ** b
