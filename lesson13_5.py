#Write a Python program to add two given lists using map and
#lambda.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print("List 1:", list1)
print("List 2:", list2)
print("Result:", result)
