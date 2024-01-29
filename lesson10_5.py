#Write a Python program that calculates the Fibonacci sequence up to a given number n
#using a while loop. The Fibonacci sequence is a series of numbers where each number
#is the sum of the two preceding ones


def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence
target_number = 50

result_sequence = fibonacci_sequence(target_number)

print(f"{target_number}: {result_sequence}")
