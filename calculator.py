#!/usr/bin/python3

import math
import sys

def square_root(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        return "Cannot find the square root of a negative number."

def natural_logarithm(number):
    if number > 0:
        return math.log(number)
    else:
        return "Natural logarithm is not defined for non-positive numbers."

def power(base, exponent):
    return math.pow(base, exponent)

def factorial(number):
    if number >= 0:
        return math.factorial(number)
    else:
        return "Factorial is not defined for negative numbers."

def calculator():
    if len(sys.argv) < 3:
        print("Usage: python calculator.py <operation> <operand1> <operand2>")
        sys.exit(1)

    operation = sys.argv[1]
    operand1 = float(sys.argv[2])
    operand2 = None

    if operation not in ['sqrt', 'log', 'pow', 'fact']:
        print("Invalid operation. Choose from: sqrt, log, pow, fact")
        sys.exit(1)

    if operation in ['sqrt', 'log', 'fact']:
        result = None
        if operation == 'sqrt':
            result = square_root(operand1)
        elif operation == 'log':
            result = natural_logarithm(operand1)
        elif operation == 'fact':
            result = factorial(operand1)
        print(f"The result is: {result}")

    elif operation == 'pow':
        if len(sys.argv) != 4:
            print("Usage for power operation: python calculator.py pow <base> <exponent>")
            sys.exit(1)
        operand2 = float(sys.argv[3])
        result = power(operand1, operand2)
        print(f"{operand1} raised to the power of {operand2} is: {result}")

if __name__ == "__main__":
    calculator()
