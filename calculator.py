import math

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
