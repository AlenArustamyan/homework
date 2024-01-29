#count all letters, digits, and special symbols from a given string



word = input("enter word ")
alphabets = 0
special_symbols = 0
digits = 0
for x in word:
    if x.isalpha():
        alphabets +=1
    elif x.isalpha():
        digits +=1
    else:
        special_symbols +=1
print("alphabets ", alphabets,"digits ",digits,"special_symbols ",special_symbols)
