#Write a Python function that takes two sets as input and returns a new set containing
#elements that are present in both input sets

def find_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    return common_elements

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

result_set = find_common_elements(set_a, set_b)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Common Elements: {result_set}")
