# Write a Python program to get the smallest number from a list.
list = [5, 7, 3, 9, 11]

min = list[0]
for number in list:
    if number < min:
        min = number

print(min)

