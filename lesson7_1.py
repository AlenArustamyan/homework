#Arrange string characters such that lowercase letters should come first

def arrangecharacters(input_str):
    lowerchars = ''.join(ch for ch in input_str if ch.islower())
    upperchars = ''.join(ch for ch in input_str if ch.isupper())

    result_str = lowerchars + upperchars
    return result_str

my_input = input(" enter string")
arrangecharacters = arrangecharacters(my_input)
print("arranged string")