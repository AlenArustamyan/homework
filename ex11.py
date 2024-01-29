#Write a function that checks if a given string is a valid email address


import re

def valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_pattern, email):
        return True
    else:
        return False

email_to_check = "user@example.com"
if valid_email(email_to_check):
    print(email_to_check)
else:
    print(email_to_check)
