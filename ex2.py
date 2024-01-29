#Create a Python class representing a basic calculator with methods for addition,
#subtraction, multiplication, and division.


class BasicCalculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        result = num1 + num2
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        return result

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            print("Error")
            return None

calculator = BasicCalculator()

result_addition = calculator.add(5, 3)
print( result_addition)

result_subtraction = calculator.subtract(8, 2)
print( result_subtraction)

result_multiplication = calculator.multiply(4, 6)
print( result_multiplication)

result_division = calculator.divide(10, 2)
print(result_division)
