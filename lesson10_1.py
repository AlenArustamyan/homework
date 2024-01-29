#Write a Python program that asks the user to enter a password. Keep asking for the
#password until the correct password "secret" is entered. Provide appropriate feedback
#to the user




word = input("enter password ")
num = 3
while word != "python":
    if num ==0:
        print(" many wrong attempts")
    else:
        print(f"wrong password you have {num} chances")
        word = input("enter password ")
        num = num -1
        print("Correct")

