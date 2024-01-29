# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers
n = int(input("Input a number "))
d = dict()
for x in range(1, n + 1):
    d[x] = x * x

print(d)
