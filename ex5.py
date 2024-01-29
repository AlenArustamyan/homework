#Write a function that calculates the square root of a number using the math module

import math

def calculate(number):
    if number >= 0:
        result = math.sqrt(number)
        return result
    else:
        print("Error: Cannot calculate square root of a negative number.")
        return None

input_number = 25

result = calculate(input_number)
if result is not None:
    print(result)
