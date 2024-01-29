# Write a function that will get a function string and check if the password is strong
#or not.
#Strong password must contain | One uppercase letter | one special symbol | one
#number
#Length of the password should be 8 or more
#If your password is Strong you will return True. else return False

import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*()-_+=]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True
password_to_check = input("Enter the password to check: ")
result = is_strong_password(password_to_check)

if result:
    print("Password is Strong!")
else:
    print("Password is not Strong.")
