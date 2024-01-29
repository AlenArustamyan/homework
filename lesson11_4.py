#Write a python function, which add a new value
#with given key in dict.

def add_to_dict(input_dict, key, value):
    input_dict[key] = value
    return input_dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4

result_dict = add_to_dict(my_dict, new_key, new_value)
print(my_dict)
print(result_dict)
