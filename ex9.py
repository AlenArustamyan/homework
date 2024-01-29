#Write a function that finds the key with the maximum value in a dictionary


def find_key_with_max_value(dictionary):
    if not dictionary:
        print("Error")
        return None

    max_key = max(dictionary, key=dictionary.get)
    return max_key

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

max_key = find_key_with_max_value(scores)

if max_key is not None:
    print(max_key)
