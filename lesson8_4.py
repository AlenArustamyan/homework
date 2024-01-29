#Write a Python function that takes two sets as input and returns a new set containing
#elements that are present in either of the input sets, but not in both.


def find_exclusive_elements(set1, set2):
    exclusive_elements = set1.symmetric_difference(set2)
    return exclusive_elements
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

result_set = find_exclusive_elements(set_a, set_b)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Exclusive Elements: {result_set}")
