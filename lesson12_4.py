#Write a function that calculates the sum of squares of numbers from 1 to n.

x = int(input("enter number "))
def number(x):
    total = 0
    for i in range(1,x+1):
        total = total +(x+1)
    return total
print(number(x))
