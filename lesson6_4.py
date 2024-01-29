#Write a program that prompts the user to enter a word and checks if it is
#a palindrome. A palindrome is a word that reads the same backward as
#forward. Use string slicing and an if-else statement to compare the
#original word with its reverse


def palindrome(word):
    reverseword = word[::-1]
    if word == reverseword:
        return True
    else:
        return False

word2 = input(" Enter a word")
if palindrome(word2):
    print(f"{word2} is palindrome")
else:
    print(f"{word2} is not palindrome")