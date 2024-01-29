#Write a Python program to square and cube every number in a given list of
#integers using Lambda.
numbers = [11,33,44,55,66]
print(list(map(lambda x : x**2,numbers)))
print(list(map(lambda x : x**3,numbers)))