# Write a Python program to get the largest number from a list.
list = [1, 2, 9, 54]

max = list[0]
for number in list:
    if number > max:
        max = number

print(max)
