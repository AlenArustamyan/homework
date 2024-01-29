#Write a python program which concat 2 dicts.
def concat_dicts(dict1, dict2):
    return {**dict1, **dict2}
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

result_dict = concat_dicts(dict_a, dict_b)
print(result_dict)
