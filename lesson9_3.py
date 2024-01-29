#Print a right-angled triangle pattern using a nested for loop. The pattern should have 5
#rows.

for row in range(5):
    for col in range(row + 1):
        print("*", end=" ")
    print()
