#Given a list of numbers, write a function to find the sum of all numbers in the list that
#can be divided by 7.


def sum_numbers(numbers):
    result_sum = sum(num for num in numbers if num % 7 == 0)
    return result_sum

# Example usage:
number_list = [14, 21, 35, 42, 50, 63, 70, 77]

result = sum_numbers(number_list)
print(result)
