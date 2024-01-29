#Write a function that prints all prime numbers up to a given limit
for i in range(2,101):
    for x in range(2,101):
        if i%x == 0:
            break
    if i == x:
        print(i,end=",")