#Write a python function which create dict from 2
#lists with the same length

def create_dict_from_lists(keys, values):
    if len(keys) != len(values):
        print("Error:")
        return None

    result_dict = dict(zip(keys, values))
    return result_dict
keys_list = ["name", "age", "city"]
values_list = ["Alen", 18, "Yerevan"]

result_dict = create_dict_from_lists(keys_list, values_list)

if result_dict:
    print("Resulting dictionary:", result_dict)
