#Given a string, create a dictionary where keys are characters, and values are
#their ASCII values.

def create_ascii_dict(input_string):


    char_ascii_dict = {}

    for char in input_string:
        char_ascii_dict[char] = ord(char)

    return char_ascii_dict

# Example usage:
input_str = "hello"

result_dict = create_ascii_dict(input_str)
print(result_dict)
