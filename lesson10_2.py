#Write a Python program that asks the user to enter a password. Keep asking for the
#password until the correct password "secret" is entered. Provide appropriate feedback
#to the user.


correct_password = "python"

while True:
    user_password = input("Enter the password: ")

    if user_password == correct_password:
        print("Correct password.")
        break
    else:
        print("Incorrect password.")
