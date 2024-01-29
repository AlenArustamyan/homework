#Write a Python program that calculates the sum of all even numbers between 1 and 100
#using a while loop.
number = 2
sum_of_evens = 0
while number <= 100:
    sum_of_evens += number
    number += 2
print(f"Sum of even numbers between 1 and 100: {sum_of_evens}")
