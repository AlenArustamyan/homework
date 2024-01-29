#Write a Python function to calculate count of each letter in string

def lettercount(string):
    count = {}
    for ch in string:
        if ch.isalpha():
            ch = ch.lower()
