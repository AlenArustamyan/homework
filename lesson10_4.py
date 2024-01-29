#Write a Python program that generates a random number between 1 and 100 and asks
#the user to guess the number. The program should give hints whether the guessed
#number is too high or too low until the correct number is guessed

import random

secret_number = random.randint(1, 100)

while True:
    user = int(input("Guess the number (between 1 and 100): "))
    if user == secret_number:
        print(f"correct {secret_number}.")
        break
    elif user < secret_number:
        print(" low. Try again.")
    else:
        print(" high. Try again.")
