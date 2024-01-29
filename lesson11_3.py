#Write a Python function to calculate the factorial of a number (a non-negative
#integer). The function accepts the number as an argument


def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *=i
    return result
number = 8
factorial_result = factorial(number)
print(factorial_result)
